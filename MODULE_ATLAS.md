# Paloma's Orrery -- Module Atlas

Generated: April 15, 2026
Modules: 99 | Functions: 768 | Lines: 79,581

---

## How to Use This Document

Upload this file to a Claude session. Then ask questions:

- "What modules are involved in rendering comets?"
- "I want to add a new spacecraft encounter -- what do I touch?"
- "What imports spacecraft_encounters and what does it import?"
- "Show me the pipeline from GUI click to rendered figure"
- "What would break if I changed constants_new?"

Claude searches this atlas, reads relevant source files,
and explains in context.

---

## Roles at a Glance

| Role | Count | Description |
|------|-------|-------------|
| gui | 6 | Applications the user launches (GUIs, editors) |
| rendering | 22 | Builds visual traces, figures, and charts |
| rendering/shells | 15 | Planetary shell visualizations (sphere layers) |
| computation | 15 | Math, orbital mechanics, data processing |
| data | 13 | Catalogs, constants, and static datasets |
| cache | 8 | Fetch, store, and retrieve computed data |
| pipeline | 4 | Transforms data between stages (export, conversion) |
| scenario | 3 | Specific Earth system scenarios |
| utility | 5 | Shared helper functions |
| devtool | 1 | Developer tools (dependency tracing, atlas) |
| other | 7 | Uncategorized |

---

## GUI: Applications the user launches (GUIs, editors)

### earth_system_controller.py

**Role:** gui | **Lines:** 81

> earth_system_controller.py - KMZ layer selector for Google Earth Pro.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `class MissionControlApp` (line 16)

---

### earth_system_visualization_gui.py

**Role:** gui | **Lines:** 1,822

> Earth System Visualization GUI for Paloma's Orrery Hub window with climate data visualizations

**Depends on:** climate_cache_manager, energy_imbalance, paleoclimate_dual_scale, paleoclimate_human_origins_full, paleoclimate_visualization, paleoclimate_visualization_full, paleoclimate_wet_bulb_full, save_utils
**Consumed by:** palomas_orrery

**Public functions:**

- `load_co2_data()` (line 46) -- Load Mauna Loa CO2 data from cache
- `load_temperature_data()` (line 57) -- Load NASA GISS temperature data from cache
- `load_ice_data()` (line 68) -- Load Arctic sea ice extent data from cache
- `create_keeling_curve()` (line 79) -- Create interactive Keeling Curve visualization
- `create_temperature_viz()` (line 201) -- Create interactive temperature anomaly visualization
- `create_monthly_temperature_lines()` (line 342) -- Create year-over-year monthly temperature visualization (line chart).
- `create_warming_stripes()` (line 468) -- Create Ed Hawkins style warming stripes visualization (heatmap).
- `open_monthly_temp_lines()` (line 558) -- Open the monthly temperature year-over-year line chart.
- `open_warming_stripes()` (line 574) -- Open the Ed Hawkins warming stripes heatmap.
- `create_ice_viz()` (line 590) -- Create Arctic sea ice extent visualization - Updated with correct data source
- `load_sea_level_data()` (line 771) -- Load sea level data from cached JSON file
- `create_sea_level_viz()` (line 785) -- Create interactive sea level rise visualization
- `load_ph_data()` (line 938) -- Load ocean pH data from JSON cache
- `create_ph_viz()` (line 950) -- Create interactive ocean acidification (pH) visualization
- `create_planetary_boundaries_viz()` (line 1122) -- Planetary Boundaries - keep Tony's style & notes
- `open_ph_viz()` (line 1410) -- Open ocean pH visualization in browser
- `open_planetary_boundaries()` (line 1430) -- Open Planetary Boundaries visualization in browser
- `open_paleoclimate_viz()` (line 1450) -- Open Cenozoic paleoclimate visualization
- `open_paleoclimate_dual_scale_viz()` (line 1467) -- Open dual-scale paleoclimate visualization (modern + deep time)
- `open_phanerozoic_viz()` (line 1484) -- Open Phanerozoic (540 Ma) paleoclimate visualization
- `open_human_origins_viz()` (line 1505) -- Open Paleoclimate + Human Origins visualization (540 Ma + 25 hominin species)
- `open_sea_level_viz()` (line 1526) -- Open sea level visualization in browser
- `open_keeling_curve()` (line 1547) -- Open Keeling Curve in browser
- `open_temperature_viz()` (line 1561) -- Open temperature visualization in browser
- `open_ice_viz()` (line 1575) -- Open Arctic ice visualization in browser
- `open_energy_imbalance()` (line 1591) -- Open energy imbalance visualization in browser
- `run_update_in_thread(update_button, status_label, window)` (line 1605) -- Run climate data update in background thread
- `open_wet_bulb_viz()` (line 1665) -- Open Wet Bulb Temperature paleoclimate visualization
- `open_google_earth_controller()` (line 1683) -- Launch the Google Earth KML layer controller
- `open_earth_system_gui(parent)` (line 1698) -- Open Earth System Visualization hub window

---

### orbital_param_viz.py

**Role:** gui | **Lines:** 1,936

> orbital_param_viz.py - Interactive orbital element visualization tool.

**Depends on:** apsidal_markers, constants_new, idealized_orbits, palomas_orrery_helpers, shutdown_handler
**Consumed by:** palomas_orrery

**Public functions:**

- `class CreateToolTip` (line 32) -- Create a tooltip for a given widget with intelligent positioning to prevent clipping.
- `rotation_matrix_x(angle)` (line 138) -- Create rotation matrix around X axis
- `rotation_matrix_z(angle)` (line 145) -- Create rotation matrix around Z axis
- `add_coordinate_frame(fig, name, color, R_transform, axis_length, show_labels, opacity, line_width, show_in_legend, visible)` (line 152) -- Add a 3D coordinate frame with the given transformation.
- `add_angle_arc(fig, angle_rad, radius, axis, color, label, start_angle, show_in_legend, legendgroup)` (line 221) -- Add an arc showing a rotation angle
- `create_orbital_transformation_viz(fig, obj_name, planetary_params, show_steps, show_axes, plot_date, center_object, parent_planets, show_apsidal_markers, current_position)` (line 250) -- Create a visualization showing how orbital parameters transform to 3D orbit.
- `create_eccentricity_demo_window(parent, objects, planetary_params_override)` (line 1081) -- Create a window with an interactive eccentricity slider visualization.
- `create_orbital_viz_window(root, objects, planetary_params, parent_planets, current_positions, current_date)` (line 1910) -- Create a window for orbital parameter visualization.
- `create_orbital_transformation_viz_legacy(fig, obj_name, planetary_params)` (line 2291) -- Legacy function for compatibility

---

### palomas_orrery.py

**Role:** gui | **Lines:** 8,254

> palomas_orrery.py - Main GUI and plotting engine for Paloma's Orrery.

**Depends on:** apsidal_markers, asteroid_belt_visualization_shells, celestial_objects, close_approach_data, comet_visualization_shells, constants_new, earth_system_visualization_gui, exoplanet_orbits, exoplanet_stellar_properties, exoplanet_systems, formatting_utils, idealized_orbits, orbit_data_manager, orbital_elements, orbital_param_viz, osculating_cache_manager, palomas_orrery_helpers, planet_visualization, save_utils, sgr_a_grand_tour, shared_utilities, shutdown_handler, social_media_export, solar_visualization_shells, spacecraft_encounters, star_sphere_builder, visualization_utils
**Consumed by:** (none -- standalone)

**Public functions:**

- `get_fetch_interval_for_type(obj_type, obj_name, trajectory_interval, default_interval, satellite_interval, planetary_params)` (line 312) -- Get the appropriate fetch interval based on object type.
- `create_dates_list_for_object(obj, obj_type, date_obj, trajectory_points, orbital_points, satellite_days, satellite_points, start_date, end_date, planetary_params, parent_planets, center_object_name, max_date, settings)` (line 333) -- Create a list of dates for plotting based on object type.
- `handle_update_dialog(num_objects)` (line 415) -- Handle the update dialog for cache updates.
- `get_interval_settings()` (line 477) -- Get all interval settings from the GUI entries.
- `get_date_from_gui()` (line 551) -- Get the date from GUI entry fields.
- `create_animation_dates(current_date, step, N)` (line 570) -- Create dates list specifically for animations.
- `calculate_axis_range_from_orbits(selected_objects, positions, planetary_params, parent_planets, center_object_name)` (line 605) -- Calculate appropriate axis range based on orbital parameters.
- `get_improved_axis_range(scale_var, custom_scale_entry, selected_objects, positions, planetary_params, parent_planets, center_object_name)` (line 817) -- Get axis range using improved scaling logic.
- `get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name)` (line 835) -- Get axis range for animations using the same logic as static plots.
- `calculate_satellite_precession_info(selected_objects, start_date, end_date, center_object_name)` (line 856) -- Calculate precession information for selected satellites based on date range.
- `load_window_config()` (line 1015) -- Load saved window geometry and sash positions from config file.
- `save_window_config()` (line 1025) -- Save current window geometry and sash positions to config file.
- `fetch_position(object_id, date_obj, center_id, id_type, override_location, mission_url, mission_info)` (line 1141)
- `calculate_analytical_position(obj_name, date_obj, center_id)` (line 1617) -- Calculate position from analytical orbital elements when Horizons is unavailable.
- `fetch_radec_for_hover(object_id, date_obj, id_type)` (line 1700) -- Fetch RA/Dec and uncertainties for hover text
- `add_celestial_object(fig, obj_data, name, color, symbol, marker_size, hover_data, center_object_name)` (line 1770)
- `update_status_display(message, status_type)` (line 1843) -- Update status display with color coding and history
- `configure_controls_canvas(event)` (line 1882)
- `class ScrollableFrame` (line 2665) -- A scrollable frame that can contain multiple widgets with a vertical scrollbar.
- `class CreateToolTip` (line 2766) -- Create a tooltip for a given widget with intelligent positioning to prevent clipping.
- `pulse_progress_bar()` (line 2923) -- Create a pulsating effect for the progress bar
- `update_orbit_paths(center_object_name)` (line 2929) -- For each object in the global 'objects' list that has an 'id', check if its orbit path is
- `plot_orbit_paths(fig, objects_to_plot, center_object_name)` (line 3027) -- Plot orbit paths using data from orbit_data_manager or temp cache.
- `plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id, show_lines, center_object_name, show_closest_approach, trajectory_marker_color)` (line 3081) -- Plot actual orbit positions for selected objects.
- `export_social_view()` (line 3482) -- Export the last plotted figure as a social media view.
- `plot_objects()` (line 3509)
- `animate_objects(step, label)` (line 5308)
- `on_closing()` (line 6992) -- Handle cleanup when the main window is closed.
- `periodic_config_save()` (line 7017)
- `set_palomas_birthday()` (line 7024)
- `update_date_fields(new_date)` (line 7028)
- `fill_now()` (line 7041)
- `calculate_next_vernal_equinox(from_date)` (line 7068) -- Calculate the next vernal equinox (March equinox) from a given date.
- `fill_next_vernal_equinox()` (line 7138) -- Fill the date fields with the next vernal equinox from the current date.
- `toggle_all_shells()` (line 7149) -- Toggle all sun shell checkboxes based on the main shell checkbox.
- `handle_mission_selection()` (line 7181)
- `animate_one_minute()` (line 7187)
- `animate_one_hour()` (line 7193)
- `animate_one_day()` (line 7198)
- `animate_one_week()` (line 7204)
- `animate_one_month()` (line 7209)
- `animate_one_year()` (line 7214)
- `animate_palomas_birthday()` (line 7219)
- `report_callback_exception(exc_type, exc_value, exc_traceback)` (line 7249)
- `sync_end_date_from_days()` (line 7261) -- Calculate end date from start date + days to plot
- `sync_days_from_dates()` (line 7292) -- Calculate days to plot from start and end dates
- `sync_days_from_dates()` (line 7304) -- Calculate days to plot from start and end dates
- `sync_end_date_from_days()` (line 7403) -- Calculate end date from start date + days to plot
- `sync_days_from_dates()` (line 7435) -- Calculate days to plot from start and end dates
- `get_end_date_from_gui()` (line 7447) -- Get end date from GUI fields. Defaults empty fields to avoid crash.
- `can_be_horizons_center(obj)` (line 7479) -- Check if object can be used as Horizons coordinate center.
- `create_celestial_checkbutton(name, variable)` (line 7581)
- `create_mission_checkbutton(name, variable, dates)` (line 8111)
- `create_comet_checkbutton(name, variable, dates, perihelion)` (line 8567) -- Creates a checkbutton for a comet with a tooltip containing its description,
- `create_interstellar_checkbutton(name, variable, dates, perihelion)` (line 8685) -- Creates a checkbutton for an interstellar/hyperbolic object with a tooltip
- `toggle_special_fetch_mode()` (line 8782) -- DEPRECATED: Special fetch mode removed - two-layer trajectories provide automatic detail
- `create_exoplanet_checkbutton(name, variable, is_star)` (line 8798) -- Create checkbutton for exoplanet objects
- `open_star_visualization()` (line 8819) -- Inform user about standalone Star Visualization executable.
- `launch_galactic_center()` (line 8892) -- Launch the Sagittarius A* Grand Tour visualization.
- `update_center_dropdown()` (line 9050) -- Update the center dropdown to show only Sun + selected centerable objects.
- `setup_center_dropdown_traces()` (line 9111) -- Add traces to all object IntVars to update center dropdown on selection change.
- `on_center_change()` (line 9129) -- Update frame title when the center object is changed.
- `open_orbital_param_visualization()` (line 9567) -- Opens the orbital parameter visualization window by calling the
- `restore_sash_positions()` (line 9739)

---

### palomas_orrery_dashboard.py

**Role:** gui | **Lines:** 599

> Paloma's Orrery Dashboard Central launch point for the Paloma's Orrery suite.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `class PalomasOrreryDashboard` (line 175) -- Main dashboard window.
- `main()` (line 696)

---

### star_visualization_gui.py

**Role:** gui | **Lines:** 1,406

> star_visualization_gui.py - Stellar visualization GUI for Paloma's Orrery.

**Depends on:** constants_new, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, plot_data_exchange, plot_data_report_widget, report_manager, save_utils, social_media_export, star_notes
**Consumed by:** (none -- standalone)

**Public functions:**

- `is_frozen()` (line 46) -- Check if running as a PyInstaller frozen executable.
- `class ScrollableFrame` (line 72) -- A scrollable frame widget.
- `class LazyStarPropertiesLoader` (line 93) -- Loads star properties on-demand rather than all at startup.
- `class StarVisualizationSearchWidget` (line 198) -- Search widget with unified display for all star information.
- `class StarVisualizationGUI` (line 800) -- Main GUI window with search and visualization controls.

---

## RENDERING: Builds visual traces, figures, and charts

### exoplanet_orbits.py

**Role:** rendering | **Lines:** 613

> exoplanet_orbits.py - Keplerian Orbit Calculations for Exoplanets

**Depends on:** exoplanet_stellar_properties, exoplanet_systems, formatting_utils
**Consumed by:** palomas_orrery

**Public functions:**

- `solve_kepler_equation(M, e, tolerance, max_iterations)` (line 50) -- Solve Kepler's equation: M = E - e*sin(E) for eccentric anomaly E
- `calculate_true_anomaly(E, e)` (line 86) -- Calculate true anomaly from eccentric anomaly
- `calculate_keplerian_orbit(a, e, i_deg, omega_deg, Omega_deg, period_days, epoch, date, num_points)` (line 103) -- Calculate complete orbital path in 3D space
- `calculate_planet_position(a, e, i_deg, omega_deg, Omega_deg, period_days, epoch, date)` (line 170) -- Calculate planet's current position at specific date
- `calculate_binary_star_orbits(star_A_mass, star_B_mass, binary_separation, binary_period, binary_eccentricity)` (line 239) -- Calculate orbital parameters for both stars in binary system
- `calculate_binary_star_position(star_params, date, epoch, i_deg, Omega_deg)` (line 286) -- Calculate position of one star in binary system at given date
- `plot_exoplanet_orbits(fig, exoplanet_objects, host_star_system, date, show_orbits, show_markers)` (line 373) -- Plot exoplanet orbits in Plotly figure
- `plot_binary_host_stars(fig, host_star_system, date, show_orbits, show_markers, system_data)` (line 476) -- Plot binary star system (both stars orbiting barycenter)
- `calculate_exoplanet_axis_range(exoplanet_objects)` (line 670) -- Calculate appropriate axis range for exoplanet system

---

### hr_diagram_apparent_magnitude.py

**Role:** rendering | **Lines:** 430

> hr_diagram_apparent_magnitude.py - HR diagram pipeline for apparent magnitude queries.

**Depends on:** data_acquisition, data_processing, incremental_cache_manager, object_type_analyzer, plot_data_exchange, report_manager, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_2d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 62) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, mag_limit)` (line 123) -- Complete star processing pipeline for magnitude-based visualization.
- `main()` (line 204)

---

### hr_diagram_distance.py

**Role:** rendering | **Lines:** 449

> hr_diagram_distance.py - HR diagram pipeline for distance-based queries.

**Depends on:** catalog_selection, data_acquisition_distance, data_processing, incremental_cache_manager, object_type_analyzer, plot_data_exchange, report_manager, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_2d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 64) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, max_light_years)` (line 126) -- Complete star processing pipeline for distance-based visualization.
- `main()` (line 206)

---

### paleoclimate_dual_scale.py

**Role:** rendering | **Lines:** 955

> Dual-Scale Paleoclimate Visualization for Paloma's Orrery Side-by-side layout: Deep Time (log scale) + Modern Era (linear scale)

**Depends on:** paleoclimate_visualization, save_utils
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `load_modern_temperature_data_ma_bp()` (line 65) -- Load modern instrumental temperature data using Ma BP (Before Present = 2025)
- `load_projection_scenarios()` (line 137) -- Load future climate projection scenarios
- `load_cat_policies_and_action()` (line 234) -- Load Climate Action Tracker "Policies and Action" temperature range
- `create_paleoclimate_dual_scale_visualization()` (line 258) -- Create dual-scale paleoclimate visualization with side-by-side layout
- `main()` (line 1065) -- Test the dual-scale visualization

---

### paleoclimate_human_origins_full.py

**Role:** rendering | **Lines:** 1,884

> Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present)

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `d18o_to_temperature_approx(d18o_values)` (line 235) -- Convert benthic delta18O to approximate temperature anomaly
- `load_lr04_data()` (line 257) -- Load LR04 benthic stack from cache
- `load_scotese_phanerozoic_data()` (line 268) -- Load Scotese et al. (2021) Phanerozoic temperature data
- `load_holocene_data()` (line 325) -- Load Kaufman et al. (2020) Holocene temperature reconstruction
- `calculate_preindustrial_offset(holocene_data)` (line 361) -- Calculate offset to normalize to pre-industrial (1850-1900) baseline
- `load_modern_temperature_data()` (line 391) -- Load modern instrumental temperature data to extend to present
- `create_paleoclimate_visualization()` (line 429) -- Create Phanerozoic paleoclimate visualization
- `main()` (line 2043) -- Test the visualization

---

### paleoclimate_visualization.py

**Role:** rendering | **Lines:** 478

> Paleoclimate Visualization for Paloma's Orrery Cenozoic temperature and CO₂ reconstruction (66 Ma - present)

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui, paleoclimate_dual_scale

**Public functions:**

- `d18o_to_temperature_approx(d18o_values)` (line 58) -- Convert benthic δ18O to approximate temperature anomaly
- `load_lr04_data()` (line 80) -- Load LR04 benthic stack from cache
- `load_holocene_data()` (line 92) -- Load Kaufman et al. (2020) Holocene temperature reconstruction
- `calculate_preindustrial_offset(holocene_data)` (line 128) -- Calculate offset to normalize to pre-industrial (1850-1900) baseline
- `load_modern_temperature_data()` (line 158) -- Load modern instrumental temperature data to extend to present
- `create_paleoclimate_visualization()` (line 196) -- Create Cenozoic paleoclimate visualization
- `main()` (line 539) -- Test the visualization

---

### paleoclimate_visualization_full.py

**Role:** rendering | **Lines:** 1,487

> Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present)

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `d18o_to_temperature_approx(d18o_values)` (line 61) -- Convert benthic delta18O to approximate temperature anomaly
- `load_lr04_data()` (line 83) -- Load LR04 benthic stack from cache
- `load_scotese_phanerozoic_data()` (line 94) -- Load Scotese et al. (2021) Phanerozoic temperature data
- `load_holocene_data()` (line 151) -- Load Kaufman et al. (2020) Holocene temperature reconstruction
- `calculate_preindustrial_offset(holocene_data)` (line 187) -- Calculate offset to normalize to pre-industrial (1850-1900) baseline
- `load_modern_temperature_data()` (line 217) -- Load modern instrumental temperature data to extend to present
- `create_paleoclimate_visualization()` (line 255) -- Create Phanerozoic paleoclimate visualization
- `main()` (line 1613) -- Test the visualization

---

### paleoclimate_wet_bulb_full.py

**Role:** rendering | **Lines:** 2,224

> Paleoclimate + Wet Bulb Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) with human survivability context

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `date_to_age_ma(date_str, reference_year)` (line 315) -- Convert a date string (YYYY-MM-DD) to age in millions of years before present.
- `d18o_to_temperature_approx(d18o_values)` (line 345) -- Convert benthic delta18O to approximate temperature anomaly
- `load_lr04_data()` (line 367) -- Load LR04 benthic stack from cache
- `load_scotese_phanerozoic_data()` (line 378) -- Load Scotese et al. (2021) Phanerozoic temperature data
- `load_holocene_data()` (line 435) -- Load Kaufman et al. (2020) Holocene temperature reconstruction
- `calculate_preindustrial_offset(holocene_data)` (line 471) -- Calculate offset to normalize to pre-industrial (1850-1900) baseline
- `load_modern_temperature_data()` (line 501) -- Load modern instrumental temperature data to extend to present.
- `calculate_trendline_points(events, num_points)` (line 572) -- Calculate linear regression in TIME (Years), then generate
- `create_paleoclimate_visualization()` (line 613) -- Create Phanerozoic paleoclimate visualization
- `main()` (line 2447) -- Test the visualization

---

### planet_visualization.py

**Role:** rendering | **Lines:** 1,046

> Celestial Body Visualization Module Functions for creating layered visualizations of solar system bodies (Sun, planets) in 3D plots. Each celestial body has individual shell components that can be toggled with selection variables.

**Depends on:** asteroid_belt_visualization_shells, constants_new, earth_visualization_shells, eris_visualization_shells, jupiter_visualization_shells, mars_visualization_shells, mercury_visualization_shells, moon_visualization_shells, neptune_visualization_shells, planet9_visualization_shells, planet_visualization_utilities, pluto_visualization_shells, saturn_visualization_shells, solar_visualization_shells, uranus_visualization_shells, venus_visualization_shells
**Consumed by:** palomas_orrery, palomas_orrery_helpers

**Public functions:**

- `create_sun_visualization(fig, sun_shell_vars, animate, frames)` (line 328) -- Creates a visualization of the Sun's layers based on which shells are selected.
- `create_sun_corona_from_distance(fig, sun_shell_vars, sun_position)` (line 442) -- Creates a simplified Sun corona visualization for non-Sun-centered views.
- `create_celestial_body_visualization(fig, body_name, shell_vars, animate, frames, center_position)` (line 562) -- Unified function to create shell visualizations for any celestial body (Sun or planets).
- `create_planet_visualization(fig, planet_name, shell_vars, animate, frames, center_position)` (line 902) -- Creates a visualization of a planet's layers based on which shells are selected.
- `create_planet_shell_traces(planet_name, shell_vars, center_position)` (line 1138) -- Creates traces for planet shells without adding them to a figure.

---

### planet_visualization_utilities.py

**Role:** rendering | **Lines:** 290

> Celestial Body Visualization Module Functions for creating layered visualizations of solar system bodies (Sun, planets) in 3D plots. Each celestial body has individual shell components that can be toggled with selection variables.

**Depends on:** constants_new
**Consumed by:** comet_visualization_shells, earth_visualization_shells, eris_visualization_shells, jupiter_visualization_shells, mars_visualization_shells, mercury_visualization_shells, moon_visualization_shells, neptune_visualization_shells, planet9_visualization_shells, planet_visualization, pluto_visualization_shells, saturn_visualization_shells, solar_visualization_shells, uranus_visualization_shells, venus_visualization_shells

**Public functions:**

- `rotate_points(x, y, z, angle, axis)` (line 92) -- Rotate points around a specified axis by the given angle.
- `create_hover_markers_for_planet(center_position, radius, color, name, description, num_points)` (line 140) -- Creates clean hover markers for a planet with proper hover text formatting.
- `create_magnetosphere_shape(params)` (line 197) -- Creates points for a magnetosphere with asymmetry, compressed on sunward side
- `create_sphere_points(radius, n_points)` (line 251) -- Create points for a sphere surface to represent celestial body layers.
- `create_sun_direction_indicator_old(center_position)` (line 272) -- Creates a visual indicator showing the direction to the Sun (along negative X-axis).

---

### planetarium_apparent_magnitude.py

**Role:** rendering | **Lines:** 352

> planetarium_apparent_magnitude.py - Create 3D visualization for stars brighter than specified apparent magnitude.

**Depends on:** data_acquisition, data_processing, incremental_cache_manager, messier_object_data_handler, shutdown_handler, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_3d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 48) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, mag_limit)` (line 109) -- Complete star processing pipeline for magnitude-based 3D visualization.
- `main()` (line 186)

---

### planetarium_distance.py

**Role:** rendering | **Lines:** 399

> planetarium_distance.py - 3D star field pipeline for distance-based queries.

**Depends on:** catalog_selection, data_acquisition, data_processing, incremental_cache_manager, shutdown_handler, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_3d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 66) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, max_light_years)` (line 127) -- Complete star processing pipeline for distance-based 3D visualization.
- `main()` (line 214)

---

### plot_data_report_widget.py

**Role:** rendering | **Lines:** 560

> plot_data_report_widget.py - Embedded report panel for star visualization results.

**Depends on:** object_type_analyzer, report_manager
**Consumed by:** star_visualization_gui

**Public functions:**

- `class PlotDataReportWidget` (line 29) -- Widget for displaying comprehensive plot data report.
- `add_plot_report_to_gui(parent_frame, column, row)` (line 660) -- Add the plot report widget to the star visualization GUI.

---

### sgr_a_grand_tour.py

**Role:** rendering | **Lines:** 742

> sgr_a_grand_tour.py Stage 4 FINAL: The Grand Tour of the Galactic Center

**Depends on:** save_utils, sgr_a_star_data, sgr_a_visualization_core
**Consumed by:** palomas_orrery

**Public functions:**

- `generate_rosette_trace(star_name, num_orbits, points_per_orbit)` (line 68) -- Generate the relativistic spirograph trace for a star.
- `get_phase_offset(star_data, reference_year)` (line 109) -- Calculate orbital phase offset from observed periapsis times.
- `get_current_position_info(star_name, reference_year)` (line 125) -- Get descriptive info about a star's current orbital position.
- `create_grand_tour_dashboard()` (line 160) -- Build the complete Grand Tour dashboard with unified color spectrum

---

### sgr_a_visualization_animation.py

**Role:** rendering | **Lines:** 343

> sgr_a_visualization_animation.py Stage 2: Animated visualization of S-Stars orbiting Sagittarius A*.

**Depends on:** save_utils, sgr_a_star_data, sgr_a_visualization_core
**Consumed by:** (none -- standalone)

**Public functions:**

- `calculate_star_position_at_mean_anomaly(star_data, mean_anomaly_rad)` (line 36) -- Given a mean anomaly M, calculate the star's 3D position and velocity.
- `get_phase_offset(star_data, reference_year)` (line 59) -- Calculate phase offset so stars start at their actual orbital positions
- `format_velocity_display(v_km_s)` (line 75) -- Format velocity for display in animation.
- `create_animation(stars_to_show, reference_year)` (line 87) -- Create animated visualization of S-stars orbiting Sgr A*.
- `create_single_star_animation(star_name, num_orbits)` (line 373) -- Create animation focused on a single star, showing multiple orbits

---

### sgr_a_visualization_core.py

**Role:** rendering | **Lines:** 557

> sgr_a_visualization_core.py Core visualization module for S-Stars orbiting Sagittarius A*.

**Depends on:** save_utils, sgr_a_star_data
**Consumed by:** sgr_a_grand_tour, sgr_a_visualization_animation, sgr_a_visualization_precession

**Public functions:**

- `generate_orbit_points(star_data, num_points, precession_offset_deg)` (line 36) -- Generate 3D orbit points for a star.
- `generate_position_at_true_anomaly(star_data, true_anomaly_rad, precession_offset_deg)` (line 101) -- Generate 3D position for a star at a specific true anomaly.
- `create_sgr_a_marker(scale_factor)` (line 150) -- Create the Sagittarius A* black hole marker.
- `create_orbit_trace(star_name, star_data, show_periapsis)` (line 405) -- Create the orbital path trace for a star.
- `create_star_marker(star_name, star_data, true_anomaly_rad, precession_offset_deg)` (line 483) -- Create a marker showing the star's current position.
- `create_sgr_a_figure(stars_to_show, show_all_stars)` (line 535) -- Create the main Sagittarius A* visualization figure.

---

### sgr_a_visualization_precession.py

**Role:** rendering | **Lines:** 377

> sgr_a_visualization_precession.py Stage 3: The Relativistic Rosette (Schwarzschild Precession).

**Depends on:** save_utils, sgr_a_star_data, sgr_a_visualization_core
**Consumed by:** (none -- standalone)

**Public functions:**

- `apply_accuracy_patches()` (line 36) -- Apply literature-based corrections to orbital elements.
- `generate_rosette_trace(star_name, num_orbits, points_per_orbit)` (line 55) -- Generate a continuous 3D trace of a precessing orbit over many cycles.
- `generate_single_orbit_trace(star_name, precession_offset_deg)` (line 114) -- Generate a single orbit for comparison/overlay.
- `create_rosette_visualization(stars_to_show)` (line 124) -- Create the rosette visualization showing Schwarzschild precession.
- `create_single_star_rosette(star_name, num_orbits)` (line 310) -- Create a focused rosette visualization for a single star.
- `create_newton_vs_einstein_comparison(star_name)` (line 321) -- Create a side-by-side comparison showing:

---

### star_sphere_builder.py

**Role:** rendering | **Lines:** 922

> star_sphere_builder.py - Build and render celestial sphere for Paloma's Orrery.

**Depends on:** (none)
**Consumed by:** palomas_orrery

**Public functions:**

- `find_hipparcos_vot()` (line 67) -- Locate the Hipparcos VOT cache file.
- `equatorial_to_ecliptic_unit_vector(ra_deg, dec_deg)` (line 75) -- Convert equatorial RA/Dec (ICRS, degrees) to a unit vector in
- `ecliptic_longitude_to_unit_vector(lon_deg)` (line 104) -- Convert ecliptic longitude (degrees) to unit vector in ecliptic frame.
- `generate_great_circle_ecliptic(n_points)` (line 113) -- Generate points along the ecliptic great circle.
- `generate_great_circle_equator(n_points)` (line 127) -- Generate points along the celestial equator in ecliptic coordinates.
- `generate_great_circle_prime_meridian(n_points)` (line 150) -- Generate points along the RA=0h / RA=12h great circle in ecliptic coordinates.
- `load_simbad_names()` (line 176) -- Load star designations from the SIMBAD properties cache.
- `build_star_data(vot_path, simbad_names)` (line 206) -- Build the star array from Hipparcos VOT data.
- `build_grid_data()` (line 297) -- Build celestial grid data: ecliptic, equator, poles, zodiac labels.
- `build_centroid_data(stars, hip_to_index)` (line 525) -- Build constellation centroid data: brightness-weighted centroid positions
- `build_json(vot_path)` (line 606) -- Main build routine.
- `load_star_sphere_data()` (line 671) -- Load celestial sphere JSON data, caching in memory after first load.
- `add_celestial_sphere_traces(fig, axis_range, show_stars, show_names, show_grid, show_labels, show_constellation_names)` (line 697) -- Add celestial sphere traces to a Plotly 3D figure.

---

### visualization_2d.py

**Role:** rendering | **Lines:** 524

> visualization_2d.py - 2D HR diagram (color-magnitude) plot builder.

**Depends on:** constants_new, save_utils, solar_visualization_shells, star_notes, visualization_core, visualization_utils
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance

**Public functions:**

- `format_value(value, format_spec, default)` (line 34) -- Format a value using Python's built-in format function.
- `create_hover_text(df, include_3d)` (line 44) -- Create hover text with graceful handling of missing columns.
- `prepare_2d_data(combined_data)` (line 134) -- Prepare data for plotting.
- `generate_footer_text(counts_dict, estimation_results, mag_limit, max_light_years)` (line 207) -- Generate updated footer text including estimation information.
- `create_hr_diagram(combined_df, counts_dict, mag_limit, max_light_years)` (line 272) -- Create HR diagram for either magnitude or distance-based data.

---

### visualization_3d.py

**Role:** rendering | **Lines:** 858

> visualization_3d.py - 3D stellar neighborhood and planetarium plot builder.

**Depends on:** constants_new, save_utils, solar_visualization_shells, star_notes, visualization_core
**Consumed by:** planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `parse_stellar_classes(df)` (line 38) -- Parse stellar classes from spectral types.
- `expand_object_type(ot)` (line 52) -- Expand object type codes to full descriptions.
- `prepare_3d_data(combined_df, max_value, counts, mode)` (line 75) -- Prepare data for 3D visualization with proper handling of Messier objects.
- `format_value(value, format_spec, default)` (line 186) -- Format a value using Python's built-in format function.
- `create_hover_text(df, include_3d)` (line 208) -- Create hover text with graceful handling of missing columns.
- `create_hover_text_old(df, include_3d)` (line 297) -- Create hover text with graceful handling of missing columns.
- `create_notable_stars_list(combined_df, unique_notes, user_max_coord)` (line 344) -- Create list of notable stars, using vector distance for filtering.
- `create_3d_visualization(combined_df, max_value, user_max_coord)` (line 447) -- Create 3D visualization of stellar neighborhood or magnitude-limited stars.

---

### visualization_core.py

**Role:** rendering | **Lines:** 351

> visualization_core.py - Shared data preparation and formatting for star visualizations.

**Depends on:** constants_new, solar_visualization_shells, star_notes, stellar_parameters
**Consumed by:** exoplanet_stellar_properties, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, visualization_2d, visualization_3d

**Public functions:**

- `format_value(value, format_spec, default)` (line 24) -- Format values consistently across visualizations.
- `create_hover_text(df, include_3d)` (line 35) -- Create hover text for plots with identification of estimated values and special cases.
- `prepare_temperature_colors()` (line 160) -- Define consistent temperature color scales.
- `analyze_star_counts(combined_df)` (line 174) -- Analyze star counts and exclusion reasons in detail.
- `analyze_magnitude_distribution(data, mag_limit)` (line 230) -- Analyze and print the distribution of stars by magnitude ranges.
- `analyze_and_report_stars(combined_df, mode, max_value)` (line 292) -- Analyze star data and report statistics for both distance and magnitude-limited samples.
- `generate_star_count_text(counts_dict, combined_df)` (line 386) -- Generate detailed text about star counts from different catalogs.

---

### visualization_utils.py

**Role:** rendering | **Lines:** 725

> visualization_utils.py - Shared Plotly utilities for orrery and star visualizations.

**Depends on:** celestial_coordinates, formatting_utils, idealized_orbits
**Consumed by:** palomas_orrery, palomas_orrery_helpers, visualization_2d

**Public functions:**

- `add_hover_toggle_buttons(fig)` (line 24) -- Add hover text toggle buttons to any Plotly figure.
- `add_camera_center_button(fig, center_object_name)` (line 83) -- Add a button to move the camera to the center object.
- `add_look_at_object_buttons(fig, positions, center_object_name, target_objects)` (line 158) -- Add buttons to point camera from center toward specific target objects.
- `add_fly_to_object_buttons(fig, positions, center_object_name, target_objects, fly_distance, distance_scale_factor)` (line 363) -- Add buttons to fly the camera TO specific target objects, keeping focus on the object.
- `format_hover_text(obj_data, name, is_solar_system)` (line 561) -- Format hover text consistently for different types of objects.
- `format_detailed_hover_text(obj_data, obj_name, center_object_name, objects, planetary_params, parent_planets, CENTER_BODY_RADII, KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS)` (line 620) -- Generate detailed hover text for celestial objects with comprehensive information.
- `update_figure_frames(fig, include_hover_toggle)` (line 843) -- Update figure frames to maintain hover text toggle functionality in animations.

---

## RENDERING/SHELLS: Planetary shell visualizations (sphere layers)

### asteroid_belt_visualization_shells.py

**Role:** rendering/shells | **Lines:** 410

> Asteroid Belt Visualization Module Functions for creating visualizations of asteroid belt structures in 3D plots. Includes Main Belt, Hildas, Trojans, and Greeks. Also includes helper functions for dynamic Trojan positioning based on Jupiter's location.

**Depends on:** shared_utilities
**Consumed by:** palomas_orrery, planet_visualization

**Public functions:**

- `calculate_body_angle(x, y)` (line 17) -- Calculate the orbital angle of a body from its x,y coordinates.
- `get_jupiter_angle_from_data(ephemeris_data, date_index)` (line 35) -- Extract Jupiter's angle from ephemeris data.
- `estimate_jupiter_angle_from_date(date_str)` (line 61) -- Estimate Jupiter's orbital angle from a date string.
- `create_main_asteroid_belt(center_position)` (line 124) -- Creates a visualization of the main asteroid belt with density variations and Kirkwood gaps.
- `create_hilda_group(center_position)` (line 245) -- Creates a visualization of the Hilda asteroid group showing triangular structure.
- `create_jupiter_trojans_greeks(center_position, jupiter_angle)` (line 338) -- Creates a visualization of Jupiter's L4 Trojan asteroids (Greek camp).
- `create_jupiter_trojans_trojans(center_position, jupiter_angle)` (line 430) -- Creates a visualization of Jupiter's L5 Trojan asteroids (Trojan camp).

---

### comet_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,647

> comet_visualization_shells.py - Comet visual components for 3D orrery plots.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** palomas_orrery

**Public functions:**

- `calculate_tail_activity_factor(current_distance_au, perihelion_distance_au, max_active_distance_au)` (line 337) -- Calculate how active the comet is based on solar distance.
- `create_comet_nucleus(center_position, nucleus_size_km, comet_name)` (line 373) -- Creates a comet nucleus visualization as a single point.
- `create_maps_disintegration_marker(position_au, comet_name)` (line 418)
- `create_maps_ghost_tail_trace(fig)` (line 505) -- Ghost tail arc for MAPS C/2026 A1, overlaid on the perihelion
- `create_comet_coma(center_position, coma_radius_km, activity_factor, comet_name)` (line 664) -- Creates the coma (atmosphere) around the nucleus.
- `create_comet_dust_tail(center_position, velocity_vector, max_tail_length_mkm, activity_factor, comet_name, num_particles)` (line 751) -- Creates the dust tail (Type II tail).
- `create_comet_ion_tail(center_position, max_tail_length_mkm, activity_factor, comet_name, num_particles)` (line 922) -- Creates the ion tail (Type I tail, plasma tail).
- `create_comet_anti_tail(center_position, anti_tail_length_km, activity_factor, comet_name, anti_tail_color, collimation_ratio, num_particles)` (line 1054) -- Creates anti-tail jet structure pointing TOWARD the Sun.
- `create_complete_comet_visualization(comet_name, center_position, velocity_vector, current_distance_au)` (line 1235) -- Creates a complete comet visualization with nucleus, coma, and both tails.
- `add_comet_tails_to_figure(fig, comet_name, position_data, center_object_name, current_date)` (line 1450) -- Add comet visualization to figure with feature-specific thresholds.

---

### earth_visualization_shells.py

**Role:** rendering/shells | **Lines:** 846

> earth_visualization_shells.py - Earth interior and orbital shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_earth_inner_core_shell(center_position)` (line 29) -- Creates Earth's inner core shell.
- `create_earth_outer_core_shell(center_position)` (line 85) -- Creates Earth's outer core shell.
- `create_earth_lower_mantle_shell(center_position)` (line 140) -- Creates Earth's lower mantle shell.
- `create_earth_upper_mantle_shell(center_position)` (line 194) -- Creates Earth's upper mantle shell.
- `create_earth_crust_shell(center_position)` (line 248) -- Creates Earth's crust shell using Mesh3d for better performance with improved hover.
- `create_earth_atmosphere_shell(center_position)` (line 405) -- Creates Earth's lower atmosphere shell.
- `create_earth_upper_atmosphere_shell(center_position)` (line 460) -- Creates Earth's upper atmosphere shell.
- `create_earth_magnetosphere_shell(center_position)` (line 532) -- Creates Earth's magnetosphere.
- `create_earth_leo_shell(center_position)` (line 752) -- Creates a representation of Earth's Low Earth Orbit (LEO) shell.
- `create_earth_geostationary_belt_shell(center_position)` (line 850) -- Creates a representation of Earth's geostationary satellite belt at 42,164 km.
- `create_earth_hill_sphere_shell(center_position)` (line 938) -- Creates Earth's Hill sphere.

---

### eris_visualization_shells.py

**Role:** rendering/shells | **Lines:** 407

> eris_visualization_shells.py - Eris interior and boundary shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_eris_core_shell(center_position)` (line 28) -- Creates Eris's core shell.
- `create_eris_mantle_shell(center_position)` (line 107) -- Creates Eris's mantle shell.
- `create_eris_crust_shell(center_position)` (line 163) -- Creates eris's cloud layer shell.
- `create_eris_atmosphere_shell(center_position)` (line 327) -- Creates eris's atmosphere shell.
- `create_eris_hill_sphere_shell(center_position)` (line 410) -- Creates Eris's Hill sphere shell.

---

### jupiter_visualization_shells.py

**Role:** rendering/shells | **Lines:** 778

> jupiter_visualization_shells.py - Jupiter interior, ring, and magnetosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_ring_points_jupiter(inner_radius, outer_radius, n_points, thickness)` (line 19) -- Create points for a ring structure (for planets like Saturn).
- `create_jupiter_core_shell(center_position)` (line 69) -- Creates Jupiter's core shell.
- `create_jupiter_metallic_hydrogen_shell(center_position)` (line 123) -- Creates Jupiter's metallic hydrogen shell.
- `create_jupiter_molecular_hydrogen_shell(center_position)` (line 178) -- Creates Jupiter's molecular hydrogen shell.
- `create_jupiter_cloud_layer_shell(center_position)` (line 236) -- Creates Jupiter's cloud layer shell.
- `create_jupiter_upper_atmosphere_shell(center_position)` (line 397) -- Creates Jupiter's upper atmosphere shell.
- `create_jupiter_magnetosphere(center_position)` (line 452) -- Creates Jupiter's main magnetosphere structure.
- `create_jupiter_io_plasma_torus(center_position)` (line 516) -- Creates Jupiter's Io plasma torus.
- `create_jupiter_radiation_belts(center_position)` (line 599) -- Creates Jupiter's radiation belts.
- `create_jupiter_hill_sphere_shell(center_position)` (line 693) -- Creates Jupiter's Hill sphere shell.
- `create_jupiter_ring_system(center_position)` (line 775) -- Creates a visualization of Jupiter's ring system.

---

### mars_visualization_shells.py

**Role:** rendering/shells | **Lines:** 710

> mars_visualization_shells.py - Mars interior and remnant field shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_mars_inner_core_shell(center_position)` (line 26) -- Creates Mars's inner core shell.
- `create_mars_outer_core_shell(center_position)` (line 104) -- Creates Mars's outer core shell.
- `create_mars_mantle_shell(center_position)` (line 173) -- Creates Mars's mantle shell.
- `create_mars_crust_shell(center_position)` (line 228) -- Creates Mars's crust shell using Mesh3d for better performance with improved hover.
- `create_mars_atmosphere_shell(center_position)` (line 386) -- Creates Mars's lower atmosphere shell.
- `create_mars_upper_atmosphere_shell(center_position)` (line 454) -- Creates Mars's upper atmosphere shell.
- `create_mars_magnetosphere_shell(center_position)` (line 527) -- Creates Mars' induced magnetosphere and localized crustal magnetic fields.
- `create_mars_hill_sphere_shell(center_position)` (line 749) -- Creates Mars's Hill sphere.

---

### mercury_visualization_shells.py

**Role:** rendering/shells | **Lines:** 650

> mercury_visualization_shells.py - Mercury interior, exosphere, and unique feature traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_mercury_inner_core_shell(center_position)` (line 28) -- Creates Mercury's inner core shell.
- `create_mercury_outer_core_shell(center_position)` (line 79) -- Creates Mercury's outer core shell.
- `create_mercury_mantle_shell(center_position)` (line 130) -- Creates Mercury's mantle shell.
- `create_mercury_crust_shell(center_position)` (line 183) -- Creates Mercury's crust shell using Mesh3d for better performance with improved hover.
- `create_mercury_atmosphere_shell(center_position)` (line 339) -- Creates Mercury's atmosphere shell.
- `create_mercury_sodium_tail(center_position)` (line 417) -- Creates Mercury's sodium tail visualization extending away from the Sun.
- `create_mercury_magnetosphere_shell(center_position)` (line 533) -- Creates Mercury's magnetosphere.
- `create_mercury_hill_sphere_shell(center_position)` (line 705) -- Creates Mercury's Hill sphere.

---

### moon_visualization_shells.py

**Role:** rendering/shells | **Lines:** 442

> moon_visualization_shells.py - Lunar interior and exosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_moon_inner_core_shell(center_position)` (line 25) -- Creates the Moon's inner core shell.
- `create_moon_outer_core_shell(center_position)` (line 77) -- Creates the Moon's outer core shell.
- `create_moon_mantle_shell(center_position)` (line 139) -- Creates the Moon's lower mantle shell.
- `create_moon_crust_shell(center_position)` (line 213) -- Creates Earth's crust shell using Mesh3d for better performance with improved hover.
- `create_moon_exosphere_shell(center_position)` (line 396) -- Creates the Moon's exosphere shell.
- `create_moon_hill_sphere_shell(center_position)` (line 459) -- Creates the Moon's Hill sphere.

---

### neptune_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,513

> neptune_visualization_shells.py - Neptune interior, ring, and magnetosphere shell traces.

**Depends on:** planet_visualization_utilities, saturn_visualization_shells, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_neptune_core_shell(center_position)` (line 29) -- Creates Neptune's core shell.
- `create_neptune_mantle_shell(center_position)` (line 86) -- Creates Neptune's mantle shell.
- `create_neptune_cloud_layer_shell(center_position)` (line 157) -- Creates neptune's cloud layer shell.
- `create_neptune_upper_atmosphere_shell(center_position)` (line 326) -- Creates Neptune's upper atmosphere shell.
- `create_neptune_magnetosphere(center_position)` (line 414) -- Creates Neptune's main magnetosphere structure with proper tilt and offset.
- `create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth)` (line 570) -- Creates a simplified visualization of Neptune's magnetic poles and axis.
- `create_neptune_field_lines(mag_center_x, mag_center_y, mag_center_z, north_x, north_y, north_z, south_x, south_y, south_z, neptune_radius, tilt, azimuth)` (line 704) -- Creates a simple visualization of Neptune's magnetic field lines.
- `create_neptune_radiation_belts(center_position)` (line 801) -- Creates Neptune's radiation belts with proper structure reflecting the complex magnetospheric environment.
- `create_field_aligned_currents(mag_center_x, mag_center_y, mag_center_z, tilt, azimuth)` (line 1027) -- Creates visualization of field-aligned currents in Neptune's magnetosphere.
- `create_neptune_ring_system(center_position)` (line 1169) -- Creates a visualization of Neptune's ring system with proper alignment.
- `create_neptune_hill_sphere_shell(center_position)` (line 1667) -- Creates neptune's Hill sphere shell.

---

### planet9_visualization_shells.py

**Role:** rendering/shells | **Lines:** 243

> planet9_visualization_shells.py - Hypothetical Planet 9 shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_planet9_surface_shell(center_position)` (line 29) -- Creates eris's cloud layer shell.
- `create_planet9_hill_sphere_shell(center_position)` (line 204) -- Creates Planet 9's Hill sphere shell.

---

### pluto_visualization_shells.py

**Role:** rendering/shells | **Lines:** 484

> pluto_visualization_shells.py - Pluto interior and atmosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_pluto_core_shell(center_position)` (line 27) -- Creates pluto's core shell.
- `create_pluto_mantle_shell(center_position)` (line 96) -- Creates pluto's mantle shell.
- `create_pluto_crust_shell(center_position)` (line 160) -- Creates pluto's cloud layer shell.
- `create_pluto_haze_layer_shell(center_position)` (line 331) -- Creates pluto's haze layer shell.
- `create_pluto_atmosphere_shell(center_position)` (line 413) -- Creates pluto's atmosphere shell.
- `create_pluto_hill_sphere_shell(center_position)` (line 495) -- Creates pluto's Hill sphere shell.

---

### saturn_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,002

> saturn_visualization_shells.py - Saturn interior, ring, and magnetosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** neptune_visualization_shells, planet_visualization, uranus_visualization_shells

**Public functions:**

- `create_ring_points_saturn(inner_radius, outer_radius, n_points, thickness)` (line 18) -- Create points for a ring with inner and outer radius.
- `create_saturn_core_shell(center_position)` (line 61) -- Creates saturn's core shell.
- `create_saturn_metallic_hydrogen_shell(center_position)` (line 131) -- Creates Saturn's liquid metallic hydrogen shell.
- `create_saturn_molecular_hydrogen_shell(center_position)` (line 192) -- Creates Saturn's molecular hydrogen shell.
- `create_saturn_cloud_layer_shell(center_position)` (line 256) -- Creates Saturn's cloud layer shell.
- `create_saturn_upper_atmosphere_shell(center_position)` (line 464) -- Creates Saturn's upper atmosphere shell.
- `create_saturn_magnetosphere(center_position)` (line 566) -- Creates Saturn's main magnetosphere structure.
- `create_saturn_enceladus_plasma_torus(center_position)` (line 631) -- Creates Saturn's Enceladus plasma torus.
- `create_saturn_radiation_belts(center_position)` (line 737) -- Creates Saturn's radiation belts.
- `create_saturn_hill_sphere_shell(center_position)` (line 875) -- Creates Saturn's Hill sphere shell.
- `create_saturn_ring_system(center_position)` (line 954) -- Creates a visualization of Saturn's ring system.

---

### solar_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,437

> solar_visualization_shells.py - Sun interior, corona, and heliosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** palomas_orrery, palomas_orrery_helpers, planet_visualization, visualization_2d, visualization_3d, visualization_core

**Public functions:**

- `create_sun_hover_text()` (line 868)
- `create_corona_sphere(radius, n_points)` (line 905) -- Create points for a sphere surface to represent corona layers.
- `create_sun_gravitational_shell()` (line 941) -- Creates the Sun's gravitational influence shell.
- `create_sun_outer_oort_shell()` (line 968) -- Creates the Sun's outer Oort cloud shell.
- `create_sun_inner_oort_shell()` (line 995) -- Creates the Sun's inner Oort cloud shell.
- `create_sun_inner_oort_limit_shell()` (line 1022) -- Creates the inner limit of the Sun's Oort cloud shell.
- `create_sun_heliopause_shell()` (line 1049) -- Creates the Sun's heliopause shell.
- `create_sun_termination_shock_shell()` (line 1076) -- Creates the Sun's termination shock shell.
- `create_sun_outer_corona_shell()` (line 1103) -- Creates the Sun's extended outer corona (F-corona) shell.
- `create_sun_inner_corona_shell()` (line 1130) -- Creates the Sun's inner corona (K-corona) shell.
- `create_sun_streamer_belt_shell()` (line 1157) -- Visible white-light corona / helmet streamer belt: ~4-6 solar radii.
- `create_sun_roche_limit_shell()` (line 1188) -- Fluid Roche limit for cometary bodies: ~3.45 solar radii (~0.016 AU).
- `create_sun_alfven_surface_shell()` (line 1222) -- Alfven surface: the true outer boundary of the solar corona (~18.8 solar radii,
- `create_sun_chromosphere_shell()` (line 1255) -- Creates the Sun's chromosphere shell.
- `create_sun_photosphere_shell()` (line 1282) -- Creates the Sun's photosphere shell (the visible solar surface).
- `create_sun_radiative_shell()` (line 1309) -- Creates the Sun's radiative zone shell.
- `create_sun_core_shell()` (line 1336) -- Creates the Sun's core shell.
- `create_sun_hills_cloud_torus(inner_radius, outer_radius, thickness_ratio)` (line 1374) -- Create a toroidal (doughnut-shaped) Hills Cloud structure.
- `create_sun_outer_oort_clumpy(radius_min, radius_max, n_clumps)` (line 1435) -- Create a clumpy, asymmetric outer Oort Cloud with density variations.
- `create_sun_galactic_tide(radius, n_points)` (line 1503) -- Create Oort Cloud structure influenced by galactic tidal forces.
- `create_enhanced_oort_cloud_visualization()` (line 1552) -- Create a more scientifically accurate Oort Cloud visualization.
- `create_oort_cloud_density_visualization()` (line 1620) -- Alternative approach: Show Oort Cloud as density gradients rather than discrete shells.

---

### uranus_visualization_shells.py

**Role:** rendering/shells | **Lines:** 988

> uranus_visualization_shells.py - Uranus interior, ring, and magnetosphere shell traces.

**Depends on:** planet_visualization_utilities, saturn_visualization_shells, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_uranus_core_shell(center_position)` (line 30) -- Creates Uranus's core shell.
- `create_uranus_mantle_shell(center_position)` (line 85) -- Creates Uranus's matel shell.
- `create_uranus_cloud_layer_shell(center_position)` (line 149) -- Creates Uranus's cloud layer shell.
- `create_uranus_upper_atmosphere_shell(center_position)` (line 331) -- Creates Uranus's upper atmosphere shell.
- `create_uranus_magnetosphere(center_position)` (line 414) -- Creates Uranus's main magnetosphere structure.
- `create_uranus_radiation_belts(center_position)` (line 505) -- Creates Uranus's radiation belts.
- `create_uranus_ring_system(center_position)` (line 711) -- Creates a visualization of Saturn's ring system.
- `create_uranus_hill_sphere_shell(center_position)` (line 1063) -- Creates Uranus's Hill sphere shell.

---

### venus_visualization_shells.py

**Role:** rendering/shells | **Lines:** 619

> venus_visualization_shells.py - Venus interior and atmosphere shell traces.

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_venus_core_shell(center_position)` (line 28) -- Creates Venus's core shell.
- `create_venus_mantle_shell(center_position)` (line 81) -- Creates Venus's mantle shell.
- `create_venus_crust_shell(center_position)` (line 134) -- Creates Venus's crust shell using Mesh3d for better performance with improved hover.
- `create_venus_atmosphere_shell(center_position)` (line 293) -- Creates Venus's lower atmosphere shell.
- `create_venus_upper_atmosphere_shell(center_position)` (line 352) -- Creates Venus's upper atmosphere shell.
- `create_venus_magnetosphere_shell(center_position)` (line 452) -- Creates Venus's magnetosphere.
- `create_venus_hill_sphere_shell(center_position)` (line 655) -- Creates Venus's Hill sphere.

---

## COMPUTATION: Math, orbital mechanics, data processing

### apsidal_markers.py

**Role:** computation | **Lines:** 1,681

> Module for calculating perihelion, apohelion, perigee, and apogee dates based on current orbital positions and orbital elements.

**Depends on:** constants_new
**Consumed by:** close_approach_data, idealized_orbits, orbital_param_viz, palomas_orrery

**Public functions:**

- `get_apsidal_terms(center_body)` (line 55) -- Get appropriate apsidal terminology for a given central body.
- `calculate_orbital_angle_shift(ideal_pos, actual_pos)` (line 90) -- Calculate the angular separation between Keplerian and actual positions.
- `create_enhanced_apsidal_hover_text(obj_name, marker_type, date, actual_pos, ideal_pos, params, is_perihelion, center_body)` (line 120) -- Create informative hover text for apsidal markers with perturbation notes.
- `add_actual_apsidal_markers_enhanced(fig, obj_name, params, date_range, positions_dict, color_map, center_body, is_satellite, ideal_apsides, filter_by_date_range)` (line 212) -- Enhanced version that compares actual vs Keplerian positions.
- `calculate_exact_apsides(a, e, i, omega, Omega, rotate_points)` (line 358) -- Calculate exact apsidal positions at theta=0 (periapsis) and theta=pi (apoapsis).
- `add_apsidal_range_note(fig, obj_name, perihelion_date, aphelion_date, color_map, fetch_failed)` (line 466) -- Add legend entries explaining why actual apsidal markers aren't shown
- `estimate_hyperbolic_perihelion_date(current_position, q, e, date)` (line 606) -- Estimate perihelion date for hyperbolic orbits.
- `compute_apsidal_dates_from_tp(obj_name, params, current_date)` (line 643) -- Get perihelion from TP and aphelion from Tapo.
- `add_actual_apsidal_markers(fig, obj_name, params, date_range, positions_dict, color_map, center_body, is_satellite)` (line 672) -- Add markers for actual perihelion/aphelion (or perigee/apogee) dates.
- `fetch_positions_for_apsidal_dates(obj_id, params, date_range, center_id, id_type, is_satellite, fetch_position)` (line 824) -- Fetch actual positions for all apsidal dates within the date range.
- `get_orbital_period_days(body_name, semi_major_axis_au)` (line 872) -- Get orbital period in Earth days for a given body.
- `calculate_true_anomaly_from_position(x, y, z, a, e, i, omega, Omega)` (line 907) -- Calculate the true anomaly from a position in 3D space.
- `true_to_eccentric_anomaly(true_anomaly, e)` (line 952) -- Convert true anomaly to eccentric anomaly.
- `eccentric_to_mean_anomaly(E, e)` (line 991) -- Convert eccentric anomaly to mean anomaly.
- `calculate_time_to_anomaly(current_M, target_M, orbital_period_days)` (line 1010) -- Calculate time to reach a target mean anomaly from current mean anomaly.
- `calculate_apsidal_dates(date, current_x, current_y, current_z, a, e, i, omega, Omega, body_name)` (line 1035) -- Calculate dates for perihelion/apohelion (or perigee/apogee for satellites).
- `add_perihelion_marker(fig, x, y, z, obj_name, a, e, date, current_position, orbital_params, color_map, q, center_body)` (line 1104) -- Add a perihelion/perigee marker with accurate date calculation.
- `add_apohelion_marker(fig, x, y, z, obj_name, a, e, date, current_position, orbital_params, color_map, center_body)` (line 1240) -- Add an apohelion/apogee marker to the plot with accurate date calculation.
- `add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range, marker_color, obj_info)` (line 1369) -- Find and mark the closest plotted approach point from trajectory data.
- `solve_kepler_equation(M, e, tolerance, max_iterations)` (line 1505) -- Solve Kepler's equation M = E - e*sin(E) for eccentric anomaly E.
- `eccentric_to_true_anomaly(E, e)` (line 1535) -- Convert eccentric anomaly to true anomaly.
- `calculate_keplerian_position(orbital_params, current_datetime, rotate_points)` (line 1557) -- Calculate the Keplerian (analytical) position of an object at a given time.
- `add_keplerian_position_marker(fig, obj_name, orbital_params, current_datetime, rotate_points, center_body)` (line 1688) -- Add a Keplerian (analytical) current position marker to the plot.
- `compute_pairwise_encounter(sc_positions, target_positions, sc_dates, target_dates)` (line 1789) -- Find the closest approach between two objects from their position time series.
- `add_encounter_marker(fig, encounter, sc_name, target_name, color_map, obj_info)` (line 1910) -- Add an encounter marker to a 3D Plotly figure.

---

### catalog_selection.py

**Role:** computation | **Lines:** 92

> catalog_selection.py - Unified star selection from Hipparcos and Gaia catalogs.

**Depends on:** data_processing
**Consumed by:** data_acquisition_distance, hr_diagram_distance, planetarium_distance

**Public functions:**

- `select_stars(hip_data, gaia_data, mode, limit_value)` (line 17) -- Unified star selection function applying consistent catalog separation logic.

---

### celestial_coordinates.py

**Role:** computation | **Lines:** 454

> celestial_coordinates.py Module for calculating and formatting Right Ascension and Declination coordinates for celestial objects in Paloma's Orrery.

**Depends on:** (none)
**Consumed by:** visualization_utils

**Public functions:**

- `format_ra_dec_string(ra_hours, ra_minutes, ra_seconds, dec_degrees, dec_arcmin, dec_arcsec, precision_ra_sec, precision_dec_arcsec)` (line 11) -- Format RA/Dec values into standard astronomical notation strings.
- `format_ra_dec_decimal(ra_decimal_hours, dec_decimal_degrees, precision)` (line 41) -- Format RA/Dec in decimal format.
- `extract_jpl_radec(obj_data)` (line 60) -- Extract RA/Dec from JPL Horizons data if available.
- `calculate_radec_for_position(obj_data, obj_name)` (line 89) -- Extract RA/Dec from JPL Horizons data.
- `add_radec_to_hover_text(hover_text, obj_data, obj_name, insert_after_line)` (line 107) -- Add RA/Dec to hover text - always Earth-centered.
- `get_precision_note(obj_data, obj_name)` (line 383) -- Get precision estimate - prefer actual JPL uncertainties,
- `format_radec_hover_component(obj_data, obj_name, compact)` (line 454) -- Format RA/Dec for hover text with actual uncertainties when available.
- `determine_coordinate_precision(obj_data, obj_name)` (line 493) -- Determine appropriate precision for RA/Dec display based on object type and data source.

---

### coordinate_system_guide.py

**Role:** computation | **Lines:** 547

> coordinate_system_guide.py - Educational reference for J2000 Ecliptic Coordinate System

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `create_coordinate_system_diagram()` (line 18) -- Create an interactive 3D diagram showing the J2000 Ecliptic coordinate system.
- `create_coordinate_system_guide()` (line 228) -- Create and open an HTML file with 3D visualization and reference text side by side.

---

### data_acquisition.py

**Role:** computation | **Lines:** 220

> data_acquisition.py - Unified module for both distance- and magnitude-based queries, integrating the simpler logic of data_acquisition_distance.py.

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, incremental_cache_manager, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `calculate_parallax_limit(max_light_years)` (line 27) -- Calculate minimum parallax for a given distance in light-years.
- `initialize_vizier(timeout)` (line 32) -- Initialize Vizier with no row limit and a set of columns you actually need.
- `load_or_fetch_hipparcos_data(v, hip_data_file, mode, mag_limit, parallax_constraint)` (line 52) -- Load or fetch Hipparcos data.
- `load_or_fetch_gaia_data(v, gaia_data_file, mode, mag_limit, parallax_constraint)` (line 95) -- Load or fetch Gaia data.
- `estimate_vmag_from_gaia(gaia_data)` (line 141) -- Convert Gaia G magnitudes (plus BP-RP) to an approximate Johnson V magnitude.
- `align_coordinate_systems(hip_data)` (line 159) -- Align coordinate systems by ensuring RA_ICRS, DE_ICRS exist in the table.
- `process_distance_data(data, max_light_years)` (line 178) -- Convert parallax to distance (pc, ly) and filter out anything beyond max_light_years.
- `load_stellar_data(mode, max_value, hip_file, gaia_file)` (line 197) -- Main function to load or fetch data from Hipparcos and Gaia, either for a distance-based

---

### data_acquisition_distance.py

**Role:** computation | **Lines:** 169

> data_acquisition_distance.py - Module for fetching stellar data based on distance.

**Depends on:** catalog_selection, vot_cache_manager
**Consumed by:** hr_diagram_distance

**Public functions:**

- `initialize_vizier()` (line 9) -- Initialize Vizier with unlimited rows and all columns.
- `calculate_parallax_limit(max_light_years)` (line 17) -- Calculate minimum parallax for given distance in light-years.
- `fetch_gaia_data(vizier, gaia_data_file, min_parallax_mas)` (line 23) -- Fetch stars from Gaia EDR3 catalog.
- `fetch_hipparcos_data(vizier, hip_data_file, min_parallax_mas)` (line 49) -- Fetch stars from Hipparcos catalog.
- `process_gaia_data(gaia_data, max_light_years)` (line 75) -- Process Gaia data and calculate distances.
- `process_hipparcos_data(hip_data, max_light_years)` (line 105) -- Process Hipparcos data and calculate distances.
- `align_coordinate_systems(hip_data)` (line 136) -- Align coordinate systems between catalogs.
- `estimate_vmag_from_gaia(gaia_data)` (line 160) -- Convert Gaia G magnitudes to Johnson V magnitudes.
- `fetch_stellar_data(max_light_years)` (line 173) -- Main function to fetch stellar data within specified distance.

---

### data_processing.py

**Role:** computation | **Lines:** 434

> data_processing.py - Star catalog data cleaning, merging, and analysis.

**Depends on:** (none)
**Consumed by:** catalog_selection, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `convert_icrs_to_radec_strings(data)` (line 26) -- Convert ICRS coordinates (decimal degrees) to formatted RA/Dec strings.
- `estimate_vmag_from_gaia(gaia_data)` (line 96) -- Estimate V magnitude from Gaia G magnitude and BP-RP color.
- `calculate_distances(data)` (line 112) -- Calculate distances in parsecs and light-years
- `align_coordinate_systems(hip_data)` (line 126) -- Ensure RA and Dec columns are consistent and in degrees.
- `generate_unique_ids(stars, catalog)` (line 144) -- Generate unique IDs for stars based on their catalog.
- `select_stars_by_magnitude(hip_data, gaia_data, mag_limit)` (line 172) -- Select stars based on a clean separation:
- `analyze_additional_stars(new_data, old_data)` (line 242) -- Analyze properties of stars present in new data but not in old
- `examine_outliers(data)` (line 270) -- Print details of potential outlier stars
- `print_star_details(star)` (line 289) -- Print relevant details for a single star
- `select_stars_by_distance(hip_data, gaia_data, max_light_years)` (line 300) -- Select stars based on distance criteria while maintaining clean catalog separation:
- `calculate_distances(data)` (line 394) -- Calculate distances in parsecs and light-years from parallax.
- `calculate_cartesian_coordinates(data)` (line 409) -- Calculate x, y, z coordinates from RA, Dec, and distance.
- `validate_coordinates(data)` (line 480) -- Validate calculated coordinates and report any issues.
- `filter_by_mag_limit(combined_data, mag_limit)` (line 502) -- Filter the combined data to include only stars within the specified mag_limit.
- `update_counts(filtered_data, mag_limit)` (line 508) -- Update counts of stars in each category based on the filtered data.

---

### earth_system_generator.py

**Role:** computation | **Lines:** 688

> Paloma's Orrery: Earth System Generator Engine Architecture: The Teaser (Plotly) & Blockbuster (KMZ) Pipeline

**Depends on:** scenarios_coral_bleaching, scenarios_heatwaves, scenarios_western_heatwave_march_2026
**Consumed by:** scenarios_western_heatwave_march_2026

**Public functions:**

- `run_scenario(scenario, status_callback)` (line 59) -- Orchestrates the full pipeline for one scenario.
- `build_spikes_kml(scenario_id, date, lats, lons, values, thresholds, intel_path, legend_risk_path, pin_stations)` (line 137) -- Builds the vertical extrusion spikes KML layer.
- `build_heatmap_kml(scenario_id, date, lats, lons, values, thresholds)` (line 227) -- Builds the ground overlay heatmap KML layer with contour PNG.
- `build_impact_kml(scenario_id, date, populations, legend_pop_path, thresholds)` (line 268) -- Builds the population impact circles KML layer.
- `generate_plotly_teaser(scenario_id, title, lats, lons, values, output_dir, thresholds, briefing, description, mobile_briefing, encyclopedia)` (line 326) -- Generates the fast-loading 2D Plotly Teaser for Web Gallery use.
- `package_and_cleanup(scenario_id, files_to_package, output_dir)` (line 503) -- Zips the raw KML and PNG files into a single-document KMZ.
- `create_legend_card(thresholds, scenario_id)` (line 568) -- Creates the risk scale legend image from threshold bands.
- `create_pop_legend_card(scenario_id)` (line 635) -- Creates the population circle key with tiered size/color.
- `create_intel_card(title, description, briefing, date, scenario_id)` (line 675) -- Creates the dynamic briefing text card.
- `create_circle_polygon(lat, lon, radius_km, num_points)` (line 723) -- Generates a circle polygon for KML population impact layer.
- `kml_to_mpl_color(kml_color)` (line 743) -- Converts KML AABBGGRR hex color to matplotlib-compatible hex.
- `class MissionSelector` (line 761) -- Tkinter GUI for selecting and running scenarios.

---

### energy_imbalance.py

**Role:** computation | **Lines:** 839

> Energy Imbalance Visualization for Paloma's Orrery Modern era (2005-2025) temperature and energy imbalance

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `load_ocean_heat_content()` (line 35) -- Load NOAA ocean heat content data and convert to energy imbalance
- `load_modern_temperature_data()` (line 74) -- Load NASA GISS instrumental temperature data (1880-2025)
- `create_energy_imbalance_visualization()` (line 105) -- Create energy imbalance visualization (2005-2025)
- `main()` (line 926) -- Create and save the visualization

---

### fetch_climate_data.py

**Role:** computation | **Lines:** 761

> Climate Data Fetcher - Paloma's Orrery Preserves critical climate datasets for future reference

**Depends on:** (none)
**Consumed by:** climate_cache_manager

**Public functions:**

- `fetch_ocean_ph_bcodmo()` (line 43) -- Fetch ocean pH data from BCO-DMO HOT dataset
- `fetch_ocean_ph_hot_direct()` (line 66) -- Try to fetch pH data directly from HOT program
- `parse_carbonate_data(lines, source)` (line 90) -- Parse carbonate chemistry data (flexible parser)
- `create_ph_metadata(records)` (line 188) -- Create metadata for ocean pH dataset
- `fetch_ocean_ph()` (line 241) -- Main function to fetch ocean pH data
- `fetch_nasa_sea_level()` (line 270) -- Fetch NASA sea level data from science.nasa.gov indicator page
- `status_print(msg)` (line 344) -- Print status message with indentation
- `fetch_mauna_loa_co2(status_callback)` (line 349) -- Fetch Mauna Loa CO2 monthly data
- `fetch_nasa_giss_temperature(status_callback)` (line 419) -- Fetch NASA GISS global temperature data
- `fetch_arctic_ice()` (line 480) -- Fetch NSIDC Arctic sea ice extent data (V4 Excel format)
- `create_co2_metadata(records)` (line 566) -- Create metadata for CO2 dataset
- `create_temperature_metadata(records)` (line 591) -- Create metadata for temperature dataset
- `create_ice_metadata(records)` (line 616) -- Create metadata for Arctic sea ice dataset
- `create_sea_level_metadata(records)` (line 644) -- Create metadata for sea level dataset
- `save_cache(output_file, records, metadata_func)` (line 672) -- Safely save data to JSON cache with comprehensive fail-safe protection
- `main()` (line 786) -- Main function to fetch all climate data

---

### fetch_paleoclimate_data.py

**Role:** computation | **Lines:** 169

> Paleoclimate Data Fetcher for Paloma's Orrery Fetches and caches paleoclimate proxy data from authoritative sources

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `ensure_data_dir()` (line 31) -- Create data directory if it doesn't exist
- `fetch_lr04_data()` (line 36) -- Fetch LR04 benthic stack data (5.3 Ma - present)
- `fetch_epica_co2_data()` (line 103) -- Fetch EPICA Dome C CO2 data (800 ka - present)
- `main()` (line 174) -- Fetch all paleoclimate datasets

---

### idealized_orbits.py

**Role:** computation | **Lines:** 6,164

> idealized_orbits.py - Keplerian orbit ellipse construction and satellite orbit models.

**Depends on:** apsidal_markers, constants_new, orbital_elements, osculating_cache_manager
**Consumed by:** create_ephemeris_database, orbital_param_viz, palomas_orrery, palomas_orrery_helpers, visualization_utils

**Public functions:**

- `get_planet_perturbation_note(obj_name, orbit_source)` (line 101) -- Get appropriate perturbation note for planet's Keplerian orbit hover text.
- `get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params)` (line 199) -- Compare osculating vs mean orbital elements and return perturbation assessment HTML.
- `add_mean_orbit_trace(fig, obj_name, mean_params, color_func)` (line 273) -- Add a mean orbit trace from orbital_elements.py (JPL epoch solution).
- `calculate_mars_satellite_elements(date, satellite_name)` (line 379) -- Calculate time-varying orbital elements for Mars satellites
- `calculate_jupiter_satellite_elements(date, satellite_name)` (line 437) -- Calculate time-varying orbital elements for Jupiter satellites.
- `calculate_saturn_satellite_elements(date, satellite_name)` (line 494) -- Calculate time-varying orbital elements for Saturn satellites.
- `test_mars_rotations(satellite_name, planetary_params, color, fig)` (line 544) -- Test multiple rotation combinations to find the best alignment
- `test_uranus_equatorial_transformations(satellite_name, planetary_params, color, fig)` (line 646) -- Test transformations assuming orbital elements are in Uranus's equatorial plane
- `test_uranus_rotation_combinations(satellite_name, planetary_params, color, fig)` (line 744) -- Test multiple rotation combinations for Uranus satellites systematically
- `debug_planet_transformation(planet_name)` (line 854) -- Print detailed information about the transformation for a specific planet
- `debug_mars_moons(satellites_data, parent_planets)` (line 928) -- Special debug function for Mars and its moons
- `compare_transformation_methods(fig, satellites_data, parent_planets)` (line 974) -- Plot orbits with different transformation methods for comparison
- `test_mars_negative_tilt(fig, satellites_data)` (line 1007) -- Test hypothesis that Mars needs a negative tilt application
- `debug_satellite_systems()` (line 1059)
- `rotate_points(x, y, z, angle, axis)` (line 1085) -- Rotates points (x,y,z) about the given axis by 'angle' radians.
- `plot_jupiter_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1131) -- Plot osculating orbit for Jupiter satellites.
- `plot_saturn_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1294) -- Plot osculating orbit for Saturn satellites.
- `plot_uranus_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1440) -- Plot osculating orbit for Uranus satellites.
- `plot_neptune_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1543) -- Plot osculating orbit for Neptune satellites.
- `plot_pluto_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 1676) -- Plot osculating orbit for objects in Pluto binary system.
- `plot_tno_satellite_orbit(fig, satellite_name, parent_name, date, color, show_apsidal_markers)` (line 1989) -- Plot osculating orbit for TNO (Trans-Neptunian Object) satellites.
- `add_pluto_barycenter_marker(fig, date, charon_position)` (line 2383) -- Add the Pluto-Charon barycenter marker to Pluto-centered view.
- `plot_orcus_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2451) -- Plot osculating orbit for objects in the Orcus-Vanth binary system.
- `add_orcus_barycenter_marker(fig, date, vanth_position)` (line 2676) -- Add the Orcus-Vanth barycenter marker to Orcus-centered view.
- `plot_gonggong_xiangliu_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2744) -- Plot analytical orbit for Xiangliu around Gonggong.
- `plot_patroclus_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2933) -- Plot analytical orbit for objects in the Patroclus-Menoetius binary Trojan system.
- `create_planet_transformation_matrix(planet_name)` (line 3183) -- Create a transformation matrix for a planet based on its pole direction.
- `plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig, date, days_to_plot, current_position, show_apsidal_markers)` (line 3238) -- Plot the Keplerian orbit of a satellite around its parent planet.
- `calculate_moon_orbital_elements(date)` (line 3809) -- Calculate Moon's orbital elements for a specific date
- `plot_mars_moon_osculating_orbit(fig, satellite_name, horizons_id, date, color, parent_planet)` (line 3877) -- Plot osculating orbit for Mars satellites (Phobos/Deimos)
- `plot_moon_ideal_orbit(fig, date, center_object_name, color, days_to_plot, current_position, show_apsidal_markers, planetary_params)` (line 3999) -- Plot BOTH the Moon's analytical and osculating orbits for educational comparison.
- `plot_earth_moon_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 4234) -- Plot osculating orbit for objects in the Earth-Moon binary system.
- `add_earth_moon_barycenter_marker(fig, date, moon_position)` (line 4472) -- Add the Earth-Moon barycenter marker to Earth-centered view.
- `generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points, max_distance)` (line 4545) -- Generate points for a hyperbolic orbit trajectory.
- `plot_idealized_orbits(fig, objects_to_plot, center_id, objects, planetary_params, parent_planets, color_map, date, days_to_plot, current_positions, fetch_position, show_apsidal_markers, parent_window)` (line 4643) -- Plot Keplerian orbits for planets, dwarf planets, asteroids, KBOs, and moons.
- `test_triton_rotations(satellite_name, planetary_params, color, fig)` (line 6015) -- Test multiple rotation combinations for Triton's orbit
- `test_pluto_moon_rotations(satellite_name, planetary_params, color, fig)` (line 6157) -- Fine-tuned testing of XYZ rotation combinations for Pluto's moons.
- `very_fine_pluto_rotations(satellite_name, planetary_params, color, fig, x_range, y_range, z_range, step)` (line 6395) -- Extremely fine-grained testing of XYZ rotation combinations for Pluto's moons.
- `pluto_system_final_transform(satellite_name, planetary_params, color, fig, transform)` (line 6530) -- Apply a specific optimal transformation to Pluto's moons' orbits.
- `calculate_phoebe_correction_from_normals()` (line 6645) -- Calculate the optimal rotation to align Keplerian orbit with actual orbit
- `plot_hyperbolic_osculating_orbit(fig, obj_name, obj_info, center_id, color_map, date, show_apsidal_markers, parent_window, approach)` (line 6682) -- Plot a geocentric (or planet-centric) osculating hyperbolic orbit for a
- `plot_perihelion_osculating_orbit(fig, obj_name, obj_info, color_map, date, show_apsidal_markers, parent_window)` (line 6944) -- Plot Sun-centered osculating orbit arc at perihelion epoch for comets.

---

### object_type_analyzer.py

**Role:** computation | **Lines:** 754

> Object Type Analysis and Report Generation Module Provides comprehensive analysis of astronomical data including object types, data quality metrics, and full report generation.

**Depends on:** constants_new
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, plot_data_report_widget

**Public functions:**

- `expand_object_type(ot)` (line 13) -- Expand object type codes to full descriptions.
- `class ObjectTypeAnalyzer` (line 47) -- Analyzer for categorizing and analyzing astronomical object types.
- `analyze_sample_data()` (line 865) -- Test function to demonstrate the analyzer.

---

### orbital_elements.py

**Role:** computation | **Lines:** 1,285

> Standalone data module containing orbital element dictionaries. NO IMPORTS - Pure data only to avoid circular dependencies.

**Depends on:** (none)
**Consumed by:** idealized_orbits, osculating_cache_manager, palomas_orrery, spacecraft_encounters

---

### simbad_manager.py

**Role:** computation | **Lines:** 1,028

> Enhanced SIMBAD Query Manager with configurable rate limiting and retry logic. This module replaces simbad_test.py and provides robust SIMBAD querying capabilities.

**Depends on:** messier_catalog, vot_cache_manager
**Consumed by:** create_cache_backups, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, star_properties

**Public functions:**

- `class SimbadConfig` (line 26) -- Configuration for SIMBAD queries with user-adjustable parameters.
- `class RateLimiter` (line 75) -- Token bucket rate limiter for SIMBAD queries.
- `class QueryStats` (line 123) -- Track statistics for SIMBAD queries.
- `class SimbadQueryManager` (line 173) -- Main class for managing SIMBAD queries with rate limiting and error handling.
- `create_custom_simbad()` (line 1151) -- Compatibility function for existing code.
- `query_simbad_for_star_properties(missing_ids, existing_properties, properties_file)` (line 1158) -- Compatibility wrapper for existing code.
- `quick_cache_check()` (line 1181) -- Quick check of all cache files.
- `rebuild_from_vot(mode, force)` (line 1189) -- Rebuild PKL file from VOT caches.
- `protect_all_star_data()` (line 1210) -- Create protected backups of all star data files.

---

## DATA: Catalogs, constants, and static datasets

### celestial_objects.py

**Role:** data | **Lines:** 1,225

> Paloma's Orrery - Celestial Objects Data Module

**Depends on:** (none)
**Consumed by:** palomas_orrery

**Public functions:**

- `build_objects_list(definitions, vars_dict, color_map_func)` (line 1253) -- Build the runtime objects list from definitions.
- `get_all_var_names()` (line 1283) -- Return list of all var_name strings needed for IntVar creation.
- `get_shell_var_names()` (line 1405) -- Return list of all shell var_name strings needed for IntVar creation.
- `get_shell_tooltip_names()` (line 1415) -- Return list of all shell tooltip info variable names.
- `build_shell_checkboxes(body_name, parent_frame, vars_dict, tooltips_dict, tk_module, CreateToolTip)` (line 1425) -- Build shell checkboxes for a single body.

---

### close_approach_data.py

**Role:** data | **Lines:** 519

> Fetch and cache close approach data from JPL's Small Body Close Approach Data (CAD) API for any small body against any major body.

**Depends on:** apsidal_markers
**Consumed by:** palomas_orrery

**Public functions:**

- `get_close_approaches(designation, body, date_min, date_max, dist_max, force_refresh)` (line 304) -- Return list of close approach events for a small body near a major body.
- `get_closest_approach(designation, body, date_min, date_max, dist_max, force_refresh)` (line 370) -- Return the single closest approach event (minimum dist_au) within the
- `get_approach_within_date_range(designation, body, start_date, end_date, force_refresh)` (line 390) -- Check if a cached close approach falls within a plotted date range.
- `format_approach_hover(approach, body, obj_name)` (line 439) -- Build Plotly-compatible HTML hover text for a close approach marker.
- `add_cad_perigee_marker(fig, approach, position, body, obj_name, color_map, label_suffix)` (line 493) -- Add a CAD-sourced perigee marker to a Plotly 3D figure.
- `fetch_position_at_approach(approach, designation, center_body_id, id_type)` (line 548) -- Fetch the geocentric (or other center) position of a small body at the

---

### constants_new.py

**Role:** data | **Lines:** 2,401

> constants_new.py - Central constants, parameters, and object catalogs for the orrery.

**Depends on:** (none)
**Consumed by:** apsidal_markers, exoplanet_stellar_properties, idealized_orbits, object_type_analyzer, orbital_param_viz, palomas_orrery, palomas_orrery_helpers, planet_visualization, planet_visualization_utilities, star_visualization_gui, stellar_parameters, visualization_2d, visualization_3d, visualization_core

**Public functions:**

- `color_map(planet)` (line 472)

---

### exoplanet_coordinates.py

**Role:** data | **Lines:** 399

> exoplanet_coordinates.py - Stellar Positioning and Coordinate Transformations

**Depends on:** exoplanet_systems
**Consumed by:** (none -- standalone)

**Public functions:**

- `apply_proper_motion(ra_deg, dec_deg, pmra_mas_yr, pmdec_mas_yr, epoch, target_date, distance_pc)` (line 31) -- Apply proper motion to stellar position
- `get_star_position_at_date(host_star_data, target_date)` (line 85) -- Get corrected stellar position at specific date
- `radec_to_cartesian(ra_deg, dec_deg, distance_au)` (line 124) -- Convert equatorial coordinates to 3D Cartesian
- `cartesian_to_radec(x, y, z)` (line 157) -- Convert 3D Cartesian to equatorial coordinates
- `get_star_3d_position(host_star_data, target_date)` (line 188) -- Get 3D position of host star in galactic context
- `calculate_binary_barycenter(star_A_mass, star_B_mass, star_A_position, star_B_position)` (line 220) -- Calculate center of mass for binary star system
- `create_local_frame_description(host_star_data)` (line 254) -- Generate description of local coordinate frame for exoplanet system
- `parsecs_to_lightyears(distance_pc)` (line 298) -- Convert parsecs to light-years (1 pc = 3.26156 ly)
- `lightyears_to_parsecs(distance_ly)` (line 302) -- Convert light-years to parsecs
- `parsecs_to_au(distance_pc)` (line 306) -- Convert parsecs to AU (1 pc = 206265 AU)
- `au_to_parsecs(distance_au)` (line 310) -- Convert AU to parsecs
- `stellar_parallax_to_distance(parallax_mas)` (line 314) -- Convert parallax to distance
- `distance_to_stellar_parallax(distance_pc)` (line 328) -- Convert distance to parallax
- `calculate_tangential_velocity(pmra_mas_yr, pmdec_mas_yr, distance_pc)` (line 346) -- Calculate tangential velocity from proper motion
- `get_proper_motion_summary(host_star_data)` (line 374) -- Generate human-readable summary of proper motion

---

### exoplanet_stellar_properties.py

**Role:** data | **Lines:** 485

> exoplanet_stellar_properties.py - Stellar Properties for Exoplanet Host Stars

**Depends on:** constants_new, stellar_parameters, visualization_core
**Consumed by:** exoplanet_orbits, palomas_orrery, sgr_a_star_data

**Public functions:**

- `get_temperature_color(temperature_k)` (line 49) -- Get RGB color for a given temperature using continuous interpolation.
- `get_temperature_colors_dict()` (line 109) -- Get the complete temperature-to-color mapping dictionary.
- `parse_stellar_class(spectral_type)` (line 133) -- Parse stellar luminosity class from spectral type string.
- `get_stellar_class_description(spectral_type)` (line 157) -- Get detailed description of stellar class.
- `calculate_host_star_properties(host_star_data)` (line 187) -- Calculate comprehensive stellar properties for an exoplanet host star.
- `calculate_binary_star_properties(star_A_data, star_B_data)` (line 262) -- Calculate properties for both stars in a binary system.
- `create_exoplanet_host_star_hover_text(host_star_data, system_data, enhanced_properties)` (line 283) -- Create rich hover text for exoplanet host stars.
- `create_binary_star_hover_text(star_data, star_label, system_data, enhanced_properties)` (line 390) -- Create hover text for individual stars in a binary system.
- `calculate_marker_size(luminosity, base_size, scale_factor)` (line 449) -- Calculate marker size based on stellar luminosity.
- `enrich_exoplanet_system(system_dict)` (line 478) -- Enrich an exoplanet system dictionary with calculated stellar properties.
- `get_exoplanet_object_type_description(spectral_type)` (line 509) -- Get a brief object type description for exoplanet host stars.

---

### exoplanet_systems.py

**Role:** data | **Lines:** 570

> exoplanet_systems.py - Hardcoded Exoplanet System Catalog

**Depends on:** (none)
**Consumed by:** exoplanet_coordinates, exoplanet_orbits, palomas_orrery

**Public functions:**

- `get_system(system_id)` (line 619) -- Get exoplanet system by ID
- `get_all_systems()` (line 631) -- Get list of all available system IDs
- `get_system_summary(system_id)` (line 635) -- Get quick summary of system for GUI display
- `get_planets_in_hz(system_id)` (line 659) -- Get list of planets in habitable zone

---

### messier_catalog.py

**Role:** data | **Lines:** 404

> messier_catalog.py - Static catalog of Messier objects and bright deep-sky objects.

**Depends on:** (none)
**Consumed by:** messier_object_data_handler, simbad_manager, star_properties

**Public functions:**

- `get_all_bright_objects()` (line 285) -- Combine all catalogs of bright galactic objects.
- `get_objects_brighter_than(magnitude)` (line 299) -- Return all objects brighter than the specified magnitude.
- `get_objects_by_type(obj_type)` (line 316) -- Return all objects of a specific type.
- `get_nebulae()` (line 333) -- Return all nebulae from both Messier and bright object catalogs.
- `get_star_clusters()` (line 345) -- Return all star clusters from both catalogs.
- `get_visible_objects(mag_limit)` (line 352) -- Return all objects brighter than the given magnitude.
- `get_object_info(obj_id)` (line 370) -- Get detailed information about a specific object.
- `get_catalog_statistics()` (line 385) -- Return statistics about all catalogs.

---

### sgr_a_star_data.py

**Role:** data | **Lines:** 555

> sgr_a_star_data.py Data module for the Galactic Center S-Stars visualization. Contains orbital elements and physical constants.

**Depends on:** exoplanet_stellar_properties, stellar_parameters
**Consumed by:** sgr_a_grand_tour, sgr_a_visualization_animation, sgr_a_visualization_core, sgr_a_visualization_core_arcs, sgr_a_visualization_precession

**Public functions:**

- `estimate_temperature_fallback(spectral_type)` (line 52) -- Fallback temperature estimation for B-type stars.
- `get_temperature_color_fallback(temperature_k)` (line 76) -- Fallback temperature-to-color conversion.
- `get_star_temperature(star_data)` (line 97) -- Get temperature for a star, using best available method.
- `get_star_color(star_data)` (line 111) -- Get display color for a star based on its temperature.
- `get_orbit_color(star_data)` (line 124) -- Get distinct color for orbit trace and labels.
- `get_star_data(star_name)` (line 249) -- Returns the dictionary for a specific star.
- `list_stars()` (line 253) -- Returns list of available star keys.
- `get_all_stars()` (line 257) -- Returns the complete catalog dictionary.
- `get_spectral_class_description(spectral_type)` (line 265) -- Get human-readable description of spectral type.
- `calculate_next_periapsis(star_data, reference_year)` (line 295) -- Calculate the next periapsis passage date for a star.
- `create_star_hover_text(star_name, star_data, current_distance_au, current_velocity_km_s)` (line 317) -- Create rich hover text for S-star markers.
- `calculate_periapsis_au(a_au, e)` (line 398) -- Calculate periapsis distance (closest approach to black hole).
- `calculate_apoapsis_au(a_au, e)` (line 405) -- Calculate apoapsis distance (farthest point from black hole).
- `calculate_orbital_velocity(a_au, r_au, M_solar)` (line 412) -- Calculate orbital velocity at distance r using vis-viva equation.
- `calculate_periapsis_velocity(a_au, e, M_solar)` (line 430) -- Calculate velocity at periapsis (maximum velocity).
- `calculate_apoapsis_velocity(a_au, e, M_solar)` (line 435) -- Calculate velocity at apoapsis (minimum velocity).
- `velocity_as_fraction_of_c(v_km_s)` (line 440) -- Convert velocity to fraction of speed of light.
- `format_velocity(v_km_s)` (line 444) -- Format velocity as 'X km/s (Y% c)'.
- `calculate_schwarzschild_precession_per_orbit(a_au, e, M_solar)` (line 453) -- Calculate the Schwarzschild (GR) precession per orbit.
- `calculate_gravitational_redshift(r_au, M_solar)` (line 473) -- Calculate gravitational redshift factor at distance r.
- `mean_anomaly_at_time(t_current, t_periapsis, period_yrs)` (line 494) -- Calculate mean anomaly M at a given time.
- `solve_kepler_equation(M, e, tolerance, max_iterations)` (line 505) -- Solve Kepler's equation: M = E - e*sin(E)
- `eccentric_to_true_anomaly(E, e)` (line 539) -- Convert eccentric anomaly to true anomaly.
- `true_anomaly_at_time(t_current, t_periapsis, period_yrs, e)` (line 551) -- Calculate true anomaly at a given time.
- `radius_from_true_anomaly(a_au, e, nu)` (line 561) -- Calculate orbital radius at true anomaly nu.
- `get_star_summary(star_name)` (line 572) -- Get a formatted summary of a star's orbital characteristics.
- `print_catalog_summary()` (line 611) -- Print summary for all stars in the catalog.

---

### spacecraft_encounters.py

**Role:** data | **Lines:** 1,204

> Tagged encounter data for spacecraft missions in Paloma's Orrery.

**Depends on:** orbital_elements, osculating_cache_manager
**Consumed by:** palomas_orrery

**Public functions:**

- `utc_to_tdb(dt)` (line 34) -- Convert UTC datetime to TDB for Horizons queries (~69 second offset).
- `get_encounters_for_spacecraft(spacecraft_name)` (line 321) -- Get all encounters for a given spacecraft.
- `get_encounters_in_date_range(spacecraft_name, start_date, end_date)` (line 334) -- Get encounters for a spacecraft that fall within a date range.
- `get_all_encounter_spacecraft()` (line 362) -- Get list of all spacecraft that have tagged encounters.
- `get_encounters_for_target(target_name)` (line 372) -- Get all encounters where a given body is the target, across all spacecraft.
- `get_full_mission_preset(spacecraft_name)` (line 397)
- `resolve_encounter_time(enc, sc_id, obj_start_date, obj_end_date, objects)` (line 489) -- Derive actual closest approach time from Horizons trajectory data.
- `get_encounter_preset(spacecraft_name, encounter_index)` (line 608) -- Build a close-up preset for a specific encounter.
- `get_comet_perihelion_preset(obj_name, obj_info)` (line 699) -- Build a perihelion close-up preset for a comet.
- `fetch_position_at_encounter(encounter, center_id, spacecraft_id)` (line 846) -- Fetch spacecraft position at the encounter epoch from JPL Horizons.
- `add_tagged_encounter_marker(fig, encounter, position, spacecraft_name, color_map)` (line 1024) -- Place a white diamond-open marker at the spacecraft's position at encounter epoch.
- `add_tagged_encounter_markers(fig, selected_objects, objects, dates_lists, center_object_name, center_id, color_map, show_closest_approach, positions_cache)` (line 1083) -- Add tagged encounter markers for all selected spacecraft in the plot.
- `get_encounter_summary()` (line 1200) -- Get a summary of all encounters for all spacecraft.
- `get_comet_perihelion_preset(obj_name, obj_info)` (line 1270) -- Build a perihelion close-up preset for a comet.
- `get_comet_disintegration_preset(obj_name)` (line 1384) -- Fixed preset for the MAPS disintegration event.

---

### star_notes.py

**Role:** data | **Lines:** 1,137

> star_notes.py - Curated hover text annotations for notable stars.

**Depends on:** (none)
**Consumed by:** messier_object_data_handler, star_visualization_gui, visualization_2d, visualization_3d, visualization_core

---

### star_properties.py

**Role:** data | **Lines:** 338

> star_properties.py - SIMBAD stellar property queries with local caching.

**Depends on:** messier_catalog, simbad_manager
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `get_column_value_safe(result_table, old_name, new_name)` (line 23) -- Get column value from either old (uppercase) or new (lowercase) format.
- `create_custom_simbad()` (line 41) -- Create SIMBAD instance with proper field configuration for both old and new API.
- `parse_magnitude(value)` (line 54)
- `load_existing_properties(properties_file)` (line 68) -- Load existing star and Messier object properties from a file.
- `generate_unique_ids(combined_data)` (line 122) -- Generate unique identifiers for all stars consistently.
- `save_properties_to_file(properties, properties_file)` (line 159) -- Save star properties to file with Messier object support.
- `create_custom_simbad()` (line 188)
- `query_simbad_for_star_properties(missing_ids, existing_properties, properties_file)` (line 200) -- Query Simbad for missing star properties with backward compatibility.
- `assign_properties_to_data(combined_data, existing_properties, unique_ids)` (line 357) -- Assign retrieved properties to the combined data with Messier object support.

---

### stellar_data_patches.py

**Role:** data | **Lines:** 41

> stellar_data_patches.py - Manual corrections for stars with known bad catalog data.

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `apply_temperature_patches(data)` (line 20) -- Apply known fixes for stars with missing or incorrect data.

---

### stellar_parameters.py

**Role:** data | **Lines:** 352

> stellar_parameters.py - Stellar temperature and parameter estimation from spectral types.

**Depends on:** constants_new, stellar_parameters
**Consumed by:** exoplanet_stellar_properties, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, sgr_a_star_data, stellar_parameters, visualization_core

**Public functions:**

- `estimate_temperature_from_spectral_type(sp_type)` (line 22) -- Estimate effective temperature from spectral type.
- `calculate_bv_temperature(B_V)` (line 65) -- Calculate temperature from B-V color index using Ballesteros' formula.
- `select_best_temperature(T_eff_BV, T_eff_sptype)` (line 89) -- Select the best temperature estimate based on various criteria.
- `debug_orionis_stars(data, stage)` (line 127) -- Debug function to compare Epsilon and Zeta Orionis data through processing stages.
- `calculate_stellar_parameters(combined_data)` (line 223) -- Calculate stellar parameters with parallel debugging of both Orionis stars.

---

## CACHE: Fetch, store, and retrieve computed data

### climate_cache_manager.py

**Role:** cache | **Lines:** 161

> Climate Cache Manager for Paloma's Orrery Manages safe updates of climate data caches with validation and rollback.

**Depends on:** fetch_climate_data
**Consumed by:** earth_system_visualization_gui

**Public functions:**

- `update_climate_data(status_callback)` (line 18) -- Update all climate datasets by importing and calling fetch functions directly.

---

### create_cache_backups.py

**Role:** cache | **Lines:** 8

> create_cache_backups.py - One-shot script to create timestamped backups of star data caches.

**Depends on:** simbad_manager
**Consumed by:** (none -- standalone)

---

### create_ephemeris_database.py

**Role:** cache | **Lines:** 243

> create_ephemeris_database.py - Create satellite_ephemerides.json from multiple sources

**Depends on:** idealized_orbits
**Consumed by:** (none -- standalone)

**Public functions:**

- `parse_horizons_header(filename)` (line 16) -- Parse orbital elements from JPL Horizons ephemeris file header.
- `get_idealized_orbits_data()` (line 86) -- Import orbital parameters from idealized_orbits.py if available.
- `create_satellite_ephemerides()` (line 99) -- Create comprehensive satellite ephemeris database from all available sources.
- `download_instructions()` (line 273) -- Print instructions for downloading more ephemerides.

---

### incremental_cache_manager.py

**Role:** cache | **Lines:** 657

> Smart incremental cache manager for VizieR catalog data and SIMBAD properties. Handles incremental fetching when query parameters change, avoiding redundant queries.

**Depends on:** data_acquisition
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `class CacheMetadata` (line 23) -- Metadata for cached catalog data.
- `class IncrementalCacheManager` (line 62) -- Manages incremental caching for stellar catalog data.
- `class SimbadCacheManager` (line 351) -- Manages caching for SIMBAD property queries.
- `smart_load_or_fetch_hipparcos(v, hip_data_file, mode, limit_value)` (line 422) -- Smart loading/fetching for Hipparcos data with incremental caching.
- `smart_load_or_fetch_gaia(v, gaia_data_file, mode, limit_value)` (line 559) -- Smart loading/fetching for Gaia data with incremental caching.

---

### orbit_data_manager.py

**Role:** cache | **Lines:** 1,520

> orbit_data_manager.py - Advanced orbit data caching and management

**Depends on:** (none)
**Consumed by:** osculating_cache_manager, palomas_orrery, palomas_orrery_helpers, test_orbit_cache

**Public functions:**

- `utc_to_tdb(dt)` (line 41) -- Convert UTC datetime to TDB (Terrestrial Dynamical Time) for Horizons queries.
- `repair_cache_on_load()` (line 49) -- Load cache and remove only corrupted entries
- `initialize(status_widget, root_widget, center_var, data_file)` (line 95) -- Initialize the orbit data manager by loading cached data.
- `load_orbit_paths(file_path)` (line 116) -- Load orbit paths from file with automatic repair of corrupted entries.
- `convert_single_orbit_to_new_format(orbit_key, orbit_data)` (line 338) -- Convert a single orbit from old format to new format.
- `save_orbit_paths(data, file_path)` (line 405) -- Save orbit paths data to file with safety checks.
- `convert_to_new_format(old_data)` (line 533) -- Convert old format orbit data to new time-indexed format.
- `determine_interval_for_object(obj, orbital_params, parent_planets, center_object_name)` (line 598) -- Determine appropriate time interval for fetching orbit data.
- `fetch_orbit_path(obj_info, start_date, end_date, interval, center_id, id_type)` (line 642) -- Fetch orbit path data from JPL Horizons.
- `calculate_planet9_orbit(start_date, end_date, interval)` (line 699) -- Calculate synthetic orbit for hypothetical Planet 9.
- `calculate_planet9_position(theta_offset)` (line 791) -- Calculate a fixed position for Planet 9 based on our best estimate.
- `update_status(message)` (line 843) -- Update status display if available and print to console.
- `fetch_orbit_path_by_dates(obj_info, start_date, end_date, interval, center_id, id_type)` (line 865) -- Fetch orbit path data for specific date range and convert to time-indexed format.
- `merge_orbit_data(existing_data, new_data, new_start_date, new_end_date)` (line 934) -- Merge new orbit data with existing data.
- `fetch_complete_orbit_path(obj, orbit_key, today, end_window, interval, center_id, center_id_type)` (line 960) -- Fetch and store a complete orbit path for an object.
- `get_planet9_data(center_object_name)` (line 1036) -- Get Planet 9 data for different center objects.
- `update_orbit_paths_incrementally(object_list, center_object_name, days_ahead, fetch_requests, planetary_params, parent_planets, root_widget)` (line 1066) -- Update orbit paths incrementally, fetching only missing data.
- `get_orbit_data_for_plotting(objects_to_plot, center_object_name)` (line 1320) -- Get orbit path data for plotting.
- `get_data_stats()` (line 1385) -- Get statistics about the stored orbit data.
- `on_center_change()` (line 1450) -- Update orbit paths when the center object is changed.
- `plot_orbit_paths(fig, objects_to_plot, center_object_name, color_map, parent_planets)` (line 1517) -- Plot orbit paths using time-indexed data.
- `query_horizons_elements(horizons_id, id_type, date_str, center_body)` (line 1645) -- Query JPL Horizons for osculating orbital elements (Keplerian).

---

### osculating_cache_manager.py

**Role:** cache | **Lines:** 761

> Auto-updating cache for osculating orbital elements from JPL Horizons. Uses two-generation backup protection and always-prompt user workflow.

**Depends on:** orbit_data_manager, orbital_elements
**Consumed by:** idealized_orbits, palomas_orrery, spacecraft_encounters

**Public functions:**

- `get_cache_key(obj_name, center_body)` (line 32) -- Generate cache key for an object, optionally with center body suffix.
- `get_refresh_interval(obj_name)` (line 106) -- Get recommended refresh interval for object (in days).
- `save_cache(cache)` (line 149) -- Save cache with two-generation backup protection.
- `load_cache()` (line 218) -- Load cache with two-generation recovery.
- `create_empty_cache()` (line 270) -- Create empty cache structure with metadata.
- `calculate_age_days(cache_entry)` (line 285) -- Calculate age of cache entry in days.
- `check_cache_status(obj_name, center_body)` (line 304) -- Check cache status for an object.
- `fetch_osculating_elements(obj_name, horizons_id, id_type, date, center_body)` (line 364) -- Fetch osculating elements from JPL Horizons.
- `fetch_solution_tp(obj_name, horizons_id, id_type)` (line 459) -- Fetch the solution-level TP from JPL Horizons raw response header.
- `cache_solution_tp(obj_name, tp_jd, center_body)` (line 530) -- Store solution-level TP in the osculating cache alongside existing data.
- `resolve_tp(obj_name, obj_info, center_body)` (line 566) -- Resolve the best available TP for an object using a four-path hierarchy.
- `format_age_string(age_days)` (line 653) -- Format age in human-readable string.
- `format_interval_string(interval_days)` (line 681) -- Format refresh interval in human-readable string.
- `get_elements_with_prompt(obj_name, horizons_id, id_type, plot_date, parent_window, center_body)` (line 703) -- Get orbital elements with user prompt - ALWAYS prompts with information.
- `get_fallback_elements(obj_name)` (line 817) -- Get elements from cache or manual dictionary (fallback).
- `format_for_python_dict(obj_name, elements)` (line 854) -- Format elements as Python dictionary string for easy copying.

---

### verify_orbit_cache.py

**Role:** cache | **Lines:** 170

> verify_orbit_cache.py - Safely verify and repair orbit_paths.json

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `create_backup(file_path)` (line 19) -- Create a timestamped backup of the orbit cache file.
- `verify_orbit_cache(file_path, repair)` (line 35) -- Verify the orbit cache file and optionally repair it.

---

### vot_cache_manager.py

**Role:** cache | **Lines:** 430

> VOT Cache Manager - Safe management of VizieR VOT cache files Similar protection protocols as PKL files in simbad_manager.py

**Depends on:** (none)
**Consumed by:** data_acquisition_distance, simbad_manager

**Public functions:**

- `class VOTCacheMetadata` (line 24) -- Metadata for VOT cache files
- `class VOTCacheManager` (line 44) -- Manager for safe VOT cache file operations
- `integrate_vot_protection_with_simbad_manager(simbad_manager)` (line 384) -- Add VOT cache management methods to existing SimbadQueryManager.
- `verify_vot_cache_integrity()` (line 436) -- Verify integrity of all VOT cache files
- `create_vot_cache_report()` (line 459) -- Generate detailed report of VOT cache status

---

## PIPELINE: Transforms data between stages (export, conversion)

### convert_hot_ph_to_json.py

**Role:** pipeline | **Lines:** 197

> Convert HOT ocean pH data to JSON format Manual converter for ocean acidification visualization

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `find_hot_data_file()` (line 10) -- Find HOT data file - try multiple possible filenames
- `parse_hot_ph_csv(filename)` (line 34) -- Parse HOT carbonate chemistry CSV from BCO-DMO
- `create_metadata(records)` (line 127) -- Create metadata for the pH dataset
- `main()` (line 178) -- Main conversion workflow

---

### plot_data_exchange.py

**Role:** pipeline | **Lines:** 168

> plot_data_exchange.py - JSON data exchange between subprocess scripts and GUI.

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, star_visualization_gui

**Public functions:**

- `class PlotDataExchange` (line 18) -- Exchange plot data between subprocess scripts and GUI.

---

### save_utils.py

**Role:** pipeline | **Lines:** 388

> Consolidated utility functions for saving Plotly visualizations.

**Depends on:** (none)
**Consumed by:** earth_system_visualization_gui, energy_imbalance, paleoclimate_dual_scale, paleoclimate_human_origins_full, paleoclimate_visualization, paleoclimate_visualization_full, paleoclimate_wet_bulb_full, palomas_orrery, palomas_orrery_helpers, sgr_a_grand_tour, sgr_a_visualization_animation, sgr_a_visualization_core, sgr_a_visualization_precession, shutdown_handler, social_media_export, star_visualization_gui, visualization_2d, visualization_3d

**Public functions:**

- `save_visualization(fig, default_name, mode, output_path, offline, auto_play, open_browser)` (line 109) -- Unified save function for all Plotly visualizations.
- `show_and_save(fig, default_name, auto_play)` (line 351) -- Show visualization in browser, then offer save dialog.
- `save_plot(fig, default_name)` (line 415) -- Legacy function for backward compatibility.
- `handle_save(fig, default_name)` (line 433) -- Legacy function for backward compatibility.
- `show_animation_safely(fig, default_name)` (line 446) -- Show and optionally save an animation.
- `save_html(fig, filename, offline, open_browser)` (line 467) -- Simple direct save for scripts that don't need dialogs.

---

### social_media_export.py

**Role:** pipeline | **Lines:** 969

> Generates a second HTML file from an existing Plotly figure, optimized for screen recording Instagram Reels and YouTube Shorts (9:16 portrait).

**Depends on:** save_utils
**Consumed by:** palomas_orrery, star_visualization_gui

**Public functions:**

- `get_trace_names(fig)` (line 803) -- Get a list of trace names from a Plotly figure.
- `show_trace_selection_dialog(fig, parent)` (line 827) -- Show a dialog with checkboxes for each trace in the figure.
- `export_social_html(fig, output_path, open_browser, plotly_js, trace_names)` (line 1056) -- Export a Plotly figure as a social-media-optimized HTML file.

---

## SCENARIO: Specific Earth system scenarios

### scenarios_coral_bleaching.py

**Role:** scenario | **Lines:** 191

> Paloma's Orrery: Coral Bleaching Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: NOAA Coral Reef Watch (ERDDAP API) - Degree Heating Weeks (DHW)

**Depends on:** (none)
**Consumed by:** earth_system_generator

**Public functions:**

- `fetch_noaa_coral(scenario, data_dir, status_callback)` (line 19) -- Fetches Degree Heating Week data from NOAA Coral Reef Watch ERDDAP.

---

### scenarios_heatwaves.py

**Role:** scenario | **Lines:** 622

> Paloma's Orrery: Heatwave Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: ERA5 via Open-Meteo Archive API

**Depends on:** (none)
**Consumed by:** earth_system_generator

**Public functions:**

- `fetch_era5_heatwave(scenario, data_dir, status_callback)` (line 13) -- Fetches historic wet-bulb data from ERA5 via Open-Meteo Archive API.

---

### scenarios_western_heatwave_march_2026.py

**Role:** scenario | **Lines:** 1,536

> Paloma's Orrery: Western North America Heat Dome - March 2026 Scenario Module: Parameterized Timeline Snapshots

**Depends on:** earth_system_generator
**Consumed by:** earth_system_generator

**Public functions:**

- `fetch_western_heatwave(scenario, data_dir, status_callback)` (line 841) -- Shared fetch function for all Western Heatwave snapshots.
- `generate_all(engine_module)` (line 1613) -- Generate all 5 snapshots through the engine pipeline.
- `validate_snapshots()` (line 1656) -- Quick validation: build all 5 synthetic fields and report stats.

---

## UTILITY: Shared helper functions

### formatting_utils.py

**Role:** utility | **Lines:** 16

> formatting_utils.py - Basic formatting utilities used by both palomas_orrery.py and visualization_utils.py.

**Depends on:** (none)
**Consumed by:** exoplanet_orbits, palomas_orrery, palomas_orrery_helpers, visualization_utils

**Public functions:**

- `format_maybe_float(value)` (line 3) -- If 'value' is a numeric type (int or float), return it formatted
- `format_km_float(value)` (line 12) -- Format kilometer values in scientific notation with 2 decimal places.

---

### palomas_orrery_helpers.py

**Role:** utility | **Lines:** 777

> palomas_orrery_helpers.py - Support functions extracted from the main orrery monolith.

**Depends on:** constants_new, formatting_utils, idealized_orbits, orbit_data_manager, planet_visualization, save_utils, shared_utilities, shutdown_handler, solar_visualization_shells, visualization_utils
**Consumed by:** orbital_param_viz, palomas_orrery

**Public functions:**

- `calculate_planet9_position_on_orbit(a, e, i, omega, Omega, theta)` (line 220) -- Calculate position that lies exactly on the orbit defined by the parameters
- `rotate_points2(x, y, z, angle, axis)` (line 268) -- Rotates points (x,y,z) about the given axis by 'angle' radians.
- `calculate_axis_range(objects_to_plot)` (line 316) -- Calculate appropriate axis range based on outermost planet
- `fetch_trajectory(object_id, dates_list, center_id, id_type, start_date, end_date)` (line 333) -- Fetch trajectory data in batch for all dates, handling missing epochs through interpolation.
- `fetch_orbit_path(obj_info, start_date, end_date, interval, center_id, id_type)` (line 559) -- Fetch orbit path data from JPL Horizons for the given object between start_date and end_date,
- `pad_trajectory(global_dates, object_start_date, object_end_date, object_id, center_id, id_type)` (line 609) -- Fetch trajectory and pad with None before start_date and after end_date.
- `add_url_buttons(fig, objects_to_plot, selected_objects)` (line 644) -- Add URL buttons for missions and objects in solar system visualizations.
- `get_default_camera()` (line 754) -- Return the default orthographic camera settings for top-down view
- `print_planet_positions(positions)` (line 766) -- Print positions and distances for planets.
- `create_orbit_backup()` (line 796) -- Create a backup of orbit cache on startup
- `cleanup_old_orbits()` (line 829) -- Remove orbit data older than 30 days
- `show_animation_safely(fig, default_name)` (line 901) -- Show and optionally save an animation.

---

### report_manager.py

**Role:** utility | **Lines:** 124

> Scientific Report Manager for Astronomical Data Analysis Manages generation, storage, and retrieval of analysis reports.

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, plot_data_report_widget, star_visualization_gui

**Public functions:**

- `class ReportManager` (line 13) -- Manages scientific reports for astronomical data analysis.

---

### shared_utilities.py

**Role:** utility | **Lines:** 123

> shared_utilities.py - Small shared helpers used across shell visualization modules.

**Depends on:** (none)
**Consumed by:** asteroid_belt_visualization_shells, comet_visualization_shells, earth_visualization_shells, eris_visualization_shells, jupiter_visualization_shells, mars_visualization_shells, mercury_visualization_shells, moon_visualization_shells, neptune_visualization_shells, palomas_orrery, palomas_orrery_helpers, planet9_visualization_shells, pluto_visualization_shells, saturn_visualization_shells, solar_visualization_shells, uranus_visualization_shells, venus_visualization_shells

**Public functions:**

- `create_sun_direction_indicator(center_position, axis_range, shell_radius, object_type, center_object)` (line 15) -- Creates a visual indicator showing the direction to the Sun (along negative X-axis).

---

### shutdown_handler.py

**Role:** utility | **Lines:** 73

> shutdown_handler.py - Graceful shutdown and safe figure display for Plotly.

**Depends on:** save_utils
**Consumed by:** orbital_param_viz, palomas_orrery, palomas_orrery_helpers, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `class PlotlyShutdownHandler` (line 24) -- Handles graceful shutdown for Plotly visualizations and associated threads.
- `create_monitored_thread(handler, target_func)` (line 66) -- Create a thread that's monitored by the shutdown handler.
- `show_figure_safely(fig, default_name)` (line 78) -- Show and optionally save a Plotly figure with proper cleanup.

---

## DEVTOOL: Developer tools (dependency tracing, atlas)

### dep_trace.py

**Role:** devtool | **Lines:** 399

> dep_trace.py - Targeted dependency path tracer for Paloma's Orrery Usage: python dep_trace.py <module_name> [hops]

**Depends on:** module_atlas
**Consumed by:** (none -- standalone)

**Public functions:**

- `get_imports(filepath)` (line 75) -- Extract local module imports from a Python file using AST.
- `build_graph(project_dir)` (line 93) -- Build full bidirectional dependency graph for all local modules.
- `find_neighborhood(target, deps, consumers, hops)` (line 117) -- Walk outward from target by `hops` steps in both directions.
- `get_category(mod)` (line 157) -- Get visual category for a module, using module_atlas ROLE_MAP as source.
- `get_module_description(filepath)` (line 170) -- Extract the first meaningful line of the module docstring.
- `print_report(target, nodes, edges, hubs, deps, consumers)` (line 201)
- `to_mermaid(target, nodes, edges, hubs)` (line 232)
- `ensure_vis_network(project_dir)` (line 258) -- Download vis-network.min.js once to project_dir if not present.
- `to_html(target, nodes, edges, hubs, deps, consumers, project_dir)` (line 273) -- Generate a self-contained interactive HTML graph using vis-network.
- `main()` (line 424)

---

## OTHER: Uncategorized

### add_docstrings.py

**Role:** other | **Lines:** 631

> add_docstrings.py - Add or improve module-level docstrings across the codebase.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `detect_line_ending(content_bytes)` (line 594) -- Detect whether file uses CRLF or LF.
- `has_existing_docstring(content_bytes)` (line 601) -- Check if file starts with a docstring (triple quotes).
- `has_leading_comment(content_bytes)` (line 607) -- Check if file starts with # comments (before imports).
- `insert_docstring(content_bytes, docstring_text, line_ending)` (line 613) -- Insert docstring at the top of a file, before any existing content.
- `process_module(project_dir, module_name, docstring_text, write)` (line 649) -- Process a single module: read, insert docstring, optionally write.
- `main()` (line 682)

---

### diagnose_bcodmo.py

**Role:** other | **Lines:** 65

> Diagnostic script to examine BCO-DMO pH data structure

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `examine_bcodmo_data()` (line 6) -- Download and examine the structure of BCO-DMO pH data

---

### examine_hot_csv.py

**Role:** other | **Lines:** 45

> Examine the HOT CSV file structure

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `examine_csv()` (line 6)

---

### messier_object_data_handler.py

**Role:** other | **Lines:** 329

> messier_object_data_handler.py - Messier object coordinate transforms and data preparation.

**Depends on:** messier_catalog, star_notes
**Consumed by:** planetarium_apparent_magnitude

**Public functions:**

- `class MessierObjectHandler` (line 28) -- Handles all Messier object related operations.

---

### module_atlas.py

**Role:** other | **Lines:** 484

> module_atlas.py - Codebase encyclopedia generator for Paloma's Orrery

**Depends on:** (none)
**Consumed by:** dep_trace

**Public functions:**

- `classify_role(module_name)` (line 155) -- Classify a module's functional role.
- `get_module_docstring(filepath)` (line 187) -- Extract module-level docstring, falling back to leading comments.
- `get_public_functions(filepath)` (line 274) -- Extract public function/class names with their docstrings.
- `get_local_imports(filepath, local_modules)` (line 305) -- Extract project-local imports from a Python file.
- `count_lines(filepath)` (line 328) -- Count non-blank lines in a file.
- `build_dependency_graph(project_dir)` (line 341) -- Build bidirectional dependency graph for all local modules.
- `generate_atlas(project_dir, output_path)` (line 366) -- Generate the MODULE_ATLAS.md file.
- `main()` (line 542)

---

### sgr_a_visualization_core_arcs.py

**Role:** other | **Lines:** 535

> sgr_a_visualization_core.py Core visualization module for S-Stars orbiting Sagittarius A*.

**Depends on:** sgr_a_star_data
**Consumed by:** (none -- standalone)

**Public functions:**

- `generate_orbit_points(star_data, num_points, precession_offset_deg)` (line 35) -- Generate 3D orbit points for a star.
- `generate_position_at_true_anomaly(star_data, true_anomaly_rad, precession_offset_deg)` (line 100) -- Generate 3D position for a star at a specific true anomaly.
- `create_sgr_a_marker(scale_factor)` (line 149) -- Create the Sagittarius A* black hole marker.
- `create_orbit_trace(star_name, star_data, show_periapsis)` (line 378) -- Create the orbital path trace for a star.
- `create_star_marker(star_name, star_data, true_anomaly_rad, precession_offset_deg)` (line 456) -- Create a marker showing the star's current position.
- `create_sgr_a_figure(stars_to_show, show_all_stars)` (line 508) -- Create the main Sagittarius A* visualization figure.

---

### test_orbit_cache.py

**Role:** other | **Lines:** 204

> test_orbit_cache.py - Comprehensive test suite for orbit data caching and repair

**Depends on:** orbit_data_manager
**Consumed by:** (none -- standalone)

**Public functions:**

- `class TestOrbitCache` (line 28) -- Test suite for orbit data caching functionality

---

## Alphabetical Index

| Module | Role | Lines | Deps | Consumers |
|--------|------|------:|-----:|----------:|
| add_docstrings | other | 631 | 0 | 0 |
| apsidal_markers | computation | 1,681 | 1 | 4 |
| asteroid_belt_visualization_shells | rendering/shells | 410 | 1 | 2 |
| catalog_selection | computation | 92 | 1 | 3 |
| celestial_coordinates | computation | 454 | 0 | 1 |
| celestial_objects | data | 1,225 | 0 | 1 |
| climate_cache_manager | cache | 161 | 1 | 1 |
| close_approach_data | data | 519 | 1 | 1 |
| comet_visualization_shells | rendering/shells | 1,647 | 2 | 1 |
| constants_new | data | 2,401 | 0 | 14 |
| convert_hot_ph_to_json | pipeline | 197 | 0 | 0 |
| coordinate_system_guide | computation | 547 | 0 | 0 |
| create_cache_backups | cache | 8 | 1 | 0 |
| create_ephemeris_database | cache | 243 | 1 | 0 |
| data_acquisition | computation | 220 | 0 | 4 |
| data_acquisition_distance | computation | 169 | 2 | 1 |
| data_processing | computation | 434 | 0 | 5 |
| dep_trace | devtool | 399 | 1 | 0 |
| diagnose_bcodmo | other | 65 | 0 | 0 |
| earth_system_controller | gui | 81 | 0 | 0 |
| earth_system_generator | computation | 688 | 3 | 1 |
| earth_system_visualization_gui | gui | 1,822 | 8 | 1 |
| earth_visualization_shells | rendering/shells | 846 | 2 | 1 |
| energy_imbalance | computation | 839 | 1 | 1 |
| eris_visualization_shells | rendering/shells | 407 | 2 | 1 |
| examine_hot_csv | other | 45 | 0 | 0 |
| exoplanet_coordinates | data | 399 | 1 | 0 |
| exoplanet_orbits | rendering | 613 | 3 | 1 |
| exoplanet_stellar_properties | data | 485 | 3 | 3 |
| exoplanet_systems | data | 570 | 0 | 3 |
| fetch_climate_data | computation | 761 | 0 | 1 |
| fetch_paleoclimate_data | computation | 169 | 0 | 0 |
| formatting_utils | utility | 16 | 0 | 4 |
| hr_diagram_apparent_magnitude | rendering | 430 | 12 | 1 |
| hr_diagram_distance | rendering | 449 | 13 | 1 |
| idealized_orbits | computation | 6,164 | 4 | 5 |
| incremental_cache_manager | cache | 657 | 1 | 4 |
| jupiter_visualization_shells | rendering/shells | 778 | 2 | 1 |
| mars_visualization_shells | rendering/shells | 710 | 2 | 1 |
| mercury_visualization_shells | rendering/shells | 650 | 2 | 1 |
| messier_catalog | data | 404 | 0 | 3 |
| messier_object_data_handler | other | 329 | 2 | 1 |
| module_atlas | other | 484 | 0 | 1 |
| moon_visualization_shells | rendering/shells | 442 | 2 | 1 |
| neptune_visualization_shells | rendering/shells | 1,513 | 3 | 1 |
| object_type_analyzer | computation | 754 | 1 | 3 |
| orbit_data_manager | cache | 1,520 | 0 | 4 |
| orbital_elements | computation | 1,285 | 0 | 4 |
| orbital_param_viz | gui | 1,936 | 5 | 1 |
| osculating_cache_manager | cache | 761 | 2 | 3 |
| paleoclimate_dual_scale | rendering | 955 | 2 | 1 |
| paleoclimate_human_origins_full | rendering | 1,884 | 1 | 1 |
| paleoclimate_visualization | rendering | 478 | 1 | 2 |
| paleoclimate_visualization_full | rendering | 1,487 | 1 | 1 |
| paleoclimate_wet_bulb_full | rendering | 2,224 | 1 | 1 |
| palomas_orrery | gui | 8,254 | 27 | 0 |
| palomas_orrery_dashboard | gui | 599 | 0 | 0 |
| palomas_orrery_helpers | utility | 777 | 10 | 2 |
| planet9_visualization_shells | rendering/shells | 243 | 2 | 1 |
| planet_visualization | rendering | 1,046 | 16 | 2 |
| planet_visualization_utilities | rendering | 290 | 1 | 15 |
| planetarium_apparent_magnitude | rendering | 352 | 11 | 1 |
| planetarium_distance | rendering | 399 | 11 | 1 |
| plot_data_exchange | pipeline | 168 | 0 | 3 |
| plot_data_report_widget | rendering | 560 | 2 | 1 |
| pluto_visualization_shells | rendering/shells | 484 | 2 | 1 |
| report_manager | utility | 124 | 0 | 4 |
| saturn_visualization_shells | rendering/shells | 1,002 | 2 | 3 |
| save_utils | pipeline | 388 | 0 | 18 |
| scenarios_coral_bleaching | scenario | 191 | 0 | 1 |
| scenarios_heatwaves | scenario | 622 | 0 | 1 |
| scenarios_western_heatwave_march_2026 | scenario | 1,536 | 1 | 1 |
| sgr_a_grand_tour | rendering | 742 | 3 | 1 |
| sgr_a_star_data | data | 555 | 2 | 5 |
| sgr_a_visualization_animation | rendering | 343 | 3 | 0 |
| sgr_a_visualization_core | rendering | 557 | 2 | 3 |
| sgr_a_visualization_core_arcs | other | 535 | 1 | 0 |
| sgr_a_visualization_precession | rendering | 377 | 3 | 0 |
| shared_utilities | utility | 123 | 0 | 17 |
| shutdown_handler | utility | 73 | 1 | 5 |
| simbad_manager | computation | 1,028 | 2 | 6 |
| social_media_export | pipeline | 969 | 1 | 2 |
| solar_visualization_shells | rendering/shells | 1,437 | 2 | 6 |
| spacecraft_encounters | data | 1,204 | 2 | 1 |
| star_notes | data | 1,137 | 0 | 5 |
| star_properties | data | 338 | 2 | 4 |
| star_sphere_builder | rendering | 922 | 0 | 1 |
| star_visualization_gui | gui | 1,406 | 11 | 0 |
| stellar_data_patches | data | 41 | 0 | 4 |
| stellar_parameters | data | 352 | 2 | 8 |
| test_orbit_cache | other | 204 | 1 | 0 |
| uranus_visualization_shells | rendering/shells | 988 | 3 | 1 |
| venus_visualization_shells | rendering/shells | 619 | 2 | 1 |
| verify_orbit_cache | cache | 170 | 0 | 0 |
| visualization_2d | rendering | 524 | 6 | 2 |
| visualization_3d | rendering | 858 | 5 | 2 |
| visualization_core | rendering | 351 | 4 | 7 |
| visualization_utils | rendering | 725 | 3 | 3 |
| vot_cache_manager | cache | 430 | 0 | 2 |

---

*Generated by module_atlas.py -- Paloma's Orrery Developer Tools*
