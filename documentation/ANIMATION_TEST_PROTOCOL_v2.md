# ANIMATION TEST PROTOCOL v2 -- 21/51 Through Phase 2

Tony Quintanilla, PE | Claude | June 10, 2026
Supersedes ANIMATION_TEST_PROTOCOL_v1 (Phase 1 gate -- PASSED, results below).
Phase 2 patch base: orrery repo HEAD 3f03c12 | Patched file: palomas_orrery.py
Companion tool: measure_animation_html.py (in repo)

PURPOSE. (1) Record the Phase-1 render confirmation so its numbers serve as
the regression baseline. (2) Gate Phase 2 (center-marker unification + shell
dispatch consolidation) in the live render, Mode 5. (3) Continue the
observation log that seeds the Phase-3 tier decision.

================================================================
PHASE 1 -- CONFIRMED (June 10, 2026, Mode 5 @7977a11) -- regression baseline
================================================================

Fixes: frame fence (frames carry only frame-updated traces), frame-1 sun
threading, first-frame sync mapping. Results on record:

  P1 Sun-centered, inner planets, no shells, 29 frames:
     4818 -> 271 KB (94.4%). Frame-updated 3; excluded 31. All visual checks
     passed (scrub, static orbits, first-frame sync, legend, hover).
  P2 Sun-centered + full corona set, 29 frames:
     5133 -> 593 KB (88.4%). Static shell traces 24. Shells static in playback.
  P3 Earth-centered, Moon + magnetosphere, 29 frames:
     Magnetotail anti-sunward at frame 1; Sun Direction indicator rendered for
     the first time in any animation; Moon animates around static shells.

Observation log v1 (O1-O6) recorded in HANDOFF_animation_phase1.md; outcomes
folded into the ledger (21/51 + D.Cosmetic + item 19).

These numbers are the BASELINE for Phase-2 regression: Phase 2 touches no
frame logic, so re-measured frame payloads must match Phase 1.

================================================================
PHASE 2 -- RENDER GATE (run against the June-10 Phase-2 palomas_orrery.py)
================================================================

What Phase 2 changed: ONE canonical center-body marker (the
add_celestial_object path, full hover) in both pipelines; explicit
center-marker blocks deleted; one sun-position producer; one center-shell
dispatch helper; one shell-vars map. Claude-side equivalence tests already
proved the shell dispatch is trace-for-trace identical -- the checks below
are the render-level confirmation plus the genuinely NEW pixels.

P2-1. STATIC: N3 single-marker check (the headline closure)
  Config: any shelled body (e.g. Earth) CHECKED in the menu + selected as
  CENTER + NO shells checked.
  [ ] Exactly ONE marker at origin (pre-patch this was the N3 double).
  [ ] Exactly ONE legend entry for the body.
  [ ] Hover on the marker: full formatter text (distance/velocity/period
      lines), not the old INFO one-liner.

P2-2. STATIC: Sun-centered, no shells
  [ ] Single Sun marker at origin; hover comes from the full formatter now
      (the old hover_text_sun block is gone). Content reads differently --
      judge whether it serves. If the old text is preferred, that is a
      formatter request, not a rollback.

P2-3. STATIC: shells-on regression
  Config: a known shells-on static plot (e.g. Earth center + magnetosphere).
  [ ] Render unchanged vs pre-patch (equivalence-tested; confirm by eye).
  [ ] Center marker present as always (object-loop mechanism, untouched).
  [ ] Auto scale still fits the outermost shell (static auto-scale is LIVE
      and now flows through the helper's returned axis_range).

P2-4. STATIC: osculating hover spot-check (params resolution)
  [ ] Hover a planet marker: orbital-period/element-derived lines now come
      from active (osculating) params. Differences from pre-patch will be
      subtle or nil; flag anything that looks WRONG rather than different.

P2-5. ANIMATE: center marker with shells ON (the O6a closure -- new pixels)
  Config: P3-style run (Earth center, magnetosphere, Moon, ~29 frames).
  [ ] Center marker NOW RENDERS at origin with shells on.
  [ ] Hover on it: full formatter text (the O5 closure).
  [ ] Marker is CONSTANT across frames (scrub: it never moves or flickers).
  [ ] Console: "Static shell traces (before fence)" is ONE HIGHER than the
      same config gave in Phase 1 (the marker now counts below the fence).
  [ ] Magnetotail + Sun Direction indicator unchanged from Phase 1 behavior.

P2-6. ANIMATE: center marker, no shells
  [ ] Marker renders (as before), but hover is now the full formatter text
      instead of the bare name / barycenter line.

P2-7. ANIMATE: barycenter center (transparency contract)
  Config: a barycenter-centered animation (e.g. Pluto-Charon Barycenter).
  [ ] Transparent center: NO legend entry for it (suppression preserved
      through the new wrapper); no stray visible marker.
  [ ] Hover behavior sane if the marker is reachable.

P2-8. ANIMATE: frame-payload regression (fence untouched)
  Re-run ONE Phase-1 measurement pair, same settings as P1:
    python measure_animation_html.py P1_phase1.html P1_phase2.html
  [ ] Frames payload and traces-carried-in-frames MATCH Phase 1 (within
      noise). File size may differ trivially (hover text changes).
  [ ] "Traces carried in frames" still lists ONLY moving bodies.

P2-9. ANIMATE: console line check (every run)
  [ ] "[ANIMATION] Added <body> shells (...)" still prints (now from the
      shared helper with the [ANIMATION] prefix).
  [ ] "[ANIMATION] Frame-updated traces: N; constant traces excluded: M"
      unchanged in form.

================================================================
OBSERVATION LOG v2 (continue numbering; seeds Phase 3)
================================================================

  O7. Center-marker hover content, both pipelines: the formatter shows
      "Distance to Center Surface: -<radius> km (below mean datum)" for the
      center body (object-at-distance-zero treatment). Pre-existing in
      static; animate now matches. Log whether it grates enough to promote
      the D.Cosmetic formatter-polish item.
  O8. Sun-center hover (static + animate): old text vs new full-formatter
      text -- note preference.
  O9. Anything that moved, flickered, re-ordered in the legend, or scaled
      differently vs Phase 1. Free-form; this is the ground truth Phase 3
      planning consumes.

================================================================
RECORD FOR THE LEDGER / NEXT HANDOFF
================================================================
- P2-1 through P2-9 pass/fail. On pass: move N3, O5, O6(a) to ledger
  section C; mark 21/51 Phase 2 render-confirmed.
- O7-O9 outcomes.
- New HEAD SHA after pushing.
- Open Tony calls queued for next session (ledger section G): animation
  Auto-scale-vs-shells decision; Phase 3 tier decision; optional Phase 2.5
  wrapper retirement.

Module updated: June 2026 with Anthropic's Claude Fable 5
