# CORRECT IMPLEMENTATION: Actual Apsidal Markers for Satellites

## Confirmed Approach

**✅ Use the SAME pattern as planets** (proven working at lines 2330-2375 in idealized_orbits.py)

**File:** `idealized_orbits.py`  
**Function:** `plot_idealized_orbits()`  
**Locations:** Three places where satellites are plotted

---

## Step 1: Remove Incorrect Code

### Delete from plot_satellite_orbit() function

**Lines to DELETE:** ~1592-1712 in your uploaded idealized_orbits.py

**Find and remove this entire block:**
```python
# ========== ADD ACTUAL APSIDAL MARKERS FOR SATELLITES ==========
# Display actual JPL Horizons positions at periapsis/apoapsis dates
# Shows perturbation effects: J2, N-body, tidal forces, resonances

if show_apsidal_markers and 'TP' in orbital_params:
    print(f"\n[ACTUAL APSIDAL] Attempting to fetch actual positions for {satellite_name}", flush=True)
    
    from apsidal_markers import (
        compute_apsidal_dates_from_tp,
        fetch_positions_for_apsidal_dates,
        add_actual_apsidal_markers_enhanced,
        calculate_exact_apsides
    )
    from datetime import timedelta
    
    # Calculate ideal apsidal positions for comparison
    apsides = calculate_exact_apsides(
        a, e,
        orbital_params.get('i', i),
        orbital_params.get('omega', omega),
        orbital_params.get('Omega', Omega),
        rotate_points
    )
    
    # Get periapsis/apoapsis dates from TP
    next_periapsis, next_apoapsis = compute_apsidal_dates_from_tp(
        satellite_name,
        orbital_params,
        current_date=date
    )
    
    # Map satellite name to JPL Horizons ID
    satellite_horizons_ids = {
        # Earth
        'Moon': '301',
        # Mars
        'Phobos': '401',
        'Deimos': '402',
        # Jupiter
        'Io': '501',
        'Europa': '502',
        'Ganymede': '503',
        'Callisto': '504',
        'Metis': '516',
        'Adrastea': '515',
        'Amalthea': '505',
        'Thebe': '514',
        # Saturn
        'Mimas': '601',
        'Enceladus': '602',
        'Tethys': '603',
        'Dione': '604',
        'Rhea': '605',
        'Titan': '606',
        'Hyperion': '607',
        'Iapetus': '608',
        'Phoebe': '609',
        # Uranus
        'Miranda': '705',
        'Ariel': '701',
        'Umbriel': '702',
        'Titania': '703',
        'Oberon': '704',
        # Neptune
        'Triton': '801',
        # Pluto
        'Charon': '901'
    }
    
    satellite_id = satellite_horizons_ids.get(satellite_name)
    
    if satellite_id and (next_periapsis or next_apoapsis):
        print(f"  Satellite ID: {satellite_id}", flush=True)
        print(f"  Next periapsis: {next_periapsis}", flush=True)
        print(f"  Next apoapsis: {next_apoapsis}", flush=True)
        
        try:
            # fetch_position is passed as a parameter
            
            # Fetch actual positions at apsidal dates
            positions_dict = fetch_positions_for_apsidal_dates(
                obj_id=satellite_id,
                params=orbital_params,
                date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                center_id=parent_planet,  # Use parent planet name
                id_type='majorbody',
                is_satellite=True,
                fetch_position=fetch_position
            )
            
            if positions_dict:
                print(f"  Successfully fetched {len(positions_dict)} actual positions", flush=True)
                
                # Add actual apsidal markers
                add_actual_apsidal_markers_enhanced(
                    fig,
                    satellite_name,
                    orbital_params,
                    date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                    positions_dict=positions_dict,
                    color_map=color_map,
                    center_body=parent_planet,
                    is_satellite=True,
                    ideal_apsides=apsides,
                    filter_by_date_range=False
                )
                
                print(f"  ✓ Added actual apsidal markers for {satellite_name}", flush=True)
            else:
                print(f"  ⚠ No positions fetched for {satellite_name}", flush=True)
                
        except Exception as e:
            print(f"  ⚠ Error fetching actual apsidal positions for {satellite_name}: {e}", flush=True)
            import traceback
            traceback.print_exc()
    else:
        if not satellite_id:
            print(f"  ⚠ No Horizons ID mapping for {satellite_name}", flush=True)
        if not (next_periapsis or next_apoapsis):
            print(f"  ⚠ No apsidal dates calculated for {satellite_name}", flush=True)
```

**Delete all of that** - it's in the wrong function!

---

## Step 2: Add Correct Code to plot_idealized_orbits()

### Satellite Horizons ID Mapping (Add at module level, ~line 50)

**Location:** Near the top of idealized_orbits.py with other constants

**Add this dictionary:**
```python
# Satellite Horizons IDs for actual apsidal marker fetching
SATELLITE_HORIZONS_IDS = {
    # Earth
    'Moon': '301',
    # Mars
    'Phobos': '401',
    'Deimos': '402',
    # Jupiter
    'Io': '501',
    'Europa': '502',
    'Ganymede': '503',
    'Callisto': '504',
    'Metis': '516',
    'Adrastea': '515',
    'Amalthea': '505',
    'Thebe': '514',
    # Saturn
    'Mimas': '601',
    'Enceladus': '602',
    'Tethys': '603',
    'Dione': '604',
    'Rhea': '605',
    'Titan': '606',
    'Hyperion': '607',
    'Iapetus': '608',
    'Phoebe': '609',
    # Uranus
    'Miranda': '705',
    'Ariel': '701',
    'Umbriel': '702',
    'Titania': '703',
    'Oberon': '704',
    # Neptune
    'Triton': '801',
    # Pluto
    'Charon': '901'
}
```

### Location 1: After Mars Moons Analytical Orbit (~line 1760)

**Find this code:**
```python
# Special handling for Mars moons with dual-orbit system
elif moon_name in ['Phobos', 'Deimos'] and center_id == 'Mars':
    # Get satellite's current position
    satellite_current_pos = current_positions.get(moon_name) if current_positions else None
    
    # Plot analytical orbit (time-varying elements - dotted line)
    fig = plot_satellite_orbit(
        moon_name, 
        planetary_params,
        center_id, 
        color_map(moon_name), 
        fig,
        date=date,
        days_to_plot=days_to_plot,
        current_position=satellite_current_pos,
        show_apsidal_markers=show_apsidal_markers
    )
    
    # Plot osculating orbit (JPL elements - dashed line)
    # ... code continues ...
```

**Add AFTER the plot_satellite_orbit() call and BEFORE osculating orbit:**

```python
    # ========== ADD ACTUAL APSIDAL MARKERS (Mars Moons) ==========
    if show_apsidal_markers and fetch_position:
        moon_params = planetary_params.get(moon_name)
        if moon_params and 'TP' in moon_params:
            obj_id = SATELLITE_HORIZONS_IDS.get(moon_name)
            
            if obj_id:
                try:
                    from apsidal_markers import (
                        fetch_positions_for_apsidal_dates,
                        add_actual_apsidal_markers_enhanced,
                        calculate_exact_apsides
                    )
                    from datetime import timedelta
                    
                    # Calculate ideal apsides for comparison
                    apsides = calculate_exact_apsides(
                        moon_params.get('a'),
                        moon_params.get('e'),
                        moon_params.get('i'),
                        moon_params.get('omega'),
                        moon_params.get('Omega'),
                        rotate_points
                    )
                    
                    # Fetch actual positions at apsidal dates
                    positions_dict = fetch_positions_for_apsidal_dates(
                        obj_id=obj_id,
                        params=moon_params,
                        date_range=None,
                        center_id=center_id,
                        id_type='majorbody',
                        is_satellite=True,
                        fetch_position=fetch_position
                    )
                    
                    if positions_dict:
                        # Add actual apsidal markers
                        add_actual_apsidal_markers_enhanced(
                            fig,
                            moon_name,
                            moon_params,
                            date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                            positions_dict=positions_dict,
                            color_map=color_map,
                            center_body=center_id,
                            is_satellite=True,
                            ideal_apsides=apsides,
                            filter_by_date_range=False
                        )
                        print(f"  ✓ Added actual apsidal markers for {moon_name}", flush=True)
                        
                except Exception as e:
                    print(f"  ⚠ Error adding actual markers for {moon_name}: {e}", flush=True)
```

### Location 2: After Jupiter Moons Analytical Orbit (~line 1790)

**Find this code:**
```python
# Special handling for Jupiter moons with dual-orbit system
elif moon_name in JUPITER_MOONS and center_id == 'Jupiter':
    # Get satellite's current position
    satellite_current_pos = current_positions.get(moon_name) if current_positions else None
    
    # Plot analytical orbit (time-varying elements - dotted line)
    fig = plot_satellite_orbit(
        moon_name, 
        planetary_params,
        center_id, 
        color_map(moon_name), 
        fig,
        date=date,
        days_to_plot=days_to_plot,
        current_position=satellite_current_pos,
        show_apsidal_markers=show_apsidal_markers
    )
    
    # Plot osculating orbit (JPL elements - dashed line)
    # ... code continues ...
```

**Add the SAME code block as above** (just copy the Mars moons block)

### Location 3: After Other Satellites (~line 1810)

**Find this code:**
```python
else:
    # Use the standard satellite plotting function for other moons
    # Get satellite's current position
    satellite_current_pos = current_positions.get(moon_name) if current_positions else None

    fig = plot_satellite_orbit(
        moon_name, 
        planetary_params,
        center_id, 
        color_map(moon_name), 
        fig,
        date=date,
        days_to_plot=days_to_plot,
        current_position=satellite_current_pos,
        show_apsidal_markers=show_apsidal_markers
    )
```

**Add the SAME code block after plot_satellite_orbit() call**

---

## Step 3: Also Remove fetch_position Parameter from plot_satellite_orbit()

Since we're not using it there anymore, clean up:

**Find:**
```python
def plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig=None, 
                         date=None, days_to_plot=None, current_position=None,
                         show_apsidal_markers=False, fetch_position=None):
```

**Change to:**
```python
def plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig=None, 
                         date=None, days_to_plot=None, current_position=None,
                         show_apsidal_markers=False):
```

**Remove `, fetch_position=None`** since we're not using it in this function anymore.

---

## Summary of Changes

### Remove:
1. ❌ Lines ~1592-1712 in `plot_satellite_orbit()` function
2. ❌ `fetch_position=None` parameter from `plot_satellite_orbit()` signature

### Add:
1. ✅ `SATELLITE_HORIZONS_IDS` dictionary at module level (~line 50)
2. ✅ Actual marker code after Mars moons analytical plot (~line 1760)
3. ✅ Actual marker code after Jupiter moons analytical plot (~line 1790)
4. ✅ Actual marker code after other satellites analytical plot (~line 1810)

---

## Expected Result

**Console output:**
```
[ACTUAL APSIDAL] ... (from apsidal_markers.py functions)
  ✓ Added actual apsidal markers for Phobos
```

**Visualization:**
- Phobos Actual Orbit (solid gray line)
- **Phobos Actual Periareion (filled red square on solid line)** ← NEW!
- Phobos Ideal Periareion (open red square on dotted line)
- Phobos Analytical Orbit (dotted red line)
- Phobos Osculating Orbit (dashed red line)

**No errors, no circular imports, working like planets!** ✅

---

## Testing

**Test with:**
1. Moon (Earth system)
2. Phobos (Mars system)
3. Io (Jupiter system)

**Look for:**
- Filled squares on solid orbit lines
- Console: "✓ Added actual apsidal markers"
- Legend: "Satellite Actual Periapsis"
- No errors!

---

**This is the correct approach - same as planets!** 🎯
