"""visualization_utils.py - Shared utilities for visualization functions."""

import plotly.graph_objects as go

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
            ),
            dict(
                label="Object Names Only",
                method="update",
                args=[{"hovertemplate": '%{customdata}<extra></extra>'}]
            ),
        ],
        font=dict(color='blue'),
        bgcolor='rgba(255,255,255,0.50)',
        bordercolor='white',
        borderwidth=1
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