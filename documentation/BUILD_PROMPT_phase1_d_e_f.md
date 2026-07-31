# Build Prompt — Phase 1d / 1e / 1f (L-156 provenance scanner)

**Built on `4b6b5c121745a6d69cf2d0cfdf8a07ff37e0245a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are the designer and builder for Phase 1, sub-steps 1d/1e/1f of the
provenance scanner refactor (L-156). You built 1c successfully (see
`documentation/AS_BUILT_L156_phase1c.md`). You also reviewed the v0
predesign for this work and caught four factual errors, all now corrected
in the attached R1 predesign.

Tony Quintanilla is the integrator. He mediates between sessions, holds
sole commit authority, and makes all judgment calls. He runs Python via
VS Code's Run button, and git via GitHub Desktop only.

## The work

Three sub-steps, each documented in the attached predesign
(`PREDESIGN_HANDOFF_phase1_d_e_f_R1.md`). In brief:

**1d — scanner recognition work (three pieces):**
1. Amend `build_pinned_values()` / Option A (live at lines 1409/1563-1577)
   so a bare numeric match without a corresponding import is flagged as a
   frozen copy, not silently granted V_SOURCED.
2. Add citation-form recognition for bare author-year parentheticals —
   both `(Author et al., YYYY)` and `(Author et al.)` forms. ~15
   findings affected (measured by your review, not the old ~54 estimate).
   Watch for false positives on `(May 2026)` and similar date
   parentheticals.
3. Add bare-degree F/C values to `NUMERIC_CLAIM_RE` (L-078(d)).

**1e — console output (two pieces):**
1. Tier-1 banner: prominent, bordered, informational only. NO exit-code
   gate — ever. (Design review §3c supersedes the deferred-flip in the
   Fable design and in `HANDOFF_phase1_1d_to_1f.md` at HEAD.)
2. Tier-2 label: remove "ALL ACCEPTED RESIDUALS" blanket claim, replace
   with neutral score-band names. Per-finding accepted-residual marking
   via `provenance_exceptions.json`.

**1f — mechanical code fix:**
Delete shadow constants in `comet_visualization_shells.py` (lines
492-493, 602), import `SUN_RADIUS_KM` through the shim and
`SOLAR_RADIUS_AU` (not `SUN_RADIUS_AU` — that name doesn't exist) from
`constants_new.py`. Grep the file for any other shadow constants before
treating the edit as complete.

## Sequencing (revised per your review)

**1d → 1f → 1e.** Build the frozen-copy detector first. Run the scanner.
Watch it fire on `comet_visualization_shells.py` lines 492-493. Then 1f
deletes those shadow constants; re-run the scanner; the findings should
disappear. 1e last, after the tier distribution has settled.

You recommended splitting into two sessions. Tony's call — he may
confirm or override when he reviews. If one session, the sequencing above
still holds.

## What you already know that a cold start wouldn't

You built 1c. You know the scanner's internal structure, the patch
conventions (anchored transactional, MD5 guard, bottom-up, binary mode,
all-or-nothing), the test suites, and the self-scan quirk. You also
reviewed this predesign and caught real errors. The R1 predesign
incorporates all your corrections and credits them. You do not need to
re-verify what you already verified — but do re-verify HEAD, since
your review was built on `4b6b5c12` and HEAD may have moved again by
the time this session starts.

## Decided constraints (from the predesign, not repeated in full)

Read predesign section 5 for the complete list. The key ones:
- V-ladder: V1/V2/V3/V4, four rungs, decided.
- Tier-1: permanent banner, never auto-exit.
- No Shadow Constants [CRITICAL]: provenance-discipline v1.3 at HEAD.
- `build_pinned_values()` is live — amend, don't assume retired.
- ASCII-only, LF-only, bottom-up editing, binary-mode patches.

## Errata in the document chain (from predesign section 9)

Three documents at HEAD carry known errors:
1. `HANDOFF_phase1_1d_to_1f.md`: wrong on 1e (describes deferred
   exit-gate; design review §3c supersedes).
2. Design handoff D8.5: says retire `build_pinned_values()`; not done.
3. `provenance-discipline/SKILL.md` v1.3: SHA placeholder not stamped.

The predesign and the design review are authoritative where they differ
from these.

## Reference documents to read from the repo

Pull and read from live HEAD before designing:

- `LEDGER_CONSOLIDATED.md` — entries L-156, L-158, L-078, L-173, L-174
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md`
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md`
- `documentation/AS_BUILT_L156_phase1c.md`
- `skills/provenance-discipline/SKILL.md` (v1.3 at HEAD)
- `skills/safe-file-editing/SKILL.md` (v1.1)
- `provenance_scanner.py` — the build target; read the live code,
  especially `build_pinned_values()` (line 1409), `score_unit()` Option A
  (lines 1563-1577), `has_citation()` / `SOURCE_PATTERNS`, and
  `NUMERIC_CLAIM_RE`
- `comet_visualization_shells.py` — the 1f target; read lines 42 (import),
  492-493 (shadow constants), 602 (derived shadow)
- `paleoclimate_wet_bulb_full.py` lines 137-138 — the citation-form
  motivating instances

## Verification expectations (from predesign section 8)

Same pattern as 1c: MD5 guard, anchored transactional patch, before/after
audit diff (line by line, self-scan delta first), regression suites
(test_constants_provenance 73/73, test_citation_inheritance 20/20),
py_compile, ASCII/LF gates, idempotency check. Live scan on a throwaway
clone as the runtime-equivalent agentic pre-test.

## Attached documents

1. `PREDESIGN_HANDOFF_phase1_d_e_f_R1.md` — the revised predesign
   (corrections marked **[R1]**)
2. `REVIEW_predesign_1d_1e_1f.md` — your own review of the v0 predesign
   (for reference; the R1 predesign incorporates all corrections)

## What to do now

Design and build 1d, 1e, 1f within the boundaries above. Produce
deliverables (patch script(s) + test(s)) and an as-built document per
the 1c precedent. If you find anything that contradicts the predesign or
the decided constraints, flag it for Tony rather than resolving it
yourself.

---

*Build prompt drafted July 31, 2026 by Claude Opus 4.6 at Tony's request.
Corrections from Opus 5's review integrated into the R1 predesign.*
