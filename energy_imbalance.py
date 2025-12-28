"""
Energy Imbalance Visualization for Paloma's Orrery
Modern era (2005-2025) temperature and energy imbalance

Shows the relationship between Earth's energy imbalance (cause) and 
temperature change (effect) - revealing climate inertia and committed warming.

Data Preservation is Climate Action
"""

import json
import os
import numpy as np
import pandas as pd

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Try to import save_utils, but don't fail if not available
try:
    from save_utils import save_plot
    SAVE_UTILS_AVAILABLE = True
except ImportError:
    SAVE_UTILS_AVAILABLE = False

# Data files
DATA_DIR = 'data'
GISS_TEMP_FILE = os.path.join(DATA_DIR, 'temperature_giss_monthly.json')
OHC_FILE = os.path.join(DATA_DIR, 'ohc2000m_levitus_climdash_seasonal.csv')

def load_ocean_heat_content():
    """
    Load NOAA ocean heat content data and convert to energy imbalance
    
    Returns:
        tuple: (decimal_years, ohc_anomaly_zj, imbalance_watts_per_m2)
    """
    try:
        # Load CSV (no header, format: YYYY-M,value)
        df = pd.read_csv(OHC_FILE, header=None, names=['date', 'ohc'])
        
        # Parse date
        df['year'] = df['date'].str.split('-').str[0].astype(int)
        df['month'] = df['date'].str.split('-').str[1].astype(int)
        df['decimal_year'] = df['year'] + (df['month'] - 1) / 12.0
        
        # OHC is in units of 10^22 Joules (Zettajoules)
        # Calculate rate of change for energy imbalance
        # Using gradient (centered difference)
        ohc_rate_zj_per_year = np.gradient(df['ohc'].values, df['decimal_year'].values)
        
        # Convert to W/m^2
        # 1 ZJ = 10^22 J
        # Earth surface area = 5.1 x 10^14 m^2
        # 1 year = 365.25 x 24 x 3600 seconds
        
        earth_surface_m2 = 5.1e14
        seconds_per_year = 365.25 * 24 * 3600
        zj_to_joules = 1e22
        
        watts = ohc_rate_zj_per_year * zj_to_joules / seconds_per_year
        imbalance_w_per_m2 = watts / earth_surface_m2
        
        return df['decimal_year'].values, df['ohc'].values, imbalance_w_per_m2
        
    except Exception as e:
        print(f"Warning: Could not load ocean heat content data: {e}")
        return None, None, None

def load_modern_temperature_data():
    """Load NASA GISS instrumental temperature data (1880-2025)"""
    try:
        with open(GISS_TEMP_FILE, 'r') as f:
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
                    years.pop()
        
        return np.array(years), np.array(temps)
        
    except Exception as e:
        print(f"Warning: Could not load modern temperature data: {e}")
        return None, None

def create_energy_imbalance_visualization():
    """
    Create energy imbalance visualization (2005-2025)
    
    Dual Y-axis plot showing:
    - Left: Temperature anomaly ( degC)
    - Right: Energy imbalance (W/m^2)
    
    Demonstrates the relationship between energy accumulation (cause)
    and temperature change (effect), revealing climate system inertia.
    """
    
    if not PLOTLY_AVAILABLE:
        return None
    
    # Load data
    years_temp, temp_anomaly = load_modern_temperature_data()
    years_ohc, ohc_zj, imbalance_w_m2 = load_ocean_heat_content()
    
    if years_ohc is None or years_temp is None:
        print("Could not load required data files")
        return None
    
    # Filter temperature data to OHC time range (2005-2025)
    temp_mask = (years_temp >= years_ohc.min()) & (years_temp <= years_ohc.max())
    years_temp_filtered = years_temp[temp_mask]
    temp_anomaly_filtered = temp_anomaly[temp_mask]
    
    # Create figure with dual y-axes
    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"secondary_y": True}]]
    )
    
    # Add ENSO event bands as background (plotted first so they appear behind data)
    # Each event includes characteristics explaining what made it unique
    enso_events = [
        {
            'start': 2006.5, 'end': 2007.2, 'type': 'El Nino',  # Back to original coordinates
            'color': 'rgba(255, 140, 0, 0.15)', 'label': '06/07 EN',
            'hover': '2006-07 El Nino: Moderate event. Followed 2005-06 La Nina. Brief but contributed to 2006 being 6th warmest year on record.'
        },
        {
            'start': 2007.5, 'end': 2008.2, 'type': 'La Nina', 
            'color': 'rgba(70, 130, 180, 0.15)', 'label': '07/08 LN',
            'hover': '2007-08 La Nina: Moderate event. Cooled global temperatures but 2008 still among top 10 warmest years - showing baseline warming trend.'
        },
        {
            'start': 2009.5, 'end': 2010.3, 'type': 'El Nino', 
            'color': 'rgba(255, 140, 0, 0.15)', 'label': '09/10 EN',
            'hover': '2009-10 El Nino: Moderate-Strong event. Made 2010 tied for warmest year on record (with 2005). Ended prolonged neutral/La Nina conditions.'
        },
        {
            'start': 2010.5, 'end': 2012.2, 'type': 'La Nina', 
            'color': 'rgba(70, 130, 180, 0.15)', 'label': '10/12 (L) LN',
            'hover': '2010-12 La Nina: LONG multi-year event (rare). Strong cooling yet 2010 still warmest on record. Demonstrates how much baseline warming has occurred.'
        },
        {
            'start': 2015.5, 'end': 2016.3, 'type': 'El Nino', 
            'color': 'rgba(255, 140, 0, 0.15)', 'label': '15/16 (S) EN',
            'hover': '2015-16 El Nino: SUPER event - one of strongest on record (with 1997-98, 1982-83). Made 2016 hottest year ever recorded. Massive global temperature spike.'
        },
        {
            'start': 2016.5, 'end': 2017.2, 'type': 'La Nina', 
            'color': 'rgba(70, 130, 180, 0.15)', 'label': '16/17 LN',
            'hover': '2016-17 La Nina: Brief weak event following super El Nino. Cooled temperatures but 2017 still 3rd warmest on record (behind 2016, 2015).'
        },
        # Skipping 2018/2019 Weak El Nino for clarity/space
        {
            'start': 2020.5, 'end': 2023.3, 'type': 'La Nina', 
            'color': 'rgba(70, 130, 180, 0.15)', 'label': '20/23 (3xL) LN',
            'hover': '2020-23 La Nina: UNPRECEDENTED triple-dip - 3 consecutive years (extremely rare). Despite strong cooling, 2020-2023 all in top 10 warmest years. Shows inexorable warming trend.'
        },
        {
            'start': 2023.5, 'end': 2024.3, 'type': 'El Nino', 
            'color': 'rgba(255, 140, 0, 0.15)', 'label': '23/24 EN',
            'hover': '2023-24 El Nino: Moderate-Strong event. Made 2023 hottest year on record by large margin, breaking 2016 record. Combined with long-term warming trend.'
        },
    ]
    
    # Store ENSO shapes to add to layout later (after all traces are added)
    enso_shapes = []
    enso_annotations = []
    
    # Debug: Print actual data range
    print(f"DEBUG: OHC data range: {years_ohc.min():.2f} to {years_ohc.max():.2f}", flush=True)
    
    # Base band filter on the plotted window instead of OHC-only bounds
    # This ensures all bands within the x-axis range display properly
    data_start = 2004.0  # Match x-axis range
    data_end = 2026.0    # Match x-axis range
    
    for event in enso_events:
        # Only add events that overlap with our plot window
        if event['end'] < data_start or event['start'] > data_end:
            print(f"DEBUG: Skipping {event['label']} ({event['start']}-{event['end']}) - outside plot window", flush=True)
            continue
        
        print(f"DEBUG: Adding {event['label']} ({event['start']}-{event['end']}) - {event['type']}", flush=True)
            
        # Add ENSO band as a filled scatter trace (bypasses shape rendering bug)
        fig.add_trace(
            go.Scatter(
                x=[event['start'], event['end'], event['end'], event['start'], event['start']],
                y=[0, 0, 1.5, 1.5, 0],  # Span full temperature range
                fill='toself',
                fillcolor=event['color'],
                line=dict(width=0),
                mode='none',
                showlegend=False,  # Don't clutter legend
                hoverinfo='skip'
            ),
            secondary_y=False  # Use primary y-axis (temperature scale)
        )
        # Add annotation for label at bottom (simplified) with hover info
        label_text = 'El Nino' if event['type'] == 'El Nino' else 'La Nina'
        enso_annotations.append(
            dict(
                x=(event['start'] + event['end']) / 2,  # Center of band
                y=0.02,  # Near bottom
                yref='paper',
                text=label_text,
                showarrow=False,
                font=dict(size=8, color='gray'),
                yanchor='bottom',
                hovertext=event['hover'],
                hoverlabel=dict(
                    bgcolor='white',
                    font_size=11,
                    font_family='Arial'
                )
            )
        )
    
    print(f"DEBUG: Total shapes created: {len(enso_shapes)}", flush=True)
    if len(enso_shapes) > 0:
        print(f"DEBUG: First shape: {enso_shapes[0]}", flush=True)
        print(f"DEBUG: Second shape: {enso_shapes[1] if len(enso_shapes) > 1 else 'N/A'}", flush=True)
    
    # CRITICAL DEBUG: Check if shapes are within visible x-range
    for i, shape in enumerate(enso_shapes):
        x0, x1 = shape['x0'], shape['x1']
        print(f"DEBUG: Shape {i}: x0={x0}, x1={x1}, color={shape['fillcolor']}, layer={shape['layer']}", flush=True)
    
    # Add temperature trace (left y-axis)
    fig.add_trace(
        go.Scatter(
            x=years_temp_filtered,
            y=temp_anomaly_filtered,
            mode='lines+markers',
            name='Air Temperature Anomaly (GMST)',  # Clarified
            line=dict(color='#DC143C', width=3),  # Crimson
            marker=dict(size=6, color='#DC143C'),
            hovertemplate='Year: %{x:.0f}<br>Air Temp: %{y:.2f} degC<extra></extra>',
            legendgroup='measurements',
            legendgrouptitle_text='Measurements'
        ),
        secondary_y=False
    )
    
    # Add shaded areas for energy imbalance (positive=red, negative=blue)
    # Properly segment at zero crossings - each continuous segment is separate
    
    # Find zero crossings and create segments
    segments_pos = []  # Positive segments (above zero)
    segments_neg = []  # Negative segments (below zero)
    
    current_segment_x = []
    current_segment_y = []
    is_positive = None
    
    for i, (x, y) in enumerate(zip(years_ohc, imbalance_w_m2)):
        current_positive = (y >= 0)
        
        # Handle zero crossings
        if is_positive is not None and current_positive != is_positive:
            # We crossed zero - interpolate the crossing point
            if len(current_segment_x) > 0:
                x_prev, y_prev = current_segment_x[-1], current_segment_y[-1]
                # Linear interpolation to find x where y=0
                if y_prev != y:  # Avoid division by zero
                    x_cross = x_prev + (0 - y_prev) * (x - x_prev) / (y - y_prev)
                    current_segment_x.append(x_cross)
                    current_segment_y.append(0)
                
                # Save completed segment
                if is_positive:
                    segments_pos.append((current_segment_x.copy(), current_segment_y.copy()))
                else:
                    segments_neg.append((current_segment_x.copy(), current_segment_y.copy()))
                
                # Start new segment at crossing point
                current_segment_x = [x_cross, x]
                current_segment_y = [0, y]
        else:
            current_segment_x.append(x)
            current_segment_y.append(y)
        
        is_positive = current_positive
    
    # Save final segment
    if len(current_segment_x) > 0:
        if is_positive:
            segments_pos.append((current_segment_x, current_segment_y))
        else:
            segments_neg.append((current_segment_x, current_segment_y))
    
    print(f"DEBUG: Created {len(segments_pos)} warming segments and {len(segments_neg)} cooling segments", flush=True)
    print(f"DEBUG: Total traces to be added: 5 (1 warming + 1 cooling + temp + imbalance + OHC) - CONSOLIDATED!", flush=True)
    
    # Plot positive segments (red warming) - CONSOLIDATED into single trace
    # Combine all warming segments into one trace to reduce trace count
    if segments_pos:
        all_warming_x = []
        all_warming_y = []
        
        for seg_x, seg_y in segments_pos:
            # Add the filled polygon for this segment
            all_warming_x.extend(seg_x)
            all_warming_x.extend(seg_x[::-1])
            all_warming_x.append(None)  # None creates a break between segments
            
            all_warming_y.extend(seg_y)
            all_warming_y.extend([0] * len(seg_y))
            all_warming_y.append(None)
        
        fig.add_trace(
            go.Scatter(
                x=all_warming_x,
                y=all_warming_y,
                fill='toself',
                fillcolor='rgba(255, 99, 71, 0.3)',  # Tomato red
                line=dict(width=0),
                mode='none',
                name='Ocean Warming',
                showlegend=True,
                hoverinfo='skip',
                legendgroup='ocean_heat',
                legendgrouptitle_text='Ocean Heat (0-2000m)'
            ),
            secondary_y=True
        )
    
    # Plot negative segments (blue cooling) - CONSOLIDATED into single trace
    # Combine all cooling segments into one trace to reduce trace count
    if segments_neg:
        all_cooling_x = []
        all_cooling_y = []
        
        for seg_x, seg_y in segments_neg:
            # Add the filled polygon for this segment
            all_cooling_x.extend(seg_x)
            all_cooling_x.extend(seg_x[::-1])
            all_cooling_x.append(None)  # None creates a break between segments
            
            all_cooling_y.extend([0] * len(seg_y))
            all_cooling_y.extend(seg_y[::-1])
            all_cooling_y.append(None)
        
        fig.add_trace(
            go.Scatter(
                x=all_cooling_x,
                y=all_cooling_y,
                fill='toself',
                fillcolor='rgba(70, 130, 180, 0.3)',  # Steel blue
                line=dict(width=0),
                mode='none',
                name='Ocean Cooling',
                showlegend=True,
                hoverinfo='skip',
                legendgroup='ocean_heat'
            ),
            secondary_y=True
        )
    
    # Add energy imbalance trace (right y-axis) - plot AFTER shading so line is on top
    fig.add_trace(
        go.Scatter(
            x=years_ohc,
            y=imbalance_w_m2,
            mode='lines+markers',
            name='Energy Imbalance (from ocean heat uptake)',
            line=dict(color='#FF8C00', width=3),  # Dark orange
            marker=dict(size=5, color='#FF8C00'),
            hovertemplate='Year: %{x:.1f}<br>Imbalance: %{y:.2f} W/m^2<extra></extra>',
            legendgroup='measurements'
        ),
        secondary_y=True
    )
    
    # Add cumulative integral (Ocean Heat Content) using secondary_y for reliability
    # This shows the running sum: integral of imbalance over time
    # CRITICAL: Shows ongoing energy accumulation driving temperature rise
    # Uses 2000m ocean data (centennial-millennial timescale buffer)
    fig.add_trace(
        go.Scatter(
            x=years_ohc,
            y=ohc_zj,
            mode='lines',
            name='Ocean Heat Content (OHC) (0-2000m)',
            line=dict(color='#4169E1', width=2.5, dash='dot'),  # Royal blue, dotted, thicker
            hovertemplate='Year: %{x:.1f}<br>Ocean Heat Content: %{y:.1f} ZJ<extra></extra>',
            yaxis='y2',  # Use secondary y-axis
            legendgroup='ocean_heat'
        ),
        secondary_y=True  # Plot on right axis with energy imbalance
    )
    
    # Add polynomial trend line to show acceleration
    # 2nd order polynomial shows the curvature (acceleration) in ocean heat accumulation
    coefs = np.polyfit(years_ohc, ohc_zj, 2)
    ohc_trend = np.polyval(coefs, years_ohc)
    
    fig.add_trace(
        go.Scatter(
            x=years_ohc,
            y=ohc_trend,
            mode='lines',
            name='OHC Trend (Quadratic Fit)',
            line=dict(color='#4169E1', width=1, dash='dash'),  # Light touch
            opacity=0.6,
            hovertemplate='Year: %{x:.1f}<br>Trend: %{y:.1f} ZJ<extra></extra>',
            yaxis='y2',
            legendgroup='ocean_heat',
            showlegend=True
        ),
        secondary_y=True
    )
    
    # Add zero reference line for energy imbalance
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color="gray", 
        line_width=1,
        secondary_y=True,
        annotation_text="Zero imbalance (equilibrium)",
        annotation_position="top left"
    )
    
    # Add zero line at bottom of temperature axis for visual grounding
    fig.add_hline(
        y=0,
        line_dash="solid",
        line_color="lightgray",
        line_width=1,
        secondary_y=False
    )
    
    # Update axes
    fig.update_xaxes(
    #    title_text="Year",
        gridcolor='lightgray',
        showgrid=True,
        autorange=True  # Let Plotly auto-calculate range with proper margins
    )
    
    fig.update_yaxes(
        title_text="<b>Global Mean Surface Temperature Anomaly ( degC)</b><br><i>GMST (NASA GISS)</i>",
        secondary_y=False,
        gridcolor='lightgray',
        showgrid=True,
        title_font=dict(color='#DC143C', size=14),
        tickfont=dict(color='#DC143C'),
        range=[0, 1.5]  # Proper temperature range
    )
    
    fig.update_yaxes(
        title_text="<b>Energy Imbalance (W/m^2)</b><br>"
                "<b>Ocean Heat Content (ZJ)</b><br>",
        #           "<i>Ocean Heat Uptake/Release (0-2000m)</i>",
        secondary_y=True,
        title_font=dict(color='#0A0A09', size=13),
        tickfont=dict(color="#0A0A09"),
        range=[-8, 36]  # Fixed range: covers energy imbalance (-5 to +7) and Ocean Heat Content (10 to 33)
    )
    
    # Update layout
    fig.update_layout(
        title={
            'text': "<b>Earth's Energy Imbalance & Temperature (2005-2025)</b><br>"
            #       "<i>Cause and Effect: Energy drives temperature change</i><br>"
                   "<i>Energy drives temperature change -- <b>every tenth matters!</b></i><br>"                   
                   "<span style='font-size:11px; color:#666;'>Data: NASA GISS (temperature) | NOAA NCEI (Ocean Heat Content 0-2000m)</span>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            x=0.035,
            y=1.15,
            xanchor='left',
            yanchor='top',
            bgcolor='rgba(255,255,255,0.9)',  # More opaque for better readability
            bordercolor='gray',
            borderwidth=1
        ),
        height=600,
        margin=dict(l=80, r=80, t=100, b=100),  # Restored original margins
        # Shapes removed - using traces instead to avoid rendering bug
    )
    
    # Add ENSO annotations
    for annotation in enso_annotations:
        fig.add_annotation(**annotation)
    
    # Add key annotations
    
    # Calculate year_2025 first (needed for multiple annotations)
    idx_2025 = -1  # Last data point
    temp_2025 = temp_anomaly_filtered[idx_2025]
    imbalance_2025 = imbalance_w_m2[idx_2025]
    year_2025 = years_ohc[idx_2025]  # Actual decimal year of last point
    
    # 0. Add vertical line at end of data for reference
    fig.add_vline(
        x=year_2025,
        line_dash="dot",
        line_color="gray",
        line_width=1,
        secondary_y=False
    )
    
    """
    # 0b. Calculate average annual Ocean Heat Content accumulation for comparison
    # Ocean Heat Content went from ~10 ZJ (2005) to ~33 ZJ (2025) = 23 ZJ over 20 years
    ohc_start = ohc_zj[0]
    ohc_end = ohc_zj[-1]
    years_span = years_ohc[-1] - years_ohc[0]
    avg_annual_ohc = (ohc_end - ohc_start) / years_span
    
    # Add humanity energy comparison annotation
    # Calculate committed "pipeline" warming from stored Ocean Heat Content
    # Rough estimate: Ocean Heat Content capacity ~4000 J/(kg*K), mass ~1.4e21 kg for 0-2000m
    # Stored excess heat ~23 ZJ, implies ~0.4 degC committed warming in pipeline
    pipeline_warming = 0.4  # Conservative estimate
    
    fig.add_annotation(
        x=year_2025,
        y=32.7,  # Position near top of Ocean Heat Content scale
        text=f'<b>Scale Comparison:</b><br>'
             f'Humanity\'s annual energy use: ~0.6 ZJ/yr<br>'
             f'Ocean Heat Content accumulation: ~{avg_annual_ohc:.1f} ZJ/yr<br>'
             f'<i>Ocean absorbs ~{avg_annual_ohc/0.6:.0f}x human energy use!</i><br><br>'
             f'<b>Pipeline Warming:</b><br>'
             f'Stored heat: {ohc_end - ohc_start:.1f} ZJ since 2005<br>'
             f'<i>~{pipeline_warming:.1f} degC committed warming<br>still unrealized in atmosphere</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#4169E1',  # Royal blue to match Ocean Heat Content line
        ax=-140,
        ay=-50,
        font=dict(size=9, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.95)',
        bordercolor='#4169E1',
        borderwidth=1.5,
        align='left',
        xref='x',
        yref='y2'  # Use secondary y-axis (Ocean Heat Content scale)
    )
    
    # 0c. Baseline annotation at 2005 - explain integration starting point
    ohc_baseline = ohc_zj[0]
    ohc_end = ohc_zj[-1]
    total_accumulation = ohc_end - ohc_baseline
    
    # Simple two-line approach: fit linear trend to each decade
    # First decade: 2005-2015
    mask_first = (years_ohc >= 2005) & (years_ohc < 2015)
    if np.sum(mask_first) > 1:
        coef_first = np.polyfit(years_ohc[mask_first], ohc_zj[mask_first], 1)
        slope_first = coef_first[0]  # ZJ per year
    else:
        slope_first = 1.0
    
    # Second decade: 2015-2025
    mask_second = (years_ohc >= 2015) & (years_ohc <= 2025)
    if np.sum(mask_second) > 1:
        coef_second = np.polyfit(years_ohc[mask_second], ohc_zj[mask_second], 1)
        slope_second = coef_second[0]  # ZJ per year
    else:
        slope_second = 1.2
    
    fig.add_annotation(
        x=2005.2,
        y=ohc_baseline,
        text=f'<b>Integration Baseline</b><br>'
             f'Starting: {ohc_baseline:.1f} ZJ (2005)<br>'
             f'Accumulated: {total_accumulation:.1f} ZJ (20 yrs)<br>'
             f'<i>Trend: {slope_first:.2f}[OK]{slope_second:.2f} ZJ/yr<br>(increasing rate)</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#4169E1',  # Royal blue to match Ocean Heat Content line
        ax=60,
        ay=-75,
        font=dict(size=9, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#4169E1',
        borderwidth=1.5,
        align='left',
        xref='x',
        yref='y2'  # Use secondary y-axis (Ocean Heat Content scale)
    )
    """
    
    # CORRECTED ANNOTATION SECTION FOR energy_imbalance.py
    # Replace lines 530-613 with this code

    # Calculate key values from actual data
    ohc_start = ohc_zj[0]
    ohc_end = ohc_zj[-1]
    years_span = years_ohc[-1] - years_ohc[0]
    total_accumulation = ohc_end - ohc_start
    avg_annual_ohc = total_accumulation / years_span

    # Get the quadratic fit coefficients (already calculated in line 415)
    # coefs = np.polyfit(years_ohc, ohc_zj, 2)
    # ohc_trend = np.polyval(coefs, years_ohc)

    # Calculate instantaneous slopes of the quadratic at 5-year intervals
    # For quadratic y = a*x^2 + b*x + c, the derivative (slope) is: dy/dx = 2*a*x + b
    def quadratic_slope(x, coefs):
        """Calculate instantaneous slope of quadratic at point x"""
        return 2 * coefs[0] * x + coefs[1]

    # Tony's empirically-determined values from sampling the trend line
    # These represent the instantaneous slope of the quadratic at each point
    slope_2010 = 1.00  # ZJ/yr
    slope_2015 = 1.06  # ZJ/yr
    slope_2020 = 1.10  # ZJ/yr
    slope_2025 = 1.14  # ZJ/yr

    # Find OHC values at 5-year intervals (from trend line or data)
    # We'll use the actual data points closest to these years
    def get_closest_value(year_target):
        """Get OHC value at year closest to target"""
        idx = np.argmin(np.abs(years_ohc - year_target))
        return ohc_zj[idx]

    ohc_2005 = ohc_start  # 9.0 ZJ
    ohc_2010 = get_closest_value(2010.2)  # ~14.9 ZJ
    ohc_2015 = get_closest_value(2015.2)  # ~20.2 ZJ (from trend, or ~23.4 actual)
    ohc_2020 = get_closest_value(2020.2)  # ~25.7 ZJ
    ohc_2025 = ohc_end  # 31.9 ZJ

    # ANNOTATION 1: Five-year progression markers along OHC line
    # These show the relentless accumulation and increasing rate

    # 2005.2 - Starting point (boundary condition)
    fig.add_annotation(
        x=2005.2,
        y=ohc_2005,
        text=f'March 2005: {ohc_2005:.1f} ZJ<br><i>Start</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#4169E1',
        ax=0,
        ay=-60,
        font=dict(size=7, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.85)',
        bordercolor='#4169E1',
        borderwidth=1,
        align='center',
        xref='x',
        yref='y2'
    )

    # 2010.2 - First interval
    fig.add_annotation(
        x=2010.2,
        y=ohc_2010,
        text=f'March 2010: {ohc_2010:.1f} ZJ<br><i>Rate: {slope_2010:.2f} ZJ/yr</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#4169E1',
        ax=-50,
        ay=-40,
        font=dict(size=7, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.85)',
        bordercolor='#4169E1',
        borderwidth=1,
        align='left',
        xref='x',
        yref='y2'
    )

    # 2015.2 - Midpoint
    fig.add_annotation(
        x=2015.2,
        y=ohc_2015,
        text=f'March 2015: {ohc_2015:.1f} ZJ<br><i>Rate: {slope_2015:.2f} ZJ/yr</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#4169E1',
        ax=50,
        ay=-40,
        font=dict(size=7, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.85)',
        bordercolor='#4169E1',
        borderwidth=1,
        align='right',
        xref='x',
        yref='y2'
    )

    # 2020.2 - Recent interval
    fig.add_annotation(
        x=2020.2,
        y=ohc_2020,
        text=f'March 2020: {ohc_2020:.1f} ZJ<br><i>Rate: {slope_2020:.2f} ZJ/yr</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#4169E1',
        ax=-50,
        ay=-40,
        font=dict(size=7, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.85)',
        bordercolor='#4169E1',
        borderwidth=1,
        align='left',
        xref='x',
        yref='y2'
    )

    # 2025.2 - Current endpoint (boundary condition)
    fig.add_annotation(
        x=2025.2,
    #    y=ohc_2025,
        y=31.9,
    #    text=f'March 2025: {ohc_2025:.1f} ZJ<br><i>Rate: {slope_2025:.2f} ZJ/yr</i>',
        text=f'March 2025: {31.9:.1f} ZJ<br><i>Rate: {slope_2025:.2f} ZJ/yr</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#4169E1',
        ax=0,
        ay=80,
        font=dict(size=7, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.85)',
        bordercolor='#4169E1',
        borderwidth=1,
        align='center',
        xref='x',
        yref='y2'
    )

    # ANNOTATION 2: Trend line explanation (small note near the trend line)
#    fig.add_annotation(
#        x=2012.0,
#        y=16.0,
#        text='<i>Dashed line: Quadratic fit<br>(shows acceleration)</i>',
#        showarrow=False,
#        font=dict(size=7, color='#4169E1'),
#        bgcolor='rgba(255,255,255,0.7)',
#        bordercolor='#4169E1',
#        borderwidth=0.5,
#        align='center',
#        xref='x',
#        yref='y2'
#    )

    # ANNOTATION 3: Scale Comparison (updated with corrected values)
#    pipeline_warming = 0.4  # Conservative estimate
    pipeline_warming = 0.6  # Hansen et al. (2005) - Earth's Energy Imbalance

    fig.add_annotation(
    #    x=year_2025,
        x=2025.2,
    #    y=32.7,  # Position near top of Ocean Heat Content scale
        y=31.9,
        text=f'<b>Scale Comparison:</b><br>'
            f'Humanity\'s annual energy use: ~0.6 ZJ/yr<br>'
            f'Ocean heat accumulation<br>'
    #        f'(March 2005 - March 2025): ~{avg_annual_ohc:.2f} ZJ/yr<br>'
            f'(March 2005 - March 2025): ~ 1.08 ZJ/yr<br>'
    #        f'<i>Ocean absorbs ~{avg_annual_ohc/0.6:.0f}x human energy use!</i><br><br>'
            f'<i>Ocean absorbs ~{1.075/0.6:.0f}x human energy use!</i><br>'
            f'<b>Total Accumulation (2005-2025):</b><br>'
    #        f'Final: {ohc_2025:.1f} ZJ (2025)<br>'
    #        f'March 2025: {31.9:.1f} ZJ<br>'            
    #        f'Accumulated: {total_accumulation:.1f} ZJ<br>'
            f'Accumulated since March 2005: {22.9:.1f} ZJ<br>'            
            f'Acceleration: {slope_2010:.2f} [OK] {slope_2025:.2f} ZJ/yr (+{100*(slope_2025-slope_2010)/slope_2010:.0f}%)<br>',
    #        f'<b>Pipeline Warming:</b><br>'        # this comment needs more developement
    #        f'<i>~{pipeline_warming:.1f} degC committed warming (2005)<br>still unrealized in atmosphere</i>',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#4169E1',
        ax=-145,
        ay=-60,
        font=dict(size=8, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.95)',
        bordercolor='#4169E1',
        borderwidth=1.5,
        align='left',
        xref='x',
        yref='y2'  # Use secondary y-axis (Ocean Heat Content scale)
    )

    # Note: The old "Integration Baseline" annotation has been replaced by the
    # five-year progression markers above, which show the accumulation more clearly.
    # The "Scale Comparison" now includes the final value, total accumulation,
    # and acceleration information.

    # 1. Paris Agreement (2015)
    fig.add_annotation(
        x=2015,
        y=1.2,
        text='Paris Agreement',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#2E8B57',  # Sea green
        ax=0,
        ay=-40,
        font=dict(size=10, color='#2E8B57'),
        bgcolor='rgba(255,255,255,0.95)',
        bordercolor='#2E8B57',
        borderwidth=1
    )
    
    # 1b. Key Climate Events
    """
    # 2023 Record Heat
    fig.add_annotation(
        x=2023.2,
        y=1.32,
        text='2023 Record',
        showarrow=False,
        arrowhead=2,
        arrowsize=0.8,
        arrowwidth=1,
        arrowcolor='#8B0000',  # Dark red
        ax=1,
        ay=1,
        font=dict(size=8, color='#8B0000'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#8B0000',
        borderwidth=0.5
    )
    """
    
    # 2. Present (2025) - use actual data values
    fig.add_annotation(
        x=year_2025,  # Use actual decimal year position
        y=0.6,
        text=f'April 2025<br>Imbalance: {imbalance_2025:.2f} W/m^2<br>Temp: +{temp_2025:.2f} degC',
        showarrow=False,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='red',
        ax=-60,
        ay=80,
        font=dict(size=10, color='red'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='red',
        borderwidth=1
    )
    
    # 3. The ocean buffer and visual integration explanation
    fig.add_annotation(
        x=0,
        y=-0.23,
        xref='paper',
        yref='paper',
        text=
    #    '<b>The Causal Chain:</b> Greenhouse gases (CO2, CH4) trap outgoing radiation [OK] Earth\'s energy imbalance (more in than out) [OK] '
    #         '~90% of excess energy absorbed by oceans (0-2000m layer acts as heat reservoir) [OK] atmospheric temperature rises with lag.<br>'
    #         '<b>Visual Guide:</b> Red shading = ocean warming periods (absorbing energy). Blue = cooling periods (releasing energy). '
    #         'Net red dominance [OK] blue dotted line rises (cumulative heat storage grows) [OK] continued atmospheric warming as stored heat eventually releases.<br>'

            '<b>The Causal Chain:</b> The accumulation of greenhouse gases (CO2, CH4) creates a sustained <b>Planetary Energy Imbalance (EEI)</b> (Orange line). Over 90% of this excess energy is absorbed by the' 
            'deep ocean, driving the rise of the <b>Ocean Heat Content (OHC)</b>.<br>' 

    #        '<b>ENSO & The Trade-off:</b> The El Nino-La Nina oscillation modulates this energy flow:<br>' 
            ' *<b>La Nina (Blue Bands):</b> The ocean absorbs more solar energy, temporarily <b>increasing the EEI</b> (Orange line peaks) while **cooling the atmosphere** (GMST dips).<br>' 
            ' *<b>El Nino (Orange Bands):</b> The ocean releases stored heat into the atmosphere, causing atmospheric temperature to <b>peak</b> (GMST peaks) while the planet temporarily reflects more sunlight, **decreasing the EEI** (Orange line dips).<br>'            
            '<b>Key Insight:</b> The atmospheric temperature (GMST) swings are merely a *redistribution* of heat. The net positive accumulation shown by the rising **OHC** demonstrates the growing total committed warming stored in the climate system.<br>' 

    #         '<b>Data Sources:</b> '
    #         'Temperature: <a href="https://data.giss.nasa.gov/gistemp/">NASA GISS Surface Temperature Analysis (GISTEMP v4)</a> | '
    #         'Ocean Heat Content: <a href="https://www.ncei.noaa.gov/access/global-ocean-heat-content/">NOAA NCEI Ocean Heat Content (0-2000m, Levitus et al.)</a>',

            '<b>Data Sources:</b> '
            'Temperature: <a href="https://data.giss.nasa.gov/gistemp/">NASA GISS Surface Temperature Analysis (GISTEMP v4)</a> | '
            'Ocean Heat Content: <a href="https://www.ncei.noaa.gov/access/global-ocean-heat-content/">NOAA NCEI Ocean Heat Content (0-2000m, Levitus et al.)</a> | '
            'Pipeline Warming: <a href="https://doi.org/10.1126/science.1110252">Hansen et al. (2005), Science</a>',


        showarrow=False,
        font=dict(size=9, color='#333'),
        align='left',
        bgcolor='rgba(255,250,205,0.9)',  # Light yellow
        bordercolor='#FF8C00',
        borderwidth=1,
        borderpad=8
    )
    
    return fig

def main():
    """Create and save the visualization"""
    fig = create_energy_imbalance_visualization()
    
    if fig is not None:
        # Show the visualization in browser (like other visualizations)
        fig.show()
        
        # Then offer to save using save_utils if available
        if SAVE_UTILS_AVAILABLE:
            # save_plot signature: save_plot(fig, default_name)
            save_plot(fig, 'energy_imbalance_2005_2025')
        else:
            # Fallback: save as HTML without dialog
            output_file = 'energy_imbalance_2005_2025.html'
            fig.write_html(output_file)
            print(f"[OK] Saved to: {output_file}")
        
        print("[OK] Energy imbalance visualization created successfully")
        return True
    else:
        print("[FAIL] Could not create visualization")
        return False

if __name__ == '__main__':
    main()
