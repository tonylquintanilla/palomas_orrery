# Ledger and Master Plan Update — Phase 2 Piece 1 Landed

**Built on `373c6d8be9e0b5d06b0d5b445219e0d6d152fa13`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared by:** Claude Opus 4.6 (orchestration)
**Date:** August 1, 2026

---

## 1. L-156 ledger update

### What to change

**Scanner state line.** Replace:

```
**Scanner state at HEAD (post-D8.5, `42103d6`):** Tier 1 210, Tier 2
605, Tier 3 62, Tier 4 2, total 879 across 116 files. 879 conserved
across D8.5 — 39 findings moved Tier 2 to Tier 1 (23 from Option A
retirement, 16 from staleness-credit removal).
```

With:

```
**Scanner state at HEAD (post-Phase 2 Piece 1, `373c6d8`):** Tier 1
210, Tier 2 605, Tier 3 62, Tier 4 2, total 879 across 117 files
(+1: `test_cross_checked.py`). 879 conserved across Phase 2 Piece 1 —
zero findings moved. The V_CROSS_CHECKED (V2) recognition mechanism is
live but has zero population (no annotations written yet).
```

**V-ladder description.** Replace:

```
V2 CROSS-CHECKED (never
auto-promotable to V1; requires structured, dated annotation with
blind-check field).
```

With:

```
V2 CROSS-CHECKED (never auto-promotable to V1; requires source
evidence AND two distinct checker annotations via competitive pattern;
see provenance-discipline v1.4).
```

**Add Phase 2 build history.** Insert after the "General lesson (D8.5)"
paragraph and before "### Observations":

```
### Phase 2 build history (D4: cross-checked annotation mechanism)

**Piece 1 — scanner mechanism (2026-08-01, Opus 5).** Teaches the scanner
to recognize `# Cross-checked:` annotations and score them
V_CROSS_CHECKED (V2). Delivered as transactional patch
(`documentation/patch_phase2_piece1.py`, 9 anchored edits).

New code: `parse_cross_checks(text)` parser returning `(records, issues)`,
`distinct_checker_identities()`, `_record_cross_check_diagnostics()`,
scoring branches in `score_unit()`, diagnostic subsection in
`generate_report()`. New test file: `test_cross_checked.py` (16 tests).

V2 scoring rule (decided, 5-model competitive review — GPT ×2, Opus 5 ×2,
Fable 5): `sourced AND two distinct cross-checks`. Sourced means direct
citation or inherited citation. Two distinct means two annotation lines
naming different checker identities (string-level, not model-family-level).
Anti-gaming: parenthetical `.md` reference required. ISO dates only.
`# Cross-checked:` is deliberately NOT in SOURCE_PATTERNS — a malformed
annotation earns nothing.

Predesign went through two review rounds (R0 → R1 → R2). Key findings
from the competitive review: the R0 fallback claim was factually wrong
(all 4 reviewers independently confirmed `has_citation()` does not match
"Cross-checked"); V2 must require source evidence (3/4 converged);
two distinct checkers required (3/4 converged); the worksheet inventory
was wrong (15 not 7, Opus 5 #1 only); a live false positive exists at
`planet_visualization_utilities.py` ~line 456 (Fable only). The
competitive pattern produced genuine discovery — findings missed by some
reviewers were caught by others.

Lookback bleed measured (as-built §5): an annotation promotes sourced
claims within ~50 lines below it. Containment is process-side — the
identity diff after annotation insertion catches unintended promotions.
High-exposure files: `info_dictionary.py` (up to 11 downstream per
annotation). Low-exposure files (mars, eris, earth) proceed as-is.

Decided: V_CROSS_CHECKED comment updated to "independently verified via
competitive pattern" (was "blind"). Worksheets show current values to
both models; the discipline is independent sourcing, not blindness.

**Track 1 scope (decided, not yet executed).** Complete the competitive
pattern for the 15 files that have April 2026 Gemini worksheets. Claude
independently verifies the same claims. Tony compares. Convergent claims
get annotated. Divergences discussed; unresolved claims go to GPT as
tiebreaker.

**Track 2 scope (decided, not yet executed).** New worksheets for
uncovered files, starting with `celestial_objects.py` (54 findings). Both
models get the same worksheet independently. Separate sessions.
```

**Update "What remains open."** Replace:

```
**Phase 2 (D4 cross-checked annotation backfill).** Next in the original
plan. Gated on Phase 1 (now complete).
```

With:

```
**Phase 2 (D4 cross-checked annotation backfill).** Piece 1 (scanner
mechanism) COMPLETE (`373c6d8`). The recognition and scoring are live;
zero population until annotations are written. Track 1 (Claude's
cross-check worksheets for April-worksheeted files) and Track 2 (new
worksheets for uncovered files) are next.
```

**Update the Ref list.** Add:

```
`documentation/patch_phase2_piece1.py`;
`test_cross_checked.py`;
`documentation/AS_BUILT_phase2_piece1.md`;
`documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md`;
`documentation/BUILD_PROMPT_phase2_piece1.md`;
`documentation/REVIEW_PROMPT_phase2_predesign.md`.
```

---

## 2. Master plan update

Replace the entire contents of
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` with:

```
Where we are 8/1/2026

Interactive gallery build (the master plan's own Phase 0-6): Phase 0 (stack
proof, architecture B'), Phase 1a (vocabulary), and Phase 1b (data serving
pipeline -- nightly cache builder, coverage index, served_window trust
system) are all DONE. Layer 3 (Task Scheduler) is live with a known
intermittent promotion-step glitch still being watched.

Phase 2 (current phase) -- the artifacts themselves:

Artifact 1 (Earth) -- built, Mode-5 accepted. Closed.
Artifact 2 (Jupiter/Saturn: rings, shells, radiation belts) -- next in line,
still blocked. Not on data -- the cache builder already serves the real
ported values. Blocked because the client-side JS layer that would draw
those features (L-154) doesn't exist yet.

The detour (L-154-L-162, provenance scanner rebuild) -- status:
Design and ledger formalization for the whole cluster: closed.

Scanner rebuild Phase 1 (Opus 5, sub-stepped 1a-1f): **COMPLETE.**

  1a  DONE -- MEASURED/RELATIONAL, undetermined sentinel, V-ladder, role
        veto amendment.
  1b  DONE -- V-ladder scoring applied across all findings.
  1c  DONE -- citation-block inheritance. Spin-offs: L-173 (18 uncited
        shell_configs findings), L-174 (citation-level mismatch diagnostic).
  1d  DONE -- shadow-constant detector, citation-form recognition,
        temperature units (+61 Tier-1 → L-175).
  1e  DONE -- Tier-1 banner (informational, no exit gate).
  1f  DONE -- shadow constants deleted in comet_visualization_shells.py.
  Follow-ons: build_pinned_values() bleed fix, D8.5 Option A retired.

Scanner rebuild Phase 2 (D4 cross-checked annotation): **IN PROGRESS.**

  Piece 1  DONE (373c6d8) -- scanner mechanism. parse_cross_checks()
        parser, scoring branches in score_unit(), diagnostics,
        test_cross_checked.py (16 tests). V2 requires source evidence
        AND two distinct checker annotations. Five-model competitive
        review (GPT x2, Opus 5 x2, Fable 5). Mechanism live, zero
        population until annotations written.
  Track 1  NEXT -- complete the competitive pattern for 15 files that
        have April 2026 Gemini worksheets. Claude independently verifies
        same claims, Tony compares. Convergent claims get annotated.
  Track 2  LATER -- new worksheets for uncovered files, starting with
        celestial_objects.py (54 findings).

Current scanner state at HEAD (373c6d8): Tier 1 210, Tier 2 605,
Tier 3 62, Tier 4 2 (879 findings / 117 files).

Phase 1 measured arc (the instrument got honest): Tier 1
145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171
(1d/1e/1f) -> 210 (D8.5). The first half (145 -> 132) fixed false
positives -- correctly-sourced claims scored as unsourced. The second
half (132 -> 210) fixed false negatives -- unsourced claims scored as
sourced, whether by a blind spot (temperature recognition, +61), numeric
coincidence (Option A, +23), or a marker meaning the opposite of what it
was credited for (staleness, +16). The number went up because the
instrument got honest.

Still open under L-156: Phase 2 Tracks 1-2, Phases 3-4.

What comes next, in order:

1. Phase 2 Track 1 -- Claude cross-check worksheets for the 15 files
   with Gemini coverage. Divergences discussed or sent to GPT. Opus 5
   inserts converged annotations mechanically.
2. Phase 2 Track 2 -- new worksheets for uncovered files
   (celestial_objects.py first, then neptune, pluto, saturn, venus,
   planet9, moon).
3. L-157 / L-161 -- source the genuinely uncited findings (L-173's
   shell_configs gaps, L-175's temperature claims, remaining uncited).
4. L-155 / L-160 -- Phase 3, pinning engine and test retirement.
5. Resume L-154's JS feature-rendering layer and build Artifact 2.

Adjacent, already resolved: L-162 (CENTER_BODY_RADII naming) done. L-163
(module role/domain classification) -- role side closed; domain side
deferred into the L-156 cluster.
```

---

## 3. Do we need another document before Track 1?

I don't think so. The as-built covers the build. The predesign R2 covers
the Track 1 design (§3b). The worksheets are on disk. What Track 1 needs
is the actual cross-check work — Claude independently researching the
claims against primary sources — which is a different kind of session
than what we've been doing.

A fresh session with this update pushed would come in clean for that
work. The passdown is: this update + the predesign R2 + the as-built,
all in the repo at HEAD.
