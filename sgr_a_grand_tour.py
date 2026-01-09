"""
sgr_a_grand_tour.py
Stage 4 FINAL: The Grand Tour of the Galactic Center

Features:
- Mode switch: Orbital Dynamics (Keplerian) vs Einstein's Laboratory (Relativistic)
- Unified Time Spectrum: Single 'Plasma' colorscale for apples-to-apples comparison
- Observationally Faithful: Phase offsets calculated from real periapsis times
- The "Fantastic Four": S2, S62, S4711, S4714
- Jump to Event: Zoom to periapsis regions
- Single portable HTML output

Orbital positions verified against:
- GRAVITY Collaboration (2018, 2019, 2020)
- Gillessen et al. (2017)
- Peissker et al. (2020)

Collaboration: Tony + Claude Opus 4.5 + Gemini 3 Pro
Part of Paloma's Orrery - Data Preservation is Climate Action
"""

import numpy as np
import plotly.graph_objects as go

# Import our modules
import sgr_a_star_data as data
from sgr_a_star_data import get_star_color, get_orbit_color, create_star_hover_text  # Temperature-based colors
import sgr_a_visualization_core as core
from save_utils import show_and_save

# =============================================================================
# ACCURACY PATCH (S4714)
# =============================================================================
# Adjusting semi-major axis to match literature velocity (~8% c at periapsis)
# This gives periapsis = 12 AU (matching Peissker et al. 2020)
data.S_STAR_CATALOG['S4714']['a_au'] = 800.0

# =============================================================================
# CONFIGURATION
# =============================================================================

STARS_TO_SHOW = ['S2', 'S62', 'S4711', 'S4714']

# Performance tuning
ANIMATION_FRAMES = 140       # Frames per orbit cycle
POINTS_PER_ORBIT = 80        # Resolution of rosette traces

# UNIFIED COLOR SPECTRUM
# All rosette traces use the same colorscale for apples-to-apples comparison
# Plasma: Dark Purple (Past/Now) -> Bright Yellow (Far Future)
UNIFIED_ROSETTE_COLORSCALE = 'Plasma'

# Rosette orbit counts (tuned per star's precession rate)
ROSETTE_ORBIT_COUNTS = {
    'S2': 80,       # 0.2 deg/orbit - needs many orbits to see the pattern
    'S62': 50,      # 1.3 deg/orbit - medium precession
    'S4711': 60,    # 0.2 deg/orbit - similar to S2
    'S4714': 40,    # 1.9 deg/orbit - fast precession, dramatic spiral
}

# Reference year for orbital positions (use current year)
REFERENCE_YEAR = 2025.0

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def generate_rosette_trace(star_name, num_orbits, points_per_orbit=80):
    """
    Generate the relativistic spirograph trace for a star.
    
    The trace shows how the orbit precesses over many cycles,
    creating Einstein's "rosette" pattern.
    """
    star = data.get_star_data(star_name)
    
    # Calculate Schwarzschild precession rate
    precession_deg_per_orbit = data.calculate_schwarzschild_precession_per_orbit(
        star['a_au'], star['e']
    )
    
    all_x, all_y, all_z = [], [], []
    time_fractions = []
    
    for n in range(num_orbits):
        # Each orbit is shifted by accumulated precession
        accumulated_precession = n * precession_deg_per_orbit
        
        x, y, z = core.generate_orbit_points(
            star,
            num_points=points_per_orbit,
            precession_offset_deg=accumulated_precession
        )
        
        all_x.extend(x)
        all_y.extend(y)
        all_z.extend(z)
        
        # Normalize time 0.0 (now) -> 1.0 (far future)
        time_fractions.extend([n / num_orbits] * len(x))
    
    total_precession = precession_deg_per_orbit * num_orbits
    time_span_years = num_orbits * star['period_yrs']
    
    return (np.array(all_x), np.array(all_y), np.array(all_z),
            np.array(time_fractions), precession_deg_per_orbit, 
            total_precession, time_span_years)

def get_phase_offset(star_data, reference_year=REFERENCE_YEAR):
    """
    Calculate orbital phase offset from observed periapsis times.
    
    This ensures the animation shows stars at their ACTUAL positions
    based on real astronomical observations, not arbitrary phases.
    
    The t_periapsis values come from:
    - S2: GRAVITY Collaboration (2018.38 periapsis observed)
    - S62: Peissker et al. (2003.33)
    - S4711, S4714: Peissker et al. (2020)
    """
    dt = reference_year - star_data['t_periapsis']
    orbit_fraction = (dt % star_data['period_yrs']) / star_data['period_yrs']
    return orbit_fraction * 2 * np.pi

def get_current_position_info(star_name, reference_year=REFERENCE_YEAR):
    """Get descriptive info about a star's current orbital position."""
    star = data.get_star_data(star_name)
    
    dt = reference_year - star['t_periapsis']
    orbit_fraction = (dt % star['period_yrs']) / star['period_yrs']
    
    # Calculate actual position
    M = orbit_fraction * 2 * np.pi
    E = data.solve_kepler_equation(M, star['e'])
    nu = data.eccentric_to_true_anomaly(E, star['e'])
    r = data.radius_from_true_anomaly(star['a_au'], star['e'], nu)
    v = data.calculate_orbital_velocity(star['a_au'], r)
    
    # Position description
    if orbit_fraction < 0.1 or orbit_fraction > 0.9:
        position = "near periapsis"
    elif 0.4 < orbit_fraction < 0.6:
        position = "near apoapsis"
    elif orbit_fraction < 0.5:
        position = "outbound"
    else:
        position = "inbound"
    
    return {
        'distance': r,
        'velocity': v,
        'position': position,
        'orbit_fraction': orbit_fraction
    }

# =============================================================================
# DASHBOARD ASSEMBLY
# =============================================================================

def create_grand_tour_dashboard():
    """
    Build the complete Grand Tour dashboard with unified color spectrum
    and observationally faithful orbital positions.
    """
    print("=" * 70)
    print("ASSEMBLING THE GRAND TOUR (FINAL - UNIFIED SPECTRUM EDITION)")
    print("=" * 70)
    print(f"Reference year: {REFERENCE_YEAR}")
    print(f"Featuring: {', '.join(STARS_TO_SHOW)}")
    print()
    
    # Report current positions
    print("Current orbital positions (observationally derived):")
    for star_name in STARS_TO_SHOW:
        info = get_current_position_info(star_name)
        print(f"  {star_name}: {info['distance']:.0f} AU, {info['position']}, {data.format_velocity(info['velocity'])}")
    print()
    
    fig = go.Figure()
    
    # Registry for visibility toggling
    trace_registry = {
        'sgr_a': [],        # Always visible
        'dynamics': [],     # View 1: Animation mode
        'relativity': []    # View 2: Rosette mode
    }
    
    current_idx = 0
    
    # =========================================================================
    # 1. SGR A* (The Monster at the Center)
    # =========================================================================
    print("Adding Sgr A*...")
    sgr_a_traces = core.create_sgr_a_marker(scale_factor=40)
    for trace in sgr_a_traces:
        fig.add_trace(trace)
        trace_registry['sgr_a'].append(current_idx)
        current_idx += 1
    
    # =========================================================================
    # 2. VIEW 1: ORBITAL DYNAMICS (Keplerian Animation)
    # =========================================================================
    print("Building Dynamics View...")
    
    for star_name in STARS_TO_SHOW:
        star = data.get_star_data(star_name)
        star_color = get_star_color(star)    # Temperature-based color for star marker
        orbit_color = get_orbit_color(star)  # Distinct color for orbit trace and label
        
        # A. Static orbit ellipse (use orbit_color for readability)
        x_orbit, y_orbit, z_orbit = core.generate_orbit_points(star)
        fig.add_trace(go.Scatter3d(
            x=x_orbit, y=y_orbit, z=z_orbit,
            mode='lines',
            line=dict(color=orbit_color, width=2),
            name=f"{star_name} Orbit",
            visible=True,
            hoverinfo='name'
        ))
        trace_registry['dynamics'].append(current_idx)
        current_idx += 1
        
        # B. Star marker at current position (from observations)
        phase = get_phase_offset(star)
        E = data.solve_kepler_equation(phase, star['e'])
        nu = data.eccentric_to_true_anomaly(E, star['e'])
        x_pos, y_pos, z_pos, r = core.generate_position_at_true_anomaly(star, nu)
        v = data.calculate_orbital_velocity(star['a_au'], r)
        
        # Create rich hover text (like exoplanet host stars)
        hover_text = create_star_hover_text(star_name, star, r, v)
        
        fig.add_trace(go.Scatter3d(
            x=[x_pos], y=[y_pos], z=[z_pos],
            mode='markers+text',
            marker=dict(
                size=10,
                color=star_color,  # Temperature-based color for star
                line=dict(color='white', width=2)
            ),
            text=[star_name],
            textposition='top center',
            textfont=dict(size=10, color=orbit_color),  # Label uses orbit color for readability
            name=star_name,
            visible=True,
            hovertext=[hover_text],
            hoverinfo='text'
        ))
        trace_registry['dynamics'].append(current_idx)
        current_idx += 1
    
    # =========================================================================
    # 3. VIEW 2: EINSTEIN'S LABORATORY (Relativistic Rosettes)
    # =========================================================================
    print("Building Relativity View (Unified Spectrum)...")
    
    for star_name in STARS_TO_SHOW:
        star = data.get_star_data(star_name)
        n_orbits = ROSETTE_ORBIT_COUNTS.get(star_name, 40)
        
        print(f"  {star_name}: {n_orbits} orbits...")
        x, y, z, t_vals, rate, total, time_span = generate_rosette_trace(
            star_name, n_orbits, POINTS_PER_ORBIT
        )
        
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(
                width=3,
                color=t_vals,
                colorscale=UNIFIED_ROSETTE_COLORSCALE,
                showscale=False
            ),
            name=f"{star_name} ({rate:.2f} deg/orbit)",
            visible=False,  # Hidden by default
            hovertemplate=(
                f"<b>{star['name']} - Relativistic Rosette</b><br><br>"
                f"<b>Schwarzschild Precession:</b><br>"
                f"Orbits never close due to General Relativity.<br>"
                f"Spacetime curvature near the black hole shifts<br>"
                f"periapsis forward each orbit.<br><br>"
                f"<b>What determines precession rate:</b><br>"
                f"- Black hole mass (more mass = more curvature)<br>"
                f"- How close the orbit gets (1/a dependence)<br>"
                f"- Eccentricity (elongated orbits dip closer)<br><br>"
                f"<b>This star:</b><br>"
                f"Precession rate: {rate:.3f} deg/orbit<br>"
                f"Total shown: {total:.1f} deg over {time_span:.0f} years<br><br>"
                f"<b>Color:</b> Purple (now) to Yellow (future)<br>"
                f"<extra></extra>"
            )
        ))
        trace_registry['relativity'].append(current_idx)
        current_idx += 1
    
    total_traces = current_idx
    
    # =========================================================================
    # 4. ANIMATION FRAMES (The "Whoosh")
    # =========================================================================
    print(f"Generating {ANIMATION_FRAMES} animation frames...")
    
    frames = []
    mean_anomalies = np.linspace(0, 2*np.pi, ANIMATION_FRAMES, endpoint=False)
    
    # Identify marker trace indices (every 2nd trace in dynamics group)
    marker_indices = [trace_registry['dynamics'][i] 
                      for i in range(1, len(trace_registry['dynamics']), 2)]
    
    for k, M_base in enumerate(mean_anomalies):
        frame_data = []
        
        for star_name in STARS_TO_SHOW:
            star = data.get_star_data(star_name)
            
            # Apply observationally-derived phase offset
            phase = get_phase_offset(star)
            M = (M_base + phase) % (2 * np.pi)
            
            # Solve Kepler's equation
            E = data.solve_kepler_equation(M, star['e'])
            nu = data.eccentric_to_true_anomaly(E, star['e'])
            
            # Get position and velocity
            x, y, z, r = core.generate_position_at_true_anomaly(star, nu)
            v = data.calculate_orbital_velocity(star['a_au'], r)
            
            # Temperature-based color for star marker, orbit color for label
            star_color = get_star_color(star)
            orbit_color = get_orbit_color(star)
            
            # Rich hover text (like exoplanet host stars)
            hover_text = create_star_hover_text(star_name, star, r, v)
            
            frame_data.append(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers+text',
                marker=dict(
                    size=10,
                    color=star_color,
                    line=dict(color='white', width=2)
                ),
                text=[star_name],
                textposition='top center',
                textfont=dict(size=10, color=orbit_color),
                hovertext=[hover_text],
                hoverinfo='text'
            ))
        
        frames.append(go.Frame(
            data=frame_data,
            traces=marker_indices,
            name=f"fr{k}"
        ))
    
    fig.frames = frames
    
    # =========================================================================
    # 4b. SPECIAL PERIAPSIS FRAMES (for zoom menu)
    # =========================================================================
    # Create a frame showing each star at its periapsis position
    # Other stars shown at their relative positions at that moment
    
    print("Generating special periapsis frames...")
    
    periapsis_frames = {}
    
    for target_star in STARS_TO_SHOW:
        target_data = data.get_star_data(target_star)
        
        # Calculate M_base needed to put target star at periapsis (M=0 for target)
        # Since M = M_base + phase_offset, we need M_base = -phase_offset
        target_phase = get_phase_offset(target_data)
        M_base_for_periapsis = (2 * np.pi - target_phase) % (2 * np.pi)
        
        frame_data = []
        
        for star_name in STARS_TO_SHOW:
            star = data.get_star_data(star_name)
            
            # Apply phase offset
            phase = get_phase_offset(star)
            M = (M_base_for_periapsis + phase) % (2 * np.pi)
            
            # Solve Kepler's equation
            E = data.solve_kepler_equation(M, star['e'])
            nu = data.eccentric_to_true_anomaly(E, star['e'])
            
            # Get position and velocity
            x, y, z, r = core.generate_position_at_true_anomaly(star, nu)
            v = data.calculate_orbital_velocity(star['a_au'], r)
            
            # Temperature-based color for star marker, orbit color for label
            star_color = get_star_color(star)
            orbit_color = get_orbit_color(star)
            
            # Rich hover text
            hover_text = create_star_hover_text(star_name, star, r, v)
            
            frame_data.append(go.Scatter3d(
                x=[x], y=[y], z=[z],
                mode='markers+text',
                marker=dict(
                    size=10,
                    color=star_color,
                    line=dict(color='white', width=2)
                ),
                text=[star_name],
                textposition='top center',
                textfont=dict(size=10, color=orbit_color),
                hovertext=[hover_text],
                hoverinfo='text'
            ))
        
        frame_name = f"peri_{target_star}"
        periapsis_frames[target_star] = frame_name
        
        frames.append(go.Frame(
            data=frame_data,
            traces=marker_indices,
            name=frame_name
        ))
        
        # Calculate periapsis distance and velocity for this star
        peri_dist = data.calculate_periapsis_au(target_data['a_au'], target_data['e'])
        peri_vel = data.calculate_periapsis_velocity(target_data['a_au'], target_data['e'])
        print(f"  {target_star}: periapsis frame '{frame_name}' - {peri_dist:.1f} AU, {data.format_velocity(peri_vel)}")
    
    # Update frames with periapsis frames added
    fig.frames = frames
    
    # =========================================================================
    # 5. VISIBILITY ARRAYS FOR MODE SWITCHING
    # =========================================================================
    
    def get_visibility_array(mode):
        """Generate visibility array for a given view mode."""
        vis = [False] * total_traces
        # Always show Sgr A*
        for i in trace_registry['sgr_a']:
            vis[i] = True
        # Show mode-specific traces
        for i in trace_registry[mode]:
            vis[i] = True
        return vis
    
    # =========================================================================
    # 6. UI CONTROLS
    # =========================================================================
    
    updatemenus = [
        # VIEW SWITCHER (Top-left dropdown)
        dict(
            type="dropdown",
            direction="down",
            x=0.01,
            y=0.99,
            xanchor="left",
            yanchor="top",
            bgcolor='rgba(20,20,40,0.9)',
            bordercolor='#FFD700',
            borderwidth=1,
            font=dict(color='white', size=11),
            showactive=False,  # Disable white highlight on active selection
            buttons=[
                dict(
                    label="View: Orbital Dynamics (Animation)",
                    method="update",
                    args=[
                        {"visible": get_visibility_array('dynamics')},
                        {"title": dict(
                            text="<b>Galactic Center: Orbital Dynamics</b><br>"
                                 "<sup>Keplerian Motion - Watch the 'whoosh' at periapsis!</sup>",
                            x=0.5
                        )}
                    ]
                ),
                dict(
                    label="View: Einstein's Laboratory (Rosette)",
                    method="update",
                    args=[
                        {"visible": get_visibility_array('relativity')},
                        {"title": dict(
                            text="<b>Galactic Center: Einstein's Laboratory</b><br>"
                                 "<sup>Schwarzschild Precession - Unified Time Spectrum</sup>",
                            x=0.5
                        )}
                    ]
                )
            ]
        ),
        
        # ANIMATION CONTROLS (Bottom center)
        dict(
            type="buttons",
            direction="left",
            x=0.5,
            y=-0.08,
            xanchor="center",
            bgcolor='rgba(20,20,40,0.9)',
            bordercolor='#FFD700',
            borderwidth=1,
            font=dict(color='white'),
            showactive=False,  # Disable white highlight on active selection
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[
                        None,
                        dict(
                            frame=dict(duration=20, redraw=True),
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
                            frame=dict(duration=0, redraw=True),
                            mode="immediate"
                        )
                    ]
                )
            ]
        ),
        
        # JUMP TO EVENT (Bottom-right dropdown)
        dict(
            type="dropdown",
            direction="up",
            x=0.99,
            y=-0.08,
            xanchor="right",
            bgcolor='rgba(50,20,20,0.9)',
            bordercolor='#FFD700',
            borderwidth=1,
            font=dict(color='white', size=10),
            showactive=False,  # Disable white highlight on active selection
            buttons=[
                dict(
                    label="Zoom to Region...",
                    method="skip",
                    args=["None"]
                ),
                dict(
                    label="Sgr A* Black Hole (4x zoom)",
                    method="relayout",
                    args=[{
                        "scene.camera.eye": dict(x=0.3125, y=0.3125, z=0.3125),
                        "scene.xaxis.range": [-100, 100],
                        "scene.yaxis.range": [-100, 100],
                        "scene.zaxis.range": [-100, 100]
                    }]
                ),
                dict(
                    label="S4714 at Periapsis (12 AU, 8% c)",
                    method="animate",
                    args=[
                        ["peri_S4714"],
                        {
                            "mode": "immediate",
                            "frame": {"duration": 0, "redraw": True},
                            "transition": {"duration": 0}
                        }
                    ]
                ),
                dict(
                    label="S62 at Periapsis (18 AU, 6.7% c)",
                    method="animate",
                    args=[
                        ["peri_S62"],
                        {
                            "mode": "immediate",
                            "frame": {"duration": 0, "redraw": True},
                            "transition": {"duration": 0}
                        }
                    ]
                ),
                dict(
                    label="S2 at Periapsis (120 AU, 2.5% c)",
                    method="animate",
                    args=[
                        ["peri_S2"],
                        {
                            "mode": "immediate",
                            "frame": {"duration": 0, "redraw": True},
                            "transition": {"duration": 0}
                        }
                    ]
                ),
                dict(
                    label="S4711 at Periapsis (133 AU, 4.5% c)",
                    method="animate",
                    args=[
                        ["peri_S4711"],
                        {
                            "mode": "immediate",
                            "frame": {"duration": 0, "redraw": True},
                            "transition": {"duration": 0}
                        }
                    ]
                ),
                dict(
                    label="Zoom: +/-50 AU (S4714, S62)",
                    method="relayout",
                    args=[{
                        "scene.camera.eye": dict(x=1.25, y=1.25, z=1.25),
                        "scene.xaxis.range": [-50, 50],
                        "scene.yaxis.range": [-50, 50],
                        "scene.zaxis.range": [-50, 50]
                    }]
                ),
                dict(
                    label="Zoom: +/-100 AU (S2)",
                    method="relayout",
                    args=[{
                        "scene.camera.eye": dict(x=1.25, y=1.25, z=1.25),
                        "scene.xaxis.range": [-100, 100],
                        "scene.yaxis.range": [-100, 100],
                        "scene.zaxis.range": [-100, 100]
                    }]
                ),
                dict(
                    label="Zoom: +/-150 AU (S4711)",
                    method="relayout",
                    args=[{
                        "scene.camera.eye": dict(x=1.25, y=1.25, z=1.25),
                        "scene.xaxis.range": [-150, 150],
                        "scene.yaxis.range": [-150, 150],
                        "scene.zaxis.range": [-150, 150]
                    }]
                ),
                dict(
                    label="Full System View",
                    method="relayout",
                    args=[{
                        "scene.camera.eye": dict(x=1.25, y=1.25, z=1.25),
                        "scene.xaxis.autorange": True,
                        "scene.yaxis.autorange": True,
                        "scene.zaxis.autorange": True
                    }]
                )
            ]
        )
    ]
    
    # Animation slider
    sliders = [dict(
        active=0,
        yanchor="top",
        y=-0.12,
        xanchor="left",
        x=0.1,
        len=0.8,
        pad=dict(b=10, t=30),
        bgcolor='rgba(30,30,50,0.5)',
        font=dict(color='white', size=9),
        currentvalue=dict(
            font=dict(size=11, color='white'),
            prefix="Orbital Phase: ",
            suffix=" deg",
            visible=True,
            xanchor="center"
        ),
        steps=[
            dict(
                method='animate',
                args=[
                    [f'fr{k}'],
                    dict(
                        mode='immediate',
                        frame=dict(duration=0, redraw=True),
                        transition=dict(duration=0)
                    )
                ],
                label=f'{int(k * 360 / ANIMATION_FRAMES)}'
            )
            for k in range(ANIMATION_FRAMES)
        ]
    )]
    
    # =========================================================================
    # 7. LAYOUT
    # =========================================================================
    
    # Calculate axis range
    max_range = 0
    for star_name in STARS_TO_SHOW:
        star = data.get_star_data(star_name)
        apoapsis = data.calculate_apoapsis_au(star['a_au'], star['e'])
        max_range = max(max_range, apoapsis)
    axis_range = max_range * 1.1
    
    fig.update_layout(
        title=dict(
            text="<b>Galactic Center: Grand Tour</b><br>"
                 "<sup>S-Stars Orbiting Sagittarius A* - Positions as of 2025</sup>",
            x=0.5,
            font=dict(size=16, color='white')
        ),
        scene=dict(
            xaxis=dict(
                title='X (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(8,8,18)',
                gridcolor='rgb(35,35,55)',
                showbackground=True
            ),
            yaxis=dict(
                title='Y (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(8,8,18)',
                gridcolor='rgb(35,35,55)',
                showbackground=True
            ),
            zaxis=dict(
                title='Z (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(8,8,18)',
                gridcolor='rgb(35,35,55)',
                showbackground=True
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.2, y=1.2, z=0.6)
            )
        ),
        paper_bgcolor='rgb(8,8,18)',
        plot_bgcolor='rgb(8,8,18)',
        font=dict(color='white'),
        legend=dict(
            yanchor="top",
            y=0.85,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0,0,0,0.6)',
            font=dict(size=10)
        ),
        margin=dict(l=0, r=0, t=80, b=130),
        updatemenus=updatemenus,
        sliders=sliders,
        # Start with animation paused
        transition=dict(duration=0),
    )
    
    # Explicitly set to first frame without playing
    fig.update(frames=fig.frames)
    
    # Annotations - Note: "Unified Time Spectrum" only applies to Einstein's Laboratory view
    # so we don't add it as a global annotation (it's shown in the view title instead)
    
    # Top annotation - what we're showing
    fig.add_annotation(
        text="Four representative S-stars from the ~50 known stars with measured orbits around Sgr A*",
        xref="paper", yref="paper",
        x=0.5, y=0.92,
        showarrow=False,
        font=dict(size=10, color='white'),
        opacity=0.9
    )
    
    # Animation explanation (left side, white text)
    fig.add_annotation(
        text="Animation cycles orbits by phase angle (asynchronous) | Each star completes one orbit per cycle<br>"
            "Actual positions in time shown for 2025 and for periapsis (Zoom menu)<br>"
            "About 50 S-stars have measured orbits | Stars shown here are in stable orbits<br>"
             "Toggle off 'Sgr A* (Black Hole)' to see actual-scale object illustrated as a \"red\" sphere<br>"
             "Data: GRAVITY Collaboration, Peissker et al. | Visualization: Paloma's Orrery"        ,
        xref="paper", yref="paper",
        x=0.01, y=-0.2,
        xanchor="left",
        showarrow=False,
        font=dict(size=9, color='white'),
        align="left"
    )
    
    # Source attribution and S-star context (left side, white text)
    # Positioned higher to avoid being covered by slider
#    fig.add_annotation(
#        text="~50 S-stars have measured orbits; all shown here are in stable orbits | "
#             "Toggle off 'Sgr A* (Black Hole)' to see actual-scale red sphere<br>"
#             "Data: GRAVITY Collaboration, Peissker et al. | Visualization: Paloma's Orrery",
#        xref="paper", yref="paper",
#        x=0.01, y=-0.15,
#        xanchor="left",
#        showarrow=False,
#        font=dict(size=8, color='white'),
#        align="left"
#    )
    
    print("\nDashboard assembly complete!")
    return fig

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print()
    print("*" * 70)
    print("*  PALOMA'S ORRERY - GALACTIC CENTER GRAND TOUR (FINAL)            *")
    print("*  S-Stars Orbiting Sagittarius A*                                  *")
    print("*  Observationally Faithful | Unified Time Spectrum                 *")
    print("*" * 70)
    print()
    
    # Verify S4714 patch
    s4714 = data.get_star_data('S4714')
    peri = data.calculate_periapsis_au(s4714['a_au'], s4714['e'])
    v_peri = data.calculate_periapsis_velocity(s4714['a_au'], s4714['e'])
    print(f"S4714 verification: periapsis = {peri:.1f} AU, velocity = {data.format_velocity(v_peri)}")
    print()
        
    # Build dashboard
    fig = create_grand_tour_dashboard()
    
    # Show and offer save dialog
    show_and_save(fig, "sgr_a_grand_tour")
    
    print()
    print("=" * 70)
    print("GRAND TOUR COMPLETE")
    print("=" * 70)
    print()
    print("Features:")
    print("  - Dropdown: Switch between Dynamics and Relativity views")
    print("  - Play/Pause: Animate the orbital motion")
    print("  - Zoom dropdown: Jump to periapsis regions")
    print("  - Unified Plasma colorscale: Compare precession rates visually")
    print("  - Observational fidelity: Phases from real periapsis measurements")
    print()
    print("What to watch:")
    print("  - In 2025, all stars are near apoapsis (slow phase)")
    print("  - S4714 is inbound - next periapsis ~2029!")
    print("  - In Rosette view: S4714's dramatic spiral vs S2's subtle fan")
    print()
