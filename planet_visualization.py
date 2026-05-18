"""
planet_visualization.py - High-level planet and Sun visualization orchestration.

Builds layered visualizations of solar system bodies (Sun, planets) for 3D
plots by assembling shell traces from the per-body *_visualization_shells.py
modules. Exposes the create_* functions called by palomas_orrery.py, plus
the info-text strings that populate hover tooltips for each shell.

Key functions:
    create_celestial_body_visualization(fig, body, shell_vars) - dispatch entry
    create_sun_visualization(fig, sun_shell_vars, animate, frames) - Sun shells
    create_planet_visualization(fig, planet, shell_vars) - planet shell assembly
    create_planet_shell_traces(planet, shell_vars) - return traces without adding

Consumed by: palomas_orrery.py, palomas_orrery_helpers.py

Part of Paloma's Orrery - Data Preservation is Climate Action

Module updated: May 2026 with Anthropic's Claude Opus 4.7
(provenance audit; body-radius aliases and solar/system constants now
imported from planet_visualization_utilities.py rather than redefined locally.
Removed shadow redefinition of KM_PER_AU.)
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS, CENTER_BODY_RADII)

# Shell consolidation imports (Step 3, Phase A)
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from shared_utilities import create_sun_direction_indicator
import importlib

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

from planet_visualization_utilities import (
    # Solar structure and atmosphere
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    # Heliosphere and beyond
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
    # Body-radius aliases (km and AU)
    MERCURY_RADIUS_KM, MERCURY_RADIUS_AU,
    VENUS_RADIUS_KM, VENUS_RADIUS_AU,
    EARTH_RADIUS_KM, EARTH_RADIUS_AU,
    MOON_RADIUS_KM, MOON_RADIUS_AU,
    MARS_RADIUS_KM, MARS_RADIUS_AU,
    JUPITER_RADIUS_KM, JUPITER_RADIUS_AU,
    SATURN_RADIUS_KM, SATURN_RADIUS_AU,
    URANUS_RADIUS_KM, URANUS_RADIUS_AU,
    NEPTUNE_RADIUS_KM, NEPTUNE_RADIUS_AU,
    PLUTO_RADIUS_KM, PLUTO_RADIUS_AU,
    ERIS_RADIUS_KM, ERIS_RADIUS_AU,
    PLANET9_RADIUS_KM, PLANET9_RADIUS_AU,
)

from solar_visualization_shells import (create_sun_core_shell,
                                        create_sun_radiative_shell,
                                        create_sun_photosphere_shell,
                                        create_sun_chromosphere_shell,
                                        create_sun_inner_corona_shell,
                                        create_sun_streamer_belt_shell,
                                        create_sun_roche_limit_shell,
                                        create_sun_alfven_surface_shell,                                        
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

from mercury_visualization_shells import (mercury_inner_core_info, 
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
                                        create_earth_geostationary_belt_shell,
                                        create_earth_leo_shell,
                                        earth_inner_core_info, 
                                        earth_outer_core_info,
                                        earth_lower_mantle_info, 
                                        earth_upper_mantle_info,
                                        earth_crust_info, 
                                        earth_atmosphere_info, 
                                        earth_upper_atmosphere_info,                                           
                                        earth_magnetosphere_info, 
                                        earth_hill_sphere_info,
                                        earth_geostationary_belt_info,
                                        earth_leo_shell_info)

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


# Celestial body constants (solar structure, body radii, KM_PER_AU) are
# all imported from planet_visualization_utilities.py at the top of this
# file. Do not redefine them here. Single source of truth: constants_new.py.
# See protocol v3.20.

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
            
        if sun_shell_vars.get('roche_limit') and sun_shell_vars['roche_limit'].get() == 1:
            traces.extend(create_sun_roche_limit_shell())

        if sun_shell_vars.get('streamer_belt') and sun_shell_vars['streamer_belt'].get() == 1:
            traces.extend(create_sun_streamer_belt_shell())

        if sun_shell_vars.get('alfven_surface') and sun_shell_vars['alfven_surface'].get() == 1:
            traces.extend(create_sun_alfven_surface_shell())

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
    
    if sun_shell_vars.get('roche_limit') and sun_shell_vars['roche_limit'].get() == 1:
        radius = ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=0.85, color='rgba(200, 60, 60, 0.3)', opacity=0.3),
            name='Sun: Roche Limit (Comets)',
            hovertemplate='Sun: Roche Limit (Comets)<br>~3.45 solar radii<br>Tidal disruption threshold<extra></extra>',
            showlegend=True
        ))

    if sun_shell_vars.get('streamer_belt') and sun_shell_vars['streamer_belt'].get() == 1:
        radius = STREAMER_BELT_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=0.75, color='rgba(255, 200, 80, 0.25)', opacity=0.25),
            name='Sun: Streamer Belt (Visible Corona)',
            hovertemplate='Sun: Streamer Belt<br>~6 solar radii<br>Eclipse white-light corona<extra></extra>',
            showlegend=True
        ))

    if sun_shell_vars.get('alfven_surface') and sun_shell_vars['alfven_surface'].get() == 1:
        radius = ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU
        x, y, z = create_offset_sphere(radius, n_points=30)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=0.7, color='rgba(0, 200, 200, 0.2)', opacity=0.2),
            name='Sun: Alfven Surface',
            hovertemplate='Sun: Alfven Surface<br>~18.8 solar radii<br>True corona/solar wind boundary<extra></extra>',
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

def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,
                                        center_position=(0, 0, 0),
                                        object_type=None, center_object=None):
    """
    Unified config-driven dispatch for celestial body shell visualization.

    Looks up the body's shell configs in SHELL_CONFIGS (sphere shells) and
    CUSTOM_SHELLS (non-sphere geometry). Sphere shells route through
    build_sphere_shell(); custom shells are lazy-imported by registry entry.

    Issues ONE sun direction indicator per body at the outermost active
    shell radius, replacing the per-shell indicator calls that were
    duplicated across every shell function. The indicator is suppressed
    when the body is at the origin (body-centered view) because there
    is no meaningful sunward direction from the coordinate center.

    Step 3 Phase A: only Mercury is fully wired through this function. Other
    bodies continue to render via create_planet_visualization() blocks until
    their Phase B/C/D migrations land.

    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add traces to
        body_name (str): Body name as it appears in SHELL_CONFIGS keys
                         (e.g. 'Mercury', 'Pluto', 'Sun')
        shell_vars (dict): Maps shell var names to tk.IntVar.
                           Keys may be prefixed ('mercury_inner_core') or
                           bare ('inner_core') - prefix is stripped to match
                           config keys.
        animate (bool): Reserved for future animation hooks (unused in Phase A)
        frames (list): Reserved for future animation hooks (unused in Phase A)
        center_position (tuple): (x, y, z) AU position of the body's center
        object_type (str): Object type for sun direction indicator suppression
        center_object (str): Name of object at plot center (indicator suppression)

    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    # Strip body prefix from shell_vars keys to match config keys.
    # 'mercury_inner_core' -> 'inner_core'; bare keys (Sun) pass through.
    # 'Planet 9' becomes 'planet9_'.
    body_prefix = body_name.lower().replace(' ', '') + '_'

    outermost_radius_au = 0.0

    for key, var in shell_vars.items():
        try:
            if var.get() != 1:
                continue
        except (AttributeError, TypeError):
            # var is not a tk.IntVar (e.g., plain int from tests)
            if not var:
                continue

        shell_name = key[len(body_prefix):] if key.startswith(body_prefix) else key

        if shell_name in configs:
            config = configs[shell_name]
            traces = build_sphere_shell(config, body_name, center_position)
            for t in traces:
                fig.add_trace(t)
            # Track outermost radius for indicator scaling
            if 'radius_au' in config:
                shell_r = config['radius_au']
            else:
                body_r = CENTER_BODY_RADII[body_name] / KM_PER_AU
                shell_r = config['radius_fraction'] * body_r
            outermost_radius_au = max(outermost_radius_au, shell_r)

        elif shell_name in customs:
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            traces = builder(center_position)
            for t in traces:
                fig.add_trace(t)

        # If shell_name is in neither registry, silently skip.
        # In Phase A this is expected for bodies that haven't migrated yet
        # (their dispatch is still in create_planet_visualization).

    # ONE sun direction indicator per body (replaces ~50 per-shell calls).
    # Uses outermost active shell radius for scaling. Suppresses at origin
    # (body-centered view) and for Sun shells.
    if outermost_radius_au > 0:
        indicator_traces = create_sun_direction_indicator(
            center_position=center_position,
            shell_radius=outermost_radius_au,
            object_type=object_type if object_type is not None else body_name,
            center_object=center_object,
        )
        for t in indicator_traces:
            fig.add_trace(t)

    # Store outermost shell radius for axis auto-scaling.
    # Consumed by palomas_orrery.py to set axis_range = [-2*r, 2*r]
    # when Auto scaling is active. Bodies that haven't migrated to the
    # unified dispatch don't set this attribute -- old behavior continues.
    if outermost_radius_au > 0:
        fig._shell_outermost_radius_au = outermost_radius_au

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
        # Step 3 Phase A: delegate to unified config-driven dispatch.
        # See create_celestial_body_visualization() for the new architecture.
        # NOTE: center_object hardcoded to body_name here because
        # create_planet_visualization does not receive the plot's center body.
        # This becomes correct in Phase D when callers use the unified function
        # directly with center_object=center_object_name.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Mercury',
            center_object='Mercury',
        )

    if planet_name == 'Venus':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: venus_magnetosphere -> CUSTOM_SHELLS['Venus']['magnetosphere']
        # which lazy-imports and emits both magnetosphere and bow shock traces.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Venus',
            center_object='Venus',
        )

    if planet_name == 'Earth':
        # Step 3 Phase C2: delegate to unified config-driven dispatch.
        # Custom geometry: earth_magnetosphere -> CUSTOM_SHELLS['Earth']['magnetosphere']
        # which lazy-imports and emits magnetosphere + bow shock + 2 Van Allen belt traces.
        # earth_leo and earth_geostationary_belt also lazy-imported via CUSTOM_SHELLS.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Earth',
            center_object='Earth',
        )

    if planet_name == 'Moon':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A). NOTE: center_object hardcoded
        # to body_name here because create_planet_visualization does not
        # receive the plot's center body. Corrected in Phase D when callers
        # use the unified function directly.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Moon',
            center_object='Moon',
        )

    if planet_name == 'Mars':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: mars_magnetosphere -> CUSTOM_SHELLS['Mars']['magnetosphere']
        # which lazy-imports and emits magnetosphere, bow shock, and crustal fields.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Mars',
            center_object='Mars',
        )

    if planet_name == 'Jupiter':
        # Step 3 Phase C3: delegate to unified config-driven dispatch.
        # Custom geometry: jupiter_magnetosphere, jupiter_io_plasma_torus,
        # jupiter_radiation_belts (3 belts), jupiter_ring_system (4 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Jupiter',
            center_object='Jupiter',
        )

    if planet_name == 'Saturn':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Custom geometry: saturn_magnetosphere, saturn_enceladus_plasma_torus,
        # saturn_radiation_belts (6 belts), saturn_ring_system (7 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Saturn',
            center_object='Saturn',
        )

    if planet_name == 'Uranus':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Uranus',
            center_object='Uranus',
        )

    if planet_name == 'Neptune':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn / Uranus (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Neptune',
            center_object='Neptune',
        )

    if planet_name == 'Pluto':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Pluto',
            center_object='Pluto',
        )

    if planet_name == 'Eris':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Eris',
            center_object='Eris',
        )

    if planet_name == 'Planet 9':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A) and Moon (Phase B above).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Planet 9',
            center_object='Planet 9',
        )
    
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


