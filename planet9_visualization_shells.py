"""
planet9_visualization_shells.py - Hypothetical Planet 9 shell traces.

Sphere shells for Planet 9: estimated surface and Hill sphere only.
Based on Batygin & Brown (2016) orbital predictions. All sphere-only --
fully archivable once shell_configs.py migration is complete.

Consumed by: planet_visualization.py (routing dispatcher)

Module updated: April 2026 with Anthropic's Claude Opus 4.6
April 18, 2026: provenance audit source citations added, Gemini fact-check applied.
Two corrections: (1) "Eris's orbit" typo fixed to "Planet Nine's orbit"; (2) semi-major axis
note updated to reflect 2021 refinement (~460 AU central estimate). Radius and Hill sphere
parameters confirmed per Batygin & Brown (2016, 2021) and Fortney et al. (2016).
Provenance audit identified by Anthropic's Claude Opus 4.7.
"""
import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (PLANET9_RADIUS_AU, create_sphere_points)
from shared_utilities import create_sun_direction_indicator

# Planet 9

# Source: Batygin & Brown (2016, 2021); Fortney et al. (2016);
#         radius 3-4 Earth radii (~3.7 R_E) from thermal evolution models for 5-10 Earth mass ice giant.
#         Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.
planet9_surface_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth \n" 
            "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the \n" 
            "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a \n" 
            "smaller version."
)

def create_planet9_surface_shell(center_position=(0, 0, 0)):
    """Creates eris's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(83, 68, 55)',  # optical brownish
        'opacity': 1.0,
        'name': 'Crust',
        # Source: Batygin & Brown (2016, 2021); Fortney et al. (2016);
        #         3.7 Earth radii for 5-10 Earth mass ice giant; composition modeled on Uranus/Neptune.
        #         Planet Nine is hypothetical -- all values are model predictions.
        'description': (
            "Planet 9 Surface<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth <br>" 
            "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the <br>" 
            "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a <br>" 
            "smaller version.<br>" 
            "* Mass and Density Relationship: For a given mass, the radius of a planet is strongly influenced by its density.<br>" 
            "* Terrestrial Planets: Terrestrial planets (like Earth, Mars, Venus, Mercury) are primarily composed of rock and metal, <br>" 
            "  making them quite dense. If Planet Nine were a terrestrial planet with 5-10 times the mass of Earth, its radius would <br>" 
            "  likely be significantly smaller than 3-4 Earth radii due to its high density.<br>" 
            "* Gas Giants: Gas giants (like Jupiter and Saturn) are composed mostly of hydrogen and helium, making them very large and <br>" 
            "  not very dense. A planet with several Earth masses composed primarily of these light gases would have a much larger radius <br>" 
            "  than 3-4 Earth radii.<br>" 
            "* Ice Giants: Ice giants (like Uranus and Neptune) have a composition that includes heavier elements like oxygen, carbon, <br>" 
            "  nitrogen, and sulfur, often in the form of water, methane, and ammonia ices, along with a significant amount of hydrogen and <br>" 
            "  helium. This composition results in densities higher than gas giants but lower than terrestrial planets.<br>" 
            "The 3-4 Earth radii estimate, particularly the 3.7 Earth radii figure, comes from models that assume Planet Nine has a mass <br>" 
            "around 5-10 Earth masses and an internal composition similar to Uranus and Neptune. These models predict that such a planet <br>" 
            "would have a larger radius than Earth due to its significant mass, but not as large as a pure gas giant with the same mass due <br>" 
            "to the presence of heavier \"ice\" materials. Therefore, the estimated radius of 3-4 Earth radii strongly suggests that Planet <br>" 
            "Nine, if it exists, is likely an ice giant or a sub-Neptune type of planet, rather than a rocky terrestrial planet or a large <br>" 
            "gas giant. This is also consistent with theories about how a planet could have formed or been captured in the distant outer <br>" 
            "solar system."
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * PLANET9_RADIUS_AU
    
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
        name=f"Planet 9: {layer_info['name']}",
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
    hover_texts = [layer_info['description']] * len(x_hover)

    # Just the name for "Object Names Only" mode
    layer_name = f"Planet 9: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(83, 68, 55)',  # brownish
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Planet 9: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

# Source: Batygin & Brown (2016, 2021); NASA Solar System Exploration;
#         Hill sphere ~7.6 AU derived from a=600 AU, e=0.30, m=6 Earth masses.
#         Note: 2021 refinement favors a=460 +/- 100 AU as central estimate; 600 AU remains valid for visualization.
#         Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.
planet9_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n" 
            "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU."                     
)

def create_planet9_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Planet 9's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 48000, # this is estimated based on the modeled data
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        # Source: Batygin & Brown (2016, 2021); NASA Solar System Exploration;
        #         a=600 AU baseline (2021 refinement: ~460 AU central estimate), e=0.30, m=6 Earth masses.
        #         Using perihelion distance in Hill sphere formula is more physically accurate for satellite stability.
        #         Planet Nine is hypothetical -- all values are model predictions.
        'description': (
            "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.<br><br>"
            "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br><br>" 
            "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU.<br>" 
            "To arrive at the Hill sphere estimate of 7.6 AU, we made the following key assumptions about Planet Nine: <br>" 
            "* Semi-major axis (a): We assumed a semi-major axis of 600 AU. This value is within the range of 500-700 AU suggested <br>" 
            "  by some studies, including those considering the IRAS/AKARI observations. Note: 2021 refinements by Batygin & Brown <br>" 
            "  favor a slightly closer orbit (~460 AU central estimate). The semi-major axis has a direct linear relationship with <br>" 
            "  the Hill sphere radius. A larger semi-major axis leads to a larger Hill sphere.<br>" 
            "* Eccentricity (e): We assumed an eccentricity of 0.30 (range 0.15-0.40 in newer models). This gives a perihelion <br>" 
            "  around 280 AU and an aphelion around 1120 AU. The eccentricity affects the Hill sphere radius because the formula <br>" 
            "  uses the distance to the Sun at the perihelion. A higher eccentricity would result in a smaller Hill sphere radius.<br>" 
            "* Mass of Planet Nine (m): We assumed a mass of 6 times the mass of Earth. This is the current 'sweet spot' estimate <br>" 
            "  from Batygin & Brown (2021), revised down from the original 10 Earth mass prediction. The mass has a cubic root <br>" 
            "  relationship with the Hill sphere radius.<br>" 
            "* Mass of the Sun (M): We used the standard value for the mass of the Sun. This is a well-established constant.<br>" 
            "* In summary: the region where Planet 9's gravity is strong enough to hold onto its own moons despite the Sun's pull is <br>" 
            "  what the Hill sphere represents. To estimate the radius of this safe zone, we take Planet Nine's average distance from <br>" 
            "  the Sun, which we're assuming to be 600 AU (that's 600 times the distance between the Earth and the Sun). Because <br>" 
            "  Planet Nine's orbit isn't a perfect circle but more of an oval shape (we call this eccentricity, and we're assuming <br>" 
            "  it's 0.30), the closest it gets to the Sun is a bit less than this average. To account for this, we consider the distance <br>" 
            "  at its closest approach, which is roughly its average distance multiplied by (one minus the eccentricity), <br>" 
            "  so 600AUx(1-0.30)=600AUx0.70=420AU. This closest distance is important because the Sun's gravity is strongest there, <br>" 
            "  making it harder for Planet Nine to hold onto moons. Now, we also need to consider how strong Planet Nine's gravity is <br>" 
            "  compared to the Sun's. We're assuming Planet Nine has a mass of 6 times the mass of the Earth. The Sun, of course, is <br>" 
            "  vastly more massive.<br>" 
            "* The full equation for calculating the Hill sphere radius is: r_Hill = a x (m/(3 x M))^(1/3). Where: a is the semi-major <br>" 
            "  axis of Planet Nine's orbit around the Sun; m is the mass of Planet Nine; M is the mass of the Sun."        
            )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLANET9_RADIUS_AU
    
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
            name=f"Planet 9: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Planet 9: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    # Add a sun direction indicator (arrow pointing toward Sun along negative X-axis)
    sun_traces = create_sun_direction_indicator(center_position)
    for trace in sun_traces:
        traces.append(trace)

    return traces