# planetarium_distance.py

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)
import numpy as np  # Add this import
import pandas as pd  # Add this import
import sys
import time
import plotly.io as pio
import traceback

from astropy.table import vstack

from visualization_core import analyze_and_report_stars

from data_acquisition import (
    initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data,
    calculate_parallax_limit
)
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, calculate_cartesian_coordinates,
    align_coordinate_systems 
    #select_stars_by_distance
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties,
    assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters

from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars

from visualization_3d import prepare_3d_data, create_3d_visualization, parse_stellar_classes

from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely

from catalog_selection import select_stars

from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia

from simbad_manager import SimbadQueryManager, SimbadConfig

import sys
import os

# Fix Windows console encoding for Unicode symbols
if sys.platform == 'win32':
    # Set console code page to UTF-8
    os.system('chcp 65001 > nul')
    # Ensure Python uses UTF-8 for stdout
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def ensure_cache_system_ready():
    """
    Minimal cache system initialization using existing modules.
    Ensures PKL files exist and checks cache health.
    """
    import os
    import pickle
    
    # Create empty PKL files if they don't exist
    pkl_files = [
        'star_properties_distance.pkl',
        'star_properties_magnitude.pkl'
    ]
    
    for pkl_file in pkl_files:
        if not os.path.exists(pkl_file):
            print(f"Creating missing cache: {pkl_file}")
            with open(pkl_file, 'wb') as f:
                pickle.dump({}, f)
        
    # Quick status check using existing module
    try:
        from simbad_manager import SimbadQueryManager, SimbadConfig
        config = SimbadConfig()
        manager = SimbadQueryManager(config)
        
        # Check if distance PKL has any data
        props = manager.load_existing_properties('star_properties_distance.pkl')
        if len(props) == 0:
            print("\nWarning: star_properties_distance.pkl is empty")
            print("  Stars will appear gray until properties are fetched from SIMBAD")
            print("  Properties will be fetched automatically as you use the program")
        else:
            print(f"\n[OK] Loaded {len(props)} cached star properties")
    except Exception as e:
        # Silent fail is OK here - don't clutter output
        pass


def process_stars(hip_data, gaia_data, max_light_years):
    """
    Complete star processing pipeline for distance-based 3D visualization.
    Handles selection, coordinates, properties, and parameters.
    
    Returns:
        combined_data: The processed star data
        counts: Dictionary of star counts
        unique_ids: List of unique star identifiers
        existing_properties: Dictionary of existing star properties
        missing_ids: List of IDs that were missing (for PKL update check)
    """
    
    # Step 1: Select and combine stars from both catalogs
    from catalog_selection import select_stars
    combined_data, counts = select_stars(
        hip_data, 
        gaia_data, 
        mode='distance', 
        limit_value=max_light_years
    )
    
    if combined_data is None:
        return None, {}, [], {}, []
    
    # Step 2: Calculate 3D cartesian coordinates
    from data_processing import calculate_cartesian_coordinates
    combined_data = calculate_cartesian_coordinates(combined_data)
    
    # Step 3: Load and query star properties from SIMBAD
    from star_properties import (
        load_existing_properties, 
        generate_unique_ids, 
        query_simbad_for_star_properties,
        assign_properties_to_data
    )
    
    properties_file = 'star_properties_distance.pkl'
    existing_properties = load_existing_properties(properties_file)
    unique_ids = generate_unique_ids(combined_data)
    
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
    # DEBUG: Add this to see what's happening
    print(f"DEBUG: Total stars: {len(unique_ids)}")
    print(f"DEBUG: Stars in PKL: {len(existing_properties)}")
    print(f"DEBUG: Missing from PKL: {len(missing_ids)}")
    
    if missing_ids:
        print(f"Querying SIMBAD for {len(missing_ids)} stars...")
        existing_properties = query_simbad_for_star_properties(
            missing_ids, existing_properties, properties_file
        )
    
    # Assign properties to the combined data
    combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
    
    # Step 4: Calculate stellar parameters (temperature, luminosity)
    from stellar_parameters import calculate_stellar_parameters
    combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
    
    # Step 5: Update counts with all the statistics
    counts['source_counts'] = source_counts
    counts['estimation_results'] = estimation_results
    
    # Calculate plottable count (stars with both temperature and luminosity)
    if 'Temperature' in combined_data.colnames and 'Luminosity' in combined_data.colnames:
        import numpy as np
        plottable_mask = (
    #        (~combined_data['Temperature'].isna()) &
    #        (~combined_data['Luminosity'].isna())
            (~np.isnan(combined_data['Temperature'])) &
            (~np.isnan(combined_data['Luminosity']))
        )
        counts['plottable_count'] = int(np.sum(plottable_mask))
    else:
        print("Warning: 'Temperature' or 'Luminosity' column not found in combined_data.")
        counts['plottable_count'] = 0
    
    counts['missing_temp_only'] = estimation_results.get('final_missing_temp', 0)
    counts['missing_lum_only'] = estimation_results.get('final_missing_lum', 0)
    
    # Return all needed variables for PKL update check
    return combined_data, counts, unique_ids, existing_properties, missing_ids


def main():

    # CALL THE CACHE INITIALIZATION HERE - FIRST THING IN main()
    ensure_cache_system_ready()

    # Initialize shutdown handler
    shutdown_handler = PlotlyShutdownHandler()

    # Parse command-line arguments for max light-years
    if len(sys.argv) > 1:
        try:
            max_light_years = float(sys.argv[1])
            if max_light_years <= 0:
                print("Please enter a positive number of light-years.")
                print("Note: Current maximum reliable distance is 100.1 light-years.")      # increasing limit from 100 to 100.1 ly
                return
        except ValueError:
            print("Invalid input for light-years limit. Using default value of 100.1")
            max_light_years = 100.1
    else:
        # MODIFIED: No default - require explicit parameter
        print("ERROR: Distance parameter required")
        return  # Exit without running

    print(f"Filtering stars within {max_light_years} light-years.")
    start_time = time.time()

    try:
        # Step 1: Data Acquisition
        print("Starting data acquisition...")
        v = initialize_vizier()
        min_parallax_mas = calculate_parallax_limit(max_light_years)
        
        hip_data_file = f'hipparcos_data_distance.vot'
        gaia_data_file = f'gaia_data_distance.vot'
        
        hip_data = smart_load_or_fetch_hipparcos(v, hip_data_file, 
                                                mode='distance',
                                                limit_value=max_light_years,
                                                parallax_constraint=f">={min_parallax_mas}")
        gaia_data = smart_load_or_fetch_gaia(v, gaia_data_file, 
                                            mode='distance',
                                            limit_value=max_light_years,
                                            parallax_constraint=f">={min_parallax_mas}")

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # ============ CACHE STATUS REPORT ============
        from incremental_cache_manager import IncrementalCacheManager
        cache_mgr = IncrementalCacheManager()

        hip_status, hip_meta = cache_mgr.check_cache_validity(hip_data_file, 'distance', max_light_years)
        gaia_status, gaia_meta = cache_mgr.check_cache_validity(gaia_data_file, 'distance', max_light_years)

        print("\n" + "="*60)
        print("CACHE STATUS REPORT")
        print("="*60)
        print(f"Hipparcos: {hip_status}")
        if hip_meta:
            print(f"  Cached: {hip_meta.entry_count} stars up to {hip_meta.limit_value} ly")
            print(f"  Cache date: {hip_meta.query_date}")
        print(f"Gaia: {gaia_status}")
        if gaia_meta:
            print(f"  Cached: {gaia_meta.entry_count} stars up to {gaia_meta.limit_value} ly")
            print(f"  Cache date: {gaia_meta.query_date}")

        # Explain what happened
        if hip_status == 'expand' or gaia_status == 'expand':
            print("\nOK INCREMENTAL FETCH PERFORMED - only new data fetched")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\nOK FILTERED EXISTING CACHE - no network queries needed")
        elif hip_status == 'exact' and gaia_status == 'exact':
            print("\nOK EXACT CACHE HIT - using existing data")
        elif hip_status == 'missing' or gaia_status == 'missing':
            print("\nWarning: FULL FETCH PERFORMED - no cache found")
        print("="*60 + "\n")
        # ============ END CACHE STATUS REPORT ============

        # Step 2: Data Processing
        print("Starting data processing...")
        process_start = time.time()

        # Prepare the data (distances and alignment)
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)

        if gaia_data is not None:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

        # Process everything - NOTE THE CHANGE HERE: now returns 5 values
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(hip_data, gaia_data, max_light_years)

        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return

        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 3: Analysis and Visualization
        print("Starting analysis and visualization...")
        viz_start = time.time()

        # Convert to pandas DataFrame for visualization
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

        # Only update PKL if we actually added new stars to the dataset
        if len(missing_ids) > 0:  # Now using missing_ids from process_stars
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            properties_file = 'star_properties_distance.pkl'
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)
            print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
        else:
            print("No new stars added - PKL file unchanged")

        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Debug: Find Hipparcos stars without temperature
        print("\n" + "="*60)
        print("DEBUG: Finding Hipparcos stars without temperature")
        print("="*60)

        hip_stars = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        hip_no_temp = hip_stars[(hip_stars['Temperature'].isna()) | (hip_stars['Temperature'] <= 0)]

        print(f"Total Hipparcos stars: {len(hip_stars)}")
        print(f"Hipparcos with valid temperature: {(hip_stars['Temperature'] > 0).sum()}")
        print(f"Hipparcos without valid temperature: {len(hip_no_temp)}")

        if len(hip_no_temp) > 0:
            print("\nDetails of Hipparcos stars without temperature:")
            for idx, star in hip_no_temp.iterrows():
                print(f"\n  Star: {star.get('Star_Name', 'Unknown')}")
                print(f"  HIP: {star.get('HIP', 'N/A')}")
                print(f"  Vmag: {star.get('Vmag', 'N/A')}")
                
                # Safe distance formatting
                distance = star.get('Distance_ly')
                if distance is not None and not pd.isna(distance):
                    print(f"  Distance: {distance:.1f} ly")
                else:
                    print(f"  Distance: N/A")
                    
                print(f"  Spectral Type: {star.get('Spectral_Type', 'N/A')}")
                print(f"  B-V: {star.get('B_V', 'N/A')}")
                print(f"  Temperature: {star.get('Temperature', 'N/A')}")
                print(f"  Object Type: {star.get('Object_Type', 'N/A')}")
                
                # Check why temperature is missing
                if pd.isna(star.get('B_mag')) or pd.isna(star.get('V_mag')):
                    print(f"  Issue: Missing B or V magnitude (B={star.get('B_mag', 'N/A')}, V={star.get('V_mag', 'N/A')})")
                if pd.isna(star.get('Spectral_Type')) or star.get('Spectral_Type') == '':
                    print(f"  Issue: Missing spectral type")

        print("="*60)

        # Analyze magnitude distribution
        analyze_magnitude_distribution(combined_df, mag_limit=None)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='distance',
            max_value=max_light_years
        )
        
        # Parse stellar classes
        combined_df = parse_stellar_classes(combined_df)
        
        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'distance'
        # Flatten the analysis for visualization (ADD THIS SECTION)

        # Same logic for BOTH planetarium_distance.py and planetarium_apparent_magnitude.py
        hip_df = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        gaia_df = combined_df[combined_df['Source_Catalog'] == 'Gaia']

        hip_total = len(hip_df)
        gaia_with_temp = (gaia_df['Temperature'] > 0).sum()
        gaia_without_temp = len(gaia_df) - gaia_with_temp

        flattened_analysis = {
            'total_stars': len(combined_df),
            'plottable_hip': hip_total,  # All Hipparcos stars
            'plottable_gaia': gaia_with_temp,  # Gaia WITH temperature
            'missing_temp': gaia_without_temp,  # Gaia WITHOUT temperature
            'missing_lum': 0,
            'temp_le_zero': 0
        }

        combined_df.attrs['analysis'] = flattened_analysis  # Use flattened version 

        final_counts = {
            'hip_bright_count': counts['hip_bright_count'],
            'hip_mid_count': counts['hip_mid_count'],
            'gaia_mid_count': counts['gaia_mid_count'],
            'gaia_faint_count': counts['gaia_faint_count'],
            'total_stars': counts['total_stars'],
            'plottable_count': counts['plottable_count'],
            'missing_temp_only': counts['missing_temp_only'],
            'missing_lum_only': counts['missing_lum_only'],
            'source_counts': counts['source_counts'],
            'estimation_results': counts['estimation_results']
        }

        # Prepare data for visualization
        prepared_df = prepare_3d_data(
            combined_df,  # your DataFrame from combined_data
            max_value=max_light_years,
            counts=final_counts,
            mode='distance'  # Explicitly set mode to 'distance'
        )

        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable stars found after data preparation.")
            return

        create_3d_visualization(
            combined_df=prepared_df,
            max_value=max_light_years,
            user_max_coord=None  # Optional: you can pass a custom scale value here
        )

# Define the visualize function here, just before the visualization code
        def visualize():
            try:
                prepared_df = prepare_3d_data(
                    combined_df,
                    max_value=max_light_years,
                    counts=final_counts,
                    mode='distance'
                )
                
                if prepared_df is None or len(prepared_df) == 0:
                    print("No plottable stars found after data preparation.")
                    return
                    
                # Create visualization
                fig = create_3d_visualization(prepared_df, max_light_years)
                
                # Show and save figure safely
                default_name = f"3d_stars_distance_{int(max_light_years)}ly"
                show_figure_safely(fig, default_name)
                
            except Exception as e:
                print(f"Error during visualization: {e}")
                traceback.print_exc()

        # Replace the existing visualization code with:
        viz_thread = create_monitored_thread(shutdown_handler, visualize)
        viz_thread.start()
        viz_thread.join()  # Wait for visualization to complete

        print(f"Visualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        traceback.print_exc()
        return
    finally:
        shutdown_handler.cleanup()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()


