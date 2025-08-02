import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt
from constants_new import KNOWN_ORBITAL_PERIODS
from shutdown_handler import show_figure_safely # Add this line
# from idealized_orbits import parent_planets, planetary_params     
# not needed because the dictionaries are being passed into its functions as an argument

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
                                    center_object='Sun', parent_planets=None):
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
    if e < 1.0:
        scale_basis = a  # Use semi-major axis for ellipses
    else:
        scale_basis = r_peri  # Use periapsis distance for hyperbolic orbits
    
    # Use absolute value of 'a' for scaling to handle hyperbolic orbits -- a is too small to see the orbit
#    scale_basis = abs(a)
    
    # Coordinate frame axis length - scale with a buffer
    axis_length = scale_basis * 1.5     # 150% of semi-major axis for a good visual buffer

    # Coordinate frame axis length - scale with a buffer
#    axis_length = a * 1.5  # 150% of semi-major axis for a good visual buffer

    # Coordinate frame axis length - extend to at least semi-major axis
#    axis_length = max(a * 1.1, 0.5)  # At least 110% of semi-major axis
    
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
    fig.add_trace(go.Scatter3d(
        x=x0, y=y0, z=z0,
        mode='lines',
        line=dict(color='cyan', width=4),
        name='1. Perifocal Frame',
    #    legendgroup='transformations',
        showlegend=True,
        visible=True,
        hovertemplate='<b>Perifocal Orbit</b><br>The orbit in its natural, un-rotated frame.'
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
        omega_big_arc_r = 0.35 * a
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

        arc_radius = 0.35 * a # Use the same radius as other arcs

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
    apsides_hover = [f'<b>Periapsis (final)</b><br>Distance: {r_peri:.3f} AU from {center_object}']

    if e < 1.0:
        apo_perifocal = np.array([-r_apo, 0, 0])
        apo_final = R_final @ apo_perifocal
        apsides_x.append(apo_final[0])
        apsides_y.append(apo_final[1])
        apsides_z.append(apo_final[2])
        apsides_text.append('Apoapsis (final)')
        apsides_hover.append(f'<b>Apoapsis (final)</b><br>Distance: {r_apo:.3f} AU from {center_object}')

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
                
    # Add line of nodes if inclined
    if i != 0:
        nodes_length = 1.2 * abs(a)         # to ensure the length is always a positive value
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
    
    # Add current position if we have orbital period
    if 'period' in params and params['period'] is not None:
        try:
            # Calculate mean anomaly at plot_date
            period_days = params['period']
            
            # Always use J2000 for calculation, regardless of what's in params
            epoch = dt.datetime(2000, 1, 1, 12, 0, 0)  # J2000                
            
            # Time since epoch
            time_diff = (plot_date - epoch).total_seconds() / 86400.0  # days
            
            # Mean motion (degrees per day)
            n = 360.0 / period_days
            
            # Mean anomaly at plot_date
            M0 = params.get('M', 0.0)  # Mean anomaly at epoch
            M = (M0 + n * time_diff) % 360.0
            M_rad = np.radians(M)
            
            # Solve Kepler's equation for eccentric anomaly
            E = M_rad
            for _ in range(10):  # Newton-Raphson iteration
                E = E - (E - e * np.sin(E) - M_rad) / (1 - e * np.cos(E))
            
            # True anomaly
            if e < 1:
                nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E/2), 
                                   np.sqrt(1 - e) * np.cos(E/2))
            else:
                # Hyperbolic case
                nu = 2 * np.arctan2(np.sqrt(e + 1) * np.sinh(E/2),
                                   np.sqrt(e - 1) * np.cosh(E/2))
            
            # Position in perifocal frame
            r_current = a * (1 - e**2) / (1 + e * np.cos(nu))
            x_pf = r_current * np.cos(nu)
            y_pf = r_current * np.sin(nu)
            z_pf = 0
            
            # Transform to final frame using the correct, pre-computed matrix
            pos_perifocal = np.array([x_pf, y_pf, z_pf])
            pos_final = R_final @ pos_perifocal
            
            x_final, y_final, z_final = pos_final[0], pos_final[1], pos_final[2]
            
            # Add current position marker
            fig.add_trace(
                go.Scatter3d(
                    x=[x_final], y=[y_final], z=[z_final],
                    mode='markers+text',
                    marker=dict(size=8, color='red', symbol='circle'),
                    text=[f'{obj_name}'],
                    textposition='top center',
                    name=f'{obj_name} (final)',
                    showlegend=True,
            #        visible='legendonly',
                    hovertext=f'<b>{obj_name} Position</b><br>Date: {plot_date.strftime("%Y-%m-%d")}<br>' 
                    'True Anomaly: {np.degrees(nu):.1f}°'
                )
            )
        except Exception as e:
            print(f"Could not calculate current position: {e}")

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
    • e = {e:.4f} (eccentricity)<br>
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

def create_orbital_viz_window(root, objects, planetary_params, parent_planets=None):
    """
    Create a window for orbital parameter visualization.
    To be called from palomas_orrery.py
    """
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
    
    object_var = tk.StringVar(value=objects_with_params[0] if objects_with_params else "")
    object_combo = ttk.Combobox(control_frame, textvariable=object_var, 
                                values=objects_with_params, width=25)
    object_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    
    # Display options
    ttk.Label(control_frame, text="Display Options:").grid(row=1, column=0, 
                                                           columnspan=3, padx=5, pady=(15,5))
    
    show_orbit_steps_var = tk.BooleanVar(value=True)
    show_coordinate_frames_var = tk.BooleanVar(value=True)
    show_final_only_var = tk.BooleanVar(value=False)
    
    ttk.Checkbutton(control_frame, text="Show Orbit Transformation Steps", 
                    variable=show_orbit_steps_var).grid(row=2, column=0, 
                                                        columnspan=3, padx=20, pady=2, sticky='w')
    ttk.Checkbutton(control_frame, text="Show Coordinate Frames", 
                    variable=show_coordinate_frames_var).grid(row=3, column=0, 
                                                             columnspan=3, padx=20, pady=2, sticky='w')
    ttk.Checkbutton(control_frame, text="Show Final Orbit Only (Simplified)", 
                    variable=show_final_only_var).grid(row=4, column=0, 
                                                       columnspan=3, padx=20, pady=2, sticky='w')
    
    # Add separator
    ttk.Separator(control_frame, orient='horizontal').grid(row=5, column=0, 
                                                          columnspan=3, sticky='ew', pady=10)
    
    # Orbital parameters display
    param_frame = ttk.LabelFrame(control_frame, text="Orbital Elements")
    param_frame.grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
    
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
            
            # Determine the correct boolean values based on the checkboxes
            show_final_only = show_final_only_var.get()
            
            # If "Show Final Only" is checked, it overrides the "Show Steps" option.
            show_steps_val = show_orbit_steps_var.get() and not show_final_only
            show_axes_val = show_coordinate_frames_var.get()

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
                parent_planets=parent_planets # Add this argument
            )
            
        #    if fig:
            if fig.data:    
                # Show in browser
                # Generate a descriptive default filename for the plot
                current_date_str = dt.datetime.now().strftime('%Y%m%d')
                default_name = f"Orbital_Transformation_{selected_obj.replace(' ', '_')}_{current_date_str}"

                # Use the existing safe showing/saving function from the main application
                show_figure_safely(fig, default_name)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")
    
    create_button = ttk.Button(control_frame, text="Create Visualization", 
                              command=create_visualization)
    create_button.grid(row=7, column=0, columnspan=3, pady=20, padx=5)
    
    # Information text
    info_frame = ttk.LabelFrame(main_frame, text="Understanding the Visualization")
    info_frame.pack(side='right', fill='both', expand=True)
    
    info_text = tk.Text(info_frame, wrap='word', width=60, height=35)
    info_text.pack(fill='both', expand=True, padx=5, pady=5)
    
    info_content = """ORBITAL PARAMETER TRANSFORMATION VISUALIZATION

This tool demonstrates how Keplerian orbital elements transform an orbit from its natural coordinate system (perifocal frame) to the standard ecliptic reference frame used in astronomy.

KEY CONCEPTS:

Coordinate Frames:
• Perifocal Frame (Blue): The orbit's natural coordinate system
  - X-axis points to periapsis (closest approach)
  - Orbit lies in XY plane
  - Specific to each individual orbit

• Ecliptic Frame (Gray/Red): The standard reference frame
  - XY plane is Earth's orbital plane
  - X-axis points to vernal equinox (♈)
  - Same for all objects in the solar system

TRANSFORMATION SEQUENCE:

The final orbit is placed by applying three rotations to the initial perifocal orbit: R = Rz(Ω) ⋅ Rx(i) ⋅ Rz(ω).

1. Rotate by ω (Argument of Periapsis):
   - Orients the periapsis within the orbital plane.

2. Rotate by i (Inclination):
   - Tilts the orbital plane relative to the ecliptic plane.

3. Rotate by Ω (Longitude of Ascending Node):
   - Rotates the tilted orbit to its final position in the ecliptic frame.  

IMPORTANT: The coordinate systems rotate, not the orbit itself! The orbit maintains its shape and orientation relative to each coordinate frame.

VISUAL ELEMENTS:

• Coordinate Axes: Shows each reference frame
• Orbital Curves: Shows orbit at each transformation stage
• Periapsis: Closest point from the central object (Sun: perihelion, Earth: perigee)
• Apoapsis: Farthest point from the central object (a, semi-major axis)
• Line of Nodes: Where orbit crosses reference plane
• Ascending Node: Where orbit goes above reference plane

INTERACTIVE FEATURES:

• Rotate: Click and drag to view from any angle
• Zoom: Scroll to zoom in/out
• Toggle: Click legend items to show/hide elements
• Hover: Get details about each element

NOTE ON SATELLITE ORBITS:
This visualization shows a simplified Keplerian orbit. Real-world satellite orbits (like the Moon's) are more complex and are affected by:
- The parent planet's equatorial bulge (oblateness).
- Gravitational pull from the Sun.
- Perturbations from other nearby moons.

For full accuracy, more advanced models are needed to account for these effects, such as the additional transformations found in idealized_orbits.py, and implemented in the main GUI plots.

This visualization helps understand how the abstract orbital parameters (a, e, i, ω, Ω) define the actual 3D path of celestial objects."""
    
    info_text.insert('1.0', info_content)
    info_text.config(state='disabled')  # Make read-only
    
    return viz_window

# For backward compatibility with existing code
def create_orbital_transformation_viz_legacy(fig, obj_name, planetary_params, **kwargs):
    """Legacy function for compatibility"""
    new_fig = create_orbital_transformation_viz(obj_name, planetary_params, **kwargs)
    return new_fig if new_fig else fig