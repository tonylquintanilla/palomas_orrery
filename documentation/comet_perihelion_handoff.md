# Comet Perihelion Osculating Orbit -- Handoff Document

**Project:** Paloma's Orrery  
**Prepared:** March 4, 2026  
**Updated:** March 10, 2026  
**Status:** Implemented, integrated, and visually verified.  
**Depends on:** Capability C (hyperbolic osculating orbit) -- complete and verified March 4, 2026.

---

## What This Is

Capability D: the Sun-centered counterpart to Capability C.

Capability C shows the osculating hyperbola for an asteroid flyby at a planet -- epoch = CAD perigee time, center = planet. Capability D shows the osculating conic for a comet at perihelion -- epoch = Tp from osculating elements, center = Sun.

The result: a white dotted arc showing the instantaneous Keplerian conic the comet would follow if the Sun were the only gravitational influence. For hyperbolic comets (e > 1), this is a hyperbola. For elliptical comets (e <= 1), this is an elliptical arc clipped to the plot bounds. The shape at Tp is the most physically meaningful view -- it's where the comet is most strongly influenced, moving fastest, and most clearly showing whether it is bound or unbound.

**Practical motivation (clarified March 10):** The ephemeris trace typically lacks resolution near perihelion. Comets race through perihelion and the standard trajectory points are often days apart through the most dynamic region. The osculating arc provides high-resolution perihelion detail -- 300-500 points with sinh spacing densest at periapsis -- filling the visual gap the ephemeris trace leaves.

---

## Design Decisions (March 10 Session)

### Separate function, not an extension of Capability C

`plot_hyperbolic_osculating_orbit` (Capability C) is planet-centered and fetches elements relative to Earth/Mars/etc. The new `plot_perihelion_osculating_orbit` (Capability D) is Sun-centered with a different epoch source (Tp instead of CAD JD) and handles both hyperbolic AND elliptical comets. Keeping them separate avoids tangling the two capabilities.

### Both conic types in one function

The function branches on eccentricity after fetching elements:
- **e > 1 (hyperbolic):** Reuses the sinh-spaced, asymptote-bounded arc pattern from Capability C.
- **e <= 1 (elliptical):** Uses the standard conic equation r = a(1-e^2)/(1+e*cos(theta)), clipped to plot cube bounds. For near-parabolic comets (e > 0.95), sinh spacing is used for density near perihelion; otherwise uniform spacing.

### No eccentricity threshold for the trigger

Every comet benefits from seeing the osculating arc at perihelion, regardless of eccentricity. The trigger is: object is identified as a comet AND has a TP available. Eccentricity only matters inside the function for choosing the conic type. This was a deliberate design choice -- the original handoff proposed e > 0.8, but conversation revealed this was too conservative (long-period comets like Hale-Bopp at e ~ 0.995 and Hyakutake at e ~ 0.9998 would pass, but the threshold itself was the wrong discriminator).

### Spatial clipping, not date-range clipping

The arc is clipped where r exceeds axis_range * 1.5 (same as Capability C). This is simpler than converting theta to time via Kepler's equation, and matches the user's visual expectation -- "show me what fits in my plot." For a comet like Halley (aphelion ~35 AU), only the perihelion region appears in an inner solar system plot.

### Apsidal markers toggle controls the feature

The perihelion osculating arc only appears when "Show Apsidal Markers" is on. This coupling makes sense because the perihelion marker is part of the apsidal marker system, and the osculating arc is a detail overlay on that marker.

### Perihelion velocity via vis-viva equation

Added after initial testing. The vis-viva equation `v^2 = GM * (2/r - 1/a)` evaluated at r = q gives the perihelion velocity from elements we already have. Works identically for hyperbolic (a negative, so -1/a becomes +1/|a|) and elliptical orbits. Displayed in hover text as km/s and AU/day. Provides vivid cross-comet comparison:
- MAPS (sungrazer, q = 0.005 AU): 557 km/s
- 3I/ATLAS (interstellar, q = 1.36 AU): ~68 km/s
- Halley (periodic, q = 0.587 AU): 54.5 km/s
- Earth for reference: 30 km/s

---

## Why Tp Is Already Available

The osculating cache already stores `TP` (time of perihelion) as a Julian Date for every object it has fetched from Horizons. It is stored in `entry['elements']['TP']`.

From `osculating_cache_manager.py` line ~416:
```python
cache_entry = {
    'elements': {
        'a': result['a'],
        'e': result['e'],
        ...
        'TP': result.get('TP'),   # Julian Date of perihelion passage
    },
    ...
}
```

From `orbital_elements.py`, analytical elements for known comets already carry Tp:
```python
'3I/ATLAS': {
    'TP': 2460977.974321826361,   # Time of perihelion (JD)
    ...
}
```

Converting Julian Date to datetime -- identical pattern to Capability C's CAD approach JD:
```python
from astropy.time import Time
tp_datetime = Time(tp_jd, format='jd').datetime
```

**Important: Tp epoch vs data arc.** The analytical elements may store the *next* perihelion (e.g., Halley's TP = 2061), but if the osculating cache was populated from a plot in the 1986 window, the cache stores the 1986 Tp. Path A (cache) takes priority and correctly returns the Tp matching the user's plot context. This was confirmed in Halley testing -- the pre-fetch at the 1986 plot date populated the cache with the 1986 Tp (JD 2446470.959 = Feb 9, 1986), and Path A found it.

---

## What Was Built

### 1. `plot_perihelion_osculating_orbit()` in `idealized_orbits.py`

New function appended at end of file (after `plot_hyperbolic_osculating_orbit`).

**Tp resolution -- three-path fallback:**

- **Path A: Osculating cache.** `load_cache()` -> look up `obj_name` -> read `elements.TP`. No fetch required. Preferred because the cache Tp matches the user's current plot context.
- **Path B: Analytical elements.** `orbital_elements.planetary_params[obj_name]['TP']`. For known comets not yet cached. Caution: may store a different apparition's Tp than the user intends (e.g., Halley 2061 vs 1986).
- **Path C: Horizons fetch at plot start date.** Fetch returns elements including TP. Most expensive (two fetches: one to get Tp, one to get elements AT Tp). Guarantees correct Tp for any object and any epoch.

**Element fetch at Tp:**

Bypasses the osculating cache (cache keys on obj_name + center_body with no date component). Calls `fetch_osculating_elements()` directly with `center_body='@10'` (Sun) and `date=tp_datetime`.

**Conic branches:**

- **Hyperbolic (e > 1):** Asymptote angle, binary search for clip theta, sinh-spaced 300 points per arm. Identical math to Capability C.
- **Elliptical (e <= 1):** Conic equation with semi-latus rectum. Binary search for clip theta where r exceeds plot bounds. Full ellipse if aphelion fits within clip distance. 500 points, sinh-spaced for e > 0.95, uniform otherwise.

**Perihelion velocity:** Vis-viva equation computed before the branch point, displayed in both branches' hover text.

**Shared:** Keplerian rotation (omega, i, Omega), white dotted line style, hover text with AU convention (q in both AU and km), perihelion velocity (km/s and AU/day), legend label with epoch.

### 2. `'Sun': '10'` added to `CENTER_TO_HORIZONS_ID` in `plot_hyperbolic_osculating_orbit`

One-line addition to the existing dict. Also enables future comet-planet flyby capability (Capability C already handles the geometry; it just needs the center ID).

### 3. `_is_comet()` and `_add_perihelion_osculating_orbit()` in `palomas_orrery.py`

**Comet detection by ID pattern:**
```python
def _is_comet(obj_info):
    obj_id = obj_info.get('id', '')
    name = obj_info.get('name', '')
    if obj_id.startswith('C/'):        return True   # C/ designation
    if obj_id.startswith('A/'):        return True   # A/ (pre-reclassification interstellar)
    if len(name) >= 3 and name[0].isdigit() and name[1:3] == 'I/':
        return True                                   # 1I/, 2I/, 3I/
    if obj_id.isdigit() and len(obj_id) >= 8:
        try:
            if int(obj_id) >= 90000000: return True   # Periodic comet record numbers
        except ValueError: pass
    return False
```

No eccentricity guard -- if `_is_comet()` returns True and id_type is 'smallbody', the function fires.

**Caller function:** Iterates selected objects, filters to smallbody comets, calls `plot_perihelion_osculating_orbit` for each.

### 4. Two integration points in `palomas_orrery.py`

Both are guarded by `center_object_name == 'Sun' and show_apsidal_markers_var.get()`:
- After line ~5158 (first plot path, uses `selected_objects` and `date_obj`)
- After line ~6326 (second plot path, uses `selected_object_names` and `dates_list[0]`)

### 5. Import update

Line 62: added `plot_perihelion_osculating_orbit` to the import from `idealized_orbits`.

---

## Trigger Chain

```
center == 'Sun'
  AND show_apsidal_markers == True
    -> for each selected object:
         id_type == 'smallbody'
           AND _is_comet(obj_info) == True
             -> resolve Tp (cache -> analytical -> fetch)
               -> fetch elements at Tp, center='@10', bypass cache
                 -> compute perihelion velocity (vis-viva)
                   -> branch on e: hyperbolic or elliptical arc
                     -> white dotted trace added to figure
```

Compare to Capability C trigger chain:
```
center != 'Sun'
  AND show_apsidal_markers == True
    -> for each selected object:
         id_type == 'smallbody'
           -> CAD API query for close approaches in plot window
             -> if approach found:
               -> fetch elements at perigee JD, center=planet
                 -> hyperbolic arc (e > 1 only)
```

The two capabilities are mutually exclusive by center body. Both can coexist without interference.

---

## Files Changed

| File | Change |
|------|--------|
| `idealized_orbits.py` | Add `'Sun': '10'` to `CENTER_TO_HORIZONS_ID` in `plot_hyperbolic_osculating_orbit` (line ~6660) |
| `idealized_orbits.py` | Add `plot_perihelion_osculating_orbit()` function at end of file |
| `palomas_orrery.py` | Add `plot_perihelion_osculating_orbit` to import (line ~62) |
| `palomas_orrery.py` | Add `_is_comet()` helper and `_add_perihelion_osculating_orbit()` caller (after `_add_close_approach_extras`) |
| `palomas_orrery.py` | Add Sun-centered guard block at first integration point (after line ~5158) |
| `palomas_orrery.py` | Add Sun-centered guard block at second integration point (after line ~6326) |

No other files need to change. `osculating_cache_manager.py`, `close_approach_data.py`, and `orbital_elements.py` are used as-is.

---

## Test Results (March 10, 2026)

### 3I/ATLAS -- PASSED (hyperbolic, e ~ 6.14)

- Tp source: osculating cache (Path A, from pre-fetch)
- Tp: 2025-10-29 11:34 UTC (JD 2460977.983)
- Elements at Tp: e=6.139313, a=-0.264 AU, q=1.356448 AU
- Perihelion velocity: ~68 km/s
- Axis half-width: 16.28 AU, clip theta: 95.6 deg (asymptote 99.4 deg)
- Visual: dramatic hyperbola with open arms, white dotted arc

### MAPS (C/2026 A1) -- PASSED (elliptical near-parabolic, e ~ 0.99996)

- Tp source: osculating cache (Path A)
- Tp: 2026-04-04
- Elements at Tp: e=0.999962, a=150.33 AU, q=0.00571 AU (854,430 km)
- Perihelion velocity: 557 km/s (0.32 AU/day) -- Kreutz sungrazer
- Visual: tight perihelion hairpin turn, elliptical branch with sinh spacing
- Note: fresh Horizons solution (a=150 AU) differs from analytical (a=109 AU) -- updated orbit solution

### Halley (1986 apparition) -- PASSED (elliptical, e ~ 0.967)

- Tp source: osculating cache (Path A, from pre-fetch at 1986 plot date)
- Tp: 1986-02-09 11:01 UTC (JD 2446470.959) -- correctly resolved to 1986 perihelion, not 2061
- Elements at Tp: e=0.967279, a=17.94 AU, q=0.587103 AU
- Perihelion velocity: 54.5 km/s (0.0315 AU/day, 196,278 km/hr)
- Full ellipse visible (aphelion 35.30 AU < clip 63.53 AU)
- Visual: complete elongated ellipse with retrograde tilt (i=162 deg)
- Key insight: analytical elements store 2061 Tp, but Path A correctly finds 1986 Tp from cache

### Comet eccentricity survey

| Comet | e | Classification | Branch |
|-------|---|---------------|--------|
| 3I/ATLAS | 6.140 | Interstellar | Hyperbolic |
| 2I/Borisov | 3.356 | Interstellar | Hyperbolic |
| 1I/Oumuamua | 1.201 | Interstellar | Hyperbolic |
| Borisov (C/2025 V1) | 1.010 | Barely hyperbolic | Hyperbolic |
| Wierzchos (C/2024 E1) | 1.0001 | Barely hyperbolic | Hyperbolic |
| West | 1.00002 | Barely hyperbolic | Hyperbolic |
| McNaught | 1.00002 | Barely hyperbolic | Hyperbolic |
| ATLAS (C/2024 G3) | 1.00001 | Barely hyperbolic | Hyperbolic |
| Tsuchinshan | 1.00010 | Barely hyperbolic | Hyperbolic |
| PANSTARRS | 1.00033 | Barely hyperbolic | Hyperbolic |
| C/2025 K1 | 1.00025 | Barely hyperbolic | Hyperbolic |
| Hyakutake | 0.99989 | Near-parabolic | Elliptical (sinh) |
| Ikeya-Seki | 0.99992 | Near-parabolic | Elliptical (sinh) |
| MAPS | 0.99995 | Near-parabolic | Elliptical (sinh) |
| NEOWISE | 0.99918 | Near-parabolic | Elliptical (sinh) |
| SWAN | 0.99937 | Near-parabolic | Elliptical (sinh) |
| Hale-Bopp | 0.99498 | Near-parabolic | Elliptical (sinh) |
| Lemmon | 0.99566 | Near-parabolic | Elliptical (sinh) |
| Halley | 0.96783 | Elliptical | Elliptical (sinh) |

Note: Wierzchos (e=1.0001) is technically hyperbolic despite being often described as near-parabolic. The original handoff listed it as an elliptical test case -- corrected here.

---

## Verified Patterns From Capability C

These work and are reused without modification:

| Pattern | Status |
|---------|--------|
| `fetch_osculating_elements()` direct fetch (no cache) | Verified |
| `Time(jd, format='jd').datetime` for JD conversion | Verified |
| Sinh-spaced theta, cube-bounded arc | Verified |
| Standard Keplerian rotation (omega, i, Omega) | Verified |
| White dotted line, legend label with epoch | Verified |
| Binary search for clip angle | Verified |
| Vis-viva equation for perihelion velocity | Verified (new) |

---

## For Paloma

*"When a comet swings around the Sun, there's a single moment when it's closest -- perihelion. At that exact moment, if we freeze time and ask 'what path would this comet follow if only the Sun were pulling on it?', the answer is a precise curve called the osculating conic. For comets visiting from outside the solar system -- like 3I/ATLAS -- that curve is a hyperbola: the comet swings around the Sun and leaves forever, never to return. For comets that come back -- like Halley -- that curve is a very stretched-out ellipse. The dotted white line shows that path. The colored line shows what the comet actually does, with Jupiter and Saturn also tugging on it. The difference between the dotted line and the colored line is the fingerprint of all the other planets combined.*

*The hover text also tells you how fast the comet is moving at perihelion. MAPS -- a sungrazer that almost touches the Sun -- reaches 557 km/s. That's nearly 2 million kilometers per hour. Halley, which stays farther out, peaks at 54 km/s. Earth, for comparison, moves at 30 km/s. The closer you get, the faster you go -- that's Kepler's law, and one equation (vis-viva) tells you the whole story."*

---

## Quotables

*"The epoch source changes from CAD approach JD to osculating Tp JD. The pattern is identical."*  
*"Sun is center '10' in Horizons. One line unlocks all of heliocentric space."*  
*"For interstellar comets, the osculating hyperbola at Tp is the most dramatic curve in the solar system."*  
*"Capability C proved the pattern. Capability D is the same key in a different lock."*  
*"The eccentricity threshold is the wrong discriminator. The right test is: is it a comet, and does it have a Tp?"*  
*"The osculating arc is a high-resolution perihelion detail overlay, not just a theoretical 'what if' curve."*  
*"Every comet benefits from seeing the pure Keplerian path at closest approach."*  
*"557 km/s at perihelion vs 44 km/s today -- that's what grazing the Sun does."*  
*"The closer you get, the faster you go. One equation tells you the whole story."*  
*"Plot the 1986 perihelion, not the 2061 one -- the data arc is what matters."*

---

## Session History

| Date | Event |
|------|-------|
| March 4, 2026 | Design complete. Handoff document created. Implementation not started. |
| March 10, 2026 | Design refined: both conic types (hyperbolic + elliptical) in one function; eccentricity guard removed from trigger; comet detection by ID pattern; separate function from Capability C. Code written (two patch files). |
| March 10, 2026 | Integrated, tested, verified. Three comets tested: 3I/ATLAS (hyperbolic), MAPS (near-parabolic elliptical), Halley 1986 (moderate elliptical). All passed. Vis-viva perihelion velocity added to hover text. Wierzchos reclassified as barely hyperbolic (e=1.0001). Halley Tp resolution confirmed: cache Path A correctly returns 1986 Tp when plot is set to 1986 window. |

---

**Prepared by:** Tony (with Claude)  
**Sessions:** March 4, 2026 (design), March 10, 2026 (implementation + testing)  
**Prerequisite reading:** `apophis_handoff.md` (Capabilities A-C)
