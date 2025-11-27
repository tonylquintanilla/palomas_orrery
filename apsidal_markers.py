"""
apsidal_markers.py

Module for calculating perihelion, apohelion, perigee, and apogee dates
based on current orbital positions and orbital elements.

This module provides functions to:
- Calculate true anomaly from 3D position
- Convert between anomaly types (true, eccentric, mean)
- Calculate dates for apsidal points (perihelion/apohelion, perigee/apogee)
- Add apsidal markers to Plotly 3D plots
"""

import numpy as np
import plotly.graph_objects as go
from constants_new import KNOWN_ORBITAL_PERIODS, color_map
from datetime import datetime, timedelta

# ADD THIS TO YOUR apsidal_markers.py FILE
# Place this section right after the imports, before any other function definitions

# ========== APSIDAL TERMINOLOGY SYSTEM ==========
# Maps central body to (periapsis_term, apoapsis_term)
APSIDAL_TERMINOLOGY = {
    'Sun': ('Perihelion', 'Aphelion'),
    '10': ('Perihelion', 'Aphelion'),  # Sun by ID
    'Mercury': ('Perihermion', 'Aphermion'),
    '199': ('Perihermion', 'Aphermion'),  # Mercury by ID
    'Venus': ('Pericytherion', 'Apocytherion'),
    '299': ('Pericytherion', 'Apocytherion'),  # Venus by ID
    'Earth': ('Perigee', 'Apogee'),
    '399': ('Perigee', 'Apogee'),  # Earth by ID
    'Moon': ('Periselene', 'Aposelene'),
    '301': ('Periselene', 'Aposelene'),  # Moon by ID
    'Mars': ('Periareion', 'Apoareion'),
    '499': ('Periareion', 'Apoareion'),  # Mars by ID
    'Jupiter': ('Perijove', 'Apojove'),
    '599': ('Perijove', 'Apojove'),  # Jupiter by ID
    'Saturn': ('Perisaturnium', 'Aposaturnium'),  # Also: Perichronon/Apochronon
    '699': ('Perisaturnium', 'Aposaturnium'),  # Saturn by ID
    'Uranus': ('Periuranion', 'Apouranion'),
    '799': ('Periuranion', 'Apouranion'),  # Uranus by ID
    'Neptune': ('Periposeidion', 'Apoposeidion'),
    '899': ('Periposeidion', 'Apoposeidion'),  # Neptune by ID
    'Pluto': ('Perihadion', 'Apohadion'),
    '999': ('Perihadion', 'Apohadion'),  # Pluto by ID
}

def get_apsidal_terms(center_body):
    """
    Get appropriate apsidal terminology for a given central body.
    
    Parameters:
        center_body: Name or ID of the central body (str or int)
        
    Returns:
        tuple: (periapsis_term, apoapsis_term)
        
    Examples:
        >>> get_apsidal_terms('Sun')
        ('Perihelion', 'Aphelion')
        >>> get_apsidal_terms('Jupiter')
        ('Perijove', 'Apojove')
        >>> get_apsidal_terms('599')  # Jupiter by ID
        ('Perijove', 'Apojove')
        >>> get_apsidal_terms('Ceres')  # Unknown body
        ('Periapsis', 'Apoapsis')
    """
    # Convert to string if numeric ID
    center_key = str(center_body)
    
    # Try exact match first
    if center_key in APSIDAL_TERMINOLOGY:
        return APSIDAL_TERMINOLOGY[center_key]
    
    # Try case-insensitive match for names
    for key, value in APSIDAL_TERMINOLOGY.items():
        if key.lower() == center_key.lower():
            return value
    
    # Fallback to generic terms for unknown bodies
    return ('Periapsis', 'Apoapsis')

def calculate_orbital_angle_shift(ideal_pos, actual_pos):
    """
    Calculate the angular separation between Keplerian and actual positions.
    Both positions should be dictionaries with 'x', 'y', 'z' keys.
    """
    import numpy as np
    
    # Convert positions to vectors
    ideal_vec = np.array([ideal_pos['x'], ideal_pos['y'], ideal_pos['z']])
    actual_vec = np.array([actual_pos['x'], actual_pos['y'], actual_pos['z']])
    
    # Calculate magnitudes (should be similar for perihelion)
    ideal_r = np.linalg.norm(ideal_vec)
    actual_r = np.linalg.norm(actual_vec)
    
    # Calculate angle between vectors using dot product
    dot_product = np.dot(ideal_vec, actual_vec)
    cos_angle = dot_product / (ideal_r * actual_r)
    
    # Handle numerical errors
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    
    # Calculate angle in degrees
    angle_deg = np.degrees(np.arccos(cos_angle))
    
    # Calculate distance difference as well
    delta_r = abs(actual_r - ideal_r)
    
    return angle_deg, delta_r, ideal_r, actual_r

def create_enhanced_apsidal_hover_text(obj_name, marker_type, date, actual_pos, 
                                       ideal_pos=None, params=None, is_perihelion=True,
                                       center_body='Sun'):
    """
    Create informative hover text for apsidal markers with perturbation notes.
    """
    import numpy as np
    
    # Base hover text
    actual_r = np.sqrt(actual_pos['x']**2 + actual_pos['y']**2 + actual_pos['z']**2)
    
    hover_text = f"<b>{obj_name} {marker_type}</b><br>"
    hover_text += f"Date: {date}<br>"        
    hover_text += f"Distance from {center_body}: {actual_r:.6f} AU<br>"
    
    # DEBUG: Log all conditions for perturbation analysis
    print(f"[HOVER DEBUG] {obj_name} {marker_type}:", flush=True)
    print(f"  ideal_pos is not None: {ideal_pos is not None}", flush=True)
    print(f"  params is not None: {params is not None}", flush=True)
    if params:
        print(f"  'epoch' in params: {'epoch' in params}", flush=True)
        if 'epoch' in params:
            print(f"  epoch value: {params['epoch']}", flush=True)
    
    # Add perturbation analysis if we have ideal position
    if ideal_pos and params and 'epoch' in params:
        angle_deg, delta_r, ideal_r, actual_r = calculate_orbital_angle_shift(ideal_pos, actual_pos)
        print(f"  angle_deg: {angle_deg:.3f}°", flush=True)
        
        # Determine if this is significant

        # Determine if this is significant
        epoch = params.get('epoch', 'unknown')
        
        if angle_deg > 0.5:  # Significant perturbation detected
            hover_text += "<br><b>Perturbation Analysis:</b><br>"
            hover_text += f"Keplerian orbit epoch: {epoch}<br>"
            
            # Add angular shift
            if angle_deg > 10:
                hover_text += f"<b>Angular shift: {angle_deg:.1f}°</b> (high)<br>"
            elif angle_deg > 5:
                hover_text += f"Angular shift: {angle_deg:.1f}° (moderate)<br>"
            else:
                hover_text += f"Angular shift: {angle_deg:.3f}° (low)<br>"
            
            # Add distance comparison
            hover_text += f"Keplerian distance: {ideal_r:.6f} AU<br>"
            hover_text += f"Actual distance: {actual_r:.6f} AU<br>"
            hover_text += f"Difference: {delta_r:.6f} AU<br>"
            
            # Add explanation based on time span
            if is_perihelion and 'TP' in params:
                from astropy.time import Time
                tp_time = Time(params['TP'], format='jd')
                years_from_epoch = (tp_time.datetime.year - int(epoch.split('-')[0]))
                
                if years_from_epoch > 20:
                    hover_text += f"<br><i>Note: {years_from_epoch} years of perturbations<br>"
                    hover_text += "from Jupiter/Saturn have shifted the orbit</i><br>"
                elif years_from_epoch > 5:
                    hover_text += f"<br><i>Note: {years_from_epoch} years of accumulated<br>"
                    hover_text += "perturbations since epoch</i><br>"
            
            # Special note for high eccentricity objects
            if params.get('e', 0) > 0.9:
                hover_text += "<br><i>High eccentricity makes this object<br>"
                hover_text += "particularly sensitive to perturbations</i><br>"
            
        else:  # Low deviation at this point
            hover_text += "<br><b>Perturbation Analysis:</b><br>"
            hover_text += f"Keplerian orbit epoch: {epoch}<br>"
            hover_text += f"Angular shift: {angle_deg:.3f}° (low)<br>"
            hover_text += f"Keplerian distance: {ideal_r:.6f} AU<br>"
            hover_text += f"Actual distance: {actual_r:.6f} AU<br>"
            hover_text += f"Difference: {delta_r:.6f} AU<br>"
            hover_text += "<i>Note: Low deviation expected near epoch.<br>"
            hover_text += "Osculating orbit is calibrated to match<br>"
            hover_text += "position & velocity at this moment.</i><br>"

    return hover_text

def add_actual_apsidal_markers_enhanced(fig, obj_name, params, date_range, positions_dict, 
                                       color_map, center_body='Sun', is_satellite=False,
                                       ideal_apsides=None, filter_by_date_range=True):
    """
    Enhanced version that compares actual vs Keplerian positions.
    Maintains all original parameters for backward compatibility.
    
    Parameters:
        fig: Plotly figure object
        obj_name: Name of the object
        params: Orbital parameters dictionary
        date_range: Tuple of (start_date, end_date) for filtering
        positions_dict: Dictionary of positions at apsidal dates
        color_map: Function to get color for object
        center_body: Name of central body (Sun, planet, etc.)
        is_satellite: Boolean indicating if this is a satellite
        ideal_apsides: Dictionary with 'periapsis' and 'apoapsis' Keplerian positions
        filter_by_date_range: If False, plot all apsidal dates in positions_dict
            regardless of date_range (useful for future apsides)
    """
    from datetime import datetime
    import plotly.graph_objects as go
      
    # Get parent-specific terminology (same as ideal markers)
#    near_term, far_term = get_apsidal_terms(center_body)
#    near_label = f"Actual {near_term}"
#    far_label = f"Actual {far_term}"

    # Get parent-specific terminology (same as ideal markers)
    near_term, far_term = get_apsidal_terms(center_body)
    
    # Add epoch to label if available
    epoch = params.get('epoch', '')
    if epoch:
        epoch_suffix = f" (Epoch: {epoch})"
    else:
        epoch_suffix = ""
    
    near_label = f"Keplerian {near_term}{epoch_suffix}"
    far_label = f"Keplerian {far_term}{epoch_suffix}"

    # Use same key names for ALL objects
    near_dates = params.get('perihelion_dates', [])
    far_dates = params.get('aphelion_dates', [])

    # Convert date strings to datetime objects for comparison
    near_dates_dt = []
    for d in near_dates:
        try:
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            dt = datetime.strptime(d, '%Y-%m-%d')
        near_dates_dt.append(dt)
    
    far_dates_dt = []
    for d in far_dates:
        try:
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            dt = datetime.strptime(d, '%Y-%m-%d')
        far_dates_dt.append(dt)
    
    # Filter dates if date_range is provided
#    if date_range:
    if date_range and filter_by_date_range:
        start_date, end_date = date_range
        near_dates_dt = [d for d in near_dates_dt if start_date <= d <= end_date]
        far_dates_dt = [d for d in far_dates_dt if start_date <= d <= end_date]
    
    # Add markers for near points (perihelion/perigee)
    for date in near_dates_dt:
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            actual_pos = positions_dict[date_key]
            
            # Get ideal position if available
            ideal_pos = ideal_apsides.get('periapsis') if ideal_apsides else None
            
            # Create enhanced hover text
            hover_text = create_enhanced_apsidal_hover_text(
                obj_name, 
                near_label,
                date.strftime('%Y-%m-%d %H:%M:%S'),
                actual_pos,
                ideal_pos,
                params,
                is_perihelion=True,
                center_body=center_body
            )
            
            fig.add_trace(go.Scatter3d(
                x=[actual_pos['x']],
                y=[actual_pos['y']],
                z=[actual_pos['z']],
                mode='markers',
                marker=dict(
                    size=8,
                    color='white',
                    symbol='square-open'
                ),
                name=f"{obj_name} {near_label}",
                text=[hover_text],
                customdata=[f"{obj_name} {near_label}"],  # Added
                hovertemplate='%{text}<extra></extra>',   # Fixed format
                showlegend=True
            ))
    
    # Add markers for far points (aphelion/apogee)
    for date in far_dates_dt:
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            actual_pos = positions_dict[date_key]
            
            # Get ideal position if available
            ideal_pos = ideal_apsides.get('apoapsis') if ideal_apsides else None
            
            hover_text = create_enhanced_apsidal_hover_text(
                obj_name,
                far_label, 
                date.strftime('%Y-%m-%d %H:%M:%S'),
                actual_pos,
                ideal_pos,
                params,
                is_perihelion=False,
                center_body=center_body
            )
            
            fig.add_trace(go.Scatter3d(
                x=[actual_pos['x']],
                y=[actual_pos['y']],
                z=[actual_pos['z']],
                mode='markers',
                marker=dict(
                    size=8,
                    color='white',
                    symbol='square-open'
                ),
                name=f"{obj_name} {far_label}",
                text=[hover_text],
                customdata=[f"{obj_name} {far_label}"],  # Added
                hovertemplate='%{text}<extra></extra>',   # Fixed format
                showlegend=True
            ))

def calculate_exact_apsides(a, e, i, omega, Omega, rotate_points):
    """
    Calculate exact apsidal positions at theta=0 (periapsis) and theta=pi (apoapsis).
    Uses the mathematical fact that periapsis is always at true anomaly = 0
    and apoapsis is always at true anomaly = pi.
    
    Parameters:
        a: Semi-major axis (AU)
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
        rotate_points: Function to rotate points in 3D space
        
    Returns:
        dict: {
            'periapsis': {'x': float, 'y': float, 'z': float, 'distance': float},
            'apoapsis': {'x': float, 'y': float, 'z': float, 'distance': float} or None
        }
    """
    import numpy as np
    
    # Convert angles to radians for rotations
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # ========== CALCULATE PERIAPSIS AT THETA=0 ==========
    theta_periapsis = 0.0
    
    # Calculate radius at periapsis
    if e < 1:  # Elliptical orbit
        # r = a(1-e²)/(1+e*cos(θ)) at θ=0 becomes r = a(1-e²)/(1+e) = a(1-e)
        r_periapsis = a * (1 - e)
    else:  # Hyperbolic orbit (e >= 1)
        # r = |a|(e²-1)/(1+e*cos(θ)) at θ=0 becomes r = |a|(e²-1)/(1+e) = |a|(e-1)
        r_periapsis = abs(a) * (e - 1)
    
    # Position in orbital plane at theta=0
    x_orbit_peri = r_periapsis  # r * cos(0) = r
    y_orbit_peri = 0.0          # r * sin(0) = 0
    z_orbit_peri = 0.0
    
    # Apply orbital element rotations to transform from orbital plane to 3D space
    # 1. Rotate by argument of periapsis (ω) around z-axis
    x_temp, y_temp, z_temp = rotate_points([x_orbit_peri], [y_orbit_peri], [z_orbit_peri], omega_rad, 'z')
    # 2. Rotate by inclination (i) around x-axis
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
    # 3. Rotate by longitude of ascending node (Ω) around z-axis
    x_peri, y_peri, z_peri = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
    
    # Extract single point (rotate_points returns arrays)
    peri_x = x_peri[0]
    peri_y = y_peri[0]
    peri_z = z_peri[0]
    peri_distance = np.sqrt(peri_x**2 + peri_y**2 + peri_z**2)
    
    # Create periapsis result
    periapsis_result = {
        'x': peri_x,
        'y': peri_y,
        'z': peri_z,
        'distance': peri_distance
    }
    
    # ========== CALCULATE APOAPSIS AT THETA=PI (for elliptical only) ==========
    apoapsis_result = None
    
    if e < 1:  # Only elliptical orbits have apoapsis
        theta_apoapsis = np.pi  # 180 degrees
        
        # Calculate radius at apoapsis
        # r = a(1-e²)/(1+e*cos(θ)) at θ=π becomes r = a(1-e²)/(1-e) = a(1+e)
        r_apoapsis = a * (1 + e)
        
        # Position in orbital plane at theta=pi
        x_orbit_apo = r_apoapsis * np.cos(theta_apoapsis)  # r * cos(π) = -r
        y_orbit_apo = r_apoapsis * np.sin(theta_apoapsis)  # r * sin(π) = 0
        z_orbit_apo = 0.0
        
        # Apply orbital element rotations
        # 1. Rotate by argument of periapsis (ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points([x_orbit_apo], [y_orbit_apo], [z_orbit_apo], omega_rad, 'z')
        # 2. Rotate by inclination (i) around x-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        # 3. Rotate by longitude of ascending node (Ω) around z-axis
        x_apo, y_apo, z_apo = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Extract single point
        apo_x = x_apo[0]
        apo_y = y_apo[0]
        apo_z = z_apo[0]
        apo_distance = np.sqrt(apo_x**2 + apo_y**2 + apo_z**2)
        
        # Create apoapsis result
        apoapsis_result = {
            'x': apo_x,
            'y': apo_y,
            'z': apo_z,
            'distance': apo_distance
        }
    
    return {
        'periapsis': periapsis_result,
        'apoapsis': apoapsis_result
    }

def add_apsidal_range_note(fig, obj_name, perihelion_date, aphelion_date, color_map):
    """
    Add legend entries explaining why actual apsidal markers aren't shown
    when dates are outside JPL Horizons' range.
    Now creates separate legend entries for perihelion and aphelion.
    """
    from datetime import datetime
    import plotly.graph_objects as go
    
    # JPL Horizons data limit
    JPL_MAX_DATE = datetime(2199, 12, 29)
    JPL_MIN_DATE = datetime(1900, 1, 1)
    
    added_notes = False
    
    # Check and add perihelion note separately
    if perihelion_date:
        if perihelion_date > JPL_MAX_DATE:
            date_str = perihelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Next perihelion: {date_str} (beyond JPL limit)"
            
            # Add an invisible trace for perihelion
            fig.add_trace(
                go.Scatter3d(
                    x=[None],  # No actual points
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square-open'  # Open square for perihelion
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'  # Don't show hover for this invisible trace
                )
            )
            added_notes = True
            
        elif perihelion_date < JPL_MIN_DATE:
            date_str = perihelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Perihelion: {date_str} (before JPL limit)"
            
            fig.add_trace(
                go.Scatter3d(
                    x=[None],
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square-open'
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'
                )
            )
            added_notes = True
    
    # Check and add aphelion note separately
    if aphelion_date:
        if aphelion_date > JPL_MAX_DATE:
            date_str = aphelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Next aphelion: {date_str} (beyond JPL limit)"
            
            # Add an invisible trace for aphelion
            fig.add_trace(
                go.Scatter3d(
                    x=[None],  # No actual points
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square-open'  # Solid square for aphelion
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'  # Don't show hover for this invisible trace
                )
            )
            added_notes = True
            
        elif aphelion_date < JPL_MIN_DATE:
            date_str = aphelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Aphelion: {date_str} (before JPL limit)"
            
            fig.add_trace(
                go.Scatter3d(
                    x=[None],
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square-open'
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'
                )
            )
            added_notes = True
    
    return added_notes

def estimate_hyperbolic_perihelion_date(current_position, q, e, date):
    """
    Estimate perihelion date for hyperbolic orbits.
    """
    if not current_position or 'x' not in current_position or not date:
        return "Date unknown"
    
    try:
        current_dist = np.sqrt(
            current_position['x']**2 + 
            current_position['y']**2 + 
            current_position['z']**2
        )
        
        if current_dist > q:  # Still approaching perihelion
            distance_to_go = current_dist - q
            
            # Rough velocity estimate for hyperbolic orbit (AU/day)
            if e > 5:  # Very hyperbolic
                estimated_velocity = 0.1
            else:  # Near-parabolic
                estimated_velocity = 0.05
            
            days_to_perihelion = distance_to_go / estimated_velocity
            
            if days_to_perihelion < 365:
                perihelion_date = date + timedelta(days=days_to_perihelion)
                return perihelion_date.strftime('%Y-%m-%d') + " (est)"
            else:
                return "Approaching"
        else:
            return "Near/Past perihelion"
            
    except Exception as e:
        print(f"Error estimating hyperbolic perihelion: {e}", flush=True)
        return "Approaching"

def compute_apsidal_dates_from_tp(obj_name, params, current_date=None):
    """
    Get perihelion from TP and aphelion from Tapo.
    These are the actual apsidal dates from ephemeris/observations.
    """
    from astropy.time import Time
    
    next_perihelion = None
    next_aphelion = None
    
    # Handle perihelion from TP
    if 'TP' in params:
        tp_jd = params['TP']
        tp_time = Time(tp_jd, format='jd')
        next_perihelion = tp_time.datetime
        print(f"  {obj_name}: Using TP for perihelion: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    
    # Handle aphelion from Tapo
    if 'Tapo' in params:
        tapo_jd = params['Tapo']
        tapo_time = Time(tapo_jd, format='jd')
        next_aphelion = tapo_time.datetime
        print(f"  {obj_name}: Using Tapo for aphelion: {next_aphelion.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    elif params.get('e', 0) < 1:
        # Only print warning for elliptical orbits (which should have aphelion)
        print(f"  {obj_name}: No Tapo provided - actual aphelion marker will not be plotted", flush=True)
    
    return next_perihelion, next_aphelion

def add_actual_apsidal_markers(fig, obj_name, params, date_range, positions_dict, color_map, 
                             center_body='Sun', is_satellite=False):
    """
    Add markers for actual perihelion/aphelion (or perigee/apogee) dates.
    
    Parameters:
    -----------
    fig : plotly.graph_objects.Figure
        The figure to add markers to
    obj_name : str
        Name of the celestial object
    params : dict
        Orbital parameters including actual apsidal dates
    date_range : tuple
        (start_date, end_date) to filter which markers to show
    positions_dict : dict
        Dictionary mapping dates to positions {'YYYY-MM-DD': {'x': x, 'y': y, 'z': z}}
    color_map : function
        Function to get color for the object
    center_body : str
        Name of the central body
    is_satellite : bool
        True if object is a satellite (use perigee/apogee instead of perihelion/aphelion)
    """
    from datetime import datetime
    import numpy as np
    import plotly.graph_objects as go
    
    # Handle the case where date_range might be None
    if date_range:
        start_date, end_date = date_range
    else:
        # If no date range, we'll show all markers
        start_date = None
        end_date = None
    
    # Determine which date lists to use
    if is_satellite:
        near_dates = params.get('perigee_dates', [])
        far_dates = params.get('apogee_dates', [])
        near_label = 'Perigee'
        far_label = 'Apogee'
    else:
        near_dates = params.get('perihelion_dates', [])
        far_dates = params.get('aphelion_dates', [])
        near_label = 'Perihelion'
        far_label = 'Aphelion'
    
    # Convert string dates to datetime objects for processing
    # Handle both old format (%Y-%m-%d) and new format (%Y-%m-%d %H:%M:%S)

    near_dates_dt = []
    for d in near_dates:
        try:
            # Try full datetime format first
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Fall back to date-only format
            dt = datetime.strptime(d, '%Y-%m-%d')
        near_dates_dt.append(dt)

    far_dates_dt = []
    for d in far_dates:
        try:
            # Try full datetime format first
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Fall back to date-only format
            dt = datetime.strptime(d, '%Y-%m-%d')
        far_dates_dt.append(dt)

    # Add markers for near points (perihelion/perigee)
    for i, date in enumerate(near_dates_dt):
#        date_str = near_dates[i]  # Get the original string format
        
        # Extract just the date part for position lookup
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            pos = positions_dict[date_key]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
            
            # Display full datetime if available
            date_display = date.strftime('%Y-%m-%d %H:%M:%S')
            
            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
                    mode='markers',                    
                    marker=dict(
                        size=8,
                        color='white',                        
                        symbol='square-open',  
                    ),

                    name=f"{obj_name} Actual {near_label}",
                    text=[f"<b>{obj_name} at {near_label}</b><br>"
                        f"Date: {date_display} UTC<br>"
                        f"Distance from {center_body}: {distance_au:.6f} AU"],
                    customdata=[f"{obj_name} Actual {near_label}"],  
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True

                )
            )

    # Add markers for far points (aphelion/apogee)
    for i, date in enumerate(far_dates_dt):
        date_str = far_dates[i]  # Get the original string format
        
        # Extract just the date part for position lookup
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            pos = positions_dict[date_key]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
            
            # Display full datetime if available
            date_display = date.strftime('%Y-%m-%d %H:%M:%S')
            
            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
                    mode='markers',                    
                    marker=dict(
                        size=8,
                        color='white',                        
                        symbol='square-open',  # open square for actual
                    ),

                    name=f"{obj_name} Actual {far_label}",  # Fixed: far_label
                    text=[f"<b>{obj_name} at {far_label}</b><br>"  # Fixed: far_label
                        f"Date: {date_display} UTC<br>"
                        f"Distance from {center_body}: {distance_au:.6f} AU"],
                    customdata=[f"{obj_name} Actual {far_label}"],  # Fixed: far_label                    

                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True

                )
            )

def fetch_positions_for_apsidal_dates(obj_id, params, date_range, center_id='Sun', 
                                    id_type=None, is_satellite=False, fetch_position=None):
    """
    Fetch actual positions for all apsidal dates within the date range.
    
    Returns:
        dict: Mapping of date strings to position dictionaries
    """
    from datetime import datetime

    if fetch_position is None:
        raise ValueError("fetch_position function must be provided")

    positions = {}

    # Remove the line that unpacks date_range since we're not using it
#    start_date, end_date = date_range
    
    # Get all apsidal dates
#    if is_satellite:
#        all_dates = params.get('perigee_dates', []) + params.get('apogee_dates', [])
#    else:
#        all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])
    
    # Use perihelion/aphelion for all objects (satellites and planets)
    all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])

    for date_str in all_dates:
        try:
            # Try to parse with time first, then fall back to date-only
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            
            # Always fetch, no date range check
            pos_data = fetch_position(obj_id, date_obj, center_id=center_id, id_type=id_type)
            if pos_data and 'x' in pos_data:
                # Store with date-only key for compatibility
                date_key = date_obj.strftime('%Y-%m-%d')
                positions[date_key] = pos_data
                print(f"    Fetched position for {date_str}", flush=True)

        except Exception as e:
            print(f"    Could not fetch position for {date_str}: {e}", flush=True)                
    
    return positions

def get_orbital_period_days(body_name, semi_major_axis_au=None):
    """
    Get orbital period in Earth days for a given body.
    
    Parameters:
    -----------
    body_name : str
        Name of the celestial body
    semi_major_axis_au : float, optional
        Semi-major axis in AU (used for unknown bodies via Kepler's third law)
    
    Returns:
    --------
    float
        Orbital period in Earth days
    """
    if body_name in KNOWN_ORBITAL_PERIODS:
        period = KNOWN_ORBITAL_PERIODS[body_name]
        # Handle special cases (hyperbolic/parabolic objects)
        if period is None:
            if semi_major_axis_au:
                # For hyperbolic/parabolic orbits, use Kepler's third law
                # This gives a notional period for visualization purposes
                return 365.25 * np.sqrt(abs(semi_major_axis_au)**3)
            else:
                raise ValueError(f"{body_name} has no defined orbital period (hyperbolic/parabolic orbit)")
        return period
    elif semi_major_axis_au:
        # Use Kepler's third law as fallback for unknown bodies
        # P² = a³ (where P is in years and a is in AU)
        # So P_days = 365.25 * sqrt(a³)
        return 365.25 * np.sqrt(abs(semi_major_axis_au)**3)
    else:
        raise ValueError(f"Unknown body {body_name} and no semi-major axis provided")

def calculate_true_anomaly_from_position(x, y, z, a, e, i, omega, Omega):
    """
    Calculate the true anomaly from a position in 3D space.
    
    Parameters:
        x, y, z: Current position in heliocentric/planetocentric coordinates (AU or km)
        a: Semi-major axis (same units as position)
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
    
    Returns:
        float: True anomaly in radians (0 to 2π)
    """
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Reverse rotation transformations to get back to orbital plane
    # First, reverse the Omega rotation (around z-axis)
    x1 = x * np.cos(-Omega_rad) - y * np.sin(-Omega_rad)
    y1 = x * np.sin(-Omega_rad) + y * np.cos(-Omega_rad)
    z1 = z
    
    # Then, reverse the inclination rotation (around x-axis)
    x2 = x1
    y2 = y1 * np.cos(-i_rad) - z1 * np.sin(-i_rad)
    z2 = y1 * np.sin(-i_rad) + z1 * np.cos(-i_rad)
    
    # Finally, reverse the omega rotation (around z-axis)
    x_orbital = x2 * np.cos(-omega_rad) - y2 * np.sin(-omega_rad)
    y_orbital = x2 * np.sin(-omega_rad) + y2 * np.cos(-omega_rad)
    
    # Calculate true anomaly
    true_anomaly = np.arctan2(y_orbital, x_orbital)
    
    # Ensure positive angle (0 to 2π)
    if true_anomaly < 0:
        true_anomaly += 2 * np.pi
    
    return true_anomaly


def true_to_eccentric_anomaly(true_anomaly, e):
    """
    Convert true anomaly to eccentric anomaly.
    
    Parameters:
        true_anomaly: True anomaly in radians
        e: Eccentricity
    
    Returns:
        float: Eccentric anomaly in radians (or hyperbolic eccentric anomaly for e > 1)
    """
    if e < 1:  # Elliptical orbit
        # For elliptical orbits
        cos_E = (e + np.cos(true_anomaly)) / (1 + e * np.cos(true_anomaly))
        sin_E = np.sqrt(1 - e**2) * np.sin(true_anomaly) / (1 + e * np.cos(true_anomaly))
        E = np.arctan2(sin_E, cos_E)
        
        # Ensure E is positive
        if E < 0:
            E += 2 * np.pi
            
        return E
        
    else:  # Hyperbolic orbit (e > 1)
        # For hyperbolic orbits, use hyperbolic eccentric anomaly
        if abs(true_anomaly) > np.arccos(-1/e):
            # True anomaly is beyond the asymptote - invalid for hyperbolic orbit
            return float('nan')
            
        cosh_F = (e + np.cos(true_anomaly)) / (1 + e * np.cos(true_anomaly))
        F = np.arccosh(cosh_F)
        
        # F should have the same sign as true anomaly
        if true_anomaly > np.pi:
            F = -F
            
        return F


def eccentric_to_mean_anomaly(E, e):
    """
    Convert eccentric anomaly to mean anomaly.
    Uses Kepler's equation.
    
    Parameters:
        E: Eccentric anomaly in radians (or hyperbolic eccentric anomaly)
        e: Eccentricity
    
    Returns:
        float: Mean anomaly in radians
    """
    if e < 1:  # Elliptical orbit
        M = E - e * np.sin(E)
    else:  # Hyperbolic orbit
        M = e * np.sinh(E) - E  # M = e*sinh(F) - F for hyperbolic
    return M


def calculate_time_to_anomaly(current_M, target_M, orbital_period_days):
    """
    Calculate time to reach a target mean anomaly from current mean anomaly.
    
    Parameters:
        current_M: Current mean anomaly (radians)
        target_M: Target mean anomaly (radians)
        orbital_period_days: Orbital period in days
    
    Returns:
        float: Days until target anomaly is reached
    """
    # Calculate angular distance (always forward in time)
    if target_M >= current_M:
        delta_M = target_M - current_M
    else:
        delta_M = (2 * np.pi) + target_M - current_M
    
    # Convert to time
    fraction_of_orbit = delta_M / (2 * np.pi)
    days_to_target = fraction_of_orbit * orbital_period_days
    
    return days_to_target


def calculate_apsidal_dates(date, current_x, current_y, current_z, a, e, i, omega, Omega, body_name="Object"):
    """
    Calculate dates for perihelion/apohelion (or perigee/apogee for satellites).
    
    Parameters:
        date: Current date (datetime object)
        current_x, current_y, current_z: Current position
        a: Semi-major axis
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
        body_name: Name of the body (for error messages)
    
    Returns:
        tuple: (perihelion_date, apohelion_date) or (None, None) if calculation fails
    """
    try:
        # Calculate current true anomaly
        current_theta = calculate_true_anomaly_from_position(
            current_x, current_y, current_z, a, e, i, omega, Omega
        )
        
        if e >= 1:  # Hyperbolic orbit
            # For hyperbolic orbits, apohelion doesn't exist
            # Check if we're approaching or past perihelion
            if current_theta < np.pi:
                # Approaching perihelion - estimate time
                if current_theta < 0.1:  # Very close
                    perihelion_date = date
                else:
                    # Rough estimate for hyperbolic approach
                    # This is simplified - proper calculation would be complex
                    days_estimate = 30 * (1 - current_theta/np.pi)
                    perihelion_date = date + timedelta(days=days_estimate)
            else:
                # Past perihelion
                perihelion_date = None
                
            return perihelion_date, None
                
        # For elliptical orbits
        # Get orbital period using the helper function
        try:
            orbital_period_days = get_orbital_period_days(body_name, a)
        except ValueError:
            # If body not found and no semi-major axis, use default
            print(f"Warning: Using Kepler's law for unknown body {body_name}", flush=True)
            orbital_period_days = 365.25 * np.sqrt(abs(a)**3)

        # Convert current position to mean anomaly
        E_current = true_to_eccentric_anomaly(current_theta, e)
        M_current = eccentric_to_mean_anomaly(E_current, e)
        
        # Perihelion is at M = 0
        days_to_perihelion = calculate_time_to_anomaly(M_current, 0, orbital_period_days)
        perihelion_date = date + timedelta(days=days_to_perihelion)
        
        # Apohelion is at M = π
        days_to_apohelion = calculate_time_to_anomaly(M_current, np.pi, orbital_period_days)
        apohelion_date = date + timedelta(days=days_to_apohelion)
        
        return perihelion_date, apohelion_date
        
    except Exception as ex:
        print(f"Warning: Could not calculate apsidal dates for {body_name}: {ex}", flush=True)
        return None, None


def add_perihelion_marker(fig, x, y, z, obj_name, a, e, date, current_position, 
                        orbital_params, color_map, q=None, center_body='Sun'):
    """
    Add a perihelion/perigee marker with accurate date calculation.
    Now handles full datetime precision from TP and uses proper apsidal terminology.
    
    Parameters:
        fig: Plotly figure object
        x, y, z: Position coordinates in AU
        obj_name: Name of the orbiting object
        a: Semi-major axis in AU
        e: Eccentricity
        date: Current date for calculation
        current_position: Dictionary with 'x', 'y', 'z' keys
        orbital_params: Full orbital parameters dictionary
        color_map: Function to get color for object
        q: Periapsis distance (calculated if None)
        center_body: Name or ID of central body (Sun, Earth, Jupiter, etc.)
    """
    # Get proper apsidal terminology
    near_term, far_term = get_apsidal_terms(center_body)

    # Calculate perihelion distance if not provided
    if q is None:
        q = a * (1 - e)
    
    # Calculate perihelion date
    perihelion_date_str = ""
    if date is not None and current_position is not None and e < 1:
        perihelion_date, aphelion_date = calculate_apsidal_dates(
            date,
            current_position['x'],
            current_position['y'],
            current_position['z'],
            orbital_params.get('a', a),
            orbital_params.get('e', e),
            orbital_params.get('i', 0),
            orbital_params.get('omega', 0),
            orbital_params.get('Omega', 0),
            obj_name
        )
        
        if perihelion_date is not None:
            # For elliptical orbits with TP, we can calculate precise perihelion time
            if 'TP' in orbital_params and obj_name in KNOWN_ORBITAL_PERIODS:
                period_days = KNOWN_ORBITAL_PERIODS[obj_name]
                if period_days and period_days not in [None, 1e99]:  # Valid period
                    from astropy.time import Time
                    from datetime import timedelta
                    tp_time = Time(orbital_params['TP'], format='jd')
                    tp_datetime = tp_time.datetime
                    
                    # Find the next perihelion after the current date
                    precise_perihelion = tp_datetime
                    while precise_perihelion < date:
                        precise_perihelion += timedelta(days=period_days)
                    
                    perihelion_date_str = f"<br>Date: {precise_perihelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                else:
                    # For objects without precise period info
                    perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"
            else:
                # No TP available, use calculated date
                perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"

    # For hyperbolic orbits, use TP if available
    elif 'TP' in orbital_params and e >= 1:
        from astropy.time import Time
        tp_time = Time(orbital_params['TP'], format='jd')
        tp_datetime = tp_time.datetime
        perihelion_date_str = f"<br>Date: {tp_datetime.strftime('%Y-%m-%d %H:%M:%S')} UTC"
    elif date is not None:
        perihelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d')}"
    
    # Accuracy note
    accuracy_note = ""
    if e > 0.15:  # High eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.002 AU (strong perturbations)</i>"
    elif e > 0.05:  # Moderate eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.001 AU (moderate perturbations)</i>"
    else:  # Low eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.0005 AU (minimal perturbations)</i>"
    
    # SAFETY: Ensure we always have some date string
    if perihelion_date_str == "":
        perihelion_date_str = "<br>Date: Not calculated"
        print(f"WARNING: Could not calculate {near_term} date for {obj_name}", flush=True)
    
    # Use proper terminology for this central body
    label = f"Keplerian {near_term}"
    
    # Create hover text with all information
    # Ensure q is properly formatted
    try:
        q_str = f"{q:.6f}"
    except:
        q_str = str(q)
        print(f"WARNING: Could not format q value for {obj_name}: {q}", flush=True)
    
    hover_text = f"<b>{obj_name} {label}</b>{perihelion_date_str}<br>q={q_str} AU{accuracy_note}"
    
    # DEBUG: Uncomment these lines to diagnose hover text issues
    print(f"DEBUG: {obj_name} {label} hover text: {hover_text}", flush=True)
    
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=6,
                color=color_map(obj_name),
                symbol='square-open'
            ),
            name=f"{obj_name} {label}",
            text=[hover_text],
        #    customdata=[label],
            customdata=[f"{obj_name} {label}"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )


def add_apohelion_marker(fig, x, y, z, obj_name, a, e, date, current_position,
                        orbital_params, color_map, center_body='Sun'):
    """
    Add an apohelion/apogee marker to the plot with accurate date calculation.
    Now handles full datetime precision from TP and uses proper apsidal terminology.
    
    Parameters:
        fig: Plotly figure object
        x, y, z: Position coordinates in AU
        obj_name: Name of the orbiting object
        a: Semi-major axis in AU
        e: Eccentricity
        date: Current date for calculation
        current_position: Dictionary with 'x', 'y', 'z' keys
        orbital_params: Full orbital parameters dictionary
        color_map: Function to get color for object
        center_body: Name or ID of central body (Sun, Earth, Jupiter, etc.)
    """
    # Get proper apsidal terminology
    near_term, far_term = get_apsidal_terms(center_body)

    # Calculate aphelion distance
    if e < 1:
        Q = a * (1 + e)
    else:
        # No aphelion for hyperbolic orbits
        return
    
    # Calculate aphelion date
    aphelion_date_str = ""
    if date is not None and current_position is not None and e < 1:
        perihelion_date, aphelion_date = calculate_apsidal_dates(
            date,
            current_position['x'],
            current_position['y'],
            current_position['z'],
            orbital_params.get('a', a),
            orbital_params.get('e', e),
            orbital_params.get('i', 0),
            orbital_params.get('omega', 0),
            orbital_params.get('Omega', 0),
            obj_name
        )
        
        if aphelion_date is not None:
            # For elliptical orbits with TP, we can calculate precise aphelion time
            if 'TP' in orbital_params and obj_name in KNOWN_ORBITAL_PERIODS:
                period_days = KNOWN_ORBITAL_PERIODS[obj_name]
                if period_days and period_days != 1e99:  # Not a hyperbolic placeholder
                    from astropy.time import Time
                    from datetime import timedelta
                    tp_time = Time(orbital_params['TP'], format='jd')
                    tp_datetime = tp_time.datetime
                    # Aphelion is half period after perihelion
                    precise_aphelion = tp_datetime + timedelta(days=period_days/2)
                    # Adjust for multiple orbits if needed
                    while precise_aphelion < date:
                        precise_aphelion += timedelta(days=period_days)
                    aphelion_date_str = f"<br>Date: {precise_aphelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                else:
                    aphelion_date_str = f"<br>Date: {aphelion_date.strftime('%Y-%m-%d')}"
            else:
                aphelion_date_str = f"<br>Date: {aphelion_date.strftime('%Y-%m-%d')}"
    elif date is not None:
        aphelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d')}"
    
    # Accuracy note
    accuracy_note = ""
    if e > 0.15:  # High eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.002 AU (strong perturbations)</i>"
    elif e > 0.05:  # Moderate eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.001 AU (moderate perturbations)</i>"
    else:  # Low eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.0005 AU (minimal perturbations)</i>"
    
    # SAFETY: Ensure we always have some date string
    if aphelion_date_str == "":
        aphelion_date_str = "<br>Date: Not calculated"
        print(f"WARNING: Could not calculate {far_term} date for {obj_name}", flush=True)
    
    # Use proper terminology for this central body
    label = f"Keplerian {far_term}"
    
    # Create hover text
    # Ensure Q is properly formatted
    try:
        Q_str = f"{Q:.6f}"
    except:
        Q_str = str(Q)
        print(f"WARNING: Could not format Q value for {obj_name}: {Q}", flush=True)
    
    hover_text = f"<b>{obj_name} {label}</b>{aphelion_date_str}<br>Q={Q_str} AU{accuracy_note}"
    
    # DEBUG: Uncomment these lines to diagnose hover text issues
    print(f"DEBUG: {obj_name} {label} hover text: {hover_text}", flush=True)
   
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=6,
                color=color_map(obj_name),
                symbol='square-open'
            ),
            name=f"{obj_name} {label}",
            text=[hover_text],
        #    customdata=[label],
            customdata=[f"{obj_name} {label}"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )

def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None):
    """
    Find and mark the closest plotted approach point from trajectory data.
    
    Works for ANY object passing near ANY center body, regardless of whether
    the object orbits that center. Uses proper astronomical terminology.
    
    Parameters:
        fig: Plotly figure object
        positions_dict: Dictionary with date keys and position values {'x':, 'y':, 'z':}
        obj_name: Name of the object
        center_body: Name or ID of central body (for terminology)
        color_map: Function to get object color
        date_range: Optional tuple (start_date, end_date) to filter positions
    
    Returns:
        None (modifies fig in place)
        
    Examples:
        - Comet C/2025 V1 closest plotted point to Earth → "Closest Plotted (Perigee)"
        - Asteroid flyby of Mars → "Closest Plotted (Periareion)"
        - Spacecraft encounter with Jupiter → "Closest Plotted (Perijove)"
    """
    import numpy as np
    from datetime import datetime
    
    if not positions_dict or len(positions_dict) == 0:
        print(f"No trajectory data for closest plotted of {obj_name}", flush=True)
        return
    
    # Get terminology for this center body
    near_term, far_term = get_apsidal_terms(center_body)
    
    # Calculate distances for all positions
    dates = []
    distances = []
    positions = []
    
    for date_str, pos in positions_dict.items():
        if date_range:
            # Filter by date range if provided
            try:
                date = datetime.fromisoformat(date_str)
                if not (date_range[0] <= date <= date_range[1]):
                    continue
            except:
                pass  # If date parsing fails, include the position
        
        dates.append(date_str)
        distance = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
        distances.append(distance)
        positions.append(pos)
    
    if len(distances) == 0:
        print(f"No positions in date range for {obj_name} closest plotted", flush=True)
        return
    
    # Find closest plotted point
    closest_idx = np.argmin(distances)
    closest_date = dates[closest_idx]
    closest_distance = distances[closest_idx]
    closest_pos = positions[closest_idx]
    
    # Format date nicely
    try:
        date_obj = datetime.fromisoformat(closest_date)
        date_str_formatted = date_obj.strftime('%Y-%m-%d %H:%M:%S UTC')
    except:
        date_str_formatted = closest_date
    
    # Create label using proper terminology
#    label = f"Closest Plotted ({near_term})"
    label = f"Closest Plotted Point"
    
    # Create comprehensive hover text
    km_distance = closest_distance * 149597870.7  # AU to km
    hover_text = (
        f"<b>{obj_name} {label}</b><br>"
        f"Date: {date_str_formatted}<br>"
        f"Distance from {center_body}: {closest_distance:.6f} AU<br>"
        f"Distance: {km_distance:,.0f} km"
    )
    
    # Add marker to plot - using diamond symbol to distinguish from apsidal markers
    fig.add_trace(
        go.Scatter3d(
            x=[closest_pos['x']],
            y=[closest_pos['y']],
            z=[closest_pos['z']],
            mode='markers',
            marker=dict(
                size=8,
                color=color_map(obj_name),
        #        color='white',                
                symbol='square-open',  # Different from apsidal markers (square-open)
        #        line=dict(width=2, color='white')  # White outline for visibility
            ),
            name=f"{obj_name} {label}",
            text=[hover_text],
            customdata=[f"{obj_name} {label}"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    print(f"✓ Added closest plotted marker for {obj_name} to {center_body}: {closest_distance:.6f} AU on {date_str_formatted}", flush=True)
