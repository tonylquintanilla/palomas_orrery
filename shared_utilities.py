"""
shared_utilities.py - Common utility functions shared between multiple modules
"""

import numpy as np
import math
import plotly.graph_objs as go

def create_sun_direction_indicator(center_position=(0, 0, 0), axis_range=None, shell_radius=None, 
                              object_type=None, center_object=None):
    """
    Creates a visual indicator showing the direction to the Sun (along negative X-axis).
    Scale automatically adjusts based on the plot's axis range or provided shell radius.
    Conditionally shows the indicator based on the object type and center object.
    
    Parameters:
        center_position (tuple): (x, y, z) position of the body's center
        axis_range (list): The axis range [min, max] used in the plot
        shell_radius (float): Radius of the shell being displayed, to scale indicator appropriately
        object_type (str): Type of object being visualized ('Sun' or a planet name)
        center_object (str): Name of the object at the center of the plot
    """
    # Check conditions for showing the sun direction indicator
    # Case 1: If this is a Sun shell, don't show indicator (Sun doesn't need direction to itself)
    if object_type == 'Sun':
        print(f"Sun direction indicator: Not showing for Sun shells")
        return []
        
    # Case 2: For planet shells, only show when that planet is the center object
    if object_type is not None and center_object is not None and object_type != center_object:
        print(f"Sun direction indicator: Not showing for {object_type} shells when {center_object} is at center")
        return []
    
    # Case 3: When center_object is 'Sun' and this is a planet shell, don't show the indicator
    if center_object == 'Sun' and object_type is not None and object_type != 'Sun':
        print(f"Sun direction indicator: Not showing planetary shell indicators when Sun is the center object")
        return []

    center_x, center_y, center_z = center_position
    
    # First priority: Use shell_radius if provided
    if shell_radius is not None and isinstance(shell_radius, (int, float)) and shell_radius > 0:
        # Use a fraction of the shell radius for the indicator length
        plot_scale = shell_radius * 1.15  # 110% of shell radius
        print(f"Sun direction indicator: Using shell radius {shell_radius}, scale = {plot_scale:.5f} AU")
    else:
        # Second priority: Try to extract plot scale from axis_range
        try:
            if axis_range is not None and isinstance(axis_range, (list, tuple)) and len(axis_range) >= 2:
                # Extract min and max values and ensure they're floats
                min_val = float(axis_range[0])
                max_val = float(axis_range[1])
                
                # Calculate total scale range and distance to negative X boundary
                scale_range = abs(max_val - min_val)
                distance_to_neg_x = abs(center_x - min_val)
                
                # Use 10% of total range as the scale
                plot_scale = scale_range * 0.1
                print(f"Sun direction indicator: Using 10% of range, scale = {plot_scale:.5f} AU")
            
            # If axis_range is invalid, use fallback scale based on plot size
            else:
                # Determine appropriate scale based on plot content
                if center_position != (0, 0, 0):
                    # For non-center objects, use 1/20th of the distance from origin
                    pos_distance = np.sqrt(center_x**2 + center_y**2 + center_z**2)
                    plot_scale = pos_distance / 20.0
                    print(f"Sun direction indicator: Using 1/20 of position distance, scale = {plot_scale:.5f} AU")
                else:
                    # For center objects, use a reasonable default based on URL or filename
                    import os
                    filename = os.path.basename(os.path.abspath(__file__))
                    
                    # Default scale based on common planet scales
                    if "mercury" in filename.lower() or "0.02" in str(globals()):
                        plot_scale = 0.01  # Mercury hill sphere
                    elif "jupiter" in filename.lower() or "0.5" in str(globals()):
                        plot_scale = 0.05  # Jupiter hill sphere
                    elif "saturn" in filename.lower():
                        plot_scale = 0.1   # Saturn
                    elif "neptune" in filename.lower() or "uranus" in filename.lower():
                        plot_scale = 0.5   # Outer planets
                    else:
                        # General fallback - use a reasonable value that works for most plots
                        plot_scale = 0.05
                    
                    print(f"Sun direction indicator: Using content-based default, scale = {plot_scale:.5f} AU")
        except Exception as e:
            # Last resort fallback
            print(f"Sun direction indicator: Error calculating scale: {e}")
            plot_scale = 0.05
    
    # Ensure minimum indicator size for visibility
    min_scale = 0.001  # 0.001 AU minimum size for visibility
    if plot_scale < min_scale:
        plot_scale = min_scale
        print(f"Sun direction indicator: Adjusted to minimum scale = {plot_scale:.5f} AU")
    
    # Create a line pointing in the POSITIVE X direction (toward vernal equinox)
    # +X points toward the vernal equinox ([ARIES]) - the direction from Earth to Sun on March 20
    sun_direction_x = [center_x, center_x + plot_scale]  # Line points in +X direction
    sun_direction_y = [center_y, center_y]
    sun_direction_z = [center_z, center_z]

    # Format the scale value for display - use scientific notation for very large values
    if plot_scale >= 1000:
        scale_text = f"{plot_scale:.2e} AU"
    else:
        # Show more decimal places for smaller values
        decimal_places = 5 if plot_scale < 0.1 else 2
        scale_text = f"{plot_scale:.{decimal_places}f} AU"

    # Info text for the hover
    info_text = "Vernal Equinox Direction (+X): Points toward the First Point of Aries ([ARIES]).<br>" \
                "This is the direction from Earth to the Sun at the vernal equinox (around March 20).<br>" \
                "The +X axis defines celestial longitude 0 deg in the J2000 ecliptic coordinate system.<br>" \
                f"Current indicator length: {scale_text}"

    # Create the vernal equinox direction indicator line
    indicator_trace = go.Scatter3d(
        x=sun_direction_x,
        y=sun_direction_y,
        z=sun_direction_z,
        mode='lines',
        line=dict(
            color='yellow',
            width=3,
            dash='dash'
        ),

        name='Vernal Equinox Direction (+X)',
        text=[info_text] * len(sun_direction_x),  # Add hover text
        hovertemplate='%{text}<extra></extra>',    # Enable hover with template
        showlegend=True
    )

    return [indicator_trace]

