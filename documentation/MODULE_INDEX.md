# Paloma's Orrery - Module Index

**Last Updated:** January 19, 2026  
**Repository:** Paloma's Orrery - Solar System Visualization Suite  
**Author:** Tony Quintanilla with Claude AI  
**Philosophy:** Data Preservation is Climate Action

---

## Overview

Paloma's Orrery is a comprehensive astronomical visualization application that transforms real NASA/ESA data into interactive 3D visualizations of solar system dynamics, spacecraft trajectories, stellar neighborhoods, galactic center dynamics, and Earth system processes.

**Total Python Files:** 88  
**Total Lines of Code:** ~78,400  

**Module Organization:**

- Core GUI applications: 4 (palomas_orrery.py, star_visualization_gui.py, earth_system_visualization_gui.py, orbital_param_viz.py)
- Solar system visualization modules: 25+
- Stellar visualization modules: 15+
- Climate/paleoclimate modules: 10+
- Data management and caching: 10+
- Utility and helper modules: 20+
- Development/reference modules: 4

**Recent Architectural Additions (Dec 2025 - Jan 2026):**
- Galactic Center / Sagittarius A* visualization system (S-stars with relativistic precession)
- TNO satellite visualization system with analytical fallback
- Center-body aware osculating cache
- Paleoclimate wet bulb temperature visualization
- Multi-AI collaboration workflow (Mode 7)

---

## Core Applications

| Module | Description |
|--------|-------------|
| `palomas_orrery.py` | **Primary GUI and solar system visualization engine** (~471KB, 9,464 lines). Main application with three-column tkinter layout: object selection panels for celestial bodies/missions/comets/exoplanets (left), scrollable control panels for date/time/animation/scale settings (center), and notes panel (right). Core visualization functions: `plot_objects()` generates static 3D views using JPL Horizons data, `animate_objects()` creates frame-by-frame animations. Supports TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2) with `ANALYTICAL_ANIMATION_FALLBACK` for objects without JPL ephemeris. Launches three specialized GUIs: `star_visualization_gui.py`, `earth_system_visualization_gui.py`, and `orbital_param_viz.py`. |
| `star_visualization_gui.py` | **Stellar neighborhood visualization hub** (1,557 lines). GUI for HR diagrams and 3D planetarium views of nearby stars. Supports both distance-limited and magnitude-limited queries to Hipparcos/Gaia catalogs via SIMBAD. Includes PyInstaller frozen executable support for standalone distribution. Features: catalog selection, SIMBAD property enrichment, plot data reporting. |
| `earth_system_visualization_gui.py` | **Climate data visualization hub** (2,043 lines). Central interface for Earth system science visualizations including CO2 trends, temperature anomalies, Arctic ice extent, ocean pH, sea level rise, energy imbalance, and multiple paleoclimate reconstructions. Embodies "Data Preservation is Climate Action" philosophy. |
| `orbital_param_viz.py` | **Orbital mechanics visualization tool** (2,277 lines). Interactive visualization of orbital parameters and transformations. Shows how orbital elements map to 3D trajectories, demonstrates reference frame transformations, and educates on Keplerian mechanics. |

---

## Orbital Mechanics & Calculations

| Module | Description |
|--------|-------------|
| `idealized_orbits.py` | **Core orbit visualization engine** (5,516 lines). Keplerian orbit calculations using osculating elements from `osculating_cache.json`. Supports dual-orbit systems (ideal vs actual), apsidal markers, and multi-center modes including Pluto-Charon barycenter, Orcus-Vanth barycenter. Includes `plot_tno_satellite_orbit()` for TNO moon visualization and `ANALYTICAL_FALLBACK_SATELLITES` list for objects without JPL ephemeris (e.g., MK2 calculated from arXiv:2509.05880). Handles Jupiter, Saturn, Uranus, Neptune, and Pluto moon systems with proper reference frame transformations. |
| `orbital_elements.py` | **Central orbital element repository** (1,328 lines). Standalone data module (NO IMPORTS to avoid circular dependencies). Contains `planetary_params` dictionary with osculating elements for all solar system objects, `parent_planets` mapping parent-satellite relationships, and `planet_tilts` for axial tilt data. Includes TNO satellite orbital elements (Dysnomia, Hi'iaka, Namaka, MK2) and analytical parameters for objects without JPL ephemeris. |
| `apsidal_markers.py` | **Apsidal point calculation module** (1,723 lines). Calculates perihelion/aphelion (and body-specific terms like perijove, periareion) from orbital positions and elements. Includes anomaly conversions (true, eccentric, mean), date estimation for apsidal passages, and Plotly marker generation. Features `APSIDAL_TERMINOLOGY` dictionary for correct naming by central body. |
| `celestial_coordinates.py` | **Coordinate transformation utilities** (528 lines). Handles conversions between equatorial (RA/Dec), ecliptic, galactic, and Cartesian coordinate systems. Essential for aligning data from different sources (JPL Horizons uses ecliptic, Gaia uses equatorial). |
| `coordinate_system_guide.py` | **Reference frame documentation** (664 lines). Educational module documenting coordinate system conventions used throughout the project. Explains ecliptic vs equatorial frames, epoch handling, and common pitfalls. |
| `exoplanet_coordinates.py` | **Exoplanet coordinate utilities** (517 lines). Specialized coordinate handling for exoplanet system visualization including proper motion corrections and distance-based scaling. |

---

## Cache Management

| Module | Description |
|--------|-------------|
| `orbit_data_manager.py` | **Primary orbit path cache manager** (1,816 lines). Handles efficient storage and retrieval of orbital path data with incremental updates. Manages `orbit_paths.json` (~92MB) containing trajectory data for 1,300+ objects. Features automatic refresh, data validation, and graceful degradation. |
| `osculating_cache_manager.py` | **Osculating elements cache with epoch tracking** (729 lines). Auto-updating cache for JPL Horizons osculating orbital elements. Includes `get_cache_key()` helper for center-body aware caching (e.g., `"Charon@9"` for barycenter view). Two-generation backup protection, configurable refresh intervals (weekly for planets, daily for active moons). |
| `incremental_cache_manager.py` | **Smart incremental VizieR/SIMBAD cache** (823 lines). Handles incremental fetching when query parameters change. Avoids redundant queries by tracking what's already cached. Supports both distance-limited and magnitude-limited stellar queries. |
| `vot_cache_manager.py` | **VOTable cache protection** (525 lines). Manages cached VOTable files from VizieR queries with integrity verification and backup systems. |
| `climate_cache_manager.py` | **Climate data cache manager** (203 lines). Manages cached climate datasets with validation, backup, and atomic save operations. |

---

## Stellar Visualization Pipeline

| Module | Description |
|--------|-------------|
| `data_acquisition.py` | **Unified catalog query module** (244 lines). Handles both distance-limited and magnitude-limited queries to VizieR. Requests only needed columns to avoid overloading servers on large queries. |
| `data_acquisition_distance.py` | **Distance-based stellar queries** (214 lines). Specialized module for parallax-based distance queries to Hipparcos and Gaia catalogs. |
| `data_processing.py` | **Stellar data transformation** (516 lines). Processes raw catalog data: magnitude estimation, distance calculation, coordinate alignment between Hipparcos and Gaia systems. |
| `star_properties.py` | **SIMBAD property enrichment** (392 lines). Queries SIMBAD for stellar properties (spectral types, object types) and assigns them to catalog data. |
| `stellar_parameters.py` | **Physical parameter estimation** (412 lines). Estimates stellar temperatures, radii, and luminosities from spectral types using empirical relationships. |
| `stellar_data_patches.py` | **Known data corrections** (43 lines). Patches for known errors or missing data in stellar catalogs. |
| `simbad_manager.py` | **SIMBAD query manager** (1,240 lines). Robust SIMBAD querying with configurable rate limiting, retry logic, and progress saving. Includes batch processing for large star lists. |
| `catalog_selection.py` | **Star selection logic** (103 lines). Handles selection of stars from combined Hipparcos/Gaia catalogs with deduplication and quality filtering. |
| `object_type_analyzer.py` | **SIMBAD object type analysis** (890 lines). Analyzes and categorizes SIMBAD object type codes, providing human-readable descriptions and statistics. |

---

## Stellar Visualization Output

| Module | Description |
|--------|-------------|
| `hr_diagram_distance.py` | **Distance-limited HR diagram** (543 lines). Creates Hertzsprung-Russell diagrams for stars within specified distance limits. Main entry point for distance-based stellar visualization. |
| `hr_diagram_apparent_magnitude.py` | **Magnitude-limited HR diagram** (516 lines). Creates HR diagrams for stars brighter than specified apparent magnitude. |
| `planetarium_distance.py` | **3D stellar neighborhood - distance mode** (487 lines). Creates interactive 3D "planetarium" views of nearby stars within distance limit. |
| `planetarium_apparent_magnitude.py` | **3D stellar neighborhood - magnitude mode** (434 lines). Creates 3D views of stars brighter than magnitude limit. |
| `visualization_core.py` | **Shared visualization utilities** (406 lines). Core functions used by both HR diagrams and planetarium views: temperature colors, magnitude analysis, star count reporting. |
| `visualization_2d.py` | **2D HR diagram rendering** (607 lines). Handles the actual Plotly figure creation for HR diagrams with proper axis scaling and annotations. |
| `visualization_3d.py` | **3D planetarium rendering** (977 lines). Creates interactive 3D stellar visualizations with the Sun at center. Includes coordinate transformation and hover text generation. |
| `visualization_utils.py` | **Additional visualization helpers** (775 lines). Supplementary visualization functions shared across modules. |
| `star_notes.py` | **Notable star annotations** (1,249 lines). Contains `unique_notes` dictionary with educational annotations for notable stars (Proxima Centauri, Sirius, Barnard's Star, etc.). Rich hover text with historical and scientific context. |

---

## Galactic Center Visualization (NEW Dec 2025)

| Module | Description |
|--------|-------------|
| `sgr_a_visualization_core.py` | **S-Star orbit visualization core** (660 lines). Core visualization module for S-stars orbiting Sagittarius A*. Generates 3D orbits from orbital elements, supports relativistic precession visualization. |
| `sgr_a_star_data.py` | **S-Star orbital data catalog** (672 lines). Contains orbital elements and physical constants for S-stars near Sgr A*. Data from GRAVITY Collaboration and Gillessen et al. Includes temperature-based star colors and Schwarzschild precession calculations. |
| `sgr_a_visualization_animation.py` | **S-Star animation module** (403 lines). Mean anomaly stepping animation for S-star orbits. Shows stars moving at relativistic speeds near the black hole. |
| `sgr_a_visualization_precession.py` | **Relativistic precession visualization** (447 lines). Demonstrates General Relativity effects on S-star orbits. Shows rosette patterns from Schwarzschild precession. |
| `sgr_a_grand_tour.py` | **Multi-star visualization** (843 lines). "Grand tour" of the Galactic Center showing multiple S-stars with unified temperature-based coloring. Educational visualization of the extreme environment near a supermassive black hole. |

---

## Planet Visualization Shells

Each planet has a dedicated "shells" module containing layered internal structure (core, mantle, crust) and external features (atmosphere, magnetosphere, Hill sphere). Information text for hover displays included.

| Module | Lines | Description |
|--------|-------|-------------|
| `solar_visualization_shells.py` | 1,438 | Sun structure: core, radiative zone, convective zone, photosphere, chromosphere, corona, termination shock, heliopause, Oort cloud boundaries |
| `mercury_visualization_shells.py` | 752 | Mercury: large iron core, thin silicate mantle, sodium tail, weak magnetosphere |
| `venus_visualization_shells.py` | 697 | Venus: core, mantle, thick CO2 atmosphere, sulfuric acid clouds |
| `earth_visualization_shells.py` | 781 | Earth: inner/outer core, lower/upper mantle, crust, atmosphere layers, magnetosphere |
| `moon_visualization_shells.py` | 496 | Moon: small iron core, thick mantle, regolith, exosphere |
| `mars_visualization_shells.py` | 811 | Mars: core, mantle, thin CO2 atmosphere, seasonal polar caps |
| `jupiter_visualization_shells.py` | 905 | Jupiter: metallic hydrogen core, molecular hydrogen envelope, cloud bands, Great Red Spot, massive magnetosphere |
| `saturn_visualization_shells.py` | 1,143 | Saturn: similar to Jupiter plus ring system structure |
| `uranus_visualization_shells.py` | 1,110 | Uranus: ice/rock core, water-ammonia-methane "ice" mantle, extreme axial tilt |
| `neptune_visualization_shells.py` | 1,708 | Neptune: largest shells module - includes Triton system, Great Dark Spot, dynamic atmosphere |
| `pluto_visualization_shells.py` | 537 | Pluto: nitrogen ice, water ice mantle, rocky core, thin atmosphere |
| `eris_visualization_shells.py` | 454 | Eris: surface methane ice, likely differentiated interior |
| `planet9_visualization_shells.py` | 267 | Hypothetical Planet 9: theoretical parameters for visualization |
| `asteroid_belt_visualization_shells.py` | 506 | Asteroid belt structure and major asteroid visualizations |
| `comet_visualization_shells.py` | 1,084 | Comet visualization: nucleus, coma, dust tail, ion tail. Includes `HISTORICAL_TAIL_DATA` for famous comets (Halley, Hale-Bopp, NEOWISE, etc.) with spectroscopic colors |

---

## Planet Visualization Core

| Module | Description |
|--------|-------------|
| `planet_visualization.py` | **Celestial body visualization factory** (1,120 lines). Creates layered 3D visualizations for planets and Sun. Imports shell components from individual planet modules. Main functions: `create_celestial_body_visualization()`, `create_planet_shell_traces()`. |
| `planet_visualization_utilities.py` | **Planet visualization helpers** (351 lines). Shared utility functions for planet visualization including sphere generation, color gradients, and scale calculations. |
| `shared_utilities.py` | **Cross-module utilities** (139 lines). Functions shared across visualization modules, including `create_sun_direction_indicator()` for anti-sunward vectors. |
| `formatting_utils.py` | **Number formatting utilities** (17 lines). `format_maybe_float()` and `format_km_float()` for consistent number display. |

---

## Exoplanet Systems

| Module | Description |
|--------|-------------|
| `exoplanet_systems.py` | **Hardcoded exoplanet catalog** (689 lines). Contains well-characterized exoplanet systems with complete orbital parameters: TRAPPIST-1 (7 planets, 3 in HZ), TOI-1338 (circumbinary), Proxima Centauri. Data from NASA Exoplanet Archive. |
| `exoplanet_orbits.py` | **Exoplanet orbit visualization** (748 lines). Generates 3D orbit traces for exoplanet systems. Handles binary host stars, habitable zone visualization, and proper scaling for tiny orbital radii. |
| `exoplanet_stellar_properties.py` | **Host star visualization** (607 lines). Creates visualizations for exoplanet host stars including temperature-based coloring and size scaling. |

---

## Climate & Paleoclimate Visualization

| Module | Description |
|--------|-------------|
| `fetch_climate_data.py` | **Climate data fetcher** (922 lines). Retrieves and caches critical climate datasets from NOAA, NASA GISS, NSIDC. Embodies "Data Preservation is Climate Action" - systematic archiving of potentially threatened datasets. |
| `fetch_paleoclimate_data.py` | **Paleoclimate data fetcher** (201 lines). Retrieves deep-time climate proxy data (ice cores, benthic stacks). |
| `energy_imbalance.py` | **Earth energy imbalance visualization** (951 lines). Visualizes Earth's radiative energy imbalance - the fundamental driver of climate change. |
| `paleoclimate_visualization.py` | **Quaternary paleoclimate** (560 lines). Ice age cycles visualization using LR04 benthic stack. |
| `paleoclimate_dual_scale.py` | **Dual-scale paleoclimate** (1,084 lines). Shows both deep-time and recent climate on synchronized scales. |
| `paleoclimate_visualization_full.py` | **Phanerozoic climate** (1,633 lines). 540 million year climate reconstruction using Scotese data. |
| `paleoclimate_human_origins_full.py` | **Human evolution climate context** (2,063 lines). Paleoclimate during hominin evolution with species milestones. |
| `paleoclimate_wet_bulb_full.py` | **Wet bulb temperature visualization** (2,466 lines). NEW Jan 2026. Shows Phanerozoic climate alongside modern extreme heat events on wet bulb temperature scale. Demonstrates human survivability thresholds (31-35 degC Tw) to contextualize why even small global warming translates to lethal local conditions. |

---

## Helper & Support Modules

| Module | Description |
|--------|-------------|
| `palomas_orrery_helpers.py` | **Main GUI helper functions** (851 lines). Extracted helper functions from palomas_orrery.py: trajectory fetching, orbit calculations, Planet 9 position estimation, animation safety checks. |
| `save_utils.py` | **Unified save/export utilities** (495 lines). Consistent API for saving Plotly visualizations across all modules. Supports HTML (CDN/offline), PNG (via kaleido), with dialog or direct modes. |
| `orrery_integration.py` | **External integration helpers** (395 lines). Functions for integrating orrery visualizations with external systems. |
| `plot_data_exchange.py` | **Plot data interchange** (175 lines). Standardized format for passing plot data between modules and to reporting system. |
| `plot_data_report_widget.py` | **Plot data reporting GUI** (661 lines). Tkinter widget for displaying plot metadata, star lists, and generating reports from visualizations. |
| `report_manager.py` | **Report generation** (149 lines). Creates formatted text reports from plot data including statistics and star listings. |
| `shutdown_handler.py` | **Graceful shutdown** (86 lines). Handles application shutdown, ensuring caches are saved and resources released. |
| `earth_system_controller.py` | **Earth GUI controller** (93 lines). MVC controller for earth_system_visualization_gui. |
| `earth_system_generator.py` | **Earth system data generation** (1,113 lines). Generates derived data products for Earth system visualizations. |

---

## Messier Objects

| Module | Description |
|--------|-------------|
| `messier_catalog.py` | **Messier object data** (423 lines). Contains the Messier catalog with coordinates, types, and descriptions for all 110 Messier objects. |
| `messier_object_data_handler.py` | **Messier visualization handler** (378 lines). Processes Messier catalog data for visualization, handles coordinate transformations. |

---

## Data Processing & Conversion (One-time/Development)

| Module | Description |
|--------|-------------|
| `create_ephemeris_database.py` | **Ephemeris database builder** (293 lines). Creates local ephemeris database from JPL Horizons for offline operation. |
| `verify_orbit_cache.py` | **Cache integrity verification** (201 lines). Validates orbit_paths.json integrity and reports any corruption. |
| `create_cache_backups.py` | **Backup utility** (1 line stub). Placeholder for cache backup automation. |
| `convert_hot_ph_to_json.py` | **HOT pH data converter** (234 lines). Converts Hawaii Ocean Time-series carbonate chemistry data to JSON cache format. |
| `convert_sea_level_txt_to_json_onetime.py` | **Sea level data converter** (41 lines). One-time conversion of sea level text data to JSON. |
| `examine_hot_csv.py` | **HOT data examination** (53 lines). Development utility for examining HOT dataset structure. |
| `diagnose_bcodmo.py` | **BCO-DMO diagnostic** (80 lines). Development utility for diagnosing BCO-DMO data access issues. |

---

## Reference/Obsolete Modules

| Module | Description |
|--------|-------------|
| `star_visualization_gui_before_pyinstaller_refactor.py` | **Pre-refactor backup** (1,417 lines). Preserved version before PyInstaller modifications for reference. |

---

## Configuration Files

| File | Description |
|------|-------------|
| `constants_new.py` | **Master constants module** (2,280 lines). Physical constants (KM_PER_AU, LIGHT_MINUTES_PER_AU), center body radii, known orbital periods, color maps, stellar class mappings, object type mappings. Central reference for all numeric constants. |
| `requirements.txt` | Python package dependencies |
| `window_config.json` | GUI window position/size persistence |
| `star_viz_config.json` | Star visualization GUI settings |
| `START_HERE.bat` | Windows launch script |
| `UPDATE_CODE.bat` | Windows update script |
| `update_code.sh` | Linux/macOS update script |
| `README.md` | Project documentation |

---

## Data Files (in data/ directory)

| File | Description |
|------|-------------|
| `orbit_paths.json` | ~92MB trajectory cache with 1,300+ orbital entries |
| `osculating_cache.json` | JPL Horizons osculating elements for 40+ objects |
| `star_properties_*.pkl` | Cached SIMBAD stellar properties |
| `hip_data_*.vot` | Hipparcos catalog cache |
| `gaia_data_*.vot` | Gaia catalog cache |
| `co2_mauna_loa_monthly.json` | Mauna Loa CO2 measurements |
| `temperature_giss_monthly.json` | NASA GISS temperature anomalies |
| `arctic_ice_extent_monthly.json` | NSIDC Arctic ice extent |
| `sea_level_gmsl_monthly.json` | Global mean sea level |
| `ocean_ph_hot_monthly.json` | Hawaii Ocean Time-series pH data |
| `lr04_benthic_stack.json` | LR04 paleoclimate data |

---

## TNO Satellite Systems

The orrery visualizes Trans-Neptunian Object satellite systems with full orbital mechanics:

| System | Satellites | Data Source |
|--------|------------|-------------|
| Eris | Dysnomia | JPL Horizons osculating elements |
| Haumea | Hi'iaka, Namaka | JPL Horizons osculating elements |
| Makemake | MK2 | Analytical fallback (arXiv:2509.05880) |
| Orcus | Vanth | JPL Horizons osculating elements |
| Quaoar | Weywot | JPL Horizons osculating elements |
| Gonggong | Xiangliu | JPL Horizons osculating elements |

**Analytical Fallback Architecture:**

For satellites without JPL Horizons ephemeris (like MK2), the system calculates orbits from published orbital elements:

```
ANALYTICAL_FALLBACK_SATELLITES = ['MK2']  # In idealized_orbits.py
ANALYTICAL_ANIMATION_FALLBACK = ['MK2']   # In palomas_orrery.py
```

**Data Flow (MK2 example):**
```
User selects MK2 -> fetch_trajectory() -> JPL returns empty
    |
    v
Check ANALYTICAL_ANIMATION_FALLBACK -> MK2 listed
    |
    v
Load elements from orbital_elements.py (arXiv source)
    |
    v
Calculate Keplerian orbit analytically
    |
    v
Display with "Analytical Orbit" attribution
```

---

## Data Flow Examples

*Example Data Flow (Mars Visualization):*
```
User clicks "Mars" -> palomas_orrery.py -> orbit_data_manager
-> [check cache] -> orbit_cache/mars.json -> idealized_orbits.py
-> planet_visualization.py -> plot_objects() -> Plotly render
-> save_utils.py -> PNG/HTML output

Time: Milliseconds (cached) or 1-2 seconds (fresh API call)
```

*Example Data Flow (HR Diagram):*
```
User requests 100 ly diagram -> star_visualization_gui.py
-> hr_diagram_distance.py -> data_acquisition_distance.py
-> VizieR (Hipparcos/Gaia) -> data_processing.py
-> simbad_manager.py (properties) -> stellar_parameters.py
-> visualization_2d.py -> Plotly HR diagram -> save_utils.py

Time: Seconds (cached) or minutes (fresh query + SIMBAD enrichment)
```

*Example Data Flow (Sgr A* Visualization):*
```
User selects S2 star -> sgr_a_grand_tour.py
-> sgr_a_star_data.py (orbital elements)
-> sgr_a_visualization_core.py (orbit generation)
-> Optional: sgr_a_visualization_precession.py (GR effects)
-> Plotly 3D render -> save_utils.py

Time: Milliseconds (all calculations local)
```

---

## Architecture Notes

### Layer Structure

```
Layer 1: GUI Applications
    palomas_orrery.py, star_visualization_gui.py, 
    earth_system_visualization_gui.py, orbital_param_viz.py

Layer 2: Visualization Engines
    idealized_orbits.py, planet_visualization.py, 
    visualization_2d.py, visualization_3d.py, sgr_a_*.py

Layer 3: Data Processing
    data_processing.py, stellar_parameters.py, 
    apsidal_markers.py, celestial_coordinates.py

Layer 4: Data Acquisition & Caching
    orbit_data_manager.py, osculating_cache_manager.py,
    simbad_manager.py, incremental_cache_manager.py

Layer 5: Pure Data (No Dependencies)
    orbital_elements.py, constants_new.py, 
    exoplanet_systems.py, sgr_a_star_data.py

Layer 6: Utilities
    save_utils.py, formatting_utils.py, shared_utilities.py
```

### Key Design Principles

1. **Cache Everything**: Minimize API calls, maximize offline operation
2. **Graceful Degradation**: Fall back to analytical calculations when API fails
3. **Visual Verification**: "Runs without errors" != correct physics
4. **Reference Frame Awareness**: Always check inclination to verify coordinate system
5. **Data Preservation**: Systematic archiving of potentially threatened datasets

---

## Related Documentation

- [README.md](README.md) - Project overview and setup instructions
- [FLOWCHART.md](palomas_orrery_flowchart_v15_vertical.md) - Mermaid flowchart with detailed connections
- [PROTOCOL.md](project_instructions.md) - Development protocol and collaboration methodology

---

*Generated January 19, 2026 for Paloma's Orrery project*  
*Data Preservation is Climate Action*
