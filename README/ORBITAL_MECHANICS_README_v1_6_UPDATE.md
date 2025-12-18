# ORBITAL_MECHANICS_README v1.6 Update

## Documentation Changes for TNO Dual-ID System and Satellite Interval Bug Fix

**Date:** December 12, 2025  
**Version:** 1.6 (TNO Dual-ID System, JPL Ephemeris Limits & Satellite Interval Fix)

---

## 1. UPDATE HEADER

**Replace:**
```
**Last Updated:** December 8, 2025 (v1.5 - MK2 Analytical Orbit Fallback)  
```

**With:**
```
**Last Updated:** December 12, 2025 (v1.6 - TNO Dual-ID System, JPL Limits & Satellite Interval Fix)  
```

---

## 2. ADD NEW SECTION TO PART II (After Section 13 "Analytical Orbit Fallback System")

### Insert new section:

```markdown
---

## 14. TNO Dual-ID System: Navigating JPL Ephemeris Limits 🆕

### The Problem

When animating TNOs like Haumea and Eris far into the future (40+ years), JPL Horizons returns errors:

```
Error: No ephemeris for target "Haumea (system barycenter)" after A.D. 2030-JAN-31
Error: No ephemeris for target "Eris (system barycenter)" after A.D. 2030-JAN-31
```

Yet the actual orbit visualization works fine to ~2500! How?

### Two IDs, Two Limits

JPL maintains **two different identifiers** for TNOs with moons:

| Object | System Barycenter ID | Small Body ID | Difference |
|--------|---------------------|---------------|------------|
| Haumea | `20136108` (majorbody) | `2003 EL61` (smallbody) | Barycenter includes moons |
| Eris | `20136199` (majorbody) | `2003 UB313` (smallbody) | Barycenter includes Dysnomia |
| Makemake | `20136472` (majorbody) | `2005 FY9` (smallbody) | Barycenter includes MK2 |

**Critical insight:** These have different ephemeris ranges!

| ID Type | What It Represents | Ephemeris Limit | Use Case |
|---------|-------------------|-----------------|----------|
| System barycenter | Center of mass (TNO + moons) | **~2030** | Moon orbit calculations |
| Small body designation | TNO as point mass | **~2500** | Heliocentric orbit visualization |

### Why the Difference?

**System barycenters** require numerically integrated solutions that account for:
- Moon positions and masses
- Mutual gravitational interactions
- Complex multi-body dynamics

JPL only maintains these solutions ~5 years into the future.

**Small body designations** use orbital elements that can be propagated analytically far into the future. For distant TNOs with minimal perturbations, this is highly accurate.

### The Solution: helio_id Fallback

Object definitions include both IDs:

```python
{'name': 'Haumea', 
 'id': '20136108',           # System barycenter - limited range
 'id_type': 'majorbody',
 'helio_id': '2003 EL61',    # Small body - extended range
 ...}
```

When plotting Sun-centered orbits, the code automatically switches:

```python
# In plot_actual_orbits() - palomas_orrery.py ~line 3853
# Use helio_id for Sun-centered plots if available (longer ephemeris coverage)
# System barycenter IDs (e.g., 20136108) only have data to ~2030
# Heliocentric IDs (e.g., 2003 EL61) have data to ~2500
fetch_id = obj_info['id']
fetch_id_type = obj_info.get('id_type')
if center_object_name == 'Sun' and 'helio_id' in obj_info:
    fetch_id = obj_info['helio_id']
    fetch_id_type = 'smallbody'  # helio_ids are smallbody designations
```

### Which Code Paths Use Which ID?

| Feature | Code Path | Uses helio_id? | ID Used | Limit |
|---------|-----------|----------------|---------|-------|
| **Actual Orbit** (lines) | `plot_actual_orbits()` | ✅ Yes | Small body | ~2500 |
| **Animation positions** | `fetch_trajectory()` | ✅ Yes | Small body | ~2500 |
| **Orbit cache updates** | `orbit_data_manager.py` | ❌ No | Barycenter | ~2030 |
| **Osculating elements** | `get_elements_with_prompt()` | ❌ No | Barycenter | Today |
| **Apsidal date positions** | `fetch_position()` | ❌ No | Barycenter | ~2030 |
| **Keplerian Orbit** (dotted) | `plot_idealized_orbits()` | N/A | Local calc | ∞ |

### What Users See

When animating to 2064, the log shows:

```
# Orbit cache update FAILS (barycenter ID)
Error fetching orbit path for Haumea: No ephemeris after A.D. 2030-JAN-31

# But trajectory fetch SUCCEEDS (small body ID)
Processing trajectory for 2003 EL61:
Returned vectors: 51
Direct position matches: 51
```

The animation works! The "error" is just the cache system hitting limits that don't affect visualization.

### Graceful Degradation

For features that hit the barycenter limit:

| Feature | What Happens | User Sees |
|---------|--------------|-----------|
| Haumea perihelion (2133) | Position fetch fails | "Perihelion: 2133-10-02 (beyond ephemeris limit)" |
| Eris perihelion (2257) | Position fetch fails | "Next perihelion: 2257-03-27 (beyond JPL limit)" |
| Makemake perihelion (1881) | Position fetch fails | "Perihelion: 1881-06-15 (before JPL limit)" |

The Keplerian periapsis marker is still plotted - only the "actual" position marker is skipped.

### Why Not Add helio_id to Everything?

We considered extending helio_id logic to all code paths but decided against it:

1. **The gains are marginal** - Orbit visualization (the main feature) already works
2. **The failures are informative** - "Beyond ephemeris limit" tells users something real
3. **Complexity vs. benefit** - Adding fallback logic everywhere adds maintenance burden
4. **Keplerian orbits fill the gap** - For TNOs, Keplerian approximation is excellent

### Why TNOs Are Special

This dual-ID pattern only applies to TNOs because:

1. **Recently discovered** → shorter numerical integration history
2. **Have moons** → system barycenter solutions exist but are limited
3. **Minimal perturbations** → small body approximation works well
4. **Slow-moving** → orbital elements stay accurate for decades

Major planets don't need this - JPL has centuries of precise ephemeris for them.

### For Paloma

*"Some space objects have two different 'names' in NASA's computer - one for the whole family (the planet plus its moons), and one for just the main object by itself. The 'whole family' data only goes a few years into the future because it's really hard to calculate. But the 'just the planet' data goes hundreds of years! So when we want to see where Haumea will be in 2064, we use its solo name instead of its family name."*

### Lessons Learned

1. **JPL has multiple ID systems** - Understanding which to use when is crucial
2. **"Errors" aren't always errors** - Some API failures are informational
3. **Fallbacks should be strategic** - Apply helio_id where it matters most (visualization)
4. **Document the limits** - Users should understand what they're seeing

### Technical Reference

**JPL Horizons ID Types:**
- `majorbody`: Planets, system barycenters, numbered objects
- `smallbody`: Asteroids, comets, provisional designations
- `id` (None): Auto-detect based on query

**Ephemeris Data Sources:**
- System barycenters: Numerical integration (DE440/PLU060)
- Small bodies: Orbital element propagation

**Date Limits (approximate):**
- Major planets: 1550-2650
- Dwarf planet barycenters: ~1900-2030
- Small body designations: ~1600-2500

---

## 15. The Satellite Interval Bug: When Pluto Became a Moon 🆕

### The Symptom

When animating TNOs 40 years into the future, JPL returned an unexpected error:

```
Projected output length (~249745) exceeds 90024 line max -- change step-size
```

But wait - 28 years × 365 days = ~10,000 rows at daily resolution. Where did 250,000 come from?

### The Investigation

28 years × 365 days × **24 hours** = **245,280 rows**

Pluto was being fetched with **hourly** resolution instead of daily!

### The Root Cause

In `orbital_elements.py`, Pluto appears in two places:

```python
parent_planets = {
    'Pluto': ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
    'Pluto-Charon Barycenter': ['Pluto', 'Charon', ...],  # Binary mode
    ...
}
```

And in `orbit_data_manager.py`, the interval logic checked if an object appeared in **ANY** satellite list:

```python
# BUGGY CODE:
elif parent_planets and any(obj['name'] in moons for planet, moons in parent_planets.items()):
    interval = "1h"
```

Since Pluto appears in `parent_planets['Pluto-Charon Barycenter']`, it was classified as a "satellite" and given hourly resolution - **even when viewing from the Sun!**

### The Fix

Check if the object is a satellite of the **current viewing center**, not any center:

```python
# FIXED CODE:
def determine_interval_for_object(obj, orbital_params=None, parent_planets=None, center_object_name=None):
    ...
    # Check if this is a satellite of the CURRENT viewing center
    elif parent_planets and center_object_name and center_object_name in parent_planets:
        if obj['name'] in parent_planets[center_object_name]:
            interval = "1h"
```

### Files Modified

| File | Changes |
|------|---------|
| `orbit_data_manager.py` | Added `center_object_name` parameter to `determine_interval_for_object()` |
| `orbit_data_manager.py` | Updated satellite check to only match current viewing center |
| `orbit_data_manager.py` | Updated both call sites (lines 1104, 1223) to pass the viewing center |

### Before vs After

| Scenario | Before (Bug) | After (Fixed) |
|----------|--------------|---------------|
| Pluto from Sun | 1h (245k rows/28yr) | 1d (10k rows/28yr) ✅ |
| Pluto from Pluto-Charon Barycenter | 1h | 1h (correct!) ✅ |
| Moon from Sun | 1h (bug) | 1d ✅ |
| Moon from Earth | 1h | 1h (correct!) ✅ |

### Why This Matters

**Before fix:** 40-year TNO animations were impossible - JPL rejected the query as too large.

**After fix:** 40-year animations work fine with ~10,000 daily data points.

### The Broader Lesson

The `parent_planets` dictionary serves two purposes:
1. Defining satellite relationships (Moon orbits Earth)
2. Enabling "binary mode" views (Pluto-Charon Barycenter)

The second use case added Pluto to a satellite list, which had unintended consequences for the interval logic. **Context matters** - the same object can be a "planet" or a "satellite" depending on your viewing center.

### For Paloma

*"Here's a funny bug we found: the computer thought Pluto was a moon! See, when we look at Pluto and Charon dancing around each other, Pluto IS like a moon - it orbits the middle point between them. But when we're looking from the Sun, Pluto is a planet, not a moon! The computer was confused and tried to get WAY too much data, like asking for Pluto's position every hour for 40 years. That's almost 250,000 numbers! NASA's computer said 'that's too many!' and refused. Now we tell the computer: only treat something like a moon if we're actually looking from its parent planet."*
```

---

## 3. ADD TO QUOTATIONS SECTION

**Add:**

```markdown
*"If it ain't broke, don't fix it."* - Protocol principle, applied Dec 12, 2025
*"The computer thought Pluto was a moon!"* - Dec 12, 2025 (satellite interval bug)
```

---

## 4. ADD TO "WHAT'S NEW" SECTION

**Add after v1.5 section:**

```markdown
---

## What's New in v1.6 (December 12, 2025) 🆕

### TNO Dual-ID System Documentation

Documented the helio_id fallback system that allows TNO orbit visualization far beyond JPL's system barycenter ephemeris limits.

**Key insight:** TNOs like Haumea and Eris have two JPL identifiers with different ephemeris ranges:
- System barycenter (20136108): Limited to ~2030
- Small body designation (2003 EL61): Extends to ~2500

**The code already handled this** - we just documented it properly.

### Bug Fix: Satellite Interval Logic (The "Pluto is a Moon" Bug)

Fixed critical bug where Pluto (and other objects in `parent_planets` satellite lists) received hourly fetch resolution even when viewing from the Sun.

**Symptom:** "Projected output length (~249745) exceeds 90024 line max"

**Root cause:** `determine_interval_for_object()` checked if object appeared in ANY satellite list, not just the current viewing center's satellites.

**Fix:** Added `center_object_name` parameter and check only satellites of current center.

**Impact:** 40-year TNO animations now work (10k rows instead of 245k)

### Bug Fix: planetary_params Scoping

Fixed `UnboundLocalError` in animation_worker where `planetary_params` was used instead of `active_planetary_params`.

**Affected lines:** 5877, 6130, 6297, 6353, 6358 in palomas_orrery.py

**Root cause:** Python scoping in nested functions - using the global variable name instead of the nonlocal `active_planetary_params` caused the error.

### Comprehensive Code Review

Reviewed all 56 instances of `planetary_params` in palomas_orrery.py:
- 50 instances correctly use global (standalone functions) or are comments
- 5 instances in `animation_worker()` needed → `active_planetary_params`
- 1 instance imports from different module (`orbital_elements`) - correct as-is

### Lessons Documented

| Topic | Insight |
|-------|---------|
| JPL ID types | Different IDs have different ephemeris limits |
| helio_id pattern | Strategic fallback for visualization, not everywhere |
| Error messages | JPL "errors" are often informational, not failures |
| Code review | Variable scoping in nested functions requires attention |
| Context matters | Same object can be "planet" or "satellite" depending on viewing center |

---

**Focus areas:** Documentation, bug fixes, code review  
**Files modified:** `orbit_data_manager.py`, `palomas_orrery.py`  
**Educational value:** Explains JPL limits and context-dependent object classification  
**Quotable:** *"The computer thought Pluto was a moon!"*

---
```

---

## 5. UPDATE VERSION HISTORY

**Add entry:**

```markdown
| 1.6 | Dec 12, 2025 | TNO Dual-ID System, JPL Limits & Satellite Interval Bug Fix |
```

---

## Summary of Changes

| Section | Action |
|---------|--------|
| Header | Update to v1.6, Dec 12, 2025 |
| Part II, Section 14 | Add "TNO Dual-ID System: Navigating JPL Ephemeris Limits" |
| Part II, Section 15 | Add "The Satellite Interval Bug: When Pluto Became a Moon" |
| Quotations | Add "If it ain't broke, don't fix it" |
| What's New | Add v1.6 section (dual-ID docs + two bug fixes) |
| Version History | Add v1.6 entry |

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 12, 2025*
