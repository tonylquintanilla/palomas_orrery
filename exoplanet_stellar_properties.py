"""
exoplanet_stellar_properties.py - Stellar Properties for Exoplanet Host Stars

This module integrates stellar property calculations from the star visualization
pipeline into exoplanet host star displays. It provides rich hover text and 
temperature-based coloring for exoplanet host stars, matching the quality of
information shown in the stellar neighborhood visualizations.

Key features:
- Temperature calculations from spectral types
- Temperature-to-color mapping (continuous scale)
- Luminosity calculations
- Stellar classification
- Rich hover text generation matching star visualization quality

Reuses proven functions from:
- stellar_parameters.py (temperature estimation)
- visualization_core.py (formatting, color scales)
- constants_new.py (spectral type mappings, class descriptions)

Created: October 23, 2025
Author: Tony Quintanilla with Claude AI
"""

import numpy as np
import re

# Import stellar property calculation functions
from stellar_parameters import (
    estimate_temperature_from_spectral_type,
    calculate_bv_temperature,
    select_best_temperature
)

# Import constants and mappings
from constants_new import (
    spectral_subclass_temps,
    class_mapping,
    object_type_mapping
)

# Import formatting utilities
from visualization_core import format_value

# ============================================================================
# TEMPERATURE-TO-COLOR MAPPING
# ============================================================================

def get_temperature_color(temperature_k):
    """
    Get RGB color for a given temperature using continuous interpolation.
    
    Uses the same color scale as the stellar neighborhood visualizations
    for consistency across all of Paloma's Orrery.
    
    Parameters:
        temperature_k (float): Effective temperature in Kelvin
        
    Returns:
        str: RGB color string in format 'rgb(r, g, b)'
    """
    if temperature_k is None or np.isnan(temperature_k):
        return 'rgb(128, 128, 128)'  # Gray for unknown temperature
    
    # Temperature color scale (matching stellar visualizations)
    temp_colors = {
        1300: (255, 0, 0),        # Red for L-type
        2400: (255, 0, 0),        # Red for M-type
        3700: (255, 165, 0),      # Orange for K-type
        5200: (255, 255, 0),      # Yellow for G-type (like our Sun)
        6000: (255, 255, 255),    # White for F-type
        7500: (173, 216, 230),    # Light Blue for A-type
        10000: (0, 0, 255),       # Blue for B-type
        30000: (0, 0, 139),       # Dark Blue for O-type
        50000: (75, 0, 130),      # Indigo for upper O limit
    }
    
    # Get sorted temperature breakpoints
    temp_points = sorted(temp_colors.keys())
    
    # Handle boundary cases
    if temperature_k <= temp_points[0]:
        r, g, b = temp_colors[temp_points[0]]
        return f'rgb({r}, {g}, {b})'
    if temperature_k >= temp_points[-1]:
        r, g, b = temp_colors[temp_points[-1]]
        return f'rgb({r}, {g}, {b})'
    
    # Find bracketing temperatures
    for i in range(len(temp_points) - 1):
        if temp_points[i] <= temperature_k <= temp_points[i + 1]:
            t_low = temp_points[i]
            t_high = temp_points[i + 1]
            color_low = temp_colors[t_low]
            color_high = temp_colors[t_high]
            
            # Linear interpolation
            fraction = (temperature_k - t_low) / (t_high - t_low)
            r = int(color_low[0] + fraction * (color_high[0] - color_low[0]))
            g = int(color_low[1] + fraction * (color_high[1] - color_low[1]))
            b = int(color_low[2] + fraction * (color_high[2] - color_low[2]))
            
            return f'rgb({r}, {g}, {b})'
    
    # Fallback (shouldn't reach here)
    return 'rgb(255, 255, 255)'  # White


def get_temperature_colors_dict():
    """
    Get the complete temperature-to-color mapping dictionary.
    
    Returns:
        dict: Mapping of temperatures to RGB color strings
    """
    return {
        1300: 'rgb(255, 0, 0)',        # Red for L
        2400: 'rgb(255, 0, 0)',        # Red for M
        3700: 'rgb(255, 165, 0)',      # Orange for K
        5200: 'rgb(255, 255, 0)',      # Yellow for G
        6000: 'rgb(255, 255, 255)',    # White for F
        7500: 'rgb(173, 216, 230)',    # Light Blue for A
        10000: 'rgb(0, 0, 255)',       # Blue for B
        30000: 'rgb(0, 0, 139)',       # Dark Blue for O
        50000: 'rgb(75, 0, 130)',      # Indigo for upper O limit
    }


# ============================================================================
# STELLAR CLASSIFICATION
# ============================================================================

def parse_stellar_class(spectral_type):
    """
    Parse stellar luminosity class from spectral type string.
    
    Extracts Roman numerals (I-V) and returns human-readable description.
    
    Parameters:
        spectral_type (str): Spectral type string (e.g., 'M8V', 'K0III')
        
    Returns:
        str: Human-readable stellar class (e.g., 'Main-sequence')
    """
    if spectral_type is None or not isinstance(spectral_type, str):
        return "Unknown"
    
    # Look for Roman numerals
    match = re.search(r'([IV]+)', str(spectral_type))
    if match:
        luminosity_class = match.group(1)
        return class_mapping.get(luminosity_class, luminosity_class)
    
    return "Unknown"


def get_stellar_class_description(spectral_type):
    """
    Get detailed description of stellar class.
    
    Parameters:
        spectral_type (str): Spectral type string
        
    Returns:
        str: Full description with parenthetical explanation
    """
    stellar_class = parse_stellar_class(spectral_type)
    
    if stellar_class == "Main-sequence":
        return "Main-sequence (Stars in the prime of their lives, fusing hydrogen into helium in their cores)"
    elif stellar_class == "Bright Giant":
        return "Bright Giant (Evolved star that has exhausted core hydrogen and expanded)"
    elif stellar_class == "Subgiant":
        return "Subgiant (Star transitioning from main sequence to giant phase)"
    elif stellar_class == "Giant":
        return "Giant (Evolved star with expanded outer layers)"
    elif stellar_class == "Supergiant":
        return "Supergiant (Extremely luminous evolved massive star)"
    else:
        return stellar_class


# ============================================================================
# EXOPLANET HOST STAR PROPERTIES
# ============================================================================

def calculate_host_star_properties(host_star_data):
    """
    Calculate comprehensive stellar properties for an exoplanet host star.
    
    Takes the host_star dictionary from exoplanet_systems.py and enriches it
    with calculated properties for visualization.
    
    Parameters:
        host_star_data (dict): Host star data from exoplanet_systems.py
                               Must contain: spectral_type, teff_k, mass_solar, radius_solar
                               
    Returns:
        dict: Enriched properties including:
              - temperature (K)
              - temperature_source (str)
              - color (RGB string)
              - stellar_class (str)
              - stellar_class_desc (str)
              - luminosity (Lsun)
              - abs_magnitude (float)
    """
    properties = {}
    
    # Temperature (prefer provided teff_k, fall back to spectral type estimation)
    spectral_type = host_star_data.get('spectral_type', '')
    provided_temp = host_star_data.get('teff_k')
    
    if provided_temp and not np.isnan(provided_temp):
        properties['temperature'] = provided_temp
        properties['temperature_source'] = 'literature'
    else:
        # Estimate from spectral type
        estimated_temp = estimate_temperature_from_spectral_type(spectral_type)
        properties['temperature'] = estimated_temp
        properties['temperature_source'] = 'estimated from spectral type'
    
    # Color mapping
    properties['color'] = get_temperature_color(properties['temperature'])
    
    # Stellar classification
    properties['stellar_class'] = parse_stellar_class(spectral_type)
    properties['stellar_class_desc'] = get_stellar_class_description(spectral_type)
    
    # Luminosity calculation (if radius and temperature available)
    radius_solar = host_star_data.get('radius_solar')
    temp = properties['temperature']
    
    if radius_solar and temp and not np.isnan(radius_solar) and not np.isnan(temp):
        # Stefan-Boltzmann law: L = 4π R² σ T⁴
        # In solar units: L/L☉ = (R/R☉)² × (T/T☉)⁴
        T_sun = 5772  # K
        properties['luminosity'] = (radius_solar ** 2) * ((temp / T_sun) ** 4)
    elif 'luminosity_solar' in host_star_data:
        # Use provided luminosity
        properties['luminosity'] = host_star_data['luminosity_solar']
    else:
        properties['luminosity'] = np.nan
    
    # Absolute magnitude (from luminosity)
    if properties['luminosity'] and not np.isnan(properties['luminosity']):
        M_sun = 4.83  # Absolute magnitude of the Sun
        properties['abs_magnitude'] = M_sun - 2.5 * np.log10(properties['luminosity'])
    else:
        properties['abs_magnitude'] = np.nan
    
    # Apparent magnitude (from absolute magnitude and distance)
    if 'distance_pc' in host_star_data and not np.isnan(properties.get('abs_magnitude', np.nan)):
        distance_pc = host_star_data['distance_pc']
        properties['apparent_magnitude'] = properties['abs_magnitude'] + 5 * np.log10(distance_pc / 10)
    else:
        properties['apparent_magnitude'] = np.nan
    
    return properties


def calculate_binary_star_properties(star_A_data, star_B_data):
    """
    Calculate properties for both stars in a binary system.
    
    Parameters:
        star_A_data (dict): Primary star data
        star_B_data (dict): Secondary star data
        
    Returns:
        tuple: (star_A_properties, star_B_properties)
    """
    props_A = calculate_host_star_properties(star_A_data)
    props_B = calculate_host_star_properties(star_B_data)
    
    return props_A, props_B


# ============================================================================
# HOVER TEXT GENERATION
# ============================================================================

def create_exoplanet_host_star_hover_text(host_star_data, system_data, enhanced_properties=None):
    """
    Create rich hover text for exoplanet host stars.
    
    Matches the quality and style of hover text in stellar neighborhood visualizations.
    
    Parameters:
        host_star_data (dict): Host star data from exoplanet_systems.py
        system_data (dict): Parent system data (for context like distance, notable features)
        enhanced_properties (dict, optional): Pre-calculated properties from calculate_host_star_properties()
        
    Returns:
        str: HTML-formatted hover text
    """
    # Calculate properties if not provided
    if enhanced_properties is None:
        enhanced_properties = calculate_host_star_properties(host_star_data)
    
    # Start with star name
    star_name = host_star_data.get('name', 'Unknown Star')
    hover_text = f'<b>{star_name}</b><br><br>'
    
    # Distance
    distance_pc = system_data.get('distance_pc', host_star_data.get('distance_pc'))
    distance_ly = system_data.get('distance_ly', host_star_data.get('distance_ly'))
    if distance_pc:
        hover_text += f'Distance: {format_value(distance_pc, ".2f")} pc '
        hover_text += f'({format_value(distance_ly, ".1f")} ly)<br>'
    
    # Temperature
    temp = enhanced_properties.get('temperature')
    temp_source = enhanced_properties.get('temperature_source')
    if temp and not np.isnan(temp):
        hover_text += f'Temperature: {format_value(temp, ".0f")} K'
        if temp_source != 'literature':
            hover_text += f' ({temp_source})'
        hover_text += '<br>'
    
    # Luminosity
    lum = enhanced_properties.get('luminosity')
    if lum and not np.isnan(lum):
        hover_text += f'Luminosity: {format_value(lum, ".6f")} L☉<br>'
    
    # Magnitudes
    abs_mag = enhanced_properties.get('abs_magnitude')
    app_mag = enhanced_properties.get('apparent_magnitude')
    if abs_mag and not np.isnan(abs_mag):
        hover_text += f'Absolute Magnitude: {format_value(abs_mag, ".2f")}<br>'
    if app_mag and not np.isnan(app_mag):
        hover_text += f'Apparent Magnitude: {format_value(app_mag, ".2f")}<br>'
    
    # Spectral Type
    spectral_type = host_star_data.get('spectral_type', 'Unknown')
    hover_text += f'Spectral Type: {spectral_type}'
    if 'P' in str(spectral_type).upper():
        hover_text += ' (Peculiar)'
    hover_text += '<br>'
    
    # Stellar Class
    stellar_class = enhanced_properties.get('stellar_class', 'Unknown')
    hover_text += f'Stellar Class: {stellar_class}'
    if stellar_class in class_mapping.values():
        # Already in human-readable form
        pass
    hover_text += '<br>'
    
    # Mass and Radius (physical properties)
    mass = host_star_data.get('mass_solar')
    if mass:
        hover_text += f'Mass: {format_value(mass, ".3f")} M☉<br>'
    
    radius = host_star_data.get('radius_solar')
    if radius:
        hover_text += f'Radius: {format_value(radius, ".3f")} R☉<br>'
    
    # Age (if available)
    age = host_star_data.get('age_gyr')
    if age:
        hover_text += f'Age: {format_value(age, ".1f")} Gyr<br>'
    
    # Object Type Description
    if spectral_type.startswith('M8'):
        hover_text += 'Object Type: Ultra-cool red dwarf<br>'
    elif spectral_type.startswith('M'):
        hover_text += 'Object Type: Red dwarf<br>'
    elif spectral_type.startswith('K'):
        hover_text += 'Object Type: Orange dwarf<br>'
    elif spectral_type.startswith('G'):
        hover_text += 'Object Type: Yellow dwarf (Sun-like)<br>'
    elif spectral_type.startswith('F'):
        hover_text += 'Object Type: White main-sequence star<br>'
    
    # Notable features from system
    notable_features = system_data.get('notable_features', [])
    if notable_features:
        hover_text += '<br>Note:<br>'
        for feature in notable_features:
            hover_text += f'• {feature}<br>'
    
    # Mission info (if available)
    mission_info = host_star_data.get('mission_info')
    if mission_info:
        hover_text += f'<br>{mission_info}'
    
    return hover_text


def create_binary_star_hover_text(star_data, star_label, system_data, enhanced_properties=None):
    """
    Create hover text for individual stars in a binary system.
    
    Parameters:
        star_data (dict): Individual star data (star_A or star_B)
        star_label (str): Label like "Primary" or "Secondary" or just the star name
        system_data (dict): Parent system data
        enhanced_properties (dict, optional): Pre-calculated properties
        
    Returns:
        str: HTML-formatted hover text
    """
    if enhanced_properties is None:
        enhanced_properties = calculate_host_star_properties(star_data)
    
    star_name = star_data.get('name', star_label)
    hover_text = f'<b>{star_name}</b><br>'
    hover_text += f'<i>{star_label}</i><br><br>'
    
    # Temperature
    temp = enhanced_properties.get('temperature')
    if temp and not np.isnan(temp):
        hover_text += f'Temperature: {format_value(temp, ".0f")} K<br>'
    
    # Spectral Type
    spectral_type = star_data.get('spectral_type', 'Unknown')
    hover_text += f'Spectral Type: {spectral_type}<br>'
    
    # Stellar Class
    stellar_class = enhanced_properties.get('stellar_class', 'Unknown')
    hover_text += f'Stellar Class: {stellar_class}<br>'
    
    # Mass
    mass = star_data.get('mass_solar')
    if mass:
        hover_text += f'Mass: {format_value(mass, ".3f")} M☉<br>'
    
    # Radius
    radius = star_data.get('radius_solar')
    if radius:
        hover_text += f'Radius: {format_value(radius, ".3f")} R☉<br>'
    
    # Luminosity
    lum = enhanced_properties.get('luminosity')
    if lum and not np.isnan(lum):
        hover_text += f'Luminosity: {format_value(lum, ".6f")} L☉<br>'
    
    # System context
    hover_text += f'<br>System: {system_data.get("system_name", "Unknown")}<br>'
    hover_text += f'Distance: {format_value(system_data.get("distance_ly"), ".1f")} ly'
    
    return hover_text


# ============================================================================
# MARKER SIZE CALCULATIONS
# ============================================================================

def calculate_marker_size(luminosity, base_size=8, scale_factor=2):
    """
    Calculate marker size based on stellar luminosity.
    
    Uses logarithmic scaling to show luminosity differences visually while
    keeping sizes reasonable.
    
    Parameters:
        luminosity (float): Stellar luminosity in solar units
        base_size (float): Minimum marker size
        scale_factor (float): Scaling factor for size differences
        
    Returns:
        float: Marker size in pixels
    """
    if luminosity is None or np.isnan(luminosity) or luminosity <= 0:
        return base_size
    
    # Logarithmic scaling
    size = base_size + scale_factor * np.log10(luminosity + 1)
    
    # Clamp to reasonable range
    return max(base_size, min(size, 20))


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def enrich_exoplanet_system(system_dict):
    """
    Enrich an exoplanet system dictionary with calculated stellar properties.
    
    Takes a system from exoplanet_systems.py and adds enhanced_properties
    to host_star (and star_A/star_B for binary systems).
    
    Parameters:
        system_dict (dict): System dictionary from EXOPLANET_CATALOG
        
    Returns:
        dict: Same dictionary with added 'enhanced_properties' keys
    """
    host_star = system_dict['host_star']
    
    if host_star.get('is_binary'):
        # Binary system - calculate for both stars
        props_A, props_B = calculate_binary_star_properties(
            host_star['star_A'],
            host_star['star_B']
        )
        host_star['star_A']['enhanced_properties'] = props_A
        host_star['star_B']['enhanced_properties'] = props_B
    else:
        # Single star system
        props = calculate_host_star_properties(host_star)
        host_star['enhanced_properties'] = props
    
    return system_dict


def get_exoplanet_object_type_description(spectral_type):
    """
    Get a brief object type description for exoplanet host stars.
    
    Parameters:
        spectral_type (str): Spectral type string
        
    Returns:
        str: Brief description
    """
    if not spectral_type:
        return "Unknown"
    
    sp = spectral_type.upper()
    
    if sp.startswith('M8') or sp.startswith('M9'):
        return "Ultra-cool red dwarf"
    elif sp.startswith('M'):
        return "Red dwarf"
    elif sp.startswith('K'):
        return "Orange dwarf"
    elif sp.startswith('G'):
        return "Yellow dwarf (Sun-like)"
    elif sp.startswith('F'):
        return "White main-sequence star"
    elif sp.startswith('A'):
        return "Blue-white main-sequence star"
    elif sp.startswith('B'):
        return "Hot blue star"
    elif sp.startswith('O'):
        return "Very hot blue supergiant"
    else:
        return "Star"


# ============================================================================
# TESTING AND VALIDATION
# ============================================================================

if __name__ == '__main__':
    """
    Test the stellar properties calculations with known exoplanet host stars.
    """
    print("="*80)
    print("Testing Exoplanet Stellar Properties")
    print("="*80)
    
    # Test case 1: TRAPPIST-1 (M8V ultra-cool dwarf)
    print("\nTest 1: TRAPPIST-1")
    print("-" * 40)
    
    trappist1_star = {
        'name': 'TRAPPIST-1',
        'spectral_type': 'M8V',
        'mass_solar': 0.0898,
        'radius_solar': 0.1192,
        'teff_k': 2566,
        'luminosity_solar': 0.000525,
        'distance_pc': 12.43
    }
    
    props = calculate_host_star_properties(trappist1_star)
    print(f"Temperature: {props['temperature']:.0f} K (source: {props['temperature_source']})")
    print(f"Color: {props['color']}")
    print(f"Stellar Class: {props['stellar_class']}")
    print(f"Luminosity: {props['luminosity']:.6f} L☉")
    print(f"Absolute Magnitude: {props['abs_magnitude']:.2f}")
    print(f"Apparent Magnitude: {props['apparent_magnitude']:.2f}")
    
    # Test case 2: Proxima Centauri (M5.5Ve red dwarf)
    print("\nTest 2: Proxima Centauri")
    print("-" * 40)
    
    proxima_star = {
        'name': 'Proxima Centauri',
        'spectral_type': 'M5.5Ve',
        'mass_solar': 0.1221,
        'radius_solar': 0.1542,
        'teff_k': 3042,
        'distance_pc': 1.3
    }
    
    props = calculate_host_star_properties(proxima_star)
    print(f"Temperature: {props['temperature']:.0f} K (source: {props['temperature_source']})")
    print(f"Color: {props['color']}")
    print(f"Stellar Class: {props['stellar_class']}")
    print(f"Luminosity: {props['luminosity']:.6f} L☉")
    
    # Test case 3: Temperature color interpolation
    print("\nTest 3: Temperature Color Scale")
    print("-" * 40)
    test_temps = [2000, 2566, 3042, 5772, 7500, 15000, 30000]
    for temp in test_temps:
        color = get_temperature_color(temp)
        print(f"{temp:5.0f} K -> {color}")
    
    print("\n" + "="*80)
    print("All tests completed!")
    print("="*80)
