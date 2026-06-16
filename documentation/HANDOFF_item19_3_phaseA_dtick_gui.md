# Handoff: Item 19.3 Phase A -- User-settable dtick GUI field (orrery)

Paloma's Orrery | Tony Quintanilla, PE + Claude | June 16, 2026

Built on:  orrery HEAD 30840b1b2f4e747e59738f813e56542c753d9fcd (branch main)
Pushed at: orrery HEAD 1c08a8aa12072aa0b3690523eff27e4cd120076b (branch main)
Gallery:   HEAD 2f40d9d58f8ff784ceb4eff0c870775ff5027fdc (branch main, UNCHANGED)
Design authority: documentation/3d_axis_control_handoff.md +
                  documentation/HANDOFF_item19_axis_control_orrery_v1.md
This doc: closes Phase A; sets up Phase B (Studio read-on-load).

--------------------------------------------------------------------------
## 1. What shipped (Phase A)

A user-settable grid-spacing (dtick) override on the ORRERY generation side,
at parity with Gallery Studio. A blank field keeps Phase 2's auto_dtick; a
positive value overrides the grid spacing. Threaded into all three live
build_scene call sites and exercised through a single GUI field.

Round-trip note: the Studio HALF of the round trip was already complete at
2f40d9d (scene_axis_range / scene_dtick fields, apply_config override,
collect/apply config -- landed March). Phase A added the missing orrery half.
The orrery already had a user-settable RANGE (scale_var Manual +
custom_scale_entry); the gap was a user-settable DTICK. That is what Phase A
fills.

Seven edit groups, all palomas_orrery.py (Mode 1, one transactional patch):

  - GUI widget: custom_dtick_entry (tk.Entry) + label + km-equivalent tooltip
    in scale_frame, just below custom_scale_entry.
  - Reset: _set_entry(custom_dtick_entry, '') -> blank = auto on Reset.
  - S1 read (plot_objects): parse custom_dtick (blank/0 -> None; >0 -> float).
  - S2 read (animate_objects): same parse (parallel pipeline).
  - S1 + S2 threads: dtick=custom_dtick added to both build_scene calls.
  - S3 (exoplanet static): the bare inline scene=dict(...) replaced by
    build_scene([-exo,exo], camera=..., domain=..., auto_dtick=True,
    autorange=False, dtick=custom_dtick). Kills the separate inline path and
    closes a parallel-pipeline divergence (exoplanet ANIMATION already routed
    through S2 build_scene; exoplanet STATIC did not -> static grids were
    AU-coarse). build_scene_axes emits the same 'X/Y/Z (AU)' titles, and
    update_layout merges, so camera/domain/theme are preserved.

--------------------------------------------------------------------------
## 2. Verified map (at 1c08a8a -- current line numbers)

Three live build_scene call sites, all now threading dtick (AST-confirmed):

  S1  ~5720  plot_objects     main solar-system scene
  S3  ~5998  plot_objects     exoplanet local-frame scene (migrated this phase)
  S2  ~7955  animate_objects  main animation scene

  dtick reads:  S1 ~5228, S2 ~7929
  GUI field:    ~10300 (custom_dtick_entry in scale_frame)
  Reset:        ~8328

OUT of scope (by decision, unchanged):
  S4  ~7610  animate_objects  per-frame track-camera layout (_track_axis /
             _track_dtick). Camera-tracked animations compute their own grid
             and ignore the field. This is the Phase-2 boundary (the
             per-frame autorange residual is a separate dedicated session).

--------------------------------------------------------------------------
## 3. Correction to a Phase-A design caveat (important, recorded)

During design I flagged that a manual dtick would be a no-op under Auto scale
("axis_range is None -> build_scene nulls dtick"). Tony's Studio experience
contradicted this, and the trace proved Tony right:

  - calculate_axis_range_from_orbits NEVER returns None -- it returns a
    concrete data-fit range, a barycenter-children range, or a [-1, 1]
    fallback (no orbital data). get_animation_axis_range has the same [-1, 1]
    fallback. add_center_body_shells returns a concrete range.
  - So axis_range is ALWAYS a concrete cube at the call sites under Auto OR
    Manual. The dtick override applies in both -- exactly the "leave it on
    Auto, just give me a finer grid" workflow.
  - The build_scene None-guard (481-483) is purely defensive; no orrery path
    feeds it None.

No logic changed from this correction -- only the tooltip and four comment
blocks, which now say the override works under both Auto and Manual scale.
(Lesson: Observation Override -- when Claude explains away what Tony's eyes /
experience report, that is the moment to verify the claim, not the report.)

--------------------------------------------------------------------------
## 4. Verification

Claude-side gate (sandbox; full app launch not possible there -- tk /
astroquery / customtkinter absent, Horizons network-gated):
  - py_compile PASS on the committed bytes at 1c08a8a.
  - ASCII-only + LF on all new lines.
  - AST: exactly 3 build_scene calls (S1/S2/S3), all thread dtick.
  - Real-builder assertions (extracted build_scene): blank -> auto;
    value -> override beats auto; exoplanet range -> readable; None-range
    -> no-op (defensive); S3 titles preserved as X/Y/Z (AU).
  - Round-trip: repo diff 30840b1 -> 1c08a8a == the delivered patch exactly
    (nothing extra, nothing dropped); remote HEAD matches.

Mode-5 render gate (Tony, 1c08a8a) -- ALL PASS:
  1. Regression: normal plot, dtick blank -> grid unchanged.
  2. Auto + finer dtick: Auto scale + a dtick -> grid refines on the auto cube.
  3. Manual close-approach: Manual ~0.003, blank -> readable; dtick 0.0005
     -> tightens.
  4. S3 exoplanet -- readable, labels X/Y/Z (AU), camera/theme unchanged,
     BOTH static and animated (Proxima ~+/-0.0583 AU).
  5. Animation (S2): free-camera animation + dtick -> spacing holds.
  6. Reset clears the field.

--------------------------------------------------------------------------
## 5. Phase B -- next session (Studio read-on-load)

Goal: make the round trip VISIBLE. Today, loading a raw orrery file into
Studio resets scene_axis_range / scene_dtick to 0 ("keep figure values"),
so the GUI shows 0 even though the figure carries a real baked grid. The
data round-trips; the display does not. Phase B reads the figure's
scene.xaxis range + dtick into the two fields on load, so Tony sees the
orrery's grid and refines from there.

Verified Studio touch points (at 2f40d9d -- re-pull and re-confirm at
Phase-B session start, do not trust these line numbers cold):
  - gallery/tools/gallery_studio.py
  - DEFAULT_CONFIG / PORTRAIT_CONFIG: scene_axis_range, scene_dtick (~95-96,
    ~169-170), default 0.0 = "keep figure values".
  - apply_config override block (~943-985): fires only when range>0 OR
    dtick>0; applies range + dtick + km-suffix titles to all three axes;
    uses the SHARED _calculate_grid_dtick.
  - _do_load (~5741-5813): the raw-orrery branch calls
    _apply_config_to_gui(DEFAULT_CONFIG) -> this is where a read-on-load
    populate would slot in.

OPEN DECISION for Phase B (still unmade): the km-suffix.
  Studio's override appends "(grid: N km)" to axis titles; the orrery does
  not. If Phase B populates the fields and the override fires on load,
  loaded plots gain a suffix the orrery never wrote -- a small render
  divergence. Decide: let Studio annotate (informative), or suppress to
  match the orrery exactly.

Suggested Phase-B design (one clean approach): read the figure's grid into
the fields on load; keep the >0 override semantics; when the user does not
change them, re-applying the figure's own values is idempotent. Sentinel
edge: figure with no explicit dtick -> leave field at 0 (auto/inherit).
Render gate: load the Artemis-II / Apophis-style close-approach export,
confirm the fields show the orrery's grid and a refine still works.

--------------------------------------------------------------------------
## 6. Observations (pre-existing, NOT Phase A -- triage)

Seen in the Phase-A render log; none caused by Phase A:
  - Exoplanet ANIMATION: "id_type (host_star) not allowed" ValueError when
    fetching a Horizons trajectory for the host star (proxima_star). The
    animation still produced exoplanet traces. Looks like a genuine
    exoplanet-animation bug -- confirm whether already tracked; if not,
    it wants a ledger line.
  - Exoplanet static: "No handler for object type 'exo_host_star' /
    'exoplanet'" -- the exoplanet path renders separately; benign, known.
  - Artemis II animation: "No ephemeris ... after 2026-APR-10" when the
    cache tries to extend to 2027 -- data-availability limit (Artemis II
    ephemeris ends Apr 10), not a code defect.
  - CAD: "HTTP Error 400" for des=-1024 near Moon -- pre-existing CAD API
    issue; falls back to [RESOLVE] derived time and works.

--------------------------------------------------------------------------
Written June 2026 with Anthropic's Claude Opus 4.8, in the Paloma's Orrery
double-helix workflow: Claude proposes, Tony verifies + applies + renders,
the render is ground truth. SHA chain: 30840b1 -> 1c08a8a.
