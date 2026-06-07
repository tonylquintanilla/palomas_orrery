# Paloma's Orrery - Major Refactor Planning Document

**Created**: December 31, 2025  
**Authors**: Tony + Claude Opus 4.5 + Gemini 3 Pro  
**Purpose**: Plan the reorganization of ~90 modules into a domain-based folder structure  
**Status**: PLANNING - To be executed in future session(s)

---

## Executive Summary

Paloma's Orrery has grown from a simple 2D Earth orbit calculator (September 2024) to a comprehensive astronomical visualization system with 90+ modules. The current flat file structure has become unwieldy. This document plans a refactor into logical domain folders while preserving all functionality.

---

## Proposed Directory Structure

```
palomas_orrery/
│
├── palomas_orrery.py              # Main GUI launcher (the "hub")
├── README.md                      # Project overview
│
├── docs/                          # Documentation folder
│   ├── README_ORRERY.md           # Solar system module docs
│   ├── README_STARS.md            # Stellar visualization docs
│   ├── README_EARTH_SCIENCE.md    # Climate/paleoclimate docs
│   ├── README_GALACTIC_CENTER.md  # Sgr A* visualization docs
│   ├── README_EXOPLANETS.md       # Exoplanet systems docs
│   ├── ARCHITECTURE.md            # Overall system architecture
│   ├── CHANGELOG.md               # Version history
│   └── SESSION_HANDOFFS/          # AI collaboration continuity docs
│       └── ...
│
├── orrery/                        # Solar system visualization
│   ├── __init__.py
│   ├── [modules listed below]
│   ├── planets/                   # Individual planet shells
│   └── small_bodies/              # Asteroids, comets, TNOs
│
├── stars/                         # Stellar visualization
│   ├── __init__.py
│   ├── [modules listed below]
│   └── messier/                   # Messier catalog handling
│
├── earth_science/                 # Climate & paleoclimate
│   ├── __init__.py
│   └── [modules listed below]
│
├── galactic_center/               # Sgr A* S-stars (NEW)
│   ├── __init__.py
│   └── [modules listed below]
│
├── exoplanets/                    # Exoplanet systems
│   ├── __init__.py
│   └── [modules listed below]
│
├── shared/                        # Cross-cutting utilities
│   ├── __init__.py
│   ├── [modules listed below]
│   └── cache/                     # Cache management utilities
│
└── data/                          # Data files (caches, databases)
    ├── caches/
    ├── climate/
    └── stellar/
```

---

## Module Mapping

### Current Modules → Target Locations

#### ORRERY (Solar System) - Target: `orrery/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `orbit_data_manager.py` | `orrery/` | Core orbit data |
| `osculating_cache_manager.py` | `orrery/` | Osculating elements cache |
| `orbital_elements.py` | `orrery/` | Orbital mechanics |
| `orbital_param_viz.py` | `orrery/` | Parameter visualization |
| `idealized_orbits.py` | `orrery/` | Idealized orbit calculations |
| `apsidal_markers.py` | `orrery/` | Perihelion/aphelion markers |
| `planet_visualization.py` | `orrery/` | Main planet viz |
| `planet_visualization_utilities.py` | `orrery/` | Planet viz helpers |
| `visualization_core.py` | `orrery/` | Core 3D visualization |
| `visualization_2d.py` | `orrery/` | 2D projections |
| `visualization_3d.py` | `orrery/` | 3D rendering |
| `palomas_orrery_helpers.py` | `orrery/` | GUI helpers |
| `orrery_integration.py` | `orrery/` | Integration utilities |
| `create_ephemeris_database.py` | `orrery/` | Ephemeris DB creation |
| `verify_orbit_cache.py` | `orrery/` | Cache verification |

#### ORRERY/PLANETS - Target: `orrery/planets/`

| Current Module | Target Location |
|----------------|-----------------|
| `mercury_visualization_shells.py` | `orrery/planets/` |
| `venus_visualization_shells.py` | `orrery/planets/` |
| `earth_visualization_shells.py` | `orrery/planets/` |
| `moon_visualization_shells.py` | `orrery/planets/` |
| `mars_visualization_shells.py` | `orrery/planets/` |
| `jupiter_visualization_shells.py` | `orrery/planets/` |
| `saturn_visualization_shells.py` | `orrery/planets/` |
| `uranus_visualization_shells.py` | `orrery/planets/` |
| `neptune_visualization_shells.py` | `orrery/planets/` |
| `pluto_visualization_shells.py` | `orrery/planets/` |
| `eris_visualization_shells.py` | `orrery/planets/` |
| `solar_visualization_shells.py` | `orrery/planets/` |

#### ORRERY/SMALL_BODIES - Target: `orrery/small_bodies/`

| Current Module | Target Location |
|----------------|-----------------|
| `asteroid_belt_visualization_shells.py` | `orrery/small_bodies/` |
| `comet_visualization_shells.py` | `orrery/small_bodies/` |
| `planet9_visualization_shells.py` | `orrery/small_bodies/` |

#### STARS (Stellar Visualization) - Target: `stars/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `star_visualization_gui.py` | `stars/` | Main stellar GUI |
| `star_visualization_gui_before_pyinstaller_refactor.py` | `stars/` | Backup/reference |
| `stellar_parameters.py` | `stars/` | Star property calculations |
| `stellar_data_patches.py` | `stars/` | Data corrections |
| `star_properties.py` | `stars/` | Property definitions |
| `star_notes.py` | `stars/` | Educational notes |
| `simbad_manager.py` | `stars/` | SIMBAD database interface |
| `hr_diagram_distance.py` | `stars/` | HR diagram (distance mode) |
| `hr_diagram_apparent_magnitude.py` | `stars/` | HR diagram (magnitude mode) |
| `planetarium_distance.py` | `stars/` | Sky view (distance mode) |
| `planetarium_apparent_magnitude.py` | `stars/` | Sky view (magnitude mode) |
| `celestial_coordinates.py` | `stars/` | Coordinate transforms |
| `catalog_selection.py` | `stars/` | Catalog filtering |
| `object_type_analyzer.py` | `stars/` | Object classification |
| `coordinate_system_guide.py` | `stars/` | Coordinate reference |

#### STARS/MESSIER - Target: `stars/messier/`

| Current Module | Target Location |
|----------------|-----------------|
| `messier_catalog.py` | `stars/messier/` |
| `messier_object_data_handler.py` | `stars/messier/` |

#### EARTH SCIENCE - Target: `earth_science/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `earth_system_visualization_gui.py` | `earth_science/` | Main Earth GUI |
| `climate_cache_manager.py` | `earth_science/` | Climate data cache |
| `fetch_climate_data.py` | `earth_science/` | Climate data acquisition |
| `fetch_paleoclimate_data.py` | `earth_science/` | Paleo data acquisition |
| `paleoclimate_visualization.py` | `earth_science/` | Paleo viz |
| `paleoclimate_visualization_full.py` | `earth_science/` | Full paleo viz |
| `paleoclimate_dual_scale.py` | `earth_science/` | Dual timescale viz |
| `paleoclimate_human_origins_full.py` | `earth_science/` | Human origins overlay |
| `energy_imbalance.py` | `earth_science/` | Energy budget viz |
| `convert_hot_ph_to_json.py` | `earth_science/` | Data conversion |
| `convert_sea_level_txt_to_json_onetime.py` | `earth_science/` | One-time conversion |
| `examine_hot_csv.py` | `earth_science/` | Data examination |
| `diagnose_bcodmo.py` | `earth_science/` | BCO-DMO diagnostics |

#### GALACTIC CENTER (Sgr A*) - Target: `galactic_center/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `sgr_a_star_data.py` | `galactic_center/` | S-star orbital data |
| `sgr_a_visualization_core.py` | `galactic_center/` | Core orbit generation |
| `sgr_a_visualization_animation.py` | `galactic_center/` | Keplerian animation |
| `sgr_a_visualization_precession.py` | `galactic_center/` | Relativistic rosette |
| `sgr_a_grand_tour.py` | `galactic_center/` | Unified dashboard |

#### EXOPLANETS - Target: `exoplanets/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `exoplanet_systems.py` | `exoplanets/` | System definitions |
| `exoplanet_coordinates.py` | `exoplanets/` | Coordinate handling |
| `exoplanet_orbits.py` | `exoplanets/` | Orbit calculations |
| `exoplanet_stellar_properties.py` | `exoplanets/` | Host star properties |

#### SHARED UTILITIES - Target: `shared/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `constants_new.py` | `shared/` | Physical constants |
| `shared_utilities.py` | `shared/` | Common utilities |
| `formatting_utils.py` | `shared/` | Output formatting |
| `visualization_utils.py` | `shared/` | Viz helpers |
| `save_utils.py` | `shared/` | File saving |
| `shutdown_handler.py` | `shared/` | Graceful shutdown |
| `plot_data_exchange.py` | `shared/` | Data exchange |
| `plot_data_report_widget.py` | `shared/` | Report generation |
| `report_manager.py` | `shared/` | Report management |
| `create_cache_backups.py` | `shared/` | Backup utilities |

#### SHARED/CACHE - Target: `shared/cache/`

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `incremental_cache_manager.py` | `shared/cache/` | Incremental caching |
| `vot_cache_manager.py` | `shared/cache/` | VOTable cache |
| `data_acquisition.py` | `shared/cache/` | General data acquisition |
| `data_acquisition_distance.py` | `shared/cache/` | Distance-based acquisition |
| `data_processing.py` | `shared/cache/` | Data processing |

#### MAIN GUI - Target: Root

| Current Module | Target Location | Notes |
|----------------|-----------------|-------|
| `palomas_orrery.py` | Root | Main launcher/hub |

#### DATA FILES - Target: `data/`

| Current File | Target Location | Notes |
|--------------|-----------------|-------|
| `uap_ethogram_v3.db` | `data/` | UAP database |
| Various `.json` caches | `data/caches/` | Cache files |
| Climate data files | `data/climate/` | Climate datasets |
| Stellar data files | `data/stellar/` | Star catalogs |

---

## Migration Strategy

### Phase 1: Preparation
1. Create complete backup of current state
2. Create new folder structure (empty folders with `__init__.py`)
3. Document all current import relationships

### Phase 2: Isolated Domains First
1. **Galactic Center** (already isolated, no dependencies)
2. **Exoplanets** (relatively isolated)
3. **Earth Science** (mostly self-contained)

### Phase 3: Interconnected Domains
4. **Stars** (some shared utilities)
5. **Orrery** (most complex, most dependencies)

### Phase 4: Shared Utilities
6. **Shared** (extract common code, update all imports)

### Phase 5: Finalization
7. Update main `palomas_orrery.py` hub
8. Comprehensive testing
9. Documentation updates

---

## Import Pattern Changes

### Before (flat structure):
```python
import visualization_core
from orbital_elements import calculate_position
```

### After (domain structure):
```python
from orrery import visualization_core
from orrery.orbital_elements import calculate_position
```

### Cross-domain imports:
```python
from shared.constants_new import AU_TO_KM
from shared.cache.vot_cache_manager import VOTCacheManager
```

---

## The Hub Pattern

The main `palomas_orrery.py` becomes a thin launcher:

```python
# palomas_orrery.py - Conceptual structure

class PalomasOrreryHub:
    """Main application hub - launches domain-specific visualizations."""
    
    def __init__(self):
        self.setup_main_menu()
    
    def launch_solar_system(self):
        from orrery.main_gui import SolarSystemGUI
        SolarSystemGUI()
    
    def launch_stellar_viz(self):
        from stars.star_visualization_gui import StarVisualizationGUI
        StarVisualizationGUI()
    
    def launch_earth_science(self):
        from earth_science.earth_system_visualization_gui import EarthSystemGUI
        EarthSystemGUI()
    
    def launch_galactic_center(self):
        from galactic_center.sgr_a_grand_tour import launch_grand_tour
        launch_grand_tour()
    
    def launch_exoplanets(self):
        from exoplanets.exoplanet_systems import ExoplanetGUI
        ExoplanetGUI()
```

---

## Risk Mitigation

### Risks:
1. **Broken imports**: Most common issue in refactors
2. **Circular dependencies**: Can emerge when splitting code
3. **Cache path changes**: Data files may have hardcoded paths
4. **PyInstaller impact**: Folder structure affects bundling

### Mitigations:
1. **Incremental migration**: One domain at a time, test after each
2. **Dependency mapping**: Document before moving
3. **Path abstraction**: Use `pathlib` and relative paths
4. **Backup everything**: Git commits at each stable point

---

## Immediate Action: Galactic Center Integration

**Decision**: Integrate Galactic Center NOW (before refactor) because:
1. Code is fresh and fully understood
2. It's isolated with no dependencies on existing modules
3. Provides template for how other domains will connect
4. 90% complete - just needs menu hook

### Integration Steps:
1. Copy Sgr A* modules to project folder
2. Add "Galactic Center" option to Exoplanetary Systems menu
3. Create launcher function that opens HTML in browser
4. Test the integration
5. This becomes the pattern for post-refactor domain connections

---

## Session Continuity Notes

### What Was Built (This Session):
- Complete S-star visualization system (4 modules + HTML output)
- Orbital mechanics faithful to observations (GRAVITY, Peißker et al.)
- Unified time spectrum for visual comparison
- Animation (Keplerian whoosh) + Rosette (Einstein precession) views
- Accuracy patch for S4714 (8% c literature match)

### Key Technical Decisions:
- Mean anomaly stepping for smooth animation
- Phase offsets from observed periapsis times
- Unified Plasma colorscale for apples-to-apples comparison
- S4714 semi-major axis: 800 AU (patched from 520 AU)

### Collaboration Notes:
- Three-way collaboration: Tony + Claude Opus 4.5 + Gemini 3 Pro
- Gemini provided architecture review and refinements
- Claude implemented and tested
- Tony provided vision, accuracy requirements, observational fidelity priority

---

## Files Delivered This Session

1. `sgr_a_star_data.py` - S-star orbital elements and constants
2. `sgr_a_visualization_core.py` - Orbit generation and 3D positioning
3. `sgr_a_visualization_animation.py` - Stage 2: Keplerian animation
4. `sgr_a_visualization_precession.py` - Stage 3: Relativistic rosettes
5. `sgr_a_grand_tour.py` - Stage 4: Unified dashboard
6. `sgr_a_grand_tour.html` - Portable visualization output
7. `sgr_a_newton_vs_einstein.html` - Educational comparison
8. This planning document

---

## Next Session Checklist

- [ ] Integrate Galactic Center into main GUI (if not done this session)
- [ ] Review this planning document
- [ ] Begin Phase 1: Create folder structure
- [ ] Begin Phase 2: Migrate Galactic Center (template)
- [ ] Continue with other domains as time permits

---

*"Data Preservation is Climate Action"*  
*Part of Paloma's Orrery*
