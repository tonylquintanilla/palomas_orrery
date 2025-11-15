# Paloma's Orrery - System Architecture

## 10-Layer Architecture Overview

The system follows a clean layered design where data flows vertically from external sources through processing layers to final outputs.

```
Architecture Layers/
│
├── Layer 1: External Data Sources
│   ├── JPL Horizons (orbital ephemerides)
│   ├── Gaia DR3 / Hipparcos (stellar positions)
│   ├── SIMBAD (stellar properties)
│   ├── Climate Data Sources (NOAA, NASA GISS, NSIDC)
│   └── Messier Catalog (deep sky objects)
│
├── Layer 2: Data Acquisition (6 modules)
│   ├── orbit_data_manager.py          # JPL Horizons queries
│   ├── data_acquisition.py            # VizieR catalog queries
│   ├── data_acquisition_distance.py   # Distance-based stellar queries
│   ├── simbad_manager.py              # SIMBAD API integration
│   ├── fetch_climate_data.py          # Climate data fetching
│   └── fetch_paleoclimate_data.py     # Deep-time climate data
│
├── Layer 3: Cache Management (6 modules) - "Defense-in-Depth"
│   ├── Orbit Cache
│   │   ├── orbit_data_manager.py      # Caching functions
│   │   ├── verify_orbit_cache.py      # Validation & repair
│   │   └── orbit_cache/               # JSON files (~94 MB)
│   ├── Stellar Cache
│   │   ├── vot_cache_manager.py       # VOTable management
│   │   ├── incremental_cache_manager.py  # Smart incremental updates
│   │   └── star_data/                 # .vot & .pkl files (335+ MB)
│   ├── Climate Cache
│   │   ├── climate_cache_manager.py   # Climate data validation
│   │   └── data/                      # JSON climate files
│   └── Protection Layer
│       └── create_cache_backups.py    # Automated backups
│
├── Layer 4: Data Processing (8 modules)
│   ├── Coordinate Processing
│   │   ├── data_processing.py         # Cartesian coordinate transforms
│   │   └── celestial_coordinates.py   # RA/Dec conversions
│   ├── Stellar Physics
│   │   ├── stellar_parameters.py      # Temperature, luminosity calcs
│   │   ├── stellar_data_patches.py    # Data quality corrections
│   │   └── enhanced_star_properties.py
│   ├── Orbital Mechanics
│   │   ├── refined_orbits.py          # Refined orbit calculations
│   │   ├── idealized_orbits.py        # Keplerian orbits
│   │   ├── orrery_integration.py      # Configuration management
│   │   └── apsidal_markers.py         # Perihelion/aphelion markers
│   └── Analysis
│       ├── object_type_analyzer.py    # Stellar classification
│       └── catalog_selection.py       # Star selection logic
│
├── Layer 5: Visualization Preparation (27+ modules)
│   ├── Solar System Visualization (4 modules)
│   │   ├── planet_visualization.py
│   │   ├── planet_visualization_utilities.py
│   │   ├── idealized_orbits.py
│   │   └── palomas_orrery_helpers.py
│   ├── Stellar Visualization (3 modules)
│   │   ├── visualization_3d.py        # 3D stellar neighborhoods
│   │   ├── visualization_2d.py        # HR diagrams
│   │   └── visualization_core.py      # Common utilities
│   ├── Planetary Interior Shells (14 modules)
│   │   ├── solar_visualization_shells.py
│   │   ├── mercury_visualization_shells.py
│   │   ├── venus_visualization_shells.py
│   │   ├── earth_visualization_shells.py
│   │   ├── moon_visualization_shells.py
│   │   ├── mars_visualization_shells.py
│   │   ├── jupiter_visualization_shells.py
│   │   ├── saturn_visualization_shells.py
│   │   ├── uranus_visualization_shells.py
│   │   ├── neptune_visualization_shells.py
│   │   ├── pluto_visualization_shells.py
│   │   ├── eris_visualization_shells.py
│   │   ├── planet9_visualization_shells.py
│   │   └── asteroid_belt_visualization_shells.py
│   ├── Specialized Visualizations (2 modules)
│   │   └── comet_visualization_shells.py  # Dual-tail structures
│   └── Exoplanet Systems (4 modules)
│       ├── exoplanet_systems.py
│       ├── exoplanet_orbits.py
│       ├── exoplanet_coordinates.py
│       └── exoplanet_stellar_properties.py
│
├── Layer 6: User Interface (8+ modules)
│   ├── Main Application
│   │   └── palomas_orrery.py          # Main GUI (404KB, 8,289 lines)
│   │       ├── plot_objects()         # Static 3D visualizations
│   │       └── animate_objects()      # Time evolution animations
│   ├── Specialized GUIs (3 modules)
│   │   ├── star_visualization_gui.py  # Stellar visualizations
│   │   ├── earth_system_visualization_gui.py  # Climate hub (9 viz)
│   │   └── orbital_param_viz.py       # Orbital mechanics education
│   ├── HR Diagram Variants (4 modules)
│   │   ├── hr_diagram_distance.py
│   │   ├── hr_diagram_apparent_magnitude.py
│   │   ├── planetarium_distance.py
│   │   └── planetarium_apparent_magnitude.py
│   └── Climate Visualizations (2 modules)
│       ├── paleoclimate_visualization_full.py
│       └── paleoclimate_dual_scale.py
│
├── Layer 7: Reporting & Data Exchange (3 modules)
│   ├── plot_data_exchange.py          # Save/load plot data
│   ├── report_manager.py              # Scientific report generation
│   ├── plot_data_report_widget.py     # Display statistical summaries
│   └── reports/                       # Output directory
│       ├── last_plot_data.json
│       ├── last_plot_report.json
│       └── report_*.json (timestamped archives)
│
├── Layer 8: Utilities & Support (5 modules)
│   ├── save_utils.py                  # Plot export (PNG, HTML)
│   ├── formatting_utils.py            # Text formatting
│   ├── visualization_utils.py         # Display utilities
│   ├── shared_utilities.py            # UI components (ScrollableFrame, ToolTip)
│   └── shutdown_handler.py            # Graceful cleanup
│
├── Layer 9: Configuration (2 modules)
│   ├── constants_new.py               # Physical constants (174KB!)
│   │   ├── Orbital parameters
│   │   ├── Physical constants
│   │   ├── Object type mappings
│   │   └── Exoplanet data definitions
│   └── star_notes.py                  # Educational content
│       └── unique_notes dictionary
│
└── Layer 10: Final Outputs
    ├── Interactive Plots
    │   ├── *.png files                # Static images
    │   └── *.html files               # Interactive Plotly visualizations
    ├── Data Files
    │   ├── *.json                     # Structured data
    │   ├── *.vot                      # VOTable format
    │   └── *.pkl                      # Pickle binary format
    └── Persistent Storage
        ├── orbit_cache/               # Orbital mechanics cache
        ├── star_data/                 # Stellar properties cache
        ├── data/                      # Climate & reference data
        └── reports/                   # Analysis reports
```

---

## Three Parallel Data Pipelines

The architecture supports three distinct processing pipelines that flow through the common layer structure:

```
Data Pipelines/
│
├── 🌟 Solar System Pipeline (30+ modules)
│   ├── Source: JPL Horizons
│   ├── Acquisition: orbit_data_manager.py
│   ├── Cache: orbit_cache/ (JSON, ~94 MB)
│   ├── Processing: refined_orbits.py, orrery_integration.py
│   ├── Visualization: planet_visualization.py + 14 shell modules
│   ├── Interface: palomas_orrery.py → plot_objects()
│   └── Output: 3D orrery, animations, planetary interiors, exoplanets
│
├── ⭐ Stellar Pipeline (15+ modules)
│   ├── Source: Gaia DR3, Hipparcos, SIMBAD
│   ├── Acquisition: data_acquisition.py, simbad_manager.py
│   ├── Cache: star_data/ (.vot & .pkl, 335+ MB)
│   ├── Processing: stellar_parameters.py, celestial_coordinates.py
│   ├── Visualization: visualization_3d.py, visualization_2d.py
│   ├── Interface: star_visualization_gui.py, hr_diagram_*.py
│   └── Output: 3D star maps, HR diagrams (123,000+ stars)
│
└── 🌍 Earth System Pipeline (3+ modules, growing)
    ├── Source: NOAA, NASA GISS, NSIDC, others
    ├── Acquisition: fetch_climate_data.py, fetch_paleoclimate_data.py
    ├── Cache: data/ (JSON climate files)
    ├── Processing: [minimal - direct to visualization]
    ├── Visualization: paleoclimate_visualization_*.py
    ├── Interface: earth_system_visualization_gui.py
    └── Output: 9 climate visualizations
        ├── CO₂ (Keeling Curve, 1958-2025)
        ├── Temperature anomalies (1880-2025)
        ├── Arctic sea ice extent (1979-2024)
        ├── Sea level rise (1880-2023)
        ├── Ocean acidification (1988-2023)
        ├── Planetary boundaries (2025)
        └── Paleoclimate (65 million years)
```

---

## Key Architectural Patterns

### Defense-in-Depth Cache Protection (Layer 3)

```
Cache Protection Strategy/
│
├── Multiple Validation Layers
│   ├── File size checks (prevent corruption)
│   ├── Percentage-based reduction checks
│   ├── Metadata validation
│   └── JSON/VOTable format validation
│
├── Atomic Operations
│   ├── Write to temporary files first
│   ├── Validate before replacing original
│   └── Rollback on failure
│
├── Backup Systems
│   ├── Automated backups (create_cache_backups.py)
│   ├── Timestamped backup copies
│   └── Protected data directories
│
└── Repair Mechanisms
    ├── verify_orbit_cache.py (automatic repair on load)
    ├── Rebuild .pkl from .vot caches
    └── Smart incremental updates
```

### Module Size Distribution

```
Modules by Layer/
│
├── Layer 5 (Viz Prep):     27 modules  ████████████████████████
├── Layer 4 (Processing):    8 modules  ███████
├── Layer 6 (UI):            8 modules  ███████
├── Layer 2 (Acquisition):   6 modules  █████
├── Layer 3 (Cache):         6 modules  █████
├── Layer 8 (Utils):         5 modules  ████
├── Layer 7 (Reporting):     3 modules  ██
└── Layer 9 (Config):        2 modules  █

Total: 72 active production modules
```

### Integration Architecture

```
System Integration/
│
├── Master Controller
│   └── palomas_orrery.py (8,289 lines)
│       ├── Three-column tkinter layout
│       ├── Object selection panels
│       ├── Control panels (date/time/animation/scale)
│       ├── Launches 3 specialized GUIs
│       └── Core visualization functions
│           ├── plot_objects() → static 3D plots
│           └── animate_objects() → time evolution
│
├── Cross-Cutting Support (Layers 8-9)
│   ├── constants_new.py → Feeds Layers 4-6
│   └── Utilities → Support Layers 5-10
│
└── Data Flow Checkpoints
    ├── Layer 1 → Layer 2: API rate limiting
    ├── Layer 2 → Layer 3: Cache validation
    ├── Layer 3 → Layer 4: Data integrity checks
    └── Layer 4 → Layer 5: Parameter validation
```

---

## Example Data Flows

### Mars Visualization (Typical Solar System Object)

```
User Action: Click "Mars" checkbox
    ↓
palomas_orrery.py (Layer 6)
    ↓
orbit_data_manager.py (Layer 2) → Check orbit_cache/
    ├─ Cache hit → Load from JSON
    └─ Cache miss → Query JPL Horizons
    ↓
orbit_cache/mars.json (Layer 3)
    ├─ Atomic save with validation
    └─ File size check
    ↓
refined_orbits.py (Layer 4)
    ├─ Calculate refined position
    └─ Apply perturbations
    ↓
planet_visualization.py (Layer 5)
    ├─ Prepare Mars orbit trace
    └─ mars_visualization_shells.py (if interior enabled)
    ↓
plot_objects() in palomas_orrery.py (Layer 6)
    ├─ Combine all planetary traces
    └─ Render with Plotly
    ↓
save_utils.py (Layer 8) → Export if requested
    ↓
Output: PNG or HTML file (Layer 10)

Total time: ~10-50 milliseconds (cached) or 1-2 seconds (fresh API call)
```

### HR Diagram Creation (Stellar Pipeline)

```
User Action: "Create HR diagram for stars within 50 light-years"
    ↓
star_visualization_gui.py (Layer 6)
    ↓
data_acquisition_distance.py (Layer 2)
    ├─ Check star_data/ cache
    └─ Query VizieR if needed (with rate limiting)
    ↓
vot_cache_manager.py (Layer 3)
    ├─ Save to .vot and .pkl formats
    ├─ Atomic save operations
    └─ Validation checks
    ↓
stellar_parameters.py (Layer 4)
    ├─ Calculate temperatures
    ├─ Estimate luminosities
    └─ Apply data patches
    ↓
visualization_2d.py (Layer 5)
    ├─ Prepare HR diagram data
    ├─ Temperature-based colors
    └─ Format hover text
    ↓
hr_diagram_distance.py (Layer 6)
    ├─ Create Plotly figure
    └─ Apply stellar classification overlays
    ↓
report_manager.py (Layer 7) → Generate statistics
    ↓
Output: Interactive HTML + JSON report (Layer 10)

Total time: ~100 milliseconds (cached) or 5-30 seconds (fresh query)
```

### Climate Data Update (Earth System Pipeline)

```
User Action: Click "Update CO₂ Data"
    ↓
earth_system_visualization_gui.py (Layer 6)
    ↓
fetch_climate_data.py (Layer 2)
    ├─ Query Scripps CO₂ Program
    └─ Rate limiting & error handling
    ↓
climate_cache_manager.py (Layer 3)
    ├─ Validate downloaded data
    ├─ Save to data/co2_mauna_loa_monthly.json
    └─ Atomic save with backup
    ↓
[Minimal processing at Layer 4]
    ↓
earth_system_visualization_gui.py (Layer 6)
    ├─ Create Keeling Curve visualization
    ├─ Add seasonal cycle annotation
    └─ Highlight 400+ ppm threshold
    ↓
Output: Interactive Plotly HTML (Layer 10)

Total time: ~1-3 seconds (depends on data source responsiveness)
```

---

## Architectural Benefits

✅ **Modularity** - New features integrate at appropriate layer without refactoring other layers

✅ **Defense-in-Depth** - Multi-layer cache validation prevents data corruption
   - Atomic saves
   - File size verification
   - Metadata validation
   - Automatic backups
   - Repair mechanisms

✅ **Scalability** - Each of the three pipelines can grow independently
   - Solar System: Add new objects, spacecraft, comets
   - Stellar: Expand catalog coverage, add new analyses
   - Earth System: Add climate variables, extend time series

✅ **Maintainability** - Clear layer boundaries make debugging straightforward
   - Each layer has single responsibility
   - Data flow is unidirectional (top to bottom)
   - Cross-cutting concerns isolated to Layers 8-9

✅ **Robustness** - Critical cache layer protects data integrity
   - 335+ MB of stellar data protected
   - 94 MB of orbit data protected
   - Climate time series preserved
   - Zero data loss in 6+ months of development

✅ **Testability** - Each layer can be validated independently
   - Layer 2: Test API queries in isolation
   - Layer 3: Verify cache operations
   - Layer 4: Test calculations with known inputs
   - Layer 5: Validate visualization preparation

---

## Future Growth Patterns

As the project evolves, the architecture naturally supports:

### Earth System Pipeline Expansion
- **Current:** 3 modules, 9 visualizations
- **Future:** May warrant dedicated Layer 4 processing modules as complexity grows
- **Pattern:** Climate data is simpler than orbital mechanics, so minimal processing currently

### Exoplanet System Growth
- **Current:** 3 systems, 11 planets
- **Future:** More systems can be added to Layer 5 (exoplanet_systems.py)
- **Pattern:** Self-contained in configuration, no new layer needed

### New Visualization Types
- **Future:** Spectroscopy, photometry, astrometry visualizations
- **Pattern:** Add modules to Layer 5, connect to existing pipelines

The 10-layer architecture accommodates growth without structural changes!

---

**For complete module details:** [MODULE_INDEX.md](MODULE_INDEX.md)

**For detailed documentation:** [README.md](README.md)

**For flowchart visualization:** [palomas_orrery_flowchart_v13_vertical.md](palomas_orrery_flowchart_v13_vertical.md)

---

*Architecture documented November 6, 2025*

*Paloma's Orrery - "Sky's the limit! Or stars are the limit!"*
