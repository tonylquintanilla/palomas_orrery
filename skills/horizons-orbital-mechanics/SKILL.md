---
name: horizons-orbital-mechanics
description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.
fires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning
---

# Horizons and Orbital Mechanics Reference

Skill version: 1.2 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 32619f8d and gallery @ a7d1a542. v1.2 (L-395) adds
Checking an Entry Against JPL, what the Horizons check's build learned:
JPL's Lookup cannot see record numbers; a bare number also finds
asteroids and spacecraft, so an entry is found in three steps; JPL
re-solves a record in place; and a recent comet's record number can be
given to another comet. It corrects two lines under Small-Body Record
Pinning: Encke's pin now lives in the orrery's list, and what a pin
does not follow is a NEWER record, not a new solution.
Earlier: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.

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
