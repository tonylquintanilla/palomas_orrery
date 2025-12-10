# ORBITAL_MECHANICS_README v1.5 Update

## Documentation Changes for MK2 Analytical Orbit Implementation

**Date:** December 8, 2025  
**Version:** 1.5 (MK2 Analytical Orbit Fallback)

---

## 1. UPDATE HEADER (Lines 5-6)

**Replace:**
```
**Last Updated:** December 4, 2025 (v1.4 - TNO Satellites & Barycenter Logic)  
```

**With:**
```
**Last Updated:** December 8, 2025 (v1.5 - MK2 Analytical Orbit Fallback)  
```

---

## 2. ADD TO PART I - After Section 6 "TNO Satellites" (After line 228)

### Insert new subsection:

```markdown
### MK2: The Moon Without an Ephemeris 🆕

**A special case in our solar system:**

MK2 is unique among the TNO satellites we visualize - JPL Horizons has **no ephemeris data** for it. While Dysnomia (Eris's moon), Hi'iaka and Namaka (Haumea's moons) all have JPL satellite ephemeris solutions, MK2 was discovered too recently (2015) and observed too sparsely for JPL to generate orbital predictions.

**What we know (2025 Hubble analysis):**

| Parameter | Value | Uncertainty |
|-----------|-------|-------------|
| Semi-major axis | 22,250 km | ± 780 km |
| Orbital period | 18.023 days | ± 0.017 days |
| Eccentricity | ~0 | Circular orbit |
| Inclination (to ecliptic) | ~74° | 63°-87° range |
| Diameter | ~175 km | Estimated |
| Surface reflectivity | ~4% | Very dark (charcoal-like) |

**The edge-on mystery:**

MK2's orbit is nearly **edge-on to Earth** (83.7° ± 1.0° relative to our line of sight). This means:
- From Earth, MK2 appears to move back and forth across Makemake
- We see minimal orbital width - almost a line
- This geometry made discovery difficult but enables mutual events (eclipses)
- The edge-on view is why inclination relative to ecliptic remains uncertain

**Why MK2 is so dark:**

MK2 reflects only ~4% of sunlight - darker than charcoal! This is puzzling because Makemake itself is quite bright. Theories include:
- MK2 may be a captured Kuiper Belt object (different composition)
- Its surface may be coated with dark organic compounds
- It may lack the fresh ice that makes Makemake bright

### For Paloma

*"MK2 is Makemake's shy little moon! It's so dark - like a piece of charcoal floating in space - that scientists didn't find it until 2015, even though they'd been looking at Makemake for years. And here's the cool part: from Earth, we see MK2's orbit almost edge-on, like looking at a hula hoop from the side. So MK2 looks like it's just sliding back and forth past Makemake, not going around in a big circle like we'd expect!"*
```

---

## 3. ADD NEW SECTION TO PART II (After Section 12, before Part III)

### Insert new section:

```markdown
---

## 13. Analytical Orbit Fallback System 🆕

### The Problem

Some satellites have no JPL Horizons ephemeris data. When we query JPL for MK2's position, we get nothing - JPL simply doesn't have enough observations to generate predictions.

**Satellites with JPL ephemeris:**
- Dysnomia (Eris) ✓
- Hi'iaka (Haumea) ✓
- Namaka (Haumea) ✓

**Satellites without JPL ephemeris:**
- MK2 (Makemake) ✗

### The Solution: Analytical Fallback

For satellites without JPL data, we calculate positions analytically using published orbital elements.

**Architecture:**

```
User selects MK2
    ↓
plot_tno_satellite_orbit() called
    ↓
Check osculating cache → Not found
    ↓
Check ANALYTICAL_FALLBACK_SATELLITES list → MK2 is listed
    ↓
Load elements from planetary_params
    ↓
Calculate orbit path (Keplerian)
    ↓
For animation: Calculate position at each frame date
```

### Implementation Details

**File:** `idealized_orbits.py`

```python
# Check for analytical fallback (satellites without JPL ephemeris)
# ═══════════════════════════════════════════════════════════════════
# IMPORTANT: This solution is tailored specifically for MK2:
#   1. Assumes circular orbit (e=0): mean anomaly = true anomaly
#   2. Uses J2000.0 as reference epoch with M₀=0° (arbitrary phase)
#   3. Orbital elements from arXiv:2509.05880 (Sept 2025)
#
# For other objects, you may need to:
#   - Solve Kepler's equation for eccentric anomaly (if e > 0)
#   - Use object-specific reference epoch and M₀
#   - Apply different coordinate transformations
# ═══════════════════════════════════════════════════════════════════
ANALYTICAL_FALLBACK_SATELLITES = ['MK2']  # Expandable - see notes above
```

**File:** `palomas_orrery.py` (animation section)

```python
# Same fallback pattern for animation positions
ANALYTICAL_ANIMATION_FALLBACK = ['MK2']

# When fetch_trajectory returns empty, calculate analytically
if obj['name'] in ANALYTICAL_ANIMATION_FALLBACK:
    traj = positions_over_time.get(obj['name'])
    if not traj or all(p is None for p in traj):
        # Calculate positions using orbital elements...
```

**File:** `orbital_elements.py`

```python
'MK2': {
    'a': 0.0001487,        # semi-major axis in AU (22,250 km ± 780 km)
    'e': 0.0,              # eccentricity (best fit is circular)
    'i': 74.0,             # inclination to ecliptic in degrees (63°-87° range)
    'omega': 0.0,          # argument of periapsis (undefined for circular)
    'Omega': 0.0,          # longitude of ascending node (unknown)
    'orbital_period_days': 18.023,  # ± 0.017 days
    # Source: arXiv:2509.05880 (Sept 2025) - preliminary Hubble analysis
},
```

### Position Calculation (Circular Orbit)

For MK2's circular orbit, the math simplifies significantly:

```python
# Mean motion (degrees per day)
n = 360.0 / orbital_period  # = 19.97°/day for MK2

# Mean anomaly at date (for circular orbit = true anomaly)
M = (n * days_since_J2000) % 360.0

# Position in orbital plane (circular: r = a always)
x_orb = a * cos(M)
y_orb = a * sin(M)

# Apply 3D rotations: ω → i → Ω
# (Standard Keplerian to ecliptic transformation)
```

### Velocity Calculation

For circular orbits, velocity magnitude is constant:

```python
# v = 2πa / P
v_au_day = 2 * π * a / orbital_period

# For MK2:
# v = 2π × 0.0001487 AU / 18.023 days
# v ≈ 0.0000518 AU/day
# v ≈ 323 km/hr ≈ 0.090 km/sec
```

### Hover Text Differentiation

The system clearly indicates when analytical (not JPL) data is used:

**Osculating orbit (JPL data):**
```
MK2 Osculating Orbit
Epoch: 2025-12-08
Orbital Elements (JPL):
...
Osculating orbit from JPL Horizons
satellite ephemeris solution
```

**Analytical orbit (no JPL data):**
```
MK2 Analytical Orbit
Source: Analytical (2025 preliminary)
Orbital Elements:
...
No JPL ephemeris available.
Based on arXiv:2509.05880 (Sept 2025)
preliminary Hubble orbital solution.
Inclination uncertain (63°-87° range).
```

### Limitations and Caveats

**What we know:**
- Orbital shape (circular, a = 22,250 km)
- Orbital period (18.023 days)
- Approximate inclination to ecliptic (~74°, uncertain)

**What we don't know:**
- Exact inclination (63°-87° range)
- Longitude of ascending node (Ω)
- Current orbital phase (where MK2 is in its orbit right now)

**Animation caveat:**
The animated position assumes M₀ = 0° at J2000.0 epoch. This is arbitrary - we don't actually know where MK2 was at any specific time. The animation shows correct orbital motion (period, velocity) but arbitrary phase.

### Expanding to Other Objects

To add another satellite without JPL ephemeris:

1. **Add to fallback lists** (both files):
   ```python
   ANALYTICAL_FALLBACK_SATELLITES = ['MK2', 'NewMoon']
   ANALYTICAL_ANIMATION_FALLBACK = ['MK2', 'NewMoon']
   ```

2. **Add orbital elements** to `orbital_elements.py`

3. **Consider special cases:**
   - If e > 0: Need Kepler's equation solver
   - If specific epoch known: Use that instead of J2000
   - If M₀ known: Use actual starting phase

### Why This Matters

Without this fallback system, MK2 would simply not appear in the visualization - users would see Makemake alone with no indication it has a moon. The analytical fallback:

- Shows MK2 exists and orbits Makemake
- Displays best-available orbital parameters
- Animates with correct period and velocity
- Clearly indicates data source and limitations
- Provides educational value about this distant moon
```

---

## 4. UPDATE VERSION HISTORY (Line 730)

**Add after line 730:**

```markdown
- **v1.4.1** (Dec 7, 2025): Barycenter reference frame fix - osculating elements now fetched relative to viewing center (@9 barycenter vs @999 body center), center-body aware caching with keys like "Charon@9", view-aware pre-fetch logic
- **v1.5** (Dec 8, 2025): MK2 analytical orbit fallback for satellites without JPL ephemeris, circular orbit position/velocity calculations, animation support for analytical orbits, clear hover text differentiation between osculating and analytical sources
```

---

## 4a. ADD NEW SECTION TO PART II: Barycenter Reference Frame Fix (After Section 10)

### Insert new section:

```markdown
---

## 10a. Barycenter Reference Frame Fix 🆕

### The Problem (Dec 7, 2025)

Osculating orbits should "kiss" (osculate) the actual trajectory at the epoch date - that's literally what "osculating" means. But in Pluto-Charon barycenter view, the orbits weren't touching!

**Symptom:**
- Pluto-centered view: Osculating orbits aligned perfectly ✓
- Barycenter-centered view: Orbits offset from actual positions ✗

### Root Cause: Reference Frame Mismatch

The osculating elements were being fetched relative to **Pluto's body center** (@999 in JPL Horizons), but the actual trajectories were plotted relative to the **Pluto-Charon barycenter** (@9).

```
Osculating elements: fetched @999 (Pluto body center)
Actual trajectory:   fetched @9   (Pluto-Charon barycenter)
Result:              Mismatch! Orbits don't kiss.
```

**The key insight:** Orbital elements depend on what you're orbiting around. Charon's orbit around Pluto's center is different from Charon's orbit around the system barycenter!

### The Solution: Center-Body Aware Caching

**Step 1: Track which center was used**

```python
def get_cache_key(object_name, center_body=None):
    """Generate cache key that includes center body if specified."""
    if center_body and center_body not in [None, 'Sun', '@sun', '10']:
        return f"{object_name}@{center_body}"
    return object_name

# Examples:
# get_cache_key('Charon', '9')      → "Charon@9"
# get_cache_key('Charon', '999')    → "Charon@999"  
# get_cache_key('Charon', None)     → "Charon"
```

**Step 2: Store center_body in cache metadata**

```python
cache[cache_key] = {
    'elements': { ... },
    'epoch': '2025-12-07',
    'center_body': '9',  # NEW: Track which center was used
    'timestamp': ...
}
```

**Step 3: Fetch with correct center for current view**

```python
# In pre-fetch logic:
if center_object_name == 'Pluto-Charon Barycenter':
    center_override = '9'  # Barycenter
else:
    center_override = None  # Default (heliocentric or body-relative)

elements = get_elements_with_prompt(
    obj_name,
    center_body=center_override,  # NEW parameter
    ...
)
```

### Files Modified

| File | Changes |
|------|---------|
| `orbit_data_manager.py` | Added `center_body` parameter to element fetching |
| `osculating_cache_manager.py` | Added `get_cache_key()`, store `center_body` in cache |
| `palomas_orrery.py` | View-aware pre-fetch with center override |
| `idealized_orbits.py` | Use correct cache keys based on viewing center |

### The Result

```
Console output (barycenter view):
  [PRE-FETCH] Using center override: 9 (barycenter mode)
  [CACHE] Key: Pluto@9
  [CACHE] Key: Charon@9
  ✓ Osculating orbits now kiss actual trajectories!
```

### Why This Matters

**Before fix:** Users in barycenter view saw osculating orbits that appeared "wrong" - not touching the actual positions. This undermined confidence in the visualization's accuracy.

**After fix:** The osculating orbit passes exactly through the object's current position at epoch, demonstrating true osculation. The visualization is now scientifically accurate in all viewing modes.

### For Paloma

*"When we look at the Pluto-Charon dance from different places, we have to do the math from that same place! If we're watching from the middle (the barycenter), we need to calculate the orbits from the middle too. Otherwise it's like trying to trace someone's path while standing in the wrong spot - the lines won't match up!"*
```

---

## 5. UPDATE QUOTATIONS (After line 735)

**Add:**

```markdown
*"Osculating means kissing - if the orbits don't touch, they're not osculating!"* - Dec 7, 2025
*"No JPL ephemeris? No problem - calculate it yourself!"* - Dec 8, 2025
```

---

## 6. REPLACE "What's New" SECTION (Lines 739-805)

**Replace entire section with:**

```markdown
---

## What's New in v1.4.1 (December 7, 2025) 🆕

### The Osculating Fix

**Problem:** Osculating orbits didn't "kiss" actual trajectories in barycenter view.

**Cause:** Reference frame mismatch - elements fetched @999 (Pluto), trajectories plotted @9 (barycenter).

**Solution:** Center-body aware caching with keys like "Charon@9".

```python
# Before: Same cache key regardless of viewing center
cache_key = "Charon"  # Ambiguous!

# After: Cache key includes center body
cache_key = get_cache_key("Charon", center_body="9")  # → "Charon@9"
```

**Result:** Osculating orbits now properly osculate in all viewing modes!

---

## What's New in v1.5 (December 8, 2025) 🆕

### Major Features Added

1. **MK2 Analytical Orbit Fallback**
   - Visualizes MK2's orbit using 2025 Hubble orbital solution
   - No JPL ephemeris required - calculates from orbital elements
   - Full animation support with correct 18.023-day period
   - Velocity display (~323 km/hr)

2. **Expandable Fallback Architecture**
   - `ANALYTICAL_FALLBACK_SATELLITES` list in idealized_orbits.py
   - `ANALYTICAL_ANIMATION_FALLBACK` list in palomas_orrery.py
   - Documented requirements for adding future objects

3. **Circular Orbit Optimizations**
   - Simplified math when e = 0 (mean anomaly = true anomaly)
   - No Kepler's equation needed
   - Constant velocity calculation: v = 2πa/P

4. **Clear Data Source Attribution**
   - "Analytical Orbit" vs "Osculating Orbit" in legend
   - Hover text indicates arXiv source and limitations
   - Animation position caveat (assumed phase)

### The Problem We Solved

```
Before v1.5:
  User selects MK2 → fetch_trajectory() → JPL returns nothing → MK2 invisible

After v1.5:
  User selects MK2 → fetch_trajectory() → JPL returns nothing → 
  Fallback triggered → Analytical calculation → MK2 visible and animated!
```

### Orbital Elements (2025 Hubble Analysis)

| Parameter | Value | Source |
|-----------|-------|--------|
| Semi-major axis | 22,250 km (0.0001487 AU) | arXiv:2509.05880 |
| Orbital period | 18.023 days | arXiv:2509.05880 |
| Eccentricity | 0.0 (circular) | arXiv:2509.05880 |
| Inclination | ~74° (63°-87° range) | Estimated |
| Velocity | 323 km/hr | Calculated |

### Code Highlights

**The Fallback Check:**
```python
if satellite_name in ANALYTICAL_FALLBACK_SATELLITES:
    print(f"  ⚠ No JPL ephemeris for {satellite_name}, using analytical elements")
    elements = planetary_params[satellite_name]
    orbit_source = "analytical"
```

**Circular Orbit Velocity:**
```python
# v = 2πa / P (constant for circular orbit)
v_au_day = 2 * np.pi * a / orbital_period
```

**Animation Position:**
```python
# Mean anomaly = true anomaly for circular orbit
M = (n * days_since_J2000) % 360.0
true_anomaly = np.radians(M)
```

### Educational Highlights

**For Paloma:**
*"MK2 is so new and far away that the scientists who track space objects haven't figured out exactly where it will be yet. But we know how big its orbit is and how long it takes to go around, so we can draw its path and watch it move - we just had to do the math ourselves instead of asking the computer!"*

**Key Insight:**
Sometimes the best available data isn't in official databases. The 2025 Hubble analysis provides orbital elements that won't appear in JPL Horizons for years. By implementing analytical fallbacks, we can visualize cutting-edge science.

### Lessons Learned

1. **Circular orbits simplify everything** - No Kepler's equation, constant velocity
2. **Fallback lists should be explicit** - Named list, not automatic detection
3. **Document assumptions clearly** - J2000 epoch, M₀=0° are arbitrary
4. **Velocity needs its own field** - Hover text expects `'velocity'`, not `'vx'/'vy'/'vz'`
5. **Edge-on orbits are special** - MK2's geometry explains discovery difficulty

### Files Modified

| File | Changes |
|------|---------|
| `orbital_elements.py` | Updated MK2 parameters (a, P, source comments) |
| `idealized_orbits.py` | Analytical fallback in plot_tno_satellite_orbit() |
| `palomas_orrery.py` | Animation fallback with velocity calculation |
| `constants_new.py` | Updated MK2 description |

---

**Total additions:** ~150 lines of code, ~200 lines of documentation  
**Focus areas:** Analytical orbit calculation, animation fallback, circular orbit physics  
**Educational value:** Visualizes moon that JPL can't yet track  
**Quotable:** *"No JPL ephemeris? No problem - calculate it yourself!"*

---
```

---

## Summary of Changes

| Section | Action |
|---------|--------|
| Header | Update to v1.5, Dec 8, 2025 |
| Part I, Section 6 | Add "MK2: The Moon Without an Ephemeris" subsection |
| Part II, Section 10a | Add "Barycenter Reference Frame Fix" (Dec 7 work) |
| Part II, Section 13 | Add "Analytical Orbit Fallback System" |
| Version History | Add v1.4.1 and v1.5 entries |
| Quotations | Add two new quotables |
| What's New | Add both v1.4.1 and v1.5 sections |

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 8, 2025*
