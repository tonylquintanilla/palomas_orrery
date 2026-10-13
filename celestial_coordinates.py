"""
celestial_coordinates.py
Module for calculating and formatting Right Ascension and Declination coordinates
for celestial objects in Paloma's Orrery.

Role: computation
Domain: orrery

Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
build 1: the typed sky-position table MAJOR_BODY_UNCERTAINTIES and its
"typical" fallbacks are removed; the hover prints only JPL's fetched
3-sigma figure, says "as seen from Earth", and says in words when JPL
gives none.)
Module updated: October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401,
Tony's look, option B: the sky position under one heading, "Sky position
seen from Earth:", with one uncertainty line in the same form for every
body, in place of a note in parentheses on each coordinate.)
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
    
    # Format Dec string (+/-DD deg MM' SS.S")
    dec_sign = '+' if dec_degrees >= 0 else ''
    if dec_degrees < 0 and dec_arcmin == 0 and dec_arcsec < 1:
        # Handle case where declination is slightly negative but rounds to 0
        dec_sign = '-'
        dec_string = f"{dec_sign}{abs(dec_degrees):02d} deg {dec_arcmin:02d}' {dec_arcsec:0{3+precision_dec_arcsec}.{precision_dec_arcsec}f}\""
    else:
        dec_string = f"{dec_sign}{dec_degrees:02d} deg {abs(dec_arcmin):02d}' {abs(dec_arcsec):0{3+precision_dec_arcsec}.{precision_dec_arcsec}f}\""
    
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
    dec_string = f"{dec_sign}{dec_decimal_degrees:.{precision}f} deg"
    
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
        dec_string = f"{'+' if dec_degrees >= 0 else ''}{dec_degrees:02d} deg {abs(dec_arcmin):02d}' {abs(dec_arcsec):05.2f}\""
        
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


# The sky position's uncertainty (L-401, build 1, 2026-10-12). Only JPL's
# own 3-sigma figures, fetched with the position, are printed. The typed
# table of planet and moon uncertainties that stood here, and its fallbacks
# marked "typical" for everything else, had no source line and are removed: the
# DE440 paper gives no angular accuracy for a planet (read by GPT, Claude
# Fable 5.1 and Claude Opus 5.5, 2026-10-11). Where Horizons gives no
# figure the hover says so in words ("Horizons gives no uncertainty with
# it": a spacecraft's data sheet may state one). A sourced figure for a
# planet, worked
# out from its position row and its distance from Earth, is kept for later
# on L-401.

def get_precision_note(obj_data, obj_name=None):
    """
    JPL's 3-sigma sky-position uncertainty as fetched with the position,
    e.g. "+/-0.5 arcsec", or None when Horizons gave none.

    Parameters:
        obj_data (dict): Object data, with 'ra_3sigma' and 'dec_3sigma' in
            arcseconds where fetch_radec_for_hover found them
        obj_name (str): unused; kept so existing callers need not change

    Returns:
        str or None
    """
    if 'ra_3sigma' in obj_data and obj_data['ra_3sigma'] is not None:
        ra_sigma = obj_data['ra_3sigma']  # in arcseconds
        dec_sigma = obj_data.get('dec_3sigma', ra_sigma)  # in arcseconds
        
        # Use the larger of the two for a conservative estimate
        max_sigma = max(ra_sigma, dec_sigma) if dec_sigma is not None else ra_sigma
        try:
            if not math.isfinite(float(max_sigma)):
                return None   # a masked "n.a." read as nan is no figure
        except (TypeError, ValueError):
            return None
        
        # Format based on magnitude
        if max_sigma < 0.001:
            return f"+/-{max_sigma:.4f} arcsec"
        elif max_sigma < 0.01:
            return f"+/-{max_sigma:.3f} arcsec"
        elif max_sigma < 0.1:
            return f"+/-{max_sigma:.2f} arcsec"
        elif max_sigma < 1:
            return f"+/-{max_sigma:.2f} arcsec"
        elif max_sigma < 10:
            return f"+/-{max_sigma:.1f} arcsec"
        else:
            return f"+/-{max_sigma:.0f} arcsec"
    return None


def format_radec_hover_component(obj_data, obj_name=None, compact=False):
    """
    Format RA/Dec for hover text: a heading, "Sky position seen from
    Earth:" (fetch_radec_for_hover asks from Earth's centre), the two
    coordinates, and one uncertainty line -- JPL's fetched 3-sigma figure
    where Horizons gives one, plain words where it does not.
    
    Parameters:
        obj_data (dict): Object data possibly containing JPL uncertainties
        obj_name (str): Name of the object (optional)
        compact (bool): Whether to use compact formatting
        
    Returns:
        str: Formatted RA/Dec string for hover text
    """
    
    ra_string, dec_string = extract_jpl_radec(obj_data)
    
    if not ra_string or not dec_string:
        return ""
    
    # Tony's look at L-401 build 1 (2026-10-12, option B): one heading that
    # says what the two numbers are, the two coordinates, and one
    # uncertainty line in the same form for every body.
    precision_note = get_precision_note(obj_data, obj_name)
    if precision_note:
        uncertainty = f"Uncertainty: {precision_note} (JPL, 3-sigma)"
    else:
        # "With this position": the query returned none. A spacecraft's
        # data sheet can state a predicted one for another date (the
        # Voyagers, for 2030, read 2026-10-12, L-401).
        uncertainty = "Uncertainty: none given by JPL with this position"
    
    if compact:
        return (f"Sky position seen from Earth: RA {ra_string}, Dec {dec_string}<br>"
                f"{uncertainty}")
    else:
        return (f"Sky position seen from Earth:<br>"
                f"Right Ascension: {ra_string}<br>"
                f"Declination: {dec_string}<br>"
                f"{uncertainty}")


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

