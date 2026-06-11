# ANIMATION ENGINE DESIGN v1 -- Per-Frame Element Engine (21/51 Phase 3)

Tony Quintanilla, PE | Claude | June 10, 2026 (Session A)
Design base: orrery repo HEAD 8438a85. Companion: measure_perframe_elements.py
(budget table reproduced in section 6). Decisions incorporated: Phase 3 GO
block in HANDOFF_animation_phase2.md (Q1-Q6 + rebuild-as-universal directive).

## 1. The question Session A had to answer

Tony's directive: can the engine treat ALL per-frame elements uniformly as
"call the builder at this frame's position," with the only per-element
variation being the builder function and its resolution parameter?

**Answer: YES.** Rebuild-per-frame is the universal strategy. The evidence is
that the codebase already contains the contract: the CUSTOM_SHELLS dispatch
resolves builders by dotted-name string and calls them as
`builder(center_position, **kwargs)`, where kwargs are driven by opt-in
entry flags (`needs_planet_name`, `needs_sun_position`). The engine is that
same call made N times with per-frame context instead of once with frame-1
context. No translate path, no rotate path, no second mechanism. Elements
too expensive even at reduced resolution stay frame-1 frozen by MEASURED
decision (section 6), not by separate machinery.

Two normalizations are required to make "uniform" true, both small:

- **Comet tails (Session C prerequisite):** `add_comet_tails_to_figure` is
  fig-mutating, not trace-returning. Extract a trace-returning core
  (`build_comet_tail_traces(comet_name, position, sun_position, date, ...)
  -> list[traces]`) and make the existing function a thin fig wrapper --
  the established renderer-refactor pattern. The engine consumes the core.
- **Sun direction indicator:** not a CUSTOM_SHELLS entry (the unified
  dispatch adds it directly). It joins the engine via a small built-ins
  registry (section 3) rather than by forcing it into CUSTOM_SHELLS.

## 2. Engine contract

A per-frame element is a (body, element) pair with:

    builder(**frame_context) -> list[plotly traces]

where frame_context is assembled per frame by the engine from opt-in flags:

    center_position   always (the body's position at this frame)
    sun_position      if needs_sun_position (Sun's position at this frame)
    planet_name       if needs_planet_name
    resolution_scale  if accepts_resolution (follow-on; default 1.0)

This is byte-for-byte the existing dispatch convention plus one future flag.

**Invariant (load-bearing): trace-count stability.** Plotly frames replace
data at fixed trace indices, so a builder MUST return the same number of
traces at every frame. The engine asserts `len(rebuilt) == len(allocated)`
per element per frame and fails LOUD on violation -- a silent mismatch would
shift every subsequent element's traces (the misalignment failure class the
Phase-1 sync fix guarded against). Known instability to design around: the
sun-direction indicator SUPPRESSES itself (returns fewer traces) when
sun_position == center_position (the Phase-1 discovery). The engine must
either (a) require builders to return placeholder invisible traces instead
of suppressing, or (b) treat suppression as a per-element constant decided
at allocation time (frame-1) and assert it stays constant. Recommendation:
(b) -- suppression conditions in this codebase depend on geometry that does
not flip mid-animation for any current element; assert and fail loud if one
ever does, then promote that builder to (a).

## 3. Registry: tag the existing config, don't build a second one

Single source of truth, two small additions:

1. **CUSTOM_SHELLS entries gain `'per_frame': True`** on the committed
   elements: `rotation_axis`, `dipole_cone` (Uranus/Neptune),
   `sodium_tail` (Mercury). The engine walks CUSTOM_SHELLS[body] for
   per_frame-tagged entries of every non-center animated body. No second
   config dict; a new body's axis becomes animatable by tagging its entry.
2. **ENGINE_BUILTINS** -- a short module-level list in palomas_orrery.py for
   elements that are not CUSTOM_SHELLS entries: the sun-direction indicator
   (and, when opted in, comet tails via the Session-C trace-returning core).
   Each entry: builder ref + flags, same contract as above.

Eligibility per animation: a (body, element) activates when the body is a
non-center animated object AND its element's existing trigger condition
holds (rotation axis: auto with the body's custom dispatch, per Tony's
Decision-1 note -- code-confirmed at planet_visualization.py L434, the axis
is intentionally not checkbox-gated; dipole cone: same; sodium tail: its
shell checkbox; comet tails: the opt-in mode flag, Session C).

## 4. Allocation and the frame-loop extension

At figure-build time (animate path, after the center dispatch, before the
fence):

1. For each active (body, element): call the builder ONCE with frame-1
   context. Append the returned traces to the figure (this IS frame 1's
   content). Record the absolute indices:
   `perframe_groups[(body, element)] = [idx, ...]`.
2. Extend the Phase-1 fence: `dynamic_trace_indices` = sorted union of
   `trace_indices.values()` and all perframe_groups indices. The Phase-1
   mapping machinery (`_frame_pos_by_trace_idx` / `to_frame_idx`) already
   handles arbitrary sparse sets -- designed for this; no change needed.

In the frame loop, after the existing single-point marker updates:

3. For each active (body, element): read the body's position (and Sun's,
   if flagged) from positions_over_time at this frame; call the builder;
   assert trace-count stability; write each rebuilt trace into
   `frame_data[to_frame_idx(idx)]` for the group's indices.
4. Bodies with a missing position at a frame: set the group's traces
   invisible for that frame (mirror of the existing marker behavior).

First-frame sync (Phase-1 Edit C) needs no change: frame 1's figure content
was produced by the same builders at the same context.

**Budget guardrail.** At allocation, the engine serializes one frame-1
group per element and prints:
`[ANIMATION] Per-frame engine: K elements, X KB/frame, ~Y MB over F frames`
plus a soft warning above a threshold (proposal: warn at 150 KB/frame,
~4.4 MB @29f -- the Phase-1 savings line). Numbers, not vibes, at runtime.

## 5. What stays frame-1 frozen (measured, per Decision 1)

All sphere shells and full-resolution custom meshes (magnetosphere,
bow-shock surface, belts, corona set) remain frame-1 static at the center
body and absent for non-center bodies until the reduced-resolution
follow-on passes BOTH gates: 5(a) bytes (already passing at the measured
reduction, section 6) and 5(b) Tony's Mode-5 quality judgment. Ring
systems ride the same follow-on. The disclosure (section 8) names the
freeze honestly in the meantime.

## 6. Measured budget table (live builders, June 10; harness in repo)

FIRST-CUT PRIMITIVES (committed per-frame):
  Rotation axis (Uranus)            6 traces   10.7 KB/f   0.31 MB @29f
  Rotation axis (Earth)             6 traces   10.7 KB/f   0.31 MB @29f
  Dipole cone (Uranus)              8 traces   19.5 KB/f   0.57 MB @29f
  Dipole cone (Neptune)             8 traces   19.6 KB/f   0.57 MB @29f
  Sun direction indicator           2 traces    0.8 KB/f   0.02 MB @29f
SUN-DIRECTION CUSTOMS (committed):
  Mercury sodium tail (500 pcl)     2 traces   48.5 KB/f   1.41 MB @29f
  (per-frame mode may drop particle count; 250 pcl measured ~24.9 KB/f)
MEASURED FOLLOW-ON (gate 5a):
  Earth magnetosphere FULL          8 traces  146.4 KB/f   4.25 MB @29f
  Bow shock conic 30x30 / 20x20 / 15x15:    59.5 / 26.1 / 14.5 KB/f
  Earth magnetosphere REDUCED
    (belts 40x3, shock 15x15,
     envelope un-reduced)           8 traces   62.4 KB/f   1.81 MB @29f

**Gate 5(a) verdict: PASSES.** The reduced composite sits inside the
Phase-1 savings with the envelope still at full density. Envelope reduction
(the one remaining producer promotion, section 7) brings it to ~1.4 MB @29f.
Gate 5(b) -- whether the reduced render still teaches -- is Tony's, at the
follow-on.

## 7. Resolution sweep scope (REVISED SMALLER by Session-A findings)

The "8-file parameter sweep" estimate shrank. The two heavy surfaces both
come from SHARED producers in planet_visualization_utilities:

- `create_bow_shock_shape(standoff, width, n_phi=30, n_theta=30, ...)` --
  ALREADY parameterized. Zero work; callers pass smaller n.
- `create_magnetosphere_shape(params)` -- density internal; ONE promotion
  (add n-parameters with current defaults) propagates to every
  magnetosphere body. The producer-fix principle, again.

What remains per-body: local density literals (belt n_points/n_rings,
particle counts like the sodium tail's 500) promoted to keyword args with
current defaults, plus the `accepts_resolution` dispatch flag threading a
single resolution_scale. Sphere shells: n_points already per-config in
SHELL_CONFIGS; an override is a config copy. This work is ALSO 20/N5's
backend (the shell-resolution GUI control inherits the same knobs).

## 8. Disclosure (Session C, per Decision 2 + Q2 answer)

- Per-element hover line on frame-1-frozen elements -- authoritative;
  rides the existing bow-shock sourced-vs-schematic sweep (one honesty
  convention, three siblings: conic approximation, orientation freeze,
  frame-1 position freeze).
- One `layout.annotations` footnote in PAPER coordinates (small, grey):
  "Animated per frame: markers, axes, tails. Fixed at frame 1: shells."
  Paper coords, not scene.annotations (which anchor in data space and swim
  with the camera). Legend untouched.

## 9. Auto-scale through the consolidated pipeline (Session C, Decision 3)

The engine knows every rendered extent: orbital ranges (existing
get_animation_axis_range), center-shell extent (add_center_body_shells'
returned axis_range -- currently annotated-dead in animate), and per-frame
element envelopes (max over frames of body position + element radius).
Session C replaces the unconditional get_animation_axis_range assignment
with `axis_range = max(orbital, shell, engine extents)` under Auto --
resolving the section-G dead-auto-scale question inside the consolidation
rather than as a bolt-on patch. Mode-5 gated.

## 10. Session breakdown

- **Session B (engine + first customers):** registry tags + ENGINE_BUILTINS;
  allocation; frame-loop extension; stability assert; budget guardrail;
  customers = rotation axis, dipole cone, sun-direction indicator.
  Live-dispatch tests: allocation/rebuild equivalence at frame-1; stability
  assert trips on a deliberately broken builder; measured frame payloads.
  Render gate: protocol v3 (to be issued with Session B).
- **Session C (second customers + consolidation):** comet-tail
  trace-returning refactor + opt-in mode; sodium tail; disclosure (hover +
  footnote); auto-scale consolidation. Render gate.
- **Follow-on (separately gated):** resolution sweep (sec 7) + reduced-shell
  per-frame mode; gates 5(a) re-measured per body + 5(b) Mode 5.

## 11. Risks and their guards

- Trace-count instability -> loud assert at every frame (sec 2); the one
  known conditional (indicator suppression) handled at allocation.
- Frame payload creep as elements stack -> budget guardrail print + soft
  warn; the harness stays in the repo for re-measurement.
- Builder CPU x N frames -> measured trivially small for line geometry;
  revisit only if a future builder is mesh-heavy (then it likely belongs
  frame-1 frozen anyway, by the same measured-decision rule).
- Engine/static divergence -> none introduced: the engine consumes the SAME
  builders through the SAME dispatch convention; static behavior untouched.

Module updated: June 2026 with Anthropic's Claude Fable 5
