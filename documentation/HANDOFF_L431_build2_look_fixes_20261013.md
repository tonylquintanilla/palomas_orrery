<!-- Doc-Kind: hand | Session record: Tony's look at L-431 build 2 accepted, and the three findings from his saved plot fixed in patch_L431_7. -->
# L-431 build 2: the look, and three fixes from the saved plot

Built on orrery 87a54704ab2cba6d3fbfa5cbb4c3adb698a53a02 at
https://github.com/tonylquintanilla/palomas_orrery (main); gallery
924977a3 at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Opus 5.5. Follows
`HANDOFF_L431_build2_orbits_markers_20261012.md` (the build).

## 1. The look: accepted

Tony ran patch_L431_6, the live check and the maintenance run, did the
look in the build handoff's section 7, and pushed (6bb8ef6f, then
87a54704 with his run record and the v3.93 copy). His record is
`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`. His verdicts,
one per line of the look: "correct.", "correct", "yes", "yes",
"correct"; the reinstall "done". In chat: "bottom line: looks good."

What the run showed, against what the build handoff predicted:
- The live check: Sedna drawn around the solar system's center of mass,
  a = 506.44 au; aphelion 7771-02-06 "Uncertain by about 930 days";
  the typed table's 7776. Encke's aphelion 2028-10-05 (the typed table
  has none). Mercury's aphelion a minute from the typed table's.
- The maintenance run: 25 of 25 gating checkers; Orbit markers 9 of 9
  planted faults; the gate path 0 Tier-1; the whole tree 280, the 288 to
  280 the patch predicted.
- The plot: Sedna's drawn aphelion 936.69 au; Venus (No to its update
  box) shows "From a typed period: typed value, not fetched from JPL."

## 2. Three findings from the saved plot, fixed

Claude read the plot Tony saved
(`palomas_orrery_images/solar_system_20261013_0829.html`, staged from his
computer) and his console. Three things the build missed, all fixed in
`patch_L431_7_look_fixes_20261013.py`, none needing a ruling:

1. **Encke's perihelion osculating orbit** (the white arc) printed its
   distances by the digits rule but not the sentence saying which figure
   they are rounded to. Every other marker carries it. Now it does
   (`idealized_orbits.plot_perihelion_osculating_orbit`).
2. **Sedna's perturbation block.** The orbit hover's top lines show the
   drawn elements, around the center of mass (a = 506.44 au). The block
   below compared the Sun-centred elements (a = 539.87 au) with the mean
   ones, which are around the Sun -- right, by horizons-orbital-mechanics
   1.4 -- but did not say so, so "+58.56 AU (12.2%)" read as the drawn
   orbit's. The block now reads "Perturbation (osculating vs mean, both
   around the Sun)" and prints the Sun-centred a and e it compared
   (`get_mean_vs_osculating_assessment`, new `compared_around`).
3. **The frame.** `palomas_orrery.calculate_axis_range_from_orbits`,
   which the static plot and the animation share, sized the frame from
   the Sun-centred a(1+e), 1,004 au, so it reached 1,104 au around an
   ellipse that ends at 937. It now asks
   `orbital_period.drawn_aphelion_distance` for the drawn far end where
   the orbit is drawn around another centre: 1,030 au. The animation's
   earlier range hint (for clamping the Sun-direction arrow) still reads
   the mean elements, 975 au; the frame it draws uses the fetched ones.
   Left as it was.

Each has a planted fault in `test_orbit_markers.py`, now twelve, each
caught by name:

    planted                                          caught as
    the perihelion osculating orbit's hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE
      its accuracy sentence
    Sedna's perturbation block not naming the        PERTURBATION COMPARED WITHOUT ITS CENTRE
      centre it compared around
    the frame sized from the Sun-centred orbit       FRAME SIZED FROM ANOTHER ORBIT

The checker runs the perihelion osculating orbit offline on Encke's
recorded elements, and compiles `calculate_axis_range_from_orbits` alone
from palomas_orrery.py's source, so the frame is judged without opening
the orrery's window. One correction to the checker itself: a whole
number's trailing zeros are no longer called coarse, since its place
cannot be read from the print (50,654,699.7 km to the whole kilometer
is 50,654,700).

## 3. Tested

- `test_orbit_markers.py`: 12 of 12 planted faults caught; then a clean
  pass. `test_position_digits.py`: 13 of 13.
- The window opens headless from a throwaway copy.
- Plot and Animate through the real dispatch (Sedna, Encke, Mercury from
  the Sun): the frame is +/-1,030 au in both, from Sedna's drawn far end
  of 936.71 au.
- The maintenance run on a clean clone with the patch applied: see the
  patch's NEXT lines for what to expect.

## 4. Still open (unchanged by this session)

- L-431 build 3, the website: the export carries each period and the
  elements around its centre; every room draws and prints them.
- L-401 build 3: the fly-to buttons, the parameters window, the
  animation's 2xr; then the encounter slice.
- At the design talk (on your page): a model with no stated accuracy
  (the Moon's analytical orbit) and numbers that are not distances.

## 5. For Tony

- (do) Run `patch_L431_7_look_fixes_20261013.py` from the orrery folder
  (VS Code, Run).
- (do) Run `orrery_maintenance_run.py`: 25 of 25, "Orbit markers" with
  12 of 12.
- (do) Move the patch script into `documentation/`; commit and push.
- No look is needed: the three fixes are words in two hovers and the
  frame's size, each judged by the checker. If you want to see them,
  plot Sedna and Encke from the Sun: the frame ends near 1,030 au, and
  Sedna's orbit hover says "both around the Sun".

Nothing here bumps a skill or the protocol. The next session confirms
its loaded horizons-orbital-mechanics reads 1.4 before Horizons work
(this session loaded 1.3, and was the one that bumped it).
