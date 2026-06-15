# Item 19.3 -- Phase 2 Test Protocol / Record (dtick + autorange)

Build base: `7aecc3b`  ->  Build SHAs: `bd768ee` (builder), `aa1a4cd` (call sites)
Files: `visualization_utils.py` (build_scene gains auto_dtick + axis_range=None
guard), `palomas_orrery.py` (S1/S2 call sites pass auto_dtick=True, autorange=False).
Scope: turn ON readable close-approach grids. The only additions to the scene
are dtick (auto-derived from the range span) and autorange=False, on the static
(plot_objects, S1) and animation (animate_objects, S2) main scenes.

Status: PASSED. Render gate signed off by Tony (Mode 5) at aa1a4cd.

---

## 0. Programmatic gates (Claude-side, passed)

- [x] `python3 -m py_compile palomas_orrery.py visualization_utils.py` -> clean
- [x] LF only (0 CRLF), ASCII only (0 non-ASCII), on pushed bytes
- [x] Builder smoke (ast-extracted from the pushed file):
      - default call still byte-identical to the legacy scene (Phase 1 invariant intact)
      - auto_dtick=True + autorange=False -> dtick from span on all 3 axes, base unchanged
      - Apophis-scale span 0.0008 AU -> dtick 0.0001 AU (~14,960 km gridlines), not dtick=1
      - axis_range=None -> neither dtick nor autorange emitted (Plotly auto-fits)
      - explicit dtick overrides auto_dtick

## 1. Render gate (Tony's eyes -- authoritative)

| # | Case | Expected | Result |
|---|------|----------|--------|
| 1 | Static close-approach (Arrokoth/New Horizons flyby, encounter scale) | Readable gridlines instead of an empty AU-scale cube | PASS |
| 2 | Non-tracking animation at close/non-Sun scale, played through | Grid spacing + range HOLD steady across frames (autorange=False suppresses per-frame autorange) | PASS -- held |
| 3 | Everyday Sun-centered full-system plot | Still looks right; explicit dtick (~6 clean gridlines) reads fine where Plotly auto-ticked before | PASS |

Case 2 was the load-bearing one. It held -- see the finding below.

## 2. What does NOT change (the contract)

Identical to before, on both S1 and S2: range (same axis_range), camera, domain,
aspectmode, axis titles/colors/grid/background, and the entire layout envelope
(title / legend / annotations / margin / paper_bgcolor). The ONLY additions are:
- dtick (auto-derived from the range span via the shared _calculate_grid_dtick)
- autorange=False

S3 (exoplanet, ~5996) and S4 (camera-track, _track_axis ~7652) are untouched.

Intended, visible behavior change: auto_dtick applies to ALL S1/S2 plots, so
full-system plots now carry an explicit dtick (uniform ~6 gridlines) rather than
Plotly's auto choice. Confirmed acceptable on normal plots (Case 3).

## 3. Finding -- the animation-hold result

Case 2 holding is a real result, not just a pass: it confirms that
**autorange=False on the up-front (once-set) non-tracking scene suppresses Plotly's
per-frame autorange** during playback. This is the "real fix (autorange suppression)"
named in the palomas_orrery.py June-13 note (~7847) -- now validated FOR THE
NON-TRACKING PATH. The grid/range no longer drift frame to frame.

Boundary (important): this does NOT resolve the camera-tracking (S4) per-frame
autorange residual. That path uses _track_axis with per-frame layout emission and
is untouched here. The non-tracking fix (this phase) and the tracking residual
(the June-13 dedicated-session item) are distinct problems; only the first is
closed.

## 4. Sign-off

- [x] Programmatic gates pass
- [x] Render gate cases 1-3 pass (Tony, Mode 5, aa1a4cd)
- [x] Animation-hold confirmed (autorange suppression works, non-tracking)

Item 19.3 Phase 1 (scene extraction) + Phase 2 (dtick + autorange) COMPLETE.

## 5. Cosmetic residuals (not failures)

- Trailing whitespace on palomas_orrery.py lines 5711 and 7927 (the two
  autorange=False lines). No functional effect; strip at convenience.
- MODULE_ATLAS.md lags: build_scene's auto_dtick parameter is not yet in the
  atlas. Regenerate (module_atlas.py) when convenient.

## 6. Remaining 19.3 fast-follow (not this phase)

- User-settable range/dtick GUI fields (orrery generation-time + Gallery Studio
  refinement) -- the full Studio-parity round trip.
- S3 exoplanet (5996) opt-in to build_scene / auto_dtick, with its own render gate.
