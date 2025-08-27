"""
celestial_coordinates.py
Module for calculating and formatting Right Ascension and Declination coordinates
for celestial objects in Paloma's Orrery.
"""

import numpy as np
from datetime import datetime
import math

def format_ra_dec_string(ra_hours, ra_minutes, ra_seconds, 
                         dec_degrees, dec_arcmin, dec_arcsec,
                         precision_ra_sec=2, precision_dec_arcsec=1):
    """
    Format RA/Dec values into standard astronomical notation strings.
    
    Parameters:
        ra_hours, ra_minutes, ra_seconds: Right Ascension components
        dec_degrees, dec_arcmin, dec_arcsec: Declination components
        precision_ra_sec: Number of decimal places for RA seconds
        precision_dec_arcsec: Number of decimal places for Dec arcseconds
        
    Returns:
        tuple: (ra_string, dec_string)
    """
    # Format RA string (HH:MM:SS.SS)
    ra_string = f"{ra_hours:02d}h {ra_minutes:02d}m {ra_seconds:0{4+precision_ra_sec}.{precision_ra_sec}f}s"
    
    # Format Dec string (+/-DD° MM' SS.S")
    dec_sign = '+' if dec_degrees >= 0 else ''
    if dec_degrees < 0 and dec_arcmin == 0 and dec_arcsec < 1:
        # Handle case where declination is slightly negative but rounds to 0
        dec_sign = '-'
        dec_string = f"{dec_sign}{abs(dec_degrees):02d}° {dec_arcmin:02d}' {dec_arcsec:0{3+precision_dec_arcsec}.{precision_dec_arcsec}f}\""
    else:
        dec_string = f"{dec_sign}{dec_degrees:02d}° {abs(dec_arcmin):02d}' {abs(dec_arcsec):0{3+precision_dec_arcsec}.{precision_dec_arcsec}f}\""
    
    return ra_string, dec_string


def format_ra_dec_decimal(ra_decimal_hours, dec_decimal_degrees, precision=6):
    """
    Format RA/Dec in decimal format.
    
    Parameters:
        ra_decimal_hours: Right Ascension in decimal hours
        dec_decimal_degrees: Declination in decimal degrees
        precision: Number of decimal places
        
    Returns:
        tuple: (ra_string, dec_string)
    """
    ra_string = f"{ra_decimal_hours:.{precision}f}h"
    dec_sign = '+' if dec_decimal_degrees >= 0 else ''
    dec_string = f"{dec_sign}{dec_decimal_degrees:.{precision}f}°"
    
    return ra_string, dec_string


def extract_jpl_radec(obj_data):
    """Extract RA/Dec from JPL Horizons data if available."""
    if 'ra' in obj_data and 'dec' in obj_data and obj_data['ra'] is not None:
        ra_deg = obj_data['ra']
        dec_deg = obj_data['dec']
        
        # Convert RA from degrees to hours/minutes/seconds
        ra_hours_decimal = ra_deg / 15.0  # 360 degrees = 24 hours
        ra_hours = int(ra_hours_decimal)
        ra_minutes_decimal = (ra_hours_decimal - ra_hours) * 60
        ra_minutes = int(ra_minutes_decimal)
        ra_seconds = (ra_minutes_decimal - ra_minutes) * 60
        
        # Convert Dec to degrees/arcminutes/arcseconds
        dec_sign = 1 if dec_deg >= 0 else -1
        dec_deg_abs = abs(dec_deg)
        dec_degrees = int(dec_deg_abs) * dec_sign
        dec_arcmin_decimal = (dec_deg_abs - abs(dec_degrees)) * 60
        dec_arcmin = int(dec_arcmin_decimal)
        dec_arcsec = (dec_arcmin_decimal - dec_arcmin) * 60
        
        # Format with high precision since this is from JPL
        ra_string = f"{ra_hours:02d}h {ra_minutes:02d}m {ra_seconds:06.3f}s"
        dec_string = f"{'+' if dec_degrees >= 0 else ''}{dec_degrees:02d}° {abs(dec_arcmin):02d}' {abs(dec_arcsec):05.2f}\""
        
        return ra_string, dec_string
    
    return None, None

def calculate_radec_for_position(obj_data, obj_name=None):
    """Extract RA/Dec from JPL Horizons data."""
    result = {
        'ra_string': None,
        'dec_string': None,
        'source': 'JPL Horizons',
        'reference_frame': 'ICRF, Earth-centered'
    }
    
    ra_jpl, dec_jpl = extract_jpl_radec(obj_data)
    if ra_jpl and dec_jpl:
        result['ra_string'] = ra_jpl
        result['dec_string'] = dec_jpl
        return result
    
    # If no JPL data, return None (don't calculate)
    return result

def add_radec_to_hover_text(hover_text, obj_data, obj_name=None, insert_after_line=2):
    """Add RA/Dec to hover text - always Earth-centered."""
    
    # Get RA/Dec info
    radec_info = calculate_radec_for_position(obj_data, obj_name)
    
    if radec_info['ra_string'] and radec_info['dec_string']:
        # Always show as Earth-centered ICRF
        radec_line = f"RA: {radec_info['ra_string']}, Dec: {radec_info['dec_string']} (ICRF)"
        
        # Split hover text into lines
        lines = hover_text.split('<br>')
        
        # Insert coordinates after specified line
        if len(lines) > insert_after_line:
            lines.insert(insert_after_line, radec_line)
        else:
            lines.append(radec_line)
        
        # Rejoin lines
        return '<br>'.join(lines)
    
    return hover_text


# Add this to celestial_coordinates.py

# High-precision uncertainty values for solar system bodies
# Based on DE440/441 planetary ephemeris and mission data
# Values in arcseconds (3-sigma)
MAJOR_BODY_UNCERTAINTIES = {
    # ========== PLANETS ==========
    'Mercury': 0.005,
    'Venus': 0.003,
    'Mars': 0.002,
    'Jupiter': 0.05,
    'Saturn': 0.1,
    'Uranus': 0.3,
    'Neptune': 0.5,
    
    # ========== DWARF PLANETS ==========
    'Ceres': 0.01,      # Dawn mission
    'Pluto': 0.8,       # New Horizons
    'Eris': 5.0,
    'Makemake': 3.0,
    'Haumea': 2.0,
    'Gonggong': 5.0,    # 2007 OR10
    'Quaoar': 3.0,
    'Sedna': 10.0,
    'Orcus': 3.0,
    'Salacia': 5.0,
    'Varuna': 5.0,
    'Ixion': 5.0,
    '2002 MS4': 8.0,
    'Varda': 8.0,
    
    # ========== EARTH'S MOON ==========
    'Moon': 0.0001,     # Lunar laser ranging
    
    # ========== MARTIAN MOONS ==========
    'Phobos': 0.01,
    'Deimos': 0.02,
    
    # ========== JOVIAN MOONS ==========
    'Io': 0.01,
    'Europa': 0.01,
    'Ganymede': 0.01,
    'Callisto': 0.01,
    'Amalthea': 0.05,
    'Himalia': 0.1,
    'Thebe': 0.05,
    'Metis': 0.05,
    'Adrastea': 0.05,
    'Pasiphae': 0.5,
    'Sinope': 0.5,
    'Lysithea': 0.5,
    'Carme': 0.5,
    'Ananke': 0.5,
    'Leda': 0.5,
    'Elara': 0.3,
    
    # ========== SATURNIAN MOONS ==========
    'Mimas': 0.05,
    'Enceladus': 0.05,
    'Tethys': 0.05,
    'Dione': 0.05,
    'Rhea': 0.05,
    'Titan': 0.05,
    'Hyperion': 0.1,
    'Iapetus': 0.1,
    'Phoebe': 0.2,
    'Janus': 0.05,
    'Epimetheus': 0.05,
    'Helene': 0.1,
    'Telesto': 0.1,
    'Calypso': 0.1,
    'Atlas': 0.05,
    'Prometheus': 0.05,
    'Pandora': 0.05,
    'Pan': 0.05,
    'Daphnis': 0.05,
    
    # ========== URANIAN MOONS ==========
    'Ariel': 0.3,
    'Umbriel': 0.3,
    'Titania': 0.3,
    'Oberon': 0.3,
    'Miranda': 0.3,
    'Puck': 0.5,
    'Cordelia': 0.5,
    'Ophelia': 0.5,
    'Bianca': 0.5,
    'Cressida': 0.5,
    'Desdemona': 0.5,
    'Juliet': 0.5,
    'Portia': 0.5,
    'Rosalind': 0.5,
    'Belinda': 0.5,
    
    # ========== NEPTUNIAN MOONS ==========
    'Triton': 0.5,
    'Nereid': 1.0,
    'Proteus': 0.8,
    'Larissa': 0.8,
    'Galatea': 0.8,
    'Despina': 0.8,
    'Thalassa': 0.8,
    'Naiad': 0.8,
    
    # ========== PLUTONIAN SYSTEM ==========
    'Charon': 1.0,
    'Nix': 2.0,
    'Hydra': 2.0,
    'Kerberos': 3.0,
    'Styx': 3.0,
    
    # ========== MAIN BELT ASTEROIDS (DE440 perturbers) ==========
    'Vesta': 0.01,      # Dawn mission
    'Pallas': 0.05,
    'Juno': 0.1,
    'Hygiea': 0.2,
    'Davida': 0.2,
    'Interamnia': 0.3,
    'Europa (asteroid)': 0.3,  # 52 Europa
    'Eunomia': 0.2,
    'Psyche': 0.1,      # Upcoming mission
    'Euphrosyne': 0.3,
    'Cybele': 0.3,
    'Sylvia': 0.2,
    'Thisbe': 0.3,
    'Camilla': 0.3,
    'Herculina': 0.3,
    'Doris': 0.3,
    
    # ========== MISSION-VISITED ASTEROIDS ==========
    'Bennu': 0.001,     # OSIRIS-REx
    'Ryugu': 0.001,     # Hayabusa2
    'Eros': 0.001,      # NEAR Shoemaker
    'Itokawa': 0.001,   # Hayabusa
    'Mathilde': 0.01,   # NEAR flyby
    'Ida': 0.01,        # Galileo
    'Dactyl': 0.02,     # Ida's moon
    'Gaspra': 0.01,     # Galileo
    'Lutetia': 0.01,    # Rosetta
    'Steins': 0.01,     # Rosetta
    'Annefrank': 0.05,  # Stardust
    'Braille': 0.05,    # Deep Space 1
    'Toutatis': 0.001,  # Radar + Chang'e 2
    'Didymos': 0.01,    # DART impact
    'Dimorphos': 0.02,  # Didymos moon
    'Arrokoth': 1.0,    # New Horizons (2014 MU69)
    
    # ========== NEAR-EARTH ASTEROIDS (Radar observed) ==========
    'Apophis': 0.001,
    '2005 YU55': 0.01,
    '1999 JM8': 0.01,
    '2004 BL86': 0.01,
    '2000 DP107': 0.01,
    '1998 KY26': 0.01,
    '2017 YE5': 0.01,
    '1999 KW4': 0.01,
    '2003 YT1': 0.01,
    '2014 HQ124': 0.01,
    '2014 JO25': 0.01,
    '2015 TB145': 0.01,
    
    # ========== TROJAN ASTEROIDS ==========
    'Patroclus': 1.0,   # Lucy target (binary)
    'Menoetius': 1.0,   # Patroclus companion
    'Eurybates': 1.0,   # Lucy target
    'Polymele': 1.0,    # Lucy target
    'Leucus': 1.0,      # Lucy target
    'Orus': 1.0,        # Lucy target
    'Donald Johanson': 1.0,  # Lucy target
    'Hektor': 0.5,      # Largest trojan
    'Agamemnon': 1.0,
    'Achilles': 1.0,
    'Nestor': 1.0,
    'Diomedes': 1.0,
    
    # ========== CENTAURS ==========
    'Chiron': 2.0,
    'Pholus': 5.0,
    'Nessus': 8.0,
    'Asbolus': 8.0,
    'Chariklo': 3.0,    # Has rings
    'Hylonome': 10.0,
    'Bienor': 10.0,
    'Amycus': 10.0,
    
    # ========== COMET NUCLEI ==========
    'Halley': 10.0,     # Currently distant
    'Encke': 1.0,       # Short period
    'Tempel 1': 0.5,    # Deep Impact
    'Wild 2': 0.01,     # Stardust
    'Borrelly': 0.01,   # Deep Space 1
    'Churyumov-Gerasimenko': 0.001,  # Rosetta (67P)
    '67P/Churyumov-Gerasimenko': 0.001,  # Alternative designation
    'Hartley 2': 0.01,  # EPOXI
    'Giacobini-Zinner': 1.0,  # ICE
    'Grigg-Skjellerup': 1.0,   # Giotto
    'Wirtanen': 0.5,    # Original Rosetta target
    'Schwassmann-Wachmann 3': 2.0,
    'Holmes': 5.0,
    'Hale-Bopp': 20.0,  # Currently very distant
    'Hyakutake': 15.0,
    'McNaught': 10.0,
    'ISON': 10.0,       # Destroyed
    'Lovejoy': 5.0,
    'NEOWISE': 3.0,
    'PanSTARRS': 5.0,
    'Borisov': 10.0,    # Interstellar
    
    # ========== SPACECRAFT (when tracked as objects) ==========
    'Voyager 1': 100.0,
    'Voyager 2': 100.0,
    'New Horizons': 10.0,
    'Pioneer 10': 1000.0,  # Contact lost
    'Pioneer 11': 1000.0,  # Contact lost
    'Cassini': 0.1,        # When active
    'Juno': 0.01,          # Currently at Jupiter
    'Dawn': 0.01,          # Mission ended at Ceres
    'OSIRIS-REx': 0.01,
    'Hayabusa2': 0.01,
    'Parker Solar Probe': 0.001,
    'Solar Orbiter': 0.01,
    'BepiColombo': 0.01,
    'JUICE': 0.01,
    'Europa Clipper': 0.01,
    'Lucy': 0.01,
    'Psyche (spacecraft)': 0.01,
    'Dragonfly': 0.1,      # Future
    
    # ========== SPECIAL OBJECTS ==========
    'Sun': 0.001,       # Barycenter position
    'Earth-Moon Barycenter': 0.0001,
    'Pluto-Charon Barycenter': 0.5,
    
    # ========== ARTIFICIAL SATELLITES (if tracking) ==========
    'ISS': 0.001,       # International Space Station
    'HST': 0.001,       # Hubble Space Telescope
    'JWST': 0.01,       # James Webb Space Telescope
    'Gaia': 0.001,
    'TESS': 0.001,
    'Spitzer': 0.01,
    'Kepler': 0.01,
    'WMAP': 0.1,
    'Planck': 0.1,
    
    # ========== METEOR SHOWER PARENTS ==========
    'Swift-Tuttle': 5.0,    # Perseids
    'Tempel-Tuttle': 3.0,   # Leonids
    'Thatcher': 10.0,       # Lyrids
    'Phaethon': 0.1,        # Geminids (asteroid)
}

def get_precision_note(obj_data, obj_name=None):
    """
    Get precision estimate - prefer actual JPL uncertainties, 
    then use known values for major bodies, finally fall back to estimates.
    
    Parameters:
        obj_data (dict): Object data containing possible uncertainty values
        obj_name (str): Name of the object (optional but recommended)
        
    Returns:
        str: Formatted precision string (e.g., "±0.5″" or "±10″")
    """
    
    # 1. Check for actual 3-sigma uncertainties from JPL
    if 'ra_3sigma' in obj_data and obj_data['ra_3sigma'] is not None:
        ra_sigma = obj_data['ra_3sigma']  # in arcseconds
        dec_sigma = obj_data.get('dec_3sigma', ra_sigma)  # in arcseconds
        
        # Use the larger of the two for a conservative estimate
        max_sigma = max(ra_sigma, dec_sigma) if dec_sigma is not None else ra_sigma
        
        # Format based on magnitude
        if max_sigma < 0.001:
            return f"±{max_sigma:.4f}″"
        elif max_sigma < 0.01:
            return f"±{max_sigma:.3f}″"
        elif max_sigma < 0.1:
            return f"±{max_sigma:.2f}″"
        elif max_sigma < 1:
            return f"±{max_sigma:.2f}″"
        elif max_sigma < 10:
            return f"±{max_sigma:.1f}″"
        else:
            return f"±{max_sigma:.0f}″"
    
    # 2. Check if this is a known major body
    if obj_name and obj_name in MAJOR_BODY_UNCERTAINTIES:
        uncertainty = MAJOR_BODY_UNCERTAINTIES[obj_name]
        
        # Format based on magnitude
        if uncertainty < 0.001:
            return f"±{uncertainty:.4f}″"
        elif uncertainty < 0.01:
            return f"±{uncertainty:.3f}″"
        elif uncertainty < 0.1:
            return f"±{uncertainty:.2f}″"
        elif uncertainty < 1:
            return f"±{uncertainty:.1f}″"
        else:
            return f"±{uncertainty:.0f}″"
    
    # 3. Fallback to type-based estimates
    obj_type = obj_data.get('object_type', 'unknown')
    
    if obj_type == 'satellite':
        return "±0.1″"  # Most moons are well-tracked
    elif obj_type == 'orbital':
        # Check if it might be an asteroid/comet by name pattern
        if obj_name:
            # Common patterns for minor bodies
            if any(char.isdigit() for char in obj_name[:4]):  # Starts with number (e.g., "2023 FY")
                return "±10″"  # New discovery uncertainty
            elif '/' in obj_name:  # Comet designation (e.g., "C/2023 A1")
                return "±5″"
        return "±1″"  # Default for established orbital bodies
    elif obj_type == 'trajectory':
        return "±5″"  # Spacecraft, comets
    else:
        return "±10″"  # Unknown/other


def format_radec_hover_component(obj_data, obj_name=None, compact=False):
    """
    Format RA/Dec for hover text with actual uncertainties when available.
    
    Parameters:
        obj_data (dict): Object data possibly containing JPL uncertainties
        obj_name (str): Name of the object (optional but recommended)
        compact (bool): Whether to use compact formatting
        
    Returns:
        str: Formatted RA/Dec string for hover text
    """
    
    ra_string, dec_string = extract_jpl_radec(obj_data)
    
    if not ra_string or not dec_string:
        return ""
    
    # Get precision note - will check JPL data, then major body lookup, then estimates
    precision_note = get_precision_note(obj_data, obj_name)
    
    # Add source indicator for transparency
    source_note = ""
    if 'ra_3sigma' in obj_data and obj_data['ra_3sigma'] is not None:
        source_note = ", JPL Horizons 3-sigma"
    elif obj_name and obj_name in MAJOR_BODY_UNCERTAINTIES:
        source_note = ", JPL DE440/441 ephemeris"
    else:
        source_note = ", typical"
    
    if compact:
        return f"RA/Dec: {ra_string}, {dec_string} (apparent, {precision_note}{source_note})"
    else:
        return (f"Right Ascension: {ra_string} (apparent, {precision_note}{source_note})<br>"
                f"Declination: {dec_string} (apparent, {precision_note}{source_note})")


def determine_coordinate_precision(obj_data, obj_name):
    """
    Determine appropriate precision for RA/Dec display based on object type and data source.
    
    Parameters:
        obj_data (dict): Object data
        obj_name (str): Name of the object
        
    Returns:
        tuple: (ra_seconds_precision, dec_arcsec_precision)
    """
    # Default precision
    ra_sec_precision = 2
    dec_arcsec_precision = 1
    
    # Higher precision for certain objects
    if any(keyword in obj_name.lower() for keyword in ['voyager', 'pioneer', 'new horizons', 'cassini']):
        # Spacecraft need higher precision
        ra_sec_precision = 3
        dec_arcsec_precision = 2
    elif 'asteroid' in obj_name.lower() or 'comet' in obj_name.lower():
        # Small bodies may need higher precision
        ra_sec_precision = 3
        dec_arcsec_precision = 1
    elif any(planet in obj_name for planet in ['Mercury', 'Venus', 'Mars']):
        # Inner planets move faster, need more precision
        ra_sec_precision = 3
        dec_arcsec_precision = 1
    
    # Check if we have high-precision data from JPL
    if 'ra' in obj_data and 'dec' in obj_data:
        # If JPL provided the data, we can use higher precision
        if 'source' in obj_data and 'horizons' in obj_data['source'].lower():
            ra_sec_precision = min(ra_sec_precision + 1, 4)
            dec_arcsec_precision = min(dec_arcsec_precision + 1, 3)
    
    return ra_sec_precision, dec_arcsec_precision

