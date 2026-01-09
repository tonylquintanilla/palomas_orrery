"""
sgr_a_visualization_animation.py
Stage 2: Animated visualization of S-Stars orbiting Sagittarius A*.

The "Time Dilation Trick": We step by Mean Anomaly (angle), not time.
This automatically creates the "whoosh" effect - stars speed up at periapsis
and slow down at apoapsis, exactly as Kepler's Second Law dictates.

Collaboration: Tony + Claude Opus 4.5 + Gemini 3 Pro
Part of Paloma's Orrery - Data Preservation is Climate Action
"""

import numpy as np
import plotly.graph_objects as go
import sgr_a_star_data as data
from sgr_a_star_data import get_star_color, get_orbit_color  # Temperature-based colors
import sgr_a_visualization_core as core
from save_utils import show_and_save

# =============================================================================
# ANIMATION CONFIGURATION
# =============================================================================

ANIMATION_CONFIG = {
    'num_frames': 180,           # Frames per orbit cycle (2 deg per frame)
    'frame_duration_ms': 30,     # Milliseconds per frame (lower = faster)
    'star_marker_size': 10,      # Size of moving star markers
    'show_velocity_trace': True, # Show brief trailing "comet tail"
    'trail_length': 5,           # Number of trailing positions
}

# =============================================================================
# ANIMATION HELPERS
# =============================================================================

def calculate_star_position_at_mean_anomaly(star_data, mean_anomaly_rad):
    """
    Given a mean anomaly M, calculate the star's 3D position and velocity.
    
    Returns:
        x, y, z: Position in AU
        r: Distance from Sgr A* in AU  
        v: Velocity in km/s
    """
    # Solve Kepler's equation: M -> E (Eccentric Anomaly)
    E = data.solve_kepler_equation(mean_anomaly_rad, star_data['e'])
    
    # Convert E -> nu (True Anomaly)
    nu = data.eccentric_to_true_anomaly(E, star_data['e'])
    
    # Get 3D position
    x, y, z, r = core.generate_position_at_true_anomaly(star_data, nu)
    
    # Calculate velocity at this distance
    v = data.calculate_orbital_velocity(star_data['a_au'], r)
    
    return x, y, z, r, v, nu

def get_phase_offset(star_data, reference_year=2024.0):
    """
    Calculate phase offset so stars start at their actual orbital positions
    relative to a reference year.
    
    This prevents all stars from hitting periapsis at the same animation frame.
    """
    # Time since periapsis
    dt = reference_year - star_data['t_periapsis']
    
    # Fraction of orbit completed
    orbit_fraction = (dt % star_data['period_yrs']) / star_data['period_yrs']
    
    # Convert to radians
    return orbit_fraction * 2 * np.pi

def format_velocity_display(v_km_s):
    """Format velocity for display in animation."""
    percent_c = (v_km_s / data.SPEED_OF_LIGHT_KM_S) * 100
    if percent_c >= 1.0:
        return f"{v_km_s:,.0f} km/s ({percent_c:.1f}% c)"
    else:
        return f"{v_km_s:,.0f} km/s"

# =============================================================================
# MAIN ANIMATION FUNCTION
# =============================================================================

def create_animation(stars_to_show=None, reference_year=2024.0):
    """
    Create animated visualization of S-stars orbiting Sgr A*.
    
    Args:
        stars_to_show: List of star names. Default: all four main stars.
        reference_year: Year for initial orbital positions.
    
    Returns:
        Plotly Figure with animation frames.
    """
    print("Initializing S-Star Animation...")
    
    if stars_to_show is None:
        stars_to_show = ['S2', 'S62', 'S4711', 'S4714']
    
    num_frames = ANIMATION_CONFIG['num_frames']
    frame_duration = ANIMATION_CONFIG['frame_duration_ms']
    marker_size = ANIMATION_CONFIG['star_marker_size']
    
    # =========================================================================
    # 1. CREATE BASE FIGURE (Static Elements)
    # =========================================================================
    
    # Start fresh - we'll build our own traces
    traces = []
    
    # Add Sgr A* (black hole marker)
    traces.extend(core.create_sgr_a_marker())
    
    # Add static orbit paths (no current position markers - animation will handle those)
    for star_name in stars_to_show:
        star_data = data.get_star_data(star_name)
        if star_data:
            # Get orbit color for trace (distinct from star marker)
            orbit_color = get_orbit_color(star_data)
            
            # Generate orbit path
            x_orbit, y_orbit, z_orbit = core.generate_orbit_points(star_data)
            
            # Add orbit trace
            traces.append(go.Scatter3d(
                x=x_orbit, y=y_orbit, z=z_orbit,
                mode='lines',
                line=dict(color=orbit_color, width=2, dash='solid'),
                name=star_data['name'],
                hoverinfo='name',
                opacity=0.6
            ))
    
    # Add placeholder traces for moving star markers (one per star)
    # These will be updated by animation frames
    star_marker_start_index = len(traces)
    
    for star_name in stars_to_show:
        star_data = data.get_star_data(star_name)
        star_color = get_star_color(star_data)    # Temperature-based for marker
        orbit_color = get_orbit_color(star_data)  # Distinct for label
        phase_offset = get_phase_offset(star_data, reference_year)
        x, y, z, r, v, nu = calculate_star_position_at_mean_anomaly(star_data, phase_offset)
        
        traces.append(go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='markers+text',
            marker=dict(
                size=marker_size,
                color=star_color,
                line=dict(color='white', width=2),
                symbol='circle'
            ),
            text=[star_name],
            textposition='top center',
            textfont=dict(size=10, color=orbit_color),
            name=f"{star_name} (moving)",
            hovertemplate=(
                f"<b>{star_data['name']}</b><br>"
                f"Distance: {r:.1f} AU<br>"
                f"Velocity: {format_velocity_display(v)}<br>"
                "<extra></extra>"
            ),
            showlegend=False
        ))
    
    # =========================================================================
    # 2. GENERATE ANIMATION FRAMES
    # =========================================================================
    
    print(f"Generating {num_frames} frames for {len(stars_to_show)} stars...")
    
    # Mean anomaly steps (0 to 2*pi)
    mean_anomalies = np.linspace(0, 2*np.pi, num_frames, endpoint=False)
    
    frames = []
    
    for k, M_base in enumerate(mean_anomalies):
        frame_traces = []
        
        for i, star_name in enumerate(stars_to_show):
            star_data = data.get_star_data(star_name)
            
            # Apply phase offset so stars are at correct relative positions
            phase_offset = get_phase_offset(star_data, reference_year)
            M = (M_base + phase_offset) % (2 * np.pi)
            
            # Calculate position
            x, y, z, r, v, nu = calculate_star_position_at_mean_anomaly(star_data, M)
            
            # Get temperature-based color for marker, orbit color for label
            star_color = get_star_color(star_data)
            orbit_color = get_orbit_color(star_data)
            
            # Create marker trace for this frame
            frame_traces.append(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers+text',
                marker=dict(
                    size=marker_size,
                    color=star_color,
                    line=dict(color='white', width=2)
                ),
                text=[star_name],
                textposition='top center',
                textfont=dict(size=10, color=orbit_color),
                hovertemplate=(
                    f"<b>{star_data['name']}</b><br>"
                    f"Distance: {r:.1f} AU<br>"
                    f"Velocity: {format_velocity_display(v)}<br>"
                    "<extra></extra>"
                )
            ))
        
        # Create frame - specify which trace indices to update
        frames.append(go.Frame(
            data=frame_traces,
            traces=list(range(star_marker_start_index, star_marker_start_index + len(stars_to_show))),
            name=f"frame_{k}"
        ))
    
    # =========================================================================
    # 3. ASSEMBLE FIGURE
    # =========================================================================
    
    # Calculate axis range
    max_range = 0
    for star_name in stars_to_show:
        star_data = data.get_star_data(star_name)
        apoapsis = data.calculate_apoapsis_au(star_data['a_au'], star_data['e'])
        max_range = max(max_range, apoapsis)
    axis_range = max_range * 1.1
    
    fig = go.Figure(data=traces, frames=frames)
    
    # Layout
    fig.update_layout(
        title=dict(
            text="<b>S-Stars Orbiting Sagittarius A*</b><br><sup>Animation: Mean Anomaly Stepping (Kepler's Second Law in Action)</sup>",
            x=0.5,
            font=dict(size=16, color='white')
        ),
        scene=dict(
            xaxis=dict(
                title='X (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(40,40,60)',
                showbackground=True
            ),
            yaxis=dict(
                title='Y (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(40,40,60)',
                showbackground=True
            ),
            zaxis=dict(
                title='Z (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(40,40,60)',
                showbackground=True
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.2, y=1.2, z=0.6)
            )
        ),
        paper_bgcolor='rgb(5,5,15)',
        plot_bgcolor='rgb(5,5,15)',
        font=dict(color='white'),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0,0,0,0.7)',
            font=dict(size=11)
        ),
        margin=dict(l=0, r=0, t=80, b=100),
        
        # Animation controls
        updatemenus=[dict(
            type="buttons",
            showactive=True,
            y=-0.05,
            x=0.5,
            xanchor="center",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[
                        None,
                        dict(
                            frame=dict(duration=frame_duration, redraw=True),
                            fromcurrent=True,
                            mode='immediate',
                            transition=dict(duration=0)
                        )
                    ]
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[
                        [None],
                        dict(
                            frame=dict(duration=0, redraw=False),
                            mode="immediate",
                            transition=dict(duration=0)
                        )
                    ]
                )
            ]
        )],
        
        # Slider for manual scrubbing
        sliders=[dict(
            active=0,
            yanchor="top",
            y=-0.1,
            xanchor="left",
            x=0.1,
            len=0.8,
            pad=dict(b=10, t=50),
            currentvalue=dict(
                font=dict(size=12, color='white'),
                prefix="Orbit Phase: ",
                suffix=" deg",
                visible=True,
                xanchor="center"
            ),
            steps=[
                dict(
                    method='animate',
                    args=[
                        [f'frame_{k}'],
                        dict(
                            mode='immediate',
                            frame=dict(duration=0, redraw=True),
                            transition=dict(duration=0)
                        )
                    ],
                    label=f'{int(k * 360 / num_frames)}'
                )
                for k in range(num_frames)
            ]
        )]
    )
    
    # Add annotation
    fig.add_annotation(
        text="Watch S4714 (red): hangs at apoapsis, then SNAPS through periapsis at 10% light speed!",
        xref="paper", yref="paper",
        x=0.5, y=1.02,
        showarrow=False,
        font=dict(size=11, color='yellow'),
        bgcolor='rgba(0,0,0,0.5)'
    )
    
    print("Animation ready!")
    return fig

# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def create_single_star_animation(star_name, num_orbits=3):
    """
    Create animation focused on a single star, showing multiple orbits
    to demonstrate precession (Stage 3 preview).
    """
    return create_animation(stars_to_show=[star_name])

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("S-STAR ANIMATION - Stage 2")
    print("Kepler's Second Law: Equal Areas in Equal Times")
    print("=" * 60)
    
    # Create the animation
    fig = create_animation()
    
    # Show and offer save dialog
    show_and_save(fig, "sgr_a_visualization_stage2")
    
    print("\nOpen in browser and click 'Play' to watch the stars orbit!")
    print("\nWhat to watch for:")
    print("  - S4714 (red): SNAPS through periapsis, hangs at apoapsis")
    print("  - S62 (light blue): Also highly eccentric, dramatic speed changes")
    print("  - S2 (blue): The famous 16-year orbit, more moderate eccentricity")
    print("  - S4711 (light blue): Shortest period, fastest to complete an orbit")


