<!-- Doc-Kind: hand | Brief for build 1 of L-401 (the orrery's distance digits): the body hover printed by the errors JPL states, the speed with it, the typed sky-position table out. Every question is ruled, the last one (the speed of a body with no stated error) on October 11, 2026. Written October 11, 2026. -->
# Handoff: L-401 (the distance digits), build 1, the body hover: the brief

Built on orrery 4c22b33b570a3a47a7f782da1fc675bd7b1c2da8 (the L-401
design close, pushed 2026-10-11) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
session pins both HEADs itself at its start.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written by the Fable 5.1 coordination session of October 11, which read
the orrery at HEAD and wrote no patch.

- Type: BUILD, orrery only. The gallery is read for its floor and its
  figures rule and is not touched; it prints no period and no speed
  today, and the design says nothing there waits on this.
- Why now, Tony's ruling of 2026-10-11: "let's promote L401 to next.
  accuracy and precision are fundamental." It goes ahead of everything
  on the Sun's list (L-412) and Earth's list (L-413).
- The design is ruled and recorded. Read, in this order:
  `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`
  (every ruling; section 3, the discovery; section 6, the method);
  `documentation/REVIEW_L401_distance_digits_comparison_20261011.md`
  (what the three reviewers said and which of them opened sources);
  L-401's block in the ledger; and section 2 of this brief for the
  ruling made after that record was pushed.
- Skills this session fires: provenance-discipline 2.28 (A Computed
  Position Prints What Its Errors Earn; the Report test; the stated
  floor), horizons-orbital-mechanics 1.2 (the vector table, the
  `2xr` uncertainties), orrery-coding-conventions 1.10 (hover text),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.20. In the first reply, read back each
  loaded version. No obligation travels to this session: the L-401
  design session confirmed 1.20 and bumped nothing. The protocol is
  PROJECT_INSTRUCTIONS.md v3.91.

## Read this first

- *Nothing is left to design. The last open question, the speed of a
  body whose distance has no stated error, was ruled on October 11
  (section 2). The two remaining items in the design record's section
  5 are words and a box shape, proposed by this build and approved at
  Tony's look, not asked before building.*
- *The first slice is one function:* `format_detailed_hover_text` in
  `visualization_utils.py` and its two formatters in
  `formatting_utils.py`. The other 375 sites of the discovery are one
  ledger class on L-401 and are not this session's.
- *The check must be shown failing before it is trusted passing.* A
  hover that prints ten figures where JPL knows four is the finding
  that opened this item; the test has to catch that by name.
- *One message to Tony, at the end: the look (section 6).*

## 1. Settled, so the session does not ask

- The planets and Pluto keep the three 2014 rows in `constants_new.py`
  (Folkner et al., DE430), stored as the place the words report to;
  the display uses half a unit of the place as the error.
- The Moon gains a row from the same 2014 report, "known to submeter
  accuracy", stored as its place, 1 metre. The build opens the report
  and reads the sentence before writing the row (source-then-cite).
- Small bodies take JPL's own uncertainty at 3-sigma, from the same
  vector query that returns the position: `VEC_TABLE='2xr'`, by a
  direct call to the Horizons API, because astroquery 0.4.11 cannot
  ask for it. Columns by name (`R_s`, `VR_s`, `VT_s`, `VN_s`), never by
  position. No extra query. The sigma level is written into every
  field name (`range_3sigma_km`). An error is keyed by body, centre
  and date.
- No stated error (a moon seen from its planet, a spacecraft, a
  Lagrange point, a barycentre, the Sun as a body): the distance prints
  to whole kilometres, the stated floor, with a plain sentence that
  JPL states no accuracy for it. "No error" is its own state in the
  code, never a tiny invented one. A moon in a Sun-centred plot uses
  its planet's row as a floor.
- Another centre: the larger of the two bodies' errors (Tony,
  2026-10-01, "use whichever is larger").
- Every unit carries the same error, each placed by its own Report
  test: AU, kilometres, light time. Never fewer than one figure; never
  a line dropped; plain numbers, no scientific notation.
- The speed, "Reading 1" (Tony, 2026-10-11): a small body's speed uses
  JPL's three velocity uncertainties combined into one bound, times
  three; any other body with a stated distance error prints its speed
  to the same relative precision as its distance, and the box says so.
  This can add digits: Mercury's speed earns about 41.92415 km/s.
- The sky-position line: the typed `MAJOR_BODY_UNCERTAINTIES` values
  and the ", typical" fallbacks in `celestial_coordinates.py` come
  out. Where Horizons gives no figure the line says plainly that JPL
  gives none; the small bodies' fetched 3-sigma figures stay; the line
  says "as seen from Earth", since `fetch_radec_for_hover` asks from
  Earth's centre. Kept for later, not this build: a sourced angular
  figure for a planet worked out from its position row and its
  distance from Earth.
- The box's shape, all three reviewers agreeing: one light-time line
  (light-minutes under an hour, light-hours above); the surface line
  only where the centre has a surface. Proposed by the build, approved
  at the look.

## 2. Ruled October 11, after the design record was pushed

- **The speed of a body whose distance has no stated error** (Tony:
  "approved as recommended"): a speed floor of its own, stated in the
  speed's unit, with the same plain sentence as the distance. The
  floor's value is method, not Tony's: one metre per second, printed
  as 0.001 km/s, is the proposal, parallel to the distance's whole
  kilometres and far coarser than any tracking fit. The hover says
  "JPL states no uncertainty for this body's speed" and no more. Not
  option A (following the whole-kilometre floor through the
  arithmetic, which presents a precision nothing earned) and not
  option C (dropping the line).
- **Why, from the literature, checked 2026-10-11 by the Fable session
  (sources in section 7):** no published velocity error bar exists for
  the planets, the Moon, the planetary moons, spacecraft, Lagrange
  points or barycentres. The DE440 paper gives range residuals, none
  in velocity. Horizons' pages for Io and Titan state no accuracy;
  JPL's satellite-ephemeris listing states none for any of its
  seventeen files. Horizons' statistical uncertainties are "for
  asteroids and comets only", and for any other target "n.a." symbols
  appear "(meaning "not available")". The one velocity-type figure in
  print is a spacecraft's tracking residual (Voyager 1: Doppler
  "0.133 mm/s", range "228 m"), which is the fit's residual, not a
  stated uncertainty, and no API field returns it.
- **Two things that are not sources.** The physical argument that a
  bound orbit's fractional speed error is about its fractional position
  error (a position error times the mean motion) is standard reasoning
  and supports Reading 1, but no quotable textbook line was found; it
  does not go in a hover or a `# Source:`. Jacobson's satellite
  papers (SAT441 and the Pluto system) state orbit uncertainties in
  kilometres and could not be opened from the sandbox; if the build
  wants a moon's position row later, that is where to read, and it is
  not this build.
- The close records this ruling on L-401 with its date and the
  sources, since the design record at HEAD lists the question as open.

## 3. The hover today, read at 4c22b33

- `format_detailed_hover_text` (visualization_utils.py, from line 773)
  builds one text for the static plot, the animation and the social
  export. Distance in AU through `format_maybe_float`, ten decimal
  places; kilometres through `format_km_float`, which prints `.10e`
  scientific notation; light-minutes and light-hours both, each to ten
  decimals; the surface distance in `.10e`; the speed in AU/day to ten
  decimals and in km/hr to two and km/s to three, fixed widths all.
- The sky-position line comes in through `format_radec_hover_component`
  (line 893) and `get_precision_note` in `celestial_coordinates.py`,
  which reads `MAJOR_BODY_UNCERTAINTIES` (line 140) and falls back to
  "+/-0.1 arcsec" for moons and "+/-5" or "+/-10 arcsec" for a new
  discovery, typed and unsourced.
- The period line (L-431 build 1) is appended after the speed. Its
  sentence "JPL lists no orbit uncertainty for this body" is false of
  JPL for a planet (JPL states one in the 2014 report; the small-body
  database has no entry). Reword in this build, since it opens the
  same hover: say what is true, that JPL's small-body database has no
  entry for the body and the period is rounded by its year's change.
  Proposed by the build, approved at the look, with the rest of the
  period hover's words, which L-431 left to Tony's word.
- Check All Parallel Pipelines: one function serves three of the five
  consumers; the two gallery consumers do not print this hover. Grep
  for the callers before editing and confirm the function is on the
  live path for the static plot, the animation and the social export;
  the dispatch is the proof, not the dictionary.

## 4. What the build does

- An error for every body, by class, in one place the hover reads:
  planet or Pluto, the DE430 place row; the Moon, its new row; small
  body, the `2xr` figures from the position fetch; everything else,
  the no-error state. The plot centre's own error joins it by the
  larger-of-two rule.
- The hover prints each distance unit to the Report test's place of
  the larger error, never finer than whole kilometres, never fewer
  than one figure; one light-time line; the surface line only where
  `CENTER_BODY_RADII` has a real surface for the centre; plain numbers.
- The speed by Reading 1 where the distance has an error; by the
  combined velocity sigma for a small body; at the 0.001 km/s floor
  with the sentence where there is none. The AU/day line follows the
  same error.
- The sky-position line as settled in section 1.
- The box says in words which kind of figure it is: a published
  accuracy for a planet, a computed one for the date for a small body,
  a stated floor where JPL gives none.
- Words approved by Tony are owned by the display; propose them once,
  in the patch's printed sample hovers (section 6), and record his
  verdicts from his run-record copy.
- provenance: the Moon's row carries `# Source:`, `# Read:`, `# Ref:`
  and a `# Figures:` line; the floors and the sentences are words,
  not rows; the scanner's last line still reads "GATE PATH: 0 TIER-1".
  Any constant the build needs that is not in `constants_new.py` is
  added as a row, never typed in the hover.
- A checker in the orrery maintenance run, with its dashboard button
  (Settled, Oct 10: every new check gets its button), shown failing on
  planted copies first, each caught by name: a planet printing finer
  than its row; a small body whose sigma is missing landing anywhere
  but the no-error state; a no-error body printing finer than the
  floor; a dropped line; a typed sky-position value back in the text;
  a speed finer than its distance's precision. Its passing output
  prints what it compared and how many hovers it examined.
- agentic-pre-test: py_compile; the xvfb run with Mercury, Sedna,
  Encke, Io (centred on Jupiter) and Voyager 1 plotted, the hover
  text read back from the figure; the maintenance run on a copy, 23
  of 23 plus the new checker; the patch twice over and on a CRLF copy.
- Method owed to horizons-orbital-mechanics, in ONE version, 1.3, with
  what L-431 already owes it: the `2xr` uncertainties and the
  astroquery limit; the two-centre test and its saved choice; SBDB's
  lookup of a pinned record by Horizons' name. The four steps in one
  commit (version line, skills_index.py, the protocol's history entry,
  the push). provenance-discipline needs no bump: its stated-floor
  rule already covers a speed floor the display states.

## 5. Not this session

- The other slices of L-401: the apsidal and encounter markers (their
  dates ride L-431's build 2), the orbit hovers in
  `idealized_orbits.py`, the fly-to buttons, the parameters window.
  One ledger class, recorded, not chased (The Braid).
- L-431's builds 2 and 3 (the drawn orbits and markers; the website).
- A moon's position row from Jacobson's papers (section 2).
- L-424 (the checker's one word) and L-425 (citation location checks):
  Tony's decisions, not this build's.

## 6. Tony's look, one message

- Run the patch, then `orrery_maintenance_run.py` (expect 23 of 23
  plus the new checker, and "0 TIER-1 -- the push gate holds").
- Open the orrery fresh (the window must be opened after the patch;
  his first L-431 screenshots showed the old hover for that reason),
  plot Mercury, Sedna and Encke from the Sun, Io from Jupiter, and
  Voyager 1, and hover each. The patch prints the five expected hovers
  so he can compare line by line.
- His verdicts on the words, in his run record: the no-error
  sentences, the speed line's sentence, the reworded period sentence,
  the light-time line, the surface line's presence or absence. "--
  correct" or "-- not clear" per line.
- Then move the patch into `documentation/`, commit and push.

## 7. At the close

- The ledger: L-401 (the distance digits) records build 1 and Tony's
  look by name, the October 11 velocity ruling with its sources, and
  its Gap narrows to the other slices by class. L-431 (orbital periods)
  records the reworded sentence and Tony's word on the hover. L-399
  (small bodies' own uncertainty, gallery) gains a line: the orrery now
  fetches it; the builder's half stays open there.
- Tony's page, by section, handles labelled, nothing below the marker:
  the page stands at exactly 130 lines above the marker, the cap, so
  trim before adding (a Settled line that is habit, or the two "needs
  you" bullets already done). The box says the hovers print by their
  errors and that L-431 build 2 is next.
- The handoff: `documentation/HANDOFF_L401_distance_build1_20261012.md`
  in the orrery, with both folders in its header, anchored at start and
  at the close.
- The obligation that travels: horizons-orbital-mechanics 1.3. The
  next session confirms its loaded copy reads 1.3 before Horizons work.

## 8. Sources read for the velocity ruling (2026-10-11)

- Park et al. 2021, DE440 and DE441, AJ 161:105:
  https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf (range residuals
  by planet; no velocity accuracy).
- JPL Horizons manual: https://ssd.jpl.nasa.gov/horizons/manual.html
  (uncertainties on tables 1 and 2; "n.a." where none; spacecraft
  predictions "10s or 100's of km of error").
- Horizons object pages, read through the API with OBJ_DATA='YES':
  Voyager 1 (-31), the 2022 Jacobson refit and its residuals; New
  Horizons (-98), no accuracy stated; Titan (606), no accuracy stated.
- JPL Planetary Satellite Ephemerides, file listing:
  https://ssd.jpl.nasa.gov/sats/ephem/files.html (seventeen files, no
  accuracy stated for any).
- Vallisneri et al. 2020, ephemeris uncertainties for pulsar timing,
  arXiv:2001.00595 (planets' position uncertainties in km; none in
  velocity).
- Fayolle et al. 2023, A&A 676 L6 (Galilean moons: a few km
  observational accuracy; Jupiter's ephemeris differences 2 to 5 km).
- Not opened: Jacobson 2022, the main Saturnian satellites, AJ
  164:199; the NAIF comment files (jup365.cmt, sat441.cmt).

Brief written October 11, 2026, with Anthropic's Claude Fable 5.1.
