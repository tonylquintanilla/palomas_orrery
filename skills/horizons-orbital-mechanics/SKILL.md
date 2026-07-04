---
name: horizons-orbital-mechanics
description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.
---

# Horizons and Orbital Mechanics Reference

Skill version: 1.0 | Cut from palomas_orrery @ b29ad3f8 | July 1, 2026
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
