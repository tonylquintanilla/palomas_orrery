# Paloma's Orrery -- Module Atlas

Generated: April 14, 2026
Modules: 99 | Functions: 785 | Lines: 86,139

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
| gui | 9 | Applications the user launches (GUIs, editors) |
| rendering | 22 | Builds visual traces, figures, and charts |
| rendering/shells | 15 | Planetary shell visualizations (sphere layers) |
| computation | 15 | Math, orbital mechanics, data processing |
| data | 13 | Catalogs, constants, and static datasets |
| cache | 8 | Fetch, store, and retrieve computed data |
| pipeline | 5 | Transforms data between stages (export, conversion) |
| scenario | 3 | Specific Earth system scenarios |
| utility | 6 | Shared helper functions |
| devtool | 1 | Developer tools (dependency tracing, atlas) |
| legacy | 1 | Archived / superseded modules |
| other | 1 | Uncategorized |

---

## GUI: Applications the user launches (GUIs, editors)

### earth_system_controller.py

**Role:** gui | **Lines:** 74

> (no description)

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `class MissionControlApp` (line 7)

---

### earth_system_visualization_gui.py

**Role:** gui | **Lines:** 1,807

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
- `open_warming_stripes()` (line 573) -- Open the Ed Hawkins warming stripes heatmap.
- `create_ice_viz()` (line 588) -- Create Arctic sea ice extent visualization - Updated with correct data source
- `load_sea_level_data()` (line 769) -- Load sea level data from cached JSON file
- `create_sea_level_viz()` (line 783) -- Create interactive sea level rise visualization
- `load_ph_data()` (line 936) -- Load ocean pH data from JSON cache
- `create_ph_viz()` (line 948) -- Create interactive ocean acidification (pH) visualization
- `create_planetary_boundaries_viz()` (line 1120) -- Planetary Boundaries - keep Tony's style & notes
- `open_ph_viz()` (line 1408) -- Open ocean pH visualization in browser
- `open_planetary_boundaries()` (line 1426) -- Open Planetary Boundaries visualization in browser
- `open_paleoclimate_viz()` (line 1445) -- Open Cenozoic paleoclimate visualization
- `open_paleoclimate_dual_scale_viz()` (line 1462) -- Open dual-scale paleoclimate visualization (modern + deep time)
- `open_phanerozoic_viz()` (line 1479) -- Open Phanerozoic (540 Ma) paleoclimate visualization
- `open_human_origins_viz()` (line 1500) -- Open Paleoclimate + Human Origins visualization (540 Ma + 25 hominin species)
- `open_sea_level_viz()` (line 1521) -- Open sea level visualization in browser
- `open_keeling_curve()` (line 1540) -- Open Keeling Curve in browser
- `open_temperature_viz()` (line 1552) -- Open temperature visualization in browser
- `open_ice_viz()` (line 1564) -- Open Arctic ice visualization in browser
- `open_energy_imbalance()` (line 1578) -- Open energy imbalance visualization in browser
- `run_update_in_thread(update_button, status_label, window)` (line 1590) -- Run climate data update in background thread
- `open_wet_bulb_viz()` (line 1650) -- Open Wet Bulb Temperature paleoclimate visualization
- `open_google_earth_controller()` (line 1668) -- Launch the Google Earth KML layer controller
- `open_earth_system_gui(parent)` (line 1683) -- Open Earth System Visualization hub window

---

### gallery_editor.py

**Role:** gui | **Lines:** 1,293

> Gallery Metadata Editor for Paloma's Orrery GUI to edit visualization titles, descriptions, categories, reorder items and categories, and copy/move visualizations within the gallery_metadata.json file.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `load_config(filepath)` (line 37) -- Load gallery_config.json. Returns list of category dicts.
- `save_config(filepath, categories)` (line 47) -- Save gallery_config.json.
- `config_to_map(categories)` (line 54) -- Convert category list to key->label dict.
- `config_to_color_map(categories)` (line 59) -- Convert category list to key->color dict.
- `load_metadata(filepath)` (line 68) -- Load gallery_metadata.json and return the data dict.
- `save_metadata(filepath, data)` (line 74) -- Save gallery_metadata.json with a backup first.
- `get_category_order(vizs, mode_key)` (line 90) -- Derive category display order from JSON sequence for a given mode.
- `make_label_to_key(label)` (line 111) -- Convert a category label to a snake_case key.
- `class GalleryEditor` (line 125)

---

### gallery_studio.py

**Role:** gui | **Lines:** 4,815

> Gallery Studio - Interactive HTML Export Tool for Paloma's Orrery

**Depends on:** constants_new, visualization_utils
**Consumed by:** (none -- standalone)

**Public functions:**

- `class ToolTip` (line 348) -- Hover tooltip for Tkinter widgets.
- `extract_figure_from_html(html_path)` (line 492) -- Extract Plotly figure dict from an HTML file.
- `extract_encyclopedia_for_figure(fig_dict)` (line 694) -- Extract encyclopedia entries for objects present in a Plotly figure.
- `apply_config(fig_dict, config)` (line 819) -- Apply studio configuration to a Plotly figure dict.
- `build_gallery_html(fig_dict, config, title)` (line 2003) -- Build a standalone gallery-ready HTML file from a figure dict.
- `build_social_html(fig_dict, config, title)` (line 2915) -- Build a 9:16 portrait HTML with info panel for social media.
- `class GalleryStudio` (line 3309) -- Tkinter GUI for configuring and exporting gallery-ready HTML.
- `main()` (line 5375) -- Launch the Gallery Studio.

---

### json_gallery.py

**Role:** gui | **Lines:** 524

> A lightweight Dash web application that serves interactive Plotly visualizations from the gallery folder for local development and preview. The production gallery runs as static HTML on GitHub Pages (index.html).

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `load_metadata(data_folder)` (line 84) -- Load gallery metadata from JSON file.
- `load_figure(data_folder, filename)` (line 94) -- Load a Plotly figure from JSON file.
- `get_welcome_figure()` (line 122) -- Create a placeholder figure for the landing page.
- `create_layout(metadata)` (line 146) -- Build the Dash app layout.
- `create_app(data_folder)` (line 431) -- Create and configure the Dash application.
- `main()` (line 552)

---

### orbital_param_viz.py

**Role:** gui | **Lines:** 1,923

> (no description)

**Depends on:** apsidal_markers, constants_new, idealized_orbits, palomas_orrery_helpers, shutdown_handler
**Consumed by:** palomas_orrery

**Public functions:**

- `class CreateToolTip` (line 16) -- Create a tooltip for a given widget with intelligent positioning to prevent clipping.
- `rotation_matrix_x(angle)` (line 122) -- Create rotation matrix around X axis
- `rotation_matrix_z(angle)` (line 129) -- Create rotation matrix around Z axis
- `add_coordinate_frame(fig, name, color, R_transform, axis_length, show_labels, opacity, line_width, show_in_legend, visible)` (line 136) -- Add a 3D coordinate frame with the given transformation.
- `add_angle_arc(fig, angle_rad, radius, axis, color, label, start_angle, show_in_legend, legendgroup)` (line 205) -- Add an arc showing a rotation angle
- `create_orbital_transformation_viz(fig, obj_name, planetary_params, show_steps, show_axes, plot_date, center_object, parent_planets, show_apsidal_markers, current_position)` (line 234) -- Create a visualization showing how orbital parameters transform to 3D orbit.
- `create_eccentricity_demo_window(parent, objects, planetary_params_override)` (line 1065) -- Create a window with an interactive eccentricity slider visualization.
- `create_orbital_viz_window(root, objects, planetary_params, parent_planets, current_positions, current_date)` (line 1894) -- Create a window for orbital parameter visualization.
- `create_orbital_transformation_viz_legacy(fig, obj_name, planetary_params)` (line 2275) -- Legacy function for compatibility

---

### palomas_orrery.py

**Role:** gui | **Lines:** 8,615

> Paloma's Orrery - Solar System Visualization Tool annotated by Tony working with Claude

**Depends on:** apsidal_markers, asteroid_belt_visualization_shells, celestial_objects, close_approach_data, comet_visualization_shells, constants_new, earth_system_visualization_gui, exoplanet_orbits, exoplanet_stellar_properties, exoplanet_systems, formatting_utils, idealized_orbits, orbit_data_manager, orbital_elements, orbital_param_viz, osculating_cache_manager, palomas_orrery_helpers, planet_visualization, save_utils, sgr_a_grand_tour, shared_utilities, shutdown_handler, social_media_export, solar_visualization_shells, spacecraft_encounters, star_sphere_builder, visualization_utils
**Consumed by:** (none -- standalone)

**Public functions:**

- `get_fetch_interval_for_type(obj_type, obj_name, trajectory_interval, default_interval, satellite_interval, planetary_params)` (line 294) -- Get the appropriate fetch interval based on object type.
- `create_dates_list_for_object(obj, obj_type, date_obj, trajectory_points, orbital_points, satellite_days, satellite_points, start_date, end_date, planetary_params, parent_planets, center_object_name, max_date, settings)` (line 315) -- Create a list of dates for plotting based on object type.
- `handle_update_dialog(num_objects)` (line 397) -- Handle the update dialog for cache updates.
- `get_interval_settings()` (line 459) -- Get all interval settings from the GUI entries.
- `get_date_from_gui()` (line 533) -- Get the date from GUI entry fields.
- `create_animation_dates(current_date, step, N)` (line 552) -- Create dates list specifically for animations.
- `calculate_axis_range_from_orbits(selected_objects, positions, planetary_params, parent_planets, center_object_name)` (line 602) -- Calculate appropriate axis range based on orbital parameters.
- `get_improved_axis_range(scale_var, custom_scale_entry, selected_objects, positions, planetary_params, parent_planets, center_object_name)` (line 814) -- Get axis range using improved scaling logic.
- `get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name)` (line 832) -- Get axis range for animations using the same logic as static plots.
- `calculate_satellite_precession_info(selected_objects, start_date, end_date, center_object_name)` (line 853) -- Calculate precession information for selected satellites based on date range.
- `get_best_orbit(object_name, primary, idealized_func)` (line 979) -- Get the best available orbit function for an object.
- `plot_refined_orbits_for_moons(fig, moon_names, center_id, color_map, orbit_data, date_obj, date_range)` (line 1014) -- Add refined orbit traces for moons using refined_orbits module.
- `create_refined_orbit_with_actual_data(satellite, primary, actual_orbit_data, refined_orbits_module)` (line 1153) -- Create a refined orbit using provided actual orbit data.
- `load_window_config()` (line 1405) -- Load saved window geometry and sash positions from config file.
- `save_window_config()` (line 1415) -- Save current window geometry and sash positions to config file.
- `fetch_position(object_id, date_obj, center_id, id_type, override_location, mission_url, mission_info)` (line 1531)
- `calculate_analytical_position(obj_name, date_obj, center_id)` (line 2007) -- Calculate position from analytical orbital elements when Horizons is unavailable.
- `fetch_radec_for_hover(object_id, date_obj, id_type)` (line 2090) -- Fetch RA/Dec and uncertainties for hover text
- `add_celestial_object(fig, obj_data, name, color, symbol, marker_size, hover_data, center_object_name)` (line 2160)
- `update_status_display(message, status_type)` (line 2233) -- Update status display with color coding and history
- `configure_controls_canvas(event)` (line 2272)
- `class ScrollableFrame` (line 3055) -- A scrollable frame that can contain multiple widgets with a vertical scrollbar.
- `class CreateToolTip` (line 3156) -- Create a tooltip for a given widget with intelligent positioning to prevent clipping.
- `pulse_progress_bar()` (line 3313) -- Create a pulsating effect for the progress bar
- `update_orbit_paths(center_object_name)` (line 3319) -- For each object in the global 'objects' list that has an 'id', check if its orbit path is
- `plot_orbit_paths(fig, objects_to_plot, center_object_name)` (line 3417) -- Plot orbit paths using data from orbit_data_manager or temp cache.
- `plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id, show_lines, center_object_name, show_closest_approach, trajectory_marker_color)` (line 3471) -- Plot actual orbit positions for selected objects.
- `export_social_view()` (line 3872) -- Export the last plotted figure as a social media view.
- `plot_objects()` (line 3899)
- `animate_objects(step, label)` (line 5744)
- `on_closing()` (line 7428) -- Handle cleanup when the main window is closed.
- `periodic_config_save()` (line 7453)
- `set_palomas_birthday()` (line 7460)
- `update_date_fields(new_date)` (line 7464)
- `fill_now()` (line 7477)
- `calculate_next_vernal_equinox(from_date)` (line 7504) -- Calculate the next vernal equinox (March equinox) from a given date.
- `fill_next_vernal_equinox()` (line 7574) -- Fill the date fields with the next vernal equinox from the current date.
- `toggle_all_shells()` (line 7585) -- Toggle all sun shell checkboxes based on the main shell checkbox.
- `handle_mission_selection()` (line 7617)
- `animate_one_minute()` (line 7623)
- `animate_one_hour()` (line 7629)
- `animate_one_day()` (line 7634)
- `animate_one_week()` (line 7640)
- `animate_one_month()` (line 7645)
- `animate_one_year()` (line 7650)
- `animate_palomas_birthday()` (line 7655)
- `report_callback_exception(exc_type, exc_value, exc_traceback)` (line 7685)
- `sync_end_date_from_days()` (line 7697) -- Calculate end date from start date + days to plot
- `sync_days_from_dates()` (line 7728) -- Calculate days to plot from start and end dates
- `sync_days_from_dates()` (line 7740) -- Calculate days to plot from start and end dates
- `sync_end_date_from_days()` (line 7839) -- Calculate end date from start date + days to plot
- `sync_days_from_dates()` (line 7871) -- Calculate days to plot from start and end dates
- `get_end_date_from_gui()` (line 7883) -- Get end date from GUI fields. Defaults empty fields to avoid crash.
- `can_be_horizons_center(obj)` (line 7915) -- Check if object can be used as Horizons coordinate center.
- `create_celestial_checkbutton(name, variable)` (line 8017)
- `create_mission_checkbutton(name, variable, dates)` (line 8547)
- `create_comet_checkbutton(name, variable, dates, perihelion)` (line 9003) -- Creates a checkbutton for a comet with a tooltip containing its description,
- `create_interstellar_checkbutton(name, variable, dates, perihelion)` (line 9121) -- Creates a checkbutton for an interstellar/hyperbolic object with a tooltip
- `toggle_special_fetch_mode()` (line 9218) -- DEPRECATED: Special fetch mode removed - two-layer trajectories provide automatic detail
- `create_exoplanet_checkbutton(name, variable, is_star)` (line 9234) -- Create checkbutton for exoplanet objects
- `open_star_visualization()` (line 9255) -- Inform user about standalone Star Visualization executable.
- `launch_galactic_center()` (line 9328) -- Launch the Sagittarius A* Grand Tour visualization.
- `update_center_dropdown()` (line 9486) -- Update the center dropdown to show only Sun + selected centerable objects.
- `setup_center_dropdown_traces()` (line 9547) -- Add traces to all object IntVars to update center dropdown on selection change.
- `on_center_change()` (line 9565) -- Update frame title when the center object is changed.
- `open_orbital_param_visualization()` (line 10003) -- Opens the orbital parameter visualization window by calling the
- `restore_sash_positions()` (line 10175)

---

### palomas_orrery_dashboard.py

**Role:** gui | **Lines:** 587

> Paloma's Orrery Dashboard Central launch point for the Paloma's Orrery suite.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `class PalomasOrreryDashboard` (line 162) -- Main dashboard window.
- `main()` (line 683)

---

### star_visualization_gui.py

**Role:** gui | **Lines:** 1,295

> star_visualization_gui.py - Final version with enhanced pickle file support This GUI reads the enhanced pickle files that contain both raw and calculated data UPDATED: November 28, 2025 - Added PyInstaller frozen executable support When running as exe, plotting modules are called directly instead of via subprocess

**Depends on:** constants_new, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, plot_data_exchange, plot_data_report_widget, report_manager, star_notes
**Consumed by:** (none -- standalone)

**Public functions:**

- `is_frozen()` (line 35) -- Check if running as a PyInstaller frozen executable.
- `class ScrollableFrame` (line 61) -- A scrollable frame widget.
- `class LazyStarPropertiesLoader` (line 82) -- Loads star properties on-demand rather than all at startup.
- `class StarVisualizationSearchWidget` (line 187) -- Search widget with unified display for all star information.
- `class StarVisualizationGUI` (line 789) -- Main GUI window with search and visualization controls.

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

**Role:** rendering | **Lines:** 422

> hr_diagram_apparent_magnitude.py

**Depends on:** data_acquisition, data_processing, incremental_cache_manager, object_type_analyzer, plot_data_exchange, report_manager, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_2d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 52) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, mag_limit)` (line 113) -- Complete star processing pipeline for magnitude-based visualization.
- `main()` (line 194)

---

### hr_diagram_distance.py

**Role:** rendering | **Lines:** 442

> hr_diagram_distance.py - Create HR diagram for stars within specified distance.

**Depends on:** catalog_selection, data_acquisition_distance, data_processing, incremental_cache_manager, object_type_analyzer, plot_data_exchange, report_manager, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_2d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 55) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, max_light_years)` (line 117) -- Complete star processing pipeline for distance-based visualization.
- `main()` (line 197)

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

> Paleoclimate Visualization for Paloma's Orrery Cenozoic temperature and COâ‚‚ reconstruction (66 Ma - present)

**Depends on:** save_utils
**Consumed by:** earth_system_visualization_gui, paleoclimate_dual_scale

**Public functions:**

- `d18o_to_temperature_approx(d18o_values)` (line 58) -- Convert benthic Î´18O to approximate temperature anomaly
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

**Role:** rendering | **Lines:** 391

> planetarium_distance.py

**Depends on:** catalog_selection, data_acquisition, data_processing, incremental_cache_manager, shutdown_handler, simbad_manager, star_properties, stellar_data_patches, stellar_parameters, visualization_3d, visualization_core
**Consumed by:** star_visualization_gui

**Public functions:**

- `ensure_cache_system_ready()` (line 56) -- Minimal cache system initialization using existing modules.
- `process_stars(hip_data, gaia_data, max_light_years)` (line 117) -- Complete star processing pipeline for distance-based 3D visualization.
- `main()` (line 204)

---

### plot_data_report_widget.py

**Role:** rendering | **Lines:** 552

> (no description)

**Depends on:** object_type_analyzer, report_manager
**Consumed by:** star_visualization_gui, star_visualization_gui_before_pyinstaller_refactor

**Public functions:**

- `class PlotDataReportWidget` (line 19) -- Widget for displaying comprehensive plot data report.
- `add_plot_report_to_gui(parent_frame, column, row)` (line 650) -- Add the plot report widget to the star visualization GUI.

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

**Role:** rendering | **Lines:** 513

> visualization_2d.py

**Depends on:** constants_new, save_utils, solar_visualization_shells, star_notes, visualization_core, visualization_utils
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance

**Public functions:**

- `format_value(value, format_spec, default)` (line 20) -- Format a value using Python's built-in format function.
- `create_hover_text(df, include_3d)` (line 30) -- Create hover text with graceful handling of missing columns.
- `prepare_2d_data(combined_data)` (line 120) -- Prepare data for plotting.
- `generate_footer_text(counts_dict, estimation_results, mag_limit, max_light_years)` (line 193) -- Generate updated footer text including estimation information.
- `create_hr_diagram(combined_df, counts_dict, mag_limit, max_light_years)` (line 258) -- Create HR diagram for either magnitude or distance-based data.

---

### visualization_3d.py

**Role:** rendering | **Lines:** 847

> visualization_3d.py

**Depends on:** constants_new, save_utils, solar_visualization_shells, star_notes, visualization_core
**Consumed by:** planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `parse_stellar_classes(df)` (line 24) -- Parse stellar classes from spectral types.
- `expand_object_type(ot)` (line 38) -- Expand object type codes to full descriptions.
- `prepare_3d_data(combined_df, max_value, counts, mode)` (line 61) -- Prepare data for 3D visualization with proper handling of Messier objects.
- `format_value(value, format_spec, default)` (line 172) -- Format a value using Python's built-in format function.
- `create_hover_text(df, include_3d)` (line 194) -- Create hover text with graceful handling of missing columns.
- `create_hover_text_old(df, include_3d)` (line 283) -- Create hover text with graceful handling of missing columns.
- `create_notable_stars_list(combined_df, unique_notes, user_max_coord)` (line 330) -- Create list of notable stars, using vector distance for filtering.
- `create_3d_visualization(combined_df, max_value, user_max_coord)` (line 433) -- Create 3D visualization of stellar neighborhood or magnitude-limited stars.

---

### visualization_core.py

**Role:** rendering | **Lines:** 343

> visualization_core.py

**Depends on:** constants_new, solar_visualization_shells, star_notes, stellar_parameters
**Consumed by:** exoplanet_stellar_properties, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, visualization_2d, visualization_3d

**Public functions:**

- `format_value(value, format_spec, default)` (line 14) -- Format values consistently across visualizations.
- `create_hover_text(df, include_3d)` (line 25) -- Create hover text for plots with identification of estimated values and special cases.
- `prepare_temperature_colors()` (line 150) -- Define consistent temperature color scales.
- `analyze_star_counts(combined_df)` (line 164) -- Analyze star counts and exclusion reasons in detail.
- `analyze_magnitude_distribution(data, mag_limit)` (line 220) -- Analyze and print the distribution of stars by magnitude ranges.
- `analyze_and_report_stars(combined_df, mode, max_value)` (line 282) -- Analyze star data and report statistics for both distance and magnitude-limited samples.
- `generate_star_count_text(counts_dict, combined_df)` (line 376) -- Generate detailed text about star counts from different catalogs.

---

### visualization_utils.py

**Role:** rendering | **Lines:** 713

> visualization_utils.py - Shared utilities for visualization functions.

**Depends on:** celestial_coordinates, formatting_utils, idealized_orbits
**Consumed by:** gallery_studio, palomas_orrery, palomas_orrery_helpers, visualization_2d

**Public functions:**

- `add_hover_toggle_buttons(fig)` (line 9) -- Add hover text toggle buttons to any Plotly figure.
- `add_camera_center_button(fig, center_object_name)` (line 68) -- Add a button to move the camera to the center object.
- `add_look_at_object_buttons(fig, positions, center_object_name, target_objects)` (line 143) -- Add buttons to point camera from center toward specific target objects.
- `add_fly_to_object_buttons(fig, positions, center_object_name, target_objects, fly_distance, distance_scale_factor)` (line 348) -- Add buttons to fly the camera TO specific target objects, keeping focus on the object.
- `format_hover_text(obj_data, name, is_solar_system)` (line 546) -- Format hover text consistently for different types of objects.
- `format_detailed_hover_text(obj_data, obj_name, center_object_name, objects, planetary_params, parent_planets, CENTER_BODY_RADII, KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS)` (line 605) -- Generate detailed hover text for celestial objects with comprehensive information.
- `update_figure_frames(fig, include_hover_toggle)` (line 828) -- Update figure frames to maintain hover text toggle functionality in animations.

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

**Role:** rendering/shells | **Lines:** 1,631

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** palomas_orrery

**Public functions:**

- `calculate_tail_activity_factor(current_distance_au, perihelion_distance_au, max_active_distance_au)` (line 317) -- Calculate how active the comet is based on solar distance.
- `create_comet_nucleus(center_position, nucleus_size_km, comet_name)` (line 353) -- Creates a comet nucleus visualization as a single point.
- `create_maps_disintegration_marker(position_au, comet_name)` (line 398)
- `create_maps_ghost_tail_trace(fig)` (line 485) -- Ghost tail arc for MAPS C/2026 A1, overlaid on the perihelion
- `create_comet_coma(center_position, coma_radius_km, activity_factor, comet_name)` (line 644) -- Creates the coma (atmosphere) around the nucleus.
- `create_comet_dust_tail(center_position, velocity_vector, max_tail_length_mkm, activity_factor, comet_name, num_particles)` (line 731) -- Creates the dust tail (Type II tail).
- `create_comet_ion_tail(center_position, max_tail_length_mkm, activity_factor, comet_name, num_particles)` (line 902) -- Creates the ion tail (Type I tail, plasma tail).
- `create_comet_anti_tail(center_position, anti_tail_length_km, activity_factor, comet_name, anti_tail_color, collimation_ratio, num_particles)` (line 1034) -- Creates anti-tail jet structure pointing TOWARD the Sun.
- `create_complete_comet_visualization(comet_name, center_position, velocity_vector, current_distance_au)` (line 1215) -- Creates a complete comet visualization with nucleus, coma, and both tails.
- `add_comet_tails_to_figure(fig, comet_name, position_data, center_object_name, current_date)` (line 1430) -- Add comet visualization to figure with feature-specific thresholds.

---

### earth_visualization_shells.py

**Role:** rendering/shells | **Lines:** 837

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_earth_inner_core_shell(center_position)` (line 17) -- Creates Earth's inner core shell.
- `create_earth_outer_core_shell(center_position)` (line 73) -- Creates Earth's outer core shell.
- `create_earth_lower_mantle_shell(center_position)` (line 128) -- Creates Earth's lower mantle shell.
- `create_earth_upper_mantle_shell(center_position)` (line 182) -- Creates Earth's upper mantle shell.
- `create_earth_crust_shell(center_position)` (line 236) -- Creates Earth's crust shell using Mesh3d for better performance with improved hover.
- `create_earth_atmosphere_shell(center_position)` (line 393) -- Creates Earth's lower atmosphere shell.
- `create_earth_upper_atmosphere_shell(center_position)` (line 448) -- Creates Earth's upper atmosphere shell.
- `create_earth_magnetosphere_shell(center_position)` (line 520) -- Creates Earth's magnetosphere.
- `create_earth_leo_shell(center_position)` (line 740) -- Creates a representation of Earth's Low Earth Orbit (LEO) shell.
- `create_earth_geostationary_belt_shell(center_position)` (line 838) -- Creates a representation of Earth's geostationary satellite belt at 42,164 km.
- `create_earth_hill_sphere_shell(center_position)` (line 926) -- Creates Earth's Hill sphere.

---

### eris_visualization_shells.py

**Role:** rendering/shells | **Lines:** 400

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_eris_core_shell(center_position)` (line 18) -- Creates Eris's core shell.
- `create_eris_mantle_shell(center_position)` (line 97) -- Creates Eris's mantle shell.
- `create_eris_crust_shell(center_position)` (line 153) -- Creates eris's cloud layer shell.
- `create_eris_atmosphere_shell(center_position)` (line 317) -- Creates eris's atmosphere shell.
- `create_eris_hill_sphere_shell(center_position)` (line 400) -- Creates Eris's Hill sphere shell.

---

### jupiter_visualization_shells.py

**Role:** rendering/shells | **Lines:** 769

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_ring_points_jupiter(inner_radius, outer_radius, n_points, thickness)` (line 7) -- Create points for a ring structure (for planets like Saturn).
- `create_jupiter_core_shell(center_position)` (line 57) -- Creates Jupiter's core shell.
- `create_jupiter_metallic_hydrogen_shell(center_position)` (line 111) -- Creates Jupiter's metallic hydrogen shell.
- `create_jupiter_molecular_hydrogen_shell(center_position)` (line 166) -- Creates Jupiter's molecular hydrogen shell.
- `create_jupiter_cloud_layer_shell(center_position)` (line 224) -- Creates Jupiter's cloud layer shell.
- `create_jupiter_upper_atmosphere_shell(center_position)` (line 385) -- Creates Jupiter's upper atmosphere shell.
- `create_jupiter_magnetosphere(center_position)` (line 440) -- Creates Jupiter's main magnetosphere structure.
- `create_jupiter_io_plasma_torus(center_position)` (line 504) -- Creates Jupiter's Io plasma torus.
- `create_jupiter_radiation_belts(center_position)` (line 587) -- Creates Jupiter's radiation belts.
- `create_jupiter_hill_sphere_shell(center_position)` (line 681) -- Creates Jupiter's Hill sphere shell.
- `create_jupiter_ring_system(center_position)` (line 763) -- Creates a visualization of Jupiter's ring system.

---

### mars_visualization_shells.py

**Role:** rendering/shells | **Lines:** 701

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_mars_inner_core_shell(center_position)` (line 14) -- Creates Mars's inner core shell.
- `create_mars_outer_core_shell(center_position)` (line 92) -- Creates Mars's outer core shell.
- `create_mars_mantle_shell(center_position)` (line 161) -- Creates Mars's mantle shell.
- `create_mars_crust_shell(center_position)` (line 216) -- Creates Mars's crust shell using Mesh3d for better performance with improved hover.
- `create_mars_atmosphere_shell(center_position)` (line 374) -- Creates Mars's lower atmosphere shell.
- `create_mars_upper_atmosphere_shell(center_position)` (line 442) -- Creates Mars's upper atmosphere shell.
- `create_mars_magnetosphere_shell(center_position)` (line 515) -- Creates Mars' induced magnetosphere and localized crustal magnetic fields.
- `create_mars_hill_sphere_shell(center_position)` (line 737) -- Creates Mars's Hill sphere.

---

### mercury_visualization_shells.py

**Role:** rendering/shells | **Lines:** 641

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_mercury_inner_core_shell(center_position)` (line 16) -- Creates Mercury's inner core shell.
- `create_mercury_outer_core_shell(center_position)` (line 67) -- Creates Mercury's outer core shell.
- `create_mercury_mantle_shell(center_position)` (line 118) -- Creates Mercury's mantle shell.
- `create_mercury_crust_shell(center_position)` (line 171) -- Creates Mercury's crust shell using Mesh3d for better performance with improved hover.
- `create_mercury_atmosphere_shell(center_position)` (line 327) -- Creates Mercury's atmosphere shell.
- `create_mercury_sodium_tail(center_position)` (line 405) -- Creates Mercury's sodium tail visualization extending away from the Sun.
- `create_mercury_magnetosphere_shell(center_position)` (line 521) -- Creates Mercury's magnetosphere.
- `create_mercury_hill_sphere_shell(center_position)` (line 693) -- Creates Mercury's Hill sphere.

---

### moon_visualization_shells.py

**Role:** rendering/shells | **Lines:** 434

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_moon_inner_core_shell(center_position)` (line 14) -- Creates the Moon's inner core shell.
- `create_moon_outer_core_shell(center_position)` (line 66) -- Creates the Moon's outer core shell.
- `create_moon_mantle_shell(center_position)` (line 128) -- Creates the Moon's lower mantle shell.
- `create_moon_crust_shell(center_position)` (line 202) -- Creates Earth's crust shell using Mesh3d for better performance with improved hover.
- `create_moon_exosphere_shell(center_position)` (line 385) -- Creates the Moon's exosphere shell.
- `create_moon_hill_sphere_shell(center_position)` (line 448) -- Creates the Moon's Hill sphere.

---

### neptune_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,504

> (no description)

**Depends on:** planet_visualization_utilities, saturn_visualization_shells, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_neptune_core_shell(center_position)` (line 17) -- Creates Neptune's core shell.
- `create_neptune_mantle_shell(center_position)` (line 74) -- Creates Neptune's mantle shell.
- `create_neptune_cloud_layer_shell(center_position)` (line 145) -- Creates neptune's cloud layer shell.
- `create_neptune_upper_atmosphere_shell(center_position)` (line 314) -- Creates Neptune's upper atmosphere shell.
- `create_neptune_magnetosphere(center_position)` (line 402) -- Creates Neptune's main magnetosphere structure with proper tilt and offset.
- `create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth)` (line 558) -- Creates a simplified visualization of Neptune's magnetic poles and axis.
- `create_neptune_field_lines(mag_center_x, mag_center_y, mag_center_z, north_x, north_y, north_z, south_x, south_y, south_z, neptune_radius, tilt, azimuth)` (line 692) -- Creates a simple visualization of Neptune's magnetic field lines.
- `create_neptune_radiation_belts(center_position)` (line 789) -- Creates Neptune's radiation belts with proper structure reflecting the complex magnetospheric environment.
- `create_field_aligned_currents(mag_center_x, mag_center_y, mag_center_z, tilt, azimuth)` (line 1015) -- Creates visualization of field-aligned currents in Neptune's magnetosphere.
- `create_neptune_ring_system(center_position)` (line 1157) -- Creates a visualization of Neptune's ring system with proper alignment.
- `create_neptune_hill_sphere_shell(center_position)` (line 1655) -- Creates neptune's Hill sphere shell.

---

### planet9_visualization_shells.py

**Role:** rendering/shells | **Lines:** 235

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_planet9_surface_shell(center_position)` (line 18) -- Creates eris's cloud layer shell.
- `create_planet9_hill_sphere_shell(center_position)` (line 193) -- Creates Planet 9's Hill sphere shell.

---

### pluto_visualization_shells.py

**Role:** rendering/shells | **Lines:** 476

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_pluto_core_shell(center_position)` (line 16) -- Creates pluto's core shell.
- `create_pluto_mantle_shell(center_position)` (line 85) -- Creates pluto's mantle shell.
- `create_pluto_crust_shell(center_position)` (line 149) -- Creates pluto's cloud layer shell.
- `create_pluto_haze_layer_shell(center_position)` (line 320) -- Creates pluto's haze layer shell.
- `create_pluto_atmosphere_shell(center_position)` (line 402) -- Creates pluto's atmosphere shell.
- `create_pluto_hill_sphere_shell(center_position)` (line 484) -- Creates pluto's Hill sphere shell.

---

### saturn_visualization_shells.py

**Role:** rendering/shells | **Lines:** 994

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** neptune_visualization_shells, planet_visualization, uranus_visualization_shells

**Public functions:**

- `create_ring_points_saturn(inner_radius, outer_radius, n_points, thickness)` (line 7) -- Create points for a ring with inner and outer radius.
- `create_saturn_core_shell(center_position)` (line 50) -- Creates saturn's core shell.
- `create_saturn_metallic_hydrogen_shell(center_position)` (line 120) -- Creates Saturn's liquid metallic hydrogen shell.
- `create_saturn_molecular_hydrogen_shell(center_position)` (line 181) -- Creates Saturn's molecular hydrogen shell.
- `create_saturn_cloud_layer_shell(center_position)` (line 245) -- Creates Saturn's cloud layer shell.
- `create_saturn_upper_atmosphere_shell(center_position)` (line 453) -- Creates Saturn's upper atmosphere shell.
- `create_saturn_magnetosphere(center_position)` (line 555) -- Creates Saturn's main magnetosphere structure.
- `create_saturn_enceladus_plasma_torus(center_position)` (line 620) -- Creates Saturn's Enceladus plasma torus.
- `create_saturn_radiation_belts(center_position)` (line 726) -- Creates Saturn's radiation belts.
- `create_saturn_hill_sphere_shell(center_position)` (line 864) -- Creates Saturn's Hill sphere shell.
- `create_saturn_ring_system(center_position)` (line 943) -- Creates a visualization of Saturn's ring system.

---

### solar_visualization_shells.py

**Role:** rendering/shells | **Lines:** 1,425

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** palomas_orrery, palomas_orrery_helpers, planet_visualization, visualization_2d, visualization_3d, visualization_core

**Public functions:**

- `create_sun_hover_text()` (line 853)
- `create_corona_sphere(radius, n_points)` (line 890) -- Create points for a sphere surface to represent corona layers.
- `create_sun_gravitational_shell()` (line 926) -- Creates the Sun's gravitational influence shell.
- `create_sun_outer_oort_shell()` (line 953) -- Creates the Sun's outer Oort cloud shell.
- `create_sun_inner_oort_shell()` (line 980) -- Creates the Sun's inner Oort cloud shell.
- `create_sun_inner_oort_limit_shell()` (line 1007) -- Creates the inner limit of the Sun's Oort cloud shell.
- `create_sun_heliopause_shell()` (line 1034) -- Creates the Sun's heliopause shell.
- `create_sun_termination_shock_shell()` (line 1061) -- Creates the Sun's termination shock shell.
- `create_sun_outer_corona_shell()` (line 1088) -- Creates the Sun's extended outer corona (F-corona) shell.
- `create_sun_inner_corona_shell()` (line 1115) -- Creates the Sun's inner corona (K-corona) shell.
- `create_sun_streamer_belt_shell()` (line 1142) -- Visible white-light corona / helmet streamer belt: ~4-6 solar radii.
- `create_sun_roche_limit_shell()` (line 1173) -- Fluid Roche limit for cometary bodies: ~3.45 solar radii (~0.016 AU).
- `create_sun_alfven_surface_shell()` (line 1207) -- Alfven surface: the true outer boundary of the solar corona (~18.8 solar radii,
- `create_sun_chromosphere_shell()` (line 1240) -- Creates the Sun's chromosphere shell.
- `create_sun_photosphere_shell()` (line 1267) -- Creates the Sun's photosphere shell (the visible solar surface).
- `create_sun_radiative_shell()` (line 1294) -- Creates the Sun's radiative zone shell.
- `create_sun_core_shell()` (line 1321) -- Creates the Sun's core shell.
- `create_sun_hills_cloud_torus(inner_radius, outer_radius, thickness_ratio)` (line 1359) -- Create a toroidal (doughnut-shaped) Hills Cloud structure.
- `create_sun_outer_oort_clumpy(radius_min, radius_max, n_clumps)` (line 1420) -- Create a clumpy, asymmetric outer Oort Cloud with density variations.
- `create_sun_galactic_tide(radius, n_points)` (line 1488) -- Create Oort Cloud structure influenced by galactic tidal forces.
- `create_enhanced_oort_cloud_visualization()` (line 1537) -- Create a more scientifically accurate Oort Cloud visualization.
- `create_oort_cloud_density_visualization()` (line 1605) -- Alternative approach: Show Oort Cloud as density gradients rather than discrete shells.

---

### uranus_visualization_shells.py

**Role:** rendering/shells | **Lines:** 979

> (no description)

**Depends on:** planet_visualization_utilities, saturn_visualization_shells, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_uranus_core_shell(center_position)` (line 18) -- Creates Uranus's core shell.
- `create_uranus_mantle_shell(center_position)` (line 73) -- Creates Uranus's matel shell.
- `create_uranus_cloud_layer_shell(center_position)` (line 137) -- Creates Uranus's cloud layer shell.
- `create_uranus_upper_atmosphere_shell(center_position)` (line 319) -- Creates Uranus's upper atmosphere shell.
- `create_uranus_magnetosphere(center_position)` (line 402) -- Creates Uranus's main magnetosphere structure.
- `create_uranus_radiation_belts(center_position)` (line 493) -- Creates Uranus's radiation belts.
- `create_uranus_ring_system(center_position)` (line 699) -- Creates a visualization of Saturn's ring system.
- `create_uranus_hill_sphere_shell(center_position)` (line 1051) -- Creates Uranus's Hill sphere shell.

---

### venus_visualization_shells.py

**Role:** rendering/shells | **Lines:** 610

> (no description)

**Depends on:** planet_visualization_utilities, shared_utilities
**Consumed by:** planet_visualization

**Public functions:**

- `create_venus_core_shell(center_position)` (line 16) -- Creates Venus's core shell.
- `create_venus_mantle_shell(center_position)` (line 69) -- Creates Venus's mantle shell.
- `create_venus_crust_shell(center_position)` (line 122) -- Creates Venus's crust shell using Mesh3d for better performance with improved hover.
- `create_venus_atmosphere_shell(center_position)` (line 281) -- Creates Venus's lower atmosphere shell.
- `create_venus_upper_atmosphere_shell(center_position)` (line 340) -- Creates Venus's upper atmosphere shell.
- `create_venus_magnetosphere_shell(center_position)` (line 440) -- Creates Venus's magnetosphere.
- `create_venus_hill_sphere_shell(center_position)` (line 643) -- Creates Venus's Hill sphere.

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

**Role:** computation | **Lines:** 83

> (no description)

**Depends on:** data_processing
**Consumed by:** data_acquisition_distance, hr_diagram_distance, planetarium_distance

**Public functions:**

- `select_stars(hip_data, gaia_data, mode, limit_value)` (line 5) -- Unified star selection function applying consistent catalog separation logic.

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

**Role:** computation | **Lines:** 422

> data_processing.py

**Depends on:** (none)
**Consumed by:** catalog_selection, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `convert_icrs_to_radec_strings(data)` (line 11) -- Convert ICRS coordinates (decimal degrees) to formatted RA/Dec strings.
- `estimate_vmag_from_gaia(gaia_data)` (line 81) -- Estimate V magnitude from Gaia G magnitude and BP-RP color.
- `calculate_distances(data)` (line 97) -- Calculate distances in parsecs and light-years
- `align_coordinate_systems(hip_data)` (line 111) -- Ensure RA and Dec columns are consistent and in degrees.
- `generate_unique_ids(stars, catalog)` (line 129) -- Generate unique IDs for stars based on their catalog.
- `select_stars_by_magnitude(hip_data, gaia_data, mag_limit)` (line 157) -- Select stars based on a clean separation:
- `analyze_additional_stars(new_data, old_data)` (line 227) -- Analyze properties of stars present in new data but not in old
- `examine_outliers(data)` (line 255) -- Print details of potential outlier stars
- `print_star_details(star)` (line 274) -- Print relevant details for a single star
- `select_stars_by_distance(hip_data, gaia_data, max_light_years)` (line 285) -- Select stars based on distance criteria while maintaining clean catalog separation:
- `calculate_distances(data)` (line 379) -- Calculate distances in parsecs and light-years from parallax.
- `calculate_cartesian_coordinates(data)` (line 394) -- Calculate x, y, z coordinates from RA, Dec, and distance.
- `validate_coordinates(data)` (line 465) -- Validate calculated coordinates and report any issues.
- `filter_by_mag_limit(combined_data, mag_limit)` (line 487) -- Filter the combined data to include only stars within the specified mag_limit.
- `update_counts(filtered_data, mag_limit)` (line 493) -- Update counts of stars in each category based on the filtered data.

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

**Role:** computation | **Lines:** 6,149

> idealized_orbits.py

**Depends on:** apsidal_markers, constants_new, orbital_elements, osculating_cache_manager
**Consumed by:** create_ephemeris_database, orbital_param_viz, orrery_integration, palomas_orrery, palomas_orrery_helpers, visualization_utils

**Public functions:**

- `get_planet_perturbation_note(obj_name, orbit_source)` (line 82) -- Get appropriate perturbation note for planet's Keplerian orbit hover text.
- `get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params)` (line 180) -- Compare osculating vs mean orbital elements and return perturbation assessment HTML.
- `add_mean_orbit_trace(fig, obj_name, mean_params, color_func)` (line 254) -- Add a mean orbit trace from orbital_elements.py (JPL epoch solution).
- `calculate_mars_satellite_elements(date, satellite_name)` (line 360) -- Calculate time-varying orbital elements for Mars satellites
- `calculate_jupiter_satellite_elements(date, satellite_name)` (line 418) -- Calculate time-varying orbital elements for Jupiter satellites.
- `calculate_saturn_satellite_elements(date, satellite_name)` (line 475) -- Calculate time-varying orbital elements for Saturn satellites.
- `test_mars_rotations(satellite_name, planetary_params, color, fig)` (line 525) -- Test multiple rotation combinations to find the best alignment
- `test_uranus_equatorial_transformations(satellite_name, planetary_params, color, fig)` (line 627) -- Test transformations assuming orbital elements are in Uranus's equatorial plane
- `test_uranus_rotation_combinations(satellite_name, planetary_params, color, fig)` (line 725) -- Test multiple rotation combinations for Uranus satellites systematically
- `debug_planet_transformation(planet_name)` (line 835) -- Print detailed information about the transformation for a specific planet
- `debug_mars_moons(satellites_data, parent_planets)` (line 909) -- Special debug function for Mars and its moons
- `compare_transformation_methods(fig, satellites_data, parent_planets)` (line 955) -- Plot orbits with different transformation methods for comparison
- `test_mars_negative_tilt(fig, satellites_data)` (line 988) -- Test hypothesis that Mars needs a negative tilt application
- `debug_satellite_systems()` (line 1040)
- `rotate_points(x, y, z, angle, axis)` (line 1066) -- Rotates points (x,y,z) about the given axis by 'angle' radians.
- `plot_jupiter_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1112) -- Plot osculating orbit for Jupiter satellites.
- `plot_saturn_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1275) -- Plot osculating orbit for Saturn satellites.
- `plot_uranus_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1421) -- Plot osculating orbit for Uranus satellites.
- `plot_neptune_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)` (line 1524) -- Plot osculating orbit for Neptune satellites.
- `plot_pluto_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 1657) -- Plot osculating orbit for objects in Pluto binary system.
- `plot_tno_satellite_orbit(fig, satellite_name, parent_name, date, color, show_apsidal_markers)` (line 1970) -- Plot osculating orbit for TNO (Trans-Neptunian Object) satellites.
- `add_pluto_barycenter_marker(fig, date, charon_position)` (line 2364) -- Add the Pluto-Charon barycenter marker to Pluto-centered view.
- `plot_orcus_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2432) -- Plot osculating orbit for objects in the Orcus-Vanth binary system.
- `add_orcus_barycenter_marker(fig, date, vanth_position)` (line 2657) -- Add the Orcus-Vanth barycenter marker to Orcus-centered view.
- `plot_gonggong_xiangliu_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2725) -- Plot analytical orbit for Xiangliu around Gonggong.
- `plot_patroclus_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 2914) -- Plot analytical orbit for objects in the Patroclus-Menoetius binary Trojan system.
- `create_planet_transformation_matrix(planet_name)` (line 3164) -- Create a transformation matrix for a planet based on its pole direction.
- `plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig, date, days_to_plot, current_position, show_apsidal_markers)` (line 3219) -- Plot the Keplerian orbit of a satellite around its parent planet.
- `calculate_moon_orbital_elements(date)` (line 3790) -- Calculate Moon's orbital elements for a specific date
- `plot_mars_moon_osculating_orbit(fig, satellite_name, horizons_id, date, color, parent_planet)` (line 3858) -- Plot osculating orbit for Mars satellites (Phobos/Deimos)
- `plot_moon_ideal_orbit(fig, date, center_object_name, color, days_to_plot, current_position, show_apsidal_markers, planetary_params)` (line 3980) -- Plot BOTH the Moon's analytical and osculating orbits for educational comparison.
- `plot_earth_moon_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers, center_id)` (line 4215) -- Plot osculating orbit for objects in the Earth-Moon binary system.
- `add_earth_moon_barycenter_marker(fig, date, moon_position)` (line 4453) -- Add the Earth-Moon barycenter marker to Earth-centered view.
- `generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points, max_distance)` (line 4526) -- Generate points for a hyperbolic orbit trajectory.
- `plot_idealized_orbits(fig, objects_to_plot, center_id, objects, planetary_params, parent_planets, color_map, date, days_to_plot, current_positions, fetch_position, show_apsidal_markers, parent_window)` (line 4624) -- Plot Keplerian orbits for planets, dwarf planets, asteroids, KBOs, and moons.
- `test_triton_rotations(satellite_name, planetary_params, color, fig)` (line 5996) -- Test multiple rotation combinations for Triton's orbit
- `test_pluto_moon_rotations(satellite_name, planetary_params, color, fig)` (line 6138) -- Fine-tuned testing of XYZ rotation combinations for Pluto's moons.
- `very_fine_pluto_rotations(satellite_name, planetary_params, color, fig, x_range, y_range, z_range, step)` (line 6376) -- Extremely fine-grained testing of XYZ rotation combinations for Pluto's moons.
- `pluto_system_final_transform(satellite_name, planetary_params, color, fig, transform)` (line 6511) -- Apply a specific optimal transformation to Pluto's moons' orbits.
- `calculate_phoebe_correction_from_normals()` (line 6626) -- Calculate the optimal rotation to align Keplerian orbit with actual orbit
- `plot_hyperbolic_osculating_orbit(fig, obj_name, obj_info, center_id, color_map, date, show_apsidal_markers, parent_window, approach)` (line 6663) -- Plot a geocentric (or planet-centric) osculating hyperbolic orbit for a
- `plot_perihelion_osculating_orbit(fig, obj_name, obj_info, color_map, date, show_apsidal_markers, parent_window)` (line 6925) -- Plot Sun-centered osculating orbit arc at perihelion epoch for comets.

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

**Role:** data | **Lines:** 2,392

> Constants Module

**Depends on:** (none)
**Consumed by:** apsidal_markers, exoplanet_stellar_properties, gallery_studio, idealized_orbits, object_type_analyzer, orbital_param_viz, palomas_orrery, palomas_orrery_helpers, planet_visualization, planet_visualization_utilities, star_visualization_gui, star_visualization_gui_before_pyinstaller_refactor, stellar_parameters, visualization_2d, visualization_3d, visualization_core

**Public functions:**

- `color_map(planet)` (line 461)

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

**Role:** data | **Lines:** 396

> messier_catalog.py

**Depends on:** (none)
**Consumed by:** messier_object_data_handler, simbad_manager, star_properties

**Public functions:**

- `get_all_bright_objects()` (line 275) -- Combine all catalogs of bright galactic objects.
- `get_objects_brighter_than(magnitude)` (line 289) -- Return all objects brighter than the specified magnitude.
- `get_objects_by_type(obj_type)` (line 306) -- Return all objects of a specific type.
- `get_nebulae()` (line 323) -- Return all nebulae from both Messier and bright object catalogs.
- `get_star_clusters()` (line 335) -- Return all star clusters from both catalogs.
- `get_visible_objects(mag_limit)` (line 342) -- Return all objects brighter than the given magnitude.
- `get_object_info(obj_id)` (line 360) -- Get detailed information about a specific object.
- `get_catalog_statistics()` (line 375) -- Return statistics about all catalogs.

---

### sgr_a_star_data.py

**Role:** data | **Lines:** 555

> sgr_a_star_data.py Data module for the Galactic Center S-Stars visualization. Contains orbital elements and physical constants.

**Depends on:** exoplanet_stellar_properties, stellar_parameters
**Consumed by:** sgr_a_grand_tour, sgr_a_visualization_animation, sgr_a_visualization_core, sgr_a_visualization_precession

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

**Role:** data | **Lines:** 1,129

> Define unique_notes dictionary

**Depends on:** (none)
**Consumed by:** messier_object_data_handler, star_visualization_gui, star_visualization_gui_before_pyinstaller_refactor, visualization_2d, visualization_3d, visualization_core

---

### star_properties.py

**Role:** data | **Lines:** 328

> (no description)

**Depends on:** messier_catalog, simbad_manager
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `get_column_value_safe(result_table, old_name, new_name)` (line 10) -- Get column value from either old (uppercase) or new (lowercase) format.
- `create_custom_simbad()` (line 28) -- Create SIMBAD instance with proper field configuration for both old and new API.
- `parse_magnitude(value)` (line 41)
- `load_existing_properties(properties_file)` (line 55) -- Load existing star and Messier object properties from a file.
- `generate_unique_ids(combined_data)` (line 109) -- Generate unique identifiers for all stars consistently.
- `save_properties_to_file(properties, properties_file)` (line 146) -- Save star properties to file with Messier object support.
- `create_custom_simbad()` (line 175)
- `query_simbad_for_star_properties(missing_ids, existing_properties, properties_file)` (line 187) -- Query Simbad for missing star properties with backward compatibility.
- `assign_properties_to_data(combined_data, existing_properties, unique_ids)` (line 344) -- Assign retrieved properties to the combined data with Messier object support.

---

### stellar_data_patches.py

**Role:** data | **Lines:** 34

> stellar_data_patches.py

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `apply_temperature_patches(data)` (line 11) -- Apply known fixes for stars with missing or incorrect data.

---

### stellar_parameters.py

**Role:** data | **Lines:** 340

> stellar_parameters.py

**Depends on:** constants_new, stellar_parameters
**Consumed by:** exoplanet_stellar_properties, hr_diagram_apparent_magnitude, hr_diagram_distance, planetarium_apparent_magnitude, planetarium_distance, sgr_a_star_data, stellar_parameters, visualization_core

**Public functions:**

- `estimate_temperature_from_spectral_type(sp_type)` (line 7) -- Estimate effective temperature from spectral type.
- `calculate_bv_temperature(B_V)` (line 50) -- Calculate temperature from B-V color index using Ballesteros' formula.
- `select_best_temperature(T_eff_BV, T_eff_sptype)` (line 74) -- Select the best temperature estimate based on various criteria.
- `debug_orionis_stars(data, stage)` (line 112) -- Debug function to compare Epsilon and Zeta Orionis data through processing stages.
- `calculate_stellar_parameters(combined_data)` (line 208) -- Calculate stellar parameters with parallel debugging of both Orionis stars.

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

**Role:** cache | **Lines:** 2

> (no description)

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
**Consumed by:** osculating_cache_manager, palomas_orrery, palomas_orrery_helpers

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

### json_converter.py

**Role:** pipeline | **Lines:** 622

> Gallery JSON Converter - Extract Plotly figures from HTML and save as JSON.

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `extract_plotly_json_from_html(html_path)` (line 136) -- Extract Plotly figure JSON from an HTML file.
- `save_figure_json(fig, name, output_folder, category, description, auto_metadata, mode)` (line 377) -- Save a Plotly figure object directly as gallery-ready JSON.
- `convert_html_to_gallery_json(html_path, output_folder, category, description, mode)` (line 431) -- Convert a single HTML visualization to gallery-ready JSON.
- `run_interactive()` (line 591) -- Run the interactive converter with file selection dialog.
- `convert_folder(input_folder, output_folder, category)` (line 714) -- Convert all HTML files in a folder to gallery JSON.

---

### plot_data_exchange.py

**Role:** pipeline | **Lines:** 160

> (no description)

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, star_visualization_gui, star_visualization_gui_before_pyinstaller_refactor

**Public functions:**

- `class PlotDataExchange` (line 8) -- Exchange plot data between subprocess scripts and GUI.

---

### save_utils.py

**Role:** pipeline | **Lines:** 388

> Consolidated utility functions for saving Plotly visualizations.

**Depends on:** (none)
**Consumed by:** earth_system_visualization_gui, energy_imbalance, paleoclimate_dual_scale, paleoclimate_human_origins_full, paleoclimate_visualization, paleoclimate_visualization_full, paleoclimate_wet_bulb_full, palomas_orrery, palomas_orrery_helpers, sgr_a_grand_tour, sgr_a_visualization_animation, sgr_a_visualization_core, sgr_a_visualization_precession, shutdown_handler, social_media_export, visualization_2d, visualization_3d

**Public functions:**

- `save_visualization(fig, default_name, mode, output_path, offline, auto_play, open_browser)` (line 109) -- Unified save function for all Plotly visualizations.
- `show_and_save(fig, default_name, auto_play)` (line 351) -- Show visualization in browser, then offer save dialog.
- `save_plot(fig, default_name)` (line 415) -- Legacy function for backward compatibility.
- `handle_save(fig, default_name)` (line 433) -- Legacy function for backward compatibility.
- `show_animation_safely(fig, default_name)` (line 446) -- Show and optionally save an animation.
- `save_html(fig, filename, offline, open_browser)` (line 467) -- Simple direct save for scripts that don't need dialogs.

---

### social_media_export.py

**Role:** pipeline | **Lines:** 968

> Generates a second HTML file from an existing Plotly figure, optimized for screen recording Instagram Reels and YouTube Shorts (9:16 portrait).

**Depends on:** save_utils
**Consumed by:** palomas_orrery

**Public functions:**

- `get_trace_names(fig)` (line 802) -- Get a list of trace names from a Plotly figure.
- `show_trace_selection_dialog(fig, parent)` (line 826) -- Show a dialog with checkboxes for each trace in the figure.
- `export_social_html(fig, output_path, open_browser, plotly_js, trace_names)` (line 1055) -- Export a Plotly figure as a social-media-optimized HTML file.

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

### orrery_integration.py

**Role:** utility | **Lines:** 315

> Integration code for using refined orbits in palomas_orrery.py

**Depends on:** idealized_orbits
**Consumed by:** (none -- standalone)

**Public functions:**

- `class OrreryConfiguration` (line 29) -- Configuration for orbit selection and display options.
- `get_orbit_function(object_name, primary)` (line 54) -- Get the appropriate orbit function for an object.
- `create_orrery_objects(config)` (line 113) -- Create orrery objects with appropriate orbit functions.
- `plot_objects_enhanced(objects, t, ax, show_orbits, show_comparison)` (line 140) -- Enhanced version of plot_objects that can show orbit comparisons.
- `animate_objects_enhanced(objects, duration, fps, show_comparison)` (line 196) -- Enhanced animation function that supports orbit comparisons.
- `plot_palomas_orrery(date_time, show_orbits, use_refined)` (line 264) -- Main plotting function that integrates with palomas_orrery.py
- `validate_orbit_accuracy()` (line 340) -- Compare refined vs idealized orbits for all available objects.

---

### palomas_orrery_helpers.py

**Role:** utility | **Lines:** 765

> Paloma's Orrery - Solar System Visualization Tool

**Depends on:** constants_new, formatting_utils, idealized_orbits, orbit_data_manager, planet_visualization, save_utils, shared_utilities, shutdown_handler, solar_visualization_shells, visualization_utils
**Consumed by:** orbital_param_viz, palomas_orrery

**Public functions:**

- `calculate_planet9_position_on_orbit(a, e, i, omega, Omega, theta)` (line 205) -- Calculate position that lies exactly on the orbit defined by the parameters
- `rotate_points2(x, y, z, angle, axis)` (line 253) -- Rotates points (x,y,z) about the given axis by 'angle' radians.
- `calculate_axis_range(objects_to_plot)` (line 301) -- Calculate appropriate axis range based on outermost planet
- `fetch_trajectory(object_id, dates_list, center_id, id_type, start_date, end_date)` (line 318) -- Fetch trajectory data in batch for all dates, handling missing epochs through interpolation.
- `fetch_orbit_path(obj_info, start_date, end_date, interval, center_id, id_type)` (line 544) -- Fetch orbit path data from JPL Horizons for the given object between start_date and end_date,
- `pad_trajectory(global_dates, object_start_date, object_end_date, object_id, center_id, id_type)` (line 594) -- Fetch trajectory and pad with None before start_date and after end_date.
- `add_url_buttons(fig, objects_to_plot, selected_objects)` (line 629) -- Add URL buttons for missions and objects in solar system visualizations.
- `get_default_camera()` (line 739) -- Return the default orthographic camera settings for top-down view
- `print_planet_positions(positions)` (line 751) -- Print positions and distances for planets.
- `create_orbit_backup()` (line 781) -- Create a backup of orbit cache on startup
- `cleanup_old_orbits()` (line 814) -- Remove orbit data older than 30 days
- `show_animation_safely(fig, default_name)` (line 886) -- Show and optionally save an animation.

---

### report_manager.py

**Role:** utility | **Lines:** 124

> Scientific Report Manager for Astronomical Data Analysis Manages generation, storage, and retrieval of analysis reports.

**Depends on:** (none)
**Consumed by:** hr_diagram_apparent_magnitude, hr_diagram_distance, plot_data_report_widget, star_visualization_gui, star_visualization_gui_before_pyinstaller_refactor

**Public functions:**

- `class ReportManager` (line 13) -- Manages scientific reports for astronomical data analysis.

---

### shared_utilities.py

**Role:** utility | **Lines:** 119

> shared_utilities.py - Common utility functions shared between multiple modules

**Depends on:** (none)
**Consumed by:** asteroid_belt_visualization_shells, comet_visualization_shells, earth_visualization_shells, eris_visualization_shells, jupiter_visualization_shells, mars_visualization_shells, mercury_visualization_shells, moon_visualization_shells, neptune_visualization_shells, palomas_orrery, palomas_orrery_helpers, planet9_visualization_shells, pluto_visualization_shells, saturn_visualization_shells, solar_visualization_shells, uranus_visualization_shells, venus_visualization_shells

**Public functions:**

- `create_sun_direction_indicator(center_position, axis_range, shell_radius, object_type, center_object)` (line 9) -- Creates a visual indicator showing the direction to the Sun (along negative X-axis).

---

### shutdown_handler.py

**Role:** utility | **Lines:** 66

> shutdown_handler.py

**Depends on:** save_utils
**Consumed by:** orbital_param_viz, palomas_orrery, palomas_orrery_helpers, planetarium_apparent_magnitude, planetarium_distance

**Public functions:**

- `class PlotlyShutdownHandler` (line 15) -- Handles graceful shutdown for Plotly visualizations and associated threads.
- `create_monitored_thread(handler, target_func)` (line 57) -- Create a thread that's monitored by the shutdown handler.
- `show_figure_safely(fig, default_name)` (line 69) -- Show and optionally save a Plotly figure with proper cleanup.

---

## DEVTOOL: Developer tools (dependency tracing, atlas)

### dep_trace.py

**Role:** devtool | **Lines:** 326

> dep_trace.py - Targeted dependency path tracer for Paloma's Orrery Usage: python dep_trace.py <module_name> [hops]

**Depends on:** (none)
**Consumed by:** (none -- standalone)

**Public functions:**

- `get_imports(filepath)` (line 72) -- Extract local module imports from a Python file using AST.
- `build_graph(project_dir)` (line 90) -- Build full bidirectional dependency graph for all local modules.
- `find_neighborhood(target, deps, consumers, hops)` (line 114) -- Walk outward from target by `hops` steps in both directions.
- `get_category(mod)` (line 154)
- `print_report(target, nodes, edges, hubs, deps, consumers)` (line 163)
- `to_mermaid(target, nodes, edges, hubs)` (line 194)
- `to_html(target, nodes, edges, hubs, deps, consumers)` (line 216) -- Generate a self-contained interactive HTML graph using vis-network.
- `main()` (line 342)

---

## LEGACY: Archived / superseded modules

### star_visualization_gui_before_pyinstaller_refactor.py

**Role:** legacy | **Lines:** 1,162

> star_visualization_gui.py - Final version with enhanced pickle file support This GUI reads the enhanced pickle files that contain both raw and calculated data

**Depends on:** constants_new, plot_data_exchange, plot_data_report_widget, report_manager, star_notes
**Consumed by:** (none -- standalone)

**Public functions:**

- `class ScrollableFrame` (line 26) -- A scrollable frame widget.
- `class LazyStarPropertiesLoader` (line 47) -- Loads star properties on-demand rather than all at startup.
- `class StarVisualizationSearchWidget` (line 152) -- Search widget with unified display for all star information.
- `class StarVisualizationGUI` (line 762) -- Main GUI window with search and visualization controls.

---

## OTHER: Uncategorized

### messier_object_data_handler.py

**Role:** other | **Lines:** 321

> messier_object_data_handler.py

**Depends on:** messier_catalog, star_notes
**Consumed by:** planetarium_apparent_magnitude

**Public functions:**

- `class MessierObjectHandler` (line 18) -- Handles all Messier object related operations.

---

## Alphabetical Index

| Module | Role | Lines | Deps | Consumers |
|--------|------|------:|-----:|----------:|
| apsidal_markers | computation | 1,681 | 1 | 4 |
| asteroid_belt_visualization_shells | rendering/shells | 410 | 1 | 2 |
| catalog_selection | computation | 83 | 1 | 3 |
| celestial_coordinates | computation | 454 | 0 | 1 |
| celestial_objects | data | 1,225 | 0 | 1 |
| climate_cache_manager | cache | 161 | 1 | 1 |
| close_approach_data | data | 519 | 1 | 1 |
| comet_visualization_shells | rendering/shells | 1,631 | 2 | 1 |
| constants_new | data | 2,392 | 0 | 16 |
| convert_hot_ph_to_json | pipeline | 197 | 0 | 0 |
| coordinate_system_guide | computation | 547 | 0 | 0 |
| create_cache_backups | cache | 2 | 1 | 0 |
| create_ephemeris_database | cache | 243 | 1 | 0 |
| data_acquisition | computation | 220 | 0 | 4 |
| data_acquisition_distance | computation | 169 | 2 | 1 |
| data_processing | computation | 422 | 0 | 5 |
| dep_trace | devtool | 326 | 0 | 0 |
| earth_system_controller | gui | 74 | 0 | 0 |
| earth_system_generator | computation | 688 | 3 | 1 |
| earth_system_visualization_gui | gui | 1,807 | 8 | 1 |
| earth_visualization_shells | rendering/shells | 837 | 2 | 1 |
| energy_imbalance | computation | 839 | 1 | 1 |
| eris_visualization_shells | rendering/shells | 400 | 2 | 1 |
| exoplanet_coordinates | data | 399 | 1 | 0 |
| exoplanet_orbits | rendering | 613 | 3 | 1 |
| exoplanet_stellar_properties | data | 485 | 3 | 3 |
| exoplanet_systems | data | 570 | 0 | 3 |
| fetch_climate_data | computation | 761 | 0 | 1 |
| fetch_paleoclimate_data | computation | 169 | 0 | 0 |
| formatting_utils | utility | 16 | 0 | 4 |
| gallery_editor | gui | 1,293 | 0 | 0 |
| gallery_studio | gui | 4,815 | 2 | 0 |
| hr_diagram_apparent_magnitude | rendering | 422 | 12 | 1 |
| hr_diagram_distance | rendering | 442 | 13 | 1 |
| idealized_orbits | computation | 6,149 | 4 | 6 |
| incremental_cache_manager | cache | 657 | 1 | 4 |
| json_converter | pipeline | 622 | 0 | 0 |
| json_gallery | gui | 524 | 0 | 0 |
| jupiter_visualization_shells | rendering/shells | 769 | 2 | 1 |
| mars_visualization_shells | rendering/shells | 701 | 2 | 1 |
| mercury_visualization_shells | rendering/shells | 641 | 2 | 1 |
| messier_catalog | data | 396 | 0 | 3 |
| messier_object_data_handler | other | 321 | 2 | 1 |
| moon_visualization_shells | rendering/shells | 434 | 2 | 1 |
| neptune_visualization_shells | rendering/shells | 1,504 | 3 | 1 |
| object_type_analyzer | computation | 754 | 1 | 3 |
| orbit_data_manager | cache | 1,520 | 0 | 3 |
| orbital_elements | computation | 1,285 | 0 | 4 |
| orbital_param_viz | gui | 1,923 | 5 | 1 |
| orrery_integration | utility | 315 | 1 | 0 |
| osculating_cache_manager | cache | 761 | 2 | 3 |
| paleoclimate_dual_scale | rendering | 955 | 2 | 1 |
| paleoclimate_human_origins_full | rendering | 1,884 | 1 | 1 |
| paleoclimate_visualization | rendering | 478 | 1 | 2 |
| paleoclimate_visualization_full | rendering | 1,487 | 1 | 1 |
| paleoclimate_wet_bulb_full | rendering | 2,224 | 1 | 1 |
| palomas_orrery | gui | 8,615 | 27 | 0 |
| palomas_orrery_dashboard | gui | 587 | 0 | 0 |
| palomas_orrery_helpers | utility | 765 | 10 | 2 |
| planet9_visualization_shells | rendering/shells | 235 | 2 | 1 |
| planet_visualization | rendering | 1,046 | 16 | 2 |
| planet_visualization_utilities | rendering | 290 | 1 | 15 |
| planetarium_apparent_magnitude | rendering | 352 | 11 | 1 |
| planetarium_distance | rendering | 391 | 11 | 1 |
| plot_data_exchange | pipeline | 160 | 0 | 4 |
| plot_data_report_widget | rendering | 552 | 2 | 2 |
| pluto_visualization_shells | rendering/shells | 476 | 2 | 1 |
| report_manager | utility | 124 | 0 | 5 |
| saturn_visualization_shells | rendering/shells | 994 | 2 | 3 |
| save_utils | pipeline | 388 | 0 | 17 |
| scenarios_coral_bleaching | scenario | 191 | 0 | 1 |
| scenarios_heatwaves | scenario | 622 | 0 | 1 |
| scenarios_western_heatwave_march_2026 | scenario | 1,536 | 1 | 1 |
| sgr_a_grand_tour | rendering | 742 | 3 | 1 |
| sgr_a_star_data | data | 555 | 2 | 4 |
| sgr_a_visualization_animation | rendering | 343 | 3 | 0 |
| sgr_a_visualization_core | rendering | 557 | 2 | 3 |
| sgr_a_visualization_precession | rendering | 377 | 3 | 0 |
| shared_utilities | utility | 119 | 0 | 17 |
| shutdown_handler | utility | 66 | 1 | 5 |
| simbad_manager | computation | 1,028 | 2 | 6 |
| social_media_export | pipeline | 968 | 1 | 1 |
| solar_visualization_shells | rendering/shells | 1,425 | 2 | 6 |
| spacecraft_encounters | data | 1,204 | 2 | 1 |
| star_notes | data | 1,129 | 0 | 6 |
| star_properties | data | 328 | 2 | 4 |
| star_sphere_builder | rendering | 922 | 0 | 1 |
| star_visualization_gui | gui | 1,295 | 9 | 0 |
| star_visualization_gui_before_pyinstaller_refactor | legacy | 1,162 | 5 | 0 |
| stellar_data_patches | data | 34 | 0 | 4 |
| stellar_parameters | data | 340 | 2 | 8 |
| uranus_visualization_shells | rendering/shells | 979 | 3 | 1 |
| venus_visualization_shells | rendering/shells | 610 | 2 | 1 |
| verify_orbit_cache | cache | 170 | 0 | 0 |
| visualization_2d | rendering | 513 | 6 | 2 |
| visualization_3d | rendering | 847 | 5 | 2 |
| visualization_core | rendering | 343 | 4 | 7 |
| visualization_utils | rendering | 713 | 3 | 4 |
| vot_cache_manager | cache | 430 | 0 | 2 |

---

*Generated by module_atlas.py -- Paloma's Orrery Developer Tools*
