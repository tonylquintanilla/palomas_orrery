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

from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia

from simbad_manager import SimbadQueryManager, SimbadConfig


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
#    else:
#        mag_limit = 3.5  # Default value
#        user_max_coord = None
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

        # Load or fetch stellar data
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
            print("\nOK INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\nOK FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\nOK EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")

        
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
        print(f"Other sources: {len(combined_df[~combined_df['Source_Catalog'].isin(['Hipparcos', 'Gaia', 'Messier'])])}")

        # Check temperature distribution
        print(f"\nTemperature data:")
        print(f"Stars WITH valid temperature: {(combined_df['Temperature'] > 0).sum()}")
        print(f"Stars WITHOUT valid temperature: {(~(combined_df['Temperature'] > 0)).sum()}")

        # By catalog and temperature
        for catalog in ['Hipparcos', 'Gaia']:
            cat_df = combined_df[combined_df['Source_Catalog'] == catalog]
            with_temp = (cat_df['Temperature'] > 0).sum()
            without_temp = (~(cat_df['Temperature'] > 0)).sum()
            print(f"{catalog}: {with_temp} with temp, {without_temp} without temp, total: {len(cat_df)}")

        # Flatten the analysis for visualization (ADD THIS SECTION)

    #    flattened_analysis = {
    #        'total_stars': analysis_results['data_quality']['total_stars'],
    #        'plottable_hip': analysis_results['plottable']['hipparcos'],
    #        'plottable_gaia': analysis_results['plottable']['gaia'],
    #        'missing_temp': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_temp'],
    #        'missing_lum': analysis_results['data_quality']['total_stars'] - analysis_results['data_quality']['valid_lum'],
    #        'temp_le_zero': 0
    #        }

        # After creating combined_df, calculate real counts
        hip_df = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        gaia_df = combined_df[combined_df['Source_Catalog'] == 'Gaia']

        hip_total = len(hip_df)
        gaia_with_temp = (gaia_df['Temperature'] > 0).sum()
        gaia_without_temp = len(gaia_df) - gaia_with_temp

        flattened_analysis = {
            'total_stars': len(combined_df),
            'plottable_hip': hip_total,  # Use actual count: 518
            'plottable_gaia': gaia_with_temp,  # 1,042
            'missing_temp': gaia_without_temp,  # 17
            'missing_lum': 0,
            'temp_le_zero': 0
        }

        combined_df.attrs['analysis'] = flattened_analysis

        # Step 8.5: Add Has_Temperature flag for gray star display
        combined_df['Has_Temperature'] = ~combined_df['Temperature'].isna() & (combined_df['Temperature'] > 0)

        print(f"\nTemperature data availability:")
        print(f"Stars with temperature data: {combined_df['Has_Temperature'].sum()}")
        print(f"Stars without temperature data: {(~combined_df['Has_Temperature']).sum()}")

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
