# UPDATED HANDOFF: Satellite Actual Apsidal Markers

**Date:** November 22, 2025  
**Token Budget:** ~98,500 / 190,000 (52%)  
**Status:** 🔴 Bug identified + 2 fixes needed

---

## Current Status

### What Works ✅
- Satellite analytical orbits (dotted lines)
- Satellite osculating orbits (dashed lines) 
- Satellite actual orbits (solid lines)
- Satellite ideal apsidal markers (open squares)
- **Planet actual apsidal markers work!** (Mercury tested)

### What Doesn't Work ❌
- **Satellite actual apsidal markers** (filled squares)
  - Moon: "No positions fetched"
  - Phobos: "No positions fetched"
  - Deimos: "No positions fetched"

---

## TWO FIXES NEEDED

### FIX #1: Key Name Mismatch (2 minutes) 🔴 URGENT

**Problem:** Satellite code sets `perihelion_dates` but fetch function looks for `perigee_dates`

**File:** `apsidal_markers.py`  
**Line:** ~764  

**Change from:**
```python
if is_satellite:
    all_dates = params.get('perigee_dates', []) + params.get('apogee_dates', [])
else:
    all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])
```

**Change to:**
```python
# Use perihelion/aphelion keys for all objects
all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])
```

**See:** [URGENT_BUG_FIX.md](computer:///mnt/user-data/outputs/URGENT_BUG_FIX.md)

---

### FIX #2: Add Satellite Marker Code (5 minutes)

**File:** `idealized_orbits.py`  
**Line:** After 2323 (`plotted.append(moon_name)`)  

**Code:** See [ADD_AFTER_LINE_2323.py](computer:///mnt/user-data/outputs/ADD_AFTER_LINE_2323.py)

**Note:** We already identified this fix in previous session

---

## Implementation Order

### Do Fix #1 FIRST (the bug fix)
1. Open `apsidal_markers.py`
2. Find line ~764
3. Change `perigee_dates` → `perihelion_dates`
4. Change `apogee_dates` → `aphelion_dates`
5. Save

### Then Do Fix #2 (add the satellite code)
1. Open `idealized_orbits.py`
2. Find line 2323 (`plotted.append(moon_name)`)
3. Add code after line 2323
4. Save

### Then Test
1. Mercury (should still work)
2. Moon (should now work)
3. Phobos (should now work)
4. Deimos (should now work)

---

## Expected Results After BOTH Fixes

**Console:**
```
[ACTUAL APSIDAL] Checking satellites for apsidal markers...

[ACTUAL APSIDAL] Processing Moon
  Object ID: 301
  Center: Earth
    Fetched position for 2025-12-03 11:26:27
  Fetched 1 positions
  ✓ Added actual apsidal markers for Moon

[ACTUAL APSIDAL] Processing Phobos
  Object ID: 401
  Center: Mars
    Fetched position for 2025-11-23 01:36:12
  Fetched 1 positions
  ✓ Added actual apsidal markers for Phobos
```

**Visualization:**
- Filled squares on solid orbit lines
- "Fear falling into War" visible! 🔴

---

## Time Estimate

- Fix #1 (bug fix): 2 minutes
- Fix #2 (add code): 5 minutes
- Testing: 5 minutes
- **Total: ~12 minutes**

---

## Files Reference

**Bug Fix:**
- [URGENT_BUG_FIX.md](computer:///mnt/user-data/outputs/URGENT_BUG_FIX.md) - Detailed explanation

**Implementation:**
- [ADD_AFTER_LINE_2323.py](computer:///mnt/user-data/outputs/ADD_AFTER_LINE_2323.py) - Code to add
- [CORRECTED_PLACEMENT.md](computer:///mnt/user-data/outputs/CORRECTED_PLACEMENT.md) - Placement details

**Understanding:**
- [TONY_WAS_RIGHT.md](computer:///mnt/user-data/outputs/TONY_WAS_RIGHT.md) - Why this approach
- [FINAL_IMPLEMENTATION_SUMMARY.md](computer:///mnt/user-data/outputs/FINAL_IMPLEMENTATION_SUMMARY.md) - Overview

---

## What We Learned

### Your Testing Revealed
1. ✅ Line 2323 is correct (not 1805)
2. ✅ No obsolete code to remove
3. ✅ Mercury works (planets are fine)
4. 🔴 Satellites don't work (key mismatch bug)

### The Bug
- Satellite code sets `perihelion_dates`
- Fetch function looks for `perigee_dates`
- **Simple mismatch!**

### The Fix
- Use same keys for everything
- Simpler, cleaner, works!

---

## Bottom Line

**TWO simple fixes:**
1. Change key names in apsidal_markers.py (line ~764)
2. Add satellite marker code in idealized_orbits.py (after line 2323)

**Total time: ~12 minutes**

**Result: "Fear falling into War" becomes visible!** 🔴

---

*"When unsure, ask." - You asked!*  
*"Discovery over delivery." - We found the bug!*  
*"Test first." - Your testing revealed the issue!*

**Ready to implement both fixes!** 🎯

---

**Token Budget:** ~98,500 / 190,000 (52% used)
