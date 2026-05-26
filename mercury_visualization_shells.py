"""
mercury_visualization_shells.py - Mercury interior, exosphere, and unique feature traces.

Custom geometry for the sodium exosphere tail (anti-sunward) and
magnetosphere (compressed by solar wind). Sphere shells (inner core,
outer core, mantle, crust, exosphere, Hill sphere) are now handled by
build_sphere_shell() in orrery_rendering.py via configs in shell_configs.py.
The _info strings remain here for GUI tooltip consumption via globals().

Mercury's core is proportionally the largest of any planet (~85% of its radius).

Consumed by: planet_visualization.py (dispatch loop via CUSTOM_SHELLS lazy import),
             palomas_orrery.py (_info strings via globals() for build_shell_checkboxes)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
    April 17, 2026: provenance audit source citations added, Gemini fact-check applied.
    Sodium tail decimal error corrected (2.4 Mkm -> 24 Mkm).
    Provenance audit identified by Anthropic's Claude Opus 4.7
"""
import numpy as np
import math
import plotly.graph_objs as go
from orrery_rendering import create_info_marker, rotate_to_sunward
from planet_visualization_utilities import (MERCURY_RADIUS_AU, KM_PER_AU, create_magnetosphere_shape)


# ============================================================
# GUI tooltip strings (_info)
# ============================================================
# These are consumed by palomas_orrery.py via globals() for
# build_shell_checkboxes() tooltip wiring. They remain here
# until Phase D migrates tooltips to shell_configs.py.

mercury_inner_core_info = (
            "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.\n" 
            "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about \n" 
            "1,000 kilometers thick based on Messenger findings (2019)."
)

# Source: NASA MESSENGER Mission; Margot et al. (2012) (outer core 1074 km)
# Verified: April 2026 via Gemini fact-check
mercury_outer_core_info = (
            "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \n" 
            "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
)

mercury_mantle_info = (
            "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \n" 
            "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \n" 
            "Earth's, estimated to be only about 331 kilometers thick."
)

# Source: NASA MESSENGER; Sori (2018) (crustal thickness ~35 km)
#         Pei et al. (2024) (diamond layer from graphite + meteorite impacts)
# Verified: April 2026 via Gemini fact-check
mercury_crust_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n"     
            "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin \n" 
            "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, \n" 
            "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
)

# Source: NASA MESSENGER; NASA Mercury Fact Sheet
# Verified: April 2026 via Gemini fact-check
mercury_atmosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n"     
            "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not \n" 
            "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, \n" 
            "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts."
)


# ============================================================
# Custom geometry functions (live -- called via CUSTOM_SHELLS lazy import)
# ============================================================

# Source: Potter & Morgan (1985); MESSENGER sodium tail observations
# Verified: April 2026 via Gemini fact-check
mercury_sodium_tail_info = (
            "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n"
            "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\n\n" 

            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \n"
            "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury's exosphere \n"
            "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.\n\n"
            "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. \n"
            "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
)

def create_mercury_sodium_tail(center_position=(0, 0, 0)):
    """Creates Mercury's sodium tail visualization extending away from the Sun."""
    
    # Define layer properties
    layer_info = {
        'name': 'Sodium Tail',
        'description': (
            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii <br>"
            "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury's exosphere <br>"
            "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.<br><br>"
            "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. <br>"
            "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
        )
    }
    
    # Sodium tail extends up to ~10,000 Mercury radii away from the Sun
    max_tail_length = 10000 * MERCURY_RADIUS_AU
    
    # Create a conical tail shape pointing away from the Sun
    # Sun is at origin (0,0,0), so tail points away from (0,0,0) relative to Mercury's position
    center_x, center_y, center_z = center_position
    
    # Calculate direction away from Sun (normalized)
    distance = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    if distance > 0:
        dir_x = center_x / distance
        dir_y = center_y / distance
        dir_z = center_z / distance
    else:
        # If Mercury is at origin, default to +x direction
        dir_x, dir_y, dir_z = 1, 0, 0
    
    # Create tail as a cone of particles with varying density
    num_particles = 500
    tail_points_x = []
    tail_points_y = []
    tail_points_z = []
    
    for i in range(num_particles):
        # Distance along tail (0 to max_tail_length)
        tail_distance = (i / num_particles) * max_tail_length
        
        # Cone widens as it extends (opening angle ~5-10 degrees)
        max_radius = tail_distance * math.tan(math.radians(7))
        
        # Random position within cone cross-section
        theta = np.random.uniform(0, 2 * math.pi)
        r = np.random.uniform(0, max_radius)
        
        # Create perpendicular vectors to tail direction
        if abs(dir_z) < 0.9:
            perp1_x = -dir_y
            perp1_y = dir_x
            perp1_z = 0
        else:
            perp1_x = 1
            perp1_y = 0
            perp1_z = -dir_x / dir_z if dir_z != 0 else 0
        
        # Normalize perp1
        perp1_len = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
        if perp1_len > 0:
            perp1_x /= perp1_len
            perp1_y /= perp1_len
            perp1_z /= perp1_len
        
        # Cross product for second perpendicular
        perp2_x = dir_y * perp1_z - dir_z * perp1_y
        perp2_y = dir_z * perp1_x - dir_x * perp1_z
        perp2_z = dir_x * perp1_y - dir_y * perp1_x
        
        # Position in tail
        x = center_x + tail_distance * dir_x + r * (math.cos(theta) * perp1_x + math.sin(theta) * perp2_x)
        y = center_y + tail_distance * dir_y + r * (math.cos(theta) * perp1_y + math.sin(theta) * perp2_y)
        z = center_z + tail_distance * dir_z + r * (math.cos(theta) * perp1_z + math.sin(theta) * perp2_z)
        
        tail_points_x.append(x)
        tail_points_y.append(y)
        tail_points_z.append(z)
    
    # Create color gradient with alpha channel for fading effect
    # RGBA colors where alpha decreases with distance
    colors = []
    for i in range(num_particles):
        alpha = 0.6 * (1 - i/num_particles)**2  # Fades with distance
        # Ensure alpha is at least 0.001 to avoid scientific notation issues
        alpha = max(alpha, 0.001)
        colors.append(f'rgba(255, 200, 100, {alpha:.3f})')
    
    trace_name = f"Mercury: {layer_info['name']}"
    traces = [
        go.Scatter3d(
            x=tail_points_x,
            y=tail_points_y,
            z=tail_points_z,
            mode='markers',
            marker=dict(
                size=2.5,
                color=colors,  # Use RGBA colors for per-point opacity
            ),
            name=trace_name,
            legendgroup=trace_name,
            hoverinfo='skip',
            showlegend=True
        )
    ]
    # Info marker at first point
    traces.append(create_info_marker(
        tail_points_x[0], tail_points_y[0], tail_points_z[0],
        'rgb(255, 200, 100)', f"{trace_name}<br><br>{layer_info['description']}", trace_name
    ))
    
    return traces


# Source: NASA MESSENGER Mission
# Verified: April 2026 via Gemini fact-check
mercury_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n" 

            "Magnetosphere: Mercury has a surprisingly active magnetosphere, given its small size and slow rotation. However, it is \n" 
            "significantly weaker and smaller than Earth's magnetosphere."
)

def create_mercury_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):

    """Creates Mercury's magnetosphere.
    
    Geometry is generated with bow shock along -X and tail along +X
    (the default when Mercury is at origin). When center_position is
    non-zero, all points are rotated so that the bow shock points
    toward the Sun at (0,0,0) before the center offset is applied.
    """
    traces = []
    
    # Compute sunward rotation -- promoted to orrery_rendering.rotate_to_sunward()
    # Phase C1: import replaces the local nested function
    center_x, center_y, center_z = center_position
    
    # Parameters for magnetosphere components (in Mercury radii)
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
    #    'inner_belt_distance': 1.5,  # Distance in Earth radii
    #    'outer_belt_distance': 4.5,  # Distance in Earth radii
    #    'belt_thickness': 0.5,
    }
    
    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= MERCURY_RADIUS_AU
    
    # Create magnetosphere main shape (generated along -X sunward / +X tail)
    x, y, z = create_magnetosphere_shape(params)
    
    # Rotate to actual sunward direction, then offset to center position
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position, sun_position=sun_position)

    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    magnetosphere_text = ["Magnetosphere: Mercury has a surprisingly active magnetosphere, given its small size and slow rotation. <br>" 
                          "However, it is significantly weaker and smaller than Earth's magnetosphere.<br>" 
                          "* Intrinsic Magnetic Field: Mercury generates an internal magnetic field, likely due to dynamo action in <br>" 
                          "  its partially liquid outer core. This was a significant discovery by Mariner 10 in the 1970s and has been <br>" 
                          "  further studied by the MESSENGER and BepiColombo missions.<br>" 
                          "* Interaction with the Solar Wind: This weak magnetic field is still strong enough to deflect the solar wind, <br>" 
                          "  creating a small magnetosphere around the planet. This magnetosphere has features similar to Earth's, including <br>" 
                          "  a bow shock, magnetopause, and magnetotail.<br>" 
                          "  Dynamic and Leaky: Due to its proximity to the Sun, Mercury's magnetosphere experiences a much stronger and more <br>" 
                          "  dynamic solar wind than Earth. This interaction can lead to magnetic reconnection events and a \"leakier\" <br>" 
                          "  magnetosphere, allowing more solar wind particles to reach the planet's surface and contribute to its exosphere.<br>" 
                          "* No Stable Radiation Belts: Unlike Earth's Van Allen radiation belts, Mercury's small and dynamic magnetosphere <br>" 
                          "  doesn't have stable regions for trapping high-energy particles for extended periods.<br><br>" 
                          "* Sunward Distance (to the Bow Shock): The bow shock is the outermost boundary where the supersonic solar <br>" 
                          "  wind is slowed and heated as it encounters Mercury's magnetosphere. A typical sunward distance to the bow shock is <br>" 
                          "  estimated to be around 1.4 to 2.0 radii from the center of Mercury.<br>" 
                          "* Equatorial Radius (of the Magnetopause): The magnetopause is the boundary where Mercury's magnetic field <br>" 
                          "  pressure balances the solar wind pressure. In the equatorial plane (perpendicular to the magnetic poles), the <br>" 
                          "  magnetopause typically extends to about 1.1 to 1.5 radii from the center of Mercury. <br>" 
                          "* Polar Radius (of the Magnetopause): Estimates for the distance to the magnetopause at the poles range <br>" 
                          "  from about 0.8 to 1.2 radii from the center. In some models, it can be very close to the surface.<br>" 
                          "* Tail Length (Magnetotail): around 10 to 30 radii downwind. However, it can be significantly longer or <br>" 
                          "  shorter depending on solar wind conditions and magnetic reconnection events.<br>" 
                          "* Tail Base Radius: we can estimate it to be around 1.1 to 1.5 radii.<br>" 
                          "* Tail End Radius: likely in the range of 2 to 5 radii, but this is highly variable and less well-defined."]

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Mercury: Magnetosphere',
            legendgroup='Mercury: Magnetosphere',
            hoverinfo='skip',
            showlegend=True
        )
    )
    # Info marker at first point on magnetosphere structure
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(180, 180, 255)', f"Mercury: Magnetosphere<br><br>{magnetosphere_text[0]}", 'Mercury: Magnetosphere'
    ))
    
    # 2. Create and add bow shock
    bow_shock_x = []
    bow_shock_y = []
    bow_shock_z = []
    
    n_phi = 30
    n_theta = 30
    bow_shock_standoff = 15 * MERCURY_RADIUS_AU
    bow_shock_width = 25 * MERCURY_RADIUS_AU
    
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
    
    # Rotate to actual sunward direction, then offset to center position
    bow_shock_x = np.array(bow_shock_x)
    bow_shock_y = np.array(bow_shock_y)
    bow_shock_z = np.array(bow_shock_z)
  
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position, sun_position=sun_position
    )

    bow_shock_x = bow_shock_x + center_x
    bow_shock_y = bow_shock_y + center_y
    bow_shock_z = bow_shock_z + center_z
    
    bow_shock_text = ["Bow Shock: The bow shock is the outermost boundary where the supersonic solar wind is slowed and heated as <br>" 
                      "it encounters Mercury's magnetosphere. This distance is highly variable depending on the solar wind conditions, <br>" 
                      "but a typical sunward distance to the bow shock is estimated to be around 1.4 to 2.0 radii from the center of Mercury.<br>"
                      "The Bow Shock points towards the Sun. The XY plane is the ecliptic."]

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
            name='Mercury: Bow Shock',
            legendgroup='Mercury: Bow Shock',
            hoverinfo='skip',
            showlegend=True
        )
    )
    # Info marker at first point on bow shock structure
    traces.append(create_info_marker(
        bow_shock_x[0], bow_shock_y[0], bow_shock_z[0],
        'rgb(255, 200, 150)', f"Mercury: Bow Shock<br><br>{bow_shock_text[0]}", 'Mercury: Bow Shock'
    ))
        
    # Phase A (May 2026): sun direction indicator emission moved to dispatch
    # loop in planet_visualization.py. One indicator per body, not per shell.

    return traces

# Source: NASA Solar System Dynamics
# Verified: April 2026 via Gemini fact-check
mercury_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.003 AU TO VISUALIZE.\n\n" 
            "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it \n" 
            "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on \n" 
            "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the \n" 
            "extent of Mercury's Hill sphere compared to planets farther out."
)
