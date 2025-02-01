# Paloma's Orrery

An interactive solar system visualization tool with support for stellar neighborhood mapping and Hertzsprung-Russell diagrams.

## Summary

The provided code is a complex Python application that visualizes the solar system using data from the JPL Horizons system. It allows users to select celestial objects (planets, dwarf planets, moons, asteroids, comets, and missions) and visualize their positions and orbits on a given date or over a period of time.

Here's a breakdown of the code's functionality:

1. Initialization and Imports:

Imports necessary libraries like tkinter, astroquery, numpy, plotly, etc.
Defines constants for colors, orbital parameters, physical properties of celestial objects, and hover text.
Sets up a shutdown handler for graceful exit.
Initializes the main tkinter window (root).
Defines global variables like today.
2. UI Elements:

ScrollableFrame Class: Creates a custom scrollable frame to hold the numerous checkboxes.
Input Frame:
Date Selection: Entry widgets for year, month, day, and hour, along with a "Now" button to fill in the current date.
Object Selection: Checkbuttons for each celestial object, grouped into categories (Planets, Dwarf Planets, Moons, Asteroids, KBOs, Missions, Comets).
Center Object Selection: A dropdown menu to select the central body for the plot (Sun or a planet).
Scale Options: Radio buttons for automatic or manual scaling, with an entry for custom scale values.
Animation Controls: Entry for the number of frames and buttons to animate the motion over hours, days, weeks, months, or years.
"Paloma's Birthday" Buttons: Set the date to Paloma's birthday or animate from that date over years.
Stellar Visualization Buttons: Buttons to launch separate scripts (planetarium_distance.py, hr_diagram_distance.py, etc.) for visualizing stars and the Hertzsprung-Russell diagram.
Status Label and Progress Bar: Displays messages and a progress bar during data fetching and plotting.
Note Frame: A text area displaying additional information or instructions.
3. Core Functions:

create_sun_visualization(fig, animate=False, frames=None): Creates a 3D visualization of the Sun's layers (core, radiative zone, convective zone, photosphere, chromosphere, inner corona, outer corona, termination shock, heliopause, inner and outer Oort Cloud, and the Sun's gravitational influence) using sphere equations and adds them to a plotly figure.
create_corona_sphere(radius, n_points=100): Generates points to represent a spherical surface for the Sun's layers.
get_default_camera(): Returns default orthographic camera settings for a top-down view.
calculate_axis_range(objects_to_plot): Calculates the appropriate axis range for the plot based on the selected objects.
plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id='Sun', show_lines=False): Plots the actual orbital trajectories of selected objects fetched from the JPL Horizons system.
fetch_position(object_id, date_obj, center_id='Sun', id_type=None, override_location=None, mission_url=None, mission_info=None): Fetches the position of a celestial object for a specific date from the JPL Horizons system.
fetch_trajectory_with_batching(obj_id, dates_list, center_id='Sun', id_type=None, batch_size=50): Fetches the trajectory of an object over a range of dates, batching the requests to avoid URL length limitations.
fetch_trajectory(obj_id, dates_list, center_id='Sun', id_type=None): A wrapper for fetch_trajectory_with_batching.
print_planet_positions(positions): Prints the fetched positions and distances of planets to the console.
format_maybe_float(value): Formats a numeric value to 8 decimal places or returns "N/A" if the value is not numeric.
add_celestial_object(fig, obj_data, name, color, symbol='circle', marker_size=DEFAULT_MARKER_SIZE, hover_data="Full Object Info"): Adds a celestial object to the plotly figure with specified properties.
debug_trajectory_data(objects, selected_objects, center_id='Sun'): A debug function to analyze and print trajectory data, especially for missions and comets.
plot_objects(): The main function that orchestrates the plotting process:
Gets the user-selected date and center object.
Creates a plotly figure.
Adds the Sun's visualization if the Sun is the center.
Fetches positions and trajectories of selected objects.
Adds objects to the plot using add_celestial_object.
Plots idealized orbits if the center is the Sun using plot_idealized_orbits.
Sets the axis ranges and updates the layout.
Displays the plot using show_figure_safely.
plot_idealized_orbits(fig, objects_to_plot, center_id='Sun'): Plots idealized Keplerian orbits for planets and dwarf planets based on orbital parameters (semi-major axis, eccentricity, inclination, etc.). It handles rotations to account for the argument of periapsis and longitude of the ascending node. It skips satellites, comets, and missions.
show_animation_safely(fig, default_name): Displays and optionally saves an animated plotly figure, handling temporary file cleanup.
animate_objects(step, label): Creates the animation by generating a sequence of frames and updating the plot accordingly.
on_closing(): Handles cleanup (removing temporary files) when the main window is closed.
fill_now(): Fills the date entry fields with the current date and time.
set_palomas_birthday(): Sets the date to Paloma's birthday.
update_date_fields(new_date): Updates the date entry fields with a given date.
handle_mission_selection(): Handles mission selection (currently does not adjust the date).
animate_one_day(), animate_one_week(), animate_one_month(), animate_one_year(), animate_palomas_birthday(): Wrapper functions for animate_objects with specific time steps.
CreateToolTip(object, text): Creates a custom tooltip for a given widget with intelligent positioning.
report_callback_exception(self, exc_type, exc_value, exc_traceback): Handles exceptions in Tkinter callbacks.
call_planetarium_distance_script_with_input(): Calls the planetarium_distance.py script with user input for the number of light-years.
call_planetarium_apparent_magnitude_script_with_input(): Calls the planetarium_apparent_magnitude.py script with user input for the maximum apparent magnitude and optionally, the manual scale.
call_hr_diagram_distance_script_with_input(): Calls the hr_diagram_distance.py script with user input for the number of light-years.
call_hr_diagram_apparent_magnitude_script_with_input(): Calls the hr_diagram_apparent_magnitude.py script with user input for the maximum apparent magnitude.
4. Object Data:

The objects list defines the celestial objects that can be selected and visualized. Each object has properties like:
name: The name of the object.
id: The JPL Horizons ID.
var: The tkinter variable linked to the object's checkbox.
color: The color used for plotting.
symbol: The marker symbol used for plotting.
is_mission: Boolean indicating if it's a space mission.
is_comet: Boolean indicating if it's a comet.
id_type: The type of ID used in JPL Horizons (e.g., 'majorbody', 'smallbody', 'id').
start_date, end_date: For missions and comets, the start and end dates of their activity.
mission_url: A URL with more information about the mission.
mission_info: A brief description of the mission or object.
is_satellite: Boolean indicating if the object is a satellite.
5. Main Loop:

root.mainloop() starts the tkinter event loop, making the application interactive.

## Features

- Real-time 3D visualization of celestial objects using NASA JPL Horizons data
- Interactive plots of planets, dwarf planets, moons, asteroids, and space missions
- Solar system animation capabilities (days, weeks, months, years)
- Detailed visualization of the Sun's structure from core to heliopause and Oort Cloud
- Stellar neighborhood mapping up to 100 light-years
- Hertzsprung-Russell diagrams for stellar classification
- Support for both distance-based and apparent magnitude-based star plotting
- Visualization of Messier objects (nebulae and star clusters)
- Interactive camera controls and notable star navigation
- Toggle between detailed and simplified hover information

## Requirements

### Python Version
- Python 3.8 or higher

### Required Libraries
```
numpy>=1.24.0
pandas>=2.0.0
plotly>=5.18.0
astropy>=5.3.4
astroquery>=0.4.6
kaleido>=0.2.1  # Required for saving static images
tk>=0.1.0
python-dateutil>=2.8.2
requests>=2.31.0
ipython>=8.12.0
scipy>=1.11.0  # Add this line

### Installation

1. Clone this repository:
```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main program:
```bash
python palomas_orrery.py
```

2. Using the Interface:
   - Select celestial objects from the scrollable menu
   - Choose a center object (default: Sun)
   - Set the date and time for visualization
   - Select scale options (Auto or Manual)
   - Generate different types of visualizations:
     * Solar System 3D plots
     * Stellar neighborhood 3D plots (distance or magnitude based)
     * Hertzsprung-Russell diagrams (2D)

## Visualization Types

### 1. Solar System
- Interactive 3D plots with accurate orbital trajectories
- Detailed Sun visualization from core to outer corona
- Mission paths and comet trajectories
- Animated position tracking
- Scale options from planetary orbits to Oort Cloud

### 2. Stellar Neighborhood
- **Distance-based mapping:**
  * Up to 100 light-years from Sun
  * Shows actual stellar positions in 3D space
  * Combined data from Hipparcos and Gaia catalogs

- **Apparent magnitude plots:**
  * Range from -1.44 (Sirius) to 9.0 (space visibility limit)
  * Includes Messier objects
  * Shows both nearby and distant bright stars
  * Reveals galactic structure at higher magnitudes

### 3. Hertzsprung-Russell Diagrams
- Temperature vs Luminosity plots
- Stellar classification visualization
- Main sequence and evolved star populations
- Options for both distance and magnitude-limited samples

## Data Files

The program creates and uses several data cache files:

### VOTable Files (.vot)
1. `hipparcos_data_magnitude.vot` (~193KB)
2. `gaia_data_magnitude.vot` 
   - ~1.2MB for magnitude 4 (default)
   - Up to ~292MB for magnitude 9
3. `hipparcos_data_distance.vot` (~30KB)
4. `gaia_data_distance.vot` (~9.4MB)

### Property Cache Files (.pkl)
1. `star_properties_magnitude.pkl` (~12MB)
2. `star_properties_distance.pkl` (~1MB)

Note: Files are created on first run and reused in subsequent sessions.

## Data Sources

- Solar system positions: [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- Stellar data:
  * [Hipparcos Catalog](https://www.cosmos.esa.int/web/hipparcos)
  * [Gaia DR3](https://www.cosmos.esa.int/web/gaia)
- Object properties: [SIMBAD database](http://simbad.u-strasbg.fr/simbad/)
- Messier objects: [SEDS Messier Database](http://www.messier.seds.org/)

## Performance Notes

- Initial data fetching may take several minutes, especially for higher magnitude limits
- Animation speed depends on number of objects selected
- Large-scale visualizations (e.g., Oort Cloud) may require manual scale adjustment
- Toggle between detailed and simple hover text can improve performance

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants.
Updated January 16, 2025.

## License

MIT License - See LICENSE file for details.