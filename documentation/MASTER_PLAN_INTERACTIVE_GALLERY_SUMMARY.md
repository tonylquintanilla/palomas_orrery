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
