# Handoff: Item 19.3 -- Orrery-side 3D Axis Control (scene-builder extraction)

Paloma's Orrery | Tony Quintanilla, PE + Claude | June 14, 2026

Built on: orrery HEAD 1288b51757f5e4ca8974099c2b6b9835f55020e5 (branch main)
Gallery:  HEAD 2f40d9d58f8ff784ceb4eff0c870775ff5027fdc (branch main)
Design authority: documentation/3d_axis_control_handoff.md (Studio side DONE)
This doc: the next-session entry point. Design is settled; this is buildable.

--------------------------------------------------------------------------
## 1. Session goal

Bring the 3D axis controls (dtick + range + grid/axes/aspectmode) to the
ORRERY generation side, at parity with Gallery Studio (already verified
@2f40d9d). The remaining item-19 core. Studio refines post-hoc; the orrery
must set sensible values at generation so close-approach / flyby plots are
readable without a Studio round trip.

Delivered as a SCENE-DICT extraction (not a full layout merge). Two phases
with a render gate between them.

--------------------------------------------------------------------------
## 2. Verified map (at 1288b51 -- do NOT trust the design-authority doc's
   line numbers; they are stale from March)

Four independent scene-construction sites + one copy:

  S1  5704  plot_objects        main solar-system scene        TWIN
  S2  7940  animate_objects     main animation scene           TWIN
  S3  5996  plot_objects        exoplanet local-frame override VARIANT
  S4  7652  animate_objects     per-frame track-camera layout  VARIANT
           (_track_frame_layout / _track_axis)
  --  8127  animate_objects     scene=_tl0.scene (COPY, consumer; no build)

Helpers already present (range math has a home; the gap is the DICT assembly):
  calculate_axis_range_from_orbits()      line 605
  get_improved_axis_range()               line 827
  get_animation_axis_range()              line 845
  _animate_axis_range_hint()              line 2143
  visualization_utils._calculate_grid_dtick(axis_span)  line 333  (SHARED w/ Studio)
  traces_extent_from_center() -> fig._body_element_extent_au  (extent producer;
    already consumed by Fly-To and camera tracking)

--------------------------------------------------------------------------
## 3. Key finding -- _track_axis is the reference implementation

S4's _track_axis (line 7627) already returns the COMPLETE, correct spec:
  range + autorange=False + dtick=_track_dtick + showgrid + gridcolor='gray'
  + showbackground + backgroundcolor='black'
with a docstring explaining the Plotly frame-merge inheritance gotcha
(omitted axis props inherit the previous frame -> inconsistent 3D grid).

The two MAIN paths (S1/S2) set range + styling but NOT dtick and NOT
autorange=False. THAT is why close-approach plots are unreadable: Plotly
auto-ticks at dtick=1 on an AU-scale cube. S3 (exoplanet) is barest: range +
title only, no styling, no dtick.

So this feature is "generalize S4's disciplined spec to S1/S2/S3 via a shared
builder," not "invent a new capability." Low risk.

--------------------------------------------------------------------------
## 4. Decision (the session's direction-setting call)

(a2) SCENE-GRANULARITY extraction. Unify the self-contained scene=... object
(axes + aspectmode + camera + domain), which is VERIFIED byte-identical across
the twins. STOP at the layout envelope (title, annotation, legend, margin,
footer), which has already DRIFTED -- some intentionally. Do NOT merge the
envelope; that is the divergence audit's job (Section 8).

Rationale: extract along the seam where the sites are verifiably identical;
stop the instant extraction would require deciding which of two divergent
versions is canonical. The scene dict is identical (verified diff: same
aspectmode='cube', same camera=get_default_camera(), same
domain=dict(x=[0.2,1.0], y=[0.0,1.0])). The envelope is not -- see Section 8.

The FULL plot_objects/animate_objects function-body merge stays OFF the list
entirely (high blast radius; chokepoints earned most of its value). This scene
extraction neither touches nor depends on it.

--------------------------------------------------------------------------
## 5. Builder design (model on _track_axis)

  def build_scene_axes(x_range, y_range, z_range,   # each [lo, hi]
                       dtick=None,        # None -> omit (Plotly auto, current
                                          #   S1/S2 behavior); float -> set
                                          #   dtick AND autorange=False
                       styled=True,       # True -> backgroundcolor='black',
                                          #   gridcolor='gray', showbackground,
                                          #   showgrid; False -> bare (S3)
                       show_grid=True, show_axes=True,
                       titles=('X (AU)','Y (AU)','Z (AU)')):
      # returns dict(xaxis=..., yaxis=..., zaxis=...)

  def build_scene(x_range, y_range, z_range, dtick=None, styled=True,
                  show_grid=True, show_axes=True,
                  aspectmode='cube', aspectratio=None,
                  camera=None, domain=None):
      # wraps build_scene_axes; adds aspectmode, plus aspectratio/camera/domain
      # ONLY when not None. returns the scene dict.

  # convenience for symmetric paths:
  def symmetric_ranges(r): return ([-r, r], [-r, r], [-r, r])

Coupling rule (from _track_axis): when dtick is a float, ALSO set
autorange=False. When dtick is None, omit both. This is the one behavior that
makes dtick actually hold.

Site reproduction (Phase 1 = byte-identical):
  S1: build_scene(symmetric_ranges(r), dtick=None, styled=True,
                  camera=get_default_camera(),
                  domain=dict(x=[0.2,1.0], y=[0.0,1.0]))
  S2: same shape as S1 (twin)
  S3: build_scene(symmetric_ranges(exo_axis_range), dtick=None, styled=False,
                  camera=None, domain=None)   # bare, no aspect extras beyond cube
  S4: build_scene([cx-rt,cx+rt],[cy-rt,cy+rt],[cz-rt,cz+rt],
                  dtick=_track_dtick, styled=True,
                  aspectratio=dict(x=1,y=1,z=1))   # per-axis centers from _e
      (S4 already passes per-axis ranges -> this is WHY the builder takes
       per-axis ranges, not one symmetric value)

--------------------------------------------------------------------------
## 6. Two-phase plan (render gate between)

PHASE 1 -- behavior-preserving extraction. Builder defaults reproduce EACH
site byte-identical (S1/S2 with dtick=None, S3 bare, S4 full). Mode-5 gate
MUST show ZERO render change on a solar-system view, an exoplanet view, and a
camera-tracking animation. This proves the parallel-pipeline refactor moved
nothing. Push, re-pin HEAD.

PHASE 2 -- the fix (auto-only, Q2). Turn on dtick for S1/S2 via
_calculate_grid_dtick(span) (+ autorange=False). Evaluate range: if the
existing range logic does NOT already fit non-Sun-center extent (read
get_improved_axis_range / get_animation_axis_range FIRST), add extent-driven
autofit consuming fig._body_element_extent_au. Mode-5 gate on the canonical
Apophis Earth-centered case (readable grid + geometry fills the cube) AND
confirm NO regression on Sun-centered solar-system and on the track path.
S3 dtick + styling = optional opt-in, separate render gate on an exoplanet
system; lower priority.

--------------------------------------------------------------------------
## 7. Parity (provable, not asserted) + Studio composition

- Orrery dtick MUST call visualization_utils._calculate_grid_dtick -- the
  exact function Studio imports. Then orrery-static, orrery-animate,
  orrery-track, and Studio all share one dtick source.
- Confirm where _track_dtick is computed. If not already via
  _calculate_grid_dtick, route it through for full parity (one-line win).
- Studio composition: Studio default scene_axis_range/scene_dtick = 0.0 means
  "keep figure values," so an orrery-baked dtick/range is respected unless the
  user sets a Studio override. ROUND-TRIP TEST: generate in orrery with auto
  dtick -> open in Studio (no override) -> confirm no double-apply; then set a
  Studio override -> confirm it wins.

--------------------------------------------------------------------------
## 8. Divergence-audit SEED (the envelope drift we are deliberately NOT
   merging -- catalogued here so the audit starts warm, not cold)

Verified diff of S1 (5704) vs S2 (7940) envelope:
  1. title -- INTENTIONAL: S1 = computed date-range title_text; S2 = literal
     "Paloma's Orrery - Animation Over Below Dates" (dates live in the slider).
  2. annotation text -- EDITORIAL: S1 interleaves exoplanet notes inline via
     per-line conditionals; S2 swaps the WHOLE block via one top-level
     `if not is_exoplanet_mode else`. Displayed copy differs in exoplanet mode.
     Merging requires deciding which approach is canonical -> audit's call.
  3. annotation y -- S1 y=0.80; S2 y=0.7.
  4. footer link -- S1 "Paloma's Orrery GitHub Page"; S2 "Search: NASA",
     different coords.
Also: legend/margin/bgcolor/font ARE identical across the twins but are LEFT
per-site on purpose -- pulling them into a half-envelope helper is the slope
into the editorial merge. Line held at the scene sub-object.

Leave a `# TWIN: paired with <other line> -- envelope drift catalogued in
divergence-audit seed` breadcrumb at S1 and S2.

--------------------------------------------------------------------------
## 9. Confirm-at-implementation checklist (read before editing)

[ ] Read get_improved_axis_range (827) + get_animation_axis_range (845):
    do they already fit non-Sun-center extent? -> decides Phase-2 range scope.
[ ] Confirm where _track_dtick is computed (parity routing).
[ ] Confirm S4's exact lexical position relative to _track_frame_layout (the
    awk "nearest def" heuristic was ambiguous on 7940; verify before edits).
[ ] Bottom-up edits (highest line numbers first): S4(7652) -> S3(5996) ->
    S2(7940) -> S1(5704), then insert builders above their first use.
[ ] Studio round-trip test (Section 7).

--------------------------------------------------------------------------
## 10. Test protocol

- py_compile palomas_orrery.py ; ASCII/LF check ; bottom-up edits.
- Live-dispatch smoke: CONSTRUCT scenes via the new builder for the static and
  animate paths and INSPECT the axis dicts; assert S1/S2 produce identical
  scene dicts (parity smoke). Do NOT smoke the builder in isolation only --
  exercise the live call sites.
- xvfb-run pre-test (SystemButtonFace->gray90 swap, restore after).
- Mode-5 gate per phase (Section 6). Tony's eyes are ground truth.

--------------------------------------------------------------------------
## 11. SHA carry

Built on 1288b51. After Phase 1 push, record the new SHA here and re-pin HEAD
before Phase 2. After Phase 2 push, record again. Update LEDGER item 19.

Module updated: June 2026 with Anthropic's Claude (design session; no code
this session -- handoff + ledger only).
