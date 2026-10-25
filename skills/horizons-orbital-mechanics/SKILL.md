---
name: horizons-orbital-mechanics
description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data, position_accuracy, orbital_period, period_fetch, path_plan). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, a small body's position uncertainty (VEC_TABLE 2xr), orbital periods and the centre they are taken around, the drawn orbit and its markers' dates, which Horizons record serves a body (helio_id, a pinned comet record, a skip list), encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.
fires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning, 2xr uncertainties, periods, the drawn orbit's centre, the Horizons check (horizons_check.py, its period comparison and the data sheets' re-read), the period fetch before it (period_fetch.py), which record serves a body (helio_id, re-pinning a comet, JPL's exact name, a body on a skip list), a spacecraft path's plan and its flybys (path_plan.py -- the Hill sphere, JPL's GM, the window and step, the orbiter rule for an arrival, a departure, a capture), a comet whose designation matches its own pieces
---

# Horizons and Orbital Mechanics Reference

Read this file in 3 parts: lines 1-234, 235-414, 415-560.

Skill version: 1.11 | 2026-10-25, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 0c27f47a. v1.11 (L-443 build B, with L-470) adds the
orbiter rule to How a Path's Events Are Found, by Tony's ruling of
2026-10-24 ("yes that would work well"): the days a path spends inside
one body's Hill sphere form a stretch; one nearest approach in it is a
flyby, more than one a capture, whose first and last nearest approaches
are the events, and a capture running to the end of JPL's data is an
arrival with no departure; passes of the Sun stay events; the rule is
among a plan's inputs. Also: a long JPL run prints as it goes, saves as
it goes and keeps under the maintenance run's 15 minutes; the twelve
are keyed, so KEYING loses its preview. And two rules from C/2025 K1 to
Which Record Serves a Body: a comet whose designation also matches its
own pieces is asked by JPL's permanent number for it; a path cache keyed
by name does not notice a new record.
Earlier: 1.10 | 2026-10-24, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 206f96c9. v1.10 (L-443, slice 2) adds How a Path's
Events Are Found, the method path_plan.py was built on: an event is a
nearest approach inside the body's Hill sphere, from JPL's own GM, that
needs finer steps than the weekly backbone by the orrery's curvature
rule; found from daily positions around the Sun, then to the minute in
two passes; its window and step by spacecraft_encounters' own rule; made
again on a 30-day cycle with the past carried. The Hill sphere was not
in the design record: without it the first offline run took nearest
approaches tens of millions of km from Mercury and the Moon for events.
Earlier: 1.9 | 2026-10-22, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ bfb6c474. v1.9 (L-443, with L-470) adds Which Record
Serves a Body: around the Sun a body with a helio_id is asked by it, in
every reader; a TNO's small-body record is JPL's "integrated barycenter";
a pinned comet is re-pinned to its newest record on Tony's word; JPL's
exact name is read for each entry before it is served; an orbit JPL
classes as open is not drawn as an ellipse; and a name on a skip list
says which record failed around which centre, and is tested before it
comes off (Tony, 2026-10-22: "some idiosyncrasies in Horizons are
addressed with specific record numbers, which can change").
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-12, 2026-10-13 and 2026-10-14 (L-431), 2026-10-15
(L-444, L-445), 2026-10-22 (L-443), 2026-10-24 (L-443) and 2026-10-25
(L-443).

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- Horizons Center Body Rules
- JPL Binary System IDs
- Which Record Serves a Body (L-443)
- Small-Body Record Pinning (periodic comets)
- A Small Body's Uncertainty Comes With Its Position (L-401)
- A Period Depends on Its Centre (L-431)
- The Drawn Orbit Follows the Period's Centre (L-431, build 2)
- Checking an Entry Against JPL (L-395)
- Where the Check Lives, and What It Compares (L-395, L-431 build 3)
- How a Path's Events Are Found (L-443)
- Reference Frame Diagnostic
- Query Mechanics
- Encounter and Flyby Resolution
- Field Notes

## Horizons Center Body Rules

Only NUMERIC IDs can be coordinate centers.
- Planets: 499 (Mars). Moons: 301 (Moon). Spacecraft: -61 (Juno).
- center_id pattern: add 'center_id': '2101955' for objects with numeric
  mission-target IDs that use a designation for normal plotting.
- helio_id vs center_id point in OPPOSITE directions -- one identifies the
  object as seen from the Sun, the other makes the object the center.
  Confirm which you need before wiring a query.

## JPL Binary System IDs

- 20XXXXXX = barycenter; 920XXXXXX = primary; 120XXXXXX = secondary.
- Derive the primary's position from the secondary via the mass ratio when
  Horizons serves only one member.

## Which Record Serves a Body (L-443)

Learned bringing 50 of the orrery's bodies to the website, 2026-10-22.
Design record: documentation/DESIGN_L443_objects_rulings_20261022.md;
JPL's answers: documentation/CHECK_L443_jpl_names_20261022.md and
CHECK_L443_classes_pairs_20261022.md. A record number is JPL's
bookkeeping, not the body: it can be re-solved, replaced by a newer
one, or answer only for some centres. So the method is to know which
record each question asks, and to ask the same one everywhere.

- ONE RECORD PER BODY AND CENTRE, IN EVERY READER. Around the Sun, a
  body with a `helio_id` is asked by its helio_id, as a small body
  (`helio_id_type`, else 'smallbody'), by every reader: the orrery's
  position fetch, its elements pre-fetch at both sites (the static plot
  and the animation), `export_objects.served_identity`, `period_fetch.py`
  and the website's builder. Until 2026-10-22 the pre-fetch asked the
  body's own `id`, so the orrery drew the orbit from one record and the
  marker from another. Around any other centre the body's `id` serves.
- A TNO'S SMALL-BODY RECORD IS THE PAIR'S CENTRE. JPL's Lookup names
  every helio_id record served here (Eris, Haumea, Makemake, Gonggong,
  Quaoar, Orcus, Patroclus) "integrated barycenter": the small-body
  solution follows the shared centre of the body and its moons. So it
  serves the system around the Sun. The system-barycentre numbers for
  Orcus (20090482) and Patroclus (20000617) are found in BOTH of JPL's
  indexes, which the Horizons check reads as a wrong id_type (Checking
  an Entry Against JPL, below); the small-body records 2004 DW and
  A906 UL are found in one. Whether the drawing says "shared centre" is
  the barycenter rule's, in orrery-coding-conventions.
- A PINNED COMET GOES STALE. Three periodic comets were pinned to a
  record that was no longer their newest: Schaumasse, Howell and
  Churyumov-Gerasimenko, re-pinned on Tony's word of 2026-10-22
  ("Re-pin to the newest") to 90000356, 90000901 and 90000703. List a
  comet's records with COMMAND='DES=<desig>;' and take the newest
  apparition's. The check reports a newer record; only Tony's word
  re-pins (Small-Body Record Pinning, below).
- JPL'S EXACT NAME, READ BEFORE SERVING. Every served entry carries
  `horizons_name`, JPL's own form of its name, read from the Lookup (or
  the main service, for a pinned record) the day the entry is keyed,
  never typed from memory. The check then holds it to JPL.
- AN OPEN ORBIT IS NOT AN ELLIPSE. The website draws an orbit from its
  elements with an elliptic solver (render_orbits.solve_kepler,
  sweep_conic), so a comet JPL classes hyperbolic (SBDB class HYP, as
  Wierzchos) or one fitted with e near 1 waits for a path drawing and is
  not served as an orbit. Read SBDB's class; do not judge from the name.
- A SKIP NAMES WHAT FAILED. Six lists in palomas_orrery.py keep a body
  out of a Horizons question: SKIP_HORIZONS_PREFETCH in plot_objects and
  in animate_objects, SKIP_HORIZONS_TRAJECTORY in the static plot's
  trajectory worker, and the fallbacks ANALYTICAL_POSITION_FALLBACK
  (plot_actual_orbits and the static worker) and
  ANALYTICAL_ANIMATION_FALLBACK (animation_worker), which act only when
  Horizons returned nothing. period_fetch.py copies the pre-fetch list
  as SKIP_NAMES. A name goes on a list with a comment naming the record
  that failed, the centre it failed around, and the date. Gonggong
  (id 920225088, its body-centre record; helio_id 2007 OR10) is on all
  six, every line from 2026-02-04 (commit c60572d), with no such
  comment, so it has no fetched period (L-470). The lists' own comment
  speaks only for the moons.
- TAKING A NAME OFF A SKIP LIST IS A TEST. Ask each record the orrery
  would ask, around each centre the body is plotted from: around the
  Sun, the helio_id; around any other centre, the id. If every one
  answers, the name comes off every list that names it, in one patch,
  and the period fetch then fetches its period. If one fails, the name
  stays and gains its comment. A skip kept for some centres and not
  others is not in this method yet; it is written here before it is
  built.
- A COMET WHOSE DESIGNATION MATCHES ITS OWN PIECES IS ASKED BY JPL'S
  PERMANENT NUMBER (L-470, Tony's ruling of 2026-10-24, "B"). After
  C/2025 K1 broke up, asking for "C/2025 K1" returned four records, the
  comet and its pieces B, C and D; the record number the entry had been
  pinned to instead (90004912) was later given to another comet,
  PANSTARRS (C/2025 B1), so the orrery drew the wrong comet. JPL's
  permanent number for the comet, asked as DES=1004075;, returns exactly
  its newest fit. Each piece is asked by its own designation (C/2025
  K1-B and so on), which returns one record. A record number is pinned
  only for a periodic comet whose designation alone is ambiguous across
  apparitions.
- A PATH CACHE KEYED BY NAME DOES NOT NOTICE A NEW RECORD (L-470). The
  orrery's path cache, data/orbit_paths.json on Tony's machine, is keyed
  by name and centre, so when an entry's id changes, a path cached under
  the old id is still served under the name. After an id change, compare
  the cached path with the new record's positions at shared dates before
  trusting it (the C/2025 K1 patch did, and found it was the comet,
  within 0.024 AU of piece B on 320 dates).

## Small-Body Record Pinning (periodic comets)

90000000+ numeric IDs are Horizons small-body RECORD numbers -- one
specific orbit solution, usually the current apparition. Use them to pin
periodic comets:
- A bare short designation ("2P") with id_type='smallbody' resolves
  AMBIGUOUSLY (Encke: 61 historical apparition records), and adding
  closest_apparition throws a syntax error -- astroquery prepends the
  required DES= key only for id_type='designation'/'name', never for
  'smallbody'.
- House pattern: pin the specific current record, no apparition flag
  needed. Halley id='90000030' and Encke '90000091', both in
  celestial_objects.py since 2026-10-10 (L-395). Proven live 2026-07-11.
- Cost of pinning: JPL re-solves a record IN PLACE (Encke's 90000091
  took new solutions on 2026-10-01 and 2026-10-09 under the same
  number), so a pin fixes the apparition, not the numbers. What a pin
  does not follow is a NEWER record, which JPL adds for a new
  apparition. The Horizons check (horizons_check.py, in the orrery's
  maintenance run since 2026-10-14; the website's Daily Run before
  that) confirms every 30 days that each pin is still
  the newest record for its comet and reports a newer one for Tony; it
  never re-pins.
- The Small-Body Database (SBDB) cannot find a Horizons record number,
  as JPL's Lookup cannot (below). Ask it by the name Horizons gives the record: "2P/Encke"
  becomes "2P", and a name ending in a bracketed designation, such as
  "MAPS (C/2026 A1)", becomes that designation
  (`orbital_period.sbdb_search_string`, L-431). SBDB's solution may not
  be the pinned record's: its sigma for 2P's period read 0.00011075 d on
  2026-10-11, where an earlier read had 0.00021413 d.

## A Small Body's Uncertainty Comes With Its Position (L-401)

Learned building the orrery's body hover, 2026-10-11 and 12. Design:
documentation/DESIGN_L401_distance_digits_rulings_20261011.md; build:
documentation/HANDOFF_L401_distance_build1_20261012.md.

- Horizons' vector query with VEC_TABLE='2xr' returns, beside the
  state, its 1-sigma uncertainties: X_s, Y_s, Z_s, VX_s, VY_s, VZ_s,
  and the same in the RTN frame, R_s, T_s, N_s, VR_s, VT_s, VN_s. R
  points "from coordinate origin to target point", so 3 x R_s is the
  3-sigma of the distance from whatever centre was asked, not only the
  Sun (read 2026-10-12 with the centre at Earth). Units follow
  OUT_UNITS: AU and AU/day with 'AU-D'.
- For asteroids and comets only. Read a missing column or "n.a." as
  MISSING, never as zero.
- Table 2 has no light time, range or range rate; work range and range
  rate out from the state.
- astroquery 0.4.11 cannot do this. Its request sets no VEC_TABLE, and
  its parser has no unit for the extra columns (a KeyError) and fills
  "n.a." with 0. So take astroquery's own request
  (`vectors(get_query_payload=True)`), add VEC_TABLE, send it directly,
  and read the columns BY NAME, never by position
  (`position_accuracy.fetch_small_body_state`). The header's first
  column reads "JDTDB,".
- It is the position query, not an extra one. If it fails, fetch the
  position the old way and record the uncertainty as missing; the
  display then says it is not included. Never a tiny invented figure.
- Write the sigma level into every field name (`range_3sigma_km`), and
  key the figure by body, centre and date.
- A check that it is the right figure: 3 x R_s matches the observer
  table's quantity 39 (RNG_3sigma). Sedna from the Sun, 2026-10-12:
  257,820 km against 257,817.569 km.
- A speed's bound: VR_s, VT_s and VN_s combined by root-sum-square,
  times 3 (ruled 2026-10-11).

## A Period Depends on Its Centre (L-431)

Learned building orbital periods, 2026-10-10 and 11. Rulings:
documentation/DESIGN_L431_orbital_periods_rulings_20261011.md.

- A distant body's osculating period depends on the centre it is taken
  around. Sedna around the Sun: 12,917 years (2025-10-10) and 12,547
  (2026-10-10); around the solar system's barycentre, 11,389.74 and
  11,389.72. Encke is steady around the Sun (0.29 d in a year) and not
  around the barycentre (7.75 d).
- The two-centre test: ask Horizons' PR at the plot date and a Julian
  year later (a year earlier if refused), around '@sun' and '@0'; keep
  the centre whose period moved less. The choice is saved with the
  period record in the orbit cache; a refresh asks only the chosen
  centre, and runs the test again if that centre moved more than the
  other did when it was chosen. Moons and the Pluto system keep the
  centre the orrery gives them (`orbital_period.build_period_record`).
- Horizons prints PR as 9.999E+99 for an open orbit; astroquery 0.4.11
  maps PR to `P`, in days.
- A body's period may be asked of another TARGET than the body (L-445,
  Tony's ruling of 2026-10-15: "Confirmed as recommended, the
  barycenter."). Earth's centre (399) circles the Earth-Moon barycentre
  once a month, so its period around the Sun swings through the month;
  Earth's period is asked of the barycentre, Horizons target 3. Earth's
  identity and position stay 399. The one home of the map is
  `orbital_period.PERIOD_TARGETS`, applied only around the Sun (Earth
  around the Earth-Moon barycentre stays 399). The record carries
  `target`, and `target_label` when it is not the body; every reader --
  the export, the period fetch, the Horizons check, the hover -- takes
  it from the record, never from a second map. The elements fetch's PR
  is then another body's and is not compared, and the record's elements
  are the target's, never drawn as the body's orbit.

## The Drawn Orbit Follows the Period's Centre (L-431, build 2)

Learned building the drawn ellipse and its markers, 2026-10-12. Ruling
7 of documentation/DESIGN_L431_orbital_periods_rulings_20261011.md;
build: documentation/HANDOFF_L431_build2_orbits_markers_20261012.md.

- The ellipse is drawn around the same centre as the period, so the
  hover and the drawing describe one orbit. The period query already
  returns the elements around its centre at the plot date; the period
  record keeps them, and `orbital_period.drawing_orbit` hands them to
  the drawing. No extra query.
- In a Sun-centred plot an ellipse around the solar system's
  barycentre is moved so its focus sits at the barycentre. Where that
  is, seen from the Sun, is the body's position from its Sun-centred
  elements minus its position from its barycentric elements, both at
  the one date; the two ellipses then meet at the body. For Sedna on
  2026-10-12 the shift was about 0.005 au (the Sun's distance from the
  barycentre, astropy's built-in ephemeris), three times its 3-sigma
  position uncertainty, so the move shows in the digits.
- Pair a record's elements with the plot's only when their dates
  match. A record from another date, or one saved before build 2 with
  no elements, leaves the drawing around its own centre, says so in the
  orbit's hover, and times its markers by the period the elements fetch
  gave around that centre, then the typed table, marked.
- A marker's date is worked out from the period that belongs to the
  drawn elements, never a period around another centre: TP plus whole
  periods, and half of one for an aphelion. A Keplerian position's mean
  motion likewise. Mixing them describes two orbits.
- A date stepped from a period carries that period's error times the
  number of periods stepped, stated in the hover where it is more than
  a day: Sedna's aphelion, half of SBDB's 1,864-day sigma, about 930
  days.
- An orbit drawn around the barycentre gets no comparison with the
  stored "mean" elements; the hover says why in one sentence (Tony's
  ruling, 2026-10-13). Around the Sun, a body this far out has elements
  that move with the Sun's own wobble about the barycentre, which the
  planets cause by pulling on the Sun (Sedna's period around the Sun
  moved 370 years in one year). The stored "mean" elements are JPL's
  elements around the Sun at the orbit solution's epoch, not means:
  Sedna's are at 2018 (a = 481 au; its `epoch` field holds the date
  Tony downloaded them, 2025). Against today's Sun-centred a of 540 au
  the difference mostly shows the wobble, not a change in Sedna's path.
  An orbit drawn around the Sun keeps its comparison. (1.4 said the
  comparison stays Sun-centred; a label saying so was built and then
  removed the same day.)

## Checking an Entry Against JPL (L-395)

Learned building the Horizons check, 2026-10-07 to 2026-10-10. The
design and every answer it rests on are in the orrery's documentation/:
DESIGN_L395_horizons_check_20261007.md and
HORIZONS_ANSWERS_L395_20261007.md.

- Two services. The Lookup (`api/horizons_lookup.api`) turns a name or
  number into the objects it matches. Horizons' main service
  (`api/horizons.api`) answers about one record (COMMAND='<record>') or
  lists every record for a designation (COMMAND='DES=<desig>;').
- The Lookup cannot see record numbers: "90000030" and "90000091" both
  give "no matches found". A pinned record is checked through the main
  service.
- A bare number is ambiguous. "499" also finds asteroid 499 Venusia;
  "9" finds the Pluto barycentre, asteroid 9 Metis and spacecraft with
  9 in their names. So an entry is found in three steps: search the
  index its id_type points at (group=mb for a blank, group=sb for
  "smallbody"); keep the match whose primary SPKID (major bodies) or
  primary designation (small bodies) equals the id; exactly one must
  remain. The other index must find nothing, or the id_type is wrong.
- JPL's names are not the orrery's. A comet carries its designation in
  brackets ("MAPS (C/2026 A1)", "ATLAS (C/2025 N1)"); the main service
  names a pinned periodic record "1P/Halley". The list keeps JPL's exact
  form in `horizons_name` and its own in `name`.
- A RECENT comet's record number is not stable. 90004956 held MAPS
  (C/2026 A1) on 2026-10-07 and another comet, PANSTARRS (C/2025 Y3),
  on 2026-10-10; MAPS had moved to 90004957. Halley's and Encke's
  numbers did not move. So find a comet with a single record by its
  designation, as the orrery finds MAPS, and pin a record number only
  for a periodic comet with many records, where the designation alone
  is ambiguous. A pin is checked by its record's name as well as its
  number, which is how a record that changed hands shows.
- Read JPL's live answers, not its documentation's examples: the
  Lookup's documentation gives Apophis's primary SPKID as 2099942,
  while the live answer is 20099942, with 2099942 an older alias.

## Where the Check Lives, and What It Compares (L-395, L-431 build 3)

Moved 2026-10-14 from the website's Daily Run into the orrery (Tony,
2026-10-12: "the orrery stores and serves the data not the other way
around"). The move's brief is
documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md; the
build's record, documentation/HANDOFF_L431_build3_website_20261014.md.

- `horizons_check.py` is a GENERATOR row of the orrery's maintenance
  run, just before the objects export, so the export carries the dates
  it writes. `check_horizons_confirmations.py` is a CHECKER row that
  reads what it wrote, offline. The website keeps an offline check of
  its own, `tools/check_horizons_confirmations.py`, which reads the
  dates from the pulled export and goes red, naming the objects, on the
  day one turns 30 days old.
- `period_fetch.py` runs first, a GENERATOR row just before the check
  (L-444, 2026-10-15). For each served object whose period is not
  fetched -- typed, none, or a new object with no cache entry -- it
  makes plotting's own call, `fetch_osculating_elements(...,
  center_body=None, with_period=True)`, without the dialog, and saves
  it as plotting does, so the check compares the new period with JPL
  the same day. It asks nothing on most runs, saves nothing for a body
  whose answer is not whole, and says UNREACHABLE. The check itself
  still fills no gaps.
- Only what is due is asked: a part of an entry never confirmed, one
  confirmed 30 days ago or more, or one that has changed since (the
  record keeps what was confirmed, so a change shows). On most runs it
  asks JPL nothing. An identity or a period is asked again from day 25
  ("renewing"): the website goes red at day 30 and sees a new date only
  after the orrery's push and its own pull, so asking at day 30 would
  leave it red every cycle. The offline checker passes a renewing
  confirmation until day 30. The data sheets keep 30.
- A small body's COMMAND ends with ';', sent as %3B, as JPL's own
  examples send it; a bare ';' in a URL can end the parameter early.
- The period: for an entry whose period was fetched, one ELEMENTS query
  as the orrery asked it -- the same COMMAND, CENTER the period's own
  centre, TLIST the period's own date written as a calendar Julian day,
  OUT_UNITS AU-D -- and JPL's PR must lie within the period's own error
  of the period the website prints. A typed period, or none, is not
  compared; the line names it as not from JPL.
- Any failure to get JPL's answer is "could not reach JPL". It never
  passes, nothing is recorded for that part, it stays due, and the run
  asks JPL nothing more that day. The verdict says UNREACHABLE by name:
  the convention for every row that needs the network.
- The data sheets: every spacecraft in the list (an id starting with
  '-') has its Horizons data sheet re-read on the same 30-day cycle,
  into `data/spacecraft_sheets.json`. Red only where a row of
  `constants_new.py` quotes a figure from the sheet and the sheet no
  longer gives it (Tony's option A, 2026-10-12: "the row claims the
  figure, not the page"); a patch to the row clears it. A sheet whose
  "Revised:" date moved and whose figure did not is noted, not red.
  Nothing here edits a row.
- The thirteen identity confirmations of 2026-10-10 were carried over
  with their dates, so the move asked JPL nothing. The offline tests run
  on JPL's recorded answers,
  `documentation/worksheets/horizons_answers_L395.json`. Its identity
  answers are JPL's own; its elements and data-sheet answers were
  written in JPL's format by the build, which could not reach JPL, and
  the file says so for each, so the first live run is the real test of
  the parsing. The same file freezes the inputs the test runs on (the
  three cache entries, the carried confirmations, the seeded sheets):
  a test that read the live records would fail on the day the check
  first worked.

## How a Path's Events Are Found (L-443)

Built 2026-10-24 for slice 2's paths, in `path_plan.py`; the rulings are
1, 5 and 7 of documentation/DESIGN_L443_slice2_rulings_20261023.md
("One path rule, the orrery's"; the nearest approach, "which is
mechanical"; the 30-day cycle). The offline suite, `test_path_plan.py`,
runs on a made-up solar system written in JPL's vector format; the
first run against JPL is Tony's.

- AN EVENT is a nearest approach that needs finer steps than the path's
  backbone, a point every 7 days (Voyager 1's proven step). Two tests:
  - it is a PASS: the nearest approach lies inside the body's Hill
    sphere, r x (GM / (3 GM of the primary)) ** (1/3), r the body's
    distance from its primary at that moment. The Moon's primary is
    Earth; every other body's is the Sun. The Sun, the drawing's own
    centre, has no gate. Without this test the curvature rule alone took
    nearest approaches 85 million km from Mercury and 103 million km
    from the Moon for events (the first offline run): it cannot tell a
    pass from two bodies merely being nearest each other.
  - the CURVATURE RULE: about 30 points through a half circle at the
    passing distance and speed, so an ideal step of pi x d / v / 30
    (spacecraft_encounters._calculate_encounter_resolution), shorter
    than the backbone's.
  A daily sample can sit up to half a day of travel from the true
  nearest moment, so both tests are first put to the distance less half
  a day's travel, then again at the nearest minute.
- GM IS JPL'S, read from the body's data sheet (OBJ_DATA=YES,
  MAKE_EPHEM=NO) when a plan is made. A major body's sheet prints it
  three ways, read 2026-10-24 for 399, 599, 301, 10 and 999:
  "GM, km^3/s^2 = ...", "GM (km^3/s^2) = ..." and "GM (planet) km^3/s^2
  = ...". A small body's prints "GM= <value>" or "GM= n.a.". Never the
  "GM 1-sigma" line, which can come first. A body whose sheet gives no
  GM has no Hill sphere to pass inside and is named as not searched;
  that is most small bodies, so a spacecraft's asteroid flybys are not
  events of the drawing (they bend nothing a Sun-centred room shows).
- WHERE THE NUMBERS COME FROM. Each body's position, and each path's,
  daily around the Sun, one fetch per body shared by every due path;
  the distance is worked out here. The nearest minute in two passes,
  resolve_encounter_time's numbers: hourly for 1.5 days either side,
  then each minute for 90 minutes either side of the nearest hour.
  Around a major body the path is asked centred on it ('500@<id>');
  around a small body, which Horizons cannot centre on by its
  designation, both are asked around the Sun and differenced.
- THE WINDOW AND THE STEP are spacecraft_encounters' own (half-width
  four times the distance, the crossing time times 1.5, about 30 points
  through the half circle), so the orrery's encounter views and the
  website use one rule. Its steps stop at six hours; where the ideal is
  a day or more the step is whole days, never more than the ideal.
- THE 30-DAY CYCLE. A plan is made again when it is 30 days old, or at
  once when its inputs change (id, id_type, span, the bodies searched).
  Events more than 30 days old are carried, not asked again, and the
  search starts 3 days before them; a path whose span ended before that
  asks nothing. A failure to reach JPL keeps every plan as it was and
  says UNREACHABLE by name.
- TIMES. Horizons labels a vector table's times TDB (its JDTDB column);
  the plan writes its moments in that scale. The first live run is the
  test that the windows' START and STOP times are read in the same.
- THE ORBITER RULE (Tony's ruling of 2026-10-24, L-443; built
  2026-10-25, `orbiter_rule`). The days a path spends inside one body's
  Hill sphere, each day tested at its distance less half a day's travel,
  form a STRETCH. One nearest approach in a stretch is a FLYBY. More than
  one is a CAPTURE: its first nearest approach, the ARRIVAL, is an
  event, and its last before the spacecraft leaves, the DEPARTURE; the
  approaches between are not, because in the Solar System room the
  spacecraft rides with the body and the loops wait for the body's own
  room. A capture that runs to the end of the days searched is an
  arrival with no departure (`stays`: a landing, or the end of JPL's
  data); one already under way on the first day searched gives no new
  arrival (a plan made again carries it). The Sun has no Hill-sphere
  gate, so every nearest approach to it can be an event, kind
  `perihelion` (Parker's 42 among them). Each event names its kind:
  flyby, arrival, departure or perihelion. On the preview of 2026-10-24
  the rule turns Juno's 110 passes of Jupiter and Europa Clipper's 83
  into one arrival each.
- THE RULE IS AMONG A PLAN'S INPUTS (`RULE`, now 2), so a plan made by
  an older rule is made again at once, like one whose id or span
  changed.
- A LONG RUN PRINTS AS IT GOES, SAVES AS IT GOES, AND KEEPS UNDER THE
  MAINTENANCE RUN'S 15 MINUTES (Tony, 2026-10-24, after a first preview
  sat 20 minutes on a blank window). A first line before JPL is asked
  anything; a line, with the seconds since the start, as each answer
  arrives and each event is found; each plan saved as it is made; and a
  10-minute limit after which nothing new is started, what is left
  named and taken up by the next run. The dashboard's "Path Plan --
  every path, now" lifts the limit (--all --no-limit). The same shape
  suits any JPL run that can take minutes.
- KEYING. A key in the objects export with no website entry stops the
  website's objects mirror, and with it the Daily Run's pulls. So a
  spacecraft is keyed in the same round as its website entry. The twelve
  were keyed on 2026-10-25 (orrery patch_L443_13), and the temporary
  --preview flag that planned them by name before then went with it;
  that patch carried each preview plan made by the orbiter rule into
  data/path_plans.json under its new key, so no second half-hour run was
  needed. A spacecraft serves no orbital period in the export.
- ON THE WEBSITE the builder thins each event's window at the event's
  own scale, a point kept where the path bends away from the chord by
  more than 1% of the passing distance (gallery-cache-builder, A
  Spacecraft Is Fetched by Its Plan): the encounter rule's window for a
  pass of the Sun at 0.3 AU runs about 50 days either side at 6-hour
  steps, some 400 points for a gentle curve.

## Reference Frame Diagnostic

Inclination tells you the frame: low (1-5 deg) = equatorial; high
(20-30 deg) = ecliptic. Reference frames can differ for the SAME object
across queries -- when a rendered orbit looks wrong, check inclination
before touching code. Osculating elements must match the viewing center
(the Charon@9 lesson: elements about the Pluto barycenter, viewed from
Pluto, render wrong).

## Query Mechanics

- Horizons step format: {number}{unit} -- 1m, 5m, 1h, 6h, 1d.
- API returns empty -> check the explicit fallback list (Graceful
  Fallback pattern, resident protocol Part 2): fallback -> calculate
  locally -> attribute the source. Explicit lists, not automatic.
- Cache structure: cache[name]['elements'] (nested dict) -- the elements
  live one level down.

## Encounter and Flyby Resolution

Two length scales, two jobs:
- Cube scale (dist_km * 4) frames the VIEW.
- Curvature scale drives the FETCH STEP -- sample finely enough that the
  hyperbolic arc curves smoothly through closest approach.
Close-approach plots then need the 3D axis dtick/range override (see
orrery-coding-conventions) because default AU-scale axes make
Earth-neighborhood geometry invisible.

Encounter-building workflow note: the end-to-end encounter pipeline
(spacecraft_encounters entries, encounter export, camera capture) is
still evolving under ledger item L-046. This skill carries the stable
orbital-mechanics facts; do not treat it as the encounter build recipe.
Read the current code and ledger item at HEAD before building encounters.

## Field Notes

- The barycenter rule (visualize only when the barycenter lies outside
  the primary; mass ratio as gatekeeper) lives in
  orrery-coding-conventions -- it is a rendering decision.
- Celestial sphere in the ecliptic frame: unit vectors rotated from
  equatorial via obliquity about the X axis.
- Roche limit is not absolute: tensile strength allows survival inside it.
- When Claude's rendered geometry disagrees with Tony's eyes, the render
  wins and frames are the first suspect. Never explain away what the eyes
  see.
