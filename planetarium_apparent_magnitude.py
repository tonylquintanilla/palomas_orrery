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

# Import modules - using same structure as other planetarium modules
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

from messier_object_data_handler import MessierObjectHandler  # Add this with other imports

def convert_messier_to_df(messier_objects):
    """Convert Messier objects to a DataFrame format compatible with stellar data."""
    if not messier_objects:
        return pd.DataFrame()
        
    # Create DataFrame with Messier data
    messier_df = pd.DataFrame(messier_objects)
    
    # Print incoming columns to debug
    print("\nIncoming Messier DataFrame columns:", messier_df.columns.tolist())
    
    # Rename columns to match stellar data format
    column_mapping = {
        'vmag': 'Apparent_Magnitude',
        'distance_ly': 'Distance_ly',  # Ensure correct capitalization
        'type': 'Object_Type',       # Add type mapping
        'name': 'Object_Name'        # Map name separately from Star_Name
    }
    messier_df = messier_df.rename(columns=column_mapping)
    
    # Create Star_Name from messier_id and name
    messier_df['Star_Name'] = messier_df.apply(
        lambda row: f"{row['messier_id']}: {row['Object_Name']}", 
        axis=1
    )
    
    # Ensure Source_Catalog is set correctly
    messier_df['Source_Catalog'] = 'Messier'
    
    # Add required columns with placeholder values
    messier_df['Temperature'] = np.nan
    messier_df['Luminosity'] = np.nan
    messier_df['Temperature_Normalized'] = 0.5  # Middle value for color scale
    messier_df['Temperature_Method'] = 'none'
    messier_df['Spectral_Type'] = None
    messier_df['B_V'] = np.nan
    messier_df['Abs_Mag'] = np.nan
    
    # Calculate Distance_pc from Distance_ly
    messier_df['Distance_pc'] = messier_df['Distance_ly'] / 3.26156
    
    # Print final columns to debug
    print("\nFinal Messier DataFrame columns:", messier_df.columns.tolist())
    print(f"Number of Messier objects formatted: {len(messier_df)}")
    for _, row in messier_df.iterrows():
        print(f"  {row['messier_id']}: {row['Star_Name']}")
        print(f"    Distance: {row['Distance_ly']:.1f} ly")
        print(f"    Magnitude: {row['Apparent_Magnitude']:.1f}")
    
    return messier_df

def main():
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
        mag_limit = 3.5  # Default value
        user_max_coord = None

    print(f"Filtering stars and objects with apparent magnitude ≤ {mag_limit}.")
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

        # Load or fetch stellar data
        hip_data = load_or_fetch_hipparcos_data(v, hip_data_file, mag_limit)
        gaia_data = load_or_fetch_gaia_data(v, gaia_data_file, mag_limit)

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Step 3: Data Processing
        print("\nStarting data processing...")
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

        # Step 4: Star Properties
        print("\nRetrieving star properties...")
        properties_start = time.time()
        
        properties_file = 'star_properties_magnitude.pkl'
        existing_properties = load_existing_properties(properties_file)
        unique_ids = generate_unique_ids(combined_data)
        
        # Query properties for stars and handle Messier objects
        missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
        if missing_ids:
            existing_properties = query_simbad_for_star_properties(
                missing_ids, existing_properties, properties_file
            )
        
        combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
        print(f"Property retrieval completed in {time.time() - properties_start:.2f} seconds.")

        # Step 5: Calculate Stellar Parameters
        print("\nCalculating stellar parameters...")
        params_start = time.time()
        
        combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
        print(f"Parameter calculations completed in {time.time() - params_start:.2f} seconds.")

        # Step 6: Convert to DataFrame and validate
        combined_df = combined_data.to_pandas()
        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Step 7: Fetch and Process Messier Objects
        print("\nProcessing Messier objects...")
        messier_objects = messier_handler.get_visible_objects(mag_limit)
        
        if messier_objects:
            print(f"Found {len(messier_objects)} Messier objects within magnitude {mag_limit}")
            messier_df = messier_handler.create_dataframe(messier_objects)
            
            # Combine with stellar data
            if not messier_df.empty:
                combined_df = pd.concat([combined_df, messier_df], ignore_index=True)
                print(f"Added {len(messier_df)} Messier objects to visualization dataset")

        # Step 8: Analysis
        print("\nRunning analysis...")
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )

        # Parse stellar classes and set mode
        combined_df = parse_stellar_classes(combined_df)
        combined_df.attrs['mode'] = 'magnitude'

        # Step 9: Prepare Data for Visualization
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

        # Step 10: Create Visualization
        print("\nCreating visualization...")

        # Create a class to hold the figure result
        class ThreadResult:
            def __init__(self):
                self.figure = None

        def visualize(result):
            try:
                result.figure = create_3d_visualization(prepared_df, mag_limit, user_max_coord=user_max_coord)
            except Exception as e:
                print(f"Error during visualization: {e}")
                traceback.print_exc()
                result.figure = None

        # Create result holder
        result = ThreadResult()

        # Run visualization in monitored thread
        viz_thread = create_monitored_thread(shutdown_handler, visualize, result)
        viz_thread.start()
        viz_thread.join()  # Wait for thread to complete

        # Show and save figure safely in main thread
        if result.figure is not None:
            default_name = f"3d_stars_magnitude_{mag_limit}"
            show_figure_safely(result.figure, default_name)

    except Exception as e:
        print(f"Error during execution: {e}")
        traceback.print_exc()
        return
    finally:
        shutdown_handler.cleanup()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()
