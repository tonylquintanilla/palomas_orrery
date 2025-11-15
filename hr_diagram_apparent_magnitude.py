# hr_diagram_apparent_magnitude.py

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

import sys
import time
import pandas as pd  # Add at top of file with other imports
from datetime import datetime

# Import modules
from data_acquisition import initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, select_stars_by_magnitude,
    calculate_cartesian_coordinates, align_coordinate_systems
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties, assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters
# from visualization import analyze_magnitude_distribution, prepare_2d_data, create_hr_diagram

from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars, generate_star_count_text

from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia

from simbad_manager import SimbadQueryManager, SimbadConfig

from plot_data_exchange import PlotDataExchange

import sys
import os

from object_type_analyzer import ObjectTypeAnalyzer

from report_manager import ReportManager

from stellar_data_patches import apply_temperature_patches

from visualization_2d import prepare_2d_data, create_hr_diagram

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
    Complete star processing pipeline for magnitude-based visualization.
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
    
# After calling select_stars_by_magnitude (or process_stars)
    print(f"\nDEBUG after select_stars_by_magnitude:")
    print(f"  Combined data: {len(combined_data)} stars")

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

    # Parse command-line arguments
    if len(sys.argv) > 1:
        try:
            mag_limit = float(sys.argv[1])
            if mag_limit < -1.44 or mag_limit > 9:
                print("Please enter a magnitude between -1.44 and 9.")
                print("Note: Sirius at magnitude -1.44 is the brightest star.")
                return
        except ValueError:
            print("Invalid input for magnitude limit. Using default value of 4.")
            mag_limit = 4
#    else:
#        mag_limit = 4  # Default value
    else:
        return      # prevents running this module without gui input

    print(f"Filtering stars with apparent magnitude ≤ {mag_limit}.")
    start_time = time.time()

    try:
        # Step 1: Data Acquisition
        print("Starting data acquisition...")
        v = initialize_vizier()
        hip_data_file = 'hipparcos_data_magnitude.vot'
        gaia_data_file = 'gaia_data_magnitude.vot'

#        hip_data_file = 'star_data/hipparcos_data_magnitude.vot'
#        gaia_data_file = 'star_data/gaia_data_magnitude.vot'

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
            print("\n✔ INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\n✔ FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\n✔ EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")

# Debug: Check what smart_load_or_fetch returned
        import numpy as np
        
        if hip_data is not None:
            print(f"\nDEBUG after smart_load_or_fetch:")
            print(f"  Hipparcos: {len(hip_data)} stars returned")
            if 'Vmag' in hip_data.colnames:
                vmags = hip_data['Vmag']
                print(f"    Vmag range: {np.min(vmags):.2f} to {np.max(vmags):.2f}")
                print(f"    Stars <= {mag_limit}: {np.sum(vmags <= mag_limit)}")
        
        if gaia_data is not None:
    #        print(f"  Gaia: {len(gaia_data)} stars returned")
    #        if 'Gmag' in gaia_data.colnames:
    #            gmags = gaia_data['Gmag']
    #            print(f"    Gmag range: {np.min(gmags):.2f} to {np.max(gmags):.2f}")
    #            print(f"    Stars <= {mag_limit}: {np.sum(gmags <= mag_limit)}")

            # Debug output for Gaia
            print(f"  Gaia: {len(gaia_data)} stars returned")
            if len(gaia_data) > 0:
                gmags = gaia_data['Gmag'].filled(np.nan)
                gmags = gmags[~np.isnan(gmags)]  # Remove NaN values
                if len(gmags) > 0:
                    print(f"    Gmag range: {np.min(gmags):.2f} to {np.max(gmags):.2f}")
                    print(f"    Stars <= {mag_limit}: {len(gaia_data)}")
                else:
                    print(f"    All Gmag values are NaN")
            else:
                print(f"    No stars found in magnitude range")                

        # Step 2: Data Processing
        print("Starting data processing...")
        process_start = time.time()

        # Calculate distances and align coordinates
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        


        """
        # Select stars and combine data
        combined_data, counts = select_stars_by_magnitude(hip_data, gaia_data, mag_limit)
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
            
        combined_data = calculate_cartesian_coordinates(combined_data)
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 3: Star Properties
        print("Retrieving star properties...")
        properties_start = time.time()
        
        properties_file = 'star_data/star_properties_magnitude.pkl'
        existing_properties = load_existing_properties(properties_file)
        unique_ids = generate_unique_ids(combined_data)
        
        missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
        if missing_ids:
            existing_properties = query_simbad_for_star_properties(
                missing_ids, existing_properties, properties_file
            )
        else:
            print("All star properties are already cached.")
        
        combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
        print(f"Property retrieval completed in {time.time() - properties_start:.2f} seconds.")

        # Step 4: Calculate Stellar Parameters
        print("Calculating stellar parameters...")
        params_start = time.time()
        
#        combined_data, source_counts = calculate_stellar_parameters(combined_data)
        combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
        print(f"Parameter calculations completed in {time.time() - params_start:.2f} seconds.")
        """

# Process all star data using consolidated function
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(
            hip_data, gaia_data, mag_limit
        )
        
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
        
        # Extract the nested values from counts for use later in the code
        source_counts = counts.get('source_counts', {})
        estimation_results = counts.get('estimation_results', {})
        
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 5: Analysis and Visualization
        print("Starting analysis and visualization...")
        viz_start = time.time()

        # Convert to pandas DataFrame for visualization
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

# Expand object types BEFORE generating report
    #    print("Expanding object type descriptions...")
    #    if 'Object_Type' in combined_df.columns:
    #        combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
    #        print(f"Expanded object types for {combined_df['Object_Type_Desc'].notna().sum()} stars")
    #    else:
    #        print("Warning: Object_Type column not found in combined_df")
    #        print(f"Available columns: {combined_df.columns.tolist()}")

        # Expand object types BEFORE generating report
        print("Expanding object type descriptions...")
        from object_type_analyzer import expand_object_type  # Import here, right before use
        if 'Object_Type' in combined_df.columns:
            combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
            print(f"Expanded object types for {combined_df['Object_Type_Desc'].notna().sum()} stars")
        else:
            print("Warning: Object_Type column not found in combined_df")
            print(f"Available columns: {combined_df.columns.tolist()}")           

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

        # Analyze magnitude distribution
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )
        
        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'magnitude'

        # Flatten the analysis for visualization
        flattened_analysis = {
            'total_stars': analysis_results['data_quality']['total_stars'],
            'plottable_hip': analysis_results['plottable']['hipparcos'],
            'plottable_gaia': analysis_results['plottable']['gaia'],
            'missing_temp': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_temp'],
            'missing_lum': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_lum'],
            'temp_le_zero': 0
        }
        combined_df.attrs['analysis'] = flattened_analysis

        # Generate comprehensive report using ObjectTypeAnalyzer
        print("Generating comprehensive report...")
        analyzer = ObjectTypeAnalyzer()
        report_data = analyzer.generate_complete_report(
            combined_df,
            mode='magnitude',
            limit_value=mag_limit
        )
        print(f"Report generated with {len(report_data['sections'])} sections")

        # Save the scientific report
        report_mgr = ReportManager()
        report_mgr.save_report(report_data, archive=True)

        # Prepare data for visualization
    #    prepared_df = prepare_2d_data(combined_data)
        prepared_df = prepare_2d_data(combined_df)
        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable stars found after data preparation.")
            return

        # Calculate final counts for visualization
        total_stars = len(combined_df)
        plottable_mask = (~combined_df['Temperature'].isna()) & (~combined_df['Luminosity'].isna())
        plottable_count = plottable_mask.sum()
        missing_temp_only = combined_df['Temperature'].isna().sum()
        missing_lum_only = combined_df['Luminosity'].isna().sum()

        final_counts = {
            'hip_bright_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Hipparcos') &
                (combined_df['Apparent_Magnitude'] <= 1.73)
            ]),
            'hip_mid_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Hipparcos') &
                (combined_df['Apparent_Magnitude'] > 1.73) &
                (combined_df['Apparent_Magnitude'] <= 4.0)
            ]),
            'gaia_mid_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Gaia') &
                (combined_df['Apparent_Magnitude'] > 1.73) &
                (combined_df['Apparent_Magnitude'] <= 4.0)
            ]),
            'gaia_faint_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Gaia') &
                (combined_df['Apparent_Magnitude'] > 4.0) &
                (combined_df['Apparent_Magnitude'] <= mag_limit)
            ]),
            'total_stars': len(combined_df),
            'plottable_count': plottable_count,
        #    'missing_temp': estimation_results['final_missing_temp'],
        #    'missing_lum': estimation_results['final_missing_lum'],
            'missing_temp_only': missing_temp_only,
            'missing_lum_only': missing_lum_only,
            'estimation_results': estimation_results,
            'source_counts': source_counts
        }

        # Create visualization
        create_hr_diagram(
            combined_df=prepared_df,
            counts_dict=final_counts,
            mag_limit=mag_limit
        )

        # Save plot data for GUI
        PlotDataExchange.save_plot_data(
            combined_df=combined_df,  # Use full combined_df, not prepared_df
            counts_dict=final_counts,
            processing_times={'total': time.time() - start_time},
            mode='magnitude',
            limit_value=mag_limit
        )

        print(f"Visualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()
        return

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()
