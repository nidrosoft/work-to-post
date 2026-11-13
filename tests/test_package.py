"""Release regression checks. These do not measure model or audience behavior."""

import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package", ROOT / "scripts/package.py")
package = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="work-to-post-package-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "kit"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            "dist", "__pycache__", "local", "pilots", ".git"))
        self.manifest = json.loads((self.root / "release-manifest.json").read_text())

    def save_manifest(self):
        (self.root / "release-manifest.json").write_text(
            json.dumps(self.manifest), encoding="utf-8")

    def build(self):
        return package.build(self.root)

    def test_reproducible_build(self):
        guide, archive = self.build()
        before = (guide.read_bytes(), archive.read_bytes())
        self.build()
        self.assertEqual(before, (guide.read_bytes(), archive.read_bytes()))

    def test_only_explicit_files_are_distributed(self):
        for name in (".env", "private-prospect-notes.md",
                     "work-to-post/.hidden-note", "work-to-post/assets/local-client.txt"):
            (self.root / name).write_text("LOCAL_SENTINEL_NOT_FOR_RELEASE", encoding="utf-8")
        _, archive = self.build()
        prefix = self.manifest["archive_root"] + "/"
        with zipfile.ZipFile(archive) as zipped:
            self.assertIsNone(zipped.testzip())
            self.assertEqual(set(zipped.namelist()),
                             {prefix + name for name in self.manifest["files"]})
            for name in zipped.namelist():
                self.assertNotIn(b"LOCAL_SENTINEL_NOT_FOR_RELEASE", zipped.read(name))
                self.assertNotIn("..", PurePosixPath(name).parts)

    def test_full_license_notices_travel_with_guide_and_zip(self):
        guide, archive = self.build()
        original = (self.root / "LICENSE").read_bytes().strip()
        upstream = (self.root / "third_party/no-ai-slop/LICENSE").read_bytes().strip()
        self.assertIn(b"Copyright (c) 2026 Cyriac Zeh", original)
        self.assertIn(b"Copyright (c) 2026 Peter Yang", upstream)
        for notice in (original, upstream):
            self.assertIn(notice, guide.read_bytes())
        prefix = self.manifest["archive_root"] + "/"
        with zipfile.ZipFile(archive) as zipped:
            self.assertEqual(original, zipped.read(prefix + "LICENSE").strip())
            self.assertEqual(upstream, zipped.read(
                prefix + "third_party/no-ai-slop/LICENSE").strip())
            self.assertIn(upstream, zipped.read(prefix + "THIRD_PARTY_NOTICES.md"))
            self.assertEqual(guide.read_bytes(), zipped.read(prefix + "WORK-TO-POST.md"))

    def test_missing_declared_source_does_not_replace_release(self):
        guide, archive = self.build()
        before = (guide.read_bytes(), archive.read_bytes())
        (self.root / "TRY-IT.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing release file"):
            self.build()
        self.assertEqual(before, (guide.read_bytes(), archive.read_bytes()))

    def test_manifest_rejects_unsafe_paths(self):
        original = json.dumps(self.manifest)
        mutations = [
            ("files", "../outside.txt", "VERSION"),
            ("files", "extra.txt", "../outside.txt"),
            ("files", "/absolute.txt", "VERSION"),
            ("files", "extra.txt", "directory\\outside.txt"),
            ("archive_file", None, "../outside.zip"),
            ("archive_root", None, "nested/root"),
        ]
        for field, key, value in mutations:
            with self.subTest(field=field, key=key, value=value):
                self.manifest = json.loads(original)
                if key is None:
                    self.manifest[field] = value
                else:
                    self.manifest[field][key] = value
                self.save_manifest()
                with self.assertRaises(ValueError):
                    self.build()

    def test_license_entries_cannot_be_silently_omitted(self):
        original = json.dumps(self.manifest)
        for name in package.REQUIRED:
            with self.subTest(name=name):
                self.manifest = json.loads(original)
                del self.manifest["files"][name]
                self.save_manifest()
                with self.assertRaisesRegex(ValueError, "both license notices"):
                    self.build()

    def test_symlink_source_file_is_rejected(self):
        source = self.root / "TRY-IT.md"
        source.unlink()
        source.symlink_to(self.root / "README.md")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.build()

    def test_symlink_source_directory_is_rejected(self):
        (self.root / "linked").symlink_to(self.root / "work-to-post", target_is_directory=True)
        self.manifest["files"]["extra.md"] = "linked/assets/profile.md"
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.build()

    def test_symlink_output_is_rejected_without_changing_target(self):
        unrelated = self.root / "keep.txt"
        unrelated.write_text("keep this")
        output = self.root / "WORK-TO-POST.md"
        output.unlink(missing_ok=True)
        output.symlink_to(unrelated)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.build()
        self.assertEqual("keep this", unrelated.read_text())

    def test_fenced_examples_are_preserved(self):
        fence = chr(96) * 3
        example = f"{fence}md\n# A sample heading\n[example](not-a-real-module.md)\n{fence}\n"
        profile = self.root / "work-to-post/assets/profile.md"
        profile.write_text(profile.read_text() + "\n" + example)
        guide, _ = self.build()
        self.assertIn(example, guide.read_text())

    def test_guide_keeps_all_fifteen_angles(self):
        guide, _ = self.build()
        ids = re.findall(r"^### (A\d{2}) ", guide.read_text(), re.M)
        self.assertEqual([f"A{number:02}" for number in range(1, 16)], ids)

    def test_all_distributed_markdown_links_resolve(self):
        _, archive = self.build()
        with zipfile.ZipFile(archive) as zipped:
            names = set(zipped.namelist())
            texts = {name: zipped.read(name).decode("utf-8")
                     for name in names if name.endswith(".md")}
        for name, text in texts.items():
            prose = []
            package.transform_prose(text, lambda line: prose.append(line) or line)
            for _, target in package.LINK.findall("".join(prose)):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                relative, _, fragment = target.partition("#")
                destination = ((PurePosixPath(name).parent / relative).as_posix()
                               if relative else name)
                with self.subTest(file=name, link=target):
                    self.assertIn(destination, names)
                    if fragment:
                        document = texts[destination]
                        headings = re.findall(r"^#{1,6} (.+)$", document, re.M)
                        self.assertIn(fragment, {package.slug(h) for h in headings})


if __name__ == "__main__":
    unittest.main()
