# Paloma's Orrery -- Last updated: November 15, 2025

An advanced astronomical visualization tool that transforms NASA/ESA data into interactive 3D and 2D visualizations of the solar system and stellar neighborhood.

## About

Created by Tony Quintanilla with assistance from Claude, ChatGPT, Gemini, and DeepSeek AI assistants.

## Platform

Important: Windows 10/11 only. Not built for macOS or Linux

## Table of Contents

1.  [Overview](#overview)
2.  [Quick Start & Installation (Main Gate)](#quick-start--installation-main-gate)
3.  [For Developers: Installing from GitHub (Side Gate)](#for-developers-installing-from-github-side-gate)
4.  [Usage](#usage)
5.  [Features](#features)
6.  [Architecture](#architecture)
7.  [Earth System Visualization](#earth-system-visualization)
8.  [Module Reference](#module-reference)
9.  [Data Files](#data-files)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

## Overview

Paloma's Orrery combines scientific accuracy with visual beauty, making astronomy accessible to students, educators, and space enthusiasts. Created by civil & environmental engineer Tony Quintanilla.

**Key Capabilities:**

- Real-time planetary and spacecraft positions from JPL Horizons
- Interactive 3D solar system with 100+ objects
- Comet visualization with dual-tail structures (dust and ion tails)
- Exoplanet system visualization (11 planets in 3 systems including binary stars)
- Stellar neighborhood mapping (123,000+ stars)
- Planetary and solar interior visualizations (with reference-frame independent rendering)
- HR diagrams and stellar analysis
- Climate data preservation hub

**Resources:**

- [Google Drive Repository](https://drive.google.com/drive/folders/1pt_RZxxxZOIaCxao_iWy17x0GFkwTf6h?usp=sharing)
- [Project Website](https://tonylquintanilla.github.io/palomas_orrery/)
- [Instagram: @palomas_orrery](https://www.instagram.com/palomas_orrery/)
- [Video Tutorials](https://www.youtube.com/@tony_quintanilla/featured)
- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery)

- Contact: <tonyquintanilla@gmail.com>

---

## 🚀 Quick Start & Installation (Main Gate)

Welcome! Since you are reading this file, you have already downloaded and unzipped the project. Your first step is to install the software needed to run it.

Again, Paloma's Orrery has been developed using Python in a Windows-only environment.

### Step 1: Install Python

If you already have Python 3.11, 3.12, or 3.13, you can skip this step.

Python is the programming language that runs Paloma's Orrery.

1.  **Download Python:**
    * Go to [python.org/downloads](https://www.python.org/downloads/)
    * Download **Python 3.13.x** (or Python 3.11.x or 3.12.x - all work great)
    * **Important:** Avoid brand-new Python versions that just came out - wait 1-2 months for libraries to catch up

2.  **Install Python:**
    * Run the downloaded installer
    * **✅ CRITICAL:** Check the box that says **"Add Python to PATH"** at the bottom
    * **✅ Also check:** "Install pip"
    * Click **"Install Now"**
    * Wait for installation to complete (2-3 minutes)
    * Click "Close" when done

3.  **Verify Python is installed:**
    * **Close any open Command Prompt windows first** (they won't see the new PATH until reopened)
    * Press `Windows Key`, type `cmd`, and press Enter to open a **new** Command Prompt
    * Type: `python --version`
    * You should see: `Python 3.13.x` (or 3.11.x, 3.12.x)
    * Type: `pip --version`
    * You should see: `pip 24.x.x from ...`
    **If you see "python is not recognized":**
    * Python wasn't added to PATH, OR you're using an old Command Prompt window
    * Close Command Prompt completely and open a new one
    * If still not working: Python wasn't added to PATH during installation
    * Solution: Uninstall Python (Control Panel → Programs), then reinstall and make sure you check "Add Python to PATH"

### Step 2: Install Python Libraries

These are additional tools that Paloma's Orrery needs to run.

1.  **Open a Command Prompt:**
    * Press `Windows Key`, type `cmd`, and press Enter.

2.  **Navigate to your Project Folder:**
    * In the Command Prompt, type `cd` followed by the path to your unzipped folder. For example:
        ```bash
        cd C:\Users\YourName\Documents\palomas_orrery
        ```
    * (Replace `YourName` and the path with your actual folder location).
    * **Tip:** You can also type `cd ` (with a space) and then drag the `palomas_orrery` folder from File Explorer into the Command Prompt window.

3.  **Install all libraries at once:**
    * With your Command Prompt in the `palomas_orrery` folder, type this command and press Enter:
        ```bash
        pip install -r requirements.txt
        ```
    * This reads the `requirements.txt` file and installs everything automatically. This should take 2-5 minutes.
    * You'll see lines of text scrolling by. It's done when you see "Successfully installed..."

    * Alternative (Manual Method): If the command above fails for any reason, you can install the packages manually. Copy the entire command and paste it into your Command Prompt.
         ```bash
         pip install numpy>=1.24.0 pandas>=2.0.0 scipy>=1.11.0 astropy>=5.3.4 astroquery>=0.4.6 plotly>=5.18.0 kaleido==0.2.1 pillow>=10.0.0 matplotlib>=3.7.0 customtkinter>=5.2.0 requests>=2.31.0 beautifulsoup4>=4.12.0 python-dateutil>=2.8.2 pytz>=2023.3 openpyxl>=3.1.0
         ```

### Step 3: Run Paloma's Orrery

You're all set! The easiest way to start the program is by using the Windows batch file, !_run_palomas_orrery.bat. If you order your files alphabetically by Name, it should be at the top.

1.  **Open your `palomas_orrery` folder** in Windows File Explorer.
2.  Find the file named **`!_run_palomas_orrery.bat`**.
3.  **Double-click `!_run_palomas_orrery.bat`** to start the program.

A launcher window will appear, check for Python, and then start the main application.

(Note: Windows may show a security warning indicating "Unknown Publisher". Click "Run" to start the program.)

---

## 🔑 For Developers: Installing from GitHub (Side Gate)

This is the "side gate" for developers. This repository contains the most up-to-date **source code**.

**IMPORTANT:** Due to file size limits, the required large data files (cache, etc.) are **not** included in this repository. You must download them separately from the **"Releases"** page.

### Quick Start (for experienced Python users)

```bash
# 1. Install Python 3.11-3.13 with PATH enabled

# 2. Clone this repository (the code)
git clone [https://github.com/tonylquintanilla/palomas_orrery.git](https://github.com/tonylquintanilla/palomas_orrery.git)
cd palomas_orrery

# 3. Download the Data Files
# Go to the "Releases" tab or this link:
# [https://github.com/tonylquintanilla/palomas_orrery/releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
# Download the data .zip file from the latest release (e.g., v2.0.0).
# Unzip the `data/` and `star_data/` folders into this directory.

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the batch file (or the .py script)
!_run_palomas_orrery.bat
```

---

### Common Installation Issues

**"python is not recognized"**

* **Cause:** Python wasn't added to PATH during installation.
* **Solution:** Reinstall Python (see Step 1) and make sure you check "Add Python to PATH".

**"No module named [something]"**

* **Cause:** A required library is missing. You may have missed "Step 2: Install Python Libraries".
* **Solution:** Open Command Prompt in the project folder and run `pip install [missing-module-name]`, or just run `pip install -r requirements.txt` again.

**"Cache files not found" or "FileNotFoundError"**

* **For Google Drive Users:** You may have unzipped the folder incorrectly. Make sure all subfolders (like `data/` and `star_data/`) are in the *same main folder* as `!_run_palomas_orrery.bat`.
* **For GitHub Users:** You forgot to download the cache. The `git clone` command only downloads the code. You must *also* go to the "Releases" page, download the cache ZIP, and unzip its contents into your project folder.

### System Requirements Summary

- **Operating System:** Windows 10/11 only. Not built for macOS or Linux
- **Python Version:** 3.11, 3.12, or 3.13 (thoroughly tested)
- **Memory (RAM):** 2GB minimum, 4GB recommended for large star datasets
- **Storage:** 520MB free disk space (includes all cache files and Python code)
- **Internet:** Required for initial download and for querying objects not in cache
- **Display:** 1280×720 minimum resolution recommended

### Optional: Installing a Code Editor

While not required to run Paloma's Orrery, if you want to explore or modify the code, a good code editor makes it much easier:

**Visual Studio Code (VS Code) - Recommended:**

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install with default options
3. Open VS Code and install the Python extension (search for "Python" in the Extensions panel; View/Extensions)
4. You can then open your entire `palomas_orrery` folder in VS Code: File â†’ Open Folder

**Why use a code editor?**

- Syntax highlighting makes code easier to read
- Built-in error detection catches typos
- Easy navigation between files
- Integrated terminal

## Usage

### Basic Operations

**Plotting Solar System Objects:**

1. In the main window, you'll see checkboxes for various celestial objects
2. Select the objects you want to visualize (planets, moons, asteroids, etc.)
3. Set the date and time using the date picker controls
4. Click "Plot Entered Date"
5. An interactive 3D plot will appear where you can:
   - Click and drag to rotate the view
   - Scroll to zoom in/out
   - Click planet names in the legend to show/hide them

**Tracking Spacecraft:**

1. Navigate to the spacecraft section
2. Select missions like:
   - Voyager 1 and 2 (interstellar space)
   - Parker Solar Probe (close to the Sun)
   - New Horizons (beyond Pluto)
   - James Webb Space Telescope
3. Enable trajectory visualization to see their paths
4. Set date range to view historical positions or future predictions

**Star Visualizations:**

1. Click "2D and 3D Star Visualizations"
2. Choose your criteria:
   - **By Distance:** Enter light-years (e.g., 100 for nearby stars)
   - **By Magnitude:** Enter brightness limit (e.g., 6.0 for naked-eye stars)
3. Select visualization type:
   - **HR Diagram:** Shows stellar evolution (temperature vs. luminosity)
   - **3D Star Map:** Interactive neighborhood map with distances
4. Save your visualizations as PNG or HTML files

**Planetary Interiors:**

1. Select a planet from the interior visualization section
2. View detailed cross-sections showing:
   - Core composition and size
   - Mantle layers
   - Atmospheric structure
   - Relative scales

**Earth System Data:**

1. Look for the green 🌍 indicator next to Earth's shell checkbox
2. Enable to access climate data visualizations
3. View the Keeling Curve (CO₂ measurements from 1958-2025)
4. See [climate_readme.md](climate_readme.md) for complete documentation

### Advanced Features

**Animation Controls:**

- Use time step controls to animate orbital motion
- Watch days, months, or years of evolution
- Follow spacecraft trajectories through their missions

**Coordinate System Options:**

- **Heliocentric:** Sun-centered view (default)
- **Barycentric:** Solar system center of mass
- **Planet-centered:** View from any planet's perspective

**Lagrange Points:**

- Visualize L1-L5 gravitational equilibrium points
- Available for Earth-Moon and Sun-Earth systems
- Shows where spacecraft can maintain stable positions

**Orbital Markers:**

- Enable apsidal markers to see perihelion/aphelion points for ideal orbits and when actual perihelion dates are available
- Shows closest/farthest points for objects orbiting the Sun and planets for the actual plotted orbit
- Includes date and distance information for each marker

**Solar Structure Visualization:**

- Toggle individual Sun layers (core, radiative zone, convective zone)
- View solar atmosphere (photosphere, chromosphere, corona)
- Explore solar wind boundaries and heliosphere

**Data Export:**

- Copy star names and coordinates to clipboard
- Save plots as PNG (static images) or HTML (interactive)
- Export data as JSON, VOTable, or Pickle formats

## Features

### Solar System Visualization

| Feature | Description |
|---------|-------------|
| **Objects** | 100+ celestial bodies: all planets, major moons, asteroids, comets, dwarf planets, spacecraft |
| **Data Source** | Real-time JPL Horizons ephemerides with automatic caching |
| **Time Range** | Historical and future dates through 2199-12-29 |
| **Scales** | Inner planets to 100,000 AU Oort cloud visualization |
| **Reference Frames** | Heliocentric, barycentric, planet-centered views |
| **Orbit Calculation** | Both actual positions and idealized Keplerian orbits |
| **Caching System** | Intelligent incremental updates with automatic backup |

**Exoplanet Visualization:**

- **Systems:** 3 confirmed exoplanet systems (TRAPPIST-1, TOI-1338, Proxima Centauri)
- **Planets:** 11 exoplanets with accurate Keplerian orbital mechanics
- **Orbital Mechanics:** Full 6-parameter Keplerian orbits (a, e, i, ω, Ω, M₀) with time evolution
- **Binary Stars:** Circumbinary planet support with dual-star orbital dynamics (TOI-1338)
- **Host Stars:** Temperature-based coloring from cool red M-dwarfs (2,800K) to hot blue stars
- **Visualization Modes:**
  - System barycenter view (orbital motion around center of mass)
  - Individual star centering for binary systems
  - Planet orbit traces with customizable time spans
- **Physical Properties:** Planet radii, masses, equilibrium temperatures in hover data
- **Habitable Zones:** Visual markers for potentially life-supporting orbital regions
- **Animation Support:** Time-evolution showing planetary and stellar motion
- **Scientific Accuracy:** Data from NASA Exoplanet Archive and published literature
- See [exoplanet_readme.md](exoplanet_readme.md) for complete technical documentation

**Comet Visualization:**

- **Dual-Tail Structure:** Scientifically accurate rendering of both comet tail types
  - Dust Tail (Type II): Curved golden/yellow tail from reflected sunlight
  - Ion Tail (Type I): Straight blue plasma tail from CO⁺ emissions
  - Green coma from C₂ (dicarbon) fluorescence near nucleus
- **Astrophotography Colors:** Tail colors match long-exposure photography appearance
  - Dust tails: Whitish-yellow/gold reflecting full visible spectrum (400-700nm)
  - Ion tails: Blue from carbon monoxide ions (400-460nm emission)
- **Activity Scaling:** Tail brightness and length scale dynamically with solar distance
  - Maximum activity at perihelion
  - Tails fade beyond ~3 AU from Sun
- **Historical Comets:** Catalog includes famous comets with accurate tail parameters
  - Halley's Comet (76-year period)
  - Hale-Bopp (Great Comet of 1997)
  - NEOWISE (C/2020 F3)
  - Lemmon (C/2025 A6) - currently visible in 2025
  - Hyakutake (record 580 million km ion tail)
  - Ikeya-Seki (Great Sungrazer of 1965)
- **Physical Components:** Toggle individual features on/off
  - Nucleus marker
  - Coma (fuzzy atmosphere)
  - Dust tail
  - Ion tail
  - Sun direction indicator
- **Real-Time Positions:** JPL Horizons ephemerides for accurate comet tracking
- **Educational Tool:** Color-coded to match what astrophotography reveals vs. naked-eye appearance

### Stellar Astronomy

| Feature | Description |
|---------|-------------|
| **Star Catalogs** | 123,000 stars (magnitude 9.0), 9,700 within 100 light-years |
| **Visualizations** | HR diagrams, 3D spatial maps, constellation views |
| **Data Sources** | Gaia EDR3, Hipparcos, SIMBAD integration |
| **Deep Sky Objects** | Messier catalog (nebulae, clusters, galaxies) in magnitude mode |
| **Filtering** | By distance (light-years) or apparent magnitude |
| **Classification** | Spectral types, luminosity classes, evolutionary stages |

### Planetary Features

| Feature | Description |
|---------|-------------|
| **Interior Structures** | Multi-layer visualization for all major bodies |
| **Solar Detail** | 11-zone Sun model from core to heliosphere |
| **Radiation Belts** | Van Allen belts, Jovian plasma tori |
| **Atmospheres** | Individual atmospheric shell visualization |
| **Ring Systems** | Saturn, Jupiter, Uranus, Neptune rings |

### Interactive Features

| Feature | Description |
|---------|-------------|
| **3D Rotation & Zoom** | Full camera control with mouse/trackpad |
| **Camera View Selector** | Dropdown menu to view any object from center position - point camera from Sun toward Earth, Mars, or any plotted object |
| **Object Selection** | Multi-select with legend toggles |
| **Time Animation** | Watch orbital evolution over days to years |
| **Lagrange Points** | L1-L5 visualization for Earth-Moon and Sun-Earth systems |
| **Apsidal Markers** | Perihelion/aphelion indicators with dates |
| **Advanced Hover Info** | Detailed astronomical data with toggle controls |
| **Data Export** | PNG, HTML, JSON, VOTable, Pickle formats |
| **Copy to Clipboard** | Easy sharing of star names and coordinates |

### Educational Tools

| Tool | Description |
|------|-------------|
| **Orbital Parameter Visualization** | Interactive 3D demonstration of Keplerian elements (inclination, longitude of ascending node, argument of periapsis) showing transformation from perifocal to J2000 Ecliptic frame |
| **Interactive Eccentricity Demo** | Visual exploration of orbit shapes from circles (e=0) through ellipses, parabolas (e=1), to hyperbolas (e>1) |
| **Coordinate System Reference Guide** | Comprehensive visualization of J2000 Ecliptic system with detailed axis explanations (+X Vernal Equinox, +Y 90Â° ahead, +Z Ecliptic North) |

### Data Sources

- [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/app.html#/) - Planetary ephemerides
- [Gaia EDR3](https://www.cosmos.esa.int/web/gaia) - Stellar positions and photometry
- [Hipparcos](https://www.cosmos.esa.int/web/hipparcos/catalogues) - Bright star catalog
- [SIMBAD](https://simbad.u-strasbg.fr/simbad/) - Astronomical database
- [Scripps CO₂ Program](https://scrippsco2.ucsd.edu/) - Mauna Loa atmospheric data

## Architecture

### System Design

Paloma's Orrery follows a clean 10-layer architecture with three parallel data pipelines (Solar System, Stellar, Earth System) processing different astronomical data through common infrastructure layers.

**For complete architectural documentation:**

- **[MODULE_INDEX.md](MODULE_INDEX.md#system-architecture-overview)** - Layer descriptions and module distribution
- **[architecture_directory_tree_style.md](architecture_directory_tree_style.md)** - Directory-tree style architecture visualization  
- **[palomas_orrery_flowchart_v13_vertical.md](palomas_orrery_flowchart_v13_vertical.md)** - Interactive Mermaid flowchart

**Key Insight:** The cache management layer (Layer 3) provides defense-in-depth data protection with validation, atomic saves, backups, and automatic repair mechanisms.

### Data Flow

1. **Acquisition:** Fetch astronomical data from JPL Horizons, VizieR catalogs, and SIMBAD
2. **Processing:** Calculate positions, velocities, and stellar parameters
3. **Caching:** Store processed data with metadata for instant reuse
4. **Visualization:** Generate interactive Plotly visualizations
5. **Analysis:** Create scientific reports and statistical summaries

### Performance Optimizations

- **Incremental caching:** Only fetch new data, reuse existing
- **Smart cache management:** Automatic validation and repair
- **Compressed storage:** Efficient binary formats (PKL, VOTable)
- **Rate limiting:** Respectful API usage with automatic throttling
- **Batch processing:** Group queries for efficiency

## Earth System Visualization

### Climate Data Preservation Hub

Interactive visualizations documenting Earth's changing systems - because **data preservation is climate action**.

**Current Features (9 Active Visualizations):**

**Climate & Atmosphere:**

1. **The Keeling Curve:** Atmospheric CO₂ from Mauna Loa Observatory (1958-2025)
   - Monthly resolution with seasonal variations
   - Clear visualization of 400+ ppm threshold crossing
   - Interactive zoom and data exploration

2. **Global Temperature Anomalies:** NASA GISS land-ocean temperature index (1880-2025)
   - Annual and decadal trends
   - Pre-industrial baseline comparison
   - Paris Agreement target thresholds

3. **Monthly Temperature Progression:** Year-over-year temperature comparison
   - Each line represents one year's temperature journey
   - Reveals seasonal patterns and warming acceleration
   - Color-coded by decade for trend visualization

4. **Warming Stripes:** Ed Hawkins-style climate communication
   - Visual representation of temperature changes over time
   - Minimal design for maximum impact
   - Annual temperature data encoded as color stripes

5. **Paleoclimate History:** Deep-time climate context (65 million years to present)
   - Cenozoic Era temperature reconstruction
   - Geological period markers and context
   - Shows natural climate variability and current unprecedented rate of change

**Cryosphere:**

6. **Arctic Sea Ice Extent:** September minimum measurements (1979-2024)
   - Dramatic decline visualization
   - Statistical trend analysis with uncertainty bands
   - Critical indicator of polar amplification

**Ocean Systems:**

7. **Global Mean Sea Level Rise:** Satellite altimetry and tide gauge data (1880-2023)
   - Acceleration of sea level rise clearly visible
   - Multiple data source integration
   - Projection markers for future scenarios

8. **Ocean Acidification:** Surface ocean pH measurements (1988-2023)
   - Hawaii Ocean Time-series data from Station ALOHA
   - Shows consistent decline in ocean pH
   - Critical for marine ecosystem health

**Earth System:**

9. **Planetary Boundaries:** Stockholm Resilience Centre framework (2025)
   - 9 Earth system processes that regulate planetary stability
   - Current status: 6 of 9 boundaries transgressed
   - Visual representation of safe operating space for humanity

**Integration:** Access via Earth's shell checkbox (green indicator)

- Seamlessly integrated with solar system visualization
- Hub interface with organized categories
- One-click data updates for automated sources

**Why This Matters:**

Climate and Earth-science observatories provide irreplaceable long-term baseline data. Programs like the Keeling Curve (continuous since 1958) and satellite monitoring systems face potential defunding. This hub preserves and visualizes critical measurements that document planetary change.

**Documentation:**

See [climate_readme.md](climate_readme.md) for complete technical documentation, data sources, and update procedures.

**Data Sources:**

- Scripps CO₂ Program at Mauna Loa Observatory
- NOAA Global Monitoring Laboratory
- Additional sources as datasets are integrated

## Module Reference

**For a complete index of all 79 Python modules in the project, see [MODULE_INDEX.md](MODULE_INDEX.md).**

The following sections highlight the primary modules organized by function. Use MODULE_INDEX.md to search for specific functionality (save, cache, coordinates, etc.) or to understand the complete codebase structure.

### Primary Modules

| Module | Purpose |
|--------|---------|
| `palomas_orrery.py` | Main application launcher and entry point |
| `gui_main.py` | Primary user interface with tkinter/customtkinter |
| `data_acquisition.py` | VizieR catalog queries (Gaia, Hipparcos) |
| `data_processing.py` | Coordinate transformations and calculations |
| `simbad_manager.py` | SIMBAD API integration with rate limiting |
| `orbit_data_manager.py` | JPL Horizons queries and orbit caching |

### Visualization Modules

| Module | Purpose |
|--------|---------|
| `visualization_2d.py` | Hertzsprung-Russell diagram generation |
| `visualization_3d.py` | Interactive 3D stellar neighborhood plots |
| `visualization_core.py` | Common plotting utilities and styling |
| `planetary_shells.py` | Planetary interior cross-section rendering |
| `solar_visualization_shells.py` | Solar interior and corona visualization (reference-frame independent) |
| `comet_visualization_shells.py` | Scientifically accurate comet rendering with dual-tail structures (dust/ion) |
| `orbital_param_viz.py` | Orbital element visualization |
| `coordinate_system_guide.py` | J2000 Ecliptic coordinate system reference guide |
| `earth_system_visualization_gui.py` | Earth system data hub with climate visualizations |

### Cache Management

| Module | Purpose |
|--------|---------|
| `vot_cache_manager.py` | VizieR cache with atomic saves and validation |
| `incremental_cache_manager.py` | Smart incremental fetching for stellar datasets |
| `orbit_data_manager.py` | Orbit path caching with safety protections and incremental updates |
| `create_cache_backups.py` | Stellar data (PKL/VOT) backup creation utility |
| `verify_orbit_cache.py` | Orbit cache validation and repair utility |

### Analysis Modules

| Module | Purpose |
|--------|---------|
| `object_type_analyzer.py` | Stellar classification and type analysis |
| `report_manager.py` | Scientific report generation with statistics |
| `stellar_parameters.py` | Temperature, luminosity, and HR calculations |
| `celestial_coordinates.py` | RA/Dec coordinate system conversions |
| `stellar_data_patches.py` | Data quality improvements and corrections |
| `fetch_climate_data.py` | Climate data fetcher (Mauna Loa CO₂) |

### Orbital Calculations

| Module | Purpose |
|--------|---------|
| `idealized_orbits.py` | Simplified circular/elliptical orbits |
| `refined_orbits.py` | High-precision orbital mechanics |
| `orrery_integration.py` | Integration layer for orbit selection |
| `create_ephemeris_database.py` | Satellite ephemeris database builder |

### Exoplanet Modules

| Module | Purpose |
|--------|---------|
| `exoplanet_systems.py` | Exoplanet system catalog with host star and planet data |
| `exoplanet_orbits.py` | Keplerian orbital mechanics for exoplanets |
| `exoplanet_coordinates.py` | Stellar position calculations and proper motion |
| `exoplanet_stellar_properties.py` | Temperature-based coloring, stellar properties, hover text generation |

## Data Files

### Project Directory Structure

palomas_orrery/
├── *.py                      # Python source code
├── !_run_palomas_orrery.bat  # Windows launcher
├── README/                   # Documentation
│   ├── README.md
│   ├── paleoclimate_readme.md
│   └── climate_readme.md
├── data/                     # All program data files
│   ├── orbit_paths.json (~94 MB)
│   ├── orbit_paths_backup.json
│   ├── Climate monitoring (automated)
│   │   ├── co2_mauna_loa_monthly.json
│   │   ├── temperature_giss_monthly.json
│   │   ├── arctic_ice_extent_monthly.json
│   │   └── sea_level_gmsl_monthly.json
│   ├── Climate monitoring (manual)
│   │   ├── ocean_ph_hot_monthly.json
│   │   └── 3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv
│   └── Paleoclimate data
│       ├── epica_co2_800kyr.json
│       ├── lr04_benthic_stack.json
│       ├── temp12k_allmethods_percentiles.csv
│       └── 8c__Phanerozoic_Pole_to_Equator_Temperatures.csv
├── star_data/                # Protected stellar cache (Module 4 - Nov 2025)
│   ├── star_properties_distance.pkl (2.6 MB)
│   ├── star_properties_magnitude.pkl (31.8 MB)
│   ├── hipparcos_data_distance.vot (899 KB)
│   ├── hipparcos_data_magnitude.vot (193 KB)
│   ├── gaia_data_distance.vot (9.8 MB)
│   ├── gaia_data_magnitude.vot (291 MB)
│   └── *_metadata.json files
└── reports/                  # Generated analysis reports (Module 3 - Nov 2025)
    ├── last_plot_report.json
    ├── last_plot_data.json
    └── report_*.json (archived with timestamps)

### Cache Files (Included in Release)

- `star_properties_distance.pkl` - 9,700 stars within 100 light-years with full properties
- `star_properties_magnitude.pkl` - 123,000 stars to magnitude 9 with properties
- `hipparcos_*.vot` - Hipparcos catalog data (bright stars)
- `gaia_*.vot` - Gaia EDR3 catalog data (faint stars)

**orbit_paths.json** (~96 MB typical)

- Time-indexed orbital position data for 1000+ objects
- Supports multiple reference frames (Sun, planets, moons)
- Includes automatic backup and safety protections

**orbit_paths_backup.json**

- Automatic backup created on startup
- Used for recovery if cache becomes corrupted

### Configuration Files

- `satellite_ephemerides.json` - Satellite orbital elements and physical properties
- `*_metadata.json` - Cache validation metadata and timestamps
- `orrery_config.json` - User preferences and display settings
- `co2_mauna_loa_monthly.json` - Monthly atmospheric CO₂ measurements (1958-2025)

### Generated Reports

- `last_plot_report.json` - Current session analysis results
- `last_plot_data.json` - Data exchange between processes
- `reports/` - Archived timestamped analysis reports

### Cache File Sizes

| File Type | Approximate Size | Description |
|-----------|------------------|-------------|
| Distance PKL | 3 MB | Stars within 100 ly |
| Magnitude PKL | 32 MB | Stars to mag 9.0 |
| VOTable files | 1-291 MB each | Raw catalog data |
| Orbit cache | 96+ MB | Planetary ephemerides |
| Climate data | <1 MB | CO₂ measurements |

## Contributing

Contributions are welcome! This project is maintained by a single developer but welcomes community input.

**Areas of Interest:**

- Additional spacecraft mission data
- Enhanced solar system structure visualizations
- Improved stellar classification algorithms
- Exoplanetary system support
- Performance optimizations for large datasets
- Documentation improvements
- Climate data integration (temperature, sea level, ice extent)

**How to Contribute:**

Suggestions are welcome: <tonyquintanilla@gmail.com>

**Bug Reports:**

- Include Python version and steps to reproduce
- Attach relevant error messages or screenshots

## License

MIT License

Copyright (c) 2025 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

**Author:** Tony Quintanilla  
**Email:** <tonyquintanilla@gmail.com>  
**GitHub:** [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)  
**Website:** [tonylquintanilla.github.io/palomas_orrery](https://tonylquintanilla.github.io/palomas_orrery/)  
**Instagram:** [@palomas_orrery](https://www.instagram.com/palomas_orrery/)  
**YouTube:** [Paloma's Orrery](https://www.youtube.com/@tony_quintanilla/featured)  

**Last Updated:** November 2025

---

**Acknowledgments:**

- [NASA JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/) for planetary ephemerides
- [ESA Gaia Mission](https://www.cosmos.esa.int/web/gaia) for stellar data
- [VizieR catalog service](https://vizier.cds.unistra.fr/) (CDS, Strasbourg)
- [SIMBAD astronomical database](https://simbad.u-strasbg.fr/simbad/)
- [Scripps CO₂ Program](https://scrippsco2.ucsd.edu/) for Mauna Loa data
- [Astropy](https://www.astropy.org/) and [Astroquery](https://astroquery.readthedocs.io/) development teams
- [Plotly](https://plotly.com/) visualization library
- AI coding assistants: [Anthropic Claude](https://www.anthropic.com/claude), [OpenAI ChatGPT](https://openai.com/chatgpt), [Google Gemini](https://gemini.google.com/), [DeepSeek](https://www.deepseek.com/)
