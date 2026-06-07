# Spacecraft Closest Approach Infrastructure — Handoff Document

**Project:** Paloma's Orrery  
**Prepared:** March 4, 2026  
**Status:** Design complete. Implementation not started.  
**Related:** `apophis_handoff.md` (Capabilities A-C), `comet_perihelion_handoff.md` (Capability D)

---

## What This Is

A composable capability for marking and annotating the closest approach of any spacecraft
to any target — planets, moons, asteroids, comets, even the Sun. Motivated by the rich
mission context already in the orrery: Lucy's Patroclus flyby, Juno at Jupiter, New Horizons
at Pluto, OSIRIS-APEX at Apophis, Voyager encounters with the outer planets.

The existing `add_closest_approach_marker` already finds the closest *plotted* point from
trajectory data. This infrastructure adds precision (actual closest approach, not just
closest sampled point) and richness (hover text with approach parameters, dedicated
legend entry, optional velocity annotation).

---

## The Core Difference From the Apophis Case

**Apophis (Capabilities A-C):** Small body approaching a major planet. The JPL CAD API
serves precision approach data — date, distance, velocity, uncertainty — because the
CAD API covers all small bodies against all major planets.

**Spacecraft:** Negative SPKID numbers (`-61` for Juno, `-31` for Voyager 1, `-98` for
New Horizons). The CAD API does **not** cover spacecraft. Their closest approaches must
come from Horizons trajectory data directly.

This is actually fine — the orrery already fetches spacecraft trajectories from Horizons
at configurable time resolution. The challenge is:

1. Finding the true closest approach within the plotted window (not just the closest
   sampled point, which depends on time step)
2. Expressing it with the right apsidal terminology for the target body
3. Making hover text informative: approach date, distance, relative velocity, mission context

---

## What Already Exists

### `add_closest_approach_marker` in `apsidal_markers.py`

Already works for any object / center body pair. Finds minimum distance in
`positions_dict`, adds a marker with proper terminology (Perijove, Periareion,
Perihelion, etc.). The apsidal terms table already covers: Sun, Mercury, Venus, Earth,
Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto — everything a spacecraft might
encounter.

**Current limitation:** Uses the closest *sampled* point. If time resolution is
13 hours, the true closest approach could be hours away from the nearest sample.
For most science communication purposes this is fine — but for precise encounters
(Lucy at Patroclus: ~1 hour window) it matters.

### `show_closest_approach_var` in `palomas_orrery.py`

Already connected to the UI. Already calls `add_closest_approach_marker` for
trajectory objects in `plot_actual_orbits`. So the checkbox and basic infrastructure
exist — this work refines and extends it.

### Mission info strings in `celestial_objects.py`

Every spacecraft entry already has `mission_info` with human-readable context:
flyby date, target name, encounter speed, science goals. This is the hover text
source — just needs to be wired into the approach marker.

---

## What Needs To Change

### 1. Precision closest approach via Horizons bisection (optional enhancement)

The current approach finds the closest *sampled* point. For a higher-precision
closest approach time:

**Method A: Horizons dense fetch around the minimum**

When the closest sampled point is found, fetch a dense trajectory (e.g. 1-minute
steps) in a ±6 hour window around it. Find the true minimum from the dense sample.
No new API required — just a second Horizons call with a narrow date range and
fine time step.

```python
# After finding closest sampled point at `closest_date`:
dense_dates = [closest_date - timedelta(hours=6 + i/60)
               for i in range(720)]  # 1-min steps, 12-hr window
dense_traj = fetch_trajectory(spacecraft_id, dense_dates, center_id=target_id)
# Find true minimum in dense_traj
```

**Method B: Scipy minimize_scalar on Horizons interpolation**

More elegant but requires scipy. Probably overkill for this use case.

**Recommendation:** Method A for special encounters (Lucy/Patroclus, Juno/Io),
keep existing sampled minimum for routine use. Add a flag to `celestial_objects.py`:
`'precision_flyby': True` for encounters worth the extra fetch.

### 2. Approach velocity from trajectory data

Relative velocity at closest approach is the most scientifically interesting
annotation. Compute from consecutive position differences:

```python
# From dense trajectory around closest approach:
dt_seconds = 60  # 1-minute steps
dx = pos2['x'] - pos1['x']  # AU
dy = pos2['y'] - pos1['y']
dz = pos2['z'] - pos1['z']
dr_au = np.sqrt(dx**2 + dy**2 + dz**2)
v_km_s = dr_au * 149597870.7 / dt_seconds
```

This gives the spacecraft velocity relative to the *center body* (e.g. velocity
relative to Jupiter when approaching Juno's perijove). For encounters with small
bodies (Lucy/Patroclus), center = Sun, so this gives heliocentric velocity — not
the encounter velocity. For the encounter velocity, compute relative to the target.

**For planet flybys (Juno/Jupiter):** Velocity relative to center body is correct.

**For small body flybys (Lucy/Patroclus, OSIRIS-APEX/Apophis):**
Need two trajectories — spacecraft and target — and compute the difference.
The mission_info strings already carry encounter speed from the literature:
e.g. Patroclus flyby: 8.815 km/s. Use stored value as hover text for small
body encounters rather than computing it.

### 3. Enhanced hover text incorporating mission context

Current `add_closest_approach_marker` hover text: distance, date, generic terminology.

Enhanced hover text should include:
- Closest approach date and time
- Distance (AU, km, and body radii for planet flybys)
- Velocity at closest approach (km/s) — computed or from mission_info
- Mission name and context (from `mission_info` in `celestial_objects.py`)
- What was observed / science objectives (brief)

Pattern — build in the marker function from obj_info:

```python
mission_info = obj_info.get('mission_info', '')
hover = (
    f"<b>{obj_name} — {near_term}</b><br>"
    f"Date: {date_str_formatted}<br>"
    f"Distance: {km_distance:,.0f} km ({au_distance:.6f} AU)<br>"
    f"Velocity: {v_rel:.2f} km/s<br><br>"
    f"{mission_info}"
)
```

### 4. New function: `_add_spacecraft_encounter_markers()` in `palomas_orrery.py`

Parallel to `_add_close_approach_extras()` but for trajectory-type objects approaching
any target in the scene.

**Trigger conditions:**
- `show_apsidal_markers == True` (reuse same checkbox)
- Object has `object_type == 'trajectory'`
- A target body is also selected in the scene

**How to identify encounter targets:**

The spacecraft's `positions_dict` is already computed relative to the center body
(usually Sun). To find encounters with non-center bodies:

```python
for spacecraft_name in selected_trajectories:
    sc_positions = orbit_cache[spacecraft_name]  # heliocentric positions
    for target_name in selected_planets:
        target_positions = orbit_cache[target_name]  # also heliocentric
        # Compute relative distance at each time step
        # Find minimum -> encounter candidate
        relative_distances = compute_relative_distances(sc_positions, target_positions)
        if min(relative_distances) < ENCOUNTER_THRESHOLD_AU:
            mark_encounter(spacecraft, target, min_point)
```

**ENCOUNTER_THRESHOLD_AU** — needs calibration. Jupiter's Hill sphere is ~0.35 AU.
Saturn's is ~0.41 AU. Start generous (0.5 AU) and add a per-object override in
`celestial_objects.py` if needed.

**Center body encounters (e.g. Juno/Jupiter when center=Jupiter):**

When the user has set center=Jupiter, spacecraft positions are already Jupiter-relative.
`add_closest_approach_marker` already handles this correctly — just needs to be called
with the right `positions_dict`. This path is already working for the Juno case.

### 5. Target body coverage

The apsidal terms table in `apsidal_markers.py` already covers all planets and Moon.
For small body encounters (asteroids, comets), the function falls back to generic
terms. Add terms for the most common spacecraft targets:

```python
# In APSIDAL_TERMS dict:
'Bennu':      ('Peribennu', 'Apobennu'),
'Ryugu':      ('Periryugu', 'Aporyugu'),
'Arrokoth':   ('Periarrokoth', 'Apoarerokoth'),
'Apophis':    ('Periapophion', 'Apoapophion'),
'Patroclus':  ('Peripatroclia', 'Apopatroclia'),
# Or just use generic: ('Periapsis', 'Apoapsis') for unnamed targets
```

These are informal coinages — scientifically fine for educational use. Alternatively,
always use 'Periapsis'/'Apoapsis' for small bodies and reserve named terms for planets.

---

## Key Architecture Decision: Two Modes

**Mode 1: Center body = spacecraft target**
User sets center = Jupiter, plots Juno. Juno positions are already Jupiter-relative.
`add_closest_approach_marker` fires directly on the Juno `positions_dict`.
This already works — just needs the enhanced hover text from mission_info.

**Mode 2: Center body = Sun (heliocentric), target is a non-center body**
User plots New Horizons + Pluto, center = Sun. Both have heliocentric positions.
Need to compute New Horizons position *relative to Pluto* to find the flyby.
This is the new capability — requires pairwise relative distance computation.

Mode 1 is trivial and already nearly complete. Mode 2 is the main work.

---

## Implementation Sequence (Recommended)

**Step 1:** Add `mission_info` to hover text in `add_closest_approach_marker`.
Single targeted change to `apsidal_markers.py`. Immediately improves all
existing closest-approach markers for trajectory objects. Low risk.

**Step 2:** Add apsidal terms for common small body targets in `apsidal_markers.py`.
Surgical addition to the APSIDAL_TERMS dict.

**Step 3:** Implement Mode 2 pairwise relative distance computation in a new helper
function. Test with New Horizons + Pluto (July 2015), known closest approach
~12,472 km.

**Step 4:** Wire Mode 2 into the plotting pipeline via `_add_spacecraft_encounter_markers()`.

**Step 5 (optional):** Precision bisection for special encounters flagged with
`'precision_flyby': True` in `celestial_objects.py`.

---

## Test Cases

### Mode 1 (already works, just needs hover text enhancement)

| Spacecraft | Center | Encounter | Known distance |
|------------|--------|-----------|----------------|
| Juno | Jupiter | Perijove passes | ~4,200 km (closest) |
| Cassini | Saturn | Pericronian | ~1,600 km closest pass |

### Mode 2 (new capability)

| Spacecraft | Target | Date | Known distance |
|------------|--------|------|----------------|
| New Horizons | Pluto | 2015-Jul-14 | 12,472 km |
| New Horizons | Arrokoth | 2019-Jan-01 | ~3,500 km |
| Voyager 1 | Saturn | 1980-Nov-12 | 124,000 km |
| Lucy | Dinkinesh | 2023-Nov-01 | ~430 km |
| Lucy | Donaldjohanson | 2025-Apr-20 | ~850 km (nominal) |
| Lucy | Patroclus-Menoetius | 2033-Mar-03 | ~1,276 km |
| OSIRIS-APEX | Apophis | 2029-Apr-13 | 38,013 km (but via CAD API) |

For OSIRIS-APEX / Apophis: the approach distance is already handled by Capability B
(CAD API marker). The spacecraft-specific enhancement here is adding mission context
hover text and velocity annotation.

---

## Integration With Existing Close Approach Infrastructure

The three systems are complementary and non-overlapping:

| System | Object type | Epoch source | Distance source |
|--------|-------------|--------------|-----------------|
| Capabilities A-C | Small body → planet | JPL CAD API | CAD API |
| Capability D | Comet → Sun | Osculating elements TP | Horizons |
| **This capability** | **Spacecraft → any target** | **Horizons trajectory** | **Trajectory positions** |

No collisions. All three can coexist and fire independently on the same plot.

---

## Parallel Pipeline Note

The orrery maintains parallel data pipelines (orbit traces, position dict, hover text,
plotted period, animation). When adding encounter markers for spacecraft, verify that
`positions_dict` for trajectory objects is accessible from the same scope as the
marker call. In the Apophis case, `best_approach` had to be hoisted to outer scope.
Check whether spacecraft `positions_dict` needs similar hoisting in
`_add_spacecraft_encounter_markers()`.

---

## For Paloma

*"Every spacecraft we've ever sent into the solar system got its energy for free —
from a planet's gravity. When Voyager 2 flew past Jupiter, Saturn, Uranus, and Neptune,
each flyby swung it faster and redirected it toward the next target. Scientists called
it the 'Grand Tour,' and it only works once every 176 years when all four planets align.*

*The orrery can show exactly where each spacecraft was closest to each planet — the
moment of maximum gravity assist, when the planet's pull was strongest. That's the
moment that sent Voyager 2 on its way to the stars. We can mark every one of those
moments, for every spacecraft, against every target it ever encountered."*

---

## Quotables

*"The CAD API covers small bodies. Spacecraft need trajectory data. Two different sources, same visual language."*  
*"Mode 1 already works. Mode 2 is the new capability."*  
*"Every flyby is a free energy transfer. The marker shows where the handoff happened."*  
*"The Grand Tour only works once every 176 years. We can show the exact moments it happened."*  
*"Closest sampled point is good enough for most cases. Precision bisection for the special ones."*

---

**Prepared by:** Tony (with Claude)  
**Session:** March 4, 2026  
**Prerequisite reading:** `apophis_handoff.md`, `comet_perihelion_handoff.md`
