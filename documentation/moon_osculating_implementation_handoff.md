# Moon Osculating Orbit Implementation - Handoff Document

**Date:** November 22, 2025  
**Status:** Complete with dual-trace system (analytical + osculating)  
**Author:** Tony (with Claude)  
**Project:** Paloma's Orrery

---

## Executive Summary

The Moon now displays **two ideal orbit traces** for maximum educational value:
1. **Analytical Orbit** (dotted) - Time-averaged elements showing orbital geometry
2. **Osculating Orbit** (dashed) - Daily snapshot showing instantaneous Keplerian state

This dual-trace system demonstrates:
- How osculating orbits "kiss" the actual position at epoch
- How perturbations cause divergence in both past and future directions
- The difference between time-averaged and instantaneous orbital representations

---

## Implementation Overview

### Architecture Decision: Dual-Trace System

**Why both traces:**
- **Analytical orbit:** Shows approximate orbital geometry over time (works for any date)
- **Osculating orbit:** Shows perfect instantaneous match today (date-specific)
- **Educational value:** Direct comparison teaches perturbation effects

### Key Components

**1. Function: `plot_moon_ideal_orbit()`**
- Location: `idealized_orbits.py`, lines ~1652-1872
- Plots BOTH analytical and osculating orbits
- Takes `planetary_params` parameter for osculating elements
- Falls back to analytical-only if osculating unavailable

**2. Calling Location:**
- Location: `idealized_orbits.py`, lines ~2069-2077
- Inside `plot_idealized_orbits()` function
- Special handling for Moon (different from other satellites)

---

## The Complete Implementation

### Part 1: The Function (`plot_moon_ideal_orbit`)

**Location:** Lines ~1652-1872 in `idealized_orbits.py`

**Function Signature:**
```python
def plot_moon_ideal_orbit(fig, date, center_object_name='Earth', color=None, days_to_plot=None, 
                          current_position=None, show_apsidal_markers=False, planetary_params=None):
```

**Key Parameters:**
- `planetary_params` (dict or None): Moon's osculating elements if available
  - If provided: Plots both analytical + osculating
  - If None: Plots analytical only

**Logic Flow:**

```
1. Setup (lines 1672-1695)
   - Get Moon color
   - Calculate angular range
   - Generate theta points

2. ANALYTICAL ORBIT (lines 1697-1761)
   - Call calculate_moon_orbital_elements(date)
   - Extract: a, e, i, omega, Omega
   - Calculate orbit: r = a(1-e²)/(1+e·cos(θ))
   - Apply standard rotations (ω, i, Ω)
   - Create hover text
   - Add trace (dotted line)

3. OSCULATING ORBIT (lines 1762-1827)
   - IF planetary_params is not None:
     - Extract: a, e, i, omega, Omega, epoch
     - Calculate orbit: r = a(1-e²)/(1+e·cos(θ))
     - Apply standard rotations (ω, i, Ω)
     - Create educational hover text
     - Add trace (dashed line)
   - ELSE:
     - Print info message (no osculating available)

4. Return figure
```

**Analytical Orbit Trace:**
```python
fig.add_trace(
    go.Scatter3d(
        x=x_final_ana,
        y=y_final_ana,
        z=z_final_ana,
        mode='lines',
        line=dict(dash='dot', width=2, color=color),  # Dotted
        name="Moon Ideal Orbit (Analytical)",
        ...
    )
)
```

**Osculating Orbit Trace:**
```python
fig.add_trace(
    go.Scatter3d(
        x=x_final_osc,
        y=y_final_osc,
        z=z_final_osc,
        mode='lines',
        line=dict(dash='dash', width=2, color=color),  # Dashed
        name=f"Moon Osculating Orbit (Epoch: {epoch_osc})",
        ...
    )
)
```

---

### Part 2: The Function Call

**Location:** Lines ~2069-2077 in `idealized_orbits.py`

**Context:** Inside `plot_idealized_orbits()` function, within the satellite plotting loop

**CURRENT CODE (BROKEN):**
```python
            # Special handling for Earth's Moon with time-varying elements
            if moon_name == 'Moon' and center_id == 'Earth':
                # Get Moon's current position from current_positions
                moon_current_pos = current_positions.get('Moon') if current_positions else None

                fig = plot_moon_ideal_orbit(fig, date, center_id, color_map(moon_name), days_to_plot,
                                            current_position=moon_current_pos,
                                            show_apsidal_markers=show_apsidal_markers)
                                            # ❌ MISSING: planetary_params parameter!
```

**FIXED CODE:**
```python
            # Special handling for Earth's Moon with time-varying elements
            if moon_name == 'Moon' and center_id == 'Earth':
                # Get Moon's current position from current_positions
                moon_current_pos = current_positions.get('Moon') if current_positions else None
                
                # Get Moon's osculating elements if available
                moon_params = planetary_params.get('Moon') if planetary_params else None

                fig = plot_moon_ideal_orbit(fig, date, center_id, color_map(moon_name), days_to_plot,
                                            current_position=moon_current_pos,
                                            show_apsidal_markers=show_apsidal_markers,
                                            planetary_params=moon_params)  # ✅ ADD THIS!
```

**What Changed:**
1. **Line added:** `moon_params = planetary_params.get('Moon') if planetary_params else None`
   - Extracts Moon's osculating elements from the full dictionary
   - Returns None if Moon not in dictionary (graceful fallback)

2. **Parameter added:** `planetary_params=moon_params`
   - Passes Moon's elements to the function
   - Enables osculating orbit plotting

---

## The Fix (Step-by-Step)

### Problem Statement

**Symptom:** Only analytical orbit shows, no osculating orbit
**Cause:** `planetary_params` not passed to `plot_moon_ideal_orbit()`
**Result:** Function receives `None`, skips osculating section (line 1764 check fails)

### Solution

**Location:** `idealized_orbits.py`, lines ~2069-2077

**Step 1:** Add variable extraction
```python
moon_params = planetary_params.get('Moon') if planetary_params else None
```
- Insert AFTER: `moon_current_pos = ...` line
- Insert BEFORE: `fig = plot_moon_ideal_orbit(...)` call
- **Indentation:** Same level as `moon_current_pos` line (16 spaces / 4 tabs)

**Step 2:** Add parameter to function call
```python
planetary_params=moon_params
```
- Add as last parameter to `plot_moon_ideal_orbit()` call
- After: `show_apsidal_markers=show_apsidal_markers`
- **Indentation:** Aligned with other parameters

### Verification

**After applying fix, console should show:**
```
[ANALYTICAL] Moon orbital elements for 2025-11-22:
  a = 0.002569 AU
  e = 0.054900
  i = 5.14°
  ω = 318.15°
  Ω = 125.08°

[OSCULATING] Moon orbital elements:
  Epoch: 2025-11-20 osc.
  a = 0.002591 AU
  e = 0.049177
  i = 5.00°
  ω = 70.42°
  Ω = 345.14°
```

**Visualization should show:**
- White solid line: Actual orbit (JPL vectors)
- Dotted line: Analytical orbit
- Dashed line: Osculating orbit (THIS IS MISSING WITHOUT FIX)

---

## Educational Hover Text

### Analytical Orbit Hover Text

```
Moon Ideal Orbit (Analytical)
Date: 2025-11-22 00:00 UTC
a=0.002569 AU
e=0.054900
i=5.14°

This orbit uses time-averaged parameters
showing approximate orbital geometry.
```

### Osculating Orbit Hover Text

```
Moon Osculating Orbit
Epoch: 2025-11-20 osc.
a=0.002591 AU
e=0.049177
i=5.00°

Osculating orbit 'kisses' actual position at epoch,
then diverges as perturbations accumulate from:
• Solar gravity (largest effect)
• Earth's oblateness (J2 - equatorial bulge)
  causes nodal precession (Ω rotates ~19.3°/yr)
• Tidal forces

It fits only the present position, not past or future positions.

See 'Orbital Parameter Visualization' for J2 details
```

---

## How It Works

### Data Flow

```
1. User selects Moon visualization
   ↓
2. System fetches osculating elements (if enabled)
   ↓
3. Elements stored in planetary_params['Moon']
   ↓
4. plot_idealized_orbits() called
   ↓
5. For Moon: Extract moon_params from planetary_params
   ↓
6. plot_moon_ideal_orbit() called WITH moon_params
   ↓
7. Function plots:
   - Analytical orbit (always)
   - Osculating orbit (if moon_params not None)
   ↓
8. User sees both traces in visualization
```

### Osculating Elements Structure

```python
planetary_params = {
    'Moon': {
        'a': 0.002591,           # Semi-major axis (AU)
        'e': 0.049177,           # Eccentricity
        'i': 5.00,               # Inclination (degrees)
        'omega': 70.42,          # Argument of periapsis (degrees)
        'Omega': 345.14,         # Longitude of ascending node (degrees)
        'epoch': '2025-11-20 osc.',  # When elements were calculated
        'TP': 2460985.770707     # Time of periapsis passage (JD)
    }
}
```

### Function Call Chain

```
palomas_orrery.py
    ↓
plot_idealized_orbits(planetary_params=active_planetary_params)
    ↓
    [Inside loop for satellites]
    if moon_name == 'Moon':
        moon_params = planetary_params.get('Moon')
        ↓
        plot_moon_ideal_orbit(planetary_params=moon_params)
            ↓
            if planetary_params is not None:
                [Plot osculating orbit]
            else:
                [Skip osculating, print info message]
```

---

## Testing & Verification

### Test 1: Osculating Elements Available

**Setup:**
- Fresh osculating elements in cache
- Plot Moon for current date

**Expected Console Output:**
```
[ANALYTICAL] Moon orbital elements for 2025-11-22:
  a = 0.002569 AU
  ...

[OSCULATING] Moon orbital elements:
  Epoch: 2025-11-20 osc.
  a = 0.002591 AU
  ...
```

**Expected Visualization:**
- ✅ Analytical orbit (dotted)
- ✅ Osculating orbit (dashed)
- ✅ Both in legend
- ✅ Osculating "kisses" actual orbit at current date

### Test 2: No Osculating Elements

**Setup:**
- Delete Moon from osculating cache
- Plot Moon

**Expected Console Output:**
```
[ANALYTICAL] Moon orbital elements for 2025-11-22:
  a = 0.002569 AU
  ...

[INFO] No osculating elements available for Moon - showing analytical orbit only
```

**Expected Visualization:**
- ✅ Analytical orbit (dotted)
- ❌ No osculating orbit
- ✅ No error, graceful degradation

### Test 3: Historical Date

**Setup:**
- Plot Moon for Nov 20, 2024 (one year ago)
- Using current (2025) osculating elements

**Expected Behavior:**
- ✅ Analytical orbit shown
- ✅ Osculating orbit shown
- ⚠️ Osculating won't match exactly (wrong epoch)
- ✅ Demonstrates date-specific nature of osculating

---

## Common Issues & Troubleshooting

### Issue 1: No Osculating Orbit Visible

**Symptom:** Only analytical orbit (dotted) shows, no dashed line

**Diagnosis:**
Check console for:
```
[INFO] No osculating elements available for Moon - showing analytical orbit only
```

**Possible Causes:**
1. ❌ `planetary_params` not passed to function (THE FIX NEEDED)
2. ❌ Moon not in osculating cache
3. ❌ `planetary_params` is None in calling function

**Solution:**
1. Apply the fix (add `moon_params` extraction and pass to function)
2. Check that osculating elements were fetched for Moon
3. Verify `plot_idealized_orbits()` receives non-None `planetary_params`

### Issue 2: "moon_params is not defined" Error

**Symptom:** Python NameError when plotting

**Cause:** Variable extraction line not added before function call

**Solution:**
Add this line BEFORE the `fig = plot_moon_ideal_orbit(...)` call:
```python
moon_params = planetary_params.get('Moon') if planetary_params else None
```

**Check:**
- Indentation matches surrounding code (16 spaces)
- Line is BEFORE the function call
- No typos in variable name

### Issue 3: Osculating Orbit Doesn't Match Actual Orbit

**Symptom:** Dashed line doesn't "kiss" actual orbit at current date

**Possible Causes:**
1. Using old cached elements (not current date)
2. Plotting historical date with current elements
3. Coordinate transformation issue

**Diagnosis:**
- Check console for epoch date in `[OSCULATING]` output
- Should match current date (or be very recent)
- If epoch is old, refresh osculating elements

---

## Key Discoveries & Lessons

### Discovery 1: Osculating Orbits Diverge Both Ways

**Finding:** Osculating orbit doesn't just diverge forward in time, but BACKWARD too!

**Why:** Osculating elements are instantaneous snapshots, not predictions
- They describe orbit "frozen" at one instant
- Real orbit experienced different perturbations in past
- Real orbit will experience perturbations in future
- Only matches perfectly at epoch moment

**Educational Value:** Perfect demonstration that osculating ≠ prediction

### Discovery 2: Date-Specific Nature

**Finding:** 2025 osculating elements don't match 2024 orbit exactly

**Why:** Each date has its own osculating elements
- Elements are time-stamped
- Moon's orbit evolves continuously
- Need date-appropriate elements for historical accuracy

**Implication:** For historical dates, would need to fetch elements from that date

### Discovery 3: Dual-Trace Educational Value

**Finding:** Showing both analytical and osculating together maximizes learning

**Why:** Direct comparison shows:
- How time-averaged differs from instantaneous
- How perturbations accumulate
- When each method is appropriate
- Real-world orbital complexity

---

## Future Enhancements

### Enhancement 1: Date-Aware Display

**Concept:** Hide osculating orbit when plotting distant dates

**Logic:**
```python
days_diff = abs((plot_date - element_date).days)
if days_diff > 30:
    # Don't plot osculating (too inaccurate)
    # Show analytical only
```

**Benefit:** Avoids confusion from showing inaccurate snapshot for wrong date

### Enhancement 2: Historical Element Fetching

**Concept:** Fetch date-specific osculating elements for historical dates

**Challenge:** Would need to query JPL for historical dates
**Benefit:** Perfect "kiss" at any historical date

### Enhancement 3: Multiple Satellites

**Concept:** Apply dual-trace system to Phobos, Deimos, Io, etc.

**Status:** Partially implemented for Martian moons
**Next Steps:** Debug why osculating not plotting for non-Moon satellites

---

## Dependencies

### Required Imports
```python
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
```

### Required Functions
- `calculate_moon_orbital_elements(date)` - Analytical elements
- `rotate_points(x, y, z, angle, axis)` - Coordinate rotations
- `KNOWN_ORBITAL_PERIODS` - Moon period constant

### Required Data
- `planetary_params['Moon']` - Osculating elements dictionary
- Must include: a, e, i, omega, Omega, epoch

---

## Code Locations Quick Reference

| Component | File | Lines | Purpose |
|-----------|------|-------|---------|
| Function definition | idealized_orbits.py | 1652-1872 | Plots both orbits |
| Function call | idealized_orbits.py | 2069-2077 | WHERE TO APPLY FIX |
| Analytical calculation | idealized_orbits.py | 1697-1761 | Time-averaged orbit |
| Osculating calculation | idealized_orbits.py | 1762-1827 | Snapshot orbit |
| Hover text (analytical) | idealized_orbits.py | ~1730-1740 | Educational text |
| Hover text (osculating) | idealized_orbits.py | ~1799-1809 | Educational text with perturbations |

---

## Version History

- **v1.0** (Nov 20, 2025): Initial osculating integration
- **v1.1** (Nov 20, 2025): Added educational hover text with J2 explanation
- **v1.2** (Nov 20, 2025): Dual-trace system (analytical + osculating)
- **v1.3** (Nov 22, 2025): **Current - Handoff created, fix documented**

---

## Quick Start: Applying The Fix

**If osculating orbit not showing, follow these steps:**

1. **Open** `idealized_orbits.py`

2. **Find** line ~2070: `if moon_name == 'Moon' and center_id == 'Earth':`

3. **Locate** the Moon function call (~line 2074)

4. **Add ONE line** before the function call:
   ```python
   moon_params = planetary_params.get('Moon') if planetary_params else None
   ```

5. **Add ONE parameter** to the function call:
   ```python
   planetary_params=moon_params
   ```

6. **Save** and test

7. **Verify** console shows `[OSCULATING] Moon orbital elements:`

8. **Check** visualization shows dashed line

**That's it!** Two small changes enable the osculating orbit.

---

## Contact & Support

**Questions about this implementation?**
- Review the handoff documents in `/mnt/user-data/outputs/`
- Check `osculating_cache_system_handoff.md` for broader context
- See `orbital_mechanics_guide.md` for educational content

**Key principle:** When unsure, ask. Alignment beats assumptions.

---

*"Osculating orbits 'kiss' at epoch, then diverge in BOTH directions!"*

*"Two traces, two purposes: Analytical shows geometry, Osculating shows state. Both teach!"*

*"The fix is simple: Extract moon_params, pass to function. Two lines unlock education!"*

---

**Status:** Implementation complete, fix documented, ready to apply! 🌙✨
