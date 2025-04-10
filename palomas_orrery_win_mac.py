#Paloma's Orrery - Solar System Visualization Tool

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
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
from tkinter import scrolledtext
import threading
import time  # Used here for simulation purposes
import subprocess
import sys
import math
import tempfile
from pathlib import Path

from constants import (
    planetary_params,
    parent_planets,
    color_map,
    note_text,
    INFO,
    hover_text_sun_and_corona,
    gravitational_influence_info,
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
    core_info,
)

from visualization_utils import format_hover_text, add_hover_toggle_buttons

from save_utils import save_plot

# At the very top of the file, after imports:
from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely

# Create a global shutdown handler instance
shutdown_handler = PlotlyShutdownHandler()


# Initialize the main window
root = tk.Tk()
root.title("Paloma's Orrery - Updated January 2, 2025")
# Define 'today' once after initializing the main window
today = datetime.today()
# root.configure(bg="lightblue")  # Set the background color of the root window

# Define a standard font and button width
BUTTON_FONT = ("Arial", 10, "normal")  # You can adjust the font as needed
BUTTON_WIDTH = 17  # Number of characters wide

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

# Define controls_frame
controls_frame = tk.Frame(root)
controls_frame.grid(row=0, column=1, padx=(5, 10), pady=(10, 10), sticky='n')

# Suppress ErfaWarning messages
warnings.simplefilter('ignore', ErfaWarning)

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun

# Constants
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit
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
    

def get_script_path(script_name):
    """
    Get the absolute path to a script in the same directory.
    
    Parameters:
        script_name (str): Name of the script file
        
    Returns:
        Path: Resolved path to the script
    """
    return Path(__file__).parent / script_name

def create_sun_visualization(fig, animate=False, frames=None):
    """
    Creates a visualization of the Sun's layers including photosphere, inner corona, and outer corona.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the Sun visualization to
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        
    Returns:
        plotly.graph_objects.Figure: The updated figure

    Constants used:
        SOLAR_RADIUS_AU: Sun's radius in AU (0.00465047)
        INNER_CORONA_RADII: Inner corona extends to 2-3 solar radii (~0.014 AU)
        OUTER_CORONA_RADII: Outer corona extends to ~50 solar radii (~0.2 AU)
    """
    # Create base traces for static visualization
    def create_layer_traces():
        traces = []
        
        # 0.2. Sun's Gravitational Influence
        x, y, z = create_corona_sphere(GRAVITATIONAL_INFLUENCE_AU)

        # Create a text list matching the number of points
        text_array_gravitational_influence = [gravitational_influence_info for _ in range(len(x))]
        customdata_array_gravitational_influence = ["Sun's Gravitational Influence" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.0,
        #            color='green',
                    color= 'rgb(102, 187, 106)', 
                    opacity=0.2
                ),
                name='Sun\'s Gravitational Influence',
                text=text_array_gravitational_influence,             
                customdata=customdata_array_gravitational_influence, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='green',
                    size=0.5,
                    symbol='square-open',
                    opacity=0.2
                ),
                name='Sun\'s Gravitational Influence',
                text=['The Sun\'s gravitational influence to ~126,000 AU or 2 ly.'],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 0.3. Outer Oort Cloud
        x, y, z = create_corona_sphere(OUTER_OORT_CLOUD_AU)

        # Create a text list matching the number of points
        text_array_outer_oort = [outer_oort_info for _ in range(len(x))]
        customdata_array_outer_oort = ["Outer Oort Cloud" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.0,
                    color='white',  # Yellow approximates the visible color
                    opacity=0.2
                ),
                name='Outer Oort Cloud',
                text=text_array_outer_oort,             
                customdata=customdata_array_outer_oort, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='white',
                    size=1.0,
                    symbol='circle-open',
                    opacity=0.2
                ),
                name='Outer Oort Cloud',
                text=['Outer Oort Cloud from estimated 20,000 to 100,000 AU.'],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 0.4. Inner Oort Cloud
        x, y, z = create_corona_sphere(INNER_OORT_CLOUD_AU)

        # Create a text list matching the number of points
        text_array_inner_oort = [inner_oort_info for _ in range(len(x))]
        customdata_array_inner_oort = ["Inner Oort Cloud" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.0,
                    color='white',  # Yellow approximates the visible color
                    opacity=0.3
                ),
                name='Inner Oort Cloud',
                text=text_array_inner_oort,             
                customdata=customdata_array_inner_oort, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='white',
                    size=1.0,
                    symbol='circle-open',
                    opacity=0.3
                ),
                name='Inner Oort Cloud',
                text=['Inner Oort Cloud from estimated 2,000 to 20,000 AU.'],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 0.45. Inner Limit of Inner Oort Cloud
        x, y, z = create_corona_sphere(INNER_LIMIT_OORT_CLOUD_AU)

        # Create a text list matching the number of points
        text_array_inner_limit_oort = [inner_limit_oort_info for _ in range(len(x))]
        customdata_array_inner_limit_oort = ["Inner Limit of Oort Cloud" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.0,
                    color='white',  
                    opacity=0.3
                ),
                name='Inner Limit of Oort Cloud',
                text=text_array_inner_limit_oort,             
                customdata=customdata_array_inner_limit_oort, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='white',
                    size=1.0,
                    symbol='circle-open',
                    opacity=0.3
                ),
                name='Inner Limit of Oort Cloud',
                text=['Inner Oort Cloud from estimated 2,000 to 20,000 AU.'],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 0.5. Solar Wind and Heliopause Sphere
        x, y, z = create_corona_sphere(HELIOPAUSE_RADII * SOLAR_RADIUS_AU)

        # Create a text list matching the number of points
        text_array_solar_wind = [solar_wind_info for _ in range(len(x))]
        customdata_array_solar_wind = ["Solar Wind Heliopause" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=0.5,
                    color='rgb(135, 206, 250)',  # Nearest visible approximatation
                    opacity=0.2
                ),
                name='Solar Wind Heliopause',
                text=text_array_solar_wind,            # Replicated text
                customdata=customdata_array_solar_wind, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add Heliopause shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(135, 206, 250)',
                    size=0.5,
                    symbol='circle',
                    opacity=0.2
                ),
                name='Solar Wind Heliopause',
                text=['Solar Wind Heliopause (extends to 123 AU)'],
        #        hoverinfo='text',
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 0.7. Solar Wind and Termination Shock Sphere
        x, y, z = create_corona_sphere(TERMINATION_SHOCK_AU)

        # Create a text list matching the number of points
        text_array_termination_shock = [termination_shock_info for _ in range(len(x))]
        customdata_array_termination_shock = ["Solar Wind Termination Shock" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=0.5,
                    color='rgb(240, 244, 255)',  # Nearest visible approximatation
                    opacity=0.2
                ),
                name='Solar Wind Termination Shock',
                text=text_array_termination_shock,            # Replicated text
                customdata=customdata_array_termination_shock, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add Termination Shock shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(240, 244, 255)',
                    size=0.5,
                    symbol='circle',
                    opacity=0.2
                ),
                name='Solar Wind Termination Shock',
                text=['Solar Wind Termination Shock (extends to 94 AU)'],
        #        hoverinfo='text',
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 1. Outer Corona Sphere (most expansive, very diffuse)
        x, y, z = create_corona_sphere(OUTER_CORONA_RADII * SOLAR_RADIUS_AU)

        # Create a text list matching the number of points
        text_array_outer_corona = [outer_corona_info for _ in range(len(x))]
        customdata_array_outer_corona = ["Sun: Outer Corona" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=0.75,
                    color='rgb(25, 25, 112)',  # approximate visualization
                    opacity=0.3
                ),
                name='Sun: Outer Corona',
                text=text_array_outer_corona,            # Replicated text
                customdata=customdata_array_outer_corona, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add outer corona shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(25, 25, 112)',
                    size=0.75,
                    symbol='circle',
                    opacity=0.3
                ),
                name='Sun: Outer Corona',
                text=['Solar Outer Corona (extends to 50 solar radii or more, or 0.2 AU)'],
        #        hoverinfo='text',
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )

        # 2. Inner Corona Sphere
        x, y, z = create_corona_sphere(INNER_CORONA_RADII * SOLAR_RADIUS_AU)

        # Create a text list matching the number of points
        text_array_inner_corona = [inner_corona_info for _ in range(len(x))]
        customdata_array_inner_corona = ["Sun: Inner Corona" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1,
                    color='rgb(0, 0, 255)',  # Warmer tint
                    opacity=0.09
                ),
                name='Sun: Inner Corona',
                text=text_array_inner_corona,            # Replicated text
                customdata=customdata_array_inner_corona, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add inner corona shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(0, 0, 255)',
                    size=1,
                    symbol='circle',
                    opacity=0.09
                ),
                name='Sun: Inner Corona',
                text=['Solar Inner Corona (extends to 2-3 solar radii)'],
                hoverinfo='text',
                showlegend=False
            )
        )

        # 2.5. Chromosphere
        x, y, z = create_corona_sphere(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU)

        # Create a text list matching the number of points
        text_array_chromosphere = [chromosphere_info for _ in range(len(x))]
        customdata_array_chromosphere = ["Sun: Chromosphere" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.25,
                    color='rgb(30, 144, 255)',  # approximate visible
                    opacity=0.10
                ),
                name='Sun: Chromosphere',
                text=text_array_chromosphere,            # Replicated text
                customdata=customdata_array_chromosphere, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add chromosphere shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(30, 144, 255)',
                    size=1.25,
                    symbol='circle',
                    opacity=0.10
                ),
                name='Sun: Chromosphere',
                text=['Solar Chromosphere (surface temperature ~6,000 to 20,000 K)'],
                hoverinfo='text',
                showlegend=False
            )
        )

        # 3. Convective Zone and Photoshere Sphere
        x, y, z = create_corona_sphere(SOLAR_RADIUS_AU)

        # Create a text list matching the number of points
        text_array_photosphere = [photosphere_info for _ in range(len(x))]
        customdata_array_photosphere = ["Sun: Photosphere" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=7.0,
                    color='rgb(255, 244, 214)',  # Yellow approximates the visible color
                    opacity=1.0
                ),
                name='Sun: Photosphere',
                text=text_array_photosphere,            # Replicated text
                customdata=customdata_array_photosphere, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add photosphere shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(255, 244, 214)',
                    size=7.0,
                    symbol='circle',
                    opacity=1.0
                ),
                name='Sun: Photosphere',
                text=['Solar Photosphere (surface temperature ~6,000K)'],
                hoverinfo='text',
                showlegend=False
            )
        )
        
        # 4. Radiative Zone
        x, y, z = create_corona_sphere(RADIATIVE_ZONE_AU)

        # Create a text list matching the number of points
        text_array_radiative_zone = [radiative_zone_info for _ in range(len(x))]
        customdata_array_radiative_zone = ["Sun: Radiative Zone" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=7,
                    color='rgb(30, 144, 255)',  # arbitrary color for contrast
                    opacity=1.0
                ),
                name='Sun: Radiative Zone',
                text=text_array_radiative_zone,            # Replicated text
                customdata=customdata_array_radiative_zone, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add radiative zone shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(30, 144, 255)',
                    size=7,
                    symbol='circle',
                    opacity=1.0
                ),
                name='Sun: Radiative Zone',
                text=['Solar Radiative Zone (extends to 0.2 to 0.7 solar radii)'],
                hoverinfo='text',
                showlegend=False
            )
        )

        # 5. Core
        x, y, z = create_corona_sphere(CORE_AU)

        # Create a text list matching the number of points
        text_array_core = [core_info for _ in range(len(x))]
        customdata_array_core = ["Sun: Core" for _ in range(len(x))]

        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=10,
                    color='rgb(70, 130, 180)',  
                    opacity=1.0
                ),
                name='Sun: Core',
                text=text_array_core,            # Replicated text
                customdata=customdata_array_core, # Replicated customdata
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        # Add core shell
        traces.append(
            go.Scatter3d(
                x=[0], y=[0], z=[0],
                mode='markers',
                marker=dict(
                    color='rgb(70, 130, 180)',
                    size=10,
                    symbol='circle',
                    opacity=1.0
                ),
                name='Sun: Core',
                text=['Solar Core (temperature ~15M K)'],
                hoverinfo='text',
                showlegend=False
            )
        )

        return traces

    # Add base traces to figure
    traces = create_layer_traces()
    for trace in traces:
        fig.add_trace(trace)

    # If this is for animation, add the traces to each frame
    if animate and frames is not None:
        for frame in frames:
            frame_data = list(frame.data)  # Convert tuple to list if necessary
            frame_data.extend(traces)
            frame.data = frame_data

    return fig

def create_sun_hover_text():
    """
    Creates hover text for the Sun visualization with information about each layer.
    Future expansion could include dynamic temperature and size data.
    
    Returns:
        dict: Hover text for each layer of the Sun
    """
    return {
        'photosphere': (
            'Sun: Photosphere<br>'
            'Temperature: ~6,000K<br>'
            'Radius: 0.00465 AU'
        ),
        'inner_corona': (
            'Sun: Inner Corona<br>'
            'Temperature: >2,000,000K<br>'
            'Extends to: 2-3 solar radii (~0.014 AU)'
        ),
        'outer_corona': (
            'Sun: Outer Corona<br>'
            'Temperature: ~1,000,000K<br>'
            'Extends to: ~50 solar radii (~0.2 AU)'
        )
    }

# In the create_corona_sphere function, increase the number of points
def create_corona_sphere(radius, n_points=100):  # Increased from 50 to 100 points
    """Create points for a sphere surface to represent corona layers."""
    phi = np.linspace(0, 2*np.pi, n_points)
    theta = np.linspace(-np.pi/2, np.pi/2, n_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    return x.flatten(), y.flatten(), z.flatten()

def get_default_camera():
    """Return the default orthographic camera settings for top-down view"""
    return {
        "projection": {
            "type": "orthographic"
        },
        # Looking straight down the z-axis
        "eye": {"x": 0, "y": 0, "z": 1},  # Position above the x-y plane
        "center": {"x": 0, "y": 0, "z": 0},  # Looking at origin
        "up": {"x": 0, "y": 1, "z": 0}  # "Up" direction aligned with y-axis
    }

def calculate_axis_range(objects_to_plot):
    """Calculate appropriate axis range based on outermost planet"""
    # Find the maximum semi-major axis of selected planets
    max_orbit = max(planetary_params[obj['name']]['a'] 
                   for obj in objects_to_plot 
                   if obj['name'] in planetary_params)
    
    # Add 20% padding
    max_range = max_orbit * 1.2
    
    # Print debug info
    print(f"\nAxis range calculation:")
    print(f"Maximum orbit (AU): {max_orbit}")
    print(f"Range with padding: ±{max_range}")
    
    return [-max_range, max_range]

def plot_actual_orbits(fig, planets_to_plot, dates_lists, center_id='Sun', show_lines=False):
    for planet in planets_to_plot:
        dates_list = dates_lists.get(planet, [])
        if not dates_list:
            print(f"No dates available for {planet}, skipping.")
            continue
        obj_info = next((obj for obj in objects if obj['name'] == planet), None)
        if not obj_info:
            continue
        trajectory = fetch_trajectory(obj_info['id'], dates_list, center_id=center_id, id_type=obj_info.get('id_type'))
        # Now trajectory is a list of positions
        if trajectory:
            x = [pos['x'] for pos in trajectory if pos is not None]
            y = [pos['y'] for pos in trajectory if pos is not None]
            z = [pos['z'] for pos in trajectory if pos is not None]
            if show_lines:
                mode = 'lines'
                line = dict(color=color_map(planet), width=1)
                marker = None
            else:
                mode = 'markers'
                line = None
                marker = dict(color=color_map(planet), size=1)
            fig.add_trace(
                go.Scatter3d(
                    x=x,
                    y=y,
                    z=z,
                    mode=mode,
                    line=line,
                    marker=marker,
                    name=f"{planet} Orbit",
                    hoverinfo='none',
                    hovertemplate=None,
                    showlegend=True
                )
            )

# Function to fetch the position of a celestial object for a specific date
def fetch_position(object_id, date_obj, center_id='Sun', id_type=None, override_location=None, mission_url=None, mission_info=None):
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
        distance_lm = range_ * LIGHT_MINUTES_PER_AU if range_ is not None else 'N/A'
        distance_lh = (distance_lm / 60) if isinstance(distance_lm, float) else 'N/A'

        # Retrieve orbital period from planetary_params if available
        orbital_period = 'N/A'
        if object_id in [obj['id'] for obj in objects]:
            obj_name = next((obj['name'] for obj in objects if obj['id'] == object_id), None)
            if obj_name and obj_name in planetary_params:
                a = planetary_params[obj_name]['a']  # Semi-major axis in AU
                orbital_period_years = np.sqrt(a ** 3)  # Period in Earth years
                orbital_period = f"{orbital_period_years:.2f}"

        return {
            'x': x,
            'y': y,
            'z': z,
            'range': range_,
            'range_rate': range_rate,
            'vx': vx,
            'vy': vy,
            'vz': vz,
            'velocity': velocity,
            'distance_lm': distance_lm,
            'distance_lh': distance_lh,
            'mission_info': mission_info,  # Include mission info if available
            'orbital_period': orbital_period  # Include orbital period
        }
    except Exception as e:
        print(f"Error fetching data for object {object_id} on {date_obj}: {e}")
        return None

def fetch_trajectory_with_batching(obj_id, dates_list, center_id='Sun', id_type=None, batch_size=50):
    """Fetch trajectory data in smaller batches to avoid URL length limits."""
    all_positions = []
    
    # Split dates into smaller batches
    for i in range(0, len(dates_list), batch_size):
        batch_dates = dates_list[i:i + batch_size]
        try:
            obj = Horizons(id=obj_id, id_type=id_type, location='@' + str(center_id), epochs=Time(batch_dates).jd.tolist())
            vectors = obj.vectors()
            
            for j in range(len(vectors)):
                x = float(vectors['x'][j])
                y = float(vectors['y'][j])
                z = float(vectors['z'][j])
                all_positions.append({'x': x, 'y': y, 'z': z, 'date': batch_dates[j]})
                
        except Exception as e:
            print(f"Error fetching batch {i//batch_size + 1} for object {obj_id}: {e}")
            continue
            
    return all_positions if all_positions else None

# Replace existing fetch_trajectory with this version
def fetch_trajectory(obj_id, dates_list, center_id='Sun', id_type=None):
    """Wrapper for backwards compatibility."""
    return fetch_trajectory_with_batching(obj_id, dates_list, center_id, id_type)

def print_planet_positions(positions):
    """Print positions and distances for planets."""
    print("\nCurrent Object Positions:")
    print("=" * 50)
    for name, data in positions.items():
        if data is None:
            print(f"{name:15} No position data available")
            continue
            
        x = data.get('x', 'N/A')
        y = data.get('y', 'N/A')
        z = data.get('z', 'N/A')
        distance = data.get('range', 'N/A')
        
        # Format position information
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
            pos_str = f"({x:8.3f}, {y:8.3f}, {z:8.3f}) AU"
        else:
            pos_str = "Position data unavailable"
            
        # Format distance information
        if isinstance(distance, (int, float)):
            dist_str = f"{distance:8.3f} AU"
        else:
            dist_str = "Distance data unavailable"
        
        print(f"{name:15} Position: {pos_str:35} Distance from center: {dist_str}")
    print("=" * 50)

def format_maybe_float(value):
    """
    If 'value' is a numeric type (int or float), return it formatted
    with 5 decimal places. Otherwise, return 'N/A'.
    """
    if isinstance(value, (int, float)):
        return f"{value:.8f}"
    return "N/A"


def add_celestial_object(fig, obj_data, name, color, symbol='circle', marker_size=DEFAULT_MARKER_SIZE, hover_data="Full Object Info"):

    # Skip if there's no data
    if obj_data is None or obj_data['x'] is None:
        return

    print(f"\nAdding trace for {name}:")

    # Use format_maybe_float() for numeric fields
    distance_au   = format_maybe_float(obj_data.get('range'))
    distance_lm   = format_maybe_float(obj_data.get('distance_lm'))
    distance_lh   = format_maybe_float(obj_data.get('distance_lh'))
    velocity_au   = format_maybe_float(obj_data.get('velocity'))
    orbit_period  = obj_data.get('orbital_period', 'N/A')  # This might be a string

    # Now build your hover text strings
    full_hover_text = (
        f"<b>{name}</b><br><br>"
        f"Distance from Center: {distance_au} AU<br>"
        f"Distance: {distance_lm} light-minutes<br>"
        f"Distance: {distance_lh} light-hours<br>"
        f"Velocity: {velocity_au} AU/day<br>"
        f"Orbital Period: {orbit_period} Earth years"
    )

    if obj_data.get('mission_info'):
        full_hover_text += f"<br>{obj_data['mission_info']}"

    minimal_hover_text = f"<b>{name}</b>"

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

def debug_trajectory_data(objects, selected_objects, center_id='Sun'):
    """Debug function to analyze trajectory data for missions and comets."""
    print("\nTrajectory Debug Analysis:")
    print("=" * 50)
    
    for obj in selected_objects:
        if obj.get('is_satellite', False):
            print(f"\nAnalyzing trajectory for satellite: {obj['name']}")
            print(f"Object ID: {obj['id']}")
            print(f"ID Type: {obj.get('id_type', 'Not specified')}")
            print(f"Center ID: {center_id}")
            
            start_date = obj.get('start_date')
            end_date = obj.get('end_date')
            
            if start_date and end_date:
                total_days = (end_date - start_date).days
                interval = 4  # 4-hour intervals
                dates_list = [start_date + timedelta(hours=i) for i in range(0, total_days * 24 + 1, interval)]
                
                print(f"Date range: {start_date} to {end_date}")
                print(f"Total days: {total_days}")
                print(f"Sample interval: {interval} hours")
                print(f"Number of sample points: {len(dates_list)}")
                
                # Try to fetch first point
                try:
                    first_pos = fetch_position(obj['id'], dates_list[0], center_id=center_id, id_type=obj.get('id_type'))
                    if first_pos:
                        print("\nFirst position fetched successfully:")
                        print(f"X: {first_pos.get('x')}")
                        print(f"Y: {first_pos.get('y')}")
                        print(f"Z: {first_pos.get('z')}")
                    else:
                        print("\nFailed to fetch first position")
                except Exception as e:
                    print(f"\nError fetching first position: {e}")
                
                # Fetch full trajectory
                trajectory = fetch_trajectory(obj['id'], dates_list, center_id=center_id, id_type=obj.get('id_type'))
                if trajectory:
                    print("\nTrajectory data retrieved:")
                    print(f"Number of points: {len(trajectory)}")
                    print(f"First point: {trajectory[0]}")
                    print(f"Last point: {trajectory[-1]}")
                    
                    # Check for any None or invalid points
                    invalid_points = [i for i, pos in enumerate(trajectory) if pos is None or 
                                   any(np.isnan(pos[coord]) for coord in ['x', 'y', 'z'])]
                    if invalid_points:
                        print(f"\nWarning: Found {len(invalid_points)} invalid points at indices: {invalid_points}")
                else:
                    print("\nNo trajectory data returned")
            else:
                print("Missing start_date or end_date")

    print("\nDebug analysis complete")
    print("=" * 50)



def plot_objects():
    """Plot selected objects with proper error handling."""
    try:
        output_label.config(text="Starting data acquisition...")
        progress_bar.start(10)
        root.update_idletasks()

        # Get selected date
        try:
            year = int(entry_year.get())
            month = int(entry_month.get())
            day = int(entry_day.get())
            hour = int(entry_hour.get())
            date_obj = datetime(year, month, day, hour)
        except ValueError:
            output_label.config(text="Invalid date values.")
            progress_bar.stop()
            return

        # Get center object info
        center_object_name = center_object_var.get()
        center_object_info = next((obj for obj in objects if obj['name'] == center_object_name), None)
        if center_object_info:
            center_id = 'Sun' if center_object_name == 'Sun' else center_object_info['id']
            center_id_type = None if center_object_name == 'Sun' else center_object_info.get('id_type')
        else:
            center_id = 'Sun'
            center_id_type = None

        # Create figure
        fig = go.Figure()

        # Add Sun visualization if Sun is center
        if center_object_name == 'Sun':
            fig = create_sun_visualization(fig)
            # Add Sun marker at origin for legend and hover text
            add_celestial_object(
                fig,
                {'x': 0, 'y': 0, 'z': 0,
                 'range': 0,
                 'distance_lm': 0,
                 'distance_lh': 0,
                 'velocity': 0,
                 'orbital_period': 'N/A'
                },
                'Sun',
                color_map('Sun'),
                'circle',
                marker_size=CENTER_MARKER_SIZE
            )
        else:
            # Fetch position of center object if not the Sun
            center_pos = fetch_position(center_object_info['id'], date_obj, 
                                     center_id='399', # Use Earth as reference for non-Sun centers
                                     id_type=center_object_info.get('id_type'))
            if center_pos:
                add_celestial_object(
                    fig, 
                    {'x': 0, 'y': 0, 'z': 0}, # Plot at origin since everything is relative
                    center_object_name,
                    center_object_info['color'],
                    center_object_info['symbol'],
                    marker_size=CENTER_MARKER_SIZE
                )

        # Get selected objects
        selected_objects = [obj for obj in objects if obj['var'].get() == 1 and obj['name'] != center_object_name]
                
        # Add debug code here
        debug_trajectory_data(objects, selected_objects, center_id)

        # Calculate trajectories for missions and comets
        trajectories = {}
        for obj in selected_objects:

            if obj.get('is_satellite', False):
                # Get the parent planet's ID (first digit + 99)
                parent_planet_id = obj['id'][0] + '99'
                parent_planet_name = {
                    '399': 'Earth',
                    '499': 'Mars',
                    '599': 'Jupiter',       # 599 or 5
                    '699': 'Saturn',
                    '799': 'Uranus',
                    '899': 'Neptune',
                    '999': 'Pluto',
                    '20136199': 'Eris'        
                }.get(parent_planet_id)

                # Only plot satellite trajectory if its parent is the center
                if parent_planet_name == center_object_name:
                    dates_list = []
                    delta = timedelta(hours=4)  # 4-hour steps for smooth orbits
                    current_date = obj['start_date']
                    while current_date <= obj['end_date']:
                        dates_list.append(current_date)
                        current_date += delta

                    trajectory = fetch_trajectory(
                        obj['id'],
                        dates_list,
                        center_id=center_id,  # Use selected center
                        id_type='majorbody'
                    )

                    if trajectory:
                        x = [pos['x'] for pos in trajectory if pos is not None]
                        y = [pos['y'] for pos in trajectory if pos is not None]
                        z = [pos['z'] for pos in trajectory if pos is not None]

                        fig.add_trace(go.Scatter3d(
                            x=x, y=y, z=z,
                            mode='lines',
                            line=dict(color=obj['color'], width=1),
                            name=f"{obj['name']} Orbit",
                            hoverinfo='none',
                            showlegend=True
                        ))
    #        else:

            if obj.get('is_mission', False) or obj.get('is_comet', False):
#            if obj.get('is_mission', False) or obj.get('is_comet', False) or obj.get('is_satellite', False):  # adds satellite traces
                # Get original start/end dates from object definition
                start_date = obj.get('start_date')
                end_date = obj.get('end_date')
                
                if start_date and end_date:
                    total_days = (end_date - start_date).days
                    interval = max(1, total_days // 100)
                    dates_list = [start_date + timedelta(days=i) for i in range(0, total_days + 1, interval)]
                    trajectory = fetch_trajectory(obj['id'], dates_list, center_id=center_id, id_type=obj.get('id_type'))
                    if trajectory:
                        trajectories[obj['name']] = trajectory
                        
        # Fetch positions
        positions = {}
        for obj in selected_objects:
            pos = fetch_position(obj['id'], date_obj, center_id=center_id, 
                               id_type=obj.get('id_type'),
                               mission_info=obj.get('mission_info'))
            if pos is not None:
                positions[obj['name']] = pos

        # Plot trajectories
        for name, trajectory in trajectories.items():
            obj_info = next((obj for obj in objects if obj['name'] == name), None)
            if obj_info:
                x = [pos['x'] for pos in trajectory if pos is not None]
                y = [pos['y'] for pos in trajectory if pos is not None]
                z = [pos['z'] for pos in trajectory if pos is not None]
                
                fig.add_trace(
                    go.Scatter3d(
                        x=x, y=y, z=z,
                        mode='lines',
                        line=dict(color=obj_info['color'], width=1),
                        name=f"{name} Path",
                        hoverinfo='skip',
                        showlegend=True
                    )
                )

        # Add objects to plot
        for obj in selected_objects:
            if obj['name'] in positions:
                add_celestial_object(
                    fig, positions[obj['name']], obj['name'],
                    obj['color'], obj['symbol']
                )

        # Plot idealized orbits if Sun is center
        if center_object_name == 'Sun':
            selected_objects = [obj['name'] for obj in objects if obj['var'].get() == 1]
            plot_idealized_orbits(fig, selected_objects, center_id=center_object_name)

        # Calculate coordinate ranges including trajectories
        x_coords = []
        y_coords = []
        z_coords = []
        
        # Include regular object positions
        for obj_data in positions.values():
            if obj_data and obj_data['x'] is not None:
                x_coords.append(obj_data['x'])
                y_coords.append(obj_data['y'])
                z_coords.append(obj_data['z'])

        # Include trajectory points
        for trajectory in trajectories.values():
            for pos in trajectory:
                if pos:
                    x_coords.append(pos['x'])
                    y_coords.append(pos['y'])
                    z_coords.append(pos['z'])

        # Decide on scale
        if scale_var.get() == 'Auto':
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
                axis_range = [-1, 1]
        else:
            try:
                custom_scale = float(custom_scale_entry.get())
                axis_range = [-custom_scale, custom_scale]
            except ValueError:
                output_label.config(text="Invalid custom scale value.")
                progress_bar.stop()
                return

        # Update layout
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X (AU)', range=axis_range, backgroundcolor='black', 
                          gridcolor='gray', showbackground=True),
                yaxis=dict(title='Y (AU)', range=axis_range, backgroundcolor='black', 
                          gridcolor='gray', showbackground=True),
                zaxis=dict(title='Z (AU)', range=axis_range, backgroundcolor='black', 
                          gridcolor='gray', showbackground=True),
                aspectmode='cube',
                camera=get_default_camera()
            ),
            paper_bgcolor='black',
            plot_bgcolor='black',
            title_font_color='white',
            font_color='white',
            title=f"Paloma's Orrery for {date_obj.strftime('%B %d, %Y')}",
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
                    y=0,
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
                    y=-0.05,
                    showarrow=False,
                    font=dict(size=12, color='white'),
                    align='left',
                    xanchor='left',
                    yanchor='top'
                ),
                dict(
                    text="Click on the legend items to<br>toggle them off and back on.",
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

        # Add hover toggle buttons
        fig = add_hover_toggle_buttons(fig)

        # Generate default name with timestamp
        current_date = datetime.now()
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

def plot_idealized_orbits(fig, objects_to_plot, center_id='Sun'):
    """
    Plot idealized orbits for planets, dwarf planets, asteroids, and KBOs only.
    Skip satellites, comets, and missions as their trajectories are too complex 
    or dynamic for simple Keplerian elements.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add orbits to
        objects_to_plot (list): List of object names to potentially plot orbits for
        center_id (str): The central body ('Sun' or a planet name)
    """
    import numpy as np
    import math
    import plotly.graph_objs as go

    def rotate_points(x, y, z, angle, axis='z'):
        """
        Rotates points (x,y,z) about the given axis by 'angle' radians.
        Returns (xr, yr, zr) as numpy arrays.
        """
        xr = np.array(x, copy=True)
        yr = np.array(y, copy=True)
        zr = np.array(z, copy=True)

        if axis == 'z':
            xr = x * math.cos(angle) - y * math.sin(angle)
            yr = x * math.sin(angle) + y * math.cos(angle)
            # zr stays the same
        elif axis == 'x':
            yr = y * math.cos(angle) - z * math.sin(angle)
            zr = y * math.sin(angle) + z * math.cos(angle)
        elif axis == 'y':
            zr = z * math.cos(angle) - x * math.sin(angle)
            xr = z * math.sin(angle) + x * math.cos(angle)

        return (xr, yr, zr)

    # If center is the Sun, plot orbits for selected heliocentric objects
    if center_id == 'Sun':

        # Track skipped objects by category
        skipped = {
            'satellites': [],
            'comets': [],
            'missions': [],
            'no_params': [],
            'invalid_orbit': []
        }

        plotted = []

        for obj_name in objects_to_plot:
            # Find the object in the objects list
            obj_info = next((obj for obj in objects if obj['name'] == obj_name), None)
            if obj_info is None:
                continue
                
            # Check each skip condition and record the reason
            if obj_name not in planetary_params:
                skipped['no_params'].append(obj_name)
                continue
            elif obj_name in parent_planets:
                skipped['satellites'].append(obj_name)
                continue
            elif obj_info.get('is_comet', False):
                skipped['comets'].append(obj_name)
                continue
            elif obj_info.get('is_mission', False):
                skipped['missions'].append(obj_name)
                continue
            
            params = planetary_params[obj_name]
            # e.g. a = params['a'], e = params['e'], i = params['i'], etc.
            a = params.get('a', 0)

            # Skip if semi-major axis is zero or very small
            if a < 0.0001:
                continue

            e = params.get('e', 0)
            i = params.get('i', 0)
            omega = params.get('omega', 0)
            Omega = params.get('Omega', 0)

            # Generate ellipse in orbital plane
            theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            
            x_orbit = r * np.cos(theta)
            y_orbit = r * np.sin(theta)
            z_orbit = np.zeros_like(theta)

            # Convert angles to radians
            i_rad = math.radians(i)
            omega_rad = math.radians(omega)
            Omega_rad = math.radians(Omega)

            # Rotate ellipse by argument of periapsis (ω) around z-axis
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
            # Then rotate by inclination (i) around x-axis
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
            # Then rotate by longitude of ascending node (Ω) around z-axis
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')

            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='dot', width=1, color='white'),
                    name=f"{obj_name} Ideal Orbit (Sun-centered)",
                    hoverinfo='name'
                )
            )

            plotted.append(obj_name)

        # Print summary of plotted and skipped objects
        print("\nIdeal Orbit Summary:")
        print(f"Plotted ideal orbits for {len(plotted)} objects:")
        for obj in plotted:
            print(f"  - {obj}")

        print("\nSkipped ideal orbits for:")
        if skipped['satellites']:
            print(f"\nPlanetary Satellites ({len(skipped['satellites'])}):")
            for obj in skipped['satellites']:
                print(f"  - {obj}")
        
        if skipped['comets']:
            print(f"\nComets ({len(skipped['comets'])}):")
            for obj in skipped['comets']:
                print(f"  - {obj}")
                
        if skipped['missions']:
            print(f"\nSpace Missions ({len(skipped['missions'])}):")
            for obj in skipped['missions']:
                print(f"  - {obj}")
                
        if skipped['no_params']:
            print(f"\nNo Orbital Parameters ({len(skipped['no_params'])}):")
            for obj in skipped['no_params']:
                print(f"  - {obj}")
                
        if skipped['invalid_orbit']:
            print(f"\nInvalid Orbital Parameters ({len(skipped['invalid_orbit'])}):")
            for obj in skipped['invalid_orbit']:
                print(f"  - {obj}")
    else:
        # No idealized orbits for planetary satellites
        print(f"\nNo ideal orbits plotted - center is {center_id} (not Sun)")

    return fig

def show_animation_safely(fig, default_name):
    """Show and optionally save an animated Plotly figure with proper cleanup."""
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import webbrowser
    import os
    import tempfile
    
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    save_response = messagebox.askyesno(
        "Save Animation",
        "Would you like to save this animation as an interactive HTML file?\n"
        "Click 'Yes' to save, or 'No' to continue without saving.",
        parent=root
    )
    
    try:

        if save_response:
            # Get save location from user
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            
            if file_path:
                # Save directly to user's chosen location
                fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                print(f"Animation saved to {file_path}")
                webbrowser.open(f'file://{os.path.abspath(file_path)}')
        else:

            # If user doesn't want to save, just display the animation temporarily
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
                temp_path = tmp.name
                fig.write_html(temp_path, include_plotlyjs='cdn', auto_play=False)
                webbrowser.open(f'file://{os.path.abspath(temp_path)}')
                
                # Schedule cleanup of temporary file
                def cleanup_temp():
                    try:
                        if os.path.exists(temp_path):
                            os.unlink(temp_path)
                    except Exception as e:
                        print(f"Error cleaning up temporary file: {e}")
                
                # Schedule cleanup after a delay to ensure browser has loaded the file
                root.after(5000, cleanup_temp)
    
    except Exception as e:
        messagebox.showerror(
            "Save Error",
            f"An error occurred:\n{str(e)}",
            parent=root
        )
    finally:
        root.destroy()

def animate_objects(step, label):
    """Create animation of solar system objects without threading."""
    try:
        # Setup
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

        # Generate dates list
        current_date = datetime(int(entry_year.get()), int(entry_month.get()), 
                            int(entry_day.get()), int(entry_hour.get()))
        dates_list = []

        for i in range(N):
            if step == 'month':
                month_offset = current_date.month - 1 + i
                year = current_date.year + month_offset // 12
                month = month_offset % 12 + 1
                day = min(current_date.day, calendar.monthrange(year, month)[1])
                date = datetime(year, month, day, current_date.hour)
            elif step == 'year':
                try:
                    date = current_date.replace(year=current_date.year + i)
                except ValueError:
                    date = current_date.replace(year=current_date.year + i, month=2, day=28)
            else:
                date = current_date + step * i
            if date > HORIZONS_MAX_DATE:
                print(f"Date {date} exceeds Horizons' data range. Skipping further dates.")
                break
            dates_list.append(date)

        # Initialize figure
        fig = go.Figure()

        # If center is the Sun, draw its layered visualization 
        if center_object_name == 'Sun':
            fig = create_sun_visualization(fig)
        else:
            # Add center object marker
            fig.add_trace(
                go.Scatter3d(
                    x=[0], y=[0], z=[0],
                    mode='markers+text',
                    marker=dict(
                        color=center_object_info['color'],
                        size=CENTER_MARKER_SIZE,
                        symbol=center_object_info['symbol']
                    ),
                    name=f"{center_object_name} (Center)",
                    text=[center_object_name],
                    hoverinfo='skip',
                    showlegend=True
                )
            )

        # Add center marker
        center_marker_size = CENTER_MARKER_SIZE
        fig.add_trace(
            go.Scatter3d(
                x=[0],
                y=[0],
                z=[0],
                mode='markers+text',
                marker=dict(
                    color=center_object_info['color'],
                    size=center_marker_size,
                    symbol=center_object_info['symbol']
                ),
                name=center_object_name,
                text=[center_object_name],
                hoverinfo='skip',
                showlegend=True
            )
        )

        # Fetch positions for all objects
        positions_over_time = {}
        for obj in objects:
            if obj['var'].get() == 1 and obj['name'] != center_object_name:
                positions = fetch_trajectory(obj['id'], dates_list, center_id=center_id, 
                                        id_type=obj.get('id_type'))
                positions_over_time[obj['name']] = positions

        # Create initial traces and track indices
        trace_indices = []
        for obj in objects:
            if obj['var'].get() == 1 and obj['name'] != center_object_name:
                obj_positions = positions_over_time.get(obj['name'])
                if obj_positions and obj_positions[0]:
                    obj_data = obj_positions[0]
                    distance_from_origin = np.sqrt(obj_data['x']**2 + 
                                                obj_data['y']**2 + 
                                                obj_data['z']**2)
                    hover_texts = format_hover_text({
                        'range': distance_from_origin,
                        'mission_info': obj.get('mission_info', '')
                    }, obj['name'], True)
                    
                    full_hover_text = hover_texts[0]
                    minimal_hover_text = hover_texts[1]

                    fig.add_trace(
                        go.Scatter3d(
                            x=[obj_data['x']],
                            y=[obj_data['y']],
                            z=[obj_data['z']],
                            mode='markers',
                            marker=dict(symbol=obj['symbol'], color=obj['color'], size=6),
                            name=obj['name'],
                            text=[full_hover_text],
                            customdata=[minimal_hover_text],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )
                else:
                    fig.add_trace(
                        go.Scatter3d(
                            x=[None], y=[None], z=[None],
                            mode='markers+text',
                            marker=dict(symbol=obj['symbol'], color=obj['color'], size=6),
                            name=obj['name'],
                            text=[obj['name']],
                            textposition='top center',
                            textfont=dict(size=8, color='white'),
                            customdata=[['N/A', obj.get('mission_info')]],
                            hovertemplate=(
                                f"{obj['name']}<br>"
                                "Distance from center: N/A<br>"
                                "<extra></extra>"
                            ),
                            showlegend=True
                        )
                    )
                trace_indices.append(len(fig.data) - 1)

        # Create frames
        frames = []
        for i in range(N):
            frame_data = []
            current_date = dates_list[i]

            for obj in objects:
                if obj['var'].get() == 1 and obj['name'] != center_object_name:
                    if 'start_date' in obj and current_date < obj['start_date']:
                        frame_data.append(dict(visible=False))
                    else:
                        obj_positions = positions_over_time.get(obj['name'])
                        if obj_positions and obj_positions[i]:
                            obj_data = obj_positions[i]
                            distance_from_origin = np.sqrt(obj_data['x']**2 + 
                                                        obj_data['y']**2 + 
                                                        obj_data['z']**2)
                            
                            distance_lm = distance_from_origin * LIGHT_MINUTES_PER_AU
                            distance_lh = distance_lm / 60

                            frame_data.append(dict(
                                type='scatter3d',
                                x=[obj_data['x']],
                                y=[obj_data['y']],
                                z=[obj_data['z']],
                                text=[f"<b>{obj['name']}</b><br><br>"
                                    f"Distance from Center: {distance_from_origin:.8f} AU<br>"
                                    + (f"<br>{obj.get('mission_info', '')}" if obj.get('mission_info') else "")],
                                customdata=[f"<b>{obj['name']}</b>"],
                                hovertemplate='%{text}<extra></extra>',
                                visible=True
                            ))
                        else:
                            frame_data.append(dict(visible=False))

            frames.append(go.Frame(
                data=frame_data,
                traces=trace_indices,
                name=str(dates_list[i].strftime('%Y-%m-%d %H:00'))
            ))

        # Calculate and set axis ranges
        x_coords = []
        y_coords = []
        z_coords = []
        for obj_name, positions in positions_over_time.items():
            for pos in positions:
                if pos:
                    x_coords.append(pos['x'])
                    y_coords.append(pos['y'])
                    z_coords.append(pos['z'])

        if x_coords and y_coords and z_coords:
            max_coord = max(
                abs(max(x_coords)), abs(min(x_coords)),
                abs(max(y_coords)), abs(min(y_coords)),
                abs(max(z_coords)), abs(min(z_coords))
            )
            max_coord *= 1.2
            axis_range = [-max_coord, max_coord]
        else:
            axis_range = [-1, 1]

        if scale_var.get() == 'Manual':
            try:
                custom_scale = float(custom_scale_entry.get())
                if custom_scale > 0:
                    axis_range = [-custom_scale, custom_scale]
            except ValueError:
                pass

        selected_objects = [
            obj['name']
            for obj in objects
            if obj['var'].get() == 1 and not obj.get('is_mission', False)
        ]

        plot_idealized_orbits(fig, selected_objects, center_id=center_object_name)

        # Update layout
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
            updatemenus=[
                dict(
                    type='buttons',
                    showactive=False,
                    buttons=[
                        dict(label='Play',
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
            ],
            sliders=[dict(
                active=0,
                steps=[dict(method='animate',
                            args=[[str(dates_list[k].strftime('%Y-%m-%d %H:00'))],
                                {'frame': {'duration': 500, 'redraw': True},
                                'mode': 'immediate'}],
                            label=dates_list[k].strftime('%Y-%m-%d %H:00')) for k in range(N)],
                transition=dict(duration=0),
                x=0,
                y=0,
                currentvalue=dict(font=dict(size=14), prefix='Date: ', visible=True, xanchor='center'),
                len=1.0
            )]
        )

        # Add frames to figure
        fig.frames = frames

        # Add hover toggle buttons
        fig = add_hover_toggle_buttons(fig)

        # Generate default name with timestamp
        current_date = datetime.now()
        default_name = f"solar_system_animation_{current_date.strftime('%Y%m%d_%H%M')}"
        show_animation_safely(fig, default_name)

        output_label.config(
            text="Animation opened in browser. "
                "Use your browser's File -> Save As to save the animation if desired."
        )
        progress_bar.stop()

    except Exception as e:
        output_label.config(text=f"Error during animation: {e}")
        print(f"Error during animation: {e}")
        traceback.print_exc()
        progress_bar.stop()

def on_closing():
    """Handle cleanup when the main window is closed."""
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

# Add the closing protocol to the root window
root.protocol("WM_DELETE_WINDOW", on_closing)

# Function to fill today's date into the entry fields
def fill_now():
    now = datetime.now()
    update_date_fields(now)

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

# Function to handle mission selection (no longer adjusts date)
def handle_mission_selection():
    # Function no longer adjusts the date based on mission selection
    pass

# Animation Functions

def animate_one_day():
    animate_objects(timedelta(days=1), "Day") 

 # Add the new animate_one_week function
def animate_one_week():
    animate_objects(timedelta(weeks=1), "Week")            

def animate_one_month():
    animate_objects('month', "Month")

def animate_one_year():
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

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=(10, 5), pady=(10, 10), sticky='n')

# Configure grid weights within input_frame for proper spacing
input_frame.grid_rowconfigure(0, weight=0)  # Row for date inputs
input_frame.grid_rowconfigure(1, weight=1)  # Row for __frame
for col in range(0, 9):
    input_frame.grid_columnconfigure(col, weight=1)  # Allow columns to expand if needed

# Create a separate frame for date fields and the "Now" button
date_frame = tk.Frame(input_frame)
date_frame.grid(row=0, column=0, columnspan=9, padx=(0, 0), pady=2, sticky='w')

# Define date labels and entries with reduced padding
label_year = tk.Label(date_frame, text="Dates in UTC, Year:")
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

# "Now" button with minimal padding
now_button = tk.Button(date_frame, text="Now", command=fill_now)
now_button.grid(row=0, column=8, padx=(2, 0), pady=2, sticky='w')
CreateToolTip(now_button, "Fill the current date and time")

# Scrollable frame for celestial objects and missions
scrollable_frame = ScrollableFrame(input_frame, width=430, height=710)  # Adjust width and height as needed
scrollable_frame.grid(row=1, column=0, columnspan=9, pady=(10, 5), sticky='nsew')

# Prevent the ScrollableFrame from resizing based on its content
scrollable_frame.config(width=430, height=710)
scrollable_frame.pack_propagate(False)  # Disable automatic resizing

# Optionally, set the inner frame size slightly smaller
scrollable_frame.scrollable_frame.config(width=410, height=690)
scrollable_frame.scrollable_frame.pack_propagate(False)

# Define selection variables for each object
# Set inner planets selected by default
sun_var = tk.IntVar(value=0)  
mercury_var = tk.IntVar(value=1) # default
venus_var = tk.IntVar(value=1) # default
earth_var = tk.IntVar(value=1)  # Set Earth to 1 to preselect it by default
moon_var = tk.IntVar(value=0)  
pt5_var = tk.IntVar(value=0)
mars_var = tk.IntVar(value=1) # default
ceres_var = tk.IntVar(value=0)
jupiter_var = tk.IntVar(value=0)
saturn_var = tk.IntVar(value=0)
uranus_var = tk.IntVar(value=0)
neptune_var = tk.IntVar(value=0)
pluto_var = tk.IntVar(value=0)
haumea_var = tk.IntVar(value=0)
makemake_var = tk.IntVar(value=0)
eris_var = tk.IntVar(value=0)
voyager1_var = tk.IntVar(value=0)
voyager1h_var = tk.IntVar(value=0)
voyager2_var = tk.IntVar(value=0)
cassini_var = tk.IntVar(value=0)
new_horizons_var = tk.IntVar(value=0)
juno_var = tk.IntVar(value=0)
galileo_var = tk.IntVar(value=0)
pioneer10_var = tk.IntVar(value=0)
pioneer11_var = tk.IntVar(value=0)
europa_clipper_var = tk.IntVar(value=0)
osiris_rex_var = tk.IntVar(value=0)
parker_solar_probe_var = tk.IntVar(value=0)
jwst_var = tk.IntVar(value=0)
rosetta_var = tk.IntVar(value=0)
bepicolombo_var = tk.IntVar(value=0)
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
bennu_var = tk.IntVar(value=0)  # 0 means unselected by default
steins_var = tk.IntVar(value=0)  # 0 means unselected by default
# Define IntVar variables for new objects
soho_var = tk.IntVar(value=0)
ryugu_var = tk.IntVar(value=0)
eros_var = tk.IntVar(value=0)
itokawa_var = tk.IntVar(value=0)
change_var = tk.IntVar(value=0)
perse_var = tk.IntVar(value=0)
dart_var = tk.IntVar(value=0)
lucy_var = tk.IntVar(value=0)
nix_var = tk.IntVar(value=0)
kbo_var = tk.IntVar(value=0)
gaia_var = tk.IntVar(value=0)
hayabusa2_var = tk.IntVar(value=0)  # 0 means unselected by default
hydra_var = tk.IntVar(value=0)  # 0 means unselected by default
# Define IntVar variables for Kuiper Belt Objects
quaoar_var = tk.IntVar(value=0)
sedna_var = tk.IntVar(value=0)
orcus_var = tk.IntVar(value=0)    # 0 means unselected by default
varuna_var = tk.IntVar(value=0)
gv9_var = tk.IntVar(value=0)
ms4_var = tk.IntVar(value=0)
dw_var = tk.IntVar(value=0)
or10_var = tk.IntVar(value=0)
ixion_var = tk.IntVar(value=0)

# New Selection Variables for Major Moons

# Mars' Moons
phobos_var = tk.IntVar(value=0)
deimos_var = tk.IntVar(value=0)

# Jupiter's Galilean Moons
io_var = tk.IntVar(value=0)
europa_var = tk.IntVar(value=0)
ganymede_var = tk.IntVar(value=0)
callisto_var = tk.IntVar(value=0)

# Saturn's Major Moons
titan_var = tk.IntVar(value=0)
enceladus_var = tk.IntVar(value=0)
rhea_var = tk.IntVar(value=0)
dione_var = tk.IntVar(value=0)
tethys_var = tk.IntVar(value=0)
mimas_var = tk.IntVar(value=0)
phoebe_var = tk.IntVar(value=0)

# Uranus's Major Moons
oberon_var = tk.IntVar(value=0)
umbriel_var = tk.IntVar(value=0)
ariel_var = tk.IntVar(value=0)
miranda_var = tk.IntVar(value=0)
titania_var = tk.IntVar(value=0)

# Neptune's Major Moon
triton_var = tk.IntVar(value=0)

# Pluto's Moon
charon_var = tk.IntVar(value=0)

# Eris's Moon
dysnomia_var = tk.IntVar(value=0)

# Proxima Centauri variable
proxima_var = tk.IntVar(value=0)  

# Scrollable frame for celestial objects and missions
scrollable_frame = ScrollableFrame(input_frame)
scrollable_frame.grid(row=1, column=0, columnspan=9, pady=(10, 5), sticky='nsew')

# Tooltip for scrollable frame
CreateToolTip(scrollable_frame.scrollable_frame, "Use the scrollbar to see all objects. Categories include:\n" 
              "- Planets and Dwarf Planets;\n- Moons, Asteroids, and Kuiper Belt Objects;\n- Space Missions;\n" 
              "- Comets and Interstellar Objects!\n"
              "Select a start date for plotting within the range for all objects selected. The default start date is \'Now\'.")

# Checkbuttons for celestial objects
celestial_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Planets, Dwarf Planets, Moons, Asteroids, and Kuiper" 
                                "Belt Objects")
celestial_frame.pack(pady=(10, 5), fill='x')

def create_celestial_checkbutton(name, variable):
    # For main planets and Sun, make a bold label
    if name in ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']:
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
create_celestial_checkbutton("Mercury", mercury_var)
create_celestial_checkbutton("Venus", venus_var)
create_celestial_checkbutton("Earth", earth_var)
create_celestial_checkbutton("- Moon", moon_var)
create_celestial_checkbutton("- 2024 PT5", pt5_var)
create_celestial_checkbutton("Mars", mars_var)
create_celestial_checkbutton("- Phobos", phobos_var)
create_celestial_checkbutton("- Deimos", deimos_var)
create_celestial_checkbutton("Ceres", ceres_var)
create_celestial_checkbutton("Apophis", apophis_var)
create_celestial_checkbutton("Bennu", bennu_var)
create_celestial_checkbutton("Šteins", steins_var)
create_celestial_checkbutton("Vesta", vesta_var)
create_celestial_checkbutton("Ryugu", ryugu_var)
create_celestial_checkbutton("Eros", eros_var)
create_celestial_checkbutton("Itokawa", itokawa_var)
create_celestial_checkbutton("Jupiter", jupiter_var)
create_celestial_checkbutton("- Io", io_var)
create_celestial_checkbutton("- Europa", europa_var)
create_celestial_checkbutton("- Ganymede", ganymede_var)
create_celestial_checkbutton("- Callisto", callisto_var)
create_celestial_checkbutton("Saturn", saturn_var)
create_celestial_checkbutton("- Titan", titan_var)
create_celestial_checkbutton("- Enceladus", enceladus_var)
create_celestial_checkbutton("- Rhea", rhea_var)
create_celestial_checkbutton("- Dione", dione_var)
create_celestial_checkbutton("- Tethys", tethys_var)
create_celestial_checkbutton("- Mimas", mimas_var)
create_celestial_checkbutton("- Phoebe", phoebe_var)
create_celestial_checkbutton("Uranus", uranus_var)
create_celestial_checkbutton("- Oberon", oberon_var)
create_celestial_checkbutton("- Umbriel", umbriel_var)
create_celestial_checkbutton("- Ariel", ariel_var)
create_celestial_checkbutton("- Miranda", miranda_var)
create_celestial_checkbutton("- Titania", titania_var)
create_celestial_checkbutton("Neptune", neptune_var)
create_celestial_checkbutton("- Triton", triton_var)
create_celestial_checkbutton("Pluto", pluto_var)
create_celestial_checkbutton("- Charon", charon_var)
create_celestial_checkbutton("- Nix", nix_var)
create_celestial_checkbutton("- Hydra", hydra_var)
create_celestial_checkbutton("Haumea", haumea_var)
create_celestial_checkbutton("Makemake", makemake_var)
create_celestial_checkbutton("Eris", eris_var)
create_celestial_checkbutton("- Dysnomia", dysnomia_var)

# LabelFrame for Kuiper Belt Objects
kbo_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Kuiper Belt Objects (KBOs)")
kbo_frame.pack(pady=(10, 5), fill='x')

# Create checkbuttons for each Kuiper Belt Object within the kbo_frame

create_celestial_checkbutton("Quaoar", quaoar_var)
create_celestial_checkbutton("Sedna", sedna_var)
create_celestial_checkbutton("Orcus", orcus_var)
create_celestial_checkbutton("Varuna", varuna_var)
create_celestial_checkbutton("Ixion", ixion_var)
create_celestial_checkbutton("GV9", gv9_var)
create_celestial_checkbutton("MS4", ms4_var)
create_celestial_checkbutton("OR10", or10_var)

# create_celestial_checkbutton("NAME Proxima Centauri", proxima_var)

# Checkbuttons for missions
mission_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Space Missions")
mission_frame.pack(pady=(10, 5), fill='x')

def create_mission_checkbutton(name, variable, dates):
    checkbutton = tk.Checkbutton(mission_frame, text=f"{name} {dates}", variable=variable, command=handle_mission_selection)
    checkbutton.pack(anchor='w')
    info_text = INFO.get(name, "No information available")
    tooltip_text = f"{info_text}\nMission duration: {dates}"
    if 'mission_url' in INFO:
        tooltip_text += f"\nMore Info: {INFO['mission_url']}"
    CreateToolTip(checkbutton, tooltip_text)

create_mission_checkbutton("Pioneer 10", pioneer10_var, "(1972-03-03 to 2003-01-23)")
create_mission_checkbutton("Pioneer 11", pioneer11_var, "(1973-04-06 to 1995-09-30)")
create_mission_checkbutton("Voyager 2", voyager2_var, "(1977-08-20 to present)")
create_mission_checkbutton("Voyager 1", voyager1_var, "(1977-09-05 to present)")
# create_mission_checkbutton("Voyager 1 to heliopause", voyager1h_var, "(1977-09-05 to 2012-08-25)")
create_mission_checkbutton("Galileo", galileo_var, "(1989-10-18 to 2003-09-21)")
create_mission_checkbutton("Cassini-Huygens", cassini_var, "(1997-10-15 to 2017-09-15)")
create_mission_checkbutton("SOHO: Solar and Heliospheric Observatory", soho_var, "(1995-12-2 to present)")
create_mission_checkbutton("Rosetta", rosetta_var, "(2004-03-02 to 2016-09-30)")
create_mission_checkbutton("New Horizons", new_horizons_var, "(2006-01-19 to present)")
create_mission_checkbutton("Chang'e", change_var, "(2007-10-24 to present)")
create_mission_checkbutton("Juno", juno_var, "(2011-08-05 to present)")
create_mission_checkbutton("Gaia", gaia_var, "(2013-12-19 to 2025-12-31)")
create_mission_checkbutton("Hayabusa2", hayabusa2_var, "(2014-12-03 to 2020-12-05)")
create_mission_checkbutton("OSIRIS-REx", osiris_rex_var, "(2016-09-08 to 2023-09-24)")
create_mission_checkbutton("Parker Solar Probe", parker_solar_probe_var, "(2018-08-12 to present)")
create_mission_checkbutton("BepiColombo", bepicolombo_var, "(2018-10-20 to 2025-12-31)")
create_mission_checkbutton("Perseverance Rover", perse_var, "(2020-07-30 to present)")
create_mission_checkbutton("Lucy Mission", lucy_var, "(2021-10-17 to 2033-05-01)")
create_mission_checkbutton("DART Mission", dart_var, "(2021-11-25 to 2022-09-25)")
create_mission_checkbutton("James Webb Space Telescope", jwst_var, "(2021-12-25 to present)")
create_mission_checkbutton("Europa Clipper", europa_clipper_var, "(2024-10-14 to April 2030)")

# Checkbuttons for comets
comet_frame = tk.LabelFrame(scrollable_frame.scrollable_frame, text="Select Comets and Interstellar Objects")
comet_frame.pack(pady=(10, 5), fill='x')

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


create_comet_checkbutton("Ikeya-Seki", comet_ikeya_seki_var, "(1965-09-18 to 1966-01-01)", 
                         "October 21, 1965")
#create_comet_checkbutton("Ikeya-Seki", comet_ikeya_seki_var, "(1965-09-18 to 2025-01-01)",  # the trajectory does not extend beyond 1966-01-01
#                         "October 21, 1965")
create_comet_checkbutton("West", comet_west_var, "(1975-11-05 to 1976-06-01)", 
                         "February 25, 1976")
create_comet_checkbutton("Halley", comet_halley_var, "(1982-11-26 to 1995-10-20)", 
                         "February 9, 1986")
create_comet_checkbutton("Hyakutake", comet_hyakutake_var, "(1995-12-01 to 1996-06-01)", 
                         "May 1, 1996")
create_comet_checkbutton("Hale-Bopp", comet_hale_bopp_var, "(1995-07-23 to 2001-12-31)", 
                         "April 1, 1997")
create_comet_checkbutton("McNaught", comet_mcnaught_var, "(2006-08-07 to 2008-06-01)", 
                         "January 12, 2007")
create_comet_checkbutton("Churyumov-Gerasimenko", comet_Churyumov_Gerasimenko_var, "(2002-11-22 to 2021-05-01)", 
    "August 13, 2015")
create_comet_checkbutton("Oumuamua", oumuamua_var, "(2017-10-14 to 2018-01-01)", 
                         "September 9, 2017")
create_comet_checkbutton("Borisov", comet_borisov_var, "(2019-08-30 to 2020-10-01)", 
    "December 8, 2019")
create_comet_checkbutton("NEOWISE", comet_neowise_var, "(2020-03-27 to 2021-06-01)", 
                         "July 3, 2020")
create_comet_checkbutton("Tsuchinshan-ATLAS", comet_tsuchinshan_atlas_var, "(2023-01-09 to present)", 
                         "April 28, 2024")
create_comet_checkbutton("ATLAS", comet_atlas_var, "(2024-06-17 to present)", 
                         "January 13, 2025")

# Controls in controls_frame (Scale Options and beyond)

# Scale Options
scale_frame = tk.LabelFrame(controls_frame, text="Scale Options for Solar System Plots")
scale_frame.pack(pady=(5, 5), fill='x')

scale_var = tk.StringVar(value='Auto')

auto_scale_radio = tk.Radiobutton(scale_frame, text="Automatic Scaling of Your Plot", variable=scale_var, value='Auto')
auto_scale_radio.pack(anchor='w')
CreateToolTip(auto_scale_radio, "Automatically adjust scale based on selected objects")

manual_scale_radio = tk.Radiobutton(scale_frame, text="Or Manually Enter Scale of Your Plot in AU. Examples:\n" 
"Solar Wind Termination Shock: 94; Solar Wind Heliopause: 123;\n Sedna\'s furthest orbit (aphelion): 936; Inner Oort Cloud: 2000 to 20000;\n" 
"Outer Oort Cloud Limit: 100000; The Sun's gravitational influence: 126000;\n Proxima Centauri: 268585; Alpha Centauri: 276643", 
variable=scale_var, value='Manual')
manual_scale_radio.pack(anchor='w')

CreateToolTip(manual_scale_radio, "Set custom scale. Some key mean distances: \n* Mercury: 0.39 AU\n* Venus: 0.72 AU\n* Earth: 1 AU\n"
"* Mars: 1.52 AU\n* Asteroid Belt: between 2.2 and 3.2 AU\n* Jupiter: 5.2 AU\n* Saturn: 9.5 AU\n* Uranus: 19.2 AU\n* Neptune: 30.1 AU\n"
"* Dwarf Planet Pluto: between 30 and 49 AU.\n* Kuiper Belt: from roughly 30 to 50 AU\n* Dwarf Planet Sedna: currently at about 83.3 AU, ranging from 74 AU to 936 AU, " 
"with a mean distance of 526 AU\n* Heliopause (edge of the Sun's influence): approximately 120 AU\n* Voyager 1: currently over 165 AU")

custom_scale_entry = tk.Entry(scale_frame, width=10)
custom_scale_entry.pack(anchor='w')
custom_scale_entry.insert(0, '10')  # Default scale value

center_label = tk.Label(controls_frame, text="Select Center Object for Your Plot:")
center_label.pack(anchor='w')

center_object_var = tk.StringVar(value='Sun')
center_options = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Eris']
center_menu = ttk.Combobox(controls_frame, textvariable=center_object_var, values=center_options)
center_menu.pack(anchor='w')

CreateToolTip(center_menu, "Select the object to center the plot on. DO NOT select the same object from the Select Objects check list.")

# Number of Frames
num_frames_label = tk.Label(controls_frame, text="Enter Hours, Days, Weeks, Months or Years to Animate from \"Now\":")
num_frames_label.pack(anchor='w')
num_frames_entry = tk.Entry(controls_frame, width=5)
num_frames_entry.pack(anchor='w')
num_frames_entry.insert(0, '28')  # Default number of frames
CreateToolTip(num_frames_entry, "Enter the number of frames you wish to animate, where each frame represents an hour, day, week, month, or year. " 
              "The default value of 28, for days in the lunar month.")

# Paloma's Birthday button and its animation
paloma_buttons_frame = tk.Frame(controls_frame)
paloma_buttons_frame.pack(pady=(5, 0), fill='x')

paloma_birthday_button = tk.Button(
    paloma_buttons_frame, 
    text="Paloma's Birthday", 
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

# "Single Time Plot" Button 
plot_button = tk.Button(advance_buttons_frame, 
    text="Plot This Date", 
    command=plot_objects, 
    width=BUTTON_WIDTH, 
    font=BUTTON_FONT, 
    bg='SystemButtonFace', 
    fg='blue')
plot_button.grid(row=0, column=0, padx=(0, 5), pady=(5, 0))
CreateToolTip(plot_button, "Plot selected objects on the selected date. Plotting may take a while due to a large number of positions fetched from Horizons.")

# In the advance_buttons_frame section:
animate_hour_button = tk.Button(advance_buttons_frame, 
    text="Animate Hours", 
    command=lambda: animate_objects(timedelta(hours=1), "Hour"),
    width=BUTTON_WIDTH, 
    font=BUTTON_FONT, 
    bg='SystemButtonFace', 
    fg='blue')
animate_hour_button.grid(row=0, column=1, padx=(0, 5), pady=(5, 0))
CreateToolTip(animate_hour_button, "Animate the motion over hours. This may take a while due to the large number of positions fetched.")

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

# Create a subframe for plot button
plot_buttons_frame = tk.Frame(controls_frame)
plot_buttons_frame.pack(pady=(5, 0), fill='x')

# Create an Entry widget for the user to input the number of light-years
ly_entry_label = tk.Label(plot_buttons_frame, text="Enter number of light-years to plot up to 100:")
ly_entry_label.grid(row=4, column=0, padx=(0, 5), pady=(5, 0), sticky='w')

ly_entry = tk.Entry(plot_buttons_frame)
ly_entry.grid(row=4, column=1, padx=(5, 0), pady=(5, 0), sticky='w')
ly_entry.insert(0, '20')  # Default ly value

def call_planetarium_distance_script_with_input():
    try:
        ly_value = ly_entry.get()
        ly_value = float(ly_value)
        
        if ly_value <= 0 or ly_value > 100:
            output_label.config(text="Please enter a number between 0 and 100 light-years.")
            return
            
        script_path = get_script_path('planetarium_distance.py')        # dethreading
        subprocess.run(['python', str(script_path), str(ly_value)])     # dethreading

    #    script_path = os.path.join(os.path.dirname(__file__), 'planetarium_distance.py')
    #    subprocess.run(['python', script_path, str(ly_value)])
        
    except ValueError:
        output_label.config(text="Please enter a valid number between 0 and 100 light-years.")
    except Exception as e:
        output_label.config(text=f"Error running planetarium_distance.py: {e}")
        print(f"Error running planetarium_distance.py: {e}")
        traceback.print_exc()

# Create a single button to call the plot script
plot_button = tk.Button(
    plot_buttons_frame,
    text="3D Visualization of Stellar Neighborhood",
    command=call_planetarium_distance_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button.grid(row=5, column=0, columnspan=2, padx=(0, 5), pady=(5, 0), sticky='we')
CreateToolTip(plot_button, "3D plot of stars within the selected distance from the Sun.")

# Create a Frame for the stellar scale options
stellar_scale_frame = tk.LabelFrame(controls_frame, text="Scale Options for Apparent Magnitude 3D Plots")
stellar_scale_frame.pack(pady=(5, 0), fill='x')

stellar_scale_var = tk.StringVar(value='Auto')

# Auto scale option
stellar_auto_scale = tk.Radiobutton(stellar_scale_frame, text="Automatic Scaling of Your 3D Stellar Plots", 
                                   variable=stellar_scale_var, value='Auto')
stellar_auto_scale.pack(anchor='w')
CreateToolTip(stellar_auto_scale, "Automatically adjust scale based on the data range")

# Manual scale option
stellar_manual_scale = tk.Radiobutton(stellar_scale_frame, text="Or Manually Enter Scale of Your Plot in Light-Years:", 
                                     variable=stellar_scale_var, value='Manual')
stellar_manual_scale.pack(anchor='w')
CreateToolTip(stellar_manual_scale, "The range of the axes gets reduced to your input, so visible objects beyond that range will not display. ")

# Frame for scale entry
stellar_entry_frame = tk.Frame(stellar_scale_frame)
stellar_entry_frame.pack(anchor='w', padx=20)

# Entry for scale
stellar_scale_entry = tk.Entry(stellar_entry_frame, width=10)
stellar_scale_entry.pack(side='left')
stellar_scale_entry.insert(0, '1400')  # Default scale value

def on_stellar_scale_change(*args):
    """Enable/disable scale entry based on selected mode"""
    stellar_scale_entry.config(state='normal' if stellar_scale_var.get() == 'Manual' else 'disabled')

# Bind the scale variable to the callback
stellar_scale_var.trace('w', on_stellar_scale_change)

# Initial state setup
on_stellar_scale_change()

def call_planetarium_apparent_magnitude_script_with_input():
    try:
        # Validate magnitude input
        mag_value = mag_entry.get()
        mag_value = float(mag_value)
        if mag_value < -1.44 or mag_value > 9:
            output_label.config(text="Please enter a magnitude between -1.44 and 9.")
            return
            
        # Get scale value if manual mode is selected
        user_scale = None
        if stellar_scale_var.get() == 'Manual':
            try:
                user_scale = float(stellar_scale_entry.get())
                if user_scale <= 0:
                    output_label.config(text="Please enter a positive scale value.")
                    return
            except ValueError:
                output_label.config(text="Invalid scale value.")
                return
                
        # Build command with arguments
        script_path = get_script_path('planetarium_apparent_magnitude.py')      # dethreading
        cmd = ['python', str(script_path), str(mag_value)]                      # dethreading

    #    script_path = os.path.join(os.path.dirname(__file__), 'planetarium_apparent_magnitude.py')
    #    cmd = ['python', script_path, str(mag_value)]

        if user_scale is not None:
            cmd.append(str(user_scale))
            
        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd)
        
    except ValueError:
        output_label.config(text="Please enter a valid magnitude between -1.44 (brightest star Sirius) and 9.")
    except Exception as e:
        output_label.config(text=f"Error running planetarium_apparent_magnitude.py: {e}")
        print(f"Error running planetarium_apparent_magnitude.py: {e}")
        traceback.print_exc()

# Create a single button to call the plot script
plot_button = tk.Button(
    plot_buttons_frame,
    text="3D Visualization of Stars Visible Unaided",
    command=call_planetarium_apparent_magnitude_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button.grid(row=8, column=0, columnspan=2, padx=(0, 5), pady=(5, 0), sticky='we')
CreateToolTip(plot_button, "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; urban, 4 or less -- long load time.")

def call_hr_diagram_distance_script_with_input():
    try:
        ly_value = ly_entry.get()
        ly_value = int(ly_value)
        if ly_value <= 0:
            output_label.config(text="Please enter a positive number of light-years.")
            return

        script_path = get_script_path('hr_diagram_distance.py')         # dethreading
        subprocess.run(['python', str(script_path), str(ly_value)])     # dethreading

    #    script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_distance.py')
    #    subprocess.run(['python', script_path, str(ly_value)])

    except ValueError:
        output_label.config(text="Please enter a valid number of light-years.")
    except Exception as e:
        output_label.config(text=f"Error running hr_diagram_distance.py: {e}")
        print(f"Error running hr_diagram_distance.py: {e}")

# Create a single button to call the plot script
plot_button = tk.Button(
    plot_buttons_frame,
    text="2D Visualization of Stellar Neighborhood",
    command=call_hr_diagram_distance_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button.grid(row=6, column=0, columnspan=2, padx=(0, 5), pady=(5, 0), sticky='we')
CreateToolTip(plot_button, "2D Hertzprung-Russell plot of stars within the selected distance from the Sun.")

# Create an Entry widget for the user to input the maximum apparent magnitude
mag_entry_label = tk.Label(plot_buttons_frame, text="Enter maximum apparent magnitude (-1.44 to 9):")
mag_entry_label.grid(row=7, column=0, padx=(0, 5), pady=(5, 0), sticky='w')

mag_entry = tk.Entry(plot_buttons_frame)
mag_entry.grid(row=7, column=1, padx=(5, 0), pady=(5, 0), sticky='w')
mag_entry.insert(0, '4')  # Default magnitude value

# Function to call the hr_diagram script with user input

def call_hr_diagram_apparent_magnitude_script_with_input():
    try:
        mag_value = mag_entry.get()
        mag_value = float(mag_value)
        if mag_value < -1.44 or mag_value > 9:
            output_label.config(text="Please enter a magnitude between -1.44 and 9.")
            return

        script_path = get_script_path('hr_diagram_apparent_magnitude.py')       # dethreading
        subprocess.run(['python', str(script_path), str(mag_value)])            # dethreading

    #    script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_apparent_magnitude.py')
        # Pass magnitude value as command-line argument
    #    subprocess.run(['python', script_path, str(mag_value)])

    except ValueError:
        output_label.config(text="Please enter a valid magnitude between -1.44 (brightest star Sirius) and 9.")
    except Exception as e:
        output_label.config(text=f"Error running hr_diagram_apparent_magnitude.py: {e}")
        print(f"Error running hr_diagram_apparent_magnitude.py: {e}")
        traceback.print_exc()

# Create a button to call the HR diagram script
plot_button = tk.Button(
    plot_buttons_frame,
    text="2D Visualization of Stars Visible Unaided",
    command=call_hr_diagram_apparent_magnitude_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button.grid(row=9, column=0, columnspan=2, padx=(0, 5), pady=(5, 0), sticky='we')
CreateToolTip(plot_button, "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; urban, 4 or less -- long load time.")

# Create a LabelFrame for Status Messages
status_frame = tk.LabelFrame(controls_frame, text="Data Fetching Status for Solar Object Plotting", padx=10, pady=10, bg='SystemButtonFace', fg='black')
status_frame.pack(pady=(5, 5), fill='x')

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

# Define the list of objects
objects = [
    # Existing Celestial Objects
    {'name': 'Sun', 'id': '10', 'var': sun_var, 'color': color_map('Sun'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Mercury', 'id': '199', 'var': mercury_var, 'color': color_map('Mercury'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Venus', 'id': '299', 'var': venus_var, 'color': color_map('Venus'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Earth', 'id': '399', 'var': earth_var, 'color': color_map('Earth'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Moon', 'id': '301', 'var': moon_var, 'color': color_map('Moon'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Mars', 'id': '499', 'var': mars_var, 'color': color_map('Mars'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Ceres', 'id': 'ceres', 'var': ceres_var, 'color': color_map('Ceres'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody'},
    {'name': 'Jupiter', 'id': '599', 'var': jupiter_var, 'color': color_map('Jupiter'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Saturn', 'id': '699', 'var': saturn_var, 'color': color_map('Saturn'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Uranus', 'id': '799', 'var': uranus_var, 'color': color_map('Uranus'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Neptune', 'id': '899', 'var': neptune_var, 'color': color_map('Neptune'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Pluto', 'id': '999', 'var': pluto_var, 'color': color_map('Pluto'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
    {'name': 'Haumea', 'id': '136108', 'var': haumea_var, 'color': color_map('Haumea'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody'},
    {'name': 'Makemake', 'id': '136472', 'var': makemake_var, 'color': color_map('Makemake'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody'},
    {'name': 'Eris', 'id': '136199', 'var': eris_var, 'color': color_map('Eris'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody'},

    # Kuiper Belt Objects
    {'name': 'Quaoar', 'id': '50000', 'var': quaoar_var, 'color': color_map('Quaoar'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A large Kuiper Belt object with a ring system.', 'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/quaoar/in-depth/'},
    {'name': 'Sedna', 'id': '90377', 'var': sedna_var, 'color': color_map('Sedna'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A distant trans-Neptunian object with an extremely long orbit.', 'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/sedna/in-depth/'},
    {'name': 'Orcus', 'id': '90482', 'var': orcus_var, 'color': color_map('Orcus'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A large Kuiper Belt object with a moon named Vanth.', 'mission_url': 'https://www.celestrak.com/satcat/tables/minorplanet.txt'},
    {'name': 'Varuna', 'id': '20000', 'var': varuna_var, 'color': color_map('Varuna'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A significant Kuiper Belt Object with a rapid rotation period.', 'mission_url': 'https://www.celestrak.com/satcat/tables/minorplanet.txt'},
    {'name': 'Ixion', 'id': '2001 KX76', 'var': ixion_var, 'color': color_map('Ixion'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A large Kuiper Belt object without a known moon.', 'mission_url': 'https://www.celestrak.com/satcat/tables/minorplanet.txt'},
    {'name': 'GV9', 'id': '2004 GV9', 'var': gv9_var, 'color': color_map('GV9'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'A binary Kuiper Belt Object providing precise mass measurements through its moon.', 'mission_url': 'https://www.celestrak.com/satcat/tables/minorplanet.txt'},
    {'name': 'MS4', 'id': '2002 MS4', 'var': ms4_var, 'color': color_map('MS4'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'One of the largest unnumbered Kuiper Belt Objects with no known moons.', 'mission_url': 'https://www.minorplanetcenter.net/db_search/show_object?object_id=2002+MS4'},
    {'name': 'OR10', 'id': '2007 OR10', 'var': or10_var, 'color': color_map('OR10'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'smallbody', 'mission_info': 'One of the largest known Kuiper Belt Objects with a highly inclined orbit.', 'mission_url': 'https://www.celestrak.com/satcat/tables/minorplanet.txt'},

    # NASA Missions -- start date moved up by one day to avoid fetching errors, and default end date is 2025-01-01
    {'name': 'Pioneer 10', 'id': '-23', 'var': pioneer10_var, 'color': color_map('Pioneer 10'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1972, 3, 4, 1, 49, 4), 'end_date': datetime(2003, 1, 23, 8, 0), 'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 'mission_info': 'First spacecraft to travel through the asteroid belt and make direct observations of Jupiter.'},
    {'name': 'Pioneer 11', 'id': '-24', 'var': pioneer11_var, 'color': color_map('Pioneer 11'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1973, 4, 7, 2, 11, 0), 'end_date': datetime(1995, 9, 30, 11, 0), 'mission_url': 'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html', 'mission_info': 'First spacecraft to encounter Saturn and study its rings.'},
    {'name': 'Voyager 1', 'id': '-31', 'var': voyager1_var, 'color': color_map('Voyager 1'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
    'start_date': datetime(1977, 9, 6, 12, 56), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 'mission_info': 'Launched in 1977, Voyager 1 is the farthest spacecraft from Earth.'},
    {'name': 'Voyager 1 to heliopause', 'id': '-31', 'var': voyager1h_var, 'color': color_map('Voyager 1 to heliopause'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
    'start_date': datetime(1977, 9, 6, 12, 56), 'end_date': datetime(2012, 8, 25), 'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 'mission_info': 'Launched in 1977, Voyager 1 is the farthest spacecraft from Earth.'},
    {'name': 'Voyager 2', 'id': '-32', 'var': voyager2_var, 'color': color_map('Voyager 2'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1977, 8, 21, 14, 29), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://voyager.jpl.nasa.gov/mission/', 'mission_info': 'Launched in 1977, Voyager 2 explored all four giant planets.'},
    {'name': 'Galileo', 'id': '-77', 'var': galileo_var, 'color': color_map('Galileo'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1989, 10, 19, 16, 53), 'end_date': datetime(2003, 9, 21, 19, 57), 'mission_url': 'https://solarsystem.nasa.gov/missions/galileo/overview/', 'mission_info': 'Galileo studied Jupiter and its moons from 1995 to 2003.'},
    {'name': 'SOHO: Solar and Heliospheric Observatory', 'id': '488', 'var': soho_var, 'color': color_map('SOHO'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1995, 12, 3), 'end_date': datetime(2025, 1, 1), 'mission_info': 'Observes the Sun and heliosphere from the L1 Lagrange point.', 'mission_url': 'https://sohowww.nascom.nasa.gov/'},    
    {'name': 'Cassini-Huygens', 'id': '-82', 'var': cassini_var, 'color': color_map('Cassini-Huygens'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(1997, 10, 16, 8, 43), 'end_date': datetime(2017, 9, 15, 10, 31), 'mission_url': 'https://solarsystem.nasa.gov/missions/cassini/overview/', 'mission_info': 'Cassini studied Saturn and its moons from 2004 to 2017.'},
    {'name': 'Rosetta', 'id': '-226', 'var': rosetta_var, 'color': color_map('Rosetta'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2004, 3, 3), 'end_date': datetime(2016, 9, 30), 'mission_url': 'https://rosetta.esa.int/', 'mission_info': 'European Space Agency mission to study Comet 67P/Churyumov-Gerasimenko.'},
    {'name': 'New Horizons', 'id': '-98', 'var': new_horizons_var, 'color': color_map('New Horizons'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2006, 1, 20, 19, 0), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://www.nasa.gov/mission_pages/newhorizons/main/index.html', 'mission_info': 'New Horizons flew past Pluto in 2015 and continues into the Kuiper Belt.'},
    {'name': 'Chang\'e', 'id': 'Chang\'e', 'var': change_var, 'color': color_map('Chang\'e'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2007, 10, 25), 'end_date': datetime(2025, 1, 1), 'mission_info': 'China\'s lunar exploration program.', 'mission_url': 'http://www.clep.org.cn/'},
    {'name': 'Juno', 'id': '-61', 'var': juno_var, 'color': color_map('Juno'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2011, 8, 6, 16, 25), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://www.nasa.gov/mission_pages/juno/main/index.html', 'mission_info': 'Juno studies Jupiter\'s atmosphere and magnetosphere.'},
    {'name': 'Gaia', 'id': 'Gaia', 'var': gaia_var, 'color': color_map('Gaia'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2013, 12, 20), 'end_date': datetime(2025, 12, 31), 'mission_info': 'European Space Agency mission at L2 mapping the Milky Way.', 'mission_url': 'https://www.cosmos.esa.int/web/gaia'},
    {'name': 'Hayabusa2', 'id': 'Hayabusa2', 'var': hayabusa2_var, 'color': color_map('Hayabusa2'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2014, 12, 4), 'end_date': datetime(2020, 12, 5), 'mission_info': 'JAXA mission that returned samples from Ryugu.', 'mission_url': 'https://hayabusa2.jaxa.jp/en/'},
    {'name': 'OSIRIS-REx', 'id': '-64', 'var': osiris_rex_var, 'color': color_map('OSIRIS-REx'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2016, 9, 9), 'end_date': datetime(2023, 9, 24), 'mission_url': 'https://www.asteroidmission.org/', 'mission_info': 'NASA mission to collect samples from asteroid Bennu.'},
    {'name': 'Parker Solar Probe', 'id': '-96', 'var': parker_solar_probe_var, 'color': color_map('Parker Solar Probe'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2018, 8, 13), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://www.nasa.gov/content/goddard/parker-solar-probe', 'mission_info': 'Mission to study the outer corona of the Sun.'},
    {'name': 'Perseverance Rover', 'id': 'Perseverance', 'var': perse_var, 'color': color_map('Perseverance'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2020, 7, 31), 'end_date': datetime(2025, 1, 1), 'mission_info': 'NASA\'s Mars rover and Ingenuity helicopter.', 'mission_url': 'https://mars.nasa.gov/mars2020/'},
    {'name': 'Lucy Mission', 'id': '-49', 'var': lucy_var, 'color': color_map('Lucy'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',      # id Lucy
     'start_date': datetime(2021, 10, 17), 'end_date': datetime(2033, 4, 1), 'mission_info': 'Exploring Trojan asteroids around Jupiter.', 'mission_url': 'https://www.nasa.gov/lucy'},
    {'name': 'DART Mission', 'id': '-135', 'var': dart_var, 'color': color_map('DART'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2021, 11, 25), 'end_date': datetime(2022, 9, 25), 'mission_info': 'NASA\'s mission to test asteroid deflection.', 'mission_url': 'https://www.nasa.gov/dart'},
    {'name': 'James Webb Space Telescope', 'id': '-170', 'var': jwst_var, 'color': color_map('James Webb Space Telescope'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
     'start_date': datetime(2021, 12, 26), 'end_date': datetime(2025, 1, 1), 'mission_url': 'https://www.jwst.nasa.gov/', 'mission_info': 'NASA\'s flagship infrared space telescope.'},
    {'name': 'Europa Clipper', 'id': '-159', 'var': europa_clipper_var, 'color': color_map('Europa Clipper'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',        # id -159
     'start_date': datetime(2024, 10, 15), 'end_date': datetime(2030, 4, 1), 'mission_url': 'https://europa.nasa.gov/', 'mission_info': 'Europa Clipper will conduct detailed reconnaissance of Jupiter\'s moon Europa.'},
    {'name': 'BepiColombo', 'id': '-121', 'var': bepicolombo_var, 'color': color_map('BepiColombo'), 'symbol': 'diamond-open', 'is_mission': True, 'id_type': 'id',
    'start_date': datetime(2018, 10, 20), 'end_date': datetime(2030, 12, 31), 'mission_url': 'https://sci.esa.int/web/bepicolombo', 'mission_info': 'Joint ESA/JAXA mission to study Mercury, arriving in 2025.'},

    # Comets
    {'name': 'Ikeya-Seki', 'id': 'C/1965 S1-A', 'var': comet_ikeya_seki_var, 'color': color_map('Ikeya-Seki'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(1965, 9, 18), 'end_date': datetime(1966, 1, 1), 'mission_info': 'One of the brightest comets of the 20th century.'},
#    {'name': 'Ikeya-Seki', 'id': 'C/1965 S1-A', 'var': comet_ikeya_seki_var, 'color': color_map('Ikeya-Seki'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
#     'start_date': datetime(1965, 9, 18), 'end_date': datetime(2025, 1, 1), 'mission_info': 'One of the brightest comets of the 20th century.'},


    {'name': 'West', 'id': 'C/1975 V1', 'var': comet_west_var, 'color': color_map('Comet West'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(1975, 11, 5), 'end_date': datetime(1976, 6, 1), 'mission_info': 'Notable for its bright and impressive tail.'},
    {'name': 'Halley', 'id': '90000030', 'var': comet_halley_var, 'color': color_map('Halley'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',   
     'start_date': datetime(1982, 11, 26), 'end_date': datetime(1995, 10, 20), 'mission_info': 'Most famous comet, returned in 1986.'},
    {'name': 'Hyakutake', 'id': 'C/1996 B2', 'var': comet_hyakutake_var, 'color': color_map('Hyakutake'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(1995, 12, 1), 'end_date': datetime(1996, 6, 1), 'mission_info': 'Passed very close to Earth in 1996.'},
    {'name': 'Hale-Bopp', 'id': 'C/1995 O1', 'var': comet_hale_bopp_var, 'color': color_map('Hale-Bopp'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(1995, 7, 23), 'end_date': datetime(2001, 12, 31), 'mission_info': 'Visible to the naked eye for a record 18 months.'},
    {'name': 'McNaught', 'id': 'C/2006 P1', 'var': comet_mcnaught_var, 'color': color_map('McNaught'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2006, 8, 7), 'end_date': datetime(2008, 6, 1), 'mission_info': 'Known as the Great Comet of 2007.'},
    {'name': 'NEOWISE', 'id': 'C/2020 F3', 'var': comet_neowise_var, 'color': color_map('NEOWISE'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2020, 3, 27), 'end_date': datetime(2021, 6, 1), 'mission_info': 'Brightest comet visible from the Northern Hemisphere in decades.'},
    {'name': 'Tsuchinshan-ATLAS', 'id': 'C/2023 A3', 'var': comet_tsuchinshan_atlas_var, 'color': color_map('Tsuchinshan-ATLAS'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2023, 1, 9), 'end_date': datetime(2025, 1, 1), 'mission_info': 'A new comet discovered in 2023, expected to become bright in 2024.'},
    {'name': 'Churyumov-Gerasimenko', 'id': '90000703', 'var': comet_Churyumov_Gerasimenko_var, 'color': color_map('Churyumov-Gerasimenko'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2002, 11, 22), 'end_date': datetime(2021, 5, 1), 'mission_info': 'The comet visited by the Rosetta spacecraft.'},
    {'name': 'Borisov', 'id': 'C/2019 Q4', 'var': comet_borisov_var, 'color': color_map('Borisov'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2019, 8, 30), 'end_date': datetime(2020, 10, 1), 'mission_info': 'The second interstellar object detected, after \'Oumuamua.'},
    {'name': 'Oumuamua', 'id': 'A/2017 U1', 'var': oumuamua_var, 'color': color_map('Oumuamua'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2017, 10, 14), 'end_date': datetime(2018, 1, 1), 'mission_info': 'First known interstellar object detected passing through the Solar System.'},
    {'name': 'ATLAS', 'id': 'DES=C/2024 G3', 'var': comet_atlas_var, 'color': color_map('ATLAS'), 'symbol': 'circle-open', 'is_comet': True, 'id_type': 'smallbody',
     'start_date': datetime(2024, 6, 17), 'end_date': datetime(2026, 1, 1), 'mission_info': 'Comet C/2024 G3 (ATLAS) is creating quite a buzz in the Southern Hemisphere!'},

    # Asteroids
    {'name': '2024 PT5', 'id': '2024 PT5', 'var': pt5_var, 'color': color_map('2024 PT5'), 'symbol': 'circle-open', 'is_mission': False,
    'is_comet': False, 'id_type': 'smallbody', 'start_date': datetime(2024, 8, 1), 'end_date': datetime(2025, 1, 1), 'mission_info': 'A newly discovered small body from 2024.',
    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/des/2024%20PT5'},
    {'name': 'Apophis', 'id': '99942', 'var': apophis_var, 'color': color_map('Apophis'), 'symbol': 'circle-open', 'is_comet': False, 'id_type': 'smallbody',
     'start_date': datetime(2004, 6, 19), 'end_date': datetime(2036, 1, 1), 'mission_info': 'A near-Earth asteroid that will make a close approach in 2029.', 'mission_url': 'https://cneos.jpl.nasa.gov/apophis/'},
    {'name': 'Vesta', 'id': '4', 'var': vesta_var, 'color': color_map('Vesta'), 'symbol': 'circle-open', 'is_mission': False, 'id_type': 'smallbody',
     'mission_info': 'One of the largest objects in the asteroid belt, visited by NASA\'s Dawn mission.', 'mission_url': 'https://dawn.jpl.nasa.gov/'},
    {'name': 'Bennu', 'id': '101955', 'var': bennu_var, 'color': color_map('Bennu'), 'symbol': 'circle-open', 'is_mission': False, 'is_comet': False, 'id_type': 'smallbody',
     'mission_info': 'Studied by NASA\'s OSIRIS-REx mission.', 'mission_url': 'https://www.nasa.gov/content/osiris-rex'},
    {'name': 'Šteins', 'id': '2867', 'var': steins_var, 'color': color_map('Šteins'), 'symbol': 'circle-open', 'is_mission': False, 'is_comet': False, 'id_type': 'smallbody',
     'mission_info': 'Visited by European Space Agency\'s Rosetta spacecraft.', 'mission_url': 'https://www.esa.int/Science_Exploration/Space_Science/Rosetta'},
    {'name': 'Eros', 'id': '433', 'var': eros_var, 'color': color_map('Eros'), 'symbol': 'circle-open', 'is_mission': False, 'is_comet': False, 'id_type': 'smallbody',
    'mission_info': 'First asteroid to be orbited and landed on by NASA\'s NEAR Shoemaker spacecraft in 2000-2001.', 'mission_url': 'https://www.jhuapl.edu/near/'},
    {'name': 'Ryugu', 'id': '162173', 'var': ryugu_var, 'color': color_map('Ryugu'), 'symbol': 'circle-open', 'is_mission': False, 'is_comet': False, 'id_type': 'smallbody',
    'mission_info': 'Target of JAXA\'s Hayabusa2 mission which returned samples to Earth in 2020.', 'mission_url': 'https://www.hayabusa2.jaxa.jp/en/'},
    {'name': 'Itokawa', 'id': '25143', 'var': itokawa_var, 'color': color_map('Itokawa'), 'symbol': 'circle-open', 'is_mission': False, 'is_comet': False, 'id_type': 'smallbody',
    'mission_info': 'First asteroid from which samples were returned to Earth by JAXA\'s Hayabusa mission in 2010.', 'mission_url': 'https://www.isas.jaxa.jp/en/missions/spacecraft/past/hayabusa.html'},
        
    # --- Adding multi-point trajectories for satellites, see: https://ssd.jpl.nasa.gov/sats/ephem/

    {
    'name': 'Moon',
    'id': '301',
    'var': moon_var,
    'color': color_map('Moon'),
    'symbol': 'circle',
    'is_mission': False, 
    'is_satellite': True,         # <--- Let the code know this object is treated like a multi-point trajectory
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Moon: January 1, 2025 to January 28, 2025 (27.32 days)
    'end_date': datetime(2025, 1, 29),
    'mission_info': 'Earth orbital period: 27.32 days.'
    },

    # Mars' Moons

    {
    'name': 'Phobos', 
    'id': '401', 
    'var': phobos_var, 
    'color': color_map('Phobos'), 
    'symbol': 'circle', 
    'is_mission': False,
    'is_satellite': True,  
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Phobos: January 1, 2025 to January 1, 2025 (0.32 days)
    'end_date': datetime(2025, 1, 15),
    'mission_info': 'Mars orbital period: 0.32 Earth days.'
    },

    {
    'name': 'Deimos', 
    'id': '402', 
    'var': deimos_var, 
    'color': color_map('Deimos'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'is_satellite': True,  
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Deimos: January 1, 2025 to January 2, 2025 (1.26 days)
    'end_date': datetime(2025, 1, 15),
    'mission_info': 'Mars orbital period: 1.26 Earth days.'
    },

#    {'name': 'Phobos', 'id': '401', 'var': phobos_var, 'color': color_map('Phobos'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Deimos', 'id': '402', 'var': deimos_var, 'color': color_map('Deimos'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},

    # Jupiter's Galilean Moons

    {
    'name': 'Io', 
    'id': '10260',        # 501
    'var': io_var, 
    'color': color_map('Io'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Io: January 1, 2024 to January 2, 2024 (1.77 days)
    'end_date': datetime(2025, 1, 4),
    'mission_info': 'Jupiter orbital period: 1.77 Earth days.'
    },

    {
    'name': 
    'Europa', 
    'id': '502', 
    'var': europa_var, 
    'color': color_map('Europa'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Europa: January 1, 2025 to January 4, 2025 (3.55 days)
    'end_date': datetime(2025, 1, 6),
    'mission_info': 'Jupiter orbital period: 3.55 Earth days.'
    },

    {
    'name': 'Ganymede', 
    'id': '503', 
    'var': ganymede_var, 
    'color': color_map('Ganymede'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Ganymede: January 1, 2025 to January 8, 2025 (7.15 days)
    'end_date': datetime(2025, 1, 10),
    'mission_info': 'Jupiter orbital period: 7.15 Earth days.'
    },

    {
    'name': 'Callisto', 
    'id': '504', 
    'var': callisto_var, 
    'color': color_map('Callisto'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Callisto: January 1, 2025 to January 17, 2025 (16.69 days)
    'end_date': datetime(2025, 1, 19),
    'mission_info': 'Jupiter orbital period: 16.69 Earth days.'
    },

#    {'name': 'Io', 'id': '501', 'var': io_var, 'color': color_map('Io'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Europa', 'id': '502', 'var': europa_var, 'color': color_map('Europa'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Ganymede', 'id': '503', 'var': ganymede_var, 'color': color_map('Ganymede'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Callisto', 'id': '504', 'var': callisto_var, 'color': color_map('Callisto'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},

    # Saturn's Major Moons

    # Iapetus: January 1, 2025, to March 21, 2025 (79.32 days)

    {
    'name': 'Titan', 
    'id': '606', 
    'var': titan_var, 
    'color': color_map('Titan'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Titan: January 1, 2025 to January 16, 2025 (15.95 days)
    'end_date': datetime(2025, 1, 19),
    'mission_info': 'Saturn orbital period: 15.95 Earth days.'
    },

    {
    'name': 'Enceladus', 
    'id': '602', 
    'var': enceladus_var, 
    'color': color_map('Enceladus'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Enceladus: January 1, 2025 to January 2, 2025 (1.37 days)
    'end_date': datetime(2025, 1, 5),
    'mission_info': 'Saturn orbital period: 1.37 Earth days.'
    },

    {
    'name': 'Rhea', 
    'id': '605', 
    'var': rhea_var, 
    'color': color_map('Rhea'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Rhea: January 1, 2025 to January 5, 2025 (4.52 days)
    'end_date': datetime(2025, 1, 8),
    'mission_info': 'Saturn orbital period: 4.52 Earth days.'
    },

    {
    'name': 'Dione', 
    'id': '604', 
    'var': dione_var, 
    'color': color_map('Dione'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Dione: January 1, 2025 to January 3, 2025 (2.74 days)
    'end_date': datetime(2025, 1, 6),
    'mission_info': 'Saturn orbital period: 2.74 Earth days.'
    },

    {
    'name': 'Tethys', 
    'id': '603', 
    'var': tethys_var, 
    'color': color_map('Tethys'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Tethys: January 1, 2025 to January 2, 2025 (1.89 days)
    'end_date': datetime(2026, 1, 5),
    'mission_info': 'Saturn orbital period: 1.89 Earth days.'
    },

    {
    'name': 'Mimas', 
    'id': '601', 
    'var': mimas_var, 
    'color': color_map('Mimas'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Mimas: January 1, 2025 to January 1, 2025 (0.94 days)
    'end_date': datetime(2025, 1, 4),
    'mission_info': 'Saturn orbital period: 0.94 Earth days.'
    },

    {
    'name': 'Phoebe', 
    'id': '609', 
    'var': phoebe_var, 
    'color': color_map('Phoebe'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Phoebe: January 1, 2025, to July 5, 2026 (550.56 days)
    'end_date': datetime(2026, 7, 8),
    'mission_info': 'Saturn orbital period: 550.56 Earth days.'
    },

#    {'name': 'Titan', 'id': '601', 'var': titan_var, 'color': color_map('Titan'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Enceladus', 'id': '602', 'var': enceladus_var, 'color': color_map('Enceladus'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Rhea', 'id': '603', 'var': rhea_var, 'color': color_map('Rhea'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Dione', 'id': '604', 'var': dione_var, 'color': color_map('Dione'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Tethys', 'id': '605', 'var': tethys_var, 'color': color_map('Tethys'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Mimas', 'id': '606', 'var': mimas_var, 'color': color_map('Mimas'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Phoebe', 'id': '607', 'var': phoebe_var, 'color': color_map('Phoebe'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},

    # Uranus's Major Moons

    {
    'name': 'Oberon', 
    'id': '704', 
    'var': oberon_var, 
    'color': color_map('Oberon'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Oberon: January 1, 2025, to January 14, 2025 (13.46 days)
    'end_date': datetime(2025, 1, 17),
    'mission_info': 'Uranus orbital period: 13.46 Earth days.'
    },

    {
    'name': 'Umbriel', 
    'id': '702', 
    'var': umbriel_var, 
    'color': color_map('Umbriel'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Umbriel: January 1, 2025, to January 5, 2025 (4.14 days)
    'end_date': datetime(2025, 1, 8),
    'mission_info': 'Uranus orbital period: 4.14 Earth days.'
    },

    {
    'name': 'Ariel', 
    'id': '701', 
    'var': ariel_var, 
    'color': color_map('Ariel'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Ariel: January 1, 2025, to January 3, 2025 (2.52 days)
    'end_date': datetime(2025, 1, 6),
    'mission_info': 'Uranus orbital period: 2.52 Earth days.'
    },

    {
    'name': 'Miranda', 
    'id': '705', 
    'var': miranda_var, 
    'color': color_map('Miranda'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Miranda: January 1, 2025, to January 2, 2025 (1.41 days)
    'end_date': datetime(2025, 1, 5),
    'mission_info': 'Uranus orbital period: 1.41 Earth days.'
    },

    {
    'name': 'Titania', 
    'id': '703', 
    'var': titania_var, 
    'color': color_map('Titania'), 
    'symbol': 'circle', 'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Titania: January 1, 2025, to January 9, 2025 (8.71 days)
    'end_date': datetime(2025, 1, 12),
    'mission_info': 'Uranus orbital period: 8.71 Earth days.'
    },

#    {'name': 'Oberon', 'id': '701', 'var': oberon_var, 'color': color_map('Oberon'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Umbriel', 'id': '703', 'var': umbriel_var, 'color': color_map('Umbriel'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Ariel', 'id': '704', 'var': ariel_var, 'color': color_map('Ariel'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Miranda', 'id': '705', 'var': miranda_var, 'color': color_map('Miranda'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Titania', 'id': '706', 'var': titania_var, 'color': color_map('Titania'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},

    # Neptune's Major Moon

    # Nereid: January 1, 2025, to December 27, 2025 (360.13 days)

    {
    'name': 'Triton', 
    'id': '801', 
    'var': triton_var, 
    'color': color_map('Triton'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Triton: January 1, 2025, to January 6, 2025 (5.88 days)
    'end_date': datetime(2035, 1, 9),
    'mission_info': 'Neptune orbital period: 5.88 Earth days.'
    },

#    {'name': 'Triton', 'id': '801', 'var': triton_var, 'color': color_map('Triton'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},

    # Pluto's Moon

    # Styx: January 1, 2025, to January 21, 2025 (20.16 days)
    # Kerberos: January 1, 2025, to February 2, 2025 (32.17 days)

    {
    'name': 'Charon', 
    'id': '901', 
    'var': charon_var, 
    'color': color_map('Charon'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Charon: January 1, 2025, to January 7, 2025 (6.39 days)
    'end_date': datetime(2025, 1, 10),
    'mission_info': 'Pluto orbital period: 6.39 Earth days.'
    },

    {
    'name': 'Nix', 
    'id': '902', 
    'var': nix_var, 
    'color': color_map('Nix'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Nix: January 1, 2025, to January 25, 2025 (24.86 days)
    'end_date': datetime(2025, 1, 28),
    'mission_info': 'Pluto orbital period: 24.86 Earth days.'
    },

    {
    'name': 'Hydra', 
    'id': '903', 
    'var': hydra_var, 
    'color': color_map('Hydra'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Hydra: January 1, 2025, to February 8, 2025 (38.20 days)
    'end_date': datetime(2025, 1, 11),
    'mission_info': 'Pluto orbital period: 38.20 Earth days.'
    },

#    {'name': 'Charon', 'id': '901', 'var': charon_var, 'color': color_map('Charon'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody'},
#    {'name': 'Nix', 'id': '902', 'var': nix_var, 'color': color_map('Nix'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody',
#    'mission_info': 'One of Pluto\'s moons.', 'mission_url': 'https://solarsystem.nasa.gov/moons/pluto-moons/nix/overview/'},
#    {'name': 'Hydra', 'id': '903', 'var': hydra_var, 'color': color_map('Hydra'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody',
#    'mission_info': 'Another of Pluto\'s moons.', 'mission_url': 'https://solarsystem.nasa.gov/moons/pluto-moons/hydra/overview/'},

    # Eris's Moon

    {
    'name': 'Dysnomia', 
    'id': '120136199', 
    'var': dysnomia_var, 
    'color': color_map('Dysnomia'), 
    'symbol': 'circle', 
    'is_mission': False, 
    'id_type': 'majorbody',
    'start_date': datetime(2025, 1, 1),     # Dysnomia: January 1, 2025, to January 16, 2025 (15.79 days)
    'end_date': datetime(2025, 1, 19),
    'mission_info': 'Orbital period: 15.79 Earth days.'
    },

#    {'name': 'Eris\' Moon Dysnomia', 'id': 'Dysnomia', 'var': dysnomia_var, 'color': color_map('Dysnomia'), 'symbol': 'circle', 'is_mission': False, 'id_type': 'majorbody',
#     'mission_info': 'Companion to the dwarf planet Eris.', 'mission_url': 'https://www.nasa.gov/asteroids'},

    # Stars
    # Proxima Centauri - Our closest stellar neighbor
    {'name': 'NAME Proxima Centauri', 
    'id': 'HIP 70890',  # Hipparcos ID if we want to use that instead
    'var': proxima_var, 
    'color': 'rgb(255, 50, 50)', 
    'symbol': 'circle', 
    'is_mission': False,
    'is_fixed_star': True,  # New flag to indicate static position
    'coordinates': {
        'ra': '14h 29m 42.95s',
        'dec': '-62° 40′ 46.14″',
        'distance_ly': 4.2465  # light-years
    }}
]


# Run the Tkinter main loop
root.mainloop()
