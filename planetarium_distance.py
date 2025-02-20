# planetarium_distance.py

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)
import numpy as np  # Add this import
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

def process_stars(hip_data, gaia_data, max_light_years):
    """Process stars for distance-based 3D visualization with full count tracking."""
    # Use the unified selection function
    combined_data, counts = select_stars(
        hip_data, 
        gaia_data, 
        mode='distance', 
        limit_value=max_light_years
    )
    
    if combined_data is None:
        return None, {}

    # Add 3D-specific processing
    combined_data = calculate_cartesian_coordinates(combined_data)
    
    # Calculate stellar parameters
    combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)

    # Update counts with results from stellar parameter calculations
    counts['source_counts'] = source_counts
    counts['estimation_results'] = estimation_results

    # Safely calculate plottable count only if columns exist
    if 'Temperature' in combined_data.colnames and 'Luminosity' in combined_data.colnames:
        plottable_mask = (
            (~combined_data['Temperature'].isna()) &
            (~combined_data['Luminosity'].isna())
        )
        counts['plottable_count'] = int(np.sum(plottable_mask))
    else:
        print("Warning: 'Temperature' or 'Luminosity' column not found in combined_data.")
        counts['plottable_count'] = 0

    # Update missing parameter counts
    counts['missing_temp_only'] = estimation_results['final_missing_temp']
    counts['missing_lum_only'] = estimation_results['final_missing_lum']

    return combined_data, counts


def main():
    # Initialize shutdown handler
    shutdown_handler = PlotlyShutdownHandler()

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
        
        hip_data_file = f'hipparcos_data_distance.vot'
        gaia_data_file = f'gaia_data_distance.vot'
        
        # Load or fetch data with parallax constraint
        hip_data = load_or_fetch_hipparcos_data(v, hip_data_file, 
                                               parallax_constraint=f">={min_parallax_mas}")
        gaia_data = load_or_fetch_gaia_data(v, gaia_data_file, 
                                           parallax_constraint=f">={min_parallax_mas}")

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Step 2: Data Processing
        print("Starting data processing...")
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
        
        properties_file = f'star_properties_distance.pkl'
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
        
        # Parse stellar classes
        combined_df = parse_stellar_classes(combined_df)
        
        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'distance'

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


