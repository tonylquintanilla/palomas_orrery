"""planetarium_apparent_magnitude.py - Create 3D visualization for stars brighter than specified apparent magnitude."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import pandas as pd
import numpy as np
import astropy.units as u
import sys
import time
import traceback
import plotly.graph_objects as go

# Import modules
from data_acquisition import (
    initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data
)
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, calculate_cartesian_coordinates,
    align_coordinate_systems, select_stars_by_magnitude
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties,
    assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters
from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars
from visualization_3d import prepare_3d_data, create_3d_visualization, parse_stellar_classes
from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely
from messier_object_data_handler import MessierObjectHandler
from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia
from simbad_manager import SimbadQueryManager, SimbadConfig

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
        'star_data/star_properties_distance.pkl',
        'star_data/star_properties_magnitude.pkl'        
    ]
    
    for pkl_file in pkl_files:
#        if not os.path.exists(pkl_file):
#            print(f"Creating missing cache: {pkl_file}")
#            with open(pkl_file, 'wb') as f:
#                pickle.dump({}, f)
        
        if not os.path.exists(pkl_file):
            print(f"\n⚠️  WARNING: Cache file not found: {pkl_file}")
            print(f"   This will create an EMPTY cache file.")
            print(f"   If you have existing cache data, this may indicate a path problem.")
            response = input(f"   Create empty cache at this location? (y/n): ")
            if response.lower() == 'y':
                print(f"   Creating empty cache: {pkl_file}")
                with open(pkl_file, 'wb') as f:
                    pickle.dump({}, f)
            else:
                print(f"   Skipping cache creation. Please check your file paths.")
                print(f"   Expected location: {pkl_file}")
        elif os.path.getsize(pkl_file) < 1000:  # Less than 1KB = suspicious
                print(f"\n⚠️  WARNING: Cache file is suspiciously small: {pkl_file}")
                print(f"   Current size: {os.path.getsize(pkl_file)} bytes")
                print(f"   Expected: ~3MB (distance) or ~32MB (magnitude)")
                print(f"   This may indicate corruption or path misconfiguration.")
                response = input(f"   Continue anyway? (y/n): ")
                if response.lower() != 'y':
                    print(f"   Aborting. Please check your cache files.")
                    sys.exit(1) 

    # Quick status check using existing module
    try:
        from simbad_manager import SimbadQueryManager, SimbadConfig
        config = SimbadConfig()
        manager = SimbadQueryManager(config)
        
        # Check if magnitude PKL has any data
        props = manager.load_existing_properties('star_data/star_properties_magnitude.pkl')
        if len(props) == 0:
            print("\nWarning: star_properties_magnitude.pkl is empty")
            print("  Stars will appear gray until properties are fetched from SIMBAD")
            print("  Properties will be fetched automatically as you use the program")
        else:
            print(f"\n[OK] Loaded {len(props)} cached star properties")
    except Exception as e:
        # Silent fail is OK here - don't clutter output
        pass


def process_stars(hip_data, gaia_data, mag_limit):
    """
    Complete star processing pipeline for magnitude-based 3D visualization.
    Handles selection, coordinates, properties, and parameters.
    
    Returns:
        combined_data: The processed star data
        counts: Dictionary of star counts
        unique_ids: List of unique star identifiers
        existing_properties: Dictionary of existing star properties
        missing_ids: List of IDs that were missing (for PKL update check)
    """
    
    # Step 1: Select and combine stars from both catalogs
    from data_processing import select_stars_by_magnitude
    combined_data, counts = select_stars_by_magnitude(hip_data, gaia_data, mag_limit)
    
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
    
    properties_file = 'star_data/star_properties_magnitude.pkl'
    existing_properties = load_existing_properties(properties_file)
    unique_ids = generate_unique_ids(combined_data)
    
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
    if missing_ids:
        print(f"Querying SIMBAD for {len(missing_ids)} stars...")
        existing_properties = query_simbad_for_star_properties(
            missing_ids, existing_properties, properties_file
        )
    else:
        print("All star properties are already cached.")
    
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

    # Parse command-line arguments
    if len(sys.argv) > 1:
        try:
            mag_limit = float(sys.argv[1])
            if mag_limit < -1.44 or mag_limit > 9:
                print("Please enter a magnitude between -1.44 and 9.")
                print("Note: Sirius at magnitude -1.44 is the brightest star.")
                return

            # Check for optional scale parameter
            user_max_coord = None
            if len(sys.argv) > 2:
                user_max_coord = float(sys.argv[2])
                if user_max_coord <= 0:
                    print("Please enter a positive scale value.")
                    return
                    
        except ValueError:
            print("Invalid input for magnitude limit. Using default value of 4.")
            mag_limit = 3.5
            user_max_coord = None
    else:
        return    # prevents running this module without gui input    

    print(f"Filtering stars and objects with apparent magnitude <= {mag_limit}.")
    start_time = time.time()

    try:
        # Step 1: Initialize Messier Object Handler
        print("Initializing Messier object handler...")
        messier_handler = MessierObjectHandler()
        
        # Step 2: Data Acquisition
        print("\nStarting data acquisition...")
        v = initialize_vizier()
        hip_data_file = 'hipparcos_data_magnitude.vot'
        gaia_data_file = 'gaia_data_magnitude.vot'

#        hip_data_file = 'star_data/hipparcos_data_magnitude.vot'
#        gaia_data_file = 'star_data/gaia_data_magnitude.vot'

        # Load or fetch stellar data
        hip_data = smart_load_or_fetch_hipparcos(v, hip_data_file,
                                                mode='magnitude',
                                                limit_value=mag_limit)
        gaia_data = smart_load_or_fetch_gaia(v, gaia_data_file,
                                            mode='magnitude',
                                            limit_value=mag_limit)

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Cache status reporting
        from incremental_cache_manager import IncrementalCacheManager
        cache_mgr = IncrementalCacheManager()

        hip_status, hip_meta = cache_mgr.check_cache_validity(hip_data_file, 'magnitude', mag_limit)
        gaia_status, gaia_meta = cache_mgr.check_cache_validity(gaia_data_file, 'magnitude', mag_limit)

        print("\n" + "="*60)
        print("CACHE STATUS REPORT")
        print("="*60)
        print(f"Hipparcos: {hip_status}")
        if hip_meta:
            print(f"  Cached: {hip_meta.entry_count} stars up to magnitude {hip_meta.limit_value}")
        print(f"Gaia: {gaia_status}")
        if gaia_meta:
            print(f"  Cached: {gaia_meta.entry_count} stars up to magnitude {gaia_meta.limit_value}")

        if hip_status == 'expand' or gaia_status == 'expand':
            print("\n[OK] INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\n[OK] FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\n[OK] EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")
        
        # Step 3: Data Processing
        print("\nStarting data processing...")
        process_start = time.time()

        # Prepare the data (distances and alignment)
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        # Process all star data using consolidated function
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(
            hip_data, gaia_data, mag_limit
        )
        
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
        
        # Extract the nested values from counts for use later
        source_counts = counts.get('source_counts', {})
        estimation_results = counts.get('estimation_results', {})
        
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 4: Convert to DataFrame and apply patches
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

        # Define properties file for PKL update
        properties_file = 'star_data/star_properties_magnitude.pkl'
        
        # Only update PKL if we actually added new stars to the dataset
        if len(missing_ids) > 0:  # Now using missing_ids from process_stars
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)
            print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
        else:
            print("No new stars added - PKL file unchanged")

        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Step 5: Fetch and Process Messier Objects
        print("\nProcessing Messier objects...")
        messier_objects = messier_handler.get_visible_objects(mag_limit)
        
        if messier_objects:
            print(f"Found {len(messier_objects)} Messier objects within magnitude {mag_limit}")
            messier_df = messier_handler.create_dataframe(messier_objects)
            
            # Combine with stellar data
            if not messier_df.empty:
                combined_df = pd.concat([combined_df, messier_df], ignore_index=True)
                print(f"Added {len(messier_df)} Messier objects to visualization dataset")

        # Step 6: Analysis
        print("\nRunning analysis...")
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )

        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'magnitude'

        # Debug star counts
        print("\nDEBUG: Star count breakdown:")
        print(f"Total combined_df: {len(combined_df)}")
        print(f"Hipparcos stars: {len(combined_df[combined_df['Source_Catalog'] == 'Hipparcos'])}")
        print(f"Gaia stars: {len(combined_df[combined_df['Source_Catalog'] == 'Gaia'])}")
        print(f"Messier objects: {len(combined_df[combined_df['Source_Catalog'] == 'Messier'])}")

        # Check temperature distribution
        print(f"\nTemperature data:")
        print(f"Stars WITH valid temperature: {(combined_df['Temperature'] > 0).sum()}")
        print(f"Stars WITHOUT valid temperature: {(~(combined_df['Temperature'] > 0)).sum()}")

        # Calculate real counts for visualization
        hip_df = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        gaia_df = combined_df[combined_df['Source_Catalog'] == 'Gaia']

        hip_total = len(hip_df)
        gaia_with_temp = (gaia_df['Temperature'] > 0).sum()
        gaia_without_temp = len(gaia_df) - gaia_with_temp

        flattened_analysis = {
            'total_stars': len(combined_df),
            'plottable_hip': hip_total,
            'plottable_gaia': gaia_with_temp,
            'missing_temp': gaia_without_temp,
            'missing_lum': 0,
            'temp_le_zero': 0
        }

        combined_df.attrs['analysis'] = flattened_analysis

        # Add Has_Temperature flag for gray star display
        combined_df['Has_Temperature'] = ~combined_df['Temperature'].isna() & (combined_df['Temperature'] > 0)

        print(f"\nTemperature data availability:")
        print(f"Stars with temperature data: {combined_df['Has_Temperature'].sum()}")
        print(f"Stars without temperature data: {(~combined_df['Has_Temperature']).sum()}")

        
        # Step 7: Prepare Data for Visualization
        print("\nPreparing visualization data...")
        prepared_df = prepare_3d_data(
            combined_df,
            max_value=mag_limit,
            counts=counts,
            mode='magnitude'
        )

        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable objects found after data preparation.")
            return

        # Step 8: Create Visualization
        print("\nCreating visualization...")
        viz_start = time.time()  # ADD THIS LINE

        # Define the visualize function
        def visualize():
            try:
                fig = create_3d_visualization(prepared_df, mag_limit, user_max_coord=user_max_coord)
                
                # Show and save figure safely
                default_name = f"3d_stars_magnitude_{mag_limit}"
                show_figure_safely(fig, default_name)
                
            except Exception as e:
                print(f"Error during visualization: {e}")
                traceback.print_exc()

        # Run visualization in monitored thread
        viz_thread = create_monitored_thread(shutdown_handler, visualize)
        viz_thread.start()
        viz_thread.join()  # Wait for visualization to complete

        print(f"\nVisualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        traceback.print_exc()
        return
    finally:
        shutdown_handler.cleanup()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()