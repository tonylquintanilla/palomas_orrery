# hr_diagram_apparent_magnitude.py

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

import sys
import time
import pandas as pd  # Add at top of file with other imports

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

from visualization_2d import prepare_2d_data, create_hr_diagram

from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia

from simbad_manager import SimbadQueryManager, SimbadConfig

from plot_data_exchange import PlotDataExchange


def main():
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

        # Load or fetch data
    #    hip_data = load_or_fetch_hipparcos_data(v, hip_data_file, mag_limit)
    #    gaia_data = load_or_fetch_gaia_data(v, gaia_data_file, mag_limit)

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

        # Step 2: Data Processing
        print("Starting data processing...")
        process_start = time.time()

        # Calculate distances and align coordinates
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
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
        
        properties_file = 'star_properties_magnitude.pkl'
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

        # Step 5: Analysis and Visualization
        print("Starting analysis and visualization...")
        viz_start = time.time()

        # Convert to pandas DataFrame for visualization
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

#        config = SimbadConfig.load_from_file()
#        manager = SimbadQueryManager(config)
#        updated_properties = manager.update_calculated_properties(combined_df, properties_file)

        # Only update PKL if we actually added new stars to the dataset
        if len([uid for uid in unique_ids if uid not in existing_properties]) > 0:
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)

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
