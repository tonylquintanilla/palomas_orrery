"""visualization_utils.py - Shared utilities for visualization functions."""

import plotly.graph_objects as go
import numpy as np
from formatting_utils import format_maybe_float, format_km_float
from idealized_orbits import planetary_params
from celestial_coordinates import calculate_radec_for_position, format_radec_hover_component

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

def add_camera_center_button(fig, center_object_name='Sun'):
    """
    Add a button to move the camera to the center object.
    
    Places the camera AT the center object (like standing on it) looking outward,
    rather than looking AT the center from outside.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add buttons to
        center_object_name (str): Name of the center object (default: 'Sun')
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with camera center button
    """
    # Get existing updatemenus and convert to list
    existing_menus = list(fig.layout.updatemenus) if hasattr(fig.layout, 'updatemenus') and fig.layout.updatemenus is not None else []
    
    # Capture the CURRENT axis ranges from the figure to preserve them
    try:
        if hasattr(fig.layout, 'scene') and hasattr(fig.layout.scene, 'xaxis'):
            x_range = list(fig.layout.scene.xaxis.range)
            y_range = list(fig.layout.scene.yaxis.range)
            z_range = list(fig.layout.scene.zaxis.range)
            has_ranges = True
            print(f"[Camera Button] Preserving axis ranges: X={x_range}, Y={y_range}, Z={z_range}")
        else:
            has_ranges = False
            print(f"[Camera Button] Warning: Could not read axis ranges")
    except:
        has_ranges = False
        print(f"[Camera Button] Warning: Error reading axis ranges")
    
    # Build button args with camera AT the center looking along +X axis
    # Eye at origin (the center object), looking along +X axis
    # This puts you "at" the center object looking outward
    button_args = {
        "scene.camera": {
            "eye": {"x": 0.001, "y": 0, "z": 0},  # AT the center (tiny offset to avoid singularity)
            "center": {"x": 1, "y": 0, "z": 0},   # Looking along +X axis (toward RA=0deg)
            "up": {"x": 0, "y": 0, "z": 1}        # Z-axis is up
        }
    }
    
    # Add axis ranges if we successfully captured them
    if has_ranges:
        button_args["scene.xaxis.range"] = x_range
        button_args["scene.yaxis.range"] = y_range
        button_args["scene.zaxis.range"] = z_range
    
    # Create camera center button
    camera_button = dict(
        type="buttons",
        direction="left",
        x=0.05,
        y=1.0,
        buttons=[dict(
    #        label=f"Move Camera to {center_object_name} (Center) along the +X axis (Aries)",
            label=f"Center (Aries)",
            method="relayout",
            args=[button_args]
        )],
        bgcolor='rgba(255,255,255,0.50)',
        font=dict(color='blue'),
        bordercolor='white',
        borderwidth=1
    )
    
    # Add to existing menus
    existing_menus.append(camera_button)
    
    # Update figure layout
    fig.update_layout(updatemenus=existing_menus)
    
    return fig

def add_look_at_object_buttons(fig, positions, center_object_name='Sun', target_objects=None):
    """
    Add buttons to point camera from center toward specific target objects.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add buttons to
        positions (dict): Dictionary mapping object names to their position data
                         Each position should have 'x', 'y', 'z' keys
        center_object_name (str): Name of the center object (default: 'Sun')
        target_objects (list): List of object names to create buttons for
                              If None, creates buttons for all major planets
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with look-at buttons
    """
    # Get existing updatemenus and convert to list
    existing_menus = list(fig.layout.updatemenus) if hasattr(fig.layout, 'updatemenus') and fig.layout.updatemenus is not None else []
    
    # Capture the CURRENT axis ranges from the figure to preserve them
    try:
        if hasattr(fig.layout, 'scene') and hasattr(fig.layout.scene, 'xaxis'):
            x_range = list(fig.layout.scene.xaxis.range)
            y_range = list(fig.layout.scene.yaxis.range)
            z_range = list(fig.layout.scene.zaxis.range)
            has_ranges = True
        else:
            has_ranges = False
    except:
        has_ranges = False
    
    # Default target objects if none specified (major planets + some interesting objects)
    if target_objects is None:
#        target_objects = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 
#                         'Saturn', 'Uranus', 'Neptune', 'Pluto']
    # AFTER (auto-detect all objects):
        target_objects = [name for name in positions.keys() if name != center_object_name]
        print(f"[Camera Buttons] Auto-detected {len(target_objects)} target objects from positions")        

    
    # Get center position (default to origin if not in positions)
    center_pos = [0, 0, 0]
    if center_object_name in positions and positions[center_object_name] is not None:
        center_data = positions[center_object_name]
        if isinstance(center_data, dict) and 'x' in center_data:
            center_pos = [center_data['x'], center_data['y'], center_data['z']]
    
    # Create list of buttons
    buttons = []
    
    # First button: Look along +X axis (original behavior)
    button_args_x = {
        "scene.camera": {
            "eye": {"x": 0.001, "y": 0, "z": 0},
            "center": {"x": 1, "y": 0, "z": 0},
            "up": {"x": 0, "y": 0, "z": 1}
        }
    }
    if has_ranges:
        button_args_x["scene.xaxis.range"] = x_range
        button_args_x["scene.yaxis.range"] = y_range
        button_args_x["scene.zaxis.range"] = z_range
    
    buttons.append(dict(
        label=f"View +X axis (Aries) from {center_object_name}",
        method="relayout",
        args=[button_args_x]
    ))
    
    # Add buttons for each target object
    for target_name in target_objects:
        if target_name not in positions or positions[target_name] is None:
            continue
            
        target_data = positions[target_name]
        if not isinstance(target_data, dict) or 'x' not in target_data:
            continue
        
        target_pos = [target_data['x'], target_data['y'], target_data['z']]
        
        # Calculate direction vector from center to target
        direction = np.array(target_pos) - np.array(center_pos)
        distance = np.linalg.norm(direction)
        
        if distance < 1e-10:  # Too close, skip
            continue
        
        # Normalize the direction
        direction_norm = direction / distance
        
        # Place camera at center, looking toward target
        # Use a small offset to avoid singularity at origin
        camera_offset = 0.001
        
        # Camera position
        eye_pos = {
            'x': center_pos[0] + direction_norm[0] * camera_offset,
            'y': center_pos[1] + direction_norm[1] * camera_offset,
            'z': center_pos[2] + direction_norm[2] * camera_offset
        }
        
        # Look at the target position
        center_look = {
            'x': target_pos[0],
            'y': target_pos[1],
            'z': target_pos[2]
        }
        
        button_args = {
            "scene.camera": {
                "eye": eye_pos,
                "center": center_look,
                "up": {"x": 0, "y": 0, "z": 1}
            }
        }
        
        if has_ranges:
            button_args["scene.xaxis.range"] = x_range
            button_args["scene.yaxis.range"] = y_range
            button_args["scene.zaxis.range"] = z_range
        
        buttons.append(dict(
            label=f"View {target_name} from {center_object_name}",
            method="relayout",
            args=[button_args]
        ))
    
    # Create dropdown menu with all buttons
    if buttons:
        camera_dropdown = dict(
            type="dropdown",
            direction="down",
            x=0.02,
            y=1.0,
            xanchor="left",
            yanchor="top",
            buttons=buttons,
            bgcolor='rgba(255,255,255,0.70)',
            font=dict(color='blue'),
            bordercolor='white',
            borderwidth=1,
            pad=dict(t=0, b=0)
        )
        
        # Add to existing menus
        existing_menus.append(camera_dropdown)
        
        # Update figure layout
        fig.update_layout(updatemenus=existing_menus)
        
        # Add target marker annotation at screen center
        fig.add_annotation(
            dict(       # target marker 
                x=0.6,
                y=0.5085,
                text='<span style="vertical-align:1em;"><></span>',                
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(size=60, color='rgba(0, 255, 255, 0.5)')  # Semi-transparent cyan
            )
        )

        print(f"[Camera Buttons] Added dropdown with {len(buttons)} view options")
    
    return fig


def add_fly_to_object_buttons(fig, positions, center_object_name='Sun', target_objects=None, 
                               fly_distance=0.1, distance_scale_factor=0.05):
    """
    Add buttons to fly the camera TO specific target objects, keeping focus on the object.
    
    Unlike add_look_at_object_buttons (which views FROM center TOWARD target),
    this places the camera NEAR the target looking AT the target.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add buttons to
        positions (dict): Dictionary mapping object names to their position data
                         Each position should have 'x', 'y', 'z' keys
        center_object_name (str): Name of the center object (default: 'Sun')
        target_objects (list): List of object names to create buttons for
                              If None, creates buttons for all objects in positions
        fly_distance (float): Base distance from object for camera (AU), default 0.1
        distance_scale_factor (float): Scale factor for distance-based offset, default 0.05
                                       Camera distance = fly_distance + (object_distance * scale_factor)
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with fly-to buttons
    """
    # Get existing updatemenus and convert to list
    existing_menus = list(fig.layout.updatemenus) if hasattr(fig.layout, 'updatemenus') and fig.layout.updatemenus is not None else []
    
    # Default target objects if none specified
    if target_objects is None:
        target_objects = [name for name in positions.keys() if name != center_object_name]
        print(f"[Fly To Buttons] Auto-detected {len(target_objects)} target objects from positions")
    
    # Get center position (default to origin if not in positions)
    center_pos = np.array([0.0, 0.0, 0.0])
    if center_object_name in positions and positions[center_object_name] is not None:
        center_data = positions[center_object_name]
        if isinstance(center_data, dict) and 'x' in center_data:
            center_pos = np.array([center_data['x'], center_data['y'], center_data['z']])
    
    # Create list of buttons
    buttons = []
        
    # Capture original axis ranges for "Full View" button
    try:
        orig_x_range = list(fig.layout.scene.xaxis.range) if fig.layout.scene.xaxis.range else None
        orig_y_range = list(fig.layout.scene.yaxis.range) if fig.layout.scene.yaxis.range else None
        orig_z_range = list(fig.layout.scene.zaxis.range) if fig.layout.scene.zaxis.range else None
    except:
        orig_x_range = orig_y_range = orig_z_range = None
    
    # Add "Full View" button first if we have original ranges
    if orig_x_range and orig_y_range and orig_z_range:
        buttons.append(dict(
            label="Return to Full View",
            method="relayout",
            args=[{
                "scene.camera": {
                    "eye": {"x": 1.5, "y": 1.5, "z": 1.2},
                    "center": {"x": 0, "y": 0, "z": 0},
                    "up": {"x": 0, "y": 0, "z": 1}
                },
                "scene.xaxis.range": orig_x_range,
                "scene.yaxis.range": orig_y_range,
                "scene.zaxis.range": orig_z_range,
                "scene.aspectmode": "cube",
                "scene.aspectratio": {"x": 1, "y": 1, "z": 1}
            }]
        ))
    
    # Add buttons for each target object
    for target_name in target_objects:
        if target_name not in positions or positions[target_name] is None:
            continue
            
        target_data = positions[target_name]
        if not isinstance(target_data, dict) or 'x' not in target_data:
            continue
        
        target_pos = np.array([target_data['x'], target_data['y'], target_data['z']])
        
        # Calculate direction vector from target to center (camera will be on this side)
        direction_to_center = center_pos - target_pos
        distance_from_center = np.linalg.norm(direction_to_center)
        
        if distance_from_center < 1e-10:  # Target is at center, skip
            continue
        
        # Normalize the direction
        direction_norm = direction_to_center / distance_from_center
        
        # Calculate camera offset distance (closer for nearby objects, slightly further for distant)
        view_radius = fly_distance + (distance_from_center * distance_scale_factor)

        # Zoom axis ranges to target area
        new_x_range = [float(target_pos[0]) - view_radius, float(target_pos[0]) + view_radius]
        new_y_range = [float(target_pos[1]) - view_radius, float(target_pos[1]) + view_radius]
        new_z_range = [float(target_pos[2]) - view_radius, float(target_pos[2]) + view_radius]
        
        button_args = {
            "scene.camera": {
                "eye": {"x": 1.5, "y": 1.5, "z": 1.2},
                "center": {"x": 0, "y": 0, "z": 0},
                "up": {"x": 0, "y": 0, "z": 1}
            },
            "scene.xaxis.range": new_x_range,
            "scene.yaxis.range": new_y_range,
            "scene.zaxis.range": new_z_range,
            "scene.aspectmode": "cube",
            "scene.aspectratio": {"x": 1, "y": 1, "z": 1}            
        }
        
        # Format distance for label
        if distance_from_center < 0.01:
            dist_str = f"{distance_from_center*149597870.7:.0f} km"  # Convert AU to km
        elif distance_from_center < 1:
            dist_str = f"{distance_from_center:.3f} AU"
        else:
            dist_str = f"{distance_from_center:.2f} AU"
        
        buttons.append(dict(
            label=f"Fly to {target_name} ({dist_str})",
            method="relayout",
            args=[button_args]
        ))
    
    # Sort buttons by distance for easier navigation
    def extract_distance(button):
        label = button['label']
        if "Full View" in label:
            return -1  # Keep Full View first
        try:
            # Extract the part in parentheses
            dist_part = label.split('(')[1].split(')')[0]
            if 'km' in dist_part:
                return float(dist_part.replace(' km', '').replace(',', '')) / 149597870.7
            else:
                return float(dist_part.replace(' AU', ''))
        except:
            return float('inf')
    
    buttons.sort(key=extract_distance)
    
    # Create dropdown menu with all buttons
    if buttons:
        fly_to_dropdown = dict(
            type="dropdown",
            direction="down",
            x=0.02,
            y=0.92,  # Position below the "View from" dropdown
            xanchor="left",
            yanchor="top",
            buttons=buttons,
            bgcolor='rgba(255,255,200,0.85)',  # Slightly yellow to distinguish from View dropdown
            font=dict(color='darkgreen'),
            bordercolor='green',
            borderwidth=1,
            pad=dict(t=0, b=0)
        )
        
        # Add to existing menus
        existing_menus.append(fly_to_dropdown)
        
        # Update figure layout
        fig.update_layout(updatemenus=existing_menus)
        
        print(f"[Fly To Buttons] Added dropdown with {len(buttons)} fly-to options")
    
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

def format_detailed_hover_text(obj_data, obj_name, center_object_name, objects, planetary_params, parent_planets, CENTER_BODY_RADII, 
                               KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS):
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
    
    # Calculate velocity in km/hr and km/sec
    velocity_km_hr = "N/A"
    velocity_km_sec = "N/A"
    if isinstance(obj_data.get('velocity'), (int, float)):
        vel_km_hr_val = obj_data.get('velocity') * KM_PER_AU / 24
        vel_km_sec_val = vel_km_hr_val / 3600
        velocity_km_hr = f"{vel_km_hr_val:,.2f}"
        velocity_km_sec = f"{vel_km_sec_val:.3f}"
    
    # Calculate surface distance if we have valid distance data
    center_radius_km = CENTER_BODY_RADII.get(center_object_name, 0)  # Default to 0 if center body not found
    surface_distance_str = "N/A"
    
#    if isinstance(distance_from_origin * KM_PER_AU, (int, float)) and (distance_from_origin * KM_PER_AU) > center_radius_km:
    if isinstance(distance_from_origin * KM_PER_AU, (int, float)):
        surface_distance_km = (distance_from_origin * KM_PER_AU) - center_radius_km
        surface_distance_str = format_km_float(surface_distance_km)

    # Add an explanatory note for negative values
    if surface_distance_km < 0:
        surface_distance_str += " (below mean datum)"       # This applies to the Mars Rover that is sitting below the datum.
    
    # Check if this is a planetary satellite
    is_satellite = False
    planet = None
    for p, satellites in parent_planets.items():
        if obj_name in satellites:
            is_satellite = True
            planet = p
            break
    
    # Get orbital period information
#    calculated_period = "N/A"
    known_period = "N/A"
    
    # Calculate orbital period for non-satellites
#    if not is_satellite and obj_name in planetary_params:
#        a = planetary_params[obj_name]['a']  # Semi-major axis in AU
            
#       if a > 0:
#            orbital_period_years = np.sqrt(a ** 3)
#            calculated_period = {
#                'years': orbital_period_years,
#                'days': orbital_period_years * 365.25
#            }  # OK: Correct indentation - closes the dict properly

    
    # Format calculated period
#    if isinstance(calculated_period, dict):
#        calc_years = calculated_period.get('years')
#        calc_days = calculated_period.get('days')
#        calculated_period_str = f"{calc_years:.4f} Earth years ({calc_days:.2f} days)"
#    else:
#        calculated_period_str = str(calculated_period)
    
    # Get known orbital period if available
#    if obj_name in KNOWN_ORBITAL_PERIODS:
#        known_value = KNOWN_ORBITAL_PERIODS[obj_name]
        
#        if known_value is None:
            # Handle hyperbolic/parabolic objects
#            known_period = "N/A (hyperbolic/parabolic orbit)"
#        else:
#            known_period = {
#                'days': known_value,
#                'years': known_value / 365.25
#            }
    
    # Get known orbital period if available
    # Context-aware: Pluto uses barycentric period (6.387 days) when centered on Pluto-Charon Barycenter
    if obj_name == 'Pluto' and center_object_name == 'Pluto-Charon Barycenter':
        # Pluto orbits the barycenter with the same period as Charon (6.387 days)
        known_value = 6.387  # Binary orbital period, same as Charon
        known_period = {
            'days': known_value,
            'years': known_value / 365.25
        }
    elif obj_name in KNOWN_ORBITAL_PERIODS:
        known_value = KNOWN_ORBITAL_PERIODS[obj_name]
        
        if known_value is None:
            # Handle hyperbolic/parabolic objects
            known_period = "N/A (hyperbolic/parabolic orbit)"
        else:
            known_period = {
                'days': known_value,
                'years': known_value / 365.25
            }

    # Format known period
    if isinstance(known_period, dict):
        known_years = known_period.get('years')
        known_days = known_period.get('days')
        known_period_str = f"{known_years:.4f} Earth years ({known_days:.2f} days)"
    else:
        known_period_str = str(known_period)
    
    # Find the object's info in the objects list
    obj_info = next((o for o in objects if o['name'] == obj_name), None)
    mission_info = obj_info.get('mission_info', '') if obj_info else ''
    
    # ===== NEW: Calculate RA/Dec for full hover text =====
    radec_component = format_radec_hover_component(obj_data, obj_name, compact=False)    
        
    # Now build the hover text
    if radec_component:
            # If we have RA/Dec, include it
        full_hover_text = (
            f"<b>{obj_name}</b><br>"  # <- Note: Changed from "<br><br>" to "<br>"
            f"{radec_component}<br><br>"  # <- NEW LINE: RA/Dec info
            f"Distance from Center: {distance_au} AU<br>"
            f"Distance: {distance_km} kilometers<br>"
            f"Distance: {distance_lm} light-minutes<br>"
            f"Distance: {distance_lh} light-hours<br>"
            f"Distance to Center Surface: {surface_distance_str} kilometers<br>"
            f"Velocity: {velocity_au} AU/day<br>"
            f"Velocity: {velocity_km_hr} km/hr ({velocity_km_sec} km/sec)<br>"
        )
    
    else:
        # If no RA/Dec available, keep original format
        full_hover_text = (
            f"<b>{obj_name}</b><br><br>"
            f"Distance from Center: {distance_au} AU<br>"
            f"Distance: {distance_km} kilometers<br>"
            f"Distance: {distance_lm} light-minutes<br>"
            f"Distance to Center Surface: {surface_distance_str} kilometers<br>"
            f"Velocity: {velocity_au} AU/day<br>"
            f"Velocity: {velocity_km_hr} km/hr ({velocity_km_sec} km/sec)<br>"
        )
    
    # Add orbital period information (known period only)
    full_hover_text += f"Known Orbital Period: {known_period_str}"
    
    # Add derivation note for Orcus when derived from Vanth
    if obj_data.get('derived_from_vanth'):
        full_hover_text += (
            f"<br><br><b>Position: Derived from Vanth</b><br>"
            f"JPL cannot query Orcus (920090482) at barycenter.<br>"
            f"Derived: Orcus pos = -Vanth pos x 0.16 (mass ratio)<br>"
            f"Data: JPL Horizons ID 120090482"
        )

    # Add mission_info if it exists
    if mission_info:
        full_hover_text += f"<br>{mission_info}"
    
    # Determine if this is a satellite of the center object specifically
    satellite_note = ""
    if is_satellite and planet == center_object_name:
        satellite_note = f"<br>Moon of {center_object_name}"
    

    # ===== NEW: Calculate RA/Dec for minimal hover text =====
    radec_compact = format_radec_hover_component(obj_data, obj_name, compact=True)

    minimal_hover_text = f"<b>{obj_name}</b>"
    if radec_compact:
        minimal_hover_text += f"<br>{radec_compact}"  # <- NEW LINE   
    
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
