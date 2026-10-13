<!-- Doc-Kind: hand | Session record for L-431 build 2 (each orbit drawn around its period's centre, the markers dated from JPL's period) with L-401's second slice (the orbits' and markers' digits), the four in-passing fixes, the checker and its planted faults, and what Tony looks at. -->
# Handoff: L-431 build 2 (the drawn orbits and markers), with L-401's second slice

Built on orrery c9722520c6316d3136489e37abf0179c93a39703 at
https://github.com/tonylquintanilla/palomas_orrery ("L431 build 2", the
brief's commit; the code is as at 4037362b). The gallery is not touched.
Pushed at: Tony's commit after running the patch; the next session reads
it with `git ls-remote`.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD, orrery only.
- Brief: `documentation/HANDOFF_L431_build2_orbits_markers_brief_20261012.md`
  (Claude Fable 5.1). Design: section 2, item 7 of
  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`; the
  digits rule, `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`;
  ruling 7 of `documentation/DESIGN_rulings_20261012.md`.
- Patch: `patch_L431_6_orbits_markers_20261012.py`, saved in the orrery
  folder. Move it to `documentation/` after the run.
- Skills loaded, each matching the manifest at HEAD:
  horizons-orbital-mechanics 1.3 (the obligation build 1 left is
  discharged: Tony's reinstall of October 12 took), orrery-coding-conventions
  1.10, provenance-discipline 2.28, safe-file-editing 1.13,
  agentic-pre-test 1.3, ledger-and-session-records 1.20.
- Skill cut: horizons-orbital-mechanics 1.3 -> 1.4, protocol v3.93. The
  obligation travels (section 9).

## 1. Read this first

- *Each orbit is now drawn around the same centre as its period.*
  Sedna's ellipse is taken around the solar system's center of mass
  (about 506 au across its long half, not 540), and its hover says so.
  Mercury's and Encke's stay around the Sun.
- *The perihelion and aphelion markers are dated from the period JPL
  gave.* A date stepped from a period carries that period's uncertainty,
  stated where it is more than a day (Sedna's aphelion: about 930 days).
  A typed period says it is typed.
- *Every orbit and marker hover prints its distances by the same rule as
  the body hover.* Elements repeated from Horizons print as given.
- *Your part:* run the patch (it ends by printing the marker dates beside
  the typed table's), then the maintenance run, then the look in
  section 7. Answer Yes to Sedna's "Update Orbital Elements?" box: its
  saved record predates this build, and only a fresh fetch carries the
  center-of-mass elements.

## 2. What the patch does

Code (verified in the sandbox, section 6):
- `orbital_period.py`: the period record now keeps the elements Horizons
  gave around the period's own centre, from the query it already makes.
  New `drawing_orbit()` hands the drawing those elements, the place of
  that centre in the plot, and the period that belongs to them.
  `period_for_computation()` gives a moon's or a system's period by the
  same fallback order; `period_for_elements()` gives the period of the
  elements a window already holds. `VIEW_TO_OSCULATING_CENTRE` is the
  one home of the view-to-centre map. `_is_small_body` counts a pinned
  record number as a small body, so C/2025_K1 is asked of the Small-Body
  Database. `date_note_lines()` holds the dates' words.
- `idealized_orbits.py`: the Sun-centred branch draws from
  `drawing_orbit`, moves the ellipse and its markers to the period's
  centre, dates the aphelion from that period with its uncertainty, and
  times the Keplerian position by it. The Moon's period and the
  satellites' follow the fallback order (the typed 27.321661 default is
  gone). Every orbit hover prints its elements as given and every
  distance or speed it computes through `position_accuracy`.
- `apsidal_markers.py`: the moons' and systems' markers are dated from
  the period by the fallback order, with the carried uncertainty; every
  distance goes through `position_accuracy`; the typed "Accuracy:
  +/-0.002 AU" notes, which no source stated, are gone, replaced by the
  body hover's own sentence. `calculate_keplerian_position` takes the
  period of its elements.
- `position_accuracy.py`: `as_given`, `accuracy_for`, `au_text`,
  `km_text`, `distance_text`, `surface_text`, `speed_text`,
  `accuracy_lines`: the body hover's rule, for the orbits and markers.
- `palomas_orrery.py`: the static plot and the animation read the centre
  map from its one home (the animation's copy lacked Orcus; its
  per-object choice never used that entry, so nothing it draws changes);
  each position's full record travels to the orbit drawing.
- `osculating_cache_manager.py`: `get_fallback_elements` reads the
  centre-aware key, so declining an update keeps the view's own
  elements; a period record kept after a failed query is told this
  fetch's own period.
- `orbital_param_viz.py`: the window's period and apsis dates come from
  the period that belongs to its elements, never a barycentre view's.
- `data/provenance_exceptions.json`: the four in-passing fixes (section 4).
- `test_orbit_markers.py`, new; in the maintenance run as "Orbit markers
  (L-431, L-401)" and on the dashboard as "Orbit Markers".

Records: the skill (1.4) and `documentation/SKILL_HISTORIES.md` (its
v1.1 entry); the protocol v3.93, with v3.90 moved to
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`; the ledger (L-431,
L-401, new L-435, the stamp); your page, by section; this handoff.

Permanent after the script is archived: the code above, the checker and
its button, the four exceptions, the skill version.

## 3. Method decided in the build (not Tony's; recorded so it is not re-asked)

- **Where the barycentre sits in a Sun-centred plot.** The body's
  position from its Sun-centred elements minus its position from its
  barycentric elements, both at the one date. No extra query, and the
  two ellipses then meet at the body. Sedna, 2026-10-12: about 0.005 au,
  three times its 3-sigma position uncertainty, so it shows in the
  digits. Checked in the sandbox against astropy's own barycentre: agree
  to 4e-14 au.
- **Pairing.** A record's elements are drawn only when their date is the
  plot's elements' date. A record saved before this build has none: the
  orbit stays around its own centre, its hover says why, and its markers
  take the period the same elements fetch gave, then the typed table,
  marked.
- **One orbit, one period.** A marker's date and the Keplerian
  position's motion use the period of the drawn elements, never one
  around another centre. The comparison with JPL's mean elements keeps
  the Sun-centred elements, because the mean elements are Sun-centred.
- **The perihelion date** is TP of the drawn elements, as given: no
  period is stepped, so no uncertainty is carried. **The aphelion** is
  TP plus half the period: half its error. A moon's dates step whole
  periods from TP: that many errors.
- **The words.** "Drawn around the Sun." / "...the solar system's center
  of mass." on the orbit; "q is measured from the solar system's center
  of mass." on a moved marker; "Uncertain by about N days, from the
  period's uncertainty."; "From a typed period: typed value, not fetched
  from JPL." (the body hover's approved words); "From a period worked
  out from the orbit's size, not fetched from JPL." (new; Kepler's law,
  around the Sun only). The distance sentence under a marker is the body
  hover's, unchanged.
- **Which number is which.** An element repeated from Horizons or a
  typed table (a, e, i, omega, Omega) prints as given: the shortest
  decimal that reads back to the stored number. A distance the code
  computes (q, Q, a surface distance, a km conversion, a binary radius
  worked out from a separation and a mass ratio) prints by the body's
  error. A marker on a position JPL gave for an apsis date prints by
  that position's own uncertainty, keyed by its date.
- **A moon with no period known** gets no date ("Date: Not calculated")
  rather than one from Kepler's law with the Sun's mass, which the old
  code gave it unmarked. None of the orrery's moons lacks a typed
  period today.
- **One body cannot stop the rest.** If a record cannot be read, the
  orbit is drawn from the fetched elements and the console says so; a
  value that is not a number prints "N/A", as the body hover does.

## 4. The four in-passing fixes (ruling 7 of 2026-10-12)

Added to `data/provenance_exceptions.json`, each with its reason:
- `idealized_orbits.py`, "Theoretical minimum distance (theta=0 deg)":
  geometry, not a claim.
- `idealized_orbits.py`, "Theoretical maximum distance (theta=180 deg)":
  geometry, not a claim.
- `idealized_orbits.py`, the console print "Transformation applied: Mars
  with Y-axis rotation of 25.19 deg": a rendering setting.
- `idealized_orbits.py`, the console print "Transformation applied:
  Triton with Neptune pole orientation + 3 deg": a rendering setting.

The scanner's change, measured in the sandbox (whole tree 288 -> 280;
gate path 0 -> 0):
- `idealized_orbits.py` 29 -> 24: the four above, and Jupiter's
  "(3.13 deg X-rotation)" console print 44 lines below Mars's. The
  scanner matches an exception against a 60-line window around each
  string, so the Mars entry covers Jupiter's print too. It is the same
  kind as the two ruled; named here rather than passed silently.
- `apsidal_markers.py` 3 -> 0: the three typed "Accuracy: +/-..." notes,
  removed as invented figures (L-401: "no error" is never a tiny
  invented one).
- No finding added anywhere.

## 5. Found, recorded and not chased (The Braid)

- **On L-401:** the encounter hovers in `spacecraft_encounters.py` and
  the close-approach hover in `close_approach_data.py` were not opened
  (neither file is this build's); `apsidal_markers.add_encounter_marker`
  and `add_actual_apsidal_markers` have no caller. The parameters
  window's fallback "estimate" dates, the plot date plus a quarter and
  three quarters of a period, have no basis; with build 3's window
  slice.
- **On L-401, for a ruling (section 8):** computed numbers that are not
  distances or speeds (an eccentricity difference, an angular shift, the
  analytical Moon's e and i) are left as they were; and the analytical
  Moon's a prints at the whole-kilometer floor with the ruled sentence,
  which still implies more than an analytical model knows.
- **On L-431:** the analytical-position fallback in `palomas_orrery.py`
  (MK2, Xiangliu, Vanth; four sites) times its positions by a typed or
  Kepler period. One class. The barycentre hovers' typed periods and
  separations (`BINARY_PARAMS`) stay, by ruling 7: they retire when
  L-431 fetches them.
- **New, L-435:** your question on Settled (section 8).
- The planets' orbit-description dictionary is untouched, by ruling 7.

## 6. Tested (sandbox, which cannot reach JPL)

- py_compile on every touched module; ASCII and LF on every file.
- The orrery's window opens under xvfb with no edit to the copy.
- Live dispatch, on a throwaway copy with JPL stubbed: Plot and Animate
  pressed for Mercury, Encke and Sedna from the Sun, through the real
  `plot_objects` and `animate_objects`. Both drew Sedna's ellipse out to
  936.5 au (the center-of-mass ellipse), not the Sun-centred one's
  1,004, with the dates and digits below. The social export re-exports
  the static plot's figure, so it carries the same traces.
- Sedna's center-of-mass elements in the sandbox are a fixture, worked
  out from its cached Sun-centred elements and the Sun's motion in
  astropy's built-in ephemeris: a 506.45 au, period 4,160,226 days,
  against JPL's 4,160,096. The live run uses JPL's own.
- `test_orbit_markers.py`: nine planted faults, each in a copy of the
  real source at the line it would live in, each caught by name; then
  the real code: 1,080 drawn points on their period's centre, 14
  markers, 9 dates, 52 printed distances, the Keplerian position half a
  year on, a pre-build record, the parameters window, the Moon, Io.
- `test_position_digits.py` still passes, 13 of 13.
- The scanner, section 4.
- A cold review by a separate Claude agent, before delivery. It found
  six faults in the first draft, all fixed and rechecked: the parameters
  window would have dated Earth from the Earth-Moon view's 27-day period
  after one plot from that view; computed binary radii printed as given;
  the checker could not fail on the Keplerian position's period, the
  actual-apsis markers or the window (now three plants); one bad record
  could stop every orbit; a moon could get Kepler's law with the Sun's
  mass; and four small ones.
- The patch on a clean clone at c9722520, twice (the second refuses and
  writes nothing), and on a CRLF copy with notes in the records; the
  maintenance run on the patched clone (section 9 gives the expected
  lines).

Not tested here; the patch's live check and your look cover it: JPL's
real answers, and the hovers in your window.

## 7. Your look (Mode 5; your eyes are the acceptance)

- Run the patch. At its end it asks JPL for Sedna, Encke and Mercury at
  today's date, 00:00 UTC, and prints each body's drawn centre and its
  marker dates beside the dates the typed table would have given. It
  writes nothing.
- Run the maintenance run (section 9).
- Open the orrery fresh. Set the time to 00:00. Tick Sedna, Encke,
  Mercury and Venus, Sun at the centre, apsidal markers on, Plot.
  Answer Yes to Sedna's, Encke's and Mercury's update boxes and No to
  Venus's, so Venus shows the typed fallback once.
- What to see:
  - Sedna: its ellipse visibly smaller, its far end near 937 au from the
    Sun instead of about 1,004; its orbit hover, "Drawn around the solar
    system's center of mass."; its perihelion marker in 2076, "q is
    measured from the solar system's center of mass."; its aphelion
    around the year 7771 with "Uncertain by about 930 days". Distances to
    about the nearest million km, as its body hover prints.
  - Encke and Mercury: "Drawn around the Sun."; the markers where they
    were; Encke now has an aphelion date (the typed table never had
    Encke); Mercury's aphelion moves by seconds.
  - Venus: its aphelion line "From a typed period: typed value, not
    fetched from JPL."
  - Every marker: the "q =" or "Q =" line in AU and km, the surface
    line, and the body hover's sentence under them; no "Accuracy: +/-"
    line.
- Your verdicts, in your run record, one per line: the ellipse; the
  orbit hover's centre line; the marker dates and the uncertainty line;
  the new Kepler sentence; the distances' digits.

## 8. Your questions, and one for you

- **"Are these rulings included in a skill or only here?"** (your note
  on Settled, run record 10-12-26 2212). Three of the twelve lines are
  in a skill: orbital periods (horizons-orbital-mechanics, now with the
  drawn orbit too), the OneDrive pause (gallery-cache-builder), and the
  digits rule's principle (provenance-discipline, "A Computed Position
  Prints What Its Errors Earn"). The rest are only on the page and in
  their design records and ledger items. Some are method a skill should
  carry, because they will recur: the no-error sentence and the speed
  rule, the spacecraft data sheets, "surface" as one radius, a checker's
  word naming its case, every new check getting its button, dots placed
  by the orrery. Others are your decisions about what the project is,
  which belong on the page and the plan, not in a skill: the scattered
  disk, the fuzzy boundaries' order, the comets' order and colours, the
  Hills cloud. L-435 records the method lines as one class, each to ride
  its skill's next version.
- **One case the digits rule cannot express** (for the next design
  talk): a number the code works out from a model with no stated
  accuracy. The rule gives such a number the whole-kilometer floor and
  a sentence; for the analytical Moon's a that still reads as kilometer
  precision. And numbers that are not distances (an eccentricity, an
  angle) have no rule at all.

## 9. Tony-actions

- (do) Run `patch_L431_6_orbits_markers_20261012.py` in the orrery
  folder; paste its output, live check included, into your run record.
- (do) Run `orrery_maintenance_run.py`. Expect 25 of 25 gating checkers,
  "Orbit markers" with 9 of 9 planted faults, and "0 TIER-1 -- the push
  gate holds". Whole tree: 280 Tier-1 (288 before); the patch in the
  root folder adds no Tier-1 finding of its own.
- (do) The look, section 7; your verdicts in the run record.
- (decide) The look.
- (do) Copy PROJECT_INSTRUCTIONS.md (v3.93) to the Project's
  instructions and as `documentation/project_instructions_v3_93.md`, as
  for v3.92.
- (do) Reinstall horizons-orbital-mechanics 1.4 to the account
  (Settings > Skills) from `skills/horizons-orbital-mechanics/SKILL.md`.
  The next session confirms its loaded copy reads 1.4 before Horizons
  work.
- (do) Move the patch into `documentation/`; commit and push.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
