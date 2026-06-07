# Session Handoff: December 4, 2025

## TNO Satellite Fixes, Animation Truncation, and Barycenter Orbit Calculations

**Status:** ✅ COMPLETE AND TESTED

---

## Summary of Fixes

This session addressed multiple interconnected issues with TNO (Trans-Neptunian Object) satellite implementation, animation trajectory fetching, and actual orbit plotting. The fixes span `palomas_orrery.py`, `idealized_orbits.py`, and `visualization_utils.py`.

---

## Fix 1: Animation Trajectory Fetch - helio_id Usage

### Problem
28-year animation of Haumea and Eris failed - objects disappeared from legend and plot after initial frames.

### Root Cause
Animation trajectory fetch used system barycenter IDs (e.g., `20136108`, `20136199`) which only have JPL Horizons ephemeris data until **2030**. Animation span 2025-2052 exceeded this limit.

### Solution
Modified animation trajectory fetch to use `helio_id` when center is Sun.

### File: `palomas_orrery.py`

**Location 1:** Animation trajectory fetch (~line 5573-5580)
```python
# Use helio_id for Sun-centered plots if available (longer ephemeris coverage)
# System barycenter IDs (e.g., 20136108) only have data to ~2030
# Heliocentric IDs (e.g., 2003 EL61) have data to ~2500
fetch_id = obj['id']
fetch_id_type = obj.get('id_type')
if center_object_name == 'Sun' and 'helio_id' in obj:
    fetch_id = obj['helio_id']
    fetch_id_type = 'smallbody'  # helio_ids are smallbody designations

positions_over_time[obj['name']] = fetch_trajectory(
    fetch_id, 
    obj_dates, 
    center_id=center_id, 
    id_type=fetch_id_type
)
```

**Location 2:** pad_trajectory call (~line 5565-5572) - same pattern

**Location 3:** plot_actual_orbits function (~line 3853-3860)
```python
# Use helio_id for Sun-centered plots if available
fetch_id = obj_info['id']
fetch_id_type = obj_info.get('id_type')
if center_object_name == 'Sun' and 'helio_id' in obj_info:
    fetch_id = obj_info['helio_id']
    fetch_id_type = 'smallbody'

trajectory = fetch_trajectory(fetch_id, dates_list, center_id=center_id, id_type=fetch_id_type)
```

### Result
All TNO objects now successfully animate and plot actual orbits over 28-year spans using heliocentric IDs.

---

## Fix 2: Fractional Day Calculation - Root Cause

### Problem
28-hour animation of Triton/Pluto-Charon showed actual orbit for only 24 hours instead of 27-28 hours.

### Root Cause
The `.days` attribute returns an **integer**, truncating fractional days:
- 28 hours = 1.167 days
- `.days` returns `1` (24 hours)
- Missing ~3-4 hours of orbit

### Solution
Use `.total_seconds() / 86400` to preserve fractional days.

### File: `palomas_orrery.py`

**Critical Fix 1 - Line 453 (get_interval_settings - THE SOURCE):**
```python
# OLD (inside if block - only ran when end_date > HORIZONS_MAX_DATE):
if settings['end_date'] > HORIZONS_MAX_DATE:
    settings['end_date'] = HORIZONS_MAX_DATE
    settings['days_to_plot'] = (settings['end_date'] - settings['start_date']).total_seconds() / 86400

# NEW (OUTSIDE if block - ALWAYS runs):
if settings['end_date'] > HORIZONS_MAX_DATE:
    settings['end_date'] = HORIZONS_MAX_DATE

# Always recalculate days_to_plot from actual date range
# Use total_seconds() to preserve fractional days (e.g., 28 hours = 1.167 days, not 1 day)
settings['days_to_plot'] = (settings['end_date'] - settings['start_date']).total_seconds() / 86400
```

**Critical Fix 2 - Line 5741 (animate_objects):**
```python
# OLD:
animation_span_days = (dates_list[-1] - dates_list[0]).days if len(dates_list) > 1 else settings['days_to_plot']

# NEW:
# Use total_seconds() to preserve fractional days (e.g., 27 hours = 1.125 days, not 1 day)
animation_span_days = (dates_list[-1] - dates_list[0]).total_seconds() / 86400 if len(dates_list) > 1 else settings['days_to_plot']
```

### Other Locations Fixed (from earlier session)

**Line 795:**
```python
days_to_plot = (end_date - start_date).total_seconds() / 86400
```

**Line 4359 (plot_objects trajectories):**
```python
total_days = (end_date - start_date).total_seconds() / 86400
```

**Line 5685 (animate_objects trajectories):**
```python
total_days = (end_date - start_date).total_seconds() / 86400
```

### Result
Animation actual orbits now correctly span the full time range (e.g., 27 hours instead of truncating to 24 hours).

---

## Fix 3: Analytical Orbit Removal for Outer Planet Moons

### Problem
Neptune moons (Triton, Despina, Galatea) were showing BOTH analytical and osculating orbits. Analytical orbits were supposed to be removed.

### Root Cause
Line 3220 in `idealized_orbits.py` used `if` instead of `elif`, breaking the if/elif chain. Neptune moons got osculating orbit (lines 3194-3214), then fell through to `else` clause (line 3258) which plotted analytical orbit.

### Solution

**File:** `idealized_orbits.py`

**Fix - Line 3220:**
```python
# OLD:
# Special handling for Pluto-Charon BINARY SYSTEM
            # Two modes: traditional Pluto-centered, or barycenter-centered
            
            # Mode 1: Barycenter-centered (binary planet mode)
            if center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:

# NEW:
# Special handling for Pluto-Charon BINARY SYSTEM
            # Two modes: traditional Pluto-centered, or barycenter-centered
            
            # Mode 1: Barycenter-centered (binary planet mode)
            elif center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:
```

### Result
Neptune, Saturn, Uranus, and Pluto moons now show only osculating orbits (no analytical orbits).

---

## Fix 4: Pluto-Charon Osculating Orbit Line Style

### Problem
Pluto and Charon osculating orbits shown as solid lines, causing visual confusion with actual orbits.

### Solution

**File:** `idealized_orbits.py`

**Fix - Lines 1604-1606:**
```python
# OLD:
if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
    # Solid lines for the binary pair in barycenter mode
    line_style = dict(color=color, width=2)

# NEW:
if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
    # Dashed lines for osculating orbits (to distinguish from actual orbits)
    line_style = dict(color=color, width=2, dash='dash')
```

### Result
Pluto and Charon osculating orbits now display as dashed lines, clearly distinguishable from solid actual orbit traces.

---

## Fix 5: Barycenter-Centered Actual Orbit Calculation

### Problem
When centered on Pluto-Charon Barycenter, Pluto and Charon actual orbits plotted as tiny arcs over 28 days instead of ~4.4 complete orbits.

### Root Cause
- Pluto has `object_type='orbital'` (not 'satellite')
- Code checked `obj_type == 'satellite'` first → Pluto failed
- Fell through to `obj_type == 'orbital'` branch
- Used Pluto's **heliocentric** period (248 years = 90,560 days)
- 28 days / 90,560 days = 0.03% of orbit → tiny arc
- Reality: Pluto orbits barycenter in **6.387 days**, so 28 days = 4.4 orbits

### Solution

**File:** `palomas_orrery.py`

**Fix - Line 4434 in plot_objects():**
```python
# OLD:
elif obj_type == 'satellite' and obj['name'] in parent_planets.get(center_object_name, []):
    # Moons of the center object
    num_points = int(satellite_points) + 1
    actual_days_to_plot = settings['days_to_plot'] 
    dates_list = [date_obj + timedelta(days=float(d)) 
                for d in np.linspace(0, actual_days_to_plot, num=num_points)]

elif obj_type == 'orbital' and obj['name'] in planetary_params:

# NEW:
# Check if this object is a satellite of the current center
# (regardless of object_type - e.g., Pluto is 'orbital' but orbits the barycenter)
elif obj['name'] in parent_planets.get(center_object_name, []):
    # Moons/orbiters of the center object - use satellite settings
    num_points = int(satellite_points) + 1
    actual_days_to_plot = settings['days_to_plot'] 
    dates_list = [date_obj + timedelta(days=float(d)) 
                for d in np.linspace(0, actual_days_to_plot, num=num_points)]

elif obj_type == 'orbital' and obj['name'] in planetary_params:
```

### Key Insight
Removed `obj_type == 'satellite'` check so ANY object in `parent_planets[center_object_name]` gets treated as satellite of center, including Pluto when centered on Pluto-Charon Barycenter.

### Result
Pluto and Charon actual orbits now correctly show ~4.4 complete orbits over 28 days when viewed from barycenter.

---

## Fix 6: Pluto Hover Text Fix

### Problem
Pluto hover text showed "Calculated Orbital Period: N/A (satellite of Pluto-Charon Barycenter)" when viewing from Sun.

### Solution

**File:** `visualization_utils.py`

**Fix - Line 510-511:**
```python
# OLD:
if is_satellite:
    full_hover_text += f"Calculated Orbital Period: N/A (satellite of {planet})<br>"

# NEW:
# Only show "satellite of" message when actually viewing from the parent body
# (e.g., Pluto is in parent_planets under Pluto-Charon Barycenter, but when
# viewing from Sun, we should show its heliocentric period)
if is_satellite and planet == center_object_name:
    full_hover_text += f"Calculated Orbital Period: N/A (satellite of {planet})<br>"
```

### Result
Pluto hover text correctly shows heliocentric period when viewing from Sun, and "satellite of" message only when viewing from Pluto-Charon Barycenter.

---

## Scientific Reference Data

### JPL Ephemeris Coverage Limits
| ID Type | Coverage |
|---------|----------|
| General JPL limit | 1900-2199 |
| TNO system barycenter IDs | ~2030 limit |
| TNO heliocentric IDs | ~2500 limit |
| Haumea satellite ephemeris | 2030 limit |

### Pluto-Charon Binary System
| Parameter | Value |
|-----------|-------|
| Pluto mass | 1.307×10²² kg |
| Charon mass | 1.586×10²¹ kg |
| Mass ratio | 0.122 (TRUE BINARY) |
| Orbital period | 6.387 days |
| Semi-major axis | 19,596 km |
| Pluto orbit around barycenter | ~2,035 km radius |
| Charon orbit around barycenter | ~17,561 km radius |

---

## Testing Results

| Test | Result |
|------|--------|
| 28-year animation: Neptune, Pluto, Haumea, Eris, Makemake | ✅ All objects animate |
| Console shows helio_id usage | ✅ "Processing trajectory for 2003 EL61" |
| 28-hour animation: Triton | ✅ Full 28 hours plotted |
| 28-day Pluto-Charon Barycenter | ✅ ~4.4 complete orbits |
| Osculating orbits: dashed lines | ✅ Distinguishable from actual |
| Neptune moon: no analytical orbit | ✅ Osculating only |
| Pluto hover from Sun | ✅ Shows heliocentric period |

---

## Files Modified

| File | Changes |
|------|---------|
| `palomas_orrery.py` | helio_id usage (3 locations), fractional day fixes (4 locations), barycenter orbit calculation |
| `idealized_orbits.py` | elif fix for analytical orbit removal, osculating line style |
| `visualization_utils.py` | Pluto hover text conditional |

---

## Key Lessons Learned

### 1. `.days` Truncates - Use `.total_seconds() / 86400`
The timedelta `.days` attribute returns an integer, truncating fractional days. For sub-day precision, always use `.total_seconds() / 86400`.

### 2. Fix the Source, Not the Symptom
Line 453 (get_interval_settings) was the root cause - it set `days_to_plot` for the entire session. The animation fix at line 5741 was still needed because it recalculates from actual dates.

### 3. Object Type vs Parent Relationship
An object's `object_type` ('orbital', 'satellite') is not the same as whether it's a child of the current center. Pluto is `object_type='orbital'` but IS a satellite of Pluto-Charon Barycenter. Check `parent_planets[center]` instead.

### 4. Ephemeris ID Selection Matters
Different ID types have different ephemeris coverage. System barycenter IDs may have shorter coverage than heliocentric IDs for the same object.

---

## Next Steps

- Consider updating ORBITAL_MECHANICS_README to v1.4 with these fixes
- Animation testing for all TNO systems with satellites
- Document the helio_id/system ID distinction for future reference

---

**Session Date:** December 4, 2025  
**Documented By:** Tony (with Claude)

*"The .days truncation was the root cause - fixing it at the source fixed everything downstream."*

*"Data preservation is climate action."*

---
