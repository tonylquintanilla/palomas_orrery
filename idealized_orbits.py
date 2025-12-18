# idealized_orbits.py

import numpy as np
import math
import plotly.graph_objs as go
import traceback  # Add this import
from datetime import datetime, timedelta
from osculating_cache_manager import get_elements_with_prompt
from constants_new import color_map, KNOWN_ORBITAL_PERIODS
from orbital_elements import planetary_params as ORIGINAL_planetary_params
from apsidal_markers import (
    add_perihelion_marker,
    add_apohelion_marker,
    add_actual_apsidal_markers,
    fetch_positions_for_apsidal_dates,
    estimate_hyperbolic_perihelion_date,  # NEW
    compute_apsidal_dates_from_tp,  # NEW 
    add_apsidal_range_note, 
    add_actual_apsidal_markers_enhanced,  # Add this
    calculate_orbital_angle_shift,  # Add this
    create_enhanced_apsidal_hover_text,  # Add this
)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Import orbital element dictionaries from standalone module (no dependencies)
from orbital_elements import planetary_params, parent_planets, planet_tilts

# Dictionary of planet pole directions (J2000)
planet_poles = {
    'Mars': {'ra': 317.68, 'dec': 52.89},
    'Jupiter': {'ra': 268.05, 'dec': 64.49},
    'Saturn': {'ra': 40.58, 'dec': 83.54},
    'Uranus': {'ra': 257.43, 'dec': -15.10},
    'Neptune': {'ra': 299.36, 'dec': 43.46},
    'Pluto': {'ra': 132.99, 'dec': -6.16}
}

import numpy as np
from datetime import datetime, timedelta

JUPITER_MOONS = ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 
                 'Io', 'Europa', 'Ganymede', 'Callisto']

# Saturn moons for osculating-only dual orbit system
# Note: Phoebe included - has special Laplace plane transformation in plot_saturn_moon_osculating_orbit()
SATURN_MOONS = ['Pan', 'Daphnis', 'Prometheus', 'Pandora', 'Mimas', 'Enceladus', 
                'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 'Iapetus', 'Phoebe']

URANUS_MOONS = ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Portia', 'Mab'] 

# Neptune moons for osculating-only dual orbit system
# Note: Triton is retrograde (i~157°), Nereid highly eccentric (e~0.75) - both work with standard Keplerian
NEPTUNE_MOONS = ['Triton', 'Nereid', 'Naiad', 'Thalassa', 'Despina', 'Galatea', 'Larissa', 'Proteus']

# Pluto moons - osculating-only display (pole RA=132.99° far from ecliptic ~270°)
# Note: When "Pluto-Charon Barycenter" is center, Charon and Pluto both orbit the barycenter
PLUTO_MOONS = ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']

# For barycenter mode: objects that orbit the Pluto system barycenter
PLUTO_BARYCENTER_ORBITERS = ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']

# TNO (Trans-Neptunian Object) satellite systems - osculating only
# These use JPL satellite ephemeris solutions (not small body solutions)
ERIS_MOONS = ['Dysnomia']
HAUMEA_MOONS = ["Hi'iaka", 'Namaka']
MAKEMAKE_MOONS = ['MK2']
TNO_MOONS = ERIS_MOONS + HAUMEA_MOONS + MAKEMAKE_MOONS

def get_planet_perturbation_note(obj_name, orbit_source="Keplerian"):
    """
    Get appropriate perturbation note for planet's Keplerian orbit hover text.
    
    Parameters:
        obj_name (str): Name of the planet/object
        orbit_source (str): Either "Keplerian" or "osculating"
    
    Returns:
        str: HTML-formatted perturbation note
    """
    if orbit_source == "osculating":
        # For osculating orbits - generic perturbation note
        return (
            "<br><br><i>Osculating orbit 'kisses' actual position at epoch,<br>"
            "then diverges as perturbations accumulate from:<br>"
            "• Gravitational tugs from other planets<br>"
            "• Solar oblateness (equatorial bulge effect)<br>"
            "<br>It fits only the present position, not past or future positions.</i>"
        )
    
    # For Keplerian orbits - planet-specific perturbations
    perturbation_notes = {
        'Mercury': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Venus and Jupiter gravitational tugs<br>"
            "• Relativistic precession (+43″/century)<br>"
            "  - Einstein's General Relativity effect<br>"
            "• High eccentricity amplifies perturbations</i>"
        ),
        'Venus': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Earth and Jupiter gravitational tugs<br>"
            "• Nearly circular orbit (e ≈ 0.007)<br>"
            "• Most stable inner planet orbit</i>"
        ),
        'Earth': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Moon's gravitational influence<br>"
            "• Jupiter and Venus gravitational tugs<br>"
            "• Axial precession (25,772 year cycle)</i>"
        ),
        'Mars': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Jupiter gravitational tugs (largest)<br>"
            "• Earth and Venus effects<br>"
            "• Eccentricity varies 0.000-0.140 over ~2 Myr</i>"
        ),
        'Jupiter': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Saturn gravitational interaction<br>"
            "• Great Inequality (900-year cycle)<br>"
            "• Dominates inner solar system dynamics</i>"
        ),
        'Saturn': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Jupiter gravitational interaction<br>"
            "• Great Inequality (900-year cycle)<br>"
            "• 5:2 resonance with Jupiter</i>"
        ),
        'Uranus': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Jupiter and Saturn gravitational tugs<br>"
            "• Neptune interaction<br>"
            "• Extreme axial tilt (98°)</i>"
        ),
        'Neptune': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Jupiter and Saturn gravitational tugs<br>"
            "• Uranus interaction<br>"
            "• 3:2 resonance captures Pluto</i>"
        ),
        'Pluto': (
            "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
            "Major perturbations from:<br>"
            "• Neptune 3:2 mean motion resonance<br>"
            "• High eccentricity (e ≈ 0.25)<br>"
            "• High inclination (i ≈ 17°)</i>"
        ),
    }
    
    # Default for other objects (asteroids, comets, etc.)
    default_note = (
        "<br><br><i>Keplerian orbit uses averaged orbital elements.<br>"
        "Subject to gravitational perturbations from planets.</i>"
    )
    
    return perturbation_notes.get(obj_name, default_note)

# this function adjusts the orbital elements for phobos and deimos based on perturbations
def calculate_mars_satellite_elements(date, satellite_name):
    """
    Calculate time-varying orbital elements for Mars satellites
    Similar to your Moon implementation but with Mars-specific perturbations
    """
    # Calculate days since revision date of ephemeris for Phobos and Deimos
    base_epoch = datetime(2025, 6, 2, 0, 0, 0)

    # Calculate days since the base epoch (NOT J2000!)
    d = (date - base_epoch).days
    
    # Base elements
    if satellite_name == 'Phobos':
        a_base = 0.000062682  # AU
        e_base = 0.0151
        i_base = 1.082
        omega_base = 216.3
        Omega_base = 169.2
        
        # Mars equatorial bulge-induced precession rates (much faster than Moon)
        omega_rate = 27.0 / 365.25  # degrees/day (apsidal precession)
        Omega_rate = -158.0 / 365.25  # degrees/day (node regression)
        
        # Tidal acceleration (Phobos spiraling inward)
        # Semi-major axis decreases by ~1.8 cm/year
        a_secular = -1.8e-5 / 149597870.7 / 365.25 * d  # AU change
        
    elif satellite_name == 'Deimos':
        a_base = 0.0001568
        e_base = 0.00033
        i_base = 1.791
        omega_base = 0.0
        Omega_base = 54.4
        
        # Slower precession rates for more distant Deimos
        omega_rate = 0.84 / 365.25  # degrees/day
        Omega_rate = -7.6 / 365.25  # degrees/day
        
        # Minimal tidal effects
        a_secular = 0
    
    # Apply secular changes
    omega = (omega_base + omega_rate * d) % 360.0
    Omega = (Omega_base + Omega_rate * d) % 360.0
    a = a_base + a_secular
    
    # Could add periodic perturbations like you do for Moon
    # Solar perturbations, Mars librations, etc.
    
    return {
        'a': a,
        'e': e_base,  # Could add eccentricity variations
        'i': i_base,  # Could add inclination oscillations
        'omega': omega,
        'Omega': Omega
    }
    

def calculate_jupiter_satellite_elements(date, satellite_name):
    """
    Calculate time-varying orbital elements for Jupiter satellites.
    
    Base elements are in Jupiter equatorial frame.
    Follows same pattern as Mars satellites.
    
    Parameters:
        date: datetime object for calculation epoch
        satellite_name: Name of Jupiter moon
        
    Returns:
        dict: Orbital elements with time-varying Ω and ω
    """
    from datetime import datetime
    
    base_epoch = datetime(2025, 11, 22, 0, 0, 0)
    d = (date - base_epoch).days
    
    # Base elements in Jupiter equatorial frame
    if satellite_name == 'Io':
        a_base, e_base, i_base = 0.002819, 0.0041, 0.05
        omega_base, Omega_base = 49.1, 0.0
    elif satellite_name == 'Europa':
        a_base, e_base, i_base = 0.004486, 0.0094, 0.47
        omega_base, Omega_base = 85.2, 0.0
    elif satellite_name == 'Ganymede':
        a_base, e_base, i_base = 0.007155, 0.0013, 0.18
        omega_base, Omega_base = 192.4, 0.0
    elif satellite_name == 'Callisto':
        a_base, e_base, i_base = 0.012585, 0.0074, 0.19
        omega_base, Omega_base = 52.6, 0.0
    elif satellite_name == 'Metis':
        a_base, e_base, i_base = 0.000856, 0.0002, 0.06
        omega_base, Omega_base = 0.0, 0.0
    elif satellite_name == 'Adrastea':
        a_base, e_base, i_base = 0.000864, 0.0015, 0.03
        omega_base, Omega_base = 0.0, 0.0
    elif satellite_name == 'Amalthea':
        a_base, e_base, i_base = 0.001217, 0.0032, 0.37
        omega_base, Omega_base = 0.0, 0.0
    elif satellite_name == 'Thebe':
        a_base, e_base, i_base = 0.001486, 0.0175, 1.08
        omega_base, Omega_base = 0.0, 0.0
    else:
        print(f"Warning: No base elements defined for {satellite_name}", flush=True)
        return None
    
    # Precession rates (placeholders - can be refined later)
    omega_rate = 0.0 / 365.25
    Omega_rate = 0.0 / 365.25
    
    omega = (omega_base + omega_rate * d) % 360.0
    Omega = (Omega_base + Omega_rate * d) % 360.0
    
    return {'a': a_base, 'e': e_base, 'i': i_base, 'omega': omega, 'Omega': Omega}

def calculate_saturn_satellite_elements(date, satellite_name):
    """
    Calculate time-varying orbital elements for Saturn satellites.
    
    Base elements are in Saturn equatorial frame.
    Follows same pattern as Jupiter satellites.
    """
    from datetime import datetime
    
    base_epoch = datetime(2025, 11, 23, 0, 0, 0)
    d = (date - base_epoch).days
    
    # Base elements from orbital_elements.py (JPL Horizons derived)
    if satellite_name == 'Mimas':
        a_base, e_base, i_base = 0.001242, 0.0196, 1.572
        omega_base, Omega_base = 160.4, 66.2
    elif satellite_name == 'Enceladus':
        a_base, e_base, i_base = 0.001587, 0.0047, 0.009
        omega_base, Omega_base = 119.5, 0.0
    elif satellite_name == 'Tethys':
        a_base, e_base, i_base = 0.001970, 0.001, 1.091
        omega_base, Omega_base = 335.3, 273.0
    elif satellite_name == 'Dione':
        a_base, e_base, i_base = 0.002525, 0.0022, 0.0
        omega_base, Omega_base = 116.0, 0.0
    elif satellite_name == 'Rhea':
        a_base, e_base, i_base = 0.003524, 0.0010, 0.333
        omega_base, Omega_base = 44.3, 133.7
    elif satellite_name == 'Titan':
        a_base, e_base, i_base = 0.008168, 0.0288, 0.306
        omega_base, Omega_base = 78.3, 78.6
    elif satellite_name == 'Hyperion':
        a_base, e_base, i_base = 0.010033, 0.0232, 0.615
        omega_base, Omega_base = 214.0, 87.1
    elif satellite_name == 'Iapetus':
        a_base, e_base, i_base = 0.02380, 0.0283, 7.489
        omega_base, Omega_base = 254.5, 86.5
    else:
        print(f"Warning: No base elements defined for {satellite_name}", flush=True)
        return None
    
    omega_rate = 0.0 / 365.25
    Omega_rate = 0.0 / 365.25
    
    omega = (omega_base + omega_rate * d) % 360.0
    Omega = (Omega_base + Omega_rate * d) % 360.0
    
    return {'a': a_base, 'e': e_base, 'i': i_base, 'omega': omega, 'Omega': Omega}


def test_mars_rotations(satellite_name, planetary_params, color, fig=None):     # test function only
    """Test multiple rotation combinations to find the best alignment"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Test several different rotation combinations
        rotations = [
            {"name": "Basic", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, "extra": None},
            {"name": "Mars Tilt +", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'x', "angle": np.radians(25.19)}},
            {"name": "Mars Tilt -", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'x', "angle": np.radians(-25.19)}},
            {"name": "Mars Y", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'y', "angle": np.radians(35.4)}},
            {"name": "Mars Z", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": {"axis": 'z', "angle": np.radians(49.58)}},
            {"name": "Y+Z", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": [{"axis": 'y', "angle": np.radians(35.4)}, 
                     {"axis": 'z', "angle": np.radians(49.58)}]},
            {"name": "Z+X", "z1": Omega_rad, "x": i_rad, "z2": omega_rad, 
             "extra": [{"axis": 'z', "angle": np.radians(49.58)}, 
                     {"axis": 'x', "angle": np.radians(25.19)}]},
        ]
        
        # Define line styles for each rotation
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "longdashdotdot"]
        
        # Apply each rotation combination
        for idx, rot in enumerate(rotations):
            # Apply standard orbital element rotations
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, rot["z1"], 'z')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, rot["x"], 'x')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, rot["z2"], 'z')
            
            # Apply extra rotations if specified
            if rot["extra"]:
                if isinstance(rot["extra"], list):
                    # Apply multiple extra rotations
                    for extra_rot in rot["extra"]:
                        x_temp, y_temp, z_temp = rotate_points(
                            x_temp, y_temp, z_temp, 
                            extra_rot["angle"], extra_rot["axis"]
                        )
                else:
                    # Apply single extra rotation
                    x_temp, y_temp, z_temp = rotate_points(
                        x_temp, y_temp, z_temp, 
                        rot["extra"]["angle"], rot["extra"]["axis"]
                    )
            
            # Add trace to figure
            line_style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_temp,
                    y=y_temp,
                    z=z_temp,
                    mode='lines',
                    line=dict(dash=line_style, width=1, color=color),
                    name=f"{satellite_name} {rot['name']}",
                    text=[f"{satellite_name} {rot['name']} Rotation"] * len(x_temp),
                    customdata=[f"{satellite_name} {rot['name']} Rotation"] * len(x_temp),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
    
    except Exception as e:
        print(f"Error testing Mars rotations for {satellite_name}: {e}", flush=True)
        return fig

def test_uranus_equatorial_transformations(satellite_name, planetary_params, color, fig=None):
    """Test transformations assuming orbital elements are in Uranus's equatorial plane"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard orbital element rotation sequence - this gives us the orbit in Uranus's equatorial plane
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Now transform from Uranus's equatorial frame to ecliptic frame
        # Get Uranus's pole orientation
        uranus_pole = planet_poles['Uranus']
        ra_pole = np.radians(uranus_pole['ra'])
        dec_pole = np.radians(uranus_pole['dec'])
        
        # Calculate pole vector
        sin_dec = np.sin(dec_pole)
        cos_dec = np.cos(dec_pole)
        sin_ra = np.sin(ra_pole)
        cos_ra = np.cos(ra_pole)
        
        # Pole vector
        x_pole = cos_dec * cos_ra
        y_pole = cos_dec * sin_ra
        z_pole = sin_dec
        
        # Normalize the pole vector
        pole_norm = np.sqrt(x_pole**2 + y_pole**2 + z_pole**2)
        x_pole /= pole_norm
        y_pole /= pole_norm
        z_pole /= pole_norm
        
        print(f"Uranus pole vector: [{x_pole:.4f}, {y_pole:.4f}, {z_pole:.4f}]", flush=True)
        
        # Transform from equatorial to ecliptic
        # Step 1: First rotation to get the pole's projection onto the XY plane aligned with the X-axis
        phi = np.arctan2(y_pole, x_pole)
        x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, -phi, 'z')  # Note the negative sign
        
        # Step 2: Second rotation to align the pole with the Z-axis
        theta = np.arccos(z_pole)
        x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, -theta, 'y')  # Note the negative sign
        
        # Step 3: Third rotation to fix the orientation
        x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, phi, 'z')
        
        # Add trace to figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='solid', width=2, color=color),
                name=f"{satellite_name} Equatorial Transform",
                text=[f"{satellite_name} Equatorial Transform"] * len(x_final),
                customdata=[f"{satellite_name} Equatorial Transform"] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_uranus_equatorial_transformations: {e}", flush=True)
        traceback.print_exc()
        return fig

def test_uranus_rotation_combinations(satellite_name, planetary_params, color, fig=None):
    """Test multiple rotation combinations for Uranus satellites systematically"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot"]
        
        # Uranus's axial tilt value
        tilt = planet_tilts['Uranus']  # 97.77 degrees
        tilt_rad = np.radians(tilt)
        neg_tilt_rad = np.radians(-tilt)
        
        # Test combinations
        combinations = [
            {"name": "X+", "axis": 'x', "angle": tilt_rad},
            {"name": "X-", "axis": 'x', "angle": neg_tilt_rad},
            {"name": "Y+", "axis": 'y', "angle": tilt_rad},
            {"name": "Y-", "axis": 'y', "angle": neg_tilt_rad},
            {"name": "Z+", "axis": 'z', "angle": tilt_rad},
            {"name": "Z-", "axis": 'z', "angle": neg_tilt_rad},
            # Try some composite rotations
            {"name": "X+Y+", "rotations": [
                {"axis": 'x', "angle": tilt_rad},
                {"axis": 'y', "angle": tilt_rad}
            ]},
            {"name": "X+Z+", "rotations": [
                {"axis": 'x', "angle": tilt_rad},
                {"axis": 'z', "angle": tilt_rad}
            ]},
            {"name": "90X", "axis": 'x', "angle": np.radians(90)},
            {"name": "90Y", "axis": 'y', "angle": np.radians(90)}
        ]
        
        # Plot each combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            if "rotations" in combo:
                # Apply multiple rotations in sequence
                for rot in combo["rotations"]:
                    x_rotated, y_rotated, z_rotated = rotate_points(
                        x_rotated, y_rotated, z_rotated, 
                        rot["angle"], rot["axis"]
                    )
            else:
                # Apply single rotation
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    combo["angle"], combo["axis"]
                )
            
            # Add trace to figure
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_uranus_rotation_combinations: {e}", flush=True)
        traceback.print_exc()
        return fig

def debug_planet_transformation(planet_name):
    """Print detailed information about the transformation for a specific planet"""
    print(f"\n==== DEBUG: {planet_name} Transformation ====", flush=True)
    
    # Get the planet's axial tilt
    tilt = planet_tilts.get(planet_name, 0)
    print(f"Axial tilt: {tilt} degrees", flush=True)
    
    # Simple tilt matrix
    tilt_rad = np.radians(tilt)
    simple_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(tilt_rad), -np.sin(tilt_rad)],
        [0, np.sin(tilt_rad), np.cos(tilt_rad)]
    ])
    print("\nSimple tilt matrix:", flush=True)
    print(simple_matrix, flush=True)
    
    # If we have pole data, calculate the complex matrix
    if planet_name in planet_poles:
        pole = planet_poles[planet_name]
        ra_pole = np.radians(pole['ra'])
        dec_pole = np.radians(pole['dec'])
        
        print(f"\nPole direction: RA = {pole['ra']}°, Dec = {pole['dec']}°", flush=True)
        
        # Calculate pole vector
        sin_dec = np.sin(dec_pole)
        cos_dec = np.cos(dec_pole)
        sin_ra = np.sin(ra_pole)
        cos_ra = np.cos(ra_pole)
        
        x_pole = cos_dec * cos_ra
        y_pole = cos_dec * sin_ra
        z_pole = sin_dec
        
        print(f"Pole vector: [{x_pole:.4f}, {y_pole:.4f}, {z_pole:.4f}]", flush=True)
        
        # Calculate node vector
        node_denom = np.sqrt(x_pole**2 + y_pole**2)
        if node_denom > 0:
            x_node = -y_pole / node_denom
            y_node = x_pole / node_denom
            z_node = 0
            
            print(f"Node vector: [{x_node:.4f}, {y_node:.4f}, {z_node:.4f}]", flush=True)
            
            # Create basis vectors
            z_basis = np.array([x_pole, y_pole, z_pole])
            x_basis = np.array([x_node, y_node, z_node])
            y_basis = np.cross(z_basis, x_basis)
            
            print(f"X basis: [{x_basis[0]:.4f}, {x_basis[1]:.4f}, {x_basis[2]:.4f}]", flush=True)
            print(f"Y basis: [{y_basis[0]:.4f}, {y_basis[1]:.4f}, {y_basis[2]:.4f}]", flush=True)
            print(f"Z basis: [{z_basis[0]:.4f}, {z_basis[1]:.4f}, {z_basis[2]:.4f}]", flush=True)
            
            # Construct transformation matrix
            complex_matrix = np.vstack((x_basis, y_basis, z_basis)).T
            print("\nComplex transformation matrix:", flush=True)
            print(complex_matrix, flush=True)
            
            # Calculate the angle between simple and complex transformations
            # by comparing the transformed z-axis
            z_axis = np.array([0, 0, 1])
            simple_z = np.dot(simple_matrix, z_axis)
            complex_z = np.dot(complex_matrix, z_axis)
            
            dot_product = np.dot(simple_z, complex_z)
            angle = np.arccos(min(1, max(-1, dot_product))) * 180 / np.pi
            
            print(f"\nAngle between simple and complex transformations: {angle:.2f}°", flush=True)
        else:
            print("Cannot calculate node vector (pole is directly aligned with Z-axis)", flush=True)

def debug_mars_moons(satellites_data, parent_planets):          # test function only
    """Special debug function for Mars and its moons"""
    print("\n==== MARS SYSTEM DEBUG ====", flush=True)
    
    # Print Mars' axial tilt and pole direction
    debug_planet_transformation('Mars')
    
    # Print orbital elements for Mars' moons
    mars_moons = parent_planets.get('Mars', [])
    for moon in mars_moons:
        if moon in satellites_data:
            params = satellites_data[moon]
            print(f"\n{moon} orbital elements:", flush=True)
            for key, value in params.items():
                print(f"  {key}: {value}")
    
    # Test if the moons' inclinations are relative to:
    # 1. Mars' equator
    # 2. Mars' orbital plane
    # 3. The ecliptic
    print("\nInclination references analysis:", flush=True)
    
    # Mars' axial tilt to the ecliptic
    mars_tilt = np.radians(planet_tilts['Mars'])
    
    for moon in mars_moons:
        if moon in satellites_data:
            params = satellites_data[moon]
            i = params.get('i', 0)
            i_rad = np.radians(i)
            
            # If inclination is relative to Mars' equator,
            # then the true inclination to the ecliptic would be:
            i_to_ecliptic = np.arccos(np.cos(i_rad) * np.cos(mars_tilt) - 
                                       np.sin(i_rad) * np.sin(mars_tilt)) * 180/np.pi
            
            # If inclination is relative to the ecliptic,
            # then the true inclination to Mars' equator would be:
            i_to_equator = np.arccos(np.cos(i_rad) * np.cos(mars_tilt) + 
                                      np.sin(i_rad) * np.sin(mars_tilt)) * 180/np.pi
            
            print(f"\n{moon}:", flush=True)
            print(f"  Stated inclination: {i}°", flush=True)
            print(f"  If relative to Mars' equator, inclination to ecliptic would be ~{i_to_ecliptic:.2f}°", flush=True)
            print(f"  If relative to ecliptic, inclination to Mars' equator would be ~{i_to_equator:.2f}°", flush=True)

def compare_transformation_methods(fig, satellites_data, parent_planets):       # test function only
    """Plot orbits with different transformation methods for comparison"""
    
    # Plot Mars moons with all transformation methods
    for moon in parent_planets.get('Mars', []):
        if moon in satellites_data:
            for method in ["none", "simple", "complex"]:
                plot_satellite_orbit(
                    moon, 
                    satellites_data[moon],
                    'Mars',
                    color_map('Mars'),  # Call the function with planet name
                    fig,
                    debug=True,
                    transform_method=method
                )
    
    # Plot Jupiter moons with all transformation methods
    for moon in ['Io', 'Europa', 'Ganymede', 'Callisto']:  # Just the main moons
        if moon in satellites_data:
            for method in ["none", "simple", "complex"]:
                plot_satellite_orbit(
                    moon, 
                    satellites_data[moon],
                    'Jupiter',
                    color_map('Jupiter'),  # Changed brackets [] to parentheses ()
                    fig,
                    debug=True,
                    transform_method=method
                )
    
    return fig

def test_mars_negative_tilt(fig, satellites_data):          # test function only
    """Test hypothesis that Mars needs a negative tilt application"""
    
    # Mars moons
    for moon in ['Phobos', 'Deimos']:
        if moon in satellites_data:
            # Extract orbital elements
            params = satellites_data[moon]
            a = params.get('a', 0)
            e = params.get('e', 0)
            i = params.get('i', 0)
            omega = params.get('omega', 0)
            Omega = params.get('Omega', 0)
            
            # Standard orbital transformation
            theta = np.linspace(0, 2*np.pi, 360)
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            
            x_orbit = r * np.cos(theta)
            y_orbit = r * np.sin(theta)
            z_orbit = np.zeros_like(theta)
            
            i_rad = np.radians(i)
            omega_rad = np.radians(omega)
            Omega_rad = np.radians(Omega)
            
            # Standard rotation sequence
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
            
            # Try NEGATIVE tilt for Mars
            tilt_rad = np.radians(-planet_tilts['Mars'])
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
            
            # Add to figure
            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='solid', width=2, color='purple'),
                    name=f"{moon} (Negative Tilt Test)",
                    text=[f"{moon} with negative tilt test"] * len(x_final),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
    
    return fig

def debug_satellite_systems():
    fig = go.Figure()
    
    # Print transformation matrices
    debug_planet_transformation('Mars')
    debug_planet_transformation('Jupiter')
    
    # Special debug for Mars
    debug_mars_moons(planetary_params, parent_planets)
    
    # Compare transformation methods
    fig = compare_transformation_methods(fig, planetary_params, parent_planets)
    
    # Test negative tilt for Mars
    fig = test_mars_negative_tilt(fig, planetary_params)
    
    # Configure the layout
    fig.update_layout(
        title="Satellite System Transformation Debug",
        scene=dict(
            aspectmode='data'
        )
    )
    
    fig.show()

def rotate_points(x, y, z, angle, axis='z'):
    """
    Rotates points (x,y,z) about the given axis by 'angle' radians.
    Returns (xr, yr, zr) as numpy arrays.
    
    Parameters:
        x (array-like): x coordinates
        y (array-like): y coordinates
        z (array-like): z coordinates
        angle (float): rotation angle in radians
        axis (str): axis of rotation ('x', 'y', or 'z')
        
    Returns:
        tuple: (xr, yr, zr) rotated coordinates
    """
    # Convert inputs to numpy arrays if they aren't already
    x = np.array(x, copy=True)
    y = np.array(y, copy=True)
    z = np.array(z, copy=True)

    # Initialize rotated coordinates
    xr = x.copy()
    yr = y.copy()
    zr = z.copy()

    # Perform rotation based on specified axis
    if axis == 'z':
        # Rotate about z-axis
        xr = x * np.cos(angle) - y * np.sin(angle)
        yr = x * np.sin(angle) + y * np.cos(angle)
        # zr remains the same
    elif axis == 'x':
        # Rotate about x-axis
        yr = y * np.cos(angle) - z * np.sin(angle)
        zr = y * np.sin(angle) + z * np.cos(angle)
        # xr remains the same
    elif axis == 'y':
        # Rotate about y-axis
        zr = z * np.cos(angle) - x * np.sin(angle)
        xr = z * np.sin(angle) + x * np.cos(angle)
        # yr remains the same
    else:
        raise ValueError(f"Unknown rotation axis: {axis}. Use 'x', 'y', or 'z'.")

    return xr, yr, zr

def plot_jupiter_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for Jupiter satellites.
    
    CRITICAL: Jupiter moon osculating elements are in ECLIPTIC frame (J2000.0)
    This is DIFFERENT from analytical elements which are in Jupiter equatorial frame.
    
    Pattern follows Mars moons:
    - Analytical: Parent equatorial → ecliptic (needs rotation)
    - Osculating: Already in ecliptic (NO rotation!)
    
    Special case: Thebe shows anomalous behavior (i_osc ≈ i_analytical)
    
    Parameters:
        fig: Plotly figure to add trace to
        satellite_name: Name of Jupiter moon ('Io', 'Europa', etc.)
        date: Date for osculating elements
        color: Orbit color
        show_apsidal_markers: Whether to show apsides (not implemented yet)
        
    Returns:
        Updated figure with osculating orbit trace
    """
    # Jupiter moon Horizons IDs
    JUPITER_MOON_IDS = {
        'Metis': '516',
        'Adrastea': '515',
        'Amalthea': '505',
        'Thebe': '514',
        'Io': '501',
        'Europa': '502',
        'Ganymede': '503',
        'Callisto': '504'
    }
    
    horizons_id = JUPITER_MOON_IDS.get(satellite_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {satellite_name}", flush=True)
        return fig
    
    try:
        # Load from cache (pre-fetch already prompted user, so just use cache)
        # This matches Mars moons pattern - don't fetch again!
        from osculating_cache_manager import load_cache
        
        print(f"\n[OSCULATING] Loading cached elements for {satellite_name}...", flush=True)
        
        cache = load_cache()
        
        # Check if we have cached elements
        if satellite_name in cache:
            elements = cache[satellite_name]['elements']
            epoch = elements.get('epoch', f"{date.strftime('%Y-%m-%d')}")
            print(f"  ✓ Using cached osculating elements (epoch: {epoch})", flush=True)
        elif satellite_name in planetary_params:
            # Fallback to hardcoded analytical elements
            elements = planetary_params[satellite_name]
            epoch = 'analytical'
            print(f"  ⚠ Using fallback analytical elements from planetary_params", flush=True)
        else:
            print(f"  ⚠ No elements available for {satellite_name}, skipping orbit plot", flush=True)
            return fig

        # Extract elements
        a = elements.get('a', 0)  # AU
        e = elements.get('e', 0)
        i = elements.get('i', 0)  # degrees - ECLIPTIC FRAME!
        omega = elements.get('omega', 0)  # degrees
        Omega = elements.get('Omega', 0)  # degrees
        epoch = elements.get('epoch', 'unknown')
       
        print(f"\nPlotting osculating orbit for {satellite_name}", flush=True)
        print(f"  Inclination: {i:.4f}° (ecliptic frame)", flush=True)
        print(f"  Epoch: {epoch}", flush=True)
        
        # Generate orbit points
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        # Convert to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # CRITICAL: Osculating elements rotation sequence
        # Different from analytical! (ω, i, Ω vs Ω, i, ω)
        # This is the "inside-out" sequence
        
        # 1. Argument of periapsis (ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        
        # 2. Inclination (i) around x-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        
        # 3. Longitude of ascending node (Ω) around z-axis
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # CRITICAL: NO Jupiter rotation!
        # Osculating elements already in ecliptic frame
        # (Except possibly Thebe - see special handling below)
        
        # Special case for Thebe (anomalous behavior)
        if satellite_name == 'Thebe':
            # Thebe's osculating i ≈ 1.18° suggests Jupiter equatorial frame
            # Apply Jupiter rotation like analytical orbit
            jupiter_tilt = np.radians(3.13)
            # x_final, y_final, z_final = rotate_points(x_final, y_final, z_final, jupiter_tilt, 'y')
            # Commented out for now - test both ways
            print(f"  Note: Thebe shows anomalous reference frame behavior", flush=True)
        
        # Create educational hover text
        osculating_note = (
            "<br><br><i>Osculating orbit uses instantaneous elements<br>"
            "from JPL Horizons at specific epoch.<br>"
            "Shows exact orbital state at epoch time.<br>"
            "<br>Incorporates all physical effects:<br>"
            "• Jupiter equatorial bulge gravitational field (largest effect)<br>"
            "• Solar perturbations<br>"
            "• Other Galilean moon perturbations<br>"
            "• Tidal effects<br>"
            "<br>Reference frame: Ecliptic J2000.0<br>"
            "No Jupiter rotation applied</i>"
        )
        
        hover_text_osc = (
            f"<b>{satellite_name} Osculating Orbit</b><br>"
            f"JPL Horizons snapshot<br>"
            f"Epoch: {epoch}<br>"
            f"a={a:.6f} AU<br>"
            f"e={e:.6f}<br>"
            f"i={i:.4f}° (ecliptic)"
            f"{osculating_note}"
        )
        
        # Add dashed line to plot
        fig.add_trace(go.Scatter3d(
            x=x_final,
            y=y_final,
            z=z_final,
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f'{satellite_name} Osculating Orbit (Epoch: {epoch})',
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
        print(f"  ✓ Osculating orbit plotted (ecliptic frame, no Jupiter rotation)", flush=True)
        
        return fig
        
    except Exception as e:
        print(f"Error plotting osculating orbit for {satellite_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig


def plot_saturn_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for Saturn satellites.
    
    CRITICAL: Saturn moon osculating elements are in ECLIPTIC frame (J2000.0)
    This is DIFFERENT from analytical elements which are in Saturn equatorial frame.
    NO Saturn rotation applied to osculating orbits!
    """
    
    SATURN_MOON_IDS = {
        'Pan': '618',
        'Daphnis': '635',
        'Prometheus': '616',
        'Pandora': '617',
        'Mimas': '601',
        'Enceladus': '602',
        'Tethys': '603',
        'Dione': '604',
        'Rhea': '605',
        'Titan': '606',
        'Hyperion': '607',
        'Iapetus': '608',
        'Phoebe': '609'  # Retrograde irregular - has special Laplace plane transformation
    }

    horizons_id = SATURN_MOON_IDS.get(satellite_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {satellite_name}", flush=True)
        return fig
    
    try:
        from osculating_cache_manager import load_cache
        
        print(f"\n[OSCULATING] Loading cached elements for {satellite_name}...", flush=True)
        cache = load_cache()
        
        if satellite_name in cache:
            elements = cache[satellite_name]['elements']
            print(f"  ✓ Using cached osculating elements", flush=True)
        elif satellite_name == 'Daphnis':
            # Daphnis special case - no ephemeris after 2018-01-17
            print(f"  ⚠ Daphnis: JPL ephemeris ends 2018-01-17 (Cassini mission end)", flush=True)
            print(f"  ⚠ No current osculating elements available", flush=True)
            
            # Add informational marker at approximate Keeler Gap location
            daphnis_a = 0.0009124  # Approximate semi-major axis in AU
            
            # Create informational hover text
            daphnis_info = (
                f"<b>Daphnis (S/2005 S1)</b><br>"
                f"Keeler Gap moon - ~8 km diameter<br>"
                f"a ≈ 136,500 km (0.000912 AU)<br>"
                f"Period: ~0.594 days<br>"
                f"<br><i>⚠ JPL ephemeris limited to 2018-01-17<br>"
                f"(Cassini mission end). Current orbital<br>"
                f"elements unavailable. Discovered 2005.</i>"
            )
            
            # Add a single point marker at approximate location (not a full orbit)
            # This is informational only - shows where Daphnis should be
            fig.add_trace(go.Scatter3d(
                x=[daphnis_a], y=[0], z=[0],
                mode='markers',
                marker=dict(size=4, color=color, symbol='x'),
                name=f'Daphnis (no current ephemeris)',
                text=[daphnis_info],
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            ))
            print(f"  ✓ Added Daphnis informational marker", flush=True)
            return fig
        else:
            print(f"  Warning: No osculating elements in cache for {satellite_name}", flush=True)
            return fig
        
        a = elements.get('a', 0)
        e = elements.get('e', 0)
        i = elements.get('i', 0)
        omega = elements.get('omega', 0)
        Omega = elements.get('Omega', 0)
        epoch = elements.get('epoch', 'unknown')
       
        print(f"  Plotting osculating: i={i:.4f}° (ecliptic), epoch={epoch}", flush=True)
        
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Rotation sequence: ω, i, Ω (inside-out for osculating)
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # NO Saturn rotation - osculating already in ecliptic!
        # (Saturn analytical orbits not shown due to reference frame complexity)        
        if satellite_name == 'Phoebe':
            hover_text_osc = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (retrograde, J2000 ecliptic)<br>"
                f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
                f"<br><i>Phoebe: Irregular retrograde satellite<br>"
                f"Period: ~550 days | Discovered: 1899<br>"
                f"Osculating elements from JPL Horizons.</i>"
            )
        else:
            hover_text_osc = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
                f"<br><i>Osculating = instantaneous Keplerian fit<br>"
                f"from JPL Horizons orbital elements.<br>"
                f"Saturn analytical orbits not shown due to<br>"
                f"reference frame complexity (pole RA=40.58°).</i>"
            )

        fig.add_trace(go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f'{satellite_name} Osculating Orbit (Epoch: {epoch})',
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
        print(f"  ✓ Osculating orbit plotted (ecliptic frame)", flush=True)
        return fig
        
    except Exception as e:
        print(f"Error plotting osculating orbit for {satellite_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig

def plot_uranus_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for Uranus satellites.
    
    CRITICAL: Uranus moon osculating elements are in ECLIPTIC frame (J2000.0)
    No planet-specific rotation needed - standard Keplerian sequence only.
    
    Uranus's extreme axial tilt (97.77°) and pole RA (257.31°) make analytical
    reference frame transformations extremely complex. Osculating elements from
    JPL Horizons are already in ecliptic frame and provide excellent alignment.
    
    Following Saturn pattern: osculating-only approach.
    """
    
    URANUS_MOON_IDS = {
        'Miranda': '705',
        'Ariel': '701',
        'Umbriel': '702',
        'Titania': '703',
        'Oberon': '704',
        'Portia': '712',
        'Mab': '726'
    }

    horizons_id = URANUS_MOON_IDS.get(satellite_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {satellite_name}", flush=True)
        return fig
    
    try:
        from osculating_cache_manager import load_cache
        
        print(f"\n[OSCULATING] Loading cached elements for {satellite_name}...", flush=True)
        cache = load_cache()
        
        if satellite_name in cache:
            elements = cache[satellite_name]['elements']
            print(f"  ✓ Using cached osculating elements", flush=True)
        else:
            print(f"  Warning: No osculating elements in cache for {satellite_name}", flush=True)
            print(f"  Hint: Use osculating cache manager to fetch from JPL Horizons (ID: {horizons_id})", flush=True)
            return fig
        
        a = elements.get('a', 0)
        e = elements.get('e', 0)
        i = elements.get('i', 0)
        omega = elements.get('omega', 0)
        Omega = elements.get('Omega', 0)
        epoch = elements.get('epoch', 'unknown')
       
        print(f"  Plotting osculating: i={i:.4f}° (ecliptic), epoch={epoch}", flush=True)
        
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard Keplerian rotation sequence: ω, i, Ω
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # NO Uranus rotation - osculating already in ecliptic!
        # (Uranus analytical orbits not shown due to extreme 98° tilt complexity)
        
        hover_text_osc = (
            f"<b>{satellite_name} Osculating Orbit</b><br>"
            f"Epoch: {epoch}<br>"
            f"a={a:.6f} AU, e={e:.6f}<br>"
            f"i={i:.4f}° (J2000 ecliptic)<br>"
            f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
            f"<br><i>Osculating = instantaneous Keplerian fit<br>"
            f"from JPL Horizons orbital elements.<br>"
            f"Uranus analytical orbits not shown due to<br>"
            f"extreme axial tilt (97.77°) complexity.</i>"
        )

        fig.add_trace(go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f'{satellite_name} Osculating Orbit (Epoch: {epoch})',
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
        print(f"  ✓ Osculating orbit plotted (ecliptic frame)", flush=True)
        return fig
        
    except Exception as e:
        print(f"Error plotting osculating orbit for {satellite_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig

def plot_neptune_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for Neptune satellites.
    
    CRITICAL: Neptune moon osculating elements are in ECLIPTIC frame (J2000.0)
    No planet-specific rotation needed - standard Keplerian sequence only.
    
    Neptune's pole RA (299.36°) is ~29° from ecliptic pole, and Triton's retrograde
    orbit makes analytical transformations complex. Osculating elements from JPL
    Horizons are already in ecliptic frame and handle retrograde orbits automatically.
    
    Following Saturn/Uranus pattern: osculating-only approach.
    
    Special moons:
    - Triton: Retrograde (i~157°) - largest, doomed to break up in ~3.6 billion years
    - Nereid: Highly eccentric (e~0.75) - captured object
    """
    
    NEPTUNE_MOON_IDS = {
        'Triton': '801',
        'Nereid': '802',
        'Naiad': '803',
        'Thalassa': '804',
        'Despina': '805',
        'Galatea': '806',
        'Larissa': '807',
        'Proteus': '808'
    }

    horizons_id = NEPTUNE_MOON_IDS.get(satellite_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {satellite_name}", flush=True)
        return fig
    
    try:
        from osculating_cache_manager import load_cache
        
        print(f"\n[OSCULATING] Loading cached elements for {satellite_name}...", flush=True)
        cache = load_cache()
        
        if satellite_name in cache:
            elements = cache[satellite_name]['elements']
            print(f"  ✓ Using cached osculating elements", flush=True)
        else:
            print(f"  Warning: No osculating elements in cache for {satellite_name}", flush=True)
            print(f"  Hint: Use osculating cache manager to fetch from JPL Horizons (ID: {horizons_id})", flush=True)
            return fig
        
        a = elements.get('a', 0)
        e = elements.get('e', 0)
        i = elements.get('i', 0)
        omega = elements.get('omega', 0)
        Omega = elements.get('Omega', 0)
        epoch = elements.get('epoch', 'unknown')
       
        print(f"  Plotting osculating: i={i:.4f}° (ecliptic), epoch={epoch}", flush=True)
        
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard Keplerian rotation sequence: ω, i, Ω
        # Retrograde orbits (i > 90°) handled automatically
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # NO Neptune rotation - osculating already in ecliptic!
        
        # Special hover text for Triton and Nereid
        if satellite_name == 'Triton':
            hover_text_osc = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (retrograde, J2000 ecliptic)<br>"
                f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
                f"<br><i>Triton: Neptune's largest moon<br>"
                f"Retrograde orbit - likely captured Kuiper Belt object<br>"
                f"Spiraling inward, will break up in ~3.6 billion years<br>"
                f"(Like Phobos around Mars!)</i>"
            )
        elif satellite_name == 'Nereid':
            hover_text_osc = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
                f"<br><i>Nereid: Highly eccentric orbit (e≈0.75)<br>"
                f"Most eccentric known moon in solar system<br>"
                f"Likely perturbed by Triton's capture</i>"
            )
        else:
            hover_text_osc = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"ω={omega:.2f}°, Ω={Omega:.2f}°<br>"
                f"<br><i>Osculating = instantaneous Keplerian fit<br>"
                f"from JPL Horizons orbital elements.<br>"
                f"Neptune analytical orbits not shown due to<br>"
                f"pole orientation and Triton complexity.</i>"
            )

        fig.add_trace(go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f'{satellite_name} Osculating Orbit (Epoch: {epoch})',
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
        print(f"  ✓ Osculating orbit plotted (ecliptic frame)", flush=True)
        return fig
        
    except Exception as e:
        print(f"Error plotting osculating orbit for {satellite_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig

def plot_pluto_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers=False, center_id='Pluto'):
    """
    Plot osculating orbit for objects in Pluto binary system.
    
    Supports TWO center modes:
    1. center_id='Pluto' - Traditional view, moons orbit Pluto
    2. center_id='Pluto-Charon Barycenter' - Binary view, ALL objects orbit barycenter
    
    When "Pluto-Charon Barycenter" is the center:
    - Pluto orbits the barycenter (tiny orbit ~0.0000137 AU)
    - Charon orbits the barycenter (larger orbit ~0.000117 AU, same period)
    - Other moons orbit the barycenter (wider orbits)
    
    All osculating elements from JPL Horizons are in ECLIPTIC frame (J2000.0).
    
    Binary System Parameters (from New Horizons):
    - Total separation: 19,596 km = 0.000131 AU
    - Period: 6.387 days (both tidally locked)
    - Mass ratio: M_Charon/M_Pluto = 0.122
    - Barycenter: 2,035 km from Pluto center (OUTSIDE Pluto's 1,188 km radius!)
    - System inclination to ecliptic: ~119.6° (retrograde)
    """
    
    # Horizons IDs for Pluto system objects
    PLUTO_SYSTEM_IDS = {
        'Pluto': '999',    # Body center (orbits barycenter in Mode 3)
        'Charon': '901',   # Largest moon (binary partner)
        'Styx': '905',     # Tiny irregular
        'Nix': '902',      # Elongated
        'Kerberos': '904', # Dark surface
        'Hydra': '903'     # Most distant
    }
    
    # Binary system physical parameters (from New Horizons mission)
    BINARY_PARAMS = {
        'separation_au': 0.000131,        # 19,596 km total separation
        'period_days': 6.387,             # Orbital period
        'mass_ratio': 0.122,              # M_Charon / M_Pluto
        'eccentricity': 0.0002,           # Nearly circular
        # Fallback angular elements (only used if cache unavailable)
        'inclination_ecliptic': 119.6,    # To J2000 ecliptic (retrograde)
        'Omega_ecliptic': 223.0,          # Longitude of ascending node (approximate)
        'omega': 0.0,                     # Argument of periapsis (circular orbit)
    }
    
    mass_ratio = BINARY_PARAMS['mass_ratio']
    separation = BINARY_PARAMS['separation_au']

    horizons_id = PLUTO_SYSTEM_IDS.get(object_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {object_name}", flush=True)
        return fig
    
    is_barycenter_mode = (center_id == 'Pluto-Charon Barycenter')
    
    try:
        # Always load cache - we need it for angular elements even in barycenter mode
    #    from osculating_cache_manager import load_cache
    #    cache = load_cache()
        
        from osculating_cache_manager import load_cache, get_cache_key
        cache = load_cache()
        
        # Determine cache key suffix based on view mode
        if is_barycenter_mode:
            center_suffix = '@9'  # Barycentric view
        else:
            center_suffix = '@999'  # Pluto-centered view (or None for default)

        # Determine which orbital elements to use


        """
        if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
            # BARYCENTER MODE for Pluto/Charon:
            # - Semi-major axis: CALCULATED from mass ratio (different from Pluto-centered)
            # - Angular elements (i, ω, Ω): FROM CACHE (same orbital plane regardless of center)
            
            # Calculate semi-major axis from mass ratio
            if object_name == 'Pluto':
                a = separation * mass_ratio / (1 + mass_ratio)  # ~0.0000142 AU
            else:  # Charon
                a = separation * 1.0 / (1 + mass_ratio)  # ~0.000117 AU
            
            e = BINARY_PARAMS['eccentricity']  # Nearly circular
            
            # Get angular elements from Charon's cache (defines the orbital plane)
            # Both Pluto and Charon share the same orbital plane
            if 'Charon' in cache:
                cached_elements = cache['Charon']['elements']
                i = cached_elements.get('i', BINARY_PARAMS['inclination_ecliptic'])
                omega = cached_elements.get('omega', BINARY_PARAMS['omega'])
                Omega = cached_elements.get('Omega', BINARY_PARAMS['Omega_ecliptic'])
                epoch = cached_elements.get('epoch', f"{date.strftime('%Y-%m-%d')}")
                print(f"\n[BARYCENTER MODE] {object_name}: using Charon's cached angular elements", flush=True)
            else:
                # Fallback to approximations if no cache
                i = BINARY_PARAMS['inclination_ecliptic']
                omega = BINARY_PARAMS['omega']
                Omega = BINARY_PARAMS['Omega_ecliptic']
                epoch = f"{date.strftime('%Y-%m-%d')} (approx)"
                print(f"\n[BARYCENTER MODE] {object_name}: using fallback angular elements (no cache)", flush=True)
            
            print(f"  a={a:.7f} AU ({a * 149597870.7:.1f} km from barycenter)", flush=True)
            print(f"  i={i:.2f}°, Ω={Omega:.2f}°, ω={omega:.2f}° (from cache)", flush=True)
            """
        

        if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
            # BARYCENTER MODE for Pluto/Charon:
            # Try to use barycentric osculating elements from cache first
            # Fall back to calculated values if not available
            
            cache_key = get_cache_key(object_name, '@9')  # e.g., 'Pluto@9', 'Charon@9'
            
            if cache_key in cache:
                # USE ACTUAL BARYCENTRIC OSCULATING ELEMENTS
                elements = cache[cache_key]['elements']
                a = elements.get('a', 0)
                e = elements.get('e', BINARY_PARAMS['eccentricity'])
                i = elements.get('i', BINARY_PARAMS['inclination_ecliptic'])
                omega = elements.get('omega', BINARY_PARAMS['omega'])
                Omega = elements.get('Omega', BINARY_PARAMS['Omega_ecliptic'])
                epoch = elements.get('epoch', f"{date.strftime('%Y-%m-%d')}")
                print(f"\n[BARYCENTER MODE] {object_name}: using barycentric osculating elements ({cache_key})", flush=True)
                print(f"  a={a:.7f} AU ({a * 149597870.7:.1f} km from barycenter)", flush=True)
                print(f"  e={e:.6f}, i={i:.2f}°, Ω={Omega:.2f}°, ω={omega:.2f}°", flush=True)
            else:
                # FALLBACK: Calculate from mass ratio + angular elements from Pluto-centered cache
                print(f"\n[BARYCENTER MODE] {object_name}: no barycentric cache ({cache_key}), using calculated values", flush=True)
                
                # Calculate semi-major axis from mass ratio
                if object_name == 'Pluto':
                    a = separation * mass_ratio / (1 + mass_ratio)  # ~0.0000142 AU
                else:  # Charon
                    a = separation * 1.0 / (1 + mass_ratio)  # ~0.000117 AU
                
                e = BINARY_PARAMS['eccentricity']  # Nearly circular
                
                # Get angular elements from Charon's Pluto-centered cache (defines the orbital plane)
                if 'Charon' in cache:
                    cached_elements = cache['Charon']['elements']
                    i = cached_elements.get('i', BINARY_PARAMS['inclination_ecliptic'])
                    omega = cached_elements.get('omega', BINARY_PARAMS['omega'])
                    Omega = cached_elements.get('Omega', BINARY_PARAMS['Omega_ecliptic'])
                    epoch = cached_elements.get('epoch', f"{date.strftime('%Y-%m-%d')}")
                    print(f"  Using Charon's Pluto-centered angular elements as fallback", flush=True)
                else:
                    # Final fallback to approximations
                    i = BINARY_PARAMS['inclination_ecliptic']
                    omega = BINARY_PARAMS['omega']
                    Omega = BINARY_PARAMS['Omega_ecliptic']
                    epoch = f"{date.strftime('%Y-%m-%d')} (approx)"
                    print(f"  Using fallback angular elements (no cache)", flush=True)
                
                print(f"  a={a:.7f} AU ({a * 149597870.7:.1f} km from barycenter)", flush=True)
                print(f"  i={i:.2f}°, Ω={Omega:.2f}°, ω={omega:.2f}° (from cache)", flush=True)

        else:
            # PLUTO-CENTERED MODE or outer moons:
            # Use cached osculating elements with appropriate center
            
            # Determine the correct cache key based on view
            if is_barycenter_mode:
                cache_key = get_cache_key(object_name, '@9')  # e.g., 'Styx@9'
                fallback_key = object_name  # Fall back to Pluto-centered if barycentric not available
            else:
                cache_key = object_name  # Pluto-centered (default)
                fallback_key = None
            
            print(f"\n[OSCULATING] Loading cached elements for {object_name}...", flush=True)
            
            if cache_key in cache:
                elements = cache[cache_key]['elements']
                print(f"  ✓ Using cached osculating elements ({cache_key})", flush=True)
            elif fallback_key and fallback_key in cache:
                elements = cache[fallback_key]['elements']
                print(f"  ⚠ Using fallback cache key ({fallback_key}) - barycentric elements not cached", flush=True)
            else:
                # Try fetching from planetary_params for moons
                if object_name in planetary_params:
                    elements = planetary_params[object_name]
                    print(f"  ✓ Using analytical elements from planetary_params", flush=True)
                else:
                    print(f"  Warning: No osculating elements in cache for {object_name}", flush=True)
                    return fig
            
            a = elements.get('a', 0)
            e = elements.get('e', 0)
            i = elements.get('i', 0)
            omega = elements.get('omega', 0)
            Omega = elements.get('Omega', 0)
            epoch = elements.get('epoch', 'analytical')
        
        # Skip if no valid semi-major axis
        if a == 0:
            print(f"  Warning: Zero semi-major axis for {object_name}", flush=True)
            return fig
        
        print(f"  Plotting: a={a:.7f} AU, i={i:.4f}° (ecliptic), epoch={epoch}", flush=True)
        
        # Generate orbital path
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard Keplerian rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Build hover text based on mode and object
        if is_barycenter_mode:
            hover_text_osc = _build_barycenter_mode_hover_text(object_name, a, e, i, epoch, BINARY_PARAMS)
        else:
            hover_text_osc = _build_pluto_centered_hover_text(object_name, a, e, i, epoch)
        
        # Determine line style
        if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
            # Dashed lines for osculating orbits (to distinguish from actual orbits)
            line_style = dict(color=color, width=2, dash='dash')

            orbit_label = f'{object_name} Osculating Orbit (Epoch: {epoch})'

        else:
            # Dashed for osculating orbits
            line_style = dict(color=color, width=2, dash='dash')
            orbit_label = f'{object_name} Osculating Orbit (Epoch: {epoch})'
        
        fig.add_trace(go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='lines',
            line=line_style,
            name=orbit_label,
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
#        print(f"  ✓ Orbit plotted (ecliptic frame)", flush=True)
#        return fig

        # Add apsidal markers using standard method
        if show_apsidal_markers and e > 0.001:  # Skip for nearly circular orbits
            from apsidal_markers import add_perihelion_marker, add_apohelion_marker
            
            # Find periapsis and apoapsis indices
            periapsis_idx = np.argmin(r)
            apoapsis_idx = np.argmax(r)
            
            # Build orbital parameters dict for apsidal marker functions
            orbital_params = {
                'a': a,
                'e': e,
                'i': i,
                'omega': omega,
                'Omega': Omega
            }
            
            # Determine center body for proper terminology
            center_body = center_id if center_id != 'Pluto-Charon Barycenter' else 'Pluto-Charon Barycenter'
            
            # Add periapsis marker
            add_perihelion_marker(
                fig,
                x_final[periapsis_idx],
                y_final[periapsis_idx],
                z_final[periapsis_idx],
                object_name,
                a,
                e,
                date if date else datetime.now(),
                {'x': x_final[periapsis_idx], 'y': y_final[periapsis_idx], 'z': z_final[periapsis_idx]},
                orbital_params,
                lambda x: color,
                q=r[periapsis_idx],
                center_body=center_body
            )
            
            # Add apoapsis marker
            add_apohelion_marker(
                fig,
                x_final[apoapsis_idx],
                y_final[apoapsis_idx],
                z_final[apoapsis_idx],
                object_name,
                a,
                e,
                date if date else datetime.now(),
                {'x': x_final[apoapsis_idx], 'y': y_final[apoapsis_idx], 'z': z_final[apoapsis_idx]},
                orbital_params,
                lambda x: color,
                center_body=center_body
            )
        
        print(f"  [OK] Orbit plotted (ecliptic frame)", flush=True)
        return fig

    except Exception as e:
        print(f"Error plotting orbit for {object_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig


def plot_tno_satellite_orbit(fig, satellite_name, parent_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for TNO (Trans-Neptunian Object) satellites.
    
    Handles satellites of:
    - Eris (Dysnomia)
    - Haumea (Hi'iaka, Namaka)
    - Makemake (MK2)
    
    All use JPL satellite ephemeris solutions with barycenter-relative positioning.
    Osculating elements from JPL Horizons are in ECLIPTIC frame (J2000.0).
    
    Unlike major planet moons, TNO satellites have no reliable analytical elements,
    so we display osculating orbits ONLY (no dual-orbit comparison).
    """
    
    # JPL Horizons IDs for TNO satellites (satellite ephemeris solutions)
    TNO_SATELLITE_IDS = {
        # Eris system (barycenter: 20136199)
        'Dysnomia': '120136199',
        # Haumea system (barycenter: 20136108)
        "Hi'iaka": '120136108',
        'Namaka': '220136108',
        # Makemake system (barycenter: 20136472)
        'MK2': '120136472',
    }
    
    horizons_id = TNO_SATELLITE_IDS.get(satellite_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for TNO satellite {satellite_name}", flush=True)
        return fig
    
    try:
        # Load osculating cache
        from osculating_cache_manager import load_cache
        cache = load_cache()
        
        print(f"\n[TNO SATELLITE] Loading cached elements for {satellite_name}...", flush=True)
        
        if satellite_name in cache:
            elements = cache[satellite_name]['elements']
            epoch = elements.get('epoch', f"{date.strftime('%Y-%m-%d')}")
            print(f"  ✓ Using cached osculating elements (epoch: {epoch})", flush=True)
            
            a = elements.get('a', 0)
            e = elements.get('e', 0)
            i = elements.get('i', 0)
            omega = elements.get('omega', 0)
            Omega = elements.get('Omega', 0)
            orbit_source = "osculating"
            
    #    else:
    #        print(f"  ⚠ No cached elements for {satellite_name}, skipping orbit plot", flush=True)
    #        return fig
        
        else:
            # Check for analytical fallback (satellites without JPL ephemeris)
            # ═══════════════════════════════════════════════════════════════════
            # IMPORTANT: This solution is tailored specifically for MK2:
            #   1. Assumes circular orbit (e=0): mean anomaly = true anomaly  
            #   2. Uses J2000.0 as reference epoch with M₀=0° (arbitrary phase)
            #   3. Orbital elements from arXiv:2509.05880 (Sept 2025)
            #
            # For other objects, you may need to:
            #   - Solve Kepler's equation for eccentric anomaly (if e > 0)
            #   - Use object-specific reference epoch and M₀
            #   - Apply different coordinate transformations
            # ═══════════════════════════════════════════════════════════════════
            ANALYTICAL_FALLBACK_SATELLITES = ['MK2']  # Expandable - see notes above
           
            if satellite_name in ANALYTICAL_FALLBACK_SATELLITES:
                print(f"  ⚠ No JPL ephemeris for {satellite_name}, using analytical elements", flush=True)
                from orbital_elements import planetary_params
                
                if satellite_name in planetary_params:
                    elements = planetary_params[satellite_name]
                    epoch = "Analytical (2025 preliminary)"
                    orbit_source = "analytical"
                    
                    a = elements.get('a', 0)
                    e = elements.get('e', 0)
                    i = elements.get('i', 0)
                    omega = elements.get('omega', 0)
                    Omega = elements.get('Omega', 0)
                    
                    print(f"  ✓ Using analytical elements from planetary_params", flush=True)
                else:
                    print(f"  ⚠ No analytical elements for {satellite_name}, skipping orbit plot", flush=True)
                    return fig
            else:
                print(f"  ⚠ No cached elements for {satellite_name}, skipping orbit plot", flush=True)
                return fig

        print(f"  Elements: a={a:.6f} AU, e={e:.4f}, i={i:.2f}°, ω={omega:.2f}°, Ω={Omega:.2f}°", flush=True)
        
        # Generate orbit points
        theta = np.linspace(0, 2*np.pi, 360)
        
        # Skip if semi-major axis is invalid
        if a <= 0:
            print(f"  ⚠ Invalid semi-major axis for {satellite_name}", flush=True)
            return fig
            
        # Calculate orbit in orbital plane
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Apply 3D rotation (standard Keplerian to ecliptic transformation)
        # Rotation 1: Around z-axis by argument of periapsis (ω)
        x1 = x_orbit * np.cos(omega_rad) - y_orbit * np.sin(omega_rad)
        y1 = x_orbit * np.sin(omega_rad) + y_orbit * np.cos(omega_rad)
        z1 = z_orbit
        
        # Rotation 2: Around x-axis by inclination (i)
        x2 = x1
        y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
        z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
        
        # Rotation 3: Around z-axis by longitude of ascending node (Ω)
        x_final = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
        y_final = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
        z_final = z2
        
        """
        # Create hover text
        hover_text = (
            f"<b>{satellite_name} Osculating Orbit</b><br>"
            f"Parent: {parent_name}<br>"
            f"Epoch: {epoch}<br>"
            f"<br>"
            f"<b>Orbital Elements (JPL):</b><br>"
            f"a = {a:.6f} AU ({a * 149597870.7:.0f} km)<br>"
            f"e = {e:.4f}<br>"
            f"i = {i:.2f}°<br>"
            f"ω = {omega:.2f}°<br>"
            f"Ω = {Omega:.2f}°<br>"
            f"<br>"
            f"<i>Osculating orbit from JPL Horizons<br>"
            f"satellite ephemeris solution</i>"
        )
        """

        # Create hover text based on orbit source; currently this is for Makemake MK2 only
        if orbit_source == "analytical":
            hover_text = (
                f"<b>{satellite_name} Analytical Orbit</b><br>"
                f"Parent: {parent_name}<br>"
                f"Source: {epoch}<br>"
                f"<br>"
                f"<b>Orbital Elements for MK2:</b><br>"
                f"a = {a:.6f} AU ({a * 149597870.7:.0f} km)<br>"
                f"e = {e:.4f}<br>"
                f"i = {i:.2f}°<br>"
                f"ω = {omega:.2f}°<br>"
                f"Ω = {Omega:.2f}°<br>"
                f"<br>"
                f"<i>No JPL ephemeris available for MK2:<br>"
                f"Based on arXiv:2509.05880 (Sept 2025)<br>"
                f"preliminary Hubble orbital solution.<br>"
                f"Inclination uncertain (63°-87° range).<br>"
                f"No apsides because e=0.</i>"
            )
        else:
            hover_text = (
                f"<b>{satellite_name} Osculating Orbit</b><br>"
                f"Parent: {parent_name}<br>"
                f"Epoch: {epoch}<br>"
                f"<br>"
                f"<b>Orbital Elements (JPL):</b><br>"
                f"a = {a:.6f} AU ({a * 149597870.7:.0f} km)<br>"
                f"e = {e:.4f}<br>"
                f"i = {i:.2f}°<br>"
                f"ω = {omega:.2f}°<br>"
                f"Ω = {Omega:.2f}°<br>"
                f"<br>"
                f"<i>Osculating orbit from JPL Horizons<br>"
                f"satellite ephemeris solution</i>"
            )

        # Add orbit trace
        trace_name = f"{satellite_name} {'Analytical' if orbit_source == 'analytical' else 'Osculating'} Orbit"
        fig.add_trace(go.Scatter3d(
            x=x_final.tolist(),
            y=y_final.tolist(),
            z=z_final.tolist(),
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=trace_name,
            text=[hover_text] * len(x_final),
            customdata=[trace_name] * len(x_final),
            hoverinfo='text',
            showlegend=True
        ))
        
        print(f"  ✓ Plotted {satellite_name} {orbit_source} orbit", flush=True)

        # For analytical fallback satellites (MK2 only at this time), calculate and plot current position
        if orbit_source == "analytical":
            # Get orbital period from elements
            orbital_period = elements.get('orbital_period_days', 18.023)  # Default to MK2's period
            
            # Reference epoch: J2000.0 (2000-01-01 12:00 TDB), assume M₀ = 0°
            from datetime import datetime
            j2000 = datetime(2000, 1, 1, 12, 0, 0)
            
            # Calculate days since J2000
            delta_days = (date - j2000).total_seconds() / 86400.0
            
            # Mean motion (degrees per day)
            n = 360.0 / orbital_period
            
            # Mean anomaly at current date (for circular orbit, true anomaly = mean anomaly)
            M = (n * delta_days) % 360.0
            true_anomaly = np.radians(M)
            
            # Position in orbital plane (circular orbit: r = a)
            r_current = a  # For e=0, r is constant
            x_pos = r_current * np.cos(true_anomaly)
            y_pos = r_current * np.sin(true_anomaly)
            z_pos = 0.0
            
            # Apply same 3D rotation as orbit path
            # Rotation 1: Around z-axis by ω
            x1 = x_pos * np.cos(omega_rad) - y_pos * np.sin(omega_rad)
            y1 = x_pos * np.sin(omega_rad) + y_pos * np.cos(omega_rad)
            z1 = z_pos
            
            # Rotation 2: Around x-axis by i
            x2 = x1
            y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
            z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
            
            # Rotation 3: Around z-axis by Ω
            x_current = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
            y_current = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
            z_current = z2
            
            # Create position marker hover text
            pos_hover = (
                f"<b>{satellite_name}</b><br>"
                f"Date: {date.strftime('%Y-%m-%d %H:%M UTC')}<br>"
                f"<br>"
                f"MK2 Position: Calculated from analytical orbit<br>"
                f"Mean anomaly: {M:.1f}°<br>"
                f"Period: {orbital_period:.3f} days<br>"
                f"<br>"
                f"<i>⚠ MK2 position assumes M₀=0° at J2000.0<br>"
                f"Actual phase unknown - for visualization only</i>"
            )
            
            # Add position marker
            fig.add_trace(go.Scatter3d(
                x=[x_current],
                y=[y_current],
                z=[z_current],
                mode='markers',
                marker=dict(size=6, color=color, symbol='circle'),
                name=satellite_name,
                text=[pos_hover],
                hoverinfo='text',
                showlegend=True
            ))
            
            print(f"  ✓ Added {satellite_name} position marker (M={M:.1f}°, assumed phase)", flush=True)


        """
        # Add orbit trace
        fig.add_trace(go.Scatter3d(
            x=x_final.tolist(),
            y=y_final.tolist(),
            z=z_final.tolist(),
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f"{satellite_name} Osculating Orbit",
            text=[hover_text] * len(x_final),
            customdata=[f"{satellite_name} Osculating Orbit"] * len(x_final),
            hoverinfo='text',
            showlegend=True
        ))
        
        print(f"  ✓ Plotted {satellite_name} osculating orbit", flush=True)
        
        # Add apsidal markers if requested
        if show_apsidal_markers and e > 0.001:  # Skip for nearly circular orbits
            # Periapsis point (theta = 0)
            r_peri = a * (1 - e)
            peri_x = r_peri * (np.cos(Omega_rad) * np.cos(omega_rad) - 
                              np.sin(Omega_rad) * np.sin(omega_rad) * np.cos(i_rad))
            peri_y = r_peri * (np.sin(Omega_rad) * np.cos(omega_rad) + 
                              np.cos(Omega_rad) * np.sin(omega_rad) * np.cos(i_rad))
            peri_z = r_peri * np.sin(omega_rad) * np.sin(i_rad)
            
            fig.add_trace(go.Scatter3d(
                x=[peri_x], y=[peri_y], z=[peri_z],
                mode='markers',
                marker=dict(size=5, color=color, symbol='diamond'),
                name=f"{satellite_name} Periapsis",
                text=[f"{satellite_name} Periapsis<br>r = {r_peri:.6f} AU"],
                hoverinfo='text',
                showlegend=True
            ))
            
            # Apoapsis point (theta = π)
            r_apo = a * (1 + e)
            apo_x = -r_peri * (np.cos(Omega_rad) * np.cos(omega_rad) - 
                             np.sin(Omega_rad) * np.sin(omega_rad) * np.cos(i_rad))
            apo_y = -r_peri * (np.sin(Omega_rad) * np.cos(omega_rad) + 
                             np.cos(Omega_rad) * np.sin(omega_rad) * np.cos(i_rad))
            apo_z = -r_peri * np.sin(omega_rad) * np.sin(i_rad)
            
            fig.add_trace(go.Scatter3d(
                x=[apo_x], y=[apo_y], z=[apo_z],
                mode='markers',
                marker=dict(size=5, color=color, symbol='square'),
                name=f"{satellite_name} Apoapsis",
                text=[f"{satellite_name} Apoapsis<br>r = {r_apo:.6f} AU"],
                hoverinfo='text',
                showlegend=True
            ))
        
        return fig
        """

        # Add apsidal markers using standard method
        if show_apsidal_markers and e > 0.001:  # Skip for nearly circular orbits (like MK2) because every point is at the same distance.
    #    if show_apsidal_markers:  # Skip for nearly circular orbits    
            from apsidal_markers import add_perihelion_marker, add_apohelion_marker
            
            # Find periapsis and apoapsis indices
            periapsis_idx = np.argmin(r)
            apoapsis_idx = np.argmax(r)
            
            # Build orbital parameters dict for apsidal marker functions
            orbital_params = {
                'a': a,
                'e': e,
                'i': i,
                'omega': omega,
                'Omega': Omega
            }
            
            # Add periapsis marker
            add_perihelion_marker(
                fig,
                x_final[periapsis_idx],
                y_final[periapsis_idx],
                z_final[periapsis_idx],
                satellite_name,
                a,
                e,
                date if date else datetime.now(),
                {'x': x_final[periapsis_idx], 'y': y_final[periapsis_idx], 'z': z_final[periapsis_idx]},
                orbital_params,
                lambda x: color,
                q=r[periapsis_idx],
                center_body=parent_name
            )
            
            # Add apoapsis marker
            add_apohelion_marker(
                fig,
                x_final[apoapsis_idx],
                y_final[apoapsis_idx],
                z_final[apoapsis_idx],
                satellite_name,
                a,
                e,
                date if date else datetime.now(),
                {'x': x_final[apoapsis_idx], 'y': y_final[apoapsis_idx], 'z': z_final[apoapsis_idx]},
                orbital_params,
                lambda x: color,
                center_body=parent_name
            )
        
        return fig        
        
    except Exception as e:
        print(f"Error plotting TNO satellite orbit for {satellite_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig


def _build_barycenter_mode_hover_text(object_name, a, e, i, epoch, binary_params):
    """Build hover text for barycenter-centered view."""
    
    if object_name == 'Pluto':
        return (
            f"<b>Pluto's Osculating Orbit around Barycenter</b><br>"
            f"<i>The smaller orbit of the binary pair</i><br><br>"
            f"<b>Orbital Elements (Epoch: {epoch}):</b><br>"
            f"a = {a:.7f} AU ({a * 149597870.7:.0f} km) <i>[calculated]</i><br>"
            f"e = {e:.4f} (nearly circular)<br>"
            f"i = {i:.1f}° to ecliptic <i>[osculating]</i><br>"
            f"Period: {binary_params['period_days']:.3f} days<br><br>"
            f"<b>Why Pluto's orbit is smaller:</b><br>"
            f"<i>Pluto is ~8× more massive than Charon,<br>"
            f"so it orbits closer to the barycenter.<br>"
            f"Like a heavy adult on a see-saw sitting<br>"
            f"closer to the pivot point!</i><br><br>"
            f"<b>The barycenter is OUTSIDE Pluto!</b><br>"
            f"<i>2,035 km from Pluto's center,<br>"
            f"but Pluto's radius is only 1,188 km.<br>"
            f"This makes Pluto-Charon a true binary.</i><br><br>"
            f"<b>Note:</b> <i>Semi-major axis calculated from<br>"
            f"mass ratio; angles from Charon's osculating<br>"
            f"elements (same orbital plane).</i>"
        )
    
    elif object_name == 'Charon':
        return (
            f"<b>Charon's Osculating Orbit around Barycenter</b><br>"
            f"<i>The larger orbit of the binary pair</i><br><br>"
            f"<b>Orbital Elements (Epoch: {epoch}):</b><br>"
            f"a = {a:.7f} AU ({a * 149597870.7:.0f} km) <i>[calculated]</i><br>"
            f"e = {e:.4f} (nearly circular)<br>"
            f"i = {i:.1f}° to ecliptic <i>[osculating]</i><br>"
            f"Period: {binary_params['period_days']:.3f} days<br><br>"
            f"<b>Why Charon's orbit is larger:</b><br>"
            f"<i>Charon is only 12% of Pluto's mass,<br>"
            f"so it orbits farther from the barycenter.<br>"
            f"Like a child on a see-saw sitting<br>"
            f"farther from the pivot point!</i><br><br>"
            f"<b>The Dance:</b><br>"
            f"<i>Watch Pluto and Charon orbit together,<br>"
            f"always on opposite sides of their<br>"
            f"mutual center of mass. Tidally locked,<br>"
            f"they always show the same face to each other.</i><br><br>"
            f"<b>Note:</b> <i>Semi-major axis calculated from<br>"
            f"mass ratio; angles from osculating elements<br>"
            f"(same orbital plane as Pluto).</i>"
        )
    
    else:
        # Outer moons (Styx, Nix, Kerberos, Hydra) - unchanged
        return (
            f"<b>{object_name} Orbit</b><br>"
            f"<i>(around Pluto-Charon barycenter)</i><br><br>"
            f"a = {a:.7f} AU ({a * 149597870.7:.0f} km)<br>"
            f"e = {e:.4f}<br>"
            f"i = {i:.2f}° to ecliptic<br><br>"
            f"<b>Orbital Resonance:</b><br>"
            f"<i>The outer moons orbit in near-resonance<br>"
            f"with Charon's 6.387-day period:<br>"
            f"• Styx: ~3:1 (~20.2 days)<br>"
            f"• Nix: ~4:1 (~24.9 days)<br>"
            f"• Kerberos: ~5:1 (~32.2 days)<br>"
            f"• Hydra: ~6:1 (~38.2 days)</i><br><br>"
            f"<b>Why orbits diverge:</b><br>"
            f"<i>Osculating orbit 'kisses' actual position<br>"
            f"at epoch. Perturbations from Pluto-Charon<br>"
            f"binary cause deviations over time.</i>"
        )


def _build_pluto_centered_hover_text(object_name, a, e, i, epoch):
    """Build hover text for traditional Pluto-centered view."""
    
    if object_name == 'Charon':
        return (
            f"<b>Charon Osculating Orbit</b><br>"
            f"<i>(around Pluto center)</i><br><br>"
            f"Epoch: {epoch}<br>"
            f"a = {a:.6f} AU, e = {e:.6f}<br>"
            f"i = {i:.4f}° (J2000 ecliptic)<br>"
            f"Period: 6.387 days (tidally locked)<br><br>"
            f"<b>Why orbit appears non-circular:</b><br>"
            f"<i>Charon's orbit is nearly circular (e≈0.0002),<br>"
            f"but we're viewing from Pluto's CENTER,<br>"
            f"not the barycenter. Pluto itself moves<br>"
            f"in a small counter-orbit, making Charon's<br>"
            f"path appear to wobble slightly.</i>"
        )
    else:
        return (
            f"<b>{object_name} Osculating Orbit</b><br>"
            f"<i>(around Pluto center)</i><br><br>"
            f"Epoch: {epoch}<br>"
            f"a = {a:.6f} AU, e = {e:.6f}<br>"
            f"i = {i:.4f}° (J2000 ecliptic)<br><br>"
            f"<b>Why orbits diverge:</b><br>"
            f"<i>'Osculating' means 'kissing' - this ellipse<br>"
            f"matches position & velocity at epoch only.<br>"
            f"Real orbits deviate due to:<br>"
            f"• Charon's gravity (11.7% of Pluto's mass)<br>"
            f"• Orbital resonances between moons<br>"
            f"• The Pluto-Charon binary 'wobble'<br>"
            f"The divergence you see IS the perturbation!</i>"
        )

def add_pluto_barycenter_marker(fig, date, charon_position=None):
    """
    Add the Pluto-Charon barycenter marker to Pluto-centered view.
    
    The barycenter is ~2,035 km from Pluto's center toward Charon.
    This is OUTSIDE Pluto's surface (radius ~1,188 km)!
    
    Parameters:
        fig: Plotly figure
        date: Current date for position calculation
        charon_position: Dict with Charon's x, y, z position (if available)
    """
    # Barycenter distance from Pluto center in AU
    # Calculation: separation × (m_charon / (m_pluto + m_charon))
    # = 19,596 km × (0.122 / 1.122) ≈ 2,131 km ≈ 0.0000142 AU
    BARYCENTER_DIST_AU = 0.0000142
    
    if charon_position and charon_position.get('x') is not None:
        # Calculate unit vector from Pluto toward Charon
        cx, cy, cz = charon_position['x'], charon_position['y'], charon_position['z']
        charon_dist = (cx**2 + cy**2 + cz**2)**0.5
        
        if charon_dist > 0:
            # Barycenter is along the Pluto-Charon line
            bary_x = BARYCENTER_DIST_AU * (cx / charon_dist)
            bary_y = BARYCENTER_DIST_AU * (cy / charon_dist)
            bary_z = BARYCENTER_DIST_AU * (cz / charon_dist)
        else:
            bary_x, bary_y, bary_z = BARYCENTER_DIST_AU, 0, 0
    else:
        # Fallback: place on +X axis
        bary_x, bary_y, bary_z = BARYCENTER_DIST_AU, 0, 0
    
    hover_text = (
        f"<b>Pluto-Charon Barycenter</b><br>"
        f"<i>Center of mass of the binary system</i><br><br>"
        f"Distance from Pluto center: ~2,035 km<br>"
        f"Distance from Pluto surface: ~847 km<br>"
        f"<br><b>Why this matters:</b><br>"
        f"<i>The barycenter is OUTSIDE Pluto!<br>"
        f"Both Pluto and Charon orbit this point.<br>"
        f"This makes Pluto-Charon a true binary<br>"
        f"system - unique in our solar system.<br><br>"
        f"For comparison, Earth-Moon barycenter<br>"
        f"is 4,671 km from Earth's center -<br>"
        f"still inside Earth (radius 6,371 km).</i>"
    )
    
    fig.add_trace(go.Scatter3d(
        x=[bary_x], y=[bary_y], z=[bary_z],
        mode='markers',
        marker=dict(
            size=8,
    #        color='yellow',
            color=color_map('Pluto'),
            symbol='square-open',
    #        line=dict(color='yellow', width=2)
        ),
        name='Pluto-Charon Barycenter',
        text=[hover_text],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    ))
    
    print(f"  ✓ Added barycenter marker at ({bary_x:.7f}, {bary_y:.7f}, {bary_z:.7f}) AU", flush=True)
    
    return fig

def create_planet_transformation_matrix(planet_name):
    """
    Create a transformation matrix for a planet based on its pole direction.
    Transforms from planet's equatorial coordinates to ecliptic coordinates.
    
    Parameters:
        planet_name (str): Name of the planet
        
    Returns:
        numpy.ndarray: 3x3 transformation matrix
    """
    if planet_name not in planet_poles:
        # For planets without explicit pole directions, use the axial tilt
        if planet_name in planet_tilts:
            tilt_rad = np.radians(planet_tilts[planet_name])
            # Simple rotation matrix around the x-axis
            return np.array([
                [1, 0, 0],
                [0, np.cos(tilt_rad), -np.sin(tilt_rad)],
                [0, np.sin(tilt_rad), np.cos(tilt_rad)]
            ])
        return np.identity(3)  # Identity matrix if no data available
    
    # Get pole direction
    pole = planet_poles[planet_name]
    ra_pole = np.radians(pole['ra'])
    dec_pole = np.radians(pole['dec'])
    
    # Calculate the rotation matrix from planet's equatorial to ecliptic
    sin_dec = np.sin(dec_pole)
    cos_dec = np.cos(dec_pole)
    sin_ra = np.sin(ra_pole)
    cos_ra = np.cos(ra_pole)
    
    # Planet's north pole vector in ecliptic coordinates
    x_pole = cos_dec * cos_ra
    y_pole = cos_dec * sin_ra
    z_pole = sin_dec
    
    # Find the ascending node of planet's equator on the ecliptic
    # This is perpendicular to the pole and in the ecliptic plane
    x_node = -y_pole / np.sqrt(x_pole**2 + y_pole**2)
    y_node = x_pole / np.sqrt(x_pole**2 + y_pole**2)
    z_node = 0
    
    # Create orthogonal basis vectors
    x_basis = np.array([x_node, y_node, z_node])
    z_basis = np.array([x_pole, y_pole, z_pole])
    y_basis = np.cross(z_basis, x_basis)
    
    # Construct the transformation matrix
    transform_matrix = np.vstack((x_basis, y_basis, z_basis)).T
    
    return transform_matrix

def plot_satellite_orbit(satellite_name, planetary_params, parent_planet, color, fig=None, 
                         date=None, days_to_plot=None, current_position=None,
                         show_apsidal_markers=False):
    """
    Plot the Keplerian orbit of a satellite around its parent planet.
    
    Parameters:
        satellite_name (str): Name of the satellite
        planetary_params (dict): Dictionary containing orbital parameters for all objects
        parent_planet (str): Name of the parent planet
        color (str): Color to use for the orbit line
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        date (datetime): Date for the calculation
        days_to_plot (float): Number of days to plot
        current_position (dict): Current position with 'x', 'y', 'z' keys
        
    Returns:
        plotly.graph_objects.Figure: Figure with the satellite orbit added
    """
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get the orbital parameters for this specific satellite
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)  # Semi-major axis in AU
        e = orbital_params.get('e', 0)  # Eccentricity
        i = orbital_params.get('i', 0)  # Inclination in degrees
        omega = orbital_params.get('omega', 0)  # Argument of periapsis in degrees
        Omega = orbital_params.get('Omega', 0)  # Longitude of ascending node in degrees
        
        print(f"\nPlotting {satellite_name} orbit around {parent_planet}", flush=True)
        print(f"Orbital elements: a={a}, e={e}, i={i}°, ω={omega}°, Ω={Omega}°", flush=True)
        
        # Calculate angular range based on days_to_plot
        if days_to_plot is not None and days_to_plot > 0:
            # Get the satellite's orbital period
            if 'orbital_period_days' in orbital_params:
                period_days = orbital_params['orbital_period_days']
            else:
                # Use KNOWN_ORBITAL_PERIODS from constants_new.py
                from constants_new import KNOWN_ORBITAL_PERIODS
                
                if satellite_name in KNOWN_ORBITAL_PERIODS:
                    period_value = KNOWN_ORBITAL_PERIODS[satellite_name]

                    if period_value is None:
                        # Handle hyperbolic/parabolic objects - use Kepler's law
                        period_days = 365.25 * np.sqrt(abs(a)**3) if a else 365.25

                    else:
                        # Already in days
                        period_days = period_value
                else:
                    # Fallback for unknown satellites
                    print(f"  Warning: No known period for {satellite_name}, using default", flush=True)
                    period_days = 10  # Default fallback
            
            orbital_fraction = days_to_plot / period_days
            max_angle = 2 * np.pi * orbital_fraction
            
            # Generate orbit points only for the requested time range
            num_points = max(30, int(360 * min(orbital_fraction, 1.0)))  # At least 30 points
            theta = np.linspace(0, max_angle, num_points)
            print(f"  Plotting {days_to_plot} days = {orbital_fraction:.2f} orbits (period: {period_days:.3f} days)", flush=True)
        else:
            # Full orbit
            theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness

        # Generate ellipse in orbital plane
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        # 1. Longitude of ascending node (Ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        # 2. Inclination (i) around x-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        # 3. Argument of periapsis (ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Transformation from a planet's equatorial frame to ecliptic frame:
        # 
        # This solution follows an important pattern we discovered across multiple planetary systems:
        # - For Mars satellites: Y-axis rotation of 25.19° (Mars's axial tilt) aligns orbits properly
        # - For Uranus satellites: Matching X and Y rotations of 97.77° (Uranus's axial tilt) creates proper alignment
        #
        # General principle: When satellite orbital elements are defined in a planet's equatorial reference frame
        # (as documented by JPL), the transformation to the ecliptic frame must incorporate the planet's axial tilt
        # in a manner that reflects the planet's specific orientation in space.
        #
        # For planets with moderate axial tilts (Mars), a single rotation may suffice.
        # For planets with extreme axial tilts (Uranus), compound rotations around multiple axes are required.
        #
        # This transformation correctly maps from the satellite's native reference frame (the planet's equator)
        # to the ecliptic reference frame used in our visualization.

        # Apply transformation based on the planet
        if parent_planet == 'Mars':
            # This 25° value is particularly interesting because it's very close to Mars' axial tilt of 25.19°. 
            # This suggests there might be a direct relationship between Mars' axial tilt and the reference frame used 
            # for defining its satellites' orbital elements. The fact that Deimos aligns better at 25° while Phobos aligns 
            # better at 26° could be related to: 1) Small differences in how each moon's orbital elements were measured or 
            # calculated. 2) The fact that Phobos orbits much closer to Mars and might be more affected by Mars' non-spherical 
            # gravity field 3) Possible time-dependent variations in the orbital planes. To put this discovery in context: we've 
            # essentially found that Mars' moons' orbital elements are defined in a reference frame that requires a Y-axis 
            # rotation approximately equal to Mars' axial tilt to align with the ecliptic reference frame used in your 
            # visualization. This makes intuitive sense astronomically, as it suggests the orbital elements are defined relative 
            # to Mars' equatorial plane.
            #
            # Using Mars' exact axial tilt (25.19°) as the Y-axis rotation value creates a perfect astronomical justification 
            # for the transformation. It strongly suggests that the orbital elements for Mars' satellites are indeed defined 
            # relative to Mars' equatorial plane, which makes sense from a planetary science perspective.
            #
            # "Reference Frame Note: The orbital elements for Mars' satellites (Phobos and Deimos) are provided relative to 
            # Mars' equatorial plane. When transforming these elements to ecliptic coordinates for visualization, a rotation 
            # of 25.19° around the Y-axis (equivalent to Mars' axial tilt) should be applied after the standard orbital element 
            # rotations."
            # 
            # A Y-axis rotation (not X) is needed because it represents a rotation around 
            # the ecliptic plane's normal axis, which correctly positions the orbital planes
            # of Phobos and Deimos relative to Mars' orbital plane.

            # Transform from Mars equatorial to ecliptic coordinates
            # Using Mars' axial tilt. Note: A small (~10-20°) offset remains
            # between Keplerian and actual orbits, likely due to JPL's specific
            # convention for defining the ascending node reference.

            #Different reference conventions: JPL might use a slightly different convention for defining the ascending node that 
            # we haven't identified         
            # Small systematic errors: The ~10-20° offset might be inherent to how the orbital elements are defined
            # Time-dependent effects: Small variations in Mars' orientation that aren't captured in a static transformation

            # Your time-varying elements are working correctly:
            # Ω change: -157.9° per year (matches expected -158°)
            # ω change: 27.0° per year (matches expected +27°)
            #This confirms the precession calculations are accurate.

            if date is not None:
                # Override static orbital elements with time-varying ones
                orbital_params = calculate_mars_satellite_elements(date, satellite_name)
                print(f"Using time-varying elements for {satellite_name} at {date}", flush=True)
                
                # Re-extract the updated orbital elements
                a = orbital_params.get('a', 0)
                e = orbital_params.get('e', 0)
                i = orbital_params.get('i', 0)
                omega = orbital_params.get('omega', 0)
                Omega = orbital_params.get('Omega', 0)
                
                print(f"  Time-varying: a={a:.6f} AU, e={e:.6f}, i={i:.2f}°, ω={omega:.2f}°, Ω={Omega:.2f}°", flush=True)

                # Regenerate the orbit with new elements
                theta = np.linspace(0, 2*np.pi, 360)
                r = a * (1 - e**2) / (1 + e * np.cos(theta))
                
                x_orbit = r * np.cos(theta)
                y_orbit = r * np.sin(theta)
                z_orbit = np.zeros_like(theta)
                
                # Convert updated angles to radians
                i_rad = np.radians(i)
                omega_rad = np.radians(omega)
                Omega_rad = np.radians(Omega)
                
                # Apply standard orbital rotations with updated elements
                x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
                x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
                x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')

            # The Y-rotation of 25.19° suggests the node reference is already 
            # aligned with the ecliptic in some way. However, there's still
            # a visible offset in your plot.
            
            # Try this refined approach: -- not used because it does not resolve the discrepancy
            # 1. First apply a small Z-rotation to account for the remaining offset
    #        z_adjustment = np.radians(15)  # Tune this based on the visual offset. 
    #        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, z_adjustment, 'z')
            
            # 2. Then apply the Mars tilt

            mars_y_rotation = np.radians(25.19)
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, mars_y_rotation, 'y')
            print(f"Transformation applied: Mars with Y-axis rotation of 25.19°", flush=True)   

    #        z_adjustment = np.radians(10)  # Shift the z adjustment after the y adjustment -- does not improve the discrepancy
    #        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, z_adjustment, 'z') 

        elif parent_planet == 'Jupiter':
            # Jupiter moons with time-varying MEAN elements
            JUPITER_MOONS = ['Io', 'Europa', 'Ganymede', 'Callisto', 
                             'Metis', 'Adrastea', 'Amalthea', 'Thebe']
            
            if satellite_name in JUPITER_MOONS and date is not None:
                # Get time-varying mean elements
                time_varying_params = calculate_jupiter_satellite_elements(date, satellite_name)
                
                if time_varying_params is not None:
                    print(f"Using time-varying MEAN elements for {satellite_name} at {date}", flush=True)
                    
                    # Re-extract updated elements
                    a = time_varying_params.get('a', 0)
                    e = time_varying_params.get('e', 0)
                    i = time_varying_params.get('i', 0)
                    omega = time_varying_params.get('omega', 0)
                    Omega = time_varying_params.get('Omega', 0)
                    
                    print(f"  Mean elements: a={a:.6f} AU, e={e:.6f}, i={i:.4f}° (Jupiter eq)", flush=True)
                    
                    # Regenerate orbit with updated elements
                    theta = np.linspace(0, 2*np.pi, 360)
                    r = a * (1 - e**2) / (1 + e * np.cos(theta))
                    
                    x_orbit = r * np.cos(theta)
                    y_orbit = r * np.sin(theta)
                    z_orbit = np.zeros_like(theta)
                    
                    # Apply rotations
                    i_rad = np.radians(i)
                    omega_rad = np.radians(omega)
                    Omega_rad = np.radians(Omega)
                    
                    x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
                    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
                    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
            
            # Transform from Jupiter equatorial to ecliptic
            jupiter_tilt = np.radians(3.13)
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, jupiter_tilt, 'x')
            print(f"  Transform: Jupiter equatorial → ecliptic (3.13° X-rotation)", flush=True)

        elif parent_planet == 'Saturn':
            if satellite_name == 'Phoebe':
                # Special transformation for Phoebe - irregular retrograde satellite
                # From JPL Horizons header: "mean values with respect to local Laplace plane"
                
                # Transform from Laplace plane to ecliptic:
                # 1. First align with Saturn's orbital plane
                saturn_orbit_inc = np.radians(2.485)  # Saturn's orbital inclination
                saturn_orbit_node = np.radians(113.665)  # Saturn's ascending node
                
                # 2. Apply a partial rotation between Saturn's equator and orbital plane
                # Phoebe is far enough that Laplace plane is tilted from equatorial plane
                laplace_tilt = np.radians(17.0)  # Increased from 15° based on residuals
                
                # 3. Additional node alignment correction
                # Based on the Y-component difference in normals, we need a Z rotation
                node_correction = np.radians(-30.0)  # Empirical adjustment
                
                # Apply transformations in sequence:
                # a) Rotate from Laplace plane toward Saturn's orbital plane
                x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, -laplace_tilt, 'x')
                
                # b) Apply node correction to align ascending nodes
                x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, node_correction, 'z')
                
                # c) Transform to ecliptic using Saturn's orbital elements
                x_rot3, y_rot3, z_rot3 = rotate_points(x_rot2, y_rot2, z_rot2, -saturn_orbit_node, 'z')
                x_final, y_final, z_final = rotate_points(x_rot3, y_rot3, z_rot3, -saturn_orbit_inc, 'x')
                
                print(f"Transformation applied: Phoebe from Laplace plane to ecliptic (enhanced)", flush=True)

# Saturn moons (except Phoebe) - follows Jupiter pattern. The calculate_saturn_satellite_elements() function currently only has 
# elements for the 8 major moons (Mimas through Iapetus). For Pan, Daphnis, Prometheus, and Pandora, it returns None and prints a warning.
            else:
                # Saturn moons with time-varying MEAN elements (same pattern as Jupiter)
                if satellite_name in SATURN_MOONS and date is not None:
                    # Get time-varying mean elements
                    time_varying_params = calculate_saturn_satellite_elements(date, satellite_name)
                    
                    if time_varying_params is not None:
                        print(f"Using time-varying MEAN elements for {satellite_name} at {date}", flush=True)
                        
                        # Re-extract updated elements
                        a = time_varying_params.get('a', 0)
                        e = time_varying_params.get('e', 0)
                        i = time_varying_params.get('i', 0)
                        omega = time_varying_params.get('omega', 0)
                        Omega = time_varying_params.get('Omega', 0)
                        
                        print(f"  Mean elements: a={a:.6f} AU, e={e:.6f}, i={i:.4f}° (Saturn eq)", flush=True)
                        
                        # Regenerate FULL orbit with updated elements
                        theta = np.linspace(0, 2*np.pi, 360)
                        r = a * (1 - e**2) / (1 + e * np.cos(theta))
                        
                        x_orbit = r * np.cos(theta)
                        y_orbit = r * np.sin(theta)
                        z_orbit = np.zeros_like(theta)
                        
                        # Apply rotations with updated elements
                        i_rad = np.radians(i)
                        omega_rad = np.radians(omega)
                        Omega_rad = np.radians(Omega)
                        
                        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
                        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
                        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
                
                # Transform from Saturn equatorial to ecliptic (same as Jupiter pattern)
                saturn_tilt = np.radians(-26.73)  # Saturn's axial tilt (negative for correct direction)
                x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, saturn_tilt, 'x')
                print(f"  Transform: Saturn equatorial → ecliptic (-26.73° X-rotation)", flush=True)

        elif parent_planet == 'Uranus':
            # Transformation from Uranus's equatorial frame to ecliptic frame:
            # 
            # The orbital elements in JPL Horizons are defined relative to Uranus's
            # equatorial plane (per JPL documentation), requiring a transformation
            # to the ecliptic reference frame used in our visualization.
            #
            # Our optimal transformation uses two sequential rotations:
            # 1. First rotation (X+): 105° rotation around the X-axis
            # 2. Second rotation (Y+): 105° rotation around the Y-axis
            #
            # This compound rotation of 105° (rather than Uranus's nominal axial tilt of 97.77°)
            # was determined through empirical testing to provide the best alignment between
            # Keplerian and actual satellite orbits. The 7° difference may account for:
            #   - Reference frame subtleties not captured in simple transformations
            #   - Uranus's magnetic field orientation (which is offset from its rotation axis)
            #   - The combined effect of Uranus's obliquity and orbital inclination
            #   - Possible reference epoch differences
            #
            # This solution follows a pattern we discovered across planetary systems:
            # - For Mars: Y-axis rotation of ~25° (Mars's axial tilt) aligns satellite orbits
            # - For Uranus: Matching X and Y rotations of 105° creates optimal alignment
            #
            # The need for dual-axis rotation reflects Uranus's unique 3D orientation
            # in space, where its equatorial plane is nearly perpendicular to its orbital plane.

            uranus_tilt = 105  # uranus tilt is 97.77 degrees            
            
            # First apply rotation around x-axis
            x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, np.radians(uranus_tilt), 'x')
            
            # Then apply rotation around y-axis with the same angle
            x_final, y_final, z_final = rotate_points(x_rot1, y_rot1, z_rot1, np.radians(uranus_tilt), 'y')
            
            print(f"Transformation applied: Uranus with X and Y rotations of {uranus_tilt}°", flush=True)
            
            # This transformation was determined by testing and provides the best visual alignment
            # between the Keplerian orbits and the actual orbits of Uranian satellites

        elif parent_planet == 'Neptune':
            if satellite_name == 'Triton':
                # Special transformation for Triton, Neptune's largest moon
                # Triton's orbital elements are defined relative to Neptune's equatorial plane
                # To transform to ecliptic coordinates, we use Neptune's pole orientation
                
                # Step 1: Rotate around z-axis by Neptune's pole Right Ascension
                # This aligns the x-axis with the line of nodes (intersection of Neptune's equator and the ecliptic)
                ra_pole = np.radians(planet_poles['Neptune']['ra'])
                x_rot1, y_rot1, z_rot1 = rotate_points(x_temp, y_temp, z_temp, ra_pole, 'z')
                
                # Step 2: Rotate around x-axis by (90° - Neptune's pole Declination)
                # This tilts the orbital plane to match Neptune's equatorial tilt relative to the ecliptic
                dec_pole = np.radians(90 - planet_poles['Neptune']['dec'])
                x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, dec_pole, 'x')
                
                # Step 3: Fine-tuning with a 3° z-axis rotation
                # This small adjustment compensates for reference frame differences between
                # Neptune's pole coordinates and Triton's orbital elements
                x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, np.radians(3), 'z')
                
                print(f"Transformation applied: Triton with Neptune pole orientation + 3° z-axis adjustment", flush=True)
            else:
                # Standard transformation for other Neptune satellites
                tilt_rad = np.radians(planet_tilts['Neptune'])
                x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')

        elif parent_planet == 'Pluto':
            # Special case for Pluto's satellites
            # Apply the optimized transformation: X-Tilt->Y-Tilt->Z-105
            
            # Get Pluto's axial tilt
            pluto_tilt = planet_tilts.get('Pluto', -122.53)
            pluto_tilt_rad = np.radians(pluto_tilt)
            
            # 1. X-axis rotation by Pluto's tilt
            x_rotated, y_rotated, z_rotated = rotate_points(x_temp, y_temp, z_temp, pluto_tilt_rad, 'x')
            # 2. Y-axis rotation by Pluto's tilt
            x_rotated, y_rotated, z_rotated = rotate_points(x_rotated, y_rotated, z_rotated, pluto_tilt_rad, 'y')
            # 3. Z-axis rotation by -105 degrees
            z_angle = np.radians(-105)
            x_final, y_final, z_final = rotate_points(x_rotated, y_rotated, z_rotated, z_angle, 'z')
            
            print(f"Transformation applied: Pluto X-Tilt->Y-Tilt->Z-105", flush=True)

        elif parent_planet in planet_tilts:
            # Use recorded tilt for other planets
            tilt_rad = np.radians(planet_tilts[parent_planet])
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
            print(f"Transformation applied: {parent_planet} with tilt={planet_tilts[parent_planet]}°", flush=True)
            
        else:
            # No transformation for planets without tilt data
            x_final, y_final, z_final = x_temp, y_temp, z_temp
            print(f"No transformation applied for {parent_planet} (no tilt data available)", flush=True)
        
        # Create hover text for the orbit
        # Check if epoch exists in orbital_params (from planetary_params)
        # Do this BEFORE the Mars conditional so it's available for all satellites
        epoch_from_data = orbital_params.get('epoch', None)
        
        # Special analytical note for Mars moons with time-varying elements

        if parent_planet == 'Mars' and satellite_name in ['Phobos', 'Deimos']:
            analytical_note = (
                "<br><br><i>Analytical orbit uses time-varying elements<br>"
                "calculated for this specific date.<br>"
                "<br>Elements updated based on secular variations:<br>"
                "• Apsidal precession (ω changes with time)<br>"
                "• Nodal regression (Ω changes with time)<br>"
                "• Mars equatorial bulge gravitational field effects<br>"
                "• Solar gravitational perturbations<br>"
                "<br>Shows general orbital geometry valid<br>"
                "over months for this epoch.</i>"
            )
            date_str = date.strftime('%Y-%m-%d %H:%M UTC') if date else 'N/A'
            hover_text = (
                f"{satellite_name} Analytical Orbit<br>"
                f"Elements calculated for: {date_str}<br>"
                f"a={a:.6f} AU<br>"
                f"e={e:.6f}<br>"
                f"i={i:.2f}°"
                f"{analytical_note}"
            )

            # Check if epoch exists in orbital_params (from planetary_params)


            # Build orbit label - use epoch from data if it exists
            if epoch_from_data:
                orbit_label = f"{satellite_name} Analytical Orbit (Epoch: {epoch_from_data})"
            else:
                # For Mars moons with time-varying elements, show the calculation date
                epoch_str = date.strftime('%Y-%m-%d') if date else 'epoch'
                orbit_label = f"{satellite_name} Analytical Orbit (Epoch: {epoch_str})"
        
        elif parent_planet == 'Jupiter' and satellite_name in ['Io', 'Europa', 'Ganymede', 'Callisto', 
                                                                'Metis', 'Adrastea', 'Amalthea', 'Thebe']:
            # Special analytical note for Jupiter moons with time-varying elements
            analytical_note = (
                "<br><br><i>Analytical orbit uses mean elements<br>"
                "in Jupiter equatorial frame.<br>"
                "<br>Mean orbital parameters account for:<br>"
                "• Jupiter equatorial bulge gravitational field (oblateness)<br>"
                "• Time-averaged perturbations<br>"
                "• Orbital precession effects<br>"
                "• Other Galilean moon interactions<br>"
                "<br>Transformed from Jupiter equatorial<br>"
                "to ecliptic frame (+3.13° tilt).<br>"
                "<br>Shows time-averaged orbital geometry<br>"
                "valid over orbital periods.</i>"
            )
            date_str = date.strftime('%Y-%m-%d %H:%M UTC') if date else 'N/A'
            hover_text = (
                f"{satellite_name} Analytical Orbit<br>"
                f"Mean elements (Jupiter equatorial frame)<br>"
                f"Calculation date: {date_str}<br>"
                f"a={a:.6f} AU<br>"
                f"e={e:.6f}<br>"
                f"i={i:.2f}° (before transform)"
                f"{analytical_note}"
            )
            
            # Build orbit label
            if epoch_from_data:
                orbit_label = f"{satellite_name} Analytical Orbit (Epoch: {epoch_from_data})"
            else:
                # For Jupiter moons with time-varying elements, don't show epoch (mean elements)
                orbit_label = f"{satellite_name} Analytical Orbit"
        
        else:
            # All other satellites - use epoch from data if it exists
            if epoch_from_data:
                # Epoch exists in data - use it
                hover_text = f"{satellite_name} Analytical Orbit<br>Epoch: {epoch_from_data}<br>a={a:.6f} AU<br>e={e:.6f}<br>i={i:.2f}°"
                orbit_label = f"{satellite_name} Analytical Orbit (Epoch: {epoch_from_data})"
            else:
                # No epoch in data - don't show one
                hover_text = f"{satellite_name} Analytical Orbit<br>a={a:.6f} AU<br>e={e:.6f}<br>i={i:.2f}°"
                orbit_label = f"{satellite_name} Analytical Orbit"

        # Add the orbit trace to the figure
        fig.add_trace(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='lines',
                line=dict(dash='dot', width=1, color=color),
                name=orbit_label,
                text=[hover_text] * len(x_final),
                customdata=[hover_text] * len(x_final),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )

        # Add markers at key points
        # Get semi-major axis in km for distance calculations        
        # Convert semi-major axis from AU to km
        a_km = a * 149597870.7  # 1 AU = 149,597,870.7 km
        
        # Find periapsis (closest approach to parent)
        periapsis_idx = np.argmin(r)
        
        # Prepare orbital parameters for apsidal markers
        orbital_params = planetary_params[satellite_name]
        
        # Add periapsis marker with proper date calculation
        if show_apsidal_markers:  # ADD THIS CONDITION
            add_perihelion_marker(
                fig,
                x_final[periapsis_idx],
                y_final[periapsis_idx],
                z_final[periapsis_idx],
                satellite_name,
                a,
                e,
                date if date else datetime.now(),
                current_position,
                orbital_params,
                lambda x: color,  # Simple color function
                q=r[periapsis_idx], # Pass the periapsis distance
                center_body=parent_planet  # Use parent planet for terminology
            )

        # Find apoapsis (farthest point from parent)
        apoapsis_idx = np.argmax(r)
        
        # Add apoapsis marker with proper date calculation
        if show_apsidal_markers:  # ADD THIS CONDITION
            add_apohelion_marker(
                fig,
                x_final[apoapsis_idx],
                y_final[apoapsis_idx],
                z_final[apoapsis_idx],
                satellite_name,
                a,
                e,
                date if date else datetime.now(),
                current_position,
                orbital_params,
                lambda x: color,  # Simple color function
                center_body=parent_planet  # Use parent planet for terminology
            )
        
        return fig
    
    except Exception as e:
        print(f"Error plotting {satellite_name} orbit: {e}", flush=True)
        return fig

# Add this function to idealized_orbits.py

def calculate_moon_orbital_elements(date):
    """
    Calculate Moon's orbital elements for a specific date
    Using time-varying mean elements with major perturbations
    
    Parameters:
        date (datetime): Date for which to calculate elements
        
    Returns:
        dict: Dictionary containing orbital elements {a, e, i, omega, Omega}
    """
    # Calculate Julian centuries since J2000.0
    j2000 = datetime(2000, 1, 1, 12, 0, 0)  # J2000.0 epoch
    T = (date - j2000).total_seconds() / (36525.0 * 86400.0)  # Julian centuries
    
    # Mean orbital elements with secular variations
    # These values are from JPL and are relative to the ecliptic
    a = 0.002570  # AU (384,400 km) - relatively stable
    
    # Base eccentricity with secular variation
    e_base = 0.0549  # Mean eccentricity
    
    # Inclination to ecliptic (not Earth's equator!)
    i = 5.145  # degrees - mean inclination to ecliptic
    
    # Node regression (retrograde motion)
    # The Moon's node completes one cycle in about 18.6 years
    Omega = 125.08 - 0.0529538083 * (date - j2000).days  # degrees/day
    
    # Apsidal precession
    # The Moon's line of apsides completes one cycle in about 8.85 years  
    omega = 318.15 + 0.1643573223 * (date - j2000).days  # degrees/day
    
    # Calculate perturbations for more accuracy
    # Days since J2000
    d = (date - j2000).days
    
    # Mean anomalies
    M_moon = (134.963 + 13.064993 * d) % 360  # Moon's mean anomaly
    M_sun = (357.529 + 0.98560028 * d) % 360   # Sun's mean anomaly
    D = (297.850 + 12.190749 * d) % 360        # Mean elongation
    
    # Convert to radians
    M_moon_rad = np.radians(M_moon)
    M_sun_rad = np.radians(M_sun)
    D_rad = np.radians(D)
    
    # Apply perturbations to eccentricity
    # Evection (largest perturbation)
    e_evection = 0.01098 * np.cos(2*D_rad - M_moon_rad)
    e = e_base + e_evection
    
    # Ensure physical bounds
    e = max(0.026, min(e, 0.077))
    
    # Normalize angles
    omega = omega % 360.0
    Omega = Omega % 360.0
    
    return {
        'a': a,
        'e': e,
        'i': i,
        'omega': omega,
        'Omega': Omega
    }


def plot_mars_moon_osculating_orbit(fig, satellite_name, horizons_id, date, color, parent_planet='Mars'):
    """
    Plot osculating orbit for Mars satellites (Phobos/Deimos)
    Similar to Moon's osculating orbit implementation
    
    Parameters:
        fig: Plotly figure object
        satellite_name: Name of satellite ('Phobos' or 'Deimos')
        horizons_id: JPL Horizons ID for the satellite
        date: datetime object for the epoch
        color: Color for the orbit line
        parent_planet: Name of parent planet (should be 'Mars')
        
    Returns:
        fig: Updated Plotly figure
    """

    print(f"\n[OSCULATING] Fetching elements for {satellite_name}...", flush=True)
    
    # Load from cache (pre-fetch already prompted user, so just use cache)
    from osculating_cache_manager import load_cache
    cache = load_cache()
    
    # Check if we have cached elements
    if satellite_name in cache:
#        osc_elements = cache[satellite_name]
        osc_elements = cache[satellite_name]['elements']  # Access 'elements' sub-dict
        print(f"  Using cached osculating elements", flush=True)

    else:
        print(f"  Warning: No osculating elements in cache for {satellite_name}", flush=True)
        return fig
    
    # Extract elements
    a_osc = osc_elements['a']
    e_osc = osc_elements['e']
    i_osc = osc_elements['i']
    omega_osc = osc_elements['omega']
    Omega_osc = osc_elements['Omega']
    epoch_osc = osc_elements.get('epoch', 'N/A')
    
    print(f"\n[OSCULATING] {satellite_name} orbital elements:", flush=True)
    print(f"  Epoch: {epoch_osc}", flush=True)
    print(f"  a = {a_osc:.6f} AU", flush=True)
    print(f"  e = {e_osc:.6f}", flush=True)
    print(f"  i = {i_osc:.2f}°", flush=True)
    print(f"  ω = {omega_osc:.2f}°", flush=True)
    print(f"  Ω = {Omega_osc:.2f}°", flush=True)
    
    # Generate orbit points (full orbit)
    theta = np.linspace(0, 2*np.pi, 360)
    
    # Calculate radius for each point
    r_osc = a_osc * (1 - e_osc**2) / (1 + e_osc * np.cos(theta))
    
    # Convert to Cartesian coordinates in orbital plane
    x_orbit_osc = r_osc * np.cos(theta)
    y_orbit_osc = r_osc * np.sin(theta)
    z_orbit_osc = np.zeros_like(theta)
    
    # Apply orbital element rotations
    i_rad_osc = np.radians(i_osc)
    omega_rad_osc = np.radians(omega_osc)
    Omega_rad_osc = np.radians(Omega_osc)
    
# Standard orbital rotation sequence
    # NOTE: JPL osculating elements for Mars satellites come in ECLIPTIC frame (i ≈ 27°)
    # This is DIFFERENT from analytical elements which are in Mars equatorial frame (i ≈ 1-2°)
    # Therefore we do NOT apply the Mars Y-rotation here!
    
    # 1. Rotate by argument of periapsis (ω) around z-axis
    x_temp, y_temp, z_temp = rotate_points(x_orbit_osc, y_orbit_osc, z_orbit_osc, omega_rad_osc, 'z')
    # 2. Rotate by inclination (i) around x-axis  
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad_osc, 'x')
    # 3. Rotate by longitude of ascending node (Ω) around z-axis
    x_final_osc, y_final_osc, z_final_osc = rotate_points(x_temp, y_temp, z_temp, Omega_rad_osc, 'z')
    
    # NO Mars Y-rotation needed - elements are already in ecliptic frame!
    print(f"  Note: Osculating elements are in ecliptic frame (i={i_osc:.2f}°), no Mars rotation applied", flush=True)
    
    # Create hover text
    date_str = date.strftime('%Y-%m-%d %H:%M UTC')
    osculating_note = (
        "<br><br><i>Osculating orbit uses instantaneous elements<br>"
        "from JPL Horizons at specific epoch.<br>"
        "Shows exact orbital state at epoch time.<br>"
        "<br>Incorporates all physical effects:<br>"
        "• Mars equatorial bulge gravitational field<br>"
        "• Solar perturbations<br>"
        "• Tidal effects<br>"
        "• N-body gravitational interactions</i>"
    )
    hover_text_osc = (
        f"{satellite_name} Osculating Orbit<br>"
        f"Epoch: {epoch_osc}<br>"
        f"a={a_osc:.6f} AU<br>"
        f"e={e_osc:.6f}<br>"
        f"i={i_osc:.2f}°"
        f"{osculating_note}"
    )
    
    # Add osculating trace (dashed line)
    fig.add_trace(
        go.Scatter3d(
            x=x_final_osc,
            y=y_final_osc,
            z=z_final_osc,
            mode='lines',
            line=dict(dash='dash', width=2, color=color),
            name=f"{satellite_name} Osculating Orbit (Epoch: {epoch_osc})",
            text=[hover_text_osc] * len(x_final_osc),
            customdata=[hover_text_osc] * len(x_final_osc),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    print(f"  ✓ Added osculating orbit trace for {satellite_name}", flush=True)
    
    return fig


def plot_moon_ideal_orbit(fig, date, center_object_name='Earth', color=None, days_to_plot=None, 
                          current_position=None, show_apsidal_markers=False, planetary_params=None): 

    """
    Plot BOTH the Moon's analytical and osculating orbits for educational comparison.
    
    Parameters:
        fig: Plotly figure object
        date: datetime object for the calculation epoch
        center_object_name: Name of the central body (should be 'Earth' for Moon)
        color: Color for the orbit line
        days_to_plot: Number of days to plot
        current_position: Dict with 'x', 'y', 'z' keys for current position
        planetary_params: Dictionary containing osculating elements (if available)
    """
    
    # Debug: Show current position if provided
    if current_position:
        print(f"[INFO] Moon current position: x={current_position['x']:.6f}, y={current_position['y']:.6f}, z={current_position['z']:.6f} AU", flush=True)    

    # Use default Moon color if not specified
    if color is None:
        from constants_new import color_map
        color = color_map('Moon')
    
    # Calculate angular range based on days_to_plot
    if days_to_plot is not None and days_to_plot > 0:
        # Get Moon's orbital period from constants
        moon_period_days = KNOWN_ORBITAL_PERIODS.get('Moon', 27.321661)
        orbital_fraction = days_to_plot / moon_period_days
        max_angle = 2 * np.pi * orbital_fraction
    else:
        # Default to one complete orbit
        max_angle = 2 * np.pi
        orbital_fraction = 1.0
    
    # Generate the orbit points
    if orbital_fraction < 1:
        num_points = max(180, int(360 * orbital_fraction))
    else:
        num_points = int(360 * max(1, orbital_fraction))
        num_points = min(num_points, 7200)
    
    theta = np.linspace(0, max_angle, num_points)
    
    # ==================== PLOT ANALYTICAL ORBIT ====================
    # Always plot the analytical orbit (time-averaged elements)
    analytical_elements = calculate_moon_orbital_elements(date)
    
    a_ana = analytical_elements['a']
    e_ana = analytical_elements['e']
    i_ana = analytical_elements['i']
    omega_ana = analytical_elements['omega']
    Omega_ana = analytical_elements['Omega']
    
    print(f"\n[ANALYTICAL] Moon orbital elements for {date.strftime('%Y-%m-%d')}:", flush=True)
    print(f"  a = {a_ana:.6f} AU", flush=True)
    print(f"  e = {e_ana:.6f}", flush=True)
    print(f"  i = {i_ana:.2f}°", flush=True)
    print(f"  ω = {omega_ana:.2f}°", flush=True)
    print(f"  Ω = {Omega_ana:.2f}°", flush=True)
    
    # Calculate analytical orbit
    r_ana = a_ana * (1 - e_ana**2) / (1 + e_ana * np.cos(theta))
    x_orbit_ana = r_ana * np.cos(theta)
    y_orbit_ana = r_ana * np.sin(theta)
    z_orbit_ana = np.zeros_like(theta)
    
    # Apply rotations for analytical orbit
    i_rad_ana = np.radians(i_ana)
    omega_rad_ana = np.radians(omega_ana)
    Omega_rad_ana = np.radians(Omega_ana)
    
    x_temp, y_temp, z_temp = rotate_points(x_orbit_ana, y_orbit_ana, z_orbit_ana, omega_rad_ana, 'z')
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad_ana, 'x')
    x_final_ana, y_final_ana, z_final_ana = rotate_points(x_temp, y_temp, z_temp, Omega_rad_ana, 'z')
    
    # Create hover text for analytical orbit
    date_str = date.strftime('%Y-%m-%d %H:%M UTC')

    analytical_note = (
        "<br><br><i>Analytical orbit uses time-varying elements<br>"
        "calculated for this specific date.<br>"
        "<br>Elements updated based on secular variations:<br>"
        "• Apsidal precession (ω changes with time)<br>"
        "• Nodal regression (Ω changes with time)<br>"
        "• Solar gravitational perturbations<br>"
        "• Earth's gravitational effects<br>"
        "<br>Shows general orbital geometry valid<br>"
        "over months for this epoch.</i>"
    )

    hover_text_ana = f"Moon Analytical Orbit<br>Date: {date_str}<br>a={a_ana:.6f} AU<br>e={e_ana:.6f}<br>i={i_ana:.2f}°{analytical_note}"
    
    # Add analytical trace
    fig.add_trace(
        go.Scatter3d(
            x=x_final_ana,
            y=y_final_ana,
            z=z_final_ana,
            mode='lines',
            line=dict(dash='dot', width=2, color=color),
            name=f"Moon Analytical Orbit (Epoch: {date.strftime('%Y-%m-%d')})",
            text=[hover_text_ana] * len(x_final_ana),
            customdata=[hover_text_ana] * len(x_final_ana),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # ==================== PLOT OSCULATING ORBIT (if available) ====================
        
    if planetary_params is not None:
        # planetary_params is already the Moon's elements dict (not the full dict)
        osc_elements = planetary_params

        a_osc = osc_elements['a']
        e_osc = osc_elements['e']
        i_osc = osc_elements['i']
        omega_osc = osc_elements['omega']
        Omega_osc = osc_elements['Omega']
        epoch_osc = osc_elements.get('epoch', 'N/A')
        
        print(f"\n[OSCULATING] Moon orbital elements:", flush=True)
        print(f"  Epoch: {epoch_osc}", flush=True)
        print(f"  a = {a_osc:.6f} AU", flush=True)
        print(f"  e = {e_osc:.6f}", flush=True)
        print(f"  i = {i_osc:.2f}°", flush=True)
        print(f"  ω = {omega_osc:.2f}°", flush=True)
        print(f"  Ω = {Omega_osc:.2f}°", flush=True)
        
        # Calculate osculating orbit
        r_osc = a_osc * (1 - e_osc**2) / (1 + e_osc * np.cos(theta))
        x_orbit_osc = r_osc * np.cos(theta)
        y_orbit_osc = r_osc * np.sin(theta)
        z_orbit_osc = np.zeros_like(theta)
        
        # Apply rotations for osculating orbit
        i_rad_osc = np.radians(i_osc)
        omega_rad_osc = np.radians(omega_osc)
        Omega_rad_osc = np.radians(Omega_osc)
        
        x_temp, y_temp, z_temp = rotate_points(x_orbit_osc, y_orbit_osc, z_orbit_osc, omega_rad_osc, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad_osc, 'x')
        x_final_osc, y_final_osc, z_final_osc = rotate_points(x_temp, y_temp, z_temp, Omega_rad_osc, 'z')
        
        # Create hover text for osculating orbit
        osculating_note = (
            "<br><br><i>Osculating orbit 'kisses' actual position at epoch,<br>"
            "then diverges as perturbations accumulate from:<br>"
            "• Solar gravity (largest effect)<br>"
            "• Earth's oblateness (J2 - equatorial bulge)<br>"
            "  causes nodal precession (Ω rotates ~19.3°/yr)<br>"
            "• Tidal forces<br>"
            "<br>It fits only the present position, not past or future positions.<br>"
            "<br>See 'Orbital Parameter Visualization' for equatorial bulge details</i>"
        )
        hover_text_osc = f"Moon Osculating Orbit<br>Epoch: {epoch_osc}<br>a={a_osc:.6f} AU<br>e={e_osc:.6f}<br>i={i_osc:.2f}°{osculating_note}"
        
        # Add osculating trace with different line style
        fig.add_trace(
            go.Scatter3d(
                x=x_final_osc,
                y=y_final_osc,
                z=z_final_osc,
                mode='lines',
                line=dict(dash='dash', width=2, color=color),  # Dashed line to distinguish from analytical
                name=f"Moon Osculating Orbit (Epoch: {epoch_osc})",
                text=[hover_text_osc] * len(x_final_osc),
                customdata=[hover_text_osc] * len(x_final_osc),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    else:
        print(f"[INFO] No osculating elements available for Moon - showing analytical orbit only", flush=True)
    
    # ==================== APSIDAL MARKERS ====================
    if show_apsidal_markers:
        # Use analytical elements for apsidal marker positions
        # Calculate positions using analytical orbit
        r_ana = a_ana * (1 - e_ana**2) / (1 + e_ana * np.cos(theta))
        
        # Find periapsis (closest approach - perigee for Moon)
        periapsis_idx = np.argmin(r_ana)
        
        # Prepare orbital parameters dictionary
        orbital_params = {
            'a': a_ana,
            'e': e_ana,
            'i': i_ana,
            'omega': omega_ana,
            'Omega': Omega_ana
        }
        
        # Add TP if available from analytical elements
        if 'TP' in analytical_elements:
            orbital_params['TP'] = analytical_elements['TP']
        
        # Import standard apsidal marker functions
        from apsidal_markers import add_perihelion_marker, add_apohelion_marker
        
        # Add perigee marker (uses standard function)
        add_perihelion_marker(
            fig,
            x_final_ana[periapsis_idx],
            y_final_ana[periapsis_idx],
            z_final_ana[periapsis_idx],
            'Moon',
            a_ana,
            e_ana,
            date,
            current_position,
            orbital_params,
            lambda x: color,  # Color function
            q=r_ana[periapsis_idx],  # Periapsis distance
            center_body='Earth'  # Will use "Perigee" terminology
        )
        
        # Find apoapsis (farthest point - apogee for Moon)
        apoapsis_idx = np.argmax(r_ana)
        
        # Add apogee marker (uses standard function)
        add_apohelion_marker(
            fig,
            x_final_ana[apoapsis_idx],
            y_final_ana[apoapsis_idx],
            z_final_ana[apoapsis_idx],
            'Moon',
            a_ana,
            e_ana,
            date,
            current_position,
            orbital_params,
            lambda x: color,  # Color function
            center_body='Earth'  # Will use "Apogee" terminology
        )
    
    return fig


def generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points, max_distance=100):
    """
    Generate points for a hyperbolic orbit trajectory.
    Enhanced to handle very high eccentricity cases.
    
    Parameters:
        a: Semi-major axis (negative for hyperbolic orbits)
        e: Eccentricity (> 1 for hyperbolic orbits)
        i: Inclination in degrees
        omega: Argument of perihelion in degrees
        Omega: Longitude of ascending node in degrees
        rotate_points: Function to rotate points
        max_distance: Maximum distance from Sun to plot (AU)
    
    Returns:
        tuple: (x_final, y_final, z_final, q) where q is perihelion distance
    """
    # Calculate perihelion distance
    q = abs(a) * (e - 1)
    
    # For hyperbolic orbits, the true anomaly range is limited
    theta_inf = np.arccos(-1/e)  # Asymptotic true anomaly
    
    # For very high eccentricity, we need special handling
    if e > 5:
        # High eccentricity: focus on the visible region
        # Calculate the true anomaly where r = max_distance
        # r = a(e^2 - 1) / (1 + e*cos(theta))
        # Solving for theta: cos(theta) = (a(e^2 - 1)/r - 1) / e
        
        cos_theta_max = ((abs(a) * (e**2 - 1) / max_distance) - 1) / e
        
        if cos_theta_max >= -1 and cos_theta_max <= 1:
            theta_visible = np.arccos(cos_theta_max)
            # Use the smaller angle
            theta_limit = min(theta_inf - 0.01, theta_visible)
        else:
            # Very extreme case - just show near perihelion
            theta_limit = min(theta_inf - 0.01, np.pi/4)  # Max 45 degrees
        
        # Use more points for smoother curve
        num_points = 1000
    else:
        # Standard approach for moderate eccentricity
        theta_limit = theta_inf - 0.1  # Use 0.1 radian margin
        num_points = 500
    
    # Create array of true anomaly values
    theta = np.linspace(-theta_limit, theta_limit, num_points)
    
    # Calculate radius for each true anomaly
    r = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta))
    
    # Filter out points that are too far from the Sun
    valid_mask = (r > 0) & (r <= max_distance)
    
    # Check if we have enough valid points
    if np.sum(valid_mask) < 50:
        # If too few points, focus on perihelion region
        if e > 10:
            # For extremely high eccentricity, use very small angle range
            theta_perihelion = np.linspace(-0.05, 0.05, 200)  # ±2.9 degrees
        else:
            # For high eccentricity, use small angle range
            theta_perihelion = np.linspace(-np.pi/6, np.pi/6, 500)  # ±30 degrees
        
        r_perihelion = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta_perihelion))
        valid_perihelion = (r_perihelion > 0) & (r_perihelion <= max_distance * 1.5)
        
        if np.sum(valid_perihelion) > 10:
            theta = theta_perihelion[valid_perihelion]
            r = r_perihelion[valid_perihelion]
        else:
            # Last resort: just create a small arc at perihelion
            print(f"Warning: Extremely high eccentricity (e={e:.6f}), showing minimal trajectory", flush=True)
            theta = np.linspace(-0.01, 0.01, 20)
            r = abs(a) * (e**2 - 1) / (1 + e * np.cos(theta))
    else:
        theta = theta[valid_mask]
        r = r[valid_mask]
    
    # Convert to Cartesian coordinates in orbital plane
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta)
    z_orbit = np.zeros_like(theta)
    
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Apply orbital element rotations
    x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
    
    return x_final, y_final, z_final, q

def plot_idealized_orbits(fig, objects_to_plot, center_id='Sun', objects=None, 
                          planetary_params=None, parent_planets=None, color_map=None, 
                          date=None, days_to_plot=None, current_positions=None, fetch_position=None, 
                          show_apsidal_markers=False, parent_window=None):
    """
    Plot Keplerian orbits for planets, dwarf planets, asteroids, KBOs, and moons.
    For non-Sun centers, only plots moons of that center body.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add orbits to
        objects_to_plot (list): List of object names to potentially plot orbits for
        center_id (str): The central body ('Sun' or a planet name)
        objects (list): List of object dictionaries with metadata
        planetary_params (dict): Dictionary of orbital parameters for each object
        parent_planets (dict): Dictionary mapping parent planets to their satellites
        color_map (callable): Function to get color for an object by name
        date (datetime): Date for time-varying orbital elements (used for Moon)
        
    Returns:
        plotly.graph_objects.Figure: Figure with Keplerian orbits added
    """
    # CRITICAL: Import numpy at the function level
    import numpy as np
    import plotly.graph_objects as go
    from datetime import datetime, timedelta

    # Create name to object mapping
    obj_dict = {obj['name']: obj for obj in objects} if objects else {}

    # If current_positions not provided, try to extract from objects parameter
    if current_positions is None and objects is not None:
        current_positions = {}
        for obj in objects:
            if hasattr(obj, 'name') and hasattr(obj, 'x') and hasattr(obj, 'y') and hasattr(obj, 'z'):
                current_positions[obj.name] = {
                    'x': obj.x,
                    'y': obj.y, 
                    'z': obj.z
                }

    # Track skipped objects by category
    skipped = {
        'satellites': [],
        'comets': [],
        'missions': [],
        'no_params': [],
        'invalid_orbit': [],
        'error': []  # ADD THIS LINE
    }

    plotted = []

    # If days_to_plot not provided, try to get from GUI
    if days_to_plot is None:
#        try:
#            days_to_plot = int(days_to_plot_entry.get())
#        except:
        days_to_plot = 365  # Default fallback

    # Add date parameter default
    if date is None:
        from datetime import datetime
        date = datetime.now()

    # If objects parameter is None, handle gracefully
    if objects is None:
        print("Warning: objects list is None, cannot determine object properties", flush=True)
        return fig
        
    # If planetary_params is None, handle gracefully
    if planetary_params is None:
        print("Warning: planetary_params is None, cannot plot Keplerian orbits", flush=True)
        return fig
        
    # If parent_planets is None, handle gracefully
    if parent_planets is None:
        print("Warning: parent_planets is None, cannot determine satellite relationships", flush=True)
        return fig
        
    # If color_map is None, use a default function
    if color_map is None:
        from constants_new import color_map       

    # In the section where we plot satellites of the center object:
    if center_id != 'Sun':
        # Get list of moons for this center
        moons = parent_planets.get(center_id, [])
        
        # Filter objects_to_plot to only include moons of this center
        objects_to_plot = [obj for obj in objects_to_plot if obj in moons]
        
        # For each satellite of the center object
        for moon_name in objects_to_plot:
            # Find the object in the objects list
            moon_info = next((obj for obj in objects if obj['name'] == moon_name), None)
            if moon_info is None:
                continue
                 
            # Special handling for Earth's Moon with time-varying elements
            if moon_name == 'Moon' and center_id == 'Earth':
                # Get Moon's current position from current_positions
                moon_current_pos = current_positions.get('Moon') if current_positions else None
                moon_params = planetary_params.get('Moon') if planetary_params else None

                fig = plot_moon_ideal_orbit(fig, date, center_id, color_map(moon_name), days_to_plot,
                                            current_position=moon_current_pos,
                                            show_apsidal_markers=show_apsidal_markers,
                                            planetary_params=moon_params)

            # Special handling for Mars moons with dual-orbit system
            elif moon_name in ['Phobos', 'Deimos'] and center_id == 'Mars':
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None
                
                # Plot analytical orbit (time-varying elements - dotted line)
                fig = plot_satellite_orbit(
                    moon_name, 
                    planetary_params,
                    center_id, 
                    color_map(moon_name), 
                    fig,
                    date=date,
                    days_to_plot=days_to_plot,
                    current_position=satellite_current_pos,
                    show_apsidal_markers=show_apsidal_markers
                )
                                
                # Plot osculating orbit (JPL elements - dashed line)
                # Get Horizons ID from objects list
                horizons_id = None
                for obj in objects:
                    if obj['name'] == moon_name:
                        horizons_id = obj.get('id')
                        break
                
                if horizons_id and date:
                    fig = plot_mars_moon_osculating_orbit(
                        fig,
                        moon_name,
                        horizons_id,
                        date,
                        color_map(moon_name),
                        parent_planet='Mars'
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing ID or date)", flush=True)

            # Special handling for Jupiter moons with dual-orbit system
            elif moon_name in JUPITER_MOONS and center_id == 'Jupiter':
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None
                
                # Plot analytical orbit (time-varying elements - dotted line)
                fig = plot_satellite_orbit(
                    moon_name, 
                    planetary_params,
                    center_id, 
                    color_map(moon_name), 
                    fig,
                    date=date,
                    days_to_plot=days_to_plot,
                    current_position=satellite_current_pos,
                    show_apsidal_markers=show_apsidal_markers
                )
                
                # Plot osculating orbit (JPL elements - dashed line)
                if date:
                    fig = plot_jupiter_moon_osculating_orbit(
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)

# Special handling for Saturn moons with dual-orbit system
            elif moon_name in SATURN_MOONS and center_id == 'Saturn':
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None
                
                # DECISION: Skip analytical orbits for Saturn moons
                # Saturn's pole orientation (RA=40.58°) is far from ecliptic pole (~270°),
                # making reference frame transformation complex. Osculating elements from
                # JPL are already in ecliptic frame and provide excellent alignment.
                # See: SATURN_IMPLEMENTATION_HANDOFF.md for technical details.
                
                # Special handling for Daphnis - no ephemeris after 2018
                if moon_name == 'Daphnis':
                    print(f"  [DAPHNIS] ⚠ JPL ephemeris ends 2018-01-17 (Cassini mission end)", flush=True)
                    print(f"  [DAPHNIS] Limited orbital data - osculating orbit may not be available", flush=True)
                
                # Plot osculating orbit ONLY (JPL elements - dashed line, already ecliptic)
                if date:
                    fig = plot_saturn_moon_osculating_orbit(
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)

# Special handling for Uranus moons with osculating-only system
            elif moon_name in URANUS_MOONS and center_id == 'Uranus':
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None
                
                # DECISION: Skip analytical orbits for Uranus moons
                # Uranus's extreme axial tilt (97.77°) makes reference frame transformation
                # extremely complex. Osculating elements from JPL are already in ecliptic
                # frame and provide excellent alignment.
                # See: SATELLITE_DUAL_ORBIT_HANDOFF.md for technical details.
                
                # Plot osculating orbit ONLY (JPL elements - dashed line, already ecliptic)
                if date:
                    fig = plot_uranus_moon_osculating_orbit(
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)

# Special handling for Neptune moons with osculating-only system
            elif moon_name in NEPTUNE_MOONS and center_id == 'Neptune':
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None
                
                # DECISION: Skip analytical orbits for Neptune moons
                # Neptune's pole RA (299.36°) and Triton's retrograde orbit make
                # analytical transformations complex. Osculating elements from JPL
                # are already in ecliptic frame and handle retrograde automatically.
                # See: SATELLITE_DUAL_ORBIT_HANDOFF.md for technical details.
                
                # Plot osculating orbit ONLY (JPL elements - dashed line, already ecliptic)
                if date:
                    fig = plot_neptune_moon_osculating_orbit(
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)

# Special handling for Pluto-Charon BINARY SYSTEM
            # Two modes: traditional Pluto-centered, or barycenter-centered
            
            # Mode 1: Barycenter-centered (binary planet mode)
        #    if center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:
            elif center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:
                # In barycenter mode, BOTH Pluto and Charon orbit the barycenter
                # Plus the four smaller moons (Styx, Nix, Kerberos, Hydra)
                if date:
                    fig = plot_pluto_barycenter_orbit(
                        fig,
                        moon_name,  # Can be 'Pluto', 'Charon', or other moons
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers,
                        center_id=center_id  # ADD THIS
                    )

                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)
            
            # Mode 2: Traditional Pluto-centered (for compatibility)
            elif moon_name in PLUTO_MOONS and center_id == 'Pluto':
                # Skip analytical orbit - only plot osculating
                # (Pluto pole RA=132.99° far from ecliptic, analytical transformations fail)
                if date:
                    fig = plot_pluto_barycenter_orbit(
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers,
                        center_id=center_id  # ADD THIS
                    )

                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)
                
                # Add barycenter marker for Pluto-centered view (once, after processing Charon)
                if moon_name == 'Charon':
                    charon_pos = current_positions.get('Charon') if current_positions else None
                    fig = add_pluto_barycenter_marker(fig, date, charon_position=charon_pos)

            # Special handling for TNO satellites (Eris, Haumea, Makemake moons)
            # These have no reliable analytical elements - osculating only
            elif moon_name in TNO_MOONS:
                if date:
                    fig = plot_tno_satellite_orbit(
                        fig,
                        moon_name,
                        center_id,  # parent name
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)

            else:
                # Use the standard satellite plotting function for other moons
                # Get satellite's current position
                satellite_current_pos = current_positions.get(moon_name) if current_positions else None

                fig = plot_satellite_orbit(
                    moon_name, 
                    planetary_params,
                    center_id, 
                    color_map(moon_name), 
                    fig,
                    date=date,
                    days_to_plot=days_to_plot,
                    current_position=satellite_current_pos,
                    show_apsidal_markers=show_apsidal_markers
                )
                        
            plotted.append(moon_name)
        
        # COMPLETE CODE: Add After Line 2323 in Keplerian_orbits.py
        # This version loads TP from osculating_cache.json for satellites

        # ========== ADD ACTUAL APSIDAL MARKERS FOR ALL SATELLITES ==========
        if show_apsidal_markers and fetch_position:
            print("\n[ACTUAL APSIDAL] Checking satellites for apsidal markers...", flush=True)
            
            from apsidal_markers import (
                fetch_positions_for_apsidal_dates,
                add_actual_apsidal_markers_enhanced,
                calculate_exact_apsides,
                compute_apsidal_dates_from_tp
            )
            from datetime import timedelta
            import json
            from pathlib import Path
            from astropy.time import Time
            
            # Load osculating cache once for all satellites
            osc_cache = {}
            try:
                cache_path = Path('data/osculating_cache.json')
                if cache_path.exists():
                    with open(cache_path, 'r') as f:
                        osc_cache = json.load(f)
            except Exception as e:
                print(f"  ⚠ Could not load osculating cache: {e}")
            
            for moon_name in plotted:
                moon_info = next((obj for obj in objects if obj['name'] == moon_name), None)
                
                if moon_info and moon_info.get('object_type') == 'satellite':
                    moon_params = planetary_params.get(moon_name)
                    
                    if moon_params:

# For satellites, get TP and epoch from osculating cache if not in params
                        if 'TP' not in moon_params and moon_name in osc_cache:
                            try:
                                osc_elements = osc_cache[moon_name].get('elements', {})
                                if 'TP' in osc_elements:
                                    tp_jd = osc_elements['TP']
                                    tp_time = Time(tp_jd, format='jd')
                                    moon_params['TP'] = tp_time.datetime.strftime('%Y-%m-%d %H:%M:%S')
                                    print(f"  Loaded TP from osculating cache for {moon_name}: {moon_params['TP']}")
                                # ALSO load epoch from osculating cache
                                if 'epoch' in osc_elements:
                                    moon_params['epoch'] = osc_elements['epoch']
                                    print(f"  Loaded epoch from osculating cache for {moon_name}: {moon_params['epoch']}")
                            except Exception as e:
                                print(f"  Could not load TP/epoch for {moon_name}: {e}")
                        
                        if 'TP' in moon_params:
                            obj_id = moon_info.get('id')
                            id_type = moon_info.get('id_type', None)
                            
                            if obj_id:
                                try:
                                    print(f"\n[ACTUAL APSIDAL] Processing {moon_name}", flush=True)
                                    print(f"  Object ID: {obj_id}", flush=True)
                                    print(f"  Center: {center_id}", flush=True)
                                    
                                    # Compute apsidal dates from TP
                                    next_periapsis, next_apoapsis = compute_apsidal_dates_from_tp(
                                        moon_name,
                                        moon_params,
                                        current_date=date
                                    )
                                    
                                    # Store dates in params
                                    if next_periapsis:
                                        moon_params['perihelion_dates'] = [next_periapsis.strftime('%Y-%m-%d %H:%M:%S')]
                                        print(f"  Next periapsis: {next_periapsis}")
                                    if next_apoapsis:
                                        moon_params['aphelion_dates'] = [next_apoapsis.strftime('%Y-%m-%d %H:%M:%S')]
                                        print(f"  Next apoapsis: {next_apoapsis}")
                                    
                                    # Calculate Keplerian apsides
                                    apsides = calculate_exact_apsides(
                                        moon_params.get('a'),
                                        moon_params.get('e'),
                                        moon_params.get('i'),
                                        moon_params.get('omega'),
                                        moon_params.get('Omega'),
                                        rotate_points
                                    )
                                    
                                    # Use numeric center ID for satellites
                                    satellite_center_ids = {
                                        'Earth': '399',   # Geocenter
                                        'Mars': '499',    # Mars
                                        'Jupiter': '599', # Jupiter
                                        'Saturn': '699',  # Saturn
                                        'Uranus': '799',  # Uranus
                                        'Neptune': '899', # Neptune
                                        'Pluto': '999'    # Pluto
                                    }
                                    center_id_numeric = satellite_center_ids.get(center_id, center_id)
                                    
                                    # Fetch actual positions
                                    positions_dict = fetch_positions_for_apsidal_dates(
                                        obj_id=obj_id,
                                        params=moon_params,
                                        date_range=None,
                                        center_id=center_id_numeric,  # Use numeric ID!
                                        id_type=id_type,
                                        is_satellite=True,
                                        fetch_position=fetch_position
                                    )
                                    
                                    if positions_dict:
                                        print(f"  Fetched {len(positions_dict)} positions", flush=True)
                                        
                                        add_actual_apsidal_markers_enhanced(
                                            fig,
                                            moon_name,
                                            moon_params,
                                            date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                                            positions_dict=positions_dict,
                                            color_map=color_map,
                                            center_body=center_id,
                                            is_satellite=True,
                                            ideal_apsides=apsides,
                                            filter_by_date_range=False
                                        )
                                        
                                        print(f"  ✓ Added actual apsidal markers for {moon_name}", flush=True)
                                    else:
                                        print(f"  ⚠ No positions fetched for {moon_name}", flush=True)
                                        
                                except Exception as e:
                                    print(f"  ⚠ Error adding actual markers for {moon_name}: {e}", flush=True)
                                    import traceback
                                    traceback.print_exc()
                        else:
                            print(f"  ⚠ {moon_name} has no TP in params or osculating cache", flush=True)

    # If center is the Sun, plot orbits for selected heliocentric objects
    else:
        for obj_name in objects_to_plot:
            # Find the object in the objects list
            obj_info = next((obj for obj in objects if obj['name'] == obj_name), None)
            # Get current position for this object
            current_pos = current_positions.get(obj_name) if current_positions else None
            if obj_info is None:
                continue
                
            # Check each skip condition and record the reason
            if obj_name not in planetary_params:
                skipped['no_params'].append(obj_name)
                continue

            # Check if this is a satellite of another object (but not of the center)
            # Only skip if object_type is 'satellite' - this excludes primary bodies like Pluto
            # which appear in parent_planets['Pluto-Charon Barycenter'] for binary visualization
            is_satellite_of_another = False
            if obj_info.get('object_type') == 'satellite':
                for planet, moons in parent_planets.items():
                    if obj_name in moons and planet != center_id:
                        is_satellite_of_another = True
                        break

            if is_satellite_of_another:
                # Skip satellites when centered on Sun (they orbit their parent, not Sun directly)
                skipped['satellites'].append(obj_name)
                continue

            elif obj_info.get('is_mission', False):
                skipped['missions'].append(obj_name)
                continue
            
# USE THE DATA PASSED FROM MAIN THREAD
            # planetary_params already contains the fresh data from the pre-fetch in palomas_orrery.py
            if obj_name in planetary_params:
                params = planetary_params[obj_name]
                
                a = params.get('a', 0)
                e = params.get('e', 0)
                i = params.get('i', 0)
                omega = params.get('omega', 0)
                Omega = params.get('Omega', 0)
            else:
                # Object not available anywhere
                print(f"⚠ Skipping {obj_name}: No parameters found", flush=True)
                skipped['no_params'].append(obj_name)
                continue

            # Add this debug line
            print(f"\n[DEBUG] Processing {obj_name}", flush=True)
            print(f"[DEBUG] params keys: {params.keys()}", flush=True)            

# Improved code for the hyperbolic section in idealized_orbits.py
# Based on the working pattern from orbital_param_viz.py

# Check if this is a hyperbolic orbit (e > 1)
            if e > 1:
                try:
                    x_final, y_final, z_final, q = generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points)
                    
                    epoch_str = ""
                    if 'epoch' in params:
                        epoch_str = f" (Epoch: {params['epoch']})"

                    # Plot the hyperbolic orbit path
                    fig.add_trace(
                        go.Scatter3d(
                            x=x_final,
                            y=y_final,
                            z=z_final,
                            mode='lines',
                            line=dict(dash='dot', width=1, color=color_map(obj_name)),
                            name=f"{obj_name} Keplerian Orbit{epoch_str}",
                    #        text=[f"{obj_name} Hyperbolic Orbit<br>eccentricity, e={e:.6f}<br>periapsis distance, q={q:.6f} AU"] * len(x_final),
                            text=[f"{obj_name} Hyperbolic Orbit<br>e={e:.6f}<br>q={q:.6f} AU{get_planet_perturbation_note(obj_name)}"] * len(x_final),
                            customdata=[f"{obj_name} Keplerian Orbit"] * len(x_final),
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True                    
                        )
                    )
                  
                    # ========== CALCULATE EXACT PERIAPSIS AT THETA=0 FOR HYPERBOLIC ==========
                    from apsidal_markers import calculate_exact_apsides

                    # Calculate exact apsidal positions (only periapsis for hyperbolic)
                    apsides = calculate_exact_apsides(abs(a), e, i, omega, Omega, rotate_points)

                    # ========== ADD Keplerian PERIAPSIS MARKER ==========
                    if show_apsidal_markers:  # ADD THIS CONDITION
                        if apsides['periapsis']:
                            peri = apsides['periapsis']
                            
                            # Get date from TP for hyperbolic orbits
                            date_str = ""
                            if 'TP' in params:
                                from astropy.time import Time
                                tp_time = Time(params['TP'], format='jd')
                                perihelion_datetime = tp_time.datetime
                                date_str = f"<br>Date: {perihelion_datetime.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                                
                                # Store for later use
                                params['perihelion_datetime'] = perihelion_datetime
                                params['perihelion_dates'] = [perihelion_datetime.strftime('%Y-%m-%d %H:%M:%S')]
                            
                            # Add perturbation assessment for hyperbolic orbits
                            accuracy_note = ""
                            if e > 10:
                                accuracy_note = "<br><i>Note: Extreme eccentricity - strong perturbations expected</i>"
                            elif e > 5:
                                accuracy_note = "<br><i>Note: Very high eccentricity - significant perturbations expected</i>"
                            elif e > 2:
                                accuracy_note = "<br><i>Note: High eccentricity - moderate perturbations expected</i>"
                            else:
                                accuracy_note = "<br><i>Note: Near-parabolic - perturbations possible</i>"
                            
                            hover_text = (
                                f"<b>{obj_name} Keplerian Periapsis</b>"
                                f"{date_str}"
                                f"<br>q={peri['distance']:.6f} AU"
                                f"<br>Theoretical minimum distance (θ=0°)"
                                f"<br>One-time passage (hyperbolic)"
                                f"<br>Unperturbed Keplerian position at actual periapsis time"
                                f"{accuracy_note}"
                            )
                            
                            fig.add_trace(
                                go.Scatter3d(
                                    x=[peri['x']],
                                    y=[peri['y']],
                                    z=[peri['z']],
                                    mode='markers',
                                    marker=dict(
                                        size=6,
                                        color=color_map(obj_name),
                                        symbol='square-open'
                                    ),
                                    name=f"{obj_name} Keplerian Periapsis",
                                    text=[hover_text],
                            #        hoverinfo='text',
                                    customdata=[f"{obj_name} Keplerian Periapsis"],
                                    hovertemplate='%{text}<extra></extra>',                                    
                                    showlegend=True
                                )
                            )
                            print(f"  Added Keplerian periapsis for {obj_name} at distance {peri['distance']:.6f} AU (hyperbolic)", flush=True)
                    
                    # ========== GENERATE ACTUAL PERIHELION DATE FROM TP ==========
                    if 'TP' in params:
                        from datetime import timedelta
                        from astropy.time import Time
                        
                        # For hyperbolic orbits, TP gives us the exact perihelion date and time
                        tp_jd = params['TP']
                        tp_time = Time(tp_jd, format='jd')
                        perihelion_datetime = tp_time.datetime
                        
                        # Store with full precision for display
                        params['perihelion_datetime'] = perihelion_datetime
                        # Store as string for compatibility (with time)
                        params['perihelion_dates'] = [perihelion_datetime.strftime('%Y-%m-%d %H:%M:%S')]
                        print(f"  [HYPERBOLIC] Perihelion: {params['perihelion_dates'][0]} UTC", flush=True)
                    else:
                        print(f"  [HYPERBOLIC] No TP in params for {obj_name}", flush=True)
                    
                    # ========== SIMPLIFIED ACTUAL MARKER FETCHING FOR HYPERBOLIC ==========
                    # This avoids the datetime parsing issues by fetching with date-only
                    if show_apsidal_markers:  # ADD THIS CONDITION
                        if 'perihelion_dates' in params:
                            print(f"\n[DEBUG] Attempting simplified fetch for hyperbolic {obj_name}", flush=True)
                            
                            # Get the full datetime string and extract just the date part
                            perihelion_full = params['perihelion_dates'][0]
                            perihelion_date_only = perihelion_full.split(' ')[0]  # Get just YYYY-MM-DD
                            print(f"  Full datetime: {perihelion_full}", flush=True)
                            print(f"  Date only for fetch: {perihelion_date_only}", flush=True)
                            
                            # Get object ID
                            obj_id = None
                            id_type = None
                            for obj in objects:
                                if obj['name'] == obj_name:
                                    obj_id = obj['id']
                                    id_type = obj.get('id_type', None)
                                    break
                            
                            print(f"  Object ID: {obj_id}, ID type: {id_type}", flush=True)
                            
                            if obj_id and fetch_position:
                                try:
                                    # Create a datetime object with just the date (midnight)
                                    from datetime import datetime
                                    date_obj = datetime.strptime(perihelion_date_only, '%Y-%m-%d')
                                    print(f"  Fetching position for {date_obj}", flush=True)
                                    
                                    # Fetch the position
                                    pos_data = fetch_position(obj_id, date_obj, center_id=center_id, id_type=id_type)
                                    
                                    if pos_data and 'x' in pos_data:
                                        print(f"  SUCCESS: Got position ({pos_data['x']:.3f}, {pos_data['y']:.3f}, {pos_data['z']:.3f})", flush=True)
                                        
                                        # Calculate distance for hover text
                                        import numpy as np
                                        distance_au = np.sqrt(pos_data['x']**2 + pos_data['y']**2 + pos_data['z']**2)
                                        distance_km = distance_au * 149597870.7
                                        
                                        # Manually add the actual perihelion marker
                                        fig.add_trace(
                                            go.Scatter3d(
                                                x=[pos_data['x']],
                                                y=[pos_data['y']],
                                                z=[pos_data['z']],
                                                mode='markers',
                                                marker=dict(
                                                    size=8,
                                                    color='white',
                                                    symbol='square-open'
                                                ),
                                                
                                                name=f"{obj_name} Actual Perihelion",
                                                text=[
                                                    f"<b>{obj_name} at Perihelion (Actual)</b><br>"
                                                    f"Date/Time: {perihelion_full} UTC<br>"
                                                    f"Distance from {center_id}: {distance_au:.6f} AU<br>"
                                                    f"Distance: {distance_km:.0f} km"
                                                ],  # Full hover content in text
                                                customdata=[f"{obj_name} Actual Perihelion"],  # Added customdata
                                                hovertemplate='%{text}<extra></extra>',  # Standard template

                                                showlegend=True
                                            )
                                        )
                                        print(f"  Added actual perihelion marker for {obj_name}", flush=True)
                                    else:
                                        print(f"  WARNING: No position data returned for {obj_name}", flush=True)
                                        print(f"  This might be due to limited ephemeris data for this object", flush=True)
                                        
                                except Exception as e:
                                    print(f"  ERROR fetching position: {e}", flush=True)
                                    print(f"  Error type: {type(e).__name__}", flush=True)
                                    
                                    # If it's still the NoneType * float error, it might be in fetch_position itself
                                    if "NoneType" in str(e) and "float" in str(e):
                                        print(f"  This appears to be the period calculation issue", flush=True)
                                        print(f"  The object may have limited ephemeris data in JPL Horizons", flush=True)
                            else:
                                if not obj_id:
                                    print(f"  Could not find object ID for {obj_name}", flush=True)
                                if not fetch_position:
                                    print(f"  fetch_position function not available", flush=True)
                        
                        plotted.append(obj_name)
                        print(f"Plotted hyperbolic orbit for {obj_name}: e={e:.5f}, q={q:.5f} AU", flush=True)

                except Exception as err:
                    print(f"Error plotting hyperbolic orbit for {obj_name}: {err}", flush=True)
                    import traceback
                    traceback.print_exc()
                    skipped['error'].append(obj_name)
                
                continue  # Skip to next object, don't run elliptical orbit code
            
            # For elliptical orbits (e <= 1), continue with existing code:
            # Generate ellipse in orbital plane
            theta = np.linspace(0, 2*np.pi, 360)  # 360 points for smoothness
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            
            x_orbit = r * np.cos(theta)
            y_orbit = r * np.sin(theta)
            z_orbit = np.zeros_like(theta)

            # Convert angles to radians
            i_rad = np.radians(i)
            omega_rad = np.radians(omega)
            Omega_rad = np.radians(Omega)

            # Rotate ellipse by argument of periapsis (ω) around z-axis
            x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
            # Then rotate by inclination (i) around x-axis
            x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
            # Then rotate by longitude of ascending node (Ω) around z-axis
            x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')

            # ADD THIS CODE to check for epoch
            epoch_str = ""
            if 'epoch' in params:
                epoch_str = f" (Epoch: {params['epoch']})"

            # PLOT THE ORBIT LINE - THIS IS CRITICAL!
            fig.add_trace(
                go.Scatter3d(
                    x=x_final,
                    y=y_final,
                    z=z_final,
                    mode='lines',
                    line=dict(dash='dot', width=1, color=color_map(obj_name)),
                    name=f"{obj_name} Keplerian Orbit{epoch_str}",
            #        text=[f"{obj_name} Keplerian Orbit"] * len(x_final),
                    text=[f"{obj_name} Keplerian Orbit<br>a={a:.6f} AU, e={e:.6f}, i={i:.2f}°{get_planet_perturbation_note(obj_name)}"] * len(x_final),
                    customdata=[f"{obj_name} Keplerian Orbit"] * len(x_final),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True                    
                )
            )

            # ========== CALCULATE EXACT APSIDES AT THETA=0 AND THETA=PI ==========
            from apsidal_markers import calculate_exact_apsides, compute_apsidal_dates_from_tp

            # Calculate exact apsidal positions
            apsides = calculate_exact_apsides(a, e, i, omega, Omega, rotate_points)

            # Get dates for the apsides
            if 'TP' in params:
                next_perihelion, next_aphelion = compute_apsidal_dates_from_tp(
                    obj_name, params, current_date=date
                )
            else:
                next_perihelion = next_aphelion = None

            # ========== ADD Keplerian PERIAPSIS MARKER ==========
            if show_apsidal_markers:  # ADD THIS CONDITION
                if apsides['periapsis']:
                    peri = apsides['periapsis']
                    
                    # Create hover text with date if available
                    date_str = ""
                    if next_perihelion:
                        date_str = f"<br>Date: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                    
                    # Add perturbation assessment
                    accuracy_note = ""
                    if e > 0.15:
                        accuracy_note = "<br><i>Note: High eccentricity - strong perturbations expected</i>"
                    elif e > 0.05:
                        accuracy_note = "<br><i>Note: Moderate eccentricity - perturbations expected</i>"
                    
                    hover_text = (
                        f"<b>{obj_name} Keplerian Periapsis</b>"
                        f"{date_str}"
                        f"<br>q={peri['distance']:.6f} AU"
                        f"<br>Theoretical minimum distance (θ=0°)"
                        f"<br>Unperturbed Keplerian position at actual periapsis time"
                        f"{accuracy_note}"
                    )
                    
                    fig.add_trace(
                        go.Scatter3d(
                            x=[peri['x']],
                            y=[peri['y']],
                            z=[peri['z']],
                            mode='markers',
                            marker=dict(
                                size=6,
                                color=color_map(obj_name),
                                symbol='square-open'
                            ),
                            name=f"{obj_name} Keplerian Periapsis",
                            text=[hover_text],
                    #        hoverinfo='text',
                            customdata=[f"{obj_name} Keplerian Periapsis"],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )
                    print(f"  Added Keplerian periapsis for {obj_name} at distance {peri['distance']:.6f} AU", flush=True)

            # ========== ADD Keplerian APOAPSIS MARKER ==========
            if show_apsidal_markers:  # ADD THIS CONDITION
                if apsides['apoapsis']:
                    apo = apsides['apoapsis']
                    
                    # Create hover text with date if available
                    date_str = ""
                    position_description = ""
                    
                    if next_aphelion:
                        date_str = f"<br>Date: {next_aphelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                        position_description = "<br>Unperturbed Keplerian position at actual apoapsis time"
                    elif e < 1 and 'TP' in params:
                        # Calculate Keplerian aphelion date if no Tapo provided
                        from astropy.time import Time
                        from datetime import timedelta
                        from constants_new import KNOWN_ORBITAL_PERIODS
                        
                        # NOW check if obj_name is in it
                        if obj_name in KNOWN_ORBITAL_PERIODS:
                            period_days = KNOWN_ORBITAL_PERIODS.get(obj_name)
                            if period_days and period_days not in [None, 1e99]:
                                tp_time = Time(params['TP'], format='jd')
                                tp_datetime = tp_time.datetime

                            # SAFE CALCULATION WITH OVERFLOW PROTECTION
                            half_period_days = period_days / 2
                            
                            try:
                                # Test if calculation would work
                                keplerian_aphelion = tp_datetime + timedelta(days=half_period_days)
                                date_str = f"<br>Date: {keplerian_aphelion.strftime('%Y-%m-%d %H:%M:%S')} UTC (Keplerian estimate)"
                                position_description = "<br>Unperturbed Keplerian position at Keplerian apoapsis time"
                                
                            except (OverflowError, ValueError, OSError):
                                # Handle overflow gracefully for extremely long periods
                                years_to_aphelion = int(half_period_days / 365.25)
                                date_str = f"<br>Date: Far future aphelion (~{years_to_aphelion:,} years after perihelion)"
                                position_description = "<br>Aphelion date beyond calculation range"
                                print(f"  Aphelion date overflow for {obj_name} - using fallback message", flush=True)

                # CONTEXT: This fix ensures that:
                # - The 3D aphelion marker still appears correctly in the plot
                # - The hover text shows a meaningful message instead of causing a crash
                # - Objects with normal periods work exactly as before
                # - Objects like Leleakuhonua get a "far future" message instead of an overflow error


                        #        # Aphelion occurs at period/2 after perihelion for Keplerian orbit
                        #        keplerian_aphelion = tp_datetime + timedelta(days=period_days/2)
                        #        date_str = f"<br>Date: {keplerian_aphelion.strftime('%Y-%m-%d %H:%M:%S')} UTC (Keplerian estimate)"
                        #        position_description = "<br>Unperturbed Keplerian position at Keplerian apoapsis time"

                    hover_text = (
                        f"<b>{obj_name} Keplerian Apoapsis</b>"
                        f"{date_str}"
                        f"<br>Q={apo['distance']:.6f} AU"
                        f"<br>Theoretical maximum distance (θ=180°)"
                        f"{position_description}"
                        f"{accuracy_note}"
                    )
                    
                    fig.add_trace(
                        go.Scatter3d(
                            x=[apo['x']],
                            y=[apo['y']],
                            z=[apo['z']],
                            mode='markers',
                            marker=dict(
                                size=6,
                                color=color_map(obj_name),
                                symbol='square-open'
                            ),
                            name=f"{obj_name} Keplerian Apoapsis",
                            text=[hover_text],
                    #        hoverinfo='text',
                            customdata=[f"{obj_name} Keplerian Apoapsis"],
                            hovertemplate='%{text}<extra></extra>',
                            showlegend=True
                        )
                    )
                    print(f"  Added Keplerian apoapsis for {obj_name} at distance {apo['distance']:.6f} AU", flush=True)

# Fix for Keplerian_orbits.py around lines 3200-3350
# Replace the problematic section with this corrected version:

            # ========== NEW: GENERATE APSIDAL DATES FROM TP ==========
            # Initialize these variables BEFORE any conditional logic
            next_perihelion = None
            next_aphelion = None
            peri_in_range = False
            apo_in_range = False
            
            # After adding Keplerian markers, generate actual dates from TP if available
            if show_apsidal_markers and 'TP' in params:
                from datetime import timedelta
                
                # Get apsidal dates directly from TP and Tapo
                next_perihelion, next_aphelion = compute_apsidal_dates_from_tp(
                    obj_name, params, current_date=date
                )

                # Check JPL range if needed (optional)
                JPL_MIN_DATE = datetime(1900, 1, 1)
                JPL_MAX_DATE = datetime(2199, 12, 29)
                peri_in_range = next_perihelion and JPL_MIN_DATE <= next_perihelion <= JPL_MAX_DATE
                apo_in_range = next_aphelion and JPL_MIN_DATE <= next_aphelion <= JPL_MAX_DATE
                
                # In idealized_orbits.py, when storing apsidal dates:
                if next_perihelion and peri_in_range:
                    # Store with full datetime precision
                    params['perihelion_dates'] = [next_perihelion.strftime('%Y-%m-%d %H:%M:%S')]
                    print(f"  Next perihelion: {params['perihelion_dates'][0]}", flush=True)
                elif next_perihelion and not peri_in_range:
                    print(f"  Next perihelion: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')} (outside JPL range)", flush=True)
                    
                if next_aphelion and e < 1 and apo_in_range:
                    # Store with full datetime precision
                    params['aphelion_dates'] = [next_aphelion.strftime('%Y-%m-%d %H:%M:%S')]
                    print(f"  Next aphelion: {params['aphelion_dates'][0]}", flush=True)
                elif next_aphelion and e < 1 and not apo_in_range:
                    print(f"  Next aphelion: {next_aphelion.strftime('%Y-%m-%d %H:%M:%S')} (outside JPL range)", flush=True)


            # ========== EXISTING: PLOT ACTUAL APSIDAL MARKERS ==========
            if show_apsidal_markers:  # ADD THIS CONDITION
                if 'perihelion_dates' in params or 'aphelion_dates' in params:
                    print(f"\n[DEBUG] Found apsidal dates for {obj_name}", flush=True)
                    print(f"  Perihelion dates: {params.get('perihelion_dates', [])}", flush=True)
                    print(f"  Aphelion dates: {params.get('aphelion_dates', [])}", flush=True)
                    
                    # Get the object ID for fetching positions
                    obj_id = None
                    id_type = None
                    for obj in objects:
                        if obj['name'] == obj_name:
                            obj_id = obj['id']
                            id_type = obj.get('id_type', None)
                            break
                    
                    if obj_id:
                        # Import the functions we need
                        from apsidal_markers import fetch_positions_for_apsidal_dates, add_actual_apsidal_markers_enhanced, calculate_exact_apsides, compute_apsidal_dates_from_tp
                        from datetime import datetime, timedelta

                        # Use the passed fetch_position
                        if fetch_position is None:
                            print("ERROR: fetch_position not provided to plot_idealized_orbits", flush=True)
                        else:
                            # Calculate apsides HERE, right before use
                            apsides = calculate_exact_apsides(
                                params.get('a', a),
                                params.get('e', e),
                                params.get('i', i),
                                params.get('omega', omega),
                                params.get('Omega', Omega),
                                rotate_points
                            )
                        
                            # Fetch positions for the apsidal dates
                            positions_dict = fetch_positions_for_apsidal_dates(
                                obj_id=obj_id,
                                params=params,
                                date_range=None,  # Don't restrict by date range
                                center_id=center_id,
                                id_type=id_type,
                                is_satellite=(obj_name in parent_planets.get(center_id, [])),
                                fetch_position=fetch_position
                            )
                                                        
                            print(f"  Fetched positions: {len(positions_dict)} dates", flush=True)
                            
                            # Check if fetch failed for dates that passed the initial range check
                            # This handles satellite ephemeris with shorter ranges than general JPL
                            perihelion_dates = params.get('perihelion_dates', [])
                            aphelion_dates = params.get('aphelion_dates', [])
                            expected_dates = len(perihelion_dates) + len(aphelion_dates)
                            
                            if expected_dates > 0 and len(positions_dict) == 0:
                                # Fetch failed - likely satellite ephemeris range exceeded
                                print(f"  ⚠ Fetch failed for {obj_name} apsidal dates - ephemeris range exceeded", flush=True)
                                from apsidal_markers import add_apsidal_range_note
                                
                                # Get the dates that failed
                                failed_peri = None
                                failed_apo = None
                                if perihelion_dates:
                                    try:
                                        failed_peri = datetime.strptime(perihelion_dates[0], '%Y-%m-%d %H:%M:%S')
                                    except:
                                        pass
                                if aphelion_dates:
                                    try:
                                        failed_apo = datetime.strptime(aphelion_dates[0], '%Y-%m-%d %H:%M:%S')
                                    except:
                                        pass
                                                            
                                # Add the range note with appropriate message
                                add_apsidal_range_note(
                                    fig,
                                    obj_name,
                                    failed_peri,
                                    failed_apo,
                                    color_map,
                                    fetch_failed=True  # Indicates ephemeris limit, not JPL general limit
                                )

                            # DEBUG: Check what we're passing to enhanced markers
                            print(f"[DEBUG] Calling enhanced markers for {obj_name}:", flush=True)
                            print(f"  params has epoch: {'epoch' in params}", flush=True)
                            if 'epoch' in params:
                                print(f"  epoch value: {params['epoch']}", flush=True)
                            print(f"  ideal_apsides is None: {apsides is None}", flush=True)
                            if apsides is not None:
                                print(f"  ideal_apsides keys: {apsides.keys()}", flush=True)
                            
                            # Add the actual markers
                    #        add_actual_apsidal_markers(
                            add_actual_apsidal_markers_enhanced(    
                                fig,
                                obj_name,
                                params,
                                date_range=(date - timedelta(days=365), date + timedelta(days=365)),
                                positions_dict=positions_dict,
                                color_map=color_map,
                                center_body=center_id,
                                is_satellite=(obj_name in parent_planets.get(center_id, [])),
                                ideal_apsides=apsides,
                                filter_by_date_range=False
                            )

            # ========== NEW: ADD LEGEND NOTES FOR OUT-OF-RANGE DATES ==========
            # Only check these if show_apsidal_markers is True and we have TP
            if show_apsidal_markers and 'TP' in params:
                # Check if we should add a note about out-of-range dates
                if (next_perihelion and not peri_in_range) or (next_aphelion and not apo_in_range):
                    from apsidal_markers import add_apsidal_range_note
                    add_apsidal_range_note(
                        fig,
                        obj_name,
                        next_perihelion if not peri_in_range else None,
                        next_aphelion if not apo_in_range else None,
                        color_map
                    )
                    
            # Mark this object as successfully plotted
            plotted.append(obj_name)

    # Print summary of plotted and skipped objects
    print("\nKeplerian Orbit Summary:", flush=True)
    print(f"Plotted Keplerian orbits for {len(plotted)} objects:", flush=True)
    for obj in plotted:
        print(f"  - {obj}", flush=True)

    print("\nSkipped Keplerian orbits for:", flush=True)
    for category, objects_list in skipped.items():
        if objects_list:
            print(f"\n{category.capitalize()} ({len(objects_list)}):", flush=True)
            for obj in objects_list:
                print(f"  - {obj}", flush=True)

    return fig

def test_triton_rotations(satellite_name, planetary_params, color, fig=None):
    """Test multiple rotation combinations for Triton's orbit"""
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Neptune's axial tilt is 28.32 degrees
        neptune_tilt = 28.32
        
        # Test combinations
        combinations = [
            {"name": "Standard", "rotations": []},
            {"name": "X+", "rotations": [{"axis": 'x', "angle": np.radians(neptune_tilt)}]},
            {"name": "X-", "rotations": [{"axis": 'x', "angle": np.radians(-neptune_tilt)}]},
            {"name": "Y+", "rotations": [{"axis": 'y', "angle": np.radians(neptune_tilt)}]},
            {"name": "Y-", "rotations": [{"axis": 'y', "angle": np.radians(-neptune_tilt)}]},
            {"name": "Z+", "rotations": [{"axis": 'z', "angle": np.radians(neptune_tilt)}]},
            {"name": "Z-", "rotations": [{"axis": 'z', "angle": np.radians(-neptune_tilt)}]},
            
            # Compound rotations like what worked for Uranus
            {"name": "X+Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X+Y-", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(-neptune_tilt)}
            ]},
            {"name": "X-Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(-neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X-Y-", "rotations": [
                {"axis": 'x', "angle": np.radians(-neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(-neptune_tilt)}
            ]},
            
            # Try 90-degree rotations
            {"name": "X+90", "rotations": [{"axis": 'x', "angle": np.radians(90)}]},
            {"name": "Y+90", "rotations": [{"axis": 'y', "angle": np.radians(90)}]},
            {"name": "Z+90", "rotations": [{"axis": 'z', "angle": np.radians(90)}]},
            
            # Compound rotations with 90 degrees
            {"name": "X+90_Y+", "rotations": [
                {"axis": 'x', "angle": np.radians(90)}, 
                {"axis": 'y', "angle": np.radians(neptune_tilt)}
            ]},
            {"name": "X+_Y+90", "rotations": [
                {"axis": 'x', "angle": np.radians(neptune_tilt)}, 
                {"axis": 'y', "angle": np.radians(90)}
            ]},
            
            # Try a different approach with pole-based transformation using Neptune's pole
            {"name": "Neptune Pole", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'x', "angle": np.radians(90 - planet_poles['Neptune']['dec'])}
            ]},

            # Add these to your combinations list
            {"name": "Retrograde", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'x', "angle": np.radians(90 - planet_poles['Neptune']['dec'])},
                {"axis": 'z', "angle": np.radians(180)}
            ]},
            {"name": "Complex", "rotations": [
                {"axis": 'z', "angle": np.radians(planet_poles['Neptune']['ra'])},
                {"axis": 'y', "angle": np.radians(90 - planet_poles['Neptune']['dec'])},
                {"axis": 'x', "angle": np.radians(30)}
            ]}

        ]
        
        # Define line styles and colors for each rotation
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_triton_rotations: {e}", flush=True)
        traceback.print_exc()  # This will print the full stack trace for better debugging
        return fig
    
def test_pluto_moon_rotations(satellite_name, planetary_params, color, fig=None):
#def test_pluto_moon_xyz_rotations(satellite_name, planetary_params, color, fig=None):
    """
    Fine-tuned testing of XYZ rotation combinations for Pluto's moons.
    This function focuses on variations of X, Y, and Z rotations with different angles.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        
    Returns:
        plotly.graph_objects.Figure: Figure with various test orbits added
    """
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        print(f"Testing fine-tuned XYZ rotations for {satellite_name} orbit around Pluto", flush=True)
        print(f"Orbital elements: a={a}, e={e}, i={i}°, ω={omega}°, Ω={Omega}°", flush=True)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Pluto's axial tilt value
        pluto_tilt = planet_tilts.get('Pluto', -122.53)
        pluto_tilt_rad = np.radians(pluto_tilt)
        
        # Create a list of angles to test
        # We'll focus on different angles around Pluto's tilt and other relevant values
        # Using a mix of fixed angles and variations of Pluto's tilt
        x_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        y_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        z_angles = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        
        # Define specific combinations to test
        combinations = []
        
        # Base combination that was close
        combinations.append({
            "name": "XYZ-Tilt-Base",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        # Variations around the base XYZ-Tilt rotation
        # Adjust X rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X{angle}->Y-Tilt->Z-Tilt",
                "rotations": [
                    {"axis": 'x', "angle": np.radians(angle)},
                    {"axis": 'y', "angle": pluto_tilt_rad},
                    {"axis": 'z', "angle": pluto_tilt_rad}
                ]
            })
        
        # Adjust Y rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X-Tilt->Y{angle}->Z-Tilt",
                "rotations": [
                    {"axis": 'x', "angle": pluto_tilt_rad},
                    {"axis": 'y', "angle": np.radians(angle)},
                    {"axis": 'z', "angle": pluto_tilt_rad}
                ]
            })
        
        # Adjust Z rotation
        for angle in [-135, -125, -115, -110, -105, -100, -95, -90]:
            combinations.append({
                "name": f"X-Tilt->Y-Tilt->Z{angle}",
                "rotations": [
                    {"axis": 'x', "angle": pluto_tilt_rad},
                    {"axis": 'y', "angle": pluto_tilt_rad},
                    {"axis": 'z', "angle": np.radians(angle)}
                ]
            })
        
        # Try different rotation orders
        combinations.append({
            "name": "YXZ-Tilt",
            "rotations": [
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "ZXY-Tilt",
            "rotations": [
                {"axis": 'z', "angle": pluto_tilt_rad},
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad}
            ]
        })
        
        # Try modified combinations with 90-degree rotations and Pluto's tilt
        combinations.append({
            "name": "X-90->Y-Tilt->Z-Tilt",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-90)},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "X-Tilt->Y-90->Z-Tilt",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": np.radians(-90)},
                {"axis": 'z', "angle": pluto_tilt_rad}
            ]
        })
        
        combinations.append({
            "name": "X-Tilt->Y-Tilt->Z-90",
            "rotations": [
                {"axis": 'x', "angle": pluto_tilt_rad},
                {"axis": 'y', "angle": pluto_tilt_rad},
                {"axis": 'z', "angle": np.radians(-90)}
            ]
        })
        
        # Adding some specific combinations that might work well
        combinations.append({
            "name": "X-110->Y-115->Z-105",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-110)},
                {"axis": 'y', "angle": np.radians(-115)},
                {"axis": 'z', "angle": np.radians(-105)}
            ]
        })
        
        combinations.append({
            "name": "X-115->Y-115->Z-115",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-115)},
                {"axis": 'y', "angle": np.radians(-115)},
                {"axis": 'z', "angle": np.radians(-115)}
            ]
        })
        
        combinations.append({
            "name": "X-120->Y-120->Z-120",
            "rotations": [
                {"axis": 'x', "angle": np.radians(-120)},
                {"axis": 'y', "angle": np.radians(-120)},
                {"axis": 'z', "angle": np.radians(-120)}
            ]
        })
        
        # Fine-tuning around a specific zone
        for x_angle in [-122, -123]:
            for y_angle in [-122, -123]:
                for z_angle in [-122, -123]:
                    combinations.append({
                        "name": f"X{x_angle}->Y{y_angle}->Z{z_angle}",
                        "rotations": [
                            {"axis": 'x', "angle": np.radians(x_angle)},
                            {"axis": 'y', "angle": np.radians(y_angle)},
                            {"axis": 'z', "angle": np.radians(z_angle)}
                        ]
                    })
        
        # Define line styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "solid", "dash", "dot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in test_pluto_moon_xyz_rotations: {e}", flush=True)
        traceback.print_exc()
        return fig

def very_fine_pluto_rotations(satellite_name, planetary_params, color, fig=None, 
                             x_range=(-125, -115), 
                             y_range=(-125, -115), 
                             z_range=(-125, -115),
                             step=1):
    """
    Extremely fine-grained testing of XYZ rotation combinations for Pluto's moons.
    Tests all combinations within specified ranges with the given step size.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        x_range (tuple): Range of X rotation angles to test in degrees (min, max)
        y_range (tuple): Range of Y rotation angles to test in degrees (min, max)
        z_range (tuple): Range of Z rotation angles to test in degrees (min, max)
        step (int): Step size between angles in degrees
        
    Returns:
        plotly.graph_objects.Figure: Figure with various test orbits added
    """
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        print(f"Testing very fine XYZ rotations for {satellite_name} orbit around Pluto", flush=True)
        print(f"X range: {x_range}, Y range: {y_range}, Z range: {z_range}, Step: {step}", flush=True)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Create angle ranges
        x_angles = range(x_range[0], x_range[1] + 1, step)
        y_angles = range(y_range[0], y_range[1] + 1, step)
        z_angles = range(z_range[0], z_range[1] + 1, step)
        
        # To limit the number of combinations, we'll only test a few combinations
        # where all three angles are the same or very similar
        combinations = []
        
        # Same angle for all three rotations
        for angle in range(max(x_range[0], y_range[0], z_range[0]), 
                           min(x_range[1], y_range[1], z_range[1]) + 1, 
                           step):
            combinations.append({
                "name": f"X{angle}->Y{angle}->Z{angle}",
                "rotations": [
                    {"axis": 'x', "angle": np.radians(angle)},
                    {"axis": 'y', "angle": np.radians(angle)},
                    {"axis": 'z', "angle": np.radians(angle)}
                ]
            })
        
        # Fixed X, varying Y and Z
        for x_angle in [x_range[0], (x_range[0] + x_range[1]) // 2, x_range[1]]:
            for y_angle in y_angles:
                for z_angle in z_angles:
                    if abs(y_angle - z_angle) <= step:  # Only when Y and Z are similar
                        combinations.append({
                            "name": f"X{x_angle}->Y{y_angle}->Z{z_angle}",
                            "rotations": [
                                {"axis": 'x', "angle": np.radians(x_angle)},
                                {"axis": 'y', "angle": np.radians(y_angle)},
                                {"axis": 'z', "angle": np.radians(z_angle)}
                            ]
                        })
        
        # Define line styles for different combinations
        styles = ["solid", "dash", "dot", "dashdot", "longdash", "longdashdot", "solid", "dash", "dot"]
        
        # Apply each rotation combination
        for idx, combo in enumerate(combinations):
            x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
            
            for rot in combo["rotations"]:
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, 
                    rot["angle"], rot["axis"]
                )
            
            # Add trace with unique style
            style = styles[idx % len(styles)]
            
            fig.add_trace(
                go.Scatter3d(
                    x=x_rotated,
                    y=y_rotated,
                    z=z_rotated,
                    mode='lines',
                    line=dict(dash=style, width=1, color=color),
                    name=f"{satellite_name} {combo['name']}",
                    text=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    customdata=[f"{satellite_name} {combo['name']}"] * len(x_rotated),
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        
        return fig
        
    except Exception as e:
        print(f"Error in very_fine_pluto_rotations: {e}", flush=True)
        traceback.print_exc()
        return fig

def pluto_system_final_transform(satellite_name, planetary_params, color, fig=None, transform=None):
    """
    Apply a specific optimal transformation to Pluto's moons' orbits.
    
    Parameters:
        satellite_name (str): Name of the satellite (Charon, Styx, Nix, Kerberos or Hydra)
        planetary_params (dict): Dictionary containing orbital parameters
        color (str): Color to use for the orbit lines
        fig (plotly.graph_objects.Figure): Existing figure to add the orbit to
        transform (dict, optional): Specific transformation to apply, with structure:
            {
                "x_angle": angle in degrees,
                "y_angle": angle in degrees,
                "z_angle": angle in degrees,
                "order": list of axes in order of rotation, e.g. ['x', 'y', 'z']
            }
            
    Returns:
        plotly.graph_objects.Figure: Figure with the finalized orbit
    """
    if fig is None:
        fig = go.Figure()
    
    try:
        # Get orbital parameters
        if satellite_name not in planetary_params:
            print(f"Error: No orbital parameters found for {satellite_name}", flush=True)
            return fig
            
        orbital_params = planetary_params[satellite_name]
        
        # Extract orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Default transformation if none provided
        if transform is None:
            transform = {
                "x_angle": -120,
                "y_angle": -120,
                "z_angle": -120,
                "order": ['x', 'y', 'z']
            }
        
        print(f"Applying final transformation to {satellite_name} orbit around Pluto", flush=True)
        print(f"Transformation: X={transform['x_angle']}°, Y={transform['y_angle']}°, Z={transform['z_angle']}°, Order={transform['order']}", flush=True)
        
        # Generate ellipse in orbital plane
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)

        # Convert angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)

        # Standard orbital element rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
        
        # Apply the custom transformation
        x_rotated, y_rotated, z_rotated = x_temp.copy(), y_temp.copy(), z_temp.copy()
        
        # Convert transformation angles to radians
        x_angle_rad = np.radians(transform['x_angle'])
        y_angle_rad = np.radians(transform['y_angle'])
        z_angle_rad = np.radians(transform['z_angle'])
        
        # Apply rotations in specified order
        for axis in transform['order']:
            if axis == 'x':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, x_angle_rad, 'x'
                )
            elif axis == 'y':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, y_angle_rad, 'y'
                )
            elif axis == 'z':
                x_rotated, y_rotated, z_rotated = rotate_points(
                    x_rotated, y_rotated, z_rotated, z_angle_rad, 'z'
                )
        
        # Add the finalized orbit trace
        fig.add_trace(
            go.Scatter3d(
                x=x_rotated,
                y=y_rotated,
                z=z_rotated,
                mode='lines',
                line=dict(width=2, color=color),
                name=f"{satellite_name} Final",
                text=[f"{satellite_name} Final Orbit"] * len(x_rotated),
                customdata=[f"{satellite_name} Final Orbit"] * len(x_rotated),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
        
        return fig
    
    except Exception as e:
        print(f"Error in pluto_system_final_transform: {e}", flush=True)
        traceback.print_exc()
        return fig


def calculate_phoebe_correction_from_normals():
    """
    Calculate the optimal rotation to align Keplerian orbit with actual orbit
    based on their normal vectors.
    """
    # Normal vectors from your output
    n_actual = np.array([0.1242, 0.0025, 0.9922])
    n_ideal = np.array([0.1814, -0.1036, 0.9779])
    
    # Calculate rotation axis and angle
    rotation_axis = np.cross(n_ideal, n_actual)
    rotation_axis = rotation_axis / np.linalg.norm(rotation_axis)
    
    cos_angle = np.dot(n_ideal, n_actual)
    angle = np.arccos(np.clip(cos_angle, -1, 1))
    
    print(f"Rotation axis: {rotation_axis}", flush=True)
    print(f"Rotation angle: {np.degrees(angle):.2f}°", flush=True)
    
    # Decompose into X, Y, Z rotations
    # This is approximate but gives us insight
    x_component = np.arcsin(rotation_axis[0]) * angle
    y_component = np.arcsin(rotation_axis[1]) * angle  
    z_component = np.arcsin(rotation_axis[2]) * angle
    
    print(f"Approximate decomposition:")
    print(f"  X rotation: {np.degrees(x_component):.2f}°", flush=True)
    print(f"  Y rotation: {np.degrees(y_component):.2f}°", flush=True)
    print(f"  Z rotation: {np.degrees(z_component):.2f}°", flush=True)
    
    return rotation_axis, angle