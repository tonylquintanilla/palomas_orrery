# Paloma's Orrery

**An Advanced Interactive Solar System and Stellar Visualization Suite**

A comprehensive Python application that creates stunning 3D visualizations of our solar system and stellar neighborhood. This tool combines NASA JPL Horizons data with Hipparcos/Gaia catalogs to provide unprecedented interactive astronomical visualizations.

## 🌟 Key Features

### Solar System Visualization
- **Real-time 3D positioning** of planets, moons, asteroids, and comets using NASA JPL Horizons data
- **Multi-scale visualization** from planetary cores to the Oort Cloud (126,000 AU)
- **Interactive animations** spanning minutes to years with customizable time steps
- **Comprehensive mission tracking** for 25+ space missions (Voyager, Cassini, Parker Solar Probe, etc.)
- **Detailed planetary shell systems** showing internal structure, atmospheres, and magnetospheres
- **Comet trajectory visualization** including famous comets like Halley, Hale-Bopp, and NEOWISE

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
- **Intelligent data caching** system for improved performance
- **Incremental orbit updates** to minimize processing time
- **Multi-threaded processing** with proper shutdown handling
- **Export capabilities** (HTML, PNG, SVG formats)
- **Professional hover information** with detailed astronomical data
- **Copy-to-clipboard** functionality for star names and coordinates

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

2. **Stellar Visualizations:**
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

### Core Modules

**`palomas_orrery.py`** - Main GUI application with comprehensive solar system controls
- Object selection interface with 200+ celestial bodies
- Animation controls (minutes to years)
- Scale management and center object selection
- Real-time JPL Horizons data integration

**`star_visualization_gui.py`** - Dedicated stellar visualization interface
- Star search functionality across multiple catalogs
- Distance and magnitude-based filtering
- Interactive parameter controls

**Visualization Engines:**
- `visualization_3d.py` - 3D stellar neighborhood rendering
- `visualization_2d.py` - Hertzsprung-Russell diagram generation
- `planet_visualization.py` - Planetary shell system rendering
- `solar_visualization_shells.py` - Solar structure visualization

**Data Pipeline:**
- `data_acquisition.py` - Multi-catalog stellar data fetching
- `data_processing.py` - Coordinate transformations and filtering
- `star_properties.py` - SIMBAD database integration
- `stellar_parameters.py` - Temperature and luminosity calculations

**Infrastructure:**
- `orbit_data_manager.py` - Intelligent orbit caching system
- `shutdown_handler.py` - Thread-safe application management
- `save_utils.py` - Export functionality
- `messier_object_data_handler.py` - Non-stellar object integration

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

### Data Cache Management
- **VOTable files** (.vot): Raw catalog data (30KB to 300MB)
- **Pickle files** (.pkl): Processed star properties (1MB to 12MB)
- **JSON files**: Orbit path data with incremental updates
- **Automatic refresh**: Weekly updates recommended

## 🎨 Visualization Features

### Interactive Controls
- **Multi-level zoom**: From planetary surfaces to galactic scales
- **Time animation**: Customizable step sizes and frame counts
- **Camera presets**: Navigate to notable stars and objects
- **Hover information**: Detailed astronomical data on mouse-over
- **Legend toggles**: Show/hide object categories
- **Export options**: HTML, PNG, SVG formats

### Scientific Accuracy
- **Proper coordinate systems**: ICRS alignment with celestial sphere
- **Realistic scaling**: True relative sizes and distances
- **Temperature visualization**: Black-body radiation color mapping
- **Orbital mechanics**: Kepler's laws implementation
- **Light-time corrections**: Accurate positions for observation dates

## 🔧 Configuration Options

### Solar System Plotting
```python
# Interval controls for orbit resolution
comet_interval_divisor = 100      # Comet trajectory points
mission_interval_divisor = 75     # Space mission paths  
planet_interval_divisor = 50      # Planet orbit detail
satellite_orbit_days = 56         # Moon observation period
```

### Stellar Visualization
```python
# Scale and magnitude limits
max_distance_ly = 100             # Maximum distance filter
max_apparent_magnitude = 9.0      # Naked-eye limit
temperature_range = (1300, 50000) # Color mapping bounds
```

## 📈 Performance Optimization

### Initial Setup (First Run)
- **Data fetching**: 2-5 minutes for complete catalogs
- **Property caching**: 1-3 minutes for SIMBAD queries
- **Index generation**: 30-60 seconds for search optimization

### Subsequent Sessions
- **Application launch**: 5-10 seconds from cache
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

### Orbit Data Management
The system includes intelligent orbit caching with incremental updates:
```python
# Automatic detection of outdated orbit data
# Selective updates for only changed objects
# Time-based expiration with configurable thresholds
# Backup and recovery for data integrity
```

### Multi-threaded Architecture  
- **Background data fetching** without GUI blocking
- **Thread-safe visualization** rendering
- **Graceful shutdown** handling with cleanup
- **Memory management** for large datasets

### Professional Export Pipeline
- **Publication-quality** static images
- **Interactive HTML** with full functionality  
- **Batch processing** for animation sequences
- **Custom templates** for presentations

## 🐛 Troubleshooting

### Common Issues

**Slow Initial Loading:**
- Ensure stable internet connection
- Check firewall settings for astroquery
- Verify disk space (2GB minimum)

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
rm *.vot *.pkl orbit_paths.json

# Clear only stellar data
rm star_properties_*.pkl

# Clear only orbital data  
rm orbit_paths.json
```

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

*Last updated: May 2025*  
*Version: 2.0.0*  
*Python compatibility: 3.8+*