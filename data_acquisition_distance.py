"""data_acquisition_distance.py - Module for fetching stellar data based on distance."""

import numpy as np
from astropy.table import Table, vstack
from astroquery.vizier import Vizier
from astropy.coordinates import Angle

def initialize_vizier():
    """Initialize Vizier with unlimited rows and all columns."""
    try:
        vizier = Vizier(columns=['*'], row_limit=-1)
        return vizier
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Vizier: {e}")

def calculate_parallax_limit(max_light_years):
    """Calculate minimum parallax for given distance in light-years."""
    max_distance_pc = max_light_years / 3.26156
    min_parallax_mas = (1 / max_distance_pc) * 1000
    return min_parallax_mas

def fetch_gaia_data(vizier, gaia_data_file, min_parallax_mas):
    """Fetch stars from Gaia EDR3 catalog."""
    try:
        print(f"Fetching Gaia stars with parallax >= {min_parallax_mas} mas...")
        gaia_result = vizier.query_constraints(
            catalog="I/350/gaiaedr3",
            parallax=f">={min_parallax_mas}"
        )
        if not gaia_result:
            return None
            
        gaia_data = gaia_result[0]
        print(f"Found {len(gaia_data)} Gaia stars")
        
        # Save the data
        gaia_data.write(gaia_data_file, format='votable', overwrite=True)
        print(f"Saved Gaia data to {gaia_data_file}")
        
        return gaia_data
    except Exception as e:
        raise RuntimeError(f"Error fetching Gaia data: {e}")

def fetch_hipparcos_data(vizier, hip_data_file, min_parallax_mas):
    """Fetch stars from Hipparcos catalog."""
    try:
        print(f"Fetching Hipparcos stars with parallax >= {min_parallax_mas} mas...")
        hip_result = vizier.query_constraints(
            catalog="I/239/hip_main",
            Plx=f">={min_parallax_mas}"
        )
        if not hip_result:
            return None
            
        hip_data = hip_result[0]
        print(f"Found {len(hip_data)} Hipparcos stars")
        
        # Save the data
        hip_data.write(hip_data_file, format='votable', overwrite=True)
        print(f"Saved Hipparcos data to {hip_data_file}")
        
        return hip_data
    except Exception as e:
        raise RuntimeError(f"Error fetching Hipparcos data: {e}")

def process_gaia_data(gaia_data, max_light_years):
    """Process Gaia data and calculate distances."""
    if gaia_data is None:
        return None
        
    try:
        # Calculate distances
        parallax_mas = gaia_data['Plx']
        parallax_arcsec = parallax_mas / 1000.0
        distance_pc = 1 / parallax_arcsec
        distance_ly = distance_pc * 3.26156
        
        # Add distance columns
        gaia_data['Distance_pc'] = distance_pc
        gaia_data['Distance_ly'] = distance_ly
        
        # Filter by distance and validity
        mask = (np.isfinite(distance_ly) & 
                (distance_ly > 0) & 
                (distance_ly <= max_light_years))
        
        gaia_data = gaia_data[mask]
        
        # Estimate V magnitudes
        gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)
        
        return gaia_data
    except Exception as e:
        raise RuntimeError(f"Error processing Gaia data: {e}")

def process_hipparcos_data(hip_data, max_light_years):
    """Process Hipparcos data and calculate distances."""
    if hip_data is None:
        return None
        
    try:
        # Calculate distances
        parallax_mas = hip_data['Plx']
        parallax_arcsec = parallax_mas / 1000.0
        distance_pc = 1 / parallax_arcsec
        distance_ly = distance_pc * 3.26156
        
        # Add distance columns
        hip_data['Distance_pc'] = distance_pc
        hip_data['Distance_ly'] = distance_ly
        
        # Filter by distance and validity
        mask = (np.isfinite(distance_ly) & 
                (distance_ly > 0) & 
                (distance_ly <= max_light_years))
        
        hip_data = hip_data[mask]
        
        # Verify V magnitudes exist
        if 'Vmag' not in hip_data.colnames:
            return None
            
        return hip_data
    except Exception as e:
        raise RuntimeError(f"Error processing Hipparcos data: {e}")

def align_coordinate_systems(hip_data):
    """Align coordinate systems between catalogs."""
    if hip_data is None:
        return None
        
    try:
        if 'RA_ICRS' not in hip_data.colnames:
            if 'RAICRS' in hip_data.colnames:
                hip_data.rename_column('RAICRS', 'RA_ICRS')
            elif 'RAhms' in hip_data.colnames:
                ra_hms = hip_data['RAhms']
                hip_data['RA_ICRS'] = Angle(ra_hms, unit='hourangle').degree
        
        if 'DE_ICRS' not in hip_data.colnames:
            if 'DEICRS' in hip_data.colnames:
                hip_data.rename_column('DEICRS', 'DE_ICRS')
            elif 'DEdms' in hip_data.colnames:
                dec_dms = hip_data['DEdms']
                hip_data['DE_ICRS'] = Angle(dec_dms, unit='deg').degree
                
        return hip_data
    except Exception as e:
        raise RuntimeError(f"Error aligning coordinate systems: {e}")

def estimate_vmag_from_gaia(gaia_data):
    """Convert Gaia G magnitudes to Johnson V magnitudes."""
    vmag = np.full(len(gaia_data), np.nan)
    
    if all(col in gaia_data.colnames for col in ['Gmag', 'BP-RP']):
        bp_rp = gaia_data['BP-RP']
        mask = ~np.isnan(gaia_data['Gmag']) & ~np.isnan(bp_rp)
        vmag[mask] = (gaia_data['Gmag'][mask] - 
                     (-0.0257 - 0.0924*bp_rp[mask] - 
                      0.1623*bp_rp[mask]**2 + 
                      0.0090*bp_rp[mask]**3))
    return vmag

def fetch_stellar_data(max_light_years):
    """
    Main function to fetch stellar data within specified distance.
    
    Args:
        max_light_years (float): Maximum distance in light-years
        
    Returns:
        astropy.table.Table: Combined stellar data
    """
    try:
        # Initialize Vizier
        vizier = initialize_vizier()
        
        # Calculate parallax limit
        min_parallax_mas = calculate_parallax_limit(max_light_years)
        
        # Define data files
        hip_data_file = 'hipparcos_data_distance.vot'
        gaia_data_file = 'gaia_data_distance.vot'
        
        # Fetch data from both catalogs
        hip_data = fetch_hipparcos_data(vizier, hip_data_file, min_parallax_mas)
        gaia_data = fetch_gaia_data(vizier, gaia_data_file, min_parallax_mas)
        
        # Process data
        hip_data = process_hipparcos_data(hip_data, max_light_years)
        gaia_data = process_gaia_data(gaia_data, max_light_years)
        hip_data = align_coordinate_systems(hip_data)
        
        # Combine data with proper selection logic
        from catalog_selection import select_stars
        combined_data, _ = select_stars(hip_data, gaia_data, 'distance', max_light_years)
        
        return combined_data
        
    except Exception as e:
        raise RuntimeError(f"Error fetching stellar data: {e}")

