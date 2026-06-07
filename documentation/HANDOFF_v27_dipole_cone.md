# HANDOFF v27 -- Dipole Cone (Movement 2, sub-item 2)

**Date:** June 6, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v26 -- single running ledger. The v26 rotation-axis track, the
v25 N15 ring-plane track, the v24 bow-shock / magnetosphere track (Movement 1),
and the v23 shell-consolidation D-track all remain authoritative by reference
and were untouched except the two magnetosphere hover edits in Section 6.
Nothing renumbered.
**Type:** CODE CHANGED, TESTED, RENDER-CONFIRMED on Uranus + Neptune (Mode 5).
All six files compile, ASCII-clean, LF. Builder geometry verified in-container
against the real module code; live-dispatch smoke PASS in Tony's env. ONE
exception: the cone does not yet appear in ANIMATION frames -- a parallel-
pipeline gap, deferred (Section 4).
**Built on:** GitHub repo HEAD `de12f5635a6f04c36b9e62509f24e517cce7ad07`
(v26 push). Round trip confirmed at session start (remote HEAD == base).
**Pushed at (new HEAD):** `c25bdd7d9267b4cfd43e3c8df021917bd1a49745` -- next
session's base. Round trip confirmed: remote HEAD moved de12f56 -> c25bdd7,
commit + push + project-knowledge sync in one check.
**Integrator:** Tony Quintanilla

> **The second DIRECTED consumer of the N15 pole vector.** After the rotation
> axis (v26), the dipole cone is the magnetic dipole's honest visualization:
> the body-fixed dipole sits at a fixed tilt from the spin axis but is carried
> around it by the planet's rotation, so over one day the dipole axis sweeps a
> cone about the spin pole. We draw that cone (double nappe), one arbitrary
> instantaneous dipole generator, and a sweep arrow at each tip that rides the
> cone rim and rhymes with the rotation-axis spin arrow -- so the dipole's
> sweep reads as the same rotation. Small in code; the meaningful part is the
> design conversation that established WHY the cone, not a single axis, is the
> honest object.

---

## 1. WHAT THIS SESSION DID

**Dipole cone across the two dipole bodies with a sourced tilt** -- Uranus
(60 deg, Ness et al. 1986) and Neptune (47 deg, Ness et al. 1989). Other
magnetized bodies deliberately omitted pending sourced data (Section 4).

Design (converged sketch-first over several rounds, then built):
- **One shared builder** `build_dipole_cone_traces` in
  `planet_visualization_utilities.py`. Pole-frame: consumes the IAU spin pole
  from `create_planet_transformation_matrix` (the N15 producer), so it sits
  square to the rings and radiation belts.
- **Double-nappe cone**, half-angle = the dipole tilt, apex at center. The
  dipole is two-ended, so two nappes (an hourglass about the spin axis).
- **One instantaneous dipole generator** at an arbitrary azimuth, plus a
  **sweep arrow at each tip** that rides the cone RIM (a circle about the SPIN
  axis), with the same sense and absolute arrowhead size as the rotation-axis
  spin arrow. The two arrows rhyme so a viewer reads them as one rotation. The
  single line stops asserting a fixed azimuth and instead asserts motion --
  the honest claim, since the azimuth is unrecoverable (Section 2).
- **Body-triggered**, like the rotation axis: renders once per plotted body
  that has a sourced dipole, own legend entry, toggles as a unit. NOT a shell
  checkbox (excluded from the shell loop).
- `sense` and `half_len_frac` are read from `PLANET_ROTATION` (single source of
  truth); `PLANET_DIPOLE` carries only tilt + arbitrary azimuth + source.
- **Apex at center; the dipole center offset is DEFERRED** -- magnitude sourced
  (~0.3 R_U Uranus, ~0.55 R_N Neptune), direction not (Section 4).

**Magnetosphere envelope honesty disclosure** (a Movement-1 hover edit, Uranus
+ Neptune): the envelope hover now states the shape is a schematic -- standoff
and dipole tilt/offset sourced (Slavin 1987, Ness 1986/1989), oblateness and
tail dimensions flagged as representative values within Voyager-era ranges,
dipole roll direction flagged as a fixed display choice -- and points to the
Dipole Cone for the honest sweep. Fixes a silence, per the principle in
Section 2.

**Render-confirmed (Tony, Mode 5):** Neptune (47 deg hourglass, square to the
rings), Uranus (edge-on -- the cone opens nearly horizontal off the sideways
spin axis), spin arrow and sweep arrow reading as one rotation. PASS for static
plots. The cone does NOT appear in animation frames (Section 4, deferred).

**Also this session (protocol, not orrery code):** protocol updated to **v3.28**
-- added "Live repo vs snapshots" (Context Priority + SHA Round Trip) and the
"Show the Envelope of the Unknowable" principle (beside Fetched-vs-Recalled),
removed a duplicate version-history entry, and ran a conservative conciseness
pass (795 -> 784 lines; all 14 CRITICAL gates and rule titles preserved). Built
on the uploaded v3.27 doc (the protocol lives in project knowledge / the working
copy, not pulled from the repo; its header had also lagged at v3.26 and is now
correct). PENDING COMMIT -- commit v3.28 so the doc and its version stamp travel
together; next session uses v3.28.

---

## 2. DESIGN CONVERGENCE / WHY THE CONE (the conversation was the work)

- **The arbitrariness is rotational, not geologic.** The dipole's inertial
  azimuth at a display date depends on the rotation phase, which the orrery
  does not model; the rotation period's uncertainty, compounded over ~20,000
  rotations since Voyager, smears the nominal phase around the full circle. So
  the instantaneous azimuth is UNRECOVERABLE, not merely unmodeled. The cone
  (all azimuths) is the honest object; a single line would assert a phase we
  cannot know.
- **Two cones, kept distinct.** Rotation sweeps the DIPOLE about the SPIN axis
  (this build, ~17 h, half-angle = dipole tilt). Precession sweeps the SPIN
  axis about the ORBIT normal (deferred, Earth/Mars, geologic timescale).
  Tony separated these himself after first conflating them.
- **Frame finding (confirmed in render).** The magnetosphere envelope is
  Sun-frame: nose pinned sunward, oblate cross-section ROLLED about the
  Sun-line by the tilt magnitude, at an azimuth the code itself calls arbitrary
  (U2 note). The rings, belts, rotation axis, and dipole cone are pole-frame.
  These are DIFFERENT frames and are SUPPOSED to differ -- the solar wind
  shapes the boundary, the body-fixed dipole sweeps the cone. The cone is
  Sun-independent; it does not track the envelope, and that non-alignment is
  correct, not a bug.
- **The envelope's 60/47 roll uses the tilt NUMBER but is geometrically
  decoupled from the dipole vector** -- it is a roll about the Sun-line, not a
  placement of the dipole 60 deg off the spin axis, and it is not wired to the
  dipole at all. A frozen stylized still.
- **Principle named by Tony (candidate for the Principles section, near
  Fetched-vs-Recalled):** *Where we have real geometry or physics, use it (or
  the measured range); where the value is unknowable, show the envelope of
  possibilities -- the cone -- rather than fake a point, and say so in the
  hover rather than stay silent.* The cone is to an unknowable azimuth what
  "remove and note the gap" is to an uncited number: honesty about
  indeterminacy. One layer up from Fetched-vs-Recalled.
- **"No body needs a dipole cone."** The whole orrery is chosen for
  communication, not necessity; the cone earns its place in proportion to the
  tilt (dramatic at Uranus/Neptune, a teaching anchor at Earth, degenerate and
  text-only at Saturn). Completeness is not the goal; communication is.

---

## 3. LESSONS / DISCIPLINE

- **Sketch-first, honored literally this time.** Three throwaway sketches
  (cone; dipole-axis-overlay-on-real-geometry; cone + sweep arrow) drove the
  design from renders, not prose. This directly applied the v26 lesson (a
  confident geometric claim argued in prose got retracted); this session the
  picture went first and there was nothing to retract.
- **Verified a duplicate-key scare was a false alarm before asserting it.**
  The `1728/1795` Uranus/Neptune blocks are in SHELL_CONFIGS; the `2466/2538`
  ones are in CUSTOM_SHELLS -- separate dicts, not duplicate keys (unlike the
  real `Sun` duplicate). Checked the dict boundaries first; nearly flagged a
  non-bug as a bug.
- **Builder geometry pre-tested in-container against the REAL module code**
  (stubbed pole + constants): 8 traces, dipole 60.00 / 47.00 deg off the pole,
  two nappes (one legend), two rim arcs winding with the rotation sense, two
  arrowheads; Earth/Mars return []. Compile-clean is not render-clean; the
  geometry was exercised, not just compiled.
- **Live-dispatch smoke** (`smoke_dipole_cone.py`) drives
  `create_celestial_body_visualization` with zero shells -- the v24 lesson
  (test the live trigger, not the builder in isolation). PASS in Tony's env.
- **Mode-5 render is the gate; it passed** for static plots. The animation gap
  is what the render caught that the smoke could not (Section 4).

---

## 4. DEFERRED / LEDGER

**New this session:**
- **ANIMATION parallel-pipeline gap.** The dipole cone does not appear in
  animation frames, and the rotation axis almost certainly has the SAME gap --
  both ride the body-triggered block in `create_celestial_body_visualization`,
  and the animate path evidently does not route through it. ONE fix likely
  covers both. Map the animate dispatch before patching (Check All Parallel
  Pipelines). Deferred per Tony. Most concrete next item.
- **Envelope -> dipole tie / season-derived roll** (Movement-1). Set the
  envelope roll to the dipole's PROJECTION onto the Sun-perpendicular plane,
  collapsing the two arbitrary azimuths (envelope roll + dipole) into one. GATED
  on a Mode-7 physics question: does the magnetopause asymmetry actually track
  the instantaneous dipole projection (along the magnetic equator? the
  projection? mostly solar-wind-set?). Conditional -- only if a season-derived
  roll is wanted; otherwise the frozen still + the new disclosure hover is the
  honest near-term state. Includes a templated narrative line if pursued.
- **Dipole offset DIRECTION** (Mode-7). The Voyager-2 / offset-tilted-dipole
  vector DIRECTION in body frame -- Uranus (~0.3 R_U) and Neptune (~0.55 R_N).
  Magnitude sourced, direction not. Offset stays deferred (apex at center)
  until sourced; do not fake the direction.
- **Other dipole bodies.** Earth (~11 deg -- the compass-vs-true-north anchor,
  worth a skinny cone), Jupiter (~10 deg -- modest, optional, may get lost at
  magnetosphere scale), Saturn (<1 deg -- NO cone; a sub-degree cone is
  degenerate and would imply a sweep that is not there; use a hover NOTE about
  the anomalous spin-axis alignment instead). ALL tilts/sense/poles are
  currently RECALLED and MUST be sourced (primary literature or Mode-7) before
  entering PLANET_DIPOLE. Fetched-vs-Recalled applies exactly as for the
  standoffs. PLANET_DIPOLE is structured to take them.
- **Bow shock hovers** (Uranus 23.7 R_U, Neptune 34.9 R_N) cite their standoff
  but do not flag that the boundary is a conic-section approximation -- a clean
  parallel to the envelope disclosure if wanted.
- **Protocol -> skills refactor** (process / tooling, not orrery code; Tony's
  idea, this session). Anthropic now exposes customizable skills. The protocol
  mixes two layers: resident JUDGMENT (modes, criticality philosophy, Foundation,
  "when unsure ask," the double-helix) that must stay in context, and
  trigger-fired PROCEDURE (docstring standard, agentic pre-test sequence,
  provenance-scanner mechanics, single-info-marker pattern, Horizons center-body
  rules, bottom-up / binary-mode editing) that only matters at the moment its
  task runs. The procedure layer is the spin-off candidate -- a skill loads on
  its trigger and is invisible otherwise: the "stop carrying the reference manual
  in-context" win, and a better factoring (mechanics and philosophy stop sitting
  at equal weight). TWO cautions, both from our own rules: (1) the criticality
  tiers are the sorting key -- CRITICAL gates (SHA round trip, verify-execution,
  enumerate-uploads) must fire RELIABLY, and a skill only fires if its trigger
  matches, so CRITICAL checks stay resident (or keep a one-line resident
  pointer); QUALITY/PRACTICE mechanics are the safe spin-offs. (2) Its OWN
  session, sketch-first: design which skills, what triggers each, and what the
  slimmed resident protocol keeps, BEFORE building -- a skill that fails to
  trigger when needed is worse than a paragraph that is always there.

**Carried from v26 (unchanged):**
- Duplicate `'Sun'` key in CUSTOM_SHELLS (its own ticket; trace the body list).
- ASCII sweep across the tree (`grep -rnP '[^\x00-\x7F]' --include=*.py`).
- Per-body `half_len_frac` tuning -- now also governs the cone (it shares the
  rotation-axis scale; 2.5 R reaches short of the bow shock by design, tunable).

---

## 5. LIVE FLAGS / ASSUMPTIONS

- Dipole cone is **body-triggered** (renders for Uranus/Neptune when plotted),
  own legend entry, legend-toggle as a unit. Mirrors the rotation-axis dispatch.
- `needs_planet_name` (v26) reused; the builder accepts and ignores
  `sun_position` for dispatch-signature uniformity.
- Cone parameters: half-angle = tilt (60 / 47), apex at center, double nappe,
  `AZIMUTH_DEG = 35` (arbitrary), `half_len_frac = 2.5` (= spin axis),
  arrowhead `sizeref = 0.28*half*0.5` (= spin arrow), sweep-arc span 90 deg,
  rim arc about the spin axis, sense from PLANET_ROTATION.
- Color `rgb(255, 93, 210)` magenta -- distinct from rotation-axis gold and
  field blues.
- Envelope hover disclosure: standoff / tilt / offset sourced; oblateness /
  tail / roll flagged approximate; points to the Dipole Cone.

---

## 6. FILES + INTEGRATION (built on `de12f56`, pushed at `c25bdd7`)

- **planet_visualization_utilities.py** -- APPEND `PLANET_DIPOLE` (Uranus 60 /
  Ness 1986, Neptune 47 / Ness 1989), `_DIPOLE_COLOR`,
  `build_dipole_cone_traces` (8 traces; lazy-imports the producer; sense +
  half_len_frac from PLANET_ROTATION). Section credit comment added.
- **shell_configs.py** -- `dipole_cone` CUSTOM_SHELLS entries in the WINNING
  Uranus (line ~2478) and Neptune (~2564) blocks, before each magnetosphere,
  with `needs_planet_name` and a sourced tooltip.
- **planet_visualization.py** -- shell loop now skips
  `('rotation_axis', 'dipole_cone')`; a body-triggered `dipole_cone` render
  block sits after the rotation-axis block, an exact mirror.
- **smoke_dipole_cone.py** (NEW) -- live-dispatch smoke: resolves the builder
  through CUSTOM_SHELLS, asserts 8 traces / on-pole tilt / correct sense, then
  drives `create_celestial_body_visualization` with zero shells to assert the
  cone reaches the render path for Uranus/Neptune (1 legend each) and is absent
  for Earth/Mars/Jupiter/Saturn.
- **uranus_visualization_shells.py** -- magnetosphere envelope hover:
  schematic/approximate disclosure + Dipole Cone pointer.
- **neptune_visualization_shells.py** -- same.

Verification: all six compile; LF; ASCII-clean in changes; builder geometry
in-container PASS; live-dispatch smoke PASS (Tony env); Mode-5 static render
PASS on Uranus + Neptune; animation render DEFERRED (Section 4).

---

## 7. CARRIED FORWARD (by reference; unchanged this session)

- **v26** -- rotation-axis primitive (Movement 2, sub-item 1).
- **v25** -- N15 ring-plane migration + analytical moon-orbit retirement.
- **v24** -- bow shocks + magnetosphere nest (Movement 1).
- **v23** -- shell-consolidation D-track.

---

## 8. NEXT-SESSION PRIORITIES

1. **Round trip already closed this session** (remote HEAD = `c25bdd7`); next
   session pulls and SHA-pins that as its base.
2. **Animation parallel-pipeline gap** -- map the animate dispatch; one fix
   for the rotation axis AND the dipole cone (both body-triggered). The most
   concrete deferred item.
3. **Earth dipole cone** (source the ~11 deg tilt first) -- the compass anchor.
   Jupiter optional; Saturn a hover NOTE, not a cone.
4. **Bow shock hover disclosure** -- parallel to the envelope disclosure.
5. **Envelope -> dipole tie** and **offset direction** -- Mode-7 consults
   when/if pursued; neither blocks anything.
6. **Movement 2 remaining: precession cone** (Earth / Mars; axis = orbit
   normal; geologic-timescale overlay) -- sketch-first.
