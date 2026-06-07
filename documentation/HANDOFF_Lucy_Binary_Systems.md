# Handoff: Lucy Binary Systems + TNO Moon Osculating Orbits

**Date:** February 3, 2026
**Previous Sessions:** Dynamic center dropdown refactor + Lucy single targets + center_id fix + Orcus JPL orbit resolution + Quaoar-Weywot cleanup + TNO osculating orbit routing + Earth-Moon Barycenter implementation
**Next Task:** Implement Eurybates-Queta and Polymele-Shaun binary systems; continue TNO moon testing; apply pending Vanth/Patroclus cache cleanups

---

## Session Summary (February 3, 2026)

### Earth-Moon Barycenter: COMPLETE

Implemented Earth-Moon Barycenter as a new center option in the orrery. This is the third barycenter mode (after Pluto-Charon and Orcus-Vanth). Unlike those systems, the EMB is INSIDE Earth -- but Earth's monthly wobble around it is real and visualizable.

**Key physics:**
- Mass ratio: Moon/Earth = 1.23% (highest of any planet-moon system)
- Barycenter: ~4,670 km from Earth center (~1,700 km below surface)
- Location: between outer core and lower mantle
- Period: 27.32 days -- Earth and Moon BOTH orbit EMB with this period
- Earth's heliocentric orbit is actually around the Sun-EMB, not Sun-Earth

**JPL Horizons integration:**
- `399@3` (Earth at EMB) -- fetches successfully, no fallbacks needed
- `301@3` (Moon at EMB) -- fetches successfully
- JPL ID `3` is the Earth-Moon system barycenter (already existed in Horizons)

**Test results (from logs):**
```
[EMB BARYCENTER MODE] Earth: using barycentric osculating elements (Earth@3)
  a=0.0000314 AU (4695.6 km from barycenter)
  e=0.057663, i=5.23 deg, Omega=338.66 deg, omega=284.48 deg

[EMB BARYCENTER MODE] Moon: using barycentric osculating elements (Moon@3)
  a=0.0025519 AU (381757.1 km from barycenter)
  e=0.057663, i=5.23 deg, Omega=338.66 deg, omega=104.48 deg
```

Both objects share identical e, i, Omega (same orbital plane, same eccentricity) -- omega differs by 180 deg (opposite sides of barycenter). This is exactly correct for a binary system.

**Files modified (5 files):**

| File | Change |
|------|--------|
| `celestial_objects.py` | Added Earth-Moon Barycenter object entry (ID '3', between Moon and Mars) |
| `orbital_elements.py` | Added `'Earth-Moon Barycenter': ['Earth', 'Moon']` to parent_planets mapping |
| `constants_new.py` | Added info text with scale recommendation (0.003 AU), binary params, visualization instructions. Fixed 2 unescaped apostrophes in `Earth's` |
| `idealized_orbits.py` | Added `plot_earth_moon_barycenter_orbit()` (~190 lines), `add_earth_moon_barycenter_marker()` (~65 lines), dispatch routing in `plot_osculating_orbits` |
| `palomas_orrery.py` | 8 changes: IntVar, GUI checkbox, 2 pipeline osculating center routings, 2 pipeline pre-fetch routings, trace tracking, frame loop marker update |

**No changes needed to `orbit_data_manager.py`** -- Moon routes via 3-digit satellite logic, Earth as majorbody. Both `399@3` and `301@3` work directly in JPL.

**Architecture notes:**
- `plot_earth_moon_barycenter_orbit()` handles both Earth-centered (traditional) and barycenter-centered (binary) modes
- In barycenter mode, tries cache keys `Earth@3` and `Moon@3` first, falls back to mass-ratio calculation
- `add_earth_moon_barycenter_marker()` uses Moon's position to calculate barycenter location along Earth-Moon line
- Animation frame updates derive barycenter position from Moon position each frame (pipeline 3)
- All 5 parallel pipelines patched (lesson from Orcus sessions)

**Tony's editorial changes (unrelated to EMB):**
- Commented out Haumea System Barycenter entry in celestial_objects.py
- Added scale reminders to Pluto system moons (Charon, Styx, Nix, Kerberos, Hydra)
- Adjusted Pluto scale from .002 to .0005 AU
- Minor whitespace/comment trimming

### Social Media Export Mode: DESIGNED (not implemented)

Discussion about creating screen-recording-friendly views for Instagram/YouTube Shorts. Problem: hovertext is the educational payload but trapped in ephemeral tooltips. See separate handoff document: `HANDOFF_Social_Media_View.md`.

---

## Session Summary (February 1, 2026)

### Quaoar-Weywot Barycenter: REMOVED

Removed Quaoar-Weywot Barycenter mode from the orrery. Unlike Orcus-Vanth (16% mass ratio, barycenter outside primary body), Quaoar-Weywot has a ~0.4% mass ratio -- barycenter offset is only ~7 km from Quaoar's center (inside a 1,090 km body). Not visually meaningful.

**Files edited (4 files, surgical removals):**

| File | Change |
|------|--------|
| `celestial_objects.py` | Removed Quaoar-Weywot Barycenter object entry |
| `orbital_elements.py` | Removed from `center_objects` dict |
| `palomas_orrery.py` | Removed variable, checkbox, 3 analytical fallback list entries |
| `idealized_orbits.py` | Removed Weywot from 2 `ANALYTICAL_ONLY_SATELLITES` lists |

### Weywot Osculating Orbit: FIXED

Weywot's osculating orbit was plotting with placeholder elements (i=15 deg, e=0.011, omega=0, Omega=0) because `orbit_data_manager.py` had no routing for Weywot -- queries fell through to `@sun`, returning heliocentric garbage.

**Root cause:** Missing routing entry in the osculating element location block.

**Fix applied to `orbit_data_manager.py`** (line ~1718):
```python
# Handle Weywot (Quaoar's moon)
elif horizons_id == '120050000':
    location = '@920050000'  # Relative to Quaoar primary body
```

Two additional TNO moon routings added at the same time:
```python
# Handle Vanth (Orcus's moon)
elif horizons_id == '120090482':
    location = '@20090482'  # Relative to Orcus system barycenter

# Handle Xiangliu (Gonggong's moon)
elif horizons_id == '120225088':
    location = '@20225088'  # Relative to Gonggong system barycenter
```

**Additional fix:** Weywot removed from `SKIP_HORIZONS_PREFETCH` in `palomas_orrery.py` (lines 3483 and 5180) so the osculating cache update dialog fires.

**Validated Weywot osculating elements** (from Horizons at `@920050000`):
- e = 0.2527 (moderate eccentricity -- NOT 0.011 placeholder)
- i = 154.32 deg (RETROGRADE orbit -- NOT 15 deg placeholder)
- Omega = 331.00 deg (real ascending node -- NOT 0 deg)
- omega = 36.30 deg (real argument of periapsis -- NOT 0 deg)
- a = 0.000090 AU (~13,500 km)
- Period ~11.7 days (close to 12.44 day estimate)

### Vanth Osculating Orbit: DEFERRED

Removed Vanth from `SKIP_HORIZONS_PREFETCH` and `ANALYTICAL_ONLY_SATELLITES` to test. Results:

- **Pre-fetch works:** Horizons returns valid elements for `120090482@20090482`
- **Keplerian plotting does not work:** The Orcus system function (`plot_orcus_barycenter_orbit`) has an early return in barycenter mode (line 2310-2315) and uses bare-name cache lookups in Orcus-centered mode (line 2347) that don't match the center-suffixed cache keys

**Decision:** Put Vanth back on both skip lists. The Orcus-Vanth barycenter mode works with JPL actual orbit traces -- adding osculating orbits requires reworking the Orcus system function's cache key handling for no visual gain. JPL actual orbits are the real data.

**Action items for Vanth:**
- Restore Vanth to `SKIP_HORIZONS_PREFETCH` (2 locations in palomas_orrery.py)
- Restore Vanth to `ANALYTICAL_ONLY_SATELLITES` (2 locations in idealized_orbits.py)
- Delete stale `Vanth` entry from `osculating_cache.json` (heliocentric, a=38.6 AU -- useless)
- Delete `Vanth@20090482` and `Vanth@920090482` entries from cache if present

### Apsidal Marker Bug: NOTED (not fixed)

When apsidal markers try to fetch Vanth's position at periapsis time, the Horizons query fails with:
```
Cannot find central body matching "ORCUS-VANTH BARYCENTER"
```
The apsidal code is passing the center body as a name string instead of numeric ID `@20090482`. Same issue likely affects Weywot:
```
Ambiguous target name; provide unique id: 20050000/920050000/120050000
```
These are separate bugs in the apsidal marker code path -- not blocking, but worth fixing later.

### Patroclus-Menoetius Cache: NOTED

Stale NaN entries found in `osculating_cache.json`:
- `Patroclus@20000617`: a=4.47e+83, e=NaN (920000617 at barycenter fails)
- `Menoetius@20000617`: a=4.47e+83, e=NaN (120000617 at barycenter fails)

Same pattern as Orcus primary at barycenter. Should be cleaned from cache.

---

## Previous Sessions Summary

### January 31, 2026: Orcus-Vanth Barycenter RESOLVED

Five locations in `palomas_orrery.py` patched for Orcus trajectory derivation from Vanth. ALMA orbit circles removed from `idealized_orbits.py`. Hover text explains derivation method.

### January 30, 2026: Lucy center_id Fix + Patroclus Binary

Lucy center_id corrections applied (Dinkinesh, Donaldjohanson, Eurybates, Polymele, Leucus, Orus). Patroclus-Menoetius binary components working as coordinate centers.

---

## Horizons Binary System ID Patterns

| Component | ID Pattern | Patroclus | Orcus | Quaoar | Earth-Moon |
|-----------|-----------|-----------|-------|--------|------------|
| System barycenter | `20XXXXXX` | `20000617` | `20090482` | `20050000` | `3` |
| Primary body | `920XXXXXX` | `920000617` | `920090482` | `920050000` | `399` |
| Secondary body | `120XXXXXX` | `120000617` | `120090482` | `120050000` | `301` |

**Key lessons:**
- `920XXXXXX` primary IDs often fail when queried at their own barycenter ("IOBJ out of bounds")
- `120XXXXXX` secondary IDs are more reliable for barycenter-relative queries
- Derive primary from secondary: `primary_pos = -secondary_pos * mass_ratio`
- For osculating elements: secondary at primary body (`120XXXXXX@920XXXXXX`) works (Weywot proved this)
- Earth-Moon system uses legacy IDs (3, 399, 301) -- both `399@3` and `301@3` work directly

---

## Barycenter Implementation Comparison

| Feature | Pluto-Charon | Orcus-Vanth | Earth-Moon |
|---------|-------------|-------------|------------|
| Mass ratio | 12.2% | 16% | 1.23% |
| Barycenter location | Outside Pluto | Outside Orcus | INSIDE Earth |
| Primary orbit source | Cache + mass ratio calc | Derived from secondary | JPL `399@3` direct |
| Secondary orbit source | Cache `Charon@9` | JPL `120090482@20090482` | JPL `301@3` direct |
| Animation marker | Charon position | Vanth position | Moon position |
| Scale recommendation | (default) | (default) | 0.003 AU manual |
| Shells relevant? | No | No | Yes -- shows barycenter depth |

---

## TNO Moon Osculating Orbit Status

| Moon | Routing in orbit_data_manager.py | SKIP_HORIZONS_PREFETCH | ANALYTICAL_ONLY_SATELLITES | Osculating Status |
|------|----------------------------------|----------------------|--------------------------|-------------------|
| Weywot | `120050000@920050000` | Removed (fetches work) | Removed (uses cache) | WORKING - real elements |
| Vanth | `120090482@20090482` | RESTORE (Orcus function not cache-key-aware) | RESTORE (same reason) | DEFERRED - JPL actual orbits sufficient |
| MK2 | `120136472@20136472` | Was in list | Was in list | TO TEST |
| Xiangliu | `120225088@20225088` | Was in list | Was in list | TO TEST |

### Testing Plan for Next Session

**MK2 (Makemake's moon):**
- Test Horizons query: target `120136472`, center `@20136472`
- MK2 may not have JPL satellite solution (discovered 2015 by HST, very faint)
- If fetch fails, keep on skip/analytical lists

**Xiangliu (Gonggong's moon):**
- Test Horizons query: target `120225088`, center `@20225088`
- If fetch fails, keep on skip/analytical lists

**General approach:** Test on Horizons web interface first, then remove from skip lists only if valid local elements come back.

---

## Remaining Lucy Work: Binary Systems

### Priority Targets

#### 1. Eurybates-Queta (HIGH - First Lucy Trojan encounter)
- **Flyby:** Aug 12, 2027
- **Eurybates:** ~64 km, C-type (center_id: `920003548`)
- **Queta:** ~1 km satellite (discovered 2020 by HST)
- **Horizons IDs to test:**
  - Queta: Likely `120003548` following pattern
  - System barycenter: Likely `20003548`
- **Risk:** Queta may have same `920XXXXXX` limitation as Orcus

#### 2. Polymele-Shaun (HIGH - Second Lucy Trojan encounter)
- **Flyby:** Sep 15, 2027
- **Polymele:** ~21 km, P-type (center_id: `920015094`)
- **Shaun:** ~5 km satellite (discovered 2022 via stellar occultation)
- **Challenge:** Shaun may NOT be in Horizons yet (like MK2 situation)

---

## Key Lessons from These Sessions

### Parallel Pipeline Lesson
Position data flows through 5 parallel pipelines in `palomas_orrery.py`. ALL must be patched for objects with derivation. Fix in one doesn't propagate to others.

### Skip List Gates
TNO moons have TWO gates blocking osculating orbit display:
1. `SKIP_HORIZONS_PREFETCH` - prevents the fetch dialog from firing
2. `ANALYTICAL_ONLY_SATELLITES` - bypasses cache lookup even if elements exist

Both must be opened for osculating orbits to work. But only open them when the plotting code can actually use the cached elements correctly.

### Cache Key Awareness
The Pluto system uses `get_cache_key()` with center_body suffixes (`Charon@9`, `Pluto@999`). The Orcus system function does bare-name lookups. Adding osculating orbits to Orcus system would require making it cache-key-aware -- not worth it when JPL actual orbits already work.

### ALMA vs JPL: Let the Data Speak
When two data sources disagree, use the one that provides real-time positions (JPL) and document the other (ALMA) as historical context. Verbum sapienti satis est.

### Barycenter Periods
Both objects in a binary orbit with the SAME period. Earth doesn't orbit EMB in one year -- it orbits in 27.32 days (same as Moon). The one-year period is the EMB's heliocentric orbit around the Sun. Two simultaneous motions: 27.32-day wobble + 365.26-day heliocentric orbit.

---

## Pending Edits (for Tony to apply)

### High Priority
- Restore Vanth to `SKIP_HORIZONS_PREFETCH` (lines ~3483 and ~5180 in palomas_orrery.py)
- Restore Vanth to `ANALYTICAL_ONLY_SATELLITES` (lines ~1841 and ~4373 in idealized_orbits.py)

### Cache Cleanup
- Delete stale Vanth entries from `osculating_cache.json` (heliocentric a=38.6 AU)
- Delete `Vanth@20090482` and `Vanth@920090482` entries from cache if present
- Delete NaN Patroclus/Menoetius entries from `osculating_cache.json`

### Nice to Have
- Update analytical orbit hover text in `idealized_orbits.py` to explain WHY each moon uses analytical elements:

| Moon | Updated hover text |
|------|-------------------|
| Vanth | "Analytical orbit from Hubble observations<br>(Brown et al. 2010)<br>JPL actual orbit traces used in barycenter mode<br><i>Analytical orbit shown for reference</i>" |
| MK2 | Keep current text if no JPL ephemeris; update after testing |
| Xiangliu | Keep current text if no JPL ephemeris; update after testing |

The principle: hover text should explain not just *what* the user is seeing, but *why* it's shown that way. Limitations become education.

### Known Bugs (not blocking)
- Apsidal markers pass center body as name string instead of numeric ID for TNO moons
- Weywot apsidal: "Ambiguous target name; provide unique id: 20050000/920050000/120050000"
- Vanth apsidal: "Cannot find central body matching 'ORCUS-VANTH BARYCENTER'"

---

**End of Handoff**
