"""
Celestial Body Visualization Module
==================================
Functions for creating layered visualizations of solar system bodies (Sun, planets) in 3D plots.
Each celestial body has individual shell components that can be toggled with selection variables.
"""

import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # Sun information texts
    gravitational_influence_info_hover,
    outer_oort_info_hover,
    inner_oort_info_hover,
    inner_limit_oort_info_hover,
    solar_wind_info_hover,
    termination_shock_info_hover,
    outer_corona_info_hover,
    inner_corona_info_hover,
    chromosphere_info_hover,
    photosphere_info_hover,
    radiative_zone_info_hover,
    core_info_hover
)

#####################################
# Celestial Body Constants
#####################################

# Solar Constants
SOLAR_RADIUS_AU = 0.00465047  # Sun's radius in AU
CORE_AU = 0.00093               # Core in AU, approximately 0.2 Solar radii
RADIATIVE_ZONE_AU = 0.00325     # Radiative zone in AU, approximately 0.7 Solar radii
CHROMOSPHERE_RADII = 1.5    # Chromosphere extends to about 1.5 solar radii
INNER_CORONA_RADII = 3  # Inner corona extends to 2-3 solar radii
OUTER_CORONA_RADII = 50  # Outer corona extends up to 50 solar radii
TERMINATION_SHOCK_AU = 94  # Termination shock boundary in AU
HELIOPAUSE_RADII = 26449  # Heliopause at about 123 AU
INNER_LIMIT_OORT_CLOUD_AU = 2000  # Inner Oort cloud boundary in AU
INNER_OORT_CLOUD_AU = 20000  # Inner Oort cloud outer boundary in AU
OUTER_OORT_CLOUD_AU = 100000  # Outer Oort cloud boundary in AU
GRAVITATIONAL_INFLUENCE_AU = 126000  # Sun's gravitational influence in AU

# Jupiter Constants
JUPITER_RADIUS_KM = 71492  # Equatorial radius in km
JUPITER_RADIUS_AU = JUPITER_RADIUS_KM / 149597870.7  # Convert to AU

# Earth Constants
EARTH_RADIUS_KM = 6371  # Mean radius in km
EARTH_RADIUS_AU = EARTH_RADIUS_KM / 149597870.7  # Convert to AU

#####################################
# Shared Utility Functions
#####################################

# Revised create_celestial_body_visualization function for planet_visualization.py
# This ensures consistent animation support for all celestial bodies

def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0)):
    """
    Unified function to create shell visualizations for any celestial body (Sun or planets).
    Ensures consistent animation support across all body types.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the visualization to
        body_name (str): Name of the celestial body ('Sun', 'Earth', 'Jupiter', etc.)
        shell_vars (dict): Dictionary of selection variables for each body's shells
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        center_position (tuple): (x, y, z) position of the body's center
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    print(f"\nCreating visualization for {body_name} (animate={animate})")
    
    # Create shell traces based on selected variables
    traces = []
    
    if body_name == 'Sun':
        # Handle Sun visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                # Call the appropriate shell creation function based on name
                if shell_name == 'core' and var.get() == 1:
                    traces.extend(create_sun_core_shell())
                elif shell_name == 'radiative' and var.get() == 1:
                    traces.extend(create_sun_radiative_shell())
                elif shell_name == 'photosphere' and var.get() == 1:
                    traces.extend(create_sun_photosphere_shell())
                elif shell_name == 'chromosphere' and var.get() == 1:
                    traces.extend(create_sun_chromosphere_shell())
                elif shell_name == 'inner_corona' and var.get() == 1:
                    traces.extend(create_sun_inner_corona_shell())
                elif shell_name == 'outer_corona' and var.get() == 1:
                    traces.extend(create_sun_outer_corona_shell())
                elif shell_name == 'termination_shock' and var.get() == 1:
                    traces.extend(create_sun_termination_shock_shell())
                elif shell_name == 'heliopause' and var.get() == 1:
                    traces.extend(create_sun_heliopause_shell())
                elif shell_name == 'inner_oort_limit' and var.get() == 1:
                    traces.extend(create_sun_inner_oort_limit_shell())
                elif shell_name == 'inner_oort' and var.get() == 1:
                    traces.extend(create_sun_inner_oort_shell())
                elif shell_name == 'outer_oort' and var.get() == 1:
                    traces.extend(create_sun_outer_oort_shell())
                elif shell_name == 'gravitational' and var.get() == 1:
                    traces.extend(create_sun_gravitational_shell())
    
    elif body_name == 'Earth':
        # Handle Earth visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('earth_', '')
                if shell_type == 'inner_core' and var.get() == 1:
                    traces.extend(create_earth_inner_core_shell(center_position))
                elif shell_type == 'outer_core' and var.get() == 1:
                    traces.extend(create_earth_outer_core_shell(center_position))
                elif shell_type == 'lower_mantle' and var.get() == 1:
                    traces.extend(create_earth_lower_mantle_shell(center_position))
                elif shell_type == 'upper_mantle' and var.get() == 1:
                    traces.extend(create_earth_upper_mantle_shell(center_position))
                elif shell_type == 'crust' and var.get() == 1:
                    traces.extend(create_earth_crust_shell(center_position))
                elif shell_type == 'atmosphere' and var.get() == 1:
                    traces.extend(create_earth_atmosphere_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_earth_upper_atmosphere_shell(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_earth_magnetosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_earth_hill_sphere_shell(center_position))
    
    elif body_name == 'Jupiter':
        # Handle Jupiter visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('jupiter_', '')
                if shell_type == 'core' and var.get() == 1:
                    traces.extend(create_jupiter_core_shell(center_position))
                elif shell_type == 'metallic_hydrogen' and var.get() == 1:
                    traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
                elif shell_type == 'molecular_hydrogen' and var.get() == 1:
                    traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
                elif shell_type == 'cloud_layer' and var.get() == 1:
                    traces.extend(create_jupiter_cloud_layer_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
                elif shell_type == 'ring_system' and var.get() == 1:
                    traces.extend(create_jupiter_ring_system(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_jupiter_magnetosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_jupiter_hill_sphere_shell(center_position))
    
    else:
        print(f"Warning: No visualization available for {body_name}")
        return fig
    
    # Apply consistent animation handling for all bodies
    print(f"Created {len(traces)} traces for {body_name}")
    
    # Add traces to the figure
    for trace in traces:
        fig.add_trace(trace)
    
    # IMPORTANT: Skip adding to frames completely
    if animate and frames is not None:
        print(f"Animation mode: Added {len(traces)} traces to figure only (skipping frames)")
    
    return fig

def create_sphere_points(radius, n_points=50):
    """
    Create points for a sphere surface to represent celestial body layers.
    
    Parameters:
        radius (float): Radius of the sphere in AU
        n_points (int): Number of points to generate along each dimension
        
    Returns:
        tuple: (x, y, z) coordinates as flattened arrays
    """
    phi = np.linspace(0, 2*np.pi, n_points)
    theta = np.linspace(-np.pi/2, np.pi/2, n_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    return x.flatten(), y.flatten(), z.flatten()

def create_ring_points(inner_radius, outer_radius, n_points=100, thickness=0.01):
    """
    Create points for a ring structure (for planets like Saturn).
    
    Parameters:
        inner_radius (float): Inner radius of the ring in AU
        outer_radius (float): Outer radius of the ring in AU
        n_points (int): Number of points to generate for each ring dimension
        thickness (float): Thickness of the ring in AU
        
    Returns:
        tuple: (x, y, z) coordinates as flattened arrays
    """
    # Generate radial and angular points
    radii = np.linspace(inner_radius, outer_radius, n_points // 4)
    thetas = np.linspace(0, 2*np.pi, n_points)
    
    # Create a meshgrid of radii and angles
    r, theta = np.meshgrid(radii, thetas)
    
    # Generate the ring coords on x-y plane
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Generate some points along z to give minimal thickness
    z_values = np.linspace(-thickness/2, thickness/2, 3)
    
    # Replicate the x, y coordinates for each z value
    x_all = []
    y_all = []
    z_all = []
    
    for z_val in z_values:
        x_all.append(x.flatten())
        y_all.append(y.flatten())
        z_all.append(np.full_like(x.flatten(), z_val))
    
    # Combine all points
    return np.concatenate(x_all), np.concatenate(y_all), np.concatenate(z_all)

#####################################
# Sun Visualization Functions
#####################################

def create_sun_visualization(fig, sun_shell_vars, animate=False, frames=None):
    """
    Creates a visualization of the Sun's layers based on which shells are selected.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the Sun visualization to
        sun_shell_vars (dict): Dictionary of selection variables for each Sun shell
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    # Create base traces for static visualization
    def create_layer_traces():
        traces = []
        
        # Add each selected shell based on the selection variables
        # Order from outermost to innermost
        if sun_shell_vars['gravitational'].get() == 1:
            traces.extend(create_sun_gravitational_shell())
            
        if sun_shell_vars['outer_oort'].get() == 1:
            traces.extend(create_sun_outer_oort_shell())
            
        if sun_shell_vars['inner_oort'].get() == 1:
            traces.extend(create_sun_inner_oort_shell())
            
        if sun_shell_vars['inner_oort_limit'].get() == 1:
            traces.extend(create_sun_inner_oort_limit_shell())
            
        if sun_shell_vars['heliopause'].get() == 1:
            traces.extend(create_sun_heliopause_shell())
            
        if sun_shell_vars['termination_shock'].get() == 1:
            traces.extend(create_sun_termination_shock_shell())
            
        if sun_shell_vars['outer_corona'].get() == 1:
            traces.extend(create_sun_outer_corona_shell())
            
        if sun_shell_vars['inner_corona'].get() == 1:
            traces.extend(create_sun_inner_corona_shell())
            
        if sun_shell_vars['chromosphere'].get() == 1:
            traces.extend(create_sun_chromosphere_shell())
            
        if sun_shell_vars['photosphere'].get() == 1:
            traces.extend(create_sun_photosphere_shell())
            
        if sun_shell_vars['radiative'].get() == 1:
            traces.extend(create_sun_radiative_shell())
            
        if sun_shell_vars['core'].get() == 1:
            traces.extend(create_sun_core_shell())
        
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

# Individual Sun shell creation functions

def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=40)
    
    text_array = [gravitational_influence_info_hover for _ in range(len(x))]
    customdata_array = ["Sun's Gravitational Influence" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(102, 187, 106)', 
                opacity=0.2
            ),
            name='Sun\'s Gravitational Influence',
            text=text_array,             
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='green',
    #            size=0.5,
    #            symbol='square-open',
    #            opacity=0.2
    #        ),
    #        name='Sun\'s Gravitational Influence',
    #        text=['The Sun\'s gravitational influence to ~126,000 AU or 2 ly.'],
    #        customdata=customdata_array,
    #        hoverinfo='skip',
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [outer_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Outer Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.2
            ),
            name='Outer Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='white',
    #            size=1.0,
    #            symbol='circle-open',
    #            opacity=0.2
    #        ),
    #        name='Outer Oort Cloud',
    #        text=['Outer Oort Cloud from estimated 20,000 to 100,000 AU.'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='white',
    #            size=1.0,
    #            symbol='circle-open',
    #            opacity=0.3
    #        ),
    #        name='Inner Oort Cloud',
    #        text=['Inner Oort Cloud from estimated 2,000 to 20,000 AU.'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_limit_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Limit of Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Limit of Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='white',
    #            size=1.0,
    #            symbol='circle-open',
    #            opacity=0.3
    #        ),
    #        name='Inner Limit of Oort Cloud',
    #        text=['Inner Oort Cloud from estimated 2,000 to 20,000 AU.'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=40)
    
    text_array = [solar_wind_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Heliopause" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(135, 206, 250)',
                opacity=0.2
            ),
            name='Solar Wind Heliopause',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(135, 206, 250)',
    #            size=0.5,
    #            symbol='circle',
    #            opacity=0.2
    #        ),
    #        name='Solar Wind Heliopause',
    #        text=['Solar Wind Heliopause (extends to 123 AU)'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=40)
    
    text_array = [termination_shock_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Termination Shock" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(240, 244, 255)',
                opacity=0.2
            ),
            name='Solar Wind Termination Shock',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(240, 244, 255)',
    #            size=0.5,
    #            symbol='circle',
    #            opacity=0.2
    #        ),
    #        name='Solar Wind Termination Shock',
    #        text=['Solar Wind Termination Shock (extends to 94 AU)'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_outer_corona_shell():
    """Creates the Sun's outer corona shell."""
    x, y, z = create_sphere_points(OUTER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=50)
    
    text_array = [outer_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Outer Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.75,
                color='rgb(25, 25, 112)',
                opacity=0.3
            ),
            name='Sun: Outer Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(25, 25, 112)',
    #            size=0.75,
    #            symbol='circle',
    #            opacity=0.3
    #        ),
    #        name='Sun: Outer Corona',
    #        text=['Solar Outer Corona (extends to 50 solar radii or more, or 0.2 AU)'],
    #        customdata=customdata_array,
    #        hovertemplate='%{text}<extra></extra>',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_inner_corona_shell():
    """Creates the Sun's inner corona shell."""
    x, y, z = create_sphere_points(INNER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [inner_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Inner Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1,
                color='rgb(0, 0, 255)',
                opacity=0.09
            ),
            name='Sun: Inner Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(0, 0, 255)',
    #            size=1,
    #            symbol='circle',
    #            opacity=0.09
    #        ),
    #        name='Sun: Inner Corona',
    #        text=['Solar Inner Corona (extends to 2-3 solar radii)'],
    #        hoverinfo='text',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell."""
    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [chromosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Chromosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.25,
                color='rgb(30, 144, 255)',
                opacity=0.10
            ),
            name='Sun: Chromosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(30, 144, 255)',
    #            size=1.25,
    #            symbol='circle',
    #            opacity=0.10
    #        ),
    #        name='Sun: Chromosphere',
    #        text=['Solar Chromosphere (surface temperature ~6,000 to 20,000 K)'],
    #        hoverinfo='text',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [photosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Photosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7.0,
                color='rgb(255, 244, 214)',
                opacity=1.0
            ),
            name='Sun: Photosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(255, 244, 214)',
    #            size=7.0,
    #            symbol='circle',
    #            opacity=1.0
    #        ),
    #        name='Sun: Photosphere',
    #        text=['Solar Photosphere (surface temperature ~6,000K)'],
    #        hoverinfo='text',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=60)
    
    text_array = [radiative_zone_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Radiative Zone" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color='rgb(30, 144, 255)',
                opacity=1.0
            ),
            name='Sun: Radiative Zone',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(30, 144, 255)',
    #            size=7,
    #            symbol='circle',
    #            opacity=1.0
    #        ),
    #        name='Sun: Radiative Zone',
    #        text=['Solar Radiative Zone (extends to 0.2 to 0.7 solar radii)'],
    #        hoverinfo='text',
    #        showlegend=False
    #    )
    ]
    
    return traces

def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=60)
    
    text_array = [core_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Core" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(70, 130, 180)',
                opacity=1.0
            ),
            name='Sun: Core',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    #    go.Scatter3d(
    #        x=[0], y=[0], z=[0],
    #        mode='markers',
    #        marker=dict(
    #            color='rgb(70, 130, 180)',
    #            size=10,
    #            symbol='circle',
    #            opacity=1.0
    #        ),
    #        name='Sun: Core',
    #        text=['Solar Core (temperature ~15M K)'],
    #        hoverinfo='text',
    #        hoverinfo='skip',
    #        showlegend=False
    #    )
    ]
    
    return traces

#####################################
# Planet Visualization Functions
#####################################

def create_planet_visualization(fig, planet_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0)):
    """
    Creates a visualization of a planet's layers based on which shells are selected.
    Works for both static plots and animations.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the visualization to
        planet_name (str): Name of the planet 
        shell_vars (dict): Dictionary of selection variables for each planet shell
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    # Create base traces for static visualization
    traces = []
    
    # Create shell traces based on selected variables
    if planet_name == 'Jupiter':
        if shell_vars['jupiter_core'].get() == 1:
            traces.extend(create_jupiter_core_shell(center_position))
        if shell_vars['jupiter_metallic_hydrogen'].get() == 1:
            traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
        if shell_vars['jupiter_molecular_hydrogen'].get() == 1:
            traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
        if shell_vars['jupiter_cloud_layer'].get() == 1:
            traces.extend(create_jupiter_cloud_layer_shell(center_position))
        if shell_vars['jupiter_upper_atmosphere'].get() == 1:
            traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
        if shell_vars['jupiter_ring_system'].get() == 1:
            traces.extend(create_jupiter_ring_system(center_position))
        if shell_vars['jupiter_magnetosphere'].get() == 1:
            traces.extend(create_jupiter_magnetosphere_shell(center_position))
        if shell_vars['jupiter_hill_sphere'].get() == 1:
            traces.extend(create_jupiter_hill_sphere_shell(center_position))
    
    elif planet_name == 'Earth':
        if shell_vars['earth_inner_core'].get() == 1:
            traces.extend(create_earth_inner_core_shell(center_position))
        if shell_vars['earth_outer_core'].get() == 1:
            traces.extend(create_earth_outer_core_shell(center_position))
        if shell_vars['earth_lower_mantle'].get() == 1:
            traces.extend(create_earth_lower_mantle_shell(center_position))
        if shell_vars['earth_upper_mantle'].get() == 1:
            traces.extend(create_earth_upper_mantle_shell(center_position))
        if shell_vars['earth_crust'].get() == 1:
            traces.extend(create_earth_crust_shell(center_position))
        if shell_vars['earth_atmosphere'].get() == 1:
            traces.extend(create_earth_atmosphere_shell(center_position))
        if shell_vars['earth_upper_atmosphere'].get() == 1:
            traces.extend(create_earth_upper_atmosphere_shell(center_position))
        if shell_vars['earth_magnetosphere'].get() == 1:
            traces.extend(create_earth_magnetosphere_shell(center_position))
        if shell_vars['earth_hill_sphere'].get() == 1:
            traces.extend(create_earth_hill_sphere_shell(center_position))
    
    # Add base traces to figure for static visualization
    for trace in traces:
        fig.add_trace(trace)

    # If this is for animation, add the traces to each frame
    if animate and frames is not None:
        for frame in frames:
            frame_data = list(frame.data)  # Convert tuple to list if necessary
            frame_data.extend(traces)
            frame.data = frame_data

    return fig

def create_planet_shell_traces(planet_name, shell_vars, center_position=(0, 0, 0)):
    """
    Creates traces for planet shells without adding them to a figure.
    Useful for animations where traces need to be created for each frame.
    
    Parameters:
        planet_name (str): Name of the planet
        shell_vars (dict): Dictionary of selection variables for each planet shell
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        list: List of plotly traces
    """
    traces = []
    
    # Get the prefix for this planet's shell variables
    prefix = planet_name.lower() + "_"
    
    # Check each shell variable and add corresponding traces if selected
    for shell_name, var in shell_vars.items():
        if var.get() == 1:
            # Extract the actual shell name without the planet prefix
            shell_type = shell_name.replace(prefix, "")
            
            # Dynamically call the appropriate shell creation function
            creation_func_name = f"create_{planet_name.lower()}_{shell_type}_shell"
            if creation_func_name in globals():
                creation_func = globals()[creation_func_name]
                new_traces = creation_func(center_position=center_position)
                traces.extend(new_traces)
            else:
                print(f"Warning: No creation function found for {shell_type} shell of {planet_name}")
    
    # Fix the hovertemplate for all traces
    for trace in traces:
        # Ensure proper customdata for hovering
        if hasattr(trace, 'customdata'):
            if isinstance(trace.customdata, list):
                # Make sure all customdata items reference the correct planet
                trace.customdata = [str(item).replace("Jupiter", planet_name).replace("Earth", planet_name) 
                              if "Jupiter" in str(item) or "Earth" in str(item)
                              else str(item) for item in trace.customdata]
        
        # Set correct hovertemplate
        trace.hovertemplate = '%{text}<extra></extra>'
    
    return traces

# Jupiter Shell Creation Functions

jupiter_core_info = (
            "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.\n"
            "It may be up to 10 times the mass of Earth. Recent models suggest the core might be\n"
            "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature\n"
            "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
)

def create_jupiter_core_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.1,  # Approximately 10% of Jupiter's radius
        'color': 'rgb(175, 175, 255)',  # estimated black body color at about 20,000 K
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.<br>"
            "It may be up to 10 times the mass of Earth. Recent models suggest the core might be<br>"
            "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature<br>"
            "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=4.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_metallic_hydrogen_info = (
            "Under extreme pressure, hydrogen transitions to a metallic state in this layer.\n"
            "It behaves like an electrical conductor and is responsible for generating\n"
            "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
)

def create_jupiter_metallic_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's metallic hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.8,  # Up to about 80% of Jupiter's radius
        'color': 'rgb(225, 225, 255)',  # estimated black body color at about 10,000 K
        'opacity': 0.9,
        'name': 'Metallic Hydrogen Layer',
        'description': (
            "Metallic Hydrogen Layer:<br>" 
            "Under extreme pressure, hydrogen transitions to a metallic state in this layer.<br>"
            "It behaves like an electrical conductor and is responsible for generating<br>"
            "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.5,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_molecular_hydrogen_info = (
            "This layer consists of hydrogen in its molecular form. The transition from metallic\n"
            "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass\n"
            "and is marked by decreasing temperature and pressure as you move outward. The temperature\n"
            "ranges from about 5,000K (outer) to 10,000K (inner)."
)

def create_jupiter_molecular_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's molecular hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.97,  # Up to about 97% of Jupiter's radius
        'color': 'rgb(255, 255, 200)',  # estimated black body color at about 5,000 K 
        'opacity': 0.5,
        'name': 'Molecular Hydrogen Layer',
        'description': (
            "Molecular Hydrogen Layer:<br>" 
            "This layer consists of hydrogen in its molecular form. The transition from metallic<br>"
            "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass<br>"
            "and is marked by decreasing temperature and pressure as you move outward. The temperature<br>"
            "ranges from about 5,000K (outer) to 10,000K (inner)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_cloud_layer_info = (
            "Jupiter's visible cloud layer consists of bands of different colors, caused by\n"
            "variations in chemical composition and atmospheric dynamics. The clouds are primarily\n"
            "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot\n"
            "is a massive storm system located in this layer. Temperature ranges from 120 K in\n" 
            "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
)

def create_jupiter_cloud_layer_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # The visible "surface" - 100% of Jupiter's radius
        'color': 'rgb(255, 255, 235)',  # optical
        'opacity': 1.0,
        'name': 'Cloud Layer',
        'description': (
            "Jupiter's visible cloud layer consists of bands of different colors, caused by<br>"
            "variations in chemical composition and atmospheric dynamics. The clouds are primarily<br>"
            "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot<br>"
            "is a massive storm system located in this layer. Temperature ranges from 120 K in<br>" 
            "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_upper_atmosphere_info = (
            "Jupiter's upper atmosphere includes the stratosphere and thermosphere.\n"
            "It's less dense than the cloud layer below and contains hydrocarbon haze\n"
            "produced by solar ultraviolet radiation. Aurora activity can be observed\n"
            "at Jupiter's poles, caused by interactions with its magnetic field. Temperature\n"
            "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
)

# Fix for create_jupiter_upper_atmosphere_shell function - Implementation missing
def create_jupiter_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.1,  # Extends about 10% beyond the visible radius
        'color': 'rgb(220, 240, 255)',  # optical
        'opacity': 0.5,
        'name': 'Upper Atmosphere',
        'description': (
            "Jupiter's upper atmosphere includes the stratosphere and thermosphere.<br>"
            "It's less dense than the cloud layer below and contains hydrocarbon haze<br>"
            "produced by solar ultraviolet radiation. Aurora activity can be observed<br>"
            "at Jupiter's poles, caused by interactions with its magnetic field. Temperature<br>"
            "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

def create_jupiter_magnetosphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's magnetosphere shell."""
    # Call the existing create_jupiter_magnetosphere function
    return create_jupiter_magnetosphere(center_position)
    
def create_jupiter_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 530,  # Jupiter's Hill sphere is about 530 Jupiter radii
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"
        )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_ring_system_info = (
                "Jupiter's Main Ring is a relatively bright and very thin ring.\n"
                "It extends from about 122,500 km to 129,000 km from Jupiter's center.\n"
                "Its thickness is only about 30-300 km.\n"
                "The main ring is reddish and composed of dust ejected from Jupiter's small inner moons,\n"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids.\n\n"

                "The Halo Ring is a faint, thick torus of material.\n"
                "It extends inward from the main ring to about 100,000 km from Jupiter's center.\n"
                "It is much thicker than the main ring, extending about 12,500 km vertically.\n"
                "The ring likely consists of fine dust particles pushed out of the main ring\n"
                "by electromagnetic forces from Jupiter's powerful magnetosphere.\n\n" 

                "The Amalthea Gossamer Ring is an extremely faint and wide ring.\n"
                "It extends outwards from the main ring (129,000 km) to Amalthea's orbit (182,000 km).\n"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.\n"
                "It is much fainter and more diffuse than the main ring.\n\n"    

                "The Thebe Gossamer Ring is another very faint and wide ring.\n"
                "It extends outwards from the main ring (129,000 km) to beyond Thebe's orbit (226,000 km).\n"
                "It is composed of dust particles ejected from Thebe by micrometeoroid impacts.\n"
                "It is the faintest of Jupiter's rings, with a vertical extension of about 8,600 km."                                           
)

def create_jupiter_ring_system(center_position=(0, 0, 0)):
    """
    Creates a visualization of Jupiter's ring system.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Jupiter's center
        
    Returns:
        list: A list of plotly traces representing the ring components
    """
    traces = []
    
    # Define Jupiter's ring parameters in kilometers from Jupiter's center
    # Then convert to Jupiter radii, and finally to AU
    ring_params = {
        'main_ring': {
            'inner_radius_km': 122500,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 129000,  # Outer edge (in km from Jupiter's center)
            'thickness_km': 30,         # Approximate thickness
            'color': 'rgb(180, 120, 100)',  # Reddish color
            'opacity': 0.7,
            'name': 'Main Ring',
            'description': (
                "Jupiter's Main Ring is a relatively bright and very thin ring.<br>"
                "It extends from about 122,500 km to 129,000 km from Jupiter's center.<br>"
                "Its thickness is only about 30-300 km.<br>"
                "The main ring is reddish and composed of dust ejected from Jupiter's small inner moons,<br>"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids."
            )
        },
        'halo_ring': {
            'inner_radius_km': 100000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 122500,  # Outer edge (in km from Jupiter's center)
            'thickness_km': 12500,      # Approximate thickness (thicker than the main ring)
            'color': 'rgb(150, 150, 150)',  # Grayish color
            'opacity': 0.4,
            'name': 'Halo Ring',
            'description': (
                "The Halo Ring is a faint, thick torus of material.<br>"
                "It extends inward from the main ring to about 100,000 km from Jupiter's center.<br>"
                "It is much thicker than the main ring, extending about 12,500 km vertically.<br>"
                "The ring likely consists of fine dust particles pushed out of the main ring<br>"
                "by electromagnetic forces from Jupiter's powerful magnetosphere."
            )
        },
        'amalthea_gossamer': {
            'inner_radius_km': 129000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 182000,  # Outer edge (at Amalthea's orbit)
            'thickness_km': 2000,       # Approximate thickness
            'color': 'rgb(170, 170, 190)',  # Faint bluish-gray
            'opacity': 0.2,
            'name': 'Amalthea Gossamer Ring',
            'description': (
                "The Amalthea Gossamer Ring is an extremely faint and wide ring.<br>"
                "It extends outwards from the main ring (129,000 km) to Amalthea's orbit (182,000 km).<br>"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.<br>"
                "It is much fainter and more diffuse than the main ring."
            )
        },
        'thebe_gossamer': {
            'inner_radius_km': 129000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 226000,  # Outer edge (at Thebe's orbit)
            'thickness_km': 8600,       # Approximate thickness
            'color': 'rgb(170, 170, 190)',  # Faint bluish-gray (same as Amalthea ring)
            'opacity': 0.15,
            'name': 'Thebe Gossamer Ring',
            'description': (
                "The Thebe Gossamer Ring is another very faint and wide ring.<br>"
                "It extends outwards from the main ring (129,000 km) to beyond Thebe's orbit (226,000 km).<br>"
                "It is composed of dust particles ejected from Thebe by micrometeoroid impacts.<br>"
                "It is the faintest of Jupiter's rings, with a vertical extension of about 8,600 km."
            )
        }
    }
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create traces for each ring
    for ring_name, ring_info in ring_params.items():
        # Convert km to AU
        inner_radius_au = ring_info['inner_radius_km'] / KM_PER_AU
        outer_radius_au = ring_info['outer_radius_km'] / KM_PER_AU
        thickness_au = ring_info['thickness_km'] / KM_PER_AU
        
        # Reduce point count for very large rings to improve performance
        n_points = 100
        if 'gossamer' in ring_name:
            n_points = 80  # Fewer points for larger gossamer rings
        
        # Create ring points
        x, y, z = create_ring_points(inner_radius_au, outer_radius_au, n_points, thickness_au)
        
        # Apply center position offset
        x = np.array(x) + center_x
        y = np.array(y) + center_y
        z = np.array(z) + center_z
        
        # Create a text list for hover information
        text_array = [ring_info['description'] for _ in range(len(x))]
        
        # Add ring trace
        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.5,  # Small markers for rings
                    color=ring_info['color'],
                    opacity=ring_info['opacity']
                ),
                name=f"Jupiter: {ring_info['name']}",
                text=text_array,
                customdata=[f"Jupiter: {ring_info['name']}"] * len(x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces

jupiter_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n\n"

            "Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side\n"
            "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.\n"
            "It traps charged particles, creating intense radiation belts that would be lethal to humans.\n\n"

            "Io plasma torus: A donut-shaped region of charged particles emanating from\n"
            "Jupiter's moon Io due to volcanic activity. These particles become trapped\n"
            "in Jupiter's magnetic field, forming this distinctive structure.\n\n"  

            "Inner radiation belt: Intense region of trapped high-energy particles near Jupiter\n"
            "Middle radiation belt: Region of trapped charged particles at intermediate distances from Jupiter\n"
            "Outer radiation belt: Extended region of trapped particles in Jupiter's outer magnetosphere"                      
)

def create_magnetosphere_shape(params):
    """
    Creates points for a magnetosphere with asymmetry, compressed on sunward side
    and extended on the tail side.
    
    Parameters:
        params (dict): Dictionary of shape parameters
        
    Returns:
        tuple: (x, y, z) coordinates as lists
    """
    x_coords = []
    y_coords = []
    z_coords = []
    
    # Number of points to generate (reduced for memory efficiency)
    n_phi = 20              # from 30 to 20
    n_theta = 20            # from 30 to 20
    n_tail_segments = 10    # from 20 to 10
    
    # 1. Generate sunward hemisphere (compressed, use an ellipsoid)
    for i_phi in range(int(n_phi/2)):
        phi = (i_phi / (n_phi-1)) * np.pi
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            
            # Use ellipsoidal shaping - compress in x direction (sunward)
            x = -params['sunward_distance'] * np.cos(phi)  # Negative for sunward direction
            rho = np.sin(phi)
            y = params['equatorial_radius'] * rho * np.cos(theta)
            z = params['polar_radius'] * rho * np.sin(theta)
            
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)
    
    # 2. Generate magnetotail (anti-sunward direction, expands outward)
    for i in range(n_tail_segments + 1):
        fraction = i / n_tail_segments
        tail_x = fraction * params['tail_length']  # Positive for tail direction
        tail_radius = params['tail_base_radius'] + (params['tail_end_radius'] - params['tail_base_radius']) * fraction
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            y = tail_radius * np.cos(theta)
            z = tail_radius * np.sin(theta)
            
            x_coords.append(tail_x)
            y_coords.append(y)
            z_coords.append(z)
    
    return x_coords, y_coords, z_coords

def create_jupiter_magnetosphere(center_position=(0, 0, 0)):
    """
    Creates a realistic visualization of Jupiter's magnetosphere.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Jupiter's center
        
    Returns:
        list: A list of plotly traces representing the magnetosphere components
    """
    traces = []
    
    # Parameters for magnetosphere components (in Jupiter radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 50,  # Compressed toward the sun
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 100,
        'polar_radius': 80,
        
        # Magnetotail parameters
        'tail_length': 500,  # Length of visible magnetotail
        'tail_base_radius': 150,  # Radius at the base of the tail
        'tail_end_radius': 200,  # Radius at the end of the tail
        
        # Io plasma torus
        'io_torus_distance': 5.9,  # Io's orbit is at about 5.9 Jupiter radii
        'io_torus_thickness': 2,
        'io_torus_width': 1,
        
        # Radiation belts
        'inner_belt_distance': 1.5,
        'middle_belt_distance': 3,
        'outer_belt_distance': 6,
        'belt_thickness': 0.5
    }
    
    # Scale everything by Jupiter's radius in AU
    for key in params:
        params[key] *= JUPITER_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
# Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(200, 200, 255)', # Light blue for magnetic field
                opacity=0.3
            ),
            name='Jupiter: Magnetosphere',
            text=["Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
                  "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
                  "It traps charged particles, creating intense radiation belts that would be lethal to humans."] * len(x),
            customdata=['Jupiter: Magnetosphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 2. Create and add Io plasma torus with a different color
    io_torus_x = []
    io_torus_y = []
    io_torus_z = []
    
    n_points = 100
    n_rings = 8
    
    for i_ring in range(n_rings):
        # Vary the radius slightly to create thickness
        radius_offset = (i_ring / (n_rings-1) - 0.5) * params['io_torus_thickness']
        torus_radius = params['io_torus_distance'] + radius_offset
        
        for i in range(n_points):
            angle = (i / n_points) * 2 * np.pi

            # Position in x-y plane (equatorial)
            x = torus_radius * np.cos(angle)
            y = torus_radius * np.sin(angle)
            z = 0  # In the equatorial plane    
            
            # Add some thickness variation
            jitter = (np.random.random() - 0.5) * params['io_torus_width']
            
            io_torus_x.append(x)
            io_torus_y.append(y)
            io_torus_z.append(z + jitter)     # Apply jitter to z axis
    
    # Apply center position offset
    io_torus_x = np.array(io_torus_x) + center_x
    io_torus_y = np.array(io_torus_y) + center_y
    io_torus_z = np.array(io_torus_z) + center_z

    # Create the Io plasma torus hover text and customdata arrays
    io_text = ["Io plasma torus: A donut-shaped region of charged particles emanating from<br>"
              "Jupiter's moon Io due to volcanic activity. These particles become trapped<br>"
              "in Jupiter's magnetic field, forming this distinctive structure."] * len(io_torus_x)
    io_customdata = ['Jupiter: Io Plasma Torus'] * len(io_torus_x)
    
    traces.append(
        go.Scatter3d(
            x=io_torus_x,
            y=io_torus_y,
            z=io_torus_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 100, 100)',  # Reddish color for plasma torus
                opacity=0.3
            ),
            name='Jupiter: Io Plasma Torus',
            text=io_text,
            customdata=io_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 3. Create and add radiation belts with different colors
    belt_colors = ['rgb(255, 255, 100)', 'rgb(100, 255, 150)', 'rgb(100, 200, 255)']
    belt_names = ['Jupiter: Inner Radiation Belt', 'Jupiter: Middle Radiation Belt', 'Jupiter: Outer Radiation Belt']
    belt_texts = [
        "Inner radiation belt: Intense region of trapped high-energy particles near Jupiter",
        "Middle radiation belt: Region of trapped charged particles at intermediate distances from Jupiter",
        "Outer radiation belt: Extended region of trapped particles in Jupiter's outer magnetosphere"
    ]
    
    belt_distances = [
        params['inner_belt_distance'],
        params['middle_belt_distance'],
        params['outer_belt_distance']
    ]
    
    for i, belt_distance in enumerate(belt_distances):
        belt_x = []
        belt_y = []
        belt_z = []
        
        n_points = 80
        n_rings = 5
        
        for i_ring in range(n_rings):
            # Vary the radius slightly to create thickness
            radius_offset = (i_ring / (n_rings-1) - 0.5) * params['belt_thickness']
            belt_radius = belt_distance + radius_offset
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # Create a belt around Jupiter's rotational axis
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # Add some z variation based on angle to create the shape of a belt
                # rather than a perfect torus (thinner near poles)
                z_scale = 0.2 * belt_radius  # Controls how flat the belts are
                z = z_scale * np.sin(2 * angle)
                
                belt_x.append(x)
                belt_y.append(y)
                belt_z.append(z)
        
        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z
        
        # Create the radiation belt hover text and customdata arrays
        belt_text = [belt_texts[i]] * len(belt_x)
        belt_customdata = [belt_names[i]] * len(belt_x)

        traces.append(
            go.Scatter3d(
                x=belt_x,
                y=belt_y,
                z=belt_z,
                mode='markers',
                marker=dict(
                    size=1.5,
                    color=belt_colors[i],
                    opacity=0.3
                ),
                name=belt_names[i],
                text=belt_text,
                customdata=belt_customdata,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces

jupiter_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.\n\n" 
            "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"                      
)

def create_jupiter_hill_sphere(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere."""
    # Hill sphere radius in Jupiter radii
    radius_fraction = 530  # Jupiter's Hill sphere is about 530 Jupiter radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * JUPITER_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"
    
    # Create the trace
    traces = [
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(0, 255, 0)',  # Green for Hill sphere
                opacity=0.3
            ),
            name='Jupiter: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Jupiter: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

# Earth Shell Creation Functions

earth_inner_core_info = (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.\n"
            "Despite incredible pressure, temperatures of 5,400°C (9,800°F) keep it nearly\n"
            "at melting point. It rotates slightly faster than the rest of Earth, creating\n"
            "complex dynamics in Earth's magnetic field. The inner core is approximately\n"
            "1,220 km (760 miles) in radius."
)

def create_earth_inner_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.19,  # Inner core: 0-19% of Earth's radius
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.<br>"
            "Despite incredible pressure, temperatures of 5,400°C (9,800°F) keep it nearly<br>"
            "at melting point. It rotates slightly faster than the rest of Earth, creating<br>"
            "complex dynamics in Earth's magnetic field. The inner core is approximately<br>"
            "1,220 km (760 miles) in radius."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=4.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_outer_core_info = (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.\n"
            "Convection currents in this highly conductive fluid generate Earth's\n"
            "magnetic field through a process called the geodynamo. It extends from\n"
            "1,220 to 3,500 km from Earth's center and has temperatures ranging from\n"
            "4,500°C (8,100°F) to 5,400°C (9,800°F)."
)

def create_earth_outer_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.55,  # Outer core: 19-55% of Earth's radius
        'color': 'rgb(255, 140, 0)',  # Deeper orange for liquid metal
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.<br>"
            "Convection currents in this highly conductive fluid generate Earth's<br>"
            "magnetic field through a process called the geodynamo. It extends from<br>"
            "1,220 to 3,500 km from Earth's center and has temperatures ranging from<br>"
            "4,500°C (8,100°F) to 5,400°C (9,800°F)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.7,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_lower_mantle_info = (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.\n"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.\n"
            "This region extends from 660 to 2,900 km below Earth's surface and experiences\n"
            "temperatures from 2,200°C to 4,500°C (4,000°F to 8,100°F) and extreme pressure."
)

def create_earth_lower_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Lower mantle: 55-85% of Earth's radius
        'color': 'rgb(230, 100, 20)',  # Reddish-brown
        'opacity': 0.7,
        'name': 'Lower Mantle',
        'description': (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.<br>"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.<br>"
            "This region extends from 660 to 2,900 km below Earth's surface and experiences<br>"
            "temperatures from 2,200°C to 4,500°C (4,000°F to 8,100°F) and extreme pressure."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.4,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_upper_mantle_info = (
            "The upper mantle includes the asthenosphere, a partially molten layer where\n"
            "most magma originates. This region flows more readily than the lower mantle,\n"
            "allowing tectonic plates to move. It extends from about 30 to 660 km below\n"
            "the surface, with temperatures from 500°C to 2,200°C (900°F to 4,000°F)."
)

def create_earth_upper_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.98,  # Upper mantle: 85-98% of Earth's radius
        'color': 'rgb(205, 85, 85)',  # Lighter reddish-brown
        'opacity': 0.6,
        'name': 'Upper Mantle',
        'description': (
            "The upper mantle includes the asthenosphere, a partially molten layer where<br>"
            "most magma originates. This region flows more readily than the lower mantle,<br>"
            "allowing tectonic plates to move. It extends from about 30 to 660 km below<br>"
            "the surface, with temperatures from 500°C to 2,200°C (900°F to 4,000°F)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.1,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_crust_info = (
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into\n"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)\n"
            "made primarily of granite. The crust contains all known life and the accessible portion\n"
            "of Earth's geological resources. Surface temperatures range from -80°C to 60°C (-112°F to 140°F)."
)

def create_earth_crust_shell(center_position=(0, 0, 0)):
    """Creates Earth's crust shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 98-100% of Earth's radius
        'color': 'rgb(70, 120, 160)',  # Bluish for oceans, brown for land
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into<br>"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)<br>"
            "made primarily of granite. The crust contains all known life and the accessible portion<br>"
            "of Earth's geological resources. Surface temperatures range from -80°C to 60°C (-112°F to 140°F)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_atmosphere_info = (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\n"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain\n"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from\n"
            "about 15°C (59°F) at sea level to -60°C (-76°F) at the stratopause."
)

def create_earth_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.05,  # Troposphere and stratosphere
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Lower Atmosphere',
        'description': (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>"
            "about 15°C (59°F) at sea level to -60°C (-76°F) at the stratopause."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.5,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_upper_atmosphere_info = (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\n"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\n"
            "the International Space Station orbits, and the exosphere which gradually transitions\n"
            "to space. In the thermosphere, temperatures can reach 2,000°C (3,600°F), though the\n"
            "gas is so thin that it would feel cold to human skin."
)

def create_earth_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.25,  # Mesosphere, thermosphere, and exosphere
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Upper Atmosphere',
        'description': (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes<br>"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and<br>"
            "the International Space Station orbits, and the exosphere which gradually transitions<br>"
            "to space. In the thermosphere, temperatures can reach 2,000°C (3,600°F), though the<br>"
            "gas is so thin that it would feel cold to human skin."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 

            "Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side\n"
            "and stretches into a long magnetotail on the night side. It protects Earth\n"
            "from solar radiation and cosmic rays, making complex life possible.\n\n"

            "Bow Shock: The boundary where the supersonic solar wind is first slowed\n"
            "by Earth's magnetic field, typically located about 15 Earth radii upstream\n"
            "from Earth on the Sun-facing side.\n\n"

            "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\n"
            "extending from about 1,000 km to 6,000 km above Earth's surface.\n"
            "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\n"
            "extending from about 13,000 km to 60,000 km above Earth's surface."
)

def create_earth_magnetosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's magnetosphere."""
    traces = []
    
    # Parameters for magnetosphere components (in Earth radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 10,  # Compressed toward the sun
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 12,
        'polar_radius': 10,
        
        # Magnetotail parameters
        'tail_length': 100,  # Length of visible magnetotail
        'tail_base_radius': 15,  # Radius at the base of the tail
        'tail_end_radius': 25,  # Radius at the end of the tail
        
        # Radiation belts
        'inner_belt_distance': 1.5,  # Distance in Earth radii
        'outer_belt_distance': 4.5,  # Distance in Earth radii
        'belt_thickness': 0.5,
    }
    
    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= EARTH_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    magnetosphere_text = ["Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side<br>"
                 "and stretches into a long magnetotail on the night side. It protects Earth<br>"
                 "from solar radiation and cosmic rays, making complex life possible."]
    
    magnetosphere_customdata = ['Earth: Magnetosphere']

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Earth: Magnetosphere',
            text=magnetosphere_text * len(x),
            customdata=magnetosphere_customdata * len(x),      
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 2. Create and add bow shock
    bow_shock_x = []
    bow_shock_y = []
    bow_shock_z = []
    
    n_phi = 30
    n_theta = 30
    bow_shock_standoff = 15 * EARTH_RADIUS_AU
    bow_shock_width = 25 * EARTH_RADIUS_AU
    
    # Create a paraboloid for the bow shock
    for i_phi in range(n_phi):
        phi = (i_phi / (n_phi-1)) * np.pi  # Only the front half
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            
            # Paraboloid shape, flattened in x-direction for bow shock
            x = -bow_shock_standoff * np.cos(phi)  # Negative for sunward direction
            rho = bow_shock_width * (1 + np.sin(phi)) / 2  # Wider for larger phi (away from sun)
            y = rho * np.cos(theta)
            z = rho * np.sin(theta)
            
            bow_shock_x.append(x)
            bow_shock_y.append(y)
            bow_shock_z.append(z)
    
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
    
    bow_shock_text = ["Bow Shock: The boundary where the supersonic solar wind is first slowed<br>"
                "by Earth's magnetic field, typically located about 15 Earth radii upstream<br>"
                "from Earth on the Sun-facing side."]
    
    bow_shock_customdata = ['Earth: Bow Shock']

    traces.append(
        go.Scatter3d(
            x=bow_shock_x,
            y=bow_shock_y,
            z=bow_shock_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 200, 150)',  # Orange-ish color for bow shock
                opacity=0.2
            ),
            name='Earth: Bow Shock',
            text=bow_shock_text * len(bow_shock_x),
            customdata=bow_shock_customdata * len(bow_shock_x),  # This was the line causing the error
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 3. Create and add Van Allen radiation belts
    belt_colors = ['rgb(255, 100, 100)', 'rgb(100, 200, 255)']
    belt_names = ['Earth: Inner Radiation Belt', 'Earth: Outer Radiation Belt']
    belt_texts = [
        "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)<br>"
        "extending from about 1,000 km to 6,000 km above Earth's surface.",
        "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)<br>"
        "extending from about 13,000 km to 60,000 km above Earth's surface."
    ]
    
    belt_distances = [
        params['inner_belt_distance'],
        params['outer_belt_distance']
    ]
    
    for i, belt_distance in enumerate(belt_distances):
        belt_x = []
        belt_y = []
        belt_z = []
        
        n_points = 80
        n_rings = 5
        
        for i_ring in range(n_rings):
            # Vary the radius slightly to create thickness
            radius_offset = (i_ring / (n_rings-1) - 0.5) * params['belt_thickness']
            belt_radius = belt_distance + radius_offset
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # Create a belt around Earth's rotational axis
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # Add some z variation based on angle to create the shape of a belt
                # rather than a perfect torus (thinner near poles)
                z_scale = 0.2 * belt_radius  # Controls how flat the belts are
                z = z_scale * np.sin(2 * angle)
                
                belt_x.append(x)
                belt_y.append(y)
                belt_z.append(z)
        
        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z
        
        belt_text = [belt_texts[i]]
        belt_customdata = [belt_names[i]]

        traces.append(
            go.Scatter3d(
                x=belt_x,
                y=belt_y,
                z=belt_z,
                mode='markers',
                marker=dict(
                    size=1.5,
                    color=belt_colors[i],
                    opacity=0.2
                ),
                name=belt_names[i],
                text=belt_text * len(belt_x),
                customdata=belt_customdata * len(belt_x),  # Fix here as well
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces

earth_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
            "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)."
)

def create_earth_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's Hill sphere."""
    # Hill sphere radius in Earth radii
    radius_fraction = 235  # Earth's Hill sphere is about 235 Earth radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * EARTH_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)"
    
    # Create the trace
    traces = [
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(0, 255, 0)',  # Green for Hill sphere
                opacity=0.15
            ),
            name='Earth: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Earth: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces