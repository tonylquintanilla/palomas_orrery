---
name: gallery-assembler
description: Technical home for the interactive gallery's client-side rendering mechanism -- render_orbits.py (Kepler propagation, orbit-shape sweep), resolver.py (scene resolution, served_window gating), cache_reader.py (read-only served-cache access), the trust/served_window system (M2), and the golden-artifact build+Mode-5 acceptance process. Distinct from gallery-cache-builder (nightly data production) and gallery-pipeline (the older Studio/converter/static-viewer chain). Use for propagation math, resolver/cache_reader internals, golden artifact builds, or orrery-vs-assembler boundary questions. Do not use for projects other than Paloma's Orrery.
fires_when: render_orbits.py, resolver.py, cache_reader.py, propagation math, golden artifact builds, Mode 5 acceptance, orrery/assembler boundary questions
---

# Gallery Assembler

Skill version: 1.0 | Cut from gallery @ a7abea59ed5368a38ce7364ce53b4679aa83b5a1 / orrery @ e775050d227fa63aa79e97a7af3f290a5c038899 | July 20, 2026
Sources: render_orbits.py, resolver.py, cache_reader.py (read live this
session); master plan §3; L-149/L-150/L-151.

## The boundary this skill exists to protect

The assembler is not a port of the desktop orrery -- it's new code solving
a problem the orrery never has. The orrery asks Horizons the right
question, live, every time; there's no local math to get wrong because
there's no local math. The assembler has no live connection (Pyodide can't
reach Horizons), so it must cache a recipe once and reconstruct it
correctly later, alone. Nearly everything distinguishing the two --
staging/atomic-swap, client-side propagation, trust measurement itself --
exists because of that one constraint. Full treatment: master plan §3,
protocol Part 4 ("The Orrery and the Assembler").

What carries over: orbital mechanics, Horizons conventions, the visual
language (single-info-marker pattern, AU-hover convention,
barycenter-outside-primary rule) -- as knowledge, not code. It shows up
verbatim in assembler modules (render_orbits.py's info marker matches the
orrery's exactly).

**Rule:** new objects are authored in the orrery's celestial_objects.py
FIRST, then ported to objects_config.json. Never invented fresh in the
assembler. (Encke is the known exception -- in objects_config.json for
M1/M2 testing ahead of the orrery; confirmed absent from
celestial_objects.py as of July 20, 2026. Closing that gap doubles as a
live test of the porting pipeline.)

## The three core modules

**render_orbits.py** -- no network, no file access, two jobs:
- `sweep_conic(osc, n_points)`: static orbit-shape polyline, geometric,
  no time dependence.
- `propagate_marker(osc, t_jd)`: position at a specific date, via Kepler's
  equation from the stored epoch. This is what actually renders as the
  marker -- NOT the served `as_of_today` field, which is a build-time
  cross-check only (validated once, for Earth, to 2.6e-11 AU). Don't
  conflate the two.

Both take an `osc` dict and don't care what center it's expressed in -- the
math is frame-agnostic. Feed it Earth's heliocentric elements or the
Moon's Earth-relative elements and it correctly returns a position
relative to whatever center the input describes. The math was never the
gap for Pluto/Charon or Moon/Io/Titan rendering -- the gap is one level up.

**resolver.py** -- `resolve(scene_spec, catalog, ...)` checks
`served_window` as ONE bound for the ENTIRE scene, before resolving any
individual object -- not per-object. A scene asking for just Jupiter is
gated by the same bound as a scene asking for everything. This is why
L-149 mattered: one bad participant silently narrows every scene, not
just scenes containing that object.

**cache_reader.py** -- thin, read-only wrapper over a parsed
coverage_index.json dict; never touches network or astroquery.
`require_orbit_payload(slug)` raises `MissingCachePayloadError` if an
object has no `osculating` block -- the concrete enforcement point for
L-150: an object with only a barycentric cache and no heliocentric one
fails HERE, with a specific error, the moment a whole-system scene tries
to include it. (Known stale doc: its own docstring still says
served_window is "currently null at HEAD... tracked with F1" -- pre-M2,
no longer true; fix next time you're in that file.)

## No composition between frames -- retired by design

A near-equal-mass binary needing both a wide (heliocentric) and close
(barycentric) view means TWO independent fetches -- never one derived
from the other. Composition (parent position + local offset) was tried
and retired by the v4 model correction: subtracting two large,
nearly-equal position vectors for a small relative one is catastrophic
cancellation, worsened by sampling aliasing. "Pluto/Charon two-view"
already names the correct model: two self-contained scenes. Ordinary
planet-moon systems (barycenter INSIDE the primary) don't need this --
the existing single parent-relative orbit already is their complete
picture. Same barycenter-outside-primary rule as elsewhere in this
project, not a separate judgment call.

## Trust / served_window system (M2)

Each non-excluded object: fetch elements at its own center, fetch two
check-vectors at +/-delta_days around the SAME center's epoch, compare
against Kepler propagation, cap the window at a category fraction of its
own period (_TRUST_CAP_DIVISOR: planet/dwarf_planet/asteroid = P, moon =
P/8, comet = P/2). Comets with `overrides.comet.anchor == 'Tp'` (Halley,
Encke) anchor at their solution epoch, which can be decades from "today."

Global participation is gated by `canonical_frame ==
TRUST_WINDOW_PARTICIPANT_FRAME` ('heliocentric') -- corrected in L-149
from a category check, which let Pluto (dwarf_planet, but
barycenter-centered) wrongly gate the whole site with its ~6.4-day
mutual-orbit window. Future barycenter/parent-relative objects are
excluded the same way automatically.

## Golden artifact process

7 settled artifacts: Earth; Jupiter/Saturn; Moon/Io/Titan; Halley/Encke;
Voyager 1; Pluto/Charon two-view; Halley+event_link. Each closes only
after Mode 5 -- Tony's visual confirmation, not a passing test suite.
Artifact 1 (Earth) is the only one closed (fingerprint
`abbd01094852b57f`, L-080 harness). Established conventions: dark theme,
3/4 perspective camera (eye 1.25,1.25,1.25), 25% buffer beyond the
largest orbital radius, uniform dtick.

## Layered gate, distinct from gallery-cache-builder's

This skill's artifacts get Mode 5 visual acceptance. The BUILDER's data
(gallery-cache-builder's Layer 1/2) is a separate, earlier gate -- an
artifact can only be attempted once its objects' served data passes that
gate. Don't conflate "the cache is good" with "the render is right":
Pluto/Charon and Moon/Io/Titan are both, as of tonight, in the state of
"data plumbing partially tested, render never attempted."