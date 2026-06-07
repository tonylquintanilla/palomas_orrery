# Pluto-Charon Binary System Implementation

**Date:** November 25, 2025 (Final Update)  
**Status:** Mode 2 COMPLETE ✅ | Mode 3 Ready to Implement 🔄  
**Approach:** Barycenter-centered binary planet system (like TOI-1338)  
**Pattern:** Osculating-only orbits (like Saturn)

---

## Progress Summary

### ✅ COMPLETED (This Session)

| Feature | Status | Notes |
|---------|--------|-------|
| Mode 1: Sun-centered | ✅ Working | Pluto orbits Sun normally (automatic) |
| Mode 2: Pluto-centered | ✅ Working | All 5 moons with osculating + actual orbits |
| Barycenter marker | ✅ Working | Shows barycenter location in Pluto-centered view |
| Barycenter hover text | ✅ Working | Explains binary system, compares to Earth-Moon |
| Osculating orbit divergence | ✅ Working | Shows perturbation effects visually |
| Analytical orbit removal | ✅ Fixed | Removed unwanted analytical orbits for Pluto moons |
| "Actual" → "Keplerian" labels | ✅ Fixed | Periapsis markers now correctly labeled |
| "Orbit Stability Note" fix | ✅ Fixed | Now shows consistent "Perturbation Analysis" |

### 🔄 READY FOR NEXT SESSION

| Feature | Status | Blocker |
|---------|--------|---------|
| Mode 3: Barycenter-centered | 🔄 Ready | Three bugs identified, fixes documented |

---

## Bug Fixes Applied This Session

### Fix 1: Removed Analytical Orbits for Pluto Moons
**File:** `idealized_orbits.py` lines 3077-3112  
**Problem:** Pluto moons getting both osculating AND analytical orbits  
**Fix:** Moved barycenter marker check inside the `elif moon_name in PLUTO_MOONS` block

### Fix 2: Added Barycenter Marker to Pluto-Centered View
**File:** `idealized_orbits.py` - added `add_pluto_barycenter_marker()` function  
**Feature:** White diamond marker shows barycenter location between Pluto and Charon with educational hover text

### Fix 3: "Actual" → "Keplerian" Periapsis Labels
**File:** `apsidal_markers.py` line 234  
**Change:** `near_label = f"Actual {near_term}{epoch_suffix}"` → `near_label = f"Keplerian {near_term}{epoch_suffix}"`  
**Result:** "Styx Keplerian Perihelion (Epoch: 2025-11-25 osc.)"

### Fix 4: "Orbit Stability Note" → Consistent "Perturbation Analysis"
**File:** `apsidal_markers.py` lines 183-193  
**Problem:** Low deviation showed misleading "No significant perturbations detected"  
**Fix:** Now shows "Perturbation Analysis" with explanation that low deviation is expected near epoch

---

## Mode 3: Barycenter-Centered View (Next Session)

### Three Blocking Bugs

**Bug 1: Missing parent_planets Entry (CRITICAL)**
- **File:** `orbital_elements.py` line 1236
- **Problem:** `parent_planets` has `'Pluto'` but NOT `'Pluto-Charon Barycenter'`
- **Impact:** `moons = parent_planets.get(center_id, [])` returns empty list → nothing plots
- **Fix:** Add entry:
```python
'Pluto-Charon Barycenter': ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
```

**Bug 2: center_id Defaulting to 'Sun'**
- **File:** `orbit_data_manager.py` line 1071
- **Problem:** If barycenter not in `object_list`, defaults to 'Sun'
- **Evidence:** Console shows "Fetching...relative to Sun" instead of "@9"
- **Fix:** Pass explicit center_id to `update_orbit_paths_incrementally()`

**Bug 3: Scale Mismatch**
- **File:** `palomas_orrery.py` line 548
- **Problem:** Uses Pluto's solar orbit (a=39.48 AU) for scaling
- **Evidence:** Plot shows ±59 AU scale instead of ±0.0005 AU
- **Fix:** Add special case for 'Pluto-Charon Barycenter' center:
```python
if center_id == 'Pluto-Charon Barycenter':
    return 0.00075  # Fixed range for barycentric system (~0.0005 AU * 1.5 buffer)
```

### Implementation Order
1. **Fix Bug 1** (parent_planets) → enables satellite loop to find objects
2. **Fix Bug 2** (center_id) → ensures orbits fetched relative to @9
3. **Fix Bug 3** (scaling) → makes orbits visible at correct scale

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

### Key Insight: Pluto as "Satellite"
In barycenter mode, Pluto itself becomes an orbiting object - same code path as moons, just query object 999 relative to center @9.

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
- Same period: 6.387 days (synchronized)
- Pluto's orbit: ~0.0000137 AU (smaller, closer to barycenter)
- Charon's orbit: ~0.000117 AU (larger, farther from barycenter)

---

## The Binary Planet Discovery

| Property | Earth-Moon | Pluto-Charon |
|----------|------------|--------------|
| Mass ratio | 0.0123 (1.2%) | 0.117 (11.7%) |
| Barycenter | 1,700 km from Earth center (**inside**) | 2,050 km from Pluto center (**outside!**) |
| System type | Planet with moon | **Binary planet** |

---

## Pluto's Five Moons

| Moon | ID | Period (days) | a (AU) |
|------|----|---------------|--------|
| Charon | 901 | 6.387 | 0.000131 |
| Styx | 905 | 20.16 | 0.000289 |
| Nix | 902 | 24.86 | 0.000330 |
| Kerberos | 904 | 32.17 | 0.000390 |
| Hydra | 903 | 38.20 | 0.000436 |

---

## Files Modified This Session

| File | Change |
|------|--------|
| `idealized_orbits.py` | Added `add_pluto_barycenter_marker()`, fixed if/else structure |
| `apsidal_markers.py` | Line 234: "Actual" → "Keplerian", Lines 183-193: Stability Note fix |

## Files to Modify (Next Session)

| File | Change | Priority |
|------|--------|----------|
| `orbital_elements.py` | Add 'Pluto-Charon Barycenter' to parent_planets | High |
| `orbit_data_manager.py` | Pass center_id to update function | High |
| `palomas_orrery.py` | Add barycenter scaling case | High |
| `idealized_orbits.py` | Animate barycenter marker (see Bug 4) | Medium |

---

## Bug 4: Barycenter Marker is Static in Animation

**Problem:** In Pluto-centered animation, Charon moves but the barycenter marker stays fixed at its initial position.

**Expected behavior:**
- **Pluto-centered:** Barycenter traces small circle around Pluto (like Sun orbiting Earth in geocentric view)
- **Barycenter-centered:** Pluto traces small orbit, Charon traces larger orbit (the "dance")

**Physics:** Barycenter is ALWAYS on the Pluto-Charon line at ratio:
```
barycenter_pos = charon_pos × (M_charon / (M_pluto + M_charon))
barycenter_pos = charon_pos × 0.117
```

**Fix options:**
1. Calculate barycenter from Charon's animated position at each frame
2. Add barycenter to animation position tracking as a "virtual satellite"
3. Fetch barycenter positions from JPL (if available)

**Recommended:** Option 1 - derive from Charon position (simplest, always accurate)

---

## Session Notes

### Educational Discoveries
1. **Osculating ≠ Actual:** Divergence between dashed (osculating) and solid (actual) orbits shows perturbations in action
2. **"Keplerian" labeling:** Periapsis markers from osculating TP are Keplerian predictions, not actual positions
3. **Low deviation near epoch is expected:** Osculating elements match reality BY DEFINITION at epoch

### Terminology Clarifications
- **"Closest Plotted Point"** = from actual trajectory data (correctly named)
- **"Keplerian Periapsis"** = calculated from osculating TP (now correctly named)
- **Periapsis** (generic) vs **Perihelion** (Sun-centered) - code handles automatically

---

*"Pluto and Charon dance around each other - watch them orbit together!"*

*"The barycenter is outside Pluto - that's what makes it a binary planet system!"*
