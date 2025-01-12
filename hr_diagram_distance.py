"""hr_diagram_distance.py - Create HR diagram for stars within specified distance."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

import sys
import time

# Import modules - same structure as hr_diagram_apparent_magnitude.py
from data_acquisition import (
    initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data,
    calculate_parallax_limit
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

def select_stars_by_distance(hip_data, gaia_data, max_light_years):
    """
    Select stars based on distance criteria.
    Similar to select_stars_by_magnitude but using distance as the filter.
    """
    print("\nSelecting stars by distance...")
    
    all_selected_stars = []
    hip_count = 0
    gaia_count = 0
    
    # Process Hipparcos stars
    if hip_data is not None:
        distance_mask = hip_data['Distance_ly'] <= max_light_years
        hip_stars = hip_data[distance_mask]
        if len(hip_stars) > 0:
            hip_stars['Source_Catalog'] = 'Hipparcos'
            hip_stars['Apparent_Magnitude'] = hip_stars['Vmag']
            hip_count = len(hip_stars)
            print(f"Selected {hip_count} stars from Hipparcos within {max_light_years} light-years")
            all_selected_stars.append(hip_stars)
    
    # Process Gaia stars
    if gaia_data is not None:
        distance_mask = gaia_data['Distance_ly'] <= max_light_years
        gaia_stars = gaia_data[distance_mask]
        if len(gaia_stars) > 0:
            gaia_stars['Source_Catalog'] = 'Gaia'
            gaia_stars['Apparent_Magnitude'] = gaia_stars['Estimated_Vmag']
            gaia_count = len(gaia_stars)
            print(f"Selected {gaia_count} stars from Gaia within {max_light_years} light-years")
            all_selected_stars.append(gaia_stars)
    
    if not all_selected_stars:
        print(f"No stars found within {max_light_years} light-years")
        return None, {}
    
    # Combine selected stars
    from astropy.table import vstack
    combined_data = vstack(all_selected_stars)
    
    print("\nSelection Summary:")
    print(f"Hipparcos stars: {hip_count}")
    print(f"Gaia stars: {gaia_count}")
    print(f"Total stars: {len(combined_data)}")
    
    counts = {
        'hip_count': hip_count,
        'gaia_count': gaia_count,
    }
    
    return combined_data, counts

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
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        if gaia_data is not None:
            gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

        # Select stars and combine data
        combined_data, counts = select_stars_by_distance(hip_data, gaia_data, max_light_years)
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
            
        combined_data = calculate_cartesian_coordinates(combined_data)

#        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

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
        
    #    combined_data, source_counts = calculate_stellar_parameters(combined_data)
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
        
    #    combined_data, _ = select_stars_by_distance(hip_data, gaia_data, max_light_years)
    #    if combined_data is None:
    #        print("No valid stars found to process. Exiting.")
    #        return

    #    combined_df = combined_data.to_pandas()  # Now this should work without issues
    #    if len(combined_df) == 0:
    #        print("No stars available for visualization after processing.")
    #        return

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
            'gaia_mid_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Gaia') & 
                (combined_df['Apparent_Magnitude'] > 1.73) & 
                (combined_df['Apparent_Magnitude'] <= 4.0)
            ]),
            'gaia_faint_count': len(combined_df[
                (combined_df['Source_Catalog'] == 'Gaia') & 
                (combined_df['Apparent_Magnitude'] > 4.0)
            ]),
            'source_counts': source_counts,
            'total_stars': len(combined_df),
            'plottable_count': len(combined_df),
            'missing_temp_only': len(combined_df),
            'missing_lum_only': len(combined_df)   
        }

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

