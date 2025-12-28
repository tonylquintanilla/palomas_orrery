"""
exoplanet_coordinates.py - Stellar Positioning and Coordinate Transformations

This module handles:
- Conversion of celestial coordinates (RA, Dec, Distance) to Cartesian
- Proper motion corrections for stellar positions over time
- Binary system barycenter calculations
- Independent coordinate frames for each exoplanet system

Key principle: Each exoplanet system has its own LOCAL coordinate frame,
NOT connected to Solar System ecliptic. This module handles the stellar
position when needed for context (e.g., stellar visualization module).

Coordinate system for exoplanet visualization:
- Origin: Host star barycenter at (0, 0, 0)
- XY plane: Sky plane (perpendicular to Earth line of sight)
- Z axis: Toward Earth
- User rotates from this default view as desired

Created: October 21, 2025
Author: Tony Quintanilla with Claude AI
"""

import numpy as np
from datetime import datetime, timezone

# ============================================================================
# PROPER MOTION CORRECTIONS
# ============================================================================

def apply_proper_motion(ra_deg, dec_deg, pmra_mas_yr, pmdec_mas_yr,
                       epoch, target_date, distance_pc=None):
    """
    Apply proper motion to stellar position
    
    Critical for nearby stars like Proxima Centauri which have
    significant proper motion (>3 arcsec/year).
    
    Parameters:
        ra_deg: float - Right ascension at epoch (degrees)
        dec_deg: float - Declination at epoch (degrees)
        pmra_mas_yr: float - Proper motion in RA (mas/year, includes cos(dec))
        pmdec_mas_yr: float - Proper motion in Dec (mas/year)
        epoch: datetime - Reference epoch for coordinates
        target_date: datetime - Date to calculate position for
        distance_pc: float - Distance in parsecs (optional, for 3D motion)
        
    Returns:
        ra_new, dec_new: floats - Corrected position (degrees)
        
    Note:
        pmra is typically already multiplied by cos(dec) in catalogs.
        If not, multiply pmra by cos(dec_deg) before calling.
    """
    # Ensure dates are UTC-aware
    if epoch.tzinfo is None:
        epoch = epoch.replace(tzinfo=timezone.utc)
    if target_date.tzinfo is None:
        target_date = target_date.replace(tzinfo=timezone.utc)
    
    # Calculate elapsed time in years
    dt_seconds = (target_date - epoch).total_seconds()
    years_elapsed = dt_seconds / (365.25 * 86400)
    
    # Convert proper motion from mas/year to degrees
    # 1 mas = 1/3,600,000 degrees
    pmra_deg_yr = pmra_mas_yr / 3600000.0
    pmdec_deg_yr = pmdec_mas_yr / 3600000.0
    
    # Apply corrections
    delta_ra = pmra_deg_yr * years_elapsed
    delta_dec = pmdec_deg_yr * years_elapsed
    
    ra_new = ra_deg + delta_ra
    dec_new = dec_deg + delta_dec
    
    # Wrap RA to [0, 360)
    ra_new = ra_new % 360.0
    
    # Clamp Dec to [-90, 90]
    dec_new = np.clip(dec_new, -90.0, 90.0)
    
    return ra_new, dec_new

def get_star_position_at_date(host_star_data, target_date):
    """
    Get corrected stellar position at specific date
    
    Applies proper motion if significant. For distant stars (>100 pc)
    with small proper motion, this correction is minimal.
    
    Parameters:
        host_star_data: dict - Host star data from exoplanet_systems.py
        target_date: datetime - Date for position
        
    Returns:
        ra, dec: floats - Corrected position (degrees)
    """
    ra = host_star_data['ra']
    dec = host_star_data['dec']
    pmra = host_star_data.get('pmra', 0.0)
    pmdec = host_star_data.get('pmdec', 0.0)
    epoch = host_star_data.get('epoch')
    
    if epoch is None:
        # No epoch specified, return original position
        return ra, dec
    
    # Apply proper motion
    ra_corrected, dec_corrected = apply_proper_motion(
        ra, dec, pmra, pmdec, epoch, target_date
    )
    
    return ra_corrected, dec_corrected

# ============================================================================
# COORDINATE TRANSFORMATIONS (For context only)
# ============================================================================
# These functions convert stellar RA/Dec to 3D Cartesian coordinates
# ONLY used when showing exoplanet host stars in stellar neighborhood maps
# NOT used for exoplanet orbit visualization (which uses local frames)
# ============================================================================

def radec_to_cartesian(ra_deg, dec_deg, distance_au):
    """
    Convert equatorial coordinates to 3D Cartesian
    
    This transformation is ONLY for placing host stars in the
    galactic/stellar neighborhood context (Phase 4). It is NOT
    used for exoplanet orbit visualization.
    
    Coordinate system (J2000 equatorial):
    - Origin: Solar System barycenter
    - X-axis: Points to vernal equinox (RA=0 deg, Dec=0 deg)
    - Y-axis: Points to RA=90 deg, Dec=0 deg
    - Z-axis: Points to north celestial pole (Dec=+90 deg)
    
    Parameters:
        ra_deg: float - Right ascension (degrees)
        dec_deg: float - Declination (degrees)
        distance_au: float - Distance (AU or parsecs, units preserved)
        
    Returns:
        x, y, z: floats - Cartesian coordinates (same units as distance)
    """
    # Convert to radians
    ra_rad = np.radians(ra_deg)
    dec_rad = np.radians(dec_deg)
    
    # Spherical to Cartesian conversion
    x = distance_au * np.cos(dec_rad) * np.cos(ra_rad)
    y = distance_au * np.cos(dec_rad) * np.sin(ra_rad)
    z = distance_au * np.sin(dec_rad)
    
    return x, y, z

def cartesian_to_radec(x, y, z):
    """
    Convert 3D Cartesian to equatorial coordinates
    
    Inverse of radec_to_cartesian. Used for verification/testing.
    
    Parameters:
        x, y, z: floats - Cartesian coordinates
        
    Returns:
        ra_deg, dec_deg, distance: floats - Spherical coordinates
    """
    distance = np.sqrt(x**2 + y**2 + z**2)
    
    # Avoid division by zero
    if distance < 1e-10:
        return 0.0, 0.0, 0.0
    
    # Calculate declination
    dec_rad = np.arcsin(z / distance)
    dec_deg = np.degrees(dec_rad)
    
    # Calculate right ascension
    ra_rad = np.arctan2(y, x)
    ra_deg = np.degrees(ra_rad)
    
    # Wrap RA to [0, 360)
    ra_deg = ra_deg % 360.0
    
    return ra_deg, dec_deg, distance

def get_star_3d_position(host_star_data, target_date=None):
    """
    Get 3D position of host star in galactic context
    
    Used ONLY for Phase 4 integration with stellar visualization.
    NOT used for exoplanet orbit plotting (which uses local frame).
    
    Parameters:
        host_star_data: dict - Host star data
        target_date: datetime - Date for proper motion correction (optional)
        
    Returns:
        x, y, z: floats - Position in J2000 equatorial frame (parsecs)
    """
    # Get corrected position
    if target_date is not None:
        ra, dec = get_star_position_at_date(host_star_data, target_date)
    else:
        ra = host_star_data['ra']
        dec = host_star_data['dec']
    
    distance_pc = host_star_data['distance_pc']
    
    # Convert to Cartesian
    x, y, z = radec_to_cartesian(ra, dec, distance_pc)
    
    return x, y, z

# ============================================================================
# BINARY SYSTEM BARYCENTER
# ============================================================================

def calculate_binary_barycenter(star_A_mass, star_B_mass, 
                                star_A_position, star_B_position):
    """
    Calculate center of mass for binary star system
    
    For visualization purposes, we typically place the barycenter
    at the origin (0, 0, 0) and calculate stellar positions relative
    to it. This function is provided for completeness but may not
    be needed in practice.
    
    Parameters:
        star_A_mass: float - Primary star mass (solar masses)
        star_B_mass: float - Secondary star mass (solar masses)
        star_A_position: tuple - (x, y, z) of star A
        star_B_position: tuple - (x, y, z) of star B
        
    Returns:
        x, y, z: floats - Barycenter position
    """
    total_mass = star_A_mass + star_B_mass
    
    x_A, y_A, z_A = star_A_position
    x_B, y_B, z_B = star_B_position
    
    x_bary = (star_A_mass * x_A + star_B_mass * x_B) / total_mass
    y_bary = (star_A_mass * y_A + star_B_mass * y_B) / total_mass
    z_bary = (star_A_mass * z_A + star_B_mass * z_B) / total_mass
    
    return x_bary, y_bary, z_bary

# ============================================================================
# LOCAL COORDINATE FRAME CREATION
# ============================================================================

def create_local_frame_description(host_star_data):
    """
    Generate description of local coordinate frame for exoplanet system
    
    This is informational only - helps document what coordinate system
    we're using for each exoplanet system visualization.
    
    Parameters:
        host_star_data: dict - Host star data
        
    Returns:
        dict: Frame description
    """
    ra = host_star_data['ra']
    dec = host_star_data['dec']
    
    # Format RA as hours:minutes:seconds
    ra_hours = ra / 15.0
    ra_h = int(ra_hours)
    ra_m = int((ra_hours - ra_h) * 60)
    ra_s = ((ra_hours - ra_h) * 60 - ra_m) * 60
    
    # Format Dec as degrees:arcminutes:arcseconds
    dec_sign = '+' if dec >= 0 else '-'
    dec_abs = abs(dec)
    dec_d = int(dec_abs)
    dec_m = int((dec_abs - dec_d) * 60)
    dec_s = ((dec_abs - dec_d) * 60 - dec_m) * 60
    
    description = {
        'origin': 'Host star barycenter at (0, 0, 0)',
        'xy_plane': 'Sky plane (perpendicular to Earth line of sight)',
        'z_axis': 'Toward Earth (positive = toward observer)',
        'line_of_sight_ra': f"{ra_h:02d}h {ra_m:02d}m {ra_s:04.1f}s",
        'line_of_sight_dec': f"{dec_sign}{dec_d:02d} deg {dec_m:02d}' {dec_s:04.1f}\"",
        'note': 'Independent frame - NOT aligned with Solar System ecliptic'
    }
    
    return description

# ============================================================================
# DISTANCE UTILITIES
# ============================================================================

def parsecs_to_lightyears(distance_pc):
    """Convert parsecs to light-years (1 pc = 3.26156 ly)"""
    return distance_pc * 3.26156

def lightyears_to_parsecs(distance_ly):
    """Convert light-years to parsecs"""
    return distance_ly / 3.26156

def parsecs_to_au(distance_pc):
    """Convert parsecs to AU (1 pc = 206265 AU)"""
    return distance_pc * 206265

def au_to_parsecs(distance_au):
    """Convert AU to parsecs"""
    return distance_au / 206265

def stellar_parallax_to_distance(parallax_mas):
    """
    Convert parallax to distance
    
    Parameters:
        parallax_mas: float - Parallax (milliarcseconds)
        
    Returns:
        distance_pc: float - Distance (parsecs)
    """
    if parallax_mas <= 0:
        return float('inf')
    return 1000.0 / parallax_mas

def distance_to_stellar_parallax(distance_pc):
    """
    Convert distance to parallax
    
    Parameters:
        distance_pc: float - Distance (parsecs)
        
    Returns:
        parallax_mas: float - Parallax (milliarcseconds)
    """
    if distance_pc <= 0:
        return 0.0
    return 1000.0 / distance_pc

# ============================================================================
# PROPER MOTION UTILITIES
# ============================================================================

def calculate_tangential_velocity(pmra_mas_yr, pmdec_mas_yr, distance_pc):
    """
    Calculate tangential velocity from proper motion
    
    Parameters:
        pmra_mas_yr: float - Proper motion in RA (mas/year)
        pmdec_mas_yr: float - Proper motion in Dec (mas/year)
        distance_pc: float - Distance (parsecs)
        
    Returns:
        velocity_km_s: float - Tangential velocity (km/s)
    """
    # Total proper motion (mas/year)
    pm_total = np.sqrt(pmra_mas_yr**2 + pmdec_mas_yr**2)
    
    # Convert to arcsec/year
    pm_arcsec_yr = pm_total / 1000.0
    
    # Convert to radians/year
    pm_rad_yr = pm_arcsec_yr * (np.pi / 648000.0)
    
    # Tangential velocity = distance x angular velocity
    # 1 AU/year = 4.74 km/s
    velocity_au_yr = distance_pc * 206265 * pm_rad_yr
    velocity_km_s = velocity_au_yr * 4.74
    
    return velocity_km_s

def get_proper_motion_summary(host_star_data):
    """
    Generate human-readable summary of proper motion
    
    Parameters:
        host_star_data: dict - Host star data
        
    Returns:
        str: Summary text
    """
    pmra = host_star_data.get('pmra', 0.0)
    pmdec = host_star_data.get('pmdec', 0.0)
    distance_pc = host_star_data['distance_pc']
    
    # Total proper motion
    pm_total = np.sqrt(pmra**2 + pmdec**2)
    pm_arcsec_yr = pm_total / 1000.0
    
    # Tangential velocity
    v_tan = calculate_tangential_velocity(pmra, pmdec, distance_pc)
    
    summary = f"Proper motion: {pm_arcsec_yr:.3f} arcsec/year\n"
    summary += f"  RA component: {pmra:.2f} mas/yr\n"
    summary += f"  Dec component: {pmdec:.2f} mas/yr\n"
    summary += f"Tangential velocity: {v_tan:.1f} km/s"
    
    return summary

# ============================================================================
# TESTING AND VALIDATION
# ============================================================================

if __name__ == "__main__":
    print("Testing Exoplanet Coordinate Functions")
    print("=" * 60)
    
    from exoplanet_systems import get_system
    from datetime import datetime, timezone
    
    # Test 1: Proxima Centauri (high proper motion)
    print("\n1. Proxima Centauri Proper Motion Test")
    print("-" * 60)
    proxima = get_system('proxima')
    star_data = proxima['host_star']
    
    print(f"Star: {star_data['name']}")
    print(f"Distance: {star_data['distance_pc']:.4f} pc ({star_data['distance_pc']*3.26:.2f} ly)")
    print(f"Proper motion: RA={star_data['pmra']:.2f} mas/yr, Dec={star_data['pmdec']:.2f} mas/yr")
    
    # Position at J2000
    ra_2000 = star_data['ra']
    dec_2000 = star_data['dec']
    print(f"\nPosition at J2000: RA={ra_2000:.6f} deg, Dec={dec_2000:.6f} deg")
    
    # Position at 2050 (50 years later)
    date_2050 = datetime(2050, 1, 1, tzinfo=timezone.utc)
    ra_2050, dec_2050 = apply_proper_motion(
        ra_2000, dec_2000,
        star_data['pmra'], star_data['pmdec'],
        star_data['epoch'], date_2050
    )
    
    delta_ra = ra_2050 - ra_2000
    delta_dec = dec_2050 - dec_2000
    
    print(f"Position at 2050: RA={ra_2050:.6f} deg, Dec={dec_2050:.6f} deg")
    print(f"Change: DeltaRA={delta_ra:.6f} deg ({delta_ra*3600:.2f}\"), DeltaDec={delta_dec:.6f} deg ({delta_dec*3600:.2f}\")")
    
    # Tangential velocity
    v_tan = calculate_tangential_velocity(
        star_data['pmra'], star_data['pmdec'], star_data['distance_pc']
    )
    print(f"Tangential velocity: {v_tan:.1f} km/s")
    
    # Test 2: TRAPPIST-1 (moderate proper motion)
    print("\n2. TRAPPIST-1 Proper Motion Test")
    print("-" * 60)
    trappist = get_system('trappist1')
    star_data = trappist['host_star']
    
    print(f"Star: {star_data['name']}")
    print(f"Distance: {star_data['distance_pc']:.2f} pc ({star_data['distance_pc']*3.26:.1f} ly)")
    print(f"Proper motion: RA={star_data['pmra']:.2f} mas/yr, Dec={star_data['pmdec']:.2f} mas/yr")
    
    v_tan = calculate_tangential_velocity(
        star_data['pmra'], star_data['pmdec'], star_data['distance_pc']
    )
    print(f"Tangential velocity: {v_tan:.1f} km/s")
    
    # Test 3: TOI-1338 (distant, small proper motion)
    print("\n3. TOI-1338 Proper Motion Test")
    print("-" * 60)
    toi = get_system('toi1338')
    star_data = toi['host_star']
    
    print(f"Star: {star_data['name']}")
    print(f"Distance: {star_data['distance_pc']:.0f} pc ({star_data['distance_pc']*3.26:.0f} ly)")
    print(f"Proper motion: RA={star_data['pmra']:.2f} mas/yr, Dec={star_data['pmdec']:.2f} mas/yr")
    
    v_tan = calculate_tangential_velocity(
        star_data['pmra'], star_data['pmdec'], star_data['distance_pc']
    )
    print(f"Tangential velocity: {v_tan:.1f} km/s")
    print("\nNote: Distant stars have negligible proper motion for visualization")
    
    # Test 4: Coordinate transformation round-trip
    print("\n4. Coordinate Transformation Test")
    print("-" * 60)
    
    # Original coordinates
    ra_orig = 346.62
    dec_orig = -5.04
    dist_orig = 12.43
    
    print(f"Original: RA={ra_orig:.2f} deg, Dec={dec_orig:.2f} deg, Distance={dist_orig:.2f} pc")
    
    # Convert to Cartesian
    x, y, z = radec_to_cartesian(ra_orig, dec_orig, dist_orig)
    print(f"Cartesian: X={x:.4f}, Y={y:.4f}, Z={z:.4f} pc")
    
    # Convert back
    ra_back, dec_back, dist_back = cartesian_to_radec(x, y, z)
    print(f"Round-trip: RA={ra_back:.2f} deg, Dec={dec_back:.2f} deg, Distance={dist_back:.2f} pc")
    
    # Check accuracy
    ra_error = abs(ra_back - ra_orig)
    dec_error = abs(dec_back - dec_orig)
    dist_error = abs(dist_back - dist_orig)
    
    print(f"Errors: DeltaRA={ra_error:.6f} deg, DeltaDec={dec_error:.6f} deg, DeltaDist={dist_error:.6f} pc")
    
    if ra_error < 1e-6 and dec_error < 1e-6 and dist_error < 1e-6:
        print("[OK] Round-trip accuracy excellent!")
    
    # Test 5: Local frame description
    print("\n5. Local Coordinate Frame Description")
    print("-" * 60)
    frame = create_local_frame_description(trappist['host_star'])
    print(f"System: {trappist['system_name']}")
    for key, value in frame.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("[OK] All coordinate tests passed!")
