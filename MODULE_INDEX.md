# Paloma's Orrery - Module Index

**Generated:** August 28, 2026 by `module_atlas.py`  
**Repository:** Paloma's Orrery - Solar System Visualization Suite  
**Philosophy:** Data Preservation is Climate Action

This file and `MODULE_ATLAS.md` are generated from the SAME scan
(see `module_atlas.py`) -- they cannot diverge from each other the
way the old hand-maintained MODULE_INDEX.md did. This is the light,
human-browsable view; `MODULE_ATLAS.md` is the deep reference
(functions, dependencies, consumers) meant for AI-assisted queries.

**Total Python Files:** 128  
**Total Lines of Code (non-blank):** 103,889  
**Total Public Functions/Classes:** 1,169

## Classification Coverage

**Undetermined role (3).** No valid `Role:` tag in the module docstring. Not guessed -- add the tag and re-run `add_docstrings.py`, then this file.

- `test_extractor_pins.py`
- `test_worksheet_keys.py`
- `worksheet_key_aliases.py`


---

## Core Applications

| Module | Description |
|--------|-------------|
| `earth_system_controller.py` | KMZ layer selector for Google Earth Pro. (131 lines) |
| `earth_system_visualization_gui.py` | Earth System Visualization GUI for Paloma's Orrery Hub window with climate data visualizations (1,903 lines) |
| `orbital_param_viz.py` | Interactive orbital element visualization tool. (1,938 lines) |
| `palomas_orrery.py` | Main GUI and plotting engine for Paloma's Orrery. (9,479 lines) |
| `palomas_orrery_dashboard.py` | Paloma's Orrery Dashboard Central launch point for the Paloma's Orrery suite. (1,155 lines) |
| `star_visualization_gui.py` | Stellar visualization GUI for Paloma's Orrery. (1,409 lines) |

---

## Visualization Modules

| Module | Description |
|--------|-------------|
| `exoplanet_orbits.py` | Keplerian Orbit Calculations for Exoplanets (615 lines) |
| `hr_diagram_apparent_magnitude.py` | HR diagram pipeline for apparent magnitude queries. (432 lines) |
| `hr_diagram_distance.py` | HR diagram pipeline for distance-based queries. (451 lines) |
| `orrery_rendering.py` | Rendering contract between plot_objects and animate_objects. (352 lines) |
| `paleoclimate_dual_scale.py` | Dual-Scale Paleoclimate Visualization for Paloma's Orrery Side-by-side layout: Deep Time (log scale) + Modern Era (linear scale) (957 lines) |
| `paleoclimate_human_origins_full.py` | Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) (1,886 lines) |
| `paleoclimate_visualization.py` | Paleoclimate Visualization for Paloma's Orrery Cenozoic temperature and CO₂ reconstruction (66 Ma - present) (480 lines) |
| `paleoclimate_visualization_full.py` | Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) (1,489 lines) |
| `paleoclimate_wet_bulb_full.py` | Paleoclimate + Wet Bulb Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) with human survivability context (2,226 lines) |
| `planet_visualization.py` | High-level planet and Sun visualization orchestration. (712 lines) |
| `planet_visualization_utilities.py` | Shared geometry helpers and body-radius aliases. (921 lines) |
| `planetarium_apparent_magnitude.py` | Create 3D visualization for stars brighter than specified apparent magnitude. (355 lines) |
| `planetarium_distance.py` | 3D star field pipeline for distance-based queries. (401 lines) |
| `plot_data_report_widget.py` | Embedded report panel for star visualization results. (562 lines) |
| `sgr_a_grand_tour.py` | Stage 4 FINAL: The Grand Tour of the Galactic Center (742 lines) |
| `sgr_a_visualization_animation.py` | Stage 2: Animated visualization of S-Stars orbiting Sagittarius A*. (345 lines) |
| `sgr_a_visualization_core.py` | Core visualization module for S-Stars orbiting Sagittarius A*. (561 lines) |
| `sgr_a_visualization_precession.py` | Stage 3: The Relativistic Rosette (Schwarzschild Precession). (357 lines) |
| `star_sphere_builder.py` | Build and render celestial sphere for Paloma's Orrery. (924 lines) |
| `visualization_2d.py` | 2D HR diagram (color-magnitude) plot builder. (525 lines) |
| `visualization_3d.py` | 3D stellar neighborhood and planetarium plot builder. (859 lines) |
| `visualization_core.py` | Shared data preparation and formatting for star visualizations. (352 lines) |
| `visualization_utils.py` | Shared Plotly utilities for orrery and star visualizations. (857 lines) |

---

## Planetary & Solar Shell Visualizations

| Module | Description |
|--------|-------------|
| `asteroid_belt_visualization_shells.py` | Asteroid Belt Visualization Module Functions for creating visualizations of asteroid belt structures in 3D plots. Includes Main Belt, Hildas, Trojans, and Greeks. Also includes helper functions for dynamic Trojan positioning based on Jupiter's location. (403 lines) |
| `comet_visualization_shells.py` | Comet visual components for 3D orrery plots. (1,878 lines) |
| `earth_visualization_shells.py` | Earth interior and orbital shell traces. (1,074 lines) |
| `eris_visualization_shells.py` | Eris interior and boundary shell traces. (482 lines) |
| `jupiter_visualization_shells.py` | Jupiter interior, ring, and magnetosphere shell traces. (897 lines) |
| `mars_visualization_shells.py` | Mars interior and remnant field shell traces. (811 lines) |
| `mercury_visualization_shells.py` | Mercury interior, exosphere, and unique feature traces. (368 lines) |
| `moon_visualization_shells.py` | Lunar interior and exosphere shell traces. (571 lines) |
| `neptune_visualization_shells.py` | Neptune interior, ring, and magnetosphere shell traces. (1,559 lines) |
| `planet9_visualization_shells.py` | Hypothetical Planet 9 shell traces. (269 lines) |
| `pluto_visualization_shells.py` | Pluto interior and atmosphere shell traces. (615 lines) |
| `saturn_visualization_shells.py` | Saturn interior, ring, and magnetosphere shell traces. (1,088 lines) |
| `solar_visualization_shells.py` | Sun interior, corona, and heliosphere shell traces. (1,537 lines) |
| `uranus_visualization_shells.py` | Uranus interior, ring, and magnetosphere shell traces. (1,083 lines) |
| `venus_visualization_shells.py` | Venus interior and atmosphere shell traces. (645 lines) |

---

## Orbital Mechanics & Calculations

| Module | Description |
|--------|-------------|
| `apsidal_markers.py` | Perihelion, aphelion, perigee, and apogee marker generation. (1,739 lines) |
| `catalog_selection.py` | Unified star selection from Hipparcos and Gaia catalogs. (94 lines) |
| `celestial_coordinates.py` | Module for calculating and formatting Right Ascension and Declination coordinates for celestial objects in Paloma's Orrery. (456 lines) |
| `coordinate_system_guide.py` | Educational reference for J2000 Ecliptic Coordinate System (549 lines) |
| `data_acquisition.py` | Unified module for both distance- and magnitude-based queries, integrating the simpler logic of data_acquisition_distance.py. (222 lines) |
| `data_acquisition_distance.py` | Module for fetching stellar data based on distance. (172 lines) |
| `data_processing.py` | Star catalog data cleaning, merging, and analysis. (436 lines) |
| `energy_imbalance.py` | Energy Imbalance Visualization for Paloma's Orrery Modern era (2005-2025) temperature and energy imbalance (841 lines) |
| `fetch_climate_data.py` | Climate Data Fetcher - Paloma's Orrery Preserves critical climate datasets for future reference (763 lines) |
| `fetch_paleoclimate_data.py` | Paleoclimate Data Fetcher for Paloma's Orrery Fetches and caches paleoclimate proxy data from authoritative sources (171 lines) |
| `idealized_orbits.py` | Keplerian orbit ellipse construction and satellite orbit models. Computes and plots idealized (Keplerian) orbit paths from orbital elements, with osculating element support for high-accuracy visualization. Handles elliptical, parabolic, and hyperbolic orbits. Includes specia... (6,615 lines) |
| `object_type_analyzer.py` | Object Type Analysis and Report Generation Module Provides comprehensive analysis of astronomical data including object types, data quality metrics, and full report generation. (756 lines) |
| `orbital_elements.py` | Standalone data module containing orbital element dictionaries. NO IMPORTS - Pure data only to avoid circular dependencies. (1,296 lines) |
| `simbad_manager.py` | Enhanced SIMBAD Query Manager with configurable rate limiting and retry logic. This module replaces simbad_test.py and provides robust SIMBAD querying capabilities. (1,030 lines) |

---

## Data Catalogs & Constants

| Module | Description |
|--------|-------------|
| `celestial_objects.py` | Celestial object definitions for Paloma's Orrery. (1,250 lines) |
| `close_approach_data.py` | JPL CAD API client for small-body close approach data. (512 lines) |
| `constants_new.py` | Verified numeric constants for Paloma's Orrery. (1,152 lines) |
| `exoplanet_coordinates.py` | Stellar Positioning and Coordinate Transformations (412 lines) |
| `exoplanet_stellar_properties.py` | Stellar Properties for Exoplanet Host Stars (484 lines) |
| `exoplanet_systems.py` | Hardcoded Exoplanet System Catalog (572 lines) |
| `info_dictionary.py` | Descriptive text and narrative content for Paloma's Orrery. (2,050 lines) |
| `messier_catalog.py` | Static catalog of Messier objects and bright deep-sky objects. (406 lines) |
| `sgr_a_star_data.py` | S-star catalog and orbital mechanics for Sagittarius A*. (590 lines) |
| `shell_configs.py` | Shell configuration data for all celestial bodies. (2,564 lines) |
| `spacecraft_encounters.py` | Tagged encounter data for spacecraft missions in Paloma's Orrery. (1,298 lines) |
| `star_notes.py` | Curated hover text annotations for notable stars. (1,158 lines) |
| `star_properties.py` | SIMBAD stellar property queries with local caching. (340 lines) |
| `stellar_data_patches.py` | Manual corrections for stars with known bad catalog data. (43 lines) |
| `stellar_parameters.py` | Stellar temperature and parameter estimation from spectral types. (354 lines) |

---

## Cache Management

| Module | Description |
|--------|-------------|
| `climate_cache_manager.py` | Climate Cache Manager for Paloma's Orrery Manages safe updates of climate data caches with validation and rollback. (163 lines) |
| `incremental_cache_manager.py` | Smart incremental cache manager for VizieR catalog data and SIMBAD properties. Handles incremental fetching when query parameters change, avoiding redundant queries. (659 lines) |
| `orbit_data_manager.py` | Advanced orbit data caching and management (1,550 lines) |
| `osculating_cache_manager.py` | Auto-updating cache for osculating orbital elements from JPL Horizons. Uses two-generation backup protection and always-prompt user workflow. (763 lines) |
| `vot_cache_manager.py` | VOT Cache Manager - Safe management of VizieR VOT cache files Similar protection protocols as PKL files in simbad_manager.py (432 lines) |

---

## Save, Export & Pipeline Utilities

| Module | Description |
|--------|-------------|
| `messier_object_data_handler.py` | Messier object coordinate transforms and data preparation. (331 lines) |
| `plot_data_exchange.py` | JSON data exchange between subprocess scripts and GUI. (170 lines) |
| `save_utils.py` | Unified save/export for all Plotly visualizations. (797 lines) |
| `sgr_a_visualization_core_arcs.py` | Sgr_a_visualization_core.py Core visualization module for S-Stars orbiting Sagittarius A*. (539 lines) |
| `social_media_export.py` | Generates a second HTML file from an existing Plotly figure, optimized for screen recording Instagram Reels and YouTube Shorts (9:16 portrait). (971 lines) |

---

## Earth System Scenarios

| Module | Description |
|--------|-------------|
| `scenarios_coral_bleaching.py` | Paloma's Orrery: Coral Bleaching Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: NOAA Coral Reef Watch (ERDDAP API) - Degree Heating Weeks (DHW) (193 lines) |
| `scenarios_food_insecurity.py` | Scenario registry for the IPC acute food-insecurity KMZ layers (Earth System family). (37 lines) |
| `scenarios_heatwaves.py` | Paloma's Orrery: Heatwave Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: ERA5 via Open-Meteo Archive API (711 lines) |
| `scenarios_western_heatwave_march_2026.py` | Paloma's Orrery: Western North America Heat Dome - March 2026 Scenario Module: Parameterized Timeline Snapshots (1,538 lines) |

---

## Utility & Helper Modules

| Module | Description |
|--------|-------------|
| `earth_system_common.py` | Shared, engine-agnostic helpers for the Earth System KMZ generators (climate/heat and food insecurity). (134 lines) |
| `formatting_utils.py` | Basic formatting utilities used by both palomas_orrery.py and visualization_utils.py. (19 lines) |
| `palomas_orrery_helpers.py` | Support functions extracted from the main orrery monolith. (741 lines) |
| `report_manager.py` | Scientific Report Manager for Astronomical Data Analysis Manages generation, storage, and retrieval of analysis reports. (126 lines) |
| `shared_utilities.py` | Small shared helpers used across shell visualization modules. (205 lines) |
| `shutdown_handler.py` | Graceful shutdown and safe figure display for Plotly. (75 lines) |

---

## Developer Tools

| Module | Description |
|--------|-------------|
| `add_docstrings.py` | Two related tools for module-level docstrings. (1,210 lines) |
| `constants_change_report.py` | - what moved in constants_new.py, and why. (510 lines) |
| `convert_hot_ph_to_json.py` | Convert HOT ocean pH data to JSON format Manual converter for ocean acidification visualization (199 lines) |
| `create_cache_backups.py` | One-shot script to create timestamped backups of star data caches. (10 lines) |
| `create_ephemeris_database.py` | Create satellite_ephemerides.json from multiple sources (246 lines) |
| `data_inventory.py` | Inventory data stores and gallery for handoff and headroom. (247 lines) |
| `dep_trace.py` | Targeted dependency path tracer for Paloma's Orrery Usage: python dep_trace.py <module_name> [hops] (419 lines) |
| `diagnose_bcodmo.py` | Diagnostic script to examine BCO-DMO pH data structure (67 lines) |
| `earth_system_generator.py` | Paloma's Orrery: Earth System Generator Engine Architecture: The Teaser (Plotly) & Blockbuster (KMZ) Pipeline (673 lines) |
| `examine_hot_csv.py` | Examine the HOT CSV file structure (47 lines) |
| `export_orbit_cache.py` | Phase 1b desktop devtool: read the local orbit caches and write web-servable orbit/position files for the interactive gallery. (617 lines) |
| `food_insecurity_generator.py` | IPC acute food-insecurity KMZ layer (Sudan, current period). (702 lines) |
| `ledger_index.py` | Generate the at-a-glance INDEX for the consolidated ledger. (710 lines) |
| `maintenance_run.py` | - L-188. One command, the whole maintenance suite. (477 lines) |
| `measure_animation_html.py` | Measure frame payload in a saved Plotly animation HTML. (101 lines) |
| `measure_perframe_elements.py` | Byte budget table for the per-frame animation engine. (125 lines) |
| `module_atlas.py` | Codebase encyclopedia generator for Paloma's Orrery (956 lines) |
| `provenance_history.py` | Run history and run-to-run delta for the provenance scanner (ledger L-189). (357 lines) |
| `provenance_scanner.py` | Fact provenance auditor for Paloma's Orrery. (3,066 lines) |
| `skills_index.py` | Generate the Skill Manifest table in the project instructions from the SKILL.md files in skills/. (342 lines) |
| `test_citation_inheritance.py` | Regression tests for citation-block inheritance. (516 lines) |
| `test_constants_provenance.py` | Regression tests for verified numeric constants. (389 lines) |
| `test_cross_checked.py` | Regression tests for cross-check annotations. (501 lines) |
| `test_orbit_cache.py` | Comprehensive test suite for orbit data caching and repair (224 lines) |
| `test_provenance_1d.py` | Regression tests for the Phase 1d/1e changes. (485 lines) |
| `test_reset_completeness.py` | - guard the Reset button against partial-reset drift. (119 lines) |
| `test_worksheet_checker.py` | - L-192. Can each layer actually fail? (995 lines) |
| `test_worksheet_request_builder.py` | - L-195 / L-192. Does the marker join actually join, and can it fail? (439 lines) |
| `verify_orbit_cache.py` | Safely verify and repair orbit_paths.json (172 lines) |
| `worksheet_checker.py` | - L-192. Does the worksheet say what the annotation claims it says? (2,140 lines) |
| `worksheet_keys.py` | Worksheet row keys -- one owner for the syntax and the resolution. (481 lines) |
| `worksheet_request_builder.py` | Worksheet request builder -- ask the question the checker can read. (652 lines) |

---

## Undetermined -- Needs a Role: Tag

| Module | Description |
|--------|-------------|
| `test_extractor_pins.py` | The instruction filter keeps and drops what it kept and dropped. (238 lines) |
| `test_worksheet_keys.py` | Round trip: every annotated site mints a key that resolves back. (255 lines) |
| `worksheet_key_aliases.py` | Retired worksheet keys and what replaced them. (67 lines) |

---

*Generated by `module_atlas.py` -- Paloma's Orrery Developer Tools. For function-level detail, dependencies, and consumers, see `MODULE_ATLAS.md`.*
