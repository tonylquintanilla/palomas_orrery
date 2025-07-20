# 🌌 Paloma's Orrery

## Introduction

Paloma's Orrery is an advanced astronomical visualization software that brings the cosmos to your desktop. This comprehensive tool transforms complex astronomical data into interactive visualizations of our solar system and stellar neighborhood. The visualizations are created with a Python program with the assistance of AI assistants, including Claude, ChatGPT, Gemini and DeepSeek. This Orrery is under active development as new functionalities, objects and visualizations are implemented.

Created by a civil and environmental engineer with a passion for space exploration, Paloma's Orrery bridges the gap between scientific accuracy and visual beauty, making astronomy accessible to educators, students, and space enthusiasts.

-- Tony Quintanilla, Chicago, July 15, 2025

   tonyquintanilla@gmail.com
   website: https://sites.google.com/view/tony-quintanilla
   GitHub Web Page: https://tonylquintanilla.github.io/palomas_orrery/ 
   GitHub Repository: https://github.com/tonylquintanilla/palomas_orrery
   Tube Playlist: https://www.youtube.com/@tony_quintanilla/featured

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

### Enhanced Orbital Mechanics and Visualization

1. **Accurate apsidal date calculations**:
   - Dynamic perihelion/apohelion date computation: Calculates actual dates when objects reach their closest and farthest points from the Sun based on their current orbital position
   - Support for all orbit types: Handles elliptical orbits (planets, asteroids), hyperbolic orbits (some comets), and satellite orbits (moons with perigee/apogee)

2. **Legend integration**: 
   - Apsidal markers now appear in the plot legend for easy identification

3. **Intelligent date display**: 
   - Shows calculated future dates for perihelion/apohelion, with special handling for hyperbolic orbits that may never return

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
   - **`apsidal_markers.py`**: Orbital dynamics calculations for perihelion/apohelion dates
- All visualizations: 
   - **`shutdown_handler.py`**: Clean application termination
   - **`save_utils.py`**: Export functionality
   - **`constants_new.py`**: Visual and physical constants; object descriptions for hovertext

### Technical Innovation

**Data Integration**: The software seamlessly integrates data from multiple authoritative sources:
- **NASA JPL Horizons**: Real-time solar system ephemeris data
- **ESA Hipparcos**: High-precision positions for bright stars (118,218 stars)
- **ESA Gaia DR3**: Revolutionary stellar census data for 1.8 billion stars
- **SIMBAD Database**: Comprehensive stellar properties and classifications
- **Messier Catalog**: Customized file of deep-sky objects including brighter nebulae, star clusters, and other objects

**Smart Processing Pipeline**: Raw astronomical data undergoes sophisticated processing through specialized modules. The solar system pipeline handles orbit caching with selective updates, while the stellar pipeline manages spectral classification, and multi-catalog cross-matching.

**Precise Orbital Mechanics**: The software now includes sophisticated orbital dynamics calculations through the apsidal markers system:
- **Real-time orbital position analysis**: Calculates an object's true anomaly from its current 3D position.
- **Keplerian time predictions**: Uses classical orbital mechanics to predict when objects will reach perihelion or apohelion.
- **Adaptive calculations**: Different algorithms for elliptical vs. hyperbolic orbits, ensuring accuracy across all object types.
- **Educational value**: Hover over apsidal markers to see exactly when planets and comets reach their orbital extremes.

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


## 📁 Python modules for Paloma's Orrery, alphabetically organized except for the GUI's, `palomas_orrery.py`, `star_visualization_gui.py`

**`palomas_orrery.py`** ✅ **MAIN APPLICATION**
- **Core functionality**: Main solar system visualization GUI (graphical user interface) with comprehensive controls for selecting celestial objects, setting dates, and configuring plot parameters. It serves as the central hub for all solar system plotting and animation. This GUI can also be used to access the stellar visualization GUI, `star_visualization_gui.py`. 
- **Recent enhancements**:
  - Complete planetary shell system implementation.
  - Expanded object catalog with 100+ celestial bodies and spacecraft.
  - Lagrange point visualization system.
  - Enhanced animation controls with various time steps.
  - Integration of refined and idealized orbit plotting.
  - Integration of dynamic apsidal date calculations for all orbital plots.

**`star_visualization_gui.py`**
-   **Core functionality**: Provides a dedicated GUI for stellar visualizations, launched from the main orrery application. It enables the creation of 2D H-R diagrams and 3D stellar neighborhood plots based on user-defined parameters like distance or apparent magnitude.

**`apsidal_markers.py`** ✅ **ORBITAL DYNAMICS CALCULATOR**
- **Core functionality**: Calculates accurate dates for perihelion, apohelion, perigee, and apogee based on current orbital positions and Keplerian mechanics.
- **Key Features**:
  - True anomaly calculation: Determines an object's current position in its orbit from 3D coordinates.
  - Kepler's equation solver: Converts between true, eccentric, and mean anomalies for time calculations.
  - Multi-orbit support: Handles elliptical orbits (e < 1) and hyperbolic trajectories (e ≥ 1).
  - Automated marker generation: Creates properly formatted Plotly markers with hover text and date information.
  - Satellite terminology: Automatically uses perigee/apogee for moon orbits instead of perihelion/apohelion.

**`catalog_selection.py`** ✅ **STELLAR CATALOG MANAGEMENT**
- **Core functionality**: A specialized module for the star visualization part of the application. It handles the logic for selecting stars from the Hipparcos and Gaia catalogs based on user criteria.
- **Key Features**:
  - **Unified Selection**: Provides a single function (`select_stars`) that can filter stars by either `magnitude` or `distance`.
  - **Catalog Separation Logic**: Implements a clear rule-based system for which catalog to use based on star brightness (`Vmag`), ensuring that the best data source is used for each star (e.g., Hipparcos for bright stars, Gaia for fainter ones).
  - **Data Estimation**: Integrates with functions like `estimate_vmag_from_gaia` when necessary to ensure consistent data for filtering.

**`constants_new.py`** ✅ **CENTRAL CONSTANTS & DATA**
- **Core functionality**: A centralized module that stores constants, color maps, and descriptive text used throughout the application.
- **Key Data**:
  - **Physical Constants**: `KM_PER_AU`, `LIGHT_MINUTES_PER_AU`.
  - **Object Information**: `CENTER_BODY_RADII`, `KNOWN_ORBITAL_PERIODS`.
  - **Visualization**: `color_map` function to assign consistent colors to all celestial objects.
  - **GUI Text**: Contains the long informational `note_text` for the GUI and the detailed `INFO` dictionary for object tooltips.

**`create_ephemeris_database.py`** ✅ **DATABASE BUILDER**
- **Core functionality**: A utility script to build the `satellite_ephemerides.json` file. This script is not run by the main application but is used by the developer to pre-process orbital data.
- **Key Features**:
  - **Data Aggregation**: Combines orbital parameters from `idealized_orbits.py` with more accurate data parsed from the headers of JPL Horizons ephemeris text files.
  - **Format Standardization**: Converts data from various sources into a consistent JSON format that the `refined_orbits.py` module can easily use.

**`data_acquisition.py`** ✅ **UNIFIED DATA FETCHER**
- **Core functionality**: A unified module that fetches stellar data from the Hipparcos and Gaia catalogs via the VizieR service. It replaces older, separate scripts by handling queries based on either distance (parallax) or apparent magnitude.
- **Key Features**:
    - **Dual-Mode Fetching**: Can operate in 'distance' or 'magnitude' mode to suit different visualization needs.
    - **Intelligent Caching**: Checks for existing `.vot` files to avoid redundant downloads, loading local data when available.
    - **Optimized Queries**: Built to request only essential data columns, reducing load on VizieR and speeding up large requests.
    - **Integrated Logic**: Incorporates and supersedes the logic from the older `data_acquisition_distance.py`.

**`data_processing.py`** ✅ **STELLAR DATA PIPELINE**
- **Core functionality**: The primary module for processing and combining raw stellar data after it has been fetched. It prepares the data for scientific analysis and visualization.
- **Key Features**:
    - **Catalog Merging**: Implements the critical logic for combining Hipparcos data (for bright stars, Vmag ≤ 4) and Gaia data (for fainter stars) into a single, cohesive dataset.
    - **Scientific Calculations**: Calculates distances from parallax, estimates Johnson V magnitudes for Gaia stars (using `estimate_vmag_from_gaia`), and computes final 3D Cartesian coordinates (x, y, z) for plotting.
    - **Data Cleaning**: Includes functions to align coordinate systems and filter out entries with invalid data, ensuring the quality of the final dataset.

**`earth_visualization_shells.py` / `moon_visualization_shells.py`** ✅ **PLANETARY STRUCTURE VISUALIZATION**
- **Core functionality**: These modules are responsible for creating the detailed, layered "shell" visualizations for celestial bodies. Each body with shells has its own dedicated module.
- **Key Features**:
  - **Scientifically-Based Layers**: Defines the radius, color, opacity, and detailed description for each geological and atmospheric layer (e.g., inner core, outer core, mantle, crust, atmosphere, magnetosphere, Hill sphere).
  - **Plotly Trace Generation**: Contains functions that generate the `go.Scatter3d` or `go.Mesh3d` traces required by Plotly to render the spherical shells.
  - **Detailed Hovertext**: Provides scientifically-rich descriptions for each shell that appear when a user hovers over them in the plot.

**`eris_visualization_shells.py`**
-   **Core functionality**: Renders the 3D visualization for the dwarf planet Eris, modeling its dense rocky core, ice mantle, and highly reflective crust. It also depicts its dynamic, collapsible atmosphere and its large Hill sphere.

**`formatting_utils.py`**
-   **Core functionality**: A utility module that provides simple, reusable functions for formatting numerical data, ensuring consistent string representation for floating-point numbers and values in scientific notation across the application.

**`hr_diagram_apparent_magnitude.py`**
-   **Core functionality**: A command-line utility that creates an HR diagram for stars up to a user-defined apparent magnitude. It combines data from Hipparcos and Gaia to analyze and visualize the brightest stars as seen from Earth.

**`hr_diagram_distance.py`**
-   **Core functionality**: A command-line tool that generates a Hertzsprung-Russell (HR) diagram for stars within a user-specified distance from the Sun. It sources data from the Hipparcos and Gaia catalogs and performs the necessary calculations and processing to create the 2D plot.

**`idealized_orbits.py`** ✅ **ORBITAL MECHANICS MODULE**
-   **Core functionality**: Contains the orbital elements (like semi-major axis, eccentricity, and inclination) for a wide range of solar system bodies, including planets, moons, and asteroids. It provides the foundational data for calculating and plotting idealized elliptical and hyperbolic orbits. It also handles the complex transformations required to correctly orient satellite orbits around their parent planets. Includes refined transformation logic for the satellite systems of planets with significant axial tilts, such as Mars, Saturn, and Uranus.
- Provides ideal orbital calculations from JPL Horizons ephemeris orbital elements.
- NAIF ID system integration for consistent object identification.
- Contains orbital element definitions for accurate elliptical and hyperbolic trajectory modeling for all supported JPL Horizons objects, including planets, moons, and comets.
-   **Recent enhancements**: Integration with apsidal_markers.py for accurate perihelion/apohelion date calculations based on current orbital positions.

**`jupiter_visualization_shells.py`**
-   **Core functionality**: Constructs the 3D visualization for Jupiter's complex structure, including its dense core, metallic and molecular hydrogen layers, vibrant cloud tops, extensive ring system, and powerful magnetosphere with its associated plasma torus and radiation belts.

**`mars_visualization_shells.py`**
-   **Core functionality**: Creates the 3D visualization for Mars's distinct layers, modeling its solid inner core, liquid outer core, and silicate mantle. It also visualizes the atmosphere and unique localized crustal magnetic fields.

**`mercury_visualization_shells.py`**
-   **Core functionality**: Generates the 3D visualization for Mercury's internal and external layers, including its large metallic core, thin mantle, crust, tenuous exosphere, and dynamic magnetosphere.

**`messier_catalog.py`** ✅ **DEEP-SKY OBJECT DATABASE**
- **Core functionality**: A static data module that serves as a local, offline database for well-known deep-sky objects.
- **Key Features**:
    - **Curated Catalogs**: Contains Python dictionaries with detailed information on Messier objects, prominent star clusters, and bright nebulae (e.g., Crab Nebula, Pleiades).
    - **Rich Data**: Stores essential properties like name, object type, apparent magnitude, distance, celestial coordinates (RA/Dec), and descriptive notes.
    - **Helper Functions**: Provides utility functions to easily filter and retrieve objects by brightness, type, or from specific sub-catalogs.

**`messier_object_data_handler.py`** ✅ **DEEP-SKY OBJECT INTEGRATION**
- **Core functionality**: Processes the deep-sky object data from `messier_catalog.py` and integrates it into the main data pipeline, allowing nebulae, clusters, and galaxies to be plotted alongside stars.
- **Key Features**:
    - **Data Standardization**: Converts the raw catalog data into a Pandas DataFrame with a structure that matches the stellar data.
    - **Coordinate Calculation**: Calculates the 3D Cartesian coordinates for each deep-sky object based on its RA, Dec, and distance.
    - **Hover Text Generation**: Creates detailed and minimal hover tooltips for each object, ensuring a consistent user experience across all visualized bodies.

**`neptune_visualization_shells.py`**
-   **Core functionality**: Creates the multi-layered 3D visualization for Neptune.
-   **Key Features**: Models Neptune’s core, icy mantle, and dynamic atmosphere including its cloud layers. It also visualizes its faint ring system, radiation belts, and complex, offset magnetosphere.

**`orbit_data_manager.py`** ✅ **CRITICAL MODULE**
- **Core functionality**: Manages all orbit data caching and JPL Horizons integration
- **Recent enhancements**:
  - Safe save mechanism with size checks
  - Automatic corruption detection and repair
  - Support for both old and new data formats
  - Incremental update capabilities
  - Proper error handling and backup creation

**`orrery_integration.py`** ✅ **ORBIT SELECTION & INTEGRATION**
- **Core functionality**: Acts as a bridge between the main orrery and the two orbit systems (`idealized_orbits` and `refined_orbits`).
- **Key Features**:
  - **Orbit Selection**: Contains the primary `get_orbit_function` which decides whether to use a refined or idealized orbit based on user configuration and data availability.
  - **Configuration Management**: Manages user preferences for orbit types and visualization settings (e.g., colors for refined vs. idealized orbits).
  - **Enhanced Plotting**: Provides functions to plot both refined and idealized orbits simultaneously for comparison.

**`palomas_orrery_helpers.py`** ✅ **GUI & PLOT LOGIC HELPER**
- **Core functionality**: Contains a wide range of helper functions that support `palomas_orrery.py`.
- **Key Functions**:
  - **Data Fetching**: Manages fetching trajectories (`fetch_trajectory`) and orbit paths (`fetch_orbit_path`), including padding for missions with specific date ranges.
  - **Plotting Helpers**: Adds URL buttons to the plot, provides default camera settings, and prints formatted position data to the console.
  - **Calculations**: Includes logic for calculating the position of the hypothetical Planet 9 and performing point rotations.
  - **Cache Management**: Provides startup functions for creating cache backups and performing periodic cleanup.

**`planet_visualization.py`** ✅ **PLANETARY SHELL DISPATCHER**
-   **Core functionality**: Acts as the central dispatcher for all planetary and solar structure visualizations. It contains the primary `create_celestial_body_visualization` function, which imports and calls the appropriate shell-creation functions from the various `*_visualization_shells.py` modules.
-   **Key Features**:
    -   Dynamically constructs layered visualizations for any selected celestial body (Sun, planets, dwarf planets) based on user selections from the GUI.
    -   Ensures that shell visualizations are only rendered when a celestial body is set as the center object, improving clarity and performance.
    -   Manages the integration of these complex shell structures into both static and animated Plotly figures.

**`planet_visualization_utilities.py`**
-   **Core functionality**: A support module for the planetary shell visualization system. It provides a set of shared, low-level functions used by all the `*_visualization_shells.py` modules to reduce code duplication and ensure consistency.
-   **Key Functions**:
    -   **`create_sphere_points`**: Generates the raw (x, y, z) coordinates for spherical layers.
    -   **`create_magnetosphere_shape`**: Models the asymmetric shape of a planetary magnetosphere, compressed on the sunward side and extended on the tail side.
    -   **`rotate_points`**: Applies axial tilt rotations to correctly orient structures like rings and magnetospheres.

**`planet9_visualization_shells.py`**
-   **Core functionality**: Renders the 3D visualization for the hypothetical Planet 9 based on leading scientific theories.
-   **Key Features**: Models the surface of Planet 9 assuming it is an ice giant, similar in composition to Uranus and Neptune. It also visualizes its vast, calculated Hill sphere, representing the region of its gravitational dominance in the outer solar system.

**`planetarium_apparent_magnitude.py`**
-   **Core functionality**: A command-line utility to generate a 3D visualization of the night sky, showing stars and deep-sky objects brighter than a user-specified apparent magnitude.
-   **Key Features**:
    -   Combines data from the Hipparcos (for bright stars) and Gaia (for dimmer stars) catalogs.
    -   Integrates with `messier_object_data_handler.py` to fetch and plot bright Messier objects (galaxies, nebulae, clusters) alongside stars.
    -   Calculates the 3D positions of objects and generates an interactive Plotly visualization, allowing users to explore the most prominent celestial objects as seen from Earth.

**`planetarium_distance.py`**
-   **Core functionality**: A command-line script that creates a 3D map of the Sun's stellar neighborhood for stars within a specified distance.
-   **Key Features**:
    -   Takes a distance in light-years as a command-line argument.
    -   Fetches high-precision parallax data from the Hipparcos and Gaia catalogs to identify all known stars within that radius.
    -   Processes the data to calculate 3D Cartesian coordinates and generates an interactive Plotly visualization of the local solar neighborhood.

**`pluto_visualization_shells.py`**
-   **Core functionality**: Renders the detailed, multi-layered 3D visualization for the dwarf planet Pluto and its environment.
-   **Key Features**:
    -   Models Pluto’s differentiated interior, including its large rocky core and a water-ice mantle that may host a subsurface ocean.
    -   Visualizes its complex surface crust, composed of volatile ices like nitrogen and methane.
    -   Depicts its surprisingly complex and layered atmospheric haze, which has a distinct blue tint, and its vast, tenuous outer atmosphere.

**`refined_orbits.py`** ✅ **ADVANCED ORBITAL MECHANICS**
- **Core functionality**: Works alongside `idealized_orbits.py` to provide more accurate satellite positions. It refines the idealized orbits by applying corrections based on actual ephemeris data fetched from JPL Horizons.
- **Key Features**:
  - **Correction Calculation**: Compares the orbital plane of an idealized orbit with the plane derived from actual cached data and calculates a rotational correction.
  - **Fallback System**: Intelligently falls back to an idealized orbit or a default circular orbit if ephemeris data is not available.
  - **Special Handling**: Includes specific logic for moons of Mars and Saturn's moon Phoebe, which have complex orbital dynamics.
  - **Caching**: Caches the refined orbit functions to improve performance.

**`saturn_visualization_shells.py`**
-   **Core functionality**: Constructs the comprehensive, multi-component 3D visualization for Saturn, its rings, and its magnetospheric environment.
-   **Key Features**:
    -   Models Saturn's "fuzzy" core and its vast surrounding layer of liquid metallic hydrogen.
    -   Generates its famous, complex ring system, rendering the distinct A, B, C, D, E, F, and G rings with appropriate gaps and transparency.
    -   Visualizes features of its magnetosphere, including the plasma torus sourced by the moon Enceladus's geysers and its distinct radiation belts, which are shaped by the planet's moons.

**`save_utils.py`**
-   **Core functionality**: A utility module that handles the process of saving Plotly visualizations. It uses `tkinter` to create native file-saving dialogs for a better user experience.
-   **Key Features**:
    -   Prompts the user to choose between saving as an interactive HTML file or a static PNG image.
    -   Handles all file I/O operations for saving the plot.
    -   Manages dependencies, providing a clear error message if the `kaleido` package (required for PNG export) is not installed.

**`shared_utilities.py`**
-   **Core functionality**: A general-purpose utility module that provides functions shared across different visualization types, particularly for planetary shells.
-   **Key Features**:
    -   Contains the `create_sun_direction_indicator` function, which adds a standardized, scalable arrow to planetary shell plots to indicate the direction of the Sun. This is crucial for correctly interpreting the orientation of features like magnetospheres.
    -   Ensures that visual elements are consistent across different parts of the application.

**`shutdown_handler.py`**
-   **Core functionality**: Provides a robust shutdown and cleanup mechanism for the application, ensuring that resources are managed correctly, especially when displaying plots.
-   **Key Features**:
    -   The `PlotlyShutdownHandler` class manages background threads to prevent the application from closing prematurely.
    -   The `show_figure_safely` function handles the display of Plotly figures by writing them to a temporary HTML file, opening them in a web browser, and then safely deleting the temporary file after a delay to ensure a smooth user experience without leaving junk files.

**`solar_visualization_shells.py`** ✅ **SOLAR STRUCTURE VISUALIZATION**
- **Core functionality**: Dedicated to generating the complex, multi-layered 3D visualization of the Sun and its extended environment.
- **Key Features**:
    - **Internal & Atmospheric Layers**: Renders the Sun’s core, radiative zone, photosphere, chromosphere, and the inner and outer corona.
    - **Extended Influence**: Visualizes the vast outer boundaries of the solar system, including the termination shock, the heliopause, and multiple representations of the theoretical Oort Cloud (inner/Hills cloud, outer cloud).
    - **Advanced Oort Cloud Models**: Implements modern scientific concepts of the Oort Cloud, showing it not just as a simple sphere but as a clumpy, tide-influenced, and toroidal structure.
    - **Scientific Hovertext**: Each layer is accompanied by detailed hover information explaining its physical characteristics and scientific importance.

**`star_notes.py`**
-   **Core functionality**: A data module that provides a repository of custom, detailed descriptions for prominent stars and deep-sky objects.
-   **Key Features**: Contains a Python dictionary (`unique_notes`) that maps object identifiers to rich, HTML-formatted text. This allows the application to display manually curated, in-depth information in the hover tooltips, enhancing the educational value for well-known celestial bodies.

**`star_properties.py`**
- **Core functionality**: Manages the querying and caching of stellar properties from the SIMBAD astronomical database. It acts as the bridge between the application's internal star lists and external, detailed databases.
- **Key Features**:
    - **Simbad Integration**: Queries SIMBAD for properties like spectral type, B-V color index, and official star names.
    - **Batch Processing**: Fetches data in batches to respect API limits and handle large requests efficiently.
    - **Intelligent Caching**: Saves retrieved properties to a local pickle file (`.pkl`), significantly speeding up subsequent runs.
    - **Messier Object Handling**: Includes special logic to supplement SIMBAD data with a local, more detailed `messier_catalog.py` for non-stellar objects.

**`stellar_parameters.py`**
- **Core functionality**: A scientific calculation module responsible for deriving fundamental stellar parameters when they are not directly available.
- **Key Features**:
    - **Temperature Estimation**: Contains functions to estimate a star's temperature from its spectral type (`estimate_temperature_from_spectral_type`) or its B-V color index (`calculate_bv_temperature`).
    - **Intelligent Selection**: Implements a `select_best_temperature` function that algorithmically chooses the most reliable temperature value, prioritizing B-V when consistent with spectral type but deferring to spectral type for very hot, very cool, or anomalous stars.

**`test_orbit_cache.py`** ✅ **NEW TEST SUITE**
- Comprehensive testing for cache functionality
- Isolated test environment in `test_output/` directory
- Tests for corruption handling, format conversion, and updates
- Ensures cache reliability and data integrity

**`uranus_visualization_shells.py`**
-   **Core functionality**: Generates the detailed, layered 3D visualization for the planet Uranus and its environment.
-   **Key Features**: Models Uranus's unique structure, including its small rocky core, "icy" mantle, layered atmosphere, and its complex ring system. A key feature is the implementation of the compound rotation required to correctly orient the planet's rings, radiation belts, and magnetosphere, reflecting its extreme axial tilt of ~98 degrees.

**`venus_visualization_shells.py`**
-   **Core functionality**: Creates the scientifically-based, layered 3D visualization for the planet Venus.
-   **Key Features**: Renders models for Venus's internal structure (core, mantle, crust) and its external features, including its incredibly dense atmosphere, its weak "induced" magnetosphere (formed by interaction with the solar wind), and its gravitational Hill sphere. It uses `Mesh3d` for solid surfaces to improve rendering performance.

**`verify_orbit_cache.py`** ✅ **NEW UTILITY**
- Safe verification tool for orbit cache health
- Creates timestamped backups before verification
- Reports statistics on cache contents
- Repair mode for corrupted entries

**`visualization_2d.py`**
-   **Core functionality**: The rendering engine for creating 2D Hertzsprung-Russell (H-R) diagrams.
-   **Key Features**: Takes processed star data and generates an interactive H-R plot using Plotly. It correctly handles the logarithmic axes for luminosity and the reversed temperature axis. It also adds crucial visual aids like colored vertical bands for spectral types (O, B, A, F, G, K, M) and annotations for stellar evolution regions like the Main Sequence, Giants, and White Dwarfs.

**`visualization_3d.py`**
-   **Core functionality**: The rendering engine for creating interactive 3D stellar neighborhood plots.
-   **Key Features**: Plots stars in a 3D Cartesian coordinate system (X, Y, Z in light-years). It dynamically manages marker size based on apparent magnitude and marker color based on surface temperature. It includes specialized logic to render and style different object types, such as regular stars, the Sun, and non-stellar deep-sky objects, with distinct markers and legend entries.

**`visualization_core.py`**
-   **Core functionality**: A utility module containing shared functions used by both `visualization_2d.py` and `visualization_3d.py` to ensure consistency and reduce code duplication.
-   **Key Features**: Provides common functionalities like `create_hover_text` for generating detailed tooltips, `prepare_temperature_colors` for consistent color mapping based on stellar temperature, and `analyze_star_counts` for generating the summary statistics used in plot titles and footers.

**`visualization_utils.py`**
- **Core functionality**: Provides shared utilities that enhance the user experience of Plotly figures across the entire application.
- **Key Features**: Implements the critical `add_hover_toggle_buttons` function, which adds the "Full Object Info" / "Object Names Only" toggle to visualizations. It also contains helper functions for formatting hover text consistently and ensuring that animated figures retain their full hover functionality across frames.


## 🚀 Python Installation & Quick Start

This guide provides the official, tested method for setting up Paloma's Orrery on a Windows machine. Implementation for Mac would require significant refactoring, especially with threading. 

### Step 1: Install Python

If you don't have Python, download the latest version from the official website: [python.org/downloads](https://www.python.org/downloads/).

  * **Important**: During installation, make sure to check the box that says **"Add Python to PATH"**.

### Step 2: Download the Orrery

1.  Go to the GitHub repository: [github.com/tonylquintanilla/palomas\_orrery](https://github.com/tonylquintanilla/palomas_orrery)
2.  Click the green **"Code"** button and select **"Download ZIP"**.
3.  Extract the ZIP file to a location of your choice (e.g., your Documents folder).

### Step 3: Install Required Libraries

1.  Open the **Command Prompt** (search for `cmd` in the Windows Start Menu).
2.  Navigate to the folder where you extracted the project files.
    ```bash
    # Example:
    cd C:\Users\YourName\Documents\palomas_orrery
    ```
3.  Install all the necessary libraries using the `requirements.txt` file included in the project. This single command handles everything.
    ```bash
    pip install -r requirements.txt
    ```

**What these libraries do:**

# Core data processing and scientific computing
numpy>=1.24.0         # Array processing, required by multiple dependencies
pandas>=2.0.0         # Data manipulation and analysis
scipy>=1.11.0         # Scientific computing

# Astronomical calculations and data access
astropy>=5.3.4        # Core astronomy library
astroquery>=0.4.6     # Access to astronomical databases
JPL_Horizons>=2.1.0   # JPL Horizons system interface

# Plotting and visualization
plotly>=5.18.0        # Interactive plotting library
kaleido>=0.2.1        # Required for saving static plotly images
pillow>=10.0.0        # Image processing, required by kaleido

# GUI and interface
tk>=0.1.0             # Tkinter for GUI
customtkinter>=5.2.0  # Modern themed widgets for tkinter

# Date and time handling
python-dateutil>=2.8.2  # Extended datetime functionality
pytz>=2023.3          # Timezone support

# Network and web
requests>=2.31.0      # HTTP library
beautifulsoup4>=4.12.0  # HTML parsing for web scraping
html5lib>=1.1         # HTML parsing backend

# File formats and data handling
h5py>=3.10.0          # HDF5 file format support
astropy-healpix>=1.0.0  # HEALPix support for astronomy
pyvo>=1.4             # Virtual Observatory access

# Development and debugging
ipython>=8.12.0       # Enhanced interactive Python shell
jupyter>=1.0.0        # Notebook support (optional)

# Testing and quality
pytest>=7.4.0         # Testing framework (for development)
flake8>=6.1.0         # Code linting (for development)

# Optional but recommended
astroplan>=0.9        # Observation planning
regions>=0.7          # Astronomical region handling
reproject>=0.13       # Astronomical image reprojection

# Performance optimization
numba>=0.57.0         # JIT compilation for faster computation
dask>=2023.5.0        # Parallel computing (optional)

# System and environment
setuptools>=68.0.0    # Package installation tools
wheel>=0.41.0         # Built-package format

### Step 4: Run the Application

Navigate to the project folder in your File Explorer and double-click the **`palomas_orrery.py`** file. The application will start, and you can begin exploring\!

For the best experience, you can also run the program from an editor like **VS Code**, which allows you to see all console output and error messages directly.

**Explore solar visualizations**:
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

**For stellar visualizations** 
   - In palomas_orrery.py, the main GUI, click on the blue button at the bottom, "2D and 3D Star Visualizations"
   - (optional - run `star_visualization_gui.py`):

   *Note: The stellar visualization system creates its own data files when first used:*
   - **VOT files** (`hipparcos_data.vot`, `gaia_data.vot`): Downloaded astronomical data in VOTable format
   - **PKL files** (`star_properties_distance.pkl`, `star_properties_magnitude.pkl`): Processed star data for quick searching
   
   *These files are automatically created when you first run stellar visualizations and query the Hipparcos/Gaia databases. The GitHub repository does not include these files as they are generated based on your specific search parameters and preferences. These files can become quite large.*

**Verify your orbit cache** (optional - only after you've used the software):
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

**Apsidal Markers:**
- Plot any object with an orbit (planets, asteroids, comets)
- Look for the square markers indicating perihelion/apohelion
- Hover over markers to see the calculated dates
- Note how dates change based on where the object currently is in its orbit
- Observe special handling for hyperbolic objects that may show "Past perihelion"

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

- The user can change these setting in the GUI. If you modify the settings, click "Use updated intervals below to fetch data (will not be cached)" to use them.            

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