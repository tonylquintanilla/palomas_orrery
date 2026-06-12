# HANDOFF -- Animation Phase 4: Per-Frame Magnetospheres, Camera Tracking, Rounding

Tony Quintanilla, PE | Claude Fable 5 | June 12, 2026
Built on: fa8f3502f5e969f9c85dfdec7019b2981ab3779a (brief + addendum at HEAD)
Scope authority: HANDOFF_animation_phase4_brief.md + ADDENDUM_phase4_decisions.md
Status: IMPLEMENTED, container-verified (compile + GUI launch + live-dispatch
smoke, all green). Awaiting Tony's Mode-5 render gate (list in ledger sec G).

## What shipped (decision order -- measurement gated parameters, per decision 3)

1. MEASUREMENT FIRST (decision 3). Reproduced the brief's baselines
   (Earth FULL 144.8 KB/f, REDUCED 61.9 -- within noise of 146.4/62.4),
   then measured the rounding lever live:

   | Variant                          | un-rounded | d7-rounded |
   |----------------------------------|-----------:|-----------:|
   | Earth magnetosphere FULL         | 133.4 KB/f |  67.9 KB/f |
   | Earth REDUCED (40x3, 15x15)      |  57.8      |  30.5      |
   | Jupiter magnetosphere FULL       |  79.0      |  42.7      |
   | Mercury sodium tail (500)        |  46.3      |  31.1      |
   | Same Earth geometry at 19.2 AU   | 124.5      |  70.4      |

   DECIMAL places (not significant digits) are the scale-safe form: the
   19.2-AU row proves local geometry keeps ~15 km resolution at any
   heliocentric distance. d7 chosen over d6 (10x finer for ~3 KB/f).
   CONSEQUENCES: full resolution ships (no density reduction needed --
   per-body sweep closed as not-needed in the ledger); Jupiter needs no
   special case (amendment B vindicated); all 8 magnetospheres measured
   engine-compatible with STABLE trace counts (4-12 traces each).

2. ROUNDING AT THE CHOKEPOINT. PERFRAME_COORD_DECIMALS = 7;
   _round_perframe_coords applied inside build_perframe_traces, so the
   allocation, the max-probe, the rebuild loop, AND the 150 KB/frame
   guardrail all see rounded bytes. Every engine element inherits it
   (comet tails, sodium, axes, cones, indicator) -- one producer.
   Invisible dummy slots (x=[None]) are skipped byte-exact; None gap
   separators in line traces serialize as null either way.

3. PER-FRAME MAGNETOSPHERES (opt-in). All 8 CUSTOM_SHELLS magnetosphere
   entries tagged per_frame + per_frame_opt_in (transactional binary
   patch, anchors asserted unique). _perframe_optin_active gates ALL
   THREE per_frame consumers identically -- get_center_engine_elements,
   collect_perframe_elements, and _engine_animates in the legend
   placeholders. The third was found by grep, not the brief: without it,
   a checked magnetosphere with the box OFF would vanish from legend AND
   render (the exact silent absence the placeholders exist to prevent).
   Center bodies: opt-in ON -> engine owns it (skip set), tail tracks
   the moving Sun; OFF -> static dispatch, frozen frame-1 (status quo).
   Non-center bodies: ON -> engine renders + animates (the engine IS the
   render path; static non-center shells still don't render in animate);
   OFF -> placeholder, honest no-op.

4. CAMERA TRACKING -- range-tracking, not camera-flying. Frames carry
   per-frame SCENE RANGES centered on the tracked body
   (go.Frame(layout=...)); the camera eye is never touched, so the user
   can ORBIT during playback (the track+orbit conflict the brief feared
   largely dissolves). This is the house pattern: the existing Fly To
   buttons zoom by moving ranges inside the AU cube, which also retires
   the addendum-D precision/clipping risk by construction. Window
   sizing: shells checked -> 120x body radius (frames the ~100-radii
   magnetotail with margin; ledger O13b partial); otherwise the existing
   Fly To distance formula. Initial view set to the frame-1 window with
   a _calculate_grid_dtick grid, placed AFTER all other layout calls.
   redraw=True was already set in the animate args (required for frame
   layouts to apply). RESIDUAL: frame-driven ranges stomp manual ZOOM
   during playback; JS event-based follow-on parked (addendum C).

5. UI: "Per-frame elements (rebuild each frame)" LabelFrame in the
   animation settings (decision 2): comet-tails checkbox moved in
   unchanged (same var, same default), new "Animate magnetospheres"
   checkbox (default OFF), new "Camera: track body across frames"
   combobox (default None). Tooltips explain physics + byte cost.

6. O12 INDICATOR CLAMP. create_sun_direction_indicator computes the
   ray-cube exit along the sun direction (0.95 margin; min_scale floor
   wins -- a short clipping arrow beats an invisible one). Threading:
   static dispatch passes axis_range for MANUAL scales only (Auto
   widens to 2x shell extent AFTER the dispatch runs -- clamping against
   the incoming range would over-clamp); the engine threads a
   collect-time _animate_axis_range_hint into BOTH indicator specs (the
   animate pipeline's orbital-derived Auto range can undercut the
   shell-scaled length -- the actual O12 mechanism). No-range path
   byte-identical (smoke-asserted).

7. RIDERS. (a) Epoch parser: apsidal_markers chain gained
   '%Y-%m-%d %H:%M'; the brief's "verify the four palomas_orrery sites"
   found they were WORSE than noisy -- silent J2000 fallback on every
   HH:MM epoch (wrong positions, no console trace). All four now route
   through _parse_osc_epoch with a loud [EPOCH] note. (b) O20b
   disclosure: _append_inertial_note appends "orientation fixed across
   frames (inertial -- correct physics)" to rotation-axis and
   dipole-cone hover text in animations (Envelope house style: say WHY
   it doesn't move, next to elements that do); animate=True threaded
   add_center_body_shells -> dispatch. (c) create_magnetosphere_shape
   n-params promoted, defaults byte-identical (20/N5 backend).

## Files changed (6; +416/-68)

- palomas_orrery.py -- helpers (_parse_osc_epoch, _round_perframe_coords,
  _perframe_optin_active, _animate_axis_range_hint); opt-in gates x3;
  range hints; rounding wired; tracking setup + frame layouts + initial
  view; UI group; animate=True + axis_range threading at
  add_center_body_shells; 4 epoch sites.
- shell_configs.py -- 8 magnetosphere entries tagged.
- planet_visualization.py -- _append_inertial_note + axis/cone wiring;
  dispatch signature gains axis_range; indicator call threads it.
- planet_visualization_utilities.py -- create_magnetosphere_shape
  promotion.
- shared_utilities.py -- indicator clamp.
- apsidal_markers.py -- epoch format chain.

## Verification (container side)

- py_compile clean, all touched files. ASCII/LF checks clean (4
  pre-existing em-dashes in apsidal_markers flagged, not Phase 4's).
- 45 s xvfb GUI launch: clean startup, no traceback.
- _smoke_phase4.py (live dispatch: real tk vars, module-level functions):
  PASS 1 opt-in OFF gates all three consumers, placeholder present;
  PASS 2 opt-in ON activates engine path, placeholder retired, range
  hint threaded; PASS 2b 8 traces, count stable across sun positions,
  all coords d7-rounded, 67.9 KB/f (matches the measurement table
  exactly -- the chokepoint delivers what the gate data promised);
  PASS 3 clamp engages (tip 0.0047 <= 0.005 cube), no-range path
  byte-identical at 1.15 x shell; PASS 4 epoch parser, three forms +
  garbage -> None; PASS 5 dummy slots untouched.
- Tony side: Mode-5 gate list in ledger section G (tail anti-sunward
  across frames; tracking window framing; playback feel; clamp at
  manual scales; hover wording). Animation runs need Horizons --
  unreachable from the container; the render gate is yours.

## Deferred / residual (all in the ledger)

- MAPS per-frame wiring (ADDENDUM decision 1; two-site exclusion warning
  and partition design captured there).
- JS track-and-orbit follow-on (manual-zoom stomp during playback).
- Static Fly To buttons: port the shell-aware 120x sizing (O13b rest).
- O2/O3 console notice wording when magnetosphere opt-in is ON.
- Per-body density literals: CLOSED as not needed (reopen only if
  multi-magnetosphere/60-frame budgets bite; 8-at-once = 411 KB/f
  rounded, guardrail warns correctly).

Module updated: June 2026 with Anthropic's Claude Fable 5
