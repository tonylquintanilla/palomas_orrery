"""
Dual-Scale Paleoclimate Visualization for Paloma's Orrery
Side-by-side layout: Deep Time (log scale) + Modern Era (linear scale)

This approach gives proper visual space to both geological history and 
modern/future climate projections, with the ability to draw connections
between the two timescales.

Data Preservation is Climate Action
"""

import json
import os
import numpy as np
from save_utils import save_plot
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Import data loading functions from main module
import sys
sys.path.insert(0, '/mnt/project')
from paleoclimate_visualization import (
    load_lr04_data,
    load_holocene_data, 
    load_modern_temperature_data,
    calculate_preindustrial_offset,
    d18o_to_temperature_approx,
#    GEOLOGIC_PERIODS
)

# Geologic time periods - expanded to full Earth history
GEOLOGIC_PERIODS = [
    # Precambrian (4.5 Ga - 541 Ma)
    {'name': 'Hadean', 'start': 4500, 'end': 4000, 'color': '#8B4789'},
    {'name': 'Archean', 'start': 4000, 'end': 2500, 'color': '#F0619D'},
    {'name': 'Proterozoic', 'start': 2500, 'end': 541, 'color': '#FE9D6F'},
    
    # Paleozoic (541 - 252 Ma)
    {'name': 'Cambrian', 'start': 541, 'end': 485.4, 'color': '#7FA056'},
    {'name': 'Ordovician', 'start': 485.4, 'end': 443.8, 'color': '#009270'},
    {'name': 'Silurian', 'start': 443.8, 'end': 419.2, 'color': '#B3E1B6'},
    {'name': 'Devonian', 'start': 419.2, 'end': 358.9, 'color': '#CB8C37'},
    {'name': 'Carboniferous', 'start': 358.9, 'end': 298.9, 'color': '#67A599'},
    {'name': 'Permian', 'start': 298.9, 'end': 252.2, 'color': '#F04028'},
    
    # Mesozoic (252 - 66 Ma)
    {'name': 'Triassic', 'start': 252.2, 'end': 201.3, 'color': '#812B92'},
    {'name': 'Jurassic', 'start': 201.3, 'end': 145.0, 'color': '#34B2C9'},
    {'name': 'Cretaceous', 'start': 145.0, 'end': 66.0, 'color': '#7FC64E'},
    
    # Cenozoic (66 Ma - present)
    {'name': 'Paleocene', 'start': 66.0, 'end': 56.0, 'color': '#FD9A52'},
    {'name': 'Eocene', 'start': 56.0, 'end': 33.9, 'color': '#FDB462'},
    {'name': 'Oligocene', 'start': 33.9, 'end': 23.03, 'color': '#FED7AA'},
    {'name': 'Miocene', 'start': 23.03, 'end': 5.333, 'color': '#FFFF99'},
    {'name': 'Pliocene', 'start': 5.333, 'end': 2.58, 'color': '#FFFFCC'},
    {'name': 'Pleistocene', 'start': 2.58, 'end': 0.0117, 'color': '#C6F7FF'},
#    {'name': 'Holocene', 'start': 0.0117, 'end': 0.000145, 'color': '#59DEDE'}
]

def load_modern_temperature_data_ma_bp():
    """
    Load modern instrumental temperature data using Ma BP (Before Present = 2025)
    
    This is a wrapper that converts the Ma B2100 data from the main module
    to Ma BP for consistency with the paleoclimate data in the dual-scale viz.
    """
    try:
        import json
        import os
        
        # Try multiple possible locations for the temperature file
    #    possible_paths = [
    #        'temperature_giss_monthly.json',  # Same directory
    #        os.path.join(os.path.dirname(__file__), 'temperature_giss_monthly.json'),  # Script directory
    #        '/mnt/project/temperature_giss_monthly.json'  # Fallback for testing
    #    ]
        
        # Try multiple possible locations for the temperature file
        possible_paths = [
            'data/temperature_giss_monthly.json',  # Data subdirectory (primary location)
            os.path.join(os.path.dirname(__file__), 'data/temperature_giss_monthly.json'),  # Script dir + data/
            'temperature_giss_monthly.json',  # Legacy root location (backwards compatibility)
            os.path.join(os.path.dirname(__file__), 'temperature_giss_monthly.json'),
            '/mnt/project/temperature_giss_monthly.json'  # Fallback for testing
        ]

        data = None
        for path in possible_paths:
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                break
            except FileNotFoundError:
                continue
        
        if data is None:
            print("Warning: Could not find temperature_giss_monthly.json")
            return None, None
        
        records = data['data']
        
        # Convert to arrays and get annual averages
        years = []
        temps = []
        
        for record in records:
            year = record['year']
            
            if year not in years:
                years.append(year)
                # Get all months for this year that have valid data
                year_temps = [r['anomaly_c'] for r in records 
                             if r['year'] == year and r['anomaly_c'] is not None]
                if year_temps:
                    temps.append(np.mean(year_temps))
                else:
                    # Skip years with no valid data
                    years.pop()
        
        # Convert years to Ma BP (millions of years before present = 2025)
        # Present = 2025, so years before present = 2025 - year
        current_year = 2025
        ages_ma = [(current_year - y) / 1_000_000 for y in years]
        
        return ages_ma, temps
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Warning: Could not load modern temperature data: {e}")
        return None, None


def load_projection_scenarios():
    """
    Load future climate projection scenarios
    
    SSP scenarios based on:
    IPCC AR6 Working Group I, Chapter 4, Table 4.2 - Global mean surface air 
    temperature anomalies (°C) relative to 1850-1900 baseline.
    
    Data source: Lee, J.-Y., J. Marotzke, et al. (2021): Future Global Climate: 
    Scenario-based Projections and Near-term Information. In Climate Change 2021: 
    The Physical Science Basis. Contribution of Working Group I to the Sixth 
    Assessment Report of the Intergovernmental Panel on Climate Change.
    
    Shared Socioeconomic Pathways (SSPs) represent different future climate 
    scenarios based on varying levels of greenhouse gas emissions and mitigation 
    efforts.
    
    Returns:
        list of dicts: Each dict contains 'name', 'years', 'temps', 'color', 'dash', 'width', 'description'
    """
    
    # IPCC AR6 Table 4.2 data points (Global, relative to 1850-1900)
    # Three key periods: 2021-2040, 2041-2060, 2081-2100
    
    # Use period END points for plotting (more accurate representation)
    ipcc_years = [2040, 2060, 2100]  # End years of the three IPCC periods
    
    scenarios = [
        {
            'name': 'SSP1-1.9 (IPCC AR6 WG1)',
            'ipcc_temps': [1.5, 1.7, 1.5],  # IPCC Table 4.2 values
            'color': '#1976D2',  # Blue - most ambitious
            'dash': 'solid',
            'width': 2.5,
            'description': '1.9 W/m2: Very low emissions, net-zero by 2050, limit to 1.5C',
            'ssp_label': 'SSP1-1.9 (1.9 W/m2)'
        },
        {
            'name': 'SSP1-2.6 (IPCC AR6 WG1)',
            'ipcc_temps': [1.6, 1.9, 2.0],  # IPCC Table 4.2 values
            'color': '#4CAF50',  # Green - Paris Agreement target
            'dash': 'solid',
            'width': 2.5,
            'description': '2.6 W/m2: Low emissions, Paris Agreement, well below 2C',
            'ssp_label': 'SSP1-2.6 (2.6 W/m2)'
        },
        {
            'name': 'SSP2-4.5 (IPCC AR6 WG1)',
            'ipcc_temps': [1.6, 2.1, 2.9],  # IPCC Table 4.2 values
            'color': '#FFA726',  # Orange - intermediate
            'dash': 'solid',
            'width': 2.5,
            'description': '4.5 W/m2: Intermediate emissions, middle-of-the-road',
            'ssp_label': 'SSP2-4.5 (4.5 W/m2)'
        },
        {
            'name': 'SSP3-7.0 (IPCC AR6 WG1)',
            'ipcc_temps': [1.6, 2.3, 3.9],  # IPCC Table 4.2 values
            'color': '#EF5350',  # Red-orange - high emissions
            'dash': 'solid',
            'width': 2.5,
            'description': '7.0 W/m2: High emissions, regional rivalry, continued warming',
            'ssp_label': 'SSP3-7.0 (7.0 W/m2)'
        },
        {
            'name': 'SSP5-8.5 (IPCC AR6 WG1)',
            'ipcc_temps': [1.7, 2.6, 4.8],  # IPCC Table 4.2 values
            'color': '#B71C1C',  # Dark red - fossil fuel intensive
            'dash': 'solid',
            'width': 2.5,
            'description': '8.5 W/m2: Very high emissions, fossil-fuel intensive development',
            'ssp_label': 'SSP5-8.5 (8.5 W/m2)'
        }
    ]
    
    # Interpolate to create smooth curves from current (2025) through the IPCC periods
    import numpy as np
    
    for scenario in scenarios:
        # Start from current conditions (approximately 1.2°C in 2025)
        # Then use IPCC values at period endpoints: 2040, 2060, 2100
        extended_years = [2025] + ipcc_years
        extended_temps = [1.2] + scenario['ipcc_temps']
        
        # Create smooth interpolation - stop at 2100 (no flattening beyond)
        years_fine = np.linspace(2025, 2100, 50)
        temps_fine = np.interp(years_fine, extended_years, extended_temps)
        
        scenario['years'] = years_fine.tolist()
        scenario['temps'] = temps_fine.tolist()
        
        # Remove the raw IPCC temps (no longer needed)
        del scenario['ipcc_temps']
    
    return scenarios


def load_cat_policies_and_action():
    """
    Load Climate Action Tracker "Policies and Action" temperature range
    
    Data source: Climate Action Tracker (2024). "Global Temperature Estimates - COP29". 
    Published November 13, 2024. https://climateactiontracker.org/global/temperatures/
    
    This represents the projected warming based on currently implemented policies and actions,
    showing the high and low estimates for this scenario.
    
    Returns:
        dict: Contains 'years', 'high', 'low' arrays for the temperature range
    """
    # CAT Policies and Action data from November 2024 update
    # Temperature projections relative to pre-industrial (approximated as 1850-1900)
    cat_data = {
        'years': [2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100],
        'high': [1.47, 1.72, 1.94, 2.14, 2.34, 2.54, 2.73, 2.90],  # Rounded for display
        'low': [1.47, 1.69, 1.88, 2.03, 2.17, 2.31, 2.42, 2.52],   # Rounded for display
    }
    
    return cat_data


def create_paleoclimate_dual_scale_visualization():
    """
    Create dual-scale paleoclimate visualization with side-by-side layout
    
    LEFT PLOT (70% width): Deep time with logarithmic scale (4.5 Ga to 1850 CE)
    RIGHT PLOT (30% width): Modern era with linear scale (1850 CE to 2100 CE)
    
    Both plots share the same y-axis (temperature anomaly) allowing for
    visual connections and cross-plot annotations.
    """
    
    if not PLOTLY_AVAILABLE:
        print("Error: Plotly not available")
        return None
    
    # Load all data
    lr04_data = load_lr04_data()
    if not lr04_data:
        print("Error: Could not load LR04 data")
        return None
    
    holocene_data = load_holocene_data()
    modern_ages_ma, modern_temps = load_modern_temperature_data_ma_bp()  # Use Ma BP version
    
    # Debug: Check if GISS data loaded
    if modern_ages_ma is None or modern_temps is None:
        print("WARNING: GISS data did not load!")
    else:
        modern_years = [2025 - (age * 1_000_000) for age in modern_ages_ma]
        print(f"GISS data loaded: {len(modern_ages_ma)} points from {min(modern_years):.0f} to {max(modern_years):.0f}")
    
    preindustrial_offset = calculate_preindustrial_offset(holocene_data) if holocene_data else 0.0
    
    # Process LR04 paleoclimate data
    records = lr04_data['data']
    ages_ka = np.array([r['age_ka_bp'] for r in records])
    d18o_values = np.array([r['d18o_permil'] for r in records])
    ages_ma = ages_ka / 1000.0
    temp_anomaly = d18o_to_temperature_approx(d18o_values)
    temp_anomaly = temp_anomaly - preindustrial_offset
    
    # DECISION: Define the transition point (where log becomes linear)
    TRANSITION_YEAR = 1850  # CE
    TRANSITION_MA = 0.00025  # Ma BP (250 years before 2025)
    
    # Create side-by-side subplots
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.68, 0.32],  # 68% deep time, 32% modern
        horizontal_spacing=0.02,      # Small gap for visual separation
        subplot_titles=(
            "Deep Time: Earth's Climate History",
            "Modern Era & Projections"
        ),
        specs=[[{"type": "scatter"}, {"type": "scatter"}]]
    )
    
    # ============================================================
    # LEFT PLOT: DEEP TIME (Logarithmic scale, 4.5 Ga to 1850 CE)
    # ============================================================
    
    # Filter paleoclimate data to end at 1850 CE
    deep_time_mask = ages_ma >= TRANSITION_MA
    deep_time_ages = ages_ma[deep_time_mask]
    deep_time_temps = temp_anomaly[deep_time_mask]
    
    # Add paleoclimate trace to left plot
    fig.add_trace(
        go.Scatter(
            x=deep_time_ages,
            y=deep_time_temps,
            mode='lines',
            name='Paleoclimate (LR04)',
            line=dict(color='#2E86AB', width=1.5),
            hovertemplate='<b>%{x:.3f} Ma</b><br>Temp: %{y:.2f}°C<extra></extra>',
            showlegend=True
        ),
        row=1, col=1
    )
    
    # Add Holocene data to left plot if available
    if holocene_data:
        holocene_ages = np.array(holocene_data['ages_ma'])
        holocene_temps = np.array(holocene_data['temp_median']) - preindustrial_offset
        
        # Filter to show only pre-1850 Holocene data in left plot
        holocene_deep_mask = holocene_ages >= TRANSITION_MA
        
        fig.add_trace(
            go.Scatter(
                x=holocene_ages[holocene_deep_mask],
                y=holocene_temps[holocene_deep_mask],
                mode='lines',
                name='Holocene (Kaufman 2020)',
                line=dict(color='#A06CD5', width=2),
                hovertemplate='<b>%{x:.6f} Ma</b><br>Temp: %{y:.2f}°C<extra></extra>',
                showlegend=True
            ),
            row=1, col=1
        )
    
    # Add geologic period shading to left plot
    for period in GEOLOGIC_PERIODS:
        if period['start'] >= TRANSITION_MA:  # Only show periods in deep time
            fig.add_vrect(
                x0=period['start'],
                x1=max(period['end'], TRANSITION_MA),  # Stop at transition
                fillcolor=period['color'],
                opacity=0.15,
                layer="below",
                line_width=0,
                row=1, col=1
            )
    
    # Configure left plot x-axis (logarithmic)
    fig.update_xaxes(
        title_text="Millions of Years Before Present",
        type="log",
        autorange=False,
        range=[np.log10(4500), np.log10(0.000001)],  # Extended to present (near-zero on log scale)
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        row=1, col=1
    )
    
    # Add GISS instrumental data to left plot (extends to present)
    # This helps users see the equivalence between the two plots
    if modern_ages_ma is not None and modern_temps is not None:
        fig.add_trace(
            go.Scatter(
                x=modern_ages_ma,
                y=modern_temps,
                mode='lines',
                name='Instrumental (NASA GISS)',
                line=dict(color='#D32F2F', width=2.5),
                hovertemplate='<b>%{x:.9f} Ma</b><br>Temp: %{y:.2f}°C<extra></extra>',
                showlegend=True
            ),
            row=1, col=1
        )

    
    # ============================================================
    # RIGHT PLOT: MODERN ERA (Linear scale, 1850 CE to 2100 CE)
    # ============================================================
    
    # Convert modern data from Ma to calendar years
    if modern_ages_ma is not None and modern_temps is not None:
        # Filter modern data (post-1850)
        modern_mask = np.array(modern_ages_ma) < TRANSITION_MA
        modern_years = [2025 - (age * 1_000_000) for age in np.array(modern_ages_ma)[modern_mask]]
        modern_temps_filtered = np.array(modern_temps)[modern_mask]
        
        # Adjust modern temps to match our baseline
        modern_temps_adjusted = modern_temps_filtered
        
        print(f"Adding GISS to RIGHT plot: {len(modern_years)} points from {min(modern_years):.0f} to {max(modern_years):.0f}")
        
        fig.add_trace(
            go.Scatter(
                x=modern_years,
                y=modern_temps_adjusted,
                mode='lines',
                name='Instrumental (NASA GISS)',
                line=dict(color='#D32F2F', width=2.5),
                hovertemplate='<b>Year %{x}</b><br>Temp: %{y:.2f}°C<extra></extra>',
                showlegend=False  # Hide from legend (already shown in left plot)
            ),
            row=1, col=2
        )
    
    """
    # Add Holocene data to right plot (post-1850)
    if holocene_data:
        holocene_modern_mask = holocene_ages < TRANSITION_MA
        holocene_modern_years = [2025 - (age * 1_000_000) for age in holocene_ages[holocene_modern_mask]]
        holocene_modern_temps = holocene_temps[holocene_modern_mask]
        
        fig.add_trace(
            go.Scatter(
                x=holocene_modern_years,
                y=holocene_modern_temps,
                mode='lines',
                name='Holocene (Kaufman 2020)',  # Same name as left plot
                line=dict(color='#A06CD5', width=2),
                hovertemplate='<b>Year %{x}</b><br>Temp: %{y:.2f}°C<extra></extra>',
                showlegend=False  # Hide from legend (already shown in left plot)
            ),
            row=1, col=2
        )
    """
    
    # Configure right plot x-axis (linear)
    fig.update_xaxes(
        title_text="Year (CE)",
        type="linear",
        autorange=False,
        range=[1850, 2100],
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        row=1, col=2
    )
    
    # ============================================================
    # ADD PROJECTION SCENARIOS TO RIGHT PLOT
    # ============================================================
    
    projection_scenarios = load_projection_scenarios()
    
    # Plot all SSP scenario lines (clean IPCC AR6 Table 4.2 data)
    for scenario in projection_scenarios:
        fig.add_trace(
            go.Scatter(
                x=scenario['years'],
                y=scenario['temps'],
                mode='lines+markers',
                name=scenario['name'],
                line=dict(
                    color=scenario['color'],
                    width=scenario['width'],
                    dash=scenario['dash']
                ),
                marker=dict(size=6, symbol='circle'),
                hovertemplate=(
                    f"<b>{scenario['ssp_label']}</b><br>" +
                    "Year: %{x}<br>" +
                    "Temp: %{y:.2f}C<br>" +
                    f"{scenario['description']}<extra></extra>"
                ),
                showlegend=True
            ),
            row=1, col=2
        )

    
    # ============================================================
    # ADD CAT "POLICIES AND ACTION" RANGE
    # ============================================================
    
#    cat_data = load_cat_policies_and_action()
    
    # Add upper boundary (high estimate) - invisible line
#    fig.add_trace(
#        go.Scatter(
#            x=cat_data['years'],
#            y=cat_data['high'],
#            mode='lines',
#            line=dict(width=0),
#            showlegend=False,
#            hoverinfo='skip'
#        ),
#        row=1, col=2
#    )
    
    # Add lower boundary (low estimate) with fill to create shaded band
#    fig.add_trace(
#        go.Scatter(
#            x=cat_data['years'],
#            y=cat_data['low'],
#            mode='lines',
#            name='Policies & Action (CAT)',
#            line=dict(width=0),
#            fill='tonexty',  # Fill to previous trace (the high estimate)
#            fillcolor='rgba(128, 128, 128, 0.25)',  # Semi-transparent gray
#            hovertemplate=(
#                "<b>Policies & Action (CAT)</b><br>" +
#                "Year: %{x}<br>" +
#                "Range: Current policies already implemented<br>" +
#                "Climate Action Tracker (Nov 2024)<extra></extra>"
#            ),
#            showlegend=True
#        ),
#        row=1, col=2
#    )

    
    # ============================================================
    # SHARED Y-AXIS CONFIGURATION
    # ============================================================
    
    # Both plots use same y-axis for temperature
    fig.update_yaxes(
        title_text="Temperature Anomaly (°C, relative to 1850-1900)",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        row=1, col=1
    )
        
    # ============================================================
    # CROSS-PLOT ANNOTATIONS AND CONNECTIONS
    # ============================================================
    
    # Calculate where the boundary is in paper coordinates
    # Left plot goes from x=0 to x=0.68, right plot from x=0.70 to x=1.0
    boundary_x = 0.67  # Position of the transition line as the baseline
    
    # Vertical line at 1850 CE boundary (spans both plots)
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=boundary_x,
        y0=0.12,  # Just above x-axis
        x1=boundary_x,
        y1=0.75,  # Just below title
        line=dict(
    #        color="rgba(0, 150, 0, 0.4)",
            color="rgba(0, 0, 0, 1.0)",
            width=1,
            dash="dash"
        )
    )
        
    # Add baseline threshold line for left graph
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.20,
        y0=0.0,
        x1=0.67,
        y1=0.0,
        line=dict(
            color="black",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.57,
        y=-0.50,
        text="Baseline (1850-1900)",
        showarrow=False,
        bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add baseline threshold line for right graph
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.67,
        y0=-7.40,
        x1=1.00,
        y1=-7.40,
        line=dict(
            color="black",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.70,
        y=-7.30,
        text="Baseline (1850-1900)",
        showarrow=False,
        bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 3.3°C peak 90% chance - left plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.20,
        y0=3.3,
        x1=0.67,
        y1=3.3,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )
    
    # Add 2.8°C peak 66% chance - left plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.20,
        y0=2.8,
        x1=0.67,
        y1=2.8,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )

    # Add 2.6°C peak 50% chance - left plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.2,
        y0=2.6,
        x1=0.67,
        y1=2.6,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )    

    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.25,
        y=2.85,
        text="Current policies continuing: peak warming over the 21st century, 2.6°C (50%), 2.8°C (66%), 3.3°C (90%)",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 1.28°C today - left plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.20,
        y0=1.28,
        x1=0.67,
        y1=1.28,
        line=dict(
            color="green",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.50,
        y=0.90,
        text="1.28°C Current Anomaly",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='green'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 1.28°C today - right plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-4.75,
        x1=1.00,
        y1=-4.75,
        line=dict(
            color="green",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=-5.20,
        text="1.28°C Current Anomaly",
        showarrow=False,
        bgcolor="rgba(255,255,255,0.8)",
        font=dict(size=9, color='green'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 1.5°C threshold line (Paris Agreement) - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-4.35,
        x1=1.00,
        y1=-4.35,
        line=dict(
            color="orange",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=-4.30,
        text="1.5°C Target",
        showarrow=False,
        bgcolor="rgba(255,255,255,0.8)",
        font=dict(size=9, color='orange'),
        xanchor='left',
        yanchor='bottom'
    )
    
    # Add 2°C threshold line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-3.30,
        x1=1.00,
        y1=-3.30,
        line=dict(
            color="red",
            width=2,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=-3.25,
        text="2°C Limit",
        showarrow=False,
        bgcolor="rgba(255,255,255,0.8)",
        font=dict(size=9, color='red'),
        xanchor='left',
        yanchor='bottom'
    )
    
    # Add 3.3°C trajectory line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-0.50,
        x1=1.00,
        y1=-0.50,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )

    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.88,
        y=-0.50,
        text="Peak: 3.3°C (90%)",
        showarrow=False,
        bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 2.8°C trajectory line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-1.50,
        x1=1.00,
        y1=-1.50,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.88,
        y=-1.50,
        text="Peak: 2.8°C (66%)",
        showarrow=False,
        bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 2.6°C trajectory line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.68,
        y0=-1.90,
        x1=1.00,
        y1=-1.90,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )

    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.88,
        y=-1.90,
        text="Peak: 2.6°C (50%)",
        showarrow=False,
        bgcolor="rgba(0,0,0,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add annotation for Holocene stability
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.45,
        y=1.0,
        text="Holocene<br>Stable Climate<br>(12,000 years)",
        showarrow=False,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#A06CD5',
        ax=0,
        ay=-40,
        font=dict(size=9, color='#A06CD5'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#A06CD5',
        borderwidth=1
    )
    
    # Add arrow connecting Holocene stability to modern rapid change
    fig.add_annotation(
        xref="paper",
        yref="paper",
        x=0.60,
        y=0.90,
        ax=0.75,
        ay=0.55,
        text="Rapid departure<br>from stability",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='#D32F2F',
        font=dict(size=9, color='#D32F2F'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#D32F2F',
        borderwidth=1
    )
    
    # Add vertical line at 2050 in right plot (net-zero target year)
    fig.add_vline(
        x=2050,
        line_width=2,
        line_dash="dash",
        line_color="rgba(100,100,100,0.4)",
        row=1, col=2
    )
    
    fig.add_annotation(
        xref="x2",  # Right plot x-axis
        yref="paper",
        x=2050,
        y=0.92,
        text="2050<br>Net-Zero<br>Target",
        showarrow=False,
        font=dict(size=8, color='#666'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#999',
        borderwidth=1,
        xanchor='center',
        yanchor='bottom'
    )


    
    # ============================================================
    # LAYOUT AND STYLING
    # ============================================================
    
    fig.update_layout(
        title={
            'text': "Earth's Climate: Deep Time to Future<br><sub>Dual-Scale View: Geological Context + Modern Projections</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        hovermode='closest',
        showlegend=True,
        legend=dict(
            x=0.01,
            y=0.99,
            xanchor='left',
            yanchor='top',
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#333',
            borderwidth=1
        ),
        plot_bgcolor='white',
        height=600,
        margin=dict(t=100, b=80, l=80, r=40)
    )
    
    # Add info box explaining the dual-scale approach
    info_text = (
        "<b>Dual-Scale Visualization</b><br>"
        "<br>"
        "<b>Left:</b> 4.5 billion years (log scale)<br>"
        "<b>Right:</b> 1850-2100 CE (linear scale)<br>"
        "<br>"
        "Same temperature axis enables<br>"
        "direct visual comparison across<br>"
        "geological and human timescales"
    )
    
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.02, y=0.38,
        xanchor="left", yanchor="top",
        bgcolor="rgba(255,255,255,0.95)",
        bordercolor="#2E86AB",
        borderwidth=2,
        borderpad=8,
        showarrow=False,
        font=dict(size=9),
        align="left"
    )
    
    
    # Add SSP explanation box
    ssp_text = (
        "<b>Shared Socioeconomic Pathways (SSP)</b><br>"
        "<b>Source</b>: IPCC AR6<br>"
        "<b>Numbers:</b> Radiative forcing (W/m2) by 2100<br>"
        "<b>Data periods:</b> 2021-2040, 2041-2060, 2081-2100<br>"
        "<b>Plot points:</b> Period endpoints (2040, 2060, 2100)<br>"
        "<b>Lines:</b> Smooth interpolations between endpoints<br>"
        "<br>"
        "<b>Peak Warming:</b> UNEP 2025 Emissions Gap Report<br>"
        "Shows the range with current policies continuing"
    )
    
    fig.add_annotation(
        text=ssp_text,
        xref="paper", yref="paper",
        x=0.87, y=0.99,
        xanchor="right", yanchor="top",
        bgcolor="rgba(255,255,255,0.95)",
        bordercolor="#2E86AB",
        borderwidth=2,
        borderpad=8,
        showarrow=False,
        font=dict(size=9),
        align="left"
    )
    
    # Citation
    fig.add_annotation(
        text=(
            "<b>Data Sources:</b><br>" +
            "Paleoclimate: Lisiecki, L.E.; Raymo, M.E. (2005): NOAA/WDS Paleoclimatology - Pliocene-Pleistocene Benthic Stack | "
            "Holocene: Kaufman, D.S.; McKay, N.P.; Routson, C. (2020): NOAA/WDS Paleoclimatology - Temperature 12k Database | " 
            "Instrumental: NASA Goddard Institute for Space Studies |<br>"
            "Future Projections: IPCC AR6 WG1, Table 4.2 - Lee, J.-Y., J. Marotzke, et al. (2021): Climate Change 2021: The Physical Science Basis | "
            "Peak warming over the 21st century, Figure 4.2, Emissions Gap Report 2025, UNEP | "
            "Visualization: Paloma's Orrery"
        ),
     
        xref="paper", yref="paper",
        x=0.5, y=-0.10,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='#666')
    )
    
    return fig


def main():
    """Test the dual-scale visualization"""
    if not PLOTLY_AVAILABLE:
        print("Error: Plotly not available")
        return
    
    print("Creating dual-scale paleoclimate visualization...")
    fig = create_paleoclimate_dual_scale_visualization()
    
    if fig:
        print("✓ Visualization created successfully")
        # Offer to save
        save_plot(fig, "paleoclimate_dual_scale")
        print("Opening in browser...")
        fig.show()
    else:
        print("✗ Could not create visualization - check if data is cached")

if __name__ == '__main__':
    main()
