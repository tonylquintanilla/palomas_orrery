# data_processing.py

import os
import pickle
import numpy as np
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord, Angle
from astroquery.vizier import Vizier


def convert_icrs_to_radec_strings(data):
    """
    Convert ICRS coordinates (decimal degrees) to formatted RA/Dec strings.
    Works with astropy Table objects (not pandas DataFrames).
    
    Adds two new columns:
    - ra_str: Right Ascension in format "HHh MMm SS.SSs"
    - dec_str: Declination in format "±DD° MM' SS.S""
    
    Args:
        data: Astropy Table with RA_ICRS and DE_ICRS columns
    
    Returns:
        data: Same Table with added ra_str and dec_str columns
    """
    import numpy as np
    from astropy.table import Column
    
    # Check if ICRS coordinates exist
    if 'RA_ICRS' not in data.colnames or 'DE_ICRS' not in data.colnames:
        print("Warning: No ICRS coordinates found in data")
        return data
    
    # Initialize lists for new columns
    ra_strings = []
    dec_strings = []
    
    # Process each row (astropy Table iteration)
    valid_coords = 0
    for row in data:  # Just iterate directly over the table, no .iterrows()
        ra_deg = row['RA_ICRS']
        dec_deg = row['DE_ICRS']
        
        # Check for valid coordinates (not masked or NaN)
        if (not np.ma.is_masked(ra_deg) and not np.ma.is_masked(dec_deg) and
            np.isfinite(ra_deg) and np.isfinite(dec_deg)):
            
            # Convert RA from degrees to hours:minutes:seconds
            ra_hours = ra_deg / 15.0
            ra_h = int(ra_hours)
            ra_m = int((ra_hours - ra_h) * 60)
            ra_s = ((ra_hours - ra_h) * 60 - ra_m) * 60
            
            # Convert Dec from degrees to degrees:arcminutes:arcseconds
            dec_sign = '+' if dec_deg >= 0 else '-'
            dec_deg_abs = abs(dec_deg)
            dec_d = int(dec_deg_abs)
            dec_m = int((dec_deg_abs - dec_d) * 60)
            dec_s = ((dec_deg_abs - dec_d) * 60 - dec_m) * 60
            
            # Format the strings
            ra_strings.append(f"{ra_h:02d}h {ra_m:02d}m {ra_s:05.2f}s")
            dec_strings.append(f"{dec_sign}{dec_d:02d}° {dec_m:02d}' {dec_s:04.1f}\"")
            valid_coords += 1
        else:
            ra_strings.append('')
            dec_strings.append('')
    
    # Add columns to the astropy Table
    data['ra_str'] = Column(ra_strings, dtype='U20')  # Unicode string, max 20 chars
    data['dec_str'] = Column(dec_strings, dtype='U20')

# Python objects (strings in this case), which pandas handles much better -- except this fix does not work
#    data['ra_str'] = Column(ra_strings, dtype=object)
#    data['dec_str'] = Column(dec_strings, dtype=object)
    
    print(f"Added RA/Dec strings for {valid_coords} objects")
    return data


def estimate_vmag_from_gaia(gaia_data):
    """
    Estimate V magnitude from Gaia G magnitude and BP-RP color.
    """
    vmag = np.full(len(gaia_data), np.nan)
    if all(col in gaia_data.colnames for col in ['Gmag', 'BP-RP']):
        bp_rp = gaia_data['BP-RP']
        valid_mask = ~np.isnan(gaia_data['Gmag']) & ~np.isnan(bp_rp)
        vmag[valid_mask] = (
            gaia_data['Gmag'][valid_mask]
            - (-0.0257 - 0.0924 * bp_rp[valid_mask]
               - 0.1623 * bp_rp[valid_mask] ** 2
               + 0.0090 * bp_rp[valid_mask] ** 3)
        )
    return vmag

def calculate_distances(data):
    """Calculate distances in parsecs and light-years"""
    if data is not None and 'Plx' in data.colnames:
        parallax_mas = data['Plx']
        with np.errstate(divide='ignore', invalid='ignore'):  # Add this
            parallax_arcsec = parallax_mas / 1000.0
            distance_pc = 1 / parallax_arcsec
            data['Distance_pc'] = distance_pc
            data['Distance_ly'] = distance_pc * 3.26156
        # Only filter out clearly invalid distances
        valid_dist = ~np.isnan(data['Distance_ly']) & (data['Distance_ly'] > 0)
        return data[valid_dist]
    return data

def align_coordinate_systems(hip_data):
    """Ensure RA and Dec columns are consistent and in degrees."""
    if 'RA_ICRS' not in hip_data.colnames:
        if 'RAICRS' in hip_data.colnames:
            hip_data.rename_column('RAICRS', 'RA_ICRS')
        elif 'RAhms' in hip_data.colnames:
            ra_hms = hip_data['RAhms']
            ra_deg_hip = Angle(ra_hms, unit='hourangle').degree
            hip_data['RA_ICRS'] = ra_deg_hip
    if 'DE_ICRS' not in hip_data.colnames:
        if 'DEICRS' in hip_data.colnames:
            hip_data.rename_column('DEICRS', 'DE_ICRS')
        elif 'DEdms' in hip_data.colnames:
            dec_dms = hip_data['DEdms']
            dec_deg_hip = Angle(dec_dms, unit='deg').degree
            hip_data['DE_ICRS'] = dec_deg_hip
    return hip_data

def generate_unique_ids(stars, catalog='Hipparcos'):
    """
    Generate unique IDs for stars based on their catalog.
    For Hipparcos: "HIP {HIP_number}"
    For Gaia: "Gaia DR3 {source_id}"
    """
    unique_ids = []
    if catalog == 'Hipparcos':
        for star in stars:
            if 'HIP' in stars.colnames and not np.ma.is_masked(star['HIP']):
                unique_ids.append(f"HIP {star['HIP']}")
            else:
                # Fallback if no HIP ID, use a combo of coords?
                # Ideally you always have HIP IDs for Hipparcos stars.
                ra, dec = star['RA_ICRS'], star['DE_ICRS']
                unique_ids.append(f"HIP-noID-{ra:.6f}-{dec:.6f}")
    else:  # Gaia
        if 'source_id' in stars.colnames:
            for star in stars:
                unique_ids.append(f"Gaia DR3 {star['source_id']}")
        else:
            # Fallback if no Gaia source_id, use coords as last resort
            for star in stars:
                ra, dec = star['RA_ICRS'], star['DE_ICRS']
                unique_ids.append(f"Gaia-noID-{ra:.6f}-{dec:.6f}")

    return unique_ids

def select_stars_by_magnitude(hip_data, gaia_data, mag_limit):
    """
    Select stars based on a clean separation:
    For stars brighter than Vmag ~ 3, Hipparcos may still be valuable if Gaia's measurements are flagged as unreliable due to 
    saturation effects. For stars in the range Vmag ~ 4 to 10, Gaia should be the preferred source due to its superior accuracy.
    For stars fainter than Vmag ~ 10, Gaia is far more accurate and essentially replaces Hipparcos. There are no Gaia stars below Vmag 1.73.

    - Vmag ≤ 4: Hipparcos exclusively (no overlap with Gaia) 
    - Vmag > 4: Gaia exclusively
    
    Parameters:
        hip_data: astropy Table containing Hipparcos star data
        gaia_data: astropy Table containing Gaia star data
        mag_limit: float, maximum apparent magnitude to include
    
    Returns:
        combined_data: astropy Table of selected stars
        counts: dict summarizing star counts
    """
    print("\nSelecting stars with clean separation by Vmag...")

    all_selected_stars = []

    # --- 1. Hipparcos stars (Vmag ≤ 4) ---
    if hip_data is not None:
        bright_mask = hip_data['Vmag'] <= 4  # No need to compare with mag_limit here
        bright_stars = hip_data[bright_mask]
        if len(bright_stars) > 0:
            bright_stars['Source_Catalog'] = 'Hipparcos'
            bright_stars['Apparent_Magnitude'] = bright_stars['Vmag']
            all_selected_stars.append(bright_stars)
            print(f"Selected {len(bright_stars)} bright Hipparcos stars (Vmag ≤ 4)")

    # --- 2. Gaia stars (Vmag > 4) ---
    if gaia_data is not None:
        if 'Estimated_Vmag' not in gaia_data.colnames:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

        faint_mask = (gaia_data['Estimated_Vmag'] > 4) & (gaia_data['Estimated_Vmag'] <= mag_limit)
        faint_stars = gaia_data[faint_mask]
        if len(faint_stars) > 0:
            faint_stars['Source_Catalog'] = 'Gaia'
            faint_stars['Apparent_Magnitude'] = faint_stars['Estimated_Vmag']
            all_selected_stars.append(faint_stars)
            print(f"Selected {len(faint_stars)} faint Gaia stars (4 < Vmag ≤ {mag_limit})")

    # Combine all selected stars
    if not all_selected_stars:
        print(f"No stars found within magnitude limit {mag_limit}")
        return None, {}

    combined_data = vstack(all_selected_stars)

    # Calculate final counts
    hip_count = np.sum(combined_data['Source_Catalog'] == 'Hipparcos')
    gaia_count = np.sum(combined_data['Source_Catalog'] == 'Gaia')

    print("\nFinal Selection Summary:")
    print(f"Hipparcos stars (Vmag ≤ 4): {hip_count}")
    print(f"Gaia stars (Vmag > 4): {gaia_count}")
    print(f"Total stars: {len(combined_data)}")

    counts = {
        'hip_count': hip_count,
        'gaia_count': gaia_count
    }

    return combined_data, counts

def analyze_additional_stars(new_data, old_data):
    """Analyze properties of stars present in new data but not in old"""
    # Compare magnitude distributions
    print("\nMagnitude Distribution Analysis of Additional Stars:")
    mag_bins = np.arange(4.0, 9.0, 0.5)
    new_mags = new_data['Estimated_Vmag']
    hist, bins = np.histogram(new_mags, bins=mag_bins)
    
    for i in range(len(hist)):
        print(f"V mag {bins[i]:.1f}-{bins[i+1]:.1f}: {hist[i]} stars")
        
    # Analyze parallax quality
    parallax_rel_error = new_data['e_Plx'] / new_data['Plx']
    print(f"\nParallax Quality:")
    print(f"Median relative error: {np.median(parallax_rel_error):.3f}")
    print(f"95th percentile error: {np.percentile(parallax_rel_error, 95):.3f}")
    
    # Check G-V conversion reasonableness
    g_v_diff = new_data['Gmag'] - new_data['Estimated_Vmag']
    print(f"\nG-V Magnitude Difference:")
    print(f"Mean difference: {np.mean(g_v_diff):.3f}")
    print(f"Standard deviation: {np.std(g_v_diff):.3f}")

    # Position on HR diagram
    print("\nHR Diagram Statistics:")
    print(f"Temperature range: {np.min(new_data['Temperature']):.0f}K - {np.max(new_data['Temperature']):.0f}K")
    print(f"Luminosity range: {np.min(new_data['Luminosity']):.3f} - {np.max(new_data['Luminosity']):.3f} Lsun")

def examine_outliers(data):
    """Print details of potential outlier stars"""
    # Look at stars with extreme values
    high_lum = data[data['Luminosity'] > 100]
    low_lum = data[data['Luminosity'] < 0.001]
    extreme_temp = data[(data['Temperature'] > 30000) | (data['Temperature'] < 2000)]
    
    print("\nHigh Luminosity Stars:")
    for _, star in high_lum.iterrows():
        print_star_details(star)
        
    print("\nLow Luminosity Stars:")
    for _, star in low_lum.iterrows():
        print_star_details(star)
        
    print("\nExtreme Temperature Stars:")
    for _, star in extreme_temp.iterrows():
        print_star_details(star)

def print_star_details(star):
    """Print relevant details for a single star"""
    print(f"\nStar: {star['Star_Name']}")
    print(f"Gmag: {star['Gmag']:.2f}")
    print(f"Estimated Vmag: {star['Estimated_Vmag']:.2f}")
    print(f"Parallax: {star['Plx']:.3f} ± {star['e_Plx']:.3f} mas")
    print(f"Temperature: {star['Temperature']:.0f}K")
    print(f"Luminosity: {star['Luminosity']:.3f} Lsun")

# data_processing.py

def select_stars_by_distance(hip_data, gaia_data, max_light_years):
    """
    Select stars based on distance criteria while maintaining clean catalog separation:
    - Hipparcos: primary source for bright stars (Vmag ≤ 4.0)
    - Gaia: primary source for faint stars (Vmag > 4.0)
    Both constrained by the specified distance.
    
    Parameters:
        hip_data: astropy Table containing Hipparcos star data
        gaia_data: astropy Table containing Gaia star data
        max_light_years: float, maximum distance to include
    
    Returns:
        combined_data: astropy Table of selected stars
        counts: dict summarizing star counts
    """
    print("\nSelecting stars by distance...")
    
    all_selected_stars = []
    hip_bright_count = 0  # Vmag ≤ 1.73
    hip_mid_count = 0     # 1.73 < Vmag ≤ 4.0
    gaia_mid_count = 0    # 1.73 < Vmag ≤ 4.0
    gaia_faint_count = 0  # Vmag > 4.0
    
    # Process Hipparcos stars (for bright and mid-range stars)
    if hip_data is not None:
        # First filter by distance
        distance_mask = hip_data['Distance_ly'] <= max_light_years
        mag_mask = hip_data['Vmag'] <= 4.0  # Hipparcos for Vmag ≤ 4.0 only
        hip_stars = hip_data[distance_mask & mag_mask]
        
        if len(hip_stars) > 0:
            # Add source catalog and apparent magnitude
            hip_stars['Source_Catalog'] = 'Hipparcos'
            hip_stars['Apparent_Magnitude'] = hip_stars['Vmag']
            
            # Count by magnitude ranges
            bright_mask = hip_stars['Vmag'] <= 1.73
            mid_mask = (hip_stars['Vmag'] > 1.73) & (hip_stars['Vmag'] <= 4.0)
            
            hip_bright_count = np.sum(bright_mask)
            hip_mid_count = np.sum(mid_mask)
            
            all_selected_stars.append(hip_stars)
            print(f"Selected {len(hip_stars)} Hipparcos stars within {max_light_years} light-years")
    
    # Process Gaia stars (for faint stars)
    if gaia_data is not None:
        # First filter by distance
        distance_mask = gaia_data['Distance_ly'] <= max_light_years
        mag_mask = gaia_data['Estimated_Vmag'] > 4.0  # Gaia for Vmag > 4.0 only
        gaia_stars = gaia_data[distance_mask & mag_mask]
        
        if len(gaia_stars) > 0:
            # Add source catalog and apparent magnitude
            gaia_stars['Source_Catalog'] = 'Gaia'
            gaia_stars['Apparent_Magnitude'] = gaia_stars['Estimated_Vmag']
            
            # Count by magnitude ranges
            mid_mask = (gaia_stars['Apparent_Magnitude'] > 1.73) & (gaia_stars['Apparent_Magnitude'] <= 4.0)
            faint_mask = gaia_stars['Apparent_Magnitude'] > 4.0
            
            gaia_mid_count = np.sum(mid_mask)
            gaia_faint_count = np.sum(faint_mask)
            
            all_selected_stars.append(gaia_stars)
            print(f"Selected {len(gaia_stars)} Gaia stars within {max_light_years} light-years")
    
    if not all_selected_stars:
        print(f"No stars found within {max_light_years} light-years")
        return None, {}
    
    # Combine selected stars
    from astropy.table import vstack
    combined_data = vstack(all_selected_stars)
    
    # Prepare counts dictionary
    counts = {
        'hip_bright_count': hip_bright_count,
        'hip_mid_count': hip_mid_count,
        'gaia_mid_count': gaia_mid_count,
        'gaia_faint_count': gaia_faint_count,
        'total_stars': len(combined_data)
    }
    
    print("\nFinal Selection Summary:")
    print(f"Hipparcos bright stars (Vmag ≤ 1.73): {hip_bright_count}")
    print(f"Hipparcos mid-range stars (1.73 < Vmag ≤ 4.0): {hip_mid_count}")
    print(f"Gaia mid-range stars (1.73 < Vmag ≤ 4.0): {gaia_mid_count}")
    print(f"Gaia faint stars (Vmag > 4.0): {gaia_faint_count}")
    print(f"Total stars: {len(combined_data)}")
    
    return combined_data, counts

def calculate_distances(data):
    """Calculate distances in parsecs and light-years from parallax."""
    if data is not None and 'Plx' in data.colnames:
        with np.errstate(divide='ignore', invalid='ignore'):
            parallax_mas = data['Plx']
            parallax_arcsec = parallax_mas / 1000.0
            distance_pc = 1 / parallax_arcsec
            data['Distance_pc'] = distance_pc
            data['Distance_ly'] = distance_pc * 3.26156
            
        # Filter out clearly invalid distances
        valid_dist = ~np.isnan(data['Distance_ly']) & (data['Distance_ly'] > 0)
        return data[valid_dist]
    return data

def calculate_cartesian_coordinates(data):
    """Calculate x, y, z coordinates from RA, Dec, and distance."""
    if data is None:
        return None

    print("\nCalculating cartesian coordinates...")
    
    # Create mask for Messier objects (which may have different coordinate handling)
    is_messier = data['Is_Messier'] if 'Is_Messier' in data.colnames else np.zeros(len(data), dtype=bool)
    
    # Process regular stellar objects
    stellar_mask = ~is_messier
    if np.any(stellar_mask):
        ra_deg = data['RA_ICRS'][stellar_mask]
        dec_deg = data['DE_ICRS'][stellar_mask]
        distance = data['Distance_ly'][stellar_mask]
        
        ra_rad = np.radians(ra_deg)
        dec_rad = np.radians(dec_deg)
        
        # Initialize coordinate arrays
        x = np.zeros(len(data))
        y = np.zeros(len(data))
        z = np.zeros(len(data))
        
        # Calculate coordinates for stellar objects
        x[stellar_mask] = distance * np.cos(dec_rad) * np.cos(ra_rad)
        y[stellar_mask] = distance * np.cos(dec_rad) * np.sin(ra_rad)
        z[stellar_mask] = distance * np.sin(dec_rad)
        
        print(f"Processed coordinates for {np.sum(stellar_mask)} stellar objects")
    
    # Process Messier objects
    messier_mask = is_messier
    if np.any(messier_mask):
        print(f"Processing {np.sum(messier_mask)} Messier objects...")
        
        # Extract coordinates for Messier objects
        from astropy.coordinates import SkyCoord
        import astropy.units as u
        
        for i, row in enumerate(data[messier_mask]):
            try:
                coords = SkyCoord(
                    ra=row['RA_ICRS'],
                    dec=row['DE_ICRS'],
                    unit=(u.deg, u.deg),
                    distance=row['Distance_ly'] * u.lyr
                )
                
                # Convert to cartesian coordinates
                cartesian = coords.cartesian
                x[i] = cartesian.x.value
                y[i] = cartesian.y.value
                z[i] = cartesian.z.value
                
            except Exception as e:
                print(f"Error calculating coordinates for {row['Star_Name']}: {e}")
                x[i] = np.nan
                y[i] = np.nan
                z[i] = np.nan
    
    # Add calculated coordinates to the data
    data['x'] = x
    data['y'] = y
    data['z'] = z
    
    data = convert_icrs_to_radec_strings(data)

    return data

def validate_coordinates(data):
    """Validate calculated coordinates and report any issues."""
    if data is None:
        return False
        
    invalid_mask = (
        np.isnan(data['x']) | 
        np.isnan(data['y']) | 
        np.isnan(data['z'])
    )
    
    if np.any(invalid_mask):
        print("\nWarning: Found objects with invalid coordinates:")
        for row in data[invalid_mask]:
            print(f"  {row['Star_Name']}: ({row['x']}, {row['y']}, {row['z']})")
            if row['Is_Messier']:
                print(f"    Distance: {row['Distance_ly']} ly")
                print(f"    RA, Dec: {row['RA_ICRS']}, {row['DE_ICRS']}")
        return False
    
    return True

def filter_by_mag_limit(combined_data, mag_limit):
    """Filter the combined data to include only stars within the specified mag_limit."""
    mask = combined_data['Apparent_Magnitude'] <= mag_limit
    filtered_data = combined_data[mask]
    return filtered_data

def update_counts(filtered_data, mag_limit):
    """Update counts of stars in each category based on the filtered data."""
    hip_bright_count = len(filtered_data[(filtered_data['Source_Catalog'] == 'Hipparcos') &
                                         (filtered_data['Apparent_Magnitude'] <= min(1.73, mag_limit))])
    hip_mid_count = len(filtered_data[(filtered_data['Source_Catalog'] == 'Hipparcos') &
                                      (filtered_data['Apparent_Magnitude'] > 1.73) &
                                      (filtered_data['Apparent_Magnitude'] <= min(4.0, mag_limit))])
    gaia_mid_count = len(filtered_data[(filtered_data['Source_Catalog'] == 'Gaia') &
                                       (filtered_data['Apparent_Magnitude'] > 1.73) &
                                       (filtered_data['Apparent_Magnitude'] <= min(4.0, mag_limit))])
    gaia_faint_count = len(filtered_data[(filtered_data['Source_Catalog'] == 'Gaia') &
                                         (filtered_data['Apparent_Magnitude'] > 4.0) &
                                         (filtered_data['Apparent_Magnitude'] <= mag_limit)])

    counts = {
        'hip_bright_count': hip_bright_count,
        'hip_mid_count': hip_mid_count,
        'gaia_mid_count': gaia_mid_count,
        'gaia_faint_count': gaia_faint_count,
    }

    return counts


