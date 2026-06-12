# ANIMATION PHASE 4 BRIEF -- Per-Frame Magnetosphere + Camera Tracking

Tony Quintanilla, PE | Prepared by Claude Sonnet 4.6 for Claude Fable 5
June 12, 2026 | Repo HEAD: 988d0f804ef1018a6a4e2acf46d6a6f55678d903

## What this is

A brief for the next major animation session. The per-frame engine is
proven and the core track is conditionally closed (R1 Ikeya-Seki and R2
Mercury-centered are showcase renders). This session extends the engine
with three primary features: the magnetosphere animated per frame (the
first heavy sun-dependent geometry), camera tracking that enables Mode-5
verification at close range in heliocentric animations, and the MAPS
per-frame tails wiring that the R3 retest identified as a gap.

The magnetosphere and camera tracking are one story: the camera is the
verification tool for the magnetosphere, and the magnetosphere is what
gives the camera something educationally new to show. The MAPS fix
completes the comet-tail per-frame feature that standard comets already
showcase.

Tony's instruction: think ambitiously and comprehensively. The architectural
foundation is solid; this session should build on it with confidence,
innovate where the design can be improved, and expand scope where the
educational payoff justifies it.


## The educational goal

The magnetotail swinging to stay anti-sunward as a planet orbits the Sun.
Mercury and Venus (induced magnetospheres, comet-shaped tails, fast orbital
periods) are particularly striking. Earth's magnetotail stretching into the
night side as the Sun-line rotates. This is the physics that makes the
orrery a teaching tool -- not just positions, but orientations that respond
to the Sun.


## What the engine already does

14 per_frame-tagged elements in CUSTOM_SHELLS + builtins:

    Rotation axis:  Moon, Pluto, Mercury, Venus, Mars, Earth, Jupiter,
                    Saturn, Uranus, Neptune, Sun (11 bodies)
    Dipole cone:    Uranus, Neptune
    Sodium tail:    Mercury (checkbox-gated)
    Sun direction:  indicator (builtin, all bodies with shells)
    Comet tails:    opt-in checkbox (standard comets; MAPS excluded)

Architecture (ANIMATION_ENGINE_DESIGN_v1.md is the full reference):

    builder(**frame_context) -> list[plotly traces]

Uniform rebuild-as-universal strategy. Registry = per_frame tags in
CUSTOM_SHELLS + ENGINE_BUILTINS. Trace-count stability asserted loud.
Variable-count elements (comet tails) pad-to-max with invisible dummies.
Budget guardrail warns above 150 KB/frame. Sticky-visible fix
(_normalize_perframe_visibility) ensures every slot write carries explicit
visible. The engine's Sun contract: real trajectory, fetch when unchecked,
suppression over fabrication -- never a placeholder position.

For CENTER bodies, get_center_engine_elements() is the single source of
truth: it claims only elements with BOTH per_frame AND needs_sun_position
(sun-direction indicator, sodium tail). Inertial elements (rotation axis,
dipole cone) stay with the static dispatch -- frozen is correct physics.
The dispatch receives skip_elements so engine and dispatch never double.


## Feature 1: Per-frame magnetosphere (opt-in)

All 8 magnetosphere entries in CUSTOM_SHELLS already have
needs_sun_position: True. The builders already receive sun_position and
orient the geometry anti-sunward. The engine already handles
needs_sun_position elements. What's needed is the resolution reduction to
fit the budget and the per_frame tags.

### Measured budget (from measure_perframe_elements.py, in repo)

    Earth magnetosphere FULL:       146.4 KB/f    4.25 MB @29f
    Earth magnetosphere REDUCED:     62.4 KB/f    1.81 MB @29f
      (belts 40x3, bow shock 15x15, envelope un-reduced)
    Envelope also reduced:          ~est 1.4 MB @29f
    Bow shock conic 15x15:           14.5 KB/f

    Phase 1 savings reference:      ~4.2-4.5 MB per animation

Gate 5(a) (bytes): PASSED at the reduced composite.
Gate 5(b) (quality): Tony's Mode-5 judgment -- does the reduced-density
magnetosphere still TEACH? This is the open gate for this session.

### What the design doc prescribes (feel free to improve)

    1. create_magnetosphere_shape (planet_visualization_utilities.py L208)
       -- ONE shared-producer promotion. Add n-parameters with current
       values as defaults. This propagates to every body's magnetosphere.
       This is the last remaining producer change.

    2. create_bow_shock_shape (L293) -- ALREADY parameterized with
       n_phi/n_theta. Zero work; callers pass smaller n when per-frame.

    3. Per-body density literals (belt n_points/n_rings, particle counts)
       promoted to keyword args with current defaults, so a resolution_scale
       or reduced flag can drive them down.

    4. per_frame: True tags on magnetosphere entries in CUSTOM_SHELLS.

    5. Opt-in checkbox in the animation settings panel, like the existing
       "Animate comet tails (rebuild each frame)" checkbox
       (palomas_orrery.py L10148). Default off (file size). Tooltip
       explaining the educational payoff vs the cost.

    6. For center bodies: get_center_engine_elements already returns
       elements with per_frame + needs_sun_position, so the magnetosphere
       would automatically be engine-owned for the center body (Sun
       Direction tracking at the origin while the Sun moves). Verify this
       path works.

    7. For non-center bodies: the engine's collect_perframe_elements
       (L2123) already walks CUSTOM_SHELLS for per_frame entries. Adding
       the tag should "just work" -- but the magnetosphere's builder needs
       to return a STABLE trace count across frames (the invariant).
       Verify and assert.

### Sun Direction indicator must respect the cube range

When auto-scale is set to shell extent (the Session C max(orbital, shell)
consolidation), the Sun Direction indicator can extend beyond the rendered
axis range and get clipped. The indicator's length is derived from the
outermost shell radius, but the line points toward the Sun -- which at
shell scale can be far outside the cube. The fix: clamp the indicator
length to the current axis_range so it always terminates inside the
visible volume. This applies to both the static dispatch and the per-frame
engine rebuild. (Ledger item 19 / O12; surfaced during shell-scale
testing.)

### Open question for Fable 5

The design doc's approach is reduced-resolution per-frame vs full-resolution
frame-1 frozen, selected by the opt-in checkbox. But there may be better
approaches. Could the magnetosphere orientation be updated per-frame WITHOUT
full geometry rebuild -- rotating the existing mesh coordinates? That would
be much cheaper (no new traces, just coordinate transforms). The
magnetosphere is not a simple rotation (the magnetotail geometry changes
with the sun-planet distance and angle, not just the direction), but for
some components (bow shock, magnetopause) a rotation might be a good
approximation. Worth considering if the budget can be compressed further.

Jupiter's magnetosphere is the extreme case: 146 KB/f at full resolution
is already beyond the budget guardrail for a single element. Should
Jupiter get a special low-resolution mode, or should it be excluded from
per-frame and disclosed? Educational judgment call.


## Feature 2: MAPS per-frame tails

### The gap (from R3 v4.1 testing)

The opt-in "Animate comet tails" checkbox works for standard comets (R1
Ikeya-Seki proved it -- the tail swinging at perihelion is THE educational
moment). But MAPS C/2026 A1 renders identically with the checkbox on or
off. The per-frame engine does not engage for MAPS.

Root cause: MAPS has special disintegration-mode code paths in
comet_visualization_shells.py -- "headless ghost comet" (post-disintegration
debris arc via create_maps_ghost_tail_trace) and "pre-disintegration mode"
(active comet with coma, before the disintegration point). These bypass the
standard comet tail builder (add_comet_tails_to_figure) that the engine's
capture shim (build_comet_tail_traces, L2090 of comet_visualization_shells.py)
wraps.

The engine's MAPS exclusion is explicit -- it was designed that way because
the date-gated disintegration logic and fig-coupled ghost-tail trace were
judged frame-1 static by design. But the PRE-disintegration portion (the
active comet approaching the Sun) should animate like any other comet. The
ghost tail (post-disintegration debris arc) may genuinely be frame-1 static
(it's a historical trajectory, not a live tail), but that's a design call.

### What Fable 5 should evaluate

    1. Pre-disintegration MAPS: the comet is active, has coma and tails,
       and is approaching the Sun. This portion should animate per-frame
       like Ikeya-Seki does. Wire it through the engine.

    2. Post-disintegration ghost tail: is this a historical arc that
       should be static, or should the debris also animate? The debris
       arc is computed from Barker's equation / Horizons positions along
       a fixed trajectory. It may not have a meaningful per-frame
       representation. Design call.

    3. The disintegration point itself: a marker at a fixed position.
       Static is correct.

Key files:
    comet_visualization_shells.py:
        L580   create_maps_ghost_tail_trace() -- ghost tail builder
        L487   create_maps_disintegration_marker()
        L1602  add_comet_tails_to_figure() -- main builder (fig-mutating)
        L2090  build_comet_tail_traces() -- engine capture shim
    palomas_orrery.py:
        L7268  the MAPS exclusion check in the animate path


## Feature 3: Camera tracking (Fly To across animation frames)

### The gap

Mode-5 verification of non-center body shells at solar-system scale is
blocked. The engine rebuilds primitives on a body that's a dot at
heliocentric scale. You can verify at planet-centered scale (Session B
confirmed this), but the educational render is heliocentric with the
camera following a body through its orbit.

### The mechanism (from the ledger)

go.Frame(layout=dict(scene=dict(camera=...))) can carry scene.camera per
frame. This is native Plotly -- each frame can set the camera.

### Existing Fly To implementation

    visualization_utils.py L363: add_fly_to_object_buttons()
    -- Creates per-body buttons that set camera eye/center to frame the
    body at appropriate distance. The camera math (eye position, center,
    up vector) is already there. It works for frame 1.

### What's needed

    1. At each animation frame, look up the target body's position from
       positions_over_time, compute camera eye/center (same math as
       existing Fly To at the new coordinates), embed in the frame's
       layout.

    2. A user toggle: frame-driven camera fights manual orbit. When the
       user is in "track mode," the camera follows; otherwise the camera
       is free. This could be a checkbox, a button state, or an
       interaction pattern.

    3. The camera distance should account for shell extent when shells
       are checked (item 19 in the ledger: "Fly To zoom limit ignores
       shell extent"). Planets stop too far out to see the magnetosphere.

### Open questions for Fable 5

The naive approach (set camera every frame) locks the user out of orbiting
the view during playback. Is there a way to track the body (translate the
camera center) while still allowing the user to orbit around the tracked
point? Plotly's event model may have limitations here. Explore the design
space.

The Fly To distance calculation currently uses orbital distance / marker
size. For magnetosphere visualization, the camera needs to be at shell
extent scale, not orbital scale. That's a different zoom level -- close
enough to see the magnetosphere but far enough to see it whole.


## Completion riders (bundle if scope permits)

### osc. epoch parser (D.Priority -- every-run console noise)

apsidal_markers.py L1666 strips ' osc.' correctly, but the datetime
parser (L1668-1673) tries only '%Y-%m-%d' and '%Y-%m-%d %H:%M:%S'.
Osculating epoch strings come as '2026-06-10 12:32 osc.' -- after
stripping, '2026-06-10 12:32' doesn't match either format. Add
'%Y-%m-%d %H:%M' to the format chain. The same pattern appears in
palomas_orrery.py at L4056, L5004, L5427, L6541 (those DO strip the
suffix; verify they also handle the HH:MM format).

### Non-center non-tracking hover disclosure

Elements frozen at frame 1 for non-center bodies in heliocentric
animations should carry a hover note saying the orientation is from
frame 1. Quick sweep of the info markers.

## Key files and locations

    palomas_orrery.py (10,613 lines) -- the two pipelines (plot_objects,
      animate_objects) and the per-frame engine:
        L2062  get_center_engine_elements()
        L2110  _normalize_perframe_visibility()
        L2123  collect_perframe_elements()
        L2277  build_perframe_traces()
        L2315  _pad_perframe_traces()
        L2425  add_static_only_legend_placeholders()
        L1963  add_center_body_shells()
        L10148 animate_comet_tails_var (opt-in checkbox pattern)
        L7826  add_fly_to_object_buttons (animate path)
        L5902  add_fly_to_object_buttons (static path)

    comet_visualization_shells.py (1,850 lines):
        L487   create_maps_disintegration_marker()
        L580   create_maps_ghost_tail_trace()
        L1602  add_comet_tails_to_figure() -- main builder (fig-mutating)
        L2090  build_comet_tail_traces() -- engine capture shim

    planet_visualization_utilities.py (794 lines):
        L208   create_magnetosphere_shape() -- the ONE producer to promote
        L293   create_bow_shock_shape() -- already parameterized

    planet_visualization.py (754 lines):
        L434+  create_celestial_body_visualization() -- the unified dispatch
               (skip_elements threading for engine-owned elements)

    shell_configs.py (2,684 lines):
        CUSTOM_SHELLS -- 8 magnetosphere entries, all needs_sun_position

    visualization_utils.py:
        L363   add_fly_to_object_buttons() -- existing camera math

    shared_utilities.py:
        L25    create_sun_direction_indicator() -- length = shell_radius * 1.15
               when shell_radius is provided (L85); can exceed the axis range
               when auto-scale is at shell extent. Clamp to axis_range.

    apsidal_markers.py:
        L1666  epoch parser -- missing '%Y-%m-%d %H:%M' format

    documentation/:
        ANIMATION_ENGINE_DESIGN_v1.md -- full architecture reference
        ANIMATION_TEST_PROTOCOL_v4_1.md -- current test protocol
        LEDGER_orrery_consolidated.md -- running backlog

    measure_perframe_elements.py -- live budget measurement harness


## Constraints that are load-bearing (not suggestions)

    - ASCII-only in Python source files; LF line endings
    - py_compile after every edit
    - Bottom-up editing (highest line numbers first)
    - Trace-count stability invariant: a builder MUST return the same
      number of traces at every frame (asserted loud)
    - The sticky-visible lesson: Plotly frame merges inherit the slot's
      prior state for any omitted property. Every slot write needs
      explicit visible
    - Budget guardrail: warn above 150 KB/frame
    - get_center_engine_elements is the single source of truth for the
      engine/dispatch split -- one producer, two consumers
    - Phase 1 savings (~4.2-4.5 MB) is the budget envelope reference
    - Mode-5 verification (Tony's eyes) is the final gate
    - The protocol (project_instructions_v3_28.md) governs session
      mechanics: SHA-pinned base, verify-execution-not-appearance,
      enumerate uploads before claiming a review

## What this session should produce

    At minimum:
    - Per-frame magnetosphere with opt-in checkbox (reduced resolution)
    - MAPS per-frame tails (pre-disintegration wiring into the engine)
    - Camera tracking for Fly To across animation frames
    - Sun Direction indicator clamped to axis range (no clipping)
    - The osc. epoch parser fix

    At best (Tony's instruction -- think ambitiously):
    - All of the above
    - A comprehensive resolution-management system that makes the
      budget/quality tradeoff visible and controllable
    - Camera tracking that respects user interaction (track + orbit)
    - MAPS ghost tail design resolution (animate or disclose)
    - Any architectural improvements the engine's design suggests to
      someone seeing it fresh

    The render is the proof. Tony will verify Mode 5.


Module updated: June 2026 with Anthropic's Claude Sonnet 4.6
