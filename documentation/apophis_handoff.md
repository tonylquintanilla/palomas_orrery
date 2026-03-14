# Apophis Close Approach Infrastructure — Handoff Document

**Project:** Paloma's Orrery  
**Session:** March 4, 2026  
**Status:** Capabilities A, B, C complete and verified. Capability D (Sun-centered perihelion) planned.

---

## What Was Built

Three composable capabilities for visualizing small body close approaches to major bodies. Motivated by Apophis (99942) Earth flyby on April 13, 2029. Generalizes to any small body / major planet pair.

---

## Capability A: JPL CAD API Integration

**Module:** `close_approach_data.py`

Fetches precision flyby data from the JPL Small Body Close Approach Data (CAD) API.

**Cache:** `data/close_approach_cache.json` — intentionally separate from `orbit_paths.json`. The orbit path validator expects `data_points` or `x/y/z` arrays; CAD dicts have neither and would be flagged as corrupted. Separate file prevents collision.

**Key functions:**
- `get_approach_within_date_range(designation, body, start_date, end_date)` — returns list of approach dicts in the plot window
- `fetch_position_at_approach(approach, designation, center_body_id)` — Horizons position at perigee JD
- `add_cad_perigee_marker(fig, approach, position, body, obj_name, color_map)` — white square-open marker
- `format_approach_hover(approach, body, obj_name)` — full hover text with distance, velocity, uncertainty

**Body parameter:** CAD API accepts major planets only (Earth, Mars, Jupiter, etc.). Sun is NOT supported. Perihelion is handled separately (see Capability D).

---

## Capability B: Precision Perigee Marker

White square-open marker at the JPL CAD perigee position. Consistent with other apsidal markers. Hover text includes date, center-to-center distance (AU and km), surface distance, relative velocity, 3-sigma uncertainty, and orbit solution ID.

**Note on marker offset:** The marker may not sit exactly on the plotted trajectory. This is expected — the trajectory has ~13-hour time resolution (51 points over 28 days), while the CAD perigee is precise to seconds. The offset is informative, not a bug.

---

## Capability C: Hyperbolic Osculating Orbit

**Module:** `idealized_orbits.py` — function `plot_hyperbolic_osculating_orbit()`

White dotted arc showing the instantaneous Keplerian hyperbola at perigee epoch.

**Three key design decisions:**

1. **Epoch at perigee, not plot start.** Elements are fetched at the CAD perigee JD, not the plot start date. Elements at Apr 1 give q=91,636 km (wrong). Elements at Apr 13 give q=38,012 km (matches CAD). Pass `approach=best_approach` from `_add_close_approach_extras`.

2. **Bypass the osculating cache entirely.** `osculating_cache_manager` keys on `obj_name + center_body` with no date. A cached Apr 1 entry would be returned even when requesting Apr 13. The hyperbolic fetch calls `fetch_osculating_elements()` directly — no cache read, no cache write.

3. **Arc bounded by the plotted cube.** Binary search finds theta where `r = axis_range * 1.5`. Never flies off-screen. Sinh-spaced point density: 300 points per arm, ~10x denser near periapsis than asymptotes.

**Function signature:**
```python
plot_hyperbolic_osculating_orbit(
    fig, obj_name, obj_info, center_id, color_map,
    date, show_apsidal_markers=False, parent_window=None,
    approach=None   # <-- CRITICAL: pass the CAD approach dict for correct epoch
)
```

---

## Integration Point: `_add_close_approach_extras()` in `palomas_orrery.py`

Called after `plot_idealized_orbits` when center is a major body (not Sun). Three changes were made:

1. `best_approach = None` initialized before Capability B's try block (outer scope)
2. `best_approach = best` set inside `if approaches_in_window:` block
3. `approach=best_approach` passed to `plot_hyperbolic_osculating_orbit`

**Guard:** Only fires for `MAJOR_BODY_CENTERS = {Earth, Mars, Venus, Mercury, Jupiter, Saturn, Uranus, Neptune, Moon}`. Sun excluded by design.

---

## Files Changed

| File | Change |
|------|--------|
| `close_approach_data.py` | New module — CAD API, cache, perigee marker, position fetch |
| `idealized_orbits.py` | Added `plot_hyperbolic_osculating_orbit()` |
| `palomas_orrery.py` | Added `_add_close_approach_extras()`, called after plot_idealized_orbits; 3 targeted edits to pass `best_approach` |
| `data/close_approach_cache.json` | New cache file — created on first run |

**Not changed:** `orbit_data_manager.py` (the byte-size vs entry-count safety check issue is tracked but not urgent — see below).

---

## Known Issue: orbit_data_manager Safety Check

The size-reduction safety check compares file sizes in bytes. If `orbit_paths.json` was ever written with `indent=2` (e.g., by a migration script), the file inflates ~50%. When the orrery saves it back in compact format, the safety check fires a false alarm. The fix is to compare entry counts instead of byte sizes. Not yet implemented — low priority since the CAD data now lives in its own file and the collision no longer occurs.

---

## Capability D: Sun-Centered Perihelion Osculating Orbit (PLANNED)

**Motivation:** The same precision that Capability C gives for planetary flybys would be valuable for comets at perihelion — especially hyperbolic comets like 3I/ATLAS (e >> 1).

**Why CAD API doesn't help here:** The CAD API `body` parameter supports major planets only. Sun is not a valid body. Perihelion is not catalogued as a "close approach."

**Proposed approach:** The perihelion time `Tp` is already available in the osculating elements returned by Horizons (present in `osculating_cache` as a Julian Date). Use `Tp` as the epoch to fetch elements *at* perihelion, then plot the osculating conic (hyperbola for e>1, near-parabola for e~1) centered on the Sun. No new API required.

**Trigger condition:** Center = Sun, object is a comet or high-eccentricity smallbody, apsidal markers enabled.

**Generalizes to:** Any comet with a well-defined `Tp` — Halley, ATLAS, SWAN, 3I/ATLAS, Borisov, etc.

**Implementation notes:**
- Reuse `plot_hyperbolic_osculating_orbit()` with `center_id='Sun'`
- Source epoch from `elements['TP']` in the osculating cache entry (already stored)
- Convert `Tp` (Julian Date) to datetime for the Horizons fetch
- Place a perihelion marker using existing apsidal marker infrastructure (not CAD)
- No cache bypass needed if using stored `Tp` — epoch is deterministic from elements

---

## Verification Checklist (Capabilities A-C)

- [x] CAD API fetch: `2029-Apr-13 21:46 | 38,011.5 km | 7.423 km/s`
- [x] Cache hit on second run: `[CAD] Cache hit: close_approach:2004 MN4:Earth`
- [x] Perigee marker: white square-open, correct position
- [x] Hover text: full data including 3-sigma uncertainty
- [x] Hyperbola legend: `Apophis Osculating Orbit (Epoch: 2029-04-13 osc.)`
- [x] Hyperbola q: ~38,012 km (matches CAD within 1 km)
- [x] Hyperbola arc: white dotted, cube-bounded, dense at periapsis
- [x] No dialog for hyperbola fetch (direct fetch, no cache collision)

---

## Quotables

*"Osculating elements must be fetched at the perigee epoch, not the plot start date."*  
*"Bypassing the cache is correct for precision epoch-specific fetches."*  
*"The offset between the marker and the trajectory is informative, not a bug."*  
*"It passes BELOW the geostationary ring."* — On Apophis 2029
