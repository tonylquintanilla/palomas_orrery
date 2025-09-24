# Paloma's Orrery

An advanced astronomical visualization tool that transforms NASA/ESA data into interactive 3D and 2D visualizations of the solar system and stellar neighborhood.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Architecture](#architecture)
6. [Module Reference](#module-reference)
7. [Data Files](#data-files)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Overview

Paloma's Orrery combines scientific accuracy with visual beauty, making astronomy accessible to students, educators, and space enthusiasts. Created by civil & environmental engineer Tony Quintanilla.

**Key Capabilities:**
- Real-time planetary and spacecraft positions from JPL Horizons
- Interactive 3D solar system with 100+ objects
- Stellar neighborhood mapping (123,000+ stars)
- Planetary interior visualizations
- HR diagrams and stellar analysis

**Resources:**
- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery)
- [Project Website](https://tonylquintanilla.github.io/palomas_orrery/)
- [Video Tutorials](https://www.youtube.com/@tony_quintanilla/featured)
- Contact: tonyquintanilla@gmail.com

## Installation

### Prerequisites
- Windows 10/11 
- Python 3.8+ (tested with 3.13)
- 300MB free disk space
- Internet connection

### Quick Start

1. **Install Python**
   - Download from [python.org](https://www.python.org/downloads/)
   - Check "Add Python to PATH" during installation
   - Verify: `python --version`

2. **Download Orrery**
   ```bash
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   cd palomas_orrery
   ```
   Or download ZIP from GitHub and extract.

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install numpy pandas scipy
   pip install astropy astroquery
   pip install plotly pillow kaleido==0.2.1
   pip install customtkinter
   pip install requests beautifulsoup4 python-dateutil pytz
   ```

4. **Run Program**
   ```bash
   python palomas_orrery.py
   ```

### First Run Notes
- Cache files are included! Download cache_files_compressed.zip from GitHub Releases
- Extract the cache zip to your project folder - contains all large .json, .vot, and .pkl files
- No initial cache generation needed - star visualizations work immediately
- The program will only fetch new data when you select objects not in the cache

## Usage

### Basic Operations

**Plotting Objects:**
1. Select objects from checkboxes
2. Set date and time
3. Click "Plot Entered Date"
4. Interact with 3D plot (rotate, zoom, pan)

**Spacecraft Tracking:**
1. Navigate to spacecraft section
2. Select missions (Voyager, Parker Solar Probe, etc.)
3. Enable trajectory visualization
4. Set date range for historical/predicted positions

**Star Visualizations:**
1. Click "2D and 3D Star Visualizations"
2. Enter distance (light-years) or magnitude limit
3. Choose HR diagram or 3D neighborhood plot
4. Hover over objects for detailed information

### Advanced Features

**Planetary Interiors:**
- Select Sun, planet, dwarf planet, or certain moons as center object
- Enable shell options (core, mantle, atmosphere)
- Toggle individual layers in plot legend

**Animations:**
- Set frame count and time step
- Choose animation interval (daily/weekly/monthly/yearly)
- Opens in browser with playback controls

## Features

### Data Sources
- **JPL Horizons**: Real-time ephemerides for solar system objects
- **Hipparcos/Gaia**: Stellar positions and properties (123,000+ stars)
- **SIMBAD**: Enhanced stellar properties and classifications

### Visualization Capabilities
- **3D Solar System**: 100+ objects with accurate trajectories
- **Stellar Neighborhood**: Stars within 100 light-years or visual magnitude 9
- **HR Diagrams**: Stellar classification and evolution
- **Planetary Shells**: Detailed interior structures
- **Spacecraft Missions**: Historical and current trajectories

### Smart Data Management
- **Incremental Caching**: Fetches only new data when expanding limits
- **Selective Updates**: Updates only selected objects
- **Protected Archives**: Timestamped backups prevent data loss
- **Rate Limiting**: Respects API limits (5 queries/second for SIMBAD)

### Analysis Tools
- **Object Type Analysis**: Categorizes 20+ stellar types
- **Diversity Metrics**: Shannon entropy and Simpson index
- **Scientific Reports**: Automated generation and archival
- **Data Quality Monitoring**: Completeness and accuracy checks

## Architecture

### Core Components

```
palomas_orrery/
├── palomas_orrery.py          # Main application entry
├── gui_main.py                 # Primary interface
├── data_acquisition*.py        # Data fetching modules
├── data_processing.py          # Processing and calculations
├── visualization_*.py          # 2D/3D plotting
├── simbad_manager.py          # SIMBAD API management
├── cache_managers/            # Cache handling
└── utils/                     # Supporting utilities
```

### Data Flow
1. **Acquisition**: Fetch from JPL/VizieR/SIMBAD
2. **Processing**: Calculate positions and parameters
3. **Caching**: Store with metadata for reuse
4. **Visualization**: Generate interactive plots
5. **Analysis**: Generate reports and statistics

## Module Reference

### Primary Modules

| Module | Purpose |
|--------|---------|
| `palomas_orrery.py` | Main application launcher |
| `gui_main.py` | Primary user interface |
| `data_acquisition.py` | VizieR catalog queries |
| `data_processing.py` | Coordinate calculations |
| `simbad_manager.py` | SIMBAD API with rate limiting |

### Visualization Modules

| Module | Purpose |
|--------|---------|
| `visualization_2d.py` | HR diagram generation |
| `visualization_3d.py` | 3D stellar plots |
| `visualization_core.py` | Common plotting utilities |
| `planetary_shells.py` | Planetary interior rendering |

### Cache Management

| Module | Purpose |
|--------|---------|
| `vot_cache_manager.py` | VizieR cache with atomic saves |
| `incremental_cache_manager.py` | Smart incremental fetching |
| `create_cache_backups.py` | Backup creation utility |

### Analysis Modules

| Module | Purpose |
|--------|---------|
| `object_type_analyzer.py` | Stellar classification analysis |
| `report_manager.py` | Scientific report generation |
| `stellar_parameters.py` | Temperature/luminosity calculations |
| `celestial_coordinates.py` | RA/Dec coordinate system |

## Data Files

### Cache Files
- `star_properties_distance.pkl` - Stars within 100 ly (9,700 objects)
- `star_properties_magnitude.pkl` - Stars to magnitude 9 (123,000 objects)
- `*.vot` - VizieR catalog data (Hipparcos/Gaia)
- `orbit_paths.json` - JPL Horizons orbital cache

### Configuration
- `satellite_ephemerides.json` - Satellite orbital elements
- `*_metadata.json` - Cache validation metadata

### Reports
- `last_plot_report.json` - Current analysis
- `reports/` - Archived timestamped reports

## Contributing

Contributions welcome! Areas of interest:
- Additional spacecraft missions
- Solar system structure
- Enhanced stellar classification
- Exo-planetary systems
- Performance optimizations

Please submit pull requests or contact the author.

## License

MIT License

Copyright (c) 2025 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

**Author:** Tony Quintanilla  
**Email:** tonyquintanilla@gmail.com  
**Github:** https://github.com/tonylquintanilla/palomas_orrery
**Website:** [Paloma's Orrery](https://sites.google.com/view/tony-quintanilla)  
**Updated:** September 2025