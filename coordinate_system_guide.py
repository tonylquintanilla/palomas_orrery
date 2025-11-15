"""
coordinate_system_guide.py - Educational reference for J2000 Ecliptic Coordinate System

This module creates an interactive HTML visualization with embedded reference text.
"""

import plotly.graph_objects as go
import numpy as np
import webbrowser
import tempfile
import os


def create_coordinate_system_diagram():
    """
    Create an interactive 3D diagram showing the J2000 Ecliptic coordinate system.
    
    Returns:
        plotly.graph_objects.Figure: Interactive 3D plot
    """
    
    fig = go.Figure()
    
    # Axis length
    axis_length = 2.0
    
    # Define colors
    x_color = 'red'
    y_color = 'green'
    z_color = 'blue'
    ecliptic_color = 'rgba(200, 200, 255, 0.3)'
    
    # +X Axis (Vernal Equinox direction)
    fig.add_trace(go.Scatter3d(
        x=[0, axis_length],
        y=[0, 0],
        z=[0, 0],
        mode='lines+text',
        line=dict(color=x_color, width=8),
        text=['', '+X<br>Vernal Equinox'],
        textposition='top center',
        textfont=dict(size=14, color=x_color),
        name='+X Axis',
        hovertemplate='<b>+X Axis</b><br>Points to Vernal Equinox (♈)<br>Celestial Longitude 0°<extra></extra>',
        showlegend=True
    ))
    
    # +Y Axis (90° ahead)
    fig.add_trace(go.Scatter3d(
        x=[0, 0],
        y=[0, axis_length],
        z=[0, 0],
        mode='lines+text',
        line=dict(color=y_color, width=8),
        text=['', '+Y<br>90° Ahead'],
        textposition='top center',
        textfont=dict(size=14, color=y_color),
        name='+Y Axis',
        hovertemplate='<b>+Y Axis</b><br>90° ahead of vernal equinox<br>Direction of Earth\'s motion<extra></extra>',
        showlegend=True
    ))
    
    # +Z Axis (North Ecliptic Pole)
    fig.add_trace(go.Scatter3d(
        x=[0, 0],
        y=[0, 0],
        z=[0, axis_length],
        mode='lines+text',
        line=dict(color=z_color, width=8),
        text=['', '+Z<br>Ecliptic North'],
        textposition='top center',
        textfont=dict(size=14, color=z_color),
        name='+Z Axis',
        hovertemplate='<b>+Z Axis</b><br>Ecliptic North Pole<br>Perpendicular to ecliptic plane<extra></extra>',
        showlegend=True
    ))
    
    # Draw the ecliptic plane (XY plane)
    plane_size = 1.5
    n_points = 2
    x_plane = np.linspace(-plane_size, plane_size, n_points)
    y_plane = np.linspace(-plane_size, plane_size, n_points)
    x_grid, y_grid = np.meshgrid(x_plane, y_plane)
    z_grid = np.zeros_like(x_grid)
    
    fig.add_trace(go.Surface(
        x=x_grid,
        y=y_grid,
        z=z_grid,
        colorscale=[[0, ecliptic_color], [1, ecliptic_color]],
        showscale=False,
        name='Ecliptic Plane',
        hovertemplate='<b>Ecliptic Plane (XY Plane)</b><br>Earth\'s orbital plane<extra></extra>',
        opacity=0.3,
        showlegend=True
    ))
    
    # Add Earth's orbit as a circle in the XY plane
    theta = np.linspace(0, 2*np.pi, 100)
    orbit_radius = 1.0
    earth_x = orbit_radius * np.cos(theta)
    earth_y = orbit_radius * np.sin(theta)
    earth_z = np.zeros_like(theta)
    
    fig.add_trace(go.Scatter3d(
        x=earth_x,
        y=earth_y,
        z=earth_z,
        mode='lines',
        line=dict(color='cyan', width=4, dash='dash'),
        name='Earth\'s Orbit',
        hovertemplate='<b>Earth\'s Orbit</b><br>Circular path in XY plane<br>Radius = 1 AU<extra></extra>',
        showlegend=True
    ))
    
    # Add the Sun at origin
    fig.add_trace(go.Scatter3d(
        x=[0],
        y=[0],
        z=[0],
        mode='markers+text',
        marker=dict(size=15, color='yellow', symbol='circle',
                   line=dict(color='orange', width=2)),
        text=['Sun'],
        textposition='bottom center',
        textfont=dict(size=12, color='orange'),
        name='Sun',
        hovertemplate='<b>Sun</b><br>Origin (0, 0, 0)<extra></extra>',
        showlegend=True
    ))
    
    # Add Earth at vernal equinox position (X = -1, Y = 0, Z = 0)
    # At vernal equinox (March 20), Earth is at X=-1 because the Sun's direction 
    # FROM Earth points to +X (the vernal equinox direction in the sky)
    fig.add_trace(go.Scatter3d(
        x=[-1.0],
        y=[0],
        z=[0],
        mode='markers+text',
        marker=dict(size=10, color='blue', symbol='circle'),
        text=['Earth<br>(at Vernal Equinox)'],
        textposition='top center',
        textfont=dict(size=10, color='blue'),
        name='Earth Position',
        hovertemplate='<b>Earth</b><br>Position at Vernal Equinox<br>(X=-1 AU, Y=0, Z=0)<br>Sun direction from Earth points to +X<extra></extra>',
        showlegend=True
    ))
    
    # Add an inclined orbit example (e.g., at 30° inclination)
    inclination = 30  # degrees
    inc_rad = np.radians(inclination)
    inclined_x = orbit_radius * np.cos(theta)
    inclined_y = orbit_radius * np.sin(theta) * np.cos(inc_rad)
    inclined_z = orbit_radius * np.sin(theta) * np.sin(inc_rad)
    
    fig.add_trace(go.Scatter3d(
        x=inclined_x,
        y=inclined_y,
        z=inclined_z,
        mode='lines',
        line=dict(color='magenta', width=3, dash='dot'),
        name=f'Inclined Orbit (i={inclination}°)',
        hovertemplate=f'<b>Inclined Orbit</b><br>Inclination = {inclination}°<br>Tilted relative to ecliptic<extra></extra>',
        showlegend=True
    ))
    
    # Update layout - NO HEIGHT SPECIFIED (let it fill container)
    fig.update_layout(
        scene=dict(
            xaxis=dict(
                title='X (AU)',
                range=[-2, 2],
                showgrid=True,
                gridcolor='lightgray',
                zeroline=True,
                zerolinecolor='black'
            ),
            yaxis=dict(
                title='Y (AU)',
                range=[-2, 2],
                showgrid=True,
                gridcolor='lightgray',
                zeroline=True,
                zerolinecolor='black'
            ),
            zaxis=dict(
                title='Z (AU)',
                range=[-2, 2],
                showgrid=True,
                gridcolor='lightgray',
                zeroline=True,
                zerolinecolor='black'
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.2),
                center=dict(x=0, y=0, z=-0.2)
        #        center=dict(x=0, y=0, z=-0.5)
            )
        ),
        title=dict(
            text="<b>J2000 Ecliptic Coordinate System</b><br><sub>Interactive 3D Reference Diagram</sub>",
            x=0.5,
            xanchor='center',
            font=dict(size=16)
        ),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='black',
            borderwidth=1,
            font=dict(size=10)
        ),
    #    margin=dict(l=0, r=0, t=80, b=0)
        margin=dict(l=0, r=0, t=80, b=0)
        # NO height parameter - let it be controlled by CSS
    )
    
    return fig


def create_coordinate_system_guide():
    """
    Create and open an HTML file with 3D visualization and reference text side by side.
    """
    
    # Create the 3D diagram
    fig = create_coordinate_system_diagram()
    
    # Generate the Plotly HTML as a string without the full document wrapper
    plotly_html = fig.to_html(
        include_plotlyjs='cdn',
        div_id='plotly-div',
        config={'responsive': True, 'displayModeBar': True},
        full_html=False  # KEY FIX: Don't generate full HTML, just the div
    )
    
    # Reference text content (kept in a separate variable for readability)
    reference_text = """
<div style="font-family: 'Courier New', monospace; font-size: 11px; line-height: 1.5; padding: 20px; background-color: #F5F5F5;">

<h2 style="color: #2C3E50; border-bottom: 2px solid #3498DB;">J2000 ECLIPTIC COORDINATE SYSTEM</h2>
<p style="font-style: italic; color: #555;">Used Throughout Paloma's Orrery</p>

<p style="background-color: #FFE6CC; padding: 10px; border-left: 4px solid #FF9800;">
<b>⭐ INTERACT WITH THE 3D DIAGRAM (LEFT) AS YOU READ ⭐</b><br>
<b>Rotate:</b> Click and drag | <b>Zoom:</b> Scroll wheel | <b>Pan:</b> Right-click and drag
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">WHAT IS THE J2000 ECLIPTIC COORDINATE SYSTEM?</h3>

<p>The J2000 Ecliptic coordinate system is the standard reference frame used in modern astronomy for describing positions of celestial objects in our solar system.</p>

<p>Think of it as the <b>"GPS coordinates"</b> of the solar system - just as we use latitude, longitude, and altitude on Earth, astronomers use this 3D coordinate system (X, Y, Z) to specify where everything is in space.</p>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #3498DB;">
<b>🔍 IN THE DIAGRAM:</b> You see the three colored axes (red, green, blue) emanating from the yellow Sun at the origin.
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">THE THREE AXES EXPLAINED</h3>

<h4 style="color: #C0392B;">+X AXIS (RED): Points Toward the Vernal Equinox (♈)</h4>

<ul>
<li>The vernal equinox (also called the "First Point of Aries" ♈) is where the Sun's apparent path across the sky (the ecliptic) crosses the celestial equator while moving from south to north.</li>

<li>This happens around March 20 each year, marking spring in the Northern Hemisphere.</li>

<li>On J2000.0 (Jan 1, 2000, 12:00 TT), astronomers "froze" this direction to create a stable reference.</li>

<li>This serves as <b>celestial longitude 0°</b> - think of it as "cosmic east," the universal starting direction.</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #C0392B;">
<b>🔍 IN THE DIAGRAM:</b> The <span style="color: #C0392B; font-weight: bold;">RED</span> axis points right. Earth is shown at the <b>-X</b> position during the vernal equinox because the Sun's direction <i>from Earth</i> points to <b>+X</b> (toward the vernal equinox in the sky).
</p>

<h4 style="color: #27AE60;">+Y AXIS (GREEN): 90° Ahead in Earth's Orbit</h4>

<ul>
<li>The +Y axis is 90° ahead of +X in the ecliptic plane.</li>

<li>It points in the direction of Earth's motion through space at the vernal equinox.</li>

<li>This completes the right-handed coordinate system where X × Y = Z (cross product).</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #27AE60;">
<b>🔍 IN THE DIAGRAM:</b> The <span style="color: #27AE60; font-weight: bold;">GREEN</span> axis points forward. Earth would be here 3 months after the vernal equinox (around June 20).
</p>

<h4 style="color: #2E86C1;">+Z AXIS (BLUE): Points Toward the Ecliptic North Pole</h4>

<ul>
<li>The +Z axis points perpendicular to Earth's orbital plane (the ecliptic), toward the north side.</li>

<li><b>Defined using the right-hand rule:</b> Curl your right hand fingers in the direction of Earth's orbit (counter-clockwise from above), your thumb points +Z.</li>

<li>This is <b>"cosmic north"</b> - perpendicular to Earth's orbit.</li>

<li>Objects with positive Z are "above" the ecliptic plane (north), negative Z are "below" (south).</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #2E86C1;">
<b>🔍 IN THE DIAGRAM:</b> The <span style="color: #2E86C1; font-weight: bold;">BLUE</span> axis points upward. Notice how the inclined orbit (magenta) goes above and below the ecliptic plane.
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">THE XY PLANE: EARTH'S ORBITAL PLANE (THE ECLIPTIC)</h3>

<ul>
<li>The XY plane is the <b>ecliptic itself</b> - the plane of Earth's orbit around the Sun.</li>

<li>This is the fundamental "reference table" for measuring positions of all solar system objects.</li>

<li>Most planets orbit close to this plane (within a few degrees) because the solar system formed from a rotating disk.</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #8E44AD;">
<b>🔍 IN THE DIAGRAM:</b> The blue semi-transparent plane is the ecliptic. The <span style="color: cyan; font-weight: bold;">cyan circle</span> shows Earth's orbit lying flat in this plane.
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">ORBITAL DIRECTION: PROGRADE VS RETROGRADE</h3>

<h4>PROGRADE ORBITS (inclination i &lt; 90°):</h4>
<ul>
<li>Objects orbit in the same direction as Earth - counter-clockwise when viewed from above the North Pole.</li>
<li>Most planets, asteroids, and many comets have prograde orbits.</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #16A085;">
<b>🔍 IN THE DIAGRAM:</b> Earth's orbit (cyan) goes counter-clockwise. The magenta inclined orbit is also prograde.
</p>

<h4>RETROGRADE ORBITS (inclination i &gt; 90°):</h4>
<ul>
<li>Objects orbit opposite to Earth - clockwise when viewed from above the North Pole.</li>
<li>Some comets and captured moons have retrograde orbits.</li>
</ul>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">THE J2000.0 REFERENCE EPOCH</h3>

<h4>WHAT IS J2000.0?</h4>
<ul>
<li><b>J2000.0 = January 1, 2000, at 12:00 Terrestrial Time (TT)</b></li>
<li>The "J" stands for Julian epoch, "2000.0" is the year</li>
</ul>

<h4>WHY DO WE NEED A REFERENCE EPOCH?</h4>
<ul>
<li>Earth's axis wobbles slowly (<b>precession</b>), causing the vernal equinox to drift ~50 arcseconds per year.</li>

<li>By "freezing" the coordinate system at J2000.0, we have a stable reference frame that doesn't change.</li>

<li>All modern astronomical data uses J2000.0 as the standard reference.</li>
</ul>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">HOW THIS APPLIES TO PALOMA'S ORRERY</h3>

<h4>ORBITAL POSITIONS:</h4>
<ul>
<li>Every object in Paloma's Orrery has its position calculated in J2000 Ecliptic coordinates.</li>
<li>When you see "X = 1.5 AU, Y = 0.3 AU, Z = 0.1 AU," these are distances along the three axes.</li>
</ul>

<h4>KEPLERIAN ORBITAL ELEMENTS:</h4>
<ul>
<li><b>i (inclination):</b> Angle between orbital plane and XY plane (ecliptic)</li>
<li><b>Ω (longitude of ascending node):</b> Angle from +X axis to where orbit crosses ecliptic going northward</li>
<li><b>ω (argument of periapsis):</b> Angle within orbital plane from ascending node to periapsis</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #E74C3C;">
<b>🔍 IN THE DIAGRAM:</b> The inclined orbit (<span style="color: magenta; font-weight: bold;">magenta</span>) shows how an orbit with i ≠ 0° is tilted relative to the ecliptic.
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">PRACTICAL EXAMPLES</h3>

<h4>EARTH'S POSITION:</h4>
<ul>
<li>Earth orbits in the XY plane, so Z ≈ 0 always</li>
<li>At vernal equinox (March 20): Earth is at X ≈ -1 AU, Y ≈ 0, with the Sun's direction from Earth pointing to +X (the vernal equinox in the sky)</li>
<li>Three months later (June 21): X ≈ 0, Y ≈ -1 AU</li>
<li>Six months later (Sept 22): X ≈ +1 AU, Y ≈ 0</li>
<li>Nine months later (Dec 21): X ≈ 0, Y ≈ +1 AU</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #3498DB;">
<b>🔍 IN THE DIAGRAM:</b> Follow the <span style="color: cyan; font-weight: bold;">cyan circle</span> to see Earth's circular path in the XY plane.
</p>

<h4>PLUTO'S TILTED ORBIT:</h4>
<ul>
<li>Pluto has inclination i = 17°, so its orbit is tilted significantly</li>
<li>Maximum Z value: sin(17°) × 40 AU ≈ 12 AU above/below ecliptic</li>
</ul>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #9B59B6;">
<b>🔍 IN THE DIAGRAM:</b> Imagine the <span style="color: magenta; font-weight: bold;">magenta orbit</span> stretched much larger - that's similar to Pluto's tilted orbit.
</p>

<h4>HALLEY'S COMET:</h4>
<ul>
<li>Inclination i = 162° means retrograde orbit</li>
<li>Orbits "backwards" and far out of ecliptic plane</li>
</ul>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">COMMON MISCONCEPTIONS</h3>

<table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
<tr style="background-color: #FADBD8;">
<td style="padding: 8px; border: 1px solid #ccc;"><b>❌ MISCONCEPTION</b></td>
<td style="padding: 8px; border: 1px solid #ccc;"><b>✓ REALITY</b></td>
</tr>
<tr>
<td style="padding: 8px; border: 1px solid #ccc;">"The ecliptic is Earth's equator."</td>
<td style="padding: 8px; border: 1px solid #ccc;">FALSE. The ecliptic is Earth's ORBITAL plane. Earth's equator is tilted 23.4° relative to it (causes seasons)</td>
</tr>
<tr>
<td style="padding: 8px; border: 1px solid #ccc;">"The +X axis points toward Aries."</td>
<td style="padding: 8px; border: 1px solid #ccc;">MISLEADING. Called "First Point of Aries" historically, but due to precession it now points toward Pisces.</td>
</tr>
<tr>
<td style="padding: 8px; border: 1px solid #ccc;">"J2000 coordinates become outdated."</td>
<td style="padding: 8px; border: 1px solid #ccc;">FALSE. J2000 is FIXED at the epoch. It never becomes outdated.</td>
</tr>
<tr>
<td style="padding: 8px; border: 1px solid #ccc;">"All objects orbit in the ecliptic plane."</td>
<td style="padding: 8px; border: 1px solid #ccc;">FALSE. Many comets and asteroids have high inclinations (30°, 60°, or more).</td>
</tr>
</table>

<p style="background-color: #E8F4F8; padding: 8px; border-left: 3px solid #E67E22;">
<b>🔍 IN THE DIAGRAM:</b> Compare the cyan orbit (i=0°, in ecliptic) with the magenta orbit (i=30°, tilted).
</p>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">INTERACTIVE EXPLORATION TIPS</h3>

<p><b>🎯 THINGS TO TRY IN THE 3D DIAGRAM:</b></p>

<ol>
<li><b>ROTATE THE VIEW:</b> Click and drag to see the coordinate system from different angles</li>

<li><b>ZOOM IN/OUT:</b> Use scroll wheel to examine details</li>

<li><b>HOVER OVER ELEMENTS:</b> See descriptions of each component</li>

<li><b>COMPARE ORBITS:</b> Notice how the cyan orbit (i=0°) stays in the XY plane while the magenta orbit (i=30°) crosses above and below it</li>

<li><b>FIND THE SUN:</b> The yellow marker at the origin (0,0,0)</li>

<li><b>LOCATE EARTH:</b> The blue marker on the -X axis at the vernal equinox position</li>

<li><b>WATCH HOW INCLINATION TILTS ORBITS:</b> Compare the flat cyan circle with the tilted magenta orbit</li>

<li><b>OBSERVE THE LINE OF NODES:</b> Where the inclined orbit crosses the ecliptic plane</li>
</ol>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">FURTHER LEARNING</h3>

<h4>TO VISUALIZE ORBITAL MECHANICS:</h4>
<ul>
<li>Use the <b>Orbital Parameter Transformation Visualization</b> to see how orbits rotate from perifocal to ecliptic frame</li>
<li>Explore the <b>Interactive Orbital Eccentricity Visualization</b> to understand orbital shapes</li>
</ul>

<h4>RESOURCES:</h4>
<ul>
<li><b>JPL Horizons System:</b> <a href="https://ssd.jpl.nasa.gov/horizons/" target="_blank">https://ssd.jpl.nasa.gov/horizons/</a><br>
The source of orbital data for Paloma's Orrery</li>

<li><b>Explanatory Supplement to the Astronomical Almanac</b><br>
The definitive reference for coordinate systems in astronomy</li>

<li><b>NASA's Coordinate Systems documentation</b><br>
Practical guide for understanding different reference frames</li>
</ul>

<hr style="border: 1px solid #BDC3C7;">

<h3 style="color: #2980B9;">SUMMARY</h3>

<div style="background-color: #D5F4E6; padding: 15px; border-radius: 5px; border: 2px solid #27AE60; margin-bottom: 20px;">
<p><b>The J2000 Ecliptic coordinate system provides a universal, stable framework for describing positions and motions throughout the solar system:</b></p>

<ul style="margin: 10px 0;">
<li><b style="color: #C0392B;">+X axis (RED)</b> → Vernal Equinox (♈), celestial longitude 0°</li>
<li><b style="color: #27AE60;">+Y axis (GREEN)</b> → 90° ahead, Earth's motion direction</li>
<li><b style="color: #2E86C1;">+Z axis (BLUE)</b> → North Ecliptic Pole, perpendicular to ecliptic</li>
<li><b>XY plane</b> → The ecliptic (Earth's orbital plane around the Sun)</li>
<li><b>Origin</b> → The Sun (or solar system barycenter for high precision)</li>
</ul>

<p><b>This coordinate system is used consistently throughout Paloma's Orrery for:</b></p>
<ul style="margin: 10px 0;">
<li>✓ Plotting object positions in 3D space</li>
<li>✓ Calculating orbital paths</li>
<li>✓ Defining Keplerian orbital elements</li>
<li>✓ Transforming between reference frames</li>
</ul>

<p style="margin-top: 15px;"><b>Understanding this coordinate system is key to interpreting all the visualizations in Paloma's Orrery!</b></p>
</div>

</div>
"""
    
    # Create HTML with side-by-side layout
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>J2000 Ecliptic Coordinate System Reference</title>
    <script src="https://cdn.plot.ly/plotly-2.26.0.min.js" charset="utf-8"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        html, body {{
            height: 100%;
            width: 100%;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }}
        h1 {{
            text-align: center;
            background-color: #2C3E50;
            color: white;
            padding: 15px;
            height: 50px;
            line-height: 20px;
        }}
        #container {{
            display: flex;
            height: calc(100vh - 50px);
            width: 100vw;
        }}
        #plot-container {{
            flex: 0 0 60%;
            height: 100%;
            width: 60%;
            position: relative;
            overflow: hidden;
        }}
        #plotly-div {{
            width: 100% !important;
            height: 100% !important;
        }}
        #text-container {{
            flex: 0 0 40%;
            width: 40%;
            height: 100%;
            overflow-y: auto;
            overflow-x: hidden;
            border-left: 2px solid #34495E;
        }}
        /* Custom scrollbar styling */
        #text-container::-webkit-scrollbar {{
            width: 12px;
        }}
        #text-container::-webkit-scrollbar-track {{
            background: #f1f1f1;
        }}
        #text-container::-webkit-scrollbar-thumb {{
            background: #888;
            border-radius: 6px;
        }}
        #text-container::-webkit-scrollbar-thumb:hover {{
            background: #555;
        }}
    </style>
</head>
<body>
    <h1>J2000 Ecliptic Coordinate System Reference Guide</h1>
    <div id="container">
        <div id="plot-container">
            {plotly_html}
        </div>
        <div id="text-container">
            {reference_text}
        </div>
    </div>
</body>
</html>
"""
    
    # Save to temporary file and open in browser
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html', encoding='utf-8')
    temp_file.write(html_content)
    temp_file.close()
    
    # Open in default browser
    webbrowser.open('file://' + temp_file.name)
    
    print(f"Coordinate System Reference Guide opened in browser: {temp_file.name}")


if __name__ == "__main__":
    # For testing the module independently
    create_coordinate_system_guide()
