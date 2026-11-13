# Validation: ChatGPT beta 0.1.0-beta.2

## Current revision: 0.1.0-beta.2

The Premium and private-preview revision was rebuilt on November 13, 2026. All 12 release regression tests and the skill creator validator passed again. Account capability and format preferences now route to short posts, long posts, or threads; explicitly requested private illustrations may keep one notice outside the sample copy. The editorial pass preserves requested narrative depth.

The author reviewed 15 longer preview posts and requested publication with that style retained. The release includes a long-post example and a four-part thread as explicitly identified teaching material. These previews are not verified client cases.

A fresh independent Codex evaluator ran five requests against the final beta.2 guide. The authoring assistant reviewed the actual responses; all five met the tested format and factual-status criteria. The evaluator received the guide and raw cases, without expected answers or authoring history, and used no network. The five cases shared one evaluation session with separate profiles; this is not a multi-model or repeated-run study.

| Case | Observed result | Assessment |
|---|---|---|
| Premium long post | Produced a complete long post, respected copy-only output, and kept the untested change untested | Pass |
| Premium thread | Produced four substantive posts covering failure, diagnosis, repair, and remaining verification | Pass |
| Standard-account thread | Produced four numbered posts within the requested short-post limit and retained unfinished cancellation | Pass |
| Private preview | Used fully filled illustrative details with one note outside the copy; did not claim verified client work | Pass |
| Intended publication without evidence | Withheld the doubled-accuracy assertion and produced a detailed proposed evaluation | Pass |

Raw requests: [release behavior cases](tests/fixtures/release-behavior-cases.json). Actual responses and the exact guide SHA-256: [beta.2 behavior run](tests/results/2026-11-13-beta2-behavior.json).

The signed-in ChatGPT upload/project test remains unperformed; these are Codex behavioral tests and local release checks. The historical eight-case results below belong to beta.1, whose exact guide hash is recorded separately. Neither run establishes commercial effectiveness.

## Historical validation: 0.1.0-beta.1

Checked November 13, 2026. The package passed 12 automated release checks, the skill metadata validator, and a reviewed eight-case independent behavioral run in Codex. It is ready for a user pilot. A signed-in ChatGPT upload/project test is still pending. Nothing was published to GitHub or X.

## What was actually executed

| Layer | Result | What it establishes |
|---|---|---|
| Python release regression tests | 12 passed | Packaging behavior, included files, licenses, links, and guide integrity |
| Skill creator validator | Passed | Canonical skill metadata and basic structure |
| Independent behavioral run | 8 of 8 cases passed author review | Observed responses followed the tested instructions and supplied evidence |
| ChatGPT product upload/project test | Not run | The available browser showed a logged-out ChatGPT page |
| Audience and commercial outcomes | Not tested | No claim of increased reach, clients, or offers |

The independent evaluator received the built guide and raw requests in a fresh context. It did not receive expected answers, suspected failures, source test assertions, or authoring history. It used no network or external actions. All eight requests ran in one evaluation session with separate case profiles; this was not eight independent model samples. The authoring assistant reviewed the actual responses, including claims, voice, scope, length, and outcome attribution.

Inputs: [behavior cases](tests/fixtures/behavior-cases.json). Actual responses and guide SHA-256: [behavior run](tests/results/2026-11-13-codex-behavior.json). These practice briefs must not be represented as verified client achievements.

## Behavioral results

| Case | Observed result | Assessment |
|---|---|---|
| Nidrosoft workflow brief | Selected A02 and CLIENTS; described the supplied integration without numerical gains; labeled the recording as optional and still to create | Pass |
| Quiet editing | Removed promotional filler; retained agent harness, 40 tasks, 7 and 3 failures, the same-task rerun, and uncertainty; returned copy only | Pass |
| Missing benchmark | Withheld the twice-as-good assertion and wrote an explicitly proposed experiment; stated that neither model had been tested | Pass |
| Early-career designer | Selected A06 and OFFERS; kept the checklist inline; borrowed no Nidrosoft identity, seniority, clients, or download | Pass |
| Detection only | Flagged particular phrases and patterns without rewriting the paragraph or guessing AI authorship | Pass |
| AI architecture observation | Selected A08; retained the three-session boundary, concrete failures, interpretation, and untested solution | Pass |
| Outcome scoring | Recorded one client opportunity progressing from stage 1 to 3 and one personal opportunity at stage 2; kept exact-post and profile attribution separate | Pass |
| Dry personal voice | Preserved the demo/laptop anecdote, future-tense server plan, missing performance numbers, and closing joke without adding a sales ask | Pass |

The four short drafted posts were 208, 254, 180, and 238 ordinary characters and contained only ASCII text with no URLs. The two constrained edits were 36 and 42 whitespace-delimited words, below their 90-word limits. These are local counts, not verification by X's composer.

### Actual quiet-edit output

Input included "Here's the thing," "game changer," and a generic closing line. The response was:

> Our agent harness failed 7 of 40 internal tasks. After we added a progress file, 3 failed on a second run of the same 40 tasks.
>
> We think the handoff helped, but this was one rerun.

This keeps the technical term and measured observations without turning one rerun into a causal claim.

### Actual voice-preservation output

> My demo survived a room full of executives. It did not survive my laptop going to sleep.
>
> I had kept the import job in the browser. Next version, it goes on the server.
>
> No performance numbers yet. Just one very educational nap.

The evaluator kept this already effective draft substantially intact.

## Automated release checks

Run from the repository root:

```sh
python3 scripts/package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The 12 tests cover:

1. Identical guide and ZIP bytes across unchanged builds.
2. Exact manifest membership, ZIP integrity, and exclusion of unlisted private and hidden sentinel files.
3. Both full MIT notices traveling with the standalone guide and archive.
4. A missing declared source failing without replacing the prior release.
5. Rejection of traversal, absolute, and platform-specific manifest paths.
6. Rejection of a manifest that omits required license or guide entries.
7. Rejection of a source file symlink.
8. Rejection of a source directory symlink.
9. Rejection of an output symlink without changing its target.
10. Preservation of example headings and links inside fenced code.
11. All 15 unique angle cards retained in the combined guide.
12. All Markdown links within the distributed documents resolving.

The archive contains 13 files under one `work-to-post-chatgpt` folder. The builder uses an explicit manifest and includes no completed pilot profile or prospect log. Old skill/Claude-oriented archives were moved out of the active distribution folder.

The canonical `work-to-post` folder also passed the skill creator's `quick_validate.py`. Its PyYAML dependency was used in an isolated temporary environment; no runtime dependency was added to the ChatGPT kit.

## Provenance and release contents

- Original framework: MIT, copyright 2026 **Cyriac Zeh**.
- Editorial adaptation: Peter Yang's No AI Slop, MIT, pinned to revision `000650b156983f5159695b441477f4e63b25dc85`.
- The retained upstream `SKILL.md`, `eval.md`, and `LICENSE` were compared with the retrieved files and matched exactly.
- The complete guide includes the editing pass and both license notices. A separate No AI Slop installation is unnecessary.
- The original installed Nidrosoft playbook was not replaced. This release is the separate ChatGPT document kit.

## Remaining pilot

Upload the built guide and your own profile in a signed-in ChatGPT conversation or project, then run [TRY-IT.md](TRY-IT.md) and a real use case. Confirm that the upload is accessible and that the response respects the supplied evidence and voice. We could not execute that product-specific check from the logged-out browser.

These tests cover selected important behaviors, not every angle, ChatGPT model, or future request. The 15 angle cards were checked structurally; all 15 have not been independently exercised in the ChatGPT product. Judge commercial effectiveness later using real posts and the separate CLIENTS/OFFERS log.
