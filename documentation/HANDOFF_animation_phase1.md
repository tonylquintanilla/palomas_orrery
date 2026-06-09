# HANDOFF -- Animation Refactor 21/51, Phase 1 (June 9, 2026)

Built on: orrery repo HEAD 730b2bf252351d4f99338911d7c78c1b3efdb50a (verified
via git ls-remote at session start; matches the SHA Tony supplied).
Deliverables: palomas_orrery.py (patched), measure_animation_html.py (new),
ANIMATION_TEST_PROTOCOL_v1.md (new), phase1_diff.txt (review diff vs HEAD).

## What changed (3 edit regions, 8 diff hunks, animate_objects only)

EDIT A (~L6169-6227). Frame-1 Sun position computed before the animate shell
dispatch (positions_over_time['Sun'][0] when the Sun checkbox is on; else
fetch_position('10', dates_list[0], center_id) -- mirrors the static D2
wiring); threaded into create_planet_visualization along with an explicit
center_position=(0,0,0). Effect, verified on the LIVE dispatch in-container:
magnetosphere geometry rotates with sun_position (4 traces moved in the Earth
test), and the Sun Direction indicator now emits -- it was silently SUPPRESSED
before, because the default (0,0,0) sun equaled the center and read as "body
at Sun position". The orientation is frozen at frame 1; hover disclosure of
that freeze is deferred to the bow-shock sourced-vs-schematic disclosure
remainder (one sweep, same nature).

EDIT B (~L6824-6855). dynamic_trace_indices is now the sorted set of
trace_indices values past the static fence -- ONLY the traces the frame loop
updates (single-point object/barycenter markers). Orbit paths, idealized
orbits, trajectory layers, comet tails, and the center marker are no longer
deep-copied into every frame; their initial figure data stays live. to_frame_idx
is a dict lookup into the sparse frame list. New console line reports
frame-updated vs excluded counts.

EDIT C (~L7205-7212). The post-loop first-frame sync now maps through
to_frame_idx instead of subtracting static_trace_count -- mandatory once the
frame list is sparse; plain subtraction would misalign silently.

## Verification done (Claude-side)

- py_compile clean; ASCII-only; LF endings; diff confined to the 3 regions.
- xvfb startup test: full GUI initialization, no tracebacks (45 s).
- LIVE-dispatch smoke (Edit A): create_planet_visualization ->
  create_celestial_body_visualization -> CUSTOM_SHELLS Earth magnetosphere
  builder; geometry responds to sun_position; indicator emission confirmed.
- PATTERN-level test (Edits B+C): the new fence/mapping logic, replicated
  verbatim against a synthetic figure mirroring the live structure (12 shells,
  10 registered markers, 9 orbit paths x 366 pts, 60 frames). All assertions
  pass (exclusion, alignment, sync mapping). Indicative payload: 14.92 MB ->
  0.064 MB of frames JSON (99.6%). Synthetic number -- the real one comes from
  Tony's exports via measure_animation_html.py.
- NOT verified in-container: live frame construction end-to-end (Horizons is
  unreachable from the sandbox). That is exactly what ANIMATION_TEST_PROTOCOL
  Phase 0/1 covers, with baseline-vs-patched measurement.

## Ledger-ready updates (apply to LEDGER_orrery_consolidated.md)

- PENDING ACTION: both June-8 items are AT HEAD 730b2bf (center-dropdown dedup
  verified at L9296; CUSTOM_SHELLS single 'Sun' key verified by AST). Clear
  the pending-push block; 730b2bf is the round-tripped base.
- 21/51 Animation track: Phase 1 DELIVERED (frame fence + sun threading),
  render-gated on ANIMATION_TEST_PROTOCOL_v1. Objective (2) substantially
  addressed; objective (3) partially (center-body shells were already static;
  frame budget now near-empty). Objectives (1) and remaining (3): Phase 3
  design (tiers: static-at-frame-1 disclosed / small-primitive animation /
  reduced-resolution re-emission gated on 20/N5). Phase 2 consolidation
  design pending.
- NEW finding for the record: the v27 "rotation-axis/dipole-cone animation
  gap" is, per code reading, a NON-CENTER-body gap only -- center-body
  shells (and their body-triggered axis/cone) DO dispatch in animate.
  Protocol O4 confirms in render.
- NEW divergence items recorded for Phase 2: animate center-marker hover is
  bare (static uses INFO encyclopedia); comet tails frozen at frame-1
  position in animations; offset-Sun-shells branch absent in animate.
- NEW lesson (protocol candidate): the xvfb SystemButtonFace<->gray90 sed
  round trip is NOT idempotent on files that natively contain gray90 --
  palomas_orrery.py has 26 native gray90 literals, and the restore swap
  converted them to SystemButtonFace in the test copy. Run the swap on a
  THROWAWAY copy only; never restore-in-place on the deliverable. (Caught
  this session by a copy diff; deliverable unaffected.)

## Next session

- Tony: run ANIMATION_TEST_PROTOCOL_v1 (baseline FIRST, then patch), log
  O1-O6 observations, push, carry new SHA.
- Then: Phase 2 design conversation (scene-assembly consolidation; absorbs
  D.Structural 3 wrapper retirement) and Phase 3 tier decision, both seeded
  by the observation log.

Module updated: June 2026 with Anthropic's Claude Fable 5
