# Paloma's Orrery - Module Index

**Generated:** July 17, 2026 by `module_atlas.py`  
**Repository:** Paloma's Orrery - Solar System Visualization Suite  
**Philosophy:** Data Preservation is Climate Action

This file and `MODULE_ATLAS.md` are generated from the SAME scan
(see `module_atlas.py`) -- they cannot diverge from each other the
way the old hand-maintained MODULE_INDEX.md did. This is the light,
human-browsable view; `MODULE_ATLAS.md` is the deep reference
(functions, dependencies, consumers) meant for AI-assisted queries.

**Total Python Files:** 121  
**Total Lines of Code (non-blank):** 92,000  
**Total Public Functions/Classes:** 955

---

## Core Applications

| Module | Description |
|--------|-------------|
| `earth_system_controller.py` | KMZ layer selector for Google Earth Pro. (129 lines) |
| `earth_system_visualization_gui.py` | Earth System Visualization GUI for Paloma's Orrery Hub window with climate data visualizations (1,901 lines) |
| `orbital_param_viz.py` | Interactive orbital element visualization tool. (1,936 lines) |
| `palomas_orrery.py` | Main GUI and plotting engine for Paloma's Orrery. (9,490 lines) |
| `palomas_orrery_dashboard.py` | Paloma's Orrery Dashboard Central launch point for the Paloma's Orrery suite. (686 lines) |
| `star_visualization_gui.py` | Stellar visualization GUI for Paloma's Orrery. (1,407 lines) |

---

## Visualization Modules

| Module | Description |
|--------|-------------|
| `exoplanet_orbits.py` | Keplerian Orbit Calculations for Exoplanets (613 lines) |
| `hr_diagram_apparent_magnitude.py` | HR diagram pipeline for apparent magnitude queries. (430 lines) |
| `hr_diagram_distance.py` | HR diagram pipeline for distance-based queries. (449 lines) |
| `paleoclimate_dual_scale.py` | Dual-Scale Paleoclimate Visualization for Paloma's Orrery Side-by-side layout: Deep Time (log scale) + Modern Era (linear scale) (955 lines) |
| `paleoclimate_human_origins_full.py` | Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) (1,884 lines) |
| `paleoclimate_visualization.py` | Paleoclimate Visualization for Paloma's Orrery Cenozoic temperature and CO₂ reconstruction (66 Ma - present) (478 lines) |
| `paleoclimate_visualization_full.py` | Paleoclimate Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) (1,487 lines) |
| `paleoclimate_wet_bulb_full.py` | Paleoclimate + Wet Bulb Visualization for Paloma's Orrery Phanerozoic temperature reconstruction (540 Ma - present) with human survivability context (2,224 lines) |
| `planet_visualization.py` | High-level planet and Sun visualization orchestration. (711 lines) |
| `planet_visualization_utilities.py` | Shared geometry helpers and body-radius aliases. (764 lines) |
| `planetarium_apparent_magnitude.py` | Create 3D visualization for stars brighter than specified apparent magnitude. (352 lines) |
| `planetarium_distance.py` | 3D star field pipeline for distance-based queries. (399 lines) |
| `plot_data_report_widget.py` | Embedded report panel for star visualization results. (560 lines) |
| `sgr_a_grand_tour.py` | Stage 4 FINAL: The Grand Tour of the Galactic Center (742 lines) |
| `sgr_a_visualization_animation.py` | Stage 2: Animated visualization of S-Stars orbiting Sagittarius A*. (343 lines) |
| `sgr_a_visualization_core.py` | Core visualization module for S-Stars orbiting Sagittarius A*. (557 lines) |
| `sgr_a_visualization_precession.py` | Stage 3: The Relativistic Rosette (Schwarzschild Precession). (377 lines) |
| `star_sphere_builder.py` | Build and render celestial sphere for Paloma's Orrery. (922 lines) |
| `visualization_2d.py` | 2D HR diagram (color-magnitude) plot builder. (523 lines) |
| `visualization_3d.py` | 3D stellar neighborhood and planetarium plot builder. (857 lines) |
| `visualization_core.py` | Shared data preparation and formatting for star visualizations. (350 lines) |
| `visualization_utils.py` | Shared Plotly utilities for orrery and star visualizations. (854 lines) |

---

## Planetary & Solar Shell Visualizations

| Module | Description |
|--------|-------------|
| `asteroid_belt_visualization_shells.py` | Asteroid Belt Visualization Module Functions for creating visualizations of asteroid belt structures in 3D plots. Includes Main Belt, Hildas, Trojans, and Greeks. Also includes helper functions for dynamic Trojan positioning based on Jupiter's location. (401 lines) |
| `comet_visualization_shells.py` | Comet visual components for 3D orrery plots. (1,850 lines) |
| `earth_visualization_shells.py` | Earth interior and orbital shell traces. (992 lines) |
| `eris_visualization_shells.py` | Eris interior and boundary shell traces. (464 lines) |
| `jupiter_visualization_shells.py` | Jupiter interior, ring, and magnetosphere shell traces. (891 lines) |
| `mars_visualization_shells.py` | Mars interior and remnant field shell traces. (799 lines) |
| `mercury_visualization_shells.py` | Mercury interior, exosphere, and unique feature traces. (343 lines) |
| `moon_visualization_shells.py` | Lunar interior and exosphere shell traces. (543 lines) |
| `neptune_visualization_shells.py` | Neptune interior, ring, and magnetosphere shell traces. (1,557 lines) |
| `planet9_visualization_shells.py` | Hypothetical Planet 9 shell traces. (267 lines) |
| `pluto_visualization_shells.py` | Pluto interior and atmosphere shell traces. (565 lines) |
| `saturn_visualization_shells.py` | Saturn interior, ring, and magnetosphere shell traces. (1,086 lines) |
| `solar_visualization_shells.py` | Sun interior, corona, and heliosphere shell traces. (1,312 lines) |
| `uranus_visualization_shells.py` | Uranus interior, ring, and magnetosphere shell traces. (1,081 lines) |
| `venus_visualization_shells.py` | Venus interior and atmosphere shell traces. (614 lines) |

---

## Orbital Mechanics & Calculations

| Module | Description |
|--------|-------------|
| `apsidal_markers.py` | Perihelion, aphelion, perigee, and apogee marker generation. (1,738 lines) |
| `catalog_selection.py` | Unified star selection from Hipparcos and Gaia catalogs. (92 lines) |
| `celestial_coordinates.py` | Module for calculating and formatting Right Ascension and Declination coordinates for celestial objects in Paloma's Orrery. (454 lines) |
| `coordinate_system_guide.py` | Educational reference for J2000 Ecliptic Coordinate System (547 lines) |
| `data_acquisition.py` | Unified module for both distance- and magnitude-based queries, integrating the simpler logic of data_acquisition_distance.py. (220 lines) |
| `data_acquisition_distance.py` | Module for fetching stellar data based on distance. (169 lines) |
| `data_processing.py` | Star catalog data cleaning, merging, and analysis. (434 lines) |
| `earth_system_generator.py` | Paloma's Orrery: Earth System Generator Engine Architecture: The Teaser (Plotly) & Blockbuster (KMZ) Pipeline (671 lines) |
| `energy_imbalance.py` | Energy Imbalance Visualization for Paloma's Orrery Modern era (2005-2025) temperature and energy imbalance (839 lines) |
| `fetch_climate_data.py` | Climate Data Fetcher - Paloma's Orrery Preserves critical climate datasets for future reference (761 lines) |
| `fetch_paleoclimate_data.py` | Paleoclimate Data Fetcher for Paloma's Orrery Fetches and caches paleoclimate proxy data from authoritative sources (169 lines) |
| `idealized_orbits.py` | Keplerian orbit ellipse construction and satellite orbit models. Computes and plots idealized (Keplerian) orbit paths from orbital elements, with osculating element support for high-accuracy visualization. Handles elliptical, parabolic, and hyperbolic orbits. Includes specia... (6,613 lines) |
| `object_type_analyzer.py` | Object Type Analysis and Report Generation Module Provides comprehensive analysis of astronomical data including object types, data quality metrics, and full report generation. (754 lines) |
| `orbital_elements.py` | Standalone data module containing orbital element dictionaries. NO IMPORTS - Pure data only to avoid circular dependencies. (1,294 lines) |
| `simbad_manager.py` | Enhanced SIMBAD Query Manager with configurable rate limiting and retry logic. This module replaces simbad_test.py and provides robust SIMBAD querying capabilities. (1,028 lines) |

---

## Data Catalogs & Constants

| Module | Description |
|--------|-------------|
| `celestial_objects.py` | Celestial object definitions for Paloma's Orrery. (1,248 lines) |
| `close_approach_data.py` | JPL CAD API client for small-body close approach data. (513 lines) |
| `constants_new.py` | Verified numeric constants for Paloma's Orrery. (633 lines) |
| `exoplanet_coordinates.py` | Stellar Positioning and Coordinate Transformations (399 lines) |
| `exoplanet_stellar_properties.py` | Stellar Properties for Exoplanet Host Stars (482 lines) |
| `exoplanet_systems.py` | Hardcoded Exoplanet System Catalog (570 lines) |
| `info_dictionary.py` | Descriptive text and narrative content for Paloma's Orrery. (2,046 lines) |
| `messier_catalog.py` | Static catalog of Messier objects and bright deep-sky objects. (404 lines) |
| `sgr_a_star_data.py` | S-star catalog and orbital mechanics for Sagittarius A*. (572 lines) |
| `spacecraft_encounters.py` | Tagged encounter data for spacecraft missions in Paloma's Orrery. (1,293 lines) |
| `star_notes.py` | Curated hover text annotations for notable stars. (1,156 lines) |
| `star_properties.py` | SIMBAD stellar property queries with local caching. (338 lines) |
| `stellar_data_patches.py` | Manual corrections for stars with known bad catalog data. (41 lines) |
| `stellar_parameters.py` | Stellar temperature and parameter estimation from spectral types. (352 lines) |

---

## Cache Management

| Module | Description |
|--------|-------------|
| `climate_cache_manager.py` | Climate Cache Manager for Paloma's Orrery Manages safe updates of climate data caches with validation and rollback. (161 lines) |
| `incremental_cache_manager.py` | Smart incremental cache manager for VizieR catalog data and SIMBAD properties. Handles incremental fetching when query parameters change, avoiding redundant queries. (657 lines) |
| `orbit_data_manager.py` | Advanced orbit data caching and management (1,547 lines) |
| `osculating_cache_manager.py` | Auto-updating cache for osculating orbital elements from JPL Horizons. Uses two-generation backup protection and always-prompt user workflow. (761 lines) |
| `vot_cache_manager.py` | VOT Cache Manager - Safe management of VizieR VOT cache files Similar protection protocols as PKL files in simbad_manager.py (430 lines) |

---

## Save, Export & Pipeline Utilities

| Module | Description |
|--------|-------------|
| `messier_object_data_handler.py` | Messier object coordinate transforms and data preparation. (329 lines) |
| `plot_data_exchange.py` | JSON data exchange between subprocess scripts and GUI. (168 lines) |
| `save_utils.py` | Unified save/export for all Plotly visualizations. (795 lines) |
| `sgr_a_visualization_core_arcs.py` | Sgr_a_visualization_core.py Core visualization module for S-Stars orbiting Sagittarius A*. (535 lines) |
| `social_media_export.py` | Generates a second HTML file from an existing Plotly figure, optimized for screen recording Instagram Reels and YouTube Shorts (9:16 portrait). (969 lines) |

---

## Earth System Scenarios

| Module | Description |
|--------|-------------|
| `scenarios_coral_bleaching.py` | Paloma's Orrery: Coral Bleaching Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: NOAA Coral Reef Watch (ERDDAP API) - Degree Heating Weeks (DHW) (191 lines) |
| `scenarios_heatwaves.py` | Paloma's Orrery: Heatwave Scenario Definitions Provides fetch function + SCENARIOS list for the earth_system_generator engine. Data Source: ERA5 via Open-Meteo Archive API (709 lines) |
| `scenarios_western_heatwave_march_2026.py` | Paloma's Orrery: Western North America Heat Dome - March 2026 Scenario Module: Parameterized Timeline Snapshots (1,536 lines) |

---

## Utility & Helper Modules

| Module | Description |
|--------|-------------|
| `formatting_utils.py` | Basic formatting utilities used by both palomas_orrery.py and visualization_utils.py. (16 lines) |
| `palomas_orrery_helpers.py` | Support functions extracted from the main orrery monolith. (769 lines) |
| `report_manager.py` | Scientific Report Manager for Astronomical Data Analysis Manages generation, storage, and retrieval of analysis reports. (124 lines) |
| `shared_utilities.py` | Small shared helpers used across shell visualization modules. (202 lines) |
| `shutdown_handler.py` | Graceful shutdown and safe figure display for Plotly. (73 lines) |

---

## Developer Tools

| Module | Description |
|--------|-------------|
| `add_docstrings.py` | Add or improve module-level docstrings across the codebase. (631 lines) |
| `convert_hot_ph_to_json.py` | Convert HOT ocean pH data to JSON format Manual converter for ocean acidification visualization (197 lines) |
| `create_cache_backups.py` | One-shot script to create timestamped backups of star data caches. (8 lines) |
| `create_ephemeris_database.py` | Create satellite_ephemerides.json from multiple sources (243 lines) |
| `dep_trace.py` | Targeted dependency path tracer for Paloma's Orrery Usage: python dep_trace.py <module_name> [hops] (399 lines) |
| `diagnose_bcodmo.py` | Diagnostic script to examine BCO-DMO pH data structure (65 lines) |
| `examine_hot_csv.py` | Examine the HOT CSV file structure (45 lines) |
| `module_atlas.py` | Codebase encyclopedia generator for Paloma's Orrery (643 lines) |
| `provenance_scanner.py` | Fact provenance auditor for Paloma's Orrery. (1,553 lines) |
| `test_constants_provenance.py` | Regression tests for verified numeric constants. (490 lines) |
| `test_orbit_cache.py` | Comprehensive test suite for orbit data caching and repair (204 lines) |
| `verify_orbit_cache.py` | Safely verify and repair orbit_paths.json (170 lines) |

---

## Other Modules

| Module | Description |
|--------|-------------|
| `barycenter_cache_check.py` | (no description) (7 lines) |
| `color_map.py` | Gemini 5-1-2026 Color swatch of css colors Notes: This reference maps CSS4 named colors in Python/Matplotlib. RGB values are converted to the 0-255 standard for accessibility. In Python scripts, these can be used as strings or converted to 0.0-1.0 floats by dividing by 255. (43 lines) |
| `data_inventory.py` | Inventory data stores and gallery for handoff and headroom. (245 lines) |
| `earth_system_common.py` | Shared, engine-agnostic helpers for the Earth System KMZ generators (climate/heat and food insecurity). (132 lines) |
| `export_orbit_cache.py` | Phase 1b desktop devtool: read the local orbit caches and write web-servable orbit/position files for the interactive gallery. (611 lines) |
| `food_insecurity_generator.py` | IPC acute food-insecurity KMZ layer (Sudan, current period). (700 lines) |
| `ledger_index.py` | Generate the at-a-glance INDEX for the consolidated ledger. (662 lines) |
| `measure_animation_html.py` | Measure frame payload in a saved Plotly animation HTML. (99 lines) |
| `measure_perframe_elements.py` | Byte budget table for the per-frame animation engine. (123 lines) |
| `orrery_rendering.py` | Rendering contract between plot_objects and animate_objects. (318 lines) |
| `provenance_scanner_color_patch.py` | Transactional patch: document color/RGB exclusion from provenance-scanner claims, project-wide, per Tony's call (July 16, 2026). Run this once from the repo root (same directory as provenance_scanner.py). Verified against a disposable clone: py_compile clean, ASCII-only, and re-running the scanne... (88 lines) |
| `scenarios_food_insecurity.py` | Scenario registry for the IPC acute food-insecurity KMZ layers (Earth System family). (35 lines) |
| `shell_configs.py` | Shell configuration data for all celestial bodies. (2,563 lines) |
| `skills_index.py` | Generate the Skill Manifest table in the project instructions from the SKILL.md files in skills/. (255 lines) |
| `smoke_dipole_cone.py` | - container smoke test for the dipole-cone primitive (Movement 2, June 2026). Mirrors smoke_rotation_axis.py: it exercises the LIVE dispatch, not the builder in isolation, because last session's lesson was that a builder can work while the dispatch never calls it. No network... (144 lines) |
| `smoke_phase4.py` | Phase 4 live-dispatch smoke test. Imports palomas_orrery (GUI builds under xvfb; mainloop stubbed), drives the REAL checkbox vars, and asserts: 1. Opt-in OFF: checked magnetosphere absent from collect specs and the center skip set; '(static plots only)' legend placeholder PRESENT. 2. Opt-in ON: m... (123 lines) |
| `smoke_rotation_axis.py` | - container smoke test for the rotation-axis primitive (Movement 2, June 2026). Exercises the LIVE dispatch wiring: it resolves each body's CUSTOM_SHELLS['<body>']['rotation_axis']['builder'] string and calls it exactly as planet_visualization.py does (planet_name passed v... (145 lines) |
| `test_reset_completeness.py` | - guard the Reset button against partial-reset drift. (111 lines) |
| `titan_io_probe.py` | (no description) (1 lines) |

---

*Generated by `module_atlas.py` -- Paloma's Orrery Developer Tools. For function-level detail, dependencies, and consumers, see `MODULE_ATLAS.md`.*
