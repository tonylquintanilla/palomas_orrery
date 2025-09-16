import numpy as np
from astropy.table import vstack
from data_processing import estimate_vmag_from_gaia

def select_stars(hip_data, gaia_data, mode='magnitude', limit_value=None):
    """
    Unified star selection function applying consistent catalog separation logic.
    
    Parameters:
        hip_data (astropy.table.Table): Hipparcos catalog data
        gaia_data (astropy.table.Table): Gaia catalog data
        mode (str): 'magnitude' or 'distance'
        limit_value (float): Maximum distance in light-years or magnitude limit
            
    Returns:
        tuple: (combined_data, counts)
            - combined_data: astropy Table with selected stars
            - counts: dictionary with star counts by category
    """
    print(f"\nSelecting stars by {mode}...")
    
    all_selected_stars = []
    counts = {
        'hip_bright_count': 0,
        'hip_mid_count': 0,
        'gaia_mid_count': 0,
        'gaia_faint_count': 0,
        'total_stars': 0,
        'plottable_count': 0,
        'missing_temp_only': 0,  # Initialize with defaults
        'missing_lum_only': 0,   # Initialize with defaults
        'source_counts': {},      # Initialize empty dict for source counts
        'estimation_results': {}  # Initialize empty dict for estimation results
    }
    
    if hip_data is not None:
        if mode == 'distance':
            primary_mask = hip_data['Distance_ly'] <= limit_value
        else:  # magnitude mode
            primary_mask = hip_data['Vmag'] <= limit_value
            
        # Always apply magnitude-based catalog separation for Hipparcos
        magnitude_mask = hip_data['Vmag'] <= 4.0  # Only use Hipparcos for Vmag <= 4.0
        
        # Combine masks
        hip_stars = hip_data[primary_mask & magnitude_mask]
        
        if len(hip_stars) > 0:
            # Count categories
            bright_mask = hip_stars['Vmag'] <= 1.73
            mid_mask = (hip_stars['Vmag'] > 1.73) & (hip_stars['Vmag'] <= 4.0)
            
            hip_stars['Source_Catalog'] = 'Hipparcos'
            hip_stars['Apparent_Magnitude'] = hip_stars['Vmag']
            
            counts['hip_bright_count'] = int(np.sum(bright_mask))
            counts['hip_mid_count'] = int(np.sum(mid_mask))
            
            all_selected_stars.append(hip_stars)
            print(f"Selected {len(hip_stars)} Hipparcos stars")
    
    if gaia_data is not None:
        if mode == 'distance':
            primary_mask = gaia_data['Distance_ly'] <= limit_value
        else:  # magnitude mode
            if 'Estimated_Vmag' not in gaia_data.colnames:
                gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)
            primary_mask = gaia_data['Estimated_Vmag'] <= limit_value
            
        gaia_stars = gaia_data[primary_mask]
        
        if len(gaia_stars) > 0:
            # Ensure Estimated_Vmag is present
            if 'Estimated_Vmag' not in gaia_stars.colnames:
                gaia_stars['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_stars)
                
            gaia_stars['Source_Catalog'] = 'Gaia'
            gaia_stars['Apparent_Magnitude'] = gaia_stars['Estimated_Vmag']
            
            # Always apply magnitude-based catalog separation for Gaia
            magnitude_mask = gaia_stars['Apparent_Magnitude'] > 4.0
            gaia_stars = gaia_stars[magnitude_mask]
            
            if len(gaia_stars) > 0:
                counts['gaia_faint_count'] = len(gaia_stars)
                all_selected_stars.append(gaia_stars)
                print(f"Selected {len(gaia_stars)} Gaia stars")
    
    # Combine selected stars
    if not all_selected_stars:
        print(f"No stars found within specified {mode} limit")
        return None, counts
        
    combined_data = vstack(all_selected_stars)
    counts['total_stars'] = len(combined_data)
    
    # Print summary
    print("\nFinal Selection Summary:")
    print(f"Hipparcos bright stars (Vmag <= 1.73): {counts['hip_bright_count']}")
    print(f"Hipparcos mid-range stars (1.73 < Vmag <= 4.0): {counts['hip_mid_count']}")
    print(f"Gaia faint stars (Vmag > 4.0): {counts['gaia_faint_count']}")
    print(f"Total stars: {counts['total_stars']}")
    
    return combined_data, counts