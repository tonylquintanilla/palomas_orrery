# visualization_3d.py

import numpy as np
import pandas as pd
import re
import plotly.graph_objects as go

from constants import (
    object_type_mapping, class_mapping, hover_text_sun, stellar_class_labels
)
from save_utils import save_plot
from star_notes import unique_notes
from astropy.coordinates import SkyCoord
import astropy.units as u

from visualization_core import (
    format_value, create_hover_text, prepare_temperature_colors,
    generate_star_count_text
)

def parse_stellar_classes(df):
    """Parse stellar classes from spectral types."""
    def parse_luminosity_class(spectral_type):
        if spectral_type is None or pd.isna(spectral_type):
            return "Unknown"
        match = re.search(r'([IV]+)', str(spectral_type))
        if match:
            luminosity_class = match.group(1)
            return class_mapping.get(luminosity_class, luminosity_class)
        return "Unknown"
    
    df['Stellar_Class'] = df['Spectral_Type'].apply(parse_luminosity_class)
    return df

def prepare_3d_data(combined_df, max_value, counts, mode=None):
    """Prepare data for 3D visualization with proper handling of Messier objects."""
    print("\nPreparing data for 3D visualization...")
    
    # Create mask for Messier objects based on Source_Catalog
    messier_mask = combined_df['Source_Catalog'] == 'Messier'
    
    # Remove any duplicate Messier objects that might be in the stellar data
    stellar_objects = combined_df[~messier_mask].copy()
    stellar_objects = stellar_objects[
        ~stellar_objects['Star_Name'].str.contains('M[0-9]+:', na=False)
    ]    
    # Print diagnostic information
    print(f"\nData composition before separation:")
    print(f"Total objects: {len(combined_df)}")
    print(f"Messier objects: {messier_mask.sum()}")
    print(f"Stellar objects: {(~messier_mask).sum()}")
    
    # Separate Messier objects from stars
    messier_objects = combined_df[messier_mask].copy() if messier_mask.any() else pd.DataFrame()
    stellar_objects = combined_df[~messier_mask].copy()
    
    # Process stellar objects
    plottable_stars = stellar_objects[
        ~pd.isna(stellar_objects['Temperature']) & 
        ~pd.isna(stellar_objects['Luminosity']) & 
        (stellar_objects['Temperature'] > 0)
    ].copy()
    
    print(f"\nProcessing stellar objects:")
    print(f"Total stars: {len(stellar_objects)}")
    print(f"Plottable stars: {len(plottable_stars)}")
    
    # Temperature normalization for stars
    temp_min = 1300
    temp_max = 50000
    plottable_stars['Temperature_Clipped'] = plottable_stars['Temperature'].clip(lower=temp_min, upper=temp_max)
    plottable_stars['Temperature_Normalized'] = (plottable_stars['Temperature_Clipped'] - temp_min) / (temp_max - temp_min)

    # Calculate marker sizes based on apparent magnitude
    def calculate_marker_size(app_mag, is_messier=False):
        if is_messier:
            return 20  # Fixed size for Messier objects
        if pd.isna(app_mag):
            return 2
        mag_min, mag_max = -1.44, 9
        size_min, size_max = 2, 24
        app_mag_clipped = np.clip(app_mag, mag_min, mag_max)
        log_brightness = -0.4 * app_mag_clipped
        log_brightness_min = -0.4 * mag_max
        log_brightness_max = -0.4 * mag_min
        normalized_brightness = (log_brightness - log_brightness_min) / (log_brightness_max - log_brightness_min)
        return np.clip(size_min + (size_max - size_min) * normalized_brightness, size_min, size_max)
    
    plottable_stars['Marker_Size'] = plottable_stars['Apparent_Magnitude'].apply(
        lambda x: calculate_marker_size(x, False)
    )
    
    # Create hover text for stars
    plottable_stars['Hover_Text'] = create_hover_text(plottable_stars, include_3d=True)
    plottable_stars['Min_Hover_Text'] = plottable_stars['Star_Name'].apply(
        lambda name: f'<b>{name}</b>'
    )
    
    # Process Messier objects if present
    if not messier_objects.empty:
        print(f"\nProcessing {len(messier_objects)} Messier objects")
        
        # Set fixed properties for Messier objects
        messier_objects['Temperature_Normalized'] = 0.07  # This is 7% in the color scale, about yellow or white
        messier_objects['Marker_Size'] = 30  # Fixed size
        messier_objects['Source_Catalog'] = 'Messier'  # Ensure this is set
                
        # Check for missing coordinates
        missing_coords = messier_objects[pd.isna(messier_objects['x']) | 
                                       pd.isna(messier_objects['y']) | 
                                       pd.isna(messier_objects['z'])]
        if not missing_coords.empty:
            print("\nWarning: Some Messier objects have missing coordinates:")
            for _, obj in missing_coords.iterrows():
                print(f"  {obj['Star_Name']}")
        else:
            print("All Messier objects have valid coordinates")
        
        # Combine plottable stars and Messier objects
        plottable_df = pd.concat([plottable_stars, messier_objects], ignore_index=True)
        print(f"\nFinal dataset:")
        print(f"Stars: {len(plottable_stars)}")
        print(f"Messier objects: {len(messier_objects)}")
        print(f"Total: {len(plottable_df)}")
    else:
        plottable_df = plottable_stars
        print("\nNo Messier objects to process")
    
    # Add metadata
    plottable_df.attrs['mode'] = mode
    plottable_df.attrs['max_value'] = max_value
    
    return plottable_df

def format_value(value, format_spec, default="Unknown"):
    """
    Format a value using Python's built-in format function.
    
    Parameters:
        value: The value to format
        format_spec (str): Format specification (e.g., ".2f", ".0f", etc.)
        default (str): Default value to return if formatting fails
        
    Returns:
        str: The formatted value or default string if formatting fails
    """
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return default
    try:
        # Use Python's built-in format function which correctly handles format specs
        return format(value, format_spec)
    except (ValueError, TypeError):
        return default

def create_hover_text(df, include_3d=False):
    """Create hover text with graceful handling of missing columns."""
    hover_text_list = []

    for _, row in df.iterrows():
        star_name = row["Star_Name"]
        note = unique_notes.get(star_name, "None.")

        # Get distance values, defaulting to NaN (ASSIGN THESE FIRST)
        distance_pc = row.get('Distance_pc', np.nan)
        distance_ly = row.get('Distance_ly', np.nan)

        # Calculate ly if missing but we have pc
        if pd.isna(distance_ly) and pd.notna(distance_pc):
            distance_ly = distance_pc * 3.26156

        # Format distance strings, handling NaN explicitly
        pc_str = f"{distance_pc:.2f}" if pd.notna(distance_pc) else "Unknown"
        ly_str = f"{distance_ly:.2f}" if pd.notna(distance_ly) else "Unknown"

        # Build the hover_text string incrementally using concatenation
        hover_text = f'<b>{star_name}</b><br><br>'
        hover_text += f'{note}<br><br>'
        hover_text += f'Distance: {pc_str} pc ({ly_str} ly)<br>'
        # Get values directly and format them if they exist
        hover_text += f'Object Type: {format_value(row.get("Object_Type_Desc"), "")}<br>'
        hover_text += f'Stellar Class: {format_value(row.get("Stellar_Class"), "")}<br>'
        hover_text += f'Temperature: {format_value(row.get("Temperature"), ".0f")} K<br>'
        hover_text += f'Luminosity: {format_value(row.get("Luminosity"), ".6f")} Lsun<br>'
        hover_text += f'Absolute Magnitude: {format_value(row.get("Abs_Mag"), ".2f")}<br>'
        hover_text += f'Apparent Magnitude: {format_value(row.get("Apparent_Magnitude"), ".2f")}<br>'
        hover_text += f'Spectral Type: {format_value(row.get("Spectral_Type"), "")}<br>'
        hover_text += f'Source Catalog: {format_value(row.get("Source_Catalog"), "")}<br>'

        if 'Marker_Size' in row.index:
            hover_text += f'<br>Marker Size: {format_value(row["Marker_Size"], ".2f")} px'

        hover_text_list.append(hover_text)

    return hover_text_list

def create_notable_stars_list(combined_df, unique_notes, user_max_coord=None):
    """
    Create list of notable stars, using vector distance for filtering.
    
    Parameters:
        combined_df: DataFrame containing star data
        unique_notes: Dictionary of notable star descriptions
        user_max_coord: Optional maximum display boundary value
    """
    notable_stars = []
    mode = combined_df.attrs.get('mode', 'distance')
    max_value = combined_df.attrs.get('max_value', 100.0)

    print(f"\nCreating notable stars list:")
    print(f"Mode: {mode}")
    print(f"Max distance: {max_value} light-years")
    if user_max_coord is not None:
        print(f"Display boundaries: ±{user_max_coord} light-years")

    for star_name in sorted(unique_notes.keys()):
        # Check if it's a Messier object
        is_messier = star_name.startswith('M ') or star_name.startswith('M')

        # Find the star in the combined_df
        if is_messier:
            messier_num = star_name.split()[1] if ' ' in star_name else star_name[1:]
            star_data = combined_df[
                combined_df['Star_Name'].str.contains(f"M{messier_num}", na=False)
            ]
        else:
            star_data = combined_df[combined_df['Star_Name'] == star_name]

        if not star_data.empty:
            star_row = star_data.iloc[0]
            
            # Get coordinates
            x = float(star_row['x'])
            y = float(star_row['y'])
            z = float(star_row['z'])
            
            # Calculate actual distance from Earth
            distance = np.sqrt(x*x + y*y + z*z)

            # Apply filtering based on mode
            should_include = True
            if mode == 'distance':
                if distance > max_value:
                    print(f"Skipping {star_name} - beyond distance limit ({distance:.1f} > {max_value} ly)")
                    should_include = False
            elif mode == 'magnitude':
                if star_row['Apparent_Magnitude'] > max_value and not is_messier:
                    print(f"Skipping {star_name} - too faint (mag {star_row['Apparent_Magnitude']:.1f} > {max_value})")
                    should_include = False

            # Apply display boundary filtering if specified
            if should_include and user_max_coord is not None:
                # Check if star falls outside the display boundaries
                if (abs(x) > user_max_coord or 
                    abs(y) > user_max_coord or 
                    abs(z) > user_max_coord):
                    print(f"Skipping {star_name} - outside display boundaries (±{user_max_coord} ly)")
                    should_include = False

            if should_include:
                # Use same distance for camera positioning since already calculated
                direction = {
                    'x': x/distance,
                    'y': y/distance,
                    'z': z/distance
                }
                notable_stars.append({
                    'label': star_name,
                    'method': 'relayout',
                    'args': [{
                        'scene.camera': {
                            'center': {'x': 0, 'y': 0, 'z': 0},
                            'eye': {'x': -0.005 * direction['x'],
                                  'y': -0.005 * direction['y'],
                                  'z': -0.005 * direction['z']},
                            'up': {'x': 0, 'y': 0, 'z': 1}
                        }
                    }]
                })
                print(f"Added {star_name} to notable stars list (distance: {distance:.1f} ly)")

    print(f"\nTotal notable objects included: {len(notable_stars)}")
    return notable_stars

'''
def create_notable_stars_list(combined_df, unique_notes, user_max_coord=None):
    """
    Create list of notable stars, considering both magnitude/distance limits and manual scaling.
    
    Parameters:
        combined_df: DataFrame containing star data
        unique_notes: Dictionary of notable star descriptions
        user_max_coord: Optional maximum coordinate value for manual scaling
    """
    notable_stars = []
    mode = combined_df.attrs.get('mode', 'distance')
    max_value = combined_df.attrs.get('max_value', 100.0)

    print(f"\nCreating notable stars list:")
    print(f"Mode: {mode}")
    print(f"Max value: {max_value}")
    if user_max_coord is not None:
        print(f"Manual scale: ±{user_max_coord} light-years")

    for star_name in sorted(unique_notes.keys()):
        # Check if it's a Messier object
        is_messier = star_name.startswith('M ') or star_name.startswith('M')

        # Find the star in the combined_df
        if is_messier:
            messier_num = star_name.split()[1] if ' ' in star_name else star_name[1:]
            star_data = combined_df[
                combined_df['Star_Name'].str.contains(f"M{messier_num}", na=False)
            ]
        else:
            star_data = combined_df[combined_df['Star_Name'] == star_name]

        if not star_data.empty:
            star_row = star_data.iloc[0]
            
            # Calculate absolute distance from origin
            x = float(star_row['x'])
            y = float(star_row['y'])
            z = float(star_row['z'])
            distance = np.sqrt(x*x + y*y + z*z)

            # Apply filtering based on mode
            should_include = True
            if mode == 'distance':
                if distance > max_value:
                    print(f"Skipping {star_name} - beyond distance limit ({distance:.1f} > {max_value} ly)")
                    should_include = False
            elif mode == 'magnitude':
                if star_row['Apparent_Magnitude'] > max_value and not is_messier:
                    print(f"Skipping {star_name} - too faint (mag {star_row['Apparent_Magnitude']:.1f} > {max_value})")
                    should_include = False

            # Apply manual scale filtering if specified
            if should_include and user_max_coord is not None:
                if (abs(x) > user_max_coord or 
                    abs(y) > user_max_coord or 
                    abs(z) > user_max_coord):
                    print(f"Skipping {star_name} - beyond manual scale (max coord: {max(abs(x), abs(y), abs(z)):.1f} > {user_max_coord} ly)")
                    should_include = False

            if should_include:
                # Calculate direction unit vector for camera positioning
                direction = {
                    'x': x/distance,
                    'y': y/distance,
                    'z': z/distance
                }
                notable_stars.append({
                    'label': star_name,
                    'method': 'relayout',
                    'args': [{
                        'scene.camera': {
                            'center': {'x': 0, 'y': 0, 'z': 0},
                            'eye': {'x': -0.005 * direction['x'],
                                  'y': -0.005 * direction['y'],
                                  'z': -0.005 * direction['z']},
                            'up': {'x': 0, 'y': 0, 'z': 1}
                        }
                    }]
                })
                print(f"Added {star_name} to notable stars list")

    print(f"\nTotal notable objects included: {len(notable_stars)}")
    return notable_stars
    '''

def create_3d_visualization(combined_df, max_value, user_max_coord=None):
    """
    Create 3D visualization of stellar neighborhood or magnitude-limited stars.
    
    Parameters:
        combined_df (pd.DataFrame): Prepared star data from prepare_3d_data
        max_value (float): Maximum distance or magnitude limit
        user_max_coord (float, optional): User-defined maximum coordinate value for plot axes.
    """
    print("Creating 3D visualization...")

    # Create minimal hover text version
    combined_df['Min_Hover_Text'] = combined_df['Star_Name'].apply(
        lambda name: f'<b>{name}</b>' if name else 'Unknown'
    )
    
    # Calculate axis ranges and determine scale text
    if user_max_coord is not None:
        print(f"Using user-defined scale: ±{user_max_coord} light-years")
        axis_range = [-user_max_coord, user_max_coord]
        scale_text = f" (Scale: ±{user_max_coord} light-years, manual)"
    else:
        # Calculate automatically from data
        max_coord = max(
            abs(combined_df['x'].max()), abs(combined_df['x'].min()),
            abs(combined_df['y'].max()), abs(combined_df['y'].min()),
            abs(combined_df['z'].max()), abs(combined_df['z'].min())
        )
        # Add some padding for better visualization
        max_coord = max_coord * 1.1
        print(f"Using automatic scale: ±{max_coord:.2f} light-years")
        axis_range = [-max_coord, max_coord]
        scale_text = f" (Scale: ±{max_coord:.1f} light-years, auto)"
    
    # Set default analysis results if not present in DataFrame attributes
    analysis = combined_df.attrs.get('analysis', {
        'total_stars': len(combined_df),
        'plottable_hip': len(combined_df[combined_df['Source_Catalog'] == 'Hipparcos']),
        'plottable_gaia': len(combined_df[combined_df['Source_Catalog'] == 'Gaia']),
        'missing_temp': len(combined_df[pd.isna(combined_df['Temperature'])]),
        'missing_lum': len(combined_df[pd.isna(combined_df['Luminosity'])]),
        'temp_le_zero': len(combined_df[
            (~pd.isna(combined_df['Temperature'])) & 
            (combined_df['Temperature'] <= 0)
        ])
    })

    # Set default visualization parameters if not present
    vis_params = combined_df.attrs.get('visualization_params', {
        'temp_min': 1300,
        'temp_max': 50000,
        'mag_min': -1.44,
        'mag_max': 9.0
    })

    mode = combined_df.attrs.get('mode', 'magnitude')
    
    # Define temperature-based colors
    temperature_colors = {
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

    # Create colorscale
    temp_min = vis_params['temp_min']
    temp_max = vis_params['temp_max']
    colorscale = [
        [(temp - temp_min) / (temp_max - temp_min), color]
        for temp, color in sorted(temperature_colors.items())
    ]
    
     # Create figure
    fig = go.Figure()
    
    # Add star trace with fixed hover text handling
    fig.add_trace(go.Scatter3d(
        x=combined_df['x'],
        y=combined_df['y'],
        z=combined_df['z'],
        mode='markers',
        marker=dict(
            size=combined_df['Marker_Size'],
            color=combined_df['Temperature_Normalized'],
            colorscale=colorscale,
            cmin=0,
            cmax=1,
            colorbar=dict(
                title='Temperature (K)',
                tickmode='array',
                tickvals=[
                    (temp - temp_min) / (temp_max - temp_min)
                    for temp in sorted(temperature_colors.keys())
                ],
                ticktext=[f"{temp:,}" for temp in sorted(temperature_colors.keys())],
                tickfont=dict(color='white'),
                titlefont=dict(color='white')
            ),
            showscale=True,
        ),
        text=combined_df['Hover_Text'].values,  # Use .values to avoid indexing issues
        customdata=combined_df['Min_Hover_Text'].values,
        hovertemplate='%{text}<extra></extra>',
        name='Stars',
        showlegend=True
    ))   
    
    # Add Sun with both hover text versions
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers',
        marker=dict(
            size=14,
            symbol='circle',
            color='rgb(102, 187, 106)',  # Chlorophyll green
            line=dict(color='yellow', width=2),
        ),
        text=[hover_text_sun],  # Full hover text
        customdata=['<b>Sun</b>'],  # Minimal hover text
        hovertemplate='%{text}<extra></extra>',
        name='Sun',
        showlegend=True
    ))

    # Add Messier objects with distinct symbols if present
    messier_mask = combined_df['Source_Catalog'] == 'Messier'  # Changed from Is_Messier
    print("\nChecking for Messier objects...")
    if messier_mask.any():
        messier_df = combined_df[messier_mask]
        print(f"Found {len(messier_df)} Messier objects to plot:")
        for _, obj in messier_df.iterrows():
            print(f"  {obj['Star_Name']}: ({obj['x']:.1f}, {obj['y']:.1f}, {obj['z']:.1f}) ly")

    # Add invisible trace just for legend
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],  # No actual points
            mode='markers',
            marker=dict(
                size=30,  # Fixed size for legend
                symbol='circle',
                color='goldenrod',
                opacity=1,               
                line=dict(color='yellow', width=2),
            ),
            name='Messier Objects',
            showlegend=True
        ))

        # Add actual Messier objects trace without legend
        fig.add_trace(go.Scatter3d(
            x=messier_df['x'],
            y=messier_df['y'],
            z=messier_df['z'],
            mode='markers',
            marker=dict(
                size=messier_df['Marker_Size'],
                symbol='circle-open',
                color='white',
                line=dict(color='white', width=5),
                opacity=0.5
            ),
            text=messier_df['Hover_Text'],
            customdata=messier_df['Min_Hover_Text'],
            hovertemplate='%{text}<extra></extra>',
            name='Messier Objects',
            showlegend=False  # Hide from legend since we have the other trace
        ))
    
    # Set title and footer text based on mode
    if mode == 'distance':
        title_text = f'Interactive 3D Visualization of Stars within {int(max_value)} Light-Years{scale_text}'
        footer_text = (
            f"This visualization shows <span style='color:red'>{len(combined_df):,d}</span> stars (of "
            f"<span style='color:red'>{analysis['total_stars']:,d}</span> unique stars detected) within "
            f"<span style='color:red'>{int(max_value)}</span> light-years from the Sun. "
            f"Catalog breakdown of plotted stars: <span style='color:red'>{analysis['plottable_hip']:,d}</span> from "
            f"<a href='https://www.cosmos.esa.int/web/hipparcos/catalogues' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Hipparcos</a> and "
            f"<span style='color:red'>{analysis['plottable_gaia']:,d}</span> from "
            f"<a href='https://www.cosmos.esa.int/gaia' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Gaia</a>. "
            f"Data quality: <span style='color:red'>{analysis['missing_temp']:,d}</span> stars lack temperature data,<br>"
            f"<span style='color:red'>{analysis['missing_lum']:,d}</span> lack luminosity data, and "
            f"<span style='color:red'>{analysis['temp_le_zero']:,d}</span> have invalid temperatures. "
            f"Star properties from <a href='http://simbad.u-strasbg.fr/simbad/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Simbad</a> database. "
            f"Marker size indicates luminosity (1e-6 to 1e3 Lsun), "
            f"color indicates temperature based on black-body radiation (1,300K to 50,000K).<br>"
            f"The Sun is shown in chlorophyll green at the origin (0, 0, 0). "
            f"Python script by Tony Quintanilla with assistance from ChatGPT and Claude, February 2025. "
            f"Search: <a href='https://www.nasa.gov/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>NASA</a>. "
            f"Search: <a href='http://simbad.u-strasbg.fr/simbad/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Simbad</a> "
            f"with the star name, for example: \"* alf Aql\", for star data."
        )

    else:  # magnitude mode
            # Count Messier objects
            messier_count = len(combined_df[combined_df['Source_Catalog'] == 'Messier'])
            
            title_text = f'Interactive 3D Visualization of Unaided-Eye Visible Stars<br>Apparent Magnitude ≤ {max_value}{scale_text}'
            footer_text = (    
                f"This visualization shows <span style='color:red'>{len(combined_df):,d}</span> objects visible to the naked eye "
                f"(apparent magnitude ≤ <span style='color:red'>{max_value}</span>). "
                f"Catalog breakdown of plotted stars: <span style='color:red'>{analysis['plottable_hip']:,d}</span> from "
                f"<a href='https://www.cosmos.esa.int/web/hipparcos/catalogues' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Hipparcos</a> and "
                f"<span style='color:red'>{analysis['plottable_gaia']:,d}</span> from "
                f"<a href='https://www.cosmos.esa.int/gaia' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Gaia</a>. "
                f"<span style='color:red'>{messier_count}</span> Messier objects are also displayed from the "
                f"<a href='http://www.messier.seds.org/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>SEDS Messier Catalog</a>.<br>"
            #    f"Data quality: <span style='color:red'>{analysis['missing_temp']:,d}</span> stars lack temperature data, "
            #    f"<span style='color:red'>{analysis['missing_lum']:,d}</span> lack luminosity data. "
                f"Star properties from <a href='http://simbad.u-strasbg.fr/simbad/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Simbad</a> database. "
                f"Star marker size is inversely proportional to apparent magnitude, where lower apparent magnitudes are brighter. "
                f"Star color indicates temperature based on black-body radiation (scale: 1,300K to 50,000K).<br>"
                f"The Sun is shown in chlorophyll green (source of life's energy!) at the origin of the plot (0, 0, 0). "
                f"The plot coordinates are standardized to the International Celestial Reference System, "
                f"so the Milky Way is tilted approximately 63° with respect to the<br>celestial equator. "
                f"Messier object markers do not reflect object type, apparent magnitude or temperature, but are fixed. " 
                f"Python script by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI, February 2025.<br>"
                f"Search: <a href='https://www.nasa.gov/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>NASA</a>. "
                f"Search: <a href='http://simbad.u-strasbg.fr/simbad/' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Simbad</a> "
                f"with the star name, for example: \"* alf Aql\", for star data."              
            )

    # Update layout with centered axes
    fig.update_layout(
        scene=dict(
            xaxis=dict(title='X (light-years)', range=axis_range, backgroundcolor='black', gridcolor='gray', showbackground=True),
            yaxis=dict(title='Y (light-years)', range=axis_range, backgroundcolor='black', gridcolor='gray', showbackground=True),
            zaxis=dict(title='Z (light-years)', range=axis_range, backgroundcolor='black', gridcolor='gray', showbackground=True),
            aspectmode='cube'
        ),
        paper_bgcolor='black',
        plot_bgcolor='black',
        title=dict(
            text=title_text,
            x=0.5,
            y=0.93,
            xanchor='center',
            yanchor='top',
            font=dict(color='white', size=20)
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="left",
            x=1.06,
            font=dict(color='white'),
            bgcolor='rgba(0,0,0,0.5)'
        ),
        margin=dict(t=90, b=85),
        annotations=[
            dict(
                text="Click on the legend items <br>to toggle them off or back on:",
                xref="paper",
                yref="paper",
                x=0.9,
                y=1.09,
                showarrow=False,
                font=dict(size=12, color='white'),
                align='left',
                xanchor='left',
                yanchor='top'
            ),

            dict(       # target marker 
                x=0.500,
                y=0.505,
                text='<span style="vertical-align:1em;">◇</span>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(size=70, color='rgba(0, 255, 255, 1.0)')  # Semi-transparent blue-green
            ),

        ]
    )
    
    # Add footer annotation
    fig.add_annotation(
        text=footer_text,
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=0.01,
        y=-0.15,
        font=dict(size=10, color='white')
    )

# In visualization_3d.py, replace the notable stars creation block with:

    # Create notable stars list for dropdown menu
    notable_stars = []
    for star_name in sorted(unique_notes.keys()):  # Sort alphabetically
        # Escape special regex characters in star name
        safe_star_name = re.escape(star_name)
        
        # First check if it's a Messier object
        star_data = combined_df[combined_df['Star_Name'].str.contains(safe_star_name, regex=True, na=False)]
        if star_data.empty:
            # Then check for exact matches
            star_data = combined_df[combined_df['Star_Name'] == star_name]
        
        if not star_data.empty:
            # Get the object's coordinates
            x = float(star_data['x'].iloc[0])
            y = float(star_data['y'].iloc[0])
            z = float(star_data['z'].iloc[0])
            
            # Calculate the unit vector pointing to the object
            distance = np.sqrt(x*x + y*y + z*z)
            if distance > 0:  # Avoid division by zero
                direction = {
                    'x': x/distance,
                    'y': y/distance,
                    'z': z/distance
                }
                notable_stars.append({      # this moves the camera to point to the notable star
                    'label': star_name,
                    'method': 'relayout',
                    'args': [{
                        'scene.camera': {
                            'center': {'x': 0, 'y': 0, 'z': 0},
                            'eye': {'x': -0.005 * direction['x'], 
                                  'y': -0.005 * direction['y'], 
                                  'z': -0.005 * direction['z']},
                            'up': {'x': 0, 'y': 0, 'z': 1}
                        }
                    }]
                })

# Get the list of notable stars considering both magnitude and scale limits
    notable_stars = create_notable_stars_list(combined_df, unique_notes, user_max_coord)
    
    # Update layout with buttons and menus
    fig.update_layout(
        updatemenus=[
            # Center button
            dict(
                type="buttons",
                direction="left",
                x=0.05,
                y=1.15,
                buttons=[dict(
                    label="Move Camera to the Sun (Center)",
                    method="relayout",
                    args=[{
                        "scene.camera": {
                            "center": {"x": 0, "y": 0, "z": 0},
                            "eye": {"x": 0, "y": 0.05, "z": 0},       # "y": -0.005 places the camera just in front of the Sun
                            "up": {"x": 0, "y": 0, "z": 1}
                        }
                    }]
                )],
                bgcolor='rgba(255,255,255,0.50)',
                font=dict(color='blue'),
                bordercolor='white',
                borderwidth=1
            ),
            # Notable stars dropdown (only added if there are notable stars)
            dict(
                name="notable_stars",
                type="dropdown",
                direction="down",
                x=0.01,
                y=1.05,
                buttons=notable_stars,
                pad={"r": 10, "t": 10},
                showactive=True,
                bgcolor='rgba(255,255,255,0.50)',
                font=dict(color='blue'),
                bordercolor='white',
                borderwidth=1
            ) if notable_stars else None,
            # Hover text controls
            dict(
                type="buttons",
                direction="right",
                x=0.2,
                y=0.08,
                buttons=[
                    dict(
                        label="Full Star Info",
                        method="update",
                        args=[{"hovertemplate": '%{text}<extra></extra>'}]
                    ),
                    dict(
                        label="Star Names Only",
                        method="update",
                        args=[{"hovertemplate": '%{customdata}<extra></extra>'}]
                    ),
                ],
                font=dict(color='blue'),
                bgcolor='rgba(255,255,255,0.50)',
                bordercolor='white',
                borderwidth=1
            ),
        ]
    )

    default_name = (
        f"3d_stars_magnitude_{max_value}" if combined_df.attrs['mode'] == 'magnitude'
        else f"3d_stars_distance_{max_value}ly"
    )
    save_plot(fig, default_name)    

    # Print debug info about Messier objects
    print("\nChecking for Messier objects...")
    messier_mask = combined_df['Source_Catalog'] == 'Messier'
    if messier_mask.any():
        messier_data = combined_df[messier_mask]
        print(f"Found {len(messier_data)} Messier objects to plot:")
        for _, obj in messier_data.iterrows():
            print(f"  {obj['Star_Name']}: ({obj['x']:.1f}, {obj['y']:.1f}, {obj['z']:.1f}) ly")

    # Return the figure for any further processing
    return fig

# In create_3d_visualization, after creating the figure
    print("\nChecking for Messier objects...")
    messier_mask = combined_df['Source_Catalog'] == 'Messier'
    if messier_mask.any():
        messier_data = combined_df[messier_mask]
        print(f"Found {len(messier_data)} Messier objects to plot:")
        for _, obj in messier_data.iterrows():
            print(f"  {obj['Star_Name']}: ({obj['x']:.1f}, {obj['y']:.1f}, {obj['z']:.1f}) ly")
