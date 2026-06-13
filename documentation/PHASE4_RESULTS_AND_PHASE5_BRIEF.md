# PHASE 4 MODE-5 TEST RESULTS + PHASE 5 BRIEF

Tony Quintanilla, PE | Prepared by Claude Sonnet 4.6 | June 13, 2026
Repo HEAD: ec333dff4baa422b80380a114e420f96ec75f10b

---

## PART 1: PHASE 4 MODE-5 GATE RESULTS

### Engine: PROVEN

M1 Earth heliocentric magnetosphere: PASS. Magnetotail anti-sunward
throughout the orbit, bow shock faces the Sun at every frame. No visible
seam, flicker, or geometry pop between frames -- d7 rounding invisible.
Camera tracking via Fly To zooms to full magnetosphere detail; full view
zooms back correctly.

M2 Mercury magnetosphere + sodium tail: PASS. Both sun-dependent per-frame
elements track anti-sunward simultaneously on one body, fast orbit. Engine
handles 4 element groups (rotation axis, sodium tail, magnetosphere, Sun
direction), 88.5 KB/frame, 15 frame-updated traces. Comprehensive engine
proof.

M4 Earth-centered magnetosphere: PASS. Magnetosphere tail tracks the Sun
as it orbits Earth (center body case: get_center_engine_elements owns
magnetosphere). Sun Direction indicator tracks. Rotation axis stays fixed
(inertial, correct physics).

M5 Magnetosphere opt-in OFF (null test): PASS. Magnetosphere renders but
stays frozen at frame-1 orientation. Legend shows the magnetosphere entry
correctly (it renders; it just does not move). The third-consumer fix
(legend placeholders) works as designed -- the magnetosphere does not
vanish with the box off.

H1 Inertial note: PASS. Rotation axis hover text carries the animation
orientation-fixed disclosure (Envelope style).

E1 Epoch parser: PASS. Zero instances of "[KEPLERIAN POS] Could not parse
epoch date" across three runs (MAPS Earth-centered, MAPS Sun-centered,
Mercury Sun-centered). The fix landed: _parse_osc_epoch handles all three
format forms, and the silent J2000 fallback is retired.

R1 Ikeya-Seki regression: PASS. Tails swing beautifully at perihelion.
No regression from rounding or opt-in gate changes.

### Camera/grid: works but needs the comprehensive axis control

Two diagnosed issues, both deferred to item 19:

1. PER-FRAME DTICK MISMATCH: when the user starts playback from a
   different view scale (e.g. "Return to Full View" at 0.004 AU, then
   Play expands to the 0.1 AU tracking window), the dtick from the prior
   view persists, producing a dense grid. Root cause: _track_frame_layout
   carries ranges but not dtick. The _zoom_dtick is computed (L8031) but
   not threaded into per-frame layouts. Fix belongs with the comprehensive
   GUI axis controls (scene_axis_range, scene_dtick) mirroring Gallery
   Studio, so the per-frame tracking consumes those controls consistently.

2. FLY TO MISSING TARGET: Mercury Fly To does not render Mercury at all --
   the zoom lands at coordinates where the body is not visible, and
   changing zoom depth does not fix it. Pre-existing at other scales.
   Same item 19 family: the Fly To distance formula, range computation,
   and shell-aware sizing all need the comprehensive review.

A full ledger amendment for these findings is prepared
(LEDGER_AMENDMENT_tracking_dtick.md) with the Gallery Studio reference
implementation (L4162-4200) and the three additive sub-items for item 19.

### MAPS: confirmed deferred (not a regression)

MAPS plotted with "Animate comet tails" both ON and OFF produces no comet
tails in either case. This is the expected behavior per ADDENDUM decision 1:
the two exclusion sites (L2209 engine collection, L7269 frame-1 skip block)
remain in place. The disintegration-mode code path is separate from the
standard comet tail builder. Ikeya-Seki confirms the standard pipeline is
clean.

### Pre-existing bug surfaced

idealized_orbits.py L7076: NameError: name 'color' is not defined in
plot_hyperbolic_osculating_orbit. Caught by try/except -- the Earth-centric
hyperbolic osculating orbit marker for MAPS is silently absent. Pre-existing,
not Phase 4. Ledger candidate for the MAPS maintenance session.

### Overall Phase 4 gate: PASS

The engine is comprehensively proven (4 element groups on Mercury, center
body tracking on Earth, null test clean, regressions clean, epoch parser
fixed). Camera/grid refinement is a known follow-on, properly scoped in
item 19. The animation refactor's core track is COMPLETE through Phase 4.

---

## PART 2: PHASE 5 BRIEF -- Plot-Cube Control, MAPS Completion, and Structural Cleanup

### The goal

Three tracks in one comprehensive session.

TRACK 1: Every scale-dependent rendering problem diagnosed across the
animation refactor (Phases 1-4) traces to one architectural gap: the
orrery GUI has no explicit user control over axis ranges, grid tick
spacing, or scale-aware camera positioning. Gallery Studio solved this
(scene_axis_range, scene_dtick, L4162-4200); the orrery GUI never
received the same treatment. Phase 5 closes that gap.

TRACK 2: MAPS per-frame comet tails -- the deferred completion of the
comet feature. Standard comets work (Ikeya-Seki proved it); MAPS is the
remaining gap. The partition design and exclusion-site warnings are
captured in ADDENDUM_phase4_decisions.md.

TRACK 3: Structural cleanup -- dead code, dead imports, ASCII violations,
line ending fixes, and verify-and-close items that a fresh model can
settle in a single pass.

## TRACK 1: PLOT-CUBE CONTROL AND CAMERA SYSTEM

This is item 19 from the ledger, now carrying the full fixture list
accumulated across Sessions A through Phase 4 Mode-5 testing:

### The fixture list (from the ledger, all item 19)

1. ORRERY GUI AXIS CONTROLS: scene_axis_range (symmetric +/- AU, 0 = auto)
   and scene_dtick (grid tick spacing AU, 0 = auto-calculate from range)
   in the animation settings panel. Mirroring Gallery Studio's proven
   implementation. Reference values in tooltips (Studio already has these:
   0.003 for Moon orbit, 0.001 for GEO belt). Auto-calculate dtick from
   range when dtick is 0 (Studio pattern: _calculate_grid_dtick, ~6
   gridlines across the view).

2. PER-FRAME DTICK THREADING: _track_frame_layout must carry dtick
   alongside ranges, either from the new GUI control or auto-calculated
   from _track_radius via _calculate_grid_dtick. The auto-calculation
   already exists (_zoom_dtick at L8031); it needs to flow into
   the per-frame layouts. Fixes the dense-grid anomaly.

3. FLY TO SHELL-AWARE SIZING: the static Fly To buttons
   (add_fly_to_object_buttons in visualization_utils.py L363) still use
   the orbital-distance formula. Port the shell-aware sizing (120x body
   radius when shells are checked) to the static buttons, consuming
   fig._shell_outermost_radius_au where set. One producer, two consumers
   (static Fly To + per-frame tracking).

4. FLY TO DISTANCE FLOOR: the orbital-distance formula
   (0.1 + dist * 0.05) has a 0.1 AU floor that dominates for close bodies.
   The Moon at 0.00257 AU -> 0.1 AU window (25x wider than the natural
   view). Mercury at shell scale similarly. The floor was designed for
   heliocentric distances. For close bodies, the floor should scale with
   orbital distance or natural view range, not be a fixed 0.1 AU.

5. FLY TO MISSING TARGET: Mercury Fly To does not render Mercury at all.
   The zoom/range calculation lands where the body is not visible. Root
   cause analysis needed: is the range correct but the camera center
   wrong? Is the body's position at a different coordinate than the
   range center? Diagnosed in Phase 4 M2 testing.

6. PHOTOSPHERE AUTO-SCALE COLLAPSE: static Auto = shell extent alone,
   hiding orbits (Session A Finding 1). The Session C fix
   (max(orbital, shell)) addressed the animate pipeline; verify the
   static pipeline has the same treatment.

7. SUN ORBIT CUBE BUFFER: Sun orbit around a planet center lacks
   sufficient cube buffer (O12).

### Completion riders (bundle if scope permits)

- 3D DIRECTIONAL ARROW CAMERA CONTROLS for Plotly 3D: precise camera
  positioning without the mouse. Studio has 2D D-pad pan; no 3D
  equivalent. Aids shell-scale visual verification. (Promoted June 11.)

- O14/O15 verdicts: comet-tail legend churn; sodium particle count
  (rounding now takes 500 particles to ~31 KB/f, which may settle O15
  without the knob).


## TRACK 2: MAPS PER-FRAME TAILS (completing the comet feature)

MAPS was deferred from Phase 4 per ADDENDUM decision 1. The partition
design and exclusion-site warnings are captured in ADDENDUM_phase4_decisions.md
(section "Captured for the MAPS deferral"). This track completes the comet
tail per-frame feature: standard comets work (Ikeya-Seki proved it); MAPS
is the remaining gap.

### What needs to happen

1. TWO EXCLUSION SITES must change IN LOCKSTEP:
   - palomas_orrery.py L2209 (engine comet collection -- obj_name != 'MAPS')
   - palomas_orrery.py L7269 (frame-1 skip block)
   Both match the literal string 'MAPS'. Grep-confirm both at edit time.
   If one changes and the other doesn't: the C2a doubling disease returns,
   or a dead-slot absence.

2. CLEAN PARTITION (from the ADDENDUM):
   - Engine owns ONLY the pre-disintegration active-comet traces (standard
     builder, date-gated). After the disintegration date, those slots pad
     to explicit-invisible dummies (the sticky-visible fix makes this safe).
   - Static frame-1 keeps the ghost tail and disintegration marker.
   - The vanishing tail at disintegration is correct physics -- and the
     best educational moment in the comet track. The pad-to-invisible
     mechanism that was a bug fix in 3C2 becomes the storytelling device.

3. GHOST-TAIL DESIGN CALL: static is the default. The only physically
   honest animated alternative is a GROWING debris arc (leading edge
   advancing along the Barker trajectory past the disintegration date).
   Deferred unless Fable 5 sees a clean implementation. Record the
   decision either way.

4. TRACE-COUNT INVARIANT: if the animation window spans the disintegration
   date, MAPS switches modes mid-animation. The builder must emit a
   consistent slot set across that boundary (pad-to-max, same as the
   standard variable-count handling in Phase 3 Session C).

### Bundled MAPS fixes

- idealized_orbits.py L7076: NameError: name 'color' is not defined in
  plot_hyperbolic_osculating_orbit. Pre-existing. The Earth-centric
  hyperbolic osculating orbit marker for MAPS is silently absent. Define
  the color variable from the function's parameters or trace color scheme.

- comet_visualization_shells.py L257/505/519: 3 em-dash characters
  (ASCII-convention violation, pre-existing). Fix with binary-mode
  replacement on next touch of this file -- and this IS a touch.


## TRACK 3: STRUCTURAL CLEANUP SWEEP

Mechanical items from D.Structural that a fresh model can verify and close
in a single pass. All are grep-confirm-then-delete or verify-and-close.

### Dead code removal

- Item 5: dead imports.
  * hover_text_sun import (~L208 in the shells file, unused since
    Phase 2a single-marker refactor)
  * helpers' create_planet_visualization import (unused since Phase 2.5
    wrapper retirement)
  Grep-confirm zero callers, then delete.

- Item 6: archive the retired create_planet_visualization function body.
  Annotated RETIRED June 10 with zero pipeline callers (confirmed by
  repo-wide grep of 3 sites, all switched to unified dispatch). Delete
  with grep-confirm. The helpers' dead import (item 5) joins this.

- Item 8: dead create_sun_direction_indicator imports. The old version
  in planet_visualization_utilities.py (L378, create_sun_direction_indicator_old)
  was replaced by shared_utilities.py version. Verify no remaining callers,
  then delete or annotate.

### Verify-and-close (quick, a fresh pair of eyes can settle)

- Item 13: Neptune ring info-marker rotation -- verify the marker
  placement is correct and close.
- Item 28: Neptune superimposed info markers -- verify not superimposed
  and close.

### Console polish

- O2/O3 notice wording: when magnetosphere opt-in is ON, the blanket
  "[ANIMATION] NOTE: shells checked for non-center bodies ... not yet
  rendered" still prints for sphere shells, while the engine correctly
  prints its own magnetosphere allocation lines. Amend the notice to
  exclude engine-owned elements from the "not yet rendered" claim.

- palomas_orrery_helpers.py: CRLF -> LF line endings (item 9).
  Binary-mode read/write.

### Key files and locations

    palomas_orrery.py:
        L2209  MAPS exclusion -- engine comet collection (obj_name != 'MAPS')
        L7269  MAPS exclusion -- frame-1 skip block
        L7509  _track_body setup + _track_frame_layout (Phase 4)
        L8031  _zoom_dtick computation (not yet in per-frame layouts)
        L7826  add_fly_to_object_buttons (animate path)
        L5902  add_fly_to_object_buttons (static path)

    visualization_utils.py:
        L83    add_camera_center_button()
        L363   add_fly_to_object_buttons() -- the static Fly To
        L??    _calculate_grid_dtick() -- the auto-calculator

    gallery_studio.py (reference implementation, website repo):
        L95-96    DEFAULT_CONFIG: scene_axis_range=0.0, scene_dtick=0.0
        L940-986  Application: effective_dtick, auto-calculate, apply
        L4162-4200 UI: "Axis range +/-" and "Axis dtick" fields
        L2416-2433 JS reset: camera + axis ranges; zoom uses dtick

    shared_utilities.py:
        L25    create_sun_direction_indicator() -- already consumes
               axis_range for the clamp (Phase 4); will consume the
               new GUI controls

    comet_visualization_shells.py:
        L487   create_maps_disintegration_marker()
        L580   create_maps_ghost_tail_trace()
        L1602  add_comet_tails_to_figure() -- main builder (fig-mutating)
        L2090  build_comet_tail_traces() -- engine capture shim
        L257/505/519  em-dash ASCII violations (binary-mode fix)

    idealized_orbits.py:
        L7076  plot_hyperbolic_osculating_orbit -- 'color' NameError

    palomas_orrery_helpers.py:
        CRLF -> LF conversion (item 9)

    planet_visualization_utilities.py:
        L378   create_sun_direction_indicator_old() -- dead, verify + delete
        L208   hover_text_sun import -- dead since Phase 2a

    planet_visualization.py:
        create_planet_visualization -- annotated RETIRED, delete with
        grep-confirm (item 6)

### Constraints

    Same load-bearing constraints as Phase 4 (ASCII, LF, py_compile,
    bottom-up editing, verify execution not appearance).

    Additional for this scope:
    - Changes to visualization_utils.py affect BOTH pipelines (static
      and animate) and Gallery Studio's import of _calculate_grid_dtick.
      Verify all three consumers.
    - The Fly To buttons are generated via Plotly updatemenus
      (JavaScript-level relayout). Changes to zoom logic must work in
      the JS relayout path, not just Python figure construction.
    - Gallery Studio's axis controls are the REFERENCE, not a constraint.
      The orrery's controls may need different defaults, ranges, or
      behavior (e.g. per-frame propagation, which Studio doesn't have).
      Improve on the reference where the orrery's needs differ.
    - MAPS exclusion sites must change IN LOCKSTEP (L2209 + L7269).
      Grep both before and after editing.
    - Dead code deletion: grep-confirm zero callers BEFORE deleting.
      The protocol says annotate first, delete with confirmation.
    - Binary-mode (rb/wb) for the em-dash fix and the CRLF conversion.

### What this session should produce

    At minimum:
    - GUI axis controls (scene_axis_range, scene_dtick) in animation
      settings panel
    - Per-frame dtick threading (dense grid fix)
    - Fly To shell-aware sizing for static buttons
    - Fly To distance floor fix for close bodies
    - MAPS per-frame tails (pre-disintegration wiring, lockstep exclusion)
    - idealized_orbits color fix
    - em-dash ASCII fix in comet_visualization_shells.py
    - Dead code removal (items 5, 6, 8)
    - helpers CRLF -> LF (item 9)

    At best (think ambitiously):
    - All of the above
    - Root cause and fix for Fly To missing target (Mercury)
    - Photosphere auto-scale parity between static and animate
    - 3D directional camera controls
    - A unified scale-management architecture that makes the
      relationship between axis range, dtick, camera distance, and
      shell extent explicit and consistent across all view modes
    - MAPS ghost-tail growing-arc implementation (if clean)
    - Neptune verify-and-close items (13, 28)
    - O2/O3 console notice amendment
    - Any architectural improvements visible to someone seeing the
      scaling and comet code fresh

    The render is the proof. Tony will verify Mode 5.


Module updated: June 2026 with Anthropic's Claude Sonnet 4.6
