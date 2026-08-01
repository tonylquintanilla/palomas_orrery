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
Scanner rebuild (Opus 5, Phase 1 sub-stepped 1a-1f): **PHASE 1 COMPLETE.**

  1a  DONE
  1b  DONE
  1c  DONE -- citation-block inheritance. Two spin-offs both closed:
        L-173 -- 18 genuinely uncited shell_configs.py findings, parked
          for Phase 4 Gemini worksheet.
        L-174 -- citation-level mismatch diagnostic, fixed and closed.
  1d  DONE -- three pieces: shadow-constant detector (built as dedicated
        scan_shadow_constants(), diverging from predesign's Option A
        amendment for three measured reasons); citation-form recognition
        for author-year parentheticals (~13 findings moved Tier 1 to
        Tier 2); temperature units added to NUMERIC_CLAIM_RE (+61 new
        Tier-1 findings, tracked as L-175).
  1e  DONE -- Tier-1 banner (informational, no exit gate -- ever).
        Tier labels neutralized (2/3/4); Tier 1 keeps FIX NOW.
  1f  DONE -- shadow constants deleted in comet_visualization_shells.py,
        proper imports through shim. Fire-then-silence test confirmed.

  Follow-on: build_pinned_values() citation-bleed flaw fixed. Shared
  constant_has_own_citation() predicate extracted; both pinned-value
  builders routed through it. Defensive (zero measured impact today;
  prevents future silent mis-scoring).

Current scanner state at HEAD (b813aa6): Tier 1 171, Tier 2 644,
Tier 3 62, Tier 4 2 (879 findings / 116 files). Tier 1 is 132 baseline
+ 39 newly-visible temperature claims (L-175). Phase 1 measured arc:
Tier 1 145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171
(1d/1e/1f).

Still open under L-156: D8.5 (retire or keep Option A); Phases 2-4.

What comes next, in order:

1. L-157 / L-161 -- Gemini cross-check sweeps. These source the genuinely
   uncited findings (L-173's 18 shell_configs gaps, L-175's 61 temperature
   claims, and remaining uncited claims).
2. L-155 / L-160 -- Phase 3, pinning engine and test retirement.
3. Resume L-154's own design questions -- the JS feature-rendering layer
   (geometry-building approach, legend behavior, artifact sequencing).
4. Build Artifact 2 (Jupiter/Saturn with rings, shells, radiation belts).

Adjacent, already resolved: L-162 (CENTER_BODY_RADII naming) done. L-163
(module role/domain classification) -- role side closed; domain side
deferred into the L-156 cluster.
