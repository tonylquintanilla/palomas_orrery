"""
Paleoclimate Visualization for Paloma's Orrery
Phanerozoic temperature reconstruction (540 Ma - present)

Shows the "big picture" of Earth's climate history with Plotly's zoom capability
to explore details from the Phanerozoic "double hump" down to ice ages and 
the remarkable stability of the Holocene.

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
# SCOTESE_PHANEROZOIC = '8c__Phanerozoic_Pole_to_Equator_Temperatures.csv'
SCOTESE_PHANEROZOIC = os.path.join(PALEO_DATA_DIR, '8c__Phanerozoic_Pole_to_Equator_Temperatures.csv')

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

def load_scotese_phanerozoic_data():
    """
    Load Scotese et al. (2021) Phanerozoic temperature data
    
    Returns global average temperatures from 540 Ma to 0 Ma
    Based on pole-to-equator temperature reconstructions
    """
    try:
        import csv
        
        ages_ma = []
        temps_global = []
        
        with open(SCOTESE_PHANEROZOIC, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            
            # Read header row (ages)
            header = next(reader)
            # Remove the 'latitude/age' label and convert to float
            age_values = [float(age) for age in header[1:]]
            
            # Read all latitude rows
            temp_grid = []
            for row in reader:
                if row and row[0]:  # Skip empty rows
                    try:
                        # Skip the latitude label, convert temps to float
                        temps = [float(t) for t in row[1:] if t]
                        if temps:  # Only add non-empty rows
                            temp_grid.append(temps)
                    except (ValueError, IndexError):
                        continue
            
            # Calculate global average by averaging across all latitudes for each age
            if temp_grid:
                # Convert to numpy for easier calculation
                import numpy as np
                temp_array = np.array(temp_grid)
                
                # Global average is mean across all latitudes (rows)
                global_avg_temps = np.mean(temp_array, axis=0)
                
                ages_ma = age_values
                temps_global = global_avg_temps.tolist()
        
        if ages_ma and temps_global:
            return {
                'ages_ma': ages_ma,
                'temp_global': temps_global
            }
        return None
        
    except (FileNotFoundError, Exception) as e:
        print(f"Warning: Could not load Scotese Phanerozoic data: {e}")
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
        with open('data/temperature_giss_monthly.json', 'r') as f:
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
    Create Phanerozoic paleoclimate visualization
    
    Shows temperature over the past 540 million years with:
    - Geologic period shading
    - Multiple datasets: Scotese (540-5 Ma), LR04 (5-0.01 Ma), Holocene (12 ka), Modern (1880-present)
    - Zoomable to see detail from hundreds of millions of years down to millennia
    """
    
    if not PLOTLY_AVAILABLE:
        return None
    
    # Load all data sources
    scotese_data = load_scotese_phanerozoic_data()
    lr04_data = load_lr04_data()
    holocene_data = load_holocene_data()
    modern_ages_ma, modern_temps = load_modern_temperature_data()
    
    # Calculate pre-industrial baseline offset
    preindustrial_offset = calculate_preindustrial_offset(holocene_data) if holocene_data else 0.0
    
    # --- Process LR04 Data ---
    if not lr04_data:
        return None
    
    records = lr04_data['data']
    ages_ka = np.array([r['age_ka_bp'] for r in records])
    d18o_values = np.array([r['d18o_permil'] for r in records])
    ages_ma_lr04 = ages_ka / 1000.0
    temp_anomaly_lr04 = d18o_to_temperature_approx(d18o_values)
    temp_anomaly_lr04 = temp_anomaly_lr04 - preindustrial_offset
    
    # Filter to end at Holocene start (12 ka = 0.012 Ma)
    # LR04 optimized for ice age cycles; Kaufman better for Holocene
    holocene_start_ma = 0.012
    mask_lr04 = ages_ma_lr04 >= holocene_start_ma
    ages_ma_lr04 = ages_ma_lr04[mask_lr04]
    temp_anomaly_lr04 = temp_anomaly_lr04[mask_lr04]

    # --- Process Scotese Data ---
    scotese_ages_ma = None
    scotese_temps = None
    
    if scotese_data:
        scotese_ages_ma = np.array(scotese_data['ages_ma'])
        scotese_temps_raw = np.array(scotese_data['temp_global'])
        
        # Normalize Scotese data to match LR04 at the transition point (~5 Ma)
        # Find Scotese value at 5 Ma
        transition_age = 5.0
        scotese_at_transition = np.interp(transition_age, scotese_ages_ma, scotese_temps_raw)
        
        # Find LR04 value at 5 Ma
        lr04_at_transition = np.interp(transition_age, ages_ma_lr04, temp_anomaly_lr04)
        
        # Calculate offset to align them
        scotese_offset = lr04_at_transition - scotese_at_transition
        scotese_temps = scotese_temps_raw + scotese_offset
        
        # Filter to use Scotese data for deep time (>2 Ma)
        # Scotese method: Lithologic indicators + Köppen belts (~5 Myr resolution)
        # Optimized for deep time patterns, not high-resolution recent climate
        # Use LR04/Holocene/Modern for <2 Ma (higher temporal resolution)
        mask = scotese_ages_ma >= 2.0
        scotese_ages_ma = scotese_ages_ma[mask]
        scotese_temps = scotese_temps[mask]

    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"secondary_y": True}]]
    )
    
    # Add Scotese Phanerozoic temperature trace (540-5 Ma) - plotted first so it's behind
    if scotese_ages_ma is not None and scotese_temps is not None:
        fig.add_trace(
            go.Scatter(
                x=scotese_ages_ma,
                y=scotese_temps,
                mode='lines',
                name='Phanerozoic Global Temperature (Scotese et al. 2021)',
                line=dict(color='#003049', width=2),
        #        hovertemplate='Age: %{x:.1f} Ma<br>Temp Anomaly: %{y:.1f}°C<extra></extra>'
                hovertemplate='Age: %{x:.1f} Ma<br>Temp Anomaly: %{y:.1f}°C<br><i>~5 Myr resolution (deep time method)</i><extra></extra>'
            ),
            secondary_y=False
        )
    
    # Add LR04 temperature trace (5.3 Ma - 10 ka)
    fig.add_trace(
        go.Scatter(
            x=ages_ma_lr04,
            y=temp_anomaly_lr04,
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
        
        # Filter to end at 1880 CE (where instrumental record begins)
        # 1880 CE = 145 years before 2025 = 0.000145 Ma
        instrumental_start_ma = 0.000145
        holocene_ages_filtered = []
        holocene_temps_filtered = []
        for age, temp in zip(holocene_data['ages_ma'], holocene_temps_normalized):
            if age >= instrumental_start_ma:  # Older than 1880
                holocene_ages_filtered.append(age)
                holocene_temps_filtered.append(temp)

        fig.add_trace(
            go.Scatter(
        #        x=holocene_data['ages_ma'],
        #        y=holocene_temps_normalized,
                x=holocene_ages_filtered,
                y=holocene_temps_filtered,                
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
        
        # Add Younger Dryas regional temperature bands
        # Shows spatial heterogeneity: different regions experienced different cooling
        # Based on paleoclimate reconstructions and ice core data
        
        yd_start = 0.0129  # 12,900 years ago
        yd_end = 0.0117    # 11,700 years ago
        
        # Band 1: Global average cooling (~0.5-1.5°C)
        # Subtle signal when averaged over entire planet
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[0, -1.5, -1.5, 0, 0],
                fill='toself',
                fillcolor='rgba(0,206,209,0.1)',  # Very light turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Global (~1°C)',
                showlegend=True,
                hovertemplate='Younger Dryas (Global)<br>Estimated: 0.5-1.5°C cooling<br><i>Global average signal</i><extra></extra>'
            ),
            secondary_y=False
        )
        
        # Band 2: Northern Hemisphere mid-latitudes (Europe & North America, ~2-6°C)
        # Regional cooling where most humans lived
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[-2, -6, -6, -2, -2],
                fill='toself',
                fillcolor='rgba(0,206,209,0.4)',  # Medium turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Regional (~4°C)',
                showlegend=True,
                hovertemplate='Younger Dryas (Regional)<br>Europe & North America: 2-6°C cooling<br><i>Mid-latitude Northern Hemisphere</i><extra></extra>'
            ),
            secondary_y=False
        )
        
        # Band 3: Greenland/North Atlantic extreme (~8-10°C)
        # Maximum regional impact from ice core records
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[-8, -10, -10, -8, -8],
                fill='toself',
                fillcolor='rgba(0,206,209,0.9)',  # Darker turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Greenland (~9°C)',
                showlegend=True,
                hovertemplate='Younger Dryas (Greenland)<br>GISP2 ice core: 8-10°C cooling<br><i>Maximum regional impact</i><extra></extra>'
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
            x=np.log10(0.000001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="2025",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>Present Day (2025 CE)</b><br>'
                      'Global temp: +1.28°C above pre-industrial<br>'
                      'Atmospheric CO₂: ~425 ppm<br>'
                      'Warmest decade in recorded history<br>'
                      'Rate of change: ~0.2°C per decade<br>'
                      'Unprecedented in Holocene stability',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 10 years ago (2015) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.00001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="2015",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>2015 CE</b><br>'
                      'Year of Paris Climate Agreement<br>'
                      'Global temp: +1.0°C above pre-industrial<br>'
                      'Hottest year on record (at the time)<br>'
                      '196 nations commit to climate action<br>'
                      'Beginning of renewable energy surge',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 100 years ago (1925) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.0001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="1925",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1925 CE</b><br>'
                      'The Roaring Twenties<br>'
                      'Global temp: ~0.1°C above pre-industrial<br>'
                      'World population: 2 billion<br>'
                      'Early automobile age begins<br>'
                      'CO₂ starting to rise from coal use<br>'
                      'Beginning of modern warming signal',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 1000 years ago (1025) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="1025",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1025 CE (Medieval Period)</b><br>'
                      'Height of Medieval Warm Period<br>'
                      'Vikings settled Greenland<br>'
                      'Stable Holocene climate continues<br>'
                      'Global temp within Holocene range<br>'
                      'Agriculture thriving across Europe/Asia<br>'
                      'Pre-industrial baseline conditions',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 10,000 years ago (10,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.01),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="10,000 BCE",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>10,000 BCE</b><br>'
                      'End of last Ice Age<br>'
                      'Beginning of Holocene interglacial<br>'
                      'Agricultural Revolution begins<br>'
                      'Humans start farming in Fertile Crescent<br>'
                      'Climate stability enables civilization<br>'
                      'World population: ~5 million',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )                       

        # Add annotation for 100,000 years ago (100,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.1),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="100,000 BCE",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>100,000 BCE</b><br>'
                      'Deep in Pleistocene Ice Age<br>'
                      'Modern humans in Africa<br>'
                      'Neanderthals in Europe<br>'
                      'Sea levels ~100m lower than today<br>'
                      'Massive ice sheets cover continents<br>'
                      'Temp ~5-10°C colder than present',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 1,000,000 years ago (1,000,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(1.0),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="1 million BCE (1 Ma)",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1 Million Years Ago</b><br>'
                      'Early Pleistocene Ice Age<br>'
                      'Homo erectus using fire<br>'
                      '100,000-year glacial cycles begin<br>'
                      'Ice sheets grow and retreat<br>'
                      'Human ancestors adapting to change<br>'
                      'Stone tool technology advancing',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 10 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(10),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="10 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>10 Million Years Ago</b><br>'
                      'Late Miocene Epoch<br>'
                      'Grasslands expanding worldwide<br>'
                      'Great apes diversifying in Africa<br>'
                      'Antarctica fully ice-covered<br>'
                      'Global cooling trend underway<br>'
                      'Modern ocean circulation patterns form',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 100 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(100),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="100 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>100 Million Years Ago</b><br>'
                      'Mid-Cretaceous greenhouse world<br>'
                      'Dinosaurs at peak diversity<br>'
                      'No polar ice caps<br>'
                      'Sea levels 200m higher than today<br>'
                      'CO₂ ~4x higher than pre-industrial<br>'
                      'Temp ~10°C warmer than present',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        ) 

        # Add annotation for 540 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(540),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="<540 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>Phanerozoic Eon (0.538 billion years)</b><br>'
                      'Beginning of Cambrian Period 538.8 million years ago. Cambrian Explosion of life.<br>'
                      'First animals with shells. Trilobites, early fish appear. Complex ecosystems emerge.<br><br>'
                      '<b>Proterozoic Eon (2.0 billion years)</b><br>'
                      '2.5 Billion Years Ago (Ga) to 538.8 Million Years Ago (Ma)<br>'
                      'Great Oxidation Event. Complex (eukaryotic) cells. Assembly and breakup of supercontinents.<br>' 
                      'First large, soft-bodied multicellular animals (Ediacaran biota).<br><br>'
                      '<b>Archean Eon (1.5 billion years)</b><br>'
                      '4.0 Ga to 2.5 Ga<br>'
                      'Formation of the first continental crust (cratons), the cooling of the planet, and the<br>' 
                      'origin of life (represented by microbial fossils like stromatolites).<br><br>'
                      '<b>Hadean Eon (0.5 billion years)</b><br>'
                      '4.54 Ga to 4.0 Ga<br>'
                      'Earth\'s formation (4.54 Ga). Intense meteorite bombardment.<br>' 
                      'Initial differentiation of the planet\'s core, mantle, and crust.',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
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
    
    """
    # Add Phanerozoic Eon label (spans Paleozoic + Mesozoic + Cenozoic)
    # Calculate midpoint across all three Phanerozoic eras
    phanerozoic_start = 541  # Beginning of Cambrian
    phanerozoic_end = 0.000001  # Present
    phanerozoic_midpoint_log = (np.log10(phanerozoic_start) + np.log10(phanerozoic_end)) / 2
    
    fig.add_annotation(
        x=phanerozoic_midpoint_log,
        y=1.065,  # Position above era labels
        yref="paper",
        text="<b>PHANEROZOIC EON (540 Ma - Present)</b>",
        showarrow=False,
        font=dict(size=14, color='#2C5F2D'),  # Dark green
        xanchor='center',
        yanchor='bottom',
        bgcolor='rgba(255,255,255,0.7)',
        bordercolor='#2C5F2D',
        borderwidth=2,
        borderpad=4
    )
    """
    
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
    #        y=[temp_anomaly_lr04.min(), temp_anomaly_lr04.max()],
            y=[-13.0, 0.0],            
            mode='lines',
            name='Holocene Begins (11.7 ka)',
            line=dict(color='green', width=2, dash='dash'),
            showlegend=True,
            hoverinfo='skip'
        ),
        secondary_y=False
    )
    
    # ax=0, ay=-40 → Straight down ⬇️
    # ax=40, ay=0 → Straight right ➡️
    # ax=40, ay=-60 → Diagonal up-right ↗️
    # ax=-40, ay=40 → Diagonal down-left ↙️

    # Anthropocene (recent, so use arrow like others)
    fig.add_annotation(
        x=np.log10(0.000075),  # 1950 CE is 75 years ago
        y=0.0,
        text='Proposed Anthropocene<br>(after 1950 CE)',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='red',
        ax=28,
        ay=-70,
        font=dict(size=9, color='red'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='red',
        borderwidth=1,
        hovertext='<b>Proposed Anthropocene Epoch</b><br>'
                  'Proposed start: 1950 CE (Great Acceleration)<br>'
                  'Human activity dominates Earth system<br>'
                  'Nuclear testing, plastic, concrete markers<br>'
                  'CO₂ rising faster than any natural event<br>'
                  'Sixth mass extinction underway<br>'
                  'Geologists debate: new epoch or event?',
        hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
    )

    # Origin of Humanity - about 350 to 160,000 years ago
    # Add visual period marker (blue shaded region showing event duration)
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.350,  # 350,000 ya
        x1=0.160,  # 160,000 ya
        y0=0,
        y1=1,
    #    fillcolor='#00D188,0.3', 
        fillcolor='rgba(0, 209, 136,0.1)',
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.25),  
        y=4.5,
        text='Origin of Humanity',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor="#00D188",  
        ax=0,
        ay=0, 
        font=dict(size=9, color='#00D188'),
        bgcolor='rgba(0, 209, 136,0)',
        bordercolor='#00D188',
        borderwidth=1,          
        hovertext='<b>Origin of Humanity (350,000-160,000 years ago)</b><br>'
        'The generally accepted range for the origin of Homo sapiens is between 300,000 and 200,000 years ago,<br>' 
        'although recent discoveries continually push the minimum date back. This range is based on the oldest<br>' 
        'widely recognized fossil evidence, all found in Africa.<br>' 
        '<b>Earliest Evidence (c. 300,000 years ago):</b> Fossils from the Jebel Irhoud site in Morocco, dated<br>' 
        'to approximately 300,000 years ago (with a range of 350,000 - 280,000 years ago), are currently the<br>' 
        'oldest known remains classified as early Homo sapiens. These specimens possess a mix of archaic and<br>' 
        'modern facial features.<br>' 
        '<b>Early Modern Humans (c. 233,000 - 160,000 years ago):</b><br>' 
        '- Omo I remains from Ethiopia, recently re-dated to at least 230,000 years ago.<br>' 
        '- Fossils from Herto, Ethiopia, dated to about 160,000 years ago.<br>' 
        '- The Florisbad Skull from South Africa, dated to about 260,000 years ago.<br>' 
        'The current scientific consensus suggests that Homo sapiens did not originate in a single "cradle"<br>' 
        'but rather emerged across the entire African continent from a widespread population of ancestral humans.<br>',                  
        hoverlabel=dict(bgcolor='rgba(0, 209, 136,0.7)', font_size=11)
    )

    # Younger Dryas - the "Big Freeze" that interrupted deglaciation
    # Add visual period marker (blue shaded region showing event duration)
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.0129,  # 12,900 years ago (start)
        x1=0.0117,  # 11,700 years ago (end)
        y0=0,
        y1=1,
        fillcolor='rgba(0,206,209,0)',  # Light turquoise
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.0123),  # ~12,300 years ago (middle of YD)
        y=-3.1,
        text='Younger Dryas<br>("Big Freeze")',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#00CED1',  # Dark turquoise
        ax=-95,
        ay=-95, 
        font=dict(size=9, color='#00CED1'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#00CED1',
        borderwidth=1,          
        hovertext='<b>Younger Dryas (12,900-11,700 years ago)</b><br>'
                  'Abrupt cooling event with regional variations:<br>'
                  '  • <b>Global</b>: ~1°C cooling (averaged)<br>'
                  '  • <b>Europe/N. America</b>: 2-6°C cooling<br>'
                  '  • <b>Greenland</b>: 8-10°C cooling (ice cores)<br>'
                  '<i>Brief event smoothed in 100-year resolution data</i><br>'
                  'Meltwater disrupted Gulf Stream circulation<br>'
                  'Led to megafauna extinctions & agricultural origins<br>'
                  '<b>Three turquoise bands show regional cooling ranges</b>',                  
        hoverlabel=dict(bgcolor='rgba(0,206,209,0.9)', font_size=11)
    )
    
    # Add annotation for Holocene - positioned directly over the line
    fig.add_annotation(
#        x=0.0117,
        x=np.log10(0.0117),  # Use log10 for log-scale x-axis
        xref='x',        
        y=1.5,  # Adjust this value to position vertically where you want
        text="<b>Start of Holocene</b>",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='green',
        ax=0,
        ay=-42,
        font=dict(size=9, color='green'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='green',
        borderwidth=1,
        hovertext='<b>Holocene Begins (11,700 years ago)</b><br>'
                  'End of last glacial period<br>'
                  'Rapid warming of ~5°C in centuries<br>'
                  'Ice sheets retreat, sea level rises 120m<br>'
                  'Stable, warm climate enables agriculture<br>'
                  'Human civilization flourishes<br>'
                  'Most stable climate in 800,000 years',
        hoverlabel=dict(bgcolor='rgba(34,139,34,0.9)', font_size=11)
    )

    # Medieval Warm Period
    # Add visual period marker (orange shaded region)
    # MWP: 950-1250 CE = 1075-775 years ago
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.001075,  # 950 CE (1075 years ago)
        x1=0.000775,  # 1250 CE (775 years ago)
        y0=0,
        y1=1,
        fillcolor='rgba(255,140,0,0.12)',  # Light orange
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
            x=np.log10(0.000925),  # ~1100 CE (middle of MWP) is 925 years ago
            y=0.10,
            text='Medieval Warm Period',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor='#FF8C00',  # Dark orange
            ax=-45,
            ay=-55,
            font=dict(size=9, color='#FF8C00'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#FF8C00',
            borderwidth=1,
            hovertext='<b>Medieval Warm Period (950-1250 CE)</b><br>'
                    'Regional warming in North Atlantic/Europe<br>'
                    'Vikings settled Greenland, agricultural boom<br>'
                    '<br>'
                    '<b>Temperature Ranges (see horizontal bands):</b><br>'
                    '• Regional (light orange): +0.3 to +0.5°C<br>'
                    '• Global average (dark orange): +0.1 to +0.2°C<br>'
                    '<br>'
                    '<i>Note: Century-scale event smoothed in 100-yr data</i><br>'
                    'Shows: Small global changes = large regional impacts<br>'
                    '<b>🔍 Zoom to 500-1500 CE to see temperature bands clearly!</b><br>'
                    '<b>Orange vertical region shows event duration</b>',
            hoverlabel=dict(bgcolor='rgba(255,140,0,0.9)', font_size=11)
        )

# Medieval Warm Period - Temperature Range Bands
    # Showing BOTH regional and global ranges with nested opacity
    
    # Regional range (North Atlantic/Europe): ~+0.3 to +0.5°C
    # Lighter, wider band showing local impact
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.001075,  # 950 CE
        x1=0.000775,  # 1250 CE
        y0=0.3,  # Regional range (wider)
        y1=0.5,
        fillcolor='rgba(255,140,0,0.15)',  # Light orange
        line=dict(width=0),  # No border (cleaner)
        layer="below"
    )
    
    # Global range: ~+0.1 to +0.2°C
    # Darker, narrower band showing planetary average
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.001075,  # 950 CE
        x1=0.000775,  # 1250 CE
        y0=0.1,  # Global range (narrower)
        y1=0.2,
        fillcolor='rgba(255,140,0,0.35)',  # Darker orange
        line=dict(width=0),
        layer="below"
    )

    # Little Ice Age
    # Add visual period marker (blue shaded region)
    # LIA: 1300-1850 CE = 725-175 years ago
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.000725,  # 1300 CE (725 years ago)
        x1=0.000175,  # 1850 CE (175 years ago)
        y0=0,
        y1=1,
        fillcolor='rgba(65,105,225,0.12)',  # Light royal blue
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.000450),  # ~1575 CE (middle of LIA) is 450 years ago
        y=-0.2,
        text='Little Ice Age',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#4169E1',  # Royal blue
        ax=20,
        ay=-55, 
        font=dict(size=9, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#4169E1',
        borderwidth=1,
        hovertext='<b>Little Ice Age (1300-1850 CE)</b><br>'
                  'Regional cooling in North Atlantic/Europe<br>'
                  'Viking Greenland abandoned, Thames froze, famines<br>'
                  '<br>'
                  '<b>Temperature Ranges (see horizontal bands):</b><br>'
                  '• Regional (light blue): -0.5 to -1.0°C<br>'
                  '• Global average (dark blue): -0.2 to -0.3°C<br>'
                  '<br>'
                  '<i>Note: Best visible in regional high-res proxies</i><br>'
                  'Even small global changes affect civilizations<br>'
                  '<b>🔍 Zoom to 1200-1900 CE to see temperature bands clearly!</b><br>'
                  '<b>Blue vertical region shows event duration</b>',
        hoverlabel=dict(bgcolor='rgba(65,105,225,0.9)', font_size=11)
    )

# Little Ice Age - Temperature Range Bands
    # Showing BOTH regional and global ranges with nested opacity
    
    # Regional range (North Atlantic/Europe): ~-0.5 to -1.0°C
    # Lighter, wider band showing local impact
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.000725,  # 1300 CE
        x1=0.000175,  # 1850 CE
        y0=-1.0,  # Regional range (wider)
        y1=-0.5,
        fillcolor='rgba(65,105,225,0.15)',  # Light blue
        line=dict(width=0),
        layer="below"
    )
    
    # Global range: ~-0.2 to -0.3°C
    # Darker, narrower band showing planetary average
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.000725,  # 1300 CE
        x1=0.000175,  # 1850 CE
        y0=-0.3,  # Global range (narrower)
        y1=-0.2,
        fillcolor='rgba(65,105,225,0.35)',  # Darker blue
        line=dict(width=0),
        layer="below"
    )    

# K-Pg Extinction
    fig.add_annotation(
#        x=66.0, 
        x=np.log10(66.0),
        y=-8,
        text='K-Pg Extinction<br>(Dinosaurs)',
        showarrow=False, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=0, ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>K-Pg Extinction (66 Million Years Ago)</b><br>'
                  'Asteroid impact in Yucatan Peninsula<br>'
                  'Chicxulub crater: 180 km diameter<br>'
                  '~75% of species extinct (including dinosaurs)<br>'
                  'Impact winter: years of darkness and cold<br>'
                  'Ended Mesozoic Era, began Age of Mammals<br>'
                  'Birds (avian dinosaurs) survived',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # PETM
    fig.add_annotation(
        x=np.log10(56.0),
        y=15.78,
        text='PETM<br>(Thermal Maximum)',
        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=0, 
        ay=-90,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>PETM - Paleocene-Eocene Thermal Maximum</b><br>'
                  '~56 million years ago<br>'
                  'Rapid warming of ~5-8°C in <10,000 years<br>'
                  'Massive carbon release (volcanic/methane)<br>'
                  'Ocean acidification, deep-sea extinctions<br>'
                  'Mammals diversified and spread globally<br>'
                  'Closest ancient analog to modern warming',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # Grande Coupure
    fig.add_annotation(
        x=np.log10(34.0),
        y=8.44,
        text='Grande Coupure<br>(Cooling begins)',
        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=40, 
        ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>Grande Coupure - The "Great Cut"</b><br>'
                  '~34 million years ago (Eocene-Oligocene)<br>'
                  'Abrupt cooling, ice sheets form on Antarctica<br>'
                  'Drop of ~4°C in less than 400,000 years<br>'
                  'Opening of Drake Passage (Antarctica-S.America)<br>'
                  'Circumpolar current isolates Antarctica<br>'
                  'Major faunal turnover in Europe',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
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
        borderwidth=1,
        hovertext='<b>Quaternary Ice Age Begins</b><br>'
                  '~2.6 million years ago (Pleistocene)<br>'
                  'Regular glacial-interglacial cycles begin<br>'
                  '41,000-year cycles, then 100,000-year cycles<br>'
                  'Ice sheets cover Northern Hemisphere<br>'
                  'Human ancestors adapt to climate swings<br>'
                  'Still in this ice age today (Holocene = warm phase)',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # ===== DEEP TIME EVENTS (with ? hover for minimal clutter) =====
    
    # Cretaceous Thermal Maximum
    fig.add_annotation(
        x=np.log10(90),
        y=20,
        text='?',
        showarrow=False,
        font=dict(size=16, color='#7FC64E'),  # Cretaceous green
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#7FC64E',
        borderwidth=2,
        borderpad=4,
        hovertext='<b>Cretaceous Thermal Maximum (~90 Ma)</b><br>'
                  'Peak Mesozoic greenhouse conditions<br>'
                  'Global temp ~20°C above pre-industrial<br>'
                  'High CO₂, no polar ice, warm oceans<br>'
                  'Dinosaurs thrived in hot world',
        hoverlabel=dict(bgcolor='rgba(127,198,78,0.9)', font_size=11)
    )
    
    # Permian-Triassic Extinction
    fig.add_annotation(
        x=np.log10(252),
        y=25.5,
        text='?',
        showarrow=False,
        font=dict(size=16, color='#F04028'),  # Permian red
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#F04028',
        borderwidth=2,
        borderpad=4,
        hovertext='<b>Permian-Triassic Extinction (~252 Ma)</b><br>'
                  'The "Great Dying" - worst mass extinction<br>'
                  '~96% of marine species extinct<br>'
                  '~70% of terrestrial vertebrates extinct<br>'
                  'Caused by Siberian Traps volcanism<br>'
                  'Massive CO₂ release, ocean anoxia<br>'
                  'Global temp ~28°C (peak hothouse)',
        hoverlabel=dict(bgcolor='rgba(240,64,40,0.9)', font_size=11)
    )
    
    # Carboniferous Icehouse
    fig.add_annotation(
        x=np.log10(300),
        y=-3.5,
        text='?',
        showarrow=False,
        font=dict(size=16, color='#67A599'),  # Carboniferous teal
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#67A599',
        borderwidth=2,
        borderpad=4,
        hovertext='<b>Carboniferous Icehouse (~300 Ma)</b><br>'
                  'The "Coal Age" - vast tropical forests<br>'
                  'Trees evolved lignin (hard to decompose)<br>'
                  'Massive carbon burial → coal deposits<br>'
                  'Drew down atmospheric CO₂<br>'
                  'Triggered glaciation (~12°C drop)<br>'
                  'First forests changed the planet!',
        hoverlabel=dict(bgcolor='rgba(103,165,153,0.9)', font_size=11)
    )
    
    # Late Ordovician Glaciation
    fig.add_annotation(
        x=np.log10(445),
        y=-8,
        text='?',
        showarrow=False,
        font=dict(size=16, color='#009270'),  # Ordovician green
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#009270',
        borderwidth=2,
        borderpad=4,
        hovertext='<b>Late Ordovician Glaciation (~445 Ma)</b><br>'
                  'First major Phanerozoic icehouse<br>'
                  'Rapid cooling to ~5°C<br>'
                  'Massive ice sheets on Gondwana<br>'
                  'Sea level drop of ~100m<br>'
                  'End-Ordovician mass extinction<br>'
                  '~85% of marine species extinct',
        hoverlabel=dict(bgcolor='rgba(0,146,112,0.9)', font_size=11)
    )
    
    # End-Triassic Extinction (optional but you said "all"!)
    fig.add_annotation(
        x=np.log10(201),
        y=18,
        text='?',
        showarrow=False,
        font=dict(size=16, color='#812B92'),  # Triassic purple
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#812B92',
        borderwidth=2,
        borderpad=4,
        hovertext='<b>End-Triassic Extinction (~201 Ma)</b><br>'
                  'One of the "Big Five" mass extinctions<br>'
                  '~75% of species extinct<br>'
                  'Caused by CAMP volcanism<br>'
                  '(Central Atlantic Magmatic Province)<br>'
                  'CO₂ spike, ocean acidification<br>'
                  'Opened ecological space for dinosaurs',
        hoverlabel=dict(bgcolor='rgba(129,43,146,0.9)', font_size=11)
    )
        

    # Add 3.3°C
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=3.3,
        x1=0.94,
        y1=3.3,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
    # Add 2.8°C 
#    fig.add_shape(
#        type="line",
#        xref="paper",
#        yref="y",
#        x0=0.0,
#        y0=2.8,
#        x1=0.94,
#        y1=2.8,
#        line=dict(
#            color="red",
#            width=1,
#            dash="dot"
#        )
#    )

    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=3.40,
        text="Current Policies (UNEP): 2.6°C - 3.3°C",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='red'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 2.6°C 
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=2.6,
        x1=0.94,
        y1=2.6,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
#    fig.add_annotation(
#        xref="paper",
#        yref="y",
#        x=0.82,
#        y=3.10,
#        text="2.5°C to 2.9°C Trajectory",
#        showarrow=False,
#        bgcolor="rgba(255,255,255,0.8)",
#        font=dict(size=9, color='black'),
#        xanchor='left',
#        yanchor='bottom'
#    )

    # Add 1.28°C current anomaly line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=1.28,
        x1=0.94,
        y1=1.28,
        line=dict(
            color="green",
            width=1,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=1.40,
        text="1.28°C -- Current Anomaly",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='green'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 0°C baseline - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=0,
        x1=0.94,
        y1=0,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=-1.0,
        text="0°C -- 1850 - 1900 Baseline",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    info_text = (
        "<b>Earth's Climate History (Phanerozoic Eon, 540 Ma to Present)</b><br>"
        "<br>"
        "🌍 <b>Phanerozoic:</b> Scotese et al. 2021 (540 Ma); "
        "   <i>Method: Lithologic indicators + δ¹⁸O + models</i><br>"
        "🔊 <b>Paleoclimate:</b> LR04 Benthic Stack (5.3 Ma); "
        "   <i>Method: Benthic foraminifera δ¹⁸O</i><br>"
        "❄️ <b>Younger Dryas:</b> Alley (GISP2 ice core, 2000); "
        "   <i>Method: Greenland ice core δ¹⁸O</i><br>"
        "🏔️ <b>Holocene:</b> Kaufman et al. 2020 (12 ka); "
        "   <i>Method: Multi-proxy (pollen, sediments, biomarkers)</i><br>"
        "🌡️ <b>Modern:</b> NASA GISS (1880-2025); "
        "   <i>Method: Instrumental (thermometers, satellites)</i><br>"
        "⏱️ Time Span: 540 Ma to 2100 CE<br>"
        "📏 Baseline: Pre-industrial (1850-1900)<br>"
        "<br>"
#        "ℹ️ <b>Overlapping curves show method differences</b> "
#        "   Scientific uncertainty is normal and expected!<br>"
#        "<br>"
        "💡 <b>Proxy Handoffs:</b> Each dataset ends where higher-resolution methods begin<br>"
#        "<br>"

#        "• Phanerozoic 'double hump' (540 Ma)<br>"
#        "• Mesozoic greenhouse (252-66 Ma)<br>"
#        "• Ice age cycles (last 2.6 Ma)<br>"
#        "• Holocene stability (last 12,000 years)<br>"
#        "<br>"
        "💡 <b>Key Insight:</b> The Holocene's stable climate "
        "enabled human civilization to flourish.<br>"
        "🔍 <b>Use zoom to explore details!</b>"
    )    

    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.25, y=0.95,
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
        title_text="Millions of Years Before Present (Ma, logarithmic scale)",
        autorange=False,
        range=[np.log10(540), np.log10(0.000001)],  # 540 Ma to ~present
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
            'text': "Earth's Climate History: 540 Million Years to 2100 CE (Phanerozoic Eon)<br><sub>From Cambrian Explosion to Present</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        hovermode='closest',
        showlegend=True,
        legend=dict(
            x=0.94,
            y=0.00,
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
        text="Data: Scotese et al. (2021) Phanerozoic | Lisiecki & Raymo (2005) LR04 | Kaufman et al. (2020) Holocene | Alley (2000) GISP2 Ice Core (YD) | NASA GISS | Paloma's Orrery",
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
        save_plot(fig, "paleoclimate_540Ma_to_present")        
        print("Opening in browser...")
        fig.show()
    else:
        print("✗ Could not create visualization - check if data is cached")
        print(f"Expected data file: {LR04_CACHE}")

if __name__ == '__main__':
    main()
