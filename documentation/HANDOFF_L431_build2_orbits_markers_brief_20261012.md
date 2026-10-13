<!-- Doc-Kind: hand | Brief for L-431 build 2 (the drawn ellipse around the period's centre, the markers from the fetched period) carrying L-401's second slice (the markers' and orbit hovers' digits) and four in-passing fixes. One session, one patch, one look. Rulings of 2026-10-11 and 2026-10-12. -->
# Brief: L-431 build 2, with L-401's second slice

Built on orrery 4037362b82853d48e1dd978e40f4be7ec68118f3 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched: the website is L-431's build 3.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1, in a
coordination session; the build is for an Opus session.

- Type: BUILD brief (zero code). The design is settled; Mode 5, Tony's
  look at the render, is the acceptance.
- Companions: `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`
  (the rulings; section 3 names this build; section 4 the method);
  `documentation/DESIGN_L431_orbital_periods_20261011.md` (section 6
  names every place the orrery reads a period);
  `documentation/HANDOFF_L431_period_build1_20261011.md` (what build 1
  built and what it left to this build, its section 5);
  `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`
  (the digits rule; section 3 names the marker and orbit-hover slices);
  `documentation/HANDOFF_L401_distance_build1_20261012.md` (how build 1
  prints a distance and its sentences, section 6);
  `documentation/DESIGN_rulings_20261012.md` (rulings 3 and 7).
- Why one session: L-431 build 2 and L-401's second slice open the
  same two files, `idealized_orbits.py` and `apsidal_markers.py`
  (ledger-and-session-records, Cluster the Tail by Topic). The
  in-passing fixes of ruling 7 ride the same patch because it holds
  `idealized_orbits.py` open.

## 0. Before building

- Pull the orrery at HEAD and pin the SHA. The dashboard, L-425 or
  other scaffolding sessions may have landed since 4037362b; none
  touches this build's files, but the maintenance run's row list and
  the dashboard's labels may have moved.
- Skills this task fires: horizons-orbital-mechanics (CONFIRM the
  loaded copy reads 1.3; Tony reinstalled it 2026-10-12, which this
  session is the first able to check), orrery-coding-conventions
  (markers, hover text, legendgroups, the live shell dispatch),
  provenance-discipline (A Computed Position Prints What Its Errors
  Earn; the exceptions file), safe-file-editing, agentic-pre-test,
  ledger-and-session-records. Confirm each against the manifest at
  HEAD.
- Read build 1's handoff before touching `orbital_period.py`: it owns
  the period record (centre, date, error, SBDB status) and the
  fallback order. This build READS that record; it does not re-fetch
  on its own path.

## 1. What is settled (no decisions in this build)

From the rulings record of 2026-10-11, section 2, item 7, Tony:
"Confirmed." and "Confirmed. This is the best solution.":
- The drawn ellipse is taken around the same centre as the period, so
  the hover and the drawing describe one orbit.
- The perihelion and aphelion markers use the fetched period, in the
  same fallback order (fresh fetch; the last fetched record in the
  orbit cache; the typed table, marked).
- Both change what is drawn, so they are one build with one look.

From L-401 (the distance digits), 2026-10-11 and the look of
2026-10-12: a computed number prints to the digits its errors earn,
each unit by its own error, never finer than whole kilometres; the
sentences that say why are build 1's and are not reworded here. The
surface line is measured from one radius for every centre with one.

From ruling 7 of 2026-10-12: four findings in `idealized_orbits.py`
are fixed in passing by this patch (section 4); the planets'
description dictionary is NOT touched here (one ledger row by class,
opened with the inner planets' rooms).

## 2. The build, by file

### 2a. `idealized_orbits.py`: the ellipse around the period's centre

- Where a body's period record names a centre (Sun or the solar
  system's barycentre), the ellipse is drawn from elements fetched
  around THAT centre, following the Pluto-Charon pattern already in
  the file (Pluto and Charon drawn from elements around their
  barycentre). Moons and the Pluto system keep the centre the orrery
  gives them (method 3 of the rulings record): no change.
- Sedna is the visible case: about 540 au around the Sun, about 506 au
  around the barycentre on 2026-10-10. Mercury and Encke stay around
  the Sun. The look is those three.
- The orbit's own hover (the "Keplerian orbit uses osculating
  elements" blocks and the others, 16 functions by L-401's count)
  prints by L-401's rule: a distance it computes goes through
  `position_accuracy.distance_speed_lines` or the same formatter the
  body hover uses, never a fixed ten decimals; an element it merely
  repeats from Horizons (a, e, i, omega, Omega, Tp) is printed as
  Horizons gave it, not re-rounded and not widened. If the rulings
  record is silent on a case the file presents, the builder settles it
  by that rule and says so in the handoff; a case the rule cannot
  express goes to Tony, one at a time.
- `get_fallback_elements` reads the centre-aware cache key (build 1's
  note); the Moon's typed 27.321661-day default (line 4162 at
  9f15478) and the satellites' period use (line 3434) read the period
  record through the fallback order, marked when typed.

### 2b. `apsidal_markers.py`: the markers from the fetched period

- `get_orbital_period_days` and the three sites that compute the next
  perihelion and aphelion from TP plus a period (lines 910, 1170 and
  1308 at 9f15478), and the mean motion at line 1688, read the period
  record through `orbital_period`'s fallback order. The typed table is
  the last resort and the marker's hover says "typed value, not
  fetched from JPL" when it is used, as the body hover does.
- The marker hovers (perihelion, aphelion, Kepler position, closest
  approach, encounters, the closest-plotted-point) print their
  distances by L-401's rule, the same formatter as the body hover, so
  a marker and the body it belongs to never print a distance to
  different digits. A date prints as it is computed; its uncertainty
  is the period's error carried through, stated in the hover where it
  is larger than a day.
- The parameters window's estimated apsis dates
  (`orbital_param_viz.py`, the `params['period']` fill at line 282)
  come from the same record.

### 2c. `palomas_orrery.py` and `orbital_period.py`: one home for the centre

- `VIEW_TO_OSCULATING_CENTRE` in `orbital_period.py` copies the block
  in `palomas_orrery.py` that sets `osculating_center_body`. Give it
  one home and one reader (One Value, One Home, on a mapping).
- `_is_small_body` reads id_type only, so C/2025_K1 (record 90004912,
  id_type 'id') is never asked of SBDB and its hover says the database
  has no entry. Fix on this path: a pinned record number is a small
  body.

### 2d. Not in this build

- `KNOWN_ORBITAL_PERIODS`'s 132 typed entries (one class, not chased).
- The 39 moons' typed "orbital period" in `mission_info`
  (`celestial_objects.py`), seen under the fetched period in Io's hover
  on 2026-10-12. One class.
- The fly-to buttons, the parameters window's distances, the
  animation's small-body uncertainty: L-401 build 3.
- The website: L-431 build 3.

## 3. The look (Mode 5; Tony's eyes are the acceptance)

Plot, from the Sun, with the orrery opened fresh: Sedna (the ellipse
should visibly shrink toward the barycentre figure; its hover names the
barycentre), Encke and Mercury (unchanged centre; the markers' dates
move only by the fetched period's difference from the typed one), and
one body with no fetched period, so the typed fallback and its note
are seen once. Hover a perihelion marker and an aphelion marker on
each. The patch prints, as it ends, the marker dates it computed for
those three against the dates the typed table would have given, so
the look has numbers beside it.

## 4. Build notes (method; the build session settles these and records them)

- One patch script, `patch_L431_6_<...>.py` (build 1 reached _5), under
  safe-file-editing: anchored, all-or-nothing, LF, ASCII, docstring
  stamps on every edited module. The patch predicts the scanner's
  CHANGE, not its total.
- The four in-passing fixes, named in the patch's output: the two
  "theta = 0 deg" and "theta = 180 deg" lines to
  `data/provenance_exceptions.json` as geometry; the two console prints
  of transform angles (Mars 25.19 deg, Triton 3 deg) excused the same
  way, with the reason. Expected change: minus four Tier-1 in
  `idealized_orbits.py`.
- Planted faults, shown caught in the checker before delivery: a
  marker dated from the typed period while a fetched record exists; an
  ellipse drawn around the Sun while the record names the barycentre;
  an orbit hover printing a distance to ten decimals; the Moon's typed
  default used when a fetched period exists. Extend
  `test_position_digits.py` where the orbit hovers fit its sweep, or
  give the markers their own small checker; name it what it prints and
  give it its dashboard button either way.
- The sandbox cannot reach JPL. Test with the period records already in
  `data/osculating_cache.json` and with JPL faked from the rulings
  record's section 5, as build 1 did; the live run is Tony's.
- Pre-test on a throwaway copy: py_compile, the orrery under xvfb,
  the dispatch smoke test confirming the live path draws from the
  edited functions (Verify Execution, Not Appearance: the file has
  dead copies of inline drawing code; grep for callers first).
- Check All Parallel Pipelines: the static plot, the animation and the
  social export all draw the ellipse and the markers through the same
  functions; confirm each path sees the change, and say so.
- Skills: horizons-orbital-mechanics carries the two-centre test since
  1.3; if this build adds method (the ellipse follows the period's
  centre; a marker's date carries the period's error), one version,
  under One Session, One Bump, with the protocol entry and the manifest
  run in the same commit.
- Close: L-431's Gap moves to build 3; L-401's Gap drops the markers
  and orbit hovers and keeps build 3's three slices; L-424/L-425/L-426
  untouched; the four in-passing fixes recorded on L-401 by name; Where
  We Are by section (stage 6a to "build 2 done; the website next").

## 5. For Tony, one at a time, in the build session

- (decide, only if raised) A case the digits rule cannot express for an
  orbit hover: the builder brings the one sentence, not the list.
- (decide, at the look) Whether the render is accepted. The brief
  carries no other decision.

## 6. Tony's actions, all of them

- (do) Start the Opus session from this brief, when it comes in your
  order.
- (do) Run the patch and the maintenance run; open the orrery fresh and
  do the look in section 3; push.
- (decide) The look.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
