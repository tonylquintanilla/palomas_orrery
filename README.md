# Paloma's Orrery -- Updated 8/27/25

## Table of Contents
1. [Introduction](#introduction)  
2. [Quick Start (Beginners)](#quick-start-beginners)  
   - [Prerequisites](#prerequisites)  
   - [Install Python](#1-install-python)  
   - [Download the Orrery](#2-download-the-orrery)  
   - [Install Required Libraries](#3-install-required-libraries)  
   - [Run the Program](#4-run-the-program)  
3. [First Run Tips](#first-run-tips)  
4. [Key Features (Beginner-Friendly)](#key-features-beginner-friendly)  
5. [Basic Usage Examples](#basic-usage-examples)  
6. [Advanced Features and Technical Content](#advanced-features-and-technical-content)  
   - [What Makes It Special](#what-makes-it-special)  
   - [Recent Improvements](#recent-improvements)  
   - [Architecture Overview](#architecture-overview)  
7. [Detailed Technical Reference](#detailed-technical-reference)  
8. [License](#license)  

---

## Introduction
Paloma’s Orrery is an advanced astronomical visualization tool that turns real NASA/ESA data into interactive 3D and 2D visualizations of the solar system and nearby stars. You can explore planets and moons, view spacecraft trajectories, see planetary interiors, and map the stars in your neighborhood.

Created by civil & environmental engineer Tony Quintanilla, it blends scientific accuracy with visual beauty, making astronomy accessible to students, educators, and space enthusiasts.

MIT License — Free to use, modify, and share.  

**Contact**: tonyquintanilla@gmail.com  
**Website**: [Google Sites](https://sites.google.com/view/tony-quintanilla)  
**GitHub Page**: [tonylquintanilla.github.io/palomas_orrery](https://tonylquintanilla.github.io/palomas_orrery/)  
**GitHub Repository**: [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)  
**Google Drive Repository**: [Google Drive Folder](https://drive.google.com/drive/folders/1jeqguLboO3H8Y0m1jJnGbNyyJrhhPMFU?usp=sharing)
**YouTube Playlist**: [@tony_quintanilla](https://www.youtube.com/@tony_quintanilla/featured)  

---

## Quick Start (Beginners)

### Prerequisites
- Windows 10/11 
   (Note: This program is tested only on Windows. A previous attempt to adapt it for macOS was only partially successful because the threading model works well on Windows but would need refactoring for macOS’s event-loop behavior. Advanced users are welcome to explore this further.)  
- Python 3.8+ (tested with Python 3.13)  
- Internet connection  
- ~300MB free disk space (for cache & data files)  

### 1. Install Python
Download Python from [python.org/downloads](https://www.python.org/downloads/) and during installation check “Add Python to PATH.” To confirm the installation, open a Command Prompt and type `python --version` — you should see something like `Python 3.13.0`.  

### 2. Download the Orrery
Go to [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery), click the green “Code” button, choose “Download ZIP,” and extract it to a folder of your choice.  

### 3. Install Required Libraries
You can install everything at once by opening a Command Prompt, navigating to the extracted folder, and typing `pip install -r requirements.txt`.  

Or open a Command Prompt and install step-by-step (recommended for beginners so you know what’s being added):  
1. Install the core math libraries by typing `pip install numpy pandas scipy` and pressing Enter.  
2. Install the astronomy libraries with `pip install astropy astroquery`.  
3. Install the astronomy libraries with `pip install erfa`.
4. Install the visualization libraries using `pip install plotly kaleido pillow`.  
5. Install the GUI library by typing `pip install customtkinter`.  
6. Install web and data utilities using `pip install requests beautifulsoup4 html5lib python-dateutil pytz`.  

### 4. Run the Program
You can run it three ways:  
- Double-click `palomas_orrery.py` in File Explorer.  
- Open a Command Prompt, navigate to the folder, and type `python palomas_orrery.py`.  
- In VS Code, open the project folder, open `palomas_orrery.py`, and press F5.  

---

## First Run Tips
- Start with a small selection of planets or moons.  
- The first time you plot an object, the program will ask to fetch data from JPL Horizons — choose “Yes” to build your cache.  
- On later runs, you can use the cached data for faster plotting.  
- **For star visualizations**: Expanding distance or magnitude limits fetches only new stars, while reducing limits instantly filters cached data.
- Hover over objects in the plot for extra information.  

### Star Visualization First-Time Setup

**Check for existing cache files first**:
- Look for `star_properties_distance.pkl` and `star_properties_magnitude.pkl` in your project folder
- If you downloaded the code from Google Drive or got it from someone else, you may already have these cache files (saving hours of setup!)
- Check file sizes: A populated distance PKL is typically 1-2 MB, magnitude PKL can be 10+ MB
- With existing PKL files, you can immediately visualize any distance/magnitude within the cached range

**Initial cache building (if no PKL files exist)**:
- The system includes rate limiting protection (progressive delays, batch processing)
- A full 100.1 ly cache (~14,000 stars) takes 2-3 hours but won't trigger SIMBAD limits
- Progress saves every 50 stars automatically
- **Safe to stop anytime**: Press Ctrl+C to interrupt - all progress is saved and will resume from where you left off next time

**Recommended approach for building cache from scratch**:
1. Start with 20 light-years (~100 stars, 5 minutes)
2. Expand to 50 light-years (adds ~1,500 stars, 15 minutes)
3. Later expand to 100 light-years when you have time (or interrupt and resume as needed)
4. Once cached, all future runs at any distance are instant

**Tip**: If you accidentally start a large query, don't panic - just press Ctrl+C. Your partial cache is preserved and valuable. Next run will continue from where you stopped.

---

## Key Features (Beginner-Friendly)
- Interactive solar system visualizations — select planets, moons, asteroids, comets, and spacecraft.  
- Planetary interiors — view cores, mantles, atmospheres, magnetospheres, and more.  
- Spacecraft tracking — follow historic and current missions in 3D.  
- Star maps — generate Hertzsprung–Russell diagrams and 3D local space maps.  
- Comets & asteroids — plot accurate orbits from JPL Horizons.  
- Lagrange points — visualize gravitational balance points in Earth–Moon and Sun–Earth systems.  
- Animations — watch objects move over timescales from minutes to years.  
- Celestial Coordinates - Right Ascension and Declination display with uncertainty estimates (±values represent JPL Horizons 3-sigma, JPL DE440/441 ephemeris, and typical confidence intervals).

---

## Basic Usage Examples

### Viewing Planets
1. Select planets from the checkboxes in the main window
2. Set your desired date and time
3. Click "Plot Entered Date" to generate visualization
4. Use mouse to rotate, zoom, and pan the 3D plot

### Tracking Spacecraft
1. Navigate to the spacecraft section in the scrollable panel
2. Select missions (Voyager, Parker Solar Probe, etc.)
3. Enable "Show Trajectory" for path visualization  
4. Set date range using start/end date controls
5. Plot to see historical or predicted positions

### Exploring Planetary Interiors
1. Select a planet as the center object
2. Check the shell options (core, mantle, atmosphere, etc.)
3. Plot to see the layered structure
4. Toggle shells on/off in the plot legend

### Creating Animations
1. Select objects to animate
2. Set number of frames and time step
3. Click animation buttons (daily, weekly, monthly, yearly)
4. Animation opens in browser with playback controls

### Star Visualizations
1. Click "2D and 3D Star Visualizations" button
2. Enter distance (light-years) or magnitude limit
3. Choose between 3D plot or HR diagram
4. Explore stellar neighborhoods or visible stars

---

## Advanced Features and Technical Content

### What Makes It Special

#### Scientific Accuracy Meets Visual Beauty
- Real astronomical data from NASA JPL Horizons, JPL 440/441 ephemeris, ESA Hipparcos/Gaia and SIMBAD databases.  
- Time-accurate positioning for planets, moons, asteroids, comets, and spacecraft from JPL Horizons system.  
- Stellar neighborhood mapping with accurate 3D positioning for 118,000+ stars from Hipparcos and Gaia catalogs.  
- Intelligent cache management with selective updates and automatic data cleanup.  
- Enhanced orbital mechanics with actual and idealized orbits using JPL Horizons ephemerides.  

#### Advanced Planetary Shell Visualization System
- Comprehensive planetary anatomy: core, mantle, crust, atmosphere, magnetosphere, and Hill sphere visualization.  
- Detailed solar and planetary shells:  
  - Sun: core, convective zone, radiative zone, photosphere, corona, solar wind.  
  - Terrestrial planets: differentiated core-mantle-crust structures with atmospheres.  
  - Gas giants: complex layered atmospheres, metallic hydrogen cores, ring systems, radiation belts, magnetospheres.  
  - Ice giants: unique mantle compositions and tilted magnetospheres.  
  - Dwarf planets: specialized structures including Pluto's haze layers and atmosphere.  
  - Planet 9: hypothetical ice giant structure visualization.  
- Interactive shell controls allowing selective visualization of individual planetary layers.  
- Magnetosphere modeling including plasma torus systems around Jupiter and Saturn.  

#### Advanced Features & Intelligent Data Management
- Smart selective caching only fetches data for selected objects, avoiding unnecessary requests.
- **Incremental catalog caching** fetches only new stars when expanding distance/magnitude limits.
- **Automatic cache merging** combines old and new data, removing duplicates intelligently.
- Special fetch mode for experimental plotting without cache modification.
- Automatic cache backup on startup.
- Cache validation and repair system that automatically detects and fixes corrupted data entries.  
- Multi-threaded processing with proper shutdown handling.  
- Export capabilities: HTML, PNG, plus JSON, VOTable, Pickle data files for caching.  
- Hover information with detailed astronomical data.  
- Copy-to-clipboard functionality for star names and coordinates.  
- Animation — watch solar system bodies and spacecraft move across timescales from minutes to years. 

#### Interactive Orbital Mechanics Visualization
- Educational tool showing how the six classical orbital elements define an object's orbit in space.  
- Step-by-step transformations demonstrating three key rotations (argument of periapsis, inclination, longitude of ascending node).  
- Dynamic center body for satellite orbits.  
- Designed to build strong intuition for complex orbital mechanics concepts.  

---

### Recent Improvements

#### Enhanced Planetary Shell System
1. Comprehensive planetary structure modeling:  
   - Individual shell structures for all major solar system bodies.  
   - Physically accurate layers based on current science.  
   - Interactive controls for each planetary shell component.  
   - Support for complex structures like gas giant radiation belts and plasma tori.  

2. Advanced visualization capabilities:  
   - Selective shell rendering with independent toggle controls.  
   - Center-object-aware shell display.  
   - Accurate scaling and color-coding for temperatures.  
   - Support for features like Saturn's Enceladus plasma torus.  

#### Expanded Mission and Object Coverage
1. Spacecraft tracking: Pioneer 10/11, Voyager 1/2, Galileo, Cassini, Parker Solar Probe, SOHO, Gaia, BepiColombo, Solar Orbiter, Hayabusa2, OSIRIS-REx/APEX, Perseverance rover.  
2. Enhanced celestial object catalog: Galilean moons, Jovian ring moons, Saturn's major moons, Martian moons, asteroids, extreme trans-Neptunian objects.  
3. Lagrange point visualization for Earth-Moon and Sun-Earth-Moon barycenter systems.  

#### Robust Cache Management
1. Cache validation and repair with automatic detection, backup creation, and detailed logs.  
2. Comprehensive test suite with isolated test environment.  
3. Performance tips and safe manual deletion options.  

#### Enhanced Orbital Mechanics and Visualization
1. Accurate apsidal date calculations for elliptical, hyperbolic, and satellite orbits.  
2. Legend integration for apsidal markers.  
3. Intelligent date display with special handling for hyperbolic orbits.  

#### Enhanced GUI and User Experience
1. Reorganized orbit data fetching interface.  
2. Streamlined cache update process.  
3. Advanced data fetching interval controls.  

#### Dynamic Apsidal Marker System
1. Real-time orbital calculations with unified date handling.  
2. Dual marker system for ideal and actual apsidal points.  
3. Enhanced information display with hover details.

#### Right Ascension and Declination Coordinates
1. Earth-centered apparent coordinates
2. Uncertainty values represent JPL Horizons 3-sigma confidence intervals
3. Sources: JPL Horizons real-time data, DE441 ephemeris precision, or typical class-based estimates

#### Incremental Data Caching System
1. Smart incremental fetching for stellar catalogs:
   - Only fetches new data when expanding search radius or magnitude limit
   - Filters cached data when reducing limits (no API calls needed)
   - Tracks query parameters with metadata files
   - Reduces data fetching by up to 99% for iterative exploration

2. Safe SIMBAD query management:
   - Prevents accidental mass queries with confirmation prompts
   - Requires explicit parameters to prevent unintended cache rebuilds
   - Progressive rate limiting between query batches
   - Preserves existing PKL cache integrity
---

## Architecture Overview

Paloma’s Orrery is modular by design, with separate Python files for each major functional area.  
The architecture is divided into **Core**, **Visualization**, **Data Fetching**, **Utility**, and **GUI** layers.

**📊 Visual Architecture Diagram**: [View the interactive Mermaid flowchart](https://www.mermaidchart.com/app/projects/780c7ec0-84a7-4e38-9e06-9bbfdd985750/diagrams/2c4e2ff3-5f91-4388-b3b1-50defaa41fd5/version/v0.1/edit) showing the complete module structure and data flow.

1. **Core Modules** — Handle main logic, initialization, and object plotting.  
2. **Visualization Modules** — Create plots, animations, and visual representations of planetary shells, orbits, and stars.  
3. **Data Fetching Modules** — Retrieve astronomical data from JPL Horizons, SIMBAD, Gaia, and other databases.  
4. **Utility Modules** — Handle caching, configuration, math utilities, and shared functions.  
5. **GUI Modules** — Manage the user interface and event handling.

This separation allows easier maintenance, testing, and feature expansion.

---

## Detailed Technical Reference

### Main Program
**`palomas_orrery.py`**  
The entry point. Manages the main GUI, object selection, date settings, and coordinates all plotting and animation functions.

---

### Core Helper Modules

**`palomas_orrery_helpers.py`**  
- Helper functions for the main orrery application
- Contains Planet 9 calculations, axis range calculations
- Trajectory fetching and padding functions
- Orbit backup and cleanup utilities

**`idealized_orbits.py`**  
- Plots idealized elliptical orbits using classical orbital elements
- Contains planetary parameters, parent-planet relationships, and tilt angles
- Displays periapsis/aphelion markers for educational purposes

**`orbit_data_manager.py`**
- Handles efficient storage and retrieval of orbital path data
- Uses incremental approach to minimize API calls
- Manages orbit data caching, updates, and repairs
- Converts between time-indexed and array formats

---

### Visualization Modules

**`planet_visualization.py`**  
- Comprehensive planetary shell visualization system
- Renders cores, mantles, crusts, atmospheres, magnetospheres
- Supports gas giant atmospheric layers, radiation belts, plasma tori
- Contains detailed info for all planetary bodies including the Sun

**`orbital_param_viz.py`**
- Interactive orbital mechanics visualization
- Demonstrates orbital element transformations
- Shows inclination, longitude of ascending node, and argument of periapsis

**`star_visualization_gui.py`**
- GUI for star visualizations (HR diagrams and 3D stellar maps)
- Controls for distance and magnitude-based filtering
- Integration with planetarium modules

---

### Planetarium & Star Modules

**`planetarium_distance.py`**
- 3D visualization of stars within specified distance
- Uses Hipparcos and Gaia data

**`planetarium_apparent_magnitude.py`**
- 3D visualization of stars brighter than specified magnitude
- Includes Messier objects and notable stars

**`hr_diagram_distance.py`**
- HR diagram for stars within specified distance
- Color-magnitude relationships

**`hr_diagram_apparent_magnitude.py`**
- HR diagram for stars of specified brightness
- Stellar classification visualization

---

### Data Processing Modules

**`data_acquisition.py`** / **`data_acquisition_distance.py`**
- Fetches stellar data from Vizier catalogs
- Handles both distance and magnitude-based queries

**`data_processing.py`**
- Processes raw astronomical data
- Calculates distances and coordinates
- Aligns different catalog systems

**`incremental_cache_manager.py`**
- Manages incremental fetching for VizieR catalogs
- Tracks cache metadata and query parameters
- Handles expansion, contraction, and merging of stellar data
- Minimizes API calls through intelligent cache reuse

**`star_properties.py`**
- Queries SIMBAD for stellar parameters
- Manages star property caching

**`stellar_parameters.py`**
- Calculates stellar parameters (temperature, luminosity)
- Estimates values from available data

---

### Visualization Support Modules

**`visualization_2d.py`**
- Creates 2D HR diagrams
- Handles plotting configurations

**`visualization_3d.py`**
- Creates 3D stellar neighborhood plots
- Manages 3D scene configurations

**`visualization_core.py`**
- Core visualization utilities
- Hover text formatting
- Data analysis functions

**`visualization_utils.py`**
- Additional visualization helpers
- Toggle buttons and UI controls

---

### Utility Modules

**`formatting_utils.py`**
- Number formatting utilities
- Scientific notation converters

**`shared_utilities.py`**
- Common functions shared across modules
- Sun direction indicators and other helpers

**`save_utils.py`**
- Plot saving functionality
- HTML and image export support

**`shutdown_handler.py`**
- Thread management and cleanup
- Safe figure display and closing

**`celestial_coordinates.py`**
- Calculates Earth-centered Right Ascension/Declination
- Provides uncertainty estimates from JPL Horizons
- Integrates coordinate display into hover text

---

### Special Purpose Modules

**`refined_orbits.py`** / **`orrery_integration.py`**
- Advanced orbit refinement system (optional)
- Integration with ephemeris data

**`create_ephemeris_database.py`**
- Creates satellite ephemeris databases
- Converts orbital parameters between formats

**`messier_object_data_handler.py`**
- Handles Messier catalog objects
- Special visualization for deep-sky objects

**`star_notes.py`**
- Contains notes and information about notable stars
- Used for hover text and descriptions

**`constants_new.py`**
- Constants for stellar classifications
- Color mappings and type definitions

---

### Data Files (Not Python modules but important)
- `orbit_paths.json` - Cached orbit data
- `star_properties_distance.pkl` - Cached star properties by distance
- `star_properties_magnitude.pkl` - Cached star properties by magnitude
- `satellite_ephemerides.json` - Satellite orbital elements
---

### GUI Modules

**`gui_main.py`**  
- Builds the main user interface.  
- Provides controls for object selection, date input, and feature toggles.

**`gui_star_visualization.py`**  
- Manages the star visualization interface.  
- Provides controls for HR diagram and 3D star plot settings.

**`gui_orbital_mechanics.py`**  
- Manages orbital mechanics visualization controls.  
- Allows users to step through orbital element transformations.

---

## License

MIT License  

Copyright (c) 2025 Tony Quintanilla  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
