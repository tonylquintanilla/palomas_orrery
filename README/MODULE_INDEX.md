# Paloma's Orrery - Complete Module Index

**Last Updated:** November 6, 2025

Quick-reference guide to all Python modules in the project. Use your browser's find function (Ctrl+F / Cmd+F) to search for keywords like "save", "cache", "orbit", "visualization", etc.

For detailed documentation on primary modules, see [README.md](README.md#module-reference).

---

## Important Notes

**Development vs. Production Files:**

- **Testing modules** (`*_test.py`, `inclination_test.py`) - Development/debugging only, not required for normal application use
- **Obsolete modules** (`gui_simbad_controls.py`, `save_utils_before_simplification.py`) - Not imported or used in current codebase
- **Utility scripts** (`create_cache_backups.py`) - Simple standalone scripts for maintenance tasks

**Module Organization:**

- Total modules: 79 Python files
- Active production modules: 74
- Development/testing modules: 5
- Obsolete/unused modules: 2

---

## Core Application (3 modules)

| Module | Description |
|--------|-------------|
| `palomas_orrery.py` | **Primary GUI and solar system visualization engine** (404KB, 8,289 lines). Main application with three-column tkinter layout: object selection panels for celestial bodies/missions/comets/exoplanets (left), scrollable control panels for date/time/animation/scale settings (center), and notes panel (right). Core visualization functions: `plot_objects()` generates static 3D views using JPL Horizons data, `animate_objects()` creates frame-by-frame animations. Launches three specialized GUIs: `star_visualization_gui.py` (HR diagrams and stellar neighborhoods), `earth_system_visualization_gui.py` (climate data hub), and `orbital_param_viz.py` (orbital mechanics visualization). *Note: In retrospect, plot_objects and animate_objects could have been separate modules but remain as core 1,200+ line functions.* |
| `palomas_orrery_helpers.py` | Helper functions for main application including coordinate transformations, trajectory fetching, orbit backup utilities, and visualization utilities |
| `shutdown_handler.py` | Graceful application shutdown management and cleanup routines |

---

## Data Acquisition (6 modules)

| Module | Description |
|--------|-------------|
| `data_acquisition.py` | VizieR catalog queries for Gaia and Hipparcos stellar data with rate limiting |
| `data_acquisition_distance.py` | Distance-based stellar data fetching with configurable radius queries |
| `simbad_manager.py` | SIMBAD astronomical database API integration with comprehensive rate limiting and error handling |
| `orbit_data_manager.py` | JPL Horizons orbital data fetching, caching, and incremental updates for solar system objects |
| `fetch_climate_data.py` | Climate data acquisition from multiple sources (COâ‚‚, temperature, sea level, ice extent, ocean pH) |
| `fetch_paleoclimate_data.py` | Deep-time paleoclimate data fetching (Cenozoic Era temperature reconstructions) |

---

## Data Processing & Analysis (8 modules)

| Module | Description |
|--------|-------------|
| `data_processing.py` | Core data processing including coordinate transformations and stellar parameter calculations |
| `object_type_analyzer.py` | Stellar classification and spectral type analysis with luminosity class determination |
| `stellar_parameters.py` | Temperature, luminosity, and HR diagram calculations using stellar physics |
| `stellar_data_patches.py` | Data quality improvements and corrections for known stellar catalog issues |
| `enhanced_star_properties.py` | Enhanced stellar property calculations with incremental VizieR caching integration |
| `star_properties.py` | Core stellar property calculations and data structure definitions |
| `star_notes.py` | Comprehensive documentation of named stars with cultural and astronomical significance |
| `messier_object_data_handler.py` | Messier catalog object data processing and management |

---

## Cache Management (4 modules)

| Module | Description |
|--------|-------------|
| `vot_cache_manager.py` | VizieR VOTable cache management with atomic saves and validation |
| `incremental_cache_manager.py` | Smart incremental fetching for stellar datasets, avoiding redundant queries |
| `climate_cache_manager.py` | Climate data cache manager with automated validation and update checking |
| `verify_orbit_cache.py` | Orbit cache validation and repair utility with integrity checking |

**Note:** `orbit_data_manager.py` handles orbit caching but is listed under Data Acquisition as its primary function.

---

## Visualization - Core (4 modules)

| Module | Description |
|--------|-------------|
| `visualization_2d.py` | 2D visualization including Hertzsprung-Russell diagrams with interactive features |
| `visualization_3d.py` | Interactive 3D stellar neighborhood plots with camera controls and filtering |
| `visualization_core.py` | Common plotting utilities, color schemes, and styling functions shared across visualizations |
| `visualization_utils.py` | Utility functions for plot management, save dialogs, and figure display |

---

## Visualization - Planetary Shells (11 modules)

Interior cross-section visualizations for solar system bodies with scientifically accurate layer structures:

| Module | Description |
|--------|-------------|
| `solar_visualization_shells.py` | Solar interior and corona visualization with reference-frame independent rendering |
| `mercury_visualization_shells.py` | Mercury interior structure with large iron core and sodium tail visualization |
| `venus_visualization_shells.py` | Venus interior structure with thick atmosphere and cloud layers |
| `earth_visualization_shells.py` | Earth interior structure with crust, mantle, outer/inner core layers |
| `mars_visualization_shells.py` | Mars interior structure with oxidized crust and smaller core |
| `jupiter_visualization_shells.py` | Jupiter interior with metallic hydrogen layers and Great Red Spot |
| `saturn_visualization_shells.py` | Saturn interior structure with extensive ring system visualization |
| `uranus_visualization_shells.py` | Uranus interior with ice mantle and extreme axial tilt representation |
| `neptune_visualization_shells.py` | Neptune interior structure with dynamic atmosphere features |
| `pluto_visualization_shells.py` | Pluto-Charon system interior structures with binary planet dynamics |
| `eris_visualization_shells.py` | Eris interior structure for the largest known dwarf planet |

---

## Visualization - Specialized (8 modules)

| Module | Description |
|--------|-------------|
| `orbital_param_viz.py` | Orbital element visualization with interactive parameter exploration |
| `comet_visualization_shells.py` | Scientifically accurate comet rendering with dual-tail structures (dust and ion tails) |
| `asteroid_belt_visualization_shells.py` | Asteroid belt visualization including Main Belt, Hildas, and Jupiter Trojans |
| `planet9_visualization_shells.py` | Hypothetical Planet 9 visualization with orbit uncertainty visualization |
| `moon_visualization_shells.py` | Lunar interior structure and orbital mechanics visualization |
| `earth_system_visualization_gui.py` | Earth system data hub with 9 climate visualizations and interactive controls |
| `paleoclimate_visualization_full.py` | Comprehensive paleoclimate visualization with geological period markers |
| `paleoclimate_dual_scale.py` | Dual-scale paleoclimate plots showing recent and deep-time climate data |

---

## HR Diagrams & Stellar Visualizations (4 modules)

| Module | Description |
|--------|-------------|
| `hr_diagram_distance.py` | Hertzsprung-Russell diagram for stars within specified distance from Sun |
| `hr_diagram_apparent_magnitude.py` | HR diagram using apparent magnitude for observational comparison |
| `planetarium_distance.py` | Planetarium-style visualization of nearby stellar neighborhood with distance filtering |
| `planetarium_apparent_magnitude.py` | Planetarium view using apparent magnitude for sky-as-seen representation |

---

## Coordinate Systems & Orbital Mechanics (6 modules)

| Module | Description |
|--------|-------------|
| `celestial_coordinates.py` | RA/Dec coordinate system conversions and transformations between reference frames |
| `apsidal_markers.py` | Periapsis/apoapsis markers with body-specific terminology |
| `idealized_orbits.py` | Idealized Keplerian orbit calculations for perfect elliptical paths |
| `refined_orbits.py` | Refined orbital calculations accounting for perturbations and real-world effects |
| `orrery_integration.py` | Integration module for combining orbital data into orrery visualization |
| `inclination_test.py` | Test module for orbital inclination calculations and coordinate transformations |

---

## Exoplanet Systems (4 modules)

| Module | Description |
|--------|-------------|
| `exoplanet_systems.py` | Complete exoplanet system definitions including binary star systems |
| `exoplanet_orbits.py` | Exoplanet orbital mechanics calculations and visualization |
| `exoplanet_coordinates.py` | Coordinate transformations for exoplanetary systems |
| `exoplanet_stellar_properties.py` | Host star properties and system parameters for confirmed exoplanets |

---

## User Interface Components (5 modules)

| Module | Description |
|--------|-------------|
| `star_visualization_gui.py` | Star visualization control panel with filtering and selection options |
| `gui_simbad_controls.py` | **[OBSOLETE - NOT USED]** SIMBAD query interface controls (functionality now integrated into star_visualization_gui.py) |
| `catalog_selection.py` | User interface for selecting stellar catalogs (Gaia, Hipparcos, combined) |
| `plot_data_report_widget.py` | Widget for displaying statistical reports and data summaries |
| `report_manager.py` | Report generation system with scientific statistics and formatting |

---

## Utilities & Helpers (8 modules)

| Module | Description |
|--------|-------------|
| `save_utils.py` | Plot saving utilities with format selection (PNG, HTML) and error handling dialogs |
| `save_utils_before_simplification.py` | **[OBSOLETE - OLD VERSION]** Previous version of save_utils.py before simplification (not imported by any module) |
| `create_cache_backups.py` | **[UTILITY SCRIPT]** Simple utility to create timestamped backups of stellar cache data (calls protect_all_star_data) |
| `shared_utilities.py` | Common utility functions shared across multiple modules |
| `formatting_utils.py` | Text and number formatting utilities for consistent display |
| `planet_visualization_utilities.py` | Helper functions for planetary visualization rendering |
| `planet_visualization.py` | Planetary visualization rendering and animation utilities |
| `plot_data_exchange.py` | Data exchange protocol for passing plot data between modules |
| `constants_new.py` | Physical constants, orbital parameters, and configuration values (174KB - comprehensive) |

---

## Data Conversion (1 module)

| Module | Description |
|--------|-------------|
| `convert_hot_ph_to_json.py` | Convert Hawaii Ocean Time-series (HOT) pH data from CSV/TXT to JSON format |

---

## Catalogs & Reference Data (2 modules)

| Module | Description |
|--------|-------------|
| `messier_catalog.py` | Complete Messier catalog definitions with object types and coordinates |
| `create_ephemeris_database.py` | Satellite ephemeris database creation from multiple JPL sources |

---

## Summary Statistics

- **Total Python Modules:** 79
- **Active Production Modules:** 74
- **Development/Testing Modules:** 5 (cache_test, test_orbit_cache, simbad_test, simbad_test_2, inclination_test)
- **Obsolete/Unused Modules:** 2 (gui_simbad_controls, save_utils_before_simplification)
- **Total Lines of Code:** ~15,000+ (estimated from file sizes)
- **Largest Module:** `palomas_orrery.py` (404KB, 8,289 lines - main GUI and visualization engine)
- **Most Complex:** `constants_new.py` (174KB - comprehensive orbital parameters and physical constants)
- **Visualization Modules:** 27 (including planetary shells, HR diagrams, and specialized visualizations)

**Obsolete/Development Modules:**

- `gui_simbad_controls.py` - Functionality integrated into star_visualization_gui.py
- `save_utils_before_simplification.py` - Old version of save_utils.py
- Testing modules (simbad_test.py, simbad_test_2.py, cache_test.py, test_orbit_cache.py, inclination_test.py) - Development/debugging only

---

## Quick Search Keywords

Use Ctrl+F (Windows/Linux) or Cmd+F (Mac) to search for:

- **Save/Export:** `save_utils.py`, `visualization_utils.py`
- **Cache Management:** `vot_cache_manager.py`, `incremental_cache_manager.py`, `orbit_data_manager.py`
- **Coordinates:** `celestial_coordinates.py`, `exoplanet_coordinates.py`
- **Climate Data:** `fetch_climate_data.py`, `earth_system_visualization_gui.py`, `climate_cache_manager.py`
- **Orbits:** `orbit_data_manager.py`, `idealized_orbits.py`, `refined_orbits.py`, `orbital_param_viz.py`
- **Stars:** `star_properties.py`, `stellar_parameters.py`, `star_visualization_gui.py`
- **HR Diagram:** `hr_diagram_distance.py`, `hr_diagram_apparent_magnitude.py`, `visualization_2d.py`
- **SIMBAD:** `simbad_manager.py`, `gui_simbad_controls.py`
- **JPL Horizons:** `orbit_data_manager.py`, `create_ephemeris_database.py`
- **Exoplanets:** `exoplanet_systems.py`, `exoplanet_orbits.py`, `exoplanet_stellar_properties.py`

---

## System Architecture Overview

**10-Layer Vertical Design:**

The project follows a clean layered architecture with clear data flow from external sources (top) to final outputs (bottom). Each layer has specific responsibilities:

```
Layer 1: External Data Sources (4 sources)
   ↓
Layer 2: Data Acquisition (6 modules)
   ↓
Layer 3: Cache Management (4 managers + 2 utilities)
   ↓
Layer 4: Data Processing (8 modules)
   ↓
Layer 5: Visualization Preparation (27+ modules)
   ↓
Layer 6: User Interface (8+ GUIs)
   ↓
Layer 7: Reporting & Data Exchange (3 modules)
   ↓
Layer 8: Utilities & Support (5 modules)
   ↓
Layer 9: Configuration (2 modules)
   ↓
Layer 10: Final Outputs (files and directories)
```

**Module Distribution by Layer:**

- **Layer 2 (Acquisition):** 6 modules specialized by data type (orbit, stellar, climate, Messier)
- **Layer 3 (Cache):** 4 cache managers + 2 utilities (backups, verification) - "Defense-in-Depth"
- **Layer 4 (Processing):** 8 modules for coordinate math, stellar physics, orbital mechanics
- **Layer 5 (Viz Prep):** 27 modules including 12 planetary shells, 4 exoplanet modules, specialized visualizations
- **Layer 6 (UI):** 1 main GUI (8,289 lines) + 7 specialized visualization interfaces
- **Layer 7 (Reporting):** 3 modules for data exchange and statistical reporting
- **Layer 8 (Utils):** 5 cross-cutting utilities supporting multiple layers
- **Layer 9 (Config):** 2 large reference files (constants_new.py is 174KB)
- **Layer 10 (Outputs):** PNG/HTML plots, JSON data, reports, cache directories

**Three Parallel Pipelines:**

The system supports three major data pipelines that flow through these layers:

1. **Solar System Pipeline** (30+ modules)
   - Sources: JPL Horizons
   - Flow: Horizons → orbit_data_manager → orbit_cache → refined_orbits → planet_visualization → palomas_orrery → plot_objects() → PNG/HTML
   - Output: 3D orrery visualizations, animations, planetary shells

2. **Stellar Pipeline** (15+ modules)
   - Sources: Gaia, Hipparcos, SIMBAD
   - Flow: Catalogs → data_acquisition → vot_cache_manager → stellar_parameters → visualization_3d/2d → star_visualization_gui → HR diagrams
   - Output: 3D star maps, HR diagrams, stellar neighborhoods

3. **Earth System Pipeline** (3+ modules, growing)
   - Sources: NOAA, NASA GISS, NSIDC, others
   - Flow: Climate sources → fetch_climate_data → climate_cache_manager → earth_system_visualization_gui → 9 visualizations
   - Output: Climate data preservation hub with CO₂, temperature, sea ice, ocean pH, planetary boundaries, etc.

**Integration Points:**

- **Main GUI (palomas_orrery.py)** - Master integration launching all three pipelines (404KB, 8,289 lines)
- **Constants (constants_new.py)** - Feeds all pipelines with physical parameters (174KB reference data)
- **Utilities** - Provide cross-cutting support (save, format, shutdown) across layers 5-10
- **Cache Layer (Layer 3)** - Protects data integrity for all pipelines with validation and repair

**Architectural Strengths:**

1. **Modularity:** New visualizations can be added to Layer 5 without touching other layers
2. **Robustness:** Cache validation at Layer 3 prevents corrupted data from reaching processing
3. **Maintainability:** Clear layer boundaries make debugging straightforward
4. **Extensibility:** New data sources integrate at Layers 1-2 without refactoring downstream
5. **Testability:** Each layer can be validated independently
6. **Defense-in-Depth:** Multi-layer cache protection (atomic saves, validation, backups, repair)

**Module Complexity Analysis:**

*Largest Modules (by size/lines):*
- `palomas_orrery.py` - 8,289 lines (main GUI, plot_objects(), animate_objects())
- `constants_new.py` - 174KB (comprehensive orbital parameters and physical constants)
- Visualization modules - typically 500-1,500 lines each
- Shell modules - typically 200-400 lines each (12 modules for planetary interiors)

*Most Interconnected Modules:*
- `constants_new.py` - Referenced by layers 4-6 (cross-cutting configuration)
- `palomas_orrery.py` - Integrates all three pipelines (master controller)
- `visualization_core.py` - Shared utilities for all visualization types
- Cache managers - Protect data flow between layers 2-4 (critical infrastructure)

*Example Data Flow (Mars Visualization):*
```
User clicks "Mars" → palomas_orrery.py (L6) → orbit_data_manager (L2) 
→ [check cache] → orbit_cache/mars.json (L3) → refined_orbits.py (L4) 
→ planet_visualization.py (L5) → plot_objects() (L6) → Plotly render 
→ save_utils.py (L8) → PNG/HTML output (L10)

Time: Milliseconds (cached) or 1-2 seconds (fresh API call)
```

**For Visual Architecture:**

See `architecture_ascii_visualization.md` for a complete ASCII art diagram showing all 10 layers with box-drawing characters that renders in any markdown viewer. The diagram includes:
- Complete layer-by-layer breakdown with module details
- Three parallel pipeline visualizations
- Integration points and data flow examples
- Module distribution charts
- Architectural insights and benefits

Also available: `palomas_orrery_flowchart_v13_vertical.md` for Mermaid flowchart with detailed module-level connections.

---

## File Organization Notes

**Naming Conventions:**

- `*_visualization_shells.py` - Planetary interior cross-sections
- `*_cache_manager.py` - Cache management systems
- `hr_diagram_*.py` - Hertzsprung-Russell diagram variants
- `exoplanet_*.py` - Exoplanet system modules
- `*_test.py` - Testing and validation scripts

**Integration Points:**

- Main entry: `palomas_orrery.py`
- Data flow: acquisition â†’ processing â†’ caching â†’ visualization
- UI: Various `*_gui.py` modules for different panels
- Utilities: `*_utils.py` for shared functionality

---

## See Also

- [README.md](README.md) - Project overview, installation, and quick start
- [climate_readme.md](climate_readme.md) - Climate data documentation
- [architecture_ascii_visualization.md](architecture_ascii_visualization.md) - Complete ASCII art system architecture diagram
- [palomas_orrery_flowchart_v13_vertical.md](palomas_orrery_flowchart_v13_vertical.md) - Vertical Mermaid flowchart with detailed connections
- [working_protocol_v2_3.md](working_protocol_v2_3.md) - Development collaboration protocol

---

Generated November 6, 2025 for Paloma's Orrery project
