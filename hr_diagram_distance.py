"""hr_diagram_distance.py - Create HR diagram for stars within specified distance."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

import sys
import time
import pandas as pd  # Add at top of file with other imports
from datetime import datetime

from data_acquisition_distance import (
    initialize_vizier, fetch_hipparcos_data, fetch_gaia_data,
    calculate_parallax_limit, process_hipparcos_data, process_gaia_data
)
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, calculate_cartesian_coordinates,
    align_coordinate_systems
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties,
    assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters

from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars

from visualization_2d import prepare_2d_data, create_hr_diagram

# Uses the select_stars function from the catalog_selection module
from catalog_selection import select_stars

from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia

from simbad_manager import SimbadQueryManager, SimbadConfig

from plot_data_exchange import PlotDataExchange

import sys
import os

from object_type_analyzer import ObjectTypeAnalyzer

from report_manager import ReportManager

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
        
        # Check if distance PKL has any data
        props = manager.load_existing_properties('star_data/star_properties_distance.pkl')
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
    Complete star processing pipeline for distance-based visualization.
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
    
    properties_file = 'star_data/star_properties_distance.pkl'
    existing_properties = load_existing_properties(properties_file)
    unique_ids = generate_unique_ids(combined_data)
    
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
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

    # Parse command-line arguments for max light-years
    if len(sys.argv) > 1:
        try:
            max_light_years = float(sys.argv[1])
            if max_light_years <= 0:
                print("Please enter a positive number of light-years.")
                print("Note: Current maximum reliable distance is 100.1 light-years.")
                return
        except ValueError:
            print("Invalid input for light-years limit. Using default value of 100.1.")
            max_light_years = 100.1
#    else:
#        max_light_years = 100.1  # Default value
    else:
        print("Error: Distance parameter required")
        return        

    print(f"Filtering stars within {max_light_years} light-years.")
    start_time = time.time()

    try:
        # Step 1: Data Acquisition
        print("Starting data acquisition...")
        v = initialize_vizier()
        min_parallax_mas = calculate_parallax_limit(max_light_years)
        
        # Define data files
        hip_data_file = 'hipparcos_data_distance.vot'
        gaia_data_file = 'gaia_data_distance.vot'
        
#        hip_data_file = 'star_data/hipparcos_data_distance.vot'
#        gaia_data_file = 'star_data/gaia_data_distance.vot'

        # Load or fetch data with parallax constraint
        parallax_constraint = f">={min_parallax_mas}"

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

        # Cache status reporting (ADD THIS ENTIRE BLOCK)
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

        if hip_status == 'expand' or gaia_status == 'expand':
            print("\n✓ INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\n✓ FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\n✓ EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")        
        
        # Step 2: Data Processing
        process_start = time.time()
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        if gaia_data is not None:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

        """
        # Select stars and combine data
        combined_data, counts = select_stars(hip_data, gaia_data, mode='distance', limit_value=max_light_years)
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
            
        combined_data = calculate_cartesian_coordinates(combined_data)
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 3: Star Properties
        print("Retrieving star properties...")
        properties_start = time.time()
        
        properties_file = 'star_data/star_properties_distance.pkl'
        existing_properties = load_existing_properties(properties_file)
        unique_ids = generate_unique_ids(combined_data)
        
        missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
        if missing_ids:
            existing_properties = query_simbad_for_star_properties(
                missing_ids, existing_properties, properties_file
            )
        
        combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
        print(f"Property retrieval completed in {time.time() - properties_start:.2f} seconds.")

        # Step 4: Calculate Stellar Parameters
        print("Calculating stellar parameters...")
        params_start = time.time()
        
        combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
        print(f"Parameter calculations completed in {time.time() - params_start:.2f} seconds.")
        """

        # Process all star data using consolidated function
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(
            hip_data, gaia_data, max_light_years
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

        # ADD THIS SECTION - Expand object types BEFORE generating report
        print("Expanding object type descriptions...")
        from object_type_analyzer import expand_object_type
        if 'Object_Type' in combined_df.columns:
            combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)
            print(f"Expanded object types for {combined_df['Object_Type_Desc'].notna().sum()} stars")
        else:
            print("Warning: Object_Type column not found in combined_df")
            print(f"Available columns: {combined_df.columns.tolist()}")

        print(f"DEBUG: Columns in combined_df: {combined_df.columns.tolist()}")

        # Generate comprehensive report using ObjectTypeAnalyzer
        print("Generating comprehensive report...")
        analyzer = ObjectTypeAnalyzer()

        # Prepare counts_dict from the existing counts
        counts_dict = {
            'Hipparcos_bright': counts.get('hip_bright_count', 0),
            'Hipparcos_mid': counts.get('hip_mid_count', 0),
            'Gaia_mid': counts.get('gaia_mid_count', 0),
            'Gaia_faint': counts.get('gaia_faint_count', 0),
            'total': counts.get('total_stars', len(combined_df))
        }

        # Generate the complete report
        report_data = analyzer.generate_complete_report(
            combined_df=combined_df,
            counts_dict=counts_dict,
            processing_times={'total': time.time() - start_time},
            mode='distance',
            limit_value=max_light_years
        )

        print(f"Report generated with {len(report_data['sections'])} sections")

        # Save the scientific report
        report_mgr = ReportManager()
        report_mgr.save_report(report_data, archive=True)

        # After applying the patch
        mizar = combined_df[combined_df['HIP'] == 65378]
        if len(mizar) > 0:
            print(f"\nMizar data after patch:")
            print(f"Temperature: {mizar['Temperature'].iloc[0]}")
            print(f"Luminosity: {mizar['Luminosity'].iloc[0]}")
            print(f"Is Luminosity NaN? {pd.isna(mizar['Luminosity'].iloc[0])}")
            print(f"Abs_Mag: {mizar['Abs_Mag'].iloc[0]}")

        # Define properties file for PKL update
        properties_file = 'star_data/star_properties_distance.pkl'      

        # Only update PKL if we actually added new stars to the dataset
#        if len([uid for uid in unique_ids if uid not in existing_properties]) > 0:
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
        analyze_magnitude_distribution(combined_df, mag_limit=None)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='distance',
            max_value=max_light_years
        )
        
        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'distance'

        # Flatten the analysis for visualization (ADD THIS ENTIRE BLOCK)
        flattened_analysis = {
            'total_stars': analysis_results['data_quality']['total_stars'],
            'plottable_hip': analysis_results['plottable']['hipparcos'],
            'plottable_gaia': analysis_results['plottable']['gaia'],
            'missing_temp': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_temp'],
            'missing_lum': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_lum'],
            'temp_le_zero': 0
        }
        combined_df.attrs['analysis'] = flattened_analysis

        # Prepare data for visualization
    #    prepared_df = prepare_2d_data(combined_data)
        prepared_df = prepare_2d_data(combined_df)
        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable stars found after data preparation.")
            return

        # In main() before final_counts:
        plottable_mask = (
            (~combined_df['Temperature'].isna()) & 
            (~combined_df['Luminosity'].isna()) &
            (
                ((combined_df['Source_Catalog'] == 'Hipparcos') & 
                (combined_df['Apparent_Magnitude'] <= 4.0)) |
                ((combined_df['Source_Catalog'] == 'Gaia') & 
                (combined_df['Apparent_Magnitude'] > 4.0))
            )
        )
        plottable_count = plottable_mask.sum()

        # Calculate final counts for visualization
        final_counts = {
            'hip_bright_count': counts.get('hip_bright_count', 0),
            'hip_mid_count': counts.get('hip_mid_count', 0),
            'gaia_mid_count': counts.get('gaia_mid_count', 0),
            'gaia_faint_count': counts.get('gaia_faint_count', 0),
            'total_stars': counts.get('total_stars', len(combined_df)),
            'plottable_count': plottable_count,
            'missing_temp_only': estimation_results.get('final_missing_temp', 0),
            'missing_lum_only': estimation_results.get('final_missing_lum', 0),
            'estimation_results': estimation_results,
            'source_counts': source_counts
        }

        # Right before creating the plot
        print(f"\nTotal stars in dataframe: {len(combined_df)}")
        print(f"Stars with both T and L: {len(combined_df[(combined_df['Temperature'] > 0) & (combined_df['Luminosity'] > 0)])}")

        # Check if Mizar made it to plotting
        mizar_in_plot = combined_df[combined_df['HIP'] == 65378]
        if len(mizar_in_plot) > 0:
            print(f"Mizar in final plot data: YES")
            print(f"  Will plot at: T={mizar_in_plot['Temperature'].iloc[0]}, L={mizar_in_plot['Luminosity'].iloc[0]}")
        else:
            print(f"Mizar in final plot data: NO - FILTERED OUT!")

        # Create visualization
        create_hr_diagram(
            combined_df=prepared_df,
            counts_dict=final_counts,
            max_light_years=max_light_years
        )

        # Save plot data for GUI
        PlotDataExchange.save_plot_data(
            combined_df=combined_df,  # Use full combined_df, not prepared_df
            counts_dict=final_counts,
            processing_times={'total': time.time() - start_time},
            mode='distance',
            limit_value=max_light_years
        )
        print("Plot data saved to last_plot_data.json")

        # Save plot data with complete report for GUI
    #    exchange_data = {
    #        'plot_stats': {
    #            'mode': 'distance' if 'distance' in sys.argv[0] else 'magnitude',
    #            'limit_value': max_light_years if 'distance' in sys.argv[0] else max_light_years,
    #            'total_stars': len(combined_df),
    #            'temp_valid': (~combined_df['Temperature'].isna()).sum(),
    #            'temp_missing': combined_df['Temperature'].isna().sum(),
    #            'lum_valid': (~combined_df['Luminosity'].isna()).sum(),
    #            'lum_missing': combined_df['Luminosity'].isna().sum(),
    #            'catalog_counts': counts_dict,
    #            'magnitude_stats': {
    #                'min': float(combined_df['Apparent_Magnitude'].min()),
    #                'max': float(combined_df['Apparent_Magnitude'].max()),
    #                'mean': float(combined_df['Apparent_Magnitude'].mean())
    #            } if 'Apparent_Magnitude' in combined_df.columns else None,
    #            'processing_times': {'total': time.time() - start_time},
    #            'timestamp': datetime.now().isoformat()
    #        },
    #        'report_data': report_data  # Complete report from analyzer
    #    }

    #    PlotDataExchange.save_plot_data(exchange_data)
    #    print("Plot data saved with complete report")        

        print(f"Visualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()
        return

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()

