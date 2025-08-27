# Paloma's Orrery -- Updated 8/26/25

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
- Hover over objects in the plot for extra information.  

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

**Plot Planets**  
Select one or more planets from the GUI’s object list and click “Plot Entered Date.”  

**View Planetary Shells**  
Set a planet as the center object, select the layers you want (core, mantle, atmosphere, etc.), then plot and rotate in 3D.  

**Track a Mission**  
Select a spacecraft, set its date range, and plot to see its trajectory.  

**Explore Stars**  
In the main GUI, click “2D and 3D Star Visualizations” and choose a distance or brightness filter.  

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
The entry point. Manages the main GUI, object selection, date settings, and coordinates calls to the plotting and data-fetching modules.

---

### Core Modules

**`plot_objects.py`**  
- Generates planetary, satellite, comet, asteroid, and spacecraft plots.  
- Supports both actual (JPL Horizons) and idealized orbits.  
- Handles apsidal markers, date lists, and trajectory plotting.

**`animate_objects.py`**  
- Creates time-stepped animations.  
- Handles object movement, planetary shells, and legend updates over time.  
- Supports Sun-centered and planet-centered views.

**`idealized_orbits.py`**  
- Plots idealized elliptical orbits using classical orbital elements.  
- Displays periapsis/aphelion markers for educational purposes.

---

### Visualization Modules

**`planet_visualization.py`**  
- Renders planetary shells (core, mantle, crust, atmosphere, magnetosphere).  
- Supports gas giant atmospheric layers, radiation belts, plasma tori.  
- Handles scaling, color, and transparency for shells.

**`star_visualization.py`**  
- Produces 2D Hertzsprung–Russell diagrams.  
- Generates 3D plots of local stellar neighborhoods using Hipparcos and Gaia data.  
- Includes distance and magnitude filters.

**`orbital_mechanics.py`**  
- Demonstrates transformation from orbital elements to position in space.  
- Visualizes inclination, longitude of ascending node, and argument of periapsis.

**`celestial_coordinates.py`**
- Calculates Earth-centered Right Ascension and Declination coordinates.
- Provides uncertainty estimates based on JPL Horizons data.
- Integrates coordinate display into hover text.

**`orbit_data_manager.py`**
- Handles efficient storage and retrieval of orbital path data.
- Uses incremental approach to minimize API calls.
- Manages orbit data caching and updates.

---

### Data Fetching Modules

**`fetch_horizons_data.py`**  
- Retrieves ephemerides from NASA JPL Horizons.  
- Caches results locally.  
- Supports both automatic and manual fetch modes.

**`fetch_simbad_data.py`**  
- Queries SIMBAD for stellar parameters.  
- Retrieves spectral type, luminosity class, and other metadata.

**`fetch_gaia_data.py`**  
- Retrieves star data from Gaia archive.  
- Supports bulk retrieval for 3D star visualization.

---

### Utility Modules

**`cache_management.py`**  
- Handles saving, loading, and validating cached data.  
- Detects corruption and repairs automatically.  
- Supports manual cache clearing.

**`shared_utilities.py`**  
- Contains common functions shared across modules.  
- Includes coordinate conversions, date handling, and math helpers.

**`config.py`**  
- Stores configuration constants (e.g., planetary parameters, color maps).

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
