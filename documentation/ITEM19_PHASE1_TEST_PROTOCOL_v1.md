# Item 19.3 -- Phase 1 Test Protocol (Scene-Dict Extraction)

Build base: `6a64900`  ->  Build SHA: `7aecc3b`
Files: `visualization_utils.py` (+builder), `palomas_orrery.py` (S1/S2 call sites + import)
Scope: ZERO behavior change. This phase only moves the static (plot_objects) and
animation (animate_objects) main scene dicts behind a shared `build_scene()`.
No dtick, no autorange, no range change. Those are Phase 2.

The gate is simple: every render must look EXACTLY as it did at `6a64900`. The
extraction is byte-identical by construction; this protocol is the proof against
your eyes, which are the authority I can't reach.

---

## 0. Pre-flight (already verified Claude-side; re-runnable)

- [ ] `python3 -m py_compile palomas_orrery.py visualization_utils.py` -> no output
- [ ] No CRLF: `grep -c $'\r' visualization_utils.py palomas_orrery.py` -> 0 / 0
- [ ] No non-ASCII: `grep -cP '[^\x00-\x7F]' visualization_utils.py palomas_orrery.py` -> 0 / 0

These passed on the pushed bytes. Listed so the gate is self-contained.

## 1. Figure-level byte check (optional, stronger than the eye)

Proves the LIVE dispatch (the real `fig.update_layout(scene=...)` inside
plot_objects / animate_objects), not just the builder in isolation.

Use a FIXED date and a FIXED object selection so `axis_range` is deterministic
across runs (a "now" date recomputes positions and the range will differ run to
run -- that would be a false fail).

```python
# After generating the figure, in the same session:
import json
scene = fig.to_dict()['layout']['scene']
open('scene_AFTER.json', 'w').write(json.dumps(scene, indent=2, default=str, sort_keys=True))
```

Run once on `7aecc3b` (scene_AFTER) and once on `6a64900` (scene_BEFORE), same
date + same objects, then `diff scene_BEFORE.json scene_AFTER.json` -> empty.
Do this for one static plot and one animation. Empty diff = identical scene.

(If you would rather not check out the old commit, skip this -- Section 3 is the
authoritative gate and Section 4 is the contract it is checking.)

## 2. Console watch (every render)

- [ ] No new tracebacks, no new "caught error" prints around layout/scene.
  A swallowed exception is where a dropped marker hides; there should be none here.

## 3. Visual Mode-5 gate (your eyes -- authoritative)

Render each case at `7aecc3b`. If you have a `6a64900` render handy (saved HTML
or a screenshot), compare side by side; otherwise judge against memory of the
last-known-good. PASS = indistinguishable from before.

| # | Case | Path exercised | Watch for | Pass? |
|---|------|----------------|-----------|-------|
| 1 | Static, Sun-centered, scale = Auto, full inner system | S1 (plot_objects, MIGRATED) | X/Y/Z (AU) labels, gray grid on black backplanes, cube aspect, default camera, plot area in right ~80% (domain x=[0.2,1]) | [ ] | -- correct
| 2 | Static, planet-centered (e.g. Mars 499 + moons), Auto | S1 + non-Sun-center range (line 742, UNCHANGED) | tight box around the planet exactly as before; grid/camera/domain identical | [ ] | -- correct
| 3 | Static, close-approach (Apophis or a comet close-up) | S1, AU-scale-grid case | STILL unreadable AU grid -- this is CORRECT for Phase 1 (Phase 2 fixes it). Capture this as the Phase-2 "before". | [ ] | -- i plotted the Arrokoth New Horizons flyby using the Go button. then I tried to plot an animation of Mercury and Arrokoth keeps being included in the plot even through i de-selected it. 
| 4 | Animation, Sun-centered, camera = None (free) | S2 (animate_objects, MIGRATED) | frames play; axes/grid/camera/domain identical to before; no flicker introduced | [ ] |-- mercury orbit, correct. 
| 5 | Animation, camera tracking ON (e.g. a comet) | S4 `_track_axis` (NOT migrated) | unchanged -- tracking window, per-frame grid, dtick all behave as before | [ ] | -- correct 
| 6 | Exoplanet mode plot | S3 (5996, NOT migrated) | unchanged -- bare axes exactly as before | [ ] |

Cases 1, 2, 4 are the migrated paths (the actual test). Cases 3, 5, 6 are
regression sentinels for the paths we deliberately left alone.

## 4. What does NOT change (the contract)

Phase 1 must leave ALL of the following byte-for-byte identical to `6a64900`.

Per axis (x, y, z), in both the static and animation main scenes:
- `title`        = 'X (AU)' / 'Y (AU)' / 'Z (AU)'
- `range`        = axis_range  (SAME value -- the range computation is untouched)
- `backgroundcolor` = 'black'
- `gridcolor`    = 'gray'
- `showbackground` = True
- `showgrid`     = True
- `dtick`        -> ABSENT (still no key; Phase 2 adds it)
- `autorange`    -> ABSENT (still no key; Phase 2 adds it)

Per scene:
- `aspectmode`   = 'cube'
- `camera`       = get_default_camera()  (same object)
- `domain`       = dict(x=[0.2, 1.0], y=[0.0, 1.0])  (same)

Outside the scene (the whole layout envelope stays inline at the call site,
untouched): title text, paper_bgcolor / plot_bgcolor = 'black', font colors,
showlegend, legend block, margin, annotations.

Code paths NOT migrated and therefore unchanged:
- S3 exoplanet scene (`palomas_orrery.py` ~5996)
- S4 camera-track scene (`_track_axis` ~7652)
- `axis_range` producers: get_improved_axis_range / get_animation_axis_range /
  calculate_axis_range_from_orbits

Behavior unchanged: same traces, same data, same hover text, same buttons,
same camera behavior, same animation frames, same scale modes (Auto / custom).

## 5. Sign-off

- [ ] Cases 1-6 all PASS (indistinguishable from before)
- [ ] No new console errors
- [ ] (optional) Section 1 scene diffs empty

On sign-off: Phase 1 holds. Phase 2 is then a one-arg flip in `build_scene`
(`dtick=_calculate_grid_dtick(axis_range[1]-axis_range[0])`, `autorange=False`)
applied to the S1/S2 call sites.

## 6. Known cosmetic deltas (not failures)

- Duplicate `_calculate_grid_dtick()` line in the `visualization_utils.py`
  Key-functions docstring (insertion artifact). Docstring only, no functional
  effect, does not reach the atlas. Remove the extra line with Phase 2.
- A few blank-line / trailing-whitespace differences around the S1/S2 call
  sites vs. the original. No effect.

## 7. What Phase 1 does NOT do (by design)

- Does NOT make close-approach plots readable. The AU-scale grid on Case 3 is
  expected to still be unreadable -- that is the Phase-2 fix. Capturing it now
  gives Phase 2 a clean before/after.
- Phase-2 watch item (capture now so it does not float): the animation main
  scene (S2) is set ONCE up front, not per frame. The track path learned that
  per-frame 3D layouts drop dtick/aspectmode unless the COMPLETE spec is
  re-emitted every frame (the ~7587 comment). For the non-tracking animation,
  frames should not be overriding the scene, so a single up-front dtick should
  hold -- but the animation render gate (Case 4 with dtick ON) is the one to
  watch in Phase 2. First Phase-2 step: confirm non-tracking frames carry no
  per-frame scene layout.
