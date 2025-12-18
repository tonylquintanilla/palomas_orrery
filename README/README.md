# Last updated: December 8, 2025

# Paloma's Orrery

An advanced astronomical visualization tool that transforms NASA/ESA data into interactive 3D and 2D visualizations of the solar system and stellar neighborhood.

## About

Created by Tony Quintanilla with assistance from Claude, ChatGPT, Gemini, and DeepSeek AI assistants.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Architecture](#architecture)
7. [Earth System Visualization](#earth-system-visualization)
8. [Module Reference](#module-reference)
9. [Data Files](#data-files)
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
- Pluto-Charon binary planet visualization with true barycentric orbital mechanics
- TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2)
- Stellar neighborhood mapping (123,000+ stars)
- Planetary and solar interior visualizations (with reference-frame independent rendering)
- HR diagrams and stellar analysis
- Climate data preservation hub

**Resources:**

- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery)
- [Project Website](https://tonylquintanilla.github.io/palomas_orrery/)
- [Instagram: @palomas_orrery](https://www.instagram.com/palomas_orrery/)
- [Video Tutorials](https://www.youtube.com/@tony_quintanilla/featured)
- Contact: <tonyquintanilla@gmail.com>

## Quick Start

**For experienced Python users:**

```bash
# 1. Install Python 3.11-3.13 with PATH enabled
# 2. Clone repository
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery

# 3. Download cache files from releases page
# https://github.com/tonylquintanilla/palomas_orrery/releases
# Extract cache_files_compressed.zip to project folder

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run
python palomas_orrery.py
```

**New to Python?** See the [detailed installation guide below](#installation)

## Installation

### Prerequisites

- **Windows 10/11** (Mac/Linux also supported)
- **Python 3.11 to 3.13** (tested and verified compatible)
  - As of October 2025, Python 3.13 is recommended
  - Python 3.14 was just released - wait 1-2 months before using it
- **Git** (optional but recommended)
- **520MB free disk space** (includes all cache files and code)
- **Internet connection** (for initial setup and fetching new objects)

### Step-by-Step Installation Guide for Beginners

This guide assumes you're new to Python and command-line tools. We'll walk through everything!

#### Step 1: Install Git (Optional but Recommended)

Git makes it easy to download and update the project. If you prefer, you can skip this and download a ZIP file instead (see Step 3, Option B).

**To install Git:**

1. Go to [git-scm.com/downloads](https://git-scm.com/downloads)
2. Download the installer for Windows
3. Run the installer:
   - **Important:** When you see the screen asking about additional options, **check the box for "Additional icons → On the Desktop"**
   - This creates a handy Git Bash shortcut on your desktop
   - Click "Next" through the remaining screens (other defaults are fine)
4. After installation completes, you should see a "Git Bash" icon on your desktop
5. **Close any open Command Prompt windows** (this is important!)
6. **Verify Git is installed:**
   - Press `Windows Key`, type `cmd`, and press Enter to open a **new** Command Prompt
   - Type: `git --version`
   - You should see something like `git version 2.43.0`
   **If you still see "git is not recognized" in Command Prompt:**
   - The installation might not have fully registered yet
   - Try opening "Git Bash" from your desktop icon first
   - In Git Bash, type: `git --version` - this should work
   - Then close Command Prompt completely, wait 10 seconds, and open a fresh one
   - Try `git --version` again in the new Command Prompt - it should work now
   - If it still doesn't work, restart your computer

**What's the difference between Command Prompt and Git Bash?**

- **Command Prompt (cmd):** Windows' standard terminal - you'll use this for running Python
- **Git Bash:** A Linux-style terminal that comes with Git - useful for Git commands and has Git pre-configured
- Both work for this project, but Command Prompt is simpler for beginners

**Don't want to use Git?** That's okay! Skip to Step 3, Option B to download as a ZIP file.

#### Step 2: Install Python

Python is the programming language that runs Paloma's Orrery.

1. **Download Python:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download **Python 3.13.x** (or Python 3.11.x or 3.12.x - all work great)
   - **Important:** Avoid brand-new Python versions that just came out - wait 1-2 months for libraries to catch up

2. **Install Python:**
   - Run the downloaded installer
   - **CRITICAL:** Check the box that says **"Add Python to PATH"** at the bottom
   - **Also check:** "Install pip"
   - Click **"Install Now"**
   - Wait for installation to complete (2-3 minutes)
   - Click "Close" when done

3. **Verify Python is installed:**
   - **Close any open Command Prompt windows first** (they won't see the new PATH until reopened)
   - Press `Windows Key`, type `cmd`, and press Enter to open a **new** Command Prompt
   - Type: `python --version`
   - You should see: `Python 3.13.x` (or 3.11.x, 3.12.x)
   - Type: `pip --version`
   - You should see: `pip 24.x.x from ...`
   **If you see "python is not recognized":**
   - Python wasn't added to PATH, OR you're using an old Command Prompt window
   - Close Command Prompt completely and open a new one
   - If still not working: Python wasn't added to PATH during installation
   - Solution: Uninstall Python (Control Panel → Programs), then reinstall and make sure you check "Add Python to PATH"

#### Step 3: Download Paloma's Orrery

You have two options: use Git (easier for updates) or download a ZIP file (simpler if you're not familiar with Git).

**Option A - Using Git (Recommended if you installed Git):**

1. **Choose where to save the project:**
   - Common locations: `C:\Users\YourName\Documents` or `C:\Projects`
   - For this example, we'll use Documents

2. **Open Command Prompt:**
   - Press `Windows Key`, type `cmd`, press Enter

3. **Navigate to where you want to save the project:**

   ```bash
   cd C:\Users\YourName\Documents
   ```

   (Replace `YourName` with your actual Windows username)

   **Note:** When you see code blocks labeled `bash`, it means these are commands to type in Command Prompt (or Terminal on Mac/Linux). Just type the command and press Enter - don't type the word "bash"!

4. **Download the project:**

   ```bash
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   ```

   This should only take a few seconds (the project itself is small - the large cache files come separately).

   Git will create a new folder called `palomas_orrery` and download all the files into it.

5. **Navigate into the project folder:**

   ```bash
   cd palomas_orrery
   ```

**Option B - Download as ZIP file (No Git required):**

1. Go to [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract the ZIP file to your preferred location
5. Rename the extracted folder from `palomas_orrery-main` to `palomas_orrery`
6. Open Command Prompt and navigate to the extracted folder:

   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery
   ```

#### Step 4: Download Cache Files

The cache files contain pre-processed stellar data and orbital calculations. Without them, the first run would take hours to download and process everything!

1. **Go to the releases page:**
   - Visit [github.com/tonylquintanilla/palomas_orrery/releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
   
2. **Download the cache file:**
   - Look for `cache_files_compressed.zip` (approximately 150-200 MB)
   - Click to download

3. **Extract to project folder:**
   - Open the ZIP file
   - Extract ALL contents directly into your `palomas_orrery` folder
   - The folder structure should look like:
     ```
     palomas_orrery/
     ├── palomas_orrery.py
     ├── data/
     │   └── orbit_paths.json
     ├── star_data/
     │   ├── star_properties_distance.pkl
     │   └── gaia_data_distance.vot
     └── ... (other files)
     ```

4. **Verify the files are in place:**
   - You should see `star_data/` folder with `.pkl` and `.vot` files
   - You should see `data/orbit_paths.json` (this is the largest file, ~96 MB)

#### Step 5: Install Dependencies

Python packages are like add-ons that provide extra functionality. Paloma's Orrery needs several of these.

1. **Make sure you're in the project folder:**
   - In Command Prompt, you should see something like `C:\Users\YourName\Documents\palomas_orrery>`
   - If not, navigate there with `cd C:\Users\YourName\Documents\palomas_orrery`

2. **Install all required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   This will download and install all necessary packages. It may take 2-5 minutes depending on your internet connection.

   **What you'll see:** A lot of text scrolling by as packages are downloaded and installed. This is normal!

   **If you see errors:** Most common issues:
   - "pip is not recognized" → Python wasn't installed correctly. Go back to Step 2.
   - Network errors → Check your internet connection and try again
   - Permission errors → Try running Command Prompt as Administrator

3. **Verify installation:**
   - After installation completes, you should see "Successfully installed" messages
   - No red error text at the end means success!

#### Step 6: Run Paloma's Orrery

You're ready to launch!

1. **Start the application:**

   ```bash
   python palomas_orrery.py
   ```

2. **What happens next:**
   - A GUI window will appear with the main control panel
   - The first time you run, it may take 30-60 seconds to initialize caches
   - You'll see a three-panel interface with object selection, controls, and notes

3. **Try your first visualization:**
   - Check the boxes for a few planets (Mercury, Venus, Earth, Mars)
   - Click "Plot Entered Date"
   - An interactive 3D visualization will appear in your browser!

**Congratulations!** You've successfully installed Paloma's Orrery!

### Troubleshooting

**"python is not recognized"**
- Python wasn't added to PATH during installation
- Solution: Uninstall Python, reinstall with "Add Python to PATH" checked

**"pip install" fails with permission errors**
- Try: `pip install --user -r requirements.txt`
- Or run Command Prompt as Administrator

**Application won't start**
- Make sure you're in the correct folder
- Check that all cache files were extracted properly
- Try: `python -c "import tkinter"` to verify tkinter is installed

**Visualization doesn't appear**
- Check that your default browser is working
- The plot opens as an HTML file in your browser

**"Module not found" errors**
- Some packages may not have installed correctly
- Try: `pip install [module_name]` for the specific missing module

### Updating the Application

**If you used Git:**

```bash
cd palomas_orrery
git pull
pip install -r requirements.txt  # In case new dependencies were added
```

**If you downloaded ZIP:**

1. Download the new ZIP from GitHub
2. Extract and replace files (keep your cache files!)
3. Run `pip install -r requirements.txt` if requirements changed

### Alternative IDEs

While Command Prompt works fine, you might prefer a more visual development environment:

**VS Code (Recommended):**
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install the Python extension
- Open the `palomas_orrery` folder
- Use the integrated terminal

**PyCharm:**
- Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Open the project folder
- Configure Python interpreter
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

1. Look for the green 🌍 indicator next to Earth's shell checkbox
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
- **Pluto-Charon Barycenter:** True binary planet view showing both Pluto and Charon orbiting their common center of mass (the only true binary in our solar system!)
- **TNO-centered:** View Eris, Haumea, or Makemake with their moons

**Lagrange Points:**

- Visualize L1-L5 gravitational equilibrium points
- Available for Earth-Moon and Sun-Earth systems
- Shows where spacecraft can maintain stable positions

**Orbital Markers:**

- Enable apsidal markers to see perihelion/aphelion points
- Shows closest/farthest points from the Sun
- Includes date information for each marker

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
| **Reference Frames** | Heliocentric, barycentric, planet-centered, Pluto-Charon barycenter (binary planet), TNO-centered views |
| **Orbit Calculation** | Both actual positions and idealized Keplerian orbits using osculating elements |
| **Caching System** | Intelligent incremental updates with automatic backup |

**TNO Satellite Systems:**

- **Eris/Dysnomia:** Distant dwarf planet with its moon (JPL ephemeris)
- **Haumea/Hi'iaka/Namaka:** Elongated dwarf planet with two moons (JPL ephemeris)
- **Makemake/MK2:** Dwarf planet with dark, recently-discovered moon (analytical orbit from 2025 Hubble analysis - no JPL ephemeris yet!)
- **View modes:** See satellites from heliocentric or TNO-centered perspectives
- **Analytical fallback:** Objects without JPL data calculated from published orbital elements

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
| **Coordinate System Reference Guide** | Comprehensive visualization of J2000 Ecliptic system with detailed axis explanations (+X Vernal Equinox, +Y 90° ahead, +Z Ecliptic North) |
| **Pluto-Charon Binary System** | Three-view visualization demonstrating true barycentric orbital mechanics - switch from Pluto-centered to barycenter-centered view to see Pluto's own orbit revealed (like shifting from geocentric to heliocentric thinking!) |
| **TNO Satellite Systems** | Visualize distant dwarf planet moons, including MK2 using cutting-edge 2025 Hubble orbital analysis |

### Data Sources

- [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/app.html#/) - Planetary ephemerides
- [Gaia EDR3](https://www.cosmos.esa.int/web/gaia) - Stellar positions and photometry
- [Hipparcos](https://www.cosmos.esa.int/web/hipparcos/catalogues) - Bright star catalog
- [SIMBAD](https://simbad.u-strasbg.fr/simbad/) - Astronomical database
- [Scripps CO₂ Program](https://scrippsco2.ucsd.edu/) - Mauna Loa atmospheric data
- [arXiv preprints](https://arxiv.org/) - Latest orbital solutions for newly-discovered objects

## Architecture

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
- **Analytical fallback:** Calculate orbits locally when API data unavailable

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

**Cryosphere:**

5. **Arctic Sea Ice Extent:** NSIDC satellite data (1979-2025)
   - Monthly Arctic ice coverage
   - September minimum tracking
   - Decadal decline visualization

**Sea Level:**

6. **Sea Level Rise:** NASA/TOPEX satellite altimetry (1993-2025)
   - Global mean sea level change
   - Acceleration trends
   - Millimeter precision measurements

**Ocean Health:**

7. **Ocean Acidification:** Hawaii Ocean Time-series surface pH (1988-2025)
   - Monthly pH measurements
   - CO₂ absorption impact on ocean chemistry
   - Trend analysis

**Deep Time:**

8. **Paleoclimate 800kyr:** Antarctic ice core CO₂ reconstruction
   - EPICA Dome C 800,000-year record
   - Glacial-interglacial cycles
   - Context for modern CO₂ levels

9. **Cenozoic Temperature:** 65 million years of climate context
   - Full Cenozoic Era reconstruction
   - Major climate events (PETM, EECO)
   - Long-term cooling trend into ice ages

### Why This Matters

This project began as astronomical visualization but expanded to climate data preservation as datasets began disappearing from government websites. The Earth System module serves three purposes:

1. **Educational:** Clear visualizations of climate science data
2. **Preservation:** Local copies of critical datasets
3. **Context:** Show Earth as just another planet we can study scientifically

**Data Sources:**

- Scripps CO₂ Program at Mauna Loa Observatory
- NOAA Global Monitoring Laboratory
- Additional sources as datasets are integrated

## Module Reference

**For a complete index of all 81 Python modules in the project, see [MODULE_INDEX.md](MODULE_INDEX.md).**

The following sections highlight the primary modules organized by function. Use MODULE_INDEX.md to search for specific functionality (save, cache, coordinates, etc.) or to understand the complete codebase structure.

### Primary Modules

| Module | Purpose |
|--------|---------|
| `palomas_orrery.py` | Main application (~420KB, 8,700+ lines) - GUI, plot_objects(), animate_objects() |
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
| `*_visualization_shells.py` | Planetary interior cross-sections (12 modules) |
| `comet_visualization_shells.py` | Scientifically accurate comet rendering with dual-tail structures |
| `orbital_param_viz.py` | Orbital element visualization |
| `earth_system_visualization_gui.py` | Earth system data hub with climate visualizations |

### Cache Management

| Module | Purpose |
|--------|---------|
| `vot_cache_manager.py` | VizieR cache with atomic saves and validation |
| `incremental_cache_manager.py` | Smart incremental fetching for stellar datasets |
| `osculating_cache_manager.py` | Osculating elements cache with center-body aware keys |
| `orbit_data_manager.py` | Orbit path caching with safety protections |
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
| `idealized_orbits.py` | Core orbit visualization - Keplerian calculations, osculating elements, TNO satellites, analytical fallback |
| `orbital_elements.py` | Orbital parameters, parent_planets dictionary, TNO moon elements |
| `orrery_integration.py` | Integration layer for orbit selection |
| `apsidal_markers.py` | Perihelion/aphelion markers with perturbation analysis |

### Exoplanet Modules

| Module | Purpose |
|--------|---------|
| `exoplanet_systems.py` | Exoplanet system catalog with host star and planet data |
| `exoplanet_orbits.py` | Keplerian orbital mechanics for exoplanets |
| `exoplanet_coordinates.py` | Stellar position calculations and proper motion |
| `exoplanet_stellar_properties.py` | Temperature-based coloring, stellar properties, hover text generation |

## Data Files

### Project Directory Structure

```
palomas_orrery/
├── *.py                    # Python source code
├── README/                 # Documentation
│   ├── README.md
│   ├── paleoclimate_readme.md
│   └── climate_readme.md
├── data/                   # All program data files
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
├── star_data/              # Protected stellar cache
│   ├── star_properties_distance.pkl (2.6 MB)
│   ├── star_properties_magnitude.pkl (31.8 MB)
│   ├── hipparcos_data_distance.vot (899 KB)
│   ├── hipparcos_data_magnitude.vot (193 KB)
│   ├── gaia_data_distance.vot (9.8 MB)
│   ├── gaia_data_magnitude.vot (291 MB)
│   └── *_metadata.json files
└── reports/                # Generated analysis reports
    ├── last_plot_report.json
    ├── last_plot_data.json
    └── report_*.json (archived with timestamps)
```

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

**osculating_cache.json**

- JPL Horizons orbital elements (a, e, i, ω, Ω, TP) for 40+ objects
- Epoch tracking and per-object refresh intervals
- Center-body aware keys for barycenter views

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
| Osculating cache | <1 MB | Orbital elements |
| Climate data | <1 MB | CO₂ measurements |

## Contributing

Contributions are welcome! This project is maintained by a single developer but welcomes community input.

**Areas of Interest:**

- Additional spacecraft mission data
- Enhanced solar system structure visualizations
- Improved stellar classification algorithms
- Exoplanetary system support
- Performance optimizations for large datasets
- Cross-platform testing (Mac, Linux)
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

**Last Updated:** December 2025 (v1.5 - TNO Satellites & Analytical Fallback)

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
