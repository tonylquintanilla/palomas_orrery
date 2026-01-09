"""
sgr_a_visualization_precession.py
Stage 3: The Relativistic Rosette (Schwarzschild Precession).

Visualizes the cumulative effect of General Relativity over decades/centuries.
Instead of animating a dot, we trace the future path to reveal the 'Spirograph' pattern.

This is what the GRAVITY Collaboration spent 27 years measuring to prove Einstein right.

Collaboration: Tony + Claude Opus 4.5 + Gemini 3 Pro
Part of Paloma's Orrery - Data Preservation is Climate Action
"""

import numpy as np
import plotly.graph_objects as go
import sgr_a_star_data as data
import sgr_a_visualization_core as core
from save_utils import show_and_save

# =============================================================================
# ACCURACY PATCH - S4714
# =============================================================================
# Issue: Original a=520 AU, e=0.985 gave periapsis ~7.8 AU and velocity 10.2% c
# Fix: Raise semi-major axis to 800 AU to match literature:
#      - Periapsis: ~12 AU (matches Peissker et al. 2020)
#      - Velocity: ~8% c (matches literature value)
#
# We apply this patch at runtime so the original data module stays clean.

S4714_ACCURACY_PATCH = {
    'a_au': 800.0,  # Was 520.0
    # This gives periapsis = 800 * (1 - 0.985) = 12 AU
    # And velocity ~24,000 km/s = 8% c
}

def apply_accuracy_patches():
    """Apply literature-based corrections to orbital elements."""
    # Patch S4714
    for key, value in S4714_ACCURACY_PATCH.items():
        data.S_STAR_CATALOG['S4714'][key] = value
    
    # Verify the patch
    star = data.get_star_data('S4714')
    peri = data.calculate_periapsis_au(star['a_au'], star['e'])
    v_peri = data.calculate_periapsis_velocity(star['a_au'], star['e'])
    print(f"S4714 patched: periapsis = {peri:.1f} AU, velocity = {data.format_velocity(v_peri)}")

# Apply patches on import
apply_accuracy_patches()

# =============================================================================
# ROSETTE GENERATION
# =============================================================================

def generate_rosette_trace(star_name, num_orbits=50, points_per_orbit=120):
    """
    Generate a continuous 3D trace of a precessing orbit over many cycles.
    
    This creates the famous "rosette" or "spirograph" pattern that proves
    General Relativity - the orbit doesn't close on itself, it rotates.
    
    Args:
        star_name: Name of star in catalog
        num_orbits: Number of orbital cycles to trace
        points_per_orbit: Resolution of each orbit
    
    Returns:
        x, y, z: Arrays of coordinates
        time_fraction: Array for color mapping (0 = now, 1 = far future)
        precession_rate: Degrees per orbit
        total_precession: Total rotation over all orbits
    """
    star = data.get_star_data(star_name)
    
    # Calculate precession rate (degrees per orbit)
    precession_deg_per_orbit = data.calculate_schwarzschild_precession_per_orbit(
        star['a_au'], star['e']
    )
    
    total_precession = precession_deg_per_orbit * num_orbits
    
    print(f"Generating rosette for {star['name']}:")
    print(f"  Semi-major axis: {star['a_au']:.0f} AU")
    print(f"  Eccentricity: {star['e']:.4f}")
    print(f"  Precession rate: {precession_deg_per_orbit:.4f} deg/orbit ({precession_deg_per_orbit*60:.1f} arcmin/orbit)")
    print(f"  Simulating {num_orbits} orbits = {total_precession:.1f} deg total rotation")
    print(f"  Time span: {num_orbits * star['period_yrs']:.0f} years")
    
    all_x, all_y, all_z = [], [], []
    time_fractions = []
    
    # Generate each orbit with accumulated precession
    for n in range(num_orbits):
        # Accumulated precession for this orbit
        accumulated_precession = n * precession_deg_per_orbit
        
        # Generate orbit points with this precession offset
        x, y, z = core.generate_orbit_points(
            star,
            num_points=points_per_orbit,
            precession_offset_deg=accumulated_precession
        )
        
        all_x.extend(x)
        all_y.extend(y)
        all_z.extend(z)
        
        # Time fraction for color gradient (0 = start, 1 = end)
        time_fractions.extend([n / num_orbits] * len(x))
    
    return (np.array(all_x), np.array(all_y), np.array(all_z), 
            np.array(time_fractions), precession_deg_per_orbit, total_precession)

def generate_single_orbit_trace(star_name, precession_offset_deg=0.0):
    """Generate a single orbit for comparison/overlay."""
    star = data.get_star_data(star_name)
    x, y, z = core.generate_orbit_points(star, precession_offset_deg=precession_offset_deg)
    return x, y, z

# =============================================================================
# VISUALIZATION
# =============================================================================

def create_rosette_visualization(stars_to_show=None):
    """
    Create the rosette visualization showing Schwarzschild precession.
    
    Args:
        stars_to_show: List of star names. Default: S2 and S4714 (the contrast is dramatic)
    
    Returns:
        Plotly Figure
    """
    if stars_to_show is None:
        stars_to_show = ['S2', 'S4714']
    
    fig = go.Figure()
    
    # =========================================================================
    # 1. Add Sgr A* (Black Hole)
    # =========================================================================
    fig.add_traces(core.create_sgr_a_marker(scale_factor=30))
    
    # =========================================================================
    # 2. Generate Rosette for Each Star
    # =========================================================================
    
    # Color schemes for different stars
    colorscales = {
        'S2': 'Viridis',      # Blue -> Green -> Yellow
        'S62': 'Cividis',     # Blue -> Yellow
        'S4711': 'Blues',     # Light -> Dark Blue
        'S4714': 'Plasma',    # Purple -> Orange -> Yellow
    }
    
    # Number of orbits to simulate (more for slower precession)
    orbit_counts = {
        'S2': 100,      # 0.2 deg/orbit -> need many to see pattern
        'S62': 40,      # 1.3 deg/orbit -> faster precession
        'S4711': 80,    # 0.19 deg/orbit -> similar to S2
        'S4714': 50,    # 2.9 deg/orbit -> very fast, dramatic rosette
    }
    
    max_range = 0
    colorbar_positions = [0.85, 0.15]  # Alternate positions for multiple colorbars
    
    for i, star_name in enumerate(stars_to_show):
        star = data.get_star_data(star_name)
        if star is None:
            continue
        
        n_orbits = orbit_counts.get(star_name, 50)
        
        # Generate the rosette trace
        x, y, z, time_vals, rate, total = generate_rosette_trace(
            star_name, 
            num_orbits=n_orbits
        )
        
        # Update max range for axis scaling
        apoapsis = data.calculate_apoapsis_au(star['a_au'], star['e'])
        max_range = max(max_range, apoapsis)
        
        # Add the rosette trace
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(
                width=2,
                color=time_vals,
                colorscale=colorscales.get(star_name, 'Viridis'),
                showscale=True,
                cmin=0,
                cmax=1,
                colorbar=dict(
                    title=dict(
                        text=f"{star_name}<br>Time",
                        font=dict(size=10)
                    ),
                    ticktext=['Now', 'Future'],
                    tickvals=[0, 1],
                    len=0.3,
                    y=colorbar_positions[i % len(colorbar_positions)],
                    x=1.02
                )
            ),
            name=f"{star['name']} ({rate:.2f} deg/orbit)",
            hovertemplate=(
                f"<b>{star['name']}</b><br>"
                f"Precession: {rate:.3f} deg/orbit<br>"
                f"Total rotation: {total:.1f} deg over {n_orbits} orbits<br>"
                "<extra></extra>"
            )
        ))
        
        # Add a highlighted "current" orbit (first orbit, no precession)
        x0, y0, z0 = generate_single_orbit_trace(star_name, precession_offset_deg=0)
        fig.add_trace(go.Scatter3d(
            x=x0, y=y0, z=z0,
            mode='lines',
            line=dict(
                width=4,
                color='white',
                dash='solid'
            ),
            name=f"{star_name} (current orbit)",
            opacity=0.8,
            showlegend=True
        ))
    
    # =========================================================================
    # 3. Layout
    # =========================================================================
    
    axis_range = max_range * 1.15
    
    fig.update_layout(
        title=dict(
            text="<b>General Relativity in Action: Schwarzschild Precession</b><br>"
                 "<sup>Orbits don't close - they rotate, tracing a 'rosette' pattern over time</sup>",
            x=0.5,
            font=dict(size=16, color='white')
        ),
        scene=dict(
            xaxis=dict(
                title='X (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(30,30,50)',
                showbackground=True,
                gridwidth=1
            ),
            yaxis=dict(
                title='Y (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(30,30,50)',
                showbackground=True,
                gridwidth=1
            ),
            zaxis=dict(
                title='Z (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(5,5,15)',
                gridcolor='rgb(30,30,50)',
                showbackground=True,
                gridwidth=1
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.5, y=0.5, z=0.8)  # Angled view to see rosette structure
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
            font=dict(size=10)
        ),
        margin=dict(l=0, r=100, t=80, b=0)
    )
    
    # Add explanatory annotations
    fig.add_annotation(
        text="White line = current orbit | Colored spiral = future path as orbit precesses",
        xref="paper", yref="paper",
        x=0.5, y=-0.02,
        showarrow=False,
        font=dict(size=11, color='lightgray')
    )
    
    fig.add_annotation(
        text="S4714: ~3 deg/orbit precession (dramatic spiral)<br>"
             "S2: ~0.2 deg/orbit (subtle - what GRAVITY measured for 27 years)",
        xref="paper", yref="paper",
        x=0.02, y=0.02,
        showarrow=False,
        font=dict(size=10, color='yellow'),
        align='left',
        bgcolor='rgba(0,0,0,0.5)'
    )
    
    return fig

def create_single_star_rosette(star_name, num_orbits=None):
    """
    Create a focused rosette visualization for a single star.
    Useful for educational deep-dives.
    """
    return create_rosette_visualization(stars_to_show=[star_name])

# =============================================================================
# EDUCATIONAL COMPARISON
# =============================================================================

def create_newton_vs_einstein_comparison(star_name='S2'):
    """
    Create a side-by-side comparison showing:
    - Newton: Orbit closes perfectly (same ellipse forever)
    - Einstein: Orbit precesses (rosette pattern)
    
    This is THE visualization that proves General Relativity.
    """
    fig = go.Figure()
    
    star = data.get_star_data(star_name)
    precession_rate = data.calculate_schwarzschild_precession_per_orbit(star['a_au'], star['e'])
    
    # Exaggerate precession for visual clarity (10x)
    # In reality S2's precession is subtle, but this shows the CONCEPT
    exaggeration_factor = 10
    
    print(f"\nNewton vs Einstein comparison for {star['name']}")
    print(f"  Actual precession: {precession_rate:.3f} deg/orbit")
    print(f"  Exaggerated (10x): {precession_rate * exaggeration_factor:.3f} deg/orbit")
    
    # Newton's prediction: same orbit forever
    x_newton, y_newton, z_newton = core.generate_orbit_points(star)
    
    fig.add_trace(go.Scatter3d(
        x=x_newton, y=y_newton, z=z_newton,
        mode='lines',
        line=dict(width=4, color='red'),
        name="Newton's Prediction (orbit closes)",
        opacity=0.8
    ))
    
    # Einstein's prediction: orbits precess
    num_orbits = 20
    all_x, all_y, all_z = [], [], []
    
    for n in range(num_orbits):
        offset = n * precession_rate * exaggeration_factor
        x, y, z = core.generate_orbit_points(star, precession_offset_deg=offset)
        all_x.extend(x)
        all_y.extend(y)
        all_z.extend(z)
    
    fig.add_trace(go.Scatter3d(
        x=all_x, y=all_y, z=all_z,
        mode='lines',
        line=dict(width=2, color='cyan'),
        name="Einstein's Prediction (orbit precesses)",
        opacity=0.6
    ))
    
    # Add Sgr A*
    fig.add_traces(core.create_sgr_a_marker(scale_factor=30))
    
    # Layout
    apoapsis = data.calculate_apoapsis_au(star['a_au'], star['e'])
    axis_range = apoapsis * 1.15
    
    fig.update_layout(
        title=dict(
            text=f"<b>Newton vs Einstein: {star['name']}'s Orbit</b><br>"
                 f"<sup>Precession exaggerated 10x for visibility (actual: {precession_rate:.2f} deg/orbit)</sup>",
            x=0.5,
            font=dict(size=16, color='white')
        ),
        scene=dict(
            xaxis=dict(title='X (AU)', range=[-axis_range, axis_range], backgroundcolor='rgb(5,5,15)'),
            yaxis=dict(title='Y (AU)', range=[-axis_range, axis_range], backgroundcolor='rgb(5,5,15)'),
            zaxis=dict(title='Z (AU)', range=[-axis_range, axis_range], backgroundcolor='rgb(5,5,15)'),
            aspectmode='cube',
            camera=dict(eye=dict(x=0, y=0, z=2.5))  # Top-down view
        ),
        paper_bgcolor='rgb(5,5,15)',
        font=dict(color='white'),
        legend=dict(
            yanchor="top", y=0.99,
            xanchor="left", x=0.01,
            bgcolor='rgba(0,0,0,0.7)'
        )
    )
    
    fig.add_annotation(
        text="Red = Newton (same ellipse forever)<br>Cyan = Einstein (ellipse rotates)",
        xref="paper", yref="paper",
        x=0.98, y=0.02,
        showarrow=False,
        font=dict(size=11, color='white'),
        align='right',
        bgcolor='rgba(0,0,0,0.5)'
    )
    
    return fig

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("S-STAR VISUALIZATION - Stage 3: Schwarzschild Precession")
    print("General Relativity's Signature: The Rosette Pattern")
    print("=" * 60)
    
    # Main rosette visualization
    print("\n--- Creating Main Rosette (S2 + S4714) ---")
    fig_rosette = create_rosette_visualization()
    show_and_save(fig_rosette, "sgr_a_visualization_stage3_rosette")
    
    # Newton vs Einstein comparison
    print("\n--- Creating Newton vs Einstein Comparison ---")
    fig_comparison = create_newton_vs_einstein_comparison('S2')
    show_and_save(fig_comparison, "sgr_a_newton_vs_einstein")
    
    print("\n" + "=" * 60)
    print("Stage 3 Complete!")
    print("=" * 60)
    print("\nWhat to look for in the rosette visualization:")
    print("  - S4714 (orange): Dramatic spiral - ~3 deg/orbit precession")
    print("  - S2 (green): Subtle spread - ~0.2 deg/orbit (what GRAVITY measured)")
    print("  - White lines: Current orbit position")
    print("  - Color gradient: Dark = now, bright = far future")
    print("\nWhat to look for in Newton vs Einstein:")
    print("  - Red (Newton): Single closed ellipse")
    print("  - Cyan (Einstein): Spiraling rosette pattern")
    print("  - This difference is what proves General Relativity!")


