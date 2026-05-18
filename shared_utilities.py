"""
shared_utilities.py - Small shared helpers used across shell visualization modules.

Contains create_sun_direction_indicator(), which adds a visual arrow pointing
from a body's position toward the Sun. The coordinate text box in the orrery
plot handles reference frame education (+X = vernal equinox, etc.), freeing
this indicator to serve its original purpose: showing where the Sun is.

When the body is at origin (body-centered view), the indicator is suppressed -
the Sun is visible in the plot and there is no single sunward direction from
the coordinate center.

Module updated: May 2026 with Anthropic's Claude Opus 4.7
"""

import numpy as np
import math
import plotly.graph_objs as go

from orrery_rendering import create_info_marker


def create_sun_direction_indicator(center_position=(0, 0, 0), axis_range=None, shell_radius=None, 
                              object_type=None, center_object=None):
    """
    Creates a visual indicator arrow pointing from the body toward the Sun.

    The arrow points from center_position toward the origin (where the Sun is
    in heliocentric plots). When center_position is at or near the origin
    (body-centered views), the indicator is suppressed - the Sun is visible
    in the plot and the coordinate text box provides reference frame context.

    Parameters:
        center_position (tuple): (x, y, z) position of the body's center
        axis_range (list): The axis range [min, max] used in the plot (fallback scaling)
        shell_radius (float): Radius of the outermost active shell, for scaling
        object_type (str): Type of object being visualized (for suppression logic)
        center_object (str): Name of the object at the center of the plot
    """
    center_x, center_y, center_z = center_position
    dist = math.sqrt(center_x**2 + center_y**2 + center_z**2)

    # Suppress when at or very near origin - no meaningful sunward direction.
    # The Sun is visible in the plot; the coordinate text box provides orientation.
    if dist < 1e-10:
        print("Sun direction indicator: Suppressed at origin (body-centered view)")
        return []

    # Suppress for Sun shells (Sun doesn't need direction to itself)
    if object_type == 'Sun':
        print("Sun direction indicator: Not showing for Sun shells")
        return []

    # Compute sunward direction (toward origin from center_position)
    sun_dir_x = -center_x / dist
    sun_dir_y = -center_y / dist
    sun_dir_z = -center_z / dist
    
    # Scale the indicator arrow
    if shell_radius is not None and isinstance(shell_radius, (int, float)) and shell_radius > 0:
        plot_scale = shell_radius * 1.15  # 115% of shell radius
        print(f"Sun direction indicator: Using shell radius {shell_radius}, scale = {plot_scale:.5f} AU")
    else:
        try:
            if axis_range is not None and isinstance(axis_range, (list, tuple)) and len(axis_range) >= 2:
                min_val = float(axis_range[0])
                max_val = float(axis_range[1])
                scale_range = abs(max_val - min_val)
                plot_scale = scale_range * 0.1
                print(f"Sun direction indicator: Using 10% of range, scale = {plot_scale:.5f} AU")
            else:
                # Use 1/20th of distance from origin as fallback
                plot_scale = dist / 20.0
                print(f"Sun direction indicator: Using 1/20 of position distance, scale = {plot_scale:.5f} AU")
        except Exception as e:
            print(f"Sun direction indicator: Error calculating scale: {e}")
            plot_scale = 0.05
    
    # Minimum size for visibility
    min_scale = 0.001
    if plot_scale < min_scale:
        plot_scale = min_scale
        print(f"Sun direction indicator: Adjusted to minimum scale = {plot_scale:.5f} AU")
    
    # Arrow from body center toward Sun
    tip_x = center_x + plot_scale * sun_dir_x
    tip_y = center_y + plot_scale * sun_dir_y
    tip_z = center_z + plot_scale * sun_dir_z

    # Format scale for hover text
    if plot_scale >= 1000:
        scale_text = f"{plot_scale:.2e} AU"
    else:
        decimal_places = 5 if plot_scale < 0.1 else 2
        scale_text = f"{plot_scale:.{decimal_places}f} AU"

    info_text = (
        "Sun Direction: Arrow points from this body toward the Sun.<br>"
        "The Sun is at the origin of the heliocentric coordinate system.<br>"
        f"Distance to Sun: {dist:.4f} AU<br>"
        f"Indicator length: {scale_text}"
    )

    legend_name = 'Sun Direction'

    # Dashed yellow line from center toward Sun
    indicator_trace = go.Scatter3d(
        x=[center_x, tip_x],
        y=[center_y, tip_y],
        z=[center_z, tip_z],
        mode='lines',
        line=dict(color='yellow', width=3, dash='dash'),
        name=legend_name,
        legendgroup=legend_name,
        hoverinfo='skip',
        showlegend=True
    )

    # Info marker at the tip
    info_trace = create_info_marker(
        tip_x, tip_y, tip_z,
        'yellow', info_text, legend_name
    )

    return [indicator_trace, info_trace]


# Backward compatibility alias - shell modules still import by the old name
# during migration. Points to the same function.
create_vernal_equinox_indicator = create_sun_direction_indicator
