import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt
from constants_new import KNOWN_ORBITAL_PERIODS, color_map
from shutdown_handler import show_figure_safely # Add this line
from apsidal_markers import add_perihelion_marker, add_apohelion_marker, calculate_apsidal_dates
from idealized_orbits import planetary_params, parent_planets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Ellipse, Arc
import matplotlib.patches as mpatches

class CreateToolTip(object):
    """
    Create a tooltip for a given widget with intelligent positioning to prevent clipping.
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milliseconds
        self.wraplength = 1000   # Reduced wraplength
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        try:
            # Get screen dimensions and taskbar height (estimated)
            screen_width = self.widget.winfo_screenwidth()
            screen_height = self.widget.winfo_screenheight()
            taskbar_height = 40  # Estimated Windows taskbar height

            # Create the tooltip window
            self.tw = tk.Toplevel(self.widget)
            self.tw.wm_overrideredirect(True)
            
            # Calculate usable screen height
            usable_height = screen_height - taskbar_height

            # Create the tooltip label
            label = tk.Label(
                self.tw,
                text=self.text,
                justify='left',
                background='yellow',
                relief='solid',
                borderwidth=1,
                wraplength=min(self.wraplength, screen_width - 100),
                font=("Arial", 10, "normal")
            )
            label.pack(ipadx=1, ipady=1)

            # Update the window to calculate its size
            self.tw.update_idletasks()
            tooltip_width = self.tw.winfo_width()
            tooltip_height = self.tw.winfo_height()

            # Initial x position - try positioning to the right of the widget first
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5

            # If tooltip would extend beyond right edge, try positioning to the left of the widget
            if x + tooltip_width > screen_width:
                x = self.widget.winfo_rootx() - tooltip_width - 5

            # If that would push it off the left edge, position at left screen edge with padding
            if x < 0:
                x = 5

            # Calculate vertical position
            y = self.widget.winfo_rooty()

            # If tooltip is taller than available space, position at top of screen
            if tooltip_height > usable_height:
                y = 5  # Small padding from top
            else:
                # Center vertically relative to widget if space allows
                widget_center = y + (self.widget.winfo_height() / 2)
                y = widget_center - (tooltip_height / 2)
                
                # Ensure tooltip doesn't go below usable screen area
                if y + tooltip_height > usable_height:
                    y = usable_height - tooltip_height - 5

                # Ensure tooltip doesn't go above top of screen
                if y < 5:
                    y = 5

            # Position the tooltip
            self.tw.wm_geometry(f"+{int(x)}+{int(y)}")

        except Exception as e:
            print(f"Error showing tooltip: {e}")
            import traceback
            traceback.print_exc()

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None

def rotation_matrix_x(angle):
    """Create rotation matrix around X axis"""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[1, 0, 0],
                     [0, c, -s],
                     [0, s, c]])

def rotation_matrix_z(angle):
    """Create rotation matrix around Z axis"""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])

def add_coordinate_frame(fig, name, color, R_transform, axis_length, 
                        show_labels=True, opacity=0.8, line_width=4,
                        show_in_legend=True, visible=True):
    """
    Add a 3D coordinate frame with the given transformation.
    
    Parameters:
        fig: Plotly figure
        name: Name of the frame (e.g., 'Perifocal', 'After ω')
        color: Color for the axes
        R_transform: 3x3 rotation matrix
        axis_length: Length of the axes
        show_labels: Whether to show axis labels
        opacity: Opacity of the axes
        line_width: Width of axis lines
        show_in_legend: Whether to show in legend
        visible: Whether frame is initially visible
    """
    # Base axes vectors
    axes = {
        'X': np.array([axis_length, 0, 0]),
        'Y': np.array([0, axis_length, 0]),
        'Z': np.array([0, 0, axis_length])
    }
    
    # For legend grouping
    legendgroup = f'frame_{name.replace(" ", "_")}'
    
    for i, (axis_name, axis_vec) in enumerate(axes.items()):
        # Transform the axis
        transformed = R_transform @ axis_vec
        
        # Add axis line
        fig.add_trace(go.Scatter3d(
            x=[0, transformed[0]],
            y=[0, transformed[1]], 
            z=[0, transformed[2]],
            mode='lines+text',
            line=dict(color=color, width=line_width),
            text=['', f'{axis_name}' if show_labels else ''],
            textposition='top center',
            textfont=dict(size=14, color=color),
            opacity=opacity,
    #        name=f'{name} axes' if i == 0 else '',  # Only show once in legend
            name=name if i == 0 else '',  # use the name directly            
            legendgroup=legendgroup,
            showlegend=(i == 0 and show_in_legend),
            visible=visible,
            hovertemplate=f'<b>{name} Frame</b><br>{axis_name}-axis'
        ))
        
        # Add arrow head using a small marker
        fig.add_trace(go.Scatter3d(
            x=[transformed[0] * 1.05],  # Slightly beyond the line end
            y=[transformed[1] * 1.05],
            z=[transformed[2] * 1.05],
            mode='markers',
            marker=dict(
                symbol='diamond',
                size=4,
                color=color
            ),
            opacity=opacity,
            showlegend=False,
            legendgroup=legendgroup,
            visible=visible,
            hoverinfo='skip'
        ))

def add_angle_arc(fig, angle_rad, radius, axis, color, label, start_angle=0,
                  show_in_legend=True, legendgroup=None):
    """Add an arc showing a rotation angle"""
    angle_points = 30
    angles = np.linspace(start_angle, start_angle + angle_rad, angle_points)
    
    if axis == 'z':
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        z = np.zeros_like(angles)
    elif axis == 'x':
        x = np.zeros_like(angles)
        y = radius * np.cos(angles)
        z = radius * np.sin(angles)
    
    # Add the arc
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines+text',
        line=dict(color=color, width=3),
        text=[''] * (angle_points-1) + [label],
        textposition='top center',
        name=label,
        legendgroup=legendgroup,
        showlegend=show_in_legend,
        visible=True,
        hovertemplate=f'<b>{label}</b>'
    ))

def create_orbital_transformation_viz(fig, obj_name, planetary_params, 
                                    show_steps=True, show_axes=True, 
                                    plot_date=None,
                                    center_object='Sun', parent_planets=None,
                                    show_apsidal_markers=True,
                                    current_position=None):                                    
                            
    """
    Create a visualization showing how orbital parameters transform to 3D orbit.
    This version clearly shows the coordinate system transformations.
    
    Parameters:
        fig: Plotly figure object (for compatibility, though we create a new one)
        obj_name: Name of the object
        planetary_params: Dictionary of orbital parameters
        show_steps: Whether to show intermediate transformation steps
        show_axes: Whether to show coordinate axes
        plot_date: Date for the visualization (defaults to current date)
        center_object: Name of the central body (defaults to 'Sun')
        parent_planets: Dictionary mapping planets to their satellites
    """
    
    if obj_name not in planetary_params:
        print(f"No orbital parameters found for {obj_name}")
        return fig
    
    params = planetary_params[obj_name]
    
    # Add period if missing but object is known in KNOWN_ORBITAL_PERIODS
    if 'period' not in params and obj_name in KNOWN_ORBITAL_PERIODS:
        period_value = KNOWN_ORBITAL_PERIODS[obj_name]
        if period_value is not None:  # Some objects might have None (hyperbolic)
            params['period'] = period_value
            print(f"Added known period for {obj_name}: {params['period']:.1f} days")

    
    # Extract orbital elements
    a = params.get('a', 1.0)  # Semi-major axis
    e = params.get('e', 0.0)  # Eccentricity
    i = params.get('i', 0.0)  # Inclination (degrees)
    omega = params.get('omega', 0.0)  # Argument of periapsis (degrees)
    Omega = params.get('Omega', 0.0)  # Longitude of ascending node (degrees)
    
    # Convert to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)

    # Determine the central body
    center_object = 'Sun'  # Default
    if parent_planets:
        for planet, moons in parent_planets.items():
            if obj_name in moons:
                center_object = planet
                break    
    
    # Calculate periapsis and apoapsis distances
    r_peri = a * (1 - e)
    r_apo = a * (1 + e) if e < 1 else None
    
    # Set up the plot date
    if plot_date is None:
        plot_date = dt.datetime.now()
    
    # Clear the figure and start fresh
    fig.data = []
    fig.layout = {}
        
    # Add central body
    center_color = 'yellow' if center_object == 'Sun' else 'deepskyblue'
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers+text',
        marker=dict(size=20, color=center_color,
                    line=dict(color='orange', width=2)),
        text=[center_object],
        textposition='bottom center',
        name=center_object,
        showlegend=True,
        hovertemplate=f'<b>{center_object}</b><br>Central body'
    ))
    
    # Generate orbital points in perifocal frame
    if e < 1.0:
        # Elliptical orbit: Full 360 degrees
        true_anomaly = np.linspace(0, 2 * np.pi, 200)
    else:
        # Hyperbolic orbit: Limit the true anomaly to the valid range
        # Calculate the angle of the asymptotes where the orbit goes to infinity
        nu_max = np.arccos(-1 / e)
        # Generate points within this range, leaving a small buffer to avoid infinity
        true_anomaly = np.linspace(-nu_max * 0.95, nu_max * 0.95, 200)

    # Generate orbital points in perifocal frame
#    true_anomaly = np.linspace(0, 2*np.pi, 100)

    r = a * (1 - e**2) / (1 + e * np.cos(true_anomaly))
    
    # Perifocal coordinates
    x0 = r * np.cos(true_anomaly)
    y0 = r * np.sin(true_anomaly)
    z0 = np.zeros_like(true_anomaly)
    
    # Build transformation matrices
    R1 = rotation_matrix_z(omega_rad)
    R2 = rotation_matrix_x(i_rad)
    R3 = rotation_matrix_z(Omega_rad)
    
    # Cumulative transformations
#    R_after_omega = R1
#    R_after_inclination = R2 @ R1
#    R_final = R3 @ R2 @ R1

    # Cumulative transformations
    R_after_omega = R1
    R_after_inclination = R1 @ R2  # Corrected order for intrinsic "hinge" tilt
    R_final = R3 @ R_after_inclination # Apply final extrinsic swivel to the new result
    
    # For scaling, use periapsis for hyperbolas or semi-major axis for ellipses
#    if e < 1.0:
#        scale_basis = a  # Use semi-major axis for ellipses
#    else:
#        scale_basis = r_peri  # Use periapsis distance for hyperbolic orbits
    
    # Use absolute value of 'a' for scaling to handle hyperbolic orbits -- a is too small to see the orbit
#    scale_basis = abs(a)
    
    # Coordinate frame axis length - scale with a buffer
#    axis_length = scale_basis * 1.5     # 150% of semi-major axis for a good visual buffer

    # Coordinate frame axis length - scale with a buffer
#    axis_length = a * 1.5  # 150% of semi-major axis for a good visual buffer

    # Coordinate frame axis length - extend to at least semi-major axis
#    axis_length = max(a * 1.1, 0.5)  # At least 110% of semi-major axis

    # Calculate appropriate scale_basis for the visualization
    if e >= 0.99:  # Near-parabolic or hyperbolic orbit
        # For these orbits, use perihelion distance as reference
        if a < 0:  # Hyperbolic with negative semi-major axis
            q = abs(a) * (e - 1)  # Perihelion for hyperbolic
        else:
            q = a * (1 - e)  # Perihelion for near-parabolic
        
        # Special case for known comets
        if obj_name == 'C/2025_K1':
            q = 0.33  # Known perihelion
        
        # Use a reasonable multiple of perihelion for visualization scale
        scale_basis = max(3 * q, 1.0)  # At least 1 AU
        
        # Cap the scale for better visualization
        scale_basis = min(scale_basis, 5.0)  # Maximum 5 AU for near-parabolic
        
    else:  # Elliptical orbit
        # For elliptical orbits, use the semi-major axis
        scale_basis = abs(a)
        
        # Adjust for very small orbits (like satellites)
        if scale_basis < 0.1:
            scale_basis = 0.1

    # Calculate axis length for coordinate frames
    # Should be proportional to the orbit size but not too large
    axis_length = min(0.8 * scale_basis, 2.0)  # Cap at 2 AU for frames
    
    if show_axes:
        # 1. Ecliptic reference frame (gray, always visible)
        add_coordinate_frame(fig, "Ecliptic Ref. (+X: Vernal Equinox)", "gray", np.eye(3), 
                           axis_length * 1.2, opacity=0.4, line_width=2, visible=True)
        
        # 2. Perifocal frame (blue)
        add_coordinate_frame(fig, "1. Perifocal", "cyan", np.eye(3), 
                           axis_length, opacity=0.8, visible=True)
        
        # 3. After ω rotation (purple)
        if show_steps and omega != 0:
            add_coordinate_frame(fig, "2. After ω rotation", "purple", R_after_omega, 
                               axis_length, opacity=0.7, visible=True)
        
        # 4. After ω and i rotation (orange)
        if show_steps and i != 0:
            add_coordinate_frame(fig, "3. After i rotation", "orange", 
                               R_after_inclination, axis_length, 
                               opacity=0.7, visible=True)
        
        # 5. Final = Ecliptic Frame (red)
        add_coordinate_frame(fig, "4. After Ω rotation (Final)", "red", R_final, 
                           axis_length, opacity=0.8, visible=True)
    
    # Add orbits at each transformation stage
    # 1. Perifocal orbit
#    fig.add_trace(go.Scatter3d(
#        x=x0, y=y0, z=z0,
#        mode='lines',
#        line=dict(color='cyan', width=4),
#        name='1. Perifocal Frame',
    #    legendgroup='transformations',
#        showlegend=True,
#        visible=True,
#        hovertemplate='<b>Perifocal Orbit</b><br>The orbit in its natural, un-rotated frame.'
#    ))

    # Add orbits at each transformation stage
    # 1. Perifocal orbit
    # Create the equation string based on orbit type
    if e < 1.0:  # Elliptical orbit
        orbit_type = "Ellipse"
        equation = "r = a(1 - e²) / (1 + e·cos(ν))"
    elif e == 1.0:  # Parabolic orbit
        orbit_type = "Parabola"
        equation = "r = 2p / (1 + cos(ν))"
        p_value = a * (1 - e**2)  # semi-latus rectum
    else:  # Hyperbolic orbit
        orbit_type = "Hyperbola"
        equation = "r = a(1 - e²) / (1 + e·cos(ν))"
    
    fig.add_trace(go.Scatter3d(
        x=x0, y=y0, z=z0,
        mode='lines',
        line=dict(color='cyan', width=4),
        name='1. Perifocal Frame',
        showlegend=True,
        visible=True,
        hovertemplate=(
            f'<b>Perifocal Orbit ({orbit_type})</b><br>' +
            'The orbit in its natural, un-rotated frame.<br><br>' +
            '<b>Orbit Equation (Polar form):</b><br>' +
            f'{equation}<br><br>' +
            '<b>Where:</b><br>' +
            f'• r = radius from focus ({center_object})<br>' +
            f'• ν = true anomaly (angle from periapsis)<br>' +
            f'• a = {a:.3f} AU (semi-major axis)<br>' +
            f'• e = {e:.6f} (eccentricity)<br>' +
            (f'• p = {p_value:.3f} AU (semi-latus rectum)<br>' if e == 1.0 else '') +
            '<br><b>True anomaly (ν):</b><br>' +
            'The angle measured from periapsis to the<br>' +
            'current position along the orbit, in the<br>' +
            'direction of motion.<br>' +
            '<br><b>Eccentricity (e):</b><br>' +
            'A measure of how elongated the orbit is:<br>' +
            '• e = 0: perfect circle<br>' +
            '• 0 < e < 1: ellipse<br>' +
            '• e = 1: parabola<br>' +
            '• e > 1: hyperbola<br>' +
            '<br><b>Eccentricity from apsides:</b><br>' +
            (f'e = (r_apo - r_peri) / (r_apo + r_peri)<br>' +
             f'e = ({r_apo:.3f} - {r_peri:.3f}) / ({r_apo:.3f} + {r_peri:.3f})<br>' +
             f'e = {e:.6f}' if e < 1.0 else 
             'e = (r_apo - r_peri) / (r_apo + r_peri)<br>' +
             '(Not applicable for parabolic/hyperbolic orbits)') +
            '<extra></extra>'
        )
    ))  
    
    # Add periapsis/apoapsis markers in perifocal
    fig.add_trace(go.Scatter3d(
        x=[r_peri], y=[0], z=[0],
        mode='markers+text',
        marker=dict(size=6, color='cyan', symbol='square-open'),
        text=['Periapsis'],
        textposition='bottom center',
        name='Periapsis (perifocal)',
#        legendgroup='apsides',
#        legendgrouptitle_text='Orbital Points',
        showlegend=True,
        visible=True,
        hovertemplate=f'<b>Periapsis</b><br>Distance: {r_peri:.3f} AU<br>Closest point to {center_object}'
    ))
    
    if e < 1.0:
        fig.add_trace(go.Scatter3d(
            x=[-r_apo], y=[0], z=[0],
            mode='markers+text',
            marker=dict(size=6, color='cyan', symbol='square-open'),
            text=['Apoapsis'],
            textposition='top center',
            name='Apoapsis (perifocal)',
#            legendgroup='apsides',
            showlegend=True,
            visible=True,
            hovertemplate=f'<b>Apoapsis</b><br>Distance: {r_apo:.3f} AU<br>Farthest point from {center_object} (a, semi-major axis)'
        ))

    # ========== INSERT THE NEW CODE HERE ==========
    # Add semi-major axis trace in perifocal frame
    if e < 1.0:  # Only for elliptical orbits
        # The semi-major axis is the distance from the center of the ellipse to either end
        # In the perifocal frame with focus at origin:
        # - Center of ellipse is at (-a*e, 0, 0)
        # - The semi-major axis extends from the center ±a along the major axis
        
        # Method 1: Show semi-major axis from focus to a reference point
        # This shows the actual semi-major axis length 'a'
        # We'll draw from the geometric center to one vertex to show 'a'
        ellipse_center_x = -a * e  # Center of ellipse in perifocal frame
        
        # Draw from focus (Sun) toward apoapsis direction, length = a
        fig.add_trace(go.Scatter3d(
            x=[0, -a],  # From Sun/focus toward apoapsis (negative x direction)
            y=[0, 0],
            z=[0, 0],
            mode='lines+markers+text',
            line=dict(color='cyan', width=3, dash='dashdot'),
            marker=dict(size=[4, 8], color='cyan', symbol=['circle-open', 'diamond-open']),  # Open markers
            text=['', f'a = {a:.3f} AU'],  # Label only at the end
            textposition=['bottom center', 'top center'],
            name='Semi-major axis (a)',
            showlegend=True,
            visible=True,
            hovertemplate=f'<b>Semi-major axis</b><br>a = {a:.3f} AU<br>' +
                          f'Mean distance of orbit from {center_object}<br>' +
                          f'Periapsis: {r_peri:.3f} AU<br>' +
                          f'Apoapsis: {r_apo:.3f} AU<br>' +
                          f'a = (r_peri + r_apo) / 2'
        ))
        
        # Optional: Add a subtle line showing the full major axis
        fig.add_trace(go.Scatter3d(
            x=[r_peri, -r_apo],  # Full major axis from periapsis to apoapsis
            y=[0, 0],
            z=[0, 0],
            mode='lines',
            line=dict(color='cyan', width=1, dash='dot'),
            name='Major axis',
            showlegend=False,  # Don't clutter the legend
            visible=True,
            hovertemplate='<b>Major axis</b><br>Full length = 2a'
        ))
    # ========== END OF NEW CODE ==========
    
# 2. After ω rotation
    if show_steps:
        coords1 = R_after_omega @ np.vstack([x0, y0, z0])
        fig.add_trace(go.Scatter3d(
            x=coords1[0], y=coords1[1], z=coords1[2],
            mode='lines',
            line=dict(color='purple', width=3, dash='dash'),
            name=f'2. After ω rotation ({omega:.1f}°)',
            showlegend=True,
            visible=True,
            hovertemplate=f'<b>Orbit after ω rotation</b><br>'
                          'Step 1: Orients the periapsis in the orbital plane.'
        ))

        # Add angle arc for ω
        if omega != 0:
            omega_arc_angle = np.linspace(0, omega_rad, 30)
            omega_arc_r = 0.25 * a
            fig.add_trace(go.Scatter3d(
                x=omega_arc_r * np.cos(omega_arc_angle),
                y=omega_arc_r * np.sin(omega_arc_angle),
                z=np.zeros_like(omega_arc_angle),
                mode='lines+text',
                line=dict(color='purple', width=3),
                text=[''] * 29 + [f'ω = {omega:.1f}°'],
                textposition='top center',
                name=f'ω angle ({omega:.1f}°)',
                showlegend=True,
                visible=True,
                hovertext=f'<b>Argument of Periapsis (ω)</b><br>Rotation: {omega:.1f}°<br>'
                          'Orients the periapsis relative to the line of nodes.'
            ))
    
    # After ω and i rotation
    if show_steps:
        coords2 = R_after_inclination @ np.vstack([x0, y0, z0])
        fig.add_trace(go.Scatter3d(
            x=coords2[0], y=coords2[1], z=coords2[2],
            mode='lines',
            line=dict(color='orange', width=3, dash='dot'),
            name=f'3. After ω and i rotation ({i:.1f}°)',
    #        legendgroup='transformations',
            showlegend=True,
            visible=True,
            hovertemplate=f'<b>Orbit after ω and i rotation</b><br>' 
            'Step 2: Applies the tilt to the orbital plane.'
        ))
    
# Fix for the inclination arc visibility issue in orbital_param_viz.py
# Replace the existing inclination arc section (around line 340-365) with this improved version:

    # Add inclination angle arc
    if i != 0:
        # The inclination arc should show the rotation around the X-axis (line of nodes)
        # after the ω rotation has been applied
        
        # Make the arc radius larger for better visibility
        inc_arc_r = 0.5 * scale_basis  # Increased from 0.3 * a for better visibility
        
        # Generate the arc in the YZ plane (rotation around X-axis)
        inc_arc_angle = np.linspace(0, i_rad, 30)
        
        # Create arc points - starts from Y-axis and rotates toward Z-axis
        inc_x = np.zeros_like(inc_arc_angle)
        inc_y = inc_arc_r * np.cos(inc_arc_angle)
        inc_z = inc_arc_r * np.sin(inc_arc_angle)
        
        # Transform the arc by the ω rotation to align with the line of nodes
        inc_arc_coords = R_after_omega @ np.vstack([inc_x, inc_y, inc_z])
        
        # Add the inclination arc trace
        fig.add_trace(go.Scatter3d(
            x=inc_arc_coords[0],
            y=inc_arc_coords[1],
            z=inc_arc_coords[2],
            mode='lines+markers+text',
            line=dict(color='orange', width=4),  # Increased width from 3
            marker=dict(
                size=[0] * 29 + [6],  # Add a marker at the end
                color='orange',
                symbol='diamond'
            ),
            text=[''] * 29 + [f'i = {i:.1f}°'],
            textposition='top center',
            textfont=dict(size=12, color='orange'),
            name=f'Inclination ({i:.1f}°)',
            showlegend=True,
            visible=True,
            hovertemplate=f'<b>Inclination (i)</b><br>Angle: {i:.1f}°<br>' +
                         'Tilts the orbit relative to the ecliptic plane.<br>' +
                         'Rotation around the X-axis (line of nodes).'
        ))
        
        # Optional: Add a visual guide line from origin to start of arc
        # This helps show what plane the rotation is in
        guide_start = R_after_omega @ np.array([0, inc_arc_r, 0])
        fig.add_trace(go.Scatter3d(
            x=[0, guide_start[0]],
            y=[0, guide_start[1]],
            z=[0, guide_start[2]],
            mode='lines',
            line=dict(color='orange', width=2, dash='dot'),
            showlegend=False,
            hovertemplate='Start of inclination rotation'
        ))
        
        # Add another guide line to the end of the arc
        guide_end = R_after_omega @ np.array([0, inc_arc_r * np.cos(i_rad), inc_arc_r * np.sin(i_rad)])
        fig.add_trace(go.Scatter3d(
            x=[0, guide_end[0]],
            y=[0, guide_end[1]],
            z=[0, guide_end[2]],
            mode='lines',
            line=dict(color='orange', width=2, dash='dot'),
            showlegend=False,
            hovertemplate='End of inclination rotation'
        ))

    """
    # Add inclination angle arc
    if i != 0:
        # Arc in the YZ plane after ω rotation
        inc_arc_angle = np.linspace(0, i_rad, 30)
        inc_arc_r = 0.3 * a
        inc_y = inc_arc_r * np.cos(inc_arc_angle)
        inc_z = inc_arc_r * np.sin(inc_arc_angle)
        inc_x = np.zeros_like(inc_arc_angle)
        
        # Transform arc to after ω rotation
        inc_arc_coords = R_after_omega @ np.vstack([inc_x, inc_y, inc_z])
        
        fig.add_trace(go.Scatter3d(
            x=inc_arc_coords[0],
            y=inc_arc_coords[1],
            z=inc_arc_coords[2],
            mode='lines+text',
            line=dict(color='orange', width=3),
            text=[''] * 29 + [f'i = {i:.1f}°'],
            textposition='top center',
            name=f'Inclination ({i:.1f}°)',
    #        legendgroup='angles',
            showlegend=True,
            visible=True,
            hovertext=f'<b>Inclination (i)</b><br>Angle: {i:.1f}°<br>' 
            'Tilts the orbit relative to the ecliptic plane.'
        ))
        """

    # 4. Final orbit
    coords_final = R_final @ np.vstack([x0, y0, z0])
    fig.add_trace(go.Scatter3d(
        x=coords_final[0], y=coords_final[1], z=coords_final[2],
        mode='lines',
        line=dict(color='red', width=4),
        name='4. Final Orbit',
    #    legendgroup='transformations',
        showlegend=True,
        visible=True,
        hovertemplate='<b>Final Orbit</b><br>In ecliptic coordinates'
    ))
    
    # Add Ω angle arc (longitude of ascending node)
    if Omega != 0:
        omega_big_arc_angle = np.linspace(0, Omega_rad, 30)
    #    omega_big_arc_r = 0.35 * a
        omega_big_arc_r = 0.35 * scale_basis  # Use scale_basis instead of a

        fig.add_trace(go.Scatter3d(
            x=omega_big_arc_r * np.cos(omega_big_arc_angle),
            y=omega_big_arc_r * np.sin(omega_big_arc_angle),
            z=np.zeros_like(omega_big_arc_angle),
            mode='lines+text',
            line=dict(color='red', width=4),
            text=[''] * 29 + [f'Ω = {Omega:.1f}°'],
            textposition='top center',
            name=f'Ω angle ({Omega:.1f}°)',
    #        legendgroup='angles',
            showlegend=True,
            visible=True,
            hovertext=f'<b>Longitude of Ascending Node (Ω)</b><br>Angle: {Omega:.1f}°<br>' 
            'Orients the orbit within the ecliptic frame.'
        ))

    # Add arc showing ω angle from ascending node to periapsis
    # This arc needs to be in the FINAL ORBITAL PLANE.

    if omega != 0:
        # Define the periapsis vector in the perifocal frame
        peri_perifocal = np.array([r_peri, 0, 0])
        # Calculate peri_final
        peri_final = R_final @ peri_perifocal 

    #    arc_radius = 0.35 * a # Use the same radius as other arcs
        arc_radius = 0.35 * scale_basis # Use scale_basis for consistent scaling

        # Get the actual Ascending Node point in the FINAL frame.
        # This uses the definition of the line of nodes already drawn.
        # We need a point on the orbit that is the ascending node.
        # This happens at true anomaly nu = -omega_rad in the perifocal frame.
        
        # Let's generate the ascending node point using the orbit equation,
        # then apply the full R_final transformation.
        # True anomaly for Ascending Node is -omega_rad
        r_at_AN = a * (1 - e**2) / (1 + e * np.cos(-omega_rad))
        
        # Perifocal coordinates of Ascending Node
        asc_node_perifocal = np.array([r_at_AN * np.cos(-omega_rad), 
                                       r_at_AN * np.sin(-omega_rad), 
                                       0])
        
        # Transform this point to the final frame
        asc_node_final_point = R_final @ asc_node_perifocal

        # Now, create a vector from the origin to this ascending node point, scaled for the arc
        start_vec_for_arc = (asc_node_final_point / np.linalg.norm(asc_node_final_point)) * arc_radius
        
        # Get the orbital plane's normal vector in the final frame.
        orbital_plane_normal_final = R_final @ np.array([0, 0, 1])
        orbital_plane_normal_final_norm = orbital_plane_normal_final / np.linalg.norm(orbital_plane_normal_final)

        arc_x_coords = []
        arc_y_coords = []
        arc_z_coords = []

        # Generate intermediate angles for the arc sweep
        # Sweep by omega_rad from the ascending node.
        num_points = 30
        sweep_angles = np.linspace(0, omega_rad, num_points)

        for angle in sweep_angles:
            # Rodrigues' Rotation Formula: V_rot = V*cos(theta) + (K x V)*sin(theta) + K*(K . V)*(1-cos(theta))
            V_rotated = start_vec_for_arc * np.cos(angle) + \
                        np.cross(orbital_plane_normal_final_norm, start_vec_for_arc) * np.sin(angle) + \
                        orbital_plane_normal_final_norm * np.dot(orbital_plane_normal_final_norm, start_vec_for_arc) * (1 - np.cos(angle))
            
            arc_x_coords.append(V_rotated[0])
            arc_y_coords.append(V_rotated[1])
            arc_z_coords.append(V_rotated[2])

        fig.add_trace(
            go.Scatter3d(
                x=arc_x_coords,
                y=arc_y_coords,
                z=arc_z_coords,
                mode='lines+text',
                line=dict(color='red', width=2, dash='dot'), 
                text=[''] * (len(arc_x_coords) - 1) + [f'ω = {omega:.1f}°'],
                textposition='bottom center', 
                name=f'ω angle (orbital plane)',
                showlegend=True,
                visible=True,
                hovertext=f'<b>Argument of Periapsis (ω)</b><br>'
                        f'Angle from Ascending Node to Periapsis.<br>'
                        f'Measured in the orbital plane.<br>Value: {omega:.1f}°'
            )
        )

    # Transform and add final periapsis/apoapsis markers
    peri_perifocal = np.array([r_peri, 0, 0])
    peri_final = R_final @ peri_perifocal

    # Create a combined trace for both apsides
    apsides_x = [peri_final[0]]
    apsides_y = [peri_final[1]]
    apsides_z = [peri_final[2]]
    apsides_text = ['Periapsis (final)']

# Calculate apsidal dates if we have position information
    perihelion_date_str = ""
    aphelion_date_str = ""
    
    if plot_date is None:
        plot_date = dt.datetime.now()
    
    print(f"DEBUG: Calculating apsidal dates for {obj_name}")
    print(f"  plot_date: {plot_date}")
    print(f"  current_position: {current_position}")
    
    # Try to calculate accurate dates if we have current position
    if current_position and 'x' in current_position:
        try:
            from apsidal_markers import calculate_apsidal_dates
            perihelion_date, aphelion_date = calculate_apsidal_dates(
                plot_date,
                current_position['x'],
                current_position['y'],
                current_position['z'],
                a,
                e,
                i,
                omega,
                Omega,
                obj_name
            )
            print(f"  Calculated dates - Perihelion: {perihelion_date}, Aphelion: {aphelion_date}")
            if perihelion_date:
                perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"
            if aphelion_date and e < 1:
                aphelion_date_str = f"<br>Date: {aphelion_date.strftime('%Y-%m-%d')}"
            print(f"  Date strings - Perihelion: {perihelion_date_str}, Aphelion: {aphelion_date_str}")
        except Exception as ex:
            print(f"Could not calculate apsidal dates: {ex}")
            import traceback
            traceback.print_exc()
    else:
        print("  No current position available for date calculation")
    
# ONLY use estimates if we don't have calculated dates
    if not perihelion_date_str or not aphelion_date_str:
        # Simple estimation based on orbital period
        if 'period' in params and params['period'] is not None:
            try:
                period_days = params['period']
                # For demonstration, show estimated dates
                # In reality, you'd need current mean anomaly to be accurate
                if not perihelion_date_str:
                    est_perihelion = plot_date + dt.timedelta(days=period_days/4)
                    perihelion_date_str = f"<br>Next perihelion: ~{est_perihelion.strftime('%Y-%m-%d')} (estimate)"
                if not aphelion_date_str:
                    est_aphelion = plot_date + dt.timedelta(days=3*period_days/4)
                    aphelion_date_str = f"<br>Next aphelion: ~{est_aphelion.strftime('%Y-%m-%d')} (estimate)"
            except:
                pass
        
        # Check if we have pre-calculated dates in params
        if not perihelion_date_str and 'perihelion_dates' in params and params['perihelion_dates']:
            # Find the next perihelion date after plot_date
            for date_str in params['perihelion_dates']:
                try:
                    peri_date = dt.datetime.strptime(date_str, '%Y-%m-%d')
                    if peri_date > plot_date:
                        perihelion_date_str = f"<br>Next perihelion: {date_str}"
                        break
                except:
                    pass
        
        if not aphelion_date_str and 'aphelion_dates' in params and params['aphelion_dates']:
            # Find the next aphelion date after plot_date
            for date_str in params['aphelion_dates']:
                try:
                    apo_date = dt.datetime.strptime(date_str, '%Y-%m-%d')
                    if apo_date > plot_date:
                        aphelion_date_str = f"<br>Next aphelion: {date_str}"
                        break
                except:
                    pass

    # CREATE apsides_hover OUTSIDE the if block
    apsides_hover = [f'<b>Periapsis (final)</b><br>Distance: {r_peri:.3f} AU from {center_object}{perihelion_date_str}']

    if e < 1.0:
        apo_perifocal = np.array([-r_apo, 0, 0])
        apo_final = R_final @ apo_perifocal
        apsides_x.append(apo_final[0])
        apsides_y.append(apo_final[1])
        apsides_z.append(apo_final[2])
        apsides_text.append('Apoapsis (final)')
        
        apsides_hover.append(f'<b>Apoapsis (final)</b><br>Distance: {r_apo:.3f} AU from {center_object}{aphelion_date_str}')

    fig.add_trace(go.Scatter3d(
        x=apsides_x,
        y=apsides_y,
        z=apsides_z,
        mode='markers+text',
        marker=dict(size=6, color='red', symbol='square-open'),
        text=apsides_text,
        textposition='top center',
        name='Apsides (final)',
        showlegend=True,
        visible=True,
        hovertemplate=apsides_hover
    ))
                
    # Fix for the line of nodes rendering issue in orbital_param_viz.py
    # Replace the line of nodes section (around line where it says "Add line of nodes if inclined")

    # Add line of nodes if inclined
    if i != 0:
        
        # For near-parabolic and hyperbolic orbits, use a more reasonable scale
        if e >= 0.99:  # Near-parabolic or hyperbolic
            # For these orbits, use perihelion distance as reference
            if a < 0:  # Hyperbolic with negative semi-major axis
                q = abs(a) * (e - 1)  # Perihelion for hyperbolic
            else:
                q = a * (1 - e)  # Perihelion for near-parabolic
            
            # Special case for known comets
            if obj_name == 'C/2025_K1':
                q = 0.33  # Known perihelion
            
            # Use a reasonable multiple of perihelion for line length
            nodes_length = max(3 * q, 1.0)  # At least 1 AU, at most 3x perihelion
        else:
            # For elliptical orbits, use the normal calculation
            nodes_length = 1.2 * abs(a)
        
        # Ensure nodes_length is reasonable (cap at 10 AU for visualization)
        nodes_length = min(nodes_length, 10.0)
        
        nodes_start = R3 @ np.array([-nodes_length, 0, 0])
        nodes_end = R3 @ np.array([nodes_length, 0, 0])
        
        fig.add_trace(go.Scatter3d(
            x=[nodes_start[0], nodes_end[0]],
            y=[nodes_start[1], nodes_end[1]],
            z=[nodes_start[2], nodes_end[2]],
            mode='lines',
            line=dict(color='red', width=2, dash='dashdot'),
            name='Line of Nodes',
            showlegend=True,
            visible=True,
            hovertemplate='<b>Line of Nodes</b><br>Intersection with ecliptic plane'
        ))
        
        # Ascending node marker
        asc_node = R3 @ np.array([nodes_length, 0, 0])
        fig.add_trace(go.Scatter3d(
            x=[asc_node[0]], y=[asc_node[1]], z=[asc_node[2]],
            mode='markers+text',
            marker=dict(size=6, color='red', symbol='square'),
            text=['Ascending Node'],
            textposition='top center',
            name='Ascending Node',
            showlegend=True,
            visible=True,
            hovertemplate='<b>Ascending Node</b><br>Where orbit crosses ecliptic plane northward'
        ))
    
# Add current position marker using the fetched position
    if current_position and 'x' in current_position:
        fig.add_trace(
            go.Scatter3d(
                x=[current_position['x']],
                y=[current_position['y']], 
                z=[current_position['z']],
                mode='markers+text',
                marker=dict(size=8, color='red', symbol='circle'),
                text=[f'{obj_name}'],
                textposition='top center',
                name=f'{obj_name} (final)',
                showlegend=True,
                hovertext=f'<b>{obj_name} Position</b><br>'
                         f'Date: {plot_date.strftime("%Y-%m-%d")}<br>'
                         f'X: {current_position["x"]:.3f} AU<br>'
                         f'Y: {current_position["y"]:.3f} AU<br>'
                         f'Z: {current_position["z"]:.3f} AU<br>'
                         f'Distance: {np.sqrt(current_position["x"]**2 + current_position["y"]**2 + current_position["z"]**2):.3f} AU'
            )
        )
    else:
        print(f"Warning: No position data available for {obj_name}")

    # Add direction of motion indicator
    # Define the arrow in the perifocal frame at true anomaly nu = 90 degrees
    nu_motion = np.pi / 2
    r_motion = a * (1 - e**2) / (1 + e * np.cos(nu_motion))
    
    # Position vector (start of arrow) in perifocal frame
    pos_motion_pf = np.array([0, r_motion, 0])

    # Tangent vector (direction of arrow) in perifocal frame
    tangent_vec_pf = np.array([-np.sin(nu_motion), e + np.cos(nu_motion), 0])
    tangent_vec_pf /= np.linalg.norm(tangent_vec_pf)

    # Reverse for retrograde orbits -- redundant, causes the retrograde to cancel
#    if i > 90:
#        tangent_vec_pf = -tangent_vec_pf

    arrow_len = 0.4 * a
    arrow_end_pf = pos_motion_pf + arrow_len * tangent_vec_pf

    # Transform the arrow's start and end points to the final ecliptic frame
    pos_motion_final = R_final @ pos_motion_pf
    arrow_end_final = R_final @ arrow_end_pf

    fig.add_trace(go.Scatter3d(
        x=[pos_motion_final[0], arrow_end_final[0]],
        y=[pos_motion_final[1], arrow_end_final[1]],
        z=[pos_motion_final[2], arrow_end_final[2]],
        mode='lines+markers+text',
        textposition='top center',
        line=dict(color='red', width=2),
        marker=dict(symbol='diamond', size=[0, 8], color='red'),
        name='Direction of Motion',
        showlegend=True,
        visible=True,
        hoverinfo='text',

        # Corrected: Provide text as a list for the two points
        text=['',  # No text for the start of the arrow
            f'Direction of Motion<br>'  # Text for the arrowhead
            f'Orbit is {"Retrograde (i > 90°)" if i > 90 else "Prograde (i < 90°)"}']
    ))

    # Update layout
    # Set axis range to accommodate extended coordinate frames
    axis_range = scale_basis * 2.5 # Use a larger buffer to ensure everything fits

#    axis_range = max(1.5 * scale_basis, 1.5 * axis_length)
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-axis_range, axis_range], title='X (AU)'),
            yaxis=dict(range=[-axis_range, axis_range], title='Y (AU)'),
            zaxis=dict(range=[-axis_range, axis_range], title='Z (AU)'),
            aspectmode='cube',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        title=dict(
            text=f"Orbital Parameter Transformation: {obj_name}<br><sub>Date: {plot_date.strftime('%Y-%m-%d %H:%M UTC')}</sub>",
            x=0.5,
            xanchor='center'
        ),
        margin=dict(r=50, l=50, t=80, b=50),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.5)',
            bordercolor='black',
            borderwidth=1,
            font=dict(size=12),
            itemsizing='constant',
            itemwidth=30,
            tracegroupgap=5,
            yanchor='top',
            xanchor='left'
        ),
        width=1450,
        height=680
    )
    
    # Add comprehensive annotation
    annotation_text = f"""<b>Orbital Transformation Visualization</b><br><br>
    <b>Orbital Elements:</b><br>
    • a = {a:.3f} AU (semi-major axis)<br>
    • e = {e:.6f} (eccentricity)<br>
    • i = {i:.1f}° (inclination)<br>
    • ω = {omega:.1f}° (argument of periapsis)<br>
    • Ω = {Omega:.1f}° (longitude of ascending node)<br><br>

    <b>Coordinate Frame Transformations:</b><br>
    The final transformation is a product of three rotations:<br>
    R = R_z(Ω) · R_x(i) · R_z(ω)<br><br>

    1. <b>Perifocal Frame</b> (cyan) - The orbit's 2D blueprint.<br>
    • Periapsis is aligned on the +X axis.<br><br>

    2. <b>After ω rotation</b> (purple) - Orients the ellipse.<br>
    • Rotates the frame by ω around the Z-axis.<br>
    <b>→ Sets the periapsis orientation within its orbital plane.</b><br><br>

    3. <b>After ω and i rotation</b> (orange) - Tilts the orbit.<br>
    • Tilts the frame by i around the new X-axis (the "hinge").<br>
    <b>→ Gives the orbit its tilt relative to the Ecliptic Plane.</b><br><br>

    4. <b>Final/Ecliptic Frame</b> (red) - Swivels the orbit.<br>
    • Rotates the tilted frame by Ω around the original (not orange) Z-axis.<br>
    <b>→ Swivels the orbit into its final place in the Ecliptic Frame.</b><br><br>

    <b>Key Insight:</b> This visualization shows the sequence of<br> 
    rotations applied to the initial Perifocal Orbit (cyan) to place it<br> 
    into its final orientation in the Ecliptic Frame (red).<br><br>

    <b>Interactive:</b> Click legend items to show/hide elements."""
    
    fig.add_annotation(
        text=annotation_text,
        xref="paper", yref="paper",
        x=1.03, y=0.98,                 # x=0.98 originally
        xanchor="right", yanchor="top",
        showarrow=False,
        font=dict(size=11, family="Arial"),
        align="left",
        bordercolor="gray",
        borderwidth=1,
        borderpad=10,
        bgcolor="rgba(255,255,255,0.5)"
    )
    
    return fig

# Note: Add these imports at the top of orbital_param_viz.py if not already there:
# from idealized_orbits import planetary_params, parent_planets
# from constants_new import KNOWN_ORBITAL_PERIODS

def create_eccentricity_demo_window(parent, objects=None, planetary_params_override=None):
    """
    Create a window with an interactive eccentricity slider visualization.
    Shows how eccentricity affects orbital shape from circle to hyperbola.
    
    Parameters:
        parent: Parent window
        objects: List of celestial objects from main app (optional)
        planetary_params_override: Override the global planetary_params if needed (optional)
    """
    # Use the global planetary_params by default, but allow override if passed
    params_to_use = planetary_params_override if planetary_params_override else planetary_params
    
    # Create new window
    demo_window = tk.Toplevel(parent)
    demo_window.title("Eccentricity Effects on Orbital Shape")
    demo_window.geometry("900x700")
    
    # Create main frame
    main_frame = ttk.Frame(demo_window)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create control frame at top
    control_frame = ttk.LabelFrame(main_frame, text="Eccentricity Visualization")
    control_frame.pack(fill='x', padx=5, pady=5)
    
    # Eccentricity value display and orbit type
    e_value_var = tk.StringVar(value="0.0167")  # Earth's eccentricity
    orbit_type_var = tk.StringVar(value="Ellipse")  # Earth has elliptical orbit
    
    # IMPORTANT: Define object_var HERE, before update_plot function
    object_var = tk.StringVar(value="Earth")  # Default to Earth
    
    # Labels and entry
    ttk.Label(control_frame, text="Eccentricity (e):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    # Entry field for numerical input
    e_entry = ttk.Entry(control_frame, textvariable=e_value_var, width=10, font=('TkDefaultFont', 12))
    e_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Validation function for entry
    def validate_entry(*args):
        try:
            value = float(e_value_var.get())
            if 0 <= value <= 10.0:
                e_slider.set(value)
                update_plot()
            else:
                # Clamp to valid range
                if value < 0:
                    e_value_var.set("0.0000")
                    e_slider.set(0)
                elif value > 10.0:
                    e_value_var.set("10.0000")
                    e_slider.set(10.0)
                update_plot()
        except ValueError:
            pass
    
    # Bind entry to validation
    e_entry.bind('<Return>', lambda e: validate_entry())
    e_entry.bind('<FocusOut>', lambda e: validate_entry())
    
    ttk.Label(control_frame, text="Orbit Type:").grid(row=0, column=2, padx=20, pady=5, sticky='w')
    orbit_type_label = tk.Label(control_frame, textvariable=orbit_type_var, font=('TkDefaultFont', 12, 'bold'))
    orbit_type_label.grid(row=0, column=3, padx=5, pady=5)
    
    # Slider
    e_slider = ttk.Scale(control_frame, from_=0.0, to=10.0, orient='horizontal', length=400)
    e_slider.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
    e_slider.set(0.0167)  # earth
    
    # Add tick marks
    tick_frame = ttk.Frame(control_frame)
    tick_frame.grid(row=2, column=0, columnspan=4, sticky='ew', padx=5)
    
    # Major tick marks
    ticks = [0, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0]
    tick_labels = ['0 (Circle)', '1 (Parabola)', '2', '4', '6', '8', '10']
    for i, (tick, label) in enumerate(zip(ticks, tick_labels)):
        ttk.Label(tick_frame, text=label, font=('TkDefaultFont', 9)).place(
            relx=tick/10.0, rely=0, anchor='n')
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('white')
    
    # Embed in tkinter
    canvas_frame = ttk.Frame(main_frame)
    canvas_frame.pack(fill='both', expand=True, pady=10)
    
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # Information panel
    info_frame = ttk.LabelFrame(main_frame, text="Orbital Parameters")
    info_frame.pack(fill='x', padx=5, pady=5)
    
    param_labels = {}
    param_info = [
        ('periapsis', 'Periapsis distance:', 'AU'),
        ('apoapsis', 'Apoapsis distance:', 'AU'),
        ('b', 'Semi-minor axis (b):', 'AU'),
        ('focus', 'Focus distance (c):', 'AU'),
    ]
    
    for i, (key, label, unit) in enumerate(param_info):
        ttk.Label(info_frame, text=label).grid(row=i//2, column=(i%2)*3, padx=5, pady=2, sticky='w')
        value_label = ttk.Label(info_frame, text="1.000")
        value_label.grid(row=i//2, column=(i%2)*3+1, padx=5, pady=2, sticky='e')
        ttk.Label(info_frame, text=unit).grid(row=i//2, column=(i%2)*3+2, padx=5, pady=2, sticky='w')
        param_labels[key] = value_label
    
    def update_plot(*args):
        """Update the plot based on slider value"""
        e = e_slider.get()
        print(f"Update plot called with e={e}")
        
        # Update value display
        e_value_var.set(f"{e:.6f}")
        
        # Determine orbit type
        if e < 0.01:
            orbit_type = "Circle"
            orbit_color = 'blue'
        elif e < 1.0:
            orbit_type = "Ellipse"
            orbit_color = 'green'
        elif e == 1.0:
            orbit_type = "Parabola (theoretical)"
            orbit_color = 'orange'
        else:
            orbit_type = "Hyperbola"
            orbit_color = 'red'
        
        orbit_type_var.set(orbit_type)
        
        # Clear the plot
        ax.clear()
        
        # Set up the plot with extra space for text box
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        
        # Get the selected object name - now properly accessible
        selected_obj = object_var.get()
        
        # Get the actual semi-major axis for the selected object
        if selected_obj in params_to_use:
            params = params_to_use[selected_obj]
            a = params.get('a', 1.0)  # Use object's actual semi-major axis
            print(f"Using {selected_obj}'s semi-major axis: {a} AU")
        else:
            a = 1.0  # Default to 1 AU if no data
            print(f"No data for {selected_obj}, using default a=1.0 AU")

# DYNAMIC AXES SCALING based on the orbit size
        # For hyperbolic orbits, 'a' is often negative in JPL data (standard convention)
        # We always use absolute value for distance calculations
        
        if e < 1.0:  # Ellipse or circle
            # For elliptical orbits, 'a' should be positive
            # The maximum extent is the apoapsis
            max_extent = abs(a) * (1 + e)
        elif abs(e - 1.0) < 0.01:  # Parabola
            # For parabolic orbits, show a reasonable portion
            max_extent = abs(a) * 3
        else:  # Hyperbola (e > 1)
            # For hyperbolic orbits, we need to determine the convention used
            # If a < 0, it's the JPL convention (common for comets)
            # If a > 0, it's the standard mathematical convention
            
            # Always use positive value for calculations
            a_for_calc = abs(a)
            
            # Calculate key distances
            r_peri = a_for_calc * (e - 1)  # Periapsis distance (always positive)
            center_dist = a_for_calc * e    # Distance to hyperbola center
            
            # The plot needs to show:
            # 1. The periapsis point clearly
            # 2. The hyperbola center (if reasonable)
            # 3. Enough of the trajectory to see the curve
            
            # For very high eccentricity, the center is far away
            # We should focus on the periapsis region
            if e > 5:
                # High eccentricity: focus on periapsis region
                max_extent = r_peri * 2.5  # Show 2.5x the periapsis distance
            else:
                # Moderate eccentricity: show more of the hyperbola
                max_extent = max(
                    r_peri * 3,        # At least 3x periapsis distance
                    center_dist * 1.2  # Include the center if not too far
                )
            
            print(f"DEBUG: Hyperbola scaling - a={a:.3f}, a_for_calc={a_for_calc:.3f}")
            print(f"DEBUG: e={e:.6f}, r_peri={r_peri:.3f}, center_dist={center_dist:.3f}")
            print(f"DEBUG: max_extent={max_extent:.3f}")
        
        # Add padding (20% extra space)
        plot_range = max_extent * 1.2
        
        # For extremely high eccentricity, ensure minimum visible range
        if e > 10 and plot_range < 2.0:
            plot_range = 2.0  # Minimum 2 AU range for visibility
        
        print(f"DEBUG: Final plot_range = ±{plot_range:.3f} AU")
        
        # Set up the plot with dynamic scaling
        ax.set_xlim(-plot_range, plot_range)
        ax.set_ylim(-plot_range, plot_range)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)

        if e < 1.0:  # Circle or Ellipse
            # Calculate orbital parameters
            b = a * np.sqrt(1 - e**2)  # Semi-minor axis
            c = a * e  # Focus distance from center
            
            # The center of the ellipse is at (-c, 0) from the primary focus
            center_x = -c
            center_y = 0

            # Periapsis and apoapsis distances from focus
            r_peri = a * (1 - e)
            r_apo = a * (1 + e)
            
            # Update parameter display
            param_labels['periapsis'].config(text=f"{r_peri:.3f}")
            param_labels['apoapsis'].config(text=f"{r_apo:.3f}")
            param_labels['b'].config(text=f"{b:.3f}")
            param_labels['focus'].config(text=f"{c:.3f}")
            
            # Draw the orbit using polar coordinates from the focus
            theta = np.linspace(0, 2*np.pi, 1000)
            r = a * (1 - e**2) / (1 + e * np.cos(theta))
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            
            ax.plot(x, y, color=orbit_color, linewidth=2, label=f'{orbit_type} (e={e:.6f})')
            
            # Mark the orbit center with a cross
            ax.plot(center_x, center_y, 'k+', markersize=10, markeredgewidth=2, 
                    label='Orbit Center', zorder=4)

            # Mark the foci
            # Primary focus (Sun) at origin
            ax.plot(0, 0, 'yo', markersize=10, label='Primary Focus (Sun)', zorder=5)
            
            # Empty focus at -2c from the Sun
            ax.plot(-2*c, 0, 'ko', markersize=6, label='Empty Focus', zorder=5)
            
            # Mark periapsis and apoapsis
            ax.plot(r_peri, 0, 'ro', markersize=8, label='Periapsis', zorder=5)
            ax.plot(-r_apo, 0, 'go', markersize=8, label='Apoapsis', zorder=5)
            
            # Add verification lines to show sum of distances is constant
            # Draw lines from periapsis to both foci
            ax.plot([r_peri, 0], [0, 0], 'r--', alpha=0.3, linewidth=1)
            ax.plot([r_peri, -2*c], [0, 0], 'r--', alpha=0.3, linewidth=1)
            
            # Draw lines from apoapsis to both foci
            ax.plot([-r_apo, 0], [0, 0], 'g--', alpha=0.3, linewidth=1)
            ax.plot([-r_apo, -2*c], [0, 0], 'g--', alpha=0.3, linewidth=1)
            
            # Add text box with definitions - positioned outside plot area
            textstr = f'''$\\mathbf{{Definitions}}$:
            - $\\mathbf{{{orbit_type}}}$: A conic section with eccentricity e = {e:.6f}
            - $\\mathbf{{Semi-major\\ axis\\ (a)}}$: Half the longest diameter of the ellipse
                a = {a:.3f} AU
            - $\\mathbf{{Semi-minor\\ axis\\ (b)}}$: Half the shortest diameter of the ellipse
                b = {b:.3f} AU
            - $\\mathbf{{Orbit\\ Center}}$: Geometric center of the ellipse at ({center_x:.3f}, 0) 
            - $\\mathbf{{Foci}}$: Two fixed points; the sum of distances from any
                point on the ellipse to both foci = {2*a:.3f} AU (constant)
            - $\\mathbf{{Periapsis}}$: Closest point to the primary focus (Sun)
                Distance = {r_peri:.3f} AU
            - $\\mathbf{{Apoapsis}}$: Farthest point from the primary focus
                Distance = {r_apo:.3f} AU
            - $\\mathbf{{c,\\ distance\\ from\\ center\\ to\\ either\\ foci}}$: c = {c:.3f} AU
            - $\\mathbf{{Focus\\ separation}}$: 2c = {2*c:.3f} AU
            - $\\mathbf{{Eccentricity}}$: e = c / a = {c / a:.6f}'''
            
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
            ax.text(1.02, 0.98, textstr, transform=ax.transAxes, fontsize=8,
                    verticalalignment='top', bbox=props, 
                    horizontalalignment='left')
                                
        else:  # Hyperbola
                    # For hyperbola, a is the distance from center to vertex
                    if e > 1:
                        # IMPORTANT: For hyperbolic orbits, 'a' might be negative in the data
                        # We need the absolute value for calculations
                        a_abs = abs(a)
                        
                        # Use the object's actual semi-major axis if available
                        b = a_abs * np.sqrt(e**2 - 1)
                        c = a_abs * e
                        r_peri = a_abs * (e - 1)
                        
                        # For a hyperbola with focus at origin, center is at (-c, 0)
                        center_x = -c
                        center_y = 0

                        # Update parameter display
                        param_labels['periapsis'].config(text=f"{r_peri:.3f}")
                        param_labels['apoapsis'].config(text="N/A")
                        param_labels['b'].config(text=f"{b:.3f}")
                        param_labels['focus'].config(text=f"{c:.3f}")
                        
                        # Draw hyperbola branch from focus
                        # Valid angle range for hyperbola
                        theta_max = np.arccos(-1/e)
                        
                        print(f"DEBUG: Hyperbola params - a={a}, a_abs={a_abs}, e={e}, theta_max={np.degrees(theta_max)}°")
                        print(f"DEBUG: b={b:.3f}, c={c:.3f}, r_peri={r_peri:.3f}, plot_range={plot_range:.3f}")
                        
                        # Generate angles for the hyperbola
                        # For high eccentricity, we need a focused approach
                        if e > 5:
                            # Very high eccentricity - focus on periapsis region
                            # The trajectory is almost straight, so use a small angle range
                            theta_range = min(theta_max - 0.01, np.pi/6)  # Max 30 degrees
                            num_points = 2000
                        elif e > 2:
                            # High eccentricity - use moderate angle range
                            theta_range = min(theta_max - 0.01, np.pi/3)  # Max 60 degrees
                            num_points = 1000
                        else:
                            # Normal hyperbola
                            theta_range = theta_max - 0.01
                            num_points = 500
                        
                        # Create the angle array
                        theta = np.linspace(-theta_range, theta_range, num_points)
                        
                        # Calculate radius for each angle using the conic section equation
                        # For hyperbola: r = a(e^2 - 1) / (1 + e*cos(theta))
                        denominator = 1 + e * np.cos(theta)
                        
                        # Avoid division by zero or negative radii
                        valid_angles = denominator > 0.001  # Small positive threshold
                        theta = theta[valid_angles]
                        denominator = denominator[valid_angles]
                        
                        r = a_abs * (e**2 - 1) / denominator
                        
                        print(f"DEBUG: Generated {len(theta)} angles, r range: {np.min(r) if len(r) > 0 else 0:.3f} to {np.max(r) if len(r) > 0 else 0:.3f}")
                        
                        # Filter out points that are too far from the origin
                        # For high eccentricity, be more restrictive
                        if e > 5:
                            max_r = min(plot_range, r_peri * 10)
                        else:
                            max_r = plot_range * 1.5
                            
                        valid_mask = (r > 0) & (r <= max_r)
                        
                        print(f"DEBUG: {np.sum(valid_mask)} valid points out of {len(r)} (max_r={max_r:.3f})")
                        
                        # Apply the mask
                        if np.sum(valid_mask) > 2:
                            theta = theta[valid_mask]
                            r = r[valid_mask]
                        else:
                            # Fallback: just show a tiny arc at periapsis
                            print(f"WARNING: Too few valid points for e={e:.6f}, using minimal arc")
                            theta = np.linspace(-0.01, 0.01, 50)
                            r = np.full_like(theta, r_peri)  # Just use periapsis distance
                        
                        # Convert to Cartesian coordinates
                        x = r * np.cos(theta)
                        y = r * np.sin(theta)
                        
                        print(f"DEBUG: Final plot has {len(x)} points")
                        print(f"DEBUG: x range: {np.min(x) if len(x) > 0 else 0:.3f} to {np.max(x) if len(x) > 0 else 0:.3f}")
                        print(f"DEBUG: y range: {np.min(y) if len(y) > 0 else 0:.3f} to {np.max(y) if len(y) > 0 else 0:.3f}")
                        
                        # Plot the hyperbola
                        if len(x) > 0:
                            ax.plot(x, y, color=orbit_color, linewidth=2, label=f'{orbit_type} (e={e:.6f})')
                        
                        # Mark the hyperbola center with a cross (only if it's within view)
                        if abs(center_x) < plot_range and abs(center_y) < plot_range:
                            ax.plot(center_x, center_y, 'k+', markersize=10, markeredgewidth=2, 
                                    label='Hyperbola Center', zorder=4)

                        # Draw asymptotes (corrected formula)
                        if abs(c) < plot_range * 2:  # Only if center is reasonably close
                            x_asym = np.linspace(-plot_range, plot_range, 100)
                            # Asymptotes pass through the center at (-c, 0)
                            # Slope is ±b/a
                            y_asym_upper = (b/a_abs) * (x_asym + c)
                            y_asym_lower = -(b/a_abs) * (x_asym + c)
                            
                            # Only plot points within the viewing area
                            mask = (np.abs(y_asym_upper) <= plot_range) & (np.abs(x_asym) <= plot_range)
                            if np.sum(mask) > 1:
                                ax.plot(x_asym[mask], y_asym_upper[mask], 'k--', alpha=0.3, linewidth=1)
                                ax.plot(x_asym[mask], y_asym_lower[mask], 'k--', alpha=0.3, linewidth=1)
                        
                        # Mark primary focus (Sun) at origin
                        ax.plot(0, 0, 'yo', markersize=10, label='Primary Focus (Sun)', zorder=5)
                        
                        # Mark periapsis
                        ax.plot(r_peri, 0, 'ro', markersize=8, label='Periapsis', zorder=5)
                        
                        # Add text box with definitions - positioned outside plot area
                        # Calculate actual distances for clarity
                        geometric_a = abs(center_x) + r_peri  # Sum of absolute distances
                        
                        textstr = f'''$\\mathbf{{Definitions}}$:
                        - $\\mathbf{{Hyperbola}}$: A conic section with eccentricity > 1; e = {e:.6f} 
                            Represents a fly-by trajectory with excess velocity
                            
                        - $\\mathbf{{Semi-major\\ axis\\ 'a'}}$:

                            1) Orbital mechanics, 'a' (in JPL Horizons ephemeris):
                                Used in calculations; can be a negative sum relative to the Sun (0,0)
                                Same definition: distance from geometric center to vertex (periapsis), but
                                    uses the vector distances relative to the Sun, so
                                a = distance from Sun to periapsis + (negative) distance from Sun to the center 
                                    = {r_peri:.3f} + {center_x:.3f} = {a:.3f} AU
                            
                            2) Geometric, 'a' (same as for ellipses):
                                This is the geometric distance from center to vertex (periapsis), or
                                Half the major axis distance,
                                a = distance from Sun to periapsis + (geometric) distance from Sun to the center 
                                    = {r_peri:.3f} + |{center_x:.3f}|  = {geometric_a:.3f} AU
                            
                        - $\\mathbf{{Focus\\ distance\\ , c}}$:
                            This is the distance from center to focus (Sun); uses absolute value of orbital mechanics, a
                            c = |a| $\\cdot$ e = {a_abs:.3f} $\\cdot$ {e:.6f} = {c:.3f} AU ✓
                            
                        - $\\mathbf{{Eccentricity\\ , e}}$:
                            Eccentricity definition; uses absolute value of orbital mechanics, a
                            e = c / |a| = {c:.3f} / {a_abs:.3f} = {e:.6f} ✓'''
                        
                        props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
                        ax.text(1.02, 0.98, textstr, transform=ax.transAxes, fontsize=8,
                                verticalalignment='top', bbox=props,
                                horizontalalignment='left')
        
        # Add reference circle (e=0) - scale with the object's semi-major axis
        if e > 0.01:
            circle = plt.Circle((0, 0), a, fill=False, color='gray', 
                              linestyle='--', alpha=0.3, label='Reference circle (e=0)')
            ax.add_patch(circle)
        
        # Labels and legend
        ax.set_xlabel('Distance (AU)')
        ax.set_ylabel('Distance (AU)')
        # Use selected_obj in title instead of "Demo Object"
        ax.set_title(f'{selected_obj} - Orbital Shape vs Eccentricity\n{orbit_type}: e = {e:.6f}')
        
        # Position legend to avoid text box
    #    ax.legend(loc='upper left', fontsize=9)
        # With this line to position the legend outside the plot area to the left:
        ax.legend(bbox_to_anchor=(-0.15, 1), loc='upper right', fontsize=9)        
        
        # Add educational annotations at the bottom
        # Calculate the correct sum of distances for the current semi-major axis
        if e < 0.01:
            bottom_text = 'Perfect circle: All points equidistant from center'
        elif e < 0.99:
            # For an ellipse, the sum of distances to both foci is 2a
            sum_of_distances = 2 * a
            bottom_text = f'Ellipse: Sum of distances to both foci = {sum_of_distances:.3f} AU (constant)'
        elif abs(e - 1.0) < 0.01:
            bottom_text = 'Parabola: Escape trajectory, never returns'
        else:
            bottom_text = 'Hyperbola: Excess velocity, escapes on hyperbolic path'
        
    #    ax.text(0, -2.3, bottom_text, ha='center', fontsize=9, style='italic')
        # Position bottom text dynamically based on plot range
        ax.text(0, -plot_range * 0.92, bottom_text, ha='center', fontsize=9, style='italic')
        
        # Adjust figure layout to make room for the text box
        plt.tight_layout()
        plt.subplots_adjust(right=0.65)  # Make room for text box on the right
        
        canvas.draw()
    
    # Bind slider to update function
    e_slider.config(command=update_plot)

    # Initial plot with Earth's values
    update_plot()  # This draws the initial Earth orbit
    
    # Add object selection dropdown
    select_frame = ttk.Frame(control_frame)
    select_frame.grid(row=3, column=0, columnspan=4, pady=5)
    
    ttk.Label(select_frame, text="Select Object:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    # Filter objects that have orbital parameters
    if objects and params_to_use:
        objects_with_params = [obj['name'] for obj in objects 
                              if obj['name'] in params_to_use]
        print(f"DEBUG: Found {len(objects_with_params)} objects with parameters")
    else:
        # Use all objects from params_to_use
        objects_with_params = list(params_to_use.keys()) if params_to_use else ["Earth"]
        print(f"DEBUG: Using {len(objects_with_params)} objects from planetary_params")
    
    object_combo = ttk.Combobox(select_frame, textvariable=object_var, 
                                values=objects_with_params, width=25)
    object_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    
    # Add an "Update from Object" button next to the dropdown
    def update_from_object():
        """Update the visualization with the selected object's eccentricity"""
        selected_obj = object_var.get()
        print(f"DEBUG: Update button clicked for object: {selected_obj}")
        
        if not selected_obj:
            print("DEBUG: No object selected")
            return
        
        # Check if we have the object in our params
        if selected_obj in params_to_use:
            params = params_to_use[selected_obj]
            print(f"DEBUG: Found params for {selected_obj}: {params}")
            
            if 'e' in params:
                e_val = params['e']
                print(f"DEBUG: Eccentricity value: {e_val}")
                
                # Update slider
                e_slider.set(e_val)
                print(f"DEBUG: Slider set to {e_val}")
                
                # Update entry field
                e_value_var.set(f"{e_val:.4f}")
                print(f"DEBUG: Entry field set to {e_val:.4f}")
                
                # Force update the plot
                update_plot()
                print("DEBUG: update_plot() called")
                
                # Force canvas refresh
                try:
                    canvas.draw()
                    print("DEBUG: Canvas draw() called")
                except:
                    print("DEBUG: Canvas draw() failed")
            else:
                print(f"DEBUG: No eccentricity found for {selected_obj}")
                messagebox.showwarning("No Data", f"No eccentricity data found for {selected_obj}")
        else:
            print(f"DEBUG: {selected_obj} not found in planetary_params")
            messagebox.showwarning("No Data", f"No orbital parameters found for {selected_obj}")
    
    update_button = ttk.Button(select_frame, text="Update from Object", 
                              command=update_from_object, width=20)
    update_button.grid(row=0, column=3, padx=5, pady=5)
    
    # Add the special case buttons below
    button_frame = ttk.Frame(control_frame)
    button_frame.grid(row=4, column=0, columnspan=4, pady=5)
    
    special_cases = [
        ("Perfect Circle", 0.0),
        ("Parabola (escape)", 1.0),
        ("Mild Hyperbola", 1.5),
        ("Strong Hyperbola", 2.0),
        ("3I/Atlas", 6.1511),  # Added real high-eccentricity example
    ]
    
    for i, (label, e_val) in enumerate(special_cases):
        btn = ttk.Button(button_frame, text=label, width=20,
                        command=lambda e=e_val: (e_slider.set(e), 
                                               e_value_var.set(f"{e:.6f}"), 
                                               update_plot()))
        btn.grid(row=0, column=i, padx=2)
    
    # Update instructions
    instruction_label = ttk.Label(control_frame, 
                                 text="For eccentricity illustration purposes: use slider, type a value (0-10), select object + Update, or use quick buttons",
                                 font=('TkDefaultFont', 9, 'italic'))
    instruction_label.grid(row=5, column=0, columnspan=4, pady=(5, 0))
        
    return demo_window

def create_orbital_viz_window(root, objects, planetary_params, parent_planets=None,
                            current_positions=None, current_date=None):
    """
    Create a window for orbital parameter visualization.
    To be called from palomas_orrery.py
    
    Parameters:
        root: Parent tkinter window
        objects: List of celestial objects
        planetary_params: Dictionary of orbital parameters
        parent_planets: Dictionary mapping planets to their satellites
        current_positions: Dictionary of current positions {name: {'x': x, 'y': y, 'z': z}}
        current_date: Current date being displayed
    """
    # Store these for use in create_visualization
    stored_positions = current_positions or {}
    stored_date = current_date or dt.datetime.now()

    # Create new window
    viz_window = tk.Toplevel(root)
    viz_window.title("Orbital Parameter Visualization")
    viz_window.geometry("1400x800")
    
    # Create main frame
    main_frame = ttk.Frame(viz_window)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create left frame for controls
    control_frame = ttk.LabelFrame(main_frame, text="Visualization Controls")
    control_frame.pack(side='left', fill='y', padx=(0, 10))
    
    # Object selection
    ttk.Label(control_frame, text="Select Object:").grid(row=0, column=0, 
                                                         padx=5, pady=5, sticky='w')
    
    # Filter objects that have orbital parameters
    objects_with_params = [obj['name'] for obj in objects 
                          if obj['name'] in planetary_params]
    
    object_var = tk.StringVar(value="Earth")

    object_combo = ttk.Combobox(control_frame, textvariable=object_var, 
                                values=objects_with_params, width=25)
    object_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    
    # Display options
    ttk.Label(control_frame, text="Display Options:").grid(row=1, column=0, 
                                                           columnspan=3, padx=5, pady=(15,5))
    
    show_orbit_steps_var = tk.BooleanVar(value=True)
    show_coordinate_frames_var = tk.BooleanVar(value=True)
    show_final_only_var = tk.BooleanVar(value=False)
    show_apsidal_markers_var = tk.BooleanVar(value=True)  # ADD THIS LINE
    
    ttk.Checkbutton(control_frame, text="Show Orbit Transformation Steps", 
                    variable=show_orbit_steps_var).grid(row=2, column=0, 
                                                        columnspan=3, padx=20, pady=2, sticky='w')
    ttk.Checkbutton(control_frame, text="Show Coordinate Frames", 
                    variable=show_coordinate_frames_var).grid(row=3, column=0, 
                                                             columnspan=3, padx=20, pady=2, sticky='w')
    ttk.Checkbutton(control_frame, text="Show Final Orbit Only (Simplified)", 
                    variable=show_final_only_var).grid(row=4, column=0, 
                                                       columnspan=3, padx=20, pady=2, sticky='w')
    ttk.Checkbutton(control_frame, text="Show Perihelion/Aphelion Markers",   # ADD THESE LINES
                    variable=show_apsidal_markers_var).grid(row=5, column=0, 
                                                            columnspan=3, padx=20, pady=2, sticky='w')
    
    # Add separator
    ttk.Separator(control_frame, orient='horizontal').grid(row=6, column=0, 
                                                          columnspan=3, sticky='ew', pady=10)
    
    # Orbital parameters display
    param_frame = ttk.LabelFrame(control_frame, text="Orbital Elements")
    param_frame.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
    
    # Parameter labels
    param_labels = {}
    param_names = [
        ('a', 'Semi-major axis:', 'AU'),
        ('e', 'Eccentricity:', ''),
        ('i', 'Inclination:', '°'),
        ('omega', 'Arg. of Periapsis (ω):', '°'),
        ('Omega', 'Long. of Asc. Node (Ω):', '°'),
        ('period', 'Orbital Period:', 'days')
    ]
    
    for idx, (key, label, unit) in enumerate(param_names):
        ttk.Label(param_frame, text=label).grid(row=idx, column=0, 
                                               padx=5, pady=2, sticky='w')
        value_label = ttk.Label(param_frame, text="---")
        value_label.grid(row=idx, column=1, padx=5, pady=2, sticky='e')
        unit_label = ttk.Label(param_frame, text=unit)
        unit_label.grid(row=idx, column=2, padx=5, pady=2, sticky='w')
        param_labels[key] = value_label
    
    # Display Earth's parameters immediately
    if "Earth" in planetary_params:
        params = planetary_params["Earth"]
        for key, label in param_labels.items():
            if key in params:
                value = params[key]
                if isinstance(value, float):
                    label.config(text=f"{value:.4f}" if key == 'e' 
                               else f"{value:.2f}")
                else:
                    label.config(text=str(value))
            else:
                label.config(text="---")

# Create visualization button
    def create_visualization():
        selected_obj = object_var.get()
        if not selected_obj:
            messagebox.showwarning("No Selection", "Please select an object")
            return
        
        try:
            # Update parameter display
            if selected_obj in planetary_params:
                params = planetary_params[selected_obj]
                for key, label in param_labels.items():
                    if key in params:
                        value = params[key]
                        if isinstance(value, float):
                            label.config(text=f"{value:.4f}" if key == 'e' 
                                       else f"{value:.2f}")
                        else:
                            label.config(text=str(value))
                    else:
                        label.config(text="---")
            
            # Get current position for the selected object
            current_position = None
            current_date = stored_date  # Use the stored date
            
            # Check if we have a passed position for this object
            if selected_obj in stored_positions:
                current_position = stored_positions[selected_obj]
                print(f"Using passed position for {selected_obj}: x={current_position['x']:.3f}, y={current_position['y']:.3f}, z={current_position['z']:.3f}")
            else:
                print(f"No position data passed for {selected_obj}, fetching now...")
                
                # Import fetch_trajectory from the main app
                try:
                    from palomas_orrery_helpers import fetch_trajectory
                    
                    # Get center info (assuming Sun for now)
            #        center_id = 10  # Sun's ID
                    center_id = '10'  # Sun's ID as a string
                    
                    # Find the object in the objects list
                    obj_id = None
                    id_type = None
                    for obj in objects:
                        if obj['name'] == selected_obj:
                    #        obj_id = obj['id']
                            obj_id = str(obj['id'])  # Ensure ID is a string too
                            id_type = obj.get('id_type', None)
                            break
                    
                    if obj_id:
                        print(f"  Fetching position for {selected_obj} (ID: {obj_id})...")
                        # Fetch the position
                        trajectory = fetch_trajectory(
                            obj_id,
                            [current_date.strftime('%Y-%m-%d')],
                            center_id=center_id,
                            id_type=id_type
                        )
                        
                        if trajectory and len(trajectory) > 0 and trajectory[0]:
                            current_position = trajectory[0]
                            if 'x' in current_position:
                                print(f"  Fetched position: ({current_position['x']:.3f}, {current_position['y']:.3f}, {current_position['z']:.3f})")
                            else:
                                print(f"  Position data incomplete")
                        else:
                            print(f"  No position data returned")
                    else:
                        print(f"  Could not find object ID for {selected_obj}")
                        
                except Exception as ex:
                    print(f"  Could not fetch current position: {ex}")
                    import traceback
                    traceback.print_exc()

            # Determine the correct boolean values based on the checkboxes
            show_final_only = show_final_only_var.get()
            
            # If "Show Final Only" is checked, it overrides the "Show Steps" option.
            show_steps_val = show_orbit_steps_var.get() and not show_final_only
            show_axes_val = show_coordinate_frames_var.get()
            show_apsidal_val = show_apsidal_markers_var.get()            

            # Create an empty figure object to pass to the function.
            # The function will clear and build this figure internally.
            fig = go.Figure()

            # Create the visualization with the CORRECT parameter names
            create_orbital_transformation_viz(
                fig, # Pass the figure object
                selected_obj, 
                planetary_params,
                show_steps=show_steps_val, # Corrected parameter name
                show_axes=show_axes_val,    # Corrected parameter name
                parent_planets=parent_planets, # Add this argument
                show_apsidal_markers=show_apsidal_val,
                plot_date=current_date,        # Changed from dt.datetime.now() to current_date
                current_position=current_position  # Added this new parameter
            )
            
            if fig.data:    
                # Show in browser
                # Generate a descriptive default filename for the plot
                current_date_str = dt.datetime.now().strftime('%Y%m%d')
                default_name = f"Orbital_Transformation_{selected_obj.replace(' ', '_')}_{current_date_str}"

                # Use the existing safe showing/saving function from the main application
                show_figure_safely(fig, default_name)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")
    
    create_button = ttk.Button(control_frame, text="Create Orbital Parameter Visualization", 
                              command=create_visualization, width=40)  # Increased width
    create_button.grid(row=8, column=0, columnspan=3, pady=20, padx=5)
    
    # Add the eccentricity demo button
    demo_button = ttk.Button(
        control_frame, 
        text="Interactive Orbital Eccentricity Visualization", 
        command=lambda: create_eccentricity_demo_window(viz_window, objects, planetary_params),
        width=40  # Increased width
    )
    demo_button.grid(row=9, column=0, columnspan=3, pady=10, padx=5)

    # Add debug to verify parameters exist here
    print(f"DEBUG in create_orbital_viz_window:")
    print(f"  - objects exists: {objects is not None}")
    print(f"  - planetary_params exists: {planetary_params is not None}")
    if planetary_params:
        print(f"  - planetary_params has {len(planetary_params)} objects")

    # Add tooltip for the demo button (using the CreateToolTip class already in orbital_param_viz.py)
    CreateToolTip(demo_button, 
        "Launch an interactive visualization showing how eccentricity\n"
        "affects orbital shape from circle (e=0) through ellipse,\n"
        "parabola (e=1), to hyperbola (e>1).")

    # Information text
    info_frame = ttk.LabelFrame(main_frame, text="Understanding the Visualization")
    info_frame.pack(side='right', fill='both', expand=True)
    
    info_text = tk.Text(info_frame, wrap='word', width=60, height=35)
    info_text.pack(fill='both', expand=True, padx=5, pady=5)
    
    info_content = """# ORBITAL PARAMETER TRANSFORMATION VISUALIZATION

    This tool demonstrates how Keplerian orbital elements transform an orbit from its natural coordinate system (perifocal frame) to the standard ecliptic reference frame used in astronomy.

    ## KEY CONCEPTS

    ### Coordinate Frames
    • **Perifocal Frame (Cyan)**: The orbit's natural coordinate system
    - X-axis points to periapsis (closest approach)
    - Orbit lies in XY plane
    - Specific to each individual orbit
    - This is the orbit's "2D blueprint"

    • **Ecliptic Frame (Red)**: The standard reference frame
    - XY plane is Earth's orbital plane
    - X-axis points to vernal equinox (♈)
    - Same for all objects in the solar system
    - The universal coordinate system for astronomy

    ### TRANSFORMATION SEQUENCE

    The visualization shows how three sequential rotations place the orbit into its final orientation:
    **R = Rz(Ω) · Rx(i) · Rz(ω)**

    1. **Initial State (Cyan)**: Perifocal Frame
    - The orbit in its simplest form
    - Periapsis aligned on +X axis

    2. **After ω rotation (Purple)**: Argument of Periapsis
    - Rotates the frame by ω around Z-axis
    - Sets the periapsis orientation within the orbital plane

    3. **After ω and i rotation (Orange)**: Inclination
    - Tilts the frame by i around the new X-axis (the "hinge")
    - Gives the orbit its tilt relative to the Ecliptic plane

    4. **Final State (Red)**: Longitude of Ascending Node
    - Rotates the tilted frame by Ω around the original Z-axis
    - Swivels the orbit into its final position in the Ecliptic frame

    **Important**: The coordinate systems rotate, not the orbit itself! The orbit maintains its shape and orientation relative to each coordinate frame.

    ## VISUAL ELEMENTS

    • **Coordinate Axes**: Shows each reference frame's orientation
    • **Orbital Curves**: Displays orbit at each transformation stage
    • **Periapsis/Apoapsis Markers**: 
    - Periapsis: Closest approach (perihelion for Sun, perigee for planets)
    - Apoapsis: Farthest point (aphelion for Sun, apogee for planets)
    - Hover over markers to see predicted dates and distances
    • **Current Position**: Shows the object's location at the selected date
    • **Line of Nodes**: Where orbit crosses the reference plane
    • **Ascending Node**: Where orbit rises above the reference plane

    ## INTERACTIVE FEATURES

    • **3D Navigation**:
    - Click and drag to rotate view
    - Scroll to zoom in/out
    - Double-click to reset view

    • **Display Options**:
    - Toggle transformation steps on/off
    - Show/hide coordinate frames
    - Display final orbit only (simplified view)
    - Toggle perihelion/aphelion markers

    • **Legend Interaction**:
    - Click legend items to show/hide elements
    - Useful for focusing on particular aspects of the transformation

    ## REAL-TIME INTEGRATION

    When launched from the main application:
    • Uses current date from the main plot
    • Shows actual object position at that date
    • Displays calculated apsidal dates (perihelion/aphelion)
    • All positions use JPL Horizons ephemeris data for accuracy

    ## INTERACTIVE ORBITAL ECCENTRICITY VISUALIZATION

    The **Interactive Orbital Eccentricity Visualization** is a companion tool that demonstrates how eccentricity affects orbital shape across all conic sections:

    ### Purpose
    • **Educational Focus**: Understand eccentricity's fundamental role in orbital mechanics
    • **Complete Spectrum**: Visualize all conic sections from circles to hyperbolas
    • **Interactive Learning**: Real-time manipulation of eccentricity values

    ### Features
    • **Dynamic Slider Control**: 
    - Adjust eccentricity from 0 (perfect circle) to 10+ (extreme hyperbola)
    - Real-time orbital shape updates
    - Numerical input for precise values

    • **Comprehensive Orbit Types**:
    - **Circle** (e ≈ 0): Perfect circular orbits
    - **Ellipse** (0 < e < 1): Bound, periodic orbits like planets
    - **Parabola** (e = 1): Escape velocity trajectory
    - **Hyperbola** (e > 1): Flyby trajectories with excess velocity

    • **Educational Annotations**:
    - Real-time geometric calculations
    - Focus positions and distances
    - Apsidal distances (periapsis/apoapsis)
    - Mathematical relationships (c = ae, sum of distances to foci)

    • **Object Selection**: 
    - Choose from real celestial objects
    - See actual orbital parameters
    - Compare theoretical shapes with real orbits

    ### Key Learning Points
    • **Eccentricity Scale**: 
    - Earth: e = 0.0167 (nearly circular)
    - Mars: e = 0.0934 (slightly elliptical)  
    - Comets: e ≈ 0.8-0.99 (highly elliptical)
    - Hyperbolic asteroids: e > 1 (escape trajectories)

    • **Geometric Relationships**:
    - Focus distance: c = a × e
    - Semi-minor axis: b = a√(1-e²) for ellipses
    - Periapsis distance: a(1-e) for bound orbits
    - Apoapsis distance: a(1+e) for bound orbits

    • **Physical Interpretation**:
    - Low e: Stable, circular-like orbits
    - High e: Eccentric orbits with dramatic distance variations
    - e = 1: Minimum energy for escape
    - e > 1: Excess kinetic energy, never returns

    ### Integration with Main Visualization
    • **Complementary Tools**: Use together to understand both shape (eccentricity) and orientation (other orbital elements)
    • **Real Object Data**: Eccentricity values from actual celestial objects
    • **Consistent Framework**: Same mathematical foundations and coordinate systems

    This tool provides intuitive understanding of how a single parameter—eccentricity—determines whether an object follows a closed orbit around its primary or escapes to interstellar space.

    ## NOTE ON SATELLITE ORBITS

    This visualization shows idealized Keplerian orbits. Real satellite orbits (like the Moon's) are affected by:
    - Parent planet's equatorial bulge (oblateness)
    - Gravitational pull from the Sun
    - Perturbations from other nearby moons
    - Tidal forces and resonances

    The main application uses refined models (idealized_orbits.py) that account for these effects, providing more accurate satellite positions.

    ## EDUCATIONAL VALUE

    This visualization bridges the gap between:
    - **Abstract parameters** (a, e, i, ω, Ω) that define orbits mathematically
    - **Physical reality** of how celestial objects move through 3D space

    By showing the step-by-step transformation, it helps develop intuition for how each parameter affects the final orbit orientation."""
    
    info_text.insert('1.0', info_content)
    info_text.config(state='disabled')  # Make read-only
    
    return viz_window

# For backward compatibility with existing code
def create_orbital_transformation_viz_legacy(fig, obj_name, planetary_params, **kwargs):
    """Legacy function for compatibility"""
    new_fig = create_orbital_transformation_viz(obj_name, planetary_params, **kwargs)
    return new_fig if new_fig else fig