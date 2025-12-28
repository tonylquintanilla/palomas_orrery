"""
Asteroid Belt Visualization Module
===================================
Functions for creating visualizations of asteroid belt structures in 3D plots.
Includes Main Belt, Hildas, Trojans, and Greeks.
Also includes helper functions for dynamic Trojan positioning based on Jupiter's location.
"""

import numpy as np
import plotly.graph_objs as go
from shared_utilities import create_sun_direction_indicator

#####################################
# Jupiter Angle Helper Functions
#####################################

def calculate_body_angle(x, y):
    """
    Calculate the orbital angle of a body from its x,y coordinates.
    
    Parameters:
        x (float): x-coordinate in AU
        y (float): y-coordinate in AU
        
    Returns:
        float: Angle in radians (0 to 2pi)
    """
    angle = np.arctan2(y, x)
    # Ensure angle is in range [0, 2pi]
    if angle < 0:
        angle += 2 * np.pi
    return angle


def get_jupiter_angle_from_data(ephemeris_data, date_index=0):
    """
    Extract Jupiter's angle from ephemeris data.
    
    Parameters:
        ephemeris_data (dict): Dictionary containing ephemeris data
        date_index (int): Index of the date to use (0 for first date)
        
    Returns:
        float: Jupiter's orbital angle in radians, or 0 if not found
    """
    try:
        # Look for Jupiter in the ephemeris data
        if 'Jupiter' in ephemeris_data:
            jupiter_data = ephemeris_data['Jupiter']
            if 'x' in jupiter_data and 'y' in jupiter_data:
                x = jupiter_data['x'][date_index]
                y = jupiter_data['y'][date_index]
                return calculate_body_angle(x, y)
    except (KeyError, IndexError, TypeError):
        pass
    
    # Return default angle if data not available
    return 0.0


def estimate_jupiter_angle_from_date(date_str):
    """
    Estimate Jupiter's orbital angle from a date string.
    Jupiter's orbital period is ~11.86 years.
    
    Parameters:
        date_str (str): Date in format 'YYYY-MM-DD'
        
    Returns:
        float: Estimated angle in radians
    """
    from datetime import datetime
    
    try:
        # Parse date
        date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Reference: Jupiter at angle 0 on Jan 1, 2000
        ref_date = datetime(2000, 1, 1)
        days_elapsed = (date - ref_date).days
        
        # Jupiter's orbital period in days
        jupiter_period = 11.86 * 365.25
        
        # Calculate angle (radians)
        angle = (2 * np.pi * days_elapsed / jupiter_period) % (2 * np.pi)
        
        return angle
    except:
        return 0.0

# Constants for asteroid belt distances (in AU)
MAIN_BELT_INNER = 2.2  # Inner edge of main belt
MAIN_BELT_OUTER = 3.2  # Outer edge of main belt
MAIN_BELT_PEAK = 2.7   # Peak density region

HILDA_DISTANCE = 3.97  # Hilda group distance (3:2 resonance with Jupiter)
TROJAN_DISTANCE = 5.2  # Jupiter's orbital distance (L4 and L5 points)

# Kirkwood gap locations (orbital resonances with Jupiter)
KIRKWOOD_GAPS = [
    2.06,  # 4:1 resonance
    2.5,   # 3:1 resonance
    2.82,  # 5:2 resonance
    2.95,  # 7:3 resonance
    3.27   # 2:1 resonance
]

#####################################
# Main Asteroid Belt
#####################################

main_belt_info = (
    "***PLOT WITH MANUAL SCALE AT LEAST 4 AU***\n"
    "15-25 MB PER FRAME FOR HTML.\n\n"
    "The main asteroid belt is located between Mars and Jupiter, roughly 2.2 to 3.2 AU from the Sun.\n"
    "It contains millions of rocky bodies ranging from dust particles to dwarf planet Ceres (940 km diameter).\n"
    "Despite its large number of objects, the total mass is only about 4% of the Moon's mass.\n"
    "The belt shows distinct gaps called Kirkwood gaps at distances where orbital resonances with Jupiter\n"
    "cause orbital instabilities. Peak density occurs around 2.7 AU.\n"
    "Most asteroids are C-type (carbonaceous, 75%), S-type (silicaceous, 17%), or M-type (metallic)."
)

def create_main_asteroid_belt(center_position=(0, 0, 0)):
    """
    Creates a visualization of the main asteroid belt with density variations and Kirkwood gaps.
    
    Parameters:
        center_position (tuple): (x, y, z) position of the Sun
        
    Returns:
        list: Plotly trace objects for the main belt
    """
    center_x, center_y, center_z = center_position
    
    # Create multiple density rings to show the structure
    n_particles = 8000  # Total particles to distribute
    n_rings = 30  # Number of radial rings
    
    belt_x = []
    belt_y = []
    belt_z = []
    belt_colors = []
    belt_sizes = []
    
    for i in range(n_rings):
        # Calculate radius for this ring
        radius = MAIN_BELT_INNER + (MAIN_BELT_OUTER - MAIN_BELT_INNER) * (i / (n_rings - 1))
        
        # Calculate density based on distance from peak and Kirkwood gaps
        # Gaussian peak around 2.7 AU
        density = np.exp(-((radius - MAIN_BELT_PEAK) ** 2) / (0.3 ** 2))
        
        # Apply Kirkwood gap reductions
        for gap in KIRKWOOD_GAPS:
            gap_factor = np.exp(-((radius - gap) ** 2) / (0.05 ** 2))
            density *= (1 - 0.7 * gap_factor)  # 70% reduction in gaps
        
        # Number of particles in this ring based on density
        n_in_ring = max(int(n_particles * density / n_rings), 5)
        
        # Generate particles in this ring
        for j in range(n_in_ring):
            angle = np.random.uniform(0, 2 * np.pi)
            
            # Add some radial jitter
            r_jitter = np.random.normal(0, 0.05)
            r = radius + r_jitter
            
            # Position in orbital plane with some inclination
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            
            # Vertical thickness - gets thicker farther from peak
            z_scale = 0.1 + 0.2 * abs(radius - MAIN_BELT_PEAK) / (MAIN_BELT_OUTER - MAIN_BELT_INNER)
            z = np.random.normal(0, z_scale)
            
            belt_x.append(x)
            belt_y.append(y)
            belt_z.append(z)
            
            # Color gradient: inner belt (reddish-brown) to outer belt (gray-brown)
            color_factor = (radius - MAIN_BELT_INNER) / (MAIN_BELT_OUTER - MAIN_BELT_INNER)
            r_color = int(180 + 30 * (1 - color_factor))
            g_color = int(140 + 20 * (1 - color_factor))
            b_color = int(100 + 30 * color_factor)
            belt_colors.append(f'rgb({r_color}, {g_color}, {b_color})')
            
            # Size variation
            belt_sizes.append(np.random.uniform(0.8, 2.0))
    
    # Apply center position offset
    belt_x = np.array(belt_x) + center_x
    belt_y = np.array(belt_y) + center_y
    belt_z = np.array(belt_z) + center_z
    
    # Create the main belt hover text
    belt_text = ["Main Asteroid Belt: Rocky debris between Mars and Jupiter (2.2-3.2 AU).<br>"
                 "Contains millions of asteroids with distinct Kirkwood gaps caused by<br>"
                 "Jupiter's gravitational resonances. Peak density at ~2.7 AU."] * len(belt_x)
    belt_customdata = ['Main Asteroid Belt'] * len(belt_x)
    
    traces = [
        go.Scatter3d(
            x=belt_x,
            y=belt_y,
            z=belt_z,
            mode='markers',
            marker=dict(
                size=belt_sizes,
                color=belt_colors,
                opacity=0.4
            ),
            name='Main Asteroid Belt',
            text=belt_text,
            customdata=belt_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=MAIN_BELT_PEAK
    )
    for trace in sun_traces:
        traces.append(trace)
    
    return traces

#####################################
# Hilda Family
#####################################

hilda_group_info = (
    "***PLOT WITH MANUAL SCALE AT LEAST 5 AU***\n"
    "8-12 MB PER FRAME FOR HTML.\n\n"
    "The Hilda family is a dynamical group of asteroids in a 3:2 orbital resonance with Jupiter.\n"
    "Located at approximately 3.97 AU, they orbit the Sun three times for every two Jupiter orbits.\n"
    "The group forms a distinctive triangular pattern when viewed from above, with concentrations\n"
    "at the L3, L4, and L5 Lagrange points relative to Jupiter. Named after asteroid 153 Hilda,\n"
    "discovered in 1875. Contains about 4,000 known members, most are D-type (dark, reddish) asteroids."
)

def create_hilda_group(center_position=(0, 0, 0)):
    """
    Creates a visualization of the Hilda asteroid group showing triangular structure.
    
    Parameters:
        center_position (tuple): (x, y, z) position of the Sun
        
    Returns:
        list: Plotly trace objects for Hilda group
    """
    center_x, center_y, center_z = center_position
    
    # Hildas form three concentrations 120 degrees apart
    # These correspond to stable points in the 3:2 resonance
    concentration_angles = [0, 2*np.pi/3, 4*np.pi/3]  # 0 deg, 120 deg, 240 deg
    
    hilda_x = []
    hilda_y = []
    hilda_z = []
    
    n_per_concentration = 800  # Asteroids per concentration point
    
    for base_angle in concentration_angles:
        for i in range(n_per_concentration):
            # Angular spread around each concentration
            angle = base_angle + np.random.normal(0, 0.3)  # ~17 degree spread
            
            # Radial distance with some variation
            radius = HILDA_DISTANCE + np.random.normal(0, 0.08)
            
            # Position
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = np.random.normal(0, 0.05)  # Small vertical spread
            
            hilda_x.append(x)
            hilda_y.append(y)
            hilda_z.append(z)
    
    # Apply center position offset
    hilda_x = np.array(hilda_x) + center_x
    hilda_y = np.array(hilda_y) + center_y
    hilda_z = np.array(hilda_z) + center_z
    
    # Create hover text
    hilda_text = ["Hilda Family: Asteroids in 3:2 resonance with Jupiter at ~3.97 AU.<br>"
                  "Forms distinctive triangular pattern with three main concentrations<br>"
                  "120 deg apart. Mostly D-type (dark, reddish) asteroids."] * len(hilda_x)
    hilda_customdata = ['Hilda Family'] * len(hilda_x)
    
    traces = [
        go.Scatter3d(
            x=hilda_x,
            y=hilda_y,
            z=hilda_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(200, 170, 100)',  # Golden-yellow
                opacity=0.5
            ),
            name='Hilda Family',
            text=hilda_text,
            customdata=hilda_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=HILDA_DISTANCE
    )
    for trace in sun_traces:
        traces.append(trace)
    
    return traces

#####################################
# Jupiter Trojans (L4 - Greeks)
#####################################

jupiter_trojans_greeks_info = (
    "***PLOT WITH JUPITER OR MANUAL SCALE AT LEAST 6 AU***\n"
    "10-15 MB PER FRAME FOR HTML.\n\n"
    "The Jupiter Trojans at the L4 Lagrange point (leading Jupiter by 60 deg) are traditionally\n"
    "called the 'Greek camp' after Greek heroes from the Iliad. This stable gravitational point\n"
    "at Jupiter's orbital distance (~5.2 AU) traps thousands of asteroids in a cloud formation.\n"
    "The L4 Greeks slightly outnumber the L5 Trojans. Notable members include 588 Achilles,\n"
    "624 Hektor (largest at ~250 km), and 617 Patroclus (binary asteroid, NASA Lucy mission target).\n"
    "Most are D-type asteroids - dark, reddish bodies rich in organic compounds."
)

def create_jupiter_trojans_greeks(center_position=(0, 0, 0), jupiter_angle=0):
    """
    Creates a visualization of Jupiter's L4 Trojan asteroids (Greek camp).
    
    Parameters:
        center_position (tuple): (x, y, z) position of the Sun
        jupiter_angle (float): Current angle of Jupiter in radians (for positioning L4 correctly)
        
    Returns:
        list: Plotly trace objects for L4 Trojans
    """
    center_x, center_y, center_z = center_position
    
    # L4 point is 60 degrees ahead of Jupiter
    l4_angle = jupiter_angle + np.pi/3
    
    trojan_x = []
    trojan_y = []
    trojan_z = []
    
    n_asteroids = 1500  # Number of asteroids in Greek camp
    
    for i in range(n_asteroids):
        # Create a cloud around the L4 point
        # Angular spread
        angle = l4_angle + np.random.normal(0, 0.4)  # ~23 degree spread
        
        # Radial spread around Jupiter's orbit
        radius = TROJAN_DISTANCE + np.random.normal(0, 0.15)
        
        # Position
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = np.random.normal(0, 0.2)  # Vertical spread
        
        trojan_x.append(x)
        trojan_y.append(y)
        trojan_z.append(z)
    
    # Apply center position offset
    trojan_x = np.array(trojan_x) + center_x
    trojan_y = np.array(trojan_y) + center_y
    trojan_z = np.array(trojan_z) + center_z
    
    # Create hover text
    trojan_text = ["Jupiter Trojans (L4 - Greeks): Asteroids trapped at Jupiter's leading<br>"
                   "Lagrange point (L4), 60 deg ahead. Called 'Greek camp' after Iliad heroes.<br>"
                   "Contains thousands of D-type asteroids, targets of NASA's Lucy mission."] * len(trojan_x)
    trojan_customdata = ['Jupiter Trojans (Greeks - L4)'] * len(trojan_x)
    
    traces = [
        go.Scatter3d(
            x=trojan_x,
            y=trojan_y,
            z=trojan_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(180, 100, 100)',  # Reddish
                opacity=0.5
            ),
            name='Jupiter Trojans (Greeks - L4)',
            text=trojan_text,
            customdata=trojan_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=TROJAN_DISTANCE
    )
    for trace in sun_traces:
        traces.append(trace)
    
    return traces

#####################################
# Jupiter Trojans (L5 - Trojans)
#####################################

jupiter_trojans_trojans_info = (
    "10-15 MB PER FRAME FOR HTML.\n\n"
    "The Jupiter Trojans at the L5 Lagrange point (trailing Jupiter by 60 deg) are traditionally\n"
    "called the 'Trojan camp' after Trojan heroes from the Iliad. This stable gravitational point\n"
    "at Jupiter's orbital distance (~5.2 AU) is slightly less populated than L4. Notable members\n"
    "include 884 Priamus, 1172 Aeneas, and 911 Agamemnon. The L5 camp has about 40% fewer asteroids\n"
    "than L4, though the reason for this asymmetry is not fully understood. NASA's Lucy mission\n"
    "will visit both camps. Like L4, most are dark D-type asteroids."
)

def create_jupiter_trojans_trojans(center_position=(0, 0, 0), jupiter_angle=0):
    """
    Creates a visualization of Jupiter's L5 Trojan asteroids (Trojan camp).
    
    Parameters:
        center_position (tuple): (x, y, z) position of the Sun
        jupiter_angle (float): Current angle of Jupiter in radians (for positioning L5 correctly)
        
    Returns:
        list: Plotly trace objects for L5 Trojans
    """
    center_x, center_y, center_z = center_position
    
    # L5 point is 60 degrees behind Jupiter
    l5_angle = jupiter_angle - np.pi/3
    
    trojan_x = []
    trojan_y = []
    trojan_z = []
    
    n_asteroids = 1200  # Slightly fewer than L4 (observed asymmetry)
    
    for i in range(n_asteroids):
        # Create a cloud around the L5 point
        # Angular spread
        angle = l5_angle + np.random.normal(0, 0.4)  # ~23 degree spread
        
        # Radial spread around Jupiter's orbit
        radius = TROJAN_DISTANCE + np.random.normal(0, 0.15)
        
        # Position
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = np.random.normal(0, 0.2)  # Vertical spread
        
        trojan_x.append(x)
        trojan_y.append(y)
        trojan_z.append(z)
    
    # Apply center position offset
    trojan_x = np.array(trojan_x) + center_x
    trojan_y = np.array(trojan_y) + center_y
    trojan_z = np.array(trojan_z) + center_z
    
    # Create hover text
    trojan_text = ["Jupiter Trojans (L5 - Trojans): Asteroids trapped at Jupiter's trailing<br>"
                   "Lagrange point (L5), 60 deg behind. Called 'Trojan camp' after Iliad heroes.<br>"
                   "Slightly less populated than L4, contains D-type asteroids."] * len(trojan_x)
    trojan_customdata = ['Jupiter Trojans (Trojans - L5)'] * len(trojan_x)
    
    traces = [
        go.Scatter3d(
            x=trojan_x,
            y=trojan_y,
            z=trojan_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(160, 80, 80)',  # Slightly darker reddish
                opacity=0.5
            ),
            name='Jupiter Trojans (Trojans - L5)',
            text=trojan_text,
            customdata=trojan_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position,
        shell_radius=TROJAN_DISTANCE
    )
    for trace in sun_traces:
        traces.append(trace)
    
    return traces
