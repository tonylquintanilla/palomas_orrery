---
name: horizons-orbital-mechanics
description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data, position_accuracy, orbital_period). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, a small body's position uncertainty (VEC_TABLE 2xr), orbital periods and the centre they are taken around, the drawn orbit and its markers' dates, encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.
fires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning, 2xr uncertainties, periods, the drawn orbit's centre
---

# Horizons and Orbital Mechanics Reference

Skill version: 1.5 | 2026-10-13, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 400a9615. v1.5 (L-431) corrects one bullet of 1.4, by
Tony's ruling of 2026-10-13: an orbit drawn around the solar system's
barycentre gets no comparison with the stored mean elements. 1.4 said
the comparison stays Sun-centred; for a body as far out as Sedna that
mostly measures the Sun's own wobble. A second version in one session, as interactive-exhibit 1.14
was, because the ruling came after 1.4 was installed.
Earlier: 1.4 | 2026-10-12, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ c9722520. v1.4 (L-431, with L-401) adds The Drawn Orbit
Follows the Period's Centre, what L-431's second build learned: the
period record keeps Horizons' elements around its own centre, a
barycentre ellipse in a Sun-centred plot is moved to where the
barycentre is, found from the body's two element sets at one date, a
marker's date comes from the period of the drawn elements, and a date
stepped from a period carries that period's error.
Earlier: 1.3 | 2026-10-12, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 47815de2. v1.3 (L-401, L-431) adds what two builds
learned, in one version as both items asked: A Small Body's
Uncertainty Comes With Its Position (VEC_TABLE='2xr', which astroquery
0.4.11 cannot ask for or read, so a direct call read by column name);
A Period Depends on Its Centre (the two-centre test and its saved
choice); and the Small-Body Database's lookup of a pinned record by
the name Horizons gives it, under Small-Body Record Pinning.
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-12 and 2026-10-13 (L-431).

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
  apparition. The gallery's Horizons check (tools/horizons_check.py,
  the Daily Run's step 2) confirms every 30 days that each pin is still
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
