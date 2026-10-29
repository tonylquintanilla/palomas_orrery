"""
Asteroid Belt Visualization Module
===================================
Functions for creating visualizations of asteroid belt structures in 3D plots.
Includes Main Belt, Hildas, Trojans, and Greeks.
Also includes helper functions for dynamic Trojan positioning based on Jupiter's location.


Role: rendering/shells
Domain: orrery

Module updated: May 2026 with Anthropic's Claude Opus 4.6
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
May 27, 2026: Stage 3 info-marker standard sweep + Sun Direction cleanup
    (Opus 4.7). 4 info markers brought to red-border standard; 4 dormant
    sun_direction calls removed (dist=0 suppression branch -- zero
    behavior change, confirmed v9 Residual Cleanup item 2).
May 28, 2026: Phase 1 re-pipe (Opus 4.7). 4 live inline info markers
    routed through orrery_rendering.create_info_marker() factory
    (main belt, Hilda, Trojan L4, Trojan L5). Main belt preserves white
    fill via factory color arg. No visual change beyond factory routing.
May 29, 2026: Trojan L4/L5 info markers given border_color='white' for
    contrast against their reddish dot fields (Mode 5). Main belt and
    Hilda keep the factory default red border.
Module updated: October 27, 2026 with Anthropic's Claude Opus 5.5 (L-492:
    the stale "set manual scale" and "MB per frame" sentences removed
    from the hover and info text; the opening view frames every shell).
Module updated: October 28, 2026 with Anthropic's Claude Opus 5.5 (L-443:
    the main belt drawn as the stored cloud from main_belt_sampler.py,
    measured from JPL's main-belt orbits; its hover and tooltip one text
    from the rows; the typed edges, peak and gaps removed).
"""

import numpy as np
import plotly.graph_objs as go
from orrery_rendering import create_info_marker

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
# REMOVED 2026-10-28 (L-443): MAIN_BELT_INNER 2.2, MAIN_BELT_OUTER 3.2,
# MAIN_BELT_PEAK 2.7 and the five KIRKWOOD_GAPS, typed here with no source
# and used only by the main belt's old drawing. The belt is now drawn from
# rows measured from JPL's own orbits (main_belt_sampler.py).

HILDA_DISTANCE = 3.97  # Hilda group distance (3:2 resonance with Jupiter)
TROJAN_DISTANCE = 5.2  # Jupiter's orbital distance (L4 and L5 points)

#####################################
# Main Asteroid Belt
#####################################

# L-443 (2026-10-28): the checkbox's tooltip and the cloud's hover are one
# text, written from the rows by main_belt_sampler.hover_text(). The old
# tooltip's sentences named no source and described a drawing that is
# gone (its 2.2 to 3.2 AU, its peak at 2.7 AU, its gaps).
import main_belt_sampler as _mbs
main_belt_info = _mbs.hover_text(br="\n")


def create_main_asteroid_belt(center_position=(0, 0, 0)):
    """
    The main asteroid belt as the stored cloud: dots placed at random
    inside the belt's spread measured from JPL's main-belt orbits
    (main_belt_sampler.drawn_main_belt, the same dots
    data/drawings/main_belt.json carries to the website). Not individual
    asteroids, and the same on every date (Tony's ruling of 2026-10-28,
    form B, L-443). REPLACED 2026-10-28: until then fresh random dots on
    every plot, between a typed 2.2 and 3.2 AU, with an eyeballed
    thickness and gaps.

    Parameters:
        center_position (tuple): (x, y, z) position of the Sun

    Returns:
        list: Plotly trace objects for the main belt
    """
    center_x, center_y, center_z = center_position
    rows = _mbs.rows_from_store()
    dots = _mbs.drawn_main_belt(rows)
    belt_x = np.array(dots['x'])
    belt_y = np.array(dots['y'])
    belt_z = np.array(dots['z'])

    # Rendering settings, as before: a colour from reddish-brown near the
    # Sun to grey-brown far out, across the drawing's two ends, and a
    # size between 0.8 and 2.0 from the drawing's own seed.
    near, far = _mbs.span(rows)
    radius = np.sqrt(belt_x ** 2 + belt_y ** 2 + belt_z ** 2)
    color_factor = np.clip((radius - near) / (far - near), 0.0, 1.0)
    belt_colors = ['rgb(%d, %d, %d)' % (int(180 + 30 * (1 - c)),
                                        int(140 + 20 * (1 - c)),
                                        int(100 + 30 * c))
                   for c in color_factor]
    belt_sizes = np.random.default_rng(dots['settings']['seed']).uniform(
        0.8, 2.0, len(belt_x))

    # Apply center position offset
    belt_x = belt_x + center_x
    belt_y = belt_y + center_y
    belt_z = belt_z + center_z

    belt_desc = _mbs.hover_text(rows)
    trace_name = 'Main Asteroid Belt'

    geom_trace = go.Scatter3d(
        x=belt_x, y=belt_y, z=belt_z,
        mode='markers',
        marker=dict(size=belt_sizes, color=belt_colors, opacity=0.4),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    info_trace = create_info_marker(
        belt_x[0], belt_y[0], belt_z[0],
        'white',
        f"{trace_name}<br><br>{belt_desc}",
        trace_name
    )
    traces = [geom_trace, info_trace]
    
    
    return traces

#####################################
# Hilda Family
#####################################

hilda_group_info = (
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
    hilda_desc = ("Hilda Family: Asteroids in 3:2 resonance with Jupiter at ~3.97 AU.<br>"
                  "Forms distinctive triangular pattern with three main concentrations<br>"
                  "120 deg apart. Mostly D-type (dark, reddish) asteroids.")
    trace_name = 'Hilda Family'
    
    geom_trace = go.Scatter3d(
        x=hilda_x, y=hilda_y, z=hilda_z,
        mode='markers',
        marker=dict(size=1.5, color='rgb(200, 170, 100)', opacity=0.5),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    info_trace = create_info_marker(
        hilda_x[0], hilda_y[0], hilda_z[0],
        'rgb(200, 170, 100)',
        f"{trace_name}<br><br>{hilda_desc}",
        trace_name
    )
    traces = [geom_trace, info_trace]
    
    
    return traces

#####################################
# Jupiter Trojans (L4 - Greeks)
#####################################

# Source: MPC Jupiter Trojan census; NASA Lucy mission; Marchis et al. (2006) -- Patroclus binary;
# Gemini fact-check Apr 2026: all claims correct (Hektor ~225-250 km, Achilles first discovered 1906)
jupiter_trojans_greeks_info = (
    "***PLOT WITH JUPITER***\n"
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
    # Source: MPC / NASA Lucy mission (lucy.swri.edu) -- D-type composition, L4 population
    trojan_desc = ("Jupiter Trojans (L4 - Greeks): Asteroids trapped at Jupiter's leading<br>"
                   "Lagrange point (L4), 60 deg ahead. Called 'Greek camp' after Iliad heroes.<br>"
                   "Contains thousands of D-type asteroids, targets of NASA's Lucy mission.")
    trace_name = 'Jupiter Trojans (Greeks - L4)'
    
    geom_trace = go.Scatter3d(
        x=trojan_x, y=trojan_y, z=trojan_z,
        mode='markers',
        marker=dict(size=1.5, color='rgb(180, 100, 100)', opacity=0.5),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    info_trace = create_info_marker(
        trojan_x[0], trojan_y[0], trojan_z[0],
        'rgb(180, 100, 100)',
        f"{trace_name}<br><br>{trojan_desc}",
        trace_name,
        border_color='white'  # Trojan camps: white border for contrast vs reddish dots (May 29, 2026)
    )
    traces = [geom_trace, info_trace]
    
    
    return traces

#####################################
# Jupiter Trojans (L5 - Trojans)
#####################################

jupiter_trojans_trojans_info = (
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
    trojan_desc = ("Jupiter Trojans (L5 - Trojans): Asteroids trapped at Jupiter's trailing<br>"
                   "Lagrange point (L5), 60 deg behind. Called 'Trojan camp' after Iliad heroes.<br>"
                   "Slightly less populated than L4, contains D-type asteroids.")
    trace_name = 'Jupiter Trojans (Trojans - L5)'
    
    geom_trace = go.Scatter3d(
        x=trojan_x, y=trojan_y, z=trojan_z,
        mode='markers',
        marker=dict(size=1.5, color='rgb(160, 80, 80)', opacity=0.5),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    info_trace = create_info_marker(
        trojan_x[0], trojan_y[0], trojan_z[0],
        'rgb(160, 80, 80)',
        f"{trace_name}<br><br>{trojan_desc}",
        trace_name,
        border_color='white'  # Trojan camps: white border for contrast vs reddish dots (May 29, 2026)
    )
    traces = [geom_trace, info_trace]
    
    
    return traces
