"""
Paleoclimate Visualization for Paloma's Orrery
Cenozoic temperature and CO₂ reconstruction (66 Ma - present)

Shows the "big picture" of Earth's climate history with Plotly's zoom capability
to explore details from ice ages down to the remarkable stability of the Holocene.

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

# Data files
# PALEO_DATA_DIR = 'paleoclimate_data'
PALEO_DATA_DIR = 'data'
LR04_CACHE = os.path.join(PALEO_DATA_DIR, 'lr04_benthic_stack.json')


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
    {'name': 'Holocene', 'start': 0.0117, 'end': 0.000001, 'color': '#59DEDE'}
]

def d18o_to_temperature_approx(d18o_values):
    """
    Convert benthic δ18O to approximate temperature anomaly
    
    This is a simplified conversion. Benthic δ18O reflects both 
    ice volume and deep ocean temperature. The relationship varies
    over time, but rough approximation:
    - Higher δ18O = More ice + Colder temperatures
    - Lower δ18O = Less ice + Warmer temperatures
    
    Using simplified conversion: ~4-5°C per 1‰ change
    Normalized to show relative changes from present
    """
    # Modern benthic δ18O is around 3.2‰
    modern_d18o = 3.23  # From LR04 data at 0 ka
    
    # Convert to temperature anomaly (inverted because higher δ18O = colder)
    # Using ~4.5°C per 1‰ as approximation
    temp_anomaly = -(np.array(d18o_values) - modern_d18o) * 4.5
    
    return temp_anomaly

def load_lr04_data():
    """Load LR04 benthic stack from cache"""
    try:
        with open(LR04_CACHE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def load_holocene_data():
    """Load Kaufman et al. (2020) Holocene temperature reconstruction"""
    holocene_file = os.path.join(PALEO_DATA_DIR, 'temp12k_allmethods_percentiles.csv')
    
    try:

        import csv
        ages_years = []
        temps_median = []
        temps_5th = []
        temps_95th = []
        
        with open(holocene_file, 'r') as f:
            reader = csv.DictReader(f)
            # Strip whitespace from fieldnames
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                ages_years.append(float(row['ages']))
                temps_median.append(float(row['global_median']))
                temps_5th.append(float(row['global_5']))
                temps_95th.append(float(row['global_95']))
        
        # Convert years BP to Ma BP
        ages_ma = [age / 1_000_000 for age in ages_years]
        
        return {
            'ages_ma': ages_ma,
            'temp_median': temps_median,
            'temp_5th': temps_5th,
            'temp_95th': temps_95th
        }
    except (FileNotFoundError, KeyError) as e:
        print(f"Warning: Could not load Holocene data: {e}")
        return None

def calculate_preindustrial_offset(holocene_data):
    """
    Calculate offset to normalize to pre-industrial (1850-1900) baseline
    
    The Kaufman data is relative to 19th century. We need to find what
    the temperature was during 1850-1900 period (roughly 75-125 years BP)
    and use that as our zero point.
    """
    if not holocene_data:
        return 0.0
    
    ages_years = [age * 1_000_000 for age in holocene_data['ages_ma']]
    temps = holocene_data['temp_median']
    
    # Find temperatures for 1850-1900 period (75-175 years BP to be safe)
    preindustrial_temps = []
    for age, temp in zip(ages_years, temps):
        if 75 <= age <= 175:
            preindustrial_temps.append(temp)
    
    if preindustrial_temps:
        # Average of pre-industrial period
        return np.mean(preindustrial_temps)
    else:
        # If we don't have data for that exact period, use closest point
        # Find index closest to 100 years BP
        closest_idx = min(range(len(ages_years)), 
                         key=lambda i: abs(ages_years[i] - 100))
        return temps[closest_idx]

def load_modern_temperature_data():
    """Load modern instrumental temperature data to extend to present"""
    try:
        with open('temperature_giss_monthly.json', 'r') as f:
            data = json.load(f)
        
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
        
        # Convert years to Ma BP (millions of years before present)
        # Present = 2025, so years before present = 2025 - year
        # Ma = (2025 - year) / 1,000,000
        current_year = 2025
        ages_ma = [(current_year - y) / 1_000_000 for y in years]
        
        return ages_ma, temps
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Warning: Could not load modern temperature data: {e}")
        return None, None

def create_paleoclimate_visualization():
    """
    Create Cenozoic paleoclimate visualization
    
    Shows temperature and CO₂ over the past 66 million years with:
    - Geologic period shading
    - Dual-axis plot (temp + CO₂)
    - Zoomable to see detail from millions of years down to millennia
    """
    
    if not PLOTLY_AVAILABLE:
        return None
    
    # Load data
    lr04_data = load_lr04_data()
    if not lr04_data:
        return None
    
    records = lr04_data['data']

     # ADD THIS: Load modern instrumental data
    modern_ages_ma, modern_temps = load_modern_temperature_data()   
    
    # Load Holocene reconstruction data
    holocene_data = load_holocene_data()
    
    # Calculate pre-industrial baseline offset
    preindustrial_offset = calculate_preindustrial_offset(holocene_data) if holocene_data else 0.0

    # Extract and process data
    ages_ka = np.array([r['age_ka_bp'] for r in records])
    d18o_values = np.array([r['d18o_permil'] for r in records])
    
    # Convert ages to Ma (millions of years) for better display
    ages_ma = ages_ka / 1000.0
    
    # Convert δ18O to approximate temperature anomaly
    temp_anomaly = d18o_to_temperature_approx(d18o_values)
    
    # Normalize to pre-industrial baseline
    temp_anomaly = temp_anomaly - preindustrial_offset

    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"secondary_y": True}]]
    )
    
    # Add temperature trace
    fig.add_trace(
        go.Scatter(
            x=ages_ma,
            y=temp_anomaly,
            mode='lines',
            name='Paleoclimate Benthic Stack (Lisiecki & Raymo 2005)',
            line=dict(color='#C1121F', width=1.5),
            hovertemplate='Age: %{x:.3f} Ma<br>Temp Anomaly: %{y:.1f}°C<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Add Holocene reconstruction trace
    if holocene_data:
        # Normalize Holocene data to pre-industrial
        holocene_temps_normalized = [t - preindustrial_offset for t in holocene_data['temp_median']]
        
        fig.add_trace(
            go.Scatter(
                x=holocene_data['ages_ma'],
                y=holocene_temps_normalized,
                mode='lines',
                name='Holocene Reconstruction (Kaufman 2020)',
                line=dict(color="#2CC174", width=2),
                hovertemplate='Age: %{x:.6f} Ma<br>Temp Anomaly: %{y:.2f}°C<extra></extra>'
            ),
            secondary_y=False
        )

    # ADD THIS: Add modern instrumental data
    if modern_ages_ma and modern_temps:

        # Normalize instrumental data to pre-industrial
        # NASA GISS is relative to 1951-1980, need to shift to 1850-1900
        # From literature: 1951-1980 was ~0.7°C warmer than 1850-1900
        giss_to_preindustrial_offset = 0.7
        modern_temps_normalized = [t + giss_to_preindustrial_offset - preindustrial_offset 
                                   for t in modern_temps]
        
        fig.add_trace(
            go.Scatter(
                x=modern_ages_ma,
                y=modern_temps,
                mode='lines',
                name='Instrumental Record 1880-2025 (NASA GISS)',
                line=dict(color="#3586B5", width=3),  # Bright orange-red
                hovertemplate='Year: %{customdata}<br>Temp Anomaly: %{y:.2f}°C<extra></extra>',
                customdata=[2025 - int(age * 1_000_000) for age in modern_ages_ma]
            ),
            secondary_y=False
        )
        

        # Mark "present day"
        fig.add_vline(
            x=0.000001,  # Very close to present (1 year ago)
            line_dash="solid",
            line_color="red",
            line_width=2
        )
        
        # Add annotation for present - positioned at far right
        fig.add_annotation(
    #        x=0.000001,
            x=np.log10(0.000001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1,  # Use relative positioning (top of plot)
            yref="paper",
            text="Present<br>(2025)",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1
        )

# Add geologic period shading - use actual Ma values, not log
    for period in GEOLOGIC_PERIODS:
        # Use the actual Ma values - the log axis will transform them
        fig.add_shape(
            type="rect",
            xref="x",
            yref="paper",
            x0=period['start'],  # Use actual value, not log!
            y0=0,
            x1=period['end'],     # Use actual value, not log!
            y1=1,
            fillcolor=period['color'],
            opacity=0.2,
            layer="below",
            line_width=0
        )
        
        # Calculate midpoint and width in log space for label positioning
        start_log = np.log10(period['start'])
        end_log = np.log10(period['end'])
        midpoint_log = (start_log + end_log) / 2
        period_width = abs(start_log - end_log)
        
        # Adjust font size based on period width
        if period_width > 0.3:
            font_size = 10
            opacity = 1.0
        elif period_width > 0.15:
            font_size = 8
            opacity = 0.9
        else:
            font_size = 7
            opacity = 0.8
        
        # But for annotations, we still need log space
        fig.add_annotation(
            x=midpoint_log,
            xref="x",
            y=1.02,
            yref="paper",
            text=period['name'],
            showarrow=False,
            font=dict(size=font_size, color='#333'),
            textangle=-45,
            xanchor='left',
            yanchor='bottom',
            opacity=opacity
        )


    # Add era labels (broader time divisions)
    eras = [
        {'name': 'Precambrian', 'start': 4500, 'end': 541, 'color': '#8B4789'},
        {'name': 'Paleozoic', 'start': 541, 'end': 252.2, 'color': '#7FA056'},
        {'name': 'Mesozoic', 'start': 252.2, 'end': 66.0, 'color': '#34B2C9'},
        {'name': 'Cenozoic', 'start': 66.0, 'end': 0.000001, 'color': '#FD9A52'}
    ]
    
    for era in eras:
        # Calculate midpoint in log space
        midpoint_log = (np.log10(era['start']) + np.log10(era['end'])) / 2
        
        fig.add_annotation(
            x=midpoint_log,
            y=1.00,  # Position above the period labels
            yref="paper",
            text=f"<b>{era['name']}</b>",
            showarrow=False,
            font=dict(size=12, color=era['color']),
            xanchor='center',
            yanchor='bottom'
        )

    # Mark the Holocene explicitly
    fig.add_trace(
        go.Scatter(
            x=[0.0117, 0.0117],
            y=[temp_anomaly.min(), temp_anomaly.max()],
            mode='lines',
            name='Holocene Begins (11.7 ka)',
            line=dict(color='green', width=2, dash='dash'),
            showlegend=True,
            hoverinfo='skip'
        ),
        secondary_y=False
    )
    
    # Add annotation for Holocene - positioned directly over the line
    fig.add_annotation(
#        x=0.0117,
        x=np.log10(0.0117),  # Use log10 for log-scale x-axis
        xref='x',        
        y=6,  # Adjust this value to position vertically where you want
        text="Start of Holocene<br>(11,700 years ago)",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='green',
        ax=0,
        ay=-40,
        font=dict(size=9, color='green'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='green',
        borderwidth=1
    )

    
    # Ice Ages Begin - positioned to align with data
    fig.add_annotation(
        x=np.log10(2.58),  # Use log10 for log-scale x-axis
        y=0.5,  # Adjusted y position to be closer to where data is
        text='Ice Ages Begin',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#333',
        ax=0,
        ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#333',
        borderwidth=1
    )
    
    info_text = (
        "<b>Earth's Climate History</b><br>"
        "<br>"
        "🔊 Paleoclimate: LR04 Benthic Stack (5.3 Ma)<br>"
        "🌍 Holocene: Kaufman et al. 2020 (12 ka)<br>"
        "🌡️ Modern: NASA GISS (1880-2025)<br>"
        "⏱️ Time Span: 4.5 Ga to 2100 CE<br>"
        "📏 Baseline: Pre-industrial (1850-1900)<br>"
        "<br>"
        "🔍 <b>Use zoom to explore:</b><br>"
        "• Ice age cycles (last 2.6 Ma)<br>"
        "• Holocene stability (last 12,000 years)<br>"
        "• Individual glacial/interglacial periods<br>"
        "<br>"
        "💡 <b>Key Insight:</b> The Holocene's stable climate<br>"
        "enabled human civilization to flourish."
    )    

    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.02, y=0.50,
        xanchor="left", yanchor="top",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#2E86AB",
        borderwidth=2,
        borderpad=10,
        showarrow=False,
        font=dict(size=10),
        align="left"
    )
    
    fig.update_xaxes(
        title_text="Millions of Years Before Present (Ma)",
        autorange=False,
        range=[np.log10(4500), np.log10(0.000001)],  # 4.5 Ga to ~present
        type="log",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )   

    fig.update_yaxes(
        title_text="Temperature Anomaly (°C, relative to present)",
        secondary_y=False,
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )
    
    # Layout
    fig.update_layout(
        title={
            'text': "Earth's Climate History: 530 Million Year Ago (Pliocene) to Present (Holocene)<br><sub>From Planet Formation to Climate Projections</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        hovermode='closest',
        showlegend=True,
        legend=dict(
            x=0.90,
            y=0.02,
            xanchor='right',
            yanchor='bottom',
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#333',
            borderwidth=1
        ),
        plot_bgcolor='white',
        height=700,
        margin=dict(t=100, b=80, l=80, r=80)
    )
    
    # Add source citation
    fig.add_annotation(
        text="Data: Lisiecki & Raymo (2005) LR04 | Kaufman et al. (2020) Holocene | NASA GISS | Paloma's Orrery",
        xref="paper", yref="paper",
        x=0.5, y=-0.12,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='#666')
    )
    
    return fig

def main():
    """Test the visualization"""
    if not PLOTLY_AVAILABLE:
        print("Error: Plotly not available")
        return
    
    print("Creating paleoclimate visualization...")
    fig = create_paleoclimate_visualization()
    
    if fig:
        print("✓ Visualization created successfully")
        # Offer to save
        save_plot(fig, "paleoclimate_cenozoic_66Ma")
        print("Opening in browser...")
        fig.show()
    
    else:
        print("✗ Could not create visualization - check if data is cached")
        print(f"Expected data file: {LR04_CACHE}")

if __name__ == '__main__':
    main()
