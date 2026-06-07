# Jupiter Moons - Diagnostic and Fix

## Issue Analysis

### What You're Seeing:
- ✅ "Io Actual Orbit" appears in legend
- ✅ Osculating elements fetched (twice - duplicate issue)
- ❌ Only one orbit visible (dotted line)
- ❌ No dashed osculating orbit line visible

### Root Causes:

**Issue 1: Duplicate Fetching**
The osculating elements are being fetched twice because:
1. First fetch: When plotting starts (pre-fetch or initial check)
2. Second fetch: When osculating orbit function is called

**This is the SAME issue Mars moons had initially!**

**Issue 2: Osculating Orbit Not Visible**
Either:
- Function isn't being called at all
- Function is called but trace isn't added to figure
- Trace is added but not visible (wrong coordinates/scale)

---

## Diagnostic Steps

### Step 1: Check Console Output

**Look for these messages:**
```
Adding osculating orbit for Io...
Plotting osculating orbit for Io
  Inclination: 2.2038° (ecliptic frame)
  ✓ Osculating orbit plotted
```

**If you DON'T see these:** Function isn't being called

**If you DO see these:** Function is called but trace issue

---

### Step 2: Check Integration

**Did you add the function?**
Search in idealized_orbits.py for:
```python
def plot_jupiter_moon_osculating_orbit
```

**If NOT found:** Function not integrated yet!

**Did you add the conditional call?**
Search for:
```python
if satellite_name in JUPITER_MOONS
```

**If NOT found:** Conditional not added!

---

### Step 3: Fix Duplicate Fetching

**The Mars moons solution:**

When calling osculating function, we need to pass the ALREADY FETCHED elements, not fetch again!

**Current problematic pattern:**
```python
# Somewhere: Elements fetched once
elements = get_elements_with_prompt(...)

# Later: Function fetches AGAIN
def plot_jupiter_moon_osculating_orbit(...):
    elements = get_elements_with_prompt(...)  # DUPLICATE!
```

**Fixed pattern (like Mars):**
```python
# Fetch once
elements = get_elements_with_prompt(...)

# Pass to function
def plot_jupiter_moon_osculating_orbit(fig, elements, ...):
    # Use passed elements, don't fetch again!
```

---

## Quick Fixes

### Fix 1: If Function Not Integrated

**You need to:**
1. Copy `plot_jupiter_moon_osculating_orbit` function into idealized_orbits.py
2. Add `JUPITER_MOONS` list
3. Add conditional call in Jupiter section

**Files to use:**
- Function: `/mnt/user-data/outputs/plot_jupiter_moon_osculating_orbit.py`
- Integration: `/mnt/user-data/outputs/jupiter_integration_snippet.py`

---

### Fix 2: If Function Integrated But Not Working

**Check the trace properties:**

In `plot_jupiter_moon_osculating_orbit`, the trace is added like:
```python
fig.add_trace(go.Scatter3d(
    x=x_final,
    y=y_final,
    z=z_final,
    mode='lines',
    line=dict(color=color, width=2, dash='dash'),  # DASHED LINE
    name=f'{satellite_name} Actual Orbit',
    ...
))
```

**Possible issues:**
- `x_final, y_final, z_final` are all zeros → orbit at origin
- `color` is wrong → invisible
- `dash='dash'` not working → check plotly version

**Quick test:**
Add print statement before `fig.add_trace`:
```python
print(f"Orbit coords: x range={min(x_final):.3f} to {max(x_final):.3f}")
print(f"              y range={min(y_final):.3f} to {max(y_final):.3f}")
print(f"              z range={min(z_final):.3f} to {max(z_final):.3f}")
```

If all zeros → rotation/calculation problem!

---

### Fix 3: Eliminate Duplicate Fetching

**Option A: Cache check (like Mars moons)**

Before calling osculating function, check if elements already in memory:
```python
# In plot_satellite_orbit, Jupiter section
if satellite_name in JUPITER_MOONS and date is not None:
    # Check if we already have osculating elements
    from osculating_cache_manager import load_cache
    cache = load_cache()
    cache_key = satellite_name
    
    if cache_key in cache:
        # Use cached elements, don't fetch again
        elements = cache[cache_key]['elements']
        fig = plot_jupiter_moon_osculating_orbit_with_elements(
            fig, satellite_name, elements, color
        )
    else:
        # Fetch and plot
        fig = plot_jupiter_moon_osculating_orbit(...)
```

**Option B: Pre-fetch pattern (cleaner)**

Fetch once at the beginning, then pass elements:
```python
# Early in plot_satellite_orbit
if satellite_name in JUPITER_MOONS:
    osculating_elements = get_elements_with_prompt(...)
    
# Later in Jupiter section
if satellite_name in JUPITER_MOONS:
    fig = plot_jupiter_moon_osculating_orbit_with_elements(
        fig, satellite_name, osculating_elements, color
    )
```

---

## Most Likely Issue

**Based on screenshot showing "Io Actual Orbit" but no visible dashed line:**

**The function IS being called** (that's where the legend entry comes from)

**But the orbit coordinates are wrong** (not visible in view)

**Two possibilities:**

1. **Rotation sequence wrong** → Orbit is way off screen
2. **Scale wrong** → Orbit is too small/large to see

**Quick test:**
Look at the 3D view coordinates. Io's orbit should be at:
- Distance from Jupiter: ~0.003 AU
- Should be visible near Jupiter

If you zoom WAY out and see a tiny orbit, scale is wrong.
If you don't see it anywhere, rotation is wrong.

---

## Recommended Action

**Tony, please provide:**

1. **Console output** showing:
   - "Adding osculating orbit for Io..." message
   - "Plotting osculating orbit..." message
   - Any error messages

2. **Confirmation:**
   - Did you integrate the function into idealized_orbits.py?
   - Did you add the conditional call?
   - Can you see the function definition in the file?

3. **Visual check:**
   - Zoom way out in 3D view
   - Rotate around
   - Is there a dashed line anywhere?

**Then I can provide the exact fix!**

---

## Expected vs Actual

### Expected Behavior:
```
Console:
  Plotting Io orbit around Jupiter
  Adding osculating orbit for Io...
  ⟳ Fetching osculating elements...  (ONCE ONLY!)
  ✓ Fetched elements
  Plotting osculating orbit for Io
    Inclination: 2.2038° (ecliptic frame)
    ✓ Osculating orbit plotted

Plot:
  - Dotted line (analytical)
  - Dashed line (osculating)  
  - Both visible near Jupiter
  - ~2° separation
```

### Actual Behavior (your screenshot):
```
Console:
  [Need to see this!]

Plot:
  - Dotted line visible ✅
  - "Io Actual Orbit" in legend ✅
  - Dashed line NOT visible ❌
  - Duplicate fetching ❌
```

---

## Next Steps

**Provide console output → I'll give exact fix!**

The solution exists (Mars moons work), just need to see what's different for Jupiter.

---

*"The legend shows it's trying. The view shows it's not visible. The console will show us why!"*
