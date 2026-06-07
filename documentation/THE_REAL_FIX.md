# THE REAL FIX: Add Actual Apsidal Markers to ACTUAL Orbit Trace

## Now I Understand!

You want actual apsidal markers (filled squares at TP dates) to appear on the **ACTUAL ORBIT TRACE** - the solid line showing real JPL Horizons position vectors over time!

**NOT on:**
- Analytical orbit (dotted line - `plot_satellite_orbit()`)
- Osculating orbit (dashed line - `plot_*_osculating_orbit()`)

**BUT on:**
- **Actual orbit** (solid line - `plot_actual_orbits()` in palomas_orrery.py)

---

## The Visualization Layers

**Your current visualization has THREE orbit types:**

1. **Actual orbit trace** (SOLID line)
   - Plotted by `plot_actual_orbits()` in `palomas_orrery.py`
   - Real JPL Horizons position vectors
   - Shows where satellite ACTUALLY was at each time
   - **← ACTUAL MARKERS SHOULD GO HERE!** ✅

2. **Analytical orbit** (DOTTED line)
   - Plotted by `plot_satellite_orbit()` in `idealized_orbits.py`
   - Time-varying mean elements
   - Theoretical position
   - Has ideal markers (open squares)

3. **Osculating orbit** (DASHED line)
   - Plotted by `plot_mars/jupiter_moon_osculating_orbit()`
   - Instantaneous JPL elements
   - Snapshot Keplerian orbit

---

## Where The Code Should Actually Go

The actual apsidal marker code should be added to:

**File:** `palomas_orrery.py`  
**Function:** `plot_actual_orbits()` (around line 3685)

This function:
- Fetches real JPL Horizons position vectors
- Plots the solid orbit trace
- Shows where satellite actually was

**Perfect place for actual apsidal markers!**

---

## Why The Current Approach Won't Work

The code you added to `plot_satellite_orbit()` in `idealized_orbits.py`:
- Plots on the ANALYTICAL orbit (dotted line)
- Not the ACTUAL orbit (solid line)
- Wrong orbit entirely!

**That's why it's trying to fetch positions again** - it's in the wrong place!

---

## The Correct Implementation

### Step 1: Remove Code from idealized_orbits.py

Remove the actual apsidal marker code block from `plot_satellite_orbit()` (lines ~1592-1712 in your uploaded file).

### Step 2: Add Code to palomas_orrery.py

Add the actual apsidal marker code to `plot_actual_orbits()` function.

**Location:** After plotting the solid orbit trace, before returning the figure.

**Logic:**
1. The actual orbit trace is already plotted (solid line)
2. We have the satellite name and orbital params
3. Get TP from osculating cache
4. Calculate TP date using `compute_apsidal_dates_from_tp()`
5. The position at TP is ALREADY in the plotted trace!
6. Find that position in the trace data
7. Add a marker at that point
8. Done!

---

## Key Insight

**We don't need to fetch new positions!**

The actual orbit trace ALREADY contains the position at TP (and all other times). We just need to:
1. Find the TP date
2. Find which point in the trace corresponds to TP
3. Add a marker there

**Much simpler than fetching from JPL again!**

---

## Simplified Code Approach

```python
# In plot_actual_orbits(), after plotting the orbit trace:

if show_apsidal_markers:
    # Get TP from osculating cache
    from osculating_cache_manager import load_cache
    cache = load_cache()
    
    if satellite_name in cache:
        elements = cache[satellite_name]['elements']
        TP = elements.get('TP')  # Julian Date
        
        if TP:
            # Convert TP to datetime
            from astropy.time import Time
            tp_datetime = Time(TP, format='jd').datetime
            
            # Find the closest point in our plotted trace to tp_datetime
            # (we already have positions at all the dates we plotted)
            
            # Add marker at that position
            fig.add_trace(go.Scatter3d(
                x=[x_at_tp],
                y=[y_at_tp],
                z=[z_at_tp],
                mode='markers',
                marker=dict(
                    size=8,
                    symbol='square',
                    color=color,
                    line=dict(color='white', width=2)
                ),
                name=f"{satellite_name} Actual Periapsis",
                hovertext=f"TP: {tp_datetime}",
                showlegend=True
            ))
```

---

## The Right Place

**Function:** `plot_actual_orbits()` in `palomas_orrery.py`  
**Line:** ~3685 (function definition)  
**Insert:** After the orbit trace is plotted, before `return fig`

---

## Should I Create This Fix?

I can create the proper implementation that:
1. Removes the code from `plot_satellite_orbit()` in idealized_orbits.py
2. Adds it to `plot_actual_orbits()` in palomas_orrery.py
3. Uses the already-plotted positions (no new JPL fetches needed!)
4. Adds actual markers at TP on the solid orbit trace

**Ready to create the correct fix?**

---

**Summary:**
- ❌ Wrong: Adding to analytical orbit (dotted line)
- ❌ Wrong: Adding to osculating orbit (dashed line)  
- ✅ **Correct: Adding to ACTUAL orbit trace (solid line)**

The actual markers belong on the actual orbit! 🎯
