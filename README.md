# Paloma's Orrery

An interactive solar system visualization tool with support for stellar neighborhood mapping.

## Features

- Real-time 3D visualization of celestial objects using NASA JPL Horizons data
- Interactive plots of planets, dwarf planets, moons, asteroids, and space missions
- Solar system animation capabilities (days, weeks, months, years)
- Detailed visualization of the Sun's structure from core to outer corona
- Stellar neighborhood mapping up to 100 light-years
- Hertzsprung-Russell diagrams for stellar classification
- Support for both distance-based and apparent magnitude-based star plotting

## Requirements

- Python 3.8+
- Required Python packages:
  - astropy
  - astroquery
  - numpy
  - pandas
  - plotly
  - tkinter
  - kaleido (for saving static images)

numpy>=1.24.0
pandas>=2.0.0
plotly>=5.18.0
astropy>=5.3.4
astroquery>=0.4.6
kaleido>=0.2.1
tk>=0.1.0
python-dateutil>=2.8.2
requests>=2.31.0
webbrowser>=0.0.1
matplotlib>=3.8.0
scipy>=1.11.3

requirements.txt includes all necessary packages for running Paloma's Orrery:

Core numerical and data processing libraries
Plotting and visualization tools
Astronomical data access
GUI components
Supporting utilities

Users can install these requirements using:
pip install -r requirements.txt

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
```

2. Install required packages:
```bash
pip install astropy astroquery numpy pandas plotly kaleido
```

## Usage

1. Run the main program:
```bash
python palomas_orrery.py
```

2. Use the GUI to:
   - Select celestial objects to visualize
   - Choose dates and time intervals
   - Set visualization scale
   - Select animation modes
   - Generate stellar neighborhood maps

## Visualization Types

1. Solar System:
   - Interactive 3D plots
   - Accurate orbital trajectories
   - Mission paths
   - Solar structure visualization

2. Stellar Neighborhood:
   - Distance-based mapping (up to 100 light-years)
   - Apparent magnitude plots (-1.44 to 9.0)
   - Hertzsprung-Russell diagrams
   - Messier object visualization

## Data Sources

- Solar system positions: [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- Star data: 
  - [Hipparcos Catalog](https://www.cosmos.esa.int/web/hipparcos)
  - [Gaia DR3](https://www.cosmos.esa.int/web/gaia)
- Object properties: [SIMBAD database](http://simbad.u-strasbg.fr/simbad/)

There are 4 data storage files created and used by the script. Some are very large, but they need to be created only once:

*.vot files:
1. hipparcos_data_magnitude.vot  (~ 193KB -- generated anew.)
2. gaia_data_magnitude.vot  (~292MB -- this file is very large and will take a very long time to generate. Watch your terminal output for progress in batches. I recommend running it over night and disable sleep mode! The script is fetching data from Gaia DR3.)
3. hipparcos_data_distance.vot  (~30KB -- generated anew.)
4. gaia_data_distance.vot  (~9.4MB)

*.pkl files:
1. star_properties_magnitude.pkl  (~12MB)
2. star_properties_distance.pkl  (~1MB)

These files store:
- .vot: Star catalog data from Hipparcos and Gaia missions
- .pkl: Cached star properties retrieved from SIMBAD database

The files are created when first running the program and reused in subsequent runs to avoid re-fetching data.

# Data Flow for Solar Plots

## 1. Data Acquisition Flow

### Static Plot (plot_objects)
```
fetch_position() → plot_objects() → add_celestial_object() → Plotly Figure
```

1. **fetch_position** (data_acquisition.py):
   - Queries JPL Horizons system for object coordinates
   - Returns dictionary with:
     - Position (x, y, z in AU)
     - Range from center
     - Velocity components
     - Distance in light-minutes/hours
     - Orbital period

2. **plot_objects** (palomas_orrery.py):
   - Collects positions for all selected objects
   - Handles center object selection
   - Manages scale calculations
   - Creates base Plotly figure

3. **add_celestial_object** (visualization_utils.py):
   - Creates individual Plotly traces
   - Adds hover text and formatting
   - Handles marker properties

### Animation Flow (animate_objects)
```
fetch_position() → animation_worker() → create frames → Plotly Animation
```

1. **animation_worker** (palomas_orrery.py):
   - Generates date sequence
   - Pre-calculates orbital periods
   - Creates position cache

2. **Frame Generation**:
   - Creates series of frames from position data
   - Each frame contains:
     - Updated positions
     - Hover text
     - Marker properties

## 2. Data Processing Chain

### Position Data Processing
```
JPL Horizons → fetch_position() → calculate_distances() → calculate_cartesian_coordinates()
```

- **fetch_position**:
  ```python
  {
      'x': float,  # AU
      'y': float,  # AU
      'z': float,  # AU
      'range': float,  # Distance from center (AU)
      'velocity': float,  # AU/day
      'distance_lm': float,  # Light-minutes
      'distance_lh': float,  # Light-hours
      'orbital_period': float  # Earth years
  }
  ```

### Scale Calculation Flow
```
get_positions() → calculate_axis_range() → update_layout()
```

- Determines plot boundaries based on:
  - Object positions
  - Manual/auto scaling settings
  - Center object selection

## 3. Visualization Pipeline

### Base Plot Creation
```
create_figure() → add_sun_visualization() → add_celestial_objects() → add_hover_controls()
```

### Animation Frame Generation
```
create_frames() → update_positions() → update_traces() → create_animation()
```

## 4. Key Data Structures

### Object Definition
```python
{
    'name': str,
    'id': str,
    'var': tk.IntVar,
    'color': str,
    'symbol': str,
    'is_mission': bool,
    'id_type': str,
    'start_date': datetime,  # For missions/comets
    'end_date': datetime,    # For missions/comets
    'mission_info': str      # Optional
}
```

### Position Data
```python
{
    'x': float,
    'y': float,
    'z': float,
    'range': float,
    'velocity': float,
    'distance_lm': float,
    'distance_lh': float,
    'orbital_period': float
}
```

## 5. Error Handling

- Data fetch failures handled in fetch_position()
- Position calculation errors managed in calculate_distances()
- Animation frame generation errors caught in animation_worker()
- Scale calculation fallbacks in calculate_axis_range()

## 6. Performance Considerations

- Position data cached during animations
- Batch processing for multiple objects
- Asynchronous data fetching for animations
- Scale calculations optimized for large datasets

This data flow documentation provides a comprehensive overview of how data moves through the system from initial acquisition to final visualization, helping developers understand the system architecture and data transformations at each step.

## Data Flow for Stellar Plots

The stellar data pipeline processes data through multiple modules to create visualizations:

1. Initial Data Acquisition:
   - Module: data_acquisition.py
     * initialize_vizier(): Sets up connection to VizieR service
     * load_or_fetch_hipparcos_data(): Fetches Hipparcos stars
     * load_or_fetch_gaia_data(): Fetches Gaia stars
     * calculate_parallax_limit(): Determines minimum parallax for distance filtering

2. Data Processing Pipeline:

   a) Distance-based plots (hr_diagram_distance.py, planetarium_distance.py):
      - Data Processing (data_processing.py):
        * calculate_distances(): Converts parallax to distances
        * calculate_cartesian_coordinates(): Computes 3D positions
        * select_stars_by_distance(): Filters stars within distance limit
      - Star Properties (star_properties.py):
        * load_existing_properties(): Checks cache for stellar data
        * query_simbad_for_star_properties(): Fetches new properties
        * assign_properties_to_data(): Adds properties to star data
      - Stellar Parameters (stellar_parameters.py):
        * calculate_stellar_parameters(): Computes temperatures and luminosities
        * estimate_temperature_from_spectral_type(): Temperature from spectral class
        * calculate_bv_temperature(): Temperature from B-V color
      - Visualization:
        * prepare_2d_data() or prepare_3d_data(): Formats data for plotting
        * create_hr_diagram() or create_3d_visualization(): Generates final plot

   b) Magnitude-based plots (hr_diagram_apparent_magnitude.py, planetarium_apparent_magnitude.py):
      - Data Processing (data_processing.py):
        * estimate_vmag_from_gaia(): Converts Gaia G magnitudes to V
        * select_stars_by_magnitude(): Separates Hipparcos and Gaia data
        * align_coordinate_systems(): Standardizes coordinates
      - Messier Objects (messier_object_data_handler.py):
        * get_visible_objects(): Fetches visible Messier objects
        * create_dataframe(): Formats Messier data
      - Visualization Core (visualization_core.py):
        * analyze_magnitude_distribution(): Studies magnitude ranges
        * create_hover_text(): Generates interactive labels
        * generate_star_count_text(): Prepares statistics

3. Data Storage and Caching:
   - Handled by data_acquisition.py:
     * validate_votable_file(): Checks data file integrity
     * save_properties_to_file(): Caches stellar properties
     * format_file_size(): Handles file size reporting
   - Progress reporting via ProgressReporter class:
     * start_operation(): Begins data operation
     * file_operation(): Handles file operations
     * catalog_stats(): Reports statistics

4. Visualization Components:
   - visualization_2d.py:
     * create_hr_diagram(): Generates HR diagrams
     * generate_footer_text(): Adds plot information
   - visualization_3d.py:
     * create_3d_visualization(): Creates 3D star plots
     * parse_stellar_classes(): Processes spectral types
     * create_notable_stars_list(): Handles star selection
   - visualization_utils.py:
     * add_hover_toggle_buttons(): Adds interactivity
     * format_hover_text(): Creates tooltips
     * update_figure_frames(): Handles animation frames

5. Error Handling and Cleanup:
   - shutdown_handler.py:
     * PlotlyShutdownHandler: Manages graceful shutdowns
     * create_monitored_thread(): Handles background tasks
     * show_figure_safely(): Manages plot display and saving

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants. Updated January 12, 2025.

## License

MIT License - See LICENSE file for details.