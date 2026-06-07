# Apophis Close Approach Infrastructure -- Change Manifest
# March 2026 | Capabilities A, B, C

## Summary of Changes

### FILE 1: close_approach_data.py  [NEW FILE]
Drop into project root alongside palomas_orrery.py.
Standalone module -- no changes to existing files required to use Capability A alone.

### FILE 2: idealized_orbits.py  [APPEND at end of file]
Adds: plot_hyperbolic_osculating_orbit()
One new function appended to end of file. No existing code touched.

### FILE 3: palomas_orrery.py  [TWO TARGETED INSERTS]
Insert 1: Add import to top-level imports block (line ~61 area)
Insert 2: Add CAD perigee + hyperbolic osculating calls after EACH plot_idealized_orbits call
  There are TWO plot_idealized_orbits call sites (~line 4983, ~line 6131)
  The same snippet goes after both.

---

## CHANGE 1: Import block in palomas_orrery.py

### Location: line ~61 (after idealized_orbits import)

Add this line:
```python
from idealized_orbits import plot_idealized_orbits, planetary_params, parent_planets, planet_tilts, rotate_points
from close_approach_data import get_approach_within_date_range, add_cad_perigee_marker, fetch_position_at_approach
from idealized_orbits import plot_hyperbolic_osculating_orbit
```

i.e., replace the existing line 61:
  FROM:
    from idealized_orbits import plot_idealized_orbits, planetary_params, parent_planets, planet_tilts, rotate_points

  TO:
    from idealized_orbits import plot_idealized_orbits, plot_hyperbolic_osculating_orbit, planetary_params, parent_planets, planet_tilts, rotate_points
    from close_approach_data import get_approach_within_date_range, add_cad_perigee_marker, fetch_position_at_approach

---

## CHANGE 2: After FIRST plot_idealized_orbits call (~line 4992)

Current code (lines 4983-4992):
```python
            # 6. Plot idealized orbits using your new logic
            plot_idealized_orbits(fig, selected_objects, center_id=center_object_name,
                                    objects=objects,
                                    planetary_params=active_planetary_params,
                                    parent_planets=parent_planets, color_map=color_map,
                                    date=date_obj, days_to_plot=settings['days_to_plot'],
                                    current_positions=current_positions,
                                    fetch_position=fetch_position,
                                    show_apsidal_markers=show_apsidal_markers_var.get(),
                                    parent_window=root
                                    )
```

AFTER that block, insert:

```python
            # ---- Capability B: CAD perigee marker (precision close approach) ----
            # ---- Capability C: Hyperbolic osculating orbit ----------------------
            # Called when center is a major body (not Sun) and apsidal markers enabled
            if center_object_name != 'Sun' and show_apsidal_markers_var.get():
                _add_close_approach_extras(
                    fig=fig,
                    selected_objects=selected_objects,
                    objects=objects,
                    center_object_name=center_object_name,
                    color_map=color_map,
                    date_obj=date_obj,
                    settings=settings,
                    show_apsidal_markers=show_apsidal_markers_var.get(),
                    parent_window=root,
                )
```

---

## CHANGE 3: After SECOND plot_idealized_orbits call (~line 6145)

Current code (lines 6131-6145):
```python
            plot_idealized_orbits(
                fig,
                selected_object_names,
                center_id=center_object_name,
                objects=objects,
                planetary_params=active_planetary_params,
                parent_planets=parent_planets,
                color_map=color_map,
                date=dates_list[0] if dates_list else datetime.now(),
                days_to_plot=settings['days_to_plot'],
                current_positions=initial_positions,
                fetch_position=fetch_position,
                show_apsidal_markers=show_apsidal_markers_var.get(),
                parent_window=root
            )
```

AFTER that block, insert the same snippet:

```python
            # ---- Capability B: CAD perigee marker (precision close approach) ----
            # ---- Capability C: Hyperbolic osculating orbit ----------------------
            if center_object_name != 'Sun' and show_apsidal_markers_var.get():
                _add_close_approach_extras(
                    fig=fig,
                    selected_objects=selected_object_names,
                    objects=objects,
                    center_object_name=center_object_name,
                    color_map=color_map,
                    date_obj=dates_list[0] if dates_list else datetime.now(),
                    settings=settings,
                    show_apsidal_markers=show_apsidal_markers_var.get(),
                    parent_window=root,
                )
```

---

## CHANGE 4: New helper function in palomas_orrery.py

### Location: Before the GUI setup code (early in file, after imports and constants, 
### before the first function definitions or after existing helper functions)
### Search for a good spot near other helper functions -- around line 1600-1700 area

Add this new function:

```python
# ============================================================================
# CLOSE APPROACH EXTRAS: CAD Perigee Marker + Hyperbolic Osculating Orbit
# Capabilities B and C from the Apophis close approach infrastructure (March 2026).
# Called after plot_idealized_orbits when center is a major body (not Sun).
# ============================================================================

def _add_close_approach_extras(fig, selected_objects, objects, center_object_name,
                                 color_map, date_obj, settings, show_apsidal_markers,
                                 parent_window):
    """
    Add CAD perigee marker and hyperbolic osculating orbit for small body flybys.

    Called after plot_idealized_orbits for non-Sun center views.
    Handles Capability B (precision perigee marker) and Capability C (hyperbolic
    osculating orbit) from the Apophis close approach infrastructure.

    Parameters:
        fig:                    Plotly Figure object
        selected_objects:       List of selected object names (str)
        objects:                Full objects list (dicts)
        center_object_name:     Central body name e.g. 'Earth'
        color_map:              Color lookup function
        date_obj:               Plot start date (datetime)
        settings:               Settings dict (needs 'days_to_plot', 'start_date', 'end_date')
        show_apsidal_markers:   Bool -- only run if True
        parent_window:          Tkinter root window for dialogs
    """
    if not show_apsidal_markers:
        return

    # Only run for major body centers (Earth, Mars, Jupiter, etc.)
    MAJOR_BODY_CENTERS = {'Earth', 'Mars', 'Venus', 'Mercury', 'Jupiter',
                          'Saturn', 'Uranus', 'Neptune', 'Moon'}
    if center_object_name not in MAJOR_BODY_CENTERS:
        return

    # Determine plot date range for close approach window check
    from datetime import timedelta
    days_to_plot = settings.get('days_to_plot', 365)
    start_date = date_obj
    end_date = date_obj + timedelta(days=days_to_plot)

    # Center body -> Horizons ID mapping
    CENTER_TO_HORIZONS_ID = {
        'Earth':   '399',
        'Mars':    '499',
        'Jupiter': '599',
        'Saturn':  '699',
        'Uranus':  '799',
        'Neptune': '899',
        'Venus':   '299',
        'Mercury': '199',
        'Moon':    '301',
    }

    for obj_name in selected_objects:
        # Find object metadata
        obj_info = next((o for o in objects if o['name'] == obj_name), None)
        if obj_info is None:
            continue

        # Only process smallbody objects (asteroids, comets, not planets/moons)
        if obj_info.get('id_type') not in ('smallbody',):
            continue

        designation = obj_info.get('id', obj_name)

        print(f"\n[CloseApp] Checking close approach for {obj_name} near {center_object_name}", flush=True)
        print(f"  Designation: {designation} | Date range: {start_date.date()} to {end_date.date()}", flush=True)

        # ---- Capability B: CAD Perigee Marker --------------------------------
        try:
            from close_approach_data import (get_approach_within_date_range,
                                              add_cad_perigee_marker,
                                              fetch_position_at_approach)

            approaches_in_window = get_approach_within_date_range(
                designation=designation,
                body=center_object_name,
                start_date=start_date,
                end_date=end_date,
            )

            if approaches_in_window:
                # Use the closest approach in the window
                best = min(approaches_in_window, key=lambda a: a['dist_au'])
                print(f"  [CAD] Close approach found: {best['date']} | "
                      f"{best['dist_km']:,.1f} km | {best['v_rel_kms']:.3f} km/s", flush=True)

                # Fetch precise position from Horizons at the CAD perigee epoch
                center_id_num = CENTER_TO_HORIZONS_ID.get(center_object_name, '399')
                position = fetch_position_at_approach(
                    approach=best,
                    designation=designation,
                    center_body_id=center_id_num,
                    id_type='smallbody',
                )

                if position:
                    add_cad_perigee_marker(
                        fig=fig,
                        approach=best,
                        position=position,
                        body=center_object_name,
                        obj_name=obj_name,
                        color_map=color_map,
                    )
                else:
                    print(f"  [CAD] Could not fetch Horizons position for marker -- skipping", flush=True)
            else:
                print(f"  [CAD] No close approach in plotted window for {obj_name}", flush=True)

        except Exception as e:
            print(f"  [CAD] Error in CAD perigee marker for {obj_name}: {e}", flush=True)
            import traceback
            traceback.print_exc()

        # ---- Capability C: Hyperbolic Osculating Orbit -----------------------
        # Only attempt if apsidal markers are on (same checkbox controls both)
        try:
            from idealized_orbits import plot_hyperbolic_osculating_orbit
            fig = plot_hyperbolic_osculating_orbit(
                fig=fig,
                obj_name=obj_name,
                obj_info=obj_info,
                center_id=center_object_name,
                color_map=color_map,
                date=date_obj,
                show_apsidal_markers=show_apsidal_markers,
                parent_window=parent_window,
            )
        except Exception as e:
            print(f"  [HypOsc] Error plotting hyperbolic osculating for {obj_name}: {e}", flush=True)
            import traceback
            traceback.print_exc()
```

---

## TESTING SEQUENCE

1. Load the orrery
2. Set center = Earth
3. Check Apophis
4. Set date range: April 1-29, 2029 (28 days)
5. Check "Show apsidal markers" checkbox
6. Plot

### Expected behavior:

**Capability A (CAD fetch):**
- Console: "[CAD] Querying: https://ssd-api.jpl.nasa.gov/cad.api?des=2004+MN4..."
- Returns Apophis 2029-Apr-13 approach at ~38,013 km

**Capability B (perigee marker):**
- Console: "[CAD] Added perigee marker for Apophis (Perigee)"
- Legend: "Apophis Perigee (JPL CAD)"
- Diamond-open symbol on figure (distinct from square-open Keplerian markers)
- Hover: exact time, 38,012 km center-to-center, ~31,635 km from surface, 7.422 km/s, +/-2 km uncertainty
- NOTE: Marker may sit slightly OFF the trajectory line (expected -- time resolution)

**Capability C (hyperbolic osculating orbit):**
- Prompt dialog: "Update Apophis orbital elements?" (for geocentric cache)
- If YES: Console "[HypOsc] Added hyperbolic osculating orbit for Apophis: e=4.25, q=0.000254 AU"
- Legend: "Apophis Osculating Orbit (Epoch: 2029-04-13 osc.)"
- Dashed line on figure

### What to verify visually:
- Diamond marker appears near the V-shaped closest approach of the trajectory
- Dashed hyperbola closely hugs the trajectory near closest approach
- Dashed hyperbola opens outward and diverges from trajectory farther out
- Both traces togglable via legend click

---

## NOTES

**Cache location:** close_approach data stores in orbit_paths.json under key:
  "close_approach:2004 MN4:Earth"  (or "close_approach:99942:Earth")

**Designation used:** The CAD API accepts both "99942" and "2004 MN4".
Use the id field from celestial_objects.py: '2004 MN4' is correct.

**Unit detection:** Geocentric elements for Apophis will have q ~ 38,000 km.
The existing q > 10000 detection in orbit_data_manager.py will correctly
identify these as km and convert to AU.

**Reference frame:** Geocentric osculating elements from Horizons are in
ecliptic frame (J2000). Standard rotation sequence (omega, i, Omega) applies.
No planet-specific rotation needed (same as Saturn/Uranus moon pattern).

**The offset note:** The hover text on the CAD marker explicitly tells the viewer
that the marker may not sit on the trajectory line -- this is intentional and
informative, not a bug.
