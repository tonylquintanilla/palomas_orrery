"""
Earth System Visualization GUI for Paloma's Orrery
Hub window with climate data visualizations

Data Preservation is Climate Action
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import json
import os
import threading
import queue
import numpy as np

# Try to import Plotly
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

from paleoclimate_visualization import create_paleoclimate_visualization
from paleoclimate_dual_scale import create_paleoclimate_dual_scale_visualization
from paleoclimate_visualization_full import create_paleoclimate_visualization as create_phanerozoic_viz
from paleoclimate_human_origins_full import create_paleoclimate_visualization as create_human_origins_viz
from energy_imbalance import create_energy_imbalance_visualization
from save_utils import save_plot

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False    

# Data files

CO2_DATA_FILE = 'data/co2_mauna_loa_monthly.json'
TEMP_DATA_FILE = 'data/temperature_giss_monthly.json'
ICE_DATA_FILE = 'data/arctic_ice_extent_monthly.json'  # Updated filename

def load_co2_data():
    """Load Mauna Loa CO2 data from cache"""
    try:
        with open(CO2_DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def load_temperature_data():
    """Load NASA GISS temperature data from cache"""
    try:
        with open(TEMP_DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def load_ice_data():
    """Load Arctic sea ice extent data from cache"""
    try:
        with open(ICE_DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def create_keeling_curve():
    """Create interactive Keeling Curve visualization"""
    data = load_co2_data()
    if not data:
        return None
    
    records = data['data']
    metadata = data['metadata']
    
    # Extract data
    dates = [r['decimal_date'] for r in records]
    co2_values = [r['co2_ppm'] for r in records]
    
    # Create figure
    fig = go.Figure()
    
    # Add main CO2 trend line
    fig.add_trace(go.Scatter(
        x=dates,
        y=co2_values,
        mode='lines',
        name='Atmospheric CO2',
        line=dict(color='#2E86AB', width=2),
        hovertemplate='Date: %{x:.2f}<br>CO2: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Add current value marker
    latest = records[-1]
    fig.add_trace(go.Scatter(
        x=[latest['decimal_date']],
        y=[latest['co2_ppm']],
        mode='markers',
        name='Current',
        marker=dict(color='#C1121F', size=10, symbol='diamond'),
        hovertemplate=f"Current: {latest['co2_ppm']:.2f} ppm<extra></extra>"
    ))
    
    # Add reference lines
    fig.add_hline(y=350, line_dash="dash", line_color="green", 
                  annotation_text="Pre-industrial safe zone (~350 ppm)",
                  annotation_position="left")
    fig.add_hline(y=450, line_dash="dash", line_color="orange",
                  annotation_text="Danger threshold (>450 ppm)",
                  annotation_position="left")
    
    # Calculate statistics
    first_record = records[0]
    years = latest['year'] - first_record['year']
    increase = latest['co2_ppm'] - first_record['co2_ppm']
    rate = increase / years
    
    # Add info box
    info_text = (
        f"<b>The Keeling Curve</b><br>"
        f"Current: {latest['co2_ppm']:.2f} ppm<br>"
        f"Start ({first_record['year']}): {first_record['co2_ppm']:.2f} ppm<br>"
        f"{years}-year increase: +{increase:.2f} ppm<br>"
        f"Rate: +{rate:.2f} ppm/year"
    )
    
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.02, y=0.98,
        xanchor="left", yanchor="top",
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#2E86AB",
        borderwidth=2,
        borderpad=10,
        showarrow=False,
        font=dict(size=11)
    )
    
    # Add threat warning
    threat_text = (
        "Mauna Loa Observatory threatened with closure (Aug 2025)<br>"
        "Data preservation is climate action"
    )
    
    fig.add_annotation(
        text=threat_text,
        xref="paper", yref="paper",
        x=0.98, y=0.02,
        xanchor="right", yanchor="bottom",
        bgcolor="rgba(255,200,200,0.8)",
        bordercolor="#C1121F",
        borderwidth=2,
        borderpad=8,
        showarrow=False,
        font=dict(size=9, color="#C1121F")
    )
    
    # Layout
    fig.update_layout(
        title={
            'text': "The Keeling Curve: Atmospheric CO2 at Mauna Loa Observatory (1958-2025)",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#1a1a1a'}
        },
        xaxis_title="Year",
        yaxis_title="CO2 Concentration (ppm)",
        template="plotly_white",
        width=1200,
        height=700,
        hovermode='x unified',
        showlegend=True,
        legend=dict(x=0.02, y=0.5, bgcolor="rgba(255,255,255,0.8)")
    )
    
    # Add footer with source
    fig.add_annotation(
        text=f"Data Source: {metadata['source']['organization']} | <a href=\"{metadata['source']['url']}\">{metadata['source']['url']}</a>",
        xref="paper", yref="paper",
        x=0.5, y=-0.12,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='gray')
    )
    
    return fig

def create_temperature_viz():
    """Create interactive temperature anomaly visualization"""
    data = load_temperature_data()
    if not data:
        return None
    
    records = data['data']
    metadata = data['metadata']
    
    # Extract data - create decimal dates
    dates = [r['year'] + (r['month'] - 0.5) / 12 for r in records]
    anomalies = [r['anomaly_c'] for r in records]
    
    # Create figure
    fig = go.Figure()
    
    # Add temperature trend line
    fig.add_trace(go.Scatter(
        x=dates,
        y=anomalies,
        mode='lines',
        name='Temperature Anomaly',
        line=dict(color='#C1121F', width=2),
        hovertemplate='Date: %{x:.2f}<br>Anomaly: %{y:.2f}°C<extra></extra>'
    ))
    
    # Add current value marker
    latest = records[-1]
    latest_date = latest['year'] + (latest['month'] - 0.5) / 12
    fig.add_trace(go.Scatter(
        x=[latest_date],
        y=[latest['anomaly_c']],
        mode='markers',
        name='Current',
        marker=dict(color='#8B0000', size=10, symbol='diamond'),
        hovertemplate=f"Current: +{latest['anomaly_c']:.2f}°C<extra></extra>"
    ))
    
    # Add baseline and reference lines
    fig.add_hline(y=0, line_dash="solid", line_color="gray", line_width=2,
                  annotation_text="1951-1980 baseline",
                  annotation_position="top right")
            #      annotation=dict(yshift=-10, xshift=5))
    
    fig.add_hline(y=-0.3, line_dash="dot", line_color="green", line_width=1,
                  annotation_text="Pre-industrial (~1850-1900)",
                  annotation_position="top right")
            #      annotation=dict(yshift=-10, xshift=5))
    
    fig.add_hline(y=1.5, line_dash="dash", line_color="orange",
                  annotation_text="Paris Agreement 1.5°C target",
                  annotation_position="top right")
    
    fig.add_hline(y=2.0, line_dash="dash", line_color="red",
                  annotation_text="Paris Agreement 2.0°C limit",
                  annotation_position="top right")
    
    # Calculate statistics
    first_record = records[0]
    years = latest['year'] - first_record['year']
    warming = latest['anomaly_c'] - first_record['anomaly_c']
    vs_preindustrial = latest['anomaly_c'] + 0.3
    progress_15 = (vs_preindustrial / 1.5) * 100
    progress_20 = (vs_preindustrial / 2.0) * 100
    
    # Add info box
    info_text = (
        f"<b>Global Temperature</b><br>"
        f"Current: +{latest['anomaly_c']:.2f}°C<br>"
        f"vs Pre-industrial: +{vs_preindustrial:.2f}°C<br>"
        f"{years}-yr warming: +{warming:.2f}°C<br>"
        f"Progress to 1.5°C: {progress_15:.0f}%<br>"
        f"Progress to 2.0°C: {progress_20:.0f}%<br>"
        f"(Baseline: 1951-1980 avg)"
    )
    
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.25, y=0.45,
        xanchor="right", yanchor="bottom",
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#C1121F",
        borderwidth=2,
        borderpad=10,
        showarrow=False,
        font=dict(size=11)
    )
    
    # Add threat warning
    threat_text = (
        "NASA GISS faces 52% budget cuts & institutional uncertainty<br>"
        "James Hansen's 145-year legacy dataset at risk"
    )
    
    fig.add_annotation(
        text=threat_text,
        xref="paper", yref="paper",
        x=0.70, y=0.02,
        xanchor="left", yanchor="bottom",
        bgcolor="rgba(255,200,200,0.8)",
        bordercolor="#C1121F",
        borderwidth=2,
        borderpad=8,
        showarrow=False,
        font=dict(size=9, color="#C1121F")
    )
    
    # Layout
    fig.update_layout(
        title={
            'text': "Global Mean Surface Temperature Anomaly (1880-2025)<br><sub>1951-1980 baseline is ~0.3°C warmer than pre-industrial (1850-1900). Aerosol masking effect visible 1950-1980. Data updates monthly with 1-2 month lag for quality control.</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14, 'color': '#1a1a1a'}
        },
        xaxis_title="Year (decimal notation: 2024.96 = late December)",
        yaxis_title="Temperature Anomaly (°C)",
        template="plotly_white",
        width=1200,
        height=700,
        hovermode='x unified',
        showlegend=True,
        legend=dict(x=0.50, y=0.70, bgcolor="rgba(255,255,255,0.8)"),
        margin=dict(t=120, b=120)
    )
    
    # Add footer with source
    fig.add_annotation(
        text=f"Data Source: {metadata['source']['organization']} | <a href=\"{metadata['source']['url']}\">{metadata['source']['url']}</a> | {metadata['source']['citation']}",
        xref="paper", yref="paper",
        x=0.5, y=-0.15,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='gray')
    )
    
    return fig

# Add these two functions after create_temperature_viz() in earth_system_visualization_gui.py

def create_monthly_temperature_lines():
    """
    Create year-over-year monthly temperature visualization (line chart).
    Shows all years from 1880-2025 with color spectrum.
    """
    # Load data
    data = load_temperature_data()
    
    if not data:
        return None
    
    records = data['data']
    metadata = data['metadata']
    
    # Organize data by year and month
    years_data = {}
    for r in records:
        year = r['year']
        month = r['month']
        if year not in years_data:
            years_data[year] = {}
        years_data[year][month] = r['anomaly_c']
    
    # All years
    all_years = sorted(years_data.keys())
    selected_years = all_years  # Show all years
    
    # Create figure
    fig = go.Figure()
    
    # Generate color spectrum from blue (cold) to red (hot)
    import colorsys
    n_years = len(all_years)
    
    def get_temperature_color(index, total):
        """Generate color from blue (cold) through green/yellow to red (hot)."""
        hue = 240 - (index / total * 240)  # 240° (blue) to 0° (red)
        hue = hue / 360.0
        saturation = 0.85
        value = 0.9
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        return f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})'
    
    # Add traces for each year
    for i, year in enumerate(selected_years):
        months = list(range(1, 13))
        anomalies = [years_data[year].get(m, None) for m in months]
        
        year_index = all_years.index(year)
        color = get_temperature_color(year_index, n_years)
        
        # Check if partial year
        has_data = [a for a in anomalies if a is not None]
        is_partial = len(has_data) < 12
        
        fig.add_trace(go.Scatter(
            x=months,
            y=anomalies,
            mode='lines',
            name=f'{year}' + (' (partial)' if is_partial else ''),
            line=dict(color=color, width=2, dash='dot' if is_partial else 'solid'),
            opacity=1.0,
            showlegend=True,
            hovertemplate='<b>Year:</b> %{fullData.name}<br>' +
                          '<b>Month:</b> %{x}<br>' +
                          '<b>Anomaly:</b> %{y:.2f}°C<br>' +
                          '<extra></extra>'
        ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text="Monthly Temperature Anomalies: Historical Context (1880-2025)<br>" +
                 "<sub>Color spectrum: Blue (cooler) †’ Red (warmer) showing warming trend over time</sub><br>" +
                 f"<sub>Data Source: {metadata['source']['organization']} | Baseline: 1951-1980</sub>",
            x=0.5,
            xanchor='center',
            font=dict(size=16)
        ),
        xaxis=dict(
            title="Month",
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        yaxis=dict(
            title="Temperature Anomaly (°C)",
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)'
        ),
        hovermode='closest',
        legend=dict(
            x=1.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='black',
            borderwidth=1,
            font=dict(size=9),
            yanchor='top',
            xanchor='left',
            traceorder='reversed'
        ),
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        width=1450,
        height=700,
        margin=dict(r=200, l=80, t=120, b=80)
    )
    
    # Add zero line
    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="black",
        opacity=1.0,
        annotation_text="1951-1980 baseline",
        annotation_position="top left"
    )
    
    return fig


def create_warming_stripes():
    """
    Create Ed Hawkins style warming stripes visualization (heatmap).
    Shows all years 1880-2025.
    """
    # Load data
    data = load_temperature_data()
    
    if not data:
        return None
    
    records = data['data']
    metadata = data['metadata']
    
    # Organize data by year and month
    years_data = {}
    for r in records:
        year = r['year']
        month = r['month']
        if year not in years_data:
            years_data[year] = [None] * 12
        years_data[year][month - 1] = r['anomaly_c']
    
    # All years
    start_year = min(years_data.keys())
    end_year = max(years_data.keys())
    years = list(range(start_year, end_year + 1))
    
    # Build matrix
    z_data = []
    year_labels = []
    
    for year in years:
        if year in years_data:
            z_data.append(years_data[year])
            year_labels.append(str(year))
    
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        x=month_labels,
        y=year_labels,
        colorscale='RdBu_r',  # Red-Blue reversed (red = hot)
        zmid=0,
        colorbar=dict(
            title="Anomaly (°C)",
            titleside="right",
            tickmode="linear",
            tick0=-1,
            dtick=0.5
        ),
        zmin=-1.0,
        zmax=1.5,
        hovertemplate='<b>Year:</b> %{y}<br>' +
                      '<b>Month:</b> %{x}<br>' +
                      '<b>Anomaly:</b> %{z:.2f}°C<br>' +
                      '<extra></extra>'
    ))
    
    # Layout
    fig.update_layout(
        title=dict(
            text="Warming Stripes: Monthly Temperature Anomalies (1880-2025)<br>" +
                 "<sub>Inspired by #ShowYourStripes (Prof. Ed Hawkins, 2018)</sub><br>" +
                 f"<sub>Data Source: {metadata['source']['organization']} | " +
                 f"Baseline: 1951-1980 | Blue = Cool, Red = Hot</sub>",
            x=0.5,
            xanchor='center',
            font=dict(size=16)
        ),
        xaxis=dict(
            side='top'
        ),
        yaxis=dict(
            title="Year",
            autorange=True
        ),
        width=1200,
        height=1400,
        margin=dict(r=80, l=80, t=140, b=80)
    )
    
    return fig


# Add these handler functions after open_temperature_viz()

def open_monthly_temp_lines():
    """Open the monthly temperature year-over-year line chart."""
    try:
        fig = create_monthly_temperature_lines()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found",
                "Temperature data file not found.\n"
                "Please run fetch_climate_data.py first.")
    except Exception as e:
        messagebox.showerror("Error", 
            f"Failed to create monthly temperature visualization:\n{str(e)}")


def open_warming_stripes():
    """Open the Ed Hawkins warming stripes heatmap."""
    try:
        fig = create_warming_stripes()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found",
                "Temperature data file not found.\n"
                "Please run fetch_climate_data.py first.")
    except Exception as e:
        messagebox.showerror("Error",
            f"Failed to create warming stripes visualization:\n{str(e)}")


def create_ice_viz():
    """Create Arctic sea ice extent visualization - Updated with correct data source"""
    data = load_ice_data()
    if not data:
        return None
    
    records = data['data']
    metadata = data['metadata']
    
    # Filter to September only (annual minimum)
    sept_records = [r for r in records if r['month'] == 9]
    
    # Extract September data
    years = [r['year'] for r in sept_records]
    extents = [r['extent_million_km2'] for r in sept_records]
    
    # Calculate trend line
    z = np.polyfit(years, extents, 1)
    p = np.poly1d(z)
    trend_line = p(years)
    
    # Calculate statistics
    first_extent = extents[0]
    latest_extent = extents[-1]
    min_extent = min(extents)
    min_year = years[extents.index(min_extent)]
    decline = first_extent - latest_extent
    pct_decline = (decline / first_extent) * 100
    
    # Create figure
    fig = go.Figure()
    
    # Add actual September data
    fig.add_trace(go.Scatter(
        x=years,
        y=extents,
        mode='lines+markers',
        name='September Minimum',
        line=dict(color='#00B4D8', width=2),
        marker=dict(size=6, color='#00B4D8'),
        hovertemplate='<b>%{x}</b><br>Extent: %{y:.2f} million km²<extra></extra>'
    ))
    
    # Add trend line
    fig.add_trace(go.Scatter(
        x=years,
        y=trend_line,
        mode='lines',
        name='Trend',
        line=dict(color='#03045E', width=2, dash='dash'),
        hovertemplate='Trend: %{y:.2f} million km²<extra></extra>'
    ))
    
    # Add 2012 record low annotation
    fig.add_annotation(
        x=2012,
        y=min_extent,
        text=f"Record Low: {min_extent:.2f}M km²<br>September 2012",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='#03045E',
        ax=40,
        ay=-40,
        bgcolor='white',
        bordercolor='#03045E',
        borderwidth=2,
        font=dict(size=11, color='#03045E')
    )
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Arctic Sea Ice Extent - September Minimum<br><sub>Satellite Era (1979-2025) | Full monthly data available, September shown</sub>',
            font=dict(size=18, color='#03045E', family='Arial')
        ),
        xaxis=dict(
            title='Year',
            gridcolor='lightgray',
            showgrid=True
        ),
        yaxis=dict(
            title='Sea Ice Extent (million km²)',
            gridcolor='lightgray',
            showgrid=True
        ),
        plot_bgcolor='#E8F4F8',
        paper_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.35,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#03045E',
            borderwidth=1
        ),
        width=1200,
        height=700,
        margin=dict(r=50, t=100, b=150, l=80)
    )
    
    # Add info box - top right
    info_text = (
        f"<b>September Minimum</b><br>"
        f"(Annual low point)<br><br>"
        f"<b>2025:</b> {latest_extent:.2f} million km²<br>"
        f"<b>1979:</b> {first_extent:.2f} million km²<br>"
        f"<b>Decline:</b> -{decline:.2f} million km² ({pct_decline:.1f}%)<br>"
        f"<b>Trend:</b> -12.1% per decade<br><br>"
        f"<i>Dataset contains all 12 months<br>"
        f"(561 records total)</i>"
    )
    
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.98, y=0.98,
        xanchor='right', yanchor='top',
        showarrow=False,
        bgcolor='rgba(255,255,255,0.95)',
        bordercolor='#00B4D8',
        borderwidth=2,
        borderpad=10,
        font=dict(size=10, color='#03045E')
    )
    
    # Add data source note - top left (UPDATED - crisis resolved!)
    source_note = (
        "<b>✅ Automated Data Retrieval Working</b><br>"
        "- NSIDC V4.0 Excel format (Oct 2024)<br>"
        "- Migrated from V3 CSV to V4 XLSX<br>"
        "- FTP deprecated HTTPS active<br>"
        "- Full monthly data (1979-2025)"
    )
    
    fig.add_annotation(
        text=source_note,
        xref="paper", yref="paper",
        x=0.02, y=0.20,
        xanchor='left', yanchor='top',
        showarrow=False,
        bgcolor='rgba(200,255,200,0.95)',
        bordercolor='#4CAF50',
        borderwidth=2,
        borderpad=10,
        font=dict(size=9, color='#1B5E20')
    )
    
    # Add comprehensive source information at bottom
    source_url = metadata['source'].get('data_url', metadata['source']['url'])
    citation = metadata['source'].get('citation', 'NSIDC Sea Ice Index, Version 4')
    
    source_text = (
        f"<b>Data Source:</b> {metadata['source']['organization']}<br>"
        f"<b>Primary URL:</b> <a href='{metadata['source']['url']}'>{metadata['source']['url']}</a><br>"
        f"<b>Data File:</b> <a href='{source_url}'>Sea_Ice_Index_Monthly_Data_by_Year_G02135_v4.0.xlsx</a><br>"
        f"<b>Citation:</b> {citation}<br>"
        f"<b>Format:</b> Excel (XLSX) parsed with openpyxl | <b>Sheet:</b> NH-Extent | <b>Records:</b> {len(records)} monthly values (1979-2025)<br>"
        f"<b>Note:</b> September minimum represents annual low point. March maximum typically 15-16 million km²."
    )
    
    fig.add_annotation(
        text=source_text,
        xref="paper", yref="paper",
        x=0.5, y=-0.10,
        xanchor="center", yanchor="top",
        showarrow=False,
        align='left',
        bgcolor='rgba(255,255,255,0.95)',
        bordercolor='#666',
        borderwidth=1,
        borderpad=8,
        font=dict(size=8, color='#333')
    )
    
    return fig

# Add these functions to earth_system_visualization_gui.py

def load_sea_level_data():
    """Load sea level data from cached JSON file"""
    try:
#        with open('sea_level_gmsl_monthly.json', 'r') as f:
        with open('data/sea_level_gmsl_monthly.json', 'r') as f:    
            data = json.load(f)
            return data['data'], data['metadata']
    except FileNotFoundError:
        print("Sea level data file not found. Run fetch_climate_data.py first.")
        return None, None
    except Exception as e:
        print(f"Error loading sea level data: {e}")
        return None, None

def create_sea_level_viz():
    """Create interactive sea level rise visualization"""
    records, metadata = load_sea_level_data()
    
    if not records:
        return None
    
    # Extract data  
    dates = [f"{r['year']}-{r['month']:02d}-01" for r in records]
    
    # Data is already in centimeters
    sea_level_cm = [r['gmsl_smoothed_cm'] for r in records]
    
    # Get latest values
    latest_date = dates[-1]
    latest_cm = sea_level_cm[-1]
    
    # Calculate statistics
    # Convert cm to mm (data comes in as gmsl_smoothed_cm)
    sea_level_mm = [r['gmsl_smoothed_cm'] * 10 for r in records]  # œ… Convert cm to mm
    first_mm = sea_level_mm[0]
    latest_mm = sea_level_mm[-1]
    first_year = records[0]['year']
    latest_year = records[-1]['year']
    years_span = latest_year - first_year
    total_rise_mm = latest_mm - first_mm
    total_rise_cm = total_rise_mm / 10
    rate_mm_per_year = total_rise_mm / years_span
    
    # Create figure
    fig = go.Figure()
    
    # Main sea level line
    fig.add_trace(go.Scatter(
        x=dates,
        y=sea_level_cm,
        mode='lines',
        name='Global Mean Sea Level',
        line=dict(color='#006994', width=2),
        hovertemplate='<b>%{x}</b><br>Sea Level: %{y:.2f} cm<extra></extra>'
    ))
    
    # Add current value marker
    fig.add_trace(go.Scatter(
        x=[latest_date],
        y=[latest_cm],
        mode='markers',
        name='Current Level',
        marker=dict(
            size=12,
            color='#E63946',
            symbol='diamond',
            line=dict(color='white', width=2)
        ),
        hovertemplate=f'<b>Current</b><br>{latest_date}<br>{latest_cm:.2f} cm<extra></extra>'
    ))
    
    # Add baseline (zero line for 1993)
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color="gray",
        annotation_text="1993 baseline (zero mean)",
        annotation_position="bottom right",
        annotation=dict(font_size=10, font_color="gray")
    )
        
    # Add trend line
    try:
        from scipy import stats
        import numpy as np
        
        # Simple linear regression
        x_numeric = np.arange(len(sea_level_cm))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_numeric, sea_level_cm)
        trend_line = slope * x_numeric + intercept
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=trend_line,
            mode='lines',
            name='Trend',
            line=dict(color='rgba(230, 57, 70, 0.5)', width=2, dash='dash'),
            hoverinfo='skip'
        ))
    except ImportError:
        print("scipy not available - trend line skipped")

    # Layout
    fig.update_layout(
        title={
            'text': 'Global Mean Sea Level Rise<br><sub>NASA-SSH Satellite Altimetry (60-day smoothed)</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#006994', 'family': 'Arial Black'}
        },
        xaxis_title='Year',
        yaxis_title='Sea Level Change (cm)',
        hovermode='x unified',
        template='plotly_white',
        height=700,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.30,
            bgcolor="rgba(255, 255, 255, 0.8)"
        )
    )
    
    # Add info box
    info_text = (
        f"<b>Current Status ({latest_year})</b><br>"
        f"Sea Level: <b>+{latest_cm:.2f} cm</b> ({latest_mm:.1f} mm)<br>"
        f"<br>"
        f"<b>Since {first_year} ({years_span} years)</b><br>"
        f"Total Rise: <b>+{total_rise_cm:.2f} cm</b> ({total_rise_mm:.1f} mm)<br>"
        f"Rate: <b>{rate_mm_per_year:.2f} mm/year</b><br>"
        f"<br>"
        f"<b>Threat Warning</b><br>"
        f"NASA Earth Science missions<br>"
        f"face budget uncertainty<br>"
        f"<br>"
        f"<b>Impact</b><br>"
        f"- Coastal flooding increasing<br>"
        f"- Storm surge amplification<br>"
        f"- Saltwater intrusion<br>"
        f"- Island nations at risk<br>"
        f"<br>"
        f"<i>Data: NASA Earth Indicators</i><br>"
        f"<i>32-year satellite record</i><br>"
        f"<a href='https://science.nasa.gov/earth/explore/earth-indicators/sea-leve/'>NASA Sea Level Data</a><br>"
        f"(download requires registration)"
    )

       
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.02, y=0.98,
        xanchor='left', yanchor='top',
        showarrow=False,
        font=dict(size=11, color='#333'),
        align='left',
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='#006994',
        borderwidth=2,
        borderpad=10
    )
    
    return fig

def load_ph_data():
    """Load ocean pH data from JSON cache"""
    try:
#        with open('ocean_ph_hot_monthly.json', 'r') as f:
        with open('data/ocean_ph_hot_monthly.json', 'r') as f:    
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("Error: pH data file is corrupted")
        return None

def create_ph_viz():
    """Create interactive ocean acidification (pH) visualization"""
    data = load_ph_data()
    if not data:
        return None
    
    records = data['records']
    metadata = data['metadata']
    
    if not records:
        return None
    
    # Extract data for plotting
    dates = [f"{r['year']}-{r['month']:02d}-01" for r in records]
    ph_values = [r['ph_total'] for r in records]
    years = [r['year'] for r in records]
    
    # Create figure
    fig = go.Figure()
    
    # Add pH measurements
    fig.add_trace(go.Scatter(
        x=dates,
        y=ph_values,
        mode='lines+markers',
        name='Measured pH',
        line=dict(color='#0077BE', width=2),
        marker=dict(size=4, color='#0077BE'),
        hovertemplate='<b>Date:</b> %{x}<br>' +
                      '<b>pH:</b> %{y:.4f}<br>' +
                      '<extra></extra>'
    ))
    
    # Add trend line using scipy
    if SCIPY_AVAILABLE:
        x_numeric = list(range(len(ph_values)))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_numeric, ph_values)
        trend_line = [slope * x + intercept for x in x_numeric]
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=trend_line,
            mode='lines',
            name='Trend Line',
            line=dict(color='#C1121F', width=2, dash='dash'),
            hovertemplate='<b>Trend</b><br>' +
                          '<b>pH:</b> %{y:.4f}<br>' +
                          '<extra></extra>'
        ))
    
    # Add pre-industrial reference line
    pre_industrial_ph = metadata['context']['pre_industrial_ph']
    fig.add_hline(
        y=pre_industrial_ph,
        line=dict(color='#2E7D32', width=2, dash='dot'),
        annotation_text=f'Pre-industrial pH (~{pre_industrial_ph})',
        annotation_position='top left'
    )
    
    # Add baseline reference (first full year)
    first_ph = records[0]['ph_total']
    fig.add_hline(
        y=first_ph,
        line=dict(color='#2E44B2', width=1, dash='dot'),
        annotation_text=f'Baseline {records[0]["year"]} ({first_ph:.4f})',
        annotation_position='top left',
        annotation_font=dict(size=12, color="#2E44B2")
    )
    
    # Layout with REVERSED y-axis (more acidic goes down visually)
    fig.update_layout(
        title={
            'text': f"Ocean Acidification: Surface pH at {metadata['source']['station']}<br>" +
                    "<sub>Lower pH = More Acidic Ocean | Monthly Measurements 1988-2023</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#1a1a1a'}
        },
        xaxis_title="Year",
        yaxis_title="pH (total scale)",
        yaxis=dict(
            autorange='reversed',  # REVERSED: declining pH goes visually downward
            tickformat='.3f'
        ),
        template="plotly_white",
        width=1200,
        height=700,
        hovermode='x unified',
        showlegend=True,
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)")
    )
    
    # Calculate statistics for info box
    latest_record = records[-1]
    first_record = records[0]
    ph_decline = first_record['ph_total'] - latest_record['ph_total']  # Positive = decline
    years_span = latest_record['year'] - first_record['year']
    annual_rate = metadata['statistics']['annual_rate']
    
    # Add information box
    info_text = (
        f"<b>Latest Measurement</b><br>"
        f"Date: {latest_record['year']}-{latest_record['month']:02d}<br>"
        f"pH: <b>{latest_record['ph_total']:.4f}</b><br>"
        f"<br>"
        f"<b>Since {first_record['year']} ({years_span} years)</b><br>"
        f"pH Decline: <b>{ph_decline:.4f} units</b><br>"
        f"Rate: <b>{annual_rate:.5f} units/year</b><br>"
        f"<br>"
        f"<b>Context</b><br>"
        f"Pre-industrial pH: ~{pre_industrial_ph}<br>"
        f"Total decline since 1750: ~0.1 units<br>"
        f"<br>"
        f"<b>Impact</b><br>"
        f"- Coral reef stress & bleaching<br>"
        f"- Shellfish mortality (calcification)<br>"
        f"- Food web disruption<br>"
        f"- Ecosystem collapse risk<br>"
        f"<br>"
        f"<b>Understanding pH</b><br>"
        f"<i>pH scale: Lower = More acidic</i><br>"
        f"<i>Logarithmic: 0.1 drop = 30% †’ acidity</i><br>"
        f"<i>Fastest change in 300M years</i>"
    )
    
    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.80, y=0.02,
        xanchor="left", yanchor="bottom",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#0077BE",
        borderwidth=2,
        borderpad=10,
        showarrow=False,
        font=dict(size=10),
        align='left'
    )
    
    # Add threat warning
    threat_text = (
        "Ocean chemistry changing<br>"
        "faster than any time in<br>"
        "300 million years"
    )
    
    fig.add_annotation(
        text=threat_text,
        xref="paper", yref="paper",
        x=0.40, y=0.98,
        xanchor="right", yanchor="top",
        bgcolor="rgba(255,200,200,0.8)",
        bordercolor="#C1121F",
        borderwidth=2,
        borderpad=8,
        showarrow=False,
        font=dict(size=9, color="#C1121F"),
        align='left'
    )
    
    # Add footer with source
    fig.add_annotation(
        text=f"Data Source: {metadata['source']['organization']} | <a href=\"{metadata['source']['url']}\">{metadata['source']['url']}</a>",
        xref="paper", yref="paper",
        x=0.5, y=-0.12,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='gray')
    )
    
    return fig

def create_planetary_boundaries_viz():
    """
    Planetary Boundaries - keep Tony's style & notes
    - Split wedges: Climate (RF/CO2), Biosphere (Functional/Genetic), Biogeochemical (P/N), Freshwater (Green/Blue)
    - Polar-locked labels so titles align with wedges
    - Ocean Acidification normalized to 0.10 pH drop
    - Small wedge gaps; boundary ring at 1.0 and high-risk ring at 1.6
    """
    if not PLOTLY_AVAILABLE:
        return None

    # ---------- helpers ----------
    def _safe_latest(records, key):
        return records[-1].get(key, None) if records else None

    def _normalize(val, boundary, clip=3.0):
        if val is None or boundary is None or boundary <= 0:
            return None
        return min(val / boundary, clip)

    def _color_for(norm):
        # same smooth mapping you used: green -> orange -> deep red
        if norm is None:
            return "#E8E8E8"
        if norm < 0.75:
            t = norm / 0.75
            return f"rgb({int(60+80*t)},{int(150+40*t)},{int(60-10*t)})"
        if norm < 1.0:
            t = (norm-0.75)/0.25
            return f"rgb({int(180+75*t)},{int(130+60*t)},{int(40-10*t)})"
        if norm < 1.6:
            t = (norm-1.0)/0.6
            return f"rgb(255,{int(190-120*t)},{int(30-30*t)})"
        return "rgb(220,50,40)"

    # ---------- live data for temp/pH/CO2 ----------
    temp_data = load_temperature_data()
    latest_temp_c = _safe_latest(temp_data['data'], 'anomaly_c') if temp_data and temp_data.get('data') else None

    ph_data = load_ph_data()
    latest_ph = _safe_latest(ph_data['records'], 'ph_total') if ph_data and ph_data.get('records') else None
    ph_drop = (8.2319 - latest_ph) if (latest_ph is not None) else None  # live decline vs ~8.2319 Feb 1991

    co2_data = load_co2_data() 
    latest_co2 = None
    if co2_data and co2_data.get('data'):
        latest_co2 = co2_data['data'][-1]['co2_ppm']    

    # ---------- SRC 2025 normalized values (boundary=1.0, high-riskÃ¢€°Ë†1.6) ----------
    SRC = {
        "CLIMATE_RF": 2.56,   # Radiative forcing
        "CLIMATE_CO2": 1.44,  # CO2 concentration
        "NOVEL": 1.80,
        "OZONE": 0.48,
        "AEROSOLS": 0.80,
        "OCEAN_ACID": 1.04,   # newly breached
        "FRESH_GREEN": 0.95,  # soil moisture / ET regimes
        "FRESH_BLUE": 1.16,   # surface/groundwater
        "LAND": 1.46,
        "BIO_FUNC": 2.00,     # functional diversity
        "BIO_GEN": 1.60,      # genetic diversity (Ã¢€°Ë†)
        "BIOGEO_P": 2.14,
        "BIOGEO_N": 2.82
    }

    # ---------- wedges in SRC clockwise order (top = Climate RF) ----------
    # IMPORTANT: climate wedges use src_value (value_raw=None) so they differ.
    boundaries = [
        dict(name="CLIMATE CHANGE",                     subtext="Radiative forcing",                    key="CLIMATE_RF",   value_raw=None,     boundary=1.0,   src_value=SRC["CLIMATE_RF"],    has_viz=False),
        dict(name="CLIMATE CHANGE",                     subtext="CO2 concentration",                    key="CLIMATE_CO2",  value_raw=None,     boundary=1.0,   src_value=SRC["CLIMATE_CO2"],   has_viz=False),
        dict(name="NOVEL ENTITIES",                     subtext="",                                     key="NOVEL",        value_raw=None,     boundary=1.0,   src_value=SRC["NOVEL"],         has_viz=False),
        dict(name="STRATOSPHERIC<br>OZONE DEPLETION",   subtext="",                                     key="OZONE",        value_raw=None,     boundary=1.0,   src_value=SRC["OZONE"],         has_viz=False),
        dict(name="ATMOSPHERIC AEROSOL<br>LOADING",     subtext="",                                     key="AEROSOLS",     value_raw=None,     boundary=1.0,   src_value=SRC["AEROSOLS"],      has_viz=False),
        dict(name="OCEAN<br>ACIDIFICATION",             subtext="",                                     key="OCEAN_ACID",   value_raw=None,     boundary=1.0,   src_value=SRC["OCEAN_ACID"],    has_viz=False),
        dict(name="FRESHWATER<br>CHANGE",               subtext="Green water (soil moisture)",          key="FRESH_GREEN",  value_raw=None,     boundary=1.0,   src_value=SRC["FRESH_GREEN"],   has_viz=False),
        dict(name="FRESHWATER<br>CHANGE",               subtext="Blue water (liquid)",                  key="FRESH_BLUE",   value_raw=None,     boundary=1.0,   src_value=SRC["FRESH_BLUE"],    has_viz=False),
        dict(name="LAND-SYSTEM<br>CHANGE",              subtext="",                                     key="LAND",         value_raw=None,     boundary=1.0,   src_value=SRC["LAND"],          has_viz=False),
        dict(name="BIOSPHERE INTEGRITY",                subtext="Functional",                           key="BIO_FUNC",     value_raw=None,     boundary=1.0,   src_value=SRC["BIO_FUNC"],      has_viz=False),
        dict(name="BIOSPHERE INTEGRITY",                subtext="Genetic",                              key="BIO_GEN",      value_raw=None,     boundary=1.0,   src_value=SRC["BIO_GEN"],       has_viz=False),
        dict(name="BIOGEOCHEMICAL<br>FLOWS",            subtext="Phosphorus",                           key="BIOGEO_P",     value_raw=None,     boundary=1.0,   src_value=SRC["BIOGEO_P"],      has_viz=False),
        dict(name="BIOGEOCHEMICAL<br>FLOWS",            subtext="Nitrogen",                             key="BIOGEO_N",     value_raw=None,     boundary=1.0,   src_value=SRC["BIOGEO_N"],      has_viz=False),
    ]

    # ---------- compute normalized radii ----------
    names, radii, colors, hovertext = [], [], [], []
    for b in boundaries:
        names.append(b["name"])
        if b["value_raw"] is not None:
            norm = _normalize(b["value_raw"], b["boundary"])
        else:
            norm = b["src_value"]
        radii.append(norm if norm is not None else 0.1)
        colors.append(_color_for(norm))

        # build hover text (keep your concise tone)
        zone = ("Safe operating space" if norm < 1.0 else
                "Increasing risk / zone of uncertainty" if norm < 1.6 else
                "High risk (transgressed)")
        live_note = ""
        if b["key"] == "OCEAN_ACID":
            if ph_drop is not None:
                live_note = f"<br>Live pH decline from Feb 1991: {ph_drop:.3f} "
                "(norm {min(ph_drop/0.10,3.0):.2f})"
            else:
                live_note = f"<br>SRC 2025: {SRC['OCEAN_ACID']:.2f}"
        elif b["key"] == "CLIMATE_CO2":
            if latest_co2 is not None:
                live_note = f"<br>Live CO2: {latest_co2:.1f} ppm (boundary: 350 ppm)"
            else:
                live_note = f"<br>SRC 2025: {SRC['CLIMATE_CO2']:.2f}"                
        hovertext.append(
            f"<b>{b['name'].replace('<br>', ' ')}</b><br>{b['subtext']}"
            f"<br>Normalized: {radii[-1]:.2f}<br>Status: {zone}{live_note}"
        )

    # ---------- figure ----------
    fig = go.Figure()

    # green safe-space core + rings (keeps your look)
    circle_theta = list(range(0, 361, 3))
    r_boundary = [1.0] * len(circle_theta)
    r_highrisk = [1.6] * len(circle_theta)

    fig.add_trace(go.Scatterpolar(
        r=r_boundary, theta=circle_theta, fill='toself',
        fillcolor='rgba(76,175,80,0.20)', line=dict(color='rgba(0,0,0,0)'),
        hoverinfo='skip', showlegend=False
    ))
    fig.add_trace(go.Scatterpolar(
        r=r_boundary, theta=circle_theta, mode='lines',
        line=dict(color='#4CAF50', width=2, dash='dash'),
        hoverinfo='skip', showlegend=False
    ))
    fig.add_trace(go.Scatterpolar(
        r=r_highrisk, theta=circle_theta, mode='lines',
        line=dict(color='#E53935', width=1, dash='dot'),
        hoverinfo='skip', showlegend=False
    ))

    # polar geometry €” centers + tiny gap so separators read cleanly
    N = len(boundaries)
    base_wedge_width = 360.0 / N
    theta_positions = [i * base_wedge_width for i in range(N)]
    wedge_widths = [base_wedge_width * 0.96] * N  # small gap, keeps your style

    # main wedge layer (your flat style; keep opacity)
    fig.add_trace(go.Barpolar(
        r=radii,
        theta=theta_positions,
        width=wedge_widths,
        marker_color=colors,
        marker_line_color=colors,
        marker_line_width=0,
        hovertext=hovertext,
        hovertemplate="%{hovertext}<extra></extra>",
        opacity=0.85,
        name="Planetary Boundaries"
    ))

    # layout (keep your orientation & page look)
    fig.update_layout(
        title=dict(
            text=("<b>Planetary Boundaries</b><br>"
                  "<sub>Stockholm Resilience Centre framework with live climate data integration</sub>"),
            x=0.5, xanchor="center", font=dict(size=20, family="Arial", color="#2C3E50")
        ),
        template="plotly_white",
        polar=dict(
            angularaxis=dict(
                showline=False, ticks="", showticklabels=False,
                direction="clockwise", rotation=90   # top = Climate RF
            ),
            radialaxis=dict(range=[0, 3.0], showline=False, ticks="", showticklabels=False, showgrid=False),
            bgcolor="white"
        ),
        showlegend=False,
        width=1200, height=1100,
        margin=dict(t=100, b=260, l=140, r=140),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    # ---------- POLAR-LOCKED LABELS (align with wedges; keep your text style) ----------
    label_r = [1.90] * N
#    label_theta = [th + base_wedge_width/2 for th in theta_positions]
    label_theta = theta_positions
    label_texts = []
    for b in boundaries:
        main = f"<b>{b['name']}</b>"
        sub = f"<br><span style='font-size:9px;color:#666'><i>{b['subtext']}</i></span>" if b['subtext'] else ""
        label_texts.append(main + sub)

    # small leader lines
    for ang in label_theta:
        fig.add_trace(go.Scatterpolar(
            r=[1.62, 1.84], theta=[ang, ang], mode="lines",
            line=dict(color="#999", width=1), hoverinfo="skip", showlegend=False
        ))

    fig.add_trace(go.Scatterpolar(
        r=label_r, theta=label_theta, mode="text",
        text=label_texts, hoverinfo="skip", showlegend=False,
        textfont=dict(size=10, color="#000", family="Arial")
    ))

    # center tag (your wording)
    fig.add_annotation(
        text="<b>Safe operating space</b>",
        xref="paper", yref="paper", x=0.5, y=0.60, showarrow=False,
        font=dict(size=12, color="#4CAF50"), bgcolor="rgba(255,255,255,0)", borderpad=10
    )

    # status box (keep your tone; show live temp & pH if present)
    live_count = sum(1 for b in boundaries if b['value_raw'] is not None)
    live_text = "<b>Planetary Health Check 2025</b><br><br>7/9 boundaries transgressed"
    if latest_temp_c is not None:
        live_text += f"<br>Temp anomaly (live): <b>{latest_temp_c:.3f}°C</b>"
    if ph_drop is not None:
        live_text += f"<br>Ocean pH decline (live): <b>{ph_drop:.3f}</b>"
#        "</b> (norm {min(ph_drop/0.10,3.0):.2f})"
#    live_text += f"<br><br>Live Data Integration: {live_count}/13"
    if latest_co2 is not None:
        live_text += f"<br>CO2 concentration (live): <b>{latest_co2:.1f} ppm</b>"

    fig.add_annotation(
        text=live_text,
        xref="paper", yref="paper",
        x=0.15, y=0.1, xanchor="left", yanchor="top",
        bgcolor="rgba(255,255,255,0.95)", bordercolor="#2196F3",
        borderwidth=2, borderpad=12, showarrow=False,
        font=dict(size=9), align="left"
    )

    # your legend box (keep style)
    legend_text = (
        "<b>Risk Zones:</b><br>"
        "- Safe operating space (green)<br>"
        "- Increasing risk (orange)<br>"
        "- High risk (red)<br>"
        "- No data (gray)<br>"
        "<br><b>Reference lines:</b><br>"
        "- Planetary Boundary<br>"
        "- High-risk Line"
    )
    fig.add_annotation(
        text=legend_text,
        xref="paper", yref="paper",
        x=0.94, y=1.10, xanchor="right", yanchor="top",
        bgcolor="rgba(255,255,255,0.95)", bordercolor="#999",
        borderwidth=1, borderpad=10, showarrow=False,
        font=dict(size=9), align="left"
    )

    # attribution / framework note (keep your long footer style)
    attribution_text = (
        "<b>Framework Attribution:</b><br>"
        "The 2025 update to the Planetary boundaries.<br>"
        "Licensed under <a href='https://creativecommons.org/licenses/by-nc-nd/3.0/'>CC BY-NC-ND 3.0</a>.<br>"
        "Credit: Azote for Stockholm Resilience Centre, based on analysis in Sakschewski and Caesar et al. 2025.<br>"
        "<b>Live data:</b> Temperature (NASA GISS), Ocean pH (HOT / BCO-DMO)."
    )
    fig.add_annotation(
        text=attribution_text,
        xref="paper", yref="paper",
        x=0.75, y=0.1, xanchor="center", yanchor="top",
        bgcolor="rgba(250,250,250,0.98)", bordercolor="#999",
        borderwidth=1, borderpad=12, showarrow=False,
        font=dict(size=8, color="#555"), align="left"
    )

    # educational callout (keep your box tone)
    fig.add_annotation(
        text=("Understanding Planetary Boundaries</b><br>"
              "Nine Earth-system processes regulate planetary stability. Transgressing<br>" 
              "these boundaries increases the risk of abrupt or irreversible<br>" 
              "environmental change. This visualization keeps the SRC design<br>" 
              "while linking to our live climate data for education and context."),
        xref="paper", yref="paper",
        x=0.06, y=1.10, xanchor="center", yanchor="top",
        bgcolor="rgba(255,252,240,0.95)", bordercolor="#F39C12",
        borderwidth=1, borderpad=10, showarrow=False,
        font=dict(size=9, color="#666"), align="center"
    )

    return fig



def open_ph_viz():
    """Open ocean pH visualization in browser"""
    try:
        fig = create_ph_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror(
                "Data Not Available",
                "Ocean pH data not found.\n\n"
                "Please download HOT data and run convert_hot_ph_to_json.py first."
            )
    except Exception as e:
        messagebox.showerror(
            "Visualization Error",
            f"Error creating pH visualization:\n\n{str(e)}"
        )

def open_planetary_boundaries():
    """Open Planetary Boundaries visualization in browser"""
    try:
        fig = create_planetary_boundaries_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror(
                "Visualization Error",
                "Could not create Planetary Boundaries visualization.\n\n"
                "Please ensure Plotly is installed."
            )
    except Exception as e:
        messagebox.showerror(
            "Visualization Error",
            f"Error creating Planetary Boundaries visualization:\n\n{str(e)}"
        )        


def open_paleoclimate_viz():
    """Open Cenozoic paleoclimate visualization"""
    try:
        fig = create_paleoclimate_visualization()
        if fig:
            fig.show()
            # Offer to save
            save_plot(fig, "paleoclimate_cenozoic_66Ma")
        else:
            messagebox.showerror(
                "Data Not Available",
                "Paleoclimate data not found. Please run fetch_paleoclimate_data.py first."
            )
    except Exception as e:
        messagebox.showerror("Visualization Error", f"Could not create visualization:\n{str(e)}")


def open_paleoclimate_dual_scale_viz():
    """Open dual-scale paleoclimate visualization (modern + deep time)"""
    try:
        fig = create_paleoclimate_dual_scale_visualization()
        if fig:
            fig.show()
            # Offer to save
            save_plot(fig, "paleoclimate_dual_scale")
        else:
            messagebox.showerror(
                "Data Not Available",
                "Paleoclimate data not found. Please run fetch_paleoclimate_data.py first."
            )
    except Exception as e:
        messagebox.showerror("Visualization Error", f"Could not create visualization:\n{str(e)}")        


def open_phanerozoic_viz():
    """Open Phanerozoic (540 Ma) paleoclimate visualization"""
    try:
        fig = create_phanerozoic_viz()
        if fig:
            fig.show()
            # Offer to save
            save_plot(fig, "paleoclimate_540Ma_to_present")
        else:
            messagebox.showerror(
                "Data Not Available",
                "Phanerozoic temperature data not found.\n\n"
                "Required files:\n"
                "• data/8c__Phanerozoic_Pole_to_Equator_Temperatures.csv\n"
                "• data/lr04_benthic_stack.json\n"
                "• data/temp12k_allmethods_percentiles.csv (optional)\n"
                "• data/temperature_giss_monthly.json (optional)"
            )
    except Exception as e:
        messagebox.showerror("Visualization Error", f"Could not create Phanerozoic visualization:\n{str(e)}")        

def open_human_origins_viz():
    """Open Paleoclimate + Human Origins visualization (540 Ma + 25 hominin species)"""
    try:
        fig = create_human_origins_viz()
        if fig:
            fig.show()
            # Save to output directory
            save_plot(fig, "paleoclimate_human_origins")
        else:
            messagebox.showerror(
                "Data Not Available",
                "Paleoclimate data not found.\n\n"
                "Please ensure the following files exist:\n"
                "• data/8c__Phanerozoic_Pole_to_Equator_Temperatures.csv\n"
                "• data/lr04_benthic_stack.json\n"
                "• data/temp12k_allmethods_percentiles.csv (optional)\n"
                "• data/temperature_giss_monthly.json (optional)"
            )
    except Exception as e:
        messagebox.showerror("Visualization Error", f"Could not create Human Origins visualization:\n{str(e)}")        

def open_sea_level_viz():
    """Open sea level visualization in browser"""
    try:
        fig = create_sea_level_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror(
                "Data Not Available",
                "Sea level data not found.\n\n"
                "Please run fetch_climate_data.py first to download the data."
            )
    except Exception as e:
        messagebox.showerror(
            "Visualization Error",
            f"Error creating sea level visualization:\n\n{str(e)}"
        )


def open_keeling_curve():
    """Open Keeling Curve in browser"""
    try:
        fig = create_keeling_curve()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found", 
                "CO2 data file not found. Please run fetch_climate_data.py first.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")

def open_temperature_viz():
    """Open temperature visualization in browser"""
    try:
        fig = create_temperature_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found",
                "Temperature data file not found. Please run fetch_climate_data.py first.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")

def open_ice_viz():
    """Open Arctic ice visualization in browser"""
    try:
        fig = create_ice_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found",
                "Arctic ice data file not found.\n\n"
                "The file data/arctic_ice_extent_monthly.json contains manually preserved data.\n"
                "Automated fetch failed due to NSIDC infrastructure issues.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")

def open_energy_imbalance():
    """Open energy imbalance visualization in browser"""
    try:
        fig = create_energy_imbalance_visualization()
        if fig:
            fig.show()
        else:
            messagebox.showerror("Data Not Found",
                "Required climate data not found. Please run fetch_climate_data.py first.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create visualization:\n{str(e)}")

def run_update_in_thread(update_button, status_label, window):
    """Run climate data update in background thread"""
    try:
        import climate_cache_manager
        from tkinter import messagebox
        
        # Show initial warning dialog with time estimate
        response = messagebox.askyesno(
            "Update Climate Data",
            "This will download the latest climate data from NASA, NOAA, and NSIDC.\n\n"
            "±ï¸ Expected time: ~30 seconds\n"
            "Datasets: CO2, Temperature, Arctic Ice\n\n"
            "Progress will be shown in the console window.\n\n"
            "Continue with update?",
            icon='question'
        )
        
        if not response:
            return  # User clicked No
        
        # Disable button during update
        update_button.config(state='disabled', text='Ã¢³ Updating...')
        status_label.config(text="Updating... (check console for progress)")
        
        def update_thread():
            # FIXED: Unpack all 3 return values
            success, message, details = climate_cache_manager.update_climate_data()
            
            # Re-enable button and show result (using window.after for thread safety)
            window.after(0, lambda: update_button.config(state='normal', text='ðŸ”„ Update Climate Data'))
            window.after(0, lambda: status_label.config(text=""))
            
            if success:
                # Show detailed success message
                detail_msg = message
                if details:
                    detail_msg += "\n\nDetails:\n"
                    for dataset, info in details.items():
                        if info.get('success'):
                            detail_msg += f"  œ… {dataset.upper()}: {info['records']} records\n"
                        else:
                            detail_msg += f"  Ã¢Å’ {dataset.upper()}: {info.get('error', 'Failed')}\n"
                
                window.after(0, lambda: messagebox.showinfo("œ… Update Complete", detail_msg))
            else:
                window.after(0, lambda: messagebox.showerror("Ã¢Å’ Update Failed", message))
        
        # Start thread
        thread = threading.Thread(target=update_thread, daemon=True)
        thread.start()
        
    except ImportError:
        messagebox.showwarning("Update Unavailable",
            "Climate cache manager not found.\n"
            "Run fetch_climate_data.py manually to update data.")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed:\n{str(e)}")
        update_button.config(state='normal', text='ðŸ”„ Update Climate Data')
        status_label.config(text="")

def open_earth_system_gui(parent=None):
    """
    Open Earth System Visualization hub window
    """
    if not PLOTLY_AVAILABLE:
        messagebox.showerror("Missing Dependency",
            "Plotly is required for visualizations.\n"
            "Install with: pip install plotly")
        return
    
    # Create window
    window = tk.Toplevel(parent) if parent else tk.Tk()
    window.title("🌍 Earth System Visualization")

    window.geometry("1200x900+150+0")  # Wider window for two columns "WIDTHxHEIGHT+X_POSITION+Y_POSITION"
    
    # Header
    header_frame = tk.Frame(window, bg='#2E86AB', height=80)
    header_frame.pack(fill='x')
    header_frame.pack_propagate(False)
    
    title_label = tk.Label(header_frame, 
                          text="Earth System Visualization",
                          font=('Arial', 18, 'bold'),
                          bg='#2E86AB',
                          fg='white')
    title_label.pack(pady=5)
    
    subtitle_label = tk.Label(header_frame,
                             text="Data Preservation is Climate Action",
                             font=('Arial', 10, 'italic'),
                             bg='#2E86AB',
                             fg='white')
    subtitle_label.pack()
    
    # Main content frame
    content_frame = tk.Frame(window, padx=20, pady=20)
    content_frame.pack(fill='both', expand=True)
    
    # Description
    desc_label = tk.Label(content_frame,
                         text="Select a visualization to explore Earth's changing systems.\n"
                         "Each chart shows critical data about our planet's health.",
                         font=('Arial', 10),
                         justify='left',
                         wraplength=550)
    desc_label.pack(anchor='w', pady=(0, 15))
    
    # Update Data button (prominent at top)
    update_frame = tk.Frame(content_frame, relief='solid', borderwidth=1, bg='#E8F5E9')
    update_frame.pack(fill='x', pady=(0, 10))
    
    update_button = tk.Button(update_frame,
                             text='Update Climate Data',
                             font=('Arial', 11, 'bold'),
                             bg='#4CAF50',
                             fg='white',
                             activebackground='#45a049',
                             cursor='hand2',
                             padx=20,
                             pady=10,
                             command=lambda: run_update_in_thread(update_button, status_label, window))
    update_button.pack(fill='x', padx=10, pady=10)
      
    
    update_desc = tk.Label(update_frame,
                        text="Click to download latest data from NASA and NOAA (CO2, Temperature, Arctic Ice)",
                        font=('Arial', 9),
                        bg='#E8F5E9',
                        fg='#555')
    update_desc.pack(pady=(0, 5))

    # Add sea level note
    sealevel_note = tk.Label(update_frame,
                            text="Sea Level: Manual update only (see climate_readme.md)",
                            font=('Arial', 8, 'italic'),
                            bg='#E8F5E9',
                            fg='#666')
#    sealevel_note.pack(pady=(0, 10))
    sealevel_note.pack(pady=(0, 5))

    status_label = tk.Label(update_frame,
                           text="",
                           font=('Arial', 9),
                           bg='#E8F5E9',
                           fg='#666')
    status_label.pack(pady=(0, 5))
    
    # Separator -- removed for cleaner layout
#    separator = tk.Frame(content_frame, height=2, bg='#ccc')
#    separator.pack(fill='x', pady=10)
    
    # Section label -- removed for cleaner layout
#    section_label = tk.Label(content_frame,
#                            text="Available Visualizations:",
#                            font=('Arial', 11, 'bold'),
#                            justify='left')
#    section_label.pack(anchor='w', pady=(5, 10))
    
    # Create frame for two-column layout
    buttons_frame = tk.Frame(content_frame)
    buttons_frame.pack(fill='both', expand=True)
    
    # Left column
    left_column = tk.Frame(buttons_frame)
    left_column.pack(side='left', fill='both', expand=True, padx=(0, 5))
    
    # Right column
    right_column = tk.Frame(buttons_frame)
    right_column.pack(side='left', fill='both', expand=True, padx=(5, 0))
    
    # LEFT COLUMN
    # Climate & Atmosphere section
    climate_label = tk.Label(left_column,
                            text="Climate & Atmosphere:",
                            font=('Arial', 10, 'bold'),
                            justify='left')
    climate_label.pack(anchor='w', pady=(5, 5))
    
    # Keeling Curve button
    keeling_button = tk.Button(left_column,
                              text='The Keeling Curve (Mauna Loa CO2)',
                              font=('Arial', 10),
                              bg='#2E86AB',
                              fg='white',
                              activebackground='#1a5f7a',
                              cursor='hand2',
                              padx=15,
                              pady=8,
                              command=open_keeling_curve)
    keeling_button.pack(fill='x', pady=2)
    
    # Temperature button
    temp_button = tk.Button(left_column,
                           text='Global Temperature Anomalies',
                           font=('Arial', 10),
                           bg='#C1121F',
                           fg='white',
                           activebackground='#8B0000',
                           cursor='hand2',
                           padx=15,
                           pady=8,
                           command=open_temperature_viz)
    temp_button.pack(fill='x', pady=(10, 2))
    
    # Monthly temperature progression button
    monthly_btn = tk.Button(left_column,
                           text='Monthly Temperature: Year-over-Year',
                           font=('Arial', 10),
                           bg='#E67E22',
                           fg='white',
                           activebackground='#CA6F1E',
                           cursor='hand2',
                           padx=15,
                           pady=8,
                           command=open_monthly_temp_lines)
    monthly_btn.pack(fill='x', pady=2)
    
    # Warming stripes button
    stripes_btn = tk.Button(left_column,
                           text='Warming Stripes (Ed Hawkins Style)',
                           font=('Arial', 10),
                           bg='#8E44AD',
                           fg='white',
                           activebackground='#7D3C98',
                           cursor='hand2',
                           padx=15,
                           pady=8,
                           command=open_warming_stripes)
    stripes_btn.pack(fill='x', pady=2)

    # Energy Imbalance button - the explainer showing mechanism
    energy_btn = tk.Button(left_column,
                        text='Energy Imbalance: The Climate Mechanism',
                        font=('Arial', 10),
                        bg='#FF8C00',
                        fg='white',
                        activebackground='#E07B00',
                        cursor='hand2',
                        padx=15,
                        pady=8,
                        command=open_energy_imbalance)
    energy_btn.pack(fill='x', pady=(10, 2))

    # Climate History and Projections section
    history_label = tk.Label(left_column,
                            text="Climate History and Projections:",
                            font=('Arial', 10, 'bold'),
                            justify='left')
    history_label.pack(anchor='w', pady=(10, 5))

    # Paleoclimate button
    paleo_btn = tk.Button(left_column,
                         text='Paleoclimate: Cenozoic Climate History',
                         font=('Arial', 10),
                         bg='#6B4423',
                         fg='white',
                         activebackground='#4A2F19',
                         cursor='hand2',
                         padx=15,
                         pady=8,
                         command=open_paleoclimate_viz)
    paleo_btn.pack(fill='x', pady=2)

    # Paleoclimate DUAL SCALE button
    paleo_dual_btn = tk.Button(left_column,
                         text='Paleoclimate: Dual Scale (Modern + Deep Time)',
                         font=('Arial', 10),
                         bg='#8B6914',
                         fg='white',
                         activebackground='#6B4F0F',
                         cursor='hand2',
                         padx=15,
                         pady=8,
                         command=open_paleoclimate_dual_scale_viz)
    paleo_dual_btn.pack(fill='x', pady=2)

    # Paleoclimate PHANEROZOIC button
    paleo_phan_btn = tk.Button(left_column,
                         text='Paleoclimate: Full History (540 Ma - Present)',
                         font=('Arial', 10),
                         bg='#003049',  # Dark blue to match Scotese curve color
                         fg='white',
                         activebackground='#001F2E',
                         cursor='hand2',
                         padx=15,
                         pady=8,
                         command=open_phanerozoic_viz)
    paleo_phan_btn.pack(fill='x', pady=2)

    # Paleoclimate HUMAN ORIGINS button
    human_origins_btn = tk.Button(right_column,
                         text='🧬 Human Origins (540 Ma + Evolution)',
                         font=('Arial', 10),
                         bg='#8B4513',  # Saddle brown - earthy/fossil color
                         fg='white',
                         activebackground='#A0522D',
                         cursor='hand2',
                         padx=15,
                         pady=8,
                         command=open_human_origins_viz)
    human_origins_btn.pack(fill='x', pady=2)

    # RIGHT COLUMN
    # Cryosphere section
    cryo_label = tk.Label(right_column,
                         text="Cryosphere:",
                         font=('Arial', 10, 'bold'),
                         justify='left')
    cryo_label.pack(anchor='w', pady=(5, 5))
    
    # Arctic Ice button
    ice_button = tk.Button(right_column,
                          text='Arctic Sea Ice Extent (September Minimum)',
                          font=('Arial', 10),
                          bg='#00B4D8',
                          fg='white',
                          activebackground='#0096C7',
                          cursor='hand2',
                          padx=15,
                          pady=8,
                          command=open_ice_viz)
    ice_button.pack(fill='x', pady=2)
    
    # Ocean Systems section
    ocean_label = tk.Label(right_column,
                          text="Ocean Systems:",
                          font=('Arial', 10, 'bold'),
                          justify='left')
    ocean_label.pack(anchor='w', pady=(10, 5))

    # Sea Level button
    sealevel_button = tk.Button(right_column,
                            text='Global Mean Sea Level Rise',
                            font=('Arial', 10),
                            bg='#006994',
                            fg='white',
                            activebackground='#004D6B',
                            cursor='hand2',
                            padx=15,
                            pady=8,
                            command=open_sea_level_viz)
    sealevel_button.pack(fill='x', pady=2)

    
    ph_button = tk.Button(right_column,
                        text='Ocean Acidification',
                        font=('Arial', 10),
                        bg='#0077BE',  # Ocean blue
                        fg='white',
                        activebackground='#005A8C',
                        cursor='hand2',
                        padx=15,
                        pady=8,
                        command=open_ph_viz)
    ph_button.pack(fill='x', pady=2) 

     # Earth System section (NEW!)
    earth_system_label = tk.Label(right_column,
                                  text="Earth System:",
                                  font=('Arial', 10, 'bold'),
                                  justify='left')
    earth_system_label.pack(anchor='w', pady=(10, 5))
    
    # Planetary Boundaries button (NEW!)
    pb_button = tk.Button(right_column,
                         text='Planetary Boundaries (SRC Framework)',
                         font=('Arial', 10),
                         bg='#27AE60',  # Earth green
                         fg='white',
                         activebackground='#229954',
                         cursor='hand2',
                         padx=15,
                         pady=8,
                         command=open_planetary_boundaries)
    pb_button.pack(fill='x', pady=2)   


    footer_label = tk.Label(content_frame,
                        text="10 of 10 visualizations active",  
                        font=('Arial', 9),
                        fg='#666',
                        justify='center')   
    footer_label.pack(side='bottom', pady=10)

    if not parent:
        window.mainloop()

if __name__ == '__main__':
    open_earth_system_gui()
