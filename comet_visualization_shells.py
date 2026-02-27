import numpy as np
import math
import plotly.graph_objs as go
from shared_utilities import create_sun_direction_indicator
from planet_visualization_utilities import KM_PER_AU

# Comet nucleus sizes (approximate, in km)
COMET_NUCLEUS_SIZES = {
    'Halley': 15,  # 15x8x8 km
    'Hale-Bopp': 60,  # ~60 km diameter
    'NEOWISE': 5,  # ~5 km
    'ISON': 2,  # ~2 km (before breakup)
    'West': 5,  # ~5 km
    'Ikeya-Seki': 5,  # ~5 km
    'Hyakutake': 4,  # ~4 km
    'Lemmon': 3,  # ~3 km (estimated) C/2025 A6
    '3I/ATLAS': 8,  # ~8 km (estimated, interstellar object)
    'Wierzchos': 5,  # ~2-10 km (JWST estimates), using midpoint
    'Schaumasse': 3,  # ~2.6 km nucleus
    'Howell': 3,  # ~3 km (estimated)
    'Tempel 2': 16,  # ~16x9 km, elongated nucleus (well-studied by Deep Space 1)
    'default': 5  # Default size for generic comets
}

# Historical peak tail lengths (in millions of km)
# 
# COLOR NOTE: The coma and tail colors in this dictionary represent typical appearance
# in ASTROPHOTOGRAPHY (long-exposure imaging), not naked-eye visual appearance.
# Most comets are too faint for human color vision to activate; only the brightest
# comets (magnitude < ~2) show noticeable color to the unaided eye. In those rare cases,
# dust tails appear whitish/grayish (not yellow), and ion tails may appear pale blue.
# 
# However, astrophotography reveals the true spectroscopic signatures:
# - Dust tails: Yellow/gold from reflected sunlight (full visible spectrum)
# - Ion tails: Blue from CO+ ion emissions (400-460nm)
# - Coma: Green from C2 (dicarbon) emissions (near nucleus only)
#
# Since this visualization uses semi-transparent particle rendering similar to
# long-exposure photography, and since most people are familiar with comets from
# photographs rather than naked-eye observation, these colors match astrophotography.
HISTORICAL_TAIL_DATA = {
    'Halley': {
        'max_dust_tail_length_mkm': 10,
        'max_ion_tail_length_mkm': 20,
        'peak_brightness_mag': -0.5,
        'perihelion_distance_au': 0.586,
        'description': "Halley's Comet - Most famous periodic comet, returns every 76 years",
        # NEW COLOR DATA:
        'coma_color': 'green',  # C2 emissions
        'dust_tail_color': 'yellow',  # Reflected sunlight
        'ion_tail_color': 'blue'  # CO+ emissions
    },
    'Hale-Bopp': {
        'max_dust_tail_length_mkm': 40,
        'max_ion_tail_length_mkm': 150,
        'peak_brightness_mag': -1.0,
        'perihelion_distance_au': 0.914,
        'description': "Comet Hale-Bopp - Great comet of 1997, visible to naked eye for 18 months",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    },
    'NEOWISE': {
        'max_dust_tail_length_mkm': 15,
        'max_ion_tail_length_mkm': 25,
        'peak_brightness_mag': 1.0,
        'perihelion_distance_au': 0.295,
        'description': "Comet NEOWISE (C/2020 F3) - Great comet of 2020",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    },
    'West': {
        'max_dust_tail_length_mkm': 30,
        'max_ion_tail_length_mkm': 50,
        'peak_brightness_mag': -3.0,
        'perihelion_distance_au': 0.197,
        'description': "Comet West - Spectacular great comet of 1976, nucleus fragmented",
        'coma_color': 'green',
        'dust_tail_color': 'gold',  # Very bright dust tail
        'ion_tail_color': 'cyan'
    },
    'Ikeya-Seki': {
        'max_dust_tail_length_mkm': 25,
        'max_ion_tail_length_mkm': 100,
        'peak_brightness_mag': -10.0,
        'perihelion_distance_au': 0.008,
        'description': "Comet Ikeya-Seki - Great sungrazing comet of 1965",
        'coma_color': 'white',  # Very hot, close to Sun
        'dust_tail_color': 'orange',  # Sodium emissions from Sun proximity
        'ion_tail_color': 'blue'
    },
    'Hyakutake': {
        'max_dust_tail_length_mkm': 20,
        'max_ion_tail_length_mkm': 580,
        'peak_brightness_mag': 0.0,
        'perihelion_distance_au': 0.230,
        'description': "Comet Hyakutake - Great comet of 1996, record-breaking ion tail",
        'coma_color': 'bright_green',  # Very prominent green
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'bright_blue'
    },
    'Lemmon': {
        'max_dust_tail_length_mkm': 8,
        'max_ion_tail_length_mkm': 15,
        'peak_brightness_mag': 4.5,     # at perihelion reaching magnitude 4 to 5
        'perihelion_distance_au': 0.53,
        'description': "Comet Lemmon (C/2025 A6) - Green coma from C2; bright dust tail",
        'coma_color': 'teal',  # Teal/greenish coma in astrophotography
        'dust_tail_color': 'gold',  # "Golden hued" dust tail near nucleus
        'ion_tail_color': 'blue'  # Long blue ion streamer
    },

    '3I/ATLAS': {
    # 3I/ATLAS DATA NOTES (as of Oct 28, 2025):
    # JPL Horizons: C/2025 N1, Rec #90004917, Soln.date: 2025-Oct-10
    # - Perihelion: Oct 29.48, 2025 (TP=2460977.9835 JD) at QR=1.356 AU
    # - Eccentricity: e=6.137 (highly hyperbolic, interstellar origin confirmed)
    # - Inclination: i=175.1 deg (retrograde orbit)
    # - Total magnitude: M1=12.3 (Horizons comet model)
    # - Composition: CO2-rich with H2O present (JWST/SPHEREx confirmed)
    # - Tail lengths: No official measurements; values are model-based estimates
    # - SPHEREx measured CO2 coma radius: ~3.5x10^5 km (~0.0023 AU)
    # - ESA Mars flyby (Oct 3, 2025): Imaged at ~30M km, no tail length released
    # - Colors reflect red-sloped, dust-rich appearance in imaging
    # Data arc: 2025-05-15 to 2025-09-21 (646 observations over 129 days)

    #    'max_dust_tail_length_mkm': 8,  # PRELIMINARY: model-based estimate
    #    'max_ion_tail_length_mkm': 15,  # PRELIMINARY: model-based, multi-million km extent
    #    'peak_brightness_mag': 12.3,  # M1 from JPL Horizons (total magnitude model)
    #    'perihelion_distance_au': 1.356,  # Oct 29, 2025, QR from JPL Horizons
    #    'description': "3I/ATLAS (C/2025 N1) - Interstellar; e~6.14, i~175 deg. "
    #                "JWST & SPHEREx: CO2-dominated coma with H2O, CO present; "
    #                "tail extents still TBD from official releases.",
    #    'coma_color': 'green',  # Red-sloped, dust-rich appearance in observations
    #    'dust_tail_color': 'yellow',  # Red-sloped dust tail
    #    'ion_tail_color': 'blue',  # CO2+/CO+ emissions
    #    'hyperbolic': True,  # e = 6.137 (highly hyperbolic)
    #    'co2_rich': True,  # JWST/SPHEREx confirmed
    #    'preliminary_data': True,  # Flag for tail measurement uncertainty
    #    'max_active_distance_au': 2.5  # Conservative estimate for CO2-driven activity

# 3I/ATLAS UPDATED DATA (February 2026):
        # - Perihelion: Oct 29.48, 2025 at 1.356 AU (between Mars and Earth)
        # - Closest to Earth: Dec 19, 2025 (~1.8 AU)
        # - Opposition: Jan 22, 2026 (Sun-Earth-3I aligned to 0.69 deg)
        # - Dynamics: e ~ 6.14, v_inf ~ 58 km/s (Fastest interstellar object yet)
        # - Size: Nucleus 0.82-5.6 km (Jewitt/Forbes); rotation 7.1 hr
        # - Ni/Fe ratio: 3.2 pre-perihelion -> 1.1 by late Jan (approaching solar values)
        # - SPHEREx Dec 2025: "fully active" - H2O, CO2, CO, organics, warm dust
        # - Post-perihelion outgassing now CO-dominated (surface ices depleted)
        # - Hubble Jan 7/14/22: quad-jet structure with prominent anti-tail
        #   Anti-tail: ~400,000 km sunward, tightly collimated, wobbles +/-20 deg
        #   with 7.2 hr period. Rotation axis aligned within 7 deg of Sun.
        # - VLT polarimetry: 38% linear polarization in anti-tail (sub-micron silicates)
        # - Feb 2026: mag ~16.7, coma contracted to 1.8 arcmin, faint dust tail 6 arcmin
        # - Next event: Jupiter flyby Mar 16, 2026 at 0.358 AU

        'max_dust_tail_length_mkm': 12,  # Post-perihelion dust tail confirmed in long exposures
        'max_ion_tail_length_mkm': 25,  # Models adjusted for high gas production
        'peak_brightness_mag': 9.5,      # Observed peak near perihelion
        'perihelion_distance_au': 1.356,
        'description': "3I/ATLAS (C/2025 N1) - Third confirmed interstellar object. "
                       "Post-perihelion 'greening' due to C2 release; "
                       "CO2-dominated (8:1 ratio over water). High non-gravitational "
                       "acceleration observed due to complex outgassing jets. "
                       "Hubble quad-jet structure with ~400,000 km anti-tail. "
                       "Rotation 7.1 hr, Ni/Fe ratio converging toward solar values. "
                       "Jupiter flyby Mar 16, 2026 at 0.358 AU.",
        'coma_color': '#50FF78',          # Bright Green: Dominated by C2 emissions post-perihelion
        'dust_tail_color': '#F5EBB4',     # Pale Yellow-White: Reflective sunlight off dust particles
        'ion_tail_color': '#55AAFF',      # Azure/Cyan: "Vividly blue" ion tail (Virtual Telescope Project)
        'hyperbolic': True,
        'co2_rich': True,
        'preliminary_data': False,          # Data now well-constrained by Hubble/SPHEREx/VLT
        'max_active_distance_au': 5.5,      # Activity noted out to ~6 AU inbound
        # Anti-tail properties (Hubble Jan 7/14/22, 2026)
        'anti_tail_length_km': 400000,      # ~400,000 km sunward (Earth-Moon distance scale)
        'anti_tail_color': '#C0C0C8',       # Gray/faint silver per imaging reports
        'anti_tail_collimation': 0.1,       # ~10:1 length-to-width (tightly collimated jet)
        'jet_count': 4,                     # Quad-jet: 1 anti-tail + 3 mini-jets at 120 deg spacing (Hubble Jan 2026)
    },

    'Wierzchos': {
        'max_dust_tail_length_mkm': 5,
        'max_ion_tail_length_mkm': 12,
        'peak_brightness_mag': 6.8,
        'perihelion_distance_au': 0.562,
        'description': "Comet C/2024 E1 (Wierzchos) - CO2-driven Oort Cloud comet, "
                       "3 dust tails (fan structure) and 5-degree ion tail post-perihelion Jan 2026. "
                       "APOD Feb 17 2026. Near-parabolic orbit, ~200,000 year outbound period.",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue',
        'dust_tail_count': 3,       # APOD Feb 17, 2026: 3 dust tails in fan pattern
        # Two short tails fan NW, one broader ~2 deg tail NE (Coquimbo obs Feb 13, 2026)
        'dust_tail_fan_angle': 40   # Half-angle of fan spread in degrees
    },
    'Schaumasse': {
        'max_dust_tail_length_mkm': 2,
        'max_ion_tail_length_mkm': 5,
        'peak_brightness_mag': 9.0,
        'perihelion_distance_au': 1.18,
        'description': "24P/Schaumasse - Jupiter-family periodic comet, 8.25 year period. "
                       "Discovered 1911 by Alexandre Schaumasse. Nucleus ~2.6 km.",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    },
    'Howell': {
        'max_dust_tail_length_mkm': 2,
        'max_ion_tail_length_mkm': 4,
        'peak_brightness_mag': 10.0,
        'perihelion_distance_au': 1.41,
        'description': "88P/Howell - Jupiter-family periodic comet, 5.5 year period. "
                       "Discovered 1981 by Ellen Howell. Southern hemisphere favored.",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    },
    'Tempel 2': {
        'max_dust_tail_length_mkm': 3,
        'max_ion_tail_length_mkm': 6,
        'peak_brightness_mag': 8.0,
        'perihelion_distance_au': 1.42,
        'description': "10P/Tempel 2 - Jupiter-family periodic comet, 5.37 year period. "
                       "Discovered 1873 by Wilhelm Tempel. Well-studied nucleus ~16x9 km.",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    },
    'default': {
        'max_dust_tail_length_mkm': 10,
        'max_ion_tail_length_mkm': 20,
        'peak_brightness_mag': 3.0,
        'perihelion_distance_au': 1.0,
        'description': "Generic comet parameters",
        'coma_color': 'green',
        'dust_tail_color': 'yellow',
        'ion_tail_color': 'blue'
    }
}


# Color palettes for comet features
COMET_COLOR_PALETTES = {
    'green': {
        'base_rgb': (100, 255, 100),
        'description': 'C2 diatomic carbon emissions'
    },
    'bright_green': {
        'base_rgb': (50, 255, 50),
        'description': 'Very strong C2 emissions'
    },
    'yellow': {
        'base_rgb': (255, 220, 100),
        'description': 'Reflected sunlight on dust'
    },
    'gold': {
        'base_rgb': (255, 200, 50),
        'description': 'Bright reflected sunlight'
    },
    'orange': {
        'base_rgb': (255, 150, 50),
        'description': 'Sodium D-line emissions'
    },
    'blue': {
        'base_rgb': (100, 180, 255),
        'description': 'CO+ ionized carbon monoxide'
    },
    'bright_blue': {
        'base_rgb': (80, 150, 255),
        'description': 'Strong CO+ emissions'
    },
    'cyan': {
        'base_rgb': (100, 255, 255),
        'description': 'Mixed ion emissions'
    },
    'teal': {
        'base_rgb': (80, 200, 180),  # Slightly greener teal
        'description': 'Blue-green C2 emissions (teal coma in astrophotography)'
    },    
    'white': {
        'base_rgb': (255, 255, 255),
        'description': 'Very hot, near Sun'
    }
}

def calculate_tail_activity_factor(current_distance_au, perihelion_distance_au, max_active_distance_au=3.0):
    """
    Calculate how active the comet is based on solar distance.
    
    Activity increases as comet approaches the Sun, peaks around perihelion,
    and decreases as it moves away. Uses inverse square law approximation.
    
    Parameters:
    -----------
    current_distance_au : float
        Current distance from Sun in AU
    perihelion_distance_au : float
        Perihelion distance in AU
    max_active_distance_au : float
        Distance beyond which comet becomes essentially inactive
        
    Returns:
    --------
    float : Activity factor from 0 (inactive) to 1 (peak activity)
    """
    if current_distance_au > max_active_distance_au:
        return 0.0
    
    # Activity roughly follows inverse square law but with a minimum
    # Activity = 1 at perihelion, decreases with distance
    activity = min(1.0, (perihelion_distance_au / current_distance_au) ** 1.5)
    
    # Add distance fade-out beyond max_active_distance
    if current_distance_au > perihelion_distance_au:
        fade_factor = 1.0 - ((current_distance_au - perihelion_distance_au) / 
                             (max_active_distance_au - perihelion_distance_au))
        activity *= max(0.0, fade_factor)
    
    return min(1.0, activity)


def create_comet_nucleus(center_position=(0, 0, 0), nucleus_size_km=5, comet_name="Generic"):
    """
    Creates a comet nucleus visualization as a single point.
    
    The nucleus is far too small to render at scale with the coma,
    so we represent it as a single visible marker.
    
    Parameters:
    -----------
    center_position : tuple
        (x, y, z) position in AU
    nucleus_size_km : float
        Diameter of nucleus in kilometers (for info only, not visual scale)
    comet_name : str
        Name of the comet for labeling
    """
    description = (
        f"Nucleus of {comet_name}<br>"
        f"Approximate size: {nucleus_size_km} km<br>"
        f"Cometary nuclei are 'dirty snowballs' - irregular chunks of ice, rock, and dust.<br>"
        f"As they approach the Sun, surface ice sublimates, releasing gas and dust.<br>"
        f"Note: The nucleus is far too small to show at scale with the coma."
    )
    
    trace = go.Scatter3d(
        x=[center_position[0]],
        y=[center_position[1]],
        z=[center_position[2]],
        mode='markers',
        marker=dict(
            size=4,
            color='rgb(50, 50, 50)',  # Very dark gray, almost black
            opacity=0.9,
            line=dict(color='white', width=1)  # Subtle white outline for visibility
        ),
        name=f'{comet_name}: Nucleus',
        text=[description],
        customdata=[f'{comet_name}: Nucleus'], 
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    
    return [trace]


def create_comet_coma(center_position=(0, 0, 0), coma_radius_km=100000, 
                      activity_factor=1.0, comet_name="Generic"):
    """
    Creates the coma (atmosphere) around the nucleus.
    
    Parameters:
    -----------
    center_position : tuple
        (x, y, z) position in AU
    coma_radius_km : float
        Radius of coma in kilometers
    activity_factor : float
        0-1, scales the coma size and brightness
    comet_name : str
        Name of the comet
    """
    if activity_factor < 0.1:
        return []  # No visible coma if inactive
    
    # Scale coma by activity
    effective_radius_km = coma_radius_km * activity_factor
    coma_radius_au = effective_radius_km / KM_PER_AU
    
    # Create spherical coma with radial density gradient
    n_particles = 300
    coma_points_x = []
    coma_points_y = []
    coma_points_z = []
    
    for i in range(n_particles):
        # Random spherical distribution, biased toward center
        r = coma_radius_au * (np.random.random() ** 0.5)  # Square root gives denser center
        theta = np.random.uniform(0, 2 * np.pi)
        phi = np.random.uniform(0, np.pi)
        
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        
        coma_points_x.append(center_position[0] + x)
        coma_points_y.append(center_position[1] + y)
        coma_points_z.append(center_position[2] + z)
    

# Get comet-specific color
    comet_data = HISTORICAL_TAIL_DATA.get(comet_name, HISTORICAL_TAIL_DATA['default'])
    coma_color_name = comet_data.get('coma_color', 'green')
    color_palette = COMET_COLOR_PALETTES.get(coma_color_name, COMET_COLOR_PALETTES['green'])
    base_r, base_g, base_b = color_palette['base_rgb']
    
    # Enhanced color with better visibility
    colors = []
    for i in range(n_particles):
        # Increased alpha for better visibility: 0.5-0.9 instead of 0.3
        alpha = (0.5 + 0.4 * activity_factor) * np.random.uniform(0.7, 1.0)
        # Slight color variation for natural look
        r = int(base_r * np.random.uniform(0.9, 1.0))
        g = int(base_g * np.random.uniform(0.9, 1.0))
        b = int(base_b * np.random.uniform(0.9, 1.0))
        colors.append(f'rgba({r}, {g}, {b}, {alpha:.3f})')

    
    description = (
        f"Coma of {comet_name}<br>"
        f"Radius: ~{effective_radius_km/1000:.0f} thousand km<br>"
        f"The coma is the fuzzy atmosphere of gas and dust surrounding the nucleus.<br>"
        f"It glows from reflected sunlight and fluorescence of gases like C2 (green)."
    )
    
    trace = go.Scatter3d(
        x=coma_points_x, y=coma_points_y, z=coma_points_z,
        mode='markers',
        marker=dict(
            size=3.0,
            color=colors,
            opacity=1.0
        ),
        name=f'{comet_name}: Coma',
        text=[description] * len(coma_points_x),
        customdata=[f'{comet_name}: Coma'] * len(coma_points_x), 
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    
    return [trace]


def create_comet_dust_tail(center_position=(0, 0, 0), velocity_vector=(0, 0, 0),
                           max_tail_length_mkm=10, activity_factor=1.0, 
                           comet_name="Generic", num_particles=800):
    """
    Creates the dust tail (Type II tail).
    
    The dust tail is curved, yellowish, and follows the comet's orbital path.
    Dust particles are pushed by solar radiation pressure but retain orbital momentum.
    
    Parameters:
    -----------
    center_position : tuple
        (x, y, z) position in AU
    velocity_vector : tuple
        (vx, vy, vz) velocity vector for curved tail direction
    max_tail_length_mkm : float
        Maximum tail length in millions of kilometers
    activity_factor : float
        0-1, scales tail brightness and length
    comet_name : str
        Name of the comet
    num_particles : int
        Number of particles to render
    """
    if activity_factor < 0.05:
        return []  # No visible tail if very inactive
    
    # Scale tail by activity
    effective_length_km = max_tail_length_mkm * 1e6 * activity_factor
    max_tail_length_au = effective_length_km / KM_PER_AU
    
    # Calculate anti-solar direction
    center_x, center_y, center_z = center_position
    sun_distance = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    
    if sun_distance < 1e-10:
        return []  # Can't compute at Sun's location
    
    # Anti-solar direction (away from Sun)
    anti_solar_x = center_x / sun_distance
    anti_solar_y = center_y / sun_distance
    anti_solar_z = center_z / sun_distance
    
    # Orbital velocity direction (for curve)
    vel_x, vel_y, vel_z = velocity_vector
    vel_mag = math.sqrt(vel_x**2 + vel_y**2 + vel_z**2)
    
    if vel_mag > 1e-10:
        vel_x /= vel_mag
        vel_y /= vel_mag
        vel_z /= vel_mag
    else:
        # No velocity info, make straight tail
        vel_x, vel_y, vel_z = 0, 0, 0
    
    # Dust tail curves backward along orbital path
    # Blend anti-solar direction with negative velocity direction
    curve_factor = 0.3  # How much the tail curves
    tail_dir_x = anti_solar_x - curve_factor * vel_x
    tail_dir_y = anti_solar_y - curve_factor * vel_y
    tail_dir_z = anti_solar_z - curve_factor * vel_z
    
    # Normalize
    tail_mag = math.sqrt(tail_dir_x**2 + tail_dir_y**2 + tail_dir_z**2)
    if tail_mag > 1e-10:
        tail_dir_x /= tail_mag
        tail_dir_y /= tail_mag
        tail_dir_z /= tail_mag
    else:
        tail_dir_x, tail_dir_y, tail_dir_z = anti_solar_x, anti_solar_y, anti_solar_z
    
    # Create tail particles
    tail_points_x = []
    tail_points_y = []
    tail_points_z = []
    
    for i in range(num_particles):
        # Distance along tail (0 to max_tail_length_au)
        tail_distance = (i / num_particles) * max_tail_length_au
        
        # Dust tail has a broader cone angle than ion tail
        max_radius = tail_distance * math.tan(math.radians(15))  # ~15 degree opening
        
        # Random position within cone cross-section
        theta = np.random.uniform(0, 2 * math.pi)
        r = np.random.uniform(0, max_radius) * np.random.random()**0.3  # Bias toward center
        
        # Create perpendicular vectors
        if abs(tail_dir_z) < 0.9:
            perp1_x = -tail_dir_y
            perp1_y = tail_dir_x
            perp1_z = 0
        else:
            perp1_x = 1
            perp1_y = 0
            perp1_z = -tail_dir_x / tail_dir_z if abs(tail_dir_z) > 1e-10 else 0
        
        # Normalize perp1
        perp1_len = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
        if perp1_len > 1e-10:
            perp1_x /= perp1_len
            perp1_y /= perp1_len
            perp1_z /= perp1_len
        
        # Cross product for second perpendicular
        perp2_x = tail_dir_y * perp1_z - tail_dir_z * perp1_y
        perp2_y = tail_dir_z * perp1_x - tail_dir_x * perp1_z
        perp2_z = tail_dir_x * perp1_y - tail_dir_y * perp1_x
        
        # Position in tail with slight curve
        curve_amount = (tail_distance / max_tail_length_au) ** 1.5 * curve_factor * 0.5
        x = center_x + tail_distance * tail_dir_x + r * (math.cos(theta) * perp1_x + math.sin(theta) * perp2_x)
        y = center_y + tail_distance * tail_dir_y + r * (math.cos(theta) * perp1_y + math.sin(theta) * perp2_y)
        z = center_z + tail_distance * tail_dir_z + r * (math.cos(theta) * perp1_z + math.sin(theta) * perp2_z)
        
        # Add curve in velocity direction
        x -= curve_amount * vel_x * tail_distance
        y -= curve_amount * vel_y * tail_distance
        z -= curve_amount * vel_z * tail_distance
        
        tail_points_x.append(x)
        tail_points_y.append(y)
        tail_points_z.append(z)
    
# Get comet-specific color
    comet_data = HISTORICAL_TAIL_DATA.get(comet_name, HISTORICAL_TAIL_DATA['default'])
    dust_color_name = comet_data.get('dust_tail_color', 'yellow')
    color_palette = COMET_COLOR_PALETTES.get(dust_color_name, COMET_COLOR_PALETTES['yellow'])
    base_r, base_g, base_b = color_palette['base_rgb']
    
    # Enhanced color with distance fade
    colors = []
    for i in range(num_particles):
        distance_factor = 1 - (i / num_particles)
        # Increased alpha: 0.7-0.95 at base, fading with distance
        alpha = (0.7 + 0.25 * activity_factor) * (distance_factor ** 1.2)
        alpha = max(alpha, 0.05)  # Minimum visibility
        # Color fades slightly with distance
        fade = 0.85 + 0.15 * distance_factor
        r = int(base_r * fade)
        g = int(base_g * fade)
        b = int(base_b * fade)
        colors.append(f'rgba({r}, {g}, {b}, {alpha:.3f})')

    
    description = (
        f"Dust Tail (Type II) of {comet_name}<br>"
        f"Maximum length: ~{max_tail_length_mkm * activity_factor:.1f} million km<br>"
        f"The dust tail is composed of small dust particles pushed by solar radiation pressure.<br>"
        f"It curves slightly along the comet's orbital path and appears yellowish from reflected sunlight.<br>"
        f"Dust particles are larger and slower than ions, creating the characteristic curved shape."
    )
    
    trace = go.Scatter3d(
        x=tail_points_x, y=tail_points_y, z=tail_points_z,
        mode='markers',
        marker=dict(
            size=2.0,
            color=colors,
            opacity=1.0
        ),
        name=f'{comet_name}: Dust Tail',
        text=[description] * len(tail_points_x),
        customdata=[f'{comet_name}: Dust Tail'] * len(tail_points_x),
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    
    return [trace]


def create_comet_ion_tail(center_position=(0, 0, 0), max_tail_length_mkm=20,
                          activity_factor=1.0, comet_name="Generic", num_particles=600):
    """
    Creates the ion tail (Type I tail, plasma tail).
    
    The ion tail is straight, bluish, and points directly away from the Sun.
    Ionized gas is swept away by the solar wind at high speeds.
    
    Parameters:
    -----------
    center_position : tuple
        (x, y, z) position in AU
    max_tail_length_mkm : float
        Maximum tail length in millions of kilometers
    activity_factor : float
        0-1, scales tail brightness and length
    comet_name : str
        Name of the comet
    num_particles : int
        Number of particles to render
    """
    if activity_factor < 0.05:
        return []  # No visible tail if very inactive
    
    # Scale tail by activity
    effective_length_km = max_tail_length_mkm * 1e6 * activity_factor
    max_tail_length_au = effective_length_km / KM_PER_AU
    
    # Calculate anti-solar direction (ion tail points directly away from Sun)
    center_x, center_y, center_z = center_position
    sun_distance = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    
    if sun_distance < 1e-10:
        return []  # Can't compute at Sun's location
    
    dir_x = center_x / sun_distance
    dir_y = center_y / sun_distance
    dir_z = center_z / sun_distance
    
    # Create tail particles - narrow cone, straighter than dust tail
    tail_points_x = []
    tail_points_y = []
    tail_points_z = []
    
    for i in range(num_particles):
        # Distance along tail
        tail_distance = (i / num_particles) * max_tail_length_au
        
        # Ion tail is narrower - only ~3-5 degree opening
        max_radius = tail_distance * math.tan(math.radians(4))
        
        # Random position within narrow cone
        theta = np.random.uniform(0, 2 * math.pi)
        r = np.random.uniform(0, max_radius) * np.random.random()**0.5
        
        # Create perpendicular vectors
        if abs(dir_z) < 0.9:
            perp1_x = -dir_y
            perp1_y = dir_x
            perp1_z = 0
        else:
            perp1_x = 1
            perp1_y = 0
            perp1_z = -dir_x / dir_z if abs(dir_z) > 1e-10 else 0
        
        # Normalize perp1
        perp1_len = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
        if perp1_len > 1e-10:
            perp1_x /= perp1_len
            perp1_y /= perp1_len
            perp1_z /= perp1_len
        
        # Cross product for second perpendicular
        perp2_x = dir_y * perp1_z - dir_z * perp1_y
        perp2_y = dir_z * perp1_x - dir_x * perp1_z
        perp2_z = dir_x * perp1_y - dir_y * perp1_x
        
        # Position in tail (straight line)
        x = center_x + tail_distance * dir_x + r * (math.cos(theta) * perp1_x + math.sin(theta) * perp2_x)
        y = center_y + tail_distance * dir_y + r * (math.cos(theta) * perp1_y + math.sin(theta) * perp2_y)
        z = center_z + tail_distance * dir_z + r * (math.cos(theta) * perp1_z + math.sin(theta) * perp2_z)
        
        tail_points_x.append(x)
        tail_points_y.append(y)
        tail_points_z.append(z)
    
# Get comet-specific color
    comet_data = HISTORICAL_TAIL_DATA.get(comet_name, HISTORICAL_TAIL_DATA['default'])
    ion_color_name = comet_data.get('ion_tail_color', 'blue')
    color_palette = COMET_COLOR_PALETTES.get(ion_color_name, COMET_COLOR_PALETTES['blue'])
    base_r, base_g, base_b = color_palette['base_rgb']
    
    # Enhanced color with distance fade
    colors = []
    for i in range(num_particles):
        distance_factor = 1 - (i / num_particles)
        # Increased alpha: 0.8-0.95 at base, fading with distance
        alpha = (0.8 + 0.15 * activity_factor) * (distance_factor ** 1.0)
        alpha = max(alpha, 0.1)  # Minimum visibility
        # Slight brightening toward nucleus
        brightness = 0.9 + 0.1 * distance_factor
        r = int(base_r * brightness)
        g = int(base_g * brightness)
        b = int(base_b * brightness)
        colors.append(f'rgba({r}, {g}, {b}, {alpha:.3f})')

    description = (
        f"Ion Tail (Type I, Plasma Tail) of {comet_name}<br>"
        f"Maximum length: ~{max_tail_length_mkm * activity_factor:.1f} million km<br>"
        f"The ion tail is composed of ionized gas molecules (CO+, H2O+, etc.) swept away by the solar wind.<br>"
        f"It points directly away from the Sun and appears bluish from fluorescence of ionized gases.<br>"
        f"The ion tail is typically straighter and longer than the dust tail, reaching millions of km in length."
    )
    
    trace = go.Scatter3d(
        x=tail_points_x, y=tail_points_y, z=tail_points_z,
        mode='markers',
        marker=dict(
            size=1.8,
            color=colors,
            opacity=1.0
        ),
        name=f'{comet_name}: Ion Tail',
        text=[description] * len(tail_points_x),
        customdata=[f'{comet_name}: Ion Tail'] * len(tail_points_x),
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    
    return [trace]


def create_comet_anti_tail(center_position=(0, 0, 0), anti_tail_length_km=400000,
                           activity_factor=1.0, comet_name="Generic",
                           anti_tail_color='#C0C0C8', collimation_ratio=0.1,
                           num_particles=200):
    """
    Creates anti-tail jet structure pointing TOWARD the Sun.
    
    For 3I/ATLAS, Hubble observations (Jan 7/14/22, 2026) revealed a quad-jet
    structure: 1 dominant anti-tail (sunward) + 3 mini-jets at 120 deg spacing.
    None of the mini-jets point anti-sunward as expected for a normal comet tail.
    The anti-tail extends ~400,000 km, tightly collimated (~10:1 length-to-width).
    The jet system wobbles +/-20 deg with a 7.2 hr rotation period.
    
    If the comet's data includes 'jet_count' > 1, mini-jets are rendered in the
    plane perpendicular to the sunward axis at equal angular spacing. Mini-jets
    are shorter (~40% of anti-tail) and dimmer (~60% brightness).
    
    Parameters:
    -----------
    center_position : tuple
        (x, y, z) position in AU
    anti_tail_length_km : float
        Length of anti-tail in km (e.g., 400,000 for 3I/ATLAS)
    activity_factor : float
        0-1, scales brightness and length
    comet_name : str
        Name of the comet
    anti_tail_color : str
        Hex color for the anti-tail (default gray/silver)
    collimation_ratio : float
        Width-to-length ratio (0.1 = 10:1 length-to-width, tightly collimated)
    num_particles : int
        Number of particles for the DOMINANT anti-tail jet
    """
    if activity_factor < 0.05:
        return []
    
    # Calculate SUNWARD direction (opposite of normal tail direction)
    center_x, center_y, center_z = center_position
    sun_distance = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    
    if sun_distance < 1e-10:
        return []
    
    # Unit vector TOWARD the Sun
    sun_dir_x = -center_x / sun_distance
    sun_dir_y = -center_y / sun_distance
    sun_dir_z = -center_z / sun_distance
    
    # Build perpendicular basis vectors (reused for all jets)
    if abs(sun_dir_z) < 0.9:
        perp1_x = -sun_dir_y
        perp1_y = sun_dir_x
        perp1_z = 0
    else:
        perp1_x = 1
        perp1_y = 0
        perp1_z = -sun_dir_x / sun_dir_z if abs(sun_dir_z) > 1e-10 else 0
    
    perp1_len = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
    if perp1_len > 1e-10:
        perp1_x /= perp1_len
        perp1_y /= perp1_len
        perp1_z /= perp1_len
    
    perp2_x = sun_dir_y * perp1_z - sun_dir_z * perp1_y
    perp2_y = sun_dir_z * perp1_x - sun_dir_x * perp1_z
    perp2_z = sun_dir_x * perp1_y - sun_dir_y * perp1_x
    
    # Parse color - support hex colors directly
    if anti_tail_color.startswith('#'):
        hex_color = anti_tail_color.lstrip('#')
        base_r = int(hex_color[0:2], 16)
        base_g = int(hex_color[2:4], 16)
        base_b = int(hex_color[4:6], 16)
    else:
        color_palette = COMET_COLOR_PALETTES.get(anti_tail_color, COMET_COLOR_PALETTES['white'])
        base_r, base_g, base_b = color_palette['base_rgb']
    
    # --- Helper: generate one jet as a particle cloud ---
    def _make_jet_particles(jet_dir, length_au, n_particles, alpha_scale=1.0):
        """Create particle positions and colors for a single jet."""
        jx, jy, jz = jet_dir
        half_angle = math.degrees(math.atan(collimation_ratio))
        pts_x, pts_y, pts_z = [], [], []
        
        for i in range(n_particles):
            dist = (i / n_particles) * length_au
            max_r = dist * math.tan(math.radians(half_angle))
            theta = np.random.uniform(0, 2 * math.pi)
            r = np.random.uniform(0, max_r) * np.random.random()**0.5
            
            pts_x.append(center_x + dist * jx + r * (math.cos(theta) * perp1_x + math.sin(theta) * perp2_x))
            pts_y.append(center_y + dist * jy + r * (math.cos(theta) * perp1_y + math.sin(theta) * perp2_y))
            pts_z.append(center_z + dist * jz + r * (math.cos(theta) * perp1_z + math.sin(theta) * perp2_z))
        
        colors = []
        for i in range(n_particles):
            dist_factor = 1 - (i / n_particles)
            alpha = (0.4 + 0.2 * activity_factor) * (dist_factor ** 0.8) * alpha_scale
            alpha = max(alpha, 0.05)
            colors.append(f'rgba({base_r}, {base_g}, {base_b}, {alpha:.3f})')
        
        return pts_x, pts_y, pts_z, colors
    
    traces = []
    
    # --- 1. Dominant anti-tail (sunward jet) ---
    effective_length_km = anti_tail_length_km * activity_factor
    anti_tail_au = effective_length_km / KM_PER_AU
    
    at_x, at_y, at_z, at_colors = _make_jet_particles(
        (sun_dir_x, sun_dir_y, sun_dir_z), anti_tail_au, num_particles, alpha_scale=1.0
    )
    
    description = (
        f"Anti-tail (Sunward Jet) of {comet_name}<br>"
        f"Length: ~{effective_length_km:,.0f} km toward the Sun<br>"
        f"Collimation: ~{int(1/collimation_ratio)}:1 length-to-width ratio<br>"
        f"This is a physical sunward jet, NOT a perspective effect.<br>"
        f"Possibly composed of icy fragments or large dust grains<br>"
        f"that resist solar radiation pressure."
    )
    
    traces.append(go.Scatter3d(
        x=at_x, y=at_y, z=at_z,
        mode='markers',
        marker=dict(size=1.4, color=at_colors, opacity=1.0),
        name=f'{comet_name}: Anti-tail',
        text=[description] * len(at_x),
        customdata=[f'{comet_name}: Anti-tail'] * len(at_x),
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    ))
    
    # --- 2. Mini-jets (if jet_count > 1 in comet data) ---
    comet_data = HISTORICAL_TAIL_DATA.get(comet_name, HISTORICAL_TAIL_DATA['default'])
    jet_count = comet_data.get('jet_count', 1)
    
    if jet_count > 1:
        num_mini_jets = jet_count - 1  # e.g., 3 mini-jets for quad-jet
        mini_jet_length_au = anti_tail_au * 0.4  # ~40% of anti-tail length
        mini_particles = num_particles // 3  # Fewer particles per mini-jet
        
        for j in range(num_mini_jets):
            # Equally spaced in the plane perpendicular to sunward axis
            angle = (2 * math.pi * j) / num_mini_jets
            
            # Mini-jet direction: combination of perpendicular vectors
            # These jets radiate outward from the nucleus, NOT anti-sunward
            mj_dir_x = math.cos(angle) * perp1_x + math.sin(angle) * perp2_x
            mj_dir_y = math.cos(angle) * perp1_y + math.sin(angle) * perp2_y
            mj_dir_z = math.cos(angle) * perp1_z + math.sin(angle) * perp2_z
            
            mj_x, mj_y, mj_z, mj_colors = _make_jet_particles(
                (mj_dir_x, mj_dir_y, mj_dir_z), mini_jet_length_au,
                mini_particles, alpha_scale=0.6  # Dimmer than anti-tail
            )
            
            mini_desc = (
                f"Mini-jet {j+1} of {comet_name}<br>"
                f"One of {num_mini_jets} jets at 120 deg spacing<br>"
                f"in the plane perpendicular to the sunward axis.<br>"
                f"None point anti-sunward (anomalous for comets).<br>"
                f"Hubble Jan 2026: quad-jet structure confirmed."
            )
            
            traces.append(go.Scatter3d(
                x=mj_x, y=mj_y, z=mj_z,
                mode='markers',
                marker=dict(size=1.0, color=mj_colors, opacity=1.0),
                name=f'{comet_name}: Mini-jet {j+1}',
                text=[mini_desc] * len(mj_x),
                customdata=[f'{comet_name}: Mini-jet {j+1}'] * len(mj_x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            ))
    
    return traces


def create_complete_comet_visualization(comet_name='Halley', center_position=(0, 0, 0),
                                       velocity_vector=(0, 0, 0), current_distance_au=None):
    """
    Creates a complete comet visualization with nucleus, coma, and both tails.
    
    Parameters:
    -----------
    comet_name : str
        Name of the comet (must be in HISTORICAL_TAIL_DATA or will use 'default')
    center_position : tuple
        Current (x, y, z) position in AU
    velocity_vector : tuple
        Current (vx, vy, vz) velocity for tail curvature
    current_distance_au : float or None
        Current distance from Sun in AU. If None, computed from center_position
        
    Returns:
    --------
    list : List of Plotly traces for all comet components
    """
    # Get comet data
    if comet_name not in HISTORICAL_TAIL_DATA:
        print(f"Warning: {comet_name} not found in database, using default parameters")
        comet_name_key = 'default'
    else:
        comet_name_key = comet_name
    
    comet_data = HISTORICAL_TAIL_DATA[comet_name_key]
    nucleus_size = COMET_NUCLEUS_SIZES.get(comet_name, COMET_NUCLEUS_SIZES['default'])
    
    # Calculate current distance if not provided
    if current_distance_au is None:
        cx, cy, cz = center_position
        current_distance_au = math.sqrt(cx**2 + cy**2 + cz**2)
    
    # Calculate activity factor based on distance
    perihelion_distance = comet_data['perihelion_distance_au']
    activity_factor = calculate_tail_activity_factor(current_distance_au, perihelion_distance)
    
    # Create all components
    traces = []
    
    # 1. Nucleus
    traces.extend(create_comet_nucleus(center_position, nucleus_size, comet_name))
    
    # 2. Coma (only if somewhat active)
    if activity_factor > 0.1:
        # Coma size scales with activity, typical range 50,000 - 200,000 km
        coma_size = 50000 + 150000 * activity_factor
        traces.extend(create_comet_coma(center_position, coma_size, activity_factor, comet_name))
    
    # 3. Dust tail(s)
    dust_length = comet_data['max_dust_tail_length_mkm']
    dust_tail_count = comet_data.get('dust_tail_count', 1)
    
    if dust_tail_count <= 1:
        # Standard single dust tail
        traces.extend(create_comet_dust_tail(center_position, velocity_vector, dust_length, 
                                            activity_factor, comet_name))
    else:
        # Multiple dust tails in a fan pattern
        # Fan uses perpendicular basis vectors to spread tails around the primary direction
        fan_half_angle = comet_data.get('dust_tail_fan_angle', 30)  # degrees
        
        center_x, center_y, center_z = center_position
        sun_dist = math.sqrt(center_x**2 + center_y**2 + center_z**2)
        
        if sun_dist > 1e-10:
            # Build perpendicular basis for fan spread
            anti_sun = (center_x/sun_dist, center_y/sun_dist, center_z/sun_dist)
            
            # Find a perpendicular vector using cross product with Z-up
            perp1_x = anti_sun[1] * 1 - anti_sun[2] * 0  # cross with (0,0,1)
            perp1_y = anti_sun[2] * 0 - anti_sun[0] * 1
            perp1_z = anti_sun[0] * 0 - anti_sun[1] * 0
            perp1_mag = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
            
            if perp1_mag < 1e-10:
                # Anti-sun is along Z, use X as reference
                perp1_x, perp1_y, perp1_z = 1, 0, 0
                perp1_mag = 1.0
            
            perp1_x /= perp1_mag
            perp1_y /= perp1_mag
            perp1_z /= perp1_mag
            
            # Second perpendicular (cross anti_sun x perp1)
            perp2_x = anti_sun[1]*perp1_z - anti_sun[2]*perp1_y
            perp2_y = anti_sun[2]*perp1_x - anti_sun[0]*perp1_z
            perp2_z = anti_sun[0]*perp1_y - anti_sun[1]*perp1_x
            
            fan_rad = math.radians(fan_half_angle)
            
            for t_idx in range(dust_tail_count):
                # Spread tails evenly across fan angle
                if dust_tail_count == 1:
                    angle = 0
                else:
                    angle = -fan_rad + 2 * fan_rad * t_idx / (dust_tail_count - 1)
                
                # Offset the velocity vector to curve each tail differently
                offset_scale = math.tan(angle) * 0.5
                modified_vel = (
                    velocity_vector[0] + offset_scale * perp1_x * sun_dist,
                    velocity_vector[1] + offset_scale * perp1_y * sun_dist,
                    velocity_vector[2] + offset_scale * perp1_z * sun_dist
                )
                
                # Outer tails are shorter (60% for edges, 100% for primary)
                center_weight = 1.0 - 0.4 * abs(2.0 * t_idx / (dust_tail_count - 1) - 1.0)
                tail_len = dust_length * center_weight
                
                # Fewer particles for secondary tails
                num_p = int(800 * center_weight)
                
                tail_traces = create_comet_dust_tail(
                    center_position, modified_vel, tail_len,
                    activity_factor, comet_name, num_particles=num_p
                )
                
                # Rename secondary tails in legend
                if t_idx > 0 and tail_traces:
                    for tr in tail_traces:
                        tr.name = f"{comet_name}: Dust Tail {t_idx + 1}"
                
                traces.extend(tail_traces)
    
    # 4. Ion tail
    ion_length = comet_data['max_ion_tail_length_mkm']
    traces.extend(create_comet_ion_tail(center_position, ion_length, activity_factor, comet_name))
    
    # 5. Sun direction indicator
    max_tail = max(dust_length, ion_length) * 1e6 / KM_PER_AU  # Convert to AU
    sun_traces = create_sun_direction_indicator(center_position, max_tail * activity_factor)
    traces.extend(sun_traces)
    
    return traces


# Info strings for GUI integration
comet_visualization_info = {
    'Halley': (
        "Halley's Comet Visualization\n\n"
        "This visualization shows Halley's Comet with scientifically accurate tail structures:\n"
        "* Dust Tail (yellowish): Curved tail following orbital path, up to 10 million km\n"
        "* Ion Tail (bluish): Straight tail pointing away from Sun, up to 20 million km\n"
        "* Coma: Fuzzy atmosphere around nucleus, up to 100,000 km radius\n"
        "* Nucleus: 15x8x8 km 'dirty snowball'\n\n"
        "Tail brightness and length scale with distance from the Sun.\n"
        "Most active at perihelion (0.586 AU from Sun)."
    ),
    'Hale-Bopp': (
        "Comet Hale-Bopp Visualization\n\n"
        "One of the greatest comets of the 20th century (1997):\n"
        "* Dust Tail: Up to 40 million km - one of the longest ever observed\n"
        "* Ion Tail: Up to 150 million km - spectacularly long plasma tail\n"
        "* Visible to naked eye for 18 months\n"
        "* Large nucleus: ~60 km diameter\n"
        "* Peak brightness: magnitude -1.0\n\n"
        "Hale-Bopp was remarkable for being visible even from light-polluted cities."
    ),
    'NEOWISE': (
        "Comet NEOWISE (C/2020 F3) Visualization\n\n"
        "Great comet of summer 2020:\n"
        "* Dust Tail: Up to 15 million km\n"
        "* Ion Tail: Up to 25 million km\n"
        "* Perihelion: 0.295 AU (very close to Sun)\n"
        "* Peak brightness: magnitude 1.0\n\n"
        "NEOWISE delighted millions during COVID-19 lockdowns."
    ),
    'Hyakutake': (
        "Comet Hyakutake Visualization\n\n"
        "The comet with the LONGEST ION TAIL ever recorded (1996):\n"
        "* Ion Tail: 580 million km - longer than the Sun-Jupiter distance!\n"
        "* Dust Tail: Up to 20 million km\n"
        "* Passed very close to Earth (0.10 AU)\n"
        "* Greenish coma visible to naked eye\n\n"
        "Hyakutake's record-breaking ion tail is still unmatched."
    ),
    'West': (
        "Comet West Visualization\n\n"
        "Spectacular great comet of 1976:\n"
        "* Peak brightness: magnitude -3.0 (visible in daylight!)\n"
        "* Dust Tail: Up to 30 million km\n"
        "* Ion Tail: Up to 50 million km\n"
        "* Nucleus fragmented during perihelion passage\n"
        "* Perihelion: 0.197 AU\n\n"
        "Comet West was one of the brightest comets of the 20th century."
    ),
    'Ikeya-Seki': (
        "Comet Ikeya-Seki Visualization\n\n"
        "Great sungrazing comet of 1965 - one of the brightest ever:\n"
        "* Peak brightness: magnitude -10 (brighter than the full Moon!)\n"
        "* Perihelion: 0.008 AU (450,000 km above Sun's surface)\n"
        "* Ion Tail: Up to 100 million km\n"
        "* Dust Tail: Up to 25 million km\n"
        "* Visible in daylight near the Sun\n"
        "* Nucleus fragmented from thermal stress\n\n"
        "Ikeya-Seki is a member of the Kreutz sungrazer family."
    ),
   
}


# ADD THIS FUNCTION TO comet_visualization_shells.py
# Insert this BEFORE the "if __name__ == '__main__':" section (before line 652)

# Distance thresholds for different comet features (AU)
COMET_FEATURE_THRESHOLDS = {
    'coma': 5.0,        # Sublimation begins ~5 AU
    'dust_tail': 3.5,   # Visible dust production ~3-4 AU  
    'ion_tail': 2.5     # Strong ionization ~2-3 AU
}


def add_comet_tails_to_figure(fig, comet_name, position_data, center_object_name='Sun'):
    """
    Add comet visualization to figure with feature-specific thresholds.
    
    Always shows nucleus. Coma, dust tail, and ion tail appear based on distance from Sun.
    Missing features are shown as gray entries in the legend.
    
    Parameters:
    -----------
    fig : plotly Figure
        The figure to add traces to
    comet_name : str
        Name of the comet (e.g., 'Halley', 'NEOWISE', '3I/ATLAS')
    position_data : dict
        Position data with 'x', 'y', 'z' keys (in AU) and optionally 'velocity' or 'vx', 'vy', 'vz'
    center_object_name : str
        Name of the center object (for coordinate adjustment), default 'Sun'
    
    Returns:
    --------
    fig : plotly Figure
        Figure with comet visualization traces added
    """
    import math
    import numpy as np
    import plotly.graph_objs as go
    
    
# Look up comet in database, use 'default' if not found
    # This automatically handles any comet name without manual mapping
    if comet_name in HISTORICAL_TAIL_DATA:
        db_name = comet_name
    else:
        db_name = 'default'
        print(f"[COMET VIZ] {comet_name} not in database, using default parameters")

    # Check if position data is valid
    if position_data is None:
        print(f"[COMET VIZ] Warning: No position data available for {comet_name}, skipping visualization")
        return fig

    # Get position
    pos_x = position_data.get('x', 0)
    pos_y = position_data.get('y', 0)
    pos_z = position_data.get('z', 0)
    position_au = (pos_x, pos_y, pos_z)
    
    # Calculate distance from Sun
    distance_au = math.sqrt(pos_x**2 + pos_y**2 + pos_z**2)
    
    # Get velocity if available
    velocity_km_s = position_data.get('velocity', None)
    
    # Handle both tuples and NumPy arrays for velocity
    velocity_is_zero = False
    if velocity_km_s is None:
        velocity_is_zero = True
    elif isinstance(velocity_km_s, np.ndarray):
        velocity_is_zero = np.allclose(velocity_km_s, 0)
    elif hasattr(velocity_km_s, '__iter__'):
        velocity_is_zero = all(v == 0 for v in velocity_km_s)
    else:
        velocity_is_zero = True
    
    if velocity_is_zero:
        vx = position_data.get('vx', 0)
        vy = position_data.get('vy', 0)
        vz = position_data.get('vz', 0)
        if vx != 0 or vy != 0 or vz != 0:
            velocity_km_s = (vx, vy, vz)
        else:
            velocity_km_s = (0, 40, 0)
    
    # Determine which features are visible at this distance
    features_visible = {
        'nucleus': True,
        'coma': distance_au <= COMET_FEATURE_THRESHOLDS['coma'],
        'dust_tail': distance_au <= COMET_FEATURE_THRESHOLDS['dust_tail'],
        'ion_tail': distance_au <= COMET_FEATURE_THRESHOLDS['ion_tail']
    }
    
    # Print diagnostic info
    print(f"\n[COMET VIZ] {comet_name} at {distance_au:.2f} AU from Sun")
    print(f"  Nucleus: [OK] Always visible")
    
    if features_visible['coma']:
        print(f"  Coma: [OK] Visible")
    else:
        print(f"  Coma: [FAIL] Too far (needs <{COMET_FEATURE_THRESHOLDS['coma']} AU)")
    
    if features_visible['dust_tail']:
        print(f"  Dust tail: [OK] Visible")
    else:
        print(f"  Dust tail: [FAIL] Too far (needs <{COMET_FEATURE_THRESHOLDS['dust_tail']} AU)")
    
    if features_visible['ion_tail']:
        print(f"  Ion tail: [OK] Visible")
    else:
        print(f"  Ion tail: [FAIL] Too far (needs <{COMET_FEATURE_THRESHOLDS['ion_tail']} AU)")
    
    # If comet is very far, show nucleus + legend entries for missing features
    if distance_au > COMET_FEATURE_THRESHOLDS['coma']:
        nucleus_size = COMET_NUCLEUS_SIZES.get(db_name, COMET_NUCLEUS_SIZES['default'])
        nucleus_traces = create_comet_nucleus(position_au, nucleus_size, comet_name)
        for trace in nucleus_traces:
            fig.add_trace(trace)
        
        # Add invisible legend entries for missing features
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
        
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
        
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
        
        print(f"  [OK] Added nucleus only with legend entries for missing features")
        return fig
    
    # Comet is active - create visualization with available features
    try:
        comet_data = HISTORICAL_TAIL_DATA.get(db_name, HISTORICAL_TAIL_DATA['default'])
        nucleus_size = COMET_NUCLEUS_SIZES.get(db_name, COMET_NUCLEUS_SIZES['default'])
        perihelion_distance = comet_data['perihelion_distance_au']
        activity_factor = calculate_tail_activity_factor(distance_au, perihelion_distance)
        
        traces = []
        
        # 1. Nucleus (always)
        traces.extend(create_comet_nucleus(position_au, nucleus_size, comet_name))
        
        # 2. Coma (if close enough and active)
        if features_visible['coma'] and activity_factor > 0.1:
            coma_size = 50000 + 150000 * activity_factor
            traces.extend(create_comet_coma(position_au, coma_size, activity_factor, comet_name))
        
        # 3. Dust tail(s) (if close enough)
        if features_visible['dust_tail']:
            dust_length = comet_data['max_dust_tail_length_mkm']
            dust_tail_count = comet_data.get('dust_tail_count', 1)
            
            if dust_tail_count <= 1:
                traces.extend(create_comet_dust_tail(
                    position_au, velocity_km_s, dust_length, activity_factor, comet_name
                ))
            else:
                # Multiple dust tails in fan pattern
                fan_half_angle = comet_data.get('dust_tail_fan_angle', 30)
                
                cx, cy, cz = position_au
                sun_dist = math.sqrt(cx**2 + cy**2 + cz**2)
                
                if sun_dist > 1e-10:
                    anti_sun = (cx/sun_dist, cy/sun_dist, cz/sun_dist)
                    
                    # Perpendicular basis for fan spread
                    perp1_x = anti_sun[1]*1 - anti_sun[2]*0
                    perp1_y = anti_sun[2]*0 - anti_sun[0]*1
                    perp1_z = anti_sun[0]*0 - anti_sun[1]*0
                    perp1_mag = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
                    
                    if perp1_mag < 1e-10:
                        perp1_x, perp1_y, perp1_z = 1, 0, 0
                        perp1_mag = 1.0
                    
                    perp1_x /= perp1_mag
                    perp1_y /= perp1_mag
                    perp1_z /= perp1_mag
                    
                    fan_rad = math.radians(fan_half_angle)
                    
                    for t_idx in range(dust_tail_count):
                        if dust_tail_count == 1:
                            angle = 0
                        else:
                            angle = -fan_rad + 2*fan_rad*t_idx/(dust_tail_count - 1)
                        
                        offset_scale = math.tan(angle) * 0.5
                        modified_vel = (
                            velocity_km_s[0] + offset_scale * perp1_x * sun_dist,
                            velocity_km_s[1] + offset_scale * perp1_y * sun_dist,
                            velocity_km_s[2] + offset_scale * perp1_z * sun_dist
                        )
                        
                        center_weight = 1.0 - 0.4 * abs(2.0*t_idx/(dust_tail_count-1) - 1.0)
                        tail_len = dust_length * center_weight
                        num_p = int(800 * center_weight)
                        
                        tail_traces = create_comet_dust_tail(
                            position_au, modified_vel, tail_len,
                            activity_factor, comet_name, num_particles=num_p
                        )
                        
                        if t_idx > 0 and tail_traces:
                            for tr in tail_traces:
                                tr.name = f"{comet_name}: Dust Tail {t_idx + 1}"
                        
                        traces.extend(tail_traces)
                else:
                    # Fallback to single tail if at Sun
                    traces.extend(create_comet_dust_tail(
                        position_au, velocity_km_s, dust_length, activity_factor, comet_name
                    ))
        
        # 4. Ion tail (if close enough)
        if features_visible['ion_tail']:
            ion_length = comet_data['max_ion_tail_length_mkm']
            traces.extend(create_comet_ion_tail(
                position_au, ion_length, activity_factor, comet_name
            ))
        
        # 5. Anti-tail (if comet has anti_tail_length_km defined and is active)
        anti_tail_length = comet_data.get('anti_tail_length_km', 0)
        if anti_tail_length > 0 and features_visible['coma']:
            anti_tail_color = comet_data.get('anti_tail_color', '#C0C0C8')
            anti_tail_collimation = comet_data.get('anti_tail_collimation', 0.1)
            traces.extend(create_comet_anti_tail(
                position_au, anti_tail_length, activity_factor,
                comet_name, anti_tail_color, anti_tail_collimation
            ))
        
        # 6. Sun direction indicator (if any tail is visible)
        if features_visible['dust_tail'] or features_visible['ion_tail']:
            max_tail = max(
                comet_data['max_dust_tail_length_mkm'] if features_visible['dust_tail'] else 0,
                comet_data['max_ion_tail_length_mkm'] if features_visible['ion_tail'] else 0
            )
            max_tail_au = max_tail * 1e6 / KM_PER_AU
            sun_traces = create_sun_direction_indicator(position_au, max_tail_au * activity_factor)
            traces.extend(sun_traces)
        
        # Add all traces to figure
        for trace in traces:
            fig.add_trace(trace)
        
        # Add invisible legend entries for missing features
        if not features_visible['coma']:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
        
        if not features_visible['dust_tail']:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
        
        if not features_visible['ion_tail']:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
        
        print(f"  [OK] Activity factor: {activity_factor:.1%}")
        print(f"  [OK] Added {len(traces)} visualization traces")
        
    except Exception as e:
        print(f"  [FAIL] Error creating comet visualization: {e}")
        import traceback
        traceback.print_exc()
    
    return fig


# Example usage and testing
if __name__ == "__main__":
    print("Comet Visualization System")
    print("=" * 50)
    print("\nAvailable comets:")
    for name in HISTORICAL_TAIL_DATA.keys():
        data = HISTORICAL_TAIL_DATA[name]
        print(f"\n{name}:")
        print(f"  Perihelion: {data['perihelion_distance_au']:.3f} AU")
        print(f"  Peak magnitude: {data['peak_brightness_mag']:.1f}")
        print(f"  Max dust tail: {data['max_dust_tail_length_mkm']:.0f} million km")
        print(f"  Max ion tail: {data['max_ion_tail_length_mkm']:.0f} million km")
    
    print("\n" + "=" * 50)
    print("\nActivity factor examples:")
    print("(How active the comet is at different solar distances)")
    
    for comet in ['Halley', 'Ikeya-Seki', 'Hale-Bopp']:
        perihelion = HISTORICAL_TAIL_DATA[comet]['perihelion_distance_au']
        print(f"\n{comet} (perihelion at {perihelion:.3f} AU):")
        for distance in [0.5, 1.0, 2.0, 3.0, 4.0]:
            activity = calculate_tail_activity_factor(distance, perihelion)
            print(f"  At {distance:.1f} AU: {activity:.1%} activity")
