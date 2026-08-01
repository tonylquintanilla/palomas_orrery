# As-Built: L-156 Phase 2 Piece 1 -- Cross-Checked Annotation Scanner

**Built on `523ea0247f6908f1c29d35468908e324542206bd`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Pushed at `<SHA after push>`.**

**Built by:** Claude Opus 5
**From:** `documentation/BUILD_PROMPT_phase2_piece1.md` and
`documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md`
**Date:** August 1, 2026

---

## 1. Base reconciliation

The build prompt and predesign R2 both anchor to `d03f586`. Live HEAD at
session start was `523ea02`, one commit ahead. The gap is documentation,
`MODULE_ATLAS.md`, `MODULE_INDEX.md`, and a two-line `module_atlas.py`
change; `provenance_scanner.py` is byte-identical across the two commits.
The build was done on `523ea02` and HEAD was re-confirmed unchanged at
the end of the session.

---

## 2. Delivered

| Artifact | Kind | Bytes |
|----------|------|------:|
| `patch_phase2_piece1.py` | transactional patch, 9 anchored edits | 18,776 |
| `test_cross_checked.py` | new test module, 16 tests | 20,211 |

The patch takes `provenance_scanner.py` from 119,586 to 130,996 bytes.

### What the patch changes

1. `parse_cross_checks(text)` and its three regexes, placed immediately
   after `has_citation()`.
2. `distinct_checker_identities(records)` -- first-seen order, compared
   case-folded and whitespace-normalized.
3. `CROSS_CHECK_ISSUES` module-level collector, beside `SHADOWED_STRINGS`
   and `DEEP_CITATIONS`.
4. `_record_cross_check_diagnostics()`, above `score_unit()`.
5. Two new branches at the head of `score_unit()`'s vulnerability ladder.
6. `V_CROSS_CHECKED` constant comment replaced with the decided wording;
   "NOTHING SETS THIS YET" removed.
7. Collector cleared in `scan_project()`; console notice added.
8. `cross_check_issues` kwarg threaded into `generate_report()`.
9. New `## CROSS-CHECK ANNOTATION ISSUES` subsection in the audit.

---

## 3. Acceptance evidence

Run from a clean checkout of `523ea02` with the patch applied.

| Criterion | Result |
|-----------|--------|
| 16 tests pass | 16/16 |
| Baseline identity set reproduced | 879 -> 879; 0 added, 0 removed, 0 changed |
| Reason-string distribution | identical |
| Files scanned | 116 -> 117 (the new test file) |
| Tier counts | 210 / 605 / 62 / 2, unchanged |
| `py_compile` both files | clean |
| No annotation exists in any source file | confirmed, all files swept |
| Voyager false positive | no match, tested against the live file |
| ASCII only | max byte 125 in both deliverables |
| LF only | zero CR bytes in both deliverables |

Identity key used for the diff:
`(file, kind, name, sha1(content)[:16])`.

Regression suites, all at HEAD with the patch applied:
`test_provenance_1d.py` 27/27, `test_citation_inheritance.py` 20/20,
`test_constants_provenance.py` 73/73.

`test_reset_completeness.py` could not run in the build sandbox
(`tkinter` not installed). It does not import the scanner and is
unaffected by this change; it needs a Tony-side run to confirm.

---

## 4. Deviations from the written spec

Each was flagged rather than applied silently.

### 4a. Prose dates were accepted; now rejected [defect found and closed]

The ISO-only rule cannot be enforced by a year test alone, because a
prose date contains a year. The first implementation parsed
`# Cross-checked: Gemini April 2026 (worksheet.md)` into identity
"Gemini April" and date "2026".

That is not a cosmetic mis-parse. One checker writing two annotations in
different months would produce two different identity strings and earn
V2 alone -- the exact hole the two-distinct-checkers rule exists to
close. Added `CROSS_CHECK_PROSE_MONTH_RE` and a `prose_date` error code.
This implements the decided constraint; it does not change it.

### 4b. Regex character class tightened

Spec: `r'(?mi)^\s*#\s*cross-checked\s*:'`. Delivered: `[ \t]` in place
of `\s`. Under `MULTILINE`, `\s` matches a newline, so a bare `#` line
followed by `cross-checked:` on the next line would match across the
break. Tightening only -- no valid annotation is rejected.

### 4c. Records are plain tuples

R2 section 2c writes `r.identity`; the build prompt's scoring snippet
writes `r[0]`. Delivered as plain `(identity, date, reference)` tuples,
matching the build prompt's literal code. `distinct_checker_identities()`
carries the readability that attribute access would have provided.

### 4d. `has_cross_check()` not built

R2 offered it conditionally ("if needed"). Scoring uses the structured
output, so it would have been an unused API surface.

### 4e. Test 15 implemented as a corpus sweep

Rather than a checked-in baseline artifact, the test walks every
non-test `.py` in the project directory and asserts zero records AND
zero issues. Zero records proves nothing was annotated early; zero
issues proves no existing prose is misread. This is stricter than a
scan diff -- it reaches files the role gate excludes from findings
entirely -- and runs in about a second. The full identity diff was run
in-session instead, and its result is in section 3.

### 4f. Diagnostics deduplicated; column renamed

Every unit whose context window reaches an annotation reports that
annotation's problems, so one malformed line initially produced one
table row per nearby claim. Entries are now deduplicated by
`(file, code, detail)`, and the column reads `Near line` with a note
that the annotation sits in the lookback above that line, not on it.

---

## 5. Finding: lookback bleed is real, and tight placement does not fix it

Measured, not inferred. An annotation promotes every *separately
sourced* claim within roughly 50 lines below it to V2. Beyond the window
it stops cleanly, which confirms the flat 60-line context block is the
mechanism rather than anything in the parser.

R2 section 2g test 14 names tight placement inside the existing
`# Source:` run as the mitigation. It is not sufficient. In the test
fixture the annotation is already directly beneath its own `# Source:`
line, three lines above the next claim, and the next claim still takes
V2.

Exposure per annotation across the Track 1 targets -- the worst-case
count of other findings within 50 lines below any one finding:

| File | Units | Max downstream |
|------|------:|---------------:|
| `info_dictionary.py` | 124 | 11 |
| `comet_visualization_shells.py` | 23 | 6 |
| `asteroid_belt_visualization_shells.py` | 14 | 5 |
| `jupiter_visualization_shells.py` | 19 | 3 |
| `mercury_visualization_shells.py` | 7 | 3 |
| `star_notes.py` | 34 | 3 |
| `earth_visualization_shells.py` | 27 | 2 |
| `eris_visualization_shells.py` | 5 | 1 |
| `mars_visualization_shells.py` | 4 | 0 |

A live rehearsal confirms the shape: inserting two annotations at the
first `# Source:` run in `earth_visualization_shells.py` moved exactly
one unit, the intended one. `info_dictionary.py` is where a single
annotation could silently promote up to eleven unchecked claims.

No fix was attempted. Constraint 4 forbids new positional logic, and the
remedy is a design decision, not an implementation detail. Test 14 pins
the behavior in both directions -- bleed near, no bleed far -- so a
future change to the window fails a test instead of passing quietly.

**Tony-action (decide):** whether Piece 2 needs a per-claim containment
rule before annotations go into `info_dictionary.py`, `comet_`, or
`asteroid_belt_`. The other Track 1 files are low enough exposure to
proceed as specified.

---

## 6. Skill version drift

Three numbers for `provenance-discipline`: the resident Skill Manifest
says 1.2, the installed skill says 1.3, the repo's `SKILL.md` says 1.4.
Repo wins under Context Priority; the build used 1.4.

**Tony-action (do):** run `skills_index.py` to regenerate the manifest
table, and reinstall the skill from the repo copy.

---

## 7. Tony-action rollup

- **(do)** Save `patch_phase2_piece1.py` into the repo root beside
  `provenance_scanner.py`, open in VS Code, click Run. Expect nine `ok`
  lines then `patch applied (130996 bytes, was 119586)`.
- **(do)** Save `test_cross_checked.py` into the repo root. Run it the
  same way; expect 16 passed, 0 failed.
- **(do)** Re-run `provenance_scanner.py` and confirm 879 findings,
  210 / 605 / 62 / 2, and no cross-check-issue line on the console.
- **(do)** Move `patch_phase2_piece1.py` into `documentation/` after it
  runs, matching `patch_1b_vulnerability_ladder.py` and
  `patch_retire_option_a.py`. The scanner walks the repo root only, so
  leaving it there adds a scanned file (118 rather than 117) while
  contributing zero findings.
- **(do)** Run `test_reset_completeness.py` on Windows -- it needs
  `tkinter`, which the build sandbox lacked.
- **(do)** Regenerate the Skill Manifest and reinstall
  `provenance-discipline` at 1.4 (section 6).
- **(decide)** Whether the lookback bleed needs a containment rule
  before Piece 2 Track 1 touches the high-exposure files (section 5).
- **(decide)** Whether the blind-check wording question raised earlier
  is fully settled by the new constant comment. The rung's definition
  now reads "independently verified via competitive pattern" rather
  than "blind," which resolves the conflict in the code; the worksheets
  still show current values to both checkers, which is the workflow R2
  describes.

---

## 8. Ref

- `provenance_scanner.py` at `523ea02` (pre-patch base)
- `documentation/BUILD_PROMPT_phase2_piece1.md`
- `documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md`
- `skills/provenance-discipline/SKILL.md` v1.4
- `LEDGER_CONSOLIDATED.md` L-156, L-157, L-161
- `planet_visualization_utilities.py` line 492 (false-positive anchor)
- `test_provenance_1d.py`, `test_citation_inheritance.py`,
  `test_constants_provenance.py` (regression suites)

---

*As-built prepared August 1, 2026 by Claude Opus 5.*
