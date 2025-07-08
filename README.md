# 🌌 Paloma's Orrery

## A Journey Through Space and Time

Paloma's Orrery is an advanced astronomical visualization software that brings the cosmos to your desktop. This comprehensive tool transforms complex astronomical data into stunning, interactive visualizations of our solar system and stellar neighborhood. The visualizations are created with a Python program with the assistance of AI assistants, including Claude, ChatGPT, Gemini and DeepSeek.

Created by a civil and environmental engineer with a passion for space exploration, Paloma's Orrery bridges the gap between scientific accuracy and visual beauty, making astronomy accessible to educators, students, and space enthusiasts worldwide. 

## ✨ What Makes It Special

### Scientific Accuracy Meets Visual Beauty
- **Real astronomical data** from NASA JPL Horizons, ESA Hipparcos/Gaia, and SIMBAD databases
- **Scientifically accurate Oort Cloud modeling** with new Hills Cloud, clumpy distributions, and galactic tide effects
- **Time-accurate positioning** for planets, moons, asteroids, comets, and spacecraft from 1800-2200 CE
- **Stellar neighborhood mapping** with accurate 3D positioning for 118,000+ stars from Hipparcos and Gaia catalogs
- **Intelligent cache management** with selective updates and automatic data cleanup
- **Enhanced orbital mechanics** with refined satellite orbits using JPL Horizons ephemeris corrections

### Advanced Features & Intelligent Data Management
- **Smart selective caching** system with intelligent updates - only fetches data for selected objects, avoiding unnecessary requests
- **Special fetch mode** for experimental plotting without cache modification
- **Automatic cache backup** on startup with weekly cleanup of data older than 30 days
- **Cache validation and repair** system that automatically detects and fixes corrupted data entries
- **Multi-threaded processing** with proper shutdown handling
- **Export capabilities** (HTML, PNG, SVG formats plus JSON, VOTable, Pickle data files)
- **Professional hover information** with detailed astronomical data
- **Copy-to-clipboard** functionality for star names and coordinates
- **Animation and Time Travel** - watch cosmic motions across timescales from minutes to years

## 🏗️ Architecture Overview

### Technical Innovation

**Data Integration**: The software seamlessly integrates data from multiple authoritative sources:
- **NASA JPL Horizons**: Real-time solar system ephemeris data
- **ESA Hipparcos**: High-precision positions for bright stars (118,218 stars)
- **ESA Gaia DR3**: Revolutionary stellar census data for 1.8 billion stars
- **SIMBAD Database**: Comprehensive stellar properties and classifications
- **Messier Catalog**: Deep-sky objects including nebulae, star clusters, and galaxies

**Smart Processing Pipeline**: Raw astronomical data undergoes sophisticated processing through specialized modules. The solar system pipeline handles orbit caching with selective updates and Planet 9 synthesis, while the stellar pipeline manages coordinate transformations, spectral classification, and multi-catalog cross-matching.

### Advanced Oort Cloud Modeling
The enhanced Oort Cloud visualization represents a significant advancement in astronomical software, incorporating:
- **Formation Physics**: The visualization reflects actual formation mechanisms - planetesimal scattering by giant planets, galactic tidal sculpting, and ongoing modification by stellar encounters
- **Observational Constraints**: Recent discoveries of inner Oort Cloud objects like Sedna provide direct evidence for the complex structure
- **Computational Validation**: Models incorporate results from N-body simulations showing how the original spherical population has been sculpted into the structured system observed today

### System Architecture & Data Flow

**Interactive Flowchart**: Explore the complete system architecture and data flow through our interactive Mermaid flowchart:
**[📊 Paloma's Orrery System Architecture Flowchart](https://www.mermaidchart.com/app/projects/780c7ec0-84a7-4e38-9e06-9bbfdd985750/diagrams/cc451fa5-5fc2-497b-ab37-56813ad4620c/version/v0.1/edit)**

This comprehensive flowchart visualizes:
- **Dual-pipeline architecture** with solar system and stellar processing pathways
- **Data source integration** from JPL Horizons, Hipparcos, Gaia, and SIMBAD
- **Refined orbit system** with enhanced satellite positioning capabilities
- **Module interconnections** showing how 50+ Python modules work together
- **Output generation** paths for visualizations and data exports
- **Interactive navigation** with clickable elements and detailed module descriptions

## 🚀 Recent Improvements (July 2025)

### Enhanced GUI and User Experience
1. **Reorganized orbit data fetching interface**:
   - Clear separation between cache management and fetch operations
   - New "Fetch Special" mode for experimental plotting without affecting main cache
   - Improved status display showing operation type and progress
   - Color-coded status messages (blue for cache ops, purple for special fetch)

2. **Streamlined cache update process**:
   - Removed repetitive update dialogs
   - "Remember my choice" option for session-wide preferences
   - Selective object fetching - only downloads data for selected objects
   - Clear indication of which objects need updates

3. **Advanced interval controls**:
   - Separate interval settings for different object types
   - Fine-grained control: planets (1d-7d), satellites (1h-24h), comets (1h-7d)
   - Custom intervals for eccentric orbits
   - Intelligent defaults based on object characteristics

### Robust Cache Management System
1. **Cache validation and repair**:
   - Automatic detection of corrupted JSON entries
   - Graceful handling of mixed format data (old array-based vs new time-indexed)
   - Automatic backup creation before repairs
   - Detailed repair logs showing what was fixed

2. **Safety mechanisms**:
   - Prevention of accidental overwrites (won't save tiny data over large files)
   - Atomic file operations using temporary files
   - Emergency backup creation for suspicious operations
   - Automatic format conversion for legacy data

3. **Testing infrastructure**:
   - Comprehensive test suite with 13+ tests for cache operations
   - Isolated test environment preventing main file corruption
   - Tests for corruption handling, format conversion, and incremental updates

## 📁 File Status & Integration

### Core Components

**`orbit_data_manager.py`** ✅ **CRITICAL MODULE**
- **Core functionality**: Manages all orbit data caching and JPL Horizons integration
- **Recent enhancements**:
  - Safe save mechanism with size checks
  - Automatic corruption detection and repair
  - Support for both old and new data formats
  - Incremental update capabilities
  - Proper error handling and backup creation

**`test_orbit_cache.py`** ✅ **NEW TEST SUITE**
- Comprehensive testing for cache functionality
- Isolated test environment in `test_output/` directory
- Tests corruption handling, format conversion, and updates
- Ensures cache reliability and data integrity

**`verify_orbit_cache.py`** ✅ **NEW UTILITY**
- Safe verification tool for orbit cache health
- Creates timestamped backups before verification
- Reports statistics on cache contents
- Optional repair mode for corrupted entries

## 🚀 Installation & Quick Start

### Requirements
```bash
# Core dependencies
pip install numpy scipy matplotlib plotly
pip install astropy astroquery jplephem skyfield
pip install pandas pillow kaleido tenacity

# GUI framework
pip install tkinter  # Usually comes with Python

# Optional for enhanced features
pip install pickle  # For data serialization
```

### Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   cd palomas_orrery
   ```

2. **Verify your orbit cache** (recommended after updates):
   ```bash
   python verify_orbit_cache.py
   ```

3. **Launch the main application**:
   ```bash
   python palomas_orrery.py
   ```

## 🎮 Using Paloma's Orrery

### Main Interface Navigation

1. **Object Selection:**
   - Browse through categorized celestial objects
   - Use checkboxes to select objects for plotting
   - Special categories: Planets, Moons, Asteroids, Comets, Spacecraft, etc.

2. **Cache Management:**
   - **Update Cache**: Refreshes data for all objects (use sparingly)
   - **Incremental Update**: Extends existing data to new dates
   - **Fetch Special**: Experimental mode - doesn't affect main cache
   - **Cache Info**: Shows current cache statistics

3. **Plot Controls:**
   - **Plot Selected**: Creates visualization with selected objects
   - **Remember Update Choice**: Avoid repetitive dialogs
   - **Interval Controls**: Adjust trajectory resolution by object type

4. **Time Controls:**
   - Date selector for any moment from 1800-2200 CE
   - Animation controls with adjustable speed
   - "Animate Birthdays" for special date sequences

### Performance Tips

1. **First Run**: 
   - Start with a small selection of objects
   - The cache builds incrementally as you use the software

2. **Optimal Usage**:
   - Use "Fetch Special" for experiments
   - Select only objects you need to plot
   - Use coarser intervals for long time spans

3. **Cache Maintenance**:
   - Automatic weekly cleanup removes old data
   - Run `verify_orbit_cache.py` if you suspect issues
   - Backups are created automatically

## 🔧 Configuration & Customization

### Interval Settings
```python
# In palomas_orrery.py - Adjust default intervals
default_intervals = {
    'planet': '1d',          # Daily positions for planets
    'satellite': '2h',       # 2-hour intervals for moons
    'comet': '6h',          # 6-hour intervals for comets
    'spacecraft': '1d',      # Daily for spacecraft
    'asteroid': '1d'         # Daily for asteroids
}
```

### Cache Settings
```python
# In orbit_data_manager.py
CACHE_CLEANUP_DAYS = 30     # Days to keep old data
CACHE_UPDATE_THRESHOLD = 7   # Days before suggesting update
```

## 📊 Module Architecture

### Data Pipeline Modules
- **`orbit_data_manager.py`**: Intelligent JPL Horizons caching with validation
- **`data_acquisition.py`**: Stellar data from Hipparcos/Gaia
- **`data_processing.py`**: Coordinate transformations and preprocessing
- **`star_properties.py`**: SIMBAD integration for stellar properties

### Visualization Engines
- **`palomas_orrery.py`**: Main GUI and solar system visualization
- **`star_visualization_gui.py`**: Stellar neighborhood explorer
- **`visualization_3d.py`**: 3D stellar rendering
- **`visualization_2d.py`**: HR diagram generation
- **`planet_visualization.py`**: Planetary structure visualization

### Support Infrastructure
- **`test_orbit_cache.py`**: Comprehensive cache testing
- **`verify_orbit_cache.py`**: Cache health verification
- **`shutdown_handler.py`**: Clean application termination
- **`save_utils.py`**: Export functionality

## 🌟 Future Development

Planned enhancements include:
- Integration of James Webb Space Telescope discoveries
- Exoplanet system visualizations
- Gravitational wave source mapping
- Enhanced spacecraft trajectory planning tools
- Real-time satellite tracking integration
- Variable star light curve analysis
- Binary system orbital mechanics

## 🎭 The Human Touch

While built on rigorous astronomical data and sophisticated algorithms, Paloma's Orrery never loses sight of the human element in space exploration. Every spacecraft has a story, every star has unique characteristics, and every celestial dance unfolds according to the same physical laws that govern our daily lives.

The recent GUI improvements exemplify this philosophy - instead of forcing users through repetitive dialogs, the software now remembers preferences and provides clear, color-coded feedback. The cache system protects valuable data while allowing experimentation, and the testing infrastructure ensures reliability.

## 🌐 Resources

### Visual Gallery
Visit **[Paloma's Orrery Website](https://sites.google.com/view/tony-quintanilla)** for stunning visualization examples

### Video Tutorials
Watch demonstrations on the **[YouTube Playlist](https://www.youtube.com/playlist?list=PLEGbeeSDrKst8837R5builvhDlTs7Shpm)**

### Source Code
Complete code available on **[GitHub](https://github.com/tonylquintanilla/palomas_orrery)**

### Community
- Report issues on GitHub
- Share your visualizations
- Contribute improvements

---

*"The cosmos is within us. We are made of star-stuff. We are a way for the universe to know itself."* - Carl Sagan

Paloma's Orrery: Making the universe accessible, one visualization at a time. 🌌