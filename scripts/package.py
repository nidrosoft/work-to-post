#!/usr/bin/env python3
"""Build the self-contained ChatGPT guide and an explicitly listed release ZIP."""

import json
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
MODULES = (
    "work-to-post/SKILL.md",
    "work-to-post/assets/profile.md",
    "work-to-post/assets/post-brief.md",
    "work-to-post/references/angles.md",
    "work-to-post/references/editorial.md",
    "work-to-post/references/rhythm.md",
    "work-to-post/references/review.md",
    "work-to-post/assets/review-log.md",
    "work-to-post/references/examples.md",
    "work-to-post/references/research.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
)
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
REQUIRED = {
    "WORK-TO-POST.md": "WORK-TO-POST.md",
    "LICENSE": "LICENSE",
    "THIRD_PARTY_NOTICES.md": "THIRD_PARTY_NOTICES.md",
    "third_party/no-ai-slop/LICENSE": "third_party/no-ai-slop/LICENSE",
}


def relative_path(value):
    """Reject ambiguous paths, traversal, and absolute/platform-specific paths."""
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError(f"Invalid relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ("", ".", "..") for p in value.split("/")):
        raise ValueError(f"Invalid relative path: {value!r}")
    return path


def local_path(root, value, must_exist=True):
    relative = relative_path(value)
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink not allowed in release path: {value}")
    if must_exist and not path.is_file():
        raise ValueError(f"Missing release file: {value}")
    return path


def body_of(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        match = re.match(r"\A---\n.*?\n---\n", text, re.S)
        if not match:
            raise ValueError(f"Unclosed frontmatter: {path.name}")
        text = text[match.end():].lstrip()
    return text


def slug(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


def transform_prose(text, transform):
    """Do not rewrite headings or example links inside fenced code blocks."""
    result = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^[ \t]{0,3}(\x60{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence:
            result.append(line)
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= fence[1] and not marker[2].strip()):
                fence = None
        elif marker:
            fence = (marker[1][0], len(marker[1]))
            result.append(line)
        else:
            result.append(transform(line))
    if fence:
        raise ValueError("Unclosed Markdown code fence")
    return "".join(result)


def guide_text(root):
    bodies = {}
    titles = {}
    for relative in MODULES:
        path = local_path(root, relative)
        body = body_of(path)
        if relative == "LICENSE":
            body = "# Framework MIT license\n\n" + body
        match = re.search(r"^# (.+)$", body, re.M)
        if not match:
            raise ValueError(f"Missing document title: {relative}")
        bodies[path] = body
        titles[path] = match[1]
    if len(set(slug(t) for t in titles.values())) != len(titles):
        raise ValueError("Duplicate section titles in guide")

    sections = []
    for path, body in bodies.items():
        def rewrite_link(match):
            label, target = match.groups()
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                return match[0]
            relative, _, fragment = target.partition("#")
            target_path = (path.parent / relative).resolve()
            if target_path not in titles:
                raise ValueError(f"Guide cannot resolve {target!r} from {path.name}")
            anchor = fragment or slug(titles[target_path])
            return f"[{label}](#{anchor})"

        def rewrite_line(line):
            line = LINK.sub(rewrite_link, line)
            return re.sub(r"^(#{1,5}) ", r"\1# ", line)

        sections.append(transform_prose(body, rewrite_line).strip())

    version = local_path(root, "VERSION").read_text(encoding="utf-8").strip()
    intro = f"""# Work to Post for ChatGPT

Created by **Cyriac Zeh / Nidrosoft**. Version **{version}**. MIT licensed. The embedded editorial pass adapts No AI Slop by Peter Yang; both complete license notices appear at the end of this guide.

Upload this file to a ChatGPT conversation or project and supply your own profile and source material. It contains the complete instructions, all 15 angle templates, forms, editorial pass, posting rhythm, review method, and examples. No additional skill, API key, or paid research tool is needed for drafting.

Read the core instructions, then the sections relevant to the request. Internal links point to sections of this file. Examples are teaching material and never facts about a new user. Use the current user's profile and explicit corrections.

Starter request:

> Read Work to Post and use Draft mode. Use my profile and the notes below. Choose the strongest supported angle for my intended reader. Give me one post, its supporting material, and any facts or assets still needed. Do not invent results.

"""
    contents = "\n".join(f"- [{title}](#{slug(title)})" for title in titles.values())
    return intro + contents + "\n\n" + "\n\n".join(sections) + "\n"


def read_manifest(root):
    manifest_path = local_path(root, "release-manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    prefix = relative_path(manifest["archive_root"])
    filename = relative_path(manifest["archive_file"])
    if len(prefix.parts) != 1 or len(filename.parts) != 1 or filename.suffix != ".zip":
        raise ValueError("Archive name and root must each be a single component")
    files = manifest["files"]
    if not isinstance(files, dict) or not files:
        raise ValueError("Manifest must list files")
    for destination, source in files.items():
        relative_path(destination)
        relative_path(source)
    if len({name.casefold() for name in files}) != len(files):
        raise ValueError("Archive names must be unique, including case")
    if any(files.get(name) != source for name, source in REQUIRED.items()):
        raise ValueError("Manifest must preserve the guide and both license notices")
    return manifest


def atomic_write(path, content):
    local_path(path.parent, path.name, must_exist=False)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        try:
            handle.write(content)
            handle.close()
            temporary.replace(path)
            path.chmod(0o644)
        finally:
            temporary.unlink(missing_ok=True)


def build(root=ROOT):
    root = Path(root).resolve()
    manifest = read_manifest(root)
    guide = guide_text(root).encode("utf-8")
    # Validate every declared source before changing a release artifact.
    members = {}
    for destination, source in manifest["files"].items():
        path = local_path(root, source, must_exist=source != "WORK-TO-POST.md")
        members[destination] = guide if source == "WORK-TO-POST.md" else path.read_bytes()

    dist = local_path(root, "dist", must_exist=False)
    dist.mkdir(exist_ok=True)
    target = local_path(dist, manifest["archive_file"], must_exist=False)
    with tempfile.NamedTemporaryFile(dir=dist, suffix=".zip", delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for destination in sorted(members):
                info = zipfile.ZipInfo(f'{manifest["archive_root"]}/{destination}',
                                       date_time=(2026, 11, 13, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, members[destination])
        with zipfile.ZipFile(temporary) as archive:
            bad = archive.testzip()
            if bad:
                raise ValueError(f"Corrupt ZIP member: {bad}")
        atomic_write(local_path(root, "WORK-TO-POST.md", must_exist=False), guide)
        temporary.replace(target)
        target.chmod(0o644)
    finally:
        temporary.unlink(missing_ok=True)
    return root / "WORK-TO-POST.md", target


def main():
    for path in build():
        print(f"{path.name}: {path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
