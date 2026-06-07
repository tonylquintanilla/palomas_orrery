# HANDOFF v26 -- Rotation-Axis Primitive (Movement 2, sub-item 1)

**Date:** June 5, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v25 -- single running ledger. The v25 N15 ring-plane track, the
v24 bow-shock / magnetosphere track (Movement 1), and the v23 shell-consolidation
D-track all remain authoritative by reference and were untouched (Section 7).
Nothing renumbered.
**Type:** CODE CHANGED, TESTED, RENDER-CONFIRMED on Sun / Mercury / Earth.
All five files compile, ASCII-clean, LF; live-dispatch smoke ALL PASS. PUSH PENDING
(record new HEAD below on push); Mode-5 render sweep of the other 8 bodies pending.
**Built on:** GitHub repo HEAD `17093da` (branch main). Reconciled vs v25's
expected `7140b9c`: the only intervening commit was docs-only
(`project_instructions_v3_27.md`); the seven N15 code files were byte-identical, so
the base is clean.
**Pushed at (new HEAD):** `de12f5635a6f04c36b9e62509f24e517cce7ad07` -- RECORD ON PUSH; next session's base.
**Integrator:** Tony Quintanilla

> **One primitive, the first DIRECTED consumer of the pole vector N15 built.** The
> rotation axis draws each body's spin pole as a line through the body with a
> curved spin-direction arrow at BOTH poles plus one info marker. It is the first
> consumer to use the pole's *direction* (not just its plane), wired as one shared
> builder across all 11 shell bodies. Small in code; the meaningful part is a
> render-path lesson (Section 3) that a green smoke test missed.

---

## 1. WHAT THIS SESSION DID

**Rotation-axis primitive across 11 bodies** -- 8 planets + Pluto + Sun + Moon.
Planet 9 and Eris deliberately excluded (no measured/contested spin); each carries
a "rotation axis omitted: ..." note on its body hover (the gap made visible, not
silent -- Fetched-vs-Recalled).

Design (converged in conversation over several rounds, then built):
- **One shared builder** `build_rotation_axis_traces` in the general module
  `planet_visualization_utilities.py`. No per-body axis code. All 11 bodies point
  a uniform `CUSTOM_SHELLS['<body>']['rotation_axis']` entry at it.
- **Pole from the producer.** Axis line = the IAU pole from
  `create_planet_transformation_matrix` (the N15 producer), so this is a direct
  pole-vector consumer. Extended `planet_poles` with five sourced IAU poles
  (Sun, Mercury, Venus, Earth, Moon) so the producer yields a correct pole for
  every shell body; the prior six were unchanged and cross-checked to IAU.
- **Both-ends arrows** (the key design move). A spin arrow at each pole, both
  encoding the SAME angular-velocity vector (identical circulation in 3-space).
  Seen from opposite poles one rotation reads as mirror images on screen -- which
  is how a rigid spin actually looks. This DISSOLVES the IAU-pole vs
  angular-momentum-pole question: neither end is privileged, so no convention has
  to be chosen or explained. (Venus/Uranus/Pluto would otherwise look "wrong" at
  one end.)
- **Body-triggered, not shell-triggered.** The axis renders once per body in the
  dispatch chokepoint, independent of shell checkboxes (Section 3, the bug).
- **Sourced hover** per the single-info-marker convention: one cross marker at a
  tip carries period / sense / obliquity / note; all geometry is `hoverinfo=skip`.

**Render-confirmed (Tony, Mode 5):** Sun (corona-scale, differential, legend reads
+ toggles, hover exact), Mercury, Earth (canonical 23.4 deg tilt sitting cleanly
against the magnetosphere + bow shock). "Not just right -- beautiful."

**One tuning applied after render:** arrowhead cone halved
(`sizeref = arc_r * 0.45`, was `0.9`).

---

## 2. SOURCED ROTATION DATA (all 11 bodies; source-then-cite gate passed)

Periods + obliquities: NASA NSSDCA Planetary Fact Sheet (Williams, NASA GSFC).
Spin sense: NSSDCA signed period + IAU WGCCRE prograde/retrograde W-dot convention
(Archinal et al. 2018). Poles: IAU WGCCRE (Archinal et al. 2018); Moon mean pole
also cross-checked to the SPICE PCK kernel. Giants cross-checked to Voyager 2
(Uranus: Desch 1986; Neptune: Lecacheux 1993). Sun: Carrington (1863).

| Body | Sidereal rotation | Sense | Obliquity | IAU pole RA/Dec | Pole |
|------|------|------|------|------|------|
| Sun | 25.38 d (Carrington; differential 24.5-35 d) | prograde | 7.25 to ecliptic | 286.13 / 63.87 | added |
| Mercury | 58.65 d | prograde | 0.034 | 281.01 / 61.45 | added |
| Venus | 243.02 d | RETROGRADE | 177.4 | 272.76 / 67.16 | added |
| Earth | 23.93 h | prograde | 23.44 | 0.00 / 90.00 | added |
| Moon | 27.32 d (locked) | prograde | 6.68 to orbit (1.54 to ecliptic) | 269.99 / 66.54 (J2000 mean) | added |
| Mars | 24.62 h | prograde | 25.19 | 317.68 / 52.89 | in base |
| Jupiter | 9.93 h | prograde | 3.13 | 268.06 / 64.49 | in base |
| Saturn | 10.66 h | prograde | 26.73 | 40.58 / 83.54 | in base |
| Uranus | 17.24 h | RETROGRADE | 97.77 | 257.43 / -15.10 | in base |
| Neptune | 16.11 h | prograde | 28.32 | 299.36 / 43.46 | in base |
| Pluto | 6.39 d | RETROGRADE | 122.53 | 132.99 / -6.16 | in base |

Sourcing earned its keep: would have recalled Mercury's Dec as 61.41; the IAU value
is 61.45. **Prograde vs retrograde, defined:** prograde = right-handed spin about
the north ecliptic direction (spin angular momentum points into the northern
ecliptic hemisphere; counterclockwise viewed from ecliptic north). Clean single
criterion: obliquity-to-orbit > 90 deg = retrograde (Venus, Uranus, Pluto). IAU
always names the pole north of the invariable plane as "north," so for retrograde
bodies the IAU north pole is OPPOSITE the angular-momentum vector -- the gap
the both-ends arrows made moot.

---

## 3. REASONING TRAIL, TONY-CATCHES, LESSONS

**LESSON (headline): a green smoke test passed over an axis that rendered nothing.**
The first smoke test resolved `CUSTOM_SHELLS[body]['rotation_axis']['builder']` and
called it directly -- proving the builder + config wiring, but BYPASSING the live
trigger. The dispatch loop iterates `shell_vars.items()` and renders only shells
whose checkbox is set; nothing ever put `rotation_axis` into `shell_vars`, so the
loop never reached it. Tony caught it on render (Sun, Mercury: no axis) and asked
the diagnostic question -- "what triggers it, body or shell selection?" -- which
named the fix. This is "verify execution, not appearance" / "the plot is ground
truth": the builder *working* is not the dispatch *calling* it. **Rule reinforced:
a new render primitive's smoke test must drive the LIVE dispatch entry point with
zero shells checked, not the builder in isolation.** The smoke test now does
exactly that (Section 6) and would have caught this.

**FIX:** the axis is rendered unconditionally, once, in
`create_celestial_body_visualization` -- the single chokepoint all 11 bodies route
through (the "only Mercury is wired" docstring there is stale; Phases A-C4 landed,
Sun routes via the direct call sites). So it appears on BODY selection, carries its
own legend entry (toggleable), and the shell loop now explicitly skips
`rotation_axis` so a future checkbox can't double-render it.

**TONY-CATCH / my retraction:** I claimed in chat the south arc needed a *flipped*
sweep. Wrong -- both arcs use the SAME circulation (one omega x r); a flipped sweep
would draw a false counter-rotation (two hemispheres spinning oppositely). Caught
by re-derivation before committing code. The retraction is the tell: a confident
geometric claim about a *picture*, argued in prose, that a throwaway render would
have killed in seconds.

**Sketch-first instinct (considered, NOT codified).** Tony's observation: we should
have wired a throwaway render of one body before converging the design in prose.
Agreed it's the right instinct -- a sketch's job is to kill bad design cheaply --
but Tony's call is to keep it as judgment, not a protocol rule. Noted, not codified.

**Both-ends was the right destination, reached the long way.** It dissolved the
convention question rather than answering it. We walked there through prose when we
could have looked.

---

## 4. DEFERRED / LEDGER

- **Duplicate `'Sun'` key in `CUSTOM_SHELLS`** (~lines 2500 and 2681; the second
  wins, silently dropping the first). Surfaces in the UI as "Sun appears twice in
  the body selector." REAL bug, its OWN ticket -- deliberately not folded into this
  build (conflating is how a clean fix turns messy). The Sun rotation_axis entry
  was added to the winning (last) block.
- **Magnetic dipole cone** (Uranus ~59 deg, Neptune ~47 deg; axis = spin pole) --
  deferred consumer of this same pole vector. Sketch-first when it lands.
- **Axis precession cone** (Earth / Mars; axis = ORBIT normal, NOT spin pole;
  static geological-timescale overlay) -- deferred. Sketch-first.
- **Per-body `half_len_frac` tuning** -- Mode-5 knobs (multiple of body radius).
  Current defaults sized to each body's outermost physical/field structure
  EXCLUDING the Hill sphere. Sun = 50 R_sun (outer corona); could extend to the
  heliopause (~123 AU) if wanted. Not a bug; tuning.
- **ASCII sweep across the tree** -- own small ticket.
  `grep -rnP '[^\x00-\x7F]' --include=*.py`. (Line 190 em-dash in
  planet_visualization_utilities.py already fixed by Tony.)

---

## 5. LIVE FLAGS / ASSUMPTIONS

- **`needs_planet_name`** -- new opt-in dispatch flag (additive sibling of
  `needs_sun_position`). An entry setting neither calls `builder(center_position)`
  exactly as before -- behavior-preserving for every existing shell.
- **Axis is body-triggered**, not a shell checkbox; legend-toggleable as a unit
  (pole line `showlegend=True`, rest same legendgroup).
- **Arrowhead** `sizeref = arc_r * 0.45`; arc sweep 270 deg; arc radius 0.28 * half.
- **Moon** uses the J2000 *mean* pole; it librates on the 18.6-yr node (Cassini
  state, 1.54 deg to ecliptic), so the static glyph renders ~vertical -- correct
  for the mean, labelled in hover.
- **Axis color** `rgb(255,209,102)` (warm gold), distinct from magnetosphere blues.

---

## 6. FILES + INTEGRATION (built on `17093da`)

- **planet_visualization_utilities.py** -- ADD `PLANET_ROTATION` (sourced 11-body
  table + `half_len_frac` knob), `ROTATION_AXIS_OMITTED` (Planet 9, Eris),
  `build_rotation_axis_traces` (both-ends; lazy-imports the producer; uses
  module-level `CENTER_BODY_RADII` / `KM_PER_AU`).
- **shell_configs.py** -- 11 uniform `rotation_axis` CUSTOM_SHELLS entries; NEW
  top-level `Moon` and `Pluto` blocks (were sphere-only); omitted-note appended to
  Planet 9 and Eris body hover_text.
- **planet_visualization.py** -- dispatch builds a `kwargs` dict
  (`needs_sun_position` / `needs_planet_name`); body-triggered axis render after
  the shell loop; loop skips `rotation_axis`.
- **idealized_orbits.py** -- `planet_poles` + 5 sourced IAU poles
  (Sun/Mercury/Venus/Earth/Moon), each with a `# Source:` line; prior six unchanged.
- **smoke_rotation_axis.py** (NEW) -- live-dispatch smoke: resolves each builder
  through CUSTOM_SHELLS, asserts 6 traces/body, axis parallel to producer pole
  (~0 deg), both arcs share one 3-space sense matching the flag, AND drives
  `create_celestial_body_visualization` with zero shells checked to assert the axis
  appears on body selection (1 legend each) and that Planet 9 / Eris emit none.

Verification: all 5 compile; LF; ASCII-clean in changes; smoke ALL PASS; Mode-5
render PASS on Sun, Mercury, Earth.

---

## 7. CARRIED FORWARD (by reference; unchanged this session)

- **v25** -- N15 ring-plane migration (all ring systems orient by IAU pole) +
  analytical moon-orbit retirement (Jupiter/Mars osculating-only).
- **v24** -- bow shocks + magnetosphere nest (Movement 1).
- **v23** -- shell-consolidation D-track.

---

## 8. NEXT-SESSION PRIORITIES

1. **Push + record the new HEAD SHA** in this handoff; confirm the round trip
   (project knowledge auto-syncs from the repo -- a matching remote HEAD confirms
   commit + push + sync in one check).
2. **Mode-5 render sweep** of the remaining 8 bodies: Venus (~vertical),
   Moon (~vertical), Mars, Jupiter, Saturn, Uranus (~horizontal), Neptune,
   Pluto (>90 deg). Interesting cases are the high-obliquity / retrograde ones.
3. **Optional `half_len_frac` tuning** per body once seen at scale.
4. **Duplicate-`'Sun'`-key fix** (its own ticket; trace the selector's body list).
5. **Next pole-vector consumers:** dipole cone, then precession cone --
   sketch-first.
