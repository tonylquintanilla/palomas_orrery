# Last updated: February 16, 2026

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
8. [Galactic Center Visualization](#galactic-center-visualization)
9. [Social Media Export](#social-media-export)
10. [Web Gallery](#web-gallery)
11. [Module Reference](#module-reference)
12. [Data Files](#data-files)
13. [Contributing](#contributing)
14. [License](#license)
15. [Contact](#contact)

## Overview

Paloma's Orrery combines scientific accuracy with visual beauty, making astronomy accessible to students, educators, and space enthusiasts. Created by civil & environmental engineer Tony Quintanilla.

**Key Capabilities:**

- Real-time planetary and spacecraft positions from JPL Horizons
- Interactive 3D solar system with 100+ objects
- Comet visualization with dual-tail structures (dust and ion tails)
- Exoplanet system visualization (11 planets in 3 systems including binary stars)
- Pluto-Charon binary planet visualization with true barycentric orbital mechanics
- TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2)
- Galactic Center visualization (S-stars orbiting Sagittarius A*)
- Stellar neighborhood mapping (123,000+ stars)
- Planetary and solar interior visualizations (with reference-frame independent rendering)
- Spacecraft trajectory two-layer visualization (full mission + plotted period)
- Animation system with static shell optimization (45% memory reduction)
- HR diagrams and stellar analysis
- Climate data preservation hub
- Forensic Heat Wave Analysis: 3D KML generator for wet-bulb temperature extremes
- Unified save system with CDN/offline HTML options
- Social media export: 9:16 portrait HTML for Instagram Reels and YouTube Shorts
- Web gallery at [palomasorrery.com](https://palomasorrery.com/) -- shareable interactive visualizations, no install required
- Resizable GUI columns with persistent window layout

**Resources:**

- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery)
- [Web Gallery](https://palomasorrery.com/) -- interactive visualizations in your browser
- [Instagram: @palomas_orrery](https://www.instagram.com/palomas_orrery/)
- [Video Tutorials](https://www.youtube.com/@tony_quintanilla/featured)
- Contact: <tonyquintanilla@gmail.com>

## Quick Start

### Standalone Executables (No Python Required)

Download from the [GitHub Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases):

| Platform | Download | Size |
|----------|----------|------|
| Windows 10/11 | `palomas_orrery.zip` | ~469 MB |
| macOS 10.15+ | [Available from webpage](https://sites.google.com/view/tony-quintanilla) | ~300 MB |
| Linux | Python source only | See below |

**Windows:** Extract, double-click `START_HERE.bat`

**macOS:** Download from [Tony's webpage](https://sites.google.com/view/tony-quintanilla) (iCloud link). Extract, double-click `start_orrery.command` (right-click -> Open first time to bypass Gatekeeper)

**Linux:** See [Linux Installation](#linux-installation) below. After setup, double-click `start_orrery.desktop` to launch.

### Python Source Code (All Platforms)

Download `palomas_orrery_2_1_zip.zip` (~222 MB) from the [Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases). This includes all Python code AND data files.

**Quick start:**

```bash
# 1. Extract the ZIP file
# 2. Install Python 3.11-3.13 with PATH enabled
# 3. Open terminal in the extracted folder
cd palomas_orrery

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run
python palomas_orrery.py
```

**Alternative (git clone):** Clone the repo for code only, then copy `data/` and `star_data/` folders from the release ZIP.

**New to Python?** See the [detailed installation guide below](#installation)

### Linux Installation

Download the latest release ZIP from the [Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases) and extract it.

**Ubuntu/Debian (tested on Linux Mint 22):**

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install python3 python3-pip python3-tk python3-pil.imagetk

# 2. Navigate to extracted folder
cd palomas_orrery_cross_platform

# 3. Install Python dependencies (--break-system-packages required on modern Ubuntu/Debian)
pip install -r requirements.txt --break-system-packages

# 4. Run
python3 palomas_orrery.py
```

**Fedora/RHEL:**

```bash
sudo dnf install python3 python3-pip python3-tkinter python3-pillow-tk
pip install -r requirements.txt
```

**Arch Linux:**

```bash
sudo pacman -S python python-pip tk python-pillow
pip install -r requirements.txt
```

**Important Notes:**

- `python3-tk` provides the GUI toolkit (not available via pip)
- `python3-pil.imagetk` provides ImageTk for matplotlib's Tk backend
- The `--break-system-packages` flag is required on Ubuntu 24.04+ and Debian 12+ due to PEP 668 (externally managed environments). This is safe for desktop applications.

**Known Linux Display Issues:**

The GUI may have minor cosmetic issues on some Linux window managers:

- Middle column buttons may appear slightly clipped
- Text panels may overflow their borders slightly

These are cosmetic only - all functionality works correctly. The visualizations open in your web browser and display perfectly.

### Staying Up to Date

**Releases** (v2.1.0, etc.) include everything: Python code and seed data files (orbit cache, stellar catalogs, climate data).

**Between releases**, the GitHub repository has the latest Python code. Data files aren't in the repo (via .gitignore) - they're generated and updated locally through your own use.

**Easy update (recommended):**

| Platform | File | Usage |
|----------|------|-------|
| Windows | `UPDATE_CODE.bat` | Double-click |
| macOS | `update_code.sh` | Double-click (or run in terminal) |
| Linux | `update_code.desktop` | Double-click (may need to right-click → "Allow Launching" first) |

The script automatically connects to GitHub and pulls the latest Python and README files. Your data files are preserved.

**Manual update (if you prefer):**

```bash
cd palomas_orrery

# First time only:
git init
git remote add origin https://github.com/tonylquintanilla/palomas_orrery.git
git fetch origin
git reset --hard origin/main

# Future updates:
git pull
```

**What gets updated:**

- Python files (`*.py`) - updated to latest
- README files - updated to latest  
- Data files (`data/`, `star_data/`) - preserved (not in repo)

## Installation

### Prerequisites

- **Windows 10/11, macOS 10.15+, or Linux** (all tested and supported)
- **Python 3.11 to 3.13** (tested and verified compatible)
  - As of January 2026, Python 3.13 is recommended
  - Python 3.14 was just released - wait 1-2 months before using it
- **Git** (optional but recommended)
- **520MB free disk space** (includes all cache files and code)
- **Internet connection** (for initial setup and fetching new objects)
- - **Google Earth Pro** (optional, free) - Required only for viewing Forensic Heat Wave KML visualizations. Download from [google.com/earth/versions](https://www.google.com/earth/versions/#earth-pro)

### Step-by-Step Installation Guide for Beginners

This guide assumes you're new to Python and command-line tools. We'll walk through everything!

#### Step 1: Install Git (Optional but Recommended)

Git makes it easy to download and update the project. If you prefer, you can skip this and download a ZIP file instead (see Step 3, Option B).

**To install Git:**

1. Go to [git-scm.com/downloads](https://git-scm.com/downloads)
2. Download the installer for Windows
3. Run the installer:
   - **Important:** When you see the screen asking about additional options, **check the box for "Additional icons -> On the Desktop"**
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
   - Solution: Uninstall Python (Control Panel -> Programs), then reinstall and make sure you check "Add Python to PATH"

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
   cd Documents
   ```

4. **Clone the repository:**

   ```bash
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   ```

5. **Navigate into the project folder:**

   ```bash
   cd palomas_orrery
   ```

**Option B - Download ZIP (No Git Required):**

1. Go to [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to your Documents folder
5. Open Command Prompt and navigate to the folder:

   ```bash
   cd Documents\palomas_orrery-main
   ```

#### Step 4: Download Data Files

The git repository contains code only. Data files are available from the releases page.

1. Go to the [Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases)
2. Download the latest release ZIP (e.g., `Palomas_Orrery_v2.2.0_Windows.zip`)
3. Extract ONLY these folders into your `palomas_orrery` directory:
   - `data/` (orbit_paths.json and climate data)
   - `star_data/` (stellar catalog files)

**Alternative:** Download the full release ZIP and use it directly instead of git clone - it includes everything.

#### Step 5: Install Python Dependencies

The program needs several Python libraries to run.

1. **Make sure you're in the project folder:**

   ```bash
   cd Documents\palomas_orrery
   ```

2. **Install all required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

   - This will download and install about 15 libraries
   - It may take 2-5 minutes depending on your internet speed
   - You'll see lots of text scrolling by - that's normal!

3. **Verify installation:**

   ```bash
   pip list
   ```

   - You should see libraries like: astropy, astroquery, plotly, numpy, pandas

#### Step 6: Run Paloma's Orrery

You're ready to launch!

```bash
python palomas_orrery.py
```

**What to expect:**

- First launch may take 30-60 seconds as caches are loaded
- The main window will appear with checkboxes for planets and other objects
- Select objects you want to visualize
- Click "Plot" to see a 3D visualization in your browser

**Troubleshooting first run:**

- If you see "ModuleNotFoundError": Run `pip install -r requirements.txt` again
- If the window doesn't appear: Check for error messages in Command Prompt
- If plots don't open: Make sure you have a default web browser set

### macOS-Specific Notes

**Installing Python on macOS:**

1. **Option A - Using Homebrew (Recommended):**

   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python@3.13
   ```

2. **Option B - Download from python.org:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download the macOS installer
   - Run the installer package

**Running on macOS:**

```bash
# Navigate to project folder
cd ~/Documents/palomas_orrery

# Install dependencies
pip3 install -r requirements.txt

# Run
python3 palomas_orrery.py
```

**Note:** Use `python3` and `pip3` instead of `python` and `pip` on macOS.

## Usage

### Basic Operations

**Creating a Solar System Plot:**

1. Launch the application
2. Check the boxes for objects you want to see (planets, asteroids, comets)
3. Set your preferred date range
4. Choose a center object (Sun by default)
5. Click "Plot" to generate the visualization
6. Save your visualization when prompted

**Saving Visualizations:**

When you create any visualization, a save dialog appears with three options:

- **Interactive HTML - Standard (~10 KB):** Small file, requires internet to view
- **Interactive HTML - Offline (~5 MB):** Larger file, works without internet
- **Static PNG image:** Non-interactive image file

The save dialog remembers your last save location within each session.

**Animating Orbital Motion:**

1. Select your objects
2. Choose an animation time step (day, week, month, year)
3. Click the animation button
4. Watch objects move along their orbits
5. Save the animation as an interactive HTML file

**Spacecraft Trajectories:**

1. Navigate to the spacecraft section
2. Select missions like:
   - Voyager 1 and 2 (interstellar space)
   - Parker Solar Probe (close to the Sun)
   - New Horizons (beyond Pluto)
   - James Webb Space Telescope
3. Enable trajectory visualization to see their paths
4. Set date range to view historical positions or future predictions
5. In static and animated plots, see two trajectory layers:
   - **Full Mission** (mission color) - Complete trajectory from launch to end
   - **Plotted Period** (yellow) - Just the dates you selected

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

1. Look for the green Earth indicator next to Earth's shell checkbox
2. Enable to access climate data visualizations
3. View the Keeling Curve (CO2 measurements from 1958-2025)
4. See [climate_readme.md](climate_readme.md) for complete documentation

### Advanced Features

**Animation Controls:**

- Use time step controls to animate orbital motion
- Watch days, months, or years of evolution
- Follow spacecraft trajectories through their missions
- Shell visualizations (rings, atmospheres, radiation belts) now appear in animations without memory explosion

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
- View semi-transparent overlays on solar system plots
- Accurate relative scaling

**Exoplanet Systems:**

- Three fully modeled systems available:
  - **TRAPPIST-1:** 7 Earth-sized planets in tight orbits
  - **TOI-1338:** Circumbinary planet (orbits two stars)
  - **Kepler-16:** "Tatooine" - planet with binary star sunset
- Includes binary star orbital mechanics
- Temperature-based star coloring

## Features

### Solar System Visualization

- **100+ Solar System Objects:** Major planets, dwarf planets, asteroids, comets
- **Real-time Ephemerides:** Direct JPL Horizons API integration
- **Osculating Elements:** Properly calculated orbital paths
- **Lagrange Points:** L1-L5 for Earth-Moon and Sun-Earth systems
- **Trajectory Visualization:** Historical and predicted spacecraft paths
- **Animation System:** Time-evolution with optimized shell rendering

### Stellar Neighborhood

- **123,000+ Stars:** Combined Gaia DR3 and Hipparcos catalogs
- **HR Diagrams:** Temperature-luminosity relationship visualization
- **3D Star Maps:** Interactive exploration of nearby space
- **Stellar Classification:** Spectral types with accurate colors
- **Proper Motion:** Star movement over time

### Planetary Science

- **Interior Models:** Cross-sections of all major bodies
- **Atmosphere Visualization:** Gas giants and terrestrial planets
- **Ring Systems:** Saturn, Uranus, Neptune with accurate parameters
- **Satellite Systems:** Major moons with orbital mechanics

### Earth System Science

- **Climate Data Hub:** CO2, temperature, sea level, ice extent
- **Paleoclimate Records:** 540 million years of Earth history
- **Data Preservation:** Systematic archiving of threatened datasets
- **Forensic Heat Analysis:** Visualizes "invisible" wet-bulb temperature disasters (1948–2025).

### Galactic Center

- **S-Star Visualization:** Stars orbiting Sagittarius A* black hole
- **Relativistic Effects:** Schwarzschild precession (rosette patterns)
- **Observational Fidelity:** Phase offsets from real periapsis measurements
- **Newton vs Einstein:** Visual comparison of orbital predictions

## Architecture

### Design Philosophy

- **Accuracy First:** All calculations use established astronomical methods
- **Visual Clarity:** Complex data presented intuitively
- **Offline Capability:** Works without internet after initial setup
- **Cross-Platform:** Windows, macOS, and Linux supported

### Technical Stack

- **Python 3.11-3.13:** Core language
- **Plotly:** Interactive 3D visualizations
- **CustomTkinter:** Modern GUI framework
- **Astropy/Astroquery:** Astronomical calculations and data access
- **NumPy/Pandas:** Numerical computing and data handling

### Data Pipeline

1. **Acquisition:** JPL Horizons, VizieR, SIMBAD queries
2. **Caching:** Local storage with validation and backup
3. **Processing:** Coordinate transforms, orbital calculations
4. **Visualization:** Interactive HTML with Plotly
5. **Export:** CDN or offline HTML, PNG images
6. **Gallery:** JSON extraction, GitHub Pages deployment at palomasorrery.com

### Development Complexity

Paloma's Orrery is not enterprise software. Commercial codebases are orders
of magnitude larger, maintained by teams of hundreds over decades. But for a
project built by a single developer without formal CS training, using
conversational AI collaboration, the system has grown to a scale that is
worth noting.

**System scale:** 75+ Python modules, over 78,000 lines of code, five
parallel data pipelines for position calculations, 1,350+ cached orbital
trajectories across 15 center objects, and a full web publishing pipeline
from desktop application through curation studio to browser-based gallery.

**Domain specificity:** Coordinate frame errors look plausible but are
physically wrong -- an orbit plotted in the equatorial frame when the data
is ecliptic appears rotated by 23.4 degrees, and nothing will error out.
The system handles osculating orbital elements, Schwarzschild precession,
binary star mass ratios, and the distinction between JPL ephemeris data,
calculated Keplerian elements, and cached approximations. Visual
verification catches physics errors that code review misses.

**Pipeline depth:** A change to hover text formatting can touch the desktop
app's trace generation, the social media export parser, the Gallery Studio's
hover routing, the JSON converter's extraction, and the web gallery's
display logic. Five consumers of the same data, each with its own path.

**What makes it interesting:** The complexity-to-team-size ratio. This is
the kind of system that would traditionally require a small team of
specialists -- astronomical software, web development, GUI design, data
pipeline engineering. Conversational AI collaboration compresses that:
the developer provides vision, domain knowledge, and judgment while AI
partners handle implementation, pattern recognition, and documentation.
The conversation is the development environment, and the accumulated
context across months of sessions shapes every decision. This project
would not have been possible before AI-assisted development. It began in
September 2024 and has grown alongside the rapidly improving capabilities
of the AI models themselves.

## Earth System Visualization

Access the Earth System Hub from the main interface to explore climate data:

**Current Monitoring (1958-present):**

- Atmospheric CO2 (Mauna Loa Observatory)
- Global temperature anomalies (NASA GISS)
- Arctic sea ice extent (NSIDC)
- Global mean sea level (NOAA)

**Forensic Heat Wave Analysis:**
- **Tool:** `earth_system_generator.py`
- **Output:** 3D KML layers for Google Earth Pro (Spikes, Heatmap, Impact)
- **Viewer:** [Google Earth Pro](https://www.google.com/earth/versions/#earth-pro) (free desktop application, required to view KML layers)
- **Scope:** 27 historical and modern events (NYC 1948 to US Grid 2025)
- **Metric:** Wet-Bulb Temperature ($T_w$) vs. Biological Limits (31 degC)
- **Documentation:** See [wet_bulb_temperature_readme.md](wet_bulb_temperature_readme.md)

**Paleoclimate Records:**

- 800,000-year ice core CO2 (EPICA Dome C)
- 5 million-year benthic stack (LR04)
- 12,000-year Holocene reconstruction (Temp12k)
- 540 million-year Phanerozoic temperatures

**Data Sources:**

- Scripps CO2 Program at Mauna Loa Observatory
- NOAA Global Monitoring Laboratory
- Additional sources as datasets are integrated

## Galactic Center Visualization

The Galactic Center modules visualize S-stars orbiting Sagittarius A*, the supermassive black hole at the center of our galaxy.

**Features:**

- **The Fantastic Four:** S2, S62, S4711, S4714 - stars with the most extreme orbits
- **Relativistic Precession:** General relativity causes orbits to precess, creating rosette patterns
- **Observational Data:** Orbital phases calculated from actual periapsis measurements (GRAVITY Collaboration)
- **Unified Colorscale:** Compare precession rates visually across different stars

**Modules:**

| Module | Purpose |
|--------|---------|
| `sgr_a_star_data.py` | S-star catalog with orbital parameters and physical properties |
| `sgr_a_visualization_core.py` | Static visualization of S-star orbits |
| `sgr_a_visualization_animation.py` | Animated orbital motion (Kepler's Second Law) |
| `sgr_a_visualization_precession.py` | Schwarzschild precession and Newton vs Einstein comparison |
| `sgr_a_grand_tour.py` | Complete dashboard with mode switching and zoom controls |

**Running Galactic Center Visualizations:**

```bash
# Static visualization
python sgr_a_visualization_core.py

# Animated orbits
python sgr_a_visualization_animation.py

# Relativistic precession
python sgr_a_visualization_precession.py

# Complete Grand Tour dashboard
python sgr_a_grand_tour.py
```

## Social Media Export

Export any orrery visualization as a 9:16 portrait HTML file for Instagram Reels and YouTube Shorts. The social view splits the screen into a 3D scene (top 60%) and a persistent info panel (bottom 40%) that displays the rich data normally hidden in ephemeral hover tooltips.

**How to use:** Click **Social Media Export** in the GUI, select which objects to include, choose a save location, and the HTML opens in your browser. Record with any screen capture tool at 1080x1920 resolution. No cropping needed -- the layout is locked to 9:16 with invisible black margins.

**Key features:**

- 9:16 portrait layout locked via CSS (works in any browser window size)
- Persistent info panel shows object name, coordinates, distance, velocity
- Click or hover to select objects; panel holds last selection
- Animation support with Play/Pause and date slider
- Camera angle preserved during animation playback
- Trace selection dialog to choose which objects appear
- Save dialog with timestamped defaults and directory memory
- CDN (~10 KB) or offline (~5 MB) Plotly.js options

See [social_media_readme.md](social_media_readme.md) for full documentation.

## Web Gallery

Browse interactive visualizations online at [palomasorrery.com](https://palomasorrery.com/) -- no download, no install, no Python required. Tap a link and explore.

**How it works:** The desktop app exports visualizations as HTML. A converter extracts the Plotly figure data into lightweight JSON files. The gallery viewer (a single-page HTML/CSS/JS app hosted on GitHub Pages) loads them with Plotly.js from CDN. The result is a shareable web gallery where every visualization has its own direct link.

**Features:**

- Dark space theme with gold accent matching the desktop app aesthetic
- Two modes: Desktop (landscape) and Mobile (portrait) with auto-detection
- Category-grouped navigation (Solar System, Inner Planets, Stellar, Climate, etc.)
- Shareable deep links per visualization (e.g., palomasorrery.com/#earth-birthday-2025)
- Floating info cards on mobile (tap objects for details)
- 3D zoom buttons on mobile (synthetic wheel events for Plotly.js 3D scenes)
- Light/dark theme auto-detection preserves original plot colors
- Custom domain with HTTPS (palomasorrery.com)

**Gallery pipeline:**

```
Desktop App -> save_plot() -> HTML export
    -> gallery_studio.py -> per-plot curation (optional)
    -> json_converter.py -> JSON + gallery_metadata.json
    -> gallery_editor.py -> curate titles, categories, ordering
    -> GitHub Pages (index.html) -> palomasorrery.com
```

**Gallery management tools** (in website repo `tools/` folder):

| Tool | Purpose |
|------|---------|
| `gallery_studio.py` | Per-plot curation GUI -- background, fonts, margins, portrait preset with info panel |
| `json_converter.py` | Extracts Plotly figure data from HTML exports to JSON |
| `gallery_editor.py` | Tkinter GUI for editing metadata, categories, and ordering |
| `gallery_config.json` | Single source of truth for category definitions (shared by all tools) |

See [web_gallery_handoff.md](web_gallery_handoff.md) for full technical documentation.

## Module Reference

**For a complete index of all Python modules in the project, see [MODULE_INDEX.md](MODULE_INDEX.md).**

The following sections highlight the primary modules organized by function. Use MODULE_INDEX.md to search for specific functionality (save, cache, coordinates, etc.) or to understand the complete codebase structure.

### Primary Modules

| Module | Purpose |
|--------|---------|
| `palomas_orrery.py` | Main application (~8,400 lines) - GUI, plot_objects(), animate_objects(), trajectory layers, animation shells |
| `celestial_objects.py` | Object and shell definitions data module (169 objects, 78 shell checkboxes) - separated from GUI for maintainability |
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
| `*_visualization_shells.py` | Planetary interior cross-sections (15 modules) |
| `comet_visualization_shells.py` | Scientifically accurate comet rendering with dual-tail structures |
| `orbital_param_viz.py` | Orbital element visualization |
| `earth_system_visualization_gui.py` | Earth system data hub with climate visualizations |
| `coordinate_system_guide.py` | Educational J2000 ecliptic coordinate reference |

### Galactic Center Modules

| Module | Purpose |
|--------|---------|
| `sgr_a_star_data.py` | S-star catalog with orbital and physical properties |
| `sgr_a_visualization_core.py` | Static S-star orbit visualization |
| `sgr_a_visualization_animation.py` | Animated orbital motion with Kepler's Second Law |
| `sgr_a_visualization_precession.py` | Schwarzschild precession and Newton vs Einstein |
| `sgr_a_grand_tour.py` | Complete Galactic Center dashboard |

### Save and Export Utilities

| Module | Purpose |
|--------|---------|
| `save_utils.py` | Unified save system for all visualizations - CDN/offline HTML, PNG export, session directory memory, cross-platform dialogs |
| `social_media_export.py` | 9:16 portrait HTML export for Instagram Reels / YouTube Shorts with persistent info panel |
| `shutdown_handler.py` | Graceful shutdown, thread management, delegates to save_utils |
| `palomas_orrery_helpers.py` | Animation helpers, show_animation_safely delegates to save_utils |

**Save System Features:**

- **Three HTML options:** Standard CDN (~10 KB), Offline (~5 MB), or PNG
- **Session memory:** Remembers last save directory within each session
- **Cross-platform:** Works on Windows, macOS, and Linux
- **Thread-safe:** Handles macOS worker thread restrictions gracefully
- **17 modules** use the unified save system

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
| `fetch_climate_data.py` | Climate data fetcher (Mauna Loa CO2) |

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

The project spans two repositories on disk. They are **siblings** in the
same parent folder (not nested). The orrery repo holds the desktop app;
the website repo holds the web gallery and its tooling.

```
python_work/                     # Parent folder (your workspace)
|
|- orrery/                       # Desktop app repo (palomas_orrery on GitHub)
|  |- *.py                       # Python source code (75+ modules)
|  |- README/                    # Documentation
|  |   |- README.md
|  |   |- social_media_readme.md
|  |   |- paleoclimate_readme.md
|  |   |- climate_readme.md
|  |- data/                      # All program data files
|  |   |- orbit_paths.json (~94 MB)
|  |   |- orbit_paths_backup.json
|  |   |- Climate monitoring (automated)
|  |   |   |- co2_mauna_loa_monthly.json
|  |   |   |- temperature_giss_monthly.json
|  |   |   |- arctic_ice_extent_monthly.json
|  |   |   |- sea_level_gmsl_monthly.json
|  |   |- Climate monitoring (manual)
|  |   |   |- ocean_ph_hot_monthly.json
|  |   |   |- 3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv
|  |   |- Paleoclimate data
|  |       |- epica_co2_800kyr.json
|  |       |- lr04_benthic_stack.json
|  |       |- temp12k_allmethods_percentiles.csv
|  |       |- 8c__Phanerozoic_Pole_to_Equator_Temperatures.csv
|  |   |- Heat Wave Analysis
|  |       |- weather_cache_*.json       # Cached ERA5 data
|  |       |- *_spikes_*.kml             # Generated risk layers
|  |       |- *_impact_*.kml             # Generated population layers
|  |       |- *_heatmap_*.kml            # Generated thermal layers
|  |- star_data/                  # Protected stellar cache
|  |   |- star_properties_distance.pkl (2.6 MB)
|  |   |- star_properties_magnitude.pkl (31.8 MB)
|  |   |- hipparcos_data_distance.vot (899 KB)
|  |   |- hipparcos_data_magnitude.vot (193 KB)
|  |   |- gaia_data_distance.vot (9.8 MB)
|  |   |- gaia_data_magnitude.vot (291 MB)
|  |   |- *_metadata.json files
|  |- reports/                    # Generated analysis reports
|      |- last_plot_report.json
|      |- last_plot_data.json
|      |- report_*.json (archived with timestamps)
|
|- tonyquintanilla.github.io/    # Website repo (GitHub Pages)
   |- index.html                 # Gallery viewer (single-page app)
   |- gallery/                   # JSON visualization data
   |   |- *.json                 # Converted Plotly figures
   |   |- gallery_metadata.json  # Titles, categories, ordering
   |- tools/                     # Gallery management tools
   |   |- gallery_studio.py      # Per-plot curation GUI
   |   |- json_converter.py      # HTML-to-JSON converter
   |   |- gallery_editor.py      # Metadata editor GUI
   |   |- gallery_config.json    # Category definitions
   |   |- gallery_studio_configs.json  # Saved per-plot settings
   |- gallery_config.json        # Category definitions (root copy)
   |- CNAME                      # Custom domain (palomasorrery.com)
   |- web_gallery_handoff.md     # Technical documentation
   |- README.md
```

**Why two repos?** GitHub Pages requires its own repository. The app repo
stays clean for users who download it. The website repo holds the gallery
viewer and publishing tools. Both are public (required for free GitHub
Pages).

**Cross-repo imports:** gallery_studio.py (in `tools/`) imports
`social_media_export.py` and `constants_new.py` from the `orrery/`
directory. It resolves the path by walking up the directory tree.

### Cache Files (Included in Release)

- `star_properties_distance.pkl` - 9,700 stars within 100 light-years with full properties
- `star_properties_magnitude.pkl` - 123,000 stars to magnitude 9 with properties
- `hipparcos_*.vot` - Hipparcos catalog data (bright stars)
- `gaia_*.vot` - Gaia EDR3 catalog data (faint stars)

**orbit_paths.json** (~94 MB typical)

- Time-indexed orbital position data for 1000+ objects
- Supports multiple reference frames (Sun, planets, moons)
- Includes automatic backup and safety protections

**orbit_paths_backup.json**

- Automatic backup created on startup
- Used for recovery if cache becomes corrupted

**osculating_cache.json**

- JPL Horizons orbital elements (a, e, i, omega, Omega, TP) for 40+ objects
- Epoch tracking and per-object refresh intervals
- Center-body aware keys for barycenter views

### Configuration Files

- `satellite_ephemerides.json` - Satellite orbital elements and physical properties
- `*_metadata.json` - Cache validation metadata and timestamps
- `orrery_config.json` - User preferences and display settings
- `co2_mauna_loa_monthly.json` - Monthly atmospheric CO2 measurements (1958-2025)
- `window_config.json` - Main GUI window geometry, maximized state, and column sash positions
- `star_viz_config.json` - Star visualization GUI window layout

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
| Orbit cache | 94+ MB | Planetary ephemerides |
| Osculating cache | <1 MB | Orbital elements |
| Climate data | <1 MB | CO2 measurements |

## Contributing

Contributions are welcome! This project is maintained by a single developer but welcomes community input.

**Areas of Interest:**

- Additional spacecraft mission data
- Enhanced solar system structure visualizations
- Improved stellar classification algorithms
- Exoplanetary system support
- Performance optimizations for large datasets
- Cross-platform testing (Windows, macOS & Linux all supported!)
- Documentation improvements
- Climate data integration (temperature, sea level, ice extent)

**How to Contribute:**

Suggestions are welcome: <tonyquintanilla@gmail.com>

**Bug Reports:**

- Include Python version and steps to reproduce
- Attach relevant error messages or screenshots

## License

MIT License

Copyright (c) 2025-2026 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

**Author:** Tony Quintanilla
**Email:** <tonyquintanilla@gmail.com>
**GitHub:** [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
**Website:** [palomasorrery.com](https://palomasorrery.com/)
**Instagram:** [@palomas_orrery](https://www.instagram.com/palomas_orrery/)
**YouTube:** [Paloma's Orrery](https://www.youtube.com/@tony_quintanilla/featured)

**Last Updated:** February 2026 (v2.4.0 - Web Gallery, Social Media Export, Galactic Center, Unified Save System & Resizable GUI)

---

**Acknowledgments:**

- [NASA JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/) for planetary ephemerides
- [ESA Gaia Mission](https://www.cosmos.esa.int/web/gaia) for stellar data
- [VizieR catalog service](https://vizier.cds.unistra.fr/) (CDS, Strasbourg)
- [SIMBAD astronomical database](https://simbad.u-strasbg.fr/simbad/)
- [Scripps CO2 Program](https://scrippsco2.ucsd.edu/) for Mauna Loa data
- [GRAVITY Collaboration](https://www.mpe.mpg.de/ir/gravity) for S-star orbital data
- [Astropy](https://www.astropy.org/) and [Astroquery](https://astroquery.readthedocs.io/) development teams
- [Plotly](https://plotly.com/) visualization library
- AI coding assistants: [Anthropic Claude](https://www.anthropic.com/claude), [OpenAI ChatGPT](https://openai.com/chatgpt), [Google Gemini](https://gemini.google.com/)
- Cross-platform compatibility (Windows, macOS & Linux) achieved January 2026
