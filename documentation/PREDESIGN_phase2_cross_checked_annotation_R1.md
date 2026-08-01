# Predesign R1: L-156 Phase 2 — D4 Cross-Checked Annotation + Backfill

**Built on `d03f586196bc07e8c4cb6f8435e16ac85de194b9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared by:** Claude Opus 4.6 (orchestration)
**Reviewed by:** GPT, Claude Opus 5 (×2), Claude Fable 5 (competitive)
**For:** Claude Opus 5 (builder)
**Date:** August 1, 2026

---

## 0. State of play

Scanner baseline confirmed by fresh scan against HEAD:

| Tier | Count | Label |
|------|------:|-------|
| 1    |   210 | FIX NOW |
| 2    |   605 | REVIEW |
| 3    |    62 | LOW PRIORITY |
| 4    |     2 | LOWEST PRIORITY |
| **Total** | **879** | across 116 files |

The checked-in `PROVENANCE_AUDIT.md` at this SHA shows older tier
counts (171/644/62/2) from the pre-D8.5 scoring model. The 210/605/62/2
baseline above comes from running the current scanner at HEAD.

Two carry-over items from Phase 1 are already resolved at HEAD.

---

## 1. What Phase 2 builds

Two pieces, sequenced.

**Piece 1 (scanner mechanism):** teach `provenance_scanner.py` to
recognize `# Cross-checked:` annotations and score them V_CROSS_CHECKED
(V2). One new recognition function, a change to `score_unit()`, and
tests.

**Piece 2 (backfill):** write `# Cross-checked:` annotations onto claims
verified via the competitive pattern. Two tracks:

- **Track 1:** complete the competitive pattern for files that already
  have Gemini worksheets. Claude independently verifies the same claims
  (this session). Tony compares. Convergent claims get annotated.
  Divergences get discussed; unresolved ones go to GPT as tiebreaker.

- **Track 2 (separate sessions):** new worksheets for uncovered files,
  starting with `celestial_objects.py`. Both models get the same
  worksheet independently.

**Build order:** Piece 1 first. Track 1 annotation insertion second
(after Tony confirms convergence). Track 2 is separate sessions.

---

## 2. Piece 1: Scanner mechanism — detailed spec

### 2a. The annotation form (decided)

```python
# Source: NASA Planetary Fact Sheet
# Cross-checked: Gemini 2026-04-15 (worksheet_earth_visualization.md)
# Cross-checked: Claude 2026-08-10 (worksheet_earth_visualization.md)
```

Each cross-check gets its own line naming the model and the worksheet.
The competitive pattern produces two lines — one per model. The scanner
requires BOTH a `# Source:` citation AND two valid `# Cross-checked:`
lines with distinct checker identities to score V2.

**Anti-gaming rule (decided, design review confirmed):** the parenthetical
worksheet reference is REQUIRED. An annotation without a reference does
not contribute to V2.

### 2b. Recognition logic

A new function, `has_cross_check(text)`, separate from `has_citation()`.

Returns a list of `(checker_identity, date, reference)` tuples — one
per valid annotation line found in the text. The caller uses this to
check for two distinct checker identities.

**The regex** matches lines of the form:

```
# Cross-checked: <who> <date> (<ref>)
```

Anchored to comment-line start with required colon after "Cross-checked".
This is critical — `planet_visualization_utilities.py` line 492 already
contains "Giants cross-checked to Voyager 2 (Uranus: Desch..." in a
live comment. Without the colon anchor, that line would be a false
positive today.

Specific anchoring rules:
- Must start with `#` followed by optional whitespace
- "Cross-checked" must be followed immediately by `:`
- Case-insensitive
- `(<ref>)` must be a non-empty parenthetical — but `(x)` or `(done)`
  should not qualify. Require the reference to end in `.md` (all
  worksheet files are markdown)

**Date handling:** require at least a four-digit year (YYYY) to be
present somewhere in the line between the colon and the parenthetical.
Don't attempt calendar validation — just confirm a year exists. This
rejects lines with no date while accepting `2026-04-15`, `2026-04`,
and prose like `April 2026`.

**Checker identity:** everything between the colon and the date. Two
annotations are "distinct" if their checker identities differ after
case-folding and whitespace normalization.

**Placement:** immediately after `has_citation()` in the source, same
module section. Uses the same lookback-window text that `has_citation()`
receives — no new extraction logic.

### 2c. Scoring change in `score_unit()`

**V2 requires BOTH citation AND competitive cross-check.** This is the
central design decision from the competitive review, resolving three
concerns raised independently by GPT, Fable, and Opus 5:

- Without `cited` as a prerequisite, an uncited claim with a valid
  annotation jumps V4→V2 directly — stronger than cite-to-clear.
- Without requiring two distinct checkers, a single annotation earns a
  rung defined by a two-model process.
- A cross-check is verification of a sourced claim, not a substitute
  for sourcing.

New flow:

```python
cited = has_citation(text, is_docstring=is_doc)
cross_checks = has_cross_check(text)
distinct_checkers = len(set(c.identity for c in cross_checks)) >= 2

if cited and distinct_checkers:
    V_CROSS_CHECKED
    reason: "Cross-checked by <N> models (<identities>)"
elif cited and cross_checks:
    V_SOURCED
    reason: "Cited; cross-check incomplete (<N>/2 models)"
elif cited:
    V_SOURCED  (existing reasons unchanged)
elif inherited:
    V_SOURCED  (existing reason unchanged)
else:
    V_RECALLED  (existing reasons unchanged)
```

**What happens to a malformed annotation.** `# Cross-checked:` is NOT
in SOURCE_PATTERNS and must NOT be added. A bare `# Cross-checked:`
without its reference does not match `has_cross_check()` (returns
nothing) and does not match `has_citation()` (no existing pattern
catches it). If the claim has a separate `# Source:` line, it stays V3.
If it has no source at all, it stays V4. This is the correct behavior:
an annotation without its reference earns nothing.

**The incomplete case.** One valid cross-check on a sourced claim
(only one model so far) stays V_SOURCED but gets a distinct reason
string noting the incomplete state. This surfaces in the audit as
a visible "one leg done" signal without granting V2.

**Stale interaction:** a cross-checked claim with a staleness marker
still scores V_CROSS_CHECKED (if fully qualified), with staleness
noted in the reason string.

### 2d. Diagnostics

Add a diagnostic (not a finding, not a score change) for these cases:
- Cross-check annotation present on an unsourced unit
- Two annotations with the same checker identity
- Annotation reference doesn't end in `.md`

These print to the audit's diagnostic section, same pattern as the
existing shadow-constant and citation-mismatch diagnostics.

### 2e. Report changes

The existing tier math works unchanged. A display string (C=4) with
V_CROSS_CHECKED (V=2) scores 8, Tier 3. That's a demotion from Tier 2
(C=4 × V=3 = 12). Intended effect.

Remove the "NOTHING SETS THIS YET" comment from the V_CROSS_CHECKED
constant definition. **Do NOT put a worked annotation example in that
comment block** — the scanner scans itself, and a complete example
there would grant the ladder constants V2 on themselves. Point to the
skill doc instead.

### 2f. Test plan

New test file: `test_cross_checked.py`.

**Keep all example strings inside function bodies, not as module-level
constants.** The scanner scans test files (test_reset_completeness.py
contributes 1 finding today). Module-level dicts or string constants
would create new self-scan findings.

Tests:

1. **Basic recognition:** two valid annotations with distinct checkers
   → `has_cross_check()` returns two records.

2. **Single checker:** one valid annotation → returns one record.
   Scoring: cited + one check → V_SOURCED with incomplete reason.

3. **Two checks, same identity:** two lines both saying "Gemini" →
   `distinct_checkers` is False → V_SOURCED.

4. **Full V2 scoring:** cited + two distinct valid annotations →
   `score_unit()` assigns V_CROSS_CHECKED.

5. **V2 requires citation:** two valid annotations but NO `# Source:`
   → V_RECALLED. Cross-check doesn't substitute for sourcing.

6. **Missing reference (anti-gaming):** `# Cross-checked: Gemini
   2026-04-15` (no parenthetical) → not a valid annotation.

7. **Empty or trivial reference:** `# Cross-checked: Gemini 2026-04-15
   ()` and `(x)` → not valid (no `.md` suffix).

8. **No false positives from normal citations:** `# Source: NASA` →
   `has_cross_check()` returns empty.

9. **The line 492 false positive:** the exact text from
   `planet_visualization_utilities.py` line 492 — "Giants cross-checked
   to Voyager 2 (Uranus: Desch..." → must NOT match. This is the
   anchoring test: no colon after "cross-checked" means no match.

10. **Case insensitivity:** `# cross-checked:` and `# CROSS-CHECKED:`
    both match.

11. **Date requirement:** annotation with no year anywhere → not valid.

12. **Staleness interaction:** cross-checked + stale marker → still
    V_CROSS_CHECKED, reason includes "date-sensitive."

13. **Population conservation (fixture):** add two annotations to a
    synthetic unit. Finding identity stays the same, only V and tier
    change.

14. **Lookback window bleed:** two adjacent findings, only one
    annotated. Assert the second does NOT receive V2.

15. **Scanner self-scan regression:** full scan with zero annotations
    in source files. Expected: 879 findings across 117 files (the new
    test file adds one file to the scan). Verify by identity diff,
    not just total count.

---

## 3. Piece 2: Backfill — corrected worksheet inventory

### 3a. Full worksheet inventory (corrected from R0)

Fifteen verification worksheets exist on disk (not seven — R0 missed
eight by only counting the `worksheet_*.md` naming pattern). The D3
calibration worksheet is a methodology document, not a data-verification
worksheet.

**Module-specific worksheets (7):**

| Worksheet | Target module |
|-----------|--------------|
| `worksheet_asteroid_belt.md` | asteroid_belt_visualization_shells.py |
| `worksheet_comet_visualization.md` | comet_visualization_shells.py |
| `worksheet_earth_visualization.md` | earth_visualization_shells.py |
| `worksheet_eris_visualization.md` | eris_visualization_shells.py |
| `worksheet_jupiter_visualization.md` | jupiter_visualization_shells.py |
| `worksheet_mars_visualization.md` | mars_visualization_shells.py |
| `worksheet_mercury_visualization.md` | mercury_visualization_shells.py |

**info_dictionary.py worksheets (4):**

| Worksheet | Coverage |
|-----------|----------|
| `info_dictionary_gemini_worksheet.md` | Main round |
| `info_dict_worksheet_2A_KBOs.md` | KBOs missed in round 1 |
| `info_dict_worksheet_2B_missions.md` | Missions missed in round 1 |
| `info_dict_worksheet_2C_comets_exoplanets.md` | Comets & exoplanets missed in round 1 |

**star_notes.py worksheets (2):**

| Worksheet | Coverage |
|-----------|----------|
| `provenance_worksheet_stars_final.md` | 10 star entries |
| `provenance_worksheet_stars_followup.md` | 5 additional stars |

**Cross-cutting worksheets (2):**

| Worksheet | Coverage |
|-----------|----------|
| `provenance_worksheet_final.md` | Oort Cloud, star_notes params, Uranus belts |
| `provenance_worksheet_tier1_final.md` | 7 remaining Tier-1 gaps across multiple files |

### 3b. Track 1 — completing the competitive pattern

These files have Gemini's leg. Claude independently verifies the same
claims in this orchestration session. Tony compares.

The coverage is claim-level, not file-level. A file can simultaneously
contain claims ready for competitive checking (sourced, covered by a
worksheet) and claims that need primary sourcing first (unsourced, or
not in any worksheet). Only claims where BOTH models converge AND a
`# Source:` citation exists get the `# Cross-checked:` annotation.

**Files with worksheet coverage:**

| Target module | Findings | Worksheets covering it |
|--------------|--------:|----------------------|
| `asteroid_belt_visualization_shells.py` | 7 | worksheet_asteroid_belt + provenance_worksheet_tier1_final |
| `comet_visualization_shells.py` | 23 | worksheet_comet + info_dict_2C (partial) |
| `earth_visualization_shells.py` | 27 | worksheet_earth |
| `eris_visualization_shells.py` | 5 | worksheet_eris |
| `jupiter_visualization_shells.py` | 18 | worksheet_jupiter |
| `mars_visualization_shells.py` | 4 | worksheet_mars |
| `mercury_visualization_shells.py` | 7 | worksheet_mercury |
| `info_dictionary.py` | 124 | 4 info_dict worksheets (mostly accepted residuals) |
| `star_notes.py` | 32 | stars_final + stars_followup + provenance_final |
| `solar_visualization_shells.py` | 25 | provenance_final (partial) |
| `uranus_visualization_shells.py` | 24 | provenance_final (partial — Uranus belts) |

### 3c. Track 2 — files needing entirely new worksheets

| File | Findings | Priority |
|------|--------:|----------|
| `celestial_objects.py` | 54 | First (design review) |
| `neptune_visualization_shells.py` | 26 | High |
| `pluto_visualization_shells.py` | 10 | Medium |
| `saturn_visualization_shells.py` | 10 | Medium |
| `venus_visualization_shells.py` | 8 | Medium |
| `planet9_visualization_shells.py` | 5 | L-159 (disclosed approx) |
| `moon_visualization_shells.py` | 4 | Lower |

### 3d. Files NOT in backfill scope

These need sourcing (V4 → V3) before cross-checking (V3 → V2):

| File group | Tier 1 | Problem type |
|-----------|-------:|-------------|
| `shell_configs.py` | 24 | L-173: uncited values in cited blocks |
| `idealized_orbits.py` | 26 | Uncited orbital data |
| `paleoclimate_*.py` (5 files) | 93 | L-175: uncited temperature claims |
| Sgr A* files (4) | 14 | Specialized stellar mechanics |

---

## 4. Builder instructions for Opus 5

### Piece 1 (scanner mechanism)

1. Build `has_cross_check(text)` returning structured records, not a
   boolean. The caller needs checker identity to enforce two-distinct.

2. The regex MUST anchor on `# Cross-checked:` with the colon. Without
   it, `planet_visualization_utilities.py` line 492 is a live false
   positive today. Use `r'#\s*[Cc]ross-checked\s*:'` not a loose match.

3. Do NOT put a worked annotation example in the V_CROSS_CHECKED
   constant's comment block. The scanner scans itself — a complete
   example there would grant the ladder constants V2 on themselves.
   Reference the skill doc instead.

4. Keep `test_cross_checked.py` fixtures inside function bodies, not
   as module-level constants. The scanner scans test files.

5. Do NOT add `Cross-checked` to SOURCE_PATTERNS. A malformed annotation
   should earn nothing — the correct behavior, not a design gap.

### Piece 2 Track 1 (annotation insertion)

1. Place annotations adjacent to the existing `# Source:` comment run.
   Inserting lines pushes existing comments further from claims —
   the lookback window is 30 lines back. A `# Source:` at 14-15 lines
   above its claim could be pushed out of range.

2. Annotation insertion is claim-level, not file-level. Only claims
   that are (a) already sourced, (b) covered by a worksheet, and
   (c) confirmed convergent by Tony get annotated.

3. After insertion, run a full audit and diff by finding identity
   `(file, line, name, vuln)` against the baseline. No vulnerability
   regressions allowed — a V3→V4 anywhere means an insertion pushed
   a source out of lookback range.

4. Bottom-up edit ordering within each file. Binary-mode edits. ASCII
   only. Standard safe-file-editing discipline.

---

## 5. Constraints (decided, not open for redesign)

1. **V2 = cited AND two distinct cross-checks.** Resolved by competitive
   review (4 reviewers converged).
2. **Anti-gaming rule.** No parenthetical reference → annotation not
   valid.
3. **Same lookback window.** No new extraction or positional logic.
4. **V_CROSS_CHECKED never auto-promotable to V_FETCHED.**
5. **Population conservation verified by identity diff, not total count.**
6. **`# Cross-checked:` is NOT added to SOURCE_PATTERNS.** A malformed
   annotation earns nothing — this is correct.

---

## 6. Ref

- `provenance_scanner.py` at HEAD (`d03f586`)
- `skills/provenance-discipline/SKILL.md` v1.4 (repo version)
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` §D4
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` §D4
- `LEDGER_CONSOLIDATED.md` L-156, L-157, L-161
- All 15 verification worksheets (see §3a)
- `planet_visualization_utilities.py` line 492 (false positive anchor)
- `test_provenance_1d.py` (27 tests), `test_citation_inheritance.py`
  (20 tests)
- Competitive review: GPT, Opus 5 (×2), Fable 5 — all verified against
  live repo at `d03f586`

**Note:** the resident Skill Manifest lists provenance-discipline at 1.2;
the repo's SKILL.md is at 1.4. Worth a `skills_index.py` regeneration.

---

*Predesign R1 prepared August 1, 2026 by Claude Opus 4.6.*
*Incorporates decisions from competitive review by GPT, Opus 5, Fable 5.*
*Tony-action (do): review Claude's cross-check worksheets against
Gemini's April results; flag divergences for discussion or GPT
tiebreaker.*
