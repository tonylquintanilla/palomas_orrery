# 🌌 Paloma's Orrery

## Introduction

Paloma's Orrery is an advanced astronomical visualization software that brings the cosmos to your desktop. This comprehensive tool transforms complex astronomical data into interactive visualizations of our solar system and stellar neighborhood. The visualizations are created with a Python program with the assistance of AI assistants, including Claude, ChatGPT, Gemini and DeepSeek. This Orrery is under active development as new functionalities, objects and visualizations are implemented.

Created by a civil and environmental engineer with a passion for space exploration, Paloma's Orrery bridges the gap between scientific accuracy and visual beauty, making astronomy accessible to educators, students, and space enthusiasts.

-- Tony Quintanilla, Chicago, July 13, 2025

   tonyquintanilla@gmail.com
   website: https://sites.google.com/view/tony-quintanilla
   GitHub Web Page: https://tonylquintanilla.github.io/palomas_orrery/ 
   GitHub Repository: https://github.com/tonylquintanilla/palomas_orrery
   Tube Playlist: https://www.youtube.com/playlist?list=PLEGbeeSDrKst8837R5builvhDlTs7Shpm

## 📜 Open Source & Free to Use

**MIT License** - This software is completely free and open source:

- ✅ **Download & Use**: Free for personal, educational, and commercial use
- ✅ **Modify & Customize**: Adapt the code for your specific needs
- ✅ **Redistribute**: Share your modifications with others
- ✅ **No Restrictions**: No licensing fees, ever
- ✅ **Full Source Code**: Everything is available on GitHub

**What this means**: You can download, install, use, modify ("mod"), and even sell applications based on this code. The only requirement is to include the original MIT license notice. Perfect for educators, researchers, students, and space enthusiasts who want to build upon this foundation.

### 🤖 Development Approach: AI-Assisted "Vibe Coding"

**Honest transparency**: This entire project was developed using AI assistants (Claude, ChatGPT, Gemini, DeepSeek) in what the creator calls "vibe coding" - an iterative, vision-driven approach where:

- **AI assistants provided**: Python setup guidance, code generation, library recommendations, debugging help, and technical solutions
- **Human developer provided**: Vision, objectives, testing, validation, astronomical accuracy requirements, and performance management
- **Collaborative result**: A sophisticated astronomical tool that combines AI's coding capabilities with human domain expertise

**Why this matters for you:**
- If you encounter Python environment issues, the same AI assistants that helped build this can help you troubleshoot
- The codebase is designed to be readable and modifiable, even for those learning Python
- This approach demonstrates that complex scientific software can be created through human-AI collaboration
- Bug reports and feature requests benefit from this same collaborative debugging approach
- You can expand and modify this code, it is "freeware" under the MIT License.

**Developer's role evolution**: Starting with vision and requirements, gradually learning Python through the process, now handling basic coding tasks like adding new celestial objects and ephemeris data.

## ✨ What Makes It Special

### Scientific Accuracy Meets Visual Beauty
- **Real astronomical data** from NASA JPL Horizons, ESA Hipparcos/Gaia, and SIMBAD databases
- **Time-accurate positioning** for planets, moons, asteroids, comets, and spacecraft from JPL Horizons system
- **Stellar neighborhood mapping** with accurate 3D positioning for 118,000+ stars from Hipparcos and Gaia catalogs
- **Intelligent cache management** with selective updates and automatic data cleanup
- **Enhanced orbital mechanics** with actual and idealized orbits using JPL Horizons ephemerides

### Advanced Planetary Shell Visualization System
- **Comprehensive planetary anatomy**: Core, mantle, crust, atmosphere, magnetosphere, and Hill sphere visualization
- **Detailed solar and planetary shells** 
  - **Sun**: Core, convective zone, radiative zone, photosphere, corona, solar wind 
  - **Terrestrial planets**: Differentiated core-mantle-crust structures with atmospheres
  - **Gas giants**: Complex layered atmospheres, metallic hydrogen cores, ring systems, radiation belts, magnetospheres
  - **Ice giants**: Unique mantle compositions and tilted magnetospheres
  - **Dwarf planets**: Specialized structures including Pluto's haze layers and atmosphere
  - **Planet 9**: Hypothetical ice giant structure visualization
- **Interactive shell controls** allowing selective visualization of individual planetary layers
- **Magnetosphere modeling** including plasma torus systems around Jupiter and Saturn

### Advanced Features & Intelligent Data Management
- **Smart selective caching** only fetches data for selected objects, avoiding unnecessary requests
- **Special fetch mode** for experimental plotting without cache modification
- **Automatic cache backup** on startup
- **Cache validation and repair** system that automatically detects and fixes corrupted data entries
- **Multi-threaded processing** with proper shutdown handling
- **Export capabilities** HTML, PNG, formats plus JSON, VOTable, Pickle data file for caching
- **Hover information** with detailed astronomical data
- **Copy-to-clipboard** functionality for star names and coordinates useful for additional searches
- **Animation** - watch solar system bodies and space craft motions across timescales from minutes to years

## 🚀 Recent Improvements (July 2025)

### Enhanced Planetary Shell System
1. **Comprehensive planetary structure modeling**:
   - Individual shell structures for all major solar system bodies
   - Physically accurate layer representations based on current scientific understanding
   - Interactive controls for each planetary shell component
   - Support for complex structures like gas giant radiation belts and plasma tori

2. **Advanced visualization capabilities**:
   - Selective shell rendering with independent toggle controls
   - Center-object-aware shell display (shells only appear when object is at center)
   - Scientifically accurate scaling and color-coding for different body temperatures
   - Support for unique features like Saturn's Enceladus plasma torus

### Expanded Mission and Object Coverage
1. **Comprehensive spacecraft tracking**:
   - **Historic missions**: Pioneer 10/11, Voyager 1/2, Galileo, Cassini
   - **Current missions**: Parker Solar Probe, SOHO, Gaia, BepiColombo, Solar Orbiter
   - **Sample return missions**: Hayabusa2, OSIRIS-REx/APEX
   - **Mars exploration**: Perseverance rover with accurate trajectory data

2. **Enhanced celestial object catalog**:
   - **Complete Jovian Galilean moon system**: Io, Europa, Ganymede, Callisto 
   - **Jovian ring moons**: Metis, Adrastea, Amalthea, Thebe  
   - **Saturn's major moons**: Pan, Daphnis, Prometheus, Pandora, and more
   - **Martian moons**: Phobos and Deimos with accurate orbital periods
   - **Asteroids**: near-Earth, main belt, Jovian trojans
   - **Extreme trans-Neptunian objects**: Sedna, 2017 OF201, and other distant objects

3. **Lagrange point visualization**:
   - **Earth-Moon system**: All five Lagrange points (EM-L1 through EM-L5)
   - **Sun-Earth-Moon barycenter**: All five Lagrange points (L1-L5)
   - **Mission-relevant locations** for space telescope positioning 

### Robust Cache Management System
1. **Cache validation and repair**:
   - Automatic detection of corrupted JSON file cache entries
   - Graceful handling of mixed format data (old array-based vs new time-indexed)
   - Automatic backup creation before repairs
   - Detailed repair logs showing what was fixed

2. **Testing infrastructure**:
   - Comprehensive test suite with 13+ tests for cache operations
   - Isolated test environment preventing main file corruption
   - Tests for corruption handling, format conversion, and incremental updates

### Enhanced GUI (graphical user interface) and User Experience
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

3. **Advanced data fetching interval controls**:
   - Separate interval settings for different object types
   - Fine-grained control: ellipical orbits (1d-7d), non-elliptical trajectories (1h-24h), moons (1h-7d)
   - Intelligent defaults based on object characteristics

## 🏗️ Architecture Overview

### Technical Innovation

**Data Integration**: The software seamlessly integrates data from multiple authoritative sources:
- **NASA JPL Horizons**: Real-time solar system ephemeris data
- **ESA Hipparcos**: High-precision positions for bright stars (118,218 stars)
- **ESA Gaia DR3**: Revolutionary stellar census data for 1.8 billion stars
- **SIMBAD Database**: Comprehensive stellar properties and classifications
- **Messier Catalog**: Customized file of deep-sky objects including brighter nebulae, star clusters, and other objects

**Smart Processing Pipeline**: Raw astronomical data undergoes sophisticated processing through specialized modules. The solar system pipeline handles orbit caching with selective updates, while the stellar pipeline manages spectral classification, and multi-catalog cross-matching.

### Advanced Oort Cloud Modeling
The enhanced Oort Cloud visualization incorporates:
- **Formation Physics**: The visualization reflects actual formation mechanisms - planetesimal scattering by giant planets, galactic tidal sculpting, and ongoing modification by stellar encounters
- **Observational Constraints**: Recent discoveries of inner Oort Cloud objects like Sedna provide direct evidence for the complex structure

### System Architecture & Data Flow

**Interactive Flowchart**: Explore the complete system architecture and data flow through our interactive Mermaid flowchart:
**[📊 Paloma's Orrery System Architecture Flowchart](https://www.mermaidchart.com/app/projects/780c7ec0-84a7-4e38-9e06-9bbfdd985750/diagrams/c4180507-d001-4a8d-b8b6-5e65e1d13555/version/v0.1/edit)**

This comprehensive flowchart illustrates how the program modules and functions work together:
- **Dual-pipeline architecture** with solar system and stellar processing pathways
- **Data source integration** from JPL Horizons, Hipparcos, Gaia, and SIMBAD
- **Refined orbit system** with enhanced satellite positioning transformations from heliocentric ephemeris to planet-centered orbits
- **Module interconnections** showing how 50+ Python modules work together
- **Output generation** paths for visualizations and data exports
- **Interactive navigation** with clickable elements and detailed module descriptions

## 📁 Python modules for Paloma's Orrery

### Core Components

**`palomas_orrery.py`** ✅ **MAIN APPLICATION**
- **Core functionality**: Main solar system visualization GUI (graphical user interface) with comprehensive controls
- **Recent enhancements**:
  - Complete planetary shell system implementation
  - Expanded object catalog with 100+ celestial bodies and spacecraft
  - Lagrange point visualization system
  - Enhanced animation controls with time travel capabilities
  - Specialized shell visualization for each planetary body

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
- Repair mode for corrupted entries

**`idealized_orbits.py`** ✅ **ORBITAL MECHANICS MODULE**
- Provides ideal orbital calculations from JPL Horizons ephemeris orbital elements
- NAIF ID system integration for consistent object identification
- Orbital element definitions for accurate orbital and hyperbolic trajectory modeling for all JPL Horizons objects

### Visualization Engines
- **`planet_visualization.py`**: Solar, planetary and solar system structure visualization
- **`star_visualization_gui.py`**: Stellar neighborhood GUI (graphical user interface) initiated from palomas_orrery.py
   - **`visualization_3d.py`**: 3D stellar plot rendering
   - **`visualization_2d.py`**: 2D HR diagram generation

### Support Infrastructure
- **`shutdown_handler.py`**: Clean application termination
- **`save_utils.py`**: Export functionality with file format options
- **`constants_new.py`**: Object descriptions for hovertext, color mapping and visual constants for plotting

## 🚀 Python Installation & Quick Start for Windows -- Note: this code has only been tested in Windows!

### Step 1: Install Python on Windows

**Download Python (freeware):**

**🌟 Why Python is Free:**
Python was created by Guido van Rossum in 1991 with the philosophy of making programming accessible to everyone. The Python Software Foundation (PSF) maintains this commitment to keeping Python free and open source.
This is one of the reasons Python has become so popular in scientific computing, data science, and astronomy - researchers and institutions can use it without budget constraints or licensing concerns.
Bottom line: You can download, install, and use Python completely free for Paloma's Orrery or any other project!

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download Python 3.9 or newer (recommended: Python 3.11 or 3.12 for best compatibility)
3. **Important**: During installation, check "Add Python to PATH" option
4. Choose "Install for all users" if you have administrator privileges

**Verify Installation:**
1. Open Command Prompt (Windows Key + R, type `cmd`, press Enter)
2. Type `python --version` and press Enter
3. You should see something like `Python 3.12.x`
4. Type `pip --version` to verify pip is installed

**Alternative Installation Methods (not tested):**
- **Microsoft Store**: Search for "Python" in Microsoft Store for an easy installation
- **Anaconda**: Download from [anaconda.com](https://www.anaconda.com/) for a complete data science environment

### Step 2: Set Up Your Python Environment

**Option A: Direct Installation (This is how the entire project is developed and extensively tested)**

```bash
# Core scientific computing libraries
pip install numpy scipy matplotlib plotly

# Astronomical libraries
pip install astropy astroquery jplephem skyfield

# Data handling and utilities
pip install pandas pillow kaleido tenacity
```

**What these libraries do:**

**Scientific Computing Foundation:**
- **numpy**: Fast numerical arrays and mathematical operations (the foundation for everything else)
- **scipy**: Advanced scientific computing (optimization, interpolation, signal processing)
- **matplotlib**: 2D plotting and basic visualization
- **plotly**: Interactive 3D visualizations and web-based plots (HTML files)

**Astronomical Powerhouses:**
- **astropy**: Core astronomy library (coordinates, time systems, units, file formats)
- **astroquery**: Query astronomical databases (NASA JPL Horizons, SIMBAD, Gaia)
- **jplephem**: NASA JPL planetary ephemeris data (precise planetary positions)
- **skyfield**: High-precision astronomy computations (satellite tracking, coordinate transforms)

**Data & Utility Support:**
- **pandas**: Data manipulation and analysis (handling CSV files, time series)
- **pillow**: Image processing (loading, saving, manipulating images)
- **kaleido**: Static image export for Plotly (PNG, SVG, PDF generation)
- **tenacity**: Retry logic for network operations (handles temporary download failures)

**Additional useful libraries:**
```bash
pip install requests beautifulsoup4
```
- **requests**: HTTP library for web requests (downloading data from online sources)
- **beautifulsoup4**: HTML/XML parsing (extracting data from web pages)

**GUI framework (usually pre-installed):**
```bash
# tkinter usually comes with Python, but if needed:
# On most systems, tkinter is included with Python
# If you get import errors, try:
pip install tk
```
- **tkinter**: Python's standard GUI toolkit (creates windows, buttons, menus for the interface)

**Why this approach works well:**
- ✅ Zero configuration overhead
- ✅ No environment activation/deactivation steps
- ✅ Extensively tested with this exact setup
- ✅ Perfect if this is your primary astronomical software
- ✅ Follows the "if it ain't broke, don't fix it" philosophy

**Option B: Virtual Environment (For Multi-Project Users -- not tested!)**
*Consider this if you work on multiple Python projects with potentially conflicting dependencies:*
```bash
# Navigate to your project directory
cd path\to\palomas_orrery

# Create a virtual environment
python -m venv orrery_env

# Activate the virtual environment
orrery_env\Scripts\activate

# Install dependencies (same as Option A)
pip install numpy scipy matplotlib plotly astropy astroquery jplephem skyfield pandas pillow kaleido tenacity
```

**When you might need virtual environments:**
- Working on multiple Python projects simultaneously
- Different projects require different versions of the same library
- You want to experiment without affecting your main setup
- You're contributing to open source projects with specific requirements

**Option C: Using Conda (If you have Anaconda installed -- not tested!)**
```bash
# Create a new conda environment
conda create -n orrery_env python=3.11
conda activate orrery_env

# Install dependencies
pip install numpy scipy matplotlib plotly astropy astroquery jplephem skyfield pandas pillow kaleido tenacity
```

### Step 3: Verify Installation

```bash
# Test that key libraries import correctly
python -c "import numpy, matplotlib, astropy, plotly; print('All libraries installed successfully!')"
```

### Step 4: Troubleshooting Common Windows Issues (see above note about use of AI assistants; these tips are not tested!)

**If you get "python is not recognized":**
1. Reinstall Python and ensure "Add Python to PATH" is checked
2. Manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Add `C:\Python3X\` and `C:\Python3X\Scripts\` to your PATH
   - Restart Command Prompt

**If pip installs fail:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip
```

### Step 5: Alternative Setup with requirements.txt (not tested!)

Create a `requirements.txt` file in your project directory:
```txt
numpy>=1.21.0
scipy>=1.7.0
matplotlib>=3.5.0
plotly>=5.0.0
astropy>=5.0.0
astroquery>=0.4.0
jplephem>=2.15
skyfield>=1.40
pandas>=1.3.0
pillow>=8.0.0
kaleido>=0.2.1
tenacity>=8.0.0
requests>=2.25.0
beautifulsoup4>=4.9.0
```

Then install all dependencies at once:
```bash
pip install -r requirements.txt
```

### Quick Start to install Paloma's Orrery code base

1. **Download the repository** (multiple options):

**Option A: Download ZIP file (Easiest - No git required)**
   - Go to [https://github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the ZIP file to your desired location (e.g., `C:\Users\YourName\Documents\`)
   - Rename the extracted folder from `palomas_orrery-main` to `palomas_orrery`
   
   **Pros**: ✅ Simple, no additional software needed, works for everyone  
   **Cons**: ❌ Manual process to get updates

**Option B: Git clone (Traditional method - not tested!)**
   
   *First, install git if you don't have it:*
   - Go to [https://git-scm.com/download/windows](https://git-scm.com/download/windows)
   - Download the installer (it will auto-detect 64-bit vs 32-bit)
   - Run the installer with default settings (just keep clicking "Next")
   - **Important**: During installation, when asked about "Adjusting your PATH environment", choose "Git from the command line and also from 3rd-party software"
   - Restart Command Prompt after installation
   
   *Then clone the repository:*
   ```bash
   # Open Command Prompt (Windows Key + R, type "cmd", press Enter)
   # Navigate to where you want the project (e.g., Documents):
   cd C:\Users\YourName\Documents
   
   # Clone the repository:
   git clone https://github.com/tonylquintanilla/palomas_orrery.git
   
   # Enter the project folder:
   cd palomas_orrery
   ```
   
   *To get updates later:*
   ```bash
   # Navigate to your project folder and run:
   git pull
   ```
   
   **Pros**: ✅ Easy to get updates later with `git pull`, professional workflow  
   **Cons**: ❌ Requires installing git, command line knowledge, learning curve

**Option C: GitHub Desktop (GUI git option, not tested!)**
   - Install GitHub Desktop from [desktop.github.com](https://desktop.github.com/)
   - Click "Clone a repository from the Internet"
   - Enter the repository URL: `https://github.com/tonylquintanilla/palomas_orrery`
   - Choose your local folder
   
   **Pros**: ✅ Visual interface, easy updates, no command line  
   **Cons**: ❌ Requires installing GitHub Desktop

**Recommendation**: Use Option A (Download ZIP) for simplicity. Most users just want to try the software, not manage git repositories.

2. **Launch the main GUI (graphical user interface) application, palomas_orrery.py** (multiple options):

**Option A: Double-click to run (Easiest - Developer's preferred method)**
   - Navigate to the `palomas_orrery` folder in Windows File Explorer
   - Double-click on `palomas_orrery.py`
   - Windows will run it with Python automatically
   
   **Pros**: ✅ Simple, fast, no typing required  
   **Cons**: ❌ Console window may close quickly if there are errors

**Option B: Create a desktop shortcut (Most convenient)**
   - Right-click on `palomas_orrery.py` in File Explorer
   - Select "Send to" → "Desktop (create shortcut)"
   - Double-click the shortcut anytime to run the program
   
   **Pros**: ✅ Always accessible, no navigation needed  
   **Cons**: ❌ Same error visibility issue as Option A

**Option C: Run from Visual Studio Code (IDE "Integrated Development Environment"; best for development)**

*Visual Studio Code (VS Code) is a free, popular code editor from Microsoft that's excellent for Python development:*

**Installing VS Code:**
   - Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
   - Click "Download for Windows" (it auto-detects your system)
   - Run the installer with default settings
   - **Recommended**: Check "Add to PATH" and "Add 'Open with Code' action" during installation

**Setting up for Python:**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X or click the squares icon on the left)
   - Search for "Python" and install the Microsoft Python extension
   - This adds syntax highlighting, debugging, and IntelliSense (auto-completion)

**Running Paloma's Orrery:**
   - In VS Code: File → Open Folder → Select your `palomas_orrery` folder
   - Open `palomas_orrery.py` by clicking on it in the file explorer; you will see the actual Python code
   - Press **F5** or click the triangle "Run" button in the top-right
   - Or right-click in the code and select "Run Python File in Terminal"
   - View all output, errors, and print statements in the integrated terminal area that opens below the code

**Why VS Code is great for beginners:**
   - ✅ **Free and lightweight** (unlike heavy IDEs)
   - ✅ **See the actual Python code** (allows you to modify the code if you wish)
   - ✅ **Excellent error messages** - shows exactly what went wrong and where
   - ✅ **Built-in terminal** - see all program output without separate windows
   - ✅ **Auto-completion** - helps you learn Python as you type
   - ✅ **Integrated debugging** - step through code line by line if needed
   - ✅ **Git integration** - if you use git, it's built right in
   
   **Pros**: ✅ See all output and errors, easy debugging, professional workflow, free  
   **Cons**: ❌ Requires downloading/learning a new application

**Option D: Command line (Traditional method)**
   ```bash
   # Open Command Prompt (Windows Key + R, type "cmd", press Enter)
   # Navigate to your project folder:
   cd C:\path\to\palomas_orrery
   
   # Run the program:
   python palomas_orrery.py
   ```
   
   **Pros**: ✅ See all output and errors, works on any system  
   **Cons**: ❌ Requires typing, navigation, command line knowledge

**Recommendation**: Start with Option A (double-click) for simplicity. If you encounter issues, use Option C (VS Code) or Option D (command line) to see what's happening and for troubleshooting.

3. **Explore solar visualizations**:
   - Select one or more planets from the object checkbutton list, "Select Solar Shells, Planets, Dwarf Planets, Moons..."
   - Click, "Plot Entered Date"; the program will generate the visualization
   - If this is the first time you are plotting an object or dates an interactive window will open to confirm the data fetch from Horizons
      - "New orbit data is needed for __ selected objects" 
      - "Would you like to fetch updated data from JPL Horizons?"
      - Select: "Remember my choice for this session" 
      - Click, "Yes - Update Cache" or "No - Use Existing" to add fetched data to the cache. If this is your first time, click "Yes". 
      - Creating a JSON cache file save time plotting versus fetching fresh data every time. 
   - If you want to save the image as a PNG file, click "Yes", and save the file at a location of your choice
   - If you click "No" you will be given the option to save the image as a fully functional HTML file, a much larger file size.
   - View the visualization in HTML format in your default browser. Explore this visualization and the Plotly graphic functionality.
   - There are many kinds of objects. Explore the functionality of the GUI. Read the hovertext for guidance and information.
   - If you have any comments or questions, feel free to reach out to me at tonyquintanilla@gmail.com

4. **For stellar visualizations** 
   - In palomas_orrery.py, the main GUI, click on the blue button at the bottom, "2D and 3D Star Visualizations"
   - (optional - run `star_visualization_gui.py`):

   *Note: The stellar visualization system creates its own data files when first used:*
   - **VOT files** (`hipparcos_data.vot`, `gaia_data.vot`): Downloaded astronomical data in VOTable format
   - **PKL files** (`star_properties_distance.pkl`, `star_properties_magnitude.pkl`): Processed star data for quick searching
   
   *These files are automatically created when you first run stellar visualizations and query the Hipparcos/Gaia databases. The GitHub repository does not include these files as they are generated based on your specific search parameters and preferences. These files can become quite large.*

5. **Verify your orbit cache** (optional - only after you've used the software):
   - run verify_orbit_cache.py

   *Note: The GitHub repository does not include a pre-built cache file. The orbit cache (`orbit_paths.json`) is created automatically as you use the software and fetch data for different solar system objects. This verification step is only useful after you've run the main application and built up some cached data.*

**Initial Setup Tips:**
- Start with a few objects to build your initial JSON cache. The file size will increase as you plot more objects and dates. 
- Use "Fetch Special" mode for experiments
- The software automatically creates backups and maintains cache health

### Using the Enhanced Features

**Planetary Shell Visualization:**
1. Set any planet as the center object
2. Enable shell components (core, mantle, atmosphere, etc.)
3. Observe scientifically accurate internal structure
4. Use different center objects to explore various planetary types

**Mission Tracking:**
1. Select spacecraft from the comprehensive mission list
2. Set appropriate date ranges for mission phases
3. Watch historic missions like Voyager's grand tour
4. Track current missions in real-time

**Lagrange Point Exploration:**
1. Enable Lagrange point visualization
2. Understand gravitational balance points
3. See why L2 is preferred for space telescopes
4. Explore both Earth-Moon and Sun-Earth systems

**Time Controls:**
- Date selector for any moment from January 1, 1900- December 31, 2199 CE (JPL Horizons limits)
- Default to "now" or modify the current date and the default 28 "Days to Plot" (note: the first date is the current date)
   - Or enter the end date you want
- Animation controls: enter the number of frames to animate in minutes, hours, days, weeks, months or years
- Click "Plot Entered Date" for a static plot
- Click one of the animation buttons, then "Play" in the Plotly HTML plot

### Performance Tips

1. **First Run**: 
   - Start with a small selection of objects
   - The cache builds incrementally as you use the software

2. **Optimal Usage**:
   - Use "Fetch Special" for experiments
   - Select only objects you need to plot
   - Use coarser intervals for long time spans

3. **Cache Maintenance**:
   - **Cache is precious data** - treats cached orbit data as a valuable astronomical archive
   - Cache grows as you use the software and serves as backup if JPL Horizons become unavailable or limited
   - **Manual cleanup option**: If your cache gets too large, you can clean data older than 90 days by running Python and calling `from orbit_data_manager import prune_old_data; prune_old_data()` (Developer note: This feature exists but creator avoids using it to preserve data)
   - Run `verify_orbit_cache.py` if you suspect issues, but only repairs corruption (doesn't delete good data)
   - Multiple automatic backups created to protect against data loss

## 🔧 Configuration & Customization

### Interval Settings

# In palomas_orrery.py - Adjustable default intervals for fetching data

    'Orbital objects': '1d' for closed elliptical orbits like planets, asteroids, trans-neptunian objects, many comets         
    'Trajectory objects': '6h' for open trajectories like space missions, or hyperbolic orbits like some comets or interstellar objects  
    'Satellite objects': '1h' for moon, with typically short elliptical orbital periods   

- if you modify the settings, click "Use updated intervals below to fetch data (will not be cached)" to use them.            

### Planetary Shell Configuration

# Each planet has configurable shell variables, that illustrate the inner and outer structure, for example for Mercury:
- Select the planet and the shells you wish to plot; see the hovertext for explanations. Note this feature only works in static plots. 

    'Inner Core' 
    'Outer_core'
    'Mantle'
    'Crust'
    'Atmosphere'
    'Magnetosphere' 
    'Hill Sphere' 

## 📊 Module Architecture

### Data Pipeline Modules
- Solar visualizations: 
   - **`orbit_data_manager.py`**: Intelligent JPL Horizons caching with validation
   - **`data_processing.py`**: Coordinate transformations and preprocessing
- Stellar visualizations:
   - **`data_acquisition.py`**: Stellar data from Hipparcos/Gaia
   - **`star_properties.py`**: SIMBAD integration for stellar properties

### Visualization Engines
- Solar visualizations:
   - **`palomas_orrery.py`**: Main GUI and solar system visualization
   - **`planet_visualization.py`**: Planetary structure visualization
- Stellar visualizations:
   - **`star_visualization_gui.py`**: GUI for stellar neighborhood visualization
   - **`visualization_3d.py`**: 3D stellar rendering
   - **`visualization_2d.py`**: HR diagram generation

### Support Infrastructure
- Solar visualizations:
   - **`test_orbit_cache.py`**: Comprehensive cache testing
   - **`verify_orbit_cache.py`**: Cache health verification
   - **`idealized_orbits.py`**: Theoretical orbital mechanics
- All visualizations: 
   - **`shutdown_handler.py`**: Clean application termination
   - **`save_utils.py`**: Export functionality
   - **`constants_new.py`**: Visual and physical constants; object descriptions for hovertext

## 🌟 Comprehensive Object Catalog

### Solar System Bodies
- **All planets** with detailed shell structure visualization
- **Major moons**: 50+ satellites including Galilean moons, Saturn's major moons
- **Dwarf planets**: Pluto, Eris, Ceres, etc. with accurate classifications
- **Asteroids**: Near-Earth objects, Trojan asteroids, main belt objects
- **Comets**: Active and inactive comets with eccentric orbit support
- **Trans-Neptunian objects**: Extreme distant objects like Sedna

### Spacecraft Missions
- **Historic explorers**: Pioneer 10/11, Voyager 1/2, etc.
- **Planetary orbiters**: Galileo, Cassini, etc. with mission-accurate timelines
- **Current missions**: Parker Solar Probe, SOHO, Gaia, BepiColombo, etc.
- **Sample return missions**: Hayabusa2, OSIRIS-REx/APEX, etc. 
- **Mars exploration**: Perseverance rover trajectory

### Special Objects
- **Lagrange points**: Both Earth-Moon and Sun-Earth systems
- **Theoretical objects**: Planet 9 with hypothetical parameters
- **Reference points**: Solar system barycenter is the coordinate origins (0,0,0) for all solar plots; 
   otherwise it is the selected central object, planets, the Moon, and certain other locations of space missions

## 🌟 Future Development

- As interesting objects come up, for example the new interstellar object 3I/ATLAS (2025), I may implement them using JPL Horizons ephemeris, or new functionality is developed to enhance visualizations. Suggestions are welcome, tonyquintanilla@gmail.com

## 🎭 The Human Touch

While built on rigorous astronomical data and sophisticated algorithms, Paloma's Orrery never loses sight of the human element in space exploration. Every spacecraft has a story, every star has unique characteristics, and every celestial dance unfolds according to the same physical laws that govern our daily lives.

The new planetary shell system allows users to explore the hidden interiors of worlds both familiar and exotic. From Mercury's surprisingly large core to Jupiter's complex atmospheric layers, each visualization tells the story of planetary formation and evolution.

Whether you're tracking Voyager's historic journey to the edge of the solar system or exploring the internal structure of distant worlds, Paloma's Orrery makes the cosmos accessible, beautiful, and endlessly fascinating.

---

*Enjoy the Orrery. Questions and comments are welcome. tonyquintanilla@gmail.com*