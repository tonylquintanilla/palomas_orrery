# Comet Perihelion Osculating Orbit -- Handoff Document

**Project:** Paloma's Orrery  
**Prepared:** March 4, 2026  
**Updated:** March 16, 2026  
**Status:** Capability D complete. Go: Perihelion button complete. Solution-level TP implemented and verified. Non-gravitational acceleration delta visible in hover text. Position marker timestamp added. Apsidal marker TP sources corrected.  
**Depends on:** Capability C (hyperbolic osculating orbit) -- complete and verified March 4, 2026.

---

## What This Is

Capability D: the Sun-centered counterpart to Capability C.

Capability C shows the osculating hyperbola for an asteroid flyby at a planet -- epoch = CAD perigee time, center = planet. Capability D shows the osculating conic for a comet at perihelion -- epoch = Tp from osculating elements, center = Sun.

The result: a white dotted arc showing the instantaneous Keplerian conic the comet would follow if the Sun were the only gravitational influence. For hyperbolic comets (e > 1), this is a hyperbola. For elliptical comets (e <= 1), this is an elliptical arc clipped to the plot bounds. The shape at Tp is the most physically meaningful view -- it's where the comet is most strongly influenced, moving fastest, and most clearly showing whether it is bound or unbound.

**Practical motivation (clarified March 10):** The ephemeris trace typically lacks resolution near perihelion. Comets race through perihelion and the standard trajectory points are often days apart through the most dynamic region. The osculating arc provides high-resolution perihelion detail -- 300-500 points with sinh spacing densest at periapsis -- filling the visual gap the ephemeris trace leaves.

---

## Solution-Level TP (March 16, 2026)

### The Two Kinds of TP

There are **two different kinds of TP** in the Horizons system:

1. **Solution-level TP:** A fixed parameter of the orbit determination solution (e.g., JPL#54 for 3I/ATLAS). This is the "real" perihelion time -- when the comet, pushed by its own outgassing jets, actually reaches closest approach. It appears in the Horizons raw response header: `TP= 2460977.9952628477`. It does not change with query epoch -- only with new orbit solutions.

2. **Osculating TP:** The perihelion of the instantaneous Keplerian orbit (gravity-only) at a given epoch. This varies with query epoch because perturbations and non-gravitational forces shift the osculating conic. The `astroquery` `elements()` table returns this value. When queried AT the solution Tp epoch, the osculating TP gives the pure-gravity perihelion prediction.

**The difference between these two is the non-gravitational acceleration signal.** For 3I/ATLAS (CO2 outgassing, JPL solution #54): solution TP = 11:53:11, osculating TP at perihelion = 11:34:27, delta = **18.7 minutes**. Outgassing jets shifted the actual perihelion 18.7 minutes later than pure gravity predicts.

### TP Resolution Hierarchy (`resolve_tp()`)

All TP consumers now use a single function with four-path fallback:

1. **Path 1: `solution_TP` from cache** -- authoritative, instant. Cached after first fetch.
2. **Path 2: Live `fetch_solution_tp()`** -- one Horizons call via `vectors_async().text`, parses `TP=` from header. Caches result for Path 1. Returns None for planets/satellites (no solution TP in header).
3. **Path 3: `TP` from osculating cache** -- standard for planets/satellites. Fallback for comets when Horizons unreachable.
4. **Path 4: `TP` from analytical elements** -- hardcoded last resort.

Path 2 at position 2 (before osculating cache) eliminates the bootstrap problem: on first press of Go: Perihelion, `resolve_tp()` misses Path 1 (nothing cached yet), fires Path 2 (live fetch), caches the result, and all subsequent calls hit Path 1. No manual seeding required.

### Three Functions in `osculating_cache_manager.py`

- **`fetch_solution_tp(obj_name, horizons_id, id_type)`** -- Uses `vectors_async().text` (not `elements()` which can fail with "required masses not defined"). Parses `TP= 24xxxxx.xxx` from the JD-format line in the header. Any epoch works.
- **`cache_solution_tp(obj_name, tp_jd, center_body)`** -- Stores `solution_TP` field alongside existing `TP` in the cache entry. Does not overwrite osculating TP.
- **`resolve_tp(obj_name, obj_info, center_body)`** -- Four-path hierarchy. Returns `(tp_jd, tp_source)` tuple.

### Osculating Elements ARE Available at Perihelion

Despite the web interface sometimes showing "Required masses not defined, osculating elements not available" (which depends on the coordinate center), `astroquery` with `center='@sun'` successfully returns osculating elements for 3I/ATLAS at perihelion epoch. The web interface error was caused by a non-Sun center (Arrokoth default). Sun-centered queries work at all epochs.

---

## What Was Built

### 1. `plot_perihelion_osculating_orbit()` in `idealized_orbits.py`

New function appended at end of file (after `plot_hyperbolic_osculating_orbit`).

**Tp resolution:** Uses `resolve_tp()` (replaced the original three-path fallback in March 16 session).

**Element fetch at Tp:**

Bypasses the osculating cache (cache keys on obj_name + center_body with no date component). Calls `fetch_osculating_elements()` directly with `center_body='@10'` (Sun) and `date=tp_datetime`.

**Conic branches:**

- **Hyperbolic (e > 1):** Asymptote angle, binary search for clip theta, sinh-spaced 300 points per arm. Identical math to Capability C.
- **Elliptical (e <= 1):** Conic equation with semi-latus rectum. Binary search for clip theta where r exceeds plot bounds. Full ellipse if aphelion fits within clip distance. 500 points, sinh-spaced for e > 0.95, uniform otherwise.

**Perihelion velocity:** Vis-viva equation computed before the branch point, displayed in both branches' hover text.

**Non-gravitational delta (March 16):** Compares `tp_jd` (solution TP from `resolve_tp()`) with `elements.get('TP')` (osculating TP from the fetch AT the solution Tp epoch). The delta is displayed in hover text when > 0.1 minutes. Uses the osculating TP from the perihelion-epoch fetch specifically -- not from the cache, which may be from a distant epoch.

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

**Integration points:** Two guard blocks in `palomas_orrery.py` (after ~line 5158 and ~line 6326) check: center == Sun AND show_apsidal_markers AND object is comet -> call `plot_perihelion_osculating_orbit()`.

### 4. Go: Perihelion Button (March 15, 2026)

**New in `spacecraft_encounters.py`:** `get_comet_perihelion_preset(obj_name, obj_info=None)`

Builds a perihelion close-up preset for any comet. Uses `resolve_tp()` for authoritative TP, then computes:
- `q` (perihelion distance) from `a` and `e`
- Perihelion velocity via vis-viva: `v = sqrt(GM * (2/q - 1/a))`
- Time window: `crossing_time = 2*q / v`, then `window = crossing_time * 20`, floor 7 days, cap 365 days
- Plot scale: `q * 4`

Returns a preset dict with center, dates, scale, label, q, v, tp_jd, and tp_source.

**New in `palomas_orrery.py`:** `_apply_comet_perihelion_preset(comet_name)`

Applies the preset with additive behavior (same pattern as spacecraft encounter presets):
1. Ensures comet checkbox is checked (preserves other selections)
2. Ensures Sun is checked
3. Sets center to Sun
4. Turns on apsidal markers (`show_apsidal_markers_var.set(1)`)
5. Sets date range centered on Tp
6. Sets manual scale to `q * 4`
7. Sets `_encounter_plot_date` to Tp (solution TP) for position marker placement
8. Triggers `plot_objects()`

**Modified:** `create_comet_checkbutton()` and `create_interstellar_checkbutton()` in `palomas_orrery.py` -- each now adds a "Go: Perihelion" button under the comet checkbox (indented 25px, same visual pattern as spacecraft encounter Go buttons). Uses closure-capture pattern for loop variable safety.

### 5. Apsidal Marker TP Corrections (March 16, 2026)

**Keplerian Periapsis marker:** Now fetches osculating elements at the solution Tp epoch (not the pre-fetch epoch) to get the gravity-only perihelion time. For 3I/ATLAS: 11:34:27 UTC (previously 11:30:55 from pre-fetch at April 29).

**Actual Perihelion marker:** Now uses `resolve_tp()` for the solution-level TP. For 3I/ATLAS: 11:53:11 UTC (previously 11:30:55 from osculating cache, or midnight from date-only truncation).

**Midnight truncation fix:** The Actual Perihelion marker position fetch now uses full datetime (from `perihelion_full`) instead of date-only. At 68 km/s, 10 hours = 2.4 million km offset.

**Non-grav delta in Actual Perihelion hover:** Shows the shift between solution TP and osculating TP at perihelion epoch.

### 6. Position Marker Timestamp (March 16, 2026)

**`format_detailed_hover_text()` in `visualization_utils.py`:** Added `position_date` field. Shows "Position at: YYYY-MM-DD HH:MM:SS UTC" in hover text. Previously the position marker was the only one without a timestamp.

**`palomas_orrery.py`:** `obj_data['position_date'] = date_obj` injected after both `fetch_position()` call sites.

---

## Trigger Hierarchy (Capability C vs D vs Go Button)

```
center == Sun
  AND show_apsidal_markers == True
    -> for each selected comet:
         _is_comet() == True
           -> resolve_tp() for solution TP
             -> fetch elements AT Tp, center=Sun
               -> hyperbolic arc (e > 1) OR elliptical arc (e <= 1)

center != Sun
  AND show_apsidal_markers == True
    -> for each selected object:
         id_type == 'smallbody'
           -> CAD API query for close approaches in plot window
             -> if approach found:
               -> fetch elements at perigee JD, center=planet
                 -> hyperbolic arc (e > 1 only)

Go: Perihelion button pressed:
  -> get_comet_perihelion_preset() uses resolve_tp() for Tp, q, v
  -> _apply_comet_perihelion_preset() sets center=Sun, dates, scale, apsidal on
  -> _encounter_plot_date set to solution Tp
  -> plot_objects() fires -> Capability D triggers automatically
```

The two capabilities (C and D) are mutually exclusive by center body. The Go button is a convenience that sets up the view for Capability D.

---

## Files Changed

| File | Change | Session |
|------|--------|---------|
| `idealized_orbits.py` | Add `'Sun': '10'` to `CENTER_TO_HORIZONS_ID` | March 10 |
| `idealized_orbits.py` | Add `plot_perihelion_osculating_orbit()` function | March 10 |
| `idealized_orbits.py` | Replace Tp resolution with `resolve_tp()` in `plot_perihelion_osculating_orbit` | March 16 |
| `idealized_orbits.py` | Add non-grav delta to perihelion osculating orbit hover text | March 16 |
| `idealized_orbits.py` | Fix Keplerian Periapsis marker: fetch osculating TP at solution Tp epoch | March 16 |
| `idealized_orbits.py` | Fix Actual Perihelion marker: use `resolve_tp()` for solution TP | March 16 |
| `idealized_orbits.py` | Fix Actual Perihelion marker: full datetime instead of midnight truncation | March 16 |
| `palomas_orrery.py` | Add `plot_perihelion_osculating_orbit` to import | March 10 |
| `palomas_orrery.py` | Add `_is_comet()` helper and `_add_perihelion_osculating_orbit()` caller | March 10 |
| `palomas_orrery.py` | Add Sun-centered guard blocks at two integration points | March 10 |
| `palomas_orrery.py` | Add `_apply_comet_perihelion_preset()` function | March 15 |
| `palomas_orrery.py` | Modify `create_comet_checkbutton()` -- add Go: Perihelion button | March 15 |
| `palomas_orrery.py` | Modify `create_interstellar_checkbutton()` -- add Go: Perihelion button | March 15 |
| `palomas_orrery.py` | Inject `position_date` into `obj_data` at both fetch sites | March 16 |
| `palomas_orrery.py` | Set `_encounter_plot_date` from preset `tp_jd` in comet preset | March 16 |
| `spacecraft_encounters.py` | Add `get_comet_perihelion_preset()` using `resolve_tp()` | March 15/16 |
| `osculating_cache_manager.py` | Add `fetch_solution_tp()`, `cache_solution_tp()`, `resolve_tp()` | March 16 |
| `visualization_utils.py` | Add `position_date` to `format_detailed_hover_text()` | March 16 |

---

## Test Results (March 16, 2026) -- Solution TP + Non-Gravitational Delta

### 3I/ATLAS -- PASSED

Console output confirms the full pipeline:
```
[RESOLVE TP] 3I/ATLAS: Path 1 (solution TP cached) = JD 2460977.9952628477
[COMET PRESET] Position marker date set to 2025-10-29 11:53:10
  Keplerian periapsis TP (at Tp epoch): 11:34:26 UTC
  [HYPERBOLIC] Perihelion: 2025-10-29 11:53:10 UTC (source: solution TP (cached))
  [PeriOsc] Non-grav delta: 18.7 min (later)
    Solution TP:  JD 2460977.9952628477
    Osculating TP (at Tp): JD 2460977.9822540479
```

**Marker positions verified (left to right in plot):**

| Marker | Time (UTC) | Source | Physics |
|--------|-----------|--------|---------|
| Full Mission Closest Point | 05:16:48 | Nearest daily sample | Trajectory resolution limit |
| Keplerian Periapsis | 11:34:26 | Osculating TP at Tp epoch | Gravity-only prediction |
| Actual Perihelion | 11:53:11 | Solution TP via `resolve_tp()` | Full physics (incl. outgassing) |
| 3I/ATLAS Position | 11:53:10 | `_encounter_plot_date` from preset | Solution TP |
| Plotted Period Closest Point | 23:56:38 | Nearest daily sample | Trajectory resolution limit |

**Non-gravitational delta:** 18.7 minutes (solution perihelion later than Keplerian). This is the integrated effect of CO2 outgassing: `g(r) = (1 au/r)^2`, JPL solution #54.

**Position marker hover text:** "Position at: 2025-10-29 11:53:10 UTC" -- confirmed visible.

**Bootstrap behavior:** First press: Path 2 (live fetch) fires, caches `solution_TP`. Second press and all subsequent: Path 1 (cached) fires instantly. No manual seeding required.

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
| `_encounter_plot_date` one-shot override for position marker | Verified (reused from spacecraft) |
| Additive preset pattern (ensure checked, don't uncheck) | Verified (reused from spacecraft) |
| Closure-capture for loop variable in button callbacks | Verified (reused from spacecraft) |

---

## For Paloma

*"When a comet swings around the Sun, there's a single moment when it's closest -- perihelion. At that exact moment, if we freeze time and ask 'what path would this comet follow if only the Sun were pulling on it?', the answer is a precise curve called the osculating conic. For comets visiting from outside the solar system -- like 3I/ATLAS -- that curve is a hyperbola: the comet swings around the Sun and leaves forever, never to return. For comets that come back -- like Halley -- that curve is a very stretched-out ellipse. The dotted white line shows that path. The colored line shows what the comet actually does, with Jupiter and Saturn also tugging on it. The difference between the dotted line and the colored line is the fingerprint of all the other planets combined.*

*But there's something even more interesting. Comets aren't just rocks -- they're active. When 3I/ATLAS gets close to the Sun, frozen CO2 on its surface heats up and shoots out as jets. Those tiny jets actually push the comet, like a very weak rocket engine. JPL's scientists can measure this push by comparing two different predictions: one that only uses gravity (the 'Keplerian' prediction) and one that includes the jet forces (the 'solution'). For 3I/ATLAS, the jets shifted perihelion by 18.7 minutes -- the comet arrived 18.7 minutes later than pure gravity predicted. That's the fingerprint of outgassing, and the hover text shows it.*

*The hover text also tells you how fast the comet is moving at perihelion. MAPS -- a sungrazer that almost touches the Sun -- reaches 557 km/s. That's nearly 2 million kilometers per hour. Halley, which stays farther out, peaks at 54 km/s. Earth, for comparison, moves at 30 km/s. The closer you get, the faster you go -- that's Kepler's law, and one equation (vis-viva) tells you the whole story.*

*Now there's a 'Go: Perihelion' button under every comet. Press it and the orrery sets everything up to show you perihelion -- the right date, the right scale, the right center. You don't have to figure out the settings. The math figures out the settings for you."*

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
*"The math figures out the settings for you."* -- On the Go: Perihelion button  
*"There are two different kinds of TP."* -- The osculating vs solution-level insight, March 15, 2026  
*"The solution-level TP is the one true perihelion time."* -- On why raw response parsing is the right fix  
*"Required masses not defined, osculating elements not available."* -- Horizons, reminding us that vectors always work  
*"The physical signal is the same size as the computational noise."* -- On why `fetch_solution_tp()` isn't just cosmetic  
*"One authoritative TP unlocks everything else."* -- On how the fix enables the non-gravitational story  
*"The delta between Keplerian and actual perihelion is the fingerprint of outgassing."* -- The non-gravitational acceleration insight  
*"18.7 minutes of personality."* -- On the non-gravitational shift for 3I/ATLAS, March 16, 2026  
*"The osculating TP at perihelion is the purest Keplerian comparison point."* -- On why the epoch of the fetch matters  
*"Outgassing jets shifted the actual perihelion 18.7 minutes later than pure gravity predicts."* -- The physics story  

---

## Key Lessons

### March 15 Session

- **Osculating TP varies with query epoch.** The TP returned by `astroquery` `elements()` is the perihelion of the instantaneous Keplerian orbit at the query epoch, not the orbit solution's perihelion. Different query epochs -> different TPs.
- **Solution-level TP is fixed per solution.** It appears in the Horizons raw response header (`TP= <JD>`) and does not change with query epoch. Only changes when JPL publishes a new orbit solution.
- **Pre-fetch can overwrite cached TP.** The orrery's pre-fetch mechanism queries at the GUI start date, which for wide time windows can be years from perihelion. This overwrites the cache with osculating elements at a distant epoch, shifting the cached TP.
- **The Go button pattern extends cleanly to comets.** Same additive preset, same `_encounter_plot_date` override, same closure-capture for buttons. The vis-viva equation provides adaptive window sizing from orbital elements alone.

### March 16 Session

- **Live fetch at hierarchy position 2 eliminates bootstrap.** Placing `fetch_solution_tp()` before the osculating cache in the hierarchy means `resolve_tp()` fires the live fetch on first call, caches the result, and all subsequent calls hit the cached Path 1. No manual seeding, no cache deletion required.
- **The non-gravitational delta must compare the right TPs.** Using the osculating TP from the cache (pre-fetched at a distant epoch) mixes epoch drift with the physical signal. The correct comparison is solution TP vs osculating TP fetched AT the solution Tp epoch. For 3I/ATLAS: 18.7 min (correct) vs 22.2 min (with epoch drift noise).
- **The Keplerian Periapsis marker needs its own fetch at perihelion epoch.** The pre-fetch populates the cache at the window start date, giving a stale osculating TP. The marker should show the gravity-only perihelion time from elements fetched at the actual perihelion epoch. This costs one extra Horizons call but gives the physically meaningful value.
- **"Actual Perihelion" = solution TP, "Keplerian Periapsis" = osculating TP at perihelion.** The two markers now have clearly distinct physics: one includes non-gravitational forces, the other is gravity-only. The difference between them is the outgassing fingerprint.
- **Position marker timestamp makes all markers comparable.** Every marker now shows its datetime, enabling synchronicity comparison across the plot.
- **Horizons web interface center default can mislead.** The "required masses not defined" error for 3I/ATLAS was caused by a non-Sun coordinate center (Arrokoth default in the web app). Sun-centered queries work at all epochs via the API.

---

## On the Horizon

- **Test Halley and MAPS with solution TP.** Verify non-grav delta for periodic comets (expected: smaller for Halley, near-zero for well-behaved orbits).
- **Adaptive encounter resolution for perihelion.** The plotted period closest point (23:56:38) is limited by daily time steps. The `_calculate_encounter_resolution` pattern from spacecraft encounters could provide finer sampling near perihelion.
- **Window cap refinement.** Current 365-day cap may still be too generous for some objects. Consider velocity-dependent capping.

---

## Session History

| Date | Event |
|------|-------|
| March 4, 2026 | Design complete. Handoff document created. Implementation not started. |
| March 10, 2026 | Design refined: both conic types (hyperbolic + elliptical) in one function; eccentricity guard removed from trigger; comet detection by ID pattern; separate function from Capability C. Code written (two patch files). |
| March 10, 2026 | Integrated, tested, verified. Three comets tested: 3I/ATLAS (hyperbolic), MAPS (near-parabolic elliptical), Halley 1986 (moderate elliptical). All passed. Vis-viva perihelion velocity added to hover text. Wierzchos reclassified as barely hyperbolic (e=1.0001). Halley Tp resolution confirmed: cache Path A correctly returns 1986 Tp when plot is set to 1986 window. |
| March 15, 2026 | Go: Perihelion button implemented. `get_comet_perihelion_preset()` added to `spacecraft_encounters.py`. `_apply_comet_perihelion_preset()` and button wiring added to `palomas_orrery.py`. Tested on Halley (passed), MAPS (passed), 3I/ATLAS (passed with known TP offset). |
| March 15, 2026 | TP precision issue discovered and diagnosed. Osculating TP varies with query epoch; solution-level TP (from Horizons raw response header) is the authoritative source. `fetch_solution_tp()` planned for next session. Tony confirmed raw response parsing works: `TP= 2460977.9952628477` from vectors query header. |
| March 16, 2026 | Solution-level TP implemented: `fetch_solution_tp()`, `cache_solution_tp()`, `resolve_tp()` added to `osculating_cache_manager.py`. Four-path hierarchy with live fetch at position 2 eliminates bootstrap. |
| March 16, 2026 | All four items wired: position marker timestamp, non-grav delta in hover, Actual Perihelion uses solution TP, Keplerian Periapsis fetches at perihelion epoch. |
| March 16, 2026 | Verified on 3I/ATLAS: non-grav delta = 18.7 min (CO2 outgassing), all five markers at correct times, position hover shows timestamp. |

---

**Prepared by:** Tony (with Claude)  
**Sessions:** March 4 (design), March 10 (implementation + testing), March 15 (Go button + TP precision diagnosis), March 16 (solution TP + non-grav delta + apsidal marker corrections)  
**Prerequisite reading:** `apophis_handoff.md` (Capabilities A-C), `spacecraft_mission_explorer_handoff.md` (Go button pattern)
