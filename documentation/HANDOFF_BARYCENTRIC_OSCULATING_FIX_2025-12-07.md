# Handoff: Barycentric Osculating Orbit Fix

## Date: December 7, 2025

## Summary

Successfully implemented view-aware osculating orbit caching for the Pluto-Charon system. Osculating orbits now correctly "osculate" (touch the actual trajectory at epoch) in both Pluto-centered and barycenter views by using the appropriate reference frame for each view.

---

## Problem Identified

When viewing from **Pluto-Charon Barycenter**, the osculating (dashed Keplerian) orbits did not pass through the actual trajectory points. Visual inspection showed a clear gap between the osculating orbit and the plotted trajectory.

### Root Cause

**Reference frame mismatch:**
- Actual trajectories: Fetched relative to `@9` (Pluto-Charon Barycenter)
- Osculating elements: Fetched relative to `@999` (Pluto body center)

The code was using Pluto-centered (`@999`) osculating elements regardless of the view, but trajectories were correctly fetched from the barycenter (`@9`) when in barycenter view.

---

## Solution: Three-Step Implementation

### Step 1: Add MA/TA to Cache ✅

Added Mean Anomaly (MA) and True Anomaly (TA) extraction to `orbit_data_manager.py`:

```python
# Lines 1750-1758
try:
    ma_val = get_col(['MA', 'M', 'meanAnomaly'])
except KeyError:
    ma_val = None

try:
    ta_val = get_col(['TA', 'nu', 'trueAnomaly'])
except KeyError:
    ta_val = None
```

These values are stored in the cache and will enable future phase verification (confirming the osculating orbit passes through the correct point at epoch).

### Step 2: Center-Body Aware Caching ✅

**orbit_data_manager.py:**
- Added `center_body=None` parameter to `query_horizons_elements()` (line 1619)
- Added override logic to use explicit center when provided (lines 1715-1721)
- Added `'center_body': location` to result dict (line 1795)

**osculating_cache_manager.py:**
- Added `get_cache_key()` helper function (line 32) to generate cache keys like `Charon@9`
- Added `center_body=None` parameter to:
  - `check_cache_status()` (line 304)
  - `fetch_osculating_elements()` (line 364)
  - `get_elements_with_prompt()` (line 500)
- All functions now pass `center_body` through the chain

### Step 3: View-Aware Cache Keys ✅

**palomas_orrery.py:**
- Added `osculating_center_body` determination based on view center (~line 3952):
  - `'@9'` for Pluto-Charon Barycenter view
  - `'@999'` for Pluto view
  - `None` for other views (auto-detect)
- Pre-fetch now passes `center_body` to `get_elements_with_prompt()` for Pluto system objects

**idealized_orbits.py:**
- Imports `get_cache_key` alongside `load_cache`
- BARYCENTER MODE: Looks for `cache['Pluto@9']`, `cache['Charon@9']` first
- Falls back to calculated values if barycentric cache not available
- Outer moons use `get_cache_key(object_name, '@9')` in barycenter view

---

## Cache Structure After Implementation

```json
{
  "Pluto": { "metadata": { "center_body": "@sun" } },
  "Charon": { "metadata": { "center_body": "@999" } },
  "Styx": { "metadata": { "center_body": "@999" } },
  "Charon@999": { "metadata": { "center_body": "@999" } },
  "Styx@999": { "metadata": { "center_body": "@999" } },
  "Pluto@9": { "metadata": { "center_body": "@9" } },
  "Charon@9": { "metadata": { "center_body": "@9" } },
  "Styx@9": { "metadata": { "center_body": "@9" } }
}
```

Each object can now have multiple cache entries for different reference frames.

---

## Key Console Output Showing Success

### Pre-fetch with center_body override:
```
[Horizons Query] Using explicit center_body override: @9
[Horizons Query] ID: 901 | Type: majorbody | Location: @9 | Date: 2025-12-07
```

### Plotting with barycentric elements:
```
[BARYCENTER MODE] Pluto: using barycentric osculating elements (Pluto@9)
  a=0.0000142 AU (2131.3 km from barycenter)
  e=0.000167, i=112.89°, Ω=227.39°, ω=314.39°

[BARYCENTER MODE] Charon: using barycentric osculating elements (Charon@9)
  a=0.0001167 AU (17464.1 km from barycenter)
  e=0.000169, i=112.89°, Ω=227.39°, ω=171.35°

✓ Using cached osculating elements (Styx@9)
```

---

## Files Modified

| File | Changes |
|------|---------|
| `orbit_data_manager.py` | Added `center_body` parameter, override logic, MA/TA extraction |
| `osculating_cache_manager.py` | Added `get_cache_key()`, `center_body` parameter throughout |
| `palomas_orrery.py` | Pre-fetch passes `center_body` based on view |
| `idealized_orbits.py` | Uses correct cache key based on view mode |
| `osculating_cache.json` | Now contains both `@999` and `@9` entries |

---

## Remaining Issue (Minor)

**Actual apsidal markers fail in barycenter mode:**
```
Cannot find central body matching "PLUTO-CHARON BARYCENTER ", enter "*@body" for
```

The code that fetches positions for apsidal markers passes the string `"Pluto-Charon Barycenter"` instead of `"@9"` to Horizons. This is a separate bug that doesn't affect the main osculating orbit visualization.

**Location:** Likely in the `[ACTUAL APSIDAL]` processing section where it builds the Horizons query for periapsis/apoapsis position fetching.

---

## Center Body Reference

| Center ID | Name | Use Case |
|-----------|------|----------|
| `@sun`, `@0` | Solar System Barycenter | Default for planets, asteroids, comets |
| `@9` | Pluto System Barycenter | Pluto, Charon, outer moons in binary view |
| `@999` | Pluto (body center) | Satellites in Pluto-centered view |
| `@3` | Earth-Moon Barycenter | Future: Moon barycentric view |
| `@399` | Earth (body center) | Moon Earth-centered view |

---

## Testing Checklist

To verify the fix is working:

1. **Pluto heliocentric view:** `Pluto` uses `@sun` elements ✅
2. **Pluto-centered view:** `Charon`, `Styx` use `@999` elements, osculating orbits touch trajectories ✅
3. **Barycenter view:** `Pluto@9`, `Charon@9`, `Styx@9` used, osculating orbits touch trajectories ✅

---

## Lessons Learned

1. **Reference frames matter:** Osculating elements are only valid relative to the center they were calculated from
2. **Cache key strategy:** Suffix approach (`Charon@9`) provides backward compatibility while enabling multi-frame support
3. **Visual verification catches what code review misses:** The gap between osculating orbit and trajectory was obvious visually but subtle in code

---

## Future Enhancements

1. **Phase verification:** Use MA/TA to verify the osculating orbit passes through the correct point at epoch
2. **Fix apsidal marker bug:** Pass `@9` instead of string name to Horizons for barycenter view
3. **Extend to Earth-Moon system:** Same pattern could apply to `@3` (Earth-Moon barycenter) vs `@399` (Earth center)

---

## Session Duration

Approximately 2 hours spanning diagnostic investigation, three-step implementation, and testing.

---

*"The inclination tells you the reference frame." - Nov 21, 2025*

*"The cache key tells you the center." - Dec 7, 2025*
