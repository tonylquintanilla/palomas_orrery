# visualization_core.py

import numpy as np
import pandas as pd
import re
import plotly.graph_objects as go
from constants import (
    object_type_mapping, class_mapping, hover_text_sun, stellar_class_labels
)
from stellar_parameters import calculate_stellar_parameters
from star_notes import unique_notes

def format_value(value, format_spec, default="Unknown"):
    """Format values consistently across visualizations."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return default
    try:
        return format_spec.format(value)
    except (ValueError, TypeError):
        return default


def create_hover_text(df, include_3d=False):
    """
    Create hover text for plots with identification of estimated values and special cases.
    
    Parameters:
        df (pandas DataFrame): DataFrame containing star data
        include_3d (bool): Whether to include 3D coordinate information
        
    Returns:
        list: List of formatted hover texts for each star
    """
    hover_text_list = []
    
    for _, row in df.iterrows():
        hover_text = f'<b>{row["Star_Name"]}</b><br>'
        
        # Add coordinates if 3D
        if include_3d:
            hover_text += (f'Distance: {format_value(row["Distance_pc"], ".2f")} pc '
                         f'({format_value(row["Distance_ly"], ".2f")} ly)<br>')
        
        # Handle luminosity with estimation notes
        lum_estimated = row.get('Luminosity_Estimated', False)
        hover_text += f'Luminosity: {format_value(row["Luminosity"], ".6f")} Lsun'
        if lum_estimated:
            hover_text += ' (estimated from spectral type)'
            # Add note about uncertainty for peculiar or variable stars
            sp_type = str(row.get("Spectral_Type", "")).upper()
            if 'P' in sp_type or 'VAR' in sp_type:
                hover_text += '<br>Luminosity note: Star is peculiar/variable; luminosity estimate may have higher uncertainty.'
        hover_text += '<br>'
        
        # Temperature info with estimation note if applicable
        temp_estimated = row.get('Temperature_Estimated', False)
        hover_text += f'Temperature: {format_value(row["Temperature"], ".0f")} K'
        if temp_estimated:
            method = row.get('Temperature_Method', 'spectral type')
            hover_text += f' (estimated from {method})'
        hover_text += '<br>'
        
        # Add other stellar properties
        hover_text += f'Absolute Magnitude: {format_value(row["Abs_Mag"], ".2f")}<br>'
        hover_text += f'Apparent Magnitude: {format_value(row["V_mag"], ".2f")}<br>'
        
        # Add spectral and stellar class info
        sp_type = row.get("Spectral_Type", "Unknown")
        hover_text += f'Spectral Type: {sp_type}'
        if 'P' in str(sp_type).upper():
            hover_text += ' (Peculiar)'
        hover_text += '<br>'
        
        stellar_class = row.get("Stellar_Class", "Unknown")
        hover_text += f'Stellar Class: {stellar_class}'
        if stellar_class in class_mapping:
            hover_text += f' ({class_mapping[stellar_class]})'
        hover_text += '<br>'
        
        # Object type with expanded description
        obj_type = row.get("Object_Type_Desc", "Unknown")
        hover_text += f'Object Type: {obj_type}<br>'
        
        # Add parallax quality info if available
        if 'e_Plx' in row and 'Plx' in row:
            try:
                rel_error = abs(row['e_Plx'] / row['Plx'])
                if rel_error > 0.2:  # 20% error threshold
                    hover_text += f'Warning: High parallax uncertainty ({rel_error:.1%})<br>'
            except (TypeError, ZeroDivisionError):
                pass
        
        # Add custom notes from unique_notes
        note = unique_notes.get(row["Star_Name"], "None.")
        hover_text += f'Note: {note}'
        
        hover_text_list.append(hover_text)
    
    return hover_text_list

def prepare_temperature_colors():
    """Define consistent temperature color scales."""
    return {
        1300: 'rgb(255, 0, 0)',        # Red for L
        2400: 'rgb(255, 0, 0)',        # Red for M
        3700: 'rgb(255, 165, 0)',      # Orange for K
        5200: 'rgb(255, 255, 0)',      # Yellow for G
        6000: 'rgb(255, 255, 255)',    # White for F
        7500: 'rgb(173, 216, 230)',    # Light Blue for A
        10000: 'rgb(0, 0, 255)',       # Blue for B
        30000: 'rgb(0, 0, 139)',       # Dark Blue for O
        50000: 'rgb(75, 0, 130)',      # Indigo for upper O limit
    }

def analyze_star_counts(combined_df):
    """Analyze star counts and exclusion reasons in detail."""
    print("\nDetailed Star Count Analysis:")
    
    # Initial catalog breakdown
    hips_mask = combined_df['Source_Catalog'] == 'Hipparcos'
    total_hip = np.sum(hips_mask)
    total_gaia = len(combined_df) - total_hip
    
    print(f"\nInitial Counts by Catalog:")
    print(f"Hipparcos stars: {total_hip}")
    print(f"Gaia stars: {total_gaia}")
    print(f"Total unique stars: {len(combined_df)}")
    
    # Temperature analysis
    has_temp = ~pd.isna(combined_df['Temperature'])
    valid_temp = has_temp & (combined_df['Temperature'] > 0)
    print(f"\nTemperature Analysis:")
    print(f"Stars with temperature data: {np.sum(has_temp)}")
    print(f"Stars with valid temperature > 0: {np.sum(valid_temp)}")
    print(f"Stars with temperature ≤ 0: {np.sum(has_temp & ~valid_temp)}")
    
    # Luminosity analysis
    has_lum = ~pd.isna(combined_df['Luminosity'])
    print(f"\nLuminosity Analysis:")
    print(f"Stars with luminosity data: {np.sum(has_lum)}")
    
    # Plottable analysis
    plottable = valid_temp & has_lum
    
    print(f"\nPlottable Stars Analysis:")
    print(f"Stars meeting all criteria: {np.sum(plottable)}")
    print(f"Excluded due to missing/invalid temperature: {len(combined_df) - np.sum(valid_temp)}")
    print(f"Excluded due to missing luminosity: {np.sum(~has_lum)}")
    
    # Catalog breakdown of plottable stars
    plottable_hip = np.sum(plottable & hips_mask)
    plottable_gaia = np.sum(plottable & ~hips_mask)
    
    print(f"\nPlottable Stars by Catalog:")
    print(f"Hipparcos: {plottable_hip}")
    print(f"Gaia: {plottable_gaia}")
    
    return {
        'total_stars': len(combined_df),
        'plottable_stars': np.sum(plottable),
        'plottable_hip': plottable_hip,
        'plottable_gaia': plottable_gaia,
#        'missing_temp': len(combined_df) - np.sum(valid_temp),     # incorrect
#        'missing_lum': np.sum(~has_lum),                           # incorrect
        'temp_le_zero': np.sum(has_temp & ~valid_temp),
        'missing_temp_only': len(combined_df[combined_df['Temperature'].isna() & ~combined_df['Luminosity'].isna()]),
        'missing_lum_only': len(combined_df[~combined_df['Temperature'].isna() & combined_df['Luminosity'].isna()]),
        'missing_both': len(combined_df[combined_df['Temperature'].isna() & combined_df['Luminosity'].isna()])
    }

def analyze_magnitude_distribution(data, mag_limit=None):
    """Analyze and print the distribution of stars by magnitude ranges."""
    # [Existing analyze_magnitude_distribution code]
# def analyze_magnitude_distribution(data, mag_limit=8.5): 
    """
    Analyze and print the distribution of stars by magnitude ranges.

    Parameters:
        data (astropy Table or pandas DataFrame): The data containing star information.
        mag_limit (float): The upper limit of the apparent magnitude to consider.

    Returns:
        int: Total number of stars analyzed.
    """
    # Convert data to pandas DataFrame if it's an astropy Table
    if not isinstance(data, pd.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    print("\nSTAR MAGNITUDE DISTRIBUTION ANALYSIS")
    print("=" * 50)

    # Define magnitude ranges and descriptions
    mag_ranges = [
        (-2, -1, "Very bright stars (mag -2 to -1)"),
        (-1, 0, "Brightest stars (mag -1 to 0)"),
        (0, 1, "1st magnitude stars (mag 0 to 1)"),
        (1, 1.73, "Upper bright stars (mag 1 to 1.73)"),
        (1.74, 2, "Lower bright stars (mag 1.74 to 2)"),
        (2, 3, "3rd magnitude stars (mag 2 to 3)"),
        (3, 4, "4th magnitude stars (mag 3 to 4)"),
        (4, 5, "5th magnitude stars (mag 4 to 5)"),
        (5, 6, "6th magnitude stars (mag 5 to 6)"),
        (6, mag_limit, f"Faint stars (mag 6 to {mag_limit})")
    ]

    print(f"\nDistribution by Apparent Magnitude and Source:")
    print(f"{'Magnitude Range':<25} {'Total':>8} {'Hipparcos':>10} {'Gaia':>8} {'%':>7}")
    print("-" * 60)

    total_stars = 0
    for mag_min, mag_max, desc in mag_ranges:
        # Create mask for stars within the magnitude range
        mask = df['Apparent_Magnitude'].between(mag_min, mag_max)
        total = mask.sum()
        # Masks for each source catalog
        hip_mask = mask & (df['Source_Catalog'] == 'Hipparcos')
        gaia_mask = mask & (df['Source_Catalog'] == 'Gaia')
        hip_count = hip_mask.sum()
        gaia_count = gaia_mask.sum()

        if total > 0:
            percent = (total / len(df)) * 100
            print(f"{desc:<25} {total:>8d} {hip_count:>10d} {gaia_count:>8d} {percent:>6.1f}%")
            total_stars += total

    print("-" * 60)
    print(f"Total stars: {total_stars:,d}")

    return total_stars

def analyze_and_report_stars(combined_df, mode='distance', max_value=None):
    """
    Analyze star data and report statistics for both distance and magnitude-limited samples.
    
    Parameters:
        combined_df: pandas DataFrame containing the star data
        mode: 'distance' or 'magnitude' to adjust reporting format
        max_value: Maximum distance in light-years or magnitude limit
        
    Returns:
        dict: Analysis results containing counts and statistics
    """
    # Initialize analysis dictionary
    analysis = {
        'catalog_counts': {
            'hipparcos': {
                'bright': np.sum((combined_df['Source_Catalog'] == 'Hipparcos') & 
                               (combined_df['Apparent_Magnitude'] <= 1.73)),
                'mid': np.sum((combined_df['Source_Catalog'] == 'Hipparcos') & 
                            (combined_df['Apparent_Magnitude'] > 1.73) & 
                            (combined_df['Apparent_Magnitude'] <= 4.0)),
                'faint': np.sum((combined_df['Source_Catalog'] == 'Hipparcos') & 
                              (combined_df['Apparent_Magnitude'] > 4.0))
            },
            'gaia': {
                'mid': np.sum((combined_df['Source_Catalog'] == 'Gaia') & 
                            (combined_df['Apparent_Magnitude'] > 1.73) & 
                            (combined_df['Apparent_Magnitude'] <= 4.0)),
                'faint': np.sum((combined_df['Source_Catalog'] == 'Gaia') & 
                              (combined_df['Apparent_Magnitude'] > 4.0))
            }
        },
        'data_quality': {
            'total_stars': len(combined_df),
            'valid_temp': np.sum(~pd.isna(combined_df['Temperature'])),
            'valid_lum': np.sum(~pd.isna(combined_df['Luminosity'])),
            'valid_bv': np.sum(~pd.isna(combined_df['B_V'])),
            'temp_le_zero': np.sum((~pd.isna(combined_df['Temperature'])) & 
                                 (combined_df['Temperature'] <= 0))
        }
    }

    # Calculate plottable stars
    plottable = (
        ~pd.isna(combined_df['Temperature']) & 
        ~pd.isna(combined_df['Luminosity']) & 
        (combined_df['Temperature'] > 0)
    )
    
    analysis['plottable'] = {
        'total': np.sum(plottable),
        'hipparcos': np.sum(plottable & (combined_df['Source_Catalog'] == 'Hipparcos')),
        'gaia': np.sum(plottable & (combined_df['Source_Catalog'] == 'Gaia'))
    }

    # Print analysis
    print("\nStar Count Analysis:")
    print(f"Total stars analyzed: {analysis['data_quality']['total_stars']:,d}")

    # Print catalog breakdown
    print("\nCatalog Breakdown:")
    hip_bright = analysis['catalog_counts']['hipparcos']['bright']
    hip_mid = analysis['catalog_counts']['hipparcos']['mid']
    gaia_mid = analysis['catalog_counts']['gaia']['mid']
    gaia_faint = analysis['catalog_counts']['gaia']['faint']

    print(f"Hipparcos bright (≤1.73): {hip_bright:,d}")
    print(f"Mid-range stars (1.73-4.0):")
    print(f"  - From Hipparcos: {hip_mid:,d}")
    print(f"  - From Gaia: {gaia_mid:,d}")
    print(f"Gaia faint (>4.0): {gaia_faint:,d}")

    # Mode-specific reporting
    if mode == 'distance':
        print(f"\nDistance-based Analysis:")
        print(f"Stars within {max_value} light-years: {analysis['data_quality']['total_stars']:,d}")
    else:  # magnitude mode
        print(f"\nMagnitude-based Analysis:")
        print(f"Stars brighter than magnitude {max_value}: {analysis['data_quality']['total_stars']:,d}")

    # Data quality report
    print("\nData Quality:")
    print(f"Stars with valid temperature: {analysis['data_quality']['valid_temp']:,d}")
    print(f"Stars with valid luminosity: {analysis['data_quality']['valid_lum']:,d}")
    print(f"Stars with valid B-V color: {analysis['data_quality']['valid_bv']:,d}")
    
    # Plottable stars report
    print("\nPlottable Stars:")
    print(f"Total plottable: {analysis['plottable']['total']:,d}")
    print(f"  - From Hipparcos: {analysis['plottable']['hipparcos']:,d}")
    print(f"  - From Gaia: {analysis['plottable']['gaia']:,d}")

    return analysis

def generate_star_count_text(counts_dict, combined_df=None):
    """Generate detailed text about star counts from different catalogs."""
    # Get all counts
    total_stars = counts_dict['total_stars']
    plottable_count = counts_dict['plottable_count']
    missing_temp = counts_dict['missing_temp_only']
    missing_lum = counts_dict['missing_lum_only']
    
    # Catalog breakdowns
    hip_bright = counts_dict.get('hip_bright_count', 0)
    hip_mid = counts_dict.get('hip_mid_count', 0)
    gaia_mid = counts_dict.get('gaia_mid_count', 0)
    gaia_faint = counts_dict.get('gaia_faint_count', 0)
    
    # Get the bright star estimates from the estimation_results
    estimation_results = counts_dict.get('estimation_results', {})
    bright_star_estimates = estimation_results.get('bright_star_estimates', 0)
    
    return (
        f"<br>     Total stars plotted: <span style='background-color: red; color: red'>{total_stars:,d}</span>: "
        f"<a href='https://www.cosmos.esa.int/web/hipparcos/catalogues' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Hipparcos</a> bright (Vmag ≤ 1.73): <span style='background-color: red; color: red'>{hip_bright}</span> stars. "
        f"Hipparcos mid (1.73 < Vmag ≤ 4.0): <span style='background-color: red; color: red'>{hip_mid}</span> stars. "
    #    f"<a href='https://vizier.cds.unistra.fr/viz-bin/VizieR-3'>Gaia</a> mid (1.73 < Vmag ≤ 4.0): <span style='background-color: red; color: red'>{gaia_mid}</span> stars. "
        f"<a href='https://www.cosmos.esa.int/gaia' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Gaia</a> faint (Vmag > 4.0): <span style='background-color: red; color: red'>{gaia_faint}</span> stars."
        f"<br>     Search: <a href='https://www.nasa.gov/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>NASA</a>. "
        f"Search: <a href='http://simbad.u-strasbg.fr/simbad/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Simbad</a> "
        f"with the star name, for example: \"* alf Aql\", for star data (right-click will keep the hovertext box open to read the name). " 
        f"<br>     -- Python script by Tony Quintanilla, with assistance from ChatGPT, Claude, Gemini, and DeepSeek, February 2025."
        
    )
