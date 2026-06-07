# Pluto-Charon Binary System Implementation

**Date:** November 25, 2025 (Updated)  
**Status:** Mode 2 WORKING ✅ | Mode 3 In Progress 🔄  
**Approach:** Barycenter-centered binary planet system (like TOI-1338)  
**Pattern:** Osculating-only orbits (like Saturn)

---

## Progress Summary

### ✅ COMPLETED

| Feature | Status | Notes |
|---------|--------|-------|
| Mode 1: Sun-centered | ✅ Working | Pluto orbits Sun normally (automatic) |
| Mode 2: Pluto-centered | ✅ Working | All 5 moons with osculating + actual orbits |
| Barycenter marker | ✅ Working | Shows barycenter location in Pluto-centered view |
| Barycenter hover text | ✅ Working | Explains binary system, compares to Earth-Moon |
| Osculating orbit divergence | ✅ Working | Shows perturbation effects visually |
| Analytical orbit removal | ✅ Fixed | Removed unwanted analytical orbits for Pluto moons |
| Apsidal hover text | 🔄 Needs fix | "No significant perturbations" text is misleading |

### 🔄 IN PROGRESS

| Feature | Status | Blocker |
|---------|--------|---------|
| Mode 3: Barycenter-centered | 🔄 Blocked | Three bugs identified (see below) |
| Perturbation hover text | 🔄 Ready | Fix identified in apsidal_markers.py |

---

## Bug Fixes Applied This Session

### Fix 1: Removed Analytical Orbits for Pluto Moons

**Problem:** Pluto moons (Styx, Nix, Kerberos, Hydra) were getting both osculating AND analytical orbits due to incorrect if/else structure.

**Root cause:** The barycenter marker `if` block was placed outside the `elif` block, causing the `else` to pair incorrectly.

**File:** `idealized_orbits.py` lines 3077-3112

**Fix applied:** Moved barycenter marker check inside the `elif moon_name in PLUTO_MOONS` block.

### Fix 2: Added Barycenter Marker to Pluto-Centered View

**Feature:** White diamond marker shows barycenter location between Pluto and Charon.

**Educational value:**
- Shows barycenter is OUTSIDE Pluto (~2,050 km from center, ~860 km from surface)
- Compares to Earth-Moon system (barycenter inside Earth)
- Explains why Pluto-Charon is a "true binary"

**File:** `idealized_orbits.py` - added `add_pluto_barycenter_marker()` function

---

## Bug Fixes Pending

### Fix 3: Misleading "Orbit Stability Note" Hover Text

**Problem:** When angular deviation is low (< 0.5°), apsidal markers show:
```
Orbit Stability Note:
Actual position matches ideal Keplerian orbit.
No significant perturbations detected.
```

**Why this is wrong:** Osculating elements match reality BY DEFINITION at epoch. Low deviation doesn't mean "stable" or "no perturbations" - it means the measurement point is near the epoch!

**File:** `apsidal_markers.py` lines 183-193

**Fix:** Replace "Orbit Stability Note" with consistent "Perturbation Analysis" that explains why deviation is low near epoch.

---

## Mode 3: Barycenter-Centered View

### Concept

**When "Pluto-Charon Barycenter" is selected as center:**
- Barycenter is stationary (at origin)
- **Pluto orbits the barycenter** (tight orbit, ~2,050 km radius)
- **Charon orbits the barycenter** (larger orbit, ~17,550 km radius)
- **Other moons orbit the barycenter** (wider orbits)

**Yes, Pluto becomes a "satellite" of the barycenter!** This is physically correct - both bodies orbit their common center of mass.

### JPL Horizons Query Pattern

```
Center: @9 (Pluto system barycenter)
Objects:
  - 999 (Pluto body) → orbits @9
  - 901 (Charon) → orbits @9
  - 902 (Nix) → orbits @9
  - 903 (Hydra) → orbits @9
  - 904 (Kerberos) → orbits @9
  - 905 (Styx) → orbits @9
```

### Three Blocking Bugs (From Previous Session)

**Bug 1: Missing parent_planets Entry (CRITICAL)**
- File: `orbital_elements.py` line 1236
- Problem: `parent_planets` has `'Pluto'` but NOT `'Pluto-Charon Barycenter'`
- Impact: `moons = parent_planets.get(center_id, [])` returns empty list
- Fix: Add `'Pluto-Charon Barycenter': ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']`

**Bug 2: center_id Defaulting to 'Sun'**
- File: `orbit_data_manager.py` line 1071
- Problem: If barycenter not in `object_list`, defaults to 'Sun'
- Evidence: Console shows "Fetching...relative to Sun" instead of "@9"
- Fix: Pass explicit center_id to `update_orbit_paths_incrementally()`

**Bug 3: Scale Mismatch**
- File: `palomas_orrery.py` line 548
- Problem: Uses Pluto's solar orbit (a=39.48 AU) for scaling instead of barycentric distances
- Evidence: Plot shows ±59 AU scale instead of ±0.0005 AU
- Fix: Add special case for 'Pluto-Charon Barycenter' center with fixed range

### Implementation Order

1. **Fix Bug 1** (parent_planets) → enables satellite loop to find objects
2. **Fix Bug 2** (center_id) → ensures orbits fetched relative to @9
3. **Fix Bug 3** (scaling) → makes orbits visible at correct scale

---

## Comparison: TOI-1338 vs Pluto System

| Aspect | TOI-1338 A/B | Pluto-Charon |
|--------|--------------|--------------|
| System type | Binary star | Binary dwarf planet |
| Barycenter location | Between stars | Outside Pluto surface |
| Primary orbit size | Very small (stars ~at barycenter) | Small (~2,050 km) |
| Secondary orbit size | Very small | Larger (~17,550 km) |
| Visual representation | Stars shown as shells at center | Both should show visible orbits |
| Companions | Planets (b, c) orbit wide | Small moons orbit wide |

**Key difference:** TOI-1338 stars have tiny orbits relative to planet distances (shown as shells). Pluto-Charon have VISIBLE orbits around barycenter - we should show the "dance"!

---

## The Binary Planet Discovery

**Charon is NOT just a moon - Pluto-Charon is a binary planet system!**

| Property | Earth-Moon | Pluto-Charon |
|----------|------------|--------------|
| Mass ratio | Moon/Earth = 0.0123 (1.2%) | Charon/Pluto = 0.117 (11.7%) |
| Barycenter location | 1,700 km from Earth center (**inside Earth**) | 2,050 km from Pluto center (**outside Pluto!**) |
| System type | Planet with large moon | **Binary planet** |

**This is THE defining characteristic of the Pluto system - Mode 3 will show it!**

---

## Why Osculating-Only for Pluto

**Pluto pole orientation:**
- RA: 132.99° (vs ecliptic pole ~270°)
- Angular separation: ~137° from ecliptic pole
- **Conclusion:** Even worse than Saturn - analytical transformations will fail

**Additional complexity:**
- Extreme axial tilt: 122.53° (retrograde rotation like Uranus)
- Binary planet system (Charon is 1/8 Pluto's mass)
- All moons co-planar in Pluto's equator

**Solution:** Skip analytical orbits, use osculating only (like Saturn)

---

## Pluto's Five Moons

| Moon | Horizons ID | Size | Period (days) | a (AU) | Notes |
|------|-------------|------|---------------|--------|-------|
| Charon | 901 | ~1,212 km | 6.387 | 0.000131 | Binary partner, tidally locked |
| Styx | 905 | ~10-25 km | 20.16 | 0.000289 | Tiny, irregular |
| Nix | 902 | ~40 km | 24.86 | 0.000330 | Elongated |
| Kerberos | 904 | ~12-30 km | 32.17 | 0.000390 | Dark surface |
| Hydra | 903 | ~55 km | 38.20 | 0.000436 | Most distant |

**All discovered/refined by Hubble and New Horizons (2015 flyby)**

---

## Three Viewing Modes

### Mode 1: Sun-Centered ✅ WORKING
```
Center: Sun
Pluto: Orbits Sun normally (standard planet)
```
**Already works automatically - no special code needed!**

### Mode 2: Pluto-Centered ✅ WORKING
```
Center: Pluto (stationary)
Objects: Charon, Styx, Nix, Kerberos, Hydra
Bonus: Barycenter marker shows binary nature
```
**Features working:**
- All 5 moons with osculating (dashed) + actual (solid) orbits
- Barycenter diamond marker between Pluto and Charon
- Educational hover text explaining perturbations
- Proper ~0.0006 AU scaling

### Mode 3: Barycenter-Centered 🔄 BLOCKED
```
Center: Pluto-Charon Barycenter (stationary)
Objects: Pluto, Charon, Styx, Nix, Kerberos, Hydra (ALL orbit barycenter)
```
**Blocked by 3 bugs - fixes identified, ready to implement**

---

## Expected Visual: Barycenter Mode

```
              Hydra
             /
   Pluto   ◇   Charon    (both moving around ◇!)
          / \
      Styx   Nix
              \
            Kerberos
    
    ◇ = barycenter (center, stationary)
```

**The "dance":**
- Pluto and Charon orbit OPPOSITE sides of barycenter
- Same period: 6.387 days (synchronized by physics)
- Pluto's orbit: smaller (closer to barycenter, ~0.0000137 AU)
- Charon's orbit: larger (farther from barycenter, ~0.000117 AU)
- Mass ratio determines orbit sizes!

---

## Educational Story Points

### For Paloma (Age 7-8)
- "Pluto and Charon dance around each other!"
- "They both move in circles around a point between them"
- "That point is called the barycenter - it's like a balance point on a seesaw"
- "The barycenter is actually OUTSIDE Pluto - floating in space!"
- "No other planet in our solar system does this special dance"

### For Students/Public
- Binary planet system (barycenter outside Pluto)
- Mass ratio determines orbit size (Charon has larger orbit)
- Tidal locking (both always show same face to each other)
- Unique in our solar system
- New Horizons mission (2015) revealed the details

### For Advanced
- Barycenter calculation: r_Pluto/r_Charon = M_Charon/M_Pluto = 0.117
- Barycenter location: 2,050 km from Pluto center (radius 1,188 km, so ~860 km outside!)
- Both orbits are tidally locked with same 6.387 day period
- Small moons in orbital resonances (Styx, Nix, Kerberos in near 3:4:5:6 with Charon)

---

## Physics Details

### Barycenter Location
```
Mass ratio: m_Charon/m_Pluto = 0.117
Distance ratio: r_Pluto/r_Charon = 0.117

Total separation: ~19,600 km
Pluto's orbit radius from barycenter: ~2,050 km
Charon's orbit radius from barycenter: ~17,550 km
Barycenter: 2,050 km from Pluto's center (OUTSIDE Pluto surface!)
```

### Comparison to Earth-Moon
```
Earth-Moon mass ratio: 0.0123
Earth-Moon barycenter: 4,671 km from Earth's center
Earth's radius: 6,371 km
Result: Barycenter is 1,700 km INSIDE Earth

Pluto-Charon mass ratio: 0.117 (10x larger!)
Pluto-Charon barycenter: 2,050 km from Pluto's center  
Pluto's radius: 1,188 km
Result: Barycenter is 860 km OUTSIDE Pluto
```

---

## Files Modified This Session

| File | Change | Status |
|------|--------|--------|
| `idealized_orbits.py` | Added `add_pluto_barycenter_marker()` | ✅ Done |
| `idealized_orbits.py` | Fixed if/else structure for Pluto moons | ✅ Done |
| `idealized_orbits.py` | Enhanced osculating orbit hover text | ✅ Done |

## Files to Modify (Pending)

| File | Change | Priority |
|------|--------|----------|
| `apsidal_markers.py` | Fix "Orbit Stability Note" text | Medium |
| `orbital_elements.py` | Add 'Pluto-Charon Barycenter' to parent_planets | High (Mode 3) |
| `orbit_data_manager.py` | Pass center_id to update function | High (Mode 3) |
| `palomas_orrery.py` | Add barycenter scaling case | High (Mode 3) |

---

## Next Steps

### Immediate (This Session)
1. [ ] Fix apsidal_markers.py "Orbit Stability Note" → neutral "Perturbation Analysis"

### Mode 3 Implementation
2. [ ] Fix Bug 1: Add parent_planets entry for barycenter
3. [ ] Fix Bug 2: Pass center_id through to orbit fetching
4. [ ] Fix Bug 3: Add barycenter scaling case
5. [ ] Test barycenter-centered view
6. [ ] Add educational hover text for Pluto's orbit around barycenter

### Polish
7. [ ] Verify all hover text is educational and accurate
8. [ ] Test animation mode for "dance" visualization
9. [ ] Update any remaining documentation

---

## Session Notes

### Key Discovery: Osculating ≠ Analytical
The divergence between osculating (dashed) and actual (solid) orbits is **educational gold**:
- "Osculating" means "kissing" - matches at one instant only
- Real orbits deviate due to perturbations (Charon's gravity, resonances)
- Pluto moons have short periods (6-38 days) → perturbations accumulate fast
- The divergence you SEE is the perturbation in action!

### Key Insight: Pluto as "Satellite"
In barycenter mode, Pluto itself becomes an orbiting object:
- Query: Object 999 (Pluto body) relative to center @9 (barycenter)
- JPL Horizons returns Pluto's osculating elements around the barycenter
- Same code path as other moons - just add 'Pluto' to the orbiters list
- **Conceptually correct:** Both bodies orbit their common center of mass

---

*"Pluto and Charon dance around each other - watch them orbit together!"*

*"The barycenter is outside Pluto - that's what makes it a binary planet system!"*

*"In barycenter mode, even Pluto is just another object orbiting the center of mass!"*
