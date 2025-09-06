# visualization_2d.py

import numpy as np
import pandas as pd
import re
import plotly.graph_objects as go
from constants_new import (
    object_type_mapping, class_mapping, stellar_class_labels
)
import plotly.graph_objects as go
from visualization_core import (
    format_value, create_hover_text, prepare_temperature_colors, generate_star_count_text
)
from save_utils import save_plot
from star_notes import unique_notes
from visualization_utils import add_hover_toggle_buttons, update_figure_frames, format_hover_text
from solar_visualization_shells import hover_text_sun

def prepare_2d_data(combined_data):
#    """Prepare data specifically for 2D HR diagram plotting."""
    # [Existing prepare_data_for_plotting code]
# def prepare_data_for_plotting(combined_data):
    """Prepare data for plotting."""
    combined_df = combined_data.to_pandas()
    print("\nPreparing data for visualization...")

    # Filter out stars with non-positive temperatures
    combined_df = combined_df[combined_df['Temperature'] > 0].copy()

    print("Parsing stellar classes...")
    def parse_luminosity_class(spectral_type):
        if spectral_type is None or pd.isna(spectral_type):
            return "Unknown"
        match = re.search(r'([IV]+)', str(spectral_type))
        if match:
            luminosity_class = match.group(1)
            return class_mapping.get(luminosity_class, luminosity_class)
        return "Unknown"
    
    combined_df['Stellar_Class'] = combined_df['Spectral_Type'].apply(parse_luminosity_class)

    print("Expanding object type descriptions...")
    def expand_object_type(ot):
        if ot is None:
            return 'Unknown'
        ot_codes = re.split(r'[;, ]+', str(ot))
        descriptions = []
        for code in ot_codes:
            if code in object_type_mapping:
                desc = object_type_mapping[code]
            else:
                matched = False
                for key in object_type_mapping:
                    if key in code:
                        desc = object_type_mapping[key]
                        matched = True
                        break
                if not matched:
                    desc = code
            descriptions.append(desc)
        return ', '.join(descriptions)

    combined_df['Object_Type_Desc'] = combined_df['Object_Type'].apply(expand_object_type)

    # Temperature normalization
    temp_min = 1300
    temp_max = 50000
    combined_df['Temperature_Clipped'] = combined_df['Temperature'].clip(lower=temp_min, upper=temp_max)
    combined_df['Temperature_Normalized'] = (combined_df['Temperature_Clipped'] - temp_min) / (temp_max - temp_min)

    print("Calculating marker sizes...")
    def apparent_magnitude_to_size(app_mag, mag_min=-1.5, mag_max=8.5, size_min=2, size_max=24):
        if app_mag is None or np.isnan(app_mag):
            return size_min
        app_mag_clipped = np.clip(app_mag, mag_min, mag_max)
        log_brightness = -0.4 * app_mag_clipped
        log_brightness_min = -0.4 * mag_max
        log_brightness_max = -0.4 * mag_min
        normalized_brightness = (log_brightness - log_brightness_min) / (log_brightness_max - log_brightness_min)
        size = size_min + (size_max - size_min) * normalized_brightness
        return np.clip(size, size_min, size_max)

    combined_df['Marker_Size'] = combined_df['Apparent_Magnitude'].apply(apparent_magnitude_to_size)

    print("Creating hover texts...")
    hover_texts = []
    minimal_hover_texts = []  # Add this line
    for _, row in combined_df.iterrows():
        hover_text = (
            f'<b>{row["Star_Name"]}</b><br><br>'
            f'{unique_notes.get(row["Star_Name"], "None.")}<br><br>'

            f'Distance: {format(row["Distance_pc"], ".2f") if pd.notna(row["Distance_pc"]) else "Unknown"} pc ({format(row["Distance_ly"], ".2f") if pd.notna(row["Distance_ly"]) else "Unknown"} ly)<br>'

            f'Object Type: {row["Object_Type_Desc"]}<br>'
            f'Stellar Class: {row["Stellar_Class"] if pd.notna(row["Stellar_Class"]) else "Unknown"}<br>'
            f'Temperature: {format(row["Temperature"], ".0f")} K<br>'
            f'Luminosity: {format(row["Luminosity"], ".6f")} Lsun<br>'
            f'Absolute Magnitude: {format(row["Abs_Mag"], ".2f")}<br>'
            f'Apparent Magnitude: {format(row["Apparent_Magnitude"], ".2f")}<br>'
            f'Spectral Type: {row["Spectral_Type"]}<br>'
            f'Source Catalog: {row["Source_Catalog"]}<br>'
            f'Marker Size: {format(row["Marker_Size"], ".2f")} px<br>'
        )
        hover_texts.append(hover_text)

        # Add minimal hover text
        minimal_hover_text = f'<b>{row["Star_Name"]}</b>'
        minimal_hover_texts.append(minimal_hover_text)

    combined_df['Hover_Text'] = hover_texts
    combined_df['Min_Hover_Text'] = minimal_hover_texts  # Add this line
    print("Data preparation complete.")
    return combined_df

# visualization_2d.py

def generate_footer_text(counts_dict, estimation_results=None, mag_limit=None, max_light_years=None):
    """Generate updated footer text including estimation information."""
    # Extract counts
    hip_bright_count = counts_dict.get('hip_bright_count', 0)
    hip_mid_count = counts_dict.get('hip_mid_count', 0)
    gaia_mid_count = counts_dict.get('gaia_mid_count', 0)
    gaia_faint_count = counts_dict.get('gaia_faint_count', 0)
    total_stars = counts_dict.get('total_stars', 0)

    # Get estimation results
    if estimation_results is None:
        estimation_results = counts_dict.get('estimation_results', {})

    recovered_lum = estimation_results.get('recovered_lum', 0)
    recovered_temp = estimation_results.get('recovered_temp', 0)
    initial_missing_lum = estimation_results.get('initial_missing_lum', 0)
    initial_missing_temp = estimation_results.get('initial_missing_temp', 0)
    final_missing_lum = estimation_results.get('final_missing_lum', 0)
    final_missing_temp = estimation_results.get('final_missing_temp', 0)

    if mag_limit is not None:
        footer_text = (
            "     The Hertzsprung-Russell (H-R) diagram is a fundamental tool in astrophysics that graphically represents the "
            "relationship between a star's surface temperature and its luminosity (intrinsic brightness). The H-R diagram illustrates the life "
            "cycles of stars. As stars age, they move to different<br>regions on the diagram, providing insights into their evolutionary stages.<br>"

            f"     We are plotting stars with apparent magnitude (Vmag) ≤ <span style='color:red;'>{mag_limit}</span>. " 
   
            "* Star properties from <a href='https://simbad.u-strasbg.fr/simbad/'>Simbad</a>. "
            "Temperature was estimated using B-V color index, spectral type, or <a href='https://www.cosmos.esa.int/gaia' target='_blank' style='color:#1E90FF; text-decoration:underline;'>Gaia</a> BP-RP color. "
            "Luminosity was estimated using apparent<br>magnitude, distance, and extinction correction. "
            
            "Marker size indicates apparent magnitude (except Sun), temperature (Kelvin) decreases right on x-axis, "
            "and luminosity (Lsun) is on y-axis. "
            "<a href='https://en.wikipedia.org/wiki/Stellar_classification'>Harvard classification</a> "
            "spectral types shown in colored bands. "
            
    #        "<br>-- Python script by Tony Quintanilla, with assistance from ChatGPT and Claude, Updated November 2024."
        )

    elif max_light_years is not None:
        footer_text = (

            "     The Hertzsprung-Russell (H-R) diagram is a fundamental tool in astrophysics that graphically represents the "
            "relationship between a star's surface temperature and its luminosity (intrinsic brightness). The H-R diagram illustrates the life "
            "cycles of stars. As stars age, they move to different<br>regions on the diagram, providing insights into their evolutionary stages.<br>"

            f"     This H-R diagram shows {total_stars:,d} <a href='https://en.wikipedia.org/wiki/List_of_nearest_stars'>stars</a> within "
            f"<span style='background-color: red; color: red'>{int(max_light_years)}</span> light-years of the Sun. "
            "Temperature is plotted on the x-axis (decreasing to the right), "
            "and Luminosity in solar units on the y-axis. "
            "Temperatures are calculated using B-V color indices when available. "
            "The B-V color index provides<br>a quantitative measure of a star's color, which is directly related to its surface temperature. "
            "Otherwise temperature is estimated from spectral types. "
            "Star properties retrieved from the <a href='https://simbad.u-strasbg.fr/simbad/'>Simbad</a> database. "
            "<a href='https://en.wikipedia.org/wiki/Stellar_classification'>Harvard Stellar classification</a> by spectral "
            "types L through B."
    #        "-- Python script by Tony Quintanilla, with assistance from ChatGPT and Claude, November 2024."
        )

    else:
        footer_text = 'No additional information provided.'
        
    return footer_text

def create_hr_diagram(combined_df, counts_dict, mag_limit=None, max_light_years=None):
    """Create HR diagram for either magnitude or distance-based data."""

    """
    Create and display the Hertzsprung-Russell (HR) diagram.

    Parameters:
        combined_df (pandas DataFrame): The data prepared for plotting.
        hover_text_list (list): List of hover text strings for each star.
        mag_limit (float): The upper limit of the apparent magnitude.
        counts_dict (dict): Dictionary containing counts of stars in different categories.

    Returns:
        None
    """
    # Define temperature-based colors
    print("Defining color scales...")

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
    temp_min = 1300
    temp_max = 50000
    colorscale = [
        [(temp - temp_min) / (temp_max - temp_min), color]
        for temp, color in sorted(temperature_colors.items())
    ]

    # Define spectral ranges with temperature bounds and colors
    spectral_ranges = [
        {'type': 'O', 'temp_min': 30000, 'temp_max': 50000, 'color': 'rgba(75, 0, 130, 0.2)'},
        {'type': 'B', 'temp_min': 10000, 'temp_max': 30000, 'color': 'rgba(0, 0, 255, 0.2)'},
        {'type': 'A', 'temp_min': 7500,  'temp_max': 10000, 'color': 'rgba(173, 216, 230, 0.2)'},
        {'type': 'F', 'temp_min': 6000,  'temp_max': 7500,  'color': 'rgba(255, 255, 255, 0.2)'},
        {'type': 'G', 'temp_min': 5200,  'temp_max': 6000,  'color': 'rgba(255, 255, 0, 0.2)'},
        {'type': 'K', 'temp_min': 3700,  'temp_max': 5200,  'color': 'rgba(255, 165, 0, 0.2)'},
        {'type': 'M', 'temp_min': 2400,  'temp_max': 3700,  'color': 'rgba(255, 0, 0, 0.2)'},
        {'type': 'L', 'temp_min': 1300,  'temp_max': 2400,  'color': 'rgba(255, 0, 0, 0.1)'}
    ]

    # Create plot
    print("Creating HR diagram...")

    fig = go.Figure()

    # Plot stars for each catalog separately
    for catalog in ['Hipparcos', 'Gaia']:
        catalog_data = combined_df[combined_df['Source_Catalog'] == catalog]
        
    # Plot stars for each catalog separately
    for catalog in ['Hipparcos', 'Gaia']:
        catalog_data = combined_df[combined_df['Source_Catalog'] == catalog]
        
        fig.add_trace(go.Scatter(
            x=catalog_data['Temperature'],  # Remove log transform here
            y=catalog_data['Luminosity'],
            mode='markers',
            marker=dict(
                size=catalog_data['Marker_Size'],
                color=catalog_data['Temperature_Normalized'],
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
                    ticktext=[f'{temp:,}' for temp in sorted(temperature_colors.keys())],
                    tickfont=dict(color='white'),
                    titlefont=dict(color='white')
                ) if catalog == 'Hipparcos' else None,
                showscale=(catalog == 'Hipparcos'),
            ),
            text=catalog_data['Hover_Text'],
            customdata=catalog_data['Min_Hover_Text'], # Add this line
            hovertemplate='%{text}<extra></extra>',
            name=catalog,
            showlegend=True
        ))

    # Add spectral type annotations
    fig.add_annotation(
        x=0.5,
        y=1.10,
        text='Spectral Type:',
        showarrow=False,
        xref='paper',
        yref='paper',
        xanchor='center',
        yanchor='bottom',
        font=dict(color='white', size=14)
    )

    # Define fixed ranges for axes
    x_range = [np.log10(50000), np.log10(1300)]  # Temperature range
    y_range = [-6, 7]  # Luminosity range from Lsun 0.000001 to 10,000,000

    # Define explicit positions for spectral type labels
    label_positions_paper = {
        'O': 0.08,
        'B': 0.30,
        'A': 0.485,
        'F': 0.555,
        'G': 0.60,
        'K': 0.67,
        'M': 0.77,
        'L': 0.92,
    }

    # Update the spectral type bands
    for s_range in spectral_ranges:
        fig.add_shape(
            type="rect",
            xref='x',
            yref='paper',
            x0=s_range['temp_max'],  # Remove log transform
            x1=s_range['temp_min'],  # Remove log transform
            y0=0,
            y1=1,
            fillcolor=s_range['color'],
            opacity=0.65,
            line_width=0,
            layer='below'
        )

        # Add label using paper coordinates
        x_paper = label_positions_paper[s_range['type']]
        fig.add_annotation(
            x=x_paper,
            y=1.02,
            text=s_range['type'],
            showarrow=False,
            xref='paper',
            yref='paper',
            font=dict(color='white', size=12),
            align='center',
            yanchor='bottom',
            xanchor='center',
        )

# Determine the title based on the provided parameters
    if mag_limit is not None:
        title_text = f'Hertzsprung-Russell Diagram of Unaided-Eye Visible Stars (Apparent Magnitude ≤ {mag_limit})'
    elif max_light_years is not None:
#        title_text = f'Hertzsprung-Russell Diagram of Stars within {int(max_light_years)} Light-Years'
        title_text = f'Hertzsprung-Russell Diagram of Stars within {max_light_years:.1f} Light-Years'        
    else:
        title_text = 'Hertzsprung-Russell Diagram'

    # Update the plot title
    fig.update_layout(
        title=dict(
            text=title_text,
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(color='white', size=20)
        ),

    # Restore the xaxis configuration
    xaxis=dict(
        title='Temperature (K)',
#        autorange='reversed',  # This is key for proper temperature display
        type='log',
        color='white',
#        range=x_range,
        range=[np.log10(50000), np.log10(1300)],  # Explicitly set range
        tickmode='array',
        tickvals=[50000, 30000, 10000, 7500, 6000, 5200, 3700, 2400, 1300],
        ticktext=['50,000', '30,000', '10,000', '7,500', '6,000', '5,200', '3,700', '2,400', '1,300'],
    ),

        yaxis=dict(
            title='Luminosity (Lsun)',
            type='log',
            color='white',
            range=y_range,
        ),
        paper_bgcolor='black',
        plot_bgcolor='black',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.08,
            xanchor='right',
            x=1
        ),
        margin=dict(t=125, b=155),
    )

    # Add the labels (if stellar_class_labels is defined in constants_new)
    for label in stellar_class_labels:
        fig.add_annotation(
            x=label['x'],
            y=label['y'],
            text=label['text'],
            showarrow=False,
            xref='paper',
            yref='y',
            font=label['font'],  # Use the font from the dictionary
            textangle=label.get('rotation', 0),
            align='left'
        )

    # Update Sun position
    sun_minimal_hover_text = '<b>Sun</b>'  # Create minimal hover text for the Sun
    fig.add_trace(go.Scatter(
        x=[5778],  # Remove log transform
        y=[1],
        mode='markers',
        marker=dict(
            size=14,
            symbol='circle',
            color='rgb(102, 187, 106)',
            line=dict(color='white', width=1),
        ),
        text=[hover_text_sun],
        customdata=[sun_minimal_hover_text],  # Add customdata for the Sun
        hovertemplate='%{text}<extra></extra>',
        name='Sun',
        showlegend=True,
    ))

    # Prepare footer text using counts_dict
    print("Preparing footer text...")

    # Extract counts from counts_dict
    hip_bright_count = counts_dict.get('hip_bright_count', 0)
    hip_mid_count = counts_dict.get('hip_mid_count', 0)
    gaia_mid_count = counts_dict.get('gaia_mid_count', 0)
    gaia_faint_count = counts_dict.get('gaia_faint_count', 0)
    total_stars = hip_bright_count + hip_mid_count + gaia_mid_count + gaia_faint_count

    # Compute plottable and missing stars
    plottable_mask = ~np.isnan(combined_df['Temperature']) & ~np.isnan(combined_df['Luminosity'])
    plottable_count = plottable_mask.sum()
    missing_stars = total_stars - plottable_count

    # Additional counts from counts_dict
    source_counts = counts_dict.get('source_counts', {
        'bv_matched': 0,
        'bv_only': 0,
        'spectral_type_hot': 0,
        'spectral_type_cool': 0,
        'spectral_type_only': 0,
        'spectral_type_disagreement': 0,
        'none': 0
    })

    missing_temp_only = source_counts['none']
    missing_lum_only = missing_stars - missing_temp_only  # Simplified for this context
    missing_both = 0  # Adjust according to your data

    # Generate the star count text
    star_count_text = generate_star_count_text(counts_dict, combined_df)

    footer_text = generate_footer_text(
        counts_dict,
        estimation_results=counts_dict.get('estimation_results'),
        mag_limit=mag_limit,
        max_light_years=max_light_years
    )

    # Combine both texts
    full_footer_text = footer_text + star_count_text

    # Add footer annotation
    fig.add_annotation(
        text=full_footer_text,
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=-0.05,
        y=-0.15,
        xanchor='left',
        yanchor='top',
        font=dict(size=10, color='white')
    )

    # Instead of just showing the plot, offer save options
    default_name = (
        f"hr_diagram_magnitude_{mag_limit}" if mag_limit is not None
        else f"hr_diagram_distance_{max_light_years}ly"
    )

# Add hover toggle buttons
    fig = add_hover_toggle_buttons(fig)

    # Save and offer save options
    default_name = (
        f"hr_diagram_magnitude_{mag_limit}" if mag_limit is not None
        else f"hr_diagram_distance_{max_light_years}ly"
    )
    save_plot(fig, default_name)
    
    # Render the plot
    print("Rendering plot...")
    fig.show()

