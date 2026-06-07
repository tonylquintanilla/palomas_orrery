# v21 ERRATUM + D-URANUS "now"-scope close (June 1, 2026)

**Session model:** Claude Opus 4.8
**Type:** D-URANUS implement session (the "now" half). Two files edited
(`uranus_visualization_shells.py`, `idealized_orbits.py`); both compile,
ASCII-clean, LF. No rendered geometry or hover *data* changed (U1 is a 1-deg
value swap in an existing string; everything else is comments/tags).
**Integrator:** Tony Quintanilla

---

## CORRECTION to the v21 D-URANUS design (U3 premise was wrong)

v21 said: "the correct pole-vector transform already exists in
idealized_orbits.py (the moon-orbit path); extract the inline
equatorial->ecliptic transform (L683-718) into `orient_to_planet_pole()`
and route belts + rings through it -- a clean swap reusing an eye-verified
producer."

**This is false at the code level, confirmed by grep at the head of this
session (the deferred first-action grep doing its job):**

- The block v21 named, L683-718, lives inside
  `test_uranus_equatorial_transformations` -- **0 live callers. Dead code.**
- The LIVE Uranus moon producer is `plot_uranus_moon_osculating_orbit`
  (idealized_orbits.py, called at L4969). It applies **NO pole transform**.
  Its docstring: the osculating elements come from JPL Horizons *already in
  J2000 ecliptic*, so it runs the standard Keplerian sequence only
  (`# NO Uranus rotation - osculating already in ecliptic!`).
- `planet_poles['Uranus']` appears in the module **exactly once**, inside
  that dead test function. **No live code applies Uranus's pole vector to
  any geometry.**

So the moons render correctly because of the **data source** (ecliptic
Horizons elements), not a reusable transform. There is no eye-verified
producer to extract. The handoff's chain "moons track right -> they are the
reference frame -> extract that transform" breaks at the last link: the
eye-verified render contains no transform.

**Corrected fix (still deferred, now paired with item 24):** AUTHOR a new
`orient_to_planet_pole(x, y, z, planet_name)` from the IAU pole vector
(RA 257.43 / Dec -15.10), route the belt and ring builders through it, retire
the 105. It is NEW derived code **validated by render** -- it does NOT inherit
trust from the moon path. The pole-vector math in the dead test block (and the
dead `test_triton_rotations` "Neptune Pole" Euler block) is usable as
*reference only*. The open frame question is ANSWERED: both belts and rings are
built in the body-equatorial XY plane before rotation (belt:
`x=r cos, y=r sin, z` ripple; ring via `create_ring_points`: `x=r cos,
y=r sin, z~0`), so ONE producer serves both (and the bow shocks as the third
consumer). No pre-step needed -- the inputs already share the frame.

Tony's framing (June 1): rely on Horizons data + clean physics over eyeballed
alignment. The moon path already embodies this and is left untouched (gold
standard). The belt/ring fix replaces the fitted 105 with a value DERIVED from
the authoritative pole vector. Caveat recorded: belts/rings have no observational
data of their own, so the render still confirms -- but the alignment number is
derived, not eyeballed.

---

## DONE this session (the "now" half of D-URANUS)

`uranus_visualization_shells.py`:
- **U1 (value): load-bearing `magnetic_tilt_deg` HELD AT 60, on a
  significant-figures argument.** This was decided in two steps. First pass set
  it to 59 (reasoning: 59 matches the `# Source` comment; 58.6 is false-precise
  without Ness provenance). Tony then challenged the premise: maybe Ness reported
  60 precisely *because* a single Voyager-2 flyby's tilt determination does not
  justify sub-degree precision -- in which case 60 is the metrology-honest figure
  and BOTH 59 and 58.6 are spurious digits, not "refinements." Conceded: claiming
  60 was "outreach rounding" was itself an unprovable assertion about the authors'
  intent (the same cite-over-recalled error, one layer up). The matter is a
  sig-figs question, not a "refined beats abstract" question. **Resolution: one
  significant figure -> 60.** All displays now read "~60 deg"; the load-bearing
  value is 60 (L509); Source comments read "~60 deg" (L440, L560, L569); the
  provenance comment (L520-526) now states the sig-figs reasoning explicitly
  ("60, ~59, and 58.6 are the same measurement; 58.6 is spurious digits"); the U2
  block references "~60 deg, one sig fig." L446 prose hedge "nearly 60" left as-is
  (consistent). The honest unresolved sub-question, if ever revisited: the
  *reported uncertainty* on the Ness value was not sourced this session -- finding
  the primary value WITH its error bar is a "source it first" task that would
  confirm the sig-figs call empirically rather than by argument.
  **Lesson:** do not narrate an author's intent behind a published figure
  (neither "they rounded for outreach" nor "59 is the refinement") without the
  source's stated uncertainty in hand. The sig-figs framing is the honest default
  when the error bar is unknown -- display the precision the measurement supports,
  not more.
- **U2 (sign): CLOSED by convention.** 6-line comment at the
  `magnetic_tilt_deg` site recording that the dipole LEAN SIGN is a display
  convention (no axial-rotation model -> azimuth undefined), magnitude is
  sourced, reopen if axial rotation is ever modeled, and N13 (sweep-cone) is the
  planned honest visualization. No sign edit.
- **U4 (comments): 5 copy-paste "Saturn" -> "Uranus" fixes** (belt-axis comment,
  ring docstring x2, ring-param comments x2). The 10 legitimate Saturn
  *comparisons* (atmosphere banding, radiation-belt intensity, E-ring color) and
  the L1073 "mirrors Neptune 2C and Saturn" fix note were left untouched.

`idealized_orbits.py`:
- **7 dead-code tags** (no logic changed). Standalone:
  `test_uranus_equatorial_transformations`, `test_uranus_rotation_combinations`,
  `test_triton_rotations`, `create_planet_transformation_matrix`. Dead chain
  (tagged with chain note): `debug_satellite_systems` (dead root) ->
  `debug_mars_moons` -> `debug_planet_transformation`. Each tag names why it is
  dead and points to the live path; the three pole-vector experiments are
  flagged as NOT live producers (the exact recurrence-stopper for the v21 error).

Verification: `py_compile` clean on both; ASCII-clean; LF. No xvfb (nothing
changed rendered geometry or hover data -- U1 is a value swap inside an existing
string; U2/U4/tags are comments).

---

## STILL OPEN in D-URANUS (deferred, own session)

- **Belt/ring clean-physics producer** (the corrected U3) -- NOT STARTED. The
  105 deg fudge is STILL LIVE in the file as of this session: `uranus_tilt =
  np.radians(105)` at L643 (belts) and L1023 (rings), with describing comments at
  L642/L763/L772. This session DIAGNOSED and DESIGNED the fix only; it removed
  nothing. The task: author `orient_to_planet_pole`, route belts + rings through
  it, then retire the two 105 assignments. Validated by render.
  (Wording caution: earlier summaries said "retire the 105" as the plan -- that is
  future tense. The 105 is present and rendering until this task runs.)
  Pair with item 24 (bow shocks = second consumer) per v21. Internal pole-value
  inconsistency to reconcile while there: Dec -15.10 (L49 planet_poles) vs prose
  "RA 257.31 / -15.18" elsewhere -- ~0.1 deg.
- Cosmetic 18 (gossamer ring visibility), N2 (ring marker placement) -- unchanged.

## Backlog touched
- N12 (pole markers), N13 (dipole sweep-cone) -- referenced in the U2 comment as
  the planned refinement; still Bucket B.
