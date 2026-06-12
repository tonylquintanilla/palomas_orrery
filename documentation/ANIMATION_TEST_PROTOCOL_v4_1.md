# ANIMATION TEST PROTOCOL v4.1 -- Fix Pass C2 Retest

Tony Quintanilla, PE | Claude | June 11, 2026
Scope: the focused retest of the three v4 blockers. v4 items that PASSED
(C1, C3, C5, C7; C4 with caveat; C6a) are NOT re-run except where listed
under regression. Patch base: orrery repo HEAD d05f0f1 | Patched (2 files):
palomas_orrery.py, planet_visualization.py.

THE THREE FIXES (root causes in HANDOFF_animation_phase3C2.md)
1. C2a doubling: frame-1 comet block skips engine-owned comets.
2. C2b/C2c sticky visible: explicit visibility on every frame-slot write
   (Plotly frame updates are MERGES; omitted properties inherit slot
   history -- a dummied slot never revived).
3. C6d: center-body sun-direction elements join the engine
   (get_center_engine_elements = single source of truth; the dispatch
   skips exactly that set via skip_elements; static pipeline untouched,
   regression-tested HEAD-identical).

================================================================
RETEST GATE
================================================================

R1. Ikeya-Seki perihelion rerun (same config as v4 C2: opt-in checked,
    hourly frames from 10/20/1965 04:24)
  [ ] NO doubled nucleus / Sun Direction / legend entries (C2a).
  [ ] Tail PRESENT at perihelion, matching the static render's character
      (C2b) -- coma/tails APPEAR as thresholds cross and persist while
      active.
  [ ] Sun Direction indicator present and tracking through 18:24 and
      beyond (C2c). NOTE: near perihelion the indicator's LENGTH scales
      with distance/20 and becomes legitimately tiny -- builder behavior,
      identical in static; judge presence, not size.
  [ ] Console: "frame-1 static tails skipped (engine owns them)" line.
  [ ] Opt-in UNCHECKED rerun: frame-1 tails only, no skip line, no
      doubles (the skip must not fire).
  [ ] File size: report (expect a drop vs the 2426 KB doubled run).

R2. Mercury-centered Sun tracking (v4 C6d config: Mercury center, sodium
    tail checked, Sun checkbox off)
  [ ] Console: Sun-trajectory fetch line appears.
  [ ] Sodium tail SWINGS anti-sunward across frames as the Sun moves
      around Mercury.
  [ ] Sun Direction indicator tracks the moving Sun from the origin.
  [ ] NO doubled sodium/indicator (the dispatch skipped them; legend
      shows ONE of each).
  [ ] Mercury's rotation axis: STATIC (inertial -- frozen is correct).
  [ ] Rerun with Sun checkbox ON: same behavior (resolution uses the
      checked trajectory).

R3. Regression spot-checks
  [ ] One STATIC Mercury-centered plot, sodium checked: renders exactly
      as before (skip_elements is animate-only; T5 proved HEAD-identical,
      confirm by eye).
  [ ] One B1-style Uranus run: riding primitives unchanged; no engine
      element vanishes after any frame (the missing-position branch now
      writes explicit dummies -- if a body's position gaps, expect the
      new console NOTE naming the body and frame).
  [ ] MAPS animation, opt-in checked: MAPS frame-1 tails still render
      (the skip excludes MAPS).

================================================================
OBSERVATIONS (continue numbering)
================================================================
  O18. Perihelion render quality with per-frame tails working (the C2
       headline, finally visible).
  O19. Center-body sodium/indicator motion: educational read.
  O20. Free-form.

On pass: record results in the 3C handoff, push, and the Phase 3 core
track (A/B/C + fix pass) CLOSES. The ledger's render-gated markers move
to section C.

Module updated: June 2026 with Anthropic's Claude Fable 5
