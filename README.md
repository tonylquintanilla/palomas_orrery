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
- Contact: <tonyquintanilla@gmail.com>

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

3. **Navigate to where you want to save the project:**

   ```bash (command line)
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

5. **Enter the new project folder:**

   You should still be in your Documents folder. Now navigate into the new `palomas_orrery` folder that Git just created:

   ```bash
   cd palomas_orrery
   ```

   **If that doesn't work** (you get "The system cannot find the path specified"):
   - You may have navigated away from Documents
   - Use the full path instead:
  
   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery
   ```

   (Replace `YourName` with your actual Windows username)

   **To verify you're in the right place:**
   - Type: `dir` and press Enter
   - You should see files like `palomas_orrery.py`, `requirements.txt`, and many `.py` files
   - If you don't see these files, you're in the wrong folder

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
   - Click on `cache_files_compressed.zip` to download (117 MB - may take 1-2 minutes)
   - **Note:** You'll also see "Source code (zip)" and "Source code (tar.gz)" - ignore these, you already have the code from Step 3

2. **Extract cache files to your project folder:**
   - Find the downloaded `cache_files_compressed.zip` file (usually in your Downloads folder)
   - **Important:** Don't just click to open it! You need to extract it properly.
   **To access the Extract menu:**
   - **With a mouse:** Right-click on the ZIP file
   - **With a trackpad:** Try one of these:
     - Two-finger tap on the file
     - Tap with two fingers simultaneously
     - Click with one finger while holding a second finger on the trackpad
     - OR use keyboard: Click the file once to select it, then press `Shift+F10`

   - You should see a context menu appear
   - Look for **"Extract All..."** in the menu and click it
   - A window will appear asking where to extract
   - Click **"Browse..."** and navigate to your **`palomas_orrery` folder** (the main project folder where `palomas_orrery.py` is located)
   - If you used Option B (ZIP download), your folder might be called `palomas_orrery-main` instead
   - Click **"Select Folder"**, then click **"Extract"**

   **If you still can't find "Extract All..." or it's easier to just copy:**
   - Single-click the ZIP file to open it (you'll see the contents)
   - Press `Ctrl+A` to select all files inside
   - Press `Ctrl+C` to copy them
   - Open a new File Explorer window and navigate to your **`palomas_orrery` folder** (this is your main project folder)
   - Press `Ctrl+V` to paste all the files there
   - This works perfectly fine and is often simpler!

3. **Verify the files are in the right place:**
   - Open your `palomas_orrery` folder in File Explorer
   - You should see files like:
     - `palomas_orrery.py` (the main program)
     - `star_properties_distance.pkl` (from the cache)
     - `star_properties_magnitude.pkl` (from the cache)
     - Various `.vot` files (from the cache)
     - Many other `.py` files (the program code)
   - **Everything should be together in one folder** - the cache files and the Python code files should all be in the same `palomas_orrery` directory
   - If the cache files are in a subfolder, move them up to the main `palomas_orrery` folder

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

   **If you get an error like "= is not a valid operator. Did you mean == ?":**
   - There's a typo in the requirements.txt file that needs fixing
   - Fix it using Notepad:
     1. Navigate to your `palomas_orrery` folder in File Explorer
     2. Right-click on `requirements.txt` and select "Open with" → "Notepad"
     3. Find the line that says `kaleido=0.2.1`
     4. Change the single `=` to double `==` so it reads `kaleido==0.2.1`
     5. Click File → Save, then close Notepad
     6. Try the `pip install -r requirements.txt` command again

   **If the simple command doesn't work for other reasons, use the manual method:**

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

#### Step 6: Run Paloma's Orrery

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

**Problem:** Visualization features not working properly.

**Solution:**

1. Check your Python version: `python --version`
2. Make sure it's 3.11, 3.12, or 3.13
3. Reinstall plotly and kaleido:

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
- **Storage:** 520MB free disk space (includes all cache files and Python code)
- **Internet:** Required for initial download and for querying objects not in cache
- **Display:** 1280×720 minimum resolution recommended

### Optional: Installing a Code Editor

While not required to run Paloma's Orrery, if you want to explore or modify the code, a good code editor makes it much easier:

**Visual Studio Code (VS Code) - Recommended:**

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install with default options
3. Open VS Code and install the Python extension (search for "Python" in the Extensions panel; View/Extensions)
4. You can then open your entire `palomas_orrery` folder in VS Code: File → Open Folder

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

- JPL Horizons (planetary ephemerides) [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/app.html#/)
- Gaia EDR3 (stellar positions and photometry) [Gaia](https://www.cosmos.esa.int/web/gaia)
- Hipparcos (bright star catalog) [Hipparcos](https://www.cosmos.esa.int/web/hipparcos/catalogues)
- SIMBAD (astronomical database) [SIMBAD](https://simbad.u-strasbg.fr/simbad/)

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
| Distance PKL | 3 MB | Stars within 100 ly |
| Magnitude PKL | 32 MB | Stars to mag 9.0 |
| VOTable files | 1-291 MB each | Raw catalog data |
| Orbit cache | 96+ MB | Planetary ephemerides |

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
**YouTube:** [Paloma's Orrery](https://www.youtube.com/@tony_quintanilla/featured)  

**Last Updated:** October 2025

---

**Acknowledgments:**

- NASA JPL Horizons System for planetary ephemerides
- ESA Gaia Mission for stellar data
- VizieR catalog service (CDS, Strasbourg)
- SIMBAD astronomical database
- Astropy and Astroquery development teams
- Plotly visualization library
- AI coding assistants: Anthropic Claude, OpenAI ChatGPT, Google Gemini
