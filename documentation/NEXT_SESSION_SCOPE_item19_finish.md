# Next-Session Scope: Finish Item 19 -- scene_camera + scene_aspectmode parity

Paloma's Orrery | Tony Quintanilla, PE + Claude | scoped June 16, 2026

Base to pin at session start (re-confirm by round trip, do not trust cold):
  gallery  HEAD 812c05f  (tonyquintanilla.github.io, branch main)
  orrery   HEAD c28eec0  -- BUT: pasting the item-19.3 ledger block + commit
           will advance orrery HEAD off c28eec0. Re-read remote HEAD at start.
Prior session: item 19.3 round trip CLOSED (range + dtick read-on-load,
  toggle defaults). This session finishes item 19's remaining two controls.

--------------------------------------------------------------------------
## Goal

Close item 19 (plot-cube control parity, orrery <-> Gallery Studio). Bring the
last two scene controls to the read-on-load / refine state the others now have:

  DONE (prior sessions):  scene_axis_range, scene_dtick, show_axes,
                          show_grid, show_modebar
  THIS SESSION:           scene_aspectmode, scene_camera

The reusable pattern exists: _read_scene_grid_from_figure (built Phase B) +
D3 precedence (explicit Studio override wins; else read the figure). Extend it
(or add a sibling _read_scene_view_from_figure) for aspect + camera.

--------------------------------------------------------------------------
## Two halves -- different natures

### A. scene_aspectmode -- near-execution (mirrors Phase B)
Clean enum (auto / cube / data / manual) on a Combobox. Read scene.aspectmode
from the loaded figure -> set var_scene_aspect, same D3 precedence as range/
dtick. Small.
  Wrinkle: aspectmode == "manual" also uses scene.aspectratio (x/y/z). Confirm
  whether Studio exposes ratio fields; if not, either read+store the ratio
  alongside, or defer "manual" and read only auto/cube/data on load. Decide
  at session start after checking the GUI.

### B. scene_camera -- DESIGN-FIRST (the knot, sketch before code)
Studio's camera control is a 5-PRESET dropdown (original/isometric/top/front/
side) mapped through _CAMERA_PRESETS. A loaded orrery figure carries an
ARBITRARY baked camera (eye/center/up) that generally matches NO preset.
So "read camera on load" has no clean dropdown slot. Open the session on this,
sketch-first:

  Q1 -- how to represent a non-preset camera in a preset dropdown?
     (a) add an "as-loaded / custom" entry that holds the figure's actual
         eye/center/up, auto-selected when the baked camera matches no preset;
     (b) preset-match within a tolerance -> snap to the nearest named preset,
         else "custom";
     (c) read aspectmode only this session; leave camera preset-only and defer
         the arbitrary-camera read to its own item.
  Q2 -- parity scope. For range/dtick we did BOTH halves (Phase A orrery field
     + Phase B Studio read). Does item-19 camera/aspect "finish" need an
     orrery GENERATION-TIME control too, or is Studio read-on-load + refine
     the bounded, sufficient version? (Orrery camera is auto-framed per plot;
     a generation-time camera control is a bigger lift -- likely a separate
     optional, not this session. Tony's call.)

  Lean going in: aspectmode read-on-load + camera as "(a) custom/as-loaded"
  is the bounded close. Confirm by sketch, then build.

--------------------------------------------------------------------------
## Verified touch points (gallery_studio.py @ ~6804b39 -- RE-CONFIRM cold)

  DEFAULT_CONFIG       scene_aspectmode (100), scene_camera (101)
                       (also PORTRAIT 174/175, third cfg 304/305)
  apply_config         aspect set 1041-1043; _CAMERA_PRESETS + camera set
                       1046-1066
  GUI comboboxes       var_scene_aspect 4181; var_scene_camera 4199
  _collect_config      4410-4411 (saves both into _studio_config)
  _apply_config_to_gui 4493-4494 (sets both from config on load)
  _do_load             the two branches (studio / raw-orrery) -- same wiring
                       points Phase B used
  GAP                  nothing reads camera/aspect FROM the figure today

Pattern note: a custom/as-loaded camera would need somewhere to STORE the raw
eye/center/up (not just a preset name) -- e.g. a config key scene_camera_custom
that apply_config uses when scene_camera == 'custom'. Design in Q1.

--------------------------------------------------------------------------
## Ride-along cleanups (fold in if cheap)

  - 2D-plot sanity gate (deferred from Phase B): a 2D figure loads fine,
    grid/camera/aspect fields stay at defaults.
  - Optional: orrery also emits the km suffix under KM_SUFFIX_MAX_AU (full
    title parity orrery <-> Studio). Small, orrery-side -- only if in scope.

--------------------------------------------------------------------------
## Session shape

Design-then-build. Open on B/Q1+Q2 (sketch-first, the conversation is the
design). A (aspectmode) is bounded execution once the manual/aspectratio
wrinkle is settled. Same gate discipline as Phase B: live smoke against the
real reader + apply_config on synthetic figures (preset camera, arbitrary
camera, each aspectmode), then Tony's Mode-5 render gate (load a raw orrery
plot -> camera/aspect fields reflect the baked view; refine; re-export;
reload holds).

--------------------------------------------------------------------------
## State note (not item 19)

IPC API key: still no response ~1 week after the request. Food-insecurity /
Sudan KMZ track remains BLOCKED. Worth a follow-up nudge on the request; if
the key lands it jumps the queue (high mission value) over the rest of the
backlog (animation Phase 2 [needs O1-O6 first], Artemis presets + N6,
Gallery encounter-export).

Scoped June 2026 with Anthropic's Claude Opus 4.8.
