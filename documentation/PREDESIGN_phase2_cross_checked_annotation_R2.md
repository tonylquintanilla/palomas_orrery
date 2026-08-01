# Predesign R2: L-156 Phase 2 — D4 Cross-Checked Annotation + Backfill

**Built on `d03f586196bc07e8c4cb6f8435e16ac85de194b9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared by:** Claude Opus 4.6 (orchestration)
**Reviewed by:** GPT (×2), Claude Opus 5 (×2), Claude Fable 5
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
(V2). A parser function, a scoring change in `score_unit()`, diagnostics,
and tests.

**Piece 2 (backfill):** write `# Cross-checked:` annotations onto claims
verified via the competitive pattern. Two tracks:

- **Track 1:** complete the competitive pattern for files that already
  have Gemini worksheets. Claude independently verifies the same claims
  (orchestration session). Tony compares. Convergent claims get
  annotated. Divergences get discussed; unresolved ones go to GPT as
  tiebreaker.

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
requires BOTH source evidence (direct citation or inherited) AND two
valid `# Cross-checked:` lines with distinct checker identities to
score V2.

**Anti-gaming rule (decided, design review confirmed):** the parenthetical
worksheet reference is REQUIRED. An annotation without a reference does
not contribute to V2.

### 2b. Parser

A new function, `parse_cross_checks(text)`, returning
`(records, issues)`:

- **records:** list of valid `(checker_identity, date, reference)`
  tuples — one per qualifying annotation line.
- **issues:** list of `(raw_line, error_code)` for malformed annotations
  the parser rejected (e.g. `missing_reference`, `missing_year`,
  `non_markdown_reference`).

The caller uses `records` for scoring and `issues` for diagnostics.

A convenience wrapper `has_cross_check(text)` can return
`len(records) > 0` if needed, but scoring uses the structured output.

**The regex** matches lines of the form:

```
# Cross-checked: <identity> <ISO-date> (<ref>)
```

Anchored per-line in multiline text:

```python
r'(?mi)^\s*#\s*cross-checked\s*:'
```

Using `re.MULTILINE` and `re.IGNORECASE` — not manual `[Cc]`.

This is critical — `planet_visualization_utilities.py` already contains
"Giants cross-checked to Voyager 2 (Uranus: Desch..." in a comment
around lines 456-457 at HEAD. Without the colon anchor, that line
would be a false positive.

**Date format: ISO only.** The date must begin with a four-digit year:
`YYYY-MM-DD`, `YYYY-MM`, or bare `YYYY`. Prose dates like "April 2026"
are NOT accepted — they create parsing ambiguity between the checker
identity and the date (e.g. does "April" belong to the identity or the
date?). This makes the parser deterministic.

**Reference:** must be a non-empty parenthetical ending in `.md`. This
rejects trivial references like `(x)` or `(done)`. It does NOT
guarantee the file exists — repository-level traceability is a separate
integrity check, not the parser's job.

**Checker identity:** everything between the colon and the ISO date,
trimmed. Two annotations are "distinct" if their identities differ
after case-folding and whitespace normalization.

**Known limitation (document, don't over-build):** "Gemini" vs
"Gemini Pro" would count as distinct identities. The scanner checks
string identity, not model family. The competitive pattern is
human-mediated — Tony confirms the two legs are genuinely independent.
The scanner's job is to see that two different checker strings exist
with valid references, not to classify AI providers.

### 2c. Scoring change in `score_unit()`

**V2 requires BOTH source evidence AND competitive cross-check.**

Central design decision from the competitive review (5 reviewers,
two rounds):

- Without sourcing as a prerequisite, an uncited claim with valid
  annotations jumps V4→V2 — stronger than cite-to-clear.
- Without requiring two distinct checkers, a single annotation earns a
  rung defined by a two-model process.
- A cross-check is verification of a sourced claim, not a substitute
  for sourcing.

**Source evidence includes inherited citations.** A unit inside a cited
dictionary block (via the existing `inherited_citation` path) counts as
sourced for V2 purposes. The prerequisite is:

```python
sourced = cited or bool(unit.inherited_citation)
```

Not just `cited`. Without this, a unit with a legitimate enclosing-block
citation and two valid cross-checks stays V3 — inconsistent with how the
scanner already treats inherited citations as real sourcing.

New flow:

```python
cited = has_citation(text, is_docstring=is_doc)
records, issues = parse_cross_checks(text)
distinct_checkers = len({r.identity.lower().strip() for r in records}) >= 2
sourced = cited or bool(unit.inherited_citation)

if sourced and distinct_checkers:
    V_CROSS_CHECKED
    reason: "Cross-checked by <N> models (<identities>)"
elif sourced and records:
    V_SOURCED
    reason: "Cited; cross-check incomplete (<N>/2 models)"
elif cited:
    V_SOURCED  (existing reasons unchanged)
elif unit.inherited_citation:
    V_SOURCED  (existing reason unchanged)
else:
    V_RECALLED  (existing reasons unchanged)
```

**What happens to a malformed annotation.** `# Cross-checked:` is NOT
in SOURCE_PATTERNS and must NOT be added. A malformed annotation
(no reference, no year, etc.) does not contribute a record. If the claim
has a separate `# Source:` or inherited citation, it stays V3. If it has
no source at all, it stays V4. A malformed annotation earns nothing.

**The incomplete case.** One valid cross-check on a sourced claim
(only one model so far) stays V_SOURCED but gets a distinct reason
string noting the incomplete state. This surfaces in the audit as
a visible "one leg done" signal without granting V2.

**Stale interaction:** a fully qualified cross-checked claim with a
staleness marker still scores V_CROSS_CHECKED, with staleness noted
in the reason string.

### 2d. V_CROSS_CHECKED comment update

The current comment reads: "blind (the checker was not shown our value)."

Update to reflect the actual decided method: independently verified via
the competitive pattern (same worksheet, independent models, integrator
compares). The old wording conflicts with the decided workflow, where
both models see the claims — the discipline is independent research and
source citation, not blindness to the values.

**Do NOT put a worked annotation example in this comment block.** The
scanner scans itself — a complete example with a parenthetical reference
would grant the ladder constants V2 on themselves. Reference the skill
doc instead.

### 2e. Diagnostics

Report diagnostics (not findings, not score changes) for:

- Cross-check annotation on an unsourced unit (issues from
  `parse_cross_checks` + scoring context)
- Two annotations with the same checker identity
- Annotation reference doesn't end in `.md`
- Any other parse issues from the `issues` list

These print to the audit's diagnostic section, same pattern as existing
shadow-constant and citation-mismatch diagnostics. The `issues` list
from `parse_cross_checks()` feeds this — malformed annotations that the
parser rejected are visible here, not silently dropped.

**Scope note:** diagnostics require collecting issue records during
scanning, passing them to `generate_report()`, and rendering a new
subsection. This is modest plumbing but more than "one function and a
score change" — name it in the build plan.

### 2f. Report changes

The existing tier math works unchanged. A display string (C=4) with
V_CROSS_CHECKED (V=2) scores 8, Tier 3. That's a demotion from Tier 2
(C=4 × V=3 = 12). Intended effect.

Remove the "NOTHING SETS THIS YET" comment from the V_CROSS_CHECKED
constant definition.

### 2g. Test plan

New test file: `test_cross_checked.py`.

**Keep all example strings inside function bodies, not as module-level
constants.** The scanner scans test files (`test_reset_completeness.py`
contributes 1 finding today). Module-level dicts or string constants
would create new self-scan findings.

Tests:

1. **Full V2 scoring:** sourced (direct citation) + two distinct valid
   annotations → `score_unit()` assigns V_CROSS_CHECKED.

2. **V2 with inherited citation:** inherited_citation + two distinct
   valid annotations → V_CROSS_CHECKED. Source evidence includes
   inherited citations.

3. **V2 requires source evidence:** two valid annotations but NO
   `# Source:` and no inherited citation → V_RECALLED. Cross-check
   doesn't substitute for sourcing.

4. **Single checker (incomplete):** sourced + one valid annotation →
   V_SOURCED with "incomplete" reason string.

5. **Two checks, same identity:** two lines both saying "Gemini" →
   `distinct_checkers` is False → V_SOURCED.

6. **Missing reference (anti-gaming):** `# Cross-checked: Gemini
   2026-04-15` (no parenthetical) → no valid record. Claim stays at
   whatever its source status gives it.

7. **Empty or trivial reference:** `()` and `(x)` (no `.md` suffix)
   → not valid records.

8. **No false positives from normal citations:** `# Source: NASA` →
   `parse_cross_checks()` returns no records.

9. **The Voyager false positive:** the exact text from
   `planet_visualization_utilities.py` — "Giants cross-checked to
   Voyager 2 (Uranus: Desch..." — must NOT produce a record. This is
   the anchoring test: no colon directly after "cross-checked."

10. **Case insensitivity:** `# cross-checked:` and `# CROSS-CHECKED:`
    both produce valid records.

11. **ISO date requirement:** annotation with no four-digit year → not
    a valid record. Prose date "April 2026" without a YYYY token → not
    valid.

12. **Staleness interaction:** fully qualified cross-check + stale
    marker → V_CROSS_CHECKED, reason includes "date-sensitive."

13. **Population conservation (fixture):** add two annotations to a
    synthetic sourced unit. Finding identity stays the same, only V and
    tier change. Identity key: `(file, kind, name, content_fingerprint)`.

14. **Lookback window bleed:** two adjacent sourced findings, only one
    annotated with two valid cross-checks. Assert the second does NOT
    receive V2. **If this test reveals bleed:** the mitigation is tight
    placement (annotations adjacent to their claims, within the existing
    `# Source:` comment run). State this in builder instructions — do
    not block on it.

15. **Scanner self-scan regression:** full scan with zero annotations
    in source files. Compare against baseline by identity diff using
    `(file, kind, name, content_fingerprint)`. Any self-scan delta
    from the new code must be examined and explained, not just
    counted. The new test file adds one file to the scan (117 total).

16. **Parse issues:** malformed annotation → appears in the `issues`
    list with correct error code. Verify `missing_reference`,
    `missing_year`, and `non_markdown_reference` codes.

---

## 3. Piece 2: Backfill — corrected worksheet inventory

### 3a. Full worksheet inventory

Fifteen verification worksheets exist on disk. The D3 calibration
worksheet is a methodology document, not a data-verification worksheet.

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
| `info_dict_worksheet_2C_comets_exoplanets.md` | Comets & exoplanets |

**star_notes.py worksheets (2):**

| Worksheet | Coverage |
|-----------|----------|
| `provenance_worksheet_stars_final.md` | 10 star entries |
| `provenance_worksheet_stars_followup.md` | 5 additional stars |

**Cross-cutting worksheets (2):**

| Worksheet | Coverage |
|-----------|----------|
| `provenance_worksheet_final.md` | Oort Cloud, star_notes params, Uranus belts |
| `provenance_worksheet_tier1_final.md` | 7 Tier-1 gaps across multiple files |

### 3b. Track 1 — completing the competitive pattern

These files have Gemini's leg. Claude independently verifies the same
claims. Tony compares. Only claims where BOTH models converge AND
source evidence exists get the `# Cross-checked:` annotation.

**Coverage is claim-level, not file-level.** A file can contain claims
ready for cross-checking alongside claims that need primary sourcing
first. Only sourced, worksheet-covered, convergent claims get annotated.

| Target module | Findings | Worksheets covering it |
|--------------|--------:|----------------------|
| `asteroid_belt_visualization_shells.py` | 7 | worksheet_asteroid_belt + tier1_final |
| `comet_visualization_shells.py` | 23 | worksheet_comet + info_dict_2C (partial) |
| `earth_visualization_shells.py` | 27 | worksheet_earth |
| `eris_visualization_shells.py` | 5 | worksheet_eris |
| `jupiter_visualization_shells.py` | 18 | worksheet_jupiter |
| `mars_visualization_shells.py` | 4 | worksheet_mars |
| `mercury_visualization_shells.py` | 7 | worksheet_mercury |
| `info_dictionary.py` | 124 | 4 info_dict worksheets (mostly accepted residuals) |
| `star_notes.py` | 32 | stars_final + stars_followup + provenance_final |
| `solar_visualization_shells.py` | 25 | provenance_final (partial) |
| `uranus_visualization_shells.py` | 24 | provenance_final (partial) |

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

1. Build `parse_cross_checks(text)` returning `(records, issues)`.
   The caller needs structured records to enforce two-distinct-checkers,
   and needs issues for diagnostics.

2. The regex MUST use `re.MULTILINE` and anchor to line start with
   required colon: `r'(?mi)^\s*#\s*cross-checked\s*:'`. Without the
   colon, `planet_visualization_utilities.py` ~line 456 is a live
   false positive.

3. Source prerequisite for V2 is `sourced = cited or
   bool(unit.inherited_citation)`. Not just `cited`. Inherited
   citations are real sourcing.

4. Update the V_CROSS_CHECKED comment to say "independently verified
   via competitive pattern" instead of "blind (the checker was not
   shown our value)." Do NOT put a worked annotation example in that
   comment block — the scanner scans itself.

5. Keep `test_cross_checked.py` fixtures inside function bodies, not
   as module-level constants.

6. Do NOT add `Cross-checked` to SOURCE_PATTERNS. A malformed
   annotation earns nothing — correct behavior.

7. Diagnostics require plumbing: collect `issues` during scanning,
   pass to `generate_report()`, render in a new diagnostic subsection.
   Same pattern as shadow-constant diagnostics.

### Piece 2 Track 1 (annotation insertion)

1. Place annotations adjacent to the existing `# Source:` comment run,
   within it. Inserting lines pushes existing comments further from
   claims — the lookback window is 30 lines. A `# Source:` near the
   window edge could be pushed out of range.

2. Annotation insertion is claim-level, not file-level. Only claims
   that are (a) sourced, (b) covered by a worksheet, and (c) confirmed
   convergent by Tony get annotated.

3. After insertion, run a full audit and diff by stable finding identity
   `(file, kind, name, content_fingerprint)` against the baseline. No
   vulnerability regressions allowed. Line numbers shift — that's
   expected. Vuln changes — only on annotated claims, V3→V2. Any other
   vuln change means an insertion pushed a source out of lookback range.

4. Bottom-up edit ordering within each file. Binary-mode edits. ASCII
   only. Standard safe-file-editing discipline.

---

## 5. Constraints (decided, not open for redesign)

1. **V2 = sourced AND two distinct cross-checks.** Sourced means
   direct citation or inherited citation.
2. **Anti-gaming rule.** No parenthetical `.md` reference → annotation
   not valid.
3. **ISO dates only.** YYYY, YYYY-MM, or YYYY-MM-DD.
4. **Same lookback window.** No new extraction or positional logic.
5. **V_CROSS_CHECKED never auto-promotable to V_FETCHED.**
6. **Population conservation verified by identity diff, not total
   count.** Identity key: `(file, kind, name, content_fingerprint)`.
7. **`# Cross-checked:` is NOT added to SOURCE_PATTERNS.**
8. **Checker identity is string-level, not family-level.** "Gemini"
   vs "Gemini Pro" would count as distinct. Known limitation;
   competitive pattern is human-mediated.

---

## 6. Ref

- `provenance_scanner.py` at HEAD (`d03f586`)
- `skills/provenance-discipline/SKILL.md` v1.4 (repo version)
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` §D4
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` §D4
- `LEDGER_CONSOLIDATED.md` L-156, L-157, L-161
- All 15 verification worksheets (§3a)
- `planet_visualization_utilities.py` ~line 456 (false positive anchor)
- `test_provenance_1d.py` (27 tests), `test_citation_inheritance.py`
  (20 tests)
- Competitive review: GPT (×2), Opus 5 (×2), Fable 5 — all verified
  against live repo at `d03f586`

**Note:** the resident Skill Manifest lists provenance-discipline at 1.2;
the repo's SKILL.md is at 1.4. Worth a `skills_index.py` regeneration.

---

*Predesign R2 prepared August 1, 2026 by Claude Opus 4.6.*
*Incorporates two rounds of competitive review by GPT, Opus 5, Fable 5.*
*Tony-action (do): review Claude's cross-check worksheets against
Gemini's April results; flag divergences for discussion or GPT
tiebreaker.*
