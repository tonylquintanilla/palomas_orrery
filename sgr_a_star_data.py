"""
sgr_a_star_data.py
Data module for the Galactic Center S-Stars visualization.
Contains orbital elements and physical constants.

The S-stars orbit Sagittarius A*, the supermassive black hole at the
center of the Milky Way. These stars serve as "test particles" for
Einstein's General Relativity, reaching speeds up to 8% of light.

Sources:
- GRAVITY Collaboration (2018, 2019, 2020)
- Gillessen et al. (2017)
- Peissker et al. (2020)

Part of Paloma's Orrery - Data Preservation is Climate Action
"""

import math
import numpy as np
import re

# =============================================================================
# TEMPERATURE AND COLOR UTILITIES
# =============================================================================
# Import stellar property functions for consistent coloring across Paloma's Orrery
try:
    from stellar_parameters import estimate_temperature_from_spectral_type
    from exoplanet_stellar_properties import get_temperature_color
    STELLAR_PROPS_AVAILABLE = True
except ImportError:
    STELLAR_PROPS_AVAILABLE = False
    print("Note: stellar_parameters not available, using fallback colors")

# =============================================================================
# FALLBACK TEMPERATURE-TO-COLOR (if stellar_parameters unavailable)
# =============================================================================

# B-type star temperatures by subclass (for fallback estimation)
B_STAR_TEMPERATURES = {
    'O': 35000,   # O-type (hotter than B)
    'B0': 30000,
    'B1': 25400,
    'B2': 22000,
    'B3': 18700,
    'B5': 15400,
    'B7': 13000,
    'B8': 11400,
    'B9': 10500,
    'B': 20000,   # Generic B-type (mid-range)
}

def estimate_temperature_fallback(spectral_type):
    """
    Fallback temperature estimation for B-type stars.
    Used when stellar_parameters module is not available.
    """
    if spectral_type is None:
        return 20000  # Default for B-type
    
    sp = spectral_type.upper().strip()
    
    # Try exact match first
    for key in B_STAR_TEMPERATURES:
        if sp.startswith(key):
            return B_STAR_TEMPERATURES[key]
    
    # Handle ranges like "B0-2V"
    match = re.match(r'B(\d)', sp)
    if match:
        subclass = int(match.group(1))
        return B_STAR_TEMPERATURES.get(f'B{subclass}', 20000)
    
    return 20000  # Default B-type temperature


def get_temperature_color_fallback(temperature_k):
    """
    Fallback temperature-to-color conversion.
    Uses simplified blackbody color approximation.
    """
    if temperature_k is None or np.isnan(temperature_k):
        return 'rgb(180, 180, 255)'  # Default blue-white
    
    # B-type stars (10,000-30,000 K) are blue to blue-white
    if temperature_k >= 30000:
        return 'rgb(155, 176, 255)'  # Deep blue-white (O-type)
    elif temperature_k >= 20000:
        return 'rgb(170, 191, 255)'  # Blue-white (early B)
    elif temperature_k >= 15000:
        return 'rgb(185, 206, 255)'  # Light blue-white (mid B)
    elif temperature_k >= 10000:
        return 'rgb(200, 220, 255)'  # Pale blue-white (late B)
    else:
        return 'rgb(220, 235, 255)'  # Nearly white


def get_star_temperature(star_data):
    """
    Get temperature for a star, using best available method.
    """
    spectral_type = star_data.get('spectral_type', 'B')
    
    if STELLAR_PROPS_AVAILABLE:
        temp = estimate_temperature_from_spectral_type(spectral_type)
        if not np.isnan(temp):
            return temp
    
    return estimate_temperature_fallback(spectral_type)


def get_star_color(star_data):
    """
    Get display color for a star based on its temperature.
    Uses blackbody colors consistent with exoplanet host stars.
    """
    temperature = get_star_temperature(star_data)
    
    if STELLAR_PROPS_AVAILABLE:
        return get_temperature_color(temperature)
    
    return get_temperature_color_fallback(temperature)


def get_orbit_color(star_data):
    """
    Get distinct color for orbit trace and labels.
    Separate from star marker color for better readability.
    """
    return star_data.get('orbit_color', star_data.get('color', '#FFFFFF'))

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================

G_CONST = 6.67430e-11           # Gravitational constant (m^3 kg^-1 s^-2)
SPEED_OF_LIGHT = 299792458.0    # Speed of light (m/s)
SPEED_OF_LIGHT_KM_S = 299792.458  # Speed of light (km/s)
SOLAR_MASS_KG = 1.989e30        # Solar mass (kg)
AU_TO_METERS = 1.496e11         # 1 AU in meters
AU_TO_KM = 1.496e8              # 1 AU in kilometers
PARSEC_TO_AU = 206265.0         # 1 parsec in AU
YEAR_TO_SECONDS = 365.25 * 24 * 3600  # Seconds per Julian year

# =============================================================================
# SAGITTARIUS A* PROPERTIES
# =============================================================================

SGR_A_MASS_SOLAR = 4.154e6      # Solar masses (GRAVITY Collaboration 2019)
SGR_A_MASS_KG = SGR_A_MASS_SOLAR * SOLAR_MASS_KG
SGR_A_DISTANCE_PC = 8178.0      # Distance from Earth (parsecs)
SGR_A_DISTANCE_LY = 26670.0     # Distance from Earth (light years)

# Schwarzschild Radius: Rs = 2GM / c^2
# The "point of no return" - event horizon radius
SCHWARZSCHILD_RADIUS_METERS = (2 * G_CONST * SGR_A_MASS_KG) / (SPEED_OF_LIGHT**2)
SCHWARZSCHILD_RADIUS_KM = SCHWARZSCHILD_RADIUS_METERS / 1000.0
SCHWARZSCHILD_RADIUS_AU = SCHWARZSCHILD_RADIUS_METERS / AU_TO_METERS
# Result: ~0.08 AU or ~12 million km (about 40x Earth-Moon distance)

# Innermost Stable Circular Orbit (ISCO) for a non-rotating black hole
# ISCO = 3 * Rs (for Schwarzschild black hole)
ISCO_RADIUS_AU = 3 * SCHWARZSCHILD_RADIUS_AU

# =============================================================================
# THE S-STAR CATALOG
# =============================================================================
# Orbital Elements:
#   a_au:              Semi-major axis (AU)
#   e:                 Eccentricity (0 = circle, 1 = parabola)
#   period_yrs:        Orbital period (years)
#   t_periapsis:       Time of periapsis passage (decimal year)
#   arg_periapsis_deg: Argument of periapsis (degrees) - orientation of ellipse
#   inclination_deg:   Orbital inclination (degrees)
#   asc_node_deg:      Longitude of ascending node (degrees)
#
# Physical Properties:
#   mass_solar:        Estimated stellar mass (solar masses)
#   spectral_type:     Stellar classification
#   color:             Display color (hex)
#   notes:             Scientific significance

S_STAR_CATALOG = {
    'S2': {
        'name': 'S2 (S0-2)',
        'a_au': 1031.0,
        'e': 0.8843,
        'period_yrs': 16.05,
        't_periapsis': 2018.38,
        'arg_periapsis_deg': 66.13,
        'inclination_deg': 134.18,
        'asc_node_deg': 228.07,
        'color': '#6B9FFF',           # Legacy color (now used as fallback)
        'orbit_color': '#FFD700',     # Gold - distinct orbit trace color
        'mass_solar': 14.0,
        'spectral_type': 'B0-2V',
        'notes': 'The most studied S-star. Used to confirm gravitational redshift (2018) and Schwarzschild precession (2020).'
    },
    'S62': {
        'name': 'S62',
        'a_au': 740.0,
        'e': 0.976,
        'period_yrs': 9.9,
        't_periapsis': 2003.33,
        'arg_periapsis_deg': 42.6,
        'inclination_deg': 72.8,
        'asc_node_deg': 122.6,
        'color': '#9FBAFF',
        'orbit_color': '#00FF7F',     # Spring Green - distinct orbit trace color
        'mass_solar': 6.1,
        'spectral_type': 'B',
        'notes': 'Discovered ~2020. Reaches 6.7% speed of light at periapsis.'
    },
    'S4711': {
        'name': 'S4711',
        'a_au': 572.0,
        'e': 0.768,
        'period_yrs': 7.6,
        't_periapsis': 2013.4,
        'arg_periapsis_deg': 120.0,
        'inclination_deg': 110.0,
        'asc_node_deg': 100.0,
        'color': '#B4C7FF',
        'orbit_color': '#FF6B6B',     # Coral Red - distinct orbit trace color
        'mass_solar': 2.0,
        'spectral_type': 'B',
        'notes': 'Holds record for shortest known stable orbital period around Sgr A*.'
    },
    'S4714': {
        'name': 'S4714',
        'a_au': 520.0,
        'e': 0.985,
        'period_yrs': 12.0,
        't_periapsis': 2017.0,
        'arg_periapsis_deg': 130.0,
        'inclination_deg': 120.0,
        'asc_node_deg': 90.0,
        'color': '#FFB4B4',
        'orbit_color': '#DA70D6',     # Orchid Purple - distinct orbit trace color
        'mass_solar': 2.0,
        'spectral_type': 'B',
        'notes': 'The speed demon. Extreme eccentricity (0.985) brings it to 8% light speed. Potential "squeezar" candidate.'
    }
}

# =============================================================================
# HELPER FUNCTIONS - Data Access
# =============================================================================

def get_star_data(star_name):
    """Returns the dictionary for a specific star."""
    return S_STAR_CATALOG.get(star_name)

def list_stars():
    """Returns list of available star keys."""
    return list(S_STAR_CATALOG.keys())

def get_all_stars():
    """Returns the complete catalog dictionary."""
    return S_STAR_CATALOG

# =============================================================================
# HELPER FUNCTIONS - Hover Text and Display
# =============================================================================

def get_spectral_class_description(spectral_type):
    """Get human-readable description of spectral type."""
    if spectral_type is None:
        return "Unknown"
    
    sp = spectral_type.upper()
    
    # Luminosity class descriptions
    if 'V' in sp:
        lum_class = "Main-sequence"
    elif 'III' in sp:
        lum_class = "Giant"
    elif 'I' in sp:
        lum_class = "Supergiant"
    else:
        lum_class = "Main-sequence"  # Assume MS for S-stars
    
    # Spectral type descriptions
    if sp.startswith('O'):
        type_desc = "Blue supergiant"
    elif sp.startswith('B0') or sp.startswith('B1') or sp.startswith('B2'):
        type_desc = "Early B-type (hot blue)"
    elif sp.startswith('B'):
        type_desc = "B-type (blue-white)"
    else:
        type_desc = "Unknown type"
    
    return f"{type_desc}, {lum_class}"


def calculate_next_periapsis(star_data, reference_year=2025):
    """
    Calculate the next periapsis passage date for a star.
    
    Args:
        star_data: Star data dictionary with t_periapsis and period_yrs
        reference_year: Current reference year
        
    Returns:
        float: Year of next periapsis
    """
    t_peri = star_data['t_periapsis']
    period = star_data['period_yrs']
    
    # Find next periapsis after reference year
    next_peri = t_peri
    while next_peri < reference_year:
        next_peri += period
    
    return next_peri


def create_star_hover_text(star_name, star_data, current_distance_au=None, current_velocity_km_s=None):
    """
    Create rich hover text for S-star markers.
    
    Matches the style and information density of exoplanet host star hovers.
    
    Args:
        star_name: Key from catalog
        star_data: Star data dictionary
        current_distance_au: Current distance from Sgr A* (optional)
        current_velocity_km_s: Current orbital velocity (optional)
        
    Returns:
        str: HTML-formatted hover text
    """
    # Header
    hover = f"<b>{star_data['name']}</b><br><br>"
    
    # Temperature and spectral type
    temperature = get_star_temperature(star_data)
    spectral_type = star_data.get('spectral_type', 'B')
    hover += f"Temperature: {temperature:,.0f} K<br>"
    hover += f"Spectral Type: {spectral_type}<br>"
    hover += f"Classification: {get_spectral_class_description(spectral_type)}<br>"
    
    # Physical properties
    mass = star_data.get('mass_solar')
    if mass:
        hover += f"Mass: {mass:.1f} M_sun<br>"
    
    hover += "<br>"
    
    # Orbital properties
    hover += f"<b>Orbit around Sgr A*:</b><br>"
    hover += f"Period: {star_data['period_yrs']:.1f} years<br>"
    hover += f"Semi-major axis: {star_data['a_au']:,.0f} AU<br>"
    hover += f"Eccentricity: {star_data['e']:.4f}<br>"
    
    # Periapsis/apoapsis
    periapsis = calculate_periapsis_au(star_data['a_au'], star_data['e'])
    apoapsis = calculate_apoapsis_au(star_data['a_au'], star_data['e'])
    hover += f"Periapsis: {periapsis:.1f} AU<br>"
    hover += f"Apoapsis: {apoapsis:,.0f} AU<br>"
    
    # Next periapsis
    next_peri = calculate_next_periapsis(star_data)
    hover += f"Next periapsis: ~{next_peri:.1f}<br>"
    
    # Current state (if provided)
    if current_distance_au is not None and current_velocity_km_s is not None:
        hover += "<br>"
        hover += f"<b>Current State:</b><br>"
        hover += f"Distance: {current_distance_au:.1f} AU<br>"
        hover += f"Velocity: {format_velocity(current_velocity_km_s)}<br>"
    
    # Maximum velocity (at periapsis)
    v_peri = calculate_periapsis_velocity(star_data['a_au'], star_data['e'])
    hover += "<br>"
    hover += f"<b>Max velocity (periapsis):</b><br>"
    hover += f"{format_velocity(v_peri)}<br>"
    
    # Notes with squeezar explanation
    notes = star_data.get('notes', '')
    if notes:
        # Expand "squeezar" if mentioned
        if 'squeezar' in notes.lower():
            notes = notes.replace(
                'squeezar',
                'squeezar (star squeezed by tidal forces)'
            ).replace(
                'Squeezar',
                'Squeezar (star squeezed by tidal forces)'
            )
        hover += f"<br><i>{notes}</i>"
    
    return hover

# =============================================================================
# HELPER FUNCTIONS - Orbital Calculations
# =============================================================================

def calculate_periapsis_au(a_au, e):
    """
    Calculate periapsis distance (closest approach to black hole).
    q = a * (1 - e)
    """
    return a_au * (1 - e)

def calculate_apoapsis_au(a_au, e):
    """
    Calculate apoapsis distance (farthest point from black hole).
    Q = a * (1 + e)
    """
    return a_au * (1 + e)

def calculate_orbital_velocity(a_au, r_au, M_solar=SGR_A_MASS_SOLAR):
    """
    Calculate orbital velocity at distance r using vis-viva equation.
    v^2 = GM * (2/r - 1/a)
    
    Returns velocity in km/s.
    """
    # Convert to SI units
    a_m = a_au * AU_TO_METERS
    r_m = r_au * AU_TO_METERS
    M_kg = M_solar * SOLAR_MASS_KG
    
    # Vis-viva equation
    v_squared = G_CONST * M_kg * (2/r_m - 1/a_m)
    v_m_s = math.sqrt(v_squared)
    
    return v_m_s / 1000.0  # Convert to km/s

def calculate_periapsis_velocity(a_au, e, M_solar=SGR_A_MASS_SOLAR):
    """Calculate velocity at periapsis (maximum velocity)."""
    r_periapsis = calculate_periapsis_au(a_au, e)
    return calculate_orbital_velocity(a_au, r_periapsis, M_solar)

def calculate_apoapsis_velocity(a_au, e, M_solar=SGR_A_MASS_SOLAR):
    """Calculate velocity at apoapsis (minimum velocity)."""
    r_apoapsis = calculate_apoapsis_au(a_au, e)
    return calculate_orbital_velocity(a_au, r_apoapsis, M_solar)

def velocity_as_fraction_of_c(v_km_s):
    """Convert velocity to fraction of speed of light."""
    return v_km_s / SPEED_OF_LIGHT_KM_S

def format_velocity(v_km_s):
    """Format velocity as 'X km/s (Y% c)'."""
    percent_c = velocity_as_fraction_of_c(v_km_s) * 100
    return f"{v_km_s:,.0f} km/s ({percent_c:.1f}% c)"

# =============================================================================
# HELPER FUNCTIONS - Relativistic Effects
# =============================================================================

def calculate_schwarzschild_precession_per_orbit(a_au, e, M_solar=SGR_A_MASS_SOLAR):
    """
    Calculate the Schwarzschild (GR) precession per orbit.
    
    Formula: delta_phi = 6 * pi * G * M / (c^2 * a * (1 - e^2))
             = 3 * pi * Rs / (a * (1 - e^2))
    
    Returns precession in degrees per orbit.
    
    For S2: ~0.2 degrees (~12 arcminutes) per 16-year orbit.
    """
    # Use Schwarzschild radius form for numerical stability
    Rs_au = SCHWARZSCHILD_RADIUS_AU
    
    # Precession in radians
    precession_rad = 3 * math.pi * Rs_au / (a_au * (1 - e**2))
    
    # Convert to degrees
    return math.degrees(precession_rad)

def calculate_gravitational_redshift(r_au, M_solar=SGR_A_MASS_SOLAR):
    """
    Calculate gravitational redshift factor at distance r.
    
    z = 1 / sqrt(1 - Rs/r) - 1
    
    For S2 at periapsis (~120 AU): z ~ 0.0003 (detected in 2018!)
    """
    Rs_au = SCHWARZSCHILD_RADIUS_AU
    r_au = max(r_au, Rs_au * 1.001)  # Avoid singularity
    
    factor = 1 - (Rs_au / r_au)
    if factor <= 0:
        return float('inf')  # Inside event horizon
    
    return 1 / math.sqrt(factor) - 1

# =============================================================================
# HELPER FUNCTIONS - Kepler's Equation
# =============================================================================

def mean_anomaly_at_time(t_current, t_periapsis, period_yrs):
    """
    Calculate mean anomaly M at a given time.
    M = 2*pi * (t - t_periapsis) / P
    
    Returns mean anomaly in radians, normalized to [0, 2*pi).
    """
    dt = t_current - t_periapsis
    M = 2 * math.pi * dt / period_yrs
    return M % (2 * math.pi)

def solve_kepler_equation(M, e, tolerance=1e-10, max_iterations=100):
    """
    Solve Kepler's equation: M = E - e*sin(E)
    
    Uses Newton-Raphson iteration.
    
    Args:
        M: Mean anomaly (radians)
        e: Eccentricity
        
    Returns:
        E: Eccentric anomaly (radians)
    """
    # Initial guess
    if e < 0.8:
        E = M
    else:
        E = math.pi  # Better starting point for high eccentricity
    
    for _ in range(max_iterations):
        f = E - e * math.sin(E) - M
        f_prime = 1 - e * math.cos(E)
        
        if abs(f_prime) < 1e-12:
            break
            
        E_new = E - f / f_prime
        
        if abs(E_new - E) < tolerance:
            return E_new
        E = E_new
    
    return E

def eccentric_to_true_anomaly(E, e):
    """
    Convert eccentric anomaly to true anomaly.
    
    tan(nu/2) = sqrt((1+e)/(1-e)) * tan(E/2)
    
    Returns true anomaly in radians.
    """
    beta = e / (1 + math.sqrt(1 - e**2))
    nu = E + 2 * math.atan2(beta * math.sin(E), 1 - beta * math.cos(E))
    return nu

def true_anomaly_at_time(t_current, t_periapsis, period_yrs, e):
    """
    Calculate true anomaly at a given time.
    Combines mean anomaly calculation and Kepler equation solution.
    """
    M = mean_anomaly_at_time(t_current, t_periapsis, period_yrs)
    E = solve_kepler_equation(M, e)
    nu = eccentric_to_true_anomaly(E, e)
    return nu

def radius_from_true_anomaly(a_au, e, nu):
    """
    Calculate orbital radius at true anomaly nu.
    r = a * (1 - e^2) / (1 + e*cos(nu))
    """
    return a_au * (1 - e**2) / (1 + e * math.cos(nu))

# =============================================================================
# SUMMARY FUNCTIONS
# =============================================================================

def get_star_summary(star_name):
    """
    Get a formatted summary of a star's orbital characteristics.
    """
    star = get_star_data(star_name)
    if star is None:
        return f"Star '{star_name}' not found in catalog."
    
    a = star['a_au']
    e = star['e']
    
    periapsis = calculate_periapsis_au(a, e)
    apoapsis = calculate_apoapsis_au(a, e)
    v_peri = calculate_periapsis_velocity(a, e)
    v_apo = calculate_apoapsis_velocity(a, e)
    precession = calculate_schwarzschild_precession_per_orbit(a, e)
    
    lines = [
        f"=== {star['name']} ===",
        f"Spectral Type: {star['spectral_type']}",
        f"Mass: {star['mass_solar']} solar masses",
        f"",
        f"Orbital Period: {star['period_yrs']:.2f} years",
        f"Semi-major axis: {a:,.0f} AU",
        f"Eccentricity: {e:.4f}",
        f"",
        f"Periapsis: {periapsis:,.1f} AU ({periapsis/SCHWARZSCHILD_RADIUS_AU:,.0f} Rs)",
        f"Apoapsis: {apoapsis:,.1f} AU",
        f"",
        f"Velocity at periapsis: {format_velocity(v_peri)}",
        f"Velocity at apoapsis: {format_velocity(v_apo)}",
        f"",
        f"GR Precession: {precession:.4f} deg/orbit ({precession*60:.1f} arcmin/orbit)",
        f"",
        f"Notes: {star['notes']}"
    ]
    
    return "\n".join(lines)

def print_catalog_summary():
    """Print summary for all stars in the catalog."""
    print("=" * 60)
    print("S-STAR CATALOG - Stars Orbiting Sagittarius A*")
    print(f"Black Hole Mass: {SGR_A_MASS_SOLAR/1e6:.3f} million solar masses")
    print(f"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU ({SCHWARZSCHILD_RADIUS_KM/1e6:.1f} million km)")
    print("=" * 60)
    
    for star_name in list_stars():
        print()
        print(get_star_summary(star_name))
        print()

# =============================================================================
# HISTORICAL EVENTS - For "Jump to Event" feature
# =============================================================================

HISTORICAL_EVENTS = {
    'S2_periapsis_2018': {
        'name': 'S2 Periapsis 2018 - Gravitational Redshift Detection',
        'date': 2018.38,
        'star': 'S2',
        'description': 'S2 passed within 120 AU of Sgr A*. The GRAVITY instrument detected gravitational redshift exactly as Einstein predicted.',
        'camera_focus': 'periapsis'
    },
    'S2_precession_2020': {
        'name': 'S2 Schwarzschild Precession Confirmed',
        'date': 2020.0,
        'star': 'S2',
        'description': "After 27 years of observations, S2's orbit was confirmed to precess (rotate) exactly as General Relativity predicts.",
        'camera_focus': 'orbit_overview'
    },
    'S62_discovery': {
        'name': 'S62 Discovery - A Faster Star',
        'date': 2020.0,
        'star': 'S62',
        'description': 'Astronomers announced discovery of S62, which reaches 6.7% the speed of light.',
        'camera_focus': 'orbit_overview'
    },
    'S4714_discovery': {
        'name': 'S4714 Discovery - The Speed Demon',
        'date': 2020.0,
        'star': 'S4714',
        'description': 'S4714 was revealed with eccentricity 0.985, reaching 8% the speed of light at periapsis.',
        'camera_focus': 'periapsis'
    }
}

# =============================================================================
# TEST / DEMO
# =============================================================================

if __name__ == "__main__":
    print_catalog_summary()
    
    print("\n" + "=" * 60)
    print("HISTORICAL EVENTS")
    print("=" * 60)
    for event_id, event in HISTORICAL_EVENTS.items():
        print(f"\n{event['name']}")
        print(f"  Date: {event['date']}")
        print(f"  {event['description']}")
