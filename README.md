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
- **Windows 10/11** (Mac/Linux also supported)
- **Python 3.11 to 3.13** (tested and verified compatible)
- **Git** (optional but recommended)
- **300MB free disk space**
- **Internet connection**

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
   - **✅ CRITICAL:** Check the box that says **"Add Python to PATH"** at the bottom
   - **✅ Also check:** "Install pip"
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

3. **Navigate to your chosen location:**
   ```bash
   cd C:\Users\YourName\Documents
   ```
   (Replace `YourName` with your actual Windows username)

4. **Download the project:**
   ```bash
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   ```
   This will take 30-60 seconds to download.

5. **Enter the project folder:**
   ```bash
   cd palomas_orrery
   ```

**Option B - Download ZIP (No Git required):**

1. **Download the project:**
   - Go to [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
   - Click the green **"Code"** button (top right of the file list)
   - Click **"Download ZIP"**
   - The file `palomas_orrery-main.zip` will download (about 50 MB)

2. **Extract the ZIP file:**
   - Find the downloaded file (usually in your Downloads folder)
   - Right-click on `palomas_orrery-main.zip`
   - Select **"Extract All..."**
   - Choose where to extract (e.g., `C:\Users\YourName\Documents`)
   - Click **"Extract"**
   - Windows will create a folder called `palomas_orrery-main`

3. **Navigate to the folder in Command Prompt:**
   - Press `Windows Key`, type `cmd`, press Enter
   - Type:
   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery-main
   ```
   (Adjust the path to wherever you extracted the files)

#### Step 4: Download Cache Files

**These files are required for star visualizations to work!** They contain pre-downloaded astronomical data so you don't have to wait hours fetching it yourself.

1. **Download the cache:**
   - Go to [github.com/tonylquintanilla/palomas_orrery/releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
   - Find the latest release (look for v1.0.0 or higher)
   - Scroll down to **"Assets"**
   - Click on `palomas_orrery_cache_v1.0.0.zip` to download (120 MB - may take 1-2 minutes)

2. **Extract cache files to your project folder:**
   - Find the downloaded `palomas_orrery_cache_v1.0.0.zip` file
   - Right-click on it and select **"Extract All..."**
   - **IMPORTANT:** For the destination, navigate to your `palomas_orrery` (or `palomas_orrery-main`) folder
   - The cache files should end up in the same folder as `palomas_orrery.py` (not in a subfolder!)
   - Click **"Extract"**

3. **Verify the files are in the right place:**
   - Open your `palomas_orrery` folder in File Explorer
   - You should see files like:
     - `palomas_orrery.py` (the main program)
     - `star_properties_distance.pkl` (from the cache)
     - `star_properties_magnitude.pkl` (from the cache)
     - Various `.vot` files (from the cache)
   - If the cache files are in a subfolder, move them to the main folder

#### Step 5: Install Python Libraries

Python libraries (also called "packages") are additional tools that Paloma's Orrery needs to run. We'll install them all at once.

1. **Make sure you're in the project folder:**
   - In Command Prompt, type:
   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery
   ```
   (Or `palomas_orrery-main` if you downloaded the ZIP)

2. **Install all libraries at once:**
   
   **First, try this simple command:**
   ```bash
   pip install -r requirements.txt
   ```
   This reads the `requirements.txt` file and installs everything automatically. This should take 2-5 minutes.

   **If that doesn't work (you see errors), use the manual method:**
   
   Copy this entire command and paste it into Command Prompt (right-click to paste):
   ```bash
   pip install numpy>=1.24.0 pandas>=2.0.0 scipy>=1.11.0 astropy>=5.3.4 astroquery>=0.4.6 plotly>=5.18.0 kaleido==0.2.1 pillow>=10.0.0 matplotlib>=3.7.0 customtkinter>=5.2.0 requests>=2.31.0 beautifulsoup4>=4.12.0 python-dateutil>=2.8.2 pytz>=2023.3
   ```
   Press Enter and wait. This will take 3-7 minutes depending on your internet speed.

3. **What you'll see during installation:**
   - Lines of text scrolling by (this is normal!)
   - "Collecting [package name]..." - downloading the library
   - "Installing collected packages..." - setting them up
   - "Successfully installed..." at the end - you're done!

4. **If you see errors:**
   - **"pip is not recognized":** Python wasn't added to PATH. Reinstall Python with "Add to PATH" checked.
   - **"Could not install X":** Try installing that specific package separately: `pip install X`
   - **Permission errors:** Try running Command Prompt as Administrator (right-click cmd → "Run as administrator")

#### Step 6: Run Paloma's Orrery!

You're almost there! Now let's start the program.

1. **Make sure you're in the project folder:**
   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery
   ```

2. **Start the program:**
   ```bash
   python palomas_orrery.py
   ```

3. **What to expect:**
   - Command Prompt will show some loading messages (10-30 seconds)
   - A new window will appear with the Paloma's Orrery interface
   - The window has tabs at the top and controls for selecting celestial objects

4. **Important notes:**
   - **Always use** `python palomas_orrery.py` from Command Prompt to run the program
   - **Don't** try to run it by double-clicking `palomas_orrery.py` in File Explorer - this may cause crashes
   - Keep Command Prompt open while using the program - closing it will close Paloma's Orrery

### Troubleshooting Common Issues

#### "python is not recognized as an internal or external command"

**Problem:** Windows can't find Python.

**Solution:**
1. Uninstall Python (Control Panel → Programs and Features → Python → Uninstall)
2. Reinstall Python from python.org
3. **Make sure to check "Add Python to PATH"** during installation
4. Restart your computer
5. Try again

#### "No module named [something]"

**Problem:** A required library is missing.

**Solution:**
1. Install the missing library: `pip install [something]`
2. For example, if you see "No module named plotly", run: `pip install plotly`

#### Plotly or visualization errors

**Problem:** Incompatible Python or Plotly version.

**Solution:**
1. Check your Python version: `python --version`
2. Make sure it's 3.11, 3.12, or 3.13
3. If you're using a brand new Python version (like 3.14 if it just came out), downgrade to 3.13
4. Reinstall plotly and kaleido:
   ```bash
   pip uninstall plotly kaleido
   pip install plotly>=5.18.0 kaleido==0.2.1
   ```

#### Program window doesn't appear

**Problem:** Program starts but no window shows.

**Solution:**
1. Look at Command Prompt for error messages
2. Common issue: Missing cache files
   - Make sure cache files are extracted to the same folder as `palomas_orrery.py`
   - Check that files like `star_properties_magnitude.pkl` exist in your project folder
3. Try running again: `python palomas_orrery.py`

#### "Cache files not found" error

**Problem:** The cache files aren't in the right location.

**Solution:**
1. Make sure you extracted the cache ZIP to the correct folder
2. The cache files should be in the same directory as `palomas_orrery.py`
3. If they're in a subfolder like `palomas_orrery_cache_v1.0.0`, move them up one level
4. You should see both Python files (`.py`) and cache files (`.pkl`, `.vot`, `.json`) together

#### Git clone fails

**Problem:** `git clone` command doesn't work.

**Solution:**
1. If you get "git is not recognized": Git isn't installed. Either install Git (Step 1) or use Option B (download ZIP)
2. If you get a network error: Check your internet connection
3. Alternative: Just download the ZIP file (Step 3, Option B)

#### ZIP file won't extract

**Problem:** Can't extract the downloaded ZIP files.

**Solution:**
1. Right-click the ZIP file
2. Select "Extract All..." (not "Open" or "Open with")
3. Choose destination folder carefully
4. Click "Extract"
5. If Windows won't extract it, try using 7-Zip (free software: 7-zip.org)

### Your First Session

Once everything is installed and the program is running:

1. **The main window appears** with several tabs at the top
2. **Try plotting the solar system:**
   - Check boxes for planets you want to see (Earth, Mars, Jupiter, etc.)
   - Make sure today's date is selected
   - Click "Plot Entered Date"
   - An interactive 3D visualization will appear!
   - You can rotate it with your mouse

3. **Explore star visualizations:**
   - Click the "2D and 3D Star Visualizations" button
   - Enter a distance (try 100 light-years) or magnitude (try 6.0)
   - Choose "Create HR Diagram" or "Create 3D Plot"
   - These use the cache files you downloaded - no waiting!

4. **Tips for new users:**
   - The program saves your work automatically
   - Internet is only needed for new celestial objects not in the cache
   - You can save visualizations as PNG images or interactive HTML files
   - HTML files can be shared with anyone - they open in any web browser!

### System Requirements Summary

- **Operating System:** Windows 10/11, macOS 10.14+, or Linux
- **Python Version:** 3.11, 3.12, or 3.13 (thoroughly tested)
- **Memory (RAM):** 2GB minimum, 4GB recommended for large star datasets
- **Storage:** 300MB (includes all cache files)
- **Internet:** Required for initial download and for querying objects not in cache
- **Display:** 1280×720 minimum resolution recommended

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

### Features

**Solar System Visualization:**
- Real-time positions from JPL Horizons database
- 100+ objects including planets, moons, asteroids, comets
- Accurate orbital mechanics
- Historical and future date support
- Multiple reference frame options (heliocentric, barycentric, etc.)

**Stellar Astronomy:**
- 123,000+ stars in the magnitude 9 catalog
- 9,700+ stars within 100 light-years
- Hertzsprung-Russell diagrams with spectral classification
- 3D stellar neighborhood maps
- Distance and brightness filtering
- SIMBAD integration for detailed stellar properties

**Data Sources:**
- JPL Horizons (planetary ephemerides)
- Gaia EDR3 (stellar positions and photometry)
- Hipparcos (bright star catalog)
- SIMBAD (astronomical database)

**Interactive Features:**
- 3D rotation and zoom
- Object selection and filtering
- Date/time controls
- Multiple coordinate systems
- Export to PNG or HTML
- Detailed object information on hover

## Architecture

### Data Flow

1. **Acquisition**: Fetch astronomical data from JPL Horizons, VizieR catalogs, and SIMBAD
2. **Processing**: Calculate positions, velocities, and stellar parameters
3. **Caching**: Store processed data with metadata for instant reuse
4. **Visualization**: Generate interactive Plotly visualizations
5. **Analysis**: Create scientific reports and statistical summaries

### Performance Optimizations

- **Incremental caching**: Only fetch new data, reuse existing
- **Smart cache management**: Automatic validation and repair
- **Compressed storage**: Efficient binary formats (PKL, VOTable)
- **Rate limiting**: Respectful API usage with automatic throttling
- **Batch processing**: Group queries for efficiency

## Module Reference

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
| `orbital_param_viz.py` | Orbital element visualization |

### Cache Management

| Module | Purpose |
|--------|---------|
| `vot_cache_manager.py` | VizieR cache with atomic saves and validation |
| `incremental_cache_manager.py` | Smart incremental fetching for large datasets |
| `create_cache_backups.py` | Automatic backup creation utility |
| `verify_orbit_cache.py` | Orbit cache validation and repair |

### Analysis Modules

| Module | Purpose |
|--------|---------|
| `object_type_analyzer.py` | Stellar classification and type analysis |
| `report_manager.py` | Scientific report generation with statistics |
| `stellar_parameters.py` | Temperature, luminosity, and HR calculations |
| `celestial_coordinates.py` | RA/Dec coordinate system conversions |
| `stellar_data_patches.py` | Data quality improvements and corrections |

### Orbital Calculations

| Module | Purpose |
|--------|---------|
| `idealized_orbits.py` | Simplified circular/elliptical orbits |
| `refined_orbits.py` | High-precision orbital mechanics |
| `orrery_integration.py` | Integration layer for orbit selection |
| `create_ephemeris_database.py` | Satellite ephemeris database builder |

## Data Files

### Cache Files (Included in Release)

- `star_properties_distance.pkl` - 9,700 stars within 100 light-years with full properties
- `star_properties_magnitude.pkl` - 123,000 stars to magnitude 9 with properties
- `hipparcos_*.vot` - Hipparcos catalog data (bright stars)
- `gaia_*.vot` - Gaia EDR3 catalog data (faint stars)
- `orbit_paths.json` - JPL Horizons orbital cache (1,365 objects)

### Configuration Files

- `satellite_ephemerides.json` - Satellite orbital elements and physical properties
- `*_metadata.json` - Cache validation metadata and timestamps
- `orrery_config.json` - User preferences and display settings

### Generated Reports

- `last_plot_report.json` - Current session analysis results
- `last_plot_data.json` - Data exchange between processes
- `reports/` - Archived timestamped analysis reports

### Cache File Sizes

| File Type | Approximate Size | Description |
|-----------|------------------|-------------|
| Distance PKL | 15 MB | Stars within 100 ly |
| Magnitude PKL | 85 MB | Stars to mag 9.0 |
| VOTable files | 10-20 MB each | Raw catalog data |
| Orbit cache | 5-10 MB | Planetary ephemerides |

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

**How to Contribute:**
1. Fork the repository on GitHub
2. Create a feature branch
3. Make your changes with clear commit messages
4. Test thoroughly
5. Submit a pull request with a description of changes

**Code Style:**
- Follow PEP 8 Python style guidelines
- Include docstrings for functions and classes
- Comment complex algorithms
- Add error handling for external data sources

**Bug Reports:**
- Use GitHub Issues
- Include Python version, OS, and steps to reproduce
- Attach relevant error messages or screenshots

## License

MIT License

Copyright (c) 2025 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

**Author:** Tony Quintanilla  
**Email:** tonyquintanilla@gmail.com  
**GitHub:** [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)  
**Website:** [tonylquintanilla.github.io/palomas_orrery](https://tonylquintanilla.github.io/palomas_orrery/)  
**YouTube:** [@tony_quintanilla](https://www.youtube.com/@tony_quintanilla/featured)  

**Last Updated:** September 2025

---

**Acknowledgments:**
- NASA JPL Horizons System for planetary ephemerides
- ESA Gaia Mission for stellar data
- VizieR catalog service (CDS, Strasbourg)
- SIMBAD astronomical database
- Astropy and Astroquery development teams
- Plotly visualization library