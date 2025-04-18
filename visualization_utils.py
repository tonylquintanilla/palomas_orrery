"""visualization_utils.py - Shared utilities for visualization functions."""

import plotly.graph_objects as go
import numpy as np
from formatting_utils import format_maybe_float, format_km_float

def add_hover_toggle_buttons(fig):     
    """
    Add hover text toggle buttons to any Plotly figure.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add buttons to
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with hover toggle buttons
        
    Note:
        Traces must include both 'text' (full hover info) and 'customdata' (minimal hover info)
        properties for the toggle to work correctly.
    """
    # Get existing updatemenus and convert to list
    updatemenus = list(fig.layout.updatemenus) if hasattr(fig.layout, 'updatemenus') and fig.layout.updatemenus is not None else []
    
    # Create hover text toggle buttons
    hover_buttons = dict(
        type="buttons",
        direction="right",
        x=0.2,
        y=0.2,
        buttons=[
            dict(
                label="Full Object Info",
                method="update",
        #        args=[{"hovertemplate": None}]
                args=[{"hovertemplate": "%{text}<extra></extra>"}]
                # Enhanced hover template with semi-transparent background
        #        args=[{"hovertemplate": "<div style='background-color:rgba(0,0,0,0); color:white; padding:10px; border-radius:5px;'>%{text}</div><extra></extra>"}]
            ),
            dict(
                label="Object Names Only",
                method="update",
                args=[{"hovertemplate": '%{customdata}<extra></extra>'}]
                # Enhanced hover template with semi-transparent background
        #        args=[{"hovertemplate": "<div style='background-color:rgba(0,0,0,0); color:white; padding:5px; border-radius:5px;'>%{text}</div><extra></extra>"}]
            ),
        ],
        font=dict(color='blue'),        # button parameters
        bgcolor='rgba(255,255,255,0.70)',
        bordercolor='white',
        borderwidth=1,
    )
    
    # Add hover buttons to updatemenus
    updatemenus.append(hover_buttons)
    
    # Update figure layout
    fig.update_layout(updatemenus=updatemenus)

    # Update default hovertemplate for all traces that aren't orbits
    for trace in fig.data:
        if trace.hoverinfo != 'skip':  # Skip orbit traces
            trace.hovertemplate = "%{text}<extra></extra>"  # Set default template
    
    return fig

def format_hover_text(obj_data, name, is_solar_system=False):
    """
    Format hover text consistently for different types of objects.
    
    Parameters:
        obj_data (dict): Object data containing position and other properties
        name (str): Name of the object
        is_solar_system (bool): Whether this is a solar system object
        
    Returns:
        tuple: (full_hover_text, minimal_hover_text)
    """
    minimal_hover_text = f"<b>{name}</b>"
    
    if is_solar_system:
        # Format values with proper handling of non-numeric values
        range_str = f"{obj_data.get('range', 'N/A'):.5f}" if isinstance(obj_data.get('range'), (int, float)) else 'N/A'
        dist_lm_str = f"{obj_data.get('distance_lm', 'N/A'):.5f}" if isinstance(obj_data.get('distance_lm'), (int, float)) else 'N/A'
        dist_lh_str = f"{obj_data.get('distance_lh', 'N/A'):.5f}" if isinstance(obj_data.get('distance_lh'), (int, float)) else 'N/A'
        vel_str = f"{obj_data.get('velocity', 'N/A'):.5f}" if isinstance(obj_data.get('velocity'), (int, float)) else 'N/A'
        
        # Build hover text
        full_hover_text = (
            f"<b>{name}</b><br><br>"
            f"Distance from Center: {range_str} AU<br>"
            f"Distance: {dist_lm_str} light-minutes<br>"
            f"Distance: {dist_lh_str} light-hours<br>"
            f"Velocity: {vel_str} AU/day<br>"
            f"Orbital Period: {obj_data.get('orbital_period', 'N/A')} Earth years"
        )
        
        if obj_data.get('mission_info'):
            full_hover_text += f"<br>{obj_data['mission_info']}"
    else:
        # Format for stellar objects with proper handling of non-numeric values
        dist_pc = obj_data.get('Distance_pc', 'N/A')
        dist_ly = obj_data.get('Distance_ly', 'N/A')
        temp = obj_data.get('Temperature', 'N/A')
        lum = obj_data.get('Luminosity', 'N/A')
        app_mag = obj_data.get('Apparent_Magnitude', 'N/A')
        
        dist_pc_str = f"{dist_pc:.2f}" if isinstance(dist_pc, (int, float)) else 'N/A'
        dist_ly_str = f"{dist_ly:.2f}" if isinstance(dist_ly, (int, float)) else 'N/A'
        temp_str = f"{temp:.0f}" if isinstance(temp, (int, float)) else 'N/A'
        lum_str = f"{lum:.6f}" if isinstance(lum, (int, float)) else 'N/A'
        app_mag_str = f"{app_mag:.2f}" if isinstance(app_mag, (int, float)) else 'N/A'
        
        full_hover_text = (
            f"<b>{name}</b><br><br>"
            f"Distance: {dist_pc_str} pc ({dist_ly_str} ly)<br>"
            f"Temperature: {temp_str} K<br>"
            f"Luminosity: {lum_str} Lsun<br>"
            f"Apparent Magnitude: {app_mag_str}<br>"
            f"Spectral Type: {obj_data.get('Spectral_Type', 'Unknown')}<br>"
            f"Source Catalog: {obj_data.get('Source_Catalog', 'Unknown')}"
        )
    
    return full_hover_text, minimal_hover_text

def format_detailed_hover_text(obj_data, obj_name, center_object_name, objects, planetary_params, parent_planets, CENTER_BODY_RADII, KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS):
    """
    Generate detailed hover text for celestial objects with comprehensive information.
    
    Parameters:
        obj_data (dict): Object position data
        obj_name (str): Name of the celestial object
        center_object_name (str): Name of the center body
        objects (list): List of all celestial objects
        planetary_params (dict): Dictionary of planetary parameters
        parent_planets (dict): Dictionary mapping planets to their satellites
        CENTER_BODY_RADII (dict): Dictionary of body radii in km
        KM_PER_AU (float): Conversion factor from AU to km
        LIGHT_MINUTES_PER_AU (float): Conversion factor from AU to light-minutes
        KNOWN_ORBITAL_PERIODS (dict): Dictionary of known orbital periods
        
    Returns:
        tuple: (full_hover_text, minimal_hover_text, satellite_note)
    """
    # Calculate distance from center
    distance_from_origin = np.sqrt(obj_data['x']**2 + obj_data['y']**2 + obj_data['z']**2)
    
    # Format values with proper formatting functions
    distance_au = format_maybe_float(distance_from_origin)
    distance_km = format_km_float(distance_from_origin * KM_PER_AU)
    distance_lm = format_maybe_float(distance_from_origin * LIGHT_MINUTES_PER_AU)
    distance_lh = format_maybe_float(distance_from_origin * LIGHT_MINUTES_PER_AU / 60)
    velocity_au = format_maybe_float(obj_data.get('velocity', 'N/A'))
    
    # Calculate velocity in km/hr
    velocity_km_hr = "N/A"
    if isinstance(obj_data.get('velocity'), (int, float)):
        velocity_km_hr = f"{obj_data.get('velocity') * KM_PER_AU / 24:,.2f}"
    
    # Calculate surface distance if we have valid distance data
    center_radius_km = CENTER_BODY_RADII.get(center_object_name, 0)  # Default to 0 if center body not found
    surface_distance_str = "N/A"
    
    if isinstance(distance_from_origin * KM_PER_AU, (int, float)) and (distance_from_origin * KM_PER_AU) > center_radius_km:
        surface_distance_km = (distance_from_origin * KM_PER_AU) - center_radius_km
        surface_distance_str = format_km_float(surface_distance_km)
    
    # Check if this is a planetary satellite
    is_satellite = False
    planet = None
    for p, satellites in parent_planets.items():
        if obj_name in satellites:
            is_satellite = True
            planet = p
            break
    
    # Get orbital period information
    calculated_period = "N/A"
    known_period = "N/A"
    
    # Calculate orbital period for non-satellites
    if not is_satellite and obj_name in planetary_params:
        a = planetary_params[obj_name]['a']  # Semi-major axis in AU
        orbital_period_years = np.sqrt(a ** 3)  # Period in Earth years
        calculated_period = {
            'years': orbital_period_years,
            'days': orbital_period_years * 365.25
        }
    
    # Format calculated period
    if isinstance(calculated_period, dict):
        calc_years = calculated_period.get('years')
        calc_days = calculated_period.get('days')
        calculated_period_str = f"{calc_years:.4f} Earth years ({calc_days:.2f} days)"
    else:
        calculated_period_str = str(calculated_period)
    
    # Get known orbital period if available
    if obj_name in KNOWN_ORBITAL_PERIODS:
        known_value = KNOWN_ORBITAL_PERIODS[obj_name]
        
        if is_satellite:
            # For satellites, the values are in days
            known_period = {
                'days': known_value,
                'years': known_value / 365.25
            }
        else:
            # For non-satellites, the values are in years
            known_period = {
                'years': known_value,
                'days': known_value * 365.25
            }
    
    # Format known period
    if isinstance(known_period, dict):
        known_years = known_period.get('years')
        known_days = known_period.get('days')
        known_period_str = f"{known_years:.4f} Earth years ({known_days:.2f} days)"
    else:
        known_period_str = str(known_period)
    
    # Calculate percent difference between calculated and known orbital periods
    period_diff_percent = "N/A"
    if (not is_satellite and 
        isinstance(calculated_period, dict) and 
        isinstance(known_period, dict) and
        isinstance(calculated_period.get('years'), (int, float)) and 
        isinstance(known_period.get('years'), (int, float)) and
        known_period.get('years') != 0):
        
        calc_years = calculated_period.get('years')
        known_years = known_period.get('years')
        period_diff = abs(calc_years - known_years)
        period_diff_percent = f"{(period_diff / known_years * 100):.2f}"
    
    # Find the object's info in the objects list
    obj_info = next((o for o in objects if o['name'] == obj_name), None)
    mission_info = obj_info.get('mission_info', '') if obj_info else ''
    
    # Now build the hover text
    full_hover_text = (
        f"<b>{obj_name}</b><br><br>"
        f"Distance from Center: {distance_au} AU<br>"
        f"Distance: {distance_km} kilometers<br>"
        f"Distance: {distance_lm} light-minutes<br>"
        f"Distance: {distance_lh} light-hours<br>"
        f"Distance to Center Surface: {surface_distance_str} kilometers<br>"
        f"Velocity: {velocity_au} AU/day<br>"
        f"Velocity: {velocity_km_hr} km/hr<br>"
    )
    
    # Add orbital period information
    if is_satellite:
        full_hover_text += f"Calculated Orbital Period: N/A (satellite of {planet})<br>"
    else:
        full_hover_text += f"Calculated Orbital Period: {calculated_period_str}<br>"
    
    # Add known period if available
    if period_diff_percent != "N/A":
        full_hover_text += f"Known Orbital Period: {known_period_str} (Percent difference: {period_diff_percent}%)"
    else:
        full_hover_text += f"Known Orbital Period: {known_period_str}"
    
    # Add mission_info if it exists
    if mission_info:
        full_hover_text += f"<br>{mission_info}"
    
    # Determine if this is a satellite of the center object specifically
    satellite_note = ""
    if is_satellite and planet == center_object_name:
        satellite_note = f"<br>Moon of {center_object_name}"
    
    minimal_hover_text = f"<b>{obj_name}</b>"
    
    return full_hover_text, minimal_hover_text, satellite_note

def update_figure_frames(fig, include_hover_toggle=True):
    """
    Update figure frames to maintain hover text toggle functionality in animations.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure containing frames
        include_hover_toggle (bool): Whether to include hover toggle buttons
    
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    if not hasattr(fig, 'frames') or not fig.frames:
        return fig
        
    # Add hover toggle buttons if requested
    if include_hover_toggle:
        fig = add_hover_toggle_buttons(fig)
    
    # Ensure frames maintain hover text format
    for frame in fig.frames:
        for trace in frame.data:
            if hasattr(trace, 'hovertemplate'):
                trace.hovertemplate = '%{text}<extra></extra>'
    
    return fig