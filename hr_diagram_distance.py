"""hr_diagram_distance.py - Create HR diagram for stars within specified distance."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

import sys
import time
import pandas as pd  # Add at top of file with other imports

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

def main():
    # Parse command-line arguments for max light-years
    if len(sys.argv) > 1:
        try:
            max_light_years = float(sys.argv[1])
            if max_light_years <= 0:
                print("Please enter a positive number of light-years.")
                print("Note: Current maximum reliable distance is 100 light-years.")
                return
        except ValueError:
            print("Invalid input for light-years limit. Using default value of 100.")
            max_light_years = 100.0
    else:
        max_light_years = 100.0  # Default value

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
        
        # Load or fetch data with parallax constraint
        parallax_constraint = f">={min_parallax_mas}"

        hip_data = fetch_hipparcos_data(v, hip_data_file, min_parallax_mas)
        gaia_data = fetch_gaia_data(v, gaia_data_file, min_parallax_mas)

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Step 2: Data Processing
        process_start = time.time()
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        if gaia_data is not None:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

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
        
        properties_file = 'star_properties_distance.pkl'
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

        # Step 5: Analysis and Visualization
        print("Starting analysis and visualization...")
        viz_start = time.time()

        # Convert to pandas DataFrame for visualization
        combined_df = combined_data.to_pandas()
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
        
        # Prepare data for visualization
        prepared_df = prepare_2d_data(combined_data)
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

        '''
        # Calculate final counts for visualization
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
            'gaia_mid_count': 0,  # We don't use Gaia stars in this range

            'gaia_faint_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Gaia') & 
                (combined_df['Apparent_Magnitude'] > 4.0)
            ]),

            'total_stars': (
                # Only count stars we actually plot
                len(combined_df[
                    ((combined_df['Source_Catalog'] == 'Hipparcos') & 
                    (combined_df['Apparent_Magnitude'] <= 4.0)) |
                    ((combined_df['Source_Catalog'] == 'Gaia') & 
                    (combined_df['Apparent_Magnitude'] > 4.0))
                ])
            ),

            'total_stars': len(combined_df),
            'plottable_count': plottable_count,
            'missing_temp_only': estimation_results['final_missing_temp'],
            'missing_lum_only': estimation_results['final_missing_lum'],
            'estimation_results': estimation_results,
            'source_counts': source_counts
        }
        '''

        # Create visualization
        create_hr_diagram(
            combined_df=prepared_df,
            counts_dict=final_counts,
            max_light_years=max_light_years
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

