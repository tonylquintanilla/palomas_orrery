# Apophis Close Approach Infrastructure - Session Handoff
**Date:** March 1, 2026  
**Session Type:** Planning / Architecture Design  
**Status:** Design complete, ready to build

---

## Summary

Planned new infrastructure for visualizing close approaches in Paloma's Orrery, motivated by asteroid 99942 Apophis's historic Earth flyby on April 13, 2029 (Friday the 13th). The design session produced a complete architecture for three composable capabilities that work for any small body flyby, not just Apophis.

### Key Discovery: JPL Close Approach Data (CAD) API

The CAD API (`ssd-api.jpl.nasa.gov/cad.api`) is general-purpose infrastructure covering ALL small bodies in JPL's database against any major body (Earth, Moon, Mars, Jupiter, etc.). For Apophis, it returns:

- **Perigee time:** 2029-04-13 21:46:12 TDB (JD 2462240.407091595)
- **Distance:** 0.000254099 AU = 38,012.7 km center-to-center = 31,634.5 km from surface
- **3-sigma uncertainty:** +/- 2.0 km (extraordinarily precise)
- **Relative velocity:** 7.422 km/s
- **Passes BELOW geostationary orbit altitude** (38,013 km vs 42,164 km)

Cross-validated against Tony's uploaded geocentric osculating elements: Tp agrees to 0.1 seconds, QR agrees to 1.2 km. The data sources tell the same story.

---

## Architecture (Agreed)

### Capability A: CAD API Integration

**New module:** `close_approach_data.py`

**Purpose:** Fetch and cache close approach data from JPL's CAD API for any small body against any major body.

**API details:**
- Endpoint: `https://ssd-api.jpl.nasa.gov/cad.api`
- Query by designation: `?des=99942&body=Earth&date-min=2029-01-01&date-max=2030-01-01&dist-max=0.5`
- Returns JSON with: JD time, calendar date, nominal distance (AU), 3-sigma min/max distance, relative velocity (km/s), V-infinity (km/s)
- Supports bodies: Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto (use abbreviated names: `Merc`, `Venus`, `Earth`, `Mars`, `Juptr`, `Satrn`, `Urnus`, `Neptn`, `Pluto`, `Moon`)
- Also supports `body=ALL` to get all close approaches

**Function signature:**
```python
def get_close_approaches(designation, body='Earth', date_min=None, date_max=None):
    """
    Returns list of close approach events within the specified date range.
    Each event contains: jd, date_str, dist_au, dist_min_au, dist_max_au,
                         v_rel_kms, v_inf_kms, orbit_id
    """
```

**Caching:** Store in existing `data/orbit_paths.json` with `close_approach:` prefix:
```json
"close_approach:Apophis:Earth": {
    "designation": "99942",
    "body": "Earth",
    "approaches": [
        {
            "jd": 2462240.407091595,
            "date": "2029-Apr-13 21:46",
            "dist_au": 0.000254099098170977,
            "dist_min_au": 0.000254085852623379,
            "dist_max_au": 0.000254112343772133,
            "v_rel_kms": 7.42249308586014,
            "v_inf_kms": 5.84135545611464
        }
    ],
    "fetched": "2026-03-01",
    "orbit_id": "206"
}
```

Benefits of using orbit_paths.json: already has multi-generation backup safety procedures, manually searchable, one cache to manage.

### Capability B: Perigee Marker

**Integration point:** `palomas_orrery.py`, in the apsidal markers section (after existing perigee/apogee logic).

**When plotted:** Only when a CAD close approach falls within the plotted date range. Controlled by existing "Show apsidal markers" checkbox.

**How plotted:**
1. Check CAD cache for close approaches within plotted date range
2. At the CAD perigee time, fetch exact position vector from Horizons (geocentric)
3. Plot as marker with distinct style (diamond or distinct square, differentiated from Keplerian perigee/apogee markers)
4. Hover text includes:
   - Exact time (from CAD API)
   - Center-to-center distance (AU and km)
   - Surface distance (km) -- requires center body radius
   - Relative velocity (km/s)
   - 3-sigma uncertainty range (km)
   - Note: "JPL CAD close approach -- may not coincide with plotted trajectory due to time resolution"
   - Data source attribution

**Important:** The marker may not sit exactly on the plotted trajectory line. The trajectory uses evenly-spaced-in-time points (e.g., 51 points over 28 days = ~13.2 hour spacing), but periapsis timing rarely aligns with those samples. The offset between marker and trajectory is informative -- it shows the gap between plotted resolution and actual precision.

### Capability C: Hyperbolic Osculating Orbit

**Integration point:** `idealized_orbits.py`, new function `plot_hyperbolic_osculating_orbit()`

**When plotted:** When center is a major body and a plotted object has geocentric eccentricity > 1 (hyperbolic flyby).

**How it works:**
1. Use the CAD perigee time as the epoch
2. Fetch geocentric osculating elements from Horizons at that epoch (`center_body='@399'` for Earth)
3. Plot hyperbolic arc using: `r = |a|(e^2 - 1) / (1 + e * cos(theta))`
4. Theta ranges from `-arccos(-1/e)` to `+arccos(-1/e)` (asymptotic limits)
5. Standard rotation sequence (omega, i, Omega) -- same as existing osculating ellipses
6. Dashed line style, matching existing osculating orbit visual language
7. Plotly clips at renderer level -- no manual clipping needed

**Legend entry:** "Apophis Osculating Orbit (Epoch: 2029-04-13 osc.)" -- parallels Moon's "Moon Osculating Orbit (Epoch: 2029-04-01 osc.)"

**Physical meaning:** "If only Earth's gravity existed, and Apophis had exactly this position and velocity at perigee, it would follow this hyperbolic path." Near perigee, the hyperbola overlaps the actual trajectory closely. Farther out, solar perturbation causes divergence -- this divergence is physically informative.

---

## Current Apophis Implementation

Apophis is already in `celestial_objects.py`:
```python
{'name': 'Apophis', 'id': '2004 MN4', 'var_name': 'apophis_var',
 'color_key': 'Apophis', 'symbol': 'circle-open', 'object_type': 'orbital',
 'id_type': 'smallbody',
 'center_id': '2099942',  # Numeric ID for use as Horizons center
 'mission_info': 'Horizons: 2004 MN4. A near-Earth asteroid...'}
```

With Earth as center:
- Actual trajectory plots correctly (51 points, April 1-29, 2029)
- Closest plotted point: 0.000254 AU on 2029-04-13 21:41 (5 min from true perigee)
- Moon's osculating orbit and apsidal markers plot correctly
- **No geocentric osculating orbit for Apophis** (correctly -- it's a hyperbola, not handled yet)
- **No perigee marker for Apophis** (this is what we're building)

With Sun as center:
- Both Earth and Apophis heliocentric orbits plot correctly
- Osculating ellipses, Keplerian perihelion/aphelion all work
- Shows the two orbits crossing in 3D space

---

## Implementation Order

1. **close_approach_data.py** -- New module (Capability A)
2. **Perigee marker integration** in palomas_orrery.py (Capability B)
3. **Hyperbolic osculating orbit** in idealized_orbits.py (Capability C)
4. **Test with Apophis**, then verify generality with other NEOs

Each capability is independently testable.

---

## Flagged for Future (Not This Round)

### Auto-scaling for non-child objects

**Issue:** When center=Earth with Moon+Apophis checked, auto-scaling only considers the Moon (Earth's "child" satellite). The plot cube is set to +/-0.004 AU based on the Moon's orbit. But Apophis on April 1 is at 0.044 AU from Earth -- 10x outside the cube. The trajectory line extends far beyond the visible area; you only see the portion near closest approach.

**Desired behavior:** Auto-scaling should also consider checked non-child objects within the plotted date range. Find max distance of any plotted object from center, use that (with buffer) as axis range. User can still override with manual scale to zoom in.

**Why separate:** This is a general scaling improvement that affects all center-object combinations, not specific to close approaches.

### Adaptive time resolution near periapsis

**Issue:** With 51 evenly-spaced-in-time points over 28 days, each step is ~13.2 hours. Near perigee, Apophis moves at 7.4 km/s -- covering ~352,000 km per time step (nearly the Earth-Moon distance!). The trajectory makes a sharp V at perigee but the vertex is poorly resolved. The CAD marker may fall off the trajectory line.

**Applies to:** All periapsis passages -- comet perihelion (C/2023 A3, 3I/ATLAS), asteroid flybys, spacecraft encounters. Anywhere velocity peaks at closest approach.

**Possible approaches:**
- **Simple:** Insert extra trajectory points clustered near known close approaches (if CAD data exists, add ~10 points in the hour around perigee)
- **Medium:** Denser time stepping where velocity exceeds a threshold
- **Ambitious:** Fully adaptive time stepping based on angular velocity

**Why separate:** This is a trajectory plotting enhancement that benefits many scenarios beyond close approaches.

---

### Geostationary Orbit Shell for Earth

**Idea:** Add a shell to `earth_visualization_shells.py` showing the geostationary orbit altitude (42,164 km from center / 35,786 km altitude). This is where communications and weather satellites orbit.

**Why it matters:** Apophis passes at 38,013 km -- *inside* the geostationary ring. Having that shell visible gives instant visual context without any explanation needed. The viewer sees the asteroid trajectory cutting inside the satellite belt and immediately grasps the scale.

**Implementation:** Should be straightforward -- add alongside the existing natural shells (Van Allen belts, magnetosphere, etc.) as an artificial/infrastructure shell. Possibly a different visual style (thinner, different color) to distinguish human-made infrastructure from natural phenomena.

---

## Other Open Items (Tony's Irons in the Fire)

### Gallery for KMZ Files
Status: In progress. Separate from this Apophis work.

### Linux Caching Hanging
Status: Tony's scientist friend has thoughts on this. Likely a separate debugging session needed. The issue may be related to file I/O blocking or network timeout behavior on Linux vs Windows.

### Apophis-Related Context

Three spacecraft converging on Apophis:
- **RAMSES** (ESA): Launching spring 2028, arrives February 2029 -- two months before flyby
- **OSIRIS-APEX** (NASA): Repurposed from Bennu sample return, already en route. But one of the 41 projects slated for cancellation in Trump's 2026 NASA budget request
- **DESTINY+** (JAXA): Also targeting Apophis

The close approach on April 13, 2029 will be visible to the naked eye from Europe, Africa, and western Asia -- about 2 billion potential observers.

---

## Key Technical Details for Implementation

### Geocentric Osculating Elements -- What They Look Like

From Tony's uploaded ephemeris (Horizons geocentric elements for Apophis, April 2029):

The geocentric orbit is HYPERBOLIC throughout the month:
- Eccentricity ranges from ~1.86 to ~19.1 (all > 1)
- Semi-major axis is NEGATIVE (as expected for hyperbolas): ~-11,000 km
- Apoapsis distance is infinity (9.999E+99)
- Inclination swings wildly (37 deg to 163 deg) -- the orbital plane rotates as solar perturbation changes
- Elements converge near perigee: Tp converges to JD 2462240.407

At perigee epoch (Apr 13-14):
- e ~ 4.254
- QR ~ 38,011 km (center-to-center)
- i ~ 162.9 deg
- a ~ -11,682 km

The osculating cache manager currently fetches heliocentric elements (@sun). For geocentric hyperbolas, we need to fetch with `center_body='@399'`. The `orbit_data_manager.query_horizons_elements()` already supports this parameter.

### Unit Detection

The existing unit detection in `orbit_data_manager.py` uses `q > 10000` to detect km units. Geocentric elements for close approaches WILL be in km (q ~ 38,000 km for Apophis). The existing conversion logic (`KM_TO_AU = 1.0 / 149597870.7`) should handle this correctly, but verify during implementation.

### Hyperbolic Orbit Math

For e > 1 (hyperbola):
```
r = |a| * (e^2 - 1) / (1 + e * cos(theta))
theta ranges: (-arccos(-1/e), +arccos(-1/e))
```

The asymptotic half-angle is `arccos(-1/e)`. For Apophis at perigee (e ~ 4.254):
```
asymptotic_angle = arccos(-1/4.254) = arccos(-0.2351) ~ 103.6 deg
```

So theta ranges from about -103.6 to +103.6 degrees. Generate 360 points across this range for smooth rendering.

The rotation sequence is identical to elliptical osculating orbits:
1. omega (argument of periapsis) around z-axis
2. i (inclination) around x-axis  
3. Omega (longitude of ascending node) around z-axis

---

## Quotables from This Session

- "April 13, 2029. Friday the 13th. Just over three years from now."
- "Passes BELOW geostationary orbit altitude (38,013 vs 42,164 km)"
- "The 3-sigma uncertainty is +/- 2.0 km -- they know this orbit to astonishing precision"
- "The gap between marker and trajectory is informative"
- "What's the geocentric equivalent of those dashed Keplerian ellipses? A dashed Keplerian hyperbola."

---

## Files Referenced

- `/mnt/project/celestial_objects.py` -- Apophis definition with center_id
- `/mnt/project/palomas_orrery.py` -- Main orrery, apsidal markers section
- `/mnt/project/idealized_orbits.py` -- Osculating orbit plotting
- `/mnt/project/orbit_data_manager.py` -- Horizons query, unit detection
- `/mnt/project/osculating_cache_manager.py` -- Element caching with center_body support
- `/mnt/project/apsidal_markers.py` -- Apsidal terminology and marker creation
- `/mnt/project/constants_new.py` -- Apophis description text
- Uploaded: `horizons_apophis_geocentric.txt` -- Geocentric osculating elements April 2029
- Uploaded: `apophis.png` -- Earth-centered view screenshot
- Uploaded: `apophis_heliocentric.png` -- Sun-centered view screenshot
