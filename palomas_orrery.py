#Paloma's Orrery - Solar System Visualization Tool

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from astroquery.jplhorizons import Horizons
import numpy as np
from datetime import datetime, timedelta
import calendar
import plotly.graph_objs as go
import webbrowser
import os
import warnings
from astropy.utils.exceptions import ErfaWarning
from astropy.time import Time
import traceback
import threading
import time  # Used here for simulation purposes
import subprocess
import sys
import math
import json
import orbit_data_manager
import shutil

from palomas_orrery_helpers import (calculate_planet9_position_on_orbit, rotate_points2, calculate_axis_range,
                                    fetch_trajectory, fetch_orbit_path, pad_trajectory, add_url_buttons,
                                    get_default_camera, print_planet_positions, create_orbit_backup, cleanup_old_orbits, show_animation_safely)
from idealized_orbits import plot_idealized_orbits, planetary_params, parent_planets, planet_tilts, rotate_points 
from formatting_utils import format_maybe_float, format_km_float
from shared_utilities import create_sun_direction_indicator
from planet_visualization import (
    create_celestial_body_visualization,
    create_planet_visualization,
    create_planet_shell_traces,
    create_sun_visualization,

    mercury_inner_core_info,
    mercury_outer_core_info,
    mercury_mantle_info,
    mercury_crust_info,
    mercury_atmosphere_info,
    mercury_magnetosphere_info,
    mercury_hill_sphere_info,

    venus_core_info,
    venus_mantle_info,
    venus_crust_info,
    venus_atmosphere_info,
    venus_upper_atmosphere_info,
    venus_magnetosphere_info,
    venus_hill_sphere_info,

    earth_inner_core_info,
    earth_outer_core_info,
    earth_lower_mantle_info,
    earth_upper_mantle_info,
    earth_crust_info,
    earth_atmosphere_info,
    earth_upper_atmosphere_info,
    earth_magnetosphere_info,
    earth_hill_sphere_info,

    moon_inner_core_info,
    moon_outer_core_info,
    moon_mantle_info,
    moon_crust_info,
    moon_exosphere_info,
    moon_hill_sphere_info,

    mars_inner_core_info,
    mars_outer_core_info,
    mars_mantle_info,
    mars_crust_info,
    mars_atmosphere_info,
    mars_upper_atmosphere_info,
    mars_magnetosphere_info,
    mars_hill_sphere_info,

    jupiter_core_info,
    jupiter_metallic_hydrogen_info,
    jupiter_molecular_hydrogen_info,
    jupiter_cloud_layer_info,
    jupiter_upper_atmosphere_info,
    jupiter_ring_system_info,
    jupiter_radiation_belts_info,
    jupiter_io_plasma_torus_info,
    jupiter_magnetosphere_info,
    jupiter_hill_sphere_info,

    saturn_core_info,
    saturn_metallic_hydrogen_info,
    saturn_molecular_hydrogen_info,
    saturn_cloud_layer_info,
    saturn_upper_atmosphere_info,
    saturn_ring_system_info,
    saturn_radiation_belts_info,
    saturn_enceladus_plasma_torus_info,
    saturn_magnetosphere_info,
    saturn_hill_sphere_info,

    uranus_core_info,
    uranus_mantle_info,
    uranus_cloud_layer_info,
    uranus_upper_atmosphere_info,
    uranus_ring_system_info,
    uranus_radiation_belts_info,
    uranus_magnetosphere_info,
    uranus_hill_sphere_info, 

    neptune_core_info,
    neptune_mantle_info,
    neptune_cloud_layer_info,
    neptune_upper_atmosphere_info,
    neptune_ring_system_info,
    neptune_radiation_belts_info,
    neptune_magnetosphere_info,
    neptune_hill_sphere_info,

    pluto_core_info,
    pluto_mantle_info,
    pluto_crust_info,
    pluto_haze_layer_info,
    pluto_atmosphere_info,
    pluto_hill_sphere_info,

    eris_core_info,
    eris_mantle_info,
    eris_crust_info,
    eris_atmosphere_info,
    eris_hill_sphere_info, 

    planet9_surface_info,
    planet9_hill_sphere_info           
)

from solar_visualization_shells import (
    hover_text_sun,
    gravitational_influence_info,
    galactic_tide_info,
    hills_cloud_torus_info,
    outer_oort_clumpy_info,

    outer_oort_info,
    inner_oort_info,
    inner_limit_oort_info,

    solar_wind_info,
    termination_shock_info,
    outer_corona_info,
    inner_corona_info,
    chromosphere_info,
    photosphere_info,
    radiative_zone_info,
    core_info
)

from constants_new import (
    color_map,
    note_text,
    INFO,
    CENTER_BODY_RADII,
    KM_PER_AU, 
    LIGHT_MINUTES_PER_AU,
    KNOWN_ORBITAL_PERIODS
)

from visualization_utils import (format_hover_text, add_hover_toggle_buttons, format_detailed_hover_text)

from save_utils import save_plot

from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun

# Constants
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit
KM_PER_AU = 149597870.7       # Kilometers per Astronomical Unit
CORE_AU = 0.00093               # Core in AU, or approximately 0.2 Solar radii
RADIATIVE_ZONE_AU = 0.00325     # Radiative zone in AU, or approximately 0.7 Solar radii
SOLAR_RADIUS_AU = 0.00465047  # Sun's radius in AU
INNER_LIMIT_OORT_CLOUD_AU = 2000   # Inner Oort cloud inner boundary in AU.
INNER_OORT_CLOUD_AU = 20000   # Inner Oort cloud outer boundary in AU.
OUTER_OORT_CLOUD_AU = 100000   # Oort cloud outer boundary in AU.
GRAVITATIONAL_INFLUENCE_AU = 126000   # Sun's gravitational influence in AU.
CHROMOSPHERE_RADII = 1.5    # The Chromosphere extends from about 1 to 1.5 solar radii or about 0.00465 - 0.0070 AU
INNER_CORONA_RADII = 3  # Inner corona extends to 2 to 3 solar radii or about 0.01 AU
OUTER_CORONA_RADII = 50       # Outer corona extends up to 50 solar radii or about 0.2 AU, more typically 10 to 20 solar radii
TERMINATION_SHOCK_AU = 94       # Termination shock where the solar wind slows to subsonic speeds. 
HELIOPAUSE_RADII = 26449         # Outer boundary of the solar wind and solar system, about 123 AU. 
PARKER_CLOSEST_RADII = 8.2    # Parker's closest approach was 3.8 million miles on 12-24-24 at 6:53 AM EST (0.41 AU, 8.2 solar radii)

# Add these constants after existing constants
TEMP_CACHE_FILE = "orbit_paths_temp.json"
CLEANUP_TRACKING_FILE = ".last_orbit_cleanup"
temp_cache = {}  # In-memory temporary cache
remember_update_choice = None  # Session memory for dialog choice
update_choice_remembered = False  # Flag for remembering choice

print("Interpreter:", sys.executable)
print("Working directory:", os.getcwd())

# File to persist orbit path data between sessions
# ORBIT_PATHS_FILE = "orbit_paths.json"

# Create a global shutdown handler instance
shutdown_handler = PlotlyShutdownHandler()

# Initialize the main window
root = tk.Tk()
root.title("Paloma's Orrery -- Updated: June 2, 2025")
# Define 'today' once after initializing the main window
today = datetime.today()
# Add this line:
STATIC_TODAY = today  # Static reference date for orbit calculations

# First, create a container frame for the controls column
controls_container = tk.Frame(root)
controls_container.grid(row=0, column=1, padx=(5, 10), pady=(10, 10), sticky='n')

# Add these lines after creating controls_container
controls_container.grid_propagate(False)

# And add this to make it expand properly:
controls_container.pack_propagate(False)
controls_container.grid_propagate(False)
controls_container.config(width=450, height=750)  # Wider container

# Create a canvas inside the container
controls_canvas = tk.Canvas(controls_container, bg='SystemButtonFace')
controls_scrollbar = tk.Scrollbar(controls_container, orient="vertical", command=controls_canvas.yview, width=16)

# Configure the canvas
controls_canvas.configure(yscrollcommand=controls_scrollbar.set)
controls_canvas.pack(side="left", fill="both", expand=True)
controls_scrollbar.pack(side="right", fill="y")

# Create the frame that will contain all the controls
controls_frame = tk.Frame(controls_canvas, bg='SystemButtonFace')

# Add these lines after controls_frame is created
controls_container.configure(bg='SystemButtonFace')
controls_canvas.configure(bg='SystemButtonFace')
controls_frame.configure(bg='SystemButtonFace')

# Update the canvas window creation with explicit width
controls_window = controls_canvas.create_window(
    (0, 0),  # Position at top-left corner
    window=controls_frame,
    anchor="nw",
    width=controls_canvas.winfo_width(),  # Match canvas width
    tags="controls"  # Add a tag for easier reference
)

# Function to fetch the position of a celestial object for a specific date
def fetch_position(object_id, date_obj, center_id='Sun', id_type=None, override_location=None, mission_url=None, mission_info=None):  
 
    # Skip fetching for Planet 9 and use accurate position on orbit
    if object_id == 'planet9_placeholder':
        # Calculate position directly on the theoretical orbit
        x, y, z, range_val = calculate_planet9_position_on_orbit()
        
        # Return a complete position object with all necessary fields
        return {
            'x': x,
            'y': y,
            'z': z,
            'range': range_val,   # Distance based on IRAS/AKARI study estimate
            'vx': 0,
            'vy': 0,
            'vz': 0,
            'velocity': 0,
            'distance_km': range_val * KM_PER_AU,
            'distance_lm': range_val * LIGHT_MINUTES_PER_AU,
            'distance_lh': (range_val * LIGHT_MINUTES_PER_AU) / 60,
            'mission_info': "Planet 9 candidate identified in 2025 IRAS/AKARI infrared data analysis."
        }
        
    try:
        # Convert date to Julian Date
        times = Time([date_obj])
        epochs = times.jd.tolist()

        # Set location
        if override_location is not None:
            location = override_location
        else:
            location = '@' + str(center_id)

        # Query the Horizons system with coordinates relative to location
        obj = Horizons(id=object_id, id_type=id_type, location=location, epochs=epochs)
        vectors = obj.vectors()

        if len(vectors) == 0:
            print(f"No data returned for object {object_id} on {date_obj}")
            return None

        # Extract desired fields with error handling
        x = float(vectors['x'][0]) if 'x' in vectors.colnames else None
        y = float(vectors['y'][0]) if 'y' in vectors.colnames else None
        z = float(vectors['z'][0]) if 'z' in vectors.colnames else None
        range_ = float(vectors['range'][0]) if 'range' in vectors.colnames else None  # Distance in AU from the Sun
        range_rate = float(vectors['range_rate'][0]) if 'range_rate' in vectors.colnames else None  # AU/day
        vx = float(vectors['vx'][0]) if 'vx' in vectors.colnames else None  # AU/day
        vy = float(vectors['vy'][0]) if 'vy' in vectors.colnames else None
        vz = float(vectors['vz'][0]) if 'vz' in vectors.colnames else None
        velocity = np.sqrt(vx**2 + vy**2 + vz**2) if vx is not None and vy is not None and vz is not None else 'N/A'

        # Calculate distance in light-minutes and light-hours
        distance_km = range_ * KM_PER_AU if range_ is not None else 'N/A'
        distance_lm = range_ * LIGHT_MINUTES_PER_AU if range_ is not None else 'N/A'
        distance_lh = (distance_lm / 60) if isinstance(distance_lm, float) else 'N/A'

        # Find object name from id
        obj_name = next((obj['name'] for obj in objects if obj['id'] == object_id), None)
        
        # Initialize orbital period values
        calculated_orbital_period = 'N/A'
        known_orbital_period = 'N/A'
        orbital_period = 'N/A'  # Keep the original variable for backward compatibility
        
        # Find object name from id
        obj_name = next((obj['name'] for obj in objects if obj['id'] == object_id), None)
        
        # Check if it's a planetary satellite
        is_satellite = False
        for planet, satellites in parent_planets.items():
            if obj_name in satellites:
                is_satellite = True
                break

        # Get the known orbital period if available
        if obj_name in KNOWN_ORBITAL_PERIODS:
            known_value = KNOWN_ORBITAL_PERIODS[obj_name]

            if is_satellite:
                # For satellites, the values are in days
                known_orbital_period = {
                    'days': known_value,
                    'years': known_value / 365.25
                }
                # For satellites, use the known period as the main orbital_period
                orbital_period = known_orbital_period['years']
            else:
                # For non-satellites, the values are in years
                known_orbital_period = {
                    'years': known_value,
                    'days': known_value * 365.25
                }
                orbital_period = known_value  # Use the known value directly

            # Check if the value is in years or days
    #        if known_value < 100:  # Assume it's days if less than 100
    #            known_orbital_period = {
    #                'days': known_value,
    #                'years': known_value / 365.25
    #            }
    #        else:  # It's in days
    #            known_orbital_period = {
    #                'days': known_value,
    #                'years': known_value / 365.25
    #            }
        
        # Check if it's a planetary satellite
    #    is_satellite = False
    #    for planet, satellites in parent_planets.items():
    #        if obj_name in satellites:
    #            is_satellite = True
    #            break
                
        # Only calculate the orbital period for non-satellites
        if not is_satellite and obj_name and obj_name in planetary_params:
            a = planetary_params[obj_name]['a']  # Semi-major axis in AU
            orbital_period_years = np.sqrt(a ** 3)  # Period in Earth years
            calculated_orbital_period = {
                'years': orbital_period_years,
                'days': orbital_period_years * 365.25
            }
            # If no known period, use the calculated one
            if orbital_period == 'N/A':
                orbital_period = orbital_period_years

        return {
            'x': x,
            'y': y,
            'z': z,
            'range': range_,
            'range_rate': range_rate,
            'vx': vx,
            'vy': vy,
            'vz': vz,
            'velocity': velocity,\
            'distance_km': distance_km,
            'distance_lm': distance_lm,
            'distance_lh': distance_lh,
            'mission_info': mission_info,  # Include mission info if available
            'calculated_orbital_period': calculated_orbital_period,  # New: separated calculated period
            'known_orbital_period': known_orbital_period,  # New: added known period from reference data
            'orbital_period': orbital_period  # Original variable preserved for backward compatibility
        }
    except Exception as e:
        print(f"Error fetching data for object {object_id} on {date_obj}: {e}")
        return None

def add_celestial_object(fig, obj_data, name, color, symbol='circle', marker_size=DEFAULT_MARKER_SIZE, hover_data="Full Object Info", 
                         center_object_name=None):
    
    # Skip if there's no data
    if obj_data is None or obj_data['x'] is None:
        return

    print(f"\nAdding trace for {name}:")
    
    # Use the consolidated function for hover text
    full_hover_text, minimal_hover_text, satellite_note = format_detailed_hover_text(
        obj_data, 
        name, 
        center_object_name,
        objects,
        planetary_params,
        parent_planets,
        CENTER_BODY_RADII,
        KM_PER_AU,
        LIGHT_MINUTES_PER_AU,
        KNOWN_ORBITAL_PERIODS
    )
    
    # Add satellite note if present
    if satellite_note:
        full_hover_text += satellite_note
    
    print(f"Full hover text: {full_hover_text}")
    print(f"Minimal hover text: {minimal_hover_text}")

    fig.add_trace(
        go.Scatter3d(
            x=[obj_data['x']],
            y=[obj_data['y']],
            z=[obj_data['z']],
            mode='markers',
            marker=dict(
                symbol=symbol,
                color=color,
                size=marker_size
            ),
            name=name,
            text=[full_hover_text],  # Important: Wrap in list
            customdata=[minimal_hover_text],  # Important: Wrap in list
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )

# Helper function for status display with history
status_history = []
def update_status_display(message, status_type='info'):
    """Update status display with color coding and history"""
    global status_history
    
    # Color mapping
    color_map = {
        'info': 'black',
        'success': 'green',
        'warning': 'orange',
        'error': 'red',
        'special': 'blue'
    }
    
    # Add timestamp
    timestamp = datetime.now().strftime("%H:%M:%S")
    status_entry = {
        'time': timestamp,
        'message': message,
        'color': color_map.get(status_type, 'black')
    }
    
    # Add to history (keep last 3)
    status_history.append(status_entry)
    if len(status_history) > 3:
        status_history.pop(0)
    
    # Update display if status_display exists
    if 'status_display' in globals() and status_display:
        display_text = ""
        for entry in status_history:
            display_text += f"[{entry['time']}] {entry['message']}\n"
        display_text += "Refer to terminal for more details"
        
        status_display.config(text=display_text)
        
        # Color the most recent line
        if status_history:
            status_display.config(fg=status_history[-1]['color'])

def configure_controls_canvas(event):
    # Update the scrollregion to encompass the inner frame
    controls_canvas.configure(scrollregion=controls_canvas.bbox("all"))
    
    # Set the canvas window width to match the canvas width
    controls_canvas.itemconfig(controls_window, width=controls_canvas.winfo_width())
    
    # Force a redraw of the canvas
    controls_canvas.update_idletasks()

controls_frame.bind("<Configure>", configure_controls_canvas)

# Bind mousewheel scrolling
def _on_mousewheel(event):
    controls_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

controls_canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Unbind the mousewheel when mouse leaves the canvas
def _unbound_mousewheel(event):
    controls_canvas.unbind_all("<MouseWheel>")

def _bound_mousewheel(event):
    controls_canvas.bind_all("<MouseWheel>", _on_mousewheel)

controls_canvas.bind("<Enter>", _bound_mousewheel)
controls_canvas.bind("<Leave>", _unbound_mousewheel)

# Set the canvas size to match available space
controls_canvas.config(width=580, height=710)  # Adjust these values as needed

orbit_paths_over_time = None  # Will be set by orbit_data_manager

# After creating the status_display widget, initialize the orbit_data_manager
status_display = tk.Label(root, text="Data Fetching Status", font=("Arial", 10), bg='SystemButtonFace', fg='black')
orbit_paths_over_time = orbit_data_manager.initialize(status_display)

# OR alternatively, update the original status_label's text and have the display just show it:
#def update_status(text):
#    status_display.config(text=text)
#    status_display.config(text=text)

# Set inner planets selected by default
sun_var = tk.IntVar(value=0)  
sun_shells_var = tk.IntVar(value=0)  
sun_core_var = tk.IntVar(value=0)
sun_radiative_var = tk.IntVar(value=0)
sun_photosphere_var = tk.IntVar(value=0)
sun_chromosphere_var = tk.IntVar(value=0)
sun_inner_corona_var = tk.IntVar(value=0)
sun_outer_corona_var = tk.IntVar(value=0)
sun_termination_shock_var = tk.IntVar(value=0)
sun_heliopause_var = tk.IntVar(value=0)

sun_inner_oort_limit_var = tk.IntVar(value=0)
sun_inner_oort_var = tk.IntVar(value=0)
sun_outer_oort_var = tk.IntVar(value=0)

sun_hills_cloud_torus_var = tk.IntVar(value=0)
sun_outer_oort_clumpy_var = tk.IntVar(value=0)
sun_galactic_tide_var = tk.IntVar(value=0)
sun_gravitational_var = tk.IntVar(value=0)

mercury_var = tk.IntVar(value=0) # default
# Mercury inner core shell
mercury_inner_core_var = tk.IntVar(value=0)
# mercury outer core shell
mercury_outer_core_var = tk.IntVar(value=0)
# mercury mantle shell
mercury_mantle_var = tk.IntVar(value=0) 
# mercury crust shell
mercury_crust_var = tk.IntVar(value=0)
# mercury atmosphere shell
mercury_atmosphere_var = tk.IntVar(value=0)
# mercury magnetosphere shell
mercury_magnetosphere_var = tk.IntVar(value=0)
# mercury hill sphere shell
mercury_hill_sphere_var = tk.IntVar(value=0)

venus_var = tk.IntVar(value=0) # default
# venus core shell
venus_core_var = tk.IntVar(value=0)
# venus mantle shell
venus_mantle_var = tk.IntVar(value=0)
# venus crust shell
venus_crust_var = tk.IntVar(value=0)
# venus atmosphere shell
venus_atmosphere_var = tk.IntVar(value=0)
# venus upper atmosphere shell
venus_upper_atmosphere_var = tk.IntVar(value=0)
# venus magnetosphere shell
venus_magnetosphere_var = tk.IntVar(value=0)
# venus hill sphere shell
venus_hill_sphere_var = tk.IntVar(value=0)

earth_var = tk.IntVar(value=0)   
# near Earth asteroids
pt5_var = tk.IntVar(value=0)
yr4_var = tk.IntVar(value=0)
asteroid_dw_var = tk.IntVar(value=0)
# Earth shells
# Earth inner core shell
earth_inner_core_var = tk.IntVar(value=0)
# Earth outer core shell
earth_outer_core_var = tk.IntVar(value=0)
# Earth lower mantle shell
earth_lower_mantle_var = tk.IntVar(value=0)
# Earth upper mantle shell
earth_upper_mantle_var= tk.IntVar(value=0) 
# Earth crust shell
earth_crust_var = tk.IntVar(value=0)
# Earth atmosphere shell
earth_atmosphere_var = tk.IntVar(value=0)
# Earth upper atmosphere shell
earth_upper_atmosphere_var = tk.IntVar(value=0)
# Earth magnetosphere shell
earth_magnetosphere_var = tk.IntVar(value=0)
# Earth hill sphere shell
earth_hill_sphere_var = tk.IntVar(value=0)

moon_var = tk.IntVar(value=0) 
# moon shells
# moon inner core shell
moon_inner_core_var = tk.IntVar(value=0)
# moon outer core shell
moon_outer_core_var = tk.IntVar(value=0)
# moon mantle shell
moon_mantle_var = tk.IntVar(value=0)
# moon crust shell
moon_crust_var = tk.IntVar(value=0)
# moon exosphere shell
moon_exosphere_var = tk.IntVar(value=0)
# moon hill sphere shell
moon_hill_sphere_var = tk.IntVar(value=0)

mars_var = tk.IntVar(value=0)  # Set Mars to 1 to preselect it by default
# Mars' Moons
phobos_var = tk.IntVar(value=0)
deimos_var = tk.IntVar(value=0)
# Mars shells
# Mars inner core shell
mars_inner_core_var = tk.IntVar(value=0)
# Mars outer core shell
mars_outer_core_var = tk.IntVar(value=0)
# Mars mantle shell
mars_mantle_var = tk.IntVar(value=0)
# Mars crust shell
mars_crust_var = tk.IntVar(value=0)
# Mars atmosphere shell
mars_atmosphere_var = tk.IntVar(value=0)
# Mars upper atmosphere shell
mars_upper_atmosphere_var = tk.IntVar(value=0)
# Mars magnetosphere shell
mars_magnetosphere_var = tk.IntVar(value=0)
# Mars hill sphere shell
mars_hill_sphere_var = tk.IntVar(value=0)

ceres_var = tk.IntVar(value=0)

jupiter_var = tk.IntVar(value=0)
# Jupiter's Galilean Moons
io_var = tk.IntVar(value=0)
europa_var = tk.IntVar(value=0)
ganymede_var = tk.IntVar(value=0)
callisto_var = tk.IntVar(value=0)
# Jupiter's ring Moons
metis_var = tk.IntVar(value=0)
adrastea_var = tk.IntVar(value=0)
amalthea_var = tk.IntVar(value=0)
thebe_var = tk.IntVar(value=0)
# Jupiter shells
# Jupiter core shell
jupiter_core_var = tk.IntVar(value=0)
# Jupiter metallic hydrogen shell
jupiter_metallic_hydrogen_var = tk.IntVar(value=0)
# Jupiter molecular hydrogen shell
jupiter_molecular_hydrogen_var = tk.IntVar(value=0)
# Jupiter cloud layer shell
jupiter_cloud_layer_var = tk.IntVar(value=0)
# Jupiter upper atmosphere shell
jupiter_upper_atmosphere_var = tk.IntVar(value=0)
# Jupiter ring system shell
jupiter_ring_system_var = tk.IntVar(value=0)
# Jupiter magnetosphere shell
jupiter_magnetosphere_var = tk.IntVar(value=0)
# Jupiter Io torus shell
jupiter_io_plasma_torus_var = tk.IntVar(value=0)
# Jupiter Hill Sphere shell
jupiter_radiation_belts_var = tk.IntVar(value=0)
# Jupiter hill_sphere shell
jupiter_hill_sphere_var = tk.IntVar(value=0)

saturn_var = tk.IntVar(value=0)
# Saturn's Major and Ring Moons
pan_var = tk.IntVar(value=0)
daphnis_var = tk.IntVar(value=0)
prometheus_var = tk.IntVar(value=0)
pandora_var = tk.IntVar(value=0)
mimas_var = tk.IntVar(value=0)
enceladus_var = tk.IntVar(value=0)
tethys_var = tk.IntVar(value=0)
dione_var = tk.IntVar(value=0)
rhea_var = tk.IntVar(value=0)
titan_var = tk.IntVar(value=0)
hyperion_var = tk.IntVar(value=0)
iapetus_var = tk.IntVar(value=0)
phoebe_var = tk.IntVar(value=0)
# saturn core shell
saturn_core_var = tk.IntVar(value=0)
# saturn metallic hydrogen shell
saturn_metallic_hydrogen_var = tk.IntVar(value=0)
# saturn molecular hydrogen shell
saturn_molecular_hydrogen_var = tk.IntVar(value=0)
# saturn cloud layer shell
saturn_cloud_layer_var = tk.IntVar(value=0)
# saturn upper atmosphere shell
saturn_upper_atmosphere_var = tk.IntVar(value=0)
# saturn ring system shell
saturn_ring_system_var = tk.IntVar(value=0)
# saturn magnetosphere shell
saturn_magnetosphere_var = tk.IntVar(value=0)
# saturn Enceladus torus shell
saturn_enceladus_plasma_torus_var = tk.IntVar(value=0)
# saturn Hill Sphere shell
saturn_radiation_belts_var = tk.IntVar(value=0)
# saturn hill_sphere shell
saturn_hill_sphere_var = tk.IntVar(value=0)

uranus_var = tk.IntVar(value=0)
# Uranus's Major Moons
ariel_var = tk.IntVar(value=0)
umbriel_var = tk.IntVar(value=0)
titania_var = tk.IntVar(value=0)
oberon_var = tk.IntVar(value=0)
miranda_var = tk.IntVar(value=0)
portia_var = tk.IntVar(value=0)
mab_var = tk.IntVar(value=0)
# uranus core shell
uranus_core_var = tk.IntVar(value=0)
# uranus mantle shell
uranus_mantle_var = tk.IntVar(value=0)
# uranus cloud layer shell
uranus_cloud_layer_var = tk.IntVar(value=0)
# uranus upper atmosphere shell
uranus_upper_atmosphere_var = tk.IntVar(value=0)
# uranus ring system shell
uranus_ring_system_var = tk.IntVar(value=0)
# uranus magnetosphere shell
uranus_magnetosphere_var = tk.IntVar(value=0)
# uranus radiation shell
uranus_radiation_belts_var = tk.IntVar(value=0)
# uranus hill_sphere shell
uranus_hill_sphere_var = tk.IntVar(value=0)

neptune_var = tk.IntVar(value=0)
# neptune's Major Moons
triton_var = tk.IntVar(value=0)
despina_var = tk.IntVar(value=0)
galatea_var = tk.IntVar(value=0)
# neptune core shell
neptune_core_var = tk.IntVar(value=0)
# neptune mantle shell
neptune_mantle_var = tk.IntVar(value=0)
# neptune cloud layer shell
neptune_cloud_layer_var = tk.IntVar(value=0)
# neptune upper atmosphere shell
neptune_upper_atmosphere_var = tk.IntVar(value=0)
# neptune ring system shell
neptune_ring_system_var = tk.IntVar(value=0)
# neptune magnetosphere shell
neptune_magnetosphere_var = tk.IntVar(value=0)
# neptune radiation shell
neptune_radiation_belts_var = tk.IntVar(value=0)
# neptune hill_sphere shell
neptune_hill_sphere_var = tk.IntVar(value=0)

pluto_var = tk.IntVar(value=0)
# pluto's Major Moons
charon_var = tk.IntVar(value=0)
styx_var = tk.IntVar(value=0)
nix_var = tk.IntVar(value=0)
kerberos_var = tk.IntVar(value=0)
hydra_var = tk.IntVar(value=0)  
# pluto core shell
pluto_core_var = tk.IntVar(value=0)
# pluto mantle shell
pluto_mantle_var = tk.IntVar(value=0)
# pluto cloud layer shell
pluto_crust_var = tk.IntVar(value=0)
# pluto haze layer shell
pluto_haze_layer_var = tk.IntVar(value=0)
# pluto upper atmosphere shell
pluto_atmosphere_var = tk.IntVar(value=0)
# pluto hill_sphere shell
pluto_hill_sphere_var = tk.IntVar(value=0)

planet9_var = tk.IntVar(value=0)  # hypothetical
# planet9 surface shell
planet9_surface_var = tk.IntVar(value=0)
# planet9 hill_sphere shell
planet9_hill_sphere_var = tk.IntVar(value=0)

haumea_var = tk.IntVar(value=0)

makemake_var = tk.IntVar(value=0)

eris_var = tk.IntVar(value=0)       # for heliocentric plots
eris2_var = tk.IntVar(value=0)      # for Eris-centered plots
# Eris's Moon
dysnomia_var = tk.IntVar(value=0)
# eris core shell
eris_core_var = tk.IntVar(value=0)
# eris mantle shell
eris_mantle_var = tk.IntVar(value=0)
# eris cloud layer shell
eris_crust_var = tk.IntVar(value=0)
# eris upper atmosphere shell
eris_atmosphere_var = tk.IntVar(value=0)
# eris hill_sphere shell
eris_hill_sphere_var = tk.IntVar(value=0)

voyager1_var = tk.IntVar(value=0)
voyager1h_var = tk.IntVar(value=0)

voyager2_var = tk.IntVar(value=0)

cassini_var = tk.IntVar(value=0)

new_horizons_var = tk.IntVar(value=0)

juno_var = tk.IntVar(value=0)

galileo_var = tk.IntVar(value=0)

apollo11sivb_var = tk.IntVar(value=0)

pioneer10_var = tk.IntVar(value=0)

pioneer11_var = tk.IntVar(value=0)

europa_clipper_var = tk.IntVar(value=0)

osiris_rex_var = tk.IntVar(value=0)
osiris_apex_var = tk.IntVar(value=0)

parker_solar_probe_var = tk.IntVar(value=0)

jwst_var = tk.IntVar(value=0)

rosetta_var = tk.IntVar(value=0)

bepicolombo_var = tk.IntVar(value=0)

solarorbiter_var = tk.IntVar(value=0)

akatsuki_var = tk.IntVar(value=0)

comet_ikeya_seki_var = tk.IntVar(value=0)

comet_west_var = tk.IntVar(value=0)

comet_halley_var = tk.IntVar(value=0)

comet_hyakutake_var = tk.IntVar(value=0)

comet_hale_bopp_var = tk.IntVar(value=0)

comet_mcnaught_var = tk.IntVar(value=0)

comet_neowise_var = tk.IntVar(value=0)

comet_tsuchinshan_atlas_var = tk.IntVar(value=0)

comet_Churyumov_Gerasimenko_var = tk.IntVar(value=0)

comet_borisov_var = tk.IntVar(value=0)

comet_atlas_var = tk.IntVar(value=0)

oumuamua_var = tk.IntVar(value=0)

apophis_var = tk.IntVar(value=0)

vesta_var = tk.IntVar(value=0)

bennu_var = tk.IntVar(value=0)  
bennu2_var = tk.IntVar(value=0)  # Bennu as a center body

steins_var = tk.IntVar(value=0)

donaldjohanson_var = tk.IntVar(value=0)

orus_var = tk.IntVar(value=0)

polymele_var = tk.IntVar(value=0)

eurybates_var = tk.IntVar(value=0)

patroclus_var = tk.IntVar(value=0)

leucus_var = tk.IntVar(value=0)

lutetia_var = tk.IntVar(value=0) 

soho_var = tk.IntVar(value=0)

ryugu_var = tk.IntVar(value=0)

eros_var = tk.IntVar(value=0)

dinkinesh_var = tk.IntVar(value=0)

itokawa_var = tk.IntVar(value=0)

change_var = tk.IntVar(value=0)

perse_var = tk.IntVar(value=0)

dart_var = tk.IntVar(value=0)

lucy_var = tk.IntVar(value=0)

kbo_var = tk.IntVar(value=0)

gaia_var = tk.IntVar(value=0)

hayabusa2_var = tk.IntVar(value=0)  # 0 means unselected by default

# Define IntVar variables for Kuiper Belt Objects
quaoar_var = tk.IntVar(value=0)

sedna_var = tk.IntVar(value=0)

of201_var = tk.IntVar(value=0)

orcus_var = tk.IntVar(value=0)    # 0 means unselected by default

varuna_var = tk.IntVar(value=0)

gv9_var = tk.IntVar(value=0)

ms4_var = tk.IntVar(value=0)

dw_var = tk.IntVar(value=0)

gonggong_var = tk.IntVar(value=0)

arrokoth_var = tk.IntVar(value=0)
arrokoth_new_horizons_var = tk.IntVar(value=0)

ixion_var = tk.IntVar(value=0)

# Create a mapping dictionary for Sun shell variables:

sun_shell_vars = {
    'gravitational': sun_gravitational_var,
    'outer_oort_clumpy': sun_outer_oort_clumpy_var,         # New
    'hills_cloud_torus': sun_hills_cloud_torus_var,        # New
    'galactic_tide': sun_galactic_tide_var,                 # New

    'outer_oort': sun_outer_oort_var,
    'inner_oort': sun_inner_oort_var,
    'inner_oort_limit': sun_inner_oort_limit_var,

    'heliopause': sun_heliopause_var,
    'termination_shock': sun_termination_shock_var,
    'outer_corona': sun_outer_corona_var,
    'inner_corona': sun_inner_corona_var,
    'chromosphere': sun_chromosphere_var,
    'photosphere': sun_photosphere_var,
    'radiative': sun_radiative_var,
    'core': sun_core_var
}

# Create mapping dictionaries for planet shell variables:

mercury_shell_vars = {
    'mercury_inner_core': mercury_inner_core_var,
    'mercury_outer_core': mercury_outer_core_var,
    'mercury_mantle': mercury_mantle_var,
    'mercury_crust': mercury_crust_var,
    'mercury_atmosphere': mercury_atmosphere_var,
    'mercury_magnetosphere': mercury_magnetosphere_var,
    'mercury_hill_sphere': mercury_hill_sphere_var
}

venus_shell_vars = {
    'venus_core': venus_core_var,
    'venus_mantle': venus_mantle_var,
    'venus_crust': venus_crust_var,
    'venus_atmosphere': venus_atmosphere_var,
    'venus_upper_atmosphere': venus_upper_atmosphere_var,
    'venus_magnetosphere': venus_magnetosphere_var,
    'venus_hill_sphere': venus_hill_sphere_var
}

earth_shell_vars = {
    'earth_inner_core': earth_inner_core_var,
    'earth_outer_core': earth_outer_core_var,
    'earth_lower_mantle': earth_lower_mantle_var,
    'earth_upper_mantle': earth_upper_mantle_var,
    'earth_crust': earth_crust_var,
    'earth_atmosphere': earth_atmosphere_var,
    'earth_upper_atmosphere': earth_upper_atmosphere_var,
    'earth_magnetosphere': earth_magnetosphere_var,
    'earth_hill_sphere': earth_hill_sphere_var
}

moon_shell_vars = {
    'moon_inner_core': moon_inner_core_var,
    'moon_outer_core': moon_outer_core_var,
    'moon_mantle': moon_mantle_var,
    'moon_crust': moon_crust_var,
    'moon_exosphere': moon_exosphere_var,
    'moon_hill_sphere': moon_hill_sphere_var
}

mars_shell_vars = {
    'mars_inner_core': mars_inner_core_var,
    'mars_outer_core': mars_outer_core_var,
    'mars_mantle': mars_mantle_var,
    'mars_crust': mars_crust_var,
    'mars_atmosphere': mars_atmosphere_var,
    'mars_upper_atmosphere': mars_upper_atmosphere_var,
    'mars_magnetosphere': mars_magnetosphere_var,
    'mars_hill_sphere': mars_hill_sphere_var
}

jupiter_shell_vars = {
    'jupiter_core': jupiter_core_var,
    'jupiter_metallic_hydrogen': jupiter_metallic_hydrogen_var,
    'jupiter_molecular_hydrogen': jupiter_molecular_hydrogen_var,
    'jupiter_cloud_layer': jupiter_cloud_layer_var,
    'jupiter_upper_atmosphere': jupiter_upper_atmosphere_var,
    'jupiter_ring_system': jupiter_ring_system_var,
    'jupiter_radiation_belts': jupiter_radiation_belts_var,
    'jupiter_io_plasma_torus': jupiter_io_plasma_torus_var,
    'jupiter_magnetosphere': jupiter_magnetosphere_var,
    'jupiter_hill_sphere': jupiter_hill_sphere_var
}

saturn_shell_vars = {
    'saturn_core': saturn_core_var,
    'saturn_metallic_hydrogen': saturn_metallic_hydrogen_var,
    'saturn_molecular_hydrogen': saturn_molecular_hydrogen_var,
    'saturn_cloud_layer': saturn_cloud_layer_var,
    'saturn_upper_atmosphere': saturn_upper_atmosphere_var,
    'saturn_ring_system': saturn_ring_system_var,
    'saturn_radiation_belts': saturn_radiation_belts_var,
    'saturn_enceladus_plasma_torus': saturn_enceladus_plasma_torus_var,
    'saturn_magnetosphere': saturn_magnetosphere_var,
    'saturn_hill_sphere': saturn_hill_sphere_var
}

uranus_shell_vars = {
    'uranus_core': uranus_core_var,
    'uranus_mantle': uranus_mantle_var,
    'uranus_cloud_layer': uranus_cloud_layer_var,
    'uranus_upper_atmosphere': uranus_upper_atmosphere_var,
    'uranus_ring_system': uranus_ring_system_var,
    'uranus_radiation_belts': uranus_radiation_belts_var,
    'uranus_magnetosphere': uranus_magnetosphere_var,
    'uranus_hill_sphere': uranus_hill_sphere_var
}

neptune_shell_vars = {
    'neptune_core': neptune_core_var,
    'neptune_mantle': neptune_mantle_var,
    'neptune_cloud_layer': neptune_cloud_layer_var,
    'neptune_upper_atmosphere': neptune_upper_atmosphere_var,
    'neptune_ring_system': neptune_ring_system_var,
    'neptune_radiation_belts': neptune_radiation_belts_var,
    'neptune_magnetosphere': neptune_magnetosphere_var,
    'neptune_hill_sphere': neptune_hill_sphere_var
}

pluto_shell_vars = {
    'pluto_core': pluto_core_var,
    'pluto_mantle': pluto_mantle_var,
    'pluto_crust': pluto_crust_var,
    'pluto_haze_layer': pluto_haze_layer_var,
    'pluto_atmosphere': pluto_atmosphere_var,
    'pluto_hill_sphere': pluto_hill_sphere_var
}

eris_shell_vars = {
    'eris_core': eris_core_var,
    'eris_mantle': eris_mantle_var,
    'eris_crust': eris_crust_var,
    'eris_atmosphere': eris_atmosphere_var,
    'eris_hill_sphere': eris_hill_sphere_var
}

planet9_shell_vars = {
    'planet9_surface': planet9_surface_var,    
    'planet9_hill_sphere': planet9_hill_sphere_var
}

# Define the list of objects
objects = [
    # Existing Celestial Objects
    {'name': 'Sun', 'id': '10', 'var': sun_var, 'color': color_map('Sun'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "The Sun\'s gravity holds the solar system together, keeping everything in its orbit. "', 
    'mission_url': 'https://science.nasa.gov/sun/'},

    {'name': 'Mercury', 'id': '199', 'var': mercury_var, 'color': color_map('Mercury'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Mercury is the smallest planet in our solar system and the nearest to the Sun."', 
    'mission_url': 'https://science.nasa.gov/mercury/'},

    {'name': 'Venus', 'id': '299', 'var': venus_var, 'color': color_map('Venus'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Venus is the second planet from the Sun, and the sixth largest planet. It\'s the hottest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/venus/'},

    {'name': 'Earth', 'id': '399', 'var': earth_var, 'color': color_map('Earth'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'Earth orbital period: 27.32 days.', 
     'mission_url': 'https://science.nasa.gov/earth/', 'mission_info': 'Our home planet.'},

    {'name': 'Moon', 'id': '301', 'var': moon_var, 'color': color_map('Moon'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Earth orbital period: 27.32 days.', 
     'mission_url': 'https://science.nasa.gov/moon/', 'mission_info': 'NASA: "The Moon rotates exactly once each time it orbits our planet."'},

    {'name': 'Mars', 'id': '499', 'var': mars_var, 'color': color_map('Mars'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Mars is one of the easiest planets to spot in the night sky — it looks like a bright red point of light."', 
    'mission_url': 'https://science.nasa.gov/?search=mars'},

    {'name': 'Jupiter', 'id': '599', 'var': jupiter_var, 'color': color_map('Jupiter'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Jupiter is the largest and oldest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/?search=Jupiter'},

    {'name': 'Saturn', 'id': '699', 'var': saturn_var, 'color': color_map('Saturn'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Saturn is the sixth planet from the Sun and the second largest planet in our solar system."', 
    'mission_url': 'https://science.nasa.gov/saturn/'},

    {'name': 'Uranus', 'id': '799', 'var': uranus_var, 'color': color_map('Uranus'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system -- about four times wider than Earth."', 
    'mission_url': 'https://science.nasa.gov/uranus/'},

    {'name': 'Neptune', 'id': '899', 'var': neptune_var, 'color': color_map('Neptune'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Dark, cold and whipped by supersonic winds, giant Neptune is the eighth and most distant major planet orbiting our Sun."', 
    'mission_url': 'https://science.nasa.gov/neptune/'},

    {'name': 'Planet 9', 'id': 'planet9_placeholder', 'var': planet9_var, 'color': color_map('Planet 9'), 
    'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'Hypothetical planet with estimated mass of 5-10 Earths at ~400-800 AU. Not yet directly observed. Visualization is our estimate and not from JPL Horizons.',
    'mission_url': 'https://en.wikipedia.org/wiki/Planet_Nine'},

# Dwarf planets

    {'name': 'Pluto', 'id': '999', 'var': pluto_var, 'color': color_map('Pluto'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': None, 
    'mission_info': 'NASA: "Pluto is a dwarf planet located in a distant region of our solar system beyond Neptune known as the Kuiper Belt."', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/'},

    {'name': 'Ceres', 'id': 'ceres', 'var': ceres_var, 'color': color_map('Ceres'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'NASA: "Ceres was the first object discovered in the main asteroid belt and is named for the Roman goddess of agriculture."', 
    'mission_url': 'https://science.nasa.gov/mission/dawn/science/ceres/'},

    {'name': 'Haumea', 'id': '136108', 'var': haumea_var, 'color': color_map('Haumea'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'Haumea is an oval-shaped dwarf planet that is one of the fastest rotating large objects in our solar system.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/haumea/'},

    {'name': 'Eris', 'id': '136199', 'var': eris_var, 'color': color_map('Eris'), 'symbol': 'circle', 'is_mission': False, 
    # 136199 primary (required for Sun centered plots)
    'id_type': 'smallbody', 
    'mission_info': 'Eris is a dwarf planet about the same size as Pluto, but it\'s three times farther from the Sun.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/eris/'},

    {'name': 'Eris/Dysnomia', 'id': '20136199', 'var': eris2_var, 'color': color_map('Eris'), 'symbol': 'circle', 'is_mission': False, 
    # 20136199 satellite solution (required for Eris centered plots) 
    'id_type': 'smallbody', 
    'mission_info': 'Eris is a dwarf planet about the same size as Pluto, but it\'s three times farther from the Sun.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/eris/'},

    {'name': 'Gonggong', 'id': '2007 OR10', 'var': gonggong_var, 'color': color_map('Gonggong'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'Dwarf planet in the Kuiper Belt with a highly inclined orbit.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Gonggong_(dwarf_planet)'},

    {'name': 'Makemake', 'id': '136472', 'var': makemake_var, 'color': color_map('Makemake'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'Makemake is a dwarf planet slightly smaller than Pluto, and is the second-brightest object in the Kuiper Belt.', 
    'mission_url': 'https://science.nasa.gov/dwarf-planets/makemake/'},

    {'name': 'MS4', 'id': '2002 MS4', 'var': ms4_var, 'color': color_map('MS4'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'One of the largest unnumbered Kuiper Belt Objects with no known moons.', 
    'mission_url': 'https://www.minorplanetcenter.net/db_search/show_object?object_id=2002+MS4'},

    {'name': 'Orcus', 'id': '90482', 'var': orcus_var, 'color': color_map('Orcus'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A dwarf planet in the Kuiper Belt with a moon named Vanth.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Orcus_(dwarf_planet)'},

    {'name': 'Quaoar', 'id': '50000', 'var': quaoar_var, 'color': color_map('Quaoar'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A large Kuiper Belt object with a ring system.', 
    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/quaoar/in-depth/'},

    {'name': 'Sedna', 'id': '90377', 'var': sedna_var, 'color': color_map('Sedna'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A distant trans-Neptunian dwarf planet with an extremely long orbit.', 
    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/sedna/in-depth/'},

    {'name': '2017 OF201', 'id': '2017 OF201', 'var': of201_var, 'color': color_map('2017 OF201'), 'symbol': 'circle', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A extreme trans-Neptunian object with an extremely long orbit.', 
    'mission_url': 'https://en.wikipedia.org/wiki/2017_OF201#:~:text=2017%20OF201%20is%20an,have%20a%20directly%20estimated%20size.'},

    # Asteroids
    {'name': '2024 PT5', 'id': '2024 PT5', 'var': pt5_var, 'color': color_map('2024 PT5'), 'symbol': 'circle-open', 'is_mission': False,
    'is_comet': False, 'id_type': 'smallbody', 'start_date': datetime(2024, 8, 2), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Closest approach to Earth 8-9-2024.',
    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20PT5'},

    {'name': '2024 YR4', 'id': '2024 YR4', 'var': yr4_var, 'color': color_map('2024 YR4'), 'symbol': 'circle-open', 'is_mission': False,
    'is_comet': False, 'id_type': 'smallbody', 'start_date': datetime(2024, 12, 24), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Closest approach to Earth 12-25-2024 4:46 UTC.',
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/2024-yr4/'},

    {'name': '2024 DW', 'id': '2024 DW', 'var': asteroid_dw_var, 'color': color_map('2024 DW'), 'symbol': 'circle-open', 'is_mission': False,
    'is_comet': False, 'id_type': 'smallbody', 'start_date': datetime(2024, 2, 19), 'end_date': datetime(2032, 12, 31), 
    'mission_info': 'Closest approach to Earth 2-22-2024 approximately 5 UTC.',
    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20DW'},

    {'name': 'Apophis', 'id': '99942', 'var': apophis_var, 'color': color_map('Apophis'), 'symbol': 'circle-open', 'is_mission': False,
    'is_comet': False, 'id_type': 'smallbody', 'start_date': datetime(2004, 6, 20), 'end_date': datetime(2036, 1, 1), 
    'mission_info': 'A near-Earth asteroid that will make a close approach in 2029.', 
    'mission_url': 'https://cneos.jpl.nasa.gov/apophis/'},

    {'name': 'Bennu', 'id': '101955', 'var': bennu_var, 'color': color_map('Bennu'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Studied by NASA\'s OSIRIS-REx mission.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/101955-bennu/'},

    {'name': 'Bennu/OSIRIS', 'id': '2101955', 'var': bennu2_var, 'color': color_map('Bennu'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', # Bennu as a center object
    'mission_info': 'Studied by NASA\'s OSIRIS-REx mission.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/101955-bennu/'},

    {'name': 'Eros', 'id': '433', 'var': eros_var, 'color': color_map('Eros'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'First asteroid to be orbited and landed on by NASA\'s NEAR Shoemaker spacecraft in 2000-2001.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/433-eros/'},

    {'name': 'Dinkinesh', 'id': '152830', 'var': dinkinesh_var, 'color': color_map('Dinkinesh'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Dinkinesh was visited by the mission Lucy.', 
    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/dinkinesh/'},

    {'name': 'Itokawa', 'id': '25143', 'var': itokawa_var, 'color': color_map('Itokawa'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'First asteroid from which samples were returned to Earth by JAXA\'s Hayabusa mission in 2010.', 
    'mission_url': 'https://en.wikipedia.org/wiki/25143_Itokawa'},

    {'name': 'Lutetia', 'id': '21', 'var': lutetia_var, 'color': color_map('Lutetia'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Studied by European Space Agency\'s Rosetta mission.', 
    'mission_url': 'https://www.nasa.gov/image-article/asteroid-lutetia/'},

    {'name': 'Ryugu', 'id': '162173', 'var': ryugu_var, 'color': color_map('Ryugu'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Target of JAXA\'s Hayabusa2 mission which returned samples to Earth in 2020.', 
    'mission_url': 'https://en.wikipedia.org/wiki/162173_Ryugu'},

    {'name': 'Šteins', 'id': '2867', 'var': steins_var, 'color': color_map('Šteins'), 'symbol': 'circle-open', 'is_mission': False, 
     'is_comet': False, 'id_type': 'smallbody',
     'mission_info': 'Visited by European Space Agency\'s Rosetta spacecraft.', 
     'mission_url': 'https://www.esa.int/Science_Exploration/Space_Science/Rosetta'},

    {'name': 'Donaldjohanson', 'id': '52246', 'var': donaldjohanson_var, 'color': color_map('Donaldjohanson'), 'symbol': 'circle-open', 'is_mission': False, 
     'is_comet': False, 'id_type': 'smallbody',
     'mission_info': 'Visited by the NASA Lucy spacecraft.', 
     'mission_url': 'https://science.nasa.gov/solar-system/asteroids/donaldjohanson/'},

    {'name': 'Vesta', 'id': '4', 'var': vesta_var, 'color': color_map('Vesta'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'One of the largest objects in the asteroid belt, visited by NASA\'s Dawn mission.', 
    'mission_url': 'https://dawn.jpl.nasa.gov/'},

    {'name': 'Eurybates', 'id': '3548', 'var': eurybates_var, 'color': color_map('Eurybates'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Trojan asteroid that will be visited by the NASA Lucy spacecraft.', 
    'mission_url': 'https://www.nasa.gov/missions/hide-and-seek-how-nasas-lucy-mission-team-discovered-eurybates-satellite/'},

    {'name': 'Patroclus', 'id': '617', 'var': patroclus_var, 'color': color_map('Patroclus'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Trojan asteroid that will be visited by the NASA Lucy spacecraft.', 
    'mission_url': 'https://lucy.swri.edu/Patroclus.html'},

    {'name': 'Polymele', 'id': '15094', 'var': polymele_var, 'color': color_map('Polymele'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Trojan asteroid that will be visited by the NASA Lucy spacecraft.', 
    'mission_url': 'https://lucy.swri.edu/Polymele.html'},

    {'name': 'Leucus', 'id': '11351', 'var': leucus_var, 'color': color_map('Leucus'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Trojan asteroid that will be visited by the NASA Lucy spacecraft.', 
    'mission_url': 'https://lucy.swri.edu/Leucus.html'},

    {'name': 'Orus', 'id': '21900', 'var': orus_var, 'color': color_map('Orus'), 'symbol': 'circle-open', 'is_mission': False, 
    'is_comet': False, 'id_type': 'smallbody', 
    'mission_info': 'Trojan asteroid that will be visited by the NASA Lucy spacecraft.', 
    'mission_url': 'https://lucy.swri.edu/Orus.html'},

    # Kuiper Belt Objects

    {'name': 'Arrokoth', 'id': '486958', 'var': arrokoth_var, 'color': color_map('Arrokoth'), 'symbol': 'circle-open', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'Arrokoth (2014 MU69) flyby from New Horizons on January 1, 2019.', 
    'mission_url': 'https://science.nasa.gov/resource/arrokoth-2014-mu69-in-3d/'},

    {'name': 'Arrokoth/New_Horizons', 'id': '2486958', 'var': arrokoth_new_horizons_var, 'color': color_map('Arrokoth'), 'symbol': 'circle-open', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'Arrokoth (2014 MU69) flyby from New Horizons on January 1, 2019.', 
    'mission_url': 'https://science.nasa.gov/resource/arrokoth-2014-mu69-in-3d/'},

    {'name': 'Ixion', 'id': '2001 KX76', 'var': ixion_var, 'color': color_map('Ixion'), 'symbol': 'circle-open', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A large Kuiper Belt object without a known moon.', 
    'mission_url': 'https://en.wikipedia.org/wiki/28978_Ixion'},

    {'name': 'GV9', 'id': '2004 GV9', 'var': gv9_var, 'color': color_map('GV9'), 'symbol': 'circle-open', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A binary Kuiper Belt Object providing precise mass measurements through its moon.', 
    'mission_url': 'https://en.wikipedia.org/wiki/(90568)_2004_GV9'},

    {'name': 'Varuna', 'id': '20000', 'var': varuna_var, 'color': color_map('Varuna'), 'symbol': 'circle-open', 'is_mission': False, 
    'id_type': 'smallbody', 
    'mission_info': 'A significant Kuiper Belt Object with a rapid rotation period.', 
    'mission_url': 'https://en.wikipedia.org/wiki/20000_Varuna'},

    # Comets

    {'name': 'ATLAS', 'id': 'DES=C/2024 G3', 'var': comet_atlas_var, 'color': color_map('ATLAS'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2024, 6, 18), 'end_date': datetime(2029, 12, 31), 
    'mission_info': 'Comet C/2024 G3 (ATLAS) is creating quite a buzz in the Southern Hemisphere!', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/'},

    {'name': 'Churyumov', 'id': '90000702', 'var': comet_Churyumov_Gerasimenko_var, 'color': color_map('Churyumov'), # 90000703
    'symbol': 'diamond', 'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1962, 1, 21), 'end_date': datetime(2029, 12, 31), 
    # datetime(1962, 1, 20), 'end_date': datetime(2030, 12, 31) replacing datetime (2002, 11, 22), 'end_date': datetime(2021, 5, 1)
    'mission_info': '67P/Churyumov-Gerasimenko is the comet visited by the Rosetta spacecraft.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/67p-churyumov-gerasimenko/'},

    {'name': 'Hale-Bopp', 'id': 'C/1995 O1', 'var': comet_hale_bopp_var, 'color': color_map('Hale-Bopp'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1995, 7, 24), 'end_date': datetime(2001, 12, 31), 
    'mission_info': 'Visible to the naked eye for a record 18 months.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/c-1995-o1-hale-bopp/'},

    {'name': 'Halley', 'id': '90000030', 'var': comet_halley_var, 'color': color_map('Halley'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1962, 1, 22), 'end_date': datetime(2061, 7, 28), 
    # initial start date 1982-11-26. Horizons has 1962-01-20
    'mission_info': 'Most famous comet, returned in 1986 and will return in 2061.', 
    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/halley-1986'},

    {'name': 'Hyakutake', 'id': 'C/1996 B2', 'var': comet_hyakutake_var, 'color': color_map('Hyakutake'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1995, 12, 2), 'end_date': datetime(1996, 6, 1), 
    'mission_info': 'Passed very close to Earth in 1996.', 
    'mission_url': 'https://science.nasa.gov/mission/ulysses/'},

    {'name': 'Ikeya-Seki', 'id': 'C/1965 S1-A', 'var': comet_ikeya_seki_var, 'color': color_map('Ikeya-Seki'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1965, 9, 22), 'end_date': datetime(1966, 1, 14), 
    'mission_info': 'One of the brightest comets of the 20th century.', 
    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/ikeya-seki-1965'},

    {'name': 'McNaught', 'id': 'C/2006 P1', 'var': comet_mcnaught_var, 'color': color_map('McNaught'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2006, 8, 8), 'end_date': datetime(2008, 6, 1), 
    'mission_info': 'Known as the Great Comet of 2007.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/'}, 

    {'name': 'NEOWISE', 'id': 'C/2020 F3', 'var': comet_neowise_var, 'color': color_map('NEOWISE'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2020, 3, 28), 'end_date': datetime(2021, 6, 1), 
    'mission_info': 'Brightest comet visible from the Northern Hemisphere in decades.', 
    'mission_url': 'https://www.nasa.gov/missions/neowise/nasas-neowise-celebrates-10-years-plans-end-of-mission/'},

    {'name': 'Tsuchinshan', 'id': 'C/2023 A3', 'var': comet_tsuchinshan_atlas_var, 'color': color_map('Tsuchinsh'), 
    'symbol': 'diamond', 'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2023, 1, 10), 
    'end_date': datetime(2030, 12, 31), 
    'mission_info': 'Tsuchinshan-ATLAS is a new comet discovered in 2023, expected to become bright in 2024.', 
    'mission_url': 'https://en.wikipedia.org/wiki/C/2023_A3_(Tsuchinshan-ATLAS)'},

    {'name': 'West', 'id': 'C/1975 V1', 'var': comet_west_var, 'color': color_map('Comet West'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(1975, 11, 6), 'end_date': datetime(1976, 6, 1), 
    'mission_info': 'Notable for its bright and impressive tail.', 
    'mission_url': 'https://en.wikipedia.org/wiki/Comet_West'},

    {'name': 'Borisov', 'id': 'C/2019 Q4', 'var': comet_borisov_var, 'color': color_map('Borisov'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2019, 8, 31), 'end_date': datetime(2020, 10, 1), 
    'mission_info': 'The second interstellar object detected, after \'Oumuamua.', 
    'mission_url': 'https://science.nasa.gov/solar-system/comets/2i-borisov/'},

    {'name': 'Oumuamua', 'id': 'A/2017 U1', 'var': oumuamua_var, 'color': color_map('Oumuamua'), 'symbol': 'diamond', 
    'is_comet': True, 'id_type': 'smallbody', 'start_date': datetime(2017, 10, 15), 'end_date': datetime(2018, 1, 1), 
    'mission_info': 'First known interstellar object detected passing through the Solar System.', 
    'mission_url': 'https://www.jpl.nasa.gov/news/solar-systems-first-interstellar-visitor-dazzles-scientists/'},

    # NASA Missions -- start date moved up by one day to avoid fetching errors, and default end date is 2025-01-01

    # Apollo 11 S-IVB (Spacecraft) -399110 Time Specification: Start=1969-07-16:40 UT , Stop=1969-07-28 00:06, Step=1 (hours) Revised: Mar 22, 2016  
    {'name': 'Apollo 11 S-IVB', 'id': '-399110', 'var': apollo11sivb_var, 'color': color_map('Apollo 11 S-IVB'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(1969, 7, 16, 17), 'end_date': datetime(1969, 7, 28, 0, 0), # splashdown 07-24 16:50
    'mission_url': 'https://www.nasa.gov/mission/apollo-11/', 
    'mission_info': 'This is the last and most powerful stage of the Saturn V rocket that propelled the Apollo 11 mission towards the Moon.'},

    {'name': 'Pioneer10', 'id': '-23', 'var': pioneer10_var, 'color': color_map('Pioneer10'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(1972, 3, 4), 'end_date': datetime(2003, 1, 23, 8, 0), 
    'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 
    'mission_info': 'First spacecraft to travel through the asteroid belt and make direct observations of Jupiter.'},

    {'name': 'Pioneer11', 'id': '-24', 'var': pioneer11_var, 'color': color_map('Pioneer11'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(1973, 4, 7), 'end_date': datetime(1995, 9, 30, 11, 0), 
    'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 
    'mission_info': 'First spacecraft to encounter Saturn and study its rings.'},

    {'name': 'Voyager 1', 'id': '-31', 'var': voyager1_var, 'color': color_map('Voyager 1'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(1977, 9, 6), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 
    'mission_info': 'Launched in 1977, Voyager 1 is the farthest spacecraft from Earth.'},

    {'name': 'Voyager 2', 'id': '-32', 'var': voyager2_var, 'color': color_map('Voyager 2'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(1977, 8, 21), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 
    'mission_info': 'Launched in 1977, Voyager 2 explored all four giant planets.'},

    {'name': 'Galileo', 'id': '-77', 'var': galileo_var, 'color': color_map('Galileo'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(1989, 10, 19), 'end_date': datetime(2003, 9, 30), # no ephemeris after this date
    'mission_url': 'https://solarsystem.nasa.gov/missions/galileo/overview/', 
    'mission_info': 'Galileo studied Jupiter and its moons from 1995 to 2003.'},

    {'name': 'SOHO', 'id': '488', 'var': soho_var, 'color': color_map('SOHO'), 
    'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id', 'start_date': datetime(1995, 12, 3), 'end_date': datetime(2029, 12, 31), 
    'mission_info': 'The Solar and Heliospheric Observatory observes the Sun and heliosphere from the L1 Lagrange point.', 
    'mission_url': 'https://sohowww.nascom.nasa.gov/'},    

    {'name': 'Cassini', 'id': '-82', 'var': cassini_var, 'color': color_map('Cassini-Huygens'), 'symbol': 'diamond-open', 
     'is_mission': True, 'id_type': 'id', 'start_date': datetime(1997, 10, 16), 'end_date': datetime(2017, 9, 15), 
     'mission_url': 'https://solarsystem.nasa.gov/missions/cassini/overview/', 
     'mission_info': 'Cassini-Huygens studied Saturn and its moons from 2004 to 2017.'},

    {'name': 'Rosetta', 'id': '-226', 'var': rosetta_var, 'color': color_map('Rosetta'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(2004, 3, 3), 'end_date': datetime(2016, 10, 5), 
    'mission_url': 'https://rosetta.esa.int/', 
    'mission_info': 'European Space Agency mission to study Comet 67P/Churyumov-Gerasimenko.'},

    {'name': 'New Horizons', 'id': '-98', 'var': new_horizons_var, 'color': color_map('Horizons'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2006, 1, 20), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://www.nasa.gov/mission_pages/newhorizons/main/index.html', 
    'mission_info': 'New Horizons flew past Pluto in 2015 and continues into the Kuiper Belt.'},

    {'name': 'Chang\'e', 'id': 'Chang\'e', 'var': change_var, 'color': color_map('Chang\'e'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2007, 10, 25), 'end_date': datetime(2029, 12, 31), 
    'mission_info': 'China\'s lunar exploration program.', 
    'mission_url': 'http://www.clep.org.cn/'},

    {'name': 'Akatsuki', 'id': 'Akatsuki', 'var': akatsuki_var, 'color': color_map('Akatsuki'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2010, 5, 21), 'end_date': datetime(2025, 3, 2), # end ephemeris
    'mission_info': 'JAXA mission to study the atmospheric circulation of Venus', 
    'mission_url': 'https://en.wikipedia.org/wiki/Akatsuki_(spacecraft)'},

    {'name': 'Juno', 'id': '-61', 'var': juno_var, 'color': color_map('Juno'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(2011, 8, 6), 'end_date': datetime(2025, 5, 10), 
    'mission_url': 'https://www.nasa.gov/mission_pages/juno/main/index.html', 
    'mission_info': 'Juno studies Jupiter\'s atmosphere and magnetosphere.'},

    {'name': 'Gaia', 'id': 'Gaia', 'var': gaia_var, 'color': color_map('Gaia'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(2013, 12, 20), 'end_date': datetime(2025, 7, 1),    # end ephemeris 
    'mission_info': 'European Space Agency mission at L2 mapping the Milky Way.', 
    'mission_url': 'https://www.cosmos.esa.int/web/gaia'},

    {'name': 'Hayabusa2', 'id': 'Hayabusa2', 'var': hayabusa2_var, 'color': color_map('Hayabusa2'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2014, 12, 4), 'end_date': datetime(2020, 12, 5), 
    'mission_info': 'JAXA mission that returned samples from Ryugu.', 
    'mission_url': 'https://hayabusa2.jaxa.jp/en/'},

    {'name': 'OSIRISREx', 'id': '-64', 'var': osiris_rex_var, 'color': color_map('OSIRIS'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2016, 9, 10), 'end_date': datetime(2023, 9, 24), 
    'mission_url': 'https://science.nasa.gov/mission/osiris-rex/', 
    'mission_info': 'OSIRIS-REx is NASA\'s mission to collect samples from asteroid Bennu.'},

    {'name': 'OSIRISAPE', 'id': '-64', 'var': osiris_apex_var, 'color': color_map('OSIRIS'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2023, 9, 24), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://science.nasa.gov/category/missions/osiris-apex/', 
    'mission_info': 'OSIRIS-APEX is NASA\'s mission to study asteroid Apophis.'},

    {'name': 'Parker', 'id': '-96', 'var': parker_solar_probe_var, 'color': color_map('Parker Solar Probe'), 
    'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id', 'start_date': datetime(2018, 8, 13), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://www.nasa.gov/content/goddard/parker-solar-probe', 
    'mission_info': 'The Parker Solar Probe mission is to study the outer corona of the Sun.'},

    {'name': 'MarsRover', 'id': '-168', 'var': perse_var, 'color': color_map('MarsRover'), 'symbol': 'diamond-open', # Perseverance
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2020, 7, 31), 'end_date': datetime(2026, 2, 19),    # end ephemeris
    'mission_info': 'The Perseverance Rover is NASA\'s Mars rover and Ingenuity helicopter. Note: The elevation values shown (-4200m) <br>' 
    'differ from published scientific values for Jezero Crater (-2600m) due to different Mars reference systems. JPL <br>' 
    'Horizons uses one elevation datum, while scientific publications often use the Mars Orbiter Laser Altimeter (MOLA) reference areoid. <br>' 
    'The rover is correctly positioned relative to Mars, but the absolute elevation value has a systematic offset of approximately 1600m.', 
    'mission_url': 'https://mars.nasa.gov/mars2020/'},

    {'name': 'Lucy', 'id': '-49', 'var': lucy_var, 'color': color_map('Lucy'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(2021, 10, 17), 'end_date': datetime(2033, 4, 1), 
    'mission_info': 'Exploring Trojan asteroids around Jupiter.', 
    'mission_url': 'https://www.nasa.gov/lucy'},

    {'name': 'DART', 'id': '-135', 'var': dart_var, 'color': color_map('DART'), 'symbol': 'diamond-open', 'is_mission': True, 
    'id_type': 'id', 'start_date': datetime(2021, 11, 25), 'end_date': datetime(2022, 9, 25), 
    'mission_info': 'NASA\'s mission to test asteroid deflection.', 
    'mission_url': 'https://www.nasa.gov/dart'},

    {'name': 'JamesWebb', 'id': '-170', 'var': jwst_var, 'color': color_map('JamesWebb'), 
    'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id', 'start_date': datetime(2021, 12, 26), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://science.nasa.gov/mission/webb/', 
    'mission_info': 'The James Webb Space Telescope is NASA\'s flagship infrared space telescope.'},

    {'name': 'Clipper', 'id': '-159', 'var': europa_clipper_var, 'color': color_map('Clipper'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2024, 10, 15), 'end_date': datetime(2030, 4, 1), 
    'mission_url': 'https://europa.nasa.gov/', 
    'mission_info': 'Europa Clipper will conduct detailed reconnaissance of Jupiter\'s moon Europa.'},

    {'name': 'Bepi', 'id': '-121', 'var': bepicolombo_var, 'color': color_map('Bepi'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2018, 10, 20), 'end_date': datetime(2029, 12, 31), 
    'mission_url': 'https://sci.esa.int/web/bepicolombo', 'mission_info': 'BepiColombo is the joint ESA/JAXA mission to study Mercury, arriving in 2025.'},

    {'name': 'SolO', 'id': '-144', 'var': solarorbiter_var, 'color': color_map('SolO'), 'symbol': 'diamond-open', 
    'is_mission': True, 'id_type': 'id', 'start_date': datetime(2020, 2, 11), 'end_date': datetime(2030, 11, 20), 
    'mission_url': 'https://en.wikipedia.org/wiki/Solar_Orbiter', 'mission_info': 'Solar Orbiter ("SolO"), an ESA/NASA solar probe mission'},
        
    # --- Adding New Moons ---

    # Mars' Moons
    {'name': 'Phobos', 'id': '401', 'var': phobos_var, 'color': color_map('Phobos'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Mars orbital period: 0.32 Earth days.', 
     'mission_url': 'https://science.nasa.gov/resource/martian-moon-phobos/'},

    {'name': 'Deimos', 'id': '402', 'var': deimos_var, 'color': color_map('Deimos'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Mars orbital period: 1.26 Earth days. Retrogade.', 
     'mission_url': 'https://science.nasa.gov/mars/moons/deimos/'},

# Jupiter's Inner Ring Moons (Amalthea Group)
    {'name': 'Metis', 'id': '516', 'var': metis_var, 'color': color_map('Metis'), 'symbol': 'circle', 'is_mission': False,
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 0.295 Earth days (7.08 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Adrastea', 'id': '515', 'var': adrastea_var, 'color': color_map('Adrastea'), 'symbol': 'circle', 'is_mission': False,
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 0.298 Earth days (7.15 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Amalthea', 'id': '505', 'var': amalthea_var, 'color': color_map('Amalthea'), 'symbol': 'circle', 'is_mission': False,
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 0.498 Earth days (11.95 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    {'name': 'Thebe', 'id': '514', 'var': thebe_var, 'color': color_map('Thebe'), 'symbol': 'circle', 'is_mission': False,
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 0.675 Earth days (16.20 hours).', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/'},

    # Jupiter's Galilean Moons
    {'name': 'Io', 'id': '501', 'var': io_var, 'color': color_map('Io'), 'symbol': 'circle', 'is_mission': False, # instead of 501 use 59901?
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 1.77 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/io/'},

    {'name': 'Europa', 'id': '502', 'var': europa_var, 'color': color_map('Europa'), 'symbol': 'circle', 'is_mission': False,  # instead of id 502 use 59902?
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 3.55 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/europa/'},

    {'name': 'Ganymede', 'id': '503', 'var': ganymede_var, 'color': color_map('Ganymede'), 'symbol': 'circle', 'is_mission': False, # instead of 503 use 59903?
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 7.15 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/ganymede/'},

    {'name': 'Callisto', 'id': '504', 'var': callisto_var, 'color': color_map('Callisto'), 'symbol': 'circle', 'is_mission': False, # instead of 504 use 59904?
     'id_type': None, 
     'mission_info': 'Jupiter orbital period: 16.69 Earth days.', 
     'mission_url': 'https://science.nasa.gov/jupiter/jupiter-moons/callisto/'},

    # Saturn's Major Moons

    {'name': 'Pan', 'id': '618', 'var': pan_var, 'color': color_map('Pan'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 0.58 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/pan/'},

    {'name': 'Daphnis', 'id': '635', 'var': daphnis_var, 'color': color_map('Daphnis'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 0.58 Earth days. No Horizons ephemeris after 1-16-2018.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/daphnis/'},

    {'name': 'Prometheus', 'id': '616', 'var': prometheus_var, 'color': color_map('Prometheus'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 0.61 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/prometheus/'},

    {'name': 'Pandora', 'id': '617', 'var': pandora_var, 'color': color_map('Pandora'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 0.63 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/pandora/'},

    {'name': 'Mimas', 'id': '601', 'var': mimas_var, 'color': color_map('Mimas'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 0.94 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/mimas/'},

    {'name': 'Enceladus', 'id': '602', 'var': enceladus_var, 'color': color_map('Enceladus'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 1.37 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/enceladus/'},

    {'name': 'Tethys', 'id': '603', 'var': tethys_var, 'color': color_map('Tethys'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 1.89 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/tethys/'},

    {'name': 'Dione', 'id': '604', 'var': dione_var, 'color': color_map('Dione'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 2.74 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/dione/'},

    {'name': 'Rhea', 'id': '605', 'var': rhea_var, 'color': color_map('Rhea'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 4.52 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/rhea/'},

    {'name': 'Titan', 'id': '606', 'var': titan_var, 'color': color_map('Titan'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 15.95 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/titan/'},

    {'name': 'Hyperion', 'id': '607', 'var': hyperion_var, 'color': color_map('Hyperion'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 21 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/hyperion/'},

    {'name': 'Iapetus', 'id': '608', 'var': iapetus_var, 'color': color_map('Iapetus'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 79.33 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/iapetus/'},

    {'name': 'Phoebe', 'id': '609', 'var': phoebe_var, 'color': color_map('Phoebe'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Saturn orbital period: 550.56 Earth days.', 
     'mission_url': 'https://science.nasa.gov/saturn/moons/phoebe/'},

    # Uranus's Major Moons

    {'name': 'Ariel', 'id': '701', 'var': ariel_var, 'color': color_map('Ariel'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 2.52 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/ariel/'},

    {'name': 'Umbriel', 'id': '702', 'var': umbriel_var, 'color': color_map('Umbriel'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 4.14 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/umbriel/'},

    {'name': 'Titania', 'id': '703', 'var': titania_var, 'color': color_map('Titania'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 8.71 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/titania/'},

    {'name': 'Oberon', 'id': '704', 'var': oberon_var, 'color': color_map('Oberon'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 13.46 Earth days.', 
     'mission_url': 'https://science.nasa.gov/uranus/moons/oberon/'},

    {'name': 'Miranda', 'id': '705', 'var': miranda_var, 'color': color_map('Miranda'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 1.41 Earth days.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/miranda/'},   

    {'name': 'Portia', 'id': '712', 'var': portia_var, 'color': color_map('Portia'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 0.513196 Earth days or 12.317 hours.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/portia/'}, 

    {'name': 'Mab', 'id': '726', 'var': mab_var, 'color': color_map('Mab'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Uranus orbital period: 0.923293 Earth days or 22.159 hours.',
     'mission_url': 'https://science.nasa.gov/uranus/moons/mab/'},             

    # Neptune's Major Moons
    {'name': 'Triton', 'id': '801', 'var': triton_var, 'color': color_map('Triton'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Neptune orbital period: 5.88 Earth days.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/triton/'},

    {'name': 'Despina', 'id': '805', 'var': despina_var, 'color': color_map('Despina'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Neptune orbital period: 0.334656 Earth days.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/despina/'},

    {'name': 'Galatea', 'id': '806', 'var': galatea_var, 'color': color_map('Galatea'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Neptune orbital period: 0.428744 Earth days.', 
     'mission_url': 'https://science.nasa.gov/neptune/moons/galatea/'},

    # Pluto's Moon
    {'name': 'Charon', 'id': '901', 'var': charon_var, 'color': color_map('Charon'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Pluto orbital period: 6.39 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/charon/'},

    {'name': 'Styx', 'id': '905', 'var': styx_var, 'color': color_map('Styx'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Pluto orbital period: 20.16 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/styx/'},     

    {'name': 'Nix', 'id': '902', 'var': nix_var, 'color': color_map('Nix'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Pluto orbital period: 24.86 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/nix/'},

    {'name': 'Kerberos', 'id': '904', 'var': kerberos_var, 'color': color_map('Kerberos'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Pluto orbital period: 32.17 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/kerberos/'},

    {'name': 'Hydra', 'id': '903', 'var': hydra_var, 'color': color_map('Hydra'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Pluto orbital period: 38.20 Earth days.', 
     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/moons/hydra/'},

    # Eris's Moon
    {'name': 'Dysnomia', 'id': '120136199', 'var': dysnomia_var, 'color': color_map('Dysnomia'), 'symbol': 'circle', 'is_mission': False, 
     'id_type': None, 
     'mission_info': 'Eris orbital period: 15.79 Earth days.', 
     'mission_url': 'https://science.nasa.gov/resource/hubble-view-of-eris-and-dysnomia/'},

]

class ScrollableFrame(tk.Frame):
    """
    A scrollable frame that can contain multiple widgets with a vertical scrollbar.
    """
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Canvas and Scrollbar
        self.canvas = tk.Canvas(self, bg='SystemButtonFace')
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set) 

        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Scrollable Frame
        self.scrollable_frame = tk.Frame(self.canvas, bg='SystemButtonFace')
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Bind mousewheel to the canvas
        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)

        # Update scroll region when the canvas size changes
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

    def _on_mousewheel(self, event):
        if event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def _on_enter(self, event):
        # Bind the mousewheel events
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)  # Linux
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)  # Linux

    def _on_leave(self, event):
        # Unbind mousewheel events
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")   

    def _on_enter(self, event):
        # Bind the mouse wheel events when the cursor enters a widget
        event.widget.bind_all("<MouseWheel>", self._on_mousewheel)
        event.widget.bind_all("<Button-4>", self._on_mousewheel)
        event.widget.bind_all("<Button-5>", self._on_mousewheel)

    def _on_leave(self, event):
        # Unbind the mouse wheel events when the cursor leaves a widget
        event.widget.unbind_all("<MouseWheel>")
        event.widget.unbind_all("<Button-4>")
        event.widget.unbind_all("<Button-5>")

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=(10, 5), pady=(10, 10), sticky='n')

# Configure grid weights within input_frame for proper spacing
input_frame.grid_rowconfigure(0, weight=0)  # Row for date inputs
input_frame.grid_rowconfigure(1, weight=1)  # Row for __frame
for col in range(0, 9):
    input_frame.grid_columnconfigure(col, weight=1)  # Allow columns to expand if needed

# Scrollable frame for celestial objects and missions
scrollable_frame = ScrollableFrame(input_frame, width=430, height=710)  # Adjust width and height as needed
scrollable_frame.grid(row=1, column=0, columnspan=9, pady=(10, 5), sticky='nsew')

# Prevent the ScrollableFrame from resizing based on its content
scrollable_frame.config(width=430, height=710)
scrollable_frame.pack_propagate(False)  # Disable automatic resizing

# Optionally, set the inner frame size slightly smaller
scrollable_frame.scrollable_frame.config(width=410, height=690)
scrollable_frame.scrollable_frame.pack_propagate(False)

# Scrollable frame for celestial objects and missions
scrollable_frame = ScrollableFrame(input_frame)
scrollable_frame.grid(row=1, column=0, columnspan=9, pady=(10, 5), sticky='nsew')

# Custom Tooltip Class

class CreateToolTip(object):
    """
    Create a tooltip for a given widget with intelligent positioning to prevent clipping.
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milliseconds
        self.wraplength = 1000   # Reduced wraplength
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        try:
            # Get screen dimensions and taskbar height (estimated)
            screen_width = self.widget.winfo_screenwidth()
            screen_height = self.widget.winfo_screenheight()
            taskbar_height = 40  # Estimated Windows taskbar height

            # Create the tooltip window
            self.tw = tk.Toplevel(self.widget)
            self.tw.wm_overrideredirect(True)
            
            # Calculate usable screen height
            usable_height = screen_height - taskbar_height

            # Create the tooltip label
            label = tk.Label(
                self.tw,
                text=self.text,
                justify='left',
                background='yellow',
                relief='solid',
                borderwidth=1,
                wraplength=min(self.wraplength, screen_width - 100),
                font=("Arial", 10, "normal")
            )
            label.pack(ipadx=1, ipady=1)

            # Update the window to calculate its size
            self.tw.update_idletasks()
            tooltip_width = self.tw.winfo_width()
            tooltip_height = self.tw.winfo_height()

            # Initial x position - try positioning to the right of the widget first
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5

            # If tooltip would extend beyond right edge, try positioning to the left of the widget
            if x + tooltip_width > screen_width:
                x = self.widget.winfo_rootx() - tooltip_width - 5

            # If that would push it off the left edge, position at left screen edge with padding
            if x < 0:
                x = 5

            # Calculate vertical position
            y = self.widget.winfo_rooty()

            # If tooltip is taller than available space, position at top of screen
            if tooltip_height > usable_height:
                y = 5  # Small padding from top
            else:
                # Center vertically relative to widget if space allows
                widget_center = y + (self.widget.winfo_height() / 2)
                y = widget_center - (tooltip_height / 2)
                
                # Ensure tooltip doesn't go below usable screen area
                if y + tooltip_height > usable_height:
                    y = usable_height - tooltip_height - 5

                # Ensure tooltip doesn't go above top of screen
                if y < 5:
                    y = 5

            # Position the tooltip
            self.tw.wm_geometry(f"+{int(x)}+{int(y)}")

        except Exception as e:
            print(f"Error showing tooltip: {e}")
            traceback.print_exc()

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None

"""
# Ask the user whether to refresh all stored orbit paths (warn about delay)
refresh_all = messagebox.askyesno(
    "Refresh Orbit Data",
    "Would you like to refresh all stored orbit paths from JPL Horizons?\n\n"
    "This may take several minutes. Choose 'No' to only fetch missing data."
)
"""

# Create backup on startup
message, msg_type = create_orbit_backup()
update_status_display(message, msg_type)

# Initialize orbit data manager without dialogs
orbit_paths_over_time = orbit_data_manager.initialize(status_display)

# Run cleanup if needed
#cleanup_msg, cleanup_type = cleanup_old_orbits()
#if cleanup_msg:
#    update_status_display(cleanup_msg, cleanup_type)

# Print cache health summary once per session
if os.path.exists('orbit_paths.json'):
    with open('orbit_paths.json', 'r') as f:
        orbit_data = json.load(f)
        
    # Analyze cache by center object
    center_stats = {}
    for key in orbit_data.keys():
        if '_' in key:
            parts = key.split('_')
            if len(parts) >= 2:
                center = parts[1]
                center_stats[center] = center_stats.get(center, 0) + 1
    
    print("\n[CACHE HEALTH SUMMARY]")
    print(f"Total cached orbits: {len(orbit_data)}")
    print("Orbits by center object:")
    for center, count in sorted(center_stats.items()):
        print(f"  {center}: {count} orbits")
    print("\nNote: Cache can only be manually deleted by removing 'orbit_paths.json' file")
    print("-" * 50)

# CONSTANTS
BUTTON_FONT = ("Arial", 10, "normal")  # You can adjust the font as needed
BUTTON_WIDTH = 17  # Number of characters wide
# COMET_INTERVAL_DIVISOR = 100
# MISSION_INTERVAL_DIVISOR = 75
# PLANET_INTERVAL_DIVISOR = 50
# SAT_PLOT_ORBIT_DAYS = 56
# SAT_PLOT_ORBIT_PERIOD = 1

# Add a pulsating effect to the progress bar during long operations
def pulse_progress_bar():
    """Create a pulsating effect for the progress bar"""
    progress_bar.step(2)  # Increase by 2%
    root.after(100, pulse_progress_bar)  # Call again after 100ms
    
# Update orbit_paths to handle center objects
def update_orbit_paths(center_object_name='Sun'):
    """
    For each object in the global 'objects' list that has an 'id', check if its orbit path is
    stored in orbit_paths_over_time. If not (or if refresh_all is True), fetch its orbit path
    from JPL Horizons and update the global dictionary.
    
    Parameters:
        center_object_name (str): Name of the central body (default: 'Sun')
    """
# def update_orbit_paths():

    import datetime
    global orbit_paths_over_time
    
    # Get center object info
    center_object_info = next((obj for obj in objects if obj['name'] == center_object_name), None)
    if center_object_info:
        center_id = center_object_info['id']
        center_id_type = center_object_info.get('id_type')
    else:
        center_id = 'Sun'
        center_id_type = None

    updated_count = 0
    total_objects = 0
#    now = datetime.datetime.now()                       # default code 
# Use a datetime object for a specific date, such as:
#    now = datetime.datetime(1986, 4, 11)               # start date for comet Ikeya-Seki ephemeris
    # For demonstration, set the orbit path time range to one year before and after the current date.
#    start_date = now - datetime.timedelta(days=365)     # one year
#    end_date = now + datetime.timedelta(days=365)       # one year
    now = STATIC_TODAY
    start_date = now - datetime.timedelta(days=0)    # default start at now
    end_date = now + datetime.timedelta(days=365)      # default 1 year or 365 days
    
    # Iterate over all objects in the 'objects' list
    for obj in objects:
        if 'id' not in obj or obj['name'] == center_object_name:
#        if 'id' not in obj:
            continue
        total_objects += 1

        # Check if this is a satellite of the center object
        is_satellite_of_center = False
        if center_object_name in parent_planets and obj['name'] in parent_planets.get(center_object_name, []):
            is_satellite_of_center = True
            print(f"Identified {obj['name']} as a satellite of {center_object_name}")

        # Generate a unique key for this object-center pair
        orbit_key = f"{obj['name']}_{center_object_name}"

        # If refresh_all is True or the object's orbit path is missing, fetch new data.
#        if refresh_all or (obj['name'] not in orbit_paths_over_time):
        if orbit_key not in orbit_paths_over_time:
            # Determine a suitable interval.
            # Use adaptive step sizing if available – for example, for high eccentricity objects use "12h" instead of "1d".
            interval = "1d"  # default interval

            if obj['name'] in planetary_params:
                e = planetary_params[obj['name']].get('e', 0)
                if e > 0.5:  # example threshold for a highly elliptical orbit
                    interval = "12h"
            else:
                # For spacecraft, comets, and moons, use a finer interval
                # For comet Ikeya-Seki using 6h, then 2h for +/- 3 days, and 1h for +/- 1 day from perihelion 1965-10-21
                interval = "6h"
            
            # For satellites of the center object, use a much finer resolution
            if is_satellite_of_center:
                interval = "1h"  # Higher resolution for moons orbiting the center

            # Update the status in the GUI
            status_display.config(text=f"Fetching orbit path for {obj['name']} relative to {center_object_name}...")
    #        status_label.config(text=f"Fetching orbit path for {obj['name']}...")
            root.update()  # Force GUI to refresh the status
            
            path_data = fetch_orbit_path(
                obj, 
                start_date, 
                end_date, 
                interval, 
                center_id=center_id,
                id_type=obj.get('id_type')
            )           

            if path_data is not None:
                # Store with the unique key
                orbit_paths_over_time[orbit_key] = path_data
                updated_count += 1
                print(f"Updated orbit path for {obj['name']} relative to {center_object_name}")
    
    status_display.config(text=f"Orbit paths updated for {updated_count}/{total_objects} objects relative to {center_object_name}.")
    # Save the updated orbit paths to the JSON file
    orbit_data_manager.save_orbit_paths(orbit_paths_over_time)

# Load the stored orbit paths at startup
orbit_paths_over_time = orbit_data_manager.load_orbit_paths()

# Now that 'objects' is defined, update orbit paths with Sun as center (default)
# update_orbit_paths('Sun')
# update_orbit_paths()

def plot_orbit_paths(fig, objects_to_plot, center_object_name='Sun'):
    """Plot orbit paths using data from orbit_data_manager or temp cache."""
    # Check if we're in special fetch mode
    if special_fetch_var.get() == 1 and temp_cache:
        # Use temp cache data
        plot_data = {}
        print(f"[PLOT ORBIT PATHS] Using temp cache with {len(temp_cache)} orbits")
        for obj in objects_to_plot:
            orbit_key = f"{obj['name']}_{center_object_name}"
            if orbit_key in temp_cache:
                plot_data[obj['name']] = temp_cache[orbit_key]
                print(f"[PLOT ORBIT PATHS] Found {obj['name']} in temp cache with {len(temp_cache[orbit_key]['x'])} points")
    else:
        # Get orbit data in plot-ready format from main cache
        plot_data = orbit_data_manager.get_orbit_data_for_plotting(objects_to_plot, center_object_name)
        print(f"[PLOT ORBIT PATHS] Using main cache")
    
    for name, path_data in plot_data.items():
        # Skip objects that are the center
        if name == center_object_name:
            continue
            
        # Check if this is a satellite of the center object
        is_satellite_of_center = center_object_name in parent_planets and name in parent_planets.get(center_object_name, [])
        
        # Create the hover text arrays
        if is_satellite_of_center:
            hover_text = [f"{name} Orbit around {center_object_name}"] * len(path_data['x'])
            orbit_name = f"{name} Orbit around {center_object_name}"
        else:
            hover_text = [f"{name} Orbit"] * len(path_data['x'])
            orbit_name = f"{name} Orbit"

        print(f"Plotting orbit for {name} relative to {center_object_name} ({len(path_data['x'])} points)")
      
        fig.add_trace(
            go.Scatter3d(
                x=path_data['x'],
                y=path_data['y'],
                z=path_data['z'],
                mode='lines',
                line=dict(width=1, color=color_map(name)),
                name=orbit_name,
                text=hover_text,
                customdata=hover_text,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )

# Suppress ErfaWarning messages
warnings.simplefilter('ignore', ErfaWarning)
    
def plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id='Sun', show_lines=False, center_object_name='Sun'):
    """
    Plot actual orbit positions for selected objects.
    
    Parameters:
        fig: plotly figure object
        planets_to_plot: list of planet names to plot
        dates_lists: dictionary mapping planet names to lists of dates
        center_id: ID of central body (default: 'Sun')
        show_lines: whether to show lines connecting points (default: False)
        center_object_name: Name of the center object (default: 'Sun')
    """
    # Check if we're in special fetch mode and should use temp cache
    if special_fetch_var.get() == 1 and temp_cache:
        # For special fetch mode, use the temp cache data directly
        print("[SPECIAL FETCH MODE] Using temp cache for plot_actual_orbits")
        print(f"[DEBUG] Temp cache keys: {list(temp_cache.keys())}")
        print(f"[DEBUG] Looking for planets: {planets_to_plot}")
        print(f"[DEBUG] Center object: {center_object_name}")
        
        for planet in planets_to_plot:
            orbit_key = f"{planet}_{center_object_name}"
            print(f"[DEBUG] Looking for key: {orbit_key}")
            if orbit_key in temp_cache:
                path_data = temp_cache[orbit_key]
                x = path_data['x']
                y = path_data['y'] 
                z = path_data['z']
                
                if show_lines:
                    mode = 'lines'
                    line = dict(color=color_map(planet), width=1)
                    marker = None
                else:
                    mode = 'markers'
                    line = None
                    marker = dict(color=color_map(planet), size=1)

                # Create the hover text for the actual orbit
                hover_text = f"{planet} Orbit"

                fig.add_trace(
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode=mode,
                        line=line,
                        marker=marker,
                        name=f"{planet} Orbit",
                        text=[hover_text] * len(x),
                        customdata=[hover_text] * len(x),
                        hovertemplate='%{text}<extra></extra>',
                        showlegend=True
                    )
                )
                print(f"[SPECIAL FETCH] Plotted {planet} orbit with {len(x)} points from temp cache")
            else:
                print(f"[SPECIAL FETCH] {planet} not found in temp cache")
    else:
        # Normal mode - use dates_lists and fetch_trajectory
        print("[NORMAL MODE] Using dates_lists for plot_actual_orbits")
        for planet in planets_to_plot:
            dates_list = dates_lists.get(planet, [])
            if not dates_list:
                print(f"No dates available for {planet}, skipping.")
                continue
            print(f"[NORMAL MODE] {planet}: {len(dates_list)} dates from {dates_list[0]} to {dates_list[-1]}")
            
            obj_info = next((obj for obj in objects if obj['name'] == planet), None)
            if not obj_info:
                continue
            trajectory = fetch_trajectory(obj_info['id'], dates_list, center_id=center_id, id_type=obj_info.get('id_type'))
            # Now trajectory is a list of positions
            if trajectory:
                x = [pos['x'] for pos in trajectory if pos is not None]
                y = [pos['y'] for pos in trajectory if pos is not None]
                z = [pos['z'] for pos in trajectory if pos is not None]
                if show_lines:                                                 # this code adds lines betwen the markers
                    mode = 'lines'
                    line = dict(color=color_map(planet), width=1)
                    marker = None
                else:
                    mode = 'markers'
                    line = None
                    marker = dict(color=color_map(planet), size=1)

                # Create the hover text for the actual orbit
                hover_text = f"{planet} Orbit"

                fig.add_trace(
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode=mode,
                        line=line,
                        marker=marker,
                        name=f"{planet} Orbit",
                        text=[hover_text] * len(x),           # Add proper hover text
                        customdata=[hover_text] * len(x),     # Same for customdata
                        hovertemplate='%{text}<extra></extra>',
                        showlegend=True
                    )
                )
                print(f"[NORMAL MODE] Plotted {planet} orbit with {len(x)} points")

# Define dictionary mapping all celestial bodies to their shell variable dictionaries
body_shells_config = {
    'Sun': sun_shell_vars,
    'Mercury': mercury_shell_vars,
    'Venus': venus_shell_vars,
    'Earth': earth_shell_vars,
    'Moon': moon_shell_vars,
    'Mars': mars_shell_vars,
    'Jupiter': jupiter_shell_vars,
    'Saturn': saturn_shell_vars,
    'Uranus': uranus_shell_vars,
    'Neptune': neptune_shell_vars,
    'Pluto': pluto_shell_vars,
    'Eris/Dysnomia': eris_shell_vars,
    'Planet 9': planet9_shell_vars
    # Add more celestial bodies here as shell systems are developed
}

def plot_objects():
    def worker():
        try:

            # Add explicit reference to avoid issues with nested scopes
            global orbit_paths_over_time

            # Reset the global today or use a local today variable
            today = datetime.today()

            # Create figure object at the start
            fig = go.Figure()

            # Add global sun direction indicator to the plot
    #        fig = add_global_sun_direction_indicator(fig)

            # Generate default name with timestamp
            current_date = STATIC_TODAY
            default_name = f"solar_system_{current_date.strftime('%Y%m%d_%H%M')}"
                       
            output_label.config(text="Fetching data, please wait...")
            progress_bar['mode'] = 'indeterminate'
            progress_bar.start(10)  # Start the progress bar with a slight delay
            root.update_idletasks()  # Force GUI to update

            # Get user-defined interval values
            try:
                comet_interval_divisor = float(comet_interval_entry.get())
                mission_interval_divisor = float(mission_interval_entry.get())
                planet_interval_divisor = float(planet_interval_entry.get())
                sat_plot_orbit_days = int(sat_days_entry.get())
                sat_plot_orbit_period = int(sat_period_entry.get())
                
                # Ensure values are within reasonable ranges
                if comet_interval_divisor <= 0: comet_interval_divisor = 100
                if mission_interval_divisor <= 0: mission_interval_divisor = 75
                if planet_interval_divisor <= 0: planet_interval_divisor = 50
                if sat_plot_orbit_days <= 0: sat_plot_orbit_days = 56              
                if sat_plot_orbit_period <= 0: sat_plot_orbit_period = 1
                
            except ValueError:
                # Default values if parsing fails
                comet_interval_divisor = 100
                mission_interval_divisor = 75
                planet_interval_divisor = 50
                sat_plot_orbit_days = 56
                sat_plot_orbit_period = 1
                output_label.config(text="Invalid interval values, using defaults.")

            # Get the date from the entry fields
            year = int(entry_year.get())
            month = int(entry_month.get())
            day = int(entry_day.get())
            hour = int(entry_hour.get())
            minute = int(entry_minute.get())  # Get minute value
            date_obj = datetime(year, month, day, hour, minute)

            # Define hover_data with a default value
            hover_data = "Full Object Info"  # Or "Object Names Only"

            # Determine center object
            center_object_name = center_object_var.get()
            center_object_info = next((obj for obj in objects if obj['name'] == center_object_name), None)
            if center_object_info:
                if center_object_name == 'Sun':
                    center_id = 'Sun'
                    center_id_type = None
                else:
                    center_id = center_object_info['id']
                    center_id_type = center_object_info.get('id_type')
            else:
                center_id = 'Sun'
                center_id_type = None

# Get selected objects
            selected_objects = [obj for obj in objects if obj['var'].get() == 1]
            
            if not selected_objects:
                output_label.config(text="No objects selected for plotting")
                progress_bar.stop()
                return

            # Check if we're in special fetch mode or normal mode
            if special_fetch_var.get() == 0:  # Normal mode
                # Check if any selected object needs updating
                need_update = False
                for obj in selected_objects:
                    orbit_key = f"{obj['name']}_{center_object_name}"
                    if orbit_key not in orbit_paths_over_time:
                        need_update = True
                        break
                    # TODO: Could add more sophisticated checks here (date range, resolution, etc.)
                
                # Handle updates based on user preference
                should_update = False
                
                if need_update and not update_choice_remembered:
                    # Show dialog
                    dialog = tk.Toplevel(root)
                    dialog.title("Update Orbit Data?")
                    dialog.geometry("400x200")
                    
                    message = tk.Label(dialog, 
                        text=f"New orbit data is needed for {len(selected_objects)} selected objects.\n\n"
                             f"Would you like to fetch updated data from JPL Horizons?",
                        wraplength=350)
                    message.pack(pady=20)
                    
                    remember_var = tk.IntVar(value=0)
                    remember_check = tk.Checkbutton(dialog,
                        text="Remember my choice for this session\n"
                             "(Warning: This applies globally to all plots)",
                        variable=remember_var)
                    remember_check.pack(pady=10)
                    
                    button_frame = tk.Frame(dialog)
                    button_frame.pack()
                    
                    user_choice = {'update': None}
                    
                    def on_yes():
                        user_choice['update'] = True
                        if remember_var.get() == 1:
                            global remember_update_choice, update_choice_remembered
                            remember_update_choice = True
                            update_choice_remembered = True
                        dialog.destroy()
                    
                    def on_no():
                        user_choice['update'] = False
                        if remember_var.get() == 1:
                            global remember_update_choice, update_choice_remembered
                            remember_update_choice = False
                            update_choice_remembered = True
                        dialog.destroy()
                    
                    tk.Button(button_frame, text="Yes - Update Cache", 
                             command=on_yes, bg='light green').pack(side='left', padx=5)
                    tk.Button(button_frame, text="No - Use Existing", 
                             command=on_no, bg='light coral').pack(side='left', padx=5)
                    
                    dialog.wait_window()
                    
                    should_update = user_choice.get('update', False)
                
                elif need_update and update_choice_remembered:
                    # Use remembered choice
                    should_update = remember_update_choice
                
                # Perform update if needed
                if should_update:
                    update_status_display("Updating orbit cache for selected objects...", 'info')
                    progress_bar.step(10)
                    root.update_idletasks()
                    
                    updated, current, total, time_saved = orbit_data_manager.update_orbit_paths_incrementally(
                        object_list=selected_objects,
                        center_object_name=center_object_name,
                        days_ahead=int(end_date_entry.get()),
                        planetary_params=planetary_params,
                        parent_planets=parent_planets,
                        root_widget=root
                    )
                    
                    update_status_display(f"Cache updated: {updated} new, {current} current", 'success')
                else:
                    update_status_display("Using existing cache without updates", 'info')
                    
            else:  # Special fetch mode
                update_status_display("Special fetch mode: Fetching data (not cached)...", 'special')
                print(f"[SPECIAL FETCH] Getting data for {len(selected_objects)} objects")
                
                # Fetch to temp cache with custom settings
                for obj in selected_objects:
                    if obj['name'] != center_object_name:
                        orbit_key = f"{obj['name']}_{center_object_name}"
                        
                        # Determine interval based on object type and GUI settings
                        if obj['name'] in parent_planets.get(center_object_name, []):
                            interval = satellite_interval_entry.get()
                        elif obj.get('is_mission') or obj.get('is_comet'):
                            interval = mission_comet_interval_entry.get()
                        else:
                            interval = default_interval_entry.get()
                        
                        # Calculate date range
                        start_date = date_obj + timedelta(days=int(start_date_entry.get()))
                        end_date = date_obj + timedelta(days=int(end_date_entry.get()))
                        
                        # Fetch without caching to main file
                        orbit_data = fetch_orbit_path(obj, start_date, end_date, interval,
                                                    center_id=center_id, id_type=obj.get('id_type'))
                        if orbit_data:
                            temp_cache[orbit_key] = orbit_data
                
                # Save temp cache
                with open(TEMP_CACHE_FILE, 'w') as f:
                    json.dump(temp_cache, f)
                
                update_status_display(f"Special fetch complete: {len(temp_cache)} orbits in temp cache", 'special')
                print(f"[SPECIAL FETCH] Temp cache contains {len(temp_cache)} orbits")
            
            progress_bar.step(10)
            root.update_idletasks()

            # Define planets with shell visualizations
            planets_with_shells = {
                'Mercury': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': mercury_shell_vars
                },
                'Venus': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': venus_shell_vars
                },
                'Earth': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': earth_shell_vars
                },
                'Moon': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': moon_shell_vars
                },
                'Mars': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': mars_shell_vars
                },
                'Jupiter': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': jupiter_shell_vars
                },
                'Saturn': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': saturn_shell_vars
                },
                'Uranus': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': uranus_shell_vars
                },
                'Neptune': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': neptune_shell_vars
                },
                'Pluto': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': pluto_shell_vars
                },
                'Eris/Dysnomia': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': eris_shell_vars
                },
                'Planet 9': {
                    'position': None,  # Will be populated during animation
                    'shell_vars': planet9_shell_vars
                }
            }

            # Create date lists for each selected object
            dates_lists = {}
            for obj in objects:

        #    else:

                # For satellites specifically, even if they have orbital parameters, 
                # we should always fetch their actual position data
                if obj['var'].get() == 1 and obj['name'] != center_object_name:

                    # Check if this is a satellite of a planet
                    is_satellite = False
                    parent_planet = None
                    for planet, moons in parent_planets.items():
                        if obj['name'] in moons:
                            is_satellite = True
                            parent_planet = planet  # Use 'planet' to match the loop variable
                            break

                    is_parent = obj['name'] in parent_planets    
                    
                    if obj.get('is_comet', False):
                        start_date = obj.get('start_date', date_obj)
                        end_date = obj.get('end_date', date_obj)
                        total_days = (end_date - start_date).days
                        if total_days <= 0:
                            dates_list = [start_date]
                        else:
                            # Replace np.arange with np.linspace for more precise spacing
                            num_points = int(comet_interval_divisor) + 1
                            dates_list = [start_date + timedelta(days=float(d)) for d in np.linspace(0, total_days, num=num_points)]                            
                #            interval = total_days / comet_interval_divisor         # divide by 100 to have more resolution at perihelion, increase for more intervals
                #            dates_list = [start_date + timedelta(days=i) for i in np.arange(0, total_days + 1, interval)]
                        dates_lists[obj['name']] = dates_list

                    elif obj.get('is_mission', False):
                        start_date = obj.get('start_date', date_obj)
                        end_date = obj.get('end_date', date_obj)
                        total_days = (end_date - start_date).days
                        if total_days <= 0:
                            dates_list = [start_date]
                        else:
                            # Replace np.arange with np.linspace for more precise spacing
                            num_points = int(mission_interval_divisor) + 1
                            dates_list = [start_date + timedelta(days=float(d)) for d in np.linspace(0, total_days, num=num_points)]                            
                #            interval = total_days / mission_interval_divisor      # divide by 75 to have more resolution at launch
                #            dates_list = [start_date + timedelta(days=i) for i in np.arange(0, total_days + 1, interval)]
                        dates_lists[obj['name']] = dates_list

                    elif is_satellite or obj['name'] in ['Moon']:  # Explicitly check for known satellites
                        # Always use actual trajectory for satellites, regardless of planetary_params
                        # Replace range with np.linspace for more precise spacing
                        num_points = int(sat_plot_orbit_days / sat_plot_orbit_period) + 1
                        dates_list = [date_obj + timedelta(days=float(d)) for d in np.linspace(0, sat_plot_orbit_days, num=num_points)]
                        dates_lists[obj['name']] = dates_list

                    elif obj['name'] in planetary_params:
                        a = planetary_params[obj['name']]['a']  # Semi-major axis in AU
                        orbital_period_years = np.sqrt(a ** 3)  # Period in Earth years
                        orbital_period_days = orbital_period_years * 365.25                

                        days_until_horizons = (HORIZONS_MAX_DATE - date_obj).days
                        days_until_datetime_max = (datetime.max - date_obj).days

                        # List of objects known to work with their full orbital periods
                        non_problematic_objects = ['Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

                        if obj['name'] in non_problematic_objects:
                            # For well-established planets, use their full orbital period with system limits
                            capped_orbital_period_days = min(orbital_period_days, days_until_horizons, days_until_datetime_max)
                            print(f"Using full orbital period for {obj['name']}: {capped_orbital_period_days:.1f} days")
                        else:
                            # For all other objects (KBOs, dwarf planets, etc.), cap at a reasonable timeframe
                            # For objects like Sedna with extremely long periods, this is essential
            #                reasonable_period = min(10*365.25, orbital_period_days * 0.05)  # 10 years or 5% of orbit, whichever is smaller
                            reasonable_period = 3650  # 10 years 
                            capped_orbital_period_days = min(reasonable_period, days_until_horizons)
                            print(f"Applied capping for {obj['name']}: Original {orbital_period_days:.1f} → Capped {capped_orbital_period_days:.1f} days")

                        if capped_orbital_period_days <= 0:
                            dates_list = [date_obj]
                        else:

                            num_points = int(planet_interval_divisor) + 1
                            dates_list = [date_obj + timedelta(days=float(d)) for d in np.linspace(0, capped_orbital_period_days, num=num_points)]                            

                        dates_lists[obj['name']] = dates_list
                    
                        # Add in both functions where date lists are calculated
                        has_satellites = obj['name'] in parent_planets
                        print(f"\n{obj['name']} satellite status:")
                        print(f"  Has satellites: {has_satellites}")
                        if has_satellites:
                            print(f"  Satellites: {parent_planets.get(obj['name'], [])}")
                        print(f"  Date calculation method: {'satellite_parent' if has_satellites else 'no_satellites'}")

                        # Then print the actual date range being used
                        if 'dates_list' in locals() and dates_list:
                            print(f"  Date range: {dates_list[0]} to {dates_list[-1]}")
                            print(f"  Total days: {(dates_list[-1] - dates_list[0]).days}")
                            print(f"  Points: {len(dates_list)}")

                    else:   
                        # Replace range with np.linspace for more precise spacing
                        num_points = int(sat_plot_orbit_days / sat_plot_orbit_period) + 1
                        dates_list = [date_obj + timedelta(days=float(d)) for d in np.linspace(0, sat_plot_orbit_days, num=num_points)]                                                                                            # planetary satellites
                #        dates_list = [date_obj + timedelta(days=i) for i in range(0, sat_plot_orbit_days, sat_plot_orbit_period)] # starts at day 0, for 420 days, with 7 day intervals
                        dates_lists[obj['name']] = dates_list

            # Fetch positions for selected objects on the chosen date
            positions = {}
            for obj in objects:
                if obj['var'].get() == 1:

                    if obj['name'] == 'Planet 9' or obj['id'] == 'planet9_placeholder':
                        # Calculate Planet 9 position directly on its theoretical orbit
                        x, y, z, range_val = calculate_planet9_position_on_orbit()
                        # Create a complete position object
                        obj_data = {
                            'x': x,
                            'y': y,
                            'z': z,
                            'range': range_val,
                            'distance_km': range_val * KM_PER_AU,
                            'distance_lm': range_val * LIGHT_MINUTES_PER_AU,
                            'distance_lh': (range_val * LIGHT_MINUTES_PER_AU) / 60,
                            'vx': 0,
                            'vy': 0,
                            'vz': 0,
                            'velocity': 0,
                            'calculated_orbital_period': {
                                'years': np.sqrt(600**3),  # Semi-major axis^1.5
                                'days': np.sqrt(600**3) * 365.25
                            },
                            'known_orbital_period': {
                                'years': np.sqrt(600**3),
                                'days': np.sqrt(600**3) * 365.25
                            },
                            'orbital_period': np.sqrt(600**3)  # Orbital period in years
                        }
                    elif obj['name'] == center_object_name:

            #        if obj['name'] == center_object_name:
                        obj_data = {'x': 0, 'y': 0, 'z': 0}
                    else:
                        obj_data = fetch_position(obj['id'], date_obj, center_id=center_id, id_type=obj.get('id_type', None))
                    positions[obj['name']] = obj_data

                    # Store positions for planets with shells
                    if obj['name'] in planets_with_shells and obj_data and 'x' in obj_data:
                        planets_with_shells[obj['name']]['position'] = (obj_data['x'], obj_data['y'], obj_data['z'])

            # Print planet positions in the console
            print_planet_positions(positions)

            # Prepare coordinate lists for auto-scaling
            x_coords = []
            y_coords = []
            z_coords = []
            for obj_data in positions.values():
                if obj_data and obj_data['x'] is not None:
                    x_coords.append(obj_data['x'])
                    y_coords.append(obj_data['y'])
                    z_coords.append(obj_data['z'])

            # Decide on scale
            if scale_var.get() == 'Auto':
                if x_coords and y_coords and z_coords:
                    x_min, x_max = min(x_coords), max(x_coords)
                    y_min, y_max = min(y_coords), max(y_coords)
                    z_min, z_max = min(z_coords), max(z_coords)

                    x_range = x_max - x_min
                    y_range = y_max - y_min
                    z_range = z_max - z_min
                    max_range = max(x_range, y_range, z_range)
                    padding = max_range * 0.5
                    if max_range == 0:
                        padding = 1e-3

                    x_axis_range = [x_min - padding, x_max + padding]
                    y_axis_range = [y_min - padding, y_max + padding]
                    z_axis_range = [z_min - padding, z_max + padding]
                    overall_max = max(
                        abs(x_axis_range[0]), x_axis_range[1],
                        abs(y_axis_range[0]), y_axis_range[1],
                        abs(z_axis_range[0]), z_axis_range[1]
                    )
                    axis_range = [-overall_max, overall_max]
                else:
                    axis_range = [-1, 1]
            else:
                try:
                    custom_scale = float(custom_scale_entry.get())
                    axis_range = [-custom_scale, custom_scale]
                except ValueError:
                    output_label.config(text="Invalid custom scale value.")
                    progress_bar.stop()
                    return

            # Create Plotly figure
            fig = go.Figure()

            # Add hover toggle buttons
            fig = add_hover_toggle_buttons(fig)

            # Define dictionary mapping planets to their shell variable dictionaries
            planet_shells_config = {
                'Mercury': mercury_shell_vars,
                'Venus': venus_shell_vars,
                'Earth': earth_shell_vars,
                'Moon': moon_shell_vars,
                'Mars': mars_shell_vars,
                'Jupiter': jupiter_shell_vars,
                'Saturn': saturn_shell_vars,
                'Uranus': uranus_shell_vars,
                'Neptune': neptune_shell_vars,
                'Pluto': pluto_shell_vars,
                'Eris/Dysnomia': eris_shell_vars,
                'Planet 9': planet9_shell_vars               
                # Add more planets here as shell systems are developed
            }

            # Flag to track if shells have been added for center object
            center_shells_added = False

            # First add Sun visualization if needed
            if center_object_name == 'Sun' and any(var.get() == 1 for var in sun_shell_vars.values()):
                fig = create_sun_visualization(fig, sun_shell_vars)
                center_shells_added = True
                
            # Now add planet visualization if the center is a planet with shells
            elif center_object_name in planet_shells_config:
                shell_vars = planet_shells_config[center_object_name]
                if any(var.get() == 1 for var in shell_vars.values()):
                    fig = create_planet_visualization(fig, center_object_name, shell_vars)
                    center_shells_added = True

            # Add center marker only if shells haven't been added
            if not center_shells_added:
                if center_object_name == 'Sun':
                    # Just add the central Sun marker if shells not selected
                    fig.add_trace(
                        go.Scatter3d(
                            x=[0],
                            y=[0],
                            z=[0],
                            mode='markers',
                            marker=dict(
                                color='rgb(102, 187, 106)',
                                size=12,
                                symbol=center_object_info['symbol']
                            ),
                            name="Sun",
                            text=[hover_text_sun],
                            customdata=["Sun"],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )
                else:
                    # For other central bodies (planets), add the center marker trace
                    fig.add_trace(
                        go.Scatter3d(
                            x=[0],
                            y=[0],
                            z=[0],
                            mode='markers',
                            marker=dict(
                                color=center_object_info['color'],
                                size=12,
                                symbol=center_object_info['symbol']
                            ),
                            name=f"{center_object_name}",
                            text=[center_object_name],
                            hoverinfo='skip',
                            showlegend=True
                        )
                    )

            # Create dictionary of shell variables for each planet
            planet_shell_vars = {
                'Mercury': mercury_shell_vars,
                'Venus': venus_shell_vars,
                'Earth': earth_shell_vars,
                'Moon': moon_shell_vars,
                'Mars': mars_shell_vars,
                'Jupiter': jupiter_shell_vars,
                'Saturn': saturn_shell_vars,
                'Uranus': uranus_shell_vars,
                'Neptune': neptune_shell_vars,
                'Pluto': pluto_shell_vars,
                'Eris/Dysnomia': eris_shell_vars,
                'Planet 9': planet9_shell_vars               
            }

            # Add Sun direction indicator for non-center planets with shells
            for planet_name, planet_data in planets_with_shells.items():
                is_center = (center_object_name == planet_name)
                
                # Modified condition: allow shells for any planet, not just the center
                if planet_name in planet_shell_vars:
                    # For center planet, position at (0,0,0)
                    if is_center and not center_shells_added:
                        print(f"\nAdding shells for center planet {planet_name}")
                        fig = create_planet_visualization(
                            fig,                            # First parameter should be fig
                            planet_name,                    # Second parameter should be planet_name
                            planet_shell_vars[planet_name], # Third parameter should be shell_vars
                            center_position=(0, 0, 0)       # Named parameter can stay as is
                        )
                    # For non-center planets, use their actual positions
                    elif not is_center and 'position' in planet_data and planet_data['position'] is not None:
                        # Check if any shell for this planet is selected
                        if any(var.get() == 1 for var in planet_shell_vars[planet_name].values()):
                            print(f"\nAdding shells for non-center planet {planet_name}")
                            
                            # Always add the planet shells
                            fig = create_planet_visualization(
                                fig,                            
                                planet_name,                    
                                planet_shell_vars[planet_name], 
                                center_position=planet_data['position']  # Use planet's position
                            )

                            # Only add sun direction indicator when Sun is not the center
                            if center_object_name != 'Sun':
                                print(f"Adding Sun direction indicator for {planet_name}")
                                sun_direction_traces = create_sun_direction_indicator(
                                    center_position=planet_data['position'],
                                    axis_range=axis_range,  # Pass the axis_range parameter
                                    object_type=planet_name,
                                    center_object=center_object_name
                                )

                                for trace in sun_direction_traces:
                                    fig.add_trace(trace)
                            
            # Plot the actual orbits for selected objects
            selected_planets = [obj['name'] for obj in objects if obj['var'].get() == 1 and obj['name'] != center_object_name]
            # Pass center_object_name to plot_actual_orbits
            print(f"[DEBUG] Calling plot_actual_orbits with center_object_name={center_object_name}")
            plot_actual_orbits(fig, selected_planets, dates_lists, center_id=center_id, show_lines=True, center_object_name=center_object_name)       #show_lines=True

            # Refetch positions (so we can add them as Scatter3d traces)
            positions = {}
            for obj in objects:
                if obj['var'].get() == 1:
                    if obj['name'] == center_object_name:
                        obj_data = {'x': 0, 'y': 0, 'z': 0}
                    else:
                        obj_data = fetch_position(obj['id'], date_obj, center_id=center_id, id_type=obj.get('id_type', None))
                    positions[obj['name']] = obj_data

            # Plot each celestial object
            for obj in objects:
                if obj['var'].get() == 1 or obj['name'] == center_object_name:
                    obj_data = positions.get(obj['name'])
                    if obj_data:
                        marker_size = 6
                        if obj['name'] == center_object_name:
                            marker_size = 10
                        elif obj['name'] == 'Moon' and center_object_name == 'Earth':
                            marker_size = 6
                        add_celestial_object(fig, 
                                             obj_data, 
                                             obj['name'], 
                                             obj['color'], 
                                             obj['symbol'], 
                                             marker_size=marker_size, 
                                             hover_data=hover_data,
                                             center_object_name=center_object_name
                                             )  

            # Rearrange traces to ensure the center marker is on top
            center_trace_name = center_object_name  # This should match the 'name' parameter of your center marker trace

            # Extract center traces
            center_traces = [trace for trace in fig.data if trace.name == center_trace_name]

            # Extract all other traces
            other_traces = [trace for trace in fig.data if trace.name != center_trace_name]

            # Reassign fig.data with center traces at the end
            fig.data = tuple(other_traces + center_traces)

            # Find the section in plot_objects() where the figure layout is updated
            # Replace the existing title line with this enhanced version:

            # Calculate the end date for the title based on orbit data range
            try:
                # Get the end date offset from the GUI
                end_date_offset = int(end_date_entry.get())
                end_date = date_obj + timedelta(days=end_date_offset)
                
                # Format the title with date range
                if end_date_offset == 0:
                    # If no offset, just show the single date
                    title_text = f"Paloma's Orrery for {date_obj.strftime('%B %d, %Y %H:%M')} UTC"
                else:
                    # Show date range for orbit data
                    title_text = f"Paloma's Orrery for {date_obj.strftime('%B %d, %Y %H:%M')} through {end_date.strftime('%B %d, %Y')} UTC"
            except ValueError:
                # Fallback to original format if end_date_entry is invalid
                title_text = f"Paloma's Orrery for {date_obj.strftime('%B %d, %Y %H:%M')} UTC"

            # Update the figure layout section to use the new title:
            fig.update_layout(
                scene=dict(
                    xaxis=dict(
                        title='X (AU)',
                        range=axis_range,
                        backgroundcolor='black',
                        gridcolor='gray',
                        showbackground=True,
                        showgrid=True
                    ),
                    yaxis=dict(
                        title='Y (AU)',
                        range=axis_range,
                        backgroundcolor='black',
                        gridcolor='gray',
                        showbackground=True,
                        showgrid=True
                    ),
                    zaxis=dict(
                        title='Z (AU)',
                        range=axis_range,
                        backgroundcolor='black',
                        gridcolor='gray',
                        showbackground=True,
                        showgrid=True
                    ),
                    aspectmode='cube',
                    camera=get_default_camera()
                ),
                paper_bgcolor='black',
                plot_bgcolor='black',
                title_font_color='white',
                font_color='white',
                title=title_text,  # Use the calculated title with date range
                showlegend=True,
                legend=dict(
                    font=dict(color='white'),
                    x=1,
                    y=1,
                    xanchor='left',
                    yanchor='top'
                ),
                annotations=[
                    dict(
                        text="Data source: <a href='https://ssd.jpl.nasa.gov/horizons/app.html#/' target='_blank'>JPL Horizons</a>",
                        xref='paper',
                        yref='paper',
                        x=0,
                        y=0.35,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                    dict(
                        text="Search: <a href='https://www.nasa.gov/' target='_blank'>NASA</a>",
                        xref='paper',
                        yref='paper',
                        x=0,
                        y=0.3,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                    dict(
                        text="Click on the legend items to<br>"
                            "toggle them off and back on.",
                        xref='paper',
                        yref='paper',
                        x=0.95,
                        y=1.08,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                ]
            )

            # 5. Collect user-checked objects for orbits
            selected_objects = [obj['name'] for obj in objects if obj['var'].get() == 1]

            # 6. Plot idealized orbits using your new logic

            plot_idealized_orbits(fig, selected_objects, center_id=center_object_name, 
                                    objects=objects, planetary_params=planetary_params,
                                    parent_planets=parent_planets, color_map=color_map, date=date_obj)

            # Add URL buttons before showing/saving
            fig = add_url_buttons(fig, objects, selected_objects)

            # Generate default name with timestamp
#            current_date = datetime.now()
            current_date = STATIC_TODAY
            default_name = f"solar_system_{date_obj.strftime('%Y%m%d_%H%M')}"

            # Use show_figure_safely to handle both display and save options
            show_figure_safely(fig, default_name)

            output_label.config(text="Plotting complete.")
            progress_bar.stop()

        except Exception as e:
            output_label.config(text=f"Error during plotting: {e}")
            print(f"Error during plotting: {e}")
            traceback.print_exc()
            progress_bar.stop()

    # Instead of threading.Thread(...).start(), use create_monitored_thread
    plot_thread = create_monitored_thread(shutdown_handler, worker)
    plot_thread.start()

def animate_objects(step, label):
    def animation_worker():
        try:
            # Global references
            global orbit_paths_over_time

            # Initialize frames list at the beginning
            frames = []

            # Display status message at the beginning of animation
            output_label.config(text=f"Creating {label} animation. Please be patient as data is being fetched...")
            progress_bar['mode'] = 'indeterminate'
            progress_bar.start(10)  # Start the progress bar
            root.update_idletasks()  # Force GUI to update

            # Original setup code remains unchanged
            center_object_name = center_object_var.get()
            center_object_info = next((obj for obj in objects if obj['name'] == center_object_name), None)
            if center_object_info:
                if center_object_name == 'Sun':
                    center_id = 'Sun'
                    center_id_type = None
                else:
                    center_id = center_object_info['id']
                    center_id_type = center_object_info.get('id_type')
            else:
                center_id = 'Sun'
                center_id_type = None

            # Get frames number and validate
            N_str = num_frames_entry.get()
            if not N_str.strip():
                output_label.config(text="Please enter a valid number of frames.")
                return
            N = int(N_str)
            if N <= 0:
                output_label.config(text="Number of frames must be positive.")
                return

            # Get all user-defined interval values (unchanged)
            try:
                comet_interval_divisor = float(comet_interval_entry.get())
                mission_interval_divisor = float(mission_interval_entry.get())
                planet_interval_divisor = float(planet_interval_entry.get())
                sat_plot_orbit_days = int(sat_days_entry.get())
                sat_plot_orbit_period = int(sat_period_entry.get())
                end_date_offset = int(end_date_entry.get())
                start_date_offset = int(start_date_entry.get())
                
                if comet_interval_divisor <= 0: comet_interval_divisor = 100
                if mission_interval_divisor <= 0: mission_interval_divisor = 75
                if planet_interval_divisor <= 0: planet_interval_divisor = 50
                if sat_plot_orbit_days <= 0: sat_plot_orbit_days = 56              
                if sat_plot_orbit_period <= 0: sat_plot_orbit_period = 1
                
            except ValueError:
                comet_interval_divisor = 100
                mission_interval_divisor = 75
                planet_interval_divisor = 50
                sat_plot_orbit_days = 56
                sat_plot_orbit_period = 1
                end_date_offset = 365  # Default 1 year
                start_date_offset = 0   # Default 0 days (from now)
                output_label.config(text="Some invalid interval values, using defaults.")

            # Generate dates list
            current_date = datetime(
                int(entry_year.get()), 
                int(entry_month.get()), 
                int(entry_day.get()), 
                int(entry_hour.get()),
                int(entry_minute.get())
                )
            dates_list = []

            # [Code to generate dates_list based on step type]
            # This calculates days_ahead implicitly through the generation of dates_list
            days_ahead = 0
            if dates_list:
                days_ahead = (dates_list[-1] - dates_list[0]).days

            # INCREMENTAL UPDATE: Before animating, ensure we have updated data
            selected_objects = [obj for obj in objects if obj['var'].get() == 1]
            output_label.config(text="Checking for orbit data updates for animation...")
            root.update_idletasks()
            
            # Call the incremental update for selected objects only
            updated, current, total, time_saved = orbit_data_manager.update_orbit_paths_incrementally(
                object_list=selected_objects,
                center_object_name=center_object_name,
                days_ahead=max(days_ahead, 365),  # Ensure we have enough data for the animation
                planetary_params=planetary_params,
                parent_planets=parent_planets,
                root_widget=root
            )
            
            if updated > 0:
                output_label.config(text=f"Updated {updated} orbit paths. Creating animation...")
            else:
                output_label.config(text="Using existing orbit data. Creating animation...")
            root.update_idletasks()

            if step == 'month':
                # For months, properly handle month lengths
                for i in range(N):
                    month_offset = current_date.month - 1 + i
                    year = current_date.year + month_offset // 12
                    month = month_offset % 12 + 1
                    # Handle case where the day might not exist in the month
                    day = min(current_date.day, calendar.monthrange(year, month)[1])
                    date = datetime(year, month, day, current_date.hour, current_date.minute)
                    dates_list.append(date)
            elif step == 'year':
                # For years, handle leap year issues
                for i in range(N):
                    try:
                        date = current_date.replace(year=current_date.year + i)
                    except ValueError:
                        # Handle Feb 29 in non-leap years
                        date = current_date.replace(year=current_date.year + i, month=2, day=28)
                    dates_list.append(date)
            else:
                # For days, hours, minutes, etc.
                for i in range(N):
                    date = current_date + step * i
                    dates_list.append(date)
            
            # Make sure we have at least one valid date
            if not dates_list:
                output_label.config(text="No valid dates within Horizons data range.")
                return
                
            # Update N if dates were filtered out
            N = len(dates_list)
            
            # Define planets with shell visualizations
            planets_with_shells = {
                'Mercury': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': mercury_shell_vars
                },
                'Venus': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': venus_shell_vars
                },
                'Earth': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': earth_shell_vars
                },
                'Moon': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': moon_shell_vars
                },
                'Mars': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': mars_shell_vars
                },
                'Jupiter': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': jupiter_shell_vars
                },
                'Saturn': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': saturn_shell_vars
                },
                'Uranus': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': uranus_shell_vars
                },
                'Neptune': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': neptune_shell_vars
                },
                'Pluto': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': pluto_shell_vars
                },
                'Eris/Dysnomia': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': eris_shell_vars
                },
                'Planet 9': {
                    'positions': [],  # Will be populated during animation
                    'shell_vars': planet9_shell_vars
                }
            }
            
            # Initialize dates_lists dictionary
            dates_lists = {}

            # Use the same dates_list for all objects
            for obj in objects:
                if obj['var'].get() == 1 and obj['name'] != center_object_name:
                    dates_lists[obj['name']] = dates_list

            # Fetch trajectory data for all selected objects including planets with shells
            positions_over_time = {}
            for obj in objects:
                if obj['var'].get() == 1 and obj['name'] != center_object_name:
                    # Check if this is a moon of the center object
                    is_satellite = center_object_name in parent_planets and obj['name'] in parent_planets.get(center_object_name, [])

                    if 'start_date' in obj or 'end_date' in obj:
                        # Get start/end dates with fallbacks
                        start_date = obj.get('start_date', dates_list[0])
                        end_date = obj.get('end_date', dates_list[-1])

                        positions_over_time[obj['name']] = pad_trajectory(
                            dates_list, 
                            start_date,
                            end_date,
                            obj['id'], 
                            center_id, 
                            obj.get('id_type')
                        )
                    # For objects without specific date ranges, use our custom date lists
                    elif obj['name'] in dates_lists:
                        obj_dates = dates_lists[obj['name']]
                        if obj_dates:  # Only fetch if we have dates
                            positions_over_time[obj['name']] = fetch_trajectory(
                                obj['id'], 
                                obj_dates, 
                                center_id=center_id, 
                                id_type=obj.get('id_type')
                            )
                    else:
                        positions_over_time[obj['name']] = fetch_trajectory(
                            obj['id'], 
                            dates_list, 
                            center_id=center_id, 
                            id_type=obj.get('id_type')
                        )
            
            # Add position data for center planet if it has shells
            if center_object_name in planets_with_shells:
                # Create a list of positions at (0,0,0) for all frames
                center_positions = []
                for i in range(N):
                    center_positions.append({
                        'x': 0, 'y': 0, 'z': 0,
                        'date': dates_list[i]
                    })
                positions_over_time[center_object_name] = center_positions

            # Initialize figure
            fig = go.Figure()

            # Plot actual orbits using the dates_lists we just created
            selected_planets = [obj['name'] for obj in objects if obj['var'].get() == 1 and obj['name'] != center_object_name]
            plot_actual_orbits(fig, selected_planets, dates_lists, center_id=center_id, show_lines=True)

            # Define dictionary mapping planets to their shell variable dictionaries
            planet_shells_config = {
                'Mercury': mercury_shell_vars,
                'Venus': venus_shell_vars,
                'Earth': earth_shell_vars,
                'Moon': moon_shell_vars,
                'Mars': mars_shell_vars,
                'Jupiter': jupiter_shell_vars,
                'Saturn': saturn_shell_vars,
                'Uranus': uranus_shell_vars,
                'Neptune': neptune_shell_vars,
                'Pluto': pluto_shell_vars,
                'Eris/Dysnomia': eris_shell_vars,
                'Planet 9': planet9_shell_vars,              
                # Add more planets here as shell systems are developed
            }

            # Get shell traces for center object (if applicable) but don't add them to the figure yet
            shell_traces = []
            center_has_shells = False

            # Use the unified create_celestial_body_visualization function for animations
            if center_object_name in body_shells_config:
                shell_vars = body_shells_config[center_object_name]
                if any(var.get() == 1 for var in shell_vars.values()):
                    print(f"Using unified visualization function for {center_object_name} animation")
                    fig = create_celestial_body_visualization(fig, center_object_name, shell_vars, animate=True, frames=frames)
                    # We don't add a center marker because shells are displayed
                else:
                    # Add center marker since no shells are active
                    if center_object_name == 'Sun':
                        # Add the Sun marker
                        fig.add_trace(
                            go.Scatter3d(
                                x=[0], y=[0], z=[0],
                                mode='markers',
                                marker=dict(
                                    color='rgb(102, 187, 106)',      # chlorophyll green  
                                    size=12,
                                    symbol=center_object_info['symbol']
                                ),
                                name="Sun",
                                text=[hover_text_sun],
                                customdata=["Sun"],
                                hovertemplate='%{text}<extra></extra>',
                                showlegend=True
                            )
                        )
                    else:
                        # For non-Sun centers with no shells, add the center marker trace
                        fig.add_trace(
                            go.Scatter3d(
                                x=[0], y=[0], z=[0],
                                mode='markers',
                                marker=dict(
                                    color=center_object_info['color'],
                                    size=12,
                                    symbol=center_object_info['symbol']
                                ),
                                name=f"{center_object_name}",
                                text=[f"<b>{center_object_name}</b><br>Center of the current view"],
                                customdata=[f"<b>{center_object_name}</b>"],
                                hovertemplate='%{text}<extra></extra>',
                                showlegend=True
                            )
                        )
            else:
                # For center objects without shell configurations, always add the marker
            
                # Add the center object marker
                if center_object_name == 'Sun':
                    # Add the Sun marker
                    fig.add_trace(
                        go.Scatter3d(
                            x=[0], y=[0], z=[0],
                            mode='markers',
                            marker=dict(
                                color='rgb(102, 187, 106)',      # chlorophyll green  
                                size=12,
                                symbol=center_object_info['symbol']
                            ),
                            name="Sun",
                            text=[hover_text_sun],
                            customdata=["Sun"],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )
                else:
                    # For non-Sun centers (planets), add a marker at the center
                    fig.add_trace(
                        go.Scatter3d(
                            x=[0], y=[0], z=[0],
                            mode='markers',
                            marker=dict(
                                color=center_object_info['color'],
                                size=12,
                                symbol=center_object_info['symbol']
                            ),
                            name=f"{center_object_name}",
                            text=[f"<b>{center_object_name}</b><br>Center of the current view"],
                            customdata=[f"<b>{center_object_name}</b>"],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )

            # Add idealized orbits for selected objects
            selected_objects = [
                obj['name']
                for obj in objects
                if obj['var'].get() == 1
            ]
            
            plot_idealized_orbits(fig, selected_objects, center_id=center_object_name, 
                          objects=objects, planetary_params=planetary_params,
                          parent_planets=parent_planets, color_map=color_map,
                          date=dates_list[0] if dates_list else datetime.now())  # Use first animation date)            

            # Create initial traces for moving objects and store their indices
            trace_indices = {}  # Define trace_indices dictionary
            
            for obj in objects:
                if obj['var'].get() == 1 and obj['name'] != center_object_name:
                    obj_name = obj['name']
                    obj_positions = positions_over_time.get(obj_name)
                    
                    if obj_positions and len(obj_positions) > 0 and obj_positions[0] is not None and 'x' in obj_positions[0]:
                        obj_data = obj_positions[0]
                        
                        # Use format_detailed_hover_text
                        full_hover_text, minimal_hover_text, satellite_note = format_detailed_hover_text(
                            obj_data, 
                            obj_name, 
                            center_object_name,
                            objects,
                            planetary_params,
                            parent_planets,
                            CENTER_BODY_RADII,
                            KM_PER_AU,
                            LIGHT_MINUTES_PER_AU,
                            KNOWN_ORBITAL_PERIODS
                        )
                        
                        # Add satellite note if present
                        if satellite_note:
                            full_hover_text += satellite_note

                        trace = go.Scatter3d(
                            x=[obj_data['x']],
                            y=[obj_data['y']],
                            z=[obj_data['z']],
                            mode='markers',
                            marker=dict(symbol=obj['symbol'], color=obj['color'], size=6),
                            name=obj_name,
                            text=[full_hover_text],
                            customdata=[minimal_hover_text],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                        fig.add_trace(trace)
                        trace_indices[obj_name] = len(fig.data) - 1
                    else:
                        # If no initial position, still create a trace for the legend
                        trace = go.Scatter3d(
                            x=[None], y=[None], z=[None],
                            mode='markers',
                            marker=dict(symbol=obj['symbol'], color=obj['color'], size=6),
                            name=obj_name,
                            text=[obj_name],
                            customdata=[obj_name],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                        fig.add_trace(trace)
                        trace_indices[obj_name] = len(fig.data) - 1

            # First, make sure initial base traces show the first valid position
            for obj in objects:
                if obj['var'].get() == 1 and obj['name'] != center_object_name:
                    obj_name = obj['name']
                    
                    if obj_name in positions_over_time and obj_name in trace_indices:
                        trace_idx = trace_indices[obj_name]
                        obj_positions = positions_over_time[obj_name]
                        
                        # Try to find the first valid position
                        first_valid_pos = None
                        for pos in obj_positions:
                            if pos is not None and 'x' in pos:
                                first_valid_pos = pos
                                break
                        
                        if first_valid_pos:
                            # Use format_detailed_hover_text for first valid position
                            full_hover_text, minimal_hover_text, satellite_note = format_detailed_hover_text(
                                first_valid_pos, 
                                obj_name, 
                                center_object_name,
                                objects,
                                planetary_params,
                                parent_planets,
                                CENTER_BODY_RADII,
                                KM_PER_AU,
                                LIGHT_MINUTES_PER_AU,
                                KNOWN_ORBITAL_PERIODS
                            )
                            
                            # Add satellite note if present
                            if satellite_note:
                                full_hover_text += satellite_note
                            
                            # Update the trace with first valid position data
                            fig.data[trace_idx].x = [first_valid_pos['x']]
                            fig.data[trace_idx].y = [first_valid_pos['y']]
                            fig.data[trace_idx].z = [first_valid_pos['z']]
                            fig.data[trace_idx].text = [full_hover_text]
                            fig.data[trace_idx].customdata = [minimal_hover_text]
                            fig.data[trace_idx].visible = True

            # Create frames - using the base traces approach
            for i in range(N):
                frame_data = list(fig.data)  # Start with all base traces
                current_date = dates_list[i]
                
                # Update position traces for selected objects
                for obj in objects:
                    if obj['var'].get() == 1 and obj['name'] != center_object_name:
                        obj_name = obj['name']
                        
                        if obj_name in positions_over_time and obj_name in trace_indices:
                            trace_idx = trace_indices[obj_name]
                            obj_positions = positions_over_time[obj_name]
                            
                            if i < len(obj_positions) and obj_positions[i] is not None and 'x' in obj_positions[i]:
                                obj_data = obj_positions[i]

                                # Use format_detailed_hover_text
                                full_hover_text, minimal_hover_text, satellite_note = format_detailed_hover_text(
                                    obj_data, 
                                    obj_name, 
                                    center_object_name,
                                    objects,
                                    planetary_params,
                                    parent_planets,
                                    CENTER_BODY_RADII,
                                    KM_PER_AU,
                                    LIGHT_MINUTES_PER_AU,
                                    KNOWN_ORBITAL_PERIODS
                                )
                                
                                # Add satellite note if present
                                if satellite_note:
                                    full_hover_text += satellite_note

                                # Update the trace with new position data
                                frame_data[trace_idx].x = [obj_data['x']]
                                frame_data[trace_idx].y = [obj_data['y']]
                                frame_data[trace_idx].z = [obj_data['z']]
                                frame_data[trace_idx].text = [full_hover_text]
                                frame_data[trace_idx].customdata = [minimal_hover_text]
                                frame_data[trace_idx].visible = True
                            else:
                                # If position is missing for this frame, make the object invisible
                                frame_data[trace_idx].visible = False

                frames.append(go.Frame(
                    data=frame_data,
                    name=str(dates_list[i].strftime('%Y-%m-%d %H:%M'))
                ))

            # Calculate axis ranges
            x_coords = []
            y_coords = []
            z_coords = []

            # Collect coordinates from all positions for all objects
            for obj_name, positions in positions_over_time.items():
                for pos in positions:
                    if pos and pos.get('x') is not None:
                        x_coords.append(pos['x'])
                        y_coords.append(pos['y'])
                        z_coords.append(pos['z'])

            # Calculate range with padding
            if x_coords and y_coords and z_coords:
                max_coord = max(
                    abs(max(x_coords)), abs(min(x_coords)),
                    abs(max(y_coords)), abs(min(y_coords)),
                    abs(max(z_coords)), abs(min(z_coords))
                )
                # Add 20% padding
                max_coord *= 1.2
                axis_range = [-max_coord, max_coord]
            else:
                # Default range if no coordinates available
                axis_range = [-1, 1]

            # Check for manual scale override
            if scale_var.get() == 'Manual':
                try:
                    custom_scale = float(custom_scale_entry.get())
                    if custom_scale > 0:
                        axis_range = [-custom_scale, custom_scale]
                except ValueError:
                    pass  # Keep calculated range if custom scale is invalid
                    
            # For Jupiter-centered view, adjust scale if not manually set
            if center_object_name == 'Jupiter' and scale_var.get() == 'Auto':
                # Default to a scale that shows Galilean moons well
                # Jupiter's most distant major moon (Callisto) orbits at ~0.0126 AU
                # Add 50% padding for good visualization
                axis_range = [-0.02, 0.02]

            # Update layout with dynamic scaling
            fig.update_layout(
                scene=dict(
                    xaxis=dict(title='X (AU)', range=axis_range, 
                            backgroundcolor='black', gridcolor='gray', 
                            showbackground=True, showgrid=True),
                    yaxis=dict(title='Y (AU)', range=axis_range, 
                            backgroundcolor='black', gridcolor='gray', 
                            showbackground=True, showgrid=True),
                    zaxis=dict(title='Z (AU)', range=axis_range, 
                            backgroundcolor='black', gridcolor='gray', 
                            showbackground=True, showgrid=True),
                    aspectmode='cube',
                    camera=get_default_camera()
                ),
            
                paper_bgcolor='black',
                plot_bgcolor='black',
                title_font_color='white',
                font_color='white',
                title="Paloma's Orrery - Animation Over Below Dates",
                showlegend=True,
                legend=dict(
                    font=dict(color='white'),
                    x=1,
                    y=1,
                    xanchor='left',
                    yanchor='top'
                ),
                annotations=[
                    dict(
                        text="Search: <a href='https://www.nasa.gov/' target='_blank'>NASA</a>",
                        xref='paper',
                        yref='paper',
                        x=0,
                        y=0.35,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                    dict(
                        text="Data source: <a href='https://ssd.jpl.nasa.gov/horizons/app.html#/' target='_blank'>JPL Horizons</a>",
                        xref='paper',
                        yref='paper',
                        x=0,
                        y=0.3,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                    dict(
                        text="Click on the legend items <br>to toggle them off or back on:",
                        xref='paper',
                        yref='paper',
                        x=0.95,
                        y=1.07,
                        showarrow=False,
                        font=dict(size=12, color='white'),
                        align='left',
                        xanchor='left',
                        yanchor='top'
                    ),
                ],
                updatemenus=[
                    dict(
                        type='buttons',
                        showactive=False,
                        buttons=[
                            dict(label='Play  ',
                                method='animate',
                                args=[None, {'frame': {'duration': 500, 'redraw': True},
                                        'fromcurrent': True,
                                        'transition': {'duration': 0}}]),
                            dict(label='Pause',
                                method='animate',
                                args=[[None], {'frame': {'duration': 0},
                                                'mode': 'immediate',
                                                'transition': {'duration': 0}}])
                        ],
                        x=0.1,
                        y=0.85
                    )
                ]
            )

            # Add sliders for date navigation
            sliders = [dict(
                active=0,
                steps=[dict(method='animate',
                            args=[[str(dates_list[k].strftime('%Y-%m-%d %H:%M'))],
                                {'frame': {'duration': 500, 'redraw': True},
                                'mode': 'immediate'}],
                            label=dates_list[k].strftime('%Y-%m-%d %H:%M')) for k in range(N)],
                transition=dict(duration=0),
                x=0,
                y=0,
                currentvalue=dict(font=dict(size=14), prefix='Date: ', visible=True, xanchor='center'),
                len=1.0
            )]

            # First, assign frames to the figure
            fig.frames = frames

            # Then update layout with sliders
            fig.update_layout(sliders=sliders)

            # Now set the initial slider position (outside try/except)
            fig.layout.sliders[0].active = 0

            # Explicitly sync the displayed data with the first frame's data
            for obj_name, trace_idx in trace_indices.items():
                if trace_idx < len(fig.data) and 0 < len(frames) and trace_idx < len(frames[0].data):
                    fig.data[trace_idx].x = frames[0].data[trace_idx].x
                    fig.data[trace_idx].y = frames[0].data[trace_idx].y
                    fig.data[trace_idx].z = frames[0].data[trace_idx].z
                    fig.data[trace_idx].text = frames[0].data[trace_idx].text
                    fig.data[trace_idx].customdata = frames[0].data[trace_idx].customdata
                    fig.data[trace_idx].visible = frames[0].data[trace_idx].visible

            # Add hover toggle buttons
            fig = add_hover_toggle_buttons(fig)

            # Add URL buttons before showing/saving
            fig = add_url_buttons(fig, objects, selected_objects)            

            # Generate default name with timestamp
            current_date = STATIC_TODAY
            default_name = f"{center_object_name}_system_animation_{current_date.strftime('%Y%m%d_%H%M')}"
            show_animation_safely(fig, default_name)

            # Update output_label with instructions
            output_label.config(
                text=f"Animation of objects around {center_object_name} opened in browser."
            )
            progress_bar.stop()

        except Exception as e:
            output_label.config(text=f"Error during animation: {e}")
            print(f"Error during animation: {e}")
            traceback.print_exc()
            progress_bar.stop()

    # Create and start monitored thread
    animation_thread = create_monitored_thread(shutdown_handler, animation_worker)
    animation_thread.start()

"""
def on_closing():
#    Handle cleanup when the main window is closed.
    try:
        # Attempt to remove any temporary files
        temp_files = ["palomas_orrery.html", "palomas_orrery_animation.html"]
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
    finally:
        root.destroy()
"""

def on_closing():
    """Handle cleanup when the main window is closed."""
    try:
        # Clean up temp cache
        if os.path.exists(TEMP_CACHE_FILE):
            os.remove(TEMP_CACHE_FILE)
            print("[CLEANUP] Temporary cache file removed")
        
        # Existing cleanup code...
        temp_files = ["palomas_orrery.html", "palomas_orrery_animation.html"]
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
    finally:
        root.destroy()

# Add the closing protocol to the root window
root.protocol("WM_DELETE_WINDOW", on_closing)

"""
# Function to fill today's date into the entry fields
def fill_now():
    now = datetime.now()
    update_date_fields(now)
"""

def fill_now():
    now = datetime.now()
    update_date_fields(now)
    update_offset_date_displays()  # Add this line

# Function to set Paloma's Birthday
def set_palomas_birthday():
    update_date_fields(datetime(2005, 2, 4, 1))

# Function to update date fields
def update_date_fields(new_date):
    entry_year.delete(0, tk.END)
    entry_year.insert(0, new_date.year)
    entry_month.delete(0, tk.END)
    entry_month.insert(0, new_date.month)
    entry_day.delete(0, tk.END)
    entry_day.insert(0, new_date.day)
    entry_hour.delete(0, tk.END)
    entry_hour.insert(0, new_date.hour)
    entry_minute.delete(0, tk.END)
    entry_minute.insert(0, new_date.minute)

def toggle_all_shells():
    """Toggle all sun shell checkboxes based on the main shell checkbox."""
    state = sun_shells_var.get()
    sun_core_var.set(state)
    sun_radiative_var.set(state)
    sun_photosphere_var.set(state)
    sun_chromosphere_var.set(state)
    sun_inner_corona_var.set(state)
    sun_outer_corona_var.set(state)
    sun_termination_shock_var.set(state)
    sun_heliopause_var.set(state)

    sun_inner_oort_limit_var.set(state)
    sun_inner_oort_var.set(state)
    sun_outer_oort_var.set(state)

    sun_hills_cloud_torus_var.set(state) 
    sun_outer_oort_clumpy_var.set(state)           
    sun_galactic_tide_var.set(state)              
    sun_gravitational_var.set(state)

# Function to handle mission selection (no longer adjusts date)
def handle_mission_selection():
    # Function no longer adjusts the date based on mission selection
    pass

# Animation Functions

def animate_one_minute():
    # Update status before calling animate_objects
    output_label.config(text="Preparing minute-by-minute animation. Please wait...")
    root.update_idletasks()  # Force GUI to update
    animate_objects(timedelta(minutes=1), "Minute") 

def animate_one_hour():
    output_label.config(text="Preparing hour-by-hour animation. Please wait...")
    root.update_idletasks()
    animate_objects(timedelta(hours=1), "Hour") 

def animate_one_day():
    output_label.config(text="Preparing day-by-day animation. Please wait...")
    root.update_idletasks()
    animate_objects(timedelta(days=1), "Day") 

 # Add the new animate_one_week function
def animate_one_week():
    output_label.config(text="Preparing week-by-week animation. Please wait...")
    root.update_idletasks()
    animate_objects(timedelta(weeks=1), "Week")            

def animate_one_month():
    output_label.config(text="Preparing month-by-month animation. Please wait...")
    root.update_idletasks()
    animate_objects('month', "Month")

def animate_one_year():
    output_label.config(text="Preparing year-by-year animation. Please wait...")
    root.update_idletasks()
    animate_objects('year', "Year")

def animate_palomas_birthday():
    # Set Paloma's birthday in the date fields
    set_palomas_birthday()
    
    # Define Paloma's birth date
    paloma_birthday = datetime(2005, 2, 4, 1, 0, 0)  # February 4, 2005 at 01:00
    
    # Get the current date
    current_date = datetime.today()
    
    # Calculate Paloma's age
    age = current_date.year - paloma_birthday.year - ((current_date.month, current_date.day) < (paloma_birthday.month, paloma_birthday.day))
    
    # Set the number of frames to Paloma's age plus one
    num_frames = age + 1
    num_frames_entry.delete(0, tk.END)  # Clear existing value
    num_frames_entry.insert(0, str(num_frames))  # Insert new value
    
    # Optionally, update the hour to 0 for consistency
    entry_hour.delete(0, tk.END)
    entry_hour.insert(0, '0')
    
    # Call the animate_objects function with 'year' step
    animate_objects('year', "Year")  

# Get the script's saved date for version control
script_saved_date = datetime.now().strftime("%Y-%m-%d")

# Exception handling for Tkinter
# def report_callback_exception(self, exc, val, tb):
def report_callback_exception(self, exc_type, exc_value, exc_traceback):
    print('Exception in Tkinter callback')
    traceback.print_exception(exc_type, exc_value, exc_traceback)

root.report_callback_exception = report_callback_exception

# Configure grid weights for responsive design
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create a separate frame for date fields and the "Now" button
date_frame = tk.Frame(input_frame)
date_frame.grid(row=0, column=0, columnspan=9, padx=(0, 0), pady=2, sticky='w')

# Define date labels and entries with reduced padding
label_year = tk.Label(date_frame, text="Date(UTC) Year:")
label_year.grid(row=0, column=0, padx=(0, 5), pady=2, sticky='e')

entry_year = tk.Entry(date_frame, width=5)
entry_year.grid(row=0, column=1, padx=(0, 5), pady=2, sticky='w')
entry_year.insert(0, today.year)

label_month = tk.Label(date_frame, text="Month:")
label_month.grid(row=0, column=2, padx=(0, 5), pady=2, sticky='e')

entry_month = tk.Entry(date_frame, width=5)
entry_month.grid(row=0, column=3, padx=(0, 5), pady=2, sticky='w')
entry_month.insert(0, today.month)

label_day = tk.Label(date_frame, text="Day:")
label_day.grid(row=0, column=4, padx=(0, 5), pady=2, sticky='e')

entry_day = tk.Entry(date_frame, width=5)
entry_day.grid(row=0, column=5, padx=(0, 5), pady=2, sticky='w')
entry_day.insert(0, today.day)

label_hour = tk.Label(date_frame, text="Hour:")
label_hour.grid(row=0, column=6, padx=(0, 5), pady=2, sticky='e')

entry_hour = tk.Entry(date_frame, width=5)
entry_hour.grid(row=0, column=7, padx=(0, 5), pady=2, sticky='w')
entry_hour.insert(0, '0')

label_minute = tk.Label(date_frame, text="Minute:")
label_minute.grid(row=0, column=8, padx=(0, 5), pady=2, sticky='e')

entry_minute = tk.Entry(date_frame, width=5)
entry_minute.grid(row=0, column=9, padx=(0, 5), pady=2, sticky='w')
entry_minute.insert(0, '0')  # Default to 0 minutes

# "Now" button with minimal padding
now_button = tk.Button(date_frame, text="Now", command=fill_now)
now_button.grid(row=0, column=10, padx=(2, 0), pady=2, sticky='w')
CreateToolTip(now_button, "Fill the current date and time")

# Tooltip for scrollable frame
CreateToolTip(scrollable_frame.scrollable_frame, "Use the scrollbar to see all objects. Categories include:\n" 
              "- Planets and Dwarf Planets;\n- Moons, Asteroids, and Kuiper Belt Objects;\n- Space Missions;\n" 
              "- Comets and Interstellar Objects!\n"
              "Select a start date for plotting. The default start date is \'Now\'.")

# Define selection variables for each object
celestial_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Solar Shells, Planets, Dwarf Planets, Moons, Asteroids, " 
                                "Kuiper Belt Objects")
celestial_frame.pack(pady=(10, 5), fill='x')
CreateToolTip(celestial_frame, "Select celestial bodies for plotting. Selected objects will be plotted on the entered date, as well " 
              "as actual and ideal orbits. Selected objects will be animated only over the fetched dates, and will plot both actual and " 
              "ideal orbits.")

def create_celestial_checkbutton(name, variable):
    # For main planets and Sun, make a bold label
    if name in ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Eris', 'Planet 9']:
        # Create frame to hold checkbox and label
        frame = tk.Frame(celestial_frame)
        frame.pack(anchor='w')
        
        # Create checkbox without text
        checkbutton = tk.Checkbutton(frame, text='', variable=variable)
        checkbutton.pack(side='left')
        
        # Create bold label
        label = tk.Label(frame, text=name, font=("Arial", 10, "bold"))
        label.pack(side='left')
        
        # Add tooltip to the frame
        info_text = INFO.get(name.strip('- '), "No information available")
        CreateToolTip(frame, info_text)
    else:
        # Regular checkbutton for other objects
        checkbutton = tk.Checkbutton(celestial_frame, text=name, variable=variable)
        checkbutton.pack(anchor='w')
        info_text = INFO.get(name.strip('- '), "No information available")
        CreateToolTip(checkbutton, info_text)

# Existing celestial checkbuttons
create_celestial_checkbutton("Sun", sun_var)
# create_celestial_checkbutton("- Solar Shells", sun_shells_var)

# After the "- Solar Shells" checkbutton
# First, modify the existing Solar Shells checkbutton to call toggle_all_shells
sun_shells_checkbutton = tk.Checkbutton(celestial_frame, text="- Solar Shells (All)", variable=sun_shells_var, command=toggle_all_shells)
sun_shells_checkbutton.pack(anchor='w')
CreateToolTip(sun_shells_checkbutton, "Toggle all Sun shells on/off")

# Create a Frame specifically for the shell options (indented)
shell_options_frame = tk.Frame(celestial_frame)
shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# Add individual shell checkbuttons in the indented frame
sun_core_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Core", variable=sun_core_var)
sun_core_checkbutton.pack(anchor='w')
CreateToolTip(sun_core_checkbutton, core_info)

sun_radiative_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Radiative Zone", variable=sun_radiative_var)
sun_radiative_checkbutton.pack(anchor='w')
CreateToolTip(sun_radiative_checkbutton, radiative_zone_info)

sun_photosphere_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Photosphere", variable=sun_photosphere_var)
sun_photosphere_checkbutton.pack(anchor='w')
CreateToolTip(sun_photosphere_checkbutton, photosphere_info)

sun_chromosphere_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Chromosphere", variable=sun_chromosphere_var)
sun_chromosphere_checkbutton.pack(anchor='w')
CreateToolTip(sun_chromosphere_checkbutton, chromosphere_info)

sun_inner_corona_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Inner Corona", variable=sun_inner_corona_var)
sun_inner_corona_checkbutton.pack(anchor='w')
CreateToolTip(sun_inner_corona_checkbutton, inner_corona_info)

sun_outer_corona_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Outer Corona", variable=sun_outer_corona_var)
sun_outer_corona_checkbutton.pack(anchor='w')
CreateToolTip(sun_outer_corona_checkbutton, outer_corona_info)

sun_termination_shock_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Termination Shock", variable=sun_termination_shock_var)
sun_termination_shock_checkbutton.pack(anchor='w')
CreateToolTip(sun_termination_shock_checkbutton, termination_shock_info)

sun_heliopause_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Heliopause", variable=sun_heliopause_var)
sun_heliopause_checkbutton.pack(anchor='w')
CreateToolTip(sun_heliopause_checkbutton, solar_wind_info)

sun_inner_oort_limit_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Inner Limit of Oort Cloud", variable=sun_inner_oort_limit_var)
sun_inner_oort_limit_checkbutton.pack(anchor='w')
CreateToolTip(sun_inner_oort_limit_checkbutton, inner_limit_oort_info)

sun_hills_cloud_torus_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Hills Cloud Torus", variable=sun_hills_cloud_torus_var)
sun_hills_cloud_torus_checkbutton.pack(anchor='w')
CreateToolTip(sun_hills_cloud_torus_checkbutton, hills_cloud_torus_info)

sun_inner_oort_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Inner Oort Cloud", variable=sun_inner_oort_var)
sun_inner_oort_checkbutton.pack(anchor='w')
CreateToolTip(sun_inner_oort_checkbutton, inner_oort_info)

sun_outer_oort_clumpy_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Clumpy Oort Cloud", variable=sun_outer_oort_clumpy_var)
sun_outer_oort_clumpy_checkbutton.pack(anchor='w')
CreateToolTip(sun_outer_oort_clumpy_checkbutton, outer_oort_clumpy_info)

sun_galactic_tide_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Galactic Tide Influence Oort", variable=sun_galactic_tide_var)
sun_galactic_tide_checkbutton.pack(anchor='w')
CreateToolTip(sun_galactic_tide_checkbutton, galactic_tide_info)

sun_outer_oort_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Outer Oort Cloud", variable=sun_outer_oort_var)
sun_outer_oort_checkbutton.pack(anchor='w')
CreateToolTip(sun_outer_oort_checkbutton, outer_oort_info)

sun_gravitational_checkbutton = tk.Checkbutton(shell_options_frame, text="-- Gravitational Influence", variable=sun_gravitational_var)
sun_gravitational_checkbutton.pack(anchor='w')
CreateToolTip(sun_gravitational_checkbutton, gravitational_influence_info)

# inner planets
create_celestial_checkbutton("Mercury", mercury_var)
# Create a Frame specifically for the mercury shell options (indented)
mercury_shell_options_frame = tk.Frame(celestial_frame)
mercury_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# mercury inner core shell
mercury_inner_core_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Inner Core", variable=mercury_inner_core_var)
mercury_inner_core_checkbutton.pack(anchor='w')
CreateToolTip(mercury_inner_core_checkbutton, mercury_inner_core_info)
# mercury outer core shell
mercury_outer_core_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Outer Core", variable=mercury_outer_core_var)
mercury_outer_core_checkbutton.pack(anchor='w')
CreateToolTip(mercury_outer_core_checkbutton, mercury_outer_core_info)
# mercury lower mantle shell
mercury_mantle_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Mantle", variable=mercury_mantle_var)
mercury_mantle_checkbutton.pack(anchor='w')
CreateToolTip(mercury_mantle_checkbutton, mercury_mantle_info)
# mercury crust shell
mercury_crust_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Crust", variable=mercury_crust_var)
mercury_crust_checkbutton.pack(anchor='w')
CreateToolTip(mercury_crust_checkbutton, mercury_crust_info)
# mercury atmosphere shell
mercury_atmosphere_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Exosphere", variable=mercury_atmosphere_var)
mercury_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(mercury_atmosphere_checkbutton, mercury_atmosphere_info)
# mercury magnetosphere shell
mercury_magnetosphere_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Magnetosphere", variable=mercury_magnetosphere_var)
mercury_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(mercury_magnetosphere_checkbutton, mercury_magnetosphere_info)
# mercury hill sphere shell
mercury_hill_sphere_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Hill Sphere", variable=mercury_hill_sphere_var)
mercury_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(mercury_hill_sphere_checkbutton, mercury_hill_sphere_info)

create_celestial_checkbutton("Venus", venus_var)
# Create a Frame specifically for the venus shell options (indented)
venus_shell_options_frame = tk.Frame(celestial_frame)
venus_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# venus core shell
venus_core_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Core", variable=venus_core_var)
venus_core_checkbutton.pack(anchor='w')
CreateToolTip(venus_core_checkbutton, venus_core_info)
# venus mantle shell
venus_mantle_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Mantle", variable=venus_mantle_var)
venus_mantle_checkbutton.pack(anchor='w')
CreateToolTip(venus_mantle_checkbutton, venus_mantle_info)
# venus crust shell
venus_crust_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Crust", variable=venus_crust_var)
venus_crust_checkbutton.pack(anchor='w')
CreateToolTip(venus_crust_checkbutton, venus_crust_info)
# venus atmosphere shell
venus_atmosphere_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Atmosphere", variable=venus_atmosphere_var)
venus_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(venus_atmosphere_checkbutton, venus_atmosphere_info)
# venus upper atmosphere shell
venus_upper_atmosphere_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Upper Atmosphere", variable=venus_upper_atmosphere_var)
venus_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(venus_upper_atmosphere_checkbutton, venus_upper_atmosphere_info)
# venus magnetosphere shell
venus_magnetosphere_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Magnetosphere", variable=venus_magnetosphere_var)
venus_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(venus_magnetosphere_checkbutton, venus_magnetosphere_info)
# venus hill sphere shell
venus_hill_sphere_checkbutton = tk.Checkbutton(venus_shell_options_frame, text="-- Hill Sphere", variable=venus_hill_sphere_var)
venus_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(venus_hill_sphere_checkbutton, venus_hill_sphere_info)

create_celestial_checkbutton("Earth", earth_var)
# Create a Frame specifically for the Earth shell options (indented)
earth_shell_options_frame = tk.Frame(celestial_frame)
earth_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# Earth inner core shell
earth_inner_core_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Inner Core", variable=earth_inner_core_var)
earth_inner_core_checkbutton.pack(anchor='w')
CreateToolTip(earth_inner_core_checkbutton, earth_inner_core_info)
# Earth outer core shell
earth_outer_core_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Outer Core", variable=earth_outer_core_var)
earth_outer_core_checkbutton.pack(anchor='w')
CreateToolTip(earth_outer_core_checkbutton, earth_outer_core_info)
# Earth lower mantle shell
earth_lower_mantle_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Lower Mantle", variable=earth_lower_mantle_var)
earth_lower_mantle_checkbutton.pack(anchor='w')
CreateToolTip(earth_lower_mantle_checkbutton, earth_lower_mantle_info)
# Earth upper mantle shell
earth_upper_mantle_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Upper Mantle", variable=earth_upper_mantle_var)
earth_upper_mantle_checkbutton.pack(anchor='w')
CreateToolTip(earth_upper_mantle_checkbutton, earth_upper_mantle_info)
# Earth crust shell
earth_crust_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Crust", variable=earth_crust_var)
earth_crust_checkbutton.pack(anchor='w')
CreateToolTip(earth_crust_checkbutton, earth_crust_info)
# Earth atmosphere shell
earth_atmosphere_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Atmosphere", variable=earth_atmosphere_var)
earth_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(earth_atmosphere_checkbutton, earth_atmosphere_info)
# Earth upper atmosphere shell
earth_upper_atmosphere_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Upper Atmosphere", variable=earth_upper_atmosphere_var)
earth_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(earth_upper_atmosphere_checkbutton, earth_upper_atmosphere_info)
# Earth magnetosphere shell
earth_magnetosphere_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Magnetosphere", variable=earth_magnetosphere_var)
earth_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(earth_magnetosphere_checkbutton, earth_magnetosphere_info)
# Earth hill sphere shell
earth_hill_sphere_checkbutton = tk.Checkbutton(earth_shell_options_frame, text="-- Hill Sphere", variable=earth_hill_sphere_var)
earth_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(earth_hill_sphere_checkbutton, earth_hill_sphere_info)

create_celestial_checkbutton("Moon", moon_var)
# Create a Frame specifically for the moon shell options (indented)
moon_shell_options_frame = tk.Frame(celestial_frame)
moon_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# moon inner core shell
moon_inner_core_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Inner Core", variable=moon_inner_core_var)
moon_inner_core_checkbutton.pack(anchor='w')
CreateToolTip(moon_inner_core_checkbutton, moon_inner_core_info)
# moon outer core shell
moon_outer_core_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Outer Core", variable=moon_outer_core_var)
moon_outer_core_checkbutton.pack(anchor='w')
CreateToolTip(moon_outer_core_checkbutton, moon_outer_core_info)
# moon mantle shell
moon_mantle_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Mantle", variable=moon_mantle_var)
moon_mantle_checkbutton.pack(anchor='w')
CreateToolTip(moon_mantle_checkbutton, moon_mantle_info)
# moon crust shell
moon_crust_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Crust", variable=moon_crust_var)
moon_crust_checkbutton.pack(anchor='w')
CreateToolTip(moon_crust_checkbutton, moon_crust_info)
# moon exosphere shell
moon_exosphere_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Exosphere", variable=moon_exosphere_var)
moon_exosphere_checkbutton.pack(anchor='w')
CreateToolTip(moon_exosphere_checkbutton, moon_exosphere_info)
# moon hill sphere shell
moon_hill_sphere_checkbutton = tk.Checkbutton(moon_shell_options_frame, text="-- Hill Sphere", variable=moon_hill_sphere_var)
moon_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(moon_hill_sphere_checkbutton, moon_hill_sphere_info)

create_celestial_checkbutton("- 2024 PT5", pt5_var)
create_celestial_checkbutton("- 2024 DW", asteroid_dw_var)
create_celestial_checkbutton("- 2024 YR4", yr4_var)

create_celestial_checkbutton("Mars", mars_var)
# Create a Frame specifically for the Mars shell options (indented)
mars_shell_options_frame = tk.Frame(celestial_frame)
mars_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# Mars inner core shell
mars_inner_core_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Inner Core", variable=mars_inner_core_var)
mars_inner_core_checkbutton.pack(anchor='w')
CreateToolTip(mars_inner_core_checkbutton, mars_inner_core_info)
# Mars outer core shell
mars_outer_core_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Outer Core", variable=mars_outer_core_var)
mars_outer_core_checkbutton.pack(anchor='w')
CreateToolTip(mars_outer_core_checkbutton, mars_outer_core_info)
# Mars mantle shell
mars_mantle_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Mantle", variable=mars_mantle_var)
mars_mantle_checkbutton.pack(anchor='w')
CreateToolTip(mars_mantle_checkbutton, mars_mantle_info)
# mars crust shell
mars_crust_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Crust", variable=mars_crust_var)
mars_crust_checkbutton.pack(anchor='w')
CreateToolTip(mars_crust_checkbutton, mars_crust_info)
# mars atmosphere shell
mars_atmosphere_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Atmosphere", variable=mars_atmosphere_var)
mars_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(mars_atmosphere_checkbutton, mars_atmosphere_info)
# mars upper atmosphere shell
mars_upper_atmosphere_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Upper Atmosphere", variable=mars_upper_atmosphere_var)
mars_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(mars_upper_atmosphere_checkbutton, mars_upper_atmosphere_info)
# mars magnetosphere shell
mars_magnetosphere_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Magnetosphere", variable=mars_magnetosphere_var)
mars_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(mars_magnetosphere_checkbutton, mars_magnetosphere_info)
# mars hill sphere shell
mars_hill_sphere_checkbutton = tk.Checkbutton(mars_shell_options_frame, text="-- Hill Sphere", variable=mars_hill_sphere_var)
mars_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(mars_hill_sphere_checkbutton, mars_hill_sphere_info)
create_celestial_checkbutton("- Phobos", phobos_var)
create_celestial_checkbutton("- Deimos", deimos_var)

# asteroids
create_celestial_checkbutton("Apophis", apophis_var)
create_celestial_checkbutton("Bennu", bennu_var)
create_celestial_checkbutton("Ryugu", ryugu_var)
create_celestial_checkbutton("Itokawa", itokawa_var)
create_celestial_checkbutton("Eros", eros_var)
create_celestial_checkbutton("Dinkinesh", dinkinesh_var)
create_celestial_checkbutton("Vesta", vesta_var)
create_celestial_checkbutton("Šteins", steins_var)
create_celestial_checkbutton("Donaldjohanson", donaldjohanson_var)
create_celestial_checkbutton("Lutetia", lutetia_var)
create_celestial_checkbutton("Ceres", ceres_var)
create_celestial_checkbutton("Orus", orus_var)
create_celestial_checkbutton("Polymele", polymele_var)
create_celestial_checkbutton("Eurybates", eurybates_var)
create_celestial_checkbutton("Patroclus", patroclus_var)
create_celestial_checkbutton("Leucus", leucus_var)

# outer planets

create_celestial_checkbutton("Jupiter", jupiter_var)
# Create a Frame specifically for the Jupiter shell options (indented)
jupiter_shell_options_frame = tk.Frame(celestial_frame)
jupiter_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# Jupiter core shell
jupiter_core_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Core", variable=jupiter_core_var)
jupiter_core_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_core_checkbutton, jupiter_core_info)

# Jupiter metallic hydrogen shell
jupiter_metallic_hydrogen_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Metallic Hydrogen Layer", variable=jupiter_metallic_hydrogen_var)
jupiter_metallic_hydrogen_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_metallic_hydrogen_checkbutton, jupiter_metallic_hydrogen_info)

# Jupiter molecular hydrogen shell
jupiter_molecular_hydrogen_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Molecular Hydrogen Layer", variable=jupiter_molecular_hydrogen_var)
jupiter_molecular_hydrogen_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_molecular_hydrogen_checkbutton, jupiter_molecular_hydrogen_info)

# Jupiter cloud layer shell
jupiter_cloud_layer_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Cloud Layer", variable=jupiter_cloud_layer_var)
jupiter_cloud_layer_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_cloud_layer_checkbutton, jupiter_cloud_layer_info)

# Jupiter upper atmosphere shell
jupiter_upper_atmosphere_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Upper Atmosphere", variable=jupiter_upper_atmosphere_var)
jupiter_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_upper_atmosphere_checkbutton, jupiter_upper_atmosphere_info)

# Jupiter ring system shell
jupiter_ring_system_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Ring System", variable=jupiter_ring_system_var)
jupiter_ring_system_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_ring_system_checkbutton, jupiter_ring_system_info)

jupiter_radiation_belts_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Radiation Belts", variable=jupiter_radiation_belts_var)
jupiter_radiation_belts_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_radiation_belts_checkbutton, jupiter_radiation_belts_info)

jupiter_io_plasma_torus_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Io Plasma Torus", variable=jupiter_io_plasma_torus_var)
jupiter_io_plasma_torus_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_io_plasma_torus_checkbutton, jupiter_io_plasma_torus_info)

# Jupiter magnetosphere components
jupiter_magnetosphere_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Magnetosphere", variable=jupiter_magnetosphere_var)
jupiter_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_magnetosphere_checkbutton, jupiter_magnetosphere_info)

# Jupiter hill_sphere shell
jupiter_hill_sphere_checkbutton = tk.Checkbutton(jupiter_shell_options_frame, text="-- Hill Sphere", variable=jupiter_hill_sphere_var)
jupiter_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(jupiter_hill_sphere_checkbutton, jupiter_hill_sphere_info)              

create_celestial_checkbutton("- Metis", metis_var)      # 1.79 Jupiter radii, 128,000 km
create_celestial_checkbutton("- Adrastea", adrastea_var)  # 1.81 Jupiter radii, 129,000 km
create_celestial_checkbutton("- Amalthea", amalthea_var)  # 2.54 Jupiter radii, 182,000 km
create_celestial_checkbutton("- Thebe", thebe_var)        # 3.11 Jupiter radii, 226,000 km
create_celestial_checkbutton("- Io", io_var)              # 5.90 Jupiter radii, 422,000 km
create_celestial_checkbutton("- Europa", europa_var)      # 9.40 Jupiter radii, 671,000 km
create_celestial_checkbutton("- Ganymede", ganymede_var)  # 14.99 Jupiter radii, 1,070,000 km
create_celestial_checkbutton("- Callisto", callisto_var)  # 26.37 Jupiter radii, 1,883,000 km

create_celestial_checkbutton("Saturn", saturn_var)
# Create a Frame specifically for the saturn shell options (indented)
saturn_shell_options_frame = tk.Frame(celestial_frame)
saturn_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# saturn core shell
saturn_core_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Core", variable=saturn_core_var)
saturn_core_checkbutton.pack(anchor='w')
CreateToolTip(saturn_core_checkbutton, saturn_core_info)

# saturn metallic hydrogen shell
saturn_metallic_hydrogen_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Metallic Hydrogen Layer", variable=saturn_metallic_hydrogen_var)
saturn_metallic_hydrogen_checkbutton.pack(anchor='w')
CreateToolTip(saturn_metallic_hydrogen_checkbutton, saturn_metallic_hydrogen_info)

# saturn molecular hydrogen shell
saturn_molecular_hydrogen_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Molecular Hydrogen Layer", variable=saturn_molecular_hydrogen_var)
saturn_molecular_hydrogen_checkbutton.pack(anchor='w')
CreateToolTip(saturn_molecular_hydrogen_checkbutton, saturn_molecular_hydrogen_info)

# saturn cloud layer shell
saturn_cloud_layer_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Cloud Layer", variable=saturn_cloud_layer_var)
saturn_cloud_layer_checkbutton.pack(anchor='w')
CreateToolTip(saturn_cloud_layer_checkbutton, saturn_cloud_layer_info)

# saturn upper atmosphere shell
saturn_upper_atmosphere_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Upper Atmosphere", variable=saturn_upper_atmosphere_var)
saturn_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(saturn_upper_atmosphere_checkbutton, saturn_upper_atmosphere_info)

# saturn ring system shell
saturn_ring_system_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Ring System", variable=saturn_ring_system_var)
saturn_ring_system_checkbutton.pack(anchor='w')
CreateToolTip(saturn_ring_system_checkbutton, saturn_ring_system_info)

saturn_radiation_belts_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Radiation Belts", variable=saturn_radiation_belts_var)
saturn_radiation_belts_checkbutton.pack(anchor='w')
CreateToolTip(saturn_radiation_belts_checkbutton, saturn_radiation_belts_info)

saturn_enceladus_plasma_torus_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Enceladus Plasma Torus", variable=saturn_enceladus_plasma_torus_var)
saturn_enceladus_plasma_torus_checkbutton.pack(anchor='w')
CreateToolTip(saturn_enceladus_plasma_torus_checkbutton, saturn_enceladus_plasma_torus_info)

# saturn magnetosphere components
saturn_magnetosphere_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Magnetosphere", variable=saturn_magnetosphere_var)
saturn_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(saturn_magnetosphere_checkbutton, saturn_magnetosphere_info)

# saturn hill_sphere shell
saturn_hill_sphere_checkbutton = tk.Checkbutton(saturn_shell_options_frame, text="-- Hill Sphere", variable=saturn_hill_sphere_var)
saturn_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(saturn_hill_sphere_checkbutton, saturn_hill_sphere_info) 

create_celestial_checkbutton("- Pan", pan_var)
create_celestial_checkbutton("- Daphnis", daphnis_var)
create_celestial_checkbutton("- Prometheus", prometheus_var)
create_celestial_checkbutton("- Pandora", pandora_var)
create_celestial_checkbutton("- Mimas", mimas_var)
create_celestial_checkbutton("- Enceladus", enceladus_var)
create_celestial_checkbutton("- Tethys", tethys_var)
create_celestial_checkbutton("- Dione", dione_var)
create_celestial_checkbutton("- Rhea", rhea_var)
create_celestial_checkbutton("- Titan", titan_var)
create_celestial_checkbutton("- Hyperion", hyperion_var)
create_celestial_checkbutton("- Iapetus", iapetus_var)
create_celestial_checkbutton("- Phoebe", phoebe_var)

create_celestial_checkbutton("Uranus", uranus_var)
# Create a Frame specifically for the uranus shell options (indented)
uranus_shell_options_frame = tk.Frame(celestial_frame)
uranus_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# uranus core shell
uranus_core_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Core", variable=uranus_core_var)
uranus_core_checkbutton.pack(anchor='w')
CreateToolTip(uranus_core_checkbutton, uranus_core_info)

# uranus metallic hydrogen shell
uranus_mantle_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- mantle", variable=uranus_mantle_var)
uranus_mantle_checkbutton.pack(anchor='w')
CreateToolTip(uranus_mantle_checkbutton, uranus_mantle_info)

# uranus cloud layer shell
uranus_cloud_layer_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Cloud Layer", variable=uranus_cloud_layer_var)
uranus_cloud_layer_checkbutton.pack(anchor='w')
CreateToolTip(uranus_cloud_layer_checkbutton, uranus_cloud_layer_info)

# uranus upper atmosphere shell
uranus_upper_atmosphere_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Upper Atmosphere", variable=uranus_upper_atmosphere_var)
uranus_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(uranus_upper_atmosphere_checkbutton, uranus_upper_atmosphere_info)

# uranus ring system shell
uranus_ring_system_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Ring System", variable=uranus_ring_system_var)
uranus_ring_system_checkbutton.pack(anchor='w')
CreateToolTip(uranus_ring_system_checkbutton, uranus_ring_system_info)

uranus_radiation_belts_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Radiation Belts", variable=uranus_radiation_belts_var)
uranus_radiation_belts_checkbutton.pack(anchor='w')
CreateToolTip(uranus_radiation_belts_checkbutton, uranus_radiation_belts_info)

# uranus magnetosphere components
uranus_magnetosphere_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Magnetosphere", variable=uranus_magnetosphere_var)
uranus_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(uranus_magnetosphere_checkbutton, uranus_magnetosphere_info)

# uranus hill_sphere shell
uranus_hill_sphere_checkbutton = tk.Checkbutton(uranus_shell_options_frame, text="-- Hill Sphere", variable=uranus_hill_sphere_var)
uranus_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(uranus_hill_sphere_checkbutton, uranus_hill_sphere_info) 

# Uranus moons
create_celestial_checkbutton("- Ariel", ariel_var)
create_celestial_checkbutton("- Umbriel", umbriel_var)
create_celestial_checkbutton("- Titania", titania_var)
create_celestial_checkbutton("- Oberon", oberon_var)
create_celestial_checkbutton("- Miranda", miranda_var)
create_celestial_checkbutton("- Portia", portia_var)
create_celestial_checkbutton("- Mab", mab_var)

create_celestial_checkbutton("Neptune", neptune_var)

# Create a Frame specifically for the neptune shell options (indented)
neptune_shell_options_frame = tk.Frame(celestial_frame)
neptune_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# neptune core shell
neptune_core_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Core", variable=neptune_core_var)
neptune_core_checkbutton.pack(anchor='w')
CreateToolTip(neptune_core_checkbutton, neptune_core_info)

# neptune metallic hydrogen shell
neptune_mantle_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Mantle", variable=neptune_mantle_var)
neptune_mantle_checkbutton.pack(anchor='w')
CreateToolTip(neptune_mantle_checkbutton, neptune_mantle_info)

# neptune cloud layer shell
neptune_cloud_layer_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Cloud Layer", variable=neptune_cloud_layer_var)
neptune_cloud_layer_checkbutton.pack(anchor='w')
CreateToolTip(neptune_cloud_layer_checkbutton, neptune_cloud_layer_info)

# neptune upper atmosphere shell
neptune_upper_atmosphere_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Upper Atmosphere", variable=neptune_upper_atmosphere_var)
neptune_upper_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(neptune_upper_atmosphere_checkbutton, neptune_upper_atmosphere_info)

# neptune ring system shell
neptune_ring_system_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Ring System", variable=neptune_ring_system_var)
neptune_ring_system_checkbutton.pack(anchor='w')
CreateToolTip(neptune_ring_system_checkbutton, neptune_ring_system_info)

neptune_radiation_belts_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Radiation Belts", variable=neptune_radiation_belts_var)
neptune_radiation_belts_checkbutton.pack(anchor='w')
CreateToolTip(neptune_radiation_belts_checkbutton, neptune_radiation_belts_info)

# neptune magnetosphere components
neptune_magnetosphere_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Magnetosphere", variable=neptune_magnetosphere_var)
neptune_magnetosphere_checkbutton.pack(anchor='w')
CreateToolTip(neptune_magnetosphere_checkbutton, neptune_magnetosphere_info)

# neptune hill_sphere shell
neptune_hill_sphere_checkbutton = tk.Checkbutton(neptune_shell_options_frame, text="-- Hill Sphere", variable=neptune_hill_sphere_var)
neptune_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(neptune_hill_sphere_checkbutton, neptune_hill_sphere_info) 
create_celestial_checkbutton("- Triton", triton_var)
create_celestial_checkbutton("- Despina", despina_var)
create_celestial_checkbutton("- Galatea", galatea_var)

create_celestial_checkbutton("Pluto", pluto_var)

# Create a Frame specifically for the pluto shell options (indented)
pluto_shell_options_frame = tk.Frame(celestial_frame)
pluto_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# pluto core shell
pluto_core_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- Core", variable=pluto_core_var)
pluto_core_checkbutton.pack(anchor='w')
CreateToolTip(pluto_core_checkbutton, pluto_core_info)

# pluto mantle shell
pluto_mantle_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- mantle", variable=pluto_mantle_var)
pluto_mantle_checkbutton.pack(anchor='w')
CreateToolTip(pluto_mantle_checkbutton, pluto_mantle_info)

# pluto crust shell
pluto_crust_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- Crust", variable=pluto_crust_var)
pluto_crust_checkbutton.pack(anchor='w')
CreateToolTip(pluto_crust_checkbutton, pluto_crust_info)

# pluto haze layer shell
pluto_haze_layer_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- Haze Layer", variable=pluto_haze_layer_var)
pluto_haze_layer_checkbutton.pack(anchor='w')
CreateToolTip(pluto_haze_layer_checkbutton, pluto_haze_layer_info)

# pluto atmosphere shell
pluto_atmosphere_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- Atmosphere", variable=pluto_atmosphere_var)
pluto_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(pluto_atmosphere_checkbutton, pluto_atmosphere_info)

# pluto hill_sphere shell
pluto_hill_sphere_checkbutton = tk.Checkbutton(pluto_shell_options_frame, text="-- Hill Sphere", variable=pluto_hill_sphere_var)
pluto_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(pluto_hill_sphere_checkbutton, pluto_hill_sphere_info) 
create_celestial_checkbutton("- Charon", charon_var)
create_celestial_checkbutton("- Styx", styx_var)
create_celestial_checkbutton("- Nix", nix_var)
create_celestial_checkbutton("- Kerberos", kerberos_var)
create_celestial_checkbutton("- Hydra", hydra_var)

# Kuiper Belt Objects
create_celestial_checkbutton("Orcus", orcus_var)
create_celestial_checkbutton("Ixion", ixion_var)
create_celestial_checkbutton("2002 MS4", ms4_var)
create_celestial_checkbutton("2004 GV9", gv9_var)
create_celestial_checkbutton("Varuna", varuna_var)
create_celestial_checkbutton("Haumea", haumea_var)
create_celestial_checkbutton("Quaoar", quaoar_var)
create_celestial_checkbutton("Arrokoth", arrokoth_var)
create_celestial_checkbutton("Makemake", makemake_var)
create_celestial_checkbutton("Gonggong", gonggong_var)
create_celestial_checkbutton("Eris", eris_var)
# Create a Frame specifically for the eris shell options (indented)
eris_shell_options_frame = tk.Frame(celestial_frame)
eris_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# eris core shell
eris_core_checkbutton = tk.Checkbutton(eris_shell_options_frame, text="-- Core", variable=eris_core_var)
eris_core_checkbutton.pack(anchor='w')
CreateToolTip(eris_core_checkbutton, eris_core_info)

# eris mantle shell
eris_mantle_checkbutton = tk.Checkbutton(eris_shell_options_frame, text="-- Mantle", variable=eris_mantle_var)
eris_mantle_checkbutton.pack(anchor='w')
CreateToolTip(eris_mantle_checkbutton, eris_mantle_info)

# eris crust shell
eris_crust_checkbutton = tk.Checkbutton(eris_shell_options_frame, text="-- Crust", variable=eris_crust_var)
eris_crust_checkbutton.pack(anchor='w')
CreateToolTip(eris_crust_checkbutton, eris_crust_info)

# eris atmosphere shell
eris_atmosphere_checkbutton = tk.Checkbutton(eris_shell_options_frame, text="-- Atmosphere", variable=eris_atmosphere_var)
eris_atmosphere_checkbutton.pack(anchor='w')
CreateToolTip(eris_atmosphere_checkbutton, eris_atmosphere_info)

# eris hill_sphere shell
eris_hill_sphere_checkbutton = tk.Checkbutton(eris_shell_options_frame, text="-- Hill Sphere", variable=eris_hill_sphere_var)
eris_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(eris_hill_sphere_checkbutton, eris_hill_sphere_info) 
create_celestial_checkbutton("- Dysnomia", dysnomia_var)

create_celestial_checkbutton("Sedna", sedna_var)

create_celestial_checkbutton("2017 OF201", of201_var)

create_celestial_checkbutton("Planet 9", planet9_var)
# Create a Frame specifically for the planet9 shell options (indented)
planet9_shell_options_frame = tk.Frame(celestial_frame)
planet9_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels

# planet9 surface shell
planet9_surface_checkbutton = tk.Checkbutton(planet9_shell_options_frame, text="-- Surface", variable=planet9_surface_var)
planet9_surface_checkbutton.pack(anchor='w')
CreateToolTip(planet9_surface_checkbutton, planet9_surface_info)

# planet9 hill_sphere shell
planet9_hill_sphere_checkbutton = tk.Checkbutton(planet9_shell_options_frame, text="-- Hill Sphere", variable=planet9_hill_sphere_var)
planet9_hill_sphere_checkbutton.pack(anchor='w')
CreateToolTip(planet9_hill_sphere_checkbutton, planet9_hill_sphere_info) 

# Checkbuttons for missions
mission_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Space Missions")
mission_frame.pack(pady=(10, 5), fill='x')
CreateToolTip(mission_frame, "Select space missions for plotting. Selected objects will be plotted on the entered date, as well as ideal " 
              "orbits. Selected objects will be animated only over the fetched dates and only if within their defined date ranges, and will " 
              "plot both actual and ideal orbits.")

def create_mission_checkbutton(name, variable, dates):
    checkbutton = tk.Checkbutton(mission_frame, text=f"{name} {dates}", variable=variable, command=handle_mission_selection)
    checkbutton.pack(anchor='w')

    info_text = INFO.get(name, "No information available")
    tooltip_text = f"{info_text}\nMission duration: {dates}"
    if 'mission_url' in INFO:
        tooltip_text += f"\nMore Info: {INFO['mission_url']}"
    CreateToolTip(checkbutton, tooltip_text)
# Start dates are the day after launch to avoid missing Horizons data.
create_mission_checkbutton("Apollo 11 S-IVB", apollo11sivb_var, "(1969-07-16:17 to 1969-07-28:00)")     # Time Specification: Start=1969-07-16 17 UT , Stop=1969-07-28 00, Step=1 (hours)
create_mission_checkbutton("Pioneer 10", pioneer10_var, "(1972-03-04 to 2003-01-23)")
create_mission_checkbutton("Pioneer 11", pioneer11_var, "(1973-04-07 to 1995-09-30)")
create_mission_checkbutton("Voyager 2", voyager2_var, "(1977-08-21 to 2029-12-31)")
create_mission_checkbutton("Voyager 1", voyager1_var, "(1977-09-06 to 2029-12-31)")
create_mission_checkbutton("Galileo", galileo_var, "(1989-10-19 to 2003-09-30)")
create_mission_checkbutton("SOHO Solar Observatory", soho_var, "(1995-12-3 to 2029-12-31)")
create_mission_checkbutton("Cassini", cassini_var, "(1997-10-16 to 2017-09-15)")
create_mission_checkbutton("Rosetta", rosetta_var, "(2004-03-02 to 2016-10-05)")
create_mission_checkbutton("New Horizons", new_horizons_var, "(2006-01-19 to 2029-12-31)")
create_mission_checkbutton("Chang'e", change_var, "(2007-10-25 to 2029-12-31)")
create_mission_checkbutton("Akatsuki", akatsuki_var, "(2010-05-22 to 2025-03-02)")
create_mission_checkbutton("Juno", juno_var, "(2011-08-06 to 2025-5-10)")
create_mission_checkbutton("Gaia", gaia_var, "(2013-12-20 to 2025-07-01)")
create_mission_checkbutton("Hayabusa 2", hayabusa2_var, "(2014-12-04 to 2020-12-05)")
create_mission_checkbutton("OSIRIS REx", osiris_rex_var, "(2016-09-10 to 2023-09-24)")
create_mission_checkbutton("Parker Solar Probe", parker_solar_probe_var, "(2018-08-13 to 2029-12-31)")
create_mission_checkbutton("BepiColombo", bepicolombo_var, "(2018-10-21 to 2030-12-31)")
create_mission_checkbutton("Solar Orbiter", solarorbiter_var, "(2020-02-10 to 2030-11-20)")
create_mission_checkbutton("Perseverance Mars Rover", perse_var, "(2020-07-31 to 2026-2-19)")
create_mission_checkbutton("Lucy", lucy_var, "(2021-10-18 to 2033-05-01)")
create_mission_checkbutton("DART", dart_var, "(2021-11-26 to 2022-09-25)")
create_mission_checkbutton("James Webb Space Telescope", jwst_var, "(2021-12-26 to 2029-12-31)")
create_mission_checkbutton("OSIRIS APEX", osiris_apex_var, "(2023-09-24 to 2029-12-31)")
create_mission_checkbutton("Europa-Clipper", europa_clipper_var, "(2024-10-15 to April 2030)")

# Checkbuttons for comets
comet_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Comets and Interstellar Objects")
comet_frame.pack(pady=(10, 5), fill='x')
CreateToolTip(comet_frame, "Select comets for plotting. Selected objects will be plotted on the entered date, as well as ideal " 
              "orbits. Selected objects will be animated only over the fetched dates only if within their defined date ranges, and will " 
              "plot both actual and ideal orbits.")

# These functions should be defined AFTER the GUI widgets exist

def update_offset_date_displays():
    """Update the date labels next to offset fields"""
    try:
        # Get base date from entry fields
        base_date = datetime(
            int(entry_year.get()),
            int(entry_month.get()),
            int(entry_day.get()),
            int(entry_hour.get()),
            int(entry_minute.get())
        )
        
        # Update start date label
        start_offset = int(start_date_entry.get())
        start_date = base_date + timedelta(days=start_offset)
        start_date_label_display.config(text=start_date.strftime("%B %d, %Y"))
        
        # Update end date label
        end_offset = int(end_date_entry.get())
        end_date = base_date + timedelta(days=end_offset)
        end_date_label_display.config(text=end_date.strftime("%B %d, %Y"))
        
    except ValueError:
        # Handle invalid input
        start_date_label_display.config(text="Invalid date")
        end_date_label_display.config(text="Invalid date")

def toggle_special_fetch_mode():
    """Toggle visual feedback for special fetch mode"""
    if special_fetch_var.get() == 1:
        # Cyan background for special mode
        for widget in [start_date_entry, end_date_entry, default_interval_entry,
                      eccentric_interval_entry, mission_comet_interval_entry, 
                      satellite_interval_entry]:
            widget.config(bg='cyan')
        update_status_display("Special fetch mode ENABLED - data will NOT be cached", 'special')
        print("[SPECIAL MODE] Enabled - subsequent fetches will use temporary cache")
    else:
        # Normal background
        for widget in [start_date_entry, end_date_entry, default_interval_entry,
                      eccentric_interval_entry, mission_comet_interval_entry, 
                      satellite_interval_entry]:
            widget.config(bg='white')
        # Clear temp cache
        global temp_cache
        temp_cache = {}
        if os.path.exists(TEMP_CACHE_FILE):
            os.remove(TEMP_CACHE_FILE)
        update_status_display("Special fetch mode DISABLED - temp cache cleared", 'info')
        print("[SPECIAL MODE] Disabled - temporary cache cleared")

# Updated create_comet_checkbutton function
def create_comet_checkbutton(name, variable, dates, perihelion):
    """
    Creates a checkbutton for a comet with a tooltip containing its description and perihelion date.

    Parameters:
    - name (str): The name of the comet.
    - variable (tk.IntVar): The Tkinter variable linked to the checkbutton.
    - dates (str): The mission duration or observation period.
    - perihelion (str): The date of perihelion passage.
    """
    checkbutton = tk.Checkbutton(
        comet_frame,
        text=f"{name} {dates}",
        variable=variable,
        command=handle_mission_selection
    )
    checkbutton.pack(anchor='w')

    # Fetch the description from INFO
    info_text = INFO.get(name, "No information available.")

    # Create the tooltip with description and perihelion
    tooltip_text = f"{info_text}\nPerihelion: {perihelion}"
    CreateToolTip(checkbutton, tooltip_text)

create_comet_checkbutton("67P/Churyumov-Gerasimenko", comet_Churyumov_Gerasimenko_var, "(1962-1-20 to 2029-12-31)", 
    "August 13, 2015")
    # datetime(1962, 1, 20), 'end_date': datetime(2025, 12, 31) replacing datetime (2002, 11, 22), 'end_date': datetime(2021, 5, 1)
create_comet_checkbutton("Halley", comet_halley_var, "(1962-01-21 to 2061-7-28)",      
                         # initial start date 1982-11-26 to 1995-10-20. Horizons has 1962-01-20 and ongoing.
                         "February 9, 1986")
create_comet_checkbutton("Ikeya-Seki", comet_ikeya_seki_var, "(1965-09-21 to 1966-01-14)", 
                         "October 21, 1965")
create_comet_checkbutton("West", comet_west_var, "(1975-11-05 to 1976-06-01)", 
                         "February 25, 1976")
create_comet_checkbutton("Hale-Bopp", comet_hale_bopp_var, "(1995-07-23 to 2001-12-31)", 
                         "April 1, 1997")
create_comet_checkbutton("Hyakutake", comet_hyakutake_var, "(1995-12-01 to 1996-06-01)", 
                         "May 1, 1996")
create_comet_checkbutton("McNaught", comet_mcnaught_var, "(2006-08-07 to 2008-06-01)", 
                         "January 12, 2007")
create_comet_checkbutton("Oumuamua", oumuamua_var, "(2017-10-14 to 2018-01-01)", 
                         "September 9, 2017")
create_comet_checkbutton("Borisov", comet_borisov_var, "(2019-08-30 to 2020-10-01)", 
    "December 8, 2019")
create_comet_checkbutton("NEOWISE", comet_neowise_var, "(2020-03-27 to 2021-06-01)", 
                         "July 3, 2020")
create_comet_checkbutton("Tsuchinshan-ATLAS", comet_tsuchinshan_atlas_var, "(2023-01-09 to 2029-12-31)", 
                         "April 28, 2024")
create_comet_checkbutton("ATLAS", comet_atlas_var, "(2024-06-17 to 2029-12-31)", 
                         "January 13, 2025")

# Controls in controls_frame (Scale Options and beyond)

# Scale Options
scale_frame = tk.LabelFrame(controls_frame, text="Scale Options for Solar System Plots")
scale_frame.pack(pady=(5, 5), fill='x')

scale_var = tk.StringVar(value='Auto')

auto_scale_radio = tk.Radiobutton(scale_frame, text="Automatic scaling of your plot", variable=scale_var, value='Auto')
auto_scale_radio.pack(anchor='w')
CreateToolTip(auto_scale_radio, "Automatically adjust scale based on selected objects")

manual_scale_radio = tk.Radiobutton(scale_frame, text="Or manually enter scale of your plot in AU. See hovertext for suggestions.", 
variable=scale_var, value='Manual')
manual_scale_radio.pack(anchor='w')

CreateToolTip(manual_scale_radio, "Some key mean distances for custom scaling: \n* Mercury: 0.39 AU\n* Venus: 0.72 AU\n* Earth: 1 AU\n"
"* Mars: 1.52 AU\n* Asteroid Belt: between 2.2 and 3.2 AU\n* Jupiter: 5.2 AU\n* Jupiter System: 0.5 AU\n* Saturn: 9.5 AU\n* Uranus: 19.2 AU\n* Neptune: 30.1 AU\n"
"* Dwarf Planet Pluto: between 30 and 49 AU.\n* Kuiper Belt: from roughly 30 to 50 AU\n* Dwarf Planet Sedna: currently at about 83.3 AU, ranging from 74 AU to 936 AU, " 
"with a mean distance of 526 AU\n* Planet 9, use 360 AU for full orbit\n* Solar Wind Termination Shock: 94 AU\n* Heliopause (edge of the Sun's influence): 126 AU\n* Voyager 1: currently over 165 AU\n" 
"* Hypothetical \"Planet Nine\" orbit: 600 AU\n"
"* Inner Limit of Oort Cloud: 2,000 AU\n* Outer Limit of Oort Cloud: 100,000 AU\n* Extent of Solar Gravitational Influence (Hill Sphere): 126,000 AU\n* Proxima Centauri: 268,585 AU")

custom_scale_entry = tk.Entry(scale_frame, width=10)
custom_scale_entry.pack(anchor='w')
custom_scale_entry.insert(0, '10')  # Default scale value

center_label = tk.Label(controls_frame, text="Select Center Object for Your Plot:")
center_label.pack(anchor='w')

center_object_var = tk.StringVar(value='Sun')
center_options = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Bennu/OSIRIS', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Arrokoth/New_Horizons', 'Eris/Dysnomia', 'Planet 9'] 
# A unique center for Eris is required using the satellite solution not the sun centered object.
center_menu = ttk.Combobox(controls_frame, textvariable=center_object_var, values=center_options)
center_menu.pack(anchor='w')
CreateToolTip(center_menu, "Select the object to center the plot on. DO NOT select the same object from the Select Objects check list.")

"""
# Define function to update orbit paths when the center object changes
def on_center_change(*args):
# Update orbit paths when the center object is changed.
    center_object = center_object_var.get()
    if center_object != 'Sun':
        # Only fetch non-Sun centered paths when needed to avoid excessive startup time
        status_display.config(text=f"Updating orbit paths for center: {center_object}...")
        root.update()  # Force GUI to refresh
        update_orbit_paths(center_object)
        status_display.config(text=f"Orbit paths updated for center: {center_object}")
        """

def on_center_change(*args):
    """Update frame title when the center object is changed."""
    center_object = center_object_var.get()
    
    # Just update the frame title, don't fetch any data
    orbit_path_frame.config(text=f"Standard Orbit Path Fetching Controls for JSON Cache (Center: {center_object})")
    
    # Update status to show current center
    update_status_display(f"Center changed to: {center_object}", 'info')
    
    # DO NOT call update_orbit_paths or update_orbit_paths_incrementally here!
    # Data will be fetched when actually plotting with selected objects

# Bind the center_object_var to the on_center_change function
center_object_var.trace_add("write", on_center_change)

# Create a frame for the interval settings
interval_frame = tk.LabelFrame(controls_frame, text="Orbit & Trajectory Plotting Intervals for Non-Animated Plots")
interval_frame.pack(pady=(5, 5), fill='x')

# Add label and entry for comet path plotting interval
comet_interval_label = tk.Label(interval_frame, text="Comet path plotting interval = end date - start date (in days) / :")
comet_interval_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 2), sticky='w')
comet_interval_entry = tk.Entry(interval_frame, width=5)
comet_interval_entry.grid(row=0, column=1, padx=(0, 5), pady=(5, 2), sticky='w')
comet_interval_entry.insert(0, '100')  # Default value
CreateToolTip(comet_interval_label, "Higher value = fewer points = faster loading. Lower value = more detailed trajectory.")

# Add label and entry for mission path plotting interval
mission_interval_label = tk.Label(interval_frame, text="Space mission path plotting interval = end date - start date (in days) / :")
mission_interval_label.grid(row=1, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
mission_interval_entry = tk.Entry(interval_frame, width=5)
mission_interval_entry.grid(row=1, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
mission_interval_entry.insert(0, '75')  # Default value
CreateToolTip(mission_interval_label, "Higher value = fewer points = faster loading. Lower value = more detailed trajectory.")

# Add label and entry for planet orbit plotting interval
planet_interval_label = tk.Label(interval_frame, text="Planet orbit plotting interval = orbital period (in days) / :")
planet_interval_label.grid(row=2, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
planet_interval_entry = tk.Entry(interval_frame, width=5)
planet_interval_entry.grid(row=2, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
planet_interval_entry.insert(0, '50')  # Default value
CreateToolTip(planet_interval_label, "Higher value = fewer points = faster loading. Lower value = smoother orbit.")

# Add label and entry for satellite orbit days
sat_days_label = tk.Label(interval_frame, text="Planetary satellite number of days of orbit to plot:")
sat_days_label.grid(row=3, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
sat_days_entry = tk.Entry(interval_frame, width=5)
sat_days_entry.grid(row=3, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
sat_days_entry.insert(0, '56')  # Default value
CreateToolTip(sat_days_label, "Total number of days to plot for planetary moons' orbits.")

# Add label and entry for satellite orbit period
sat_period_label = tk.Label(interval_frame, text="Planetary satellite orbit plotting interval (in days):")
sat_period_label.grid(row=4, column=0, padx=(5, 5), pady=(2, 5), sticky='w')
sat_period_entry = tk.Entry(interval_frame, width=5)
sat_period_entry.grid(row=4, column=1, padx=(0, 5), pady=(2, 5), sticky='w')
sat_period_entry.insert(0, '1')  # Default value
CreateToolTip(sat_period_label, "Higher value = fewer points = faster loading. Lower value = smoother orbit.")

# Number of Frames
num_frames_label = tk.Label(controls_frame, text="Enter Hours, Days, Weeks, Months or Years to Animate starting with \"Now\":")
num_frames_label.pack(anchor='w')
num_frames_entry = tk.Entry(controls_frame, width=5)
num_frames_entry.pack(anchor='w')
num_frames_entry.insert(0, '29')  # Default number of frames
CreateToolTip(num_frames_entry, "Do not exceed 130 to avoid timing out JPL Horizons' data fetch.")

"""
# Create a new frame for orbit path fetching controls
orbit_path_frame = tk.LabelFrame(controls_frame, text="Orbit Path Fetching Controls")
orbit_path_frame.pack(pady=(5, 5), fill='x')
"""

# Update the frame title
orbit_path_frame = tk.LabelFrame(controls_frame, text="Standard Orbit Path Fetching Controls for JSON Cache")
orbit_path_frame.pack(pady=(5, 5), fill='x')

# Add special fetch checkbox ABOVE the frame
special_fetch_var = tk.IntVar(value=0)
special_fetch_check = tk.Checkbutton(
    controls_frame,
    text="Use updated Standard Orbit Path Fetching Controls for JSON Cache for a special fetch that will not be cached:",
    variable=special_fetch_var,
    command=toggle_special_fetch_mode,
    font=("Arial", 9, "bold"),
    fg='darkblue',
    wraplength=400
)
special_fetch_check.pack(pady=(5, 0), fill='x')
CreateToolTip(special_fetch_check,
    "When checked:\n"
    "• Fetches use the settings below for plotting\n"
    "• Data is stored in temporary cache only\n"
    "• Temp cache is cleared when unchecked or app closes\n"
    "• Does not affect the main JSON cache file")

# After orbit_path_frame, where you want to position the status frame:
status_frame = tk.LabelFrame(controls_frame, text="Data Fetching Status and Output Messages", padx=10, pady=10, bg='SystemButtonFace', fg='black')
status_frame.pack(pady=(5, 5), fill='x')

status_display.destroy()  # Remove the old label

# Create a NEW label in the status_frame instead of trying to re-parent
status_display = tk.Label(
    status_frame, 
    text="Data Fetching Status", 
    font=("Arial", 10), 
    bg='SystemButtonFace', 
    fg='black'
)
status_display.pack(anchor='w', padx=5, pady=5)

# Create frame for start date offset with date display
start_date_frame = tk.Frame(orbit_path_frame)
start_date_frame.grid(row=0, column=0, columnspan=2, padx=(5, 5), pady=(5, 2), sticky='w')

start_date_label = tk.Label(start_date_frame, text="Start date offset from now (in days):")
start_date_label.pack(side='left')

start_date_entry = tk.Entry(start_date_frame, width=5)
start_date_entry.pack(side='left', padx=(5, 5))
start_date_entry.insert(0, '0')

# Add label to show the calculated date
start_date_label_display = tk.Label(start_date_frame, text="", fg='blue', font=("Arial", 9, "italic"))
start_date_label_display.pack(side='left')

CreateToolTip(start_date_label, "Number of days to look back from current date (negative value means looking into the past)")

# Create frame for end date offset with date display
end_date_frame = tk.Frame(orbit_path_frame)
end_date_frame.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(2, 2), sticky='w')

end_date_label = tk.Label(end_date_frame, text="End date offset from now (in days):")
end_date_label.pack(side='left')

end_date_entry = tk.Entry(end_date_frame, width=5)
end_date_entry.pack(side='left', padx=(5, 5))
end_date_entry.insert(0, '365')

# Add label to show the calculated date
end_date_label_display = tk.Label(end_date_frame, text="", fg='blue', font=("Arial", 9, "italic"))
end_date_label_display.pack(side='left')

CreateToolTip(end_date_label, "Number of days to look ahead from current date")

# Bind update functions to the entry fields
start_date_entry.bind('<KeyRelease>', lambda e: update_offset_date_displays())
end_date_entry.bind('<KeyRelease>', lambda e: update_offset_date_displays())

# Also update when the main date fields change
for widget in [entry_year, entry_month, entry_day, entry_hour, entry_minute]:
    widget.bind('<KeyRelease>', lambda e: update_offset_date_displays())

# Schedule initial update after GUI is fully loaded
root.after(100, update_offset_date_displays)

# Add label and entry for default interval
default_interval_label = tk.Label(orbit_path_frame, text="Default interval for orbit paths:")
default_interval_label.grid(row=2, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
default_interval_entry = tk.Entry(orbit_path_frame, width=5)
default_interval_entry.grid(row=2, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
default_interval_entry.insert(0, '1d')  # Default value
CreateToolTip(default_interval_label, "Default time interval for orbit paths. Examples: 1d, 12h, 6h, 1h")

# Add label and entry for high eccentricity interval
eccentric_interval_label = tk.Label(orbit_path_frame, text="High eccentricity object interval:")
eccentric_interval_label.grid(row=3, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
eccentric_interval_entry = tk.Entry(orbit_path_frame, width=5)
eccentric_interval_entry.grid(row=3, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
eccentric_interval_entry.insert(0, '12h')  # Default value
CreateToolTip(eccentric_interval_label, "Time interval for objects with high eccentricity (e > 0.5)")

# Add label and entry for mission/comet interval
mission_comet_interval_label = tk.Label(orbit_path_frame, text="Mission/comet interval:")
mission_comet_interval_label.grid(row=4, column=0, padx=(5, 5), pady=(2, 2), sticky='w')
mission_comet_interval_entry = tk.Entry(orbit_path_frame, width=5)
mission_comet_interval_entry.grid(row=4, column=1, padx=(0, 5), pady=(2, 2), sticky='w')
mission_comet_interval_entry.insert(0, '6h')  # Default value
CreateToolTip(mission_comet_interval_label, "Time interval for spacecraft, comets, and non-satellite objects")

# Add label and entry for satellite interval
satellite_interval_label = tk.Label(orbit_path_frame, text="Satellite/moon interval:")
satellite_interval_label.grid(row=5, column=0, padx=(5, 5), pady=(2, 5), sticky='w')
satellite_interval_entry = tk.Entry(orbit_path_frame, width=5)
satellite_interval_entry.grid(row=5, column=1, padx=(0, 5), pady=(2, 5), sticky='w')
satellite_interval_entry.insert(0, '1h')  # Default value
CreateToolTip(satellite_interval_label, "Time interval for satellites (moons) of the center object")

# Add a scroll down message right before the plotting buttons
scroll_message = tk.Label(
    controls_frame,
    text="SCROLL DOWN TO SEE ALL PLOTTING BUTTONS",
    fg='red',
    bg='SystemButtonFace',
    font=("Arial", 10, "bold")
)
scroll_message.pack(pady=(10, 5))

# Paloma's Birthday button and its animation
paloma_buttons_frame = tk.Frame(controls_frame)
paloma_buttons_frame.pack(pady=(5, 0), fill='x')

# "Single Time Plot" Button 
plot_button = tk.Button(
    paloma_buttons_frame, 
    text="Plot Entered Date", 
    command=plot_objects, 
    width=BUTTON_WIDTH, 
    font=BUTTON_FONT, 
    bg='SystemButtonFace', 
    fg='blue'
)
plot_button.pack(side='left', padx=(0, 5), pady=(5, 0))
CreateToolTip(plot_button, "Plot the positions of selected objects on the selected date.")

paloma_birthday_button = tk.Button(
    paloma_buttons_frame, 
    text="Enter Paloma's Birthday", 
    command=set_palomas_birthday, 
    bg='pink', 
    fg='blue',
    width=BUTTON_WIDTH,      # Set uniform width
    font=BUTTON_FONT         # Set uniform font   
)
# Pack the button to the left with right padding
paloma_birthday_button.pack(side='left', padx=(0, 5), pady=(5, 0))
CreateToolTip(
    paloma_birthday_button, 
    "Set the date to Paloma's Birthday (2005-02-04)"
)

animate_paloma_button = tk.Button(
    paloma_buttons_frame, 
    text="Animate Birthdays", 
    command=animate_palomas_birthday, 
    bg='pink', 
    fg='blue',
    width=BUTTON_WIDTH,      # Set uniform width
    font=BUTTON_FONT         # Set uniform font
)
# Pack the button to the left with left padding
animate_paloma_button.pack(side='left', padx=(0, 5), pady=(5, 0))
CreateToolTip(
    animate_paloma_button, 
    "Animate from Paloma's Birthday over years."
)

# Advance Buttons
advance_buttons_frame = tk.Frame(controls_frame)
advance_buttons_frame.pack(pady=(5, 0), fill='x')

# "Animate Minutes" button
animate_minute_button = tk.Button(
    advance_buttons_frame, 
    text="Animate Minutes", 
#    command=lambda: animate_objects(timedelta(minutes=1), "Minute"),
    command=animate_one_minute,
    width=BUTTON_WIDTH, 
    font=BUTTON_FONT, 
    bg='SystemButtonFace', 
    fg='blue'
)
animate_minute_button.grid(row=0, column=0, padx=(0, 5), pady=(5, 0))
CreateToolTip(animate_minute_button, "Animate the motion over minutes. Shows position every minute using the minutes entry field.")

# "Animate Hours" button
animate_hour_button = tk.Button(
    advance_buttons_frame, 
    text="Animate Hours", 
#    command=lambda: animate_objects(timedelta(hours=1), "Hour"),
    command=animate_one_hour,
    width=BUTTON_WIDTH, 
    font=BUTTON_FONT, 
    bg='SystemButtonFace', 
    fg='blue'
)
animate_hour_button.grid(row=0, column=1, padx=(0, 5), pady=(5, 0))
CreateToolTip(animate_hour_button, "Animate the motion over hours. Shows position every hour.")

# First Row of Animate Buttons: "Animate Days" and "Animate Weeks"
animate_day_button = tk.Button(advance_buttons_frame, text="Animate Days", command=animate_one_day, width=BUTTON_WIDTH, font=BUTTON_FONT, bg='SystemButtonFace', fg='blue')
animate_day_button.grid(row=1, column=0, padx=(0, 5), pady=(5, 0))
CreateToolTip(animate_day_button, "Animate the motion over days. This may take a while due to the large number of positions fetched.")

animate_week_button = tk.Button(advance_buttons_frame, text="Animate Weeks", command=animate_one_week, width=BUTTON_WIDTH, font=BUTTON_FONT, bg='SystemButtonFace', fg='blue')
animate_week_button.grid(row=1, column=1, padx=(5, 0), pady=(5, 0))
CreateToolTip(animate_week_button, "Animate the motion over weeks. This may take a while due to the large number of positions fetched.")

# Second Row of Animate Buttons: "Animate Months" and "Animate Years"
animate_month_button = tk.Button(advance_buttons_frame, text="Animate Months", command=animate_one_month, width=BUTTON_WIDTH, font=BUTTON_FONT, bg='SystemButtonFace', fg='blue')
animate_month_button.grid(row=2, column=0, padx=(0, 5), pady=(5, 0))
CreateToolTip(animate_month_button, "Animate the motion over months. This may take a while due to the large number of positions fetched.")

animate_year_button = tk.Button(advance_buttons_frame, text="Animate Years", command=animate_one_year, width=BUTTON_WIDTH, font=BUTTON_FONT, bg='SystemButtonFace', fg='blue')
animate_year_button.grid(row=2, column=1, padx=(5, 0), pady=(5, 0))
CreateToolTip(animate_year_button, "Animate the motion over years. This may take a while due to the large number of positions fetched.")

# Create the output_label inside the status_frame
output_label = tk.Label(
     status_frame,
     text="",
     fg='red',
     bg='SystemButtonFace',  # Match the background of the LabelFrame
     wraplength=400,  # Increased wraplength for better readability
     justify='left',
     anchor='w'
 )
output_label.pack()

# Create a Progress Bar inside the status_frame
progress_bar = ttk.Progressbar(status_frame, orient='horizontal', mode='indeterminate', length=300)
progress_bar.pack(pady=(5, 0))

# Add the function to call star_visualization_gui.py
def open_star_visualization():
    try:
        script_path = os.path.join(os.path.dirname(__file__), 'star_visualization_gui.py')
        subprocess.Popen(['python', script_path])
    except Exception as e:
        output_label.config(text=f"Error opening star visualization: {e}")
        print(f"Error opening star visualization: {e}")

# Add Star Visualization button
star_viz_button = tk.Button(
    advance_buttons_frame, 
    text="2D and 3D Star Visualizations", 
    command=open_star_visualization,
    width=BUTTON_WIDTH*2 + 5,  # Make it span two columns
    font=BUTTON_FONT, 
#    bg='SystemButtonFace', 
#    fg='blue'
    bg='blue', 
    fg='white'
)
star_viz_button.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(5, 0))
CreateToolTip(star_viz_button, "Open a specialized UI for 2D and 3D star visualizations, " 
              "including HR diagrams and stellar neighborhoods.")

# Create a Frame for the note (right column)
note_frame = tk.Frame(root)
note_frame.grid(row=0, column=2, padx=(5, 10), pady=(10, 10), sticky='n')

# Add the "Note" Label
note_label = tk.Label(
    note_frame,
    text="Note:",
    bg='SystemButtonFace',
    fg='black',
    font=("Arial", 10, "normal")
)
note_label.pack(anchor='w', pady=(0, 5))  # Align to the left with padding below

# Add the ScrolledText widget below the "Note" label
note_text_widget = scrolledtext.ScrolledText(
    note_frame,
    wrap='word',
    width=44,
    height=44.5,
    bg='SystemButtonFace',
    fg='black',
    insertbackground='white'
)
note_text_widget.pack(expand=True, fill='both')

# Insert the note text into the ScrolledText widget
note_text_widget.insert(tk.END, note_text)

# Make the ScrolledText widget read-only
note_text_widget.config(state='disabled')

# Run the Tkinter main loop
root.mainloop()
