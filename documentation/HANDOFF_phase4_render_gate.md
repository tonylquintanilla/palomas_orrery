# HANDOFF -- Phase 4 Animation Render-Gate Session

Tony Quintanilla, PE | Claude (Fable 5) | June 13, 2026

Built on: `a69c3a7`; this session's work pushed through `33aac56`
(reticle + docs) -> `373298d` (item-1 attempt) -> item-1 REVERTED (restore
`frame.layout`). Confirmed-good base for the NEXT session is the post-revert
HEAD. Branch `main`.
Ledger: see `LEDGER_orrery_consolidated.md` (updated in place this session --
camera tracking, O13b, Gate 5(b), reticle, the dipole set, the roadmap, and
the corrected item-1 status). This handoff is the session narrative; the
ledger carries the open items.

## What this session was

A render-gate cycle on the Phase 4 animation work. Phase 4 had landed the
per-frame engine, camera tracking, d7 coordinate rounding, and element
extents; this session drove the camera-tracking feature through Tony's
Mode-5 visual gate and fixed what the render exposed. Five fixes, each
render-confirmed on live Mercury data, all landed. The session then continued
into a roadmap re-assessment, a corrected consolidation claim, the verified
dipole set, and an item-1 cube-cleanup attempt that the render falsified and
that was reverted (all below).

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

## Cube-size wobble: item 1 attempted, RENDER-FALSIFIED, REVERTED

The one residual from the render-gate fixes was the cube SIZE wobbling under
tracking (~0.15-0.65 AU, differs by axis) while CENTERING stayed steady.
Hypothesis: the JS relayout layered over the retained `frame.layout` path,
the two disagreeing per frame. Item 1 acted on that -- dropped the scene from
`frame.layout` so frames carry DATA ONLY and the JS relayout owns the window
outright.

The render falsified it. With `frame.layout` gone the cube STILL differed by
axis and swung ~0.15-0.65 -- essentially unchanged. So the two-mechanism
conflict was NOT the cause. Item 1 was pushed (`373298d`) then REVERTED:
it fixed nothing and cost the large-window partial-hold plus the no-JS
fallback, so the pre-item-1 behavior is the better baseline.

REFINED DIAGNOSIS (next-session seed, NOT verified in-container -- no browser
here): Plotly re-autoranges the 3D scene per frame when frames carry data
without an explicit range, overriding the JS relayout. The cube differs by
axis because autorange fits the asymmetric sodium tail per axis, and swings
as the tail rotates. SUPPORTING EVIDENCE from the console: track half-width
is 0.19612 AU (relayout target ~0.39 cube), but the swing's upper bound
(~0.65) matches the static auto-scale "Final axis range: +/-0.606714 AU" --
the full-orbit autorange. The scene is drifting toward the data-extent
autorange and away from the element-sized window the relayout sets.

This is COSMETIC. Centering, shell-tracking, the saved round trip, and the
reticle are all render-confirmed; Tony judged the size wobble "not a visual
problem." Won't-fix (accept the wobble) is a legitimate close if Plotly's
per-frame autorange cannot be cleanly suppressed during 3D frame animation.

## Consolidation status (corrected this session)

A stale claim was made and corrected mid-session: the
`plot_objects`/`animate_objects` consolidation is NOT all deferred. The shell
consolidation AND the Phase 2 scene-assembly consolidation both landed --
both pipelines route through shared chokepoints (`create_celestial_body_
visualization`, `add_center_body_shells`, `add_center_body_marker`,
`add_celestial_sphere_traces`), and the center-body-marker divergence that
Phase 1 deferred is RESOLVED (`add_center_body_marker` is "the ONE mechanism,
both pipelines", closing O6a/O5; Fable 5 found the root cause -- the static
path had TWO center-marker mechanisms). What remains UN-merged: the two
top-level functions are still separate (`plot_objects` ~1,760 lines,
`animate_objects` ~1,700) -- the full Rings 1-3 function merge was never
executed. Their setup / trace-building / layout / finalization are still
hand-maintained in parallel, which is where silent drift can still grow.

## Verified dipole-cone set (Tony asked it be on record)

Queried live `CUSTOM_SHELLS`: the dipole_cone exists on Uranus + Neptune
(done -- the dramatically tilted/offset dipoles). Magnetized bodies still
WITHOUT a cone, that have a real global dipole: Earth, Jupiter, Mercury
(Tony's named set) plus Saturn (MARGINAL -- dipole <1 deg from the spin axis,
near-degenerate cone). EXCLUDED on physics: Mars (crustal fields, no global
dipole) and Venus (induced magnetosphere, no internal dynamo). PROVENANCE
GATE: all dipole tilts are currently RECALLED and MUST be sourced before any
`PLANET_DIPOLE` entry (Fetched-vs-Recalled) -- show the envelope, cite the
tilt.

## Roadmap (Tony's calls this session)

Active batch is items 1/3/5. (1) cube cleanup -- attempted, render-falsified,
reverted (above); the real fix is deferred. (3) **3D axis control (dtick +
range)** in the orrery GUI + Gallery Studio -- the NEXT WARM ITEM; machinery
is hot now (`_calculate_grid_dtick`, `traces_extent_from_center`,
auto-sizing), critical for flyby/close-approach plots where geometry is
orders of magnitude below AU-scale axes, valuable for Mode 5. (5)
palate-cleansers: near-parabolic apoapsis false-precision (Envelope
candidate), stale O2/O3 console wording, 4 `apsidal_markers.py` em-dashes,
and the remaining dipole cones (set above, provenance-gated). DEDICATED
separate session (NOT a cleanup folder): the `plot_objects`/`animate_objects`
DIVERGENCE AUDIT -- map both pipelines side by side, three-bucket catalog
(shared / intentionally divergent / accidentally divergent = drift), optional
parity smoke test; map-first-decide-second. The FULL function merge stays OFF
the list (chokepoints earned most of its value; high blast radius). RESERVE:
IPC food-insecurity build (API key not yet arrived, Tony waiting a few days)
and the Gallery/Studio track (ledger section H) as the mission-flavored
option if IPC keeps waiting.

## Next session

- Start from the post-revert HEAD (`frame.layout` restored). SHA round-trip
  first as always.
- WARM ITEM: 3D axis control (dtick + range), item 3. Machinery is hot.
- Cube uniformity, if pursued: build a repro that ACTUALLY RUNS in Tony's
  browser (the two prior repros did not), use it to confirm the autorange
  hypothesis, then either suppress autorange per frame or close won't-fix.
  Centering already works, so this is polish.
- Standing deferred: MAPS per-frame wiring (ADDENDUM_phase4 decision 1);
  O2/O3 console wording; the divergence audit as its own session.

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
- **A plausible cleanup is still a claim until the render confirms it.**
  Item 1 (drop `frame.layout`, "one mechanism, uniform cube") compiled
  clean, launched clean, read as obviously-correct architecture -- and the
  render falsified it in one run. The gate caught it; the code was reverted.
  "Cleaner architecture" that removes a partially-working constraint and a
  fallback is not cleaner if it buys nothing.
- **`frame.layout` 3D scene ranges behave scale-dependently.** Plotly honors
  an explicit per-frame range for a roomy window but DROPS it for a tiny
  window far from origin (autoranges instead). That is why the tiny case
  needed the JS relayout and the large case did not -- and why removing
  `frame.layout` hurt the large case. The real adversary for cube uniformity
  is per-frame autorange, not the two mechanisms disagreeing.
- **The SHA round trip earns its keep mid-session.** HEAD moved twice between
  turns (`33aac56` then `373298d`); the round-trip check caught each push
  before building, so edits landed on the live bytes, and it surfaced that
  item 1 had been pushed (making "roll it back" a real code action, not a
  no-op).
