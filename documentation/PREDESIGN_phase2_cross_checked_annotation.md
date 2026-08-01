# Predesign: L-156 Phase 2 — D4 Cross-Checked Annotation + Backfill

**Built on `d03f586196bc07e8c4cb6f8435e16ac85de194b9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared by:** Claude Opus 4.6 (orchestration)
**For:** Claude Opus 5 (builder, Piece 1); this session (Piece 2 Track 1)
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

Two carry-over items from Phase 1 are already resolved at HEAD:
`patch_retire_option_a.py` is in `documentation/` (not repo root), and
the duplicate "Phase 1 measured arc" paragraph is gone. No action needed.

---

## 1. What Phase 2 builds

Two pieces, sequenced.

**Piece 1 (scanner mechanism):** teach `provenance_scanner.py` to
recognize `# Cross-checked:` annotations and score them V_CROSS_CHECKED
(V2) instead of V_SOURCED (V3). One new recognition function, a change
to `score_unit()`, and tests. No new positional rules — same lookback
window as `# Source:`.

**Piece 2 (backfill):** write `# Cross-checked:` annotations onto claims
that have been independently verified via the competitive pattern (same
worksheet, two models independently, Tony compares). Two tracks:

- **Track 1 (complete the competitive pattern for April-worksheeted
  files):** the April 2026 Gemini worksheets are one leg. Claude
  independently verifies the same claims (this session). Tony compares.
  Convergent values get annotated. Divergences get discussed here;
  claims that can't be settled go to GPT as a tiebreaker.

- **Track 2 (new worksheets for uncovered files):** starting with
  `celestial_objects.py` (54 findings, zero prior coverage). Both
  Claude and Gemini get the same worksheet. Separate sessions.

**Build order:** Piece 1 first (the scanner must recognize the annotation
before anyone writes one). Piece 2 Track 1 second (review here, then
Opus 5 inserts annotations mechanically). Track 2 is separate sessions.

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
needs at least one valid `# Cross-checked:` with a parenthetical
reference to score V2.

**Anti-gaming rule (decided, design review confirmed):** the parenthetical
worksheet reference is REQUIRED. An annotation without a reference scores
V_SOURCED, not V_CROSS_CHECKED. The mechanism must not become a new way
to cite-to-clear.

### 2b. Recognition logic

A new function, `has_cross_check(text)`, separate from `has_citation()`.

The regex matches:

```
# Cross-checked: <who> <date> (<ref>)
```

Where:
- `<who>` is one or more words (the checker model/identity)
- `<date>` is a date in any reasonable format (YYYY-MM-DD, YYYY-MM, or
  prose like "April 2026")
- `(<ref>)` is a parenthetical containing the worksheet/document
  reference — REQUIRED

The function returns True only if BOTH the `# Cross-checked:` prefix
AND the parenthetical reference are present.

**Placement:** immediately after `has_citation()` in the source, same
module section. Uses the same lookback-window text that `has_citation()`
receives — no new extraction logic needed.

### 2c. Scoring change in `score_unit()`

Current flow (simplified):

```
cited = has_citation(text)
if cited:        V_SOURCED
elif inherited:  V_SOURCED
else:            V_RECALLED
```

New flow:

```
cited = has_citation(text)
cross_checked = has_cross_check(text)

if cross_checked:
    V_CROSS_CHECKED  (reason: includes model + date + ref)
elif cited:
    V_SOURCED  (existing reasons unchanged)
elif inherited:
    V_SOURCED  (existing reason unchanged)
else:
    V_RECALLED  (existing reasons unchanged)
```

The cross-check test runs FIRST. A line with both `# Source:` and
`# Cross-checked:` gets V_CROSS_CHECKED — the stronger annotation wins.
A `# Cross-checked:` without a parenthetical falls through to the
`cited` branch (because `# Cross-checked:` itself will match
`has_citation()`'s existing patterns — "Verified" and "Confirmed" are
already in SOURCE_PATTERNS). This is the anti-gaming rule: the annotation
without its reference doesn't get special treatment.

**Stale interaction:** a cross-checked claim with a staleness marker
still scores V_CROSS_CHECKED, but the reason string notes the staleness.
Cross-checking confirms the value was correct at the check date;
staleness means it may have changed since. Both facts are worth
recording.

### 2d. Report changes

The existing tier math works unchanged. A display string (C=4) with
V_CROSS_CHECKED (V=2) scores 8, which is Tier 3 (5-9) — a demotion
from the current Tier 2 (C=4 × V=3 = 12). That's the intended effect.

Remove the "NOTHING SETS THIS YET" comment from the V_CROSS_CHECKED
constant definition once the recognition lands.

### 2e. Test plan

New test file: `test_cross_checked.py`.

1. **Basic recognition:** `# Cross-checked: Gemini 2026-04-15
   (worksheet_earth.md)` → `has_cross_check()` returns True.

2. **Missing reference (anti-gaming):** `# Cross-checked: Gemini
   2026-04-15` (no parenthetical) → returns False. Scores V_SOURCED
   via existing citation patterns, not V_CROSS_CHECKED.

3. **Scoring integration:** synthetic ProvenanceUnit with cross-checked
   text → `score_unit()` assigns V_CROSS_CHECKED. Same unit without the
   ref → V_SOURCED.

4. **Staleness interaction:** cross-checked + stale marker → still
   V_CROSS_CHECKED, reason includes "date-sensitive."

5. **No false positives from normal citations:** `# Source: NASA` →
   `has_cross_check()` returns False.

6. **Case insensitivity:** `# cross-checked:` and `# CROSS-CHECKED:`
   both match.

7. **Population conservation:** total finding count must not change when
   a `# Cross-checked:` annotation is added — only the tier moves.

8. **Date format variants:** `2026-04-15`, `2026-04`, `April 2026` →
   all match.

9. **Multiple cross-check lines:** two `# Cross-checked:` lines (one
   per model) → `has_cross_check()` returns True on either.

---

## 3. Piece 2 Track 1: completing the competitive pattern

### 3a. How it works

Seven Gemini worksheets exist on disk. They are the claims to check —
organized by file, grouped by feature, with our current values. Gemini
verified these in April 2026 (corrections already applied to code).

Claude independently verifies the same claims in this session. Claude
researches each claim against authoritative sources without reference to
Gemini's April answers. Tony compares:

- **Convergence** (both models found the same value from different
  sources): high confidence. Annotate.
- **Divergence** (they disagree): discuss here. If we can't settle it,
  that specific claim goes to GPT as a third cross-checker.

After Tony confirms, Opus 5 mechanically inserts the `# Cross-checked:`
annotations into the source files.

### 3b. The seven files

| Worksheet file | Target module | Findings at HEAD |
|---------------|--------------|--------:|
| `worksheet_asteroid_belt.md` | `asteroid_belt_visualization_shells.py` | 7 |
| `worksheet_comet_visualization.md` | `comet_visualization_shells.py` | 23 |
| `worksheet_earth_visualization.md` | `earth_visualization_shells.py` | 27 |
| `worksheet_eris_visualization.md` | `eris_visualization_shells.py` | 5 |
| `worksheet_jupiter_visualization.md` | `jupiter_visualization_shells.py` | 18 |
| `worksheet_mars_visualization.md` | `mars_visualization_shells.py` | 4 |
| `worksheet_mercury_visualization.md` | `mercury_visualization_shells.py` | 7 |

### 3c. Files with partial Gemini verification but no worksheet on disk

These had verification done in conversation (per scanner docstring
Stages 1-5) but no committed worksheet. They need new worksheets
drafted from scratch — both legs of the competitive pattern:

| File | Notes | Findings at HEAD |
|------|-------|--------:|
| `info_dictionary.py` | Stage 2: "54 Tier-1 processed" | 124 (mostly accepted residuals) |
| `star_notes.py` | Stage 5: "10 star entries verified" — partial | 32 |
| `solar_visualization_shells.py` | Stage 3: "34 citations added" | 25 |
| `uranus_visualization_shells.py` | Stage 3: "10 citations added" | 24 |

### 3d. Files needing entirely new worksheets (Track 2, separate sessions)

| File | Findings | Priority |
|------|--------:|----------|
| `celestial_objects.py` | 54 | First (design review) |
| `neptune_visualization_shells.py` | 26 | High |
| `pluto_visualization_shells.py` | 10 | Medium |
| `saturn_visualization_shells.py` | 10 | Medium |
| `venus_visualization_shells.py` | 8 | Medium |
| `planet9_visualization_shells.py` | 5 | L-159 (disclosed approx) |
| `moon_visualization_shells.py` | 4 | Lower |

### 3e. Files NOT in backfill scope

These need sourcing first (V4 → V3) before they could be cross-checked:

| File group | Tier 1 | Problem type |
|-----------|-------:|-------------|
| `shell_configs.py` | 24 | L-173: uncited values in cited blocks |
| `idealized_orbits.py` | 26 | Uncited orbital data |
| `paleoclimate_*.py` (4 files) | 92 | L-175: uncited temperature claims |
| Sgr A* files (4) | 14 | Specialized stellar mechanics |

---

## 4. Constraints the builder must hold

These are decided; not open for redesign.

1. **Anti-gaming rule.** `# Cross-checked:` without a parenthetical
   reference → V_SOURCED, not V_CROSS_CHECKED.

2. **Same lookback window.** No new extraction or positional logic.

3. **V_CROSS_CHECKED is never auto-promotable to V_FETCHED.**

4. **Population conservation.** Annotations change tiers, not totals.

5. **No new positional rules.** One new recognition function, not a
   new scanning architecture.

6. **Remove "NOTHING SETS THIS YET" comment** from V_CROSS_CHECKED
   definition.

---

## 5. What Opus 5 builds

**Piece 1 (scanner mechanism):**
- `provenance_scanner.py` — new `has_cross_check()`, scoring change in
  `score_unit()`, remove dead-code comment
- `test_cross_checked.py` — new test file (9+ tests)

**Piece 2 Track 1 (annotation insertion):**
- After Tony confirms convergence from the worksheet review (this
  session), Opus 5 mechanically inserts `# Cross-checked:` lines into
  the seven target files. This is Role 3 of the Review-Repair Protocol:
  transcribe confirmed results, don't embellish.

**Expected impact of Piece 1 alone:** zero change. The annotation form
doesn't exist in any file yet. Total findings: 879, unchanged.

---

## 6. Ref

- `provenance_scanner.py` at HEAD (`d03f586`)
- `skills/provenance-discipline/SKILL.md` v1.4 (repo version)
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` §D4
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` §D4
- `LEDGER_CONSOLIDATED.md` L-156, L-157, L-161
- `documentation/worksheet_*.md` (7 files)
- Scanner docstring Stages 1-5 (lines 40-79)
- `test_provenance_1d.py` (27 tests), `test_citation_inheritance.py`
  (20 tests)

---

*Predesign prepared August 1, 2026 by Claude Opus 4.6 (orchestration).*
*Tony-action (do): review Claude's cross-check worksheets against
Gemini's April results; flag divergences for discussion or GPT
tiebreaker.*
