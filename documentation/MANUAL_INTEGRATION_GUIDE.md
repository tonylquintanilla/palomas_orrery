# Exoplanet Integration - Manual Step-by-Step Guide

This guide shows exactly where to add code snippets to integrate exoplanet support into `palomas_orrery.py`.

**Files needed:**
- exoplanet_systems.py (already in /mnt/project/)
- exoplanet_orbits.py (already in /mnt/project/)
- exoplanet_coordinates.py (already in /mnt/project/)

---

## STEP 1: Add Imports (Top of File)

**Location:** After line 34 (after `from idealized_orbits import...`)

**Add these imports:**

```python
# Exoplanet system support
from exoplanet_systems import EXOPLANET_CATALOG, get_system, get_planets_in_hz
from exoplanet_orbits import (
    plot_exoplanet_orbits,
    plot_binary_host_stars,
    calculate_exoplanet_axis_range
)
```

---

## STEP 2: Create Tkinter Variables

**Location:** Around line 2275, just before the line `objects = [`

**Add these variables:**

```python
# ============== EXOPLANET TKINTER VARIABLES ==============
# TRAPPIST-1 system (40.5 light-years, 7 planets)
trappist1_star_var = tk.IntVar(value=0)
trappist1b_var = tk.IntVar(value=0)
trappist1c_var = tk.IntVar(value=0)
trappist1d_var = tk.IntVar(value=0)
trappist1e_var = tk.IntVar(value=0)
trappist1f_var = tk.IntVar(value=0)
trappist1g_var = tk.IntVar(value=0)
trappist1h_var = tk.IntVar(value=0)

# TOI-1338 binary system (1,292 light-years, 2 planets + 2 stars)
toi1338_starA_var = tk.IntVar(value=0)
toi1338_starB_var = tk.IntVar(value=0)
toi1338b_var = tk.IntVar(value=0)
toi1338c_var = tk.IntVar(value=0)

# Proxima Centauri system (4.24 light-years, 2 planets - NEAREST!)
proxima_star_var = tk.IntVar(value=0)
proximab_var = tk.IntVar(value=0)
proximad_var = tk.IntVar(value=0)
```

---

## STEP 3: Add Objects to Objects List

**Location:** Find the end of the `objects = [...]` list (around line 2600), just before the closing `]`

**Add these object entries:**

```python
    # ============== EXOPLANET SYSTEMS ==============
    
    # TRAPPIST-1 System (40.5 light-years)
    {'name': 'TRAPPIST-1 (star)', 'id': 'trappist1_star', 'var': trappist1_star_var,
     'color': 'yellow', 'symbol': 'star', 'object_type': 'exo_host_star',
     'id_type': 'host_star', 'system_id': 'trappist1',
     'mission_info': 'M8V red dwarf at 40.5 light-years hosting 7 Earth-sized planets, 3 in habitable zone.',
     'mission_url': 'https://exoplanets.nasa.gov/trappist1/'},
    
    {'name': 'TRAPPIST-1 b', 'id': 'trappist1b', 'var': trappist1b_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.01154, 'period_days': 1.51087,
     'in_habitable_zone': False,
     'mission_info': 'Innermost planet, 1.5 day period. Too hot for liquid water (400 K).',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7913/trappist-1-b/'},
    
    {'name': 'TRAPPIST-1 c', 'id': 'trappist1c', 'var': trappist1c_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.01580, 'period_days': 2.42182,
     'in_habitable_zone': False,
     'mission_info': '2.4 day period. JWST observations show no significant atmosphere.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7914/trappist-1-c/'},
    
    {'name': 'TRAPPIST-1 d', 'id': 'trappist1d', 'var': trappist1d_var,
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.02227, 'period_days': 4.04961,
     'in_habitable_zone': True,
     'mission_info': '★ IN HABITABLE ZONE ★ Inner edge, 4.0 day period. May have water.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7915/trappist-1-d/'},
    
    {'name': 'TRAPPIST-1 e', 'id': 'trappist1e', 'var': trappist1e_var,
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.02925, 'period_days': 6.09965,
     'in_habitable_zone': True,
     'mission_info': '★ IN HABITABLE ZONE ★ PRIME CANDIDATE! Most likely to have liquid water. 6.1 day period.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7916/trappist-1-e/'},
    
    {'name': 'TRAPPIST-1 f', 'id': 'trappist1f', 'var': trappist1f_var,
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.03849, 'period_days': 9.20669,
     'in_habitable_zone': True,
     'mission_info': '★ IN HABITABLE ZONE ★ 9.2 day period. May have significant water content.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7917/trappist-1-f/'},
    
    {'name': 'TRAPPIST-1 g', 'id': 'trappist1g', 'var': trappist1g_var,
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.04683, 'period_days': 12.35294,
     'in_habitable_zone': True,
     'mission_info': '★ IN HABITABLE ZONE ★ Outer edge, 12.4 day period. May have subsurface ocean.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7918/trappist-1-g/'},
    
    {'name': 'TRAPPIST-1 h', 'id': 'trappist1h', 'var': trappist1h_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'trappist1',
     'semi_major_axis_au': 0.06189, 'period_days': 18.76712,
     'in_habitable_zone': False,
     'mission_info': 'Outermost planet, 18.8 day period. Too cold for liquid water (173 K).',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7919/trappist-1-h/'},
    
    # TOI-1338 System (1,292 light-years, Binary + Circumbinary)
    {'name': 'TOI-1338 A (G-type)', 'id': 'toi1338_starA', 'var': toi1338_starA_var,
     'color': 'yellow', 'symbol': 'star', 'object_type': 'exo_host_star',
     'id_type': 'binary_star_a', 'system_id': 'toi1338',
     'mission_info': 'Primary star in binary system. G-type, 1.1 solar masses, like our Sun.',
     'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/'},
    
    {'name': 'TOI-1338 B (M-type)', 'id': 'toi1338_starB', 'var': toi1338_starB_var,
     'color': 'orange', 'symbol': 'star', 'object_type': 'exo_host_star',
     'id_type': 'binary_star_b', 'system_id': 'toi1338',
     'mission_info': 'Secondary star in binary. M-type red dwarf, 0.3 solar masses. Binary period: 14.6 days.',
     'mission_url': 'https://exoplanets.nasa.gov/news/1644/discovery-alert-first-planet-found-by-tess/'},
    
    {'name': 'TOI-1338 b', 'id': 'toi1338b', 'var': toi1338b_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'toi1338',
     'semi_major_axis_au': 0.4607, 'period_days': 95.196,
     'in_habitable_zone': False,
     'mission_info': 'Neptune-sized circumbinary planet. Discovered by Wolf Cukier (17-year-old TESS intern)!',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/8452/toi-1338-b/'},
    
    {'name': 'TOI-1338 c', 'id': 'toi1338c', 'var': toi1338c_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'toi1338',
     'semi_major_axis_au': 0.76, 'period_days': 215.5,
     'in_habitable_zone': False,
     'mission_info': 'Jupiter-mass circumbinary planet. Confirmed 2023. Only second known multi-planet circumbinary system.',
     'mission_url': 'https://arxiv.org/abs/2305.16894'},
    
    # Proxima Centauri System (4.24 light-years - NEAREST!)
    {'name': 'Proxima Centauri', 'id': 'proxima_star', 'var': proxima_star_var,
     'color': 'red', 'symbol': 'star', 'object_type': 'exo_host_star',
     'id_type': 'host_star', 'system_id': 'proxima',
     'mission_info': 'NEAREST star to the Sun! M5.5V red dwarf at 4.24 light-years. Part of Alpha Centauri system.',
     'mission_url': 'https://exoplanets.nasa.gov/proxima-b/'},
    
    {'name': 'Proxima Centauri b', 'id': 'proximab', 'var': proximab_var,
     'color': 'green', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'proxima',
     'semi_major_axis_au': 0.04856, 'period_days': 11.18427,
     'in_habitable_zone': True,
     'mission_info': '★ IN HABITABLE ZONE ★ NEAREST EXOPLANET! 11.2 day period. Stellar flares may challenge habitability.',
     'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/7167/proxima-centauri-b/'},
    
    {'name': 'Proxima Centauri d', 'id': 'proximad', 'var': proximad_var,
     'color': 'lightblue', 'symbol': 'circle', 'object_type': 'exoplanet',
     'id_type': 'exoplanet', 'system_id': 'proxima',
     'semi_major_axis_au': 0.029, 'period_days': 5.122,
     'in_habitable_zone': False,
     'mission_info': 'Sub-Earth mass planet (0.26 M⊕). Lightest planet detected by radial velocity method.',
     'mission_url': 'https://www.eso.org/public/news/eso2202/'},
```

**Note:** Make sure to add a comma after the last existing object before adding these!

---

## STEP 4: Add GUI Section

**Location:** After the `interstellar_frame` section (around line 6840), before `scale_frame`

**Add this GUI code:**

```python
# ============== EXOPLANETARY SYSTEMS GUI ==============
exoplanet_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, 
                                text="Exoplanetary Systems 🌍🌠")
exoplanet_frame.pack(pady=(10, 5), fill='x')
CreateToolTip(exoplanet_frame, 
              "Explore confirmed exoplanet systems! Select host stars and planets to visualize. "
              "Systems have independent coordinate frames (not connected to Solar System ecliptic). "
              "Green planets are in habitable zones.")

def create_exoplanet_checkbutton(name, variable, is_star=False):
    """Create checkbutton for exoplanet objects"""
    if is_star:
        # Stars get bold labels (same style as main planets)
        frame = tk.Frame(exoplanet_frame)
        frame.pack(anchor='w')
        checkbutton = tk.Checkbutton(frame, text='', variable=variable)
        checkbutton.pack(side='left')
        label = tk.Label(frame, text=name, font=("Arial", 10, "bold"))
        label.pack(side='left')
        info_text = INFO.get(name.strip('- '), "Exoplanet host star")
        CreateToolTip(frame, info_text)
    else:
        # Planets get regular checkbuttons
        checkbutton = tk.Checkbutton(exoplanet_frame, text=name, variable=variable)
        checkbutton.pack(anchor='w')
        info_text = INFO.get(name.strip('- '), "Exoplanet")
        CreateToolTip(checkbutton, info_text)

# TRAPPIST-1 System (40.5 light-years)
create_exoplanet_checkbutton("TRAPPIST-1 System (40.5 ly)", trappist1_star_var, is_star=True)
create_exoplanet_checkbutton("  - TRAPPIST-1 (star)", trappist1_star_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 b (1.5d)", trappist1b_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 c (2.4d)", trappist1c_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 d (4.0d) [HZ]", trappist1d_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 e (6.1d) [HZ] ★", trappist1e_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 f (9.2d) [HZ]", trappist1f_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 g (12.4d) [HZ]", trappist1g_var)
create_exoplanet_checkbutton("  - TRAPPIST-1 h (18.8d)", trappist1h_var)

tk.Label(exoplanet_frame, text="").pack()  # Spacer

# TOI-1338 Binary System (1,292 light-years)
create_exoplanet_checkbutton("TOI-1338 Binary (1,292 ly)", toi1338_starA_var, is_star=True)
create_exoplanet_checkbutton("  - TOI-1338 A (G-type)", toi1338_starA_var)
create_exoplanet_checkbutton("  - TOI-1338 B (M-type)", toi1338_starB_var)
create_exoplanet_checkbutton("  - TOI-1338 b (95d)", toi1338b_var)
create_exoplanet_checkbutton("  - TOI-1338 c (216d)", toi1338c_var)

tk.Label(exoplanet_frame, text="").pack()  # Spacer

# Proxima Centauri System (4.24 light-years - NEAREST!)
create_exoplanet_checkbutton("Proxima Centauri (4.24 ly) NEAREST!", proxima_star_var, is_star=True)
create_exoplanet_checkbutton("  - Proxima Centauri (star)", proxima_star_var)
create_exoplanet_checkbutton("  - Proxima b (11.2d) [HZ] ★", proximab_var)
create_exoplanet_checkbutton("  - Proxima d (5.1d)", proximad_var)
```

---

## STEP 5: Update INFO Dictionary

**Location:** Find the `INFO = {` dictionary (around line 250-500)

**Add these entries anywhere inside the INFO dictionary:**

```python
    # Exoplanet systems
    'TRAPPIST-1': 'M8V red dwarf at 40.5 ly. 7 Earth-sized planets, 3 in habitable zone.',
    'TRAPPIST-1 b': 'Innermost planet, 1.5 day period. Too hot (400 K).',
    'TRAPPIST-1 c': '2.4 day period. No significant atmosphere (JWST).',
    'TRAPPIST-1 d': '★ HABITABLE ZONE (inner edge). 4.0 day period.',
    'TRAPPIST-1 e': '★ PRIME HABITABLE ZONE CANDIDATE! Most likely liquid water. 6.1 days.',
    'TRAPPIST-1 f': '★ HABITABLE ZONE. 9.2 day period. May have water.',
    'TRAPPIST-1 g': '★ HABITABLE ZONE (outer edge). 12.4 day period.',
    'TRAPPIST-1 h': 'Outermost, 18.8 day period. Too cold (173 K).',
    
    'TOI-1338 Binary System': 'Binary star system at 1,292 ly with circumbinary planets.',
    'TOI-1338 A (G-type star)': 'Primary star, G-type, 1.1 solar masses.',
    'TOI-1338 B (M-type star)': 'Secondary star, M-type, 0.3 solar masses. Binary period: 14.6 days.',
    'TOI-1338 b': 'Neptune-sized circumbinary. Discovered by 17-year-old intern Wolf Cukier!',
    'TOI-1338 c': 'Jupiter-mass circumbinary. Confirmed 2023.',
    
    'Proxima Centauri': 'NEAREST star! M5.5V red dwarf at 4.24 ly.',
    'Proxima b': '★ HABITABLE ZONE. NEAREST EXOPLANET! 11.2 day period.',
    'Proxima d': 'Sub-Earth mass (0.26 M⊕). Lightest RV-detected planet. 5.1 days.',
```

---

## STEP 6: Modify plot_objects() Function - CRITICAL!

**Location:** Inside the `plot_objects()` function, find where idealized orbits are plotted (search for "plot_idealized_orbits"). Add this code RIGHT AFTER that section, BEFORE the axis range calculation.

**Add this plotting code:**

```python
    # ============ EXOPLANET ORBITS ============
    # Plot exoplanet systems if any exoplanet objects are selected
    exo_objects = [obj for obj in selected_objects 
                   if obj.get('object_type') == 'exoplanet']
    
    exo_host_stars = [obj for obj in selected_objects 
                      if obj.get('object_type') == 'exo_host_star']
    
    if exo_objects or exo_host_stars:
        try:
            # Determine which system(s) are selected
            exo_systems = set()
            for obj in exo_objects + exo_host_stars:
                system_id = obj.get('system_id')
                if system_id:
                    exo_systems.add(system_id)
            
            # Plot each system
            for system_id in exo_systems:
                system = get_system(system_id)
                if not system:
                    continue
                
                # Get objects for this system
                system_planets = [obj for obj in exo_objects 
                                if obj.get('system_id') == system_id]
                system_stars = [obj for obj in exo_host_stars 
                              if obj.get('system_id') == system_id]
                
                # Plot host star(s)
                if system_stars:
                    if system['host_star'].get('is_binary'):
                        # Binary system - plot both stars
                        fig = plot_binary_host_stars(fig, system, current_date, show_orbits=True)
                    else:
                        # Single star at origin
                        star_trace = go.Scatter3d(
                            x=[0], y=[0], z=[0],
                            mode='markers',
                            name=system['host_star']['name'],
                            marker=dict(size=10, color='yellow', symbol='star'),
                            text=[f"<b>{system['host_star']['name']}</b><br>"
                                  f"{system['host_star']['spectral_type']}<br>"
                                  f"{system['distance_ly']:.1f} light-years"],
                            hoverinfo='text',
                            showlegend=True
                        )
                        fig.add_trace(star_trace)
                
                # Plot planets
                if system_planets:
                    fig = plot_exoplanet_orbits(
                        fig, system_planets, system, current_date,
                        show_orbits=True, show_markers=True
                    )
                
                # Set axis range for exoplanet system
                if system_planets:
                    exo_axis_range = calculate_exoplanet_axis_range(system_planets)
                    fig.update_layout(
                        scene=dict(
                            xaxis=dict(range=[-exo_axis_range, exo_axis_range], title='X (AU)'),
                            yaxis=dict(range=[-exo_axis_range, exo_axis_range], title='Y (AU)'),
                            zaxis=dict(range=[-exo_axis_range, exo_axis_range], title='Z (AU)'),
                            aspectmode='cube'
                        )
                    )
                    
                    # Add note about coordinate system
                    print(f"\nExoplanet system '{system['system_name']}' uses independent local frame:")
                    print(f"  Origin: Host star at (0, 0, 0)")
                    print(f"  XY plane: Sky plane (perpendicular to Earth)")
                    print(f"  Z axis: Toward Earth")
                    print(f"  Axis range: ±{exo_axis_range:.4f} AU\n")
        
        except Exception as e:
            print(f"Error plotting exoplanet systems: {e}")
            import traceback
            traceback.print_exc()
```

---

## Testing Instructions

After adding all the code:

1. **Save** `palomas_orrery.py`

2. **Run the program:**
   ```bash
   cd /mnt/project
   python palomas_orrery.py
   ```

3. **Test TRAPPIST-1:**
   - Scroll to "Exoplanetary Systems" section
   - Check: TRAPPIST-1 (star)
   - Check: TRAPPIST-1 e, f, g (the habitable zone planets)
   - Click "Plot Entered Date"
   - **Expected:** See yellow star at center, 3 green planet markers with orbital paths

4. **Test axis scaling:**
   - Notice the axis range should be ±0.074 AU (much tighter than Solar System)
   - Planets should be visible and well-framed

5. **Test hover text:**
   - Hover over TRAPPIST-1 e
   - Should see: "★ IN HABITABLE ZONE ★" message

6. **Test binary system:**
   - Uncheck TRAPPIST-1 objects
   - Check: TOI-1338 A, TOI-1338 B, TOI-1338 b
   - Click "Plot Entered Date"
   - **Expected:** See two stars orbiting each other, planet orbiting both

---

## Troubleshooting

**If you get import errors:**
- Make sure exoplanet_*.py files are in /mnt/project/
- Check that all three modules are present

**If GUI doesn't show:**
- Check that GUI code is BEFORE `scale_frame = tk.LabelFrame`
- Make sure `scrollable_frame.scrollable_frame` is correct (not just `scrollable_frame`)

**If nothing plots:**
- Check console for error messages
- Verify exoplanet plotting code is in `plot_objects()` function
- Make sure it's AFTER idealized orbits section

**If axis range is wrong:**
- Exoplanet systems should have SMALL ranges (0.01-1 AU)
- If you see 30+ AU, Solar System range is being used instead

---

## What You're Learning

By integrating this manually, you're:
1. ✅ Understanding how Paloma's Orrery structures objects
2. ✅ Learning the GUI layout system (LabelFrames, checkbuttons)
3. ✅ Seeing how plot_objects() orchestrates visualization
4. ✅ Understanding modular design (separate plot functions per system type)
5. ✅ Practicing defensive programming (try/except, validation)

---

## Next Steps After Successful Integration

1. Try all 3 systems (TRAPPIST-1, TOI-1338, Proxima)
2. Test with different dates
3. Try animation (should work automatically)
4. Experiment with different planet combinations
5. Consider adding more systems!

---

**Ready?** Start with Step 1 and work through each section carefully!
