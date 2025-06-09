# Paloma's Orrery

**An Advanced Interactive Solar System and Stellar Visualization Suite**

A comprehensive Python application that creates stunning 3D visualizations of our solar system and stellar neighborhood. This tool combines NASA JPL Horizons data with Hipparcos/Gaia catalogs to provide unprecedented interactive astronomical visualizations.

## 🌟 Key Features

### Dual-Pipeline Architecture
Paloma's Orrery employs a sophisticated dual-pipeline architecture that processes astronomical data through two specialized pathways:

**🌟 Solar System Pipeline**: JPL Horizons ephemeris data → intelligent orbit management → planet visualization → animated solar system plots
**⭐ Stellar Pipeline**: Star catalog data → stellar parameter calculation → 3D/2D visualization → interactive stellar maps and HR diagrams

### Solar System Visualization
- **Real-time 3D positioning** of planets, moons, asteroids, and comets using NASA JPL Horizons data
- **Multi-scale visualization** from planetary cores to the Oort Cloud (126,000 AU)
- **Interactive animations** spanning minutes to years with customizable time steps
- **Comprehensive mission tracking** for 25+ space missions (Voyager, Cassini, Parker Solar Probe, etc.)
- **Detailed planetary shell systems** showing internal structure, atmospheres, and magnetospheres
- **Comet trajectory visualization** including famous comets like Halley, Hale-Bopp, and NEOWISE
- **Time-varying lunar orbit model** with perturbations for accurate Moon positioning

### Stellar Neighborhood Mapping
- **3D stellar maps** up to 100 light-years from the Sun
- **Magnitude-limited views** showing stars visible to the naked eye (magnitude ≤ 9)
- **Temperature-based color coding** using black-body radiation (1,300K to 50,000K)
- **Interactive camera controls** with notable star navigation
- **Messier object integration** including nebulae, star clusters, and galaxies

### Hertzsprung-Russell Diagrams
- **Interactive 2D stellar classification** plots
- **Spectral type overlays** (O, B, A, F, G, K, M, L classes)
- **Luminosity vs. temperature analysis** with stellar evolution insights
- **Comprehensive data integration** from multiple astronomical catalogs

### Advanced Features
- **Smart selective caching** system that only updates selected objects
- **Special fetch mode** for experimental plotting without cache modification
- **Automatic cache backup** on startup with single backup file
- **Weekly cache cleanup** removing data older than 30 days
- **Multi-threaded processing** with proper shutdown handling
- **Export capabilities** (HTML, PNG, SVG formats plus JSON, VOTable, Pickle data files)
- **Professional hover information** with detailed astronomical data
- **Copy-to-clipboard** functionality for star names and coordinates
- **Time-varying lunar orbit model** with perturbations for accurate Moon positioning

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 8GB+ RAM recommended for full magnitude range
- Active internet connection for initial data fetching

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/palomas_orrery.git
cd palomas_orrery
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Launch the application:**
```bash
python palomas_orrery.py
```

## 📋 System Requirements

### Core Dependencies
```
numpy>=1.24.0          # Numerical computations
pandas>=2.0.0          # Data manipulation
plotly>=5.18.0         # Interactive visualizations
astropy>=5.3.4         # Astronomical calculations
astroquery>=0.4.6      # Catalog queries
astropy-healpix>=0.7   # Sky tessellation
kaleido>=0.2.1         # Static image export
```

### Optional but Recommended
```
scipy>=1.11.0          # Scientific computing
matplotlib>=3.7.0      # Additional plotting
jupyter>=1.0.0         # Notebook support
ipython>=8.12.0        # Enhanced interactive shell
```

## 🎯 Usage Guide

### Main Interface (`palomas_orrery.py`)

1. **Solar System Visualization:**
   - Select objects from the comprehensive scrollable menu
   - Choose visualization date and time (UTC)
   - Select center object (Sun, planets, moons, or asteroids)
   - Configure scale (Auto or Manual in AU)
   - Generate static plots or animations

2. **Cache Management (New in v2.0):**
   - **No startup dialogs** - application launches immediately
   - **Selective updates** - only selected objects are updated when plotting
   - **Special fetch mode** - experiment with different parameters without affecting cache
   - **Automatic maintenance** - weekly cleanup of old data

3. **Stellar Visualizations:**
   - Launch `star_visualization_gui.py` from the main interface
   - Choose distance-based (up to 100 ly) or magnitude-based (up to mag 9) views
   - Generate 3D stellar maps or 2D HR diagrams

### Command Line Tools

**3D Stellar Distance Visualization:**
```bash
python planetarium_distance.py 50  # Stars within 50 light-years
```

**3D Magnitude-Limited Visualization:**
```bash
python planetarium_apparent_magnitude.py 4.5  # Stars brighter than magnitude 4.5
python planetarium_apparent_magnitude.py 6 1000  # With manual scale of 1000 ly
```

**Hertzsprung-Russell Diagrams:**
```bash
python hr_diagram_distance.py 25     # HR diagram for stars within 25 ly
python hr_diagram_apparent_magnitude.py 5  # HR diagram for stars brighter than mag 5
```

## 🏗️ Architecture Overview

### Dual-Pipeline Data Flow

Paloma's Orrery employs a sophisticated dual-pipeline architecture that processes solar system and stellar data through separate but coordinated pathways:

**Solar System Pipeline**: External data sources (JPL Horizons) → Data acquisition → Orbit data management → Solar visualization processing → Solar plot functions (plot_objects, animate_objects)

**Stellar Pipeline**: External data sources (Hipparcos, Gaia, SIMBAD) → Data acquisition → Data processing → Parameter calculation & selection → Stellar visualization processing → Stellar plot functions (create_3d_visualization, create_hr_diagram)

### Core Modules

**`palomas_orrery.py`** - Main GUI application with comprehensive solar system controls
- Object selection interface with 200+ celestial bodies
- Animation controls (minutes to years)
- Scale management and center object selection
- Real-time JPL Horizons data integration
- **New**: Smart cache management with selective updates

**`star_visualization_gui.py`** - Dedicated stellar visualization interface
- Star search functionality across multiple catalogs
- Distance and magnitude-based filtering
- Interactive parameter controls

**Visualization Engines:**
- `visualization_3d.py` - 3D stellar neighborhood rendering
- `visualization_2d.py` - Hertzsprung-Russell diagram generation
- `planet_visualization.py` - Planetary shell system rendering
- `solar_visualization_shells.py` - Solar structure visualization
- **`idealized_orbits.py`** - Orbital mechanics and ideal orbit plotting
  - Standard Keplerian orbit calculations
  - Special Moon orbit model with time-varying elements
  - Perturbation calculations for realistic lunar motion

**Data Pipeline:**
- `data_acquisition.py` / `data_acquisition_distance.py` - Multi-catalog stellar data fetching
- `data_processing.py` - Coordinate transformations and filtering
- `star_properties.py` - SIMBAD database integration
- `stellar_parameters.py` - Temperature and luminosity calculations

**Infrastructure:**
- `orbit_data_manager.py` - Intelligent orbit caching system with selective updates
- `shutdown_handler.py` - Thread-safe application management
- `save_utils.py` - Export functionality (plots and data files)
- `messier_object_data_handler.py` - Non-stellar object integration

## 📦 Module Reference

### Core Application Modules

**`catalog_selection.py`** - Star selection and filtering logic for distance and magnitude-based queries

**`constants_new.py`** - Physical constants, astronomical parameters, and object type mappings

**`data_acquisition.py`** - Stellar data fetching from Hipparcos, Gaia, and SIMBAD catalogs (magnitude-based)

**`data_acquisition_distance.py`** - Stellar data fetching optimized for distance-based queries

**`data_processing.py`** - Coordinate transformations, unique ID generation, and stellar data preprocessing

**`earth_visualization_shells.py`** - Create planetary structure shells.

**`eris_visualization_shells.py`** - Create planetary structure shells.

**`formatting_utils.py`** - Text formatting utilities for numerical values and hover text display

**`hr_diagram_apparent_magnitude.py`** - Command-line tool for generating H-R diagrams based on apparent magnitude

**`hr_diagram_distance.py`** - Command-line tool for generating H-R diagrams based on distance limits

**`idealized_orbits.py`** - Orbital mechanics calculations and idealized orbit plotting, including time-varying Moon orbit model

**`jupiter_visualization_shells.py`** - Create planetary structure shells.

**`mars_visualization_shells.py`** - Create planetary structure shells.

**`mercury_visualization_shells.py`** - Create planetary structure shells.

**`messier_catalog.py`** - Catalog of selected Messier objects and location data.

**`messier_object_data_handler.py`** - Integration and processing of Messier catalog deep-sky objects

**`moon_visualization_shells.py`** - Create planetary structure shells.

**`neptune_visualization_shells.py`** - Create planetary structure shells.

**`orbit_data_manager.py`** - Intelligent JPL Horizons data caching with selective updates and automatic cleanup

**`palomas_orrery.py`** - Main GUI application for solar system visualization and animation controls

**`palomas_orrery_helpers.py`** - Helper functions directly called into palomas_orrery.py.

**`planet_visualization.py`** - Planetary shell system rendering with internal structure visualization

**`planet9_visualization_shells.py`** - Create planetary structure shells.

**`planetarium_apparent_magnitude.py`** - Command-line 3D stellar visualization tool using apparent magnitude limits

**`planetarium_distance.py`** - Command-line 3D stellar visualization tool using distance limits

**`pluto_visualization_shells.py`** - Create planetary structure shells.

**`saturn_visualization_shells.py`** - Create planetary structure shells.

**`save_utils.py`** - Export functionality for plots and structured data files (PNG, HTML, JSON, VOTable, Pickle)

**`shared_utilities.py`** - Shared functions.

**`shutdown_handler.py`** - Thread-safe application shutdown and cleanup management

**`solar_visualization_shells.py`** - Solar structure visualization with detailed shell system rendering

**`star_notes.py`** - Educational content and unique notes for notable stars and astronomical objects

**`star_properties.py`** - SIMBAD database integration for stellar property queries and caching

**`star_visualization_gui.py`** - Dedicated GUI for stellar neighborhood exploration with search functionality

**`stellar_parameters.py`** - Temperature and luminosity calculations using spectral types and photometric data

**`uranus_visualization_shells.py`** - Create planetary structure shells.

**`venus_visualization_shells.py`** - Create planetary structure shells.

**`visualization_2d.py`** - Hertzsprung-Russell diagram generation with interactive stellar classification

**`visualization_3d.py`** - 3D stellar neighborhood rendering with magnitude and temperature visualization

**`visualization_core.py`** - Core visualization utilities shared between 2D and 3D stellar plotting modules

**`visualization_utils.py`** - GUI utilities including scrollable frames, tooltips, clipboard support, and star search functionality

## 📊 Data Sources & Processing

### Astronomical Catalogs
- **JPL Horizons System**: Real-time solar system positions
- **Hipparcos Catalog**: 118,218 high-precision stellar positions
- **Gaia DR3**: 1.8 billion stellar measurements
- **SIMBAD Database**: Comprehensive stellar properties
- **Messier Catalog**: Deep-sky objects and nebulae

### Photometric Systems
The application handles multiple photometric standards:

**Hipparcos (Johnson-Cousins System):**
- Direct V magnitudes for stars ≤ mag 4.0
- B-V color indices for temperature estimation
- High precision for bright stars

**Gaia (Native Photometry):**
- G, BP, RP band measurements
- V magnitude estimation: `V = G - correction_factor(BP-RP)`
- Used for stars > mag 4.0 to avoid duplicates

### Data Cache Management (Enhanced in v2.0)
- **Automatic backup**: `orbit_paths_backup.json` created on startup
- **Selective caching**: Only selected objects are updated
- **Special fetch mode**: Temporary cache for experimentation
- **Weekly cleanup**: Automatic removal of data older than 30 days
- **Multi-line status display**: Color-coded operation history
- **JSON files**: Orbit path data with metadata tracking

## 🎨 Visualization Features

### Interactive Controls
- **Multi-level zoom**: From planetary surfaces to galactic scales
- **Time animation**: Customizable step sizes and frame counts
- **Camera presets**: Navigate to notable stars and objects
- **Hover information**: Detailed astronomical data on mouse-over
- **Legend toggles**: Show/hide object categories
- **Export options**: HTML, PNG, SVG formats plus structured data files

### Scientific Accuracy
- **Proper coordinate systems**: ICRS alignment with celestial sphere
- **Realistic scaling**: True relative sizes and distances
- **Temperature visualization**: Black-body radiation color mapping
- **Orbital mechanics**: Kepler's laws implementation
- **Light-time corrections**: Accurate positions for observation dates
- **Moon orbit modeling**: Time-varying elements with solar perturbations
  - Evection: Primary perturbation due to Sun's gravity
  - Secular variations: Node regression and apsidal precession
  - Dynamic eccentricity: Varies between 0.026 and 0.077

## 🔧 Configuration Options

### Solar System Plotting
```python
# Interval controls for orbit resolution
comet_interval_divisor = 100      # Comet trajectory points
mission_interval_divisor = 75     # Space mission paths  
planet_interval_divisor = 50      # Planet orbit detail
satellite_orbit_days = 56         # Moon observation period
```

### Orbit Path Fetching Controls (New)
- **Start/End date offsets**: Dynamic date displays showing calculated dates
- **Interval settings**: Customizable for different object types
- **Special fetch mode**: Cyan-highlighted controls for experimental fetches
- **Center-aware**: Settings apply to selected center object

### Stellar Visualization
```python
# Scale and magnitude limits
max_distance_ly = 100             # Maximum distance filter
max_apparent_magnitude = 9.0      # Naked-eye limit
temperature_range = (1300, 50000) # Color mapping bounds
```

## 📈 Performance Optimization

### Initial Setup (First Run)
- **No startup delays**: Application launches immediately
- **On-demand fetching**: Data retrieved only when needed
- **Selective updates**: Only selected objects are processed

### Subsequent Sessions
- **Application launch**: 2-5 seconds from cache
- **Plot generation**: 2-5 seconds typical
- **Animation frames**: 200-500ms per frame
- **Interactive updates**: <100ms response time

### Memory Usage by Scope
- **Distance 25 ly**: ~50MB RAM
- **Distance 100 ly**: ~200MB RAM  
- **Magnitude 4**: ~100MB RAM
- **Magnitude 6**: ~500MB RAM
- **Magnitude 9**: ~2GB RAM

## ⚙️ Advanced Features

### Smart Cache Management (New in v2.0)
The system includes intelligent orbit caching with selective updates:
```python
# Only updates selected objects when plotting
# Dialog asks user preference with "remember choice" option
# Special fetch mode for experimentation without cache pollution
# Automatic weekly cleanup of data older than 30 days
# Single backup file maintained for safety
```

### Moon Orbit Model (New in v2.0)
Enhanced lunar orbit calculations with time-varying elements:
```python
# Calculates Moon's position using:
# - Base orbital elements (a=0.00257 AU, e=0.0549, i=5.145°)
# - Secular variations:
#   - Node regression: -19.341°/century (18.6 year cycle)
#   - Apsidal precession: +40.690°/century (8.85 year cycle)
# - Major perturbations:
#   - Evection: ±0.01098 eccentricity variation
#   - Annual equation: ±0.00048 eccentricity variation
# - Dynamic date-based calculations for any selected time
```

The Moon's idealized orbit now accurately reflects:
- Proper inclination to the ecliptic plane (~5.145°)
- Time-varying eccentricity (0.026 to 0.077)
- Nodal regression and apsidal advance
- Solar gravitational perturbations

This ensures the Moon's plotted position closely matches ephemeris data for any date.

### Multi-threaded Architecture  
- **Background data fetching** without GUI blocking
- **Thread-safe visualization** rendering
- **Graceful shutdown** handling with cleanup
- **Memory management** for large datasets

### Professional Export Pipeline
- **Publication-quality** static images (PNG, SVG)
- **Interactive HTML** with full functionality  
- **Structured data export** (JSON, VOTable, Pickle formats)
- **Batch processing** for animation sequences
- **Custom templates** for presentations

## 🐛 Troubleshooting

### Common Issues

**No More Midnight Update Delays (Fixed in v2.0):**
- System now only updates selected objects
- No automatic full cache updates
- Center changes don't trigger mass updates

**Memory Errors with High Magnitudes:**
- Reduce magnitude limit (try 6 instead of 9)
- Close other applications
- Consider 64-bit Python installation

**Missing Star Data:**
- Clear cache files in project directory
- Restart application to refresh SIMBAD connection
- Check for astroquery version compatibility

**Visualization Performance:**
- Use manual scaling for very large distances
- Reduce animation frame counts for smoother playback
- Enable hardware acceleration in browser

### Cache Management
```bash
# Clear all cached data
rm orbit_paths.json

# Restore from backup
cp orbit_paths_backup.json orbit_paths.json

# Clear temporary cache
rm orbit_paths_temp.json

# View cache statistics
# Check terminal output on startup for detailed cache info
```

### New Status Display
The application now features a 3-line status display showing:
- Current operation with color coding (green=success, blue=special, red=error)
- Previous two operations with timestamps
- Reference to terminal for detailed information

## 🤝 Contributing

### Development Setup
1. **Fork the repository** and create a feature branch
2. **Install development dependencies**: `pip install -r requirements-dev.txt`
3. **Run tests**: `python -m pytest tests/`
4. **Follow PEP 8** style guidelines
5. **Add documentation** for new features

### Code Structure Guidelines
- **Modular design**: Separate concerns into focused modules
- **Type hints**: Use for all function signatures
- **Error handling**: Comprehensive exception management
- **Documentation**: Docstrings for all public functions
- **Testing**: Unit tests for core functionality

### Feature Requests
Popular enhancement requests:
- **Additional catalog integration** (2MASS, WISE)
- **Exoplanet visualizations**
- **Variable star light curves**
- **Binary star orbital mechanics**
- **Galaxy structure mapping**
- ~~**Improved lunar orbit model**~~ ✓ Implemented in v2.0

## 📜 License & Attribution

### License
This project is licensed under the **MIT License with Non-Commercial Use Restriction**.

**Free for:**
- Academic research and education
- Personal astronomical exploration  
- Non-profit educational institutions
- Open source contributions

**Commercial use requires written permission** from the author.

### Data Source Credits
- **NASA/JPL-Caltech**: Horizons System ephemeris data
- **ESA/Hipparcos**: High-precision stellar astrometry
- **ESA/Gaia/DPAC**: Revolutionary stellar catalog
- **CDS, Strasbourg**: SIMBAD astronomical database
- **SEDS**: Messier catalog compilation

### Acknowledgments
Created by **Tony Quintanilla** with assistance from advanced AI systems (ChatGPT, Claude, Gemini, DeepSeek).

Special thanks to:
- NASA for open access to JPL Horizons
- ESA for the transformative Hipparcos and Gaia missions
- The astronomical community for open data sharing
- Python scientific computing ecosystem maintainers

---

## 📞 Contact & Support

**Author**: Tony Quintanilla  
**Email**: tonyquintanilla@gmail.com  
**Project Website**: [Paloma's Orrery](https://sites.google.com/view/tony-quintanilla)
**GitHub page**: [Paloma's Orrery](https://tonylquintanilla.github.io/palomas_orrery/)

**For support:**
- Create an issue on GitHub
- Check the troubleshooting section
- Review existing documentation

**For commercial licensing:**
- Contact author directly
- Include intended use case
- Specify distribution requirements

---

*Last updated: June 6, 2025*  
*Version: 2.0.0*  
*Python compatibility: 3.8+*

### Version History
- **v2.0.0** (December 2024)
  - Added smart selective cache management
  - Implemented time-varying Moon orbit model with perturbations
  - Removed startup dialogs for faster launch
  - Added weekly automatic cache cleanup
  - Enhanced orbit accuracy for all dates