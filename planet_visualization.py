"""
Celestial Body Visualization Module
==================================
Functions for creating layered visualizations of solar system bodies (Sun, planets) in 3D plots.
Each celestial body has individual shell components that can be toggled with selection variables.
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS, CENTER_BODY_RADII)

from solar_visualization_shells import (
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

from solar_visualization_shells import (create_sun_core_shell,
                                        create_sun_radiative_shell,
                                        create_sun_photosphere_shell,
                                        create_sun_chromosphere_shell,
                                        create_sun_inner_corona_shell,
                                        create_sun_outer_corona_shell,
                                        create_sun_termination_shock_shell,
                                        create_sun_heliopause_shell,

                                        create_sun_inner_oort_limit_shell,
                                        create_sun_inner_oort_shell,
                                        create_sun_outer_oort_shell,

                                        create_sun_hills_cloud_torus,
                                        create_sun_outer_oort_clumpy,
                                        create_sun_galactic_tide,
                                        create_sun_gravitational_shell)

from mercury_visualization_shells import (create_mercury_inner_core_shell, 
                                          create_mercury_outer_core_shell, 
                                          create_mercury_mantle_shell, 
                                          create_mercury_crust_shell, 
                                          create_mercury_atmosphere_shell, 
                                          create_mercury_sodium_tail,
                                          create_mercury_magnetosphere_shell, 
                                          create_mercury_hill_sphere_shell,
                                          mercury_inner_core_info, 
                                          mercury_outer_core_info, 
                                          mercury_mantle_info, 
                                          mercury_crust_info, 
                                          mercury_atmosphere_info, 
                                          mercury_sodium_tail_info, 
                                          mercury_magnetosphere_info, 
                                          mercury_hill_sphere_info)

from venus_visualization_shells import (create_venus_core_shell,  
                                        create_venus_mantle_shell, 
                                          create_venus_crust_shell, 
                                          create_venus_atmosphere_shell, 
                                          create_venus_upper_atmosphere_shell,                                           
                                          create_venus_magnetosphere_shell, 
                                          create_venus_hill_sphere_shell,
                                          venus_core_info, 
                                          venus_mantle_info, 
                                          venus_crust_info, 
                                          venus_atmosphere_info, 
                                          venus_upper_atmosphere_info,                                           
                                          venus_magnetosphere_info, 
                                          venus_hill_sphere_info)

from earth_visualization_shells import (create_earth_inner_core_shell, 
                                        create_earth_outer_core_shell, 
                                        create_earth_lower_mantle_shell,
                                        create_earth_upper_mantle_shell, 
                                        create_earth_crust_shell, 
                                        create_earth_atmosphere_shell, 
                                        create_earth_upper_atmosphere_shell,                                           
                                        create_earth_magnetosphere_shell, 
                                        create_earth_hill_sphere_shell,
                                        earth_inner_core_info, 
                                        earth_outer_core_info,
                                        earth_lower_mantle_info, 
                                        earth_upper_mantle_info,
                                        earth_crust_info, 
                                        earth_atmosphere_info, 
                                        earth_upper_atmosphere_info,                                           
                                        earth_magnetosphere_info, 
                                        earth_hill_sphere_info)

from moon_visualization_shells import (create_moon_inner_core_shell, 
                                        create_moon_outer_core_shell, 
                                        create_moon_mantle_shell,
                                        create_moon_crust_shell, 
                                        create_moon_exosphere_shell,  
                                        create_moon_hill_sphere_shell,
                                        moon_inner_core_info, 
                                        moon_outer_core_info,
                                        moon_mantle_info, 
                                        moon_crust_info, 
                                        moon_exosphere_info,  
                                        moon_hill_sphere_info)

from mars_visualization_shells import (create_mars_inner_core_shell, 
                                        create_mars_outer_core_shell, 
                                        create_mars_mantle_shell,
                                        create_mars_crust_shell, 
                                        create_mars_atmosphere_shell,
                                        create_mars_upper_atmosphere_shell,
                                        create_mars_magnetosphere_shell,                                           
                                        create_mars_hill_sphere_shell,
                                        mars_inner_core_info, 
                                        mars_outer_core_info,
                                        mars_mantle_info, 
                                        mars_crust_info, 
                                        mars_atmosphere_info, 
                                        mars_upper_atmosphere_info,
                                        mars_magnetosphere_info,                                           
                                        mars_hill_sphere_info)

from asteroid_belt_visualization_shells import (
                                        create_main_asteroid_belt,
                                        create_hilda_group,
                                        create_jupiter_trojans_greeks,
                                        create_jupiter_trojans_trojans,
                                        main_belt_info,
                                        hilda_group_info,
                                        jupiter_trojans_greeks_info,
                                        jupiter_trojans_trojans_info,
                                        get_jupiter_angle_from_data,
                                        calculate_body_angle,
                                        estimate_jupiter_angle_from_date)

from jupiter_visualization_shells import (create_jupiter_core_shell, 
                                        create_jupiter_metallic_hydrogen_shell, 
                                        create_jupiter_molecular_hydrogen_shell,
                                        create_jupiter_cloud_layer_shell, 
                                        create_jupiter_upper_atmosphere_shell,
                                        create_jupiter_ring_system,                                                                                   
                                        create_jupiter_radiation_belts,
                                        create_jupiter_io_plasma_torus,
                                        create_jupiter_magnetosphere, 
                                        create_jupiter_hill_sphere_shell,
                                        jupiter_core_info, 
                                        jupiter_metallic_hydrogen_info, 
                                        jupiter_molecular_hydrogen_info,
                                        jupiter_cloud_layer_info, 
                                        jupiter_upper_atmosphere_info,
                                        jupiter_ring_system_info,                                                                                   
                                        jupiter_radiation_belts_info,
                                        jupiter_io_plasma_torus_info,
                                        jupiter_magnetosphere_info, 
                                        jupiter_hill_sphere_info)

from saturn_visualization_shells import (create_saturn_core_shell, 
                                        create_saturn_metallic_hydrogen_shell, 
                                        create_saturn_molecular_hydrogen_shell,
                                        create_saturn_cloud_layer_shell, 
                                        create_saturn_upper_atmosphere_shell,
                                        create_saturn_ring_system,                                                                                   
                                        create_saturn_radiation_belts,
                                        create_saturn_enceladus_plasma_torus,
                                        create_saturn_magnetosphere, 
                                        create_saturn_hill_sphere_shell,
                                        saturn_core_info, 
                                        saturn_metallic_hydrogen_info, 
                                        saturn_molecular_hydrogen_info,
                                        saturn_cloud_layer_info, 
                                        saturn_upper_atmosphere_info,
                                        saturn_ring_system_info,                                                                                   
                                        saturn_radiation_belts_info,
                                        saturn_enceladus_plasma_torus_info,
                                        saturn_magnetosphere_info, 
                                        saturn_hill_sphere_info)

from uranus_visualization_shells import (create_uranus_core_shell, 
                                        create_uranus_mantle_shell, 
                                        create_uranus_cloud_layer_shell, 
                                        create_uranus_upper_atmosphere_shell,
                                        create_uranus_ring_system,                                                                                   
                                        create_uranus_radiation_belts,
                                        create_uranus_magnetosphere, 
                                        create_uranus_hill_sphere_shell,
                                        uranus_core_info, 
                                        uranus_mantle_info, 
                                        uranus_cloud_layer_info, 
                                        uranus_upper_atmosphere_info,
                                        uranus_ring_system_info,                                                                                   
                                        uranus_radiation_belts_info,
                                        uranus_magnetosphere_info, 
                                        uranus_hill_sphere_info)

from neptune_visualization_shells import (create_neptune_core_shell, 
                                        create_neptune_mantle_shell, 
                                        create_neptune_cloud_layer_shell, 
                                        create_neptune_upper_atmosphere_shell,
                                        create_neptune_ring_system,                                                                                   
                                        create_neptune_radiation_belts,
                                        create_neptune_magnetosphere, 
                                        create_neptune_hill_sphere_shell,
                                        neptune_core_info, 
                                        neptune_mantle_info, 
                                        neptune_cloud_layer_info, 
                                        neptune_upper_atmosphere_info,
                                        neptune_ring_system_info,                                                                                   
                                        neptune_radiation_belts_info,
                                        neptune_magnetosphere_info, 
                                        neptune_hill_sphere_info)

from pluto_visualization_shells import (create_pluto_core_shell,  
                                        create_pluto_mantle_shell,
                                        create_pluto_crust_shell, 
                                        create_pluto_haze_layer_shell, 
                                        create_pluto_atmosphere_shell,                                           
                                        create_pluto_hill_sphere_shell,
                                        pluto_core_info, 
                                        pluto_mantle_info,
                                        pluto_crust_info, 
                                        pluto_haze_layer_info, 
                                        pluto_atmosphere_info,                                           
                                        pluto_hill_sphere_info)

from eris_visualization_shells import (create_eris_core_shell,  
                                        create_eris_mantle_shell,
                                        create_eris_crust_shell,  
                                        create_eris_atmosphere_shell,                                           
                                        create_eris_hill_sphere_shell,
                                        eris_core_info, 
                                        eris_mantle_info,
                                        eris_crust_info, 
                                        eris_atmosphere_info,                                           
                                        eris_hill_sphere_info)

from planet9_visualization_shells import (create_planet9_surface_shell,                                           
                                        create_planet9_hill_sphere_shell,
                                        planet9_surface_info,                                           
                                        planet9_hill_sphere_info)


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
# Constants
KM_PER_AU = 149597870.7  # Conversion factor from km to AU

# Mercury Constants
MERCURY_RADIUS_KM = CENTER_BODY_RADII['Mercury']        
MERCURY_RADIUS_AU = MERCURY_RADIUS_KM / KM_PER_AU

# Venus Constants
VENUS_RADIUS_KM = CENTER_BODY_RADII['Venus']
VENUS_RADIUS_AU = VENUS_RADIUS_KM / KM_PER_AU

# Earth Constants
EARTH_RADIUS_KM = CENTER_BODY_RADII['Earth']
EARTH_RADIUS_AU = EARTH_RADIUS_KM / KM_PER_AU

# Moon Constants
MOON_RADIUS_KM = CENTER_BODY_RADII['Moon']
MOON_RADIUS_AU = MOON_RADIUS_KM / KM_PER_AU

# Mars Constants
MARS_RADIUS_KM = CENTER_BODY_RADII['Mars']  # JPL uses an equipotential virtual surface with a mean radius at the equator as the Mars datum. 
MARS_RADIUS_AU = MARS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Jupiter Constants
JUPITER_RADIUS_KM = CENTER_BODY_RADII['Jupiter']  # Equatorial radius in km
JUPITER_RADIUS_AU = JUPITER_RADIUS_KM / KM_PER_AU  # Convert to AU

# Saturn Constants
SATURN_RADIUS_KM = CENTER_BODY_RADII['Saturn']  # Equatorial radius in km
SATURN_RADIUS_AU = SATURN_RADIUS_KM / KM_PER_AU  # Convert to AU

# Uranus Constants
URANUS_RADIUS_KM = CENTER_BODY_RADII['Uranus']  # Equatorial radius in km
URANUS_RADIUS_AU = URANUS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Neptune Constants
NEPTUNE_RADIUS_KM = CENTER_BODY_RADII['Neptune']  # Equatorial radius in km
NEPTUNE_RADIUS_AU = NEPTUNE_RADIUS_KM / KM_PER_AU  # Convert to AU

# Pluto Constants
PLUTO_RADIUS_KM = CENTER_BODY_RADII['Pluto']  # Equatorial radius in km
PLUTO_RADIUS_AU = PLUTO_RADIUS_KM / KM_PER_AU  # Convert to AU

# Eris Constants
ERIS_RADIUS_KM = CENTER_BODY_RADII['Eris']  # Equatorial radius in km
ERIS_RADIUS_AU = ERIS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Planet 9 Constants
PLANET9_RADIUS_KM = CENTER_BODY_RADII['Planet 9']  # Equatorial radius in km
PLANET9_RADIUS_AU = PLANET9_RADIUS_KM / KM_PER_AU  # Convert to AU

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

        if sun_shell_vars['galactic_tide'].get() == 1:
            traces.extend(create_sun_galactic_tide())    

        if sun_shell_vars['outer_oort_clumpy'].get() == 1:
            traces.extend(create_sun_outer_oort_clumpy())   

        if sun_shell_vars['hills_cloud_torus'].get() == 1:
            traces.extend(create_sun_hills_cloud_torus())       
            

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


        if sun_shell_vars['trojans_greeks'].get() == 1:
            # Get Jupiter's current position for L4 point calculation
            jupiter_angle = 0  # Default angle
            # If Jupiter data is available in the current context, calculate its angle
            # This would need to be passed from the calling context
            traces.extend(create_jupiter_trojans_greeks(jupiter_angle=jupiter_angle))
        
        if sun_shell_vars['trojans_trojans'].get() == 1:
            # Get Jupiter's current position for L5 point calculation
            jupiter_angle = 0  # Default angle
            # If Jupiter data is available in the current context, calculate its angle
            # This would need to be passed from the calling context
            traces.extend(create_jupiter_trojans_trojans(jupiter_angle=jupiter_angle))


        if sun_shell_vars['main_belt'].get() == 1:
            traces.extend(create_main_asteroid_belt())
        
        if sun_shell_vars['hildas'].get() == 1:
            traces.extend(create_hilda_group())

            
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

def create_sun_corona_from_distance(fig, sun_shell_vars, sun_position):
    """
    Creates a simplified Sun corona visualization for non-Sun-centered views.
    Uses a simpler particle representation that scales appropriately.
    
    Parameters:
        fig: The plotly figure
        sun_shell_vars: Dictionary of Sun shell selection variables
        sun_position: (x, y, z) tuple of Sun's position in AU
        
    Returns:
        Updated figure
    """
    import numpy as np
    import plotly.graph_objects as go
    
    # Simple sphere generation at Sun's position
    def create_offset_sphere(radius_au, n_points=30):
        """Create sphere points offset to sun_position"""
        phi = np.linspace(0, 2*np.pi, n_points)
        theta = np.linspace(0, np.pi, n_points)
        phi, theta = np.meshgrid(phi, theta)
        
        x = radius_au * np.sin(theta) * np.cos(phi) + sun_position[0]
        y = radius_au * np.sin(theta) * np.sin(phi) + sun_position[1]
        z = radius_au * np.cos(theta) + sun_position[2]
        
        return x.flatten(), y.flatten(), z.flatten()
    
    # Add selected layers (outermost to innermost)
    if sun_shell_vars.get('outer_corona') and sun_shell_vars['outer_corona'].get() == 1:
        radius = OUTER_CORONA_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=0.5, color='rgba(255, 245, 200, 0.3)', opacity=0.3),
            name='Sun: Outer Corona',
            hovertemplate='Sun: Outer Corona<br>~10 solar radii<br>Temperature: ~2M K<extra></extra>',
            showlegend=True
        ))
    
    if sun_shell_vars.get('inner_corona') and sun_shell_vars['inner_corona'].get() == 1:
        radius = INNER_CORONA_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=0.75, color='rgba(255, 235, 180, 0.4)', opacity=0.4),
            name='Sun: Inner Corona',
            hovertemplate='Sun: Inner Corona<br>~3 solar radii<br>Temperature: 1-3M K<extra></extra>',
            showlegend=True
        ))
    
    if sun_shell_vars.get('chromosphere') and sun_shell_vars['chromosphere'].get() == 1:
        radius = CHROMOSPHERE_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=1.0, color='rgba(255, 100, 100, 0.5)', opacity=0.5),
            name='Sun: Chromosphere',
            hovertemplate='Sun: Chromosphere<br>~2000 km thick<br>Temperature: 4,000-20,000 K<extra></extra>',
            showlegend=True
        ))
    
    if sun_shell_vars.get('photosphere') and sun_shell_vars['photosphere'].get() == 1:
        radius = SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=40)
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=1.5, color='rgba(255, 220, 100, 0.8)', opacity=0.8),
            name='Sun: Photosphere',
            hovertemplate='Sun: Photosphere<br>Visible surface<br>Temperature: ~5,800 K<extra></extra>',
            showlegend=True
        ))
    
    return fig

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
    
    # Initialize shell_type to avoid undefined variable errors
#    shell_type = ""

    # Create shell traces based on selected variables
    traces = []
    
    if body_name == 'Sun':
        # Handle Sun visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                # Call the appropriate shell creation function based on name
                if shell_name == 'core':
                    traces.extend(create_sun_core_shell())
                elif shell_name == 'radiative':
                    traces.extend(create_sun_radiative_shell())
                elif shell_name == 'photosphere':
                    traces.extend(create_sun_photosphere_shell())
                elif shell_name == 'chromosphere':
                    traces.extend(create_sun_chromosphere_shell())
                elif shell_name == 'inner_corona':
                    traces.extend(create_sun_inner_corona_shell())
                elif shell_name == 'outer_corona':
                    traces.extend(create_sun_outer_corona_shell())
                elif shell_name == 'termination_shock':
                    traces.extend(create_sun_termination_shock_shell())
                elif shell_name == 'heliopause':
                    traces.extend(create_sun_heliopause_shell())

                elif shell_name == 'inner_oort_limit':
                    traces.extend(create_sun_inner_oort_limit_shell())
                elif shell_name == 'inner_oort':
                    traces.extend(create_sun_inner_oort_shell())
                elif shell_name == 'outer_oort':
                    traces.extend(create_sun_outer_oort_shell())

                elif shell_name == 'hills_cloud_torus':
                    traces.extend(create_sun_hills_cloud_torus())
                elif shell_name == 'outer_oort_clumpy':
                    traces.extend(create_sun_outer_oort_clumpy())
                elif shell_name == 'galactic_tide':
                    traces.extend(create_sun_galactic_tide())
                elif shell_name == 'gravitational':
                    traces.extend(create_sun_gravitational_shell())
    
    elif body_name == 'Mercury':
        # Handle Mercury visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_type = shell_name.replace('mercury_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_mercury_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_mercury_outer_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_mercury_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_mercury_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_mercury_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_mercury_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_mercury_hill_sphere_shell(center_position))

    elif body_name == 'Venus':
        # Handle Venus visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('venus_', '')
                if shell_name == 'core':
                    traces.extend(create_venus_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_venus_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_venus_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_venus_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_venus_upper_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_venus_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_venus_hill_sphere_shell(center_position))

    elif body_name == 'Earth':
        # Handle Earth visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('earth_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_earth_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_earth_outer_core_shell(center_position))
                elif shell_name == 'lower_mantle':
                    traces.extend(create_earth_lower_mantle_shell(center_position))
                elif shell_name == 'upper_mantle':
                    traces.extend(create_earth_upper_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_earth_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_earth_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_earth_upper_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_earth_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_earth_hill_sphere_shell(center_position))
    
    elif body_name == 'Moon':
        # Handle moon visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('moon_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_moon_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_moon_outer_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_moon_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_moon_crust_shell(center_position))
                elif shell_name == 'exosphere':
                    traces.extend(create_moon_exosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_moon_hill_sphere_shell(center_position))

    elif body_name == 'Mars':
        # Handle Mars visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('mars_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_mars_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_mars_outer_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_mars_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_mars_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_mars_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_mars_upper_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_mars_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_mars_hill_sphere_shell(center_position))

    elif body_name == 'Jupiter':
        # Handle Jupiter visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('jupiter_', '')
                if shell_name == 'core':
                    traces.extend(create_jupiter_core_shell(center_position))
                elif shell_name == 'metallic_hydrogen':
                    traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
                elif shell_name == 'molecular_hydrogen':
                    traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_jupiter_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_jupiter_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_jupiter_radiation_belts(center_position))
                elif shell_name == 'io_plasma_torus':
                    traces.extend(create_jupiter_io_plasma_torus(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_jupiter_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_jupiter_hill_sphere_shell(center_position))

    elif body_name == 'Saturn':
        # Handle Saturn visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('saturn_', '')
                if shell_name == 'core':
                    traces.extend(create_saturn_core_shell(center_position))
                elif shell_name == 'metallic_hydrogen':
                    traces.extend(create_saturn_metallic_hydrogen_shell(center_position))
                elif shell_name == 'molecular_hydrogen':
                    traces.extend(create_saturn_molecular_hydrogen_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_saturn_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_saturn_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_saturn_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_saturn_radiation_belts(center_position))
                elif shell_name == 'enceladus_plasma_torus':
                    traces.extend(create_saturn_enceladus_plasma_torus(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_saturn_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_saturn_hill_sphere_shell(center_position))

    elif body_name == 'Uranus':
        # Handle uranus visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('uranus_', '')
                if shell_name == 'core':
                    traces.extend(create_uranus_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_uranus_mantle_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_uranus_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_uranus_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_uranus_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_uranus_radiation_belts(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_uranus_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_uranus_hill_sphere_shell(center_position))

    elif body_name == 'Neptune':
        # Handle Neptune visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('neptune_', '')
                if shell_name == 'core':
                    traces.extend(create_neptune_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_neptune_mantle_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_neptune_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_neptune_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_neptune_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_neptune_radiation_belts(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_neptune_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_neptune_hill_sphere_shell(center_position))

    elif body_name == 'Pluto':
        # Handle Pluto visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('pluto_', '')
                if shell_name == 'core':
                    traces.extend(create_pluto_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_pluto_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_pluto_crust_shell(center_position))
                elif shell_name == 'haze_layer':
                    traces.extend(create_pluto_haze_layer_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_pluto_atmosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_pluto_hill_sphere_shell(center_position))

    elif body_name == 'Eris':
        # Handle eris visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('eris_', '')
                if shell_name == 'core':
                    traces.extend(create_eris_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_eris_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_eris_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_eris_atmosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_eris_hill_sphere_shell(center_position))

    elif body_name == 'Planet 9':
        # Handle Planet 9 visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('planet9_', '')
                if shell_name == 'surface':
                    traces.extend(create_planet9_surface_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_planet9_hill_sphere_shell(center_position))

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

    if planet_name == 'Mercury':
        if shell_vars['mercury_inner_core'].get() == 1:
            traces.extend(create_mercury_inner_core_shell(center_position))
        if shell_vars['mercury_outer_core'].get() == 1:
            traces.extend(create_mercury_outer_core_shell(center_position))
        if shell_vars['mercury_mantle'].get() == 1:
            traces.extend(create_mercury_mantle_shell(center_position))
        if shell_vars['mercury_crust'].get() == 1:
            traces.extend(create_mercury_crust_shell(center_position))
        if shell_vars['mercury_atmosphere'].get() == 1:
            traces.extend(create_mercury_atmosphere_shell(center_position))
        if shell_vars['mercury_sodium_tail'].get() == 1:  
            traces.extend(create_mercury_sodium_tail(center_position))
        if shell_vars['mercury_magnetosphere'].get() == 1:
            traces.extend(create_mercury_magnetosphere_shell(center_position))
        if shell_vars['mercury_hill_sphere'].get() == 1:
            traces.extend(create_mercury_hill_sphere_shell(center_position))

    if planet_name == 'Venus':
        if shell_vars['venus_core'].get() == 1:
            traces.extend(create_venus_core_shell(center_position))
        if shell_vars['venus_mantle'].get() == 1:
            traces.extend(create_venus_mantle_shell(center_position))
        if shell_vars['venus_crust'].get() == 1:
            traces.extend(create_venus_crust_shell(center_position))
        if shell_vars['venus_atmosphere'].get() == 1:
            traces.extend(create_venus_atmosphere_shell(center_position))
        if shell_vars['venus_upper_atmosphere'].get() == 1:
            traces.extend(create_venus_upper_atmosphere_shell(center_position))
        if shell_vars['venus_magnetosphere'].get() == 1:
            traces.extend(create_venus_magnetosphere_shell(center_position))
        if shell_vars['venus_hill_sphere'].get() == 1:
            traces.extend(create_venus_hill_sphere_shell(center_position))

    if planet_name == 'Earth':
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

    if planet_name == 'Moon':
        if shell_vars['moon_inner_core'].get() == 1:
            traces.extend(create_moon_inner_core_shell(center_position))
        if shell_vars['moon_outer_core'].get() == 1:
            traces.extend(create_moon_outer_core_shell(center_position))
        if shell_vars['moon_mantle'].get() == 1:
            traces.extend(create_moon_mantle_shell(center_position))
        if shell_vars['moon_crust'].get() == 1:
            traces.extend(create_moon_crust_shell(center_position))
        if shell_vars['moon_exosphere'].get() == 1:
            traces.extend(create_moon_exosphere_shell(center_position))
        if shell_vars['moon_hill_sphere'].get() == 1:
            traces.extend(create_moon_hill_sphere_shell(center_position))

    if planet_name == 'Mars':
        if shell_vars['mars_inner_core'].get() == 1:
            traces.extend(create_mars_inner_core_shell(center_position))
        if shell_vars['mars_outer_core'].get() == 1:
            traces.extend(create_mars_outer_core_shell(center_position))
        if shell_vars['mars_mantle'].get() == 1:
            traces.extend(create_mars_mantle_shell(center_position))
        if shell_vars['mars_crust'].get() == 1:
            traces.extend(create_mars_crust_shell(center_position))
        if shell_vars['mars_atmosphere'].get() == 1:
            traces.extend(create_mars_atmosphere_shell(center_position))
        if shell_vars['mars_upper_atmosphere'].get() == 1:
            traces.extend(create_mars_upper_atmosphere_shell(center_position))
        if shell_vars['mars_magnetosphere'].get() == 1:
            traces.extend(create_mars_magnetosphere_shell(center_position))
        if shell_vars['mars_hill_sphere'].get() == 1:
            traces.extend(create_mars_hill_sphere_shell(center_position))

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
        if shell_vars['jupiter_radiation_belts'].get() == 1:
            traces.extend(create_jupiter_radiation_belts(center_position))
        if shell_vars['jupiter_io_plasma_torus'].get() == 1:
            traces.extend(create_jupiter_io_plasma_torus(center_position))
        if shell_vars['jupiter_magnetosphere'].get() == 1:
            traces.extend(create_jupiter_magnetosphere(center_position))
        if shell_vars['jupiter_hill_sphere'].get() == 1:
            traces.extend(create_jupiter_hill_sphere_shell(center_position))

    if planet_name == 'Saturn':
        if shell_vars['saturn_core'].get() == 1:
            traces.extend(create_saturn_core_shell(center_position))
        if shell_vars['saturn_metallic_hydrogen'].get() == 1:
            traces.extend(create_saturn_metallic_hydrogen_shell(center_position))
        if shell_vars['saturn_molecular_hydrogen'].get() == 1:
            traces.extend(create_saturn_molecular_hydrogen_shell(center_position))
        if shell_vars['saturn_cloud_layer'].get() == 1:
            traces.extend(create_saturn_cloud_layer_shell(center_position))
        if shell_vars['saturn_upper_atmosphere'].get() == 1:
            traces.extend(create_saturn_upper_atmosphere_shell(center_position))
        if shell_vars['saturn_ring_system'].get() == 1:
            traces.extend(create_saturn_ring_system(center_position))
        if shell_vars['saturn_radiation_belts'].get() == 1:
            traces.extend(create_saturn_radiation_belts(center_position))
        if shell_vars['saturn_enceladus_plasma_torus'].get() == 1:
            traces.extend(create_saturn_enceladus_plasma_torus(center_position))
        if shell_vars['saturn_magnetosphere'].get() == 1:
            traces.extend(create_saturn_magnetosphere(center_position))
        if shell_vars['saturn_hill_sphere'].get() == 1:
            traces.extend(create_saturn_hill_sphere_shell(center_position))

    if planet_name == 'Uranus':
        if shell_vars['uranus_core'].get() == 1:
            traces.extend(create_uranus_core_shell(center_position))
        if shell_vars['uranus_mantle'].get() == 1:
            traces.extend(create_uranus_mantle_shell(center_position))
        if shell_vars['uranus_cloud_layer'].get() == 1:
            traces.extend(create_uranus_cloud_layer_shell(center_position))
        if shell_vars['uranus_upper_atmosphere'].get() == 1:
            traces.extend(create_uranus_upper_atmosphere_shell(center_position))
        if shell_vars['uranus_ring_system'].get() == 1:
            traces.extend(create_uranus_ring_system(center_position))
        if shell_vars['uranus_radiation_belts'].get() == 1:
            traces.extend(create_uranus_radiation_belts(center_position))
        if shell_vars['uranus_magnetosphere'].get() == 1:
            traces.extend(create_uranus_magnetosphere(center_position))
        if shell_vars['uranus_hill_sphere'].get() == 1:
            traces.extend(create_uranus_hill_sphere_shell(center_position))

    if planet_name == 'Neptune':
        if shell_vars['neptune_core'].get() == 1:
            traces.extend(create_neptune_core_shell(center_position))
        if shell_vars['neptune_mantle'].get() == 1:
            traces.extend(create_neptune_mantle_shell(center_position))
        if shell_vars['neptune_cloud_layer'].get() == 1:
            traces.extend(create_neptune_cloud_layer_shell(center_position))
        if shell_vars['neptune_upper_atmosphere'].get() == 1:
            traces.extend(create_neptune_upper_atmosphere_shell(center_position))
        if shell_vars['neptune_ring_system'].get() == 1:
            traces.extend(create_neptune_ring_system(center_position))
        if shell_vars['neptune_radiation_belts'].get() == 1:
            traces.extend(create_neptune_radiation_belts(center_position))
        if shell_vars['neptune_magnetosphere'].get() == 1:
            traces.extend(create_neptune_magnetosphere(center_position))
        if shell_vars['neptune_hill_sphere'].get() == 1:
            traces.extend(create_neptune_hill_sphere_shell(center_position))

    if planet_name == 'Pluto':
        if shell_vars['pluto_core'].get() == 1:
            traces.extend(create_pluto_core_shell(center_position))
        if shell_vars['pluto_mantle'].get() == 1:
            traces.extend(create_pluto_mantle_shell(center_position))
        if shell_vars['pluto_crust'].get() == 1:
            traces.extend(create_pluto_crust_shell(center_position))
        if shell_vars['pluto_haze_layer'].get() == 1:
            traces.extend(create_pluto_haze_layer_shell(center_position))
        if shell_vars['pluto_atmosphere'].get() == 1:
            traces.extend(create_pluto_atmosphere_shell(center_position))
        if shell_vars['pluto_hill_sphere'].get() == 1:
            traces.extend(create_pluto_hill_sphere_shell(center_position))

    if planet_name == 'Eris':
        if shell_vars['eris_core'].get() == 1:
            traces.extend(create_eris_core_shell(center_position))
        if shell_vars['eris_mantle'].get() == 1:
            traces.extend(create_eris_mantle_shell(center_position))
        if shell_vars['eris_crust'].get() == 1:
            traces.extend(create_eris_crust_shell(center_position))
        if shell_vars['eris_atmosphere'].get() == 1:
            traces.extend(create_eris_atmosphere_shell(center_position))
        if shell_vars['eris_hill_sphere'].get() == 1:
            traces.extend(create_eris_hill_sphere_shell(center_position))

    if planet_name == 'Planet 9':
        if shell_vars['planet9_surface'].get() == 1:
            traces.extend(create_planet9_surface_shell(center_position))
        if shell_vars['planet9_hill_sphere'].get() == 1:
            traces.extend(create_planet9_hill_sphere_shell(center_position))
    
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
                trace.customdata = [str(item).replace("Mercury", planet_name).replace("Venus", planet_name).replace("Earth", planet_name).replace("Moon", planet_name)
                                    .replace("Mars", planet_name).replace("Jupiter", planet_name).replace("Saturn", planet_name)
                                    .replace("Uranus", planet_name).replace("Neptune", planet_name).replace("Pluto", planet_name)
                                    .replace("Eris", planet_name).replace("Planet 9", planet_name)
                            if "Mercury" in str(item) or "Venus" in str(item) or "Earth" in str(item) or "Moon" in str(item) or "Mars" in str(item)
                                or "Jupiter" in str(item) or "Saturn" in str(item) or "Uranus" in str(item) or "Neptune" in str(item)
                                or "Pluto" in str(item) or "Eris" in str(item) or "Planet 9" in str(item)
                            else str(item) for item in trace.customdata]
        
        # Set correct hovertemplate
        trace.hovertemplate = '%{text}<extra></extra>'
    
    return traces


