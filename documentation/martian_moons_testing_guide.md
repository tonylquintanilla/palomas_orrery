# Martian Moons Testing Guide

**Date:** November 20, 2025  
**Status:** Ready to test Phobos and Deimos  
**Previous:** Moon testing complete ✅

---

## Why Test Martian Moons?

**Phobos is one of the most perturbed objects in the solar system:**
- **Extremely close** to Mars: 9,376 km (only 1.4× Mars radii!)
- **Very rapid orbit:** 7.65 hours (3.1 orbits per day)
- **Strong perturbations:**
  - Mars' oblateness (J2 coefficient)
  - Tidal forces (Phobos is spiraling inward!)
  - Solar gravity
  - Fast orbital precession

**Deimos for comparison:**
- More distant: 23,458 km from Mars
- Slower orbit: 30.3 hours
- Less perturbed but still interesting

---

## What We Learned from Moon

**Moon Results (Nov 20, 2025):**
- ✅ Osculating orbit perfectly matches at epoch
- ✅ Diverges after ~2 weeks due to perturbations
- ✅ No coordinate system issues
- ✅ Educational: Shows "kissing" behavior

**Key Insight:**
Osculating elements are **snapshot orbits** - valid for hours/days, then perturbations accumulate.

---

## Testing Predictions

### Phobos Predictions:
- **Faster divergence** than Moon (closer + more perturbed)
- May show visible divergence in **days** instead of weeks
- Perfect test of osculating elements for highly perturbed systems
- Will validate refresh interval decisions

### Deimos Predictions:
- **Similar divergence** to Moon
- More stable due to greater distance
- Should show ~2 week validity window

---

## Testing Process

### 1. Fetch Fresh Elements
```python
# System should auto-fetch for Phobos and Deimos
# Check osculating_cache.json for:
# - "Phobos" entry with epoch date
# - "Deimos" entry with epoch date
```

### 2. Verify Horizons IDs
```
Phobos: ID = 401 (majorbody)
Deimos: ID = 402 (majorbody)
Location: @499 (Mars)
```

### 3. Plot and Compare
**For each moon:**
- Plot actual orbit (JPL vectors) - ground truth
- Plot osculating orbit (ideal orbit with hover text)
- Compare alignment at epoch
- Observe divergence over time

### 4. Document Findings
**Record for each:**
- Does osculating match at epoch?
- How long until visible divergence?
- Faster/slower than Moon?
- Any coordinate issues?

---

## What to Look For

### Good Signs ✅
- Osculating orbit "kisses" actual position at epoch
- Divergence clearly from perturbations (not rotation/coordinate issues)
- Hover text explains behavior
- Legend shows orbit source and epoch

### Potential Issues ⚠️
- Osculating doesn't match at epoch (ID/coordinate problem)
- Orbit rotated wrong (coordinate system issue)
- Diverges **immediately** (elements invalid)

---

## Expected Console Output

```
[PRE-FETCH] Checking osculating elements for 2 objects...
[DEBUG] Processing Phobos...
[DEBUG] Using Horizons ID: 401 (type: majorbody)
⟳ Fetching osculating elements for Phobos from JPL Horizons...
  [Horizons Query] ID: 401 | Type: majorbody | Location: @499 | Date: 2025-11-20
✓ Fetched elements (solution date: 2025-11-20)
✓ Saved: osculating_cache.json

[DEBUG] Processing Deimos...
[DEBUG] Using Horizons ID: 402 (type: majorbody)
⟳ Fetching osculating elements for Deimos from JPL Horizons...
  [Horizons Query] ID: 402 | Type: majorbody | Location: @499 | Date: 2025-11-20
✓ Fetched elements (solution date: 2025-11-20)
✓ Saved: osculating_cache.json
```

---

## Educational Comparisons

**After testing all three:**

| Object | Orbit Period | Distance | Perturbations | Divergence Time |
|--------|-------------|----------|---------------|-----------------|
| Moon   | 27.3 days   | 384,400 km | Moderate | ~2 weeks |
| Phobos | 7.65 hours  | 9,376 km | **Very High** | ~? days |
| Deimos | 30.3 hours  | 23,458 km | Moderate | ~? weeks |

**This will show:**
- How proximity affects perturbation accumulation
- Why different objects need different refresh intervals
- Real-world validation of osculating element limitations

---

## Next Steps After Martian Moons

**If successful:**
- Test Jovian moons (Io, Europa, Ganymede)
- Test Saturnian moons (Titan, Enceladus)
- Document refresh interval recommendations
- Finalize coordinate system conclusions

**For each satellite family:**
- Compare perturbation behavior
- Validate osculating element approach
- Build educational narrative

---

## Success Metrics

**Martian Moons Testing Complete When:**
- ✅ Fresh osculating elements fetched for both
- ✅ Visual comparison done (actual vs osculating)
- ✅ Divergence behavior documented
- ✅ Comparison to Moon documented
- ✅ Any issues identified and noted

---

*"The Moon taught us osculating elements work. Now Phobos will teach us about extreme perturbations."*

**Ready to test! 🔴🌙✨**
