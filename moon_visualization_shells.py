"""
moon_visualization_shells.py - Lunar interior and exosphere shell traces.

Sphere shells for the Moon: inner core, outer core, mantle, crust,
tenuous exosphere, and Hill sphere. All sphere-only -- no custom geometry.
Candidate for full migration to shell_configs.py (no custom functions needed).

Consumed by: planet_visualization.py (routing dispatcher)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
April 18, 2026: provenance audit source citations added, Gemini fact-check applied.
All 5 flagged claims confirmed (Weber et al. 2011, NASA Moon Fact Sheet, Apollo
Seismic Experiment reports, NASA SSD, Draper 1847). No factual corrections needed.
Provenance audit identified by Anthropic's Claude Opus 4.7.
May 27, 2026: Stage 3 info-marker standard sweep (Opus 4.7). 5 info
    markers brought to red-border standard; 1 red-on-red exception
    preserved on outer_core (rgb(255, 50, 0) charcoal/ember red).
May 28, 2026: Phase 1 re-pipe (Opus 4.7). 1 live inline info marker
    routed through orrery_rendering.create_info_marker() factory
    (Hill Sphere). Already at factory size 8 / opacity 1.0; no visual
    change beyond factory routing. Moon outer_core dense-red case is
    handled via SHELL_CONFIGS info_border='white' override (Tony's
    two-standards: shell-color fill, white outline for reddish shells).
"""
import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (MOON_RADIUS_AU, create_sphere_points, create_magnetosphere_shape)
from shared_utilities import create_sun_direction_indicator
from orrery_rendering import create_info_marker

# Moon Shell Creation Functions

# Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
#         inner core ~240 km radius, 1,600-1,700 K, refined from Apollo seismic data.
moon_inner_core_info = (
            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\'s wobble suggest:<br>" 
            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."
)

def create_moon_inner_core_shell(center_position=(0, 0, 0)):
    """Creates the Moon's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.1485,  
        'color': 'rgb(255, 100, 0)',  # dark red-orange at 1700K
        'opacity': 1.0,
        'name': 'Inner Core',
        # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
        #         solid iron-rich inner core ~240 km radius, 1,600-1,700 K confirmed.
        'description': (
            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\'s wobble suggest:<br>" 
            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>" 
            "  * Estimates for the temperature of the Moon\'s inner core vary slightly depending on the studies and methods used, but <br>" 
            "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K." 
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Moon: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=4.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

moon_outer_core_info = (
            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>" 
            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."
)

def create_moon_outer_core_shell(center_position=(0, 0, 0)):
    """Creates the Moon's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.2083,  
        'color': 'rgb(255, 50, 0)',  # very dark, deep red, almost a "charcoal red" or "ember red"
        'opacity': 0.8,
        'name': 'Outer Core',
        # Source: NASA Moon Fact Sheet; Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
        #         outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick confirmed.
        'description': (
            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>" 
            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:" 
            "* The Moon's outer core is generally understood to be hotter than its solid inner core, as it is in a molten or liquid <br>" 
            "  state. <br>" 
            "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>" 
            "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let's use 1500 K as a representative <br>" 
            "  value for the outer core for your model.<br>" 
            "* Reasoning: As you move outwards, the temperature gradually decreases, but crucially, the pressure also decreases. At this <br>" 
            "  depth and pressure, the temperature is above the melting point of the iron-rich material, allowing it to be liquid."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Moon: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.7,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # NOTE: red-on-red exception (outer_core = rgb(255, 50, 0), charcoal
    # red). The hard problem: a marker the SAME color as its dense red dot
    # field is invisible, and Plotly ignores marker line WIDTH in 3D
    # (plotly.js #4118) so a border cannot be thickened to compensate.
    # FILL color, SIZE, and SYMBOL all DO render reliably -- so the fix
    # is contrast via fill, not border. EXPERIMENT v2 (May 27, 2026):
    # double marker with WHITE FILL. A size-16 white open square gives a
    # bounding silhouette; a size-8 white cross on top carries the hover.
    # White-on-red reads regardless of the border-width bug. The markers
    # intentionally do NOT match the shell color -- an info marker's job
    # is findability, not color-matching.
    # If Mode 5 rejects this, revert to single cross: drop info_ring and
    # append [shell_trace, info_trace].
    info_ring = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=16, color='white', opacity=1.0,
                    symbol='square-open', line=dict(color='white', width=2)),
        name='',
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=False
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color='white', opacity=1.0,  # exception: white fill
                    symbol='cross', line=dict(color='white', width=2)),

    #    marker=dict(size=8, color=layer_info['color'], opacity=1.0,
    #                symbol='cross', line=dict(color='white', width=2)),

        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_ring, info_trace]
    
    return traces

# Source: NASA Moon Fact Sheet; Apollo Seismic Experiment reports (deep moonquakes 700-1,200 km,
#         tidal stress origin confirmed).
moon_mantle_info = (
            "Above the core lies the Moon's mantle, which makes up the bulk of its interior:<br>" 
            "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of <br>" 
            "  elements. It's thought to be rich in olivine and pyroxene.<br>" 
            "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially <br>" 
            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>" 
            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at <br>" 
            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."
)

def create_moon_mantle_shell(center_position=(0, 0, 0)):
    """Creates the Moon's lower mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Lower mantle: 55-85% of Earth's radius
        'color': 'rgb(0, 50, 0)',  # very dark green for peridotite
        'opacity': 0.9655,
        'name': 'Mantle',
        # Source: NASA Moon Fact Sheet; Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
        #         Apollo Seismic Experiment reports (deep moonquakes, tidal stress);
        #         Draper (1847) for Draper point 798 K.
        'description': (
            "Above the core lies the Moon's mantle, which makes up the bulk of its interior:<br>" 
            "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of <br>" 
            "  elements. It's thought to be rich in olivine and pyroxene.<br>" 
            "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially <br>" 
            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>" 
            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at <br>" 
            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth.<br>" 
            "* The Moon's mantle is a thick, largely solid layer, and its temperature varies significantly with depth, becoming <br>" 
            "  cooler as you move outwards towards the crust.<br>" 
            "  * Estimates for the temperature at the boundary between the mantle and the outer core range from 1573 K to 1743 K.<br>" 
            "  * Estimates for the crust-mantle boundary are roughly 623 K to 823 K.<br>" 
            "* The \"Draper point\" is around 798 K, which is the approximate temperature at which all solids start to glow a dim <br>" 
            "  red. Therefore, the upper mantle, at these temperatures, would not visibly glow from black body radiation in normal <br>" 
            "  conditions. Its primary emission would be in the infrared spectrum, invisible to the human eye. For the bulk of the <br>" 
            "  mantle, it is primarily composed of silicate rocks like olivine and pyroxene. When seen in rock samples, these tend <br>" 
            "  to be dark greenish to black (e.g., peridotite).<br>" 
            "* Outer boundary of the mantle (base of the crust) as a fraction of Rm: 1677.4 km/1737.4 km~0.9655"
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Moon: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.4,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

moon_crust_info = (
            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:<br>" 
            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the <br>" 
            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that <br>" 
            "  filled large impact basins.<br>" 
            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 <br>" 
            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This <br>" 
            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon's crustal thickness <br>" 
            "  asymmetry point to a combination of factors related to its formation in Earth\'s intense thermal environment and a <br>" 
            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.<br>" 
            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other <br>" 
            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges."
)

def create_moon_crust_shell(center_position=(0, 0, 0)):
    """Creates Earth's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  
        'color': 'rgb(190, 190, 180)',  # slightly warm grey
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:<br>" 
            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the <br>" 
            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that <br>" 
            "  filled large impact basins.<br>" 
            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 <br>" 
            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This <br>" 
            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon's crustal thickness <br>" 
            "  asymmetry point to a combination of factors related to its formation in Earth\'s intense thermal environment and a <br>" 
            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.<br>" 
            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other <br>" 
            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges.<br>" 
            "* Given the mix of lighter highlands and darker maria, and the overall neutral tone, a medium, slightly warm grey.<br>" 
            "* Unlike Earth, the Moon does not have a global, internally generated magnetic field today. However, rocks collected <br>" 
            "  during the Apollo missions showed evidence of remnant magnetism, indicating that the Moon did possess a global <br>" 
            "  magnetic field in its early history, likely generated by a liquid core dynamo similar to Earth's. Today, there are <br>" 
            "  localized magnetic anomalies on the lunar surface, thought to be remnants of this ancient magnetic field or perhaps <br>" 
            "  due to impact processes. These regions can sometimes interact with the solar wind, creating small <br>" 
            "  \"mini-magnetospheres.\".<br>" 
            "* Solar Wind Interaction: Without a global magnetic field, the Moon is directly exposed to the solar wind, a stream of <br>" 
            "  charged particles from the Sun. This constant bombardment contributes to space weathering of the lunar surface.<br>" 
            "* Water Ice: One of the most significant discoveries in recent lunar exploration is the confirmed presence of water ice, <br>" 
            "  particularly in permanently shadowed regions within craters at the Moon\'s poles.<br>" 
            "* Regolith: The entire lunar surface is covered by a layer of fine, powdery dust and broken rock fragments called regolith. <br>" 
            "  It\'s formed by billions of years of micrometeoroid impacts and varies in thickness from a few meters in the maria to tens <br>" 
            "  of meters in the highlands.<br>" 
            "* Tidally Locked: The Moon is tidally locked with Earth, meaning the same side of the Moon (the \"near side\") always faces <br>" 
            "  Earth."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create mesh with reasonable resolution for performance
    resolution = 24  # Reduced from typical 50 for markers
    
    # Create a UV sphere
    phi = np.linspace(0, 2*np.pi, resolution)
    theta = np.linspace(-np.pi/2, np.pi/2, resolution)
    phi, theta = np.meshgrid(phi, theta)
    
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    # Apply center position offset
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create triangulation
    indices = []
    for i in range(resolution-1):
        for j in range(resolution-1):
            p1 = i * resolution + j
            p2 = i * resolution + (j + 1)
            p3 = (i + 1) * resolution + j
            p4 = (i + 1) * resolution + (j + 1)
            
            indices.append([p1, p2, p4])
            indices.append([p1, p4, p3])
    
    # Create main surface
    surface_trace = go.Mesh3d(
        x=x.flatten(), 
        y=y.flatten(), 
        z=z.flatten(),
        i=[idx[0] for idx in indices],
        j=[idx[1] for idx in indices],
        k=[idx[2] for idx in indices],
        color=layer_info['color'],
        opacity=layer_info['opacity'],
        name=f"Moon: {layer_info['name']}",
        legendgroup=f"Moon: {layer_info['name']}",
        showlegend=True,
        hoverinfo='none',  # Disable hover on mesh surface
        # Add these new parameters to make hover text invisible
        hovertemplate=' ',  # Empty template instead of None
        hoverlabel=dict(
    #        bgcolor='rgba(0,0,0,0)',  # Transparent background
            font=dict(
                color='rgba(0,0,0,0)',  # Transparent text
    #            size=0                  # Zero font size
            ),
            bordercolor='rgba(0,0,0,0)'  # Transparent border
        ), 
        # Add these new parameters to eliminate shading
        flatshading=True,  # Use flat shading instead of smooth
        lighting=dict(
            ambient=1.0,     # Set to maximum (1.0)
            diffuse=0.0,     # Turn off diffuse lighting
            specular=0.0,    # Turn off specular highlights
            roughness=1.0,   # Maximum roughness
            fresnel=0.0      # Turn off fresnel effect
        ),
        lightposition=dict(
            x=0,  # Centered light
            y=0,  # Centered light
            z=10000  # Light from very far above to minimize shadows
        )       
    )
        
    # Use the Fibonacci sphere algorithm for more even point distribution
    def fibonacci_sphere(samples=1000):
        points = []
        phi = math.pi * (3. - math.sqrt(5.))  # Golden angle in radians
        
        for i in range(samples):
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius_at_y = math.sqrt(1 - y * y)  # Radius at y
            
            theta = phi * i  # Golden angle increment
            
            x = math.cos(theta) * radius_at_y
            z = math.sin(theta) * radius_at_y
            
            points.append((x, y, z))
        
        return points
    
    # Generate fibonacci sphere points
    fib_points = fibonacci_sphere(samples=50)  # Originally, 50 hover points evenly distributed
    
    # Scale and offset the points
    x_hover = [p[0] * radius + center_x for p in fib_points]
    y_hover = [p[1] * radius + center_y for p in fib_points]
    z_hover = [p[2] * radius + center_z for p in fib_points]
        
    # Create a list of repeated descriptions for each point
    # This is crucial - we need exactly one text entry per point

    # Just the name for "Object Names Only" mode

    # Create hover trace with direct text assignment
    # Single info marker at north pole, 5% above radius
    r_info = radius * 1.05
    trace_name = f"Moon: {layer_info['name']}"

    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name=trace_name,
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[f"Moon: {layer_info['name']}"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    return [surface_trace, hover_trace]

moon_exosphere_info = (
            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly <br>" 
            "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with <br>" 
            "each other.<br>" 
            "* Sources: The exosphere is formed from gases released from the Moon\'s interior from radioactive decay, outgassing <br>" 
            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.<br>" 
            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>" 
            "  hydrogen, and other elements.<br>" 
            "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant <br>" 
            "  shielding from solar radiation or micrometeoroids."
)

def create_moon_exosphere_shell(center_position=(0, 0, 0)):
    """Creates the Moon's exosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.06, 
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Exosphere',
        'description': (
            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly <br>" 
            "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with <br>" 
            "each other.<br>" 
            "* Sources: The exosphere is formed from gases released from the Moon\'s interior from radioactive decay, outgassing <br>" 
            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.<br>" 
            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>" 
            "  hydrogen, and other elements.<br>" 
            "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant <br>" 
            "  shielding from solar radiation or micrometeoroids.<br>"  
            "* Practical or \"Dense\" Extent: For most practical purposes, where collisions between particles are still somewhat <br>" 
            "  relevant or where density is higher, the exosphere is often considered to extend up to about 100 kilometers above <br>" 
            "  the lunar surface. So, a more \"dense\" part of the exosphere extends from 1.0 Rm to roughly 1.06 Rm."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Moon: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: NASA Solar System Dynamics (SSD); Hill sphere radius ~60,000 km confirmed,
#         34.53 lunar radii derived from Moon mean radius 1,737.4 km.
moon_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.<br><br>" 
            "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity <br>" 
            "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an <br>" 
            "object is outside the Moon\'s Hill sphere, it would typically end up orbiting Earth instead of the Moon.<br>" 
            "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii." 
            )

def create_moon_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates the Moon's Hill sphere."""
    # Hill sphere radius in Moonn radii
    radius_fraction = 34.53  
    
    # Calculate radius in AU
    radius_au = radius_fraction * MOON_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 20  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = (
            "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity <br>" 
            "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an <br>" 
            "object is outside the Moon\'s Hill sphere, it would typically end up orbiting Earth instead of the Moon.<br>" 
            "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii." 
                )
    
    # Create the trace
    r_info = radius_au * 1.05
    trace_name = 'Moon: Hill Sphere'

    shell_trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=1.0,
            color='rgb(0, 255, 0)',  # Green for Hill sphere
            opacity=0.25
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    info_trace = create_info_marker(
        center_x, center_y, center_z + r_info,
        'rgb(0, 255, 0)',
        f"{trace_name}<br><br>{hover_text}",
        trace_name
    )

    traces = [shell_trace, info_trace]
    
    return traces

