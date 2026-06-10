# HANDOFF -- Animation Refactor 21/51, Phase 2 (June 10, 2026)

Built on: orrery repo HEAD 3f03c122d85dc4bbeccf69d74faeb5893c914152 (verified
via git ls-remote at session start; matches the SHA Tony supplied; Phase 1
edits confirmed present at this base).
Deliverables: palomas_orrery.py (patched), phase2_diff.txt (review diff vs
HEAD). No other files touched.

Implements the four approved steps (2a-2d) from the June-10 design decisions,
including the params-flag resolution. All decision points honored: canon =
add_celestial_object; helpers in-file near add_celestial_object; offset-Sun
and non-center shells untouched (Phase 3 fence).

## What changed (10 diff hunks, net -36 lines: ~210 duplicated lines removed,
~174 helper lines added)

NEW HELPERS (inserted after add_celestial_object, ~L1862-2035):
- get_planet_shell_vars_map() [2d] -- replaces THREE per-pipeline dict copies
  (planet_shells_config + planet_shell_vars in static, animation_shell_config
  in animate). New shelled bodies are added once, here.
- resolve_shell_sun_position() [2b] -- the one sun-position producer.
  Static passes positions.get('Sun'); animate passes the frame-1 entry.
  Fallback Horizons fetch when the Sun checkbox is off, as before.
- add_center_body_marker() [2a] -- the canonical center marker. Routes
  through add_celestial_object (full hover, RA/Dec, CENTER_MARKER_SIZE);
  transparent center colors suppress the legend entry (preserves the old
  explicit-block barycenter behavior).
- add_center_body_shells() [2c] -- the one center-shell dispatch (Sun branch
  + belts + planet branch + Auto shell scaling). log_prefix parameterizes
  the console tag: '' (static, silent as before), '[ANIMATION] ' (animate,
  matching the test-protocol console lines).

SIGNATURE EXTENSION (~L1786-1858): add_celestial_object gains optional
params=None (osculating elements for hover; defaults to module
planetary_params -- behavior-preserving for any external caller) and
show_legend=True. The ONE existing call site (static object loop, ~L5064)
now passes params=active_planetary_params -- so ALL static markers' hover,
center included, now uses fresh osculating elements (the params-flag
resolution; previously they silently used the stale module dict).

STATIC plot_objects:
- Dispatch region (~4663-4684): sun-position block + Sun/planet shell
  branches collapse to resolve_shell_sun_position + add_center_body_shells.
  _sun_pos_tuple keeps its name (the comet-tails section reuses it).
  axis_range return is LIVE here (Auto shell scaling preserved).
- Explicit center-marker block DELETED (~4686, breadcrumb comment left).
  The object loop is the static canon. ** This kills ledger N3 ** (two
  origin markers when body checked + centered + no shells).

ANIMATE animate_objects:
- Phase-1 sun-position block (~6211) collapses to resolve_shell_sun_position
  (same semantics, one producer). Phase 1's frame-fence and first-frame-sync
  edits are UNTOUCHED (verified intact post-edit).
- Dispatch (~6229) collapses to add_center_body_shells. The returned
  axis_range is intentionally UNUSED and annotated: get_animation_axis_range
  recomputes it unconditionally downstream, so the shell auto-scale was
  ALREADY dead in animate (new ledger note below). Behavior preserved, not
  silently fixed.
- add_center_body_marker call placed BEFORE the fence (~6239), unconditional.
  ** This kills O6(a) ** (no center marker with shells on) ** and O5 **
  (bare hover) -- animate's center marker is now pixel-identical in
  mechanism to static's.
- Explicit center-marker block DELETED; animation_shell_config DELETED.

## Verification done (Claude-side)

- py_compile clean; ASCII-only; LF; 10 hunks all in intended regions;
  Phase-1 fence + sync code verified intact.
- FULL module execution under xvfb (GUI built end-to-end, mainloop
  suppressed, clean shutdown) -- this is the startup test and more.
- LIVE-DISPATCH tests inside the real module namespace (real tk vars, real
  builders; only the two network calls patched):
  T1 shared map: 12 bodies, live tk.IntVars.
  T2 sun producer: Sun-center, passthrough, and fetch-fallback branches.
  T3 EQUIVALENCE: add_center_body_shells output is trace-for-trace
     IDENTICAL (names + coordinates) to the direct create_planet_visualization
     call it replaced (Earth + magnetosphere, 16 traces); Auto axis_range
     returned correctly.
  T4 Sun-center branch: sphere shell + main belt dispatch (10 traces).
  T5 center marker: origin, CENTER_MARKER_SIZE, full 359-char hover (not
     bare name), transparency suppresses legend.
- The sed display swap ran on a THROWAWAY copy only (Phase-1 lesson applied);
  the deliverable was never sed-touched.
- NOT verifiable in-container: live RA/Dec fetch inside the marker hover and
  full animation runs (Horizons unreachable). Mode-5 checklist below.

## Mode-5 checklist (Phase 2 render gate)

Static:
  [ ] Body checked + centered + NO shells: exactly ONE origin marker
      (N3 was the double -- confirm it is gone; legend shows one entry).
  [ ] Center marker hover unchanged from what you know (object-loop render).
  [ ] Sun-centered, no shells: single Sun marker, hover from the full
      formatter (the old hover_text_sun block is gone -- content may read
      slightly differently; judge).
  [ ] One shells-on static plot: unchanged vs pre-patch (T3 equivalence
      says identical; confirm by eye).
Animate:
  [ ] P3-style run (Earth center, magnetosphere, Moon): center marker NOW
      RENDERS with shells on (new pixels -- the O6a fix), full hover on it.
  [ ] Marker is constant across frames (not in trace_indices; console
      "Static shell traces" count includes it now -- one higher than before).
  [ ] Re-run one P1-style measurement: frames payload unchanged from
      Phase 1 numbers (fence untouched).
  [ ] Barycenter-centered animation (e.g. Pluto-Charon): transparent center
      suppresses the legend entry, marker behavior sane.
Cosmetic observation (pre-existing, now visible in animate too): the center
marker's hover includes "Distance to Center Surface: -6378 km (below mean
datum)" style lines -- the formatter treats the center like any object at
distance 0. Static has always shown this; animate now matches. If it grates,
it is a formatter polish item (ledger candidate), not a Phase 2 defect.

## Ledger-ready updates

- CLOSE (render-gated on the checklist above): N3 (center-marker edge case,
  double origin markers) -- root cause was two mechanisms; second mechanism
  removed. O5 and O6(a) (from the Phase-1 observation log) -- animate now
  uses the canonical marker.
- D.Structural 5 (_info import cleanup): hover_text_sun import (L208) is now
  UNUSED (its only consumer was the deleted static explicit block). Joins
  the existing import-cleanup sweep; deliberately not removed solo.
- NEW note (animate scaling): the shell auto-scale (axis_range from
  _shell_outermost_radius_au) is DEAD in animate -- get_animation_axis_range
  unconditionally recomputes axis_range downstream and does not read the
  shell radius. Pre-existing (Tony's P2/P3 render-approved the current
  scaling); now annotated at the call site. DECISION FOR LATER: should
  animation Auto scale consider shell extent? If yes, it is a one-line use
  of the helper's returned axis_range, gated on Mode-5.
- NEW cosmetic candidate: center-body hover "distance to own surface"
  lines (formatter treats center as object-at-zero). Pre-existing in static.
- 21/51: Phase 2 (2a-2d) DELIVERED, render-gated. Remaining in track:
  Phase 3 (non-center/offset-Sun/moving shells -- tier decision pending) and
  the comet-tail opt-in mode. D.Structural 3 (create_planet_visualization
  wrapper retirement) is NOT yet absorbed: the wrapper is still the live
  planet-branch entry inside add_center_body_shells; retiring it is now a
  ONE-SITE change (swap to create_celestial_body_visualization with
  center_object threading) -- a clean Phase 2.5 or Phase 3 rider.

## Next session

- Tony: run the Mode-5 checklist, push, carry the new SHA, apply ledger
  updates.
- Then: Phase 3 tier decision (the three-tier design from the Phase-1
  handoff), and optionally the wrapper-retirement rider (D.Structural 3).

Module updated: June 2026 with Anthropic's Claude Fable 5
