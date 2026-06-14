# HANDOFF -- Phase 4 Animation Render-Gate Session

Tony Quintanilla, PE | Claude (Fable 5) | June 13, 2026

Built on: `a69c3a7` (a69c3a79466e5e3f02589eaee13031800d08be73), branch `main`.
Ledger: see `LEDGER_orrery_consolidated.md` (updated in place this session --
camera tracking, O13b, Gate 5(b), reticle). This handoff is the session
narrative; the ledger carries the open items.

## What this session was

A render-gate cycle on the Phase 4 animation work. Phase 4 had landed the
per-frame engine, camera tracking, d7 coordinate rounding, and element
extents; this session drove the camera-tracking feature through Tony's
Mode-5 visual gate and fixed what the render exposed. Five fixes, each
render-confirmed on live Mercury data, all now in HEAD.

## The arc (in the order it unfolded)

1. **Grid fix (per-frame complete axis spec).** The tracked-animation grid
   flickered -- present at the initial view and the final settle frame,
   absent mid-animation. Cause: `_track_frame_layout` set `range` only, and
   Plotly applies a frame's layout as a MERGE, so dtick / aspectmode / grid
   styling were left to inheritance and not reliably reapplied per frame
   (the same merge hazard as the C2 trace-visibility fix, one layer up in
   layout). Fix: every frame now emits the COMPLETE axis spec
   (range + dtick + autorange-off + grid styling + aspectmode).

2. **Element-extent window sizing (O13b).** Tony's call: size the tracking
   AND Fly To window to the LARGEST ACTIVE element's measured extent, not a
   body-radius multiple. Architecture: one shared producer
   `traces_extent_from_center()` (shared_utilities); the static dispatch
   records `fig._body_element_extent_au` per body, the per-frame allocator
   records `_perframe_body_extent`; both the tracker and
   `add_fly_to_object_buttons` (new `target_extents` param) consume it.
   Measured to the decimal against the real Mercury builders: magnetosphere
   alone -> 0.0008 AU window; sodium tail on -> 0.196 AU (holds the whole
   10,003-radii tail the old fixed window cut at 83x); largest wins. The
   empty-box Fly To is gone.

3. **Live JS relayout (the core fix).** Sun-centered tracking of distant
   Mercury with the sodium tail OFF failed: a tiny 0.0045 AU cube sitting
   0.42 AU from origin -- Plotly silently DROPS a per-frame 3D scene range
   carried in `frame.layout` at that small window/offset ratio and
   autoranges the whole Sun-Mercury span (swung to ~0.4 AU, non-uniform,
   body off-center and effectively invisible). The frame JSON was confirmed
   correct (equal ranges, autorange:false, aspectmode:cube all present) --
   the drop is Plotly's, not ours. FIX:
   `save_utils._inject_camera_tracking` injects a `post_script` that applies
   the body-centered window with `Plotly.relayout` on load (centers the
   body) and on every `plotly_animatingframe` (holds the window). Data is
   stashed as `fig._track_relayout_data` keyed by frame date; injection
   routes through `_write_html` (the same chokepoint the encyclopedia
   overlay uses), so it reaches both the browser-opened and the saved
   offline file. The `frame.layout` path is kept as a no-JS fallback; the
   relayout runs after the frame and wins. This is the JS event-based
   follow-on the prior ledger RESIDUAL had parked -- now built.

4. **Center reticle suppression.** The teal `<>` center marker is a
   hand-aligned screen-space paper-coord annotation borrowed from the star
   visualizations -- it marks roughly where the center object APPEARS, not
   the data center, so it was never pixel-exact. At shell-scale tracking the
   eyeball error shows and there is one body to look at, nothing to
   disambiguate. Suppressed under tracking via
   `add_look_at_object_buttons(show_target_marker=_track_body is None)`;
   kept in all non-tracking and static views.

5. **Hyperbolic osculating `color` fix.** `idealized_orbits.py:7076` used an
   undefined `color`; the info-marker now uses `color='white'` (matches the
   white dotted hyperbolic line). Fired on Earth-centric hyperbolic MAPS.

## Render-gate results (Tony, Mode 5, live Mercury)

- Mercury-centered, all shells, magnetosphere animated, free camera:
  everything tracks the Sun, rotation axis stays inertial, all shells
  render, reticle suppressed, plots correctly.
- Sun-centered, track Mercury, all shells: camera follows Mercury, focus
  steady, sun-oriented shells track the Sun. Saved file identical to live.
- Saved-file round trip: opening saved tracking animations behaves exactly
  as the original render (relayout fires offline).

## Residuals / next

- **Cube-size wobble under tracking (open, judged acceptable).** With the JS
  relayout layered over the retained `frame.layout` path, the cube SIZE
  varies frame-to-frame (~0.15-0.55 AU, non-uniform); the two mechanisms
  don't perfectly agree. CENTERING is steady and Tony judged it visually
  fine. Clean removal: drop the scene from `frame.layout` so JS owns the
  window outright (one mechanism, likely uniform cube). Render-gated
  follow-up; not blocking.
- **MAPS per-frame wiring** remains DEFERRED (ADDENDUM_phase4 decision 1).
- **O2/O3 console-notice wording** slightly stale when magnetosphere opt-in
  is ON -- amend on next touch (per ledger Phase 4 residuals).

## Files touched (all in HEAD a69c3a7 except where noted)

- `palomas_orrery.py` -- grid fix, extent producer + tracker consumer,
  `fig._track_relayout_data` build, reticle suppression call.
- `save_utils.py` -- `_inject_camera_tracking` + call in `_write_html`.
- `visualization_utils.py` -- `add_look_at_object_buttons` gains
  `show_target_marker`; `add_fly_to_object_buttons` gains `target_extents`.
- `planet_visualization.py` -- dispatch records `_body_element_extent_au`.
- `shared_utilities.py` -- `traces_extent_from_center()` helper.
- `idealized_orbits.py` -- hyperbolic osculating `color` fix.

## Lessons (for the archive)

- **Per-frame 3D scene relayout via `frame.layout` is unreliable below a
  window/offset ratio.** Plotly drops the range and autoranges; the emitted
  JSON can be perfectly correct while the render is wrong. The reliable path
  is `Plotly.relayout` on `plotly_animatingframe`, injected via the
  `_write_html` chokepoint (reaches shown AND saved HTML).
- **The render splits cleanly when you size to physics.** Window = largest
  active element's MEASURED extent (one producer, both pipelines) made the
  too-loose Fly To and the too-tight tracker the same fix.
- **A hand-eyeballed screen-space marker degrades at scale.** The reticle
  was fine at AU scale and wrong at shell scale; suppress where the error
  shows rather than chase pixel alignment on a paper-coord annotation.
