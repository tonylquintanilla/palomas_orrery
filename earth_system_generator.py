"""
Paloma's Orrery: Earth System Generator Engine
Architecture: The Teaser (Plotly) & Blockbuster (KMZ) Pipeline

This is the shared engine. Scenario modules (scenarios_heatwaves.py,
scenarios_coral_bleaching.py, etc.) provide fetch functions and
SCENARIOS lists. The engine never knows or cares what boundary type
it's rendering.

Usage:
    from earth_system_generator import run_scenario
    from scenarios_heatwaves import SCENARIOS
    run_scenario(SCENARIOS[0])

Module updated: June 2026 with Anthropic's Claude Opus 4.8
- KMZ intel card -> compact always-on header + tappable info balloon
  (create_info_placemark). Population-exposure key folded into the balloon;
  risk-scale colorbar repositioned off the bottom chrome. Cards now reflow on
  mobile Google Earth instead of colliding with the search bar / toolbar.
"""
import re
import os
import math
import json
import zipfile
import textwrap
import html
import numpy as np
import simplekml
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import griddata
import tkinter as tk
from tkinter import ttk, messagebox

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


# ==========================================
#           ENGINE: CORE PIPELINE
# ==========================================

def _build_auto_mobile_briefing(briefing):
    """Auto-generate a shortened mobile briefing from the full briefing.
    
    Keeps title + first narrative paragraph. Drops attribution,
    station records, and source lines that crowd small screens.
    
    Scenario modules can override by providing their own mobile_briefing
    key in the scenario dict. This auto-version handles scenarios that
    don't provide one.
    """
    if not briefing:
        return ''
    # Normalize: both <br><br> and \n\n are paragraph breaks
    normalized = briefing.replace('<br><br>', '\n\n').replace('<BR><BR>', '\n\n')
    parts = [p.strip() for p in normalized.split('\n\n') if p.strip()]
    if len(parts) <= 2:
        return briefing  # Already short enough
    # Keep title + first narrative paragraph
    return parts[0] + '<br><br>' + parts[1]

def run_scenario(scenario, status_callback=None):
    """Orchestrates the full pipeline for one scenario.
    
    1. Fetch data (calls scenario's own fetch function)
    2. Generate legend/intel cards (KML assets)
    3. Build KML layers (spikes, heatmap, impact)
    4. Generate Plotly teaser (web gallery)
    5. Package KMZ (merged single-doc)
    
    Args:
        scenario: dict following the scenario config contract
        status_callback: optional callable(str) for GUI progress
    """
    scenario_id = scenario['scenario_id']
    name = scenario['name']
    date = scenario['date']
    thresholds = scenario['thresholds']

    # 1. FETCH DATA
    if status_callback:
        status_callback("Fetching data...")
    scenario['fetch'](scenario, DATA_DIR, status_callback=status_callback)

    lats = scenario['lats']
    lons = scenario['lons']
    values = scenario['values']

    if not values:
        raise ValueError(f"No data retrieved for {name}")

    # Fill the regional wet-bulb peak from the fetched grid before ANY briefing
    # consumer renders it -- KMZ intel card, Plotly teaser, and mobile briefing all
    # read scenario['briefing']. Producer-level substitution: no consumer sees raw
    # [TO-FETCH]. (generate_plotly_teaser keeps its own guard for standalone calls.)
    if '[TO-FETCH]' in scenario.get('briefing', ''):
        scenario['briefing'] = scenario['briefing'].replace('[TO-FETCH]', f"{max(values):.1f}")

    # 2. GENERATE LEGEND AND INTEL CARDS
    if status_callback:
        status_callback("Generating Intel Cards...")

    legend_risk_path = create_legend_card(thresholds, scenario_id)
    intel_path = create_intel_card(name, scenario.get('description', ''),
                                   scenario.get('briefing', ''), date, scenario_id)

    # 3. BUILD KML LAYERS
    if status_callback:
        status_callback("Building 3D Topology...")

    spikes_filename = build_spikes_kml(scenario_id, date, lats, lons, values,
                                        thresholds, intel_path, legend_risk_path,
                                        pin_stations=scenario.get('pin_stations'),
                                        name=name, briefing=scenario.get('briefing', ''))
    heat_filename = build_heatmap_kml(scenario_id, date, lats, lons, values, thresholds)
    impact_filename = build_impact_kml(scenario_id, date, scenario.get('populations', []),
                                        None, thresholds)

    # 4. GENERATE PLOTLY TEASER
    generate_plotly_teaser(scenario_id, f"{name} ({date})", lats, lons, values,
                           DATA_DIR, thresholds,
                           briefing=scenario.get('briefing', ''), 
                           description=scenario.get('description', ''),
                           mobile_briefing=scenario.get('mobile_briefing', ''),
                           encyclopedia=scenario.get('encyclopedia', ''))    

    # 5. PACKAGE KMZ
    img_path = os.path.join(DATA_DIR, f"{date}_heatmap_{scenario_id}.png")
    generated_files = [
        spikes_filename,
        heat_filename,
        impact_filename if impact_filename else "",
        img_path,
        legend_risk_path,
        intel_path
    ]
    package_and_cleanup(scenario_id, generated_files, DATA_DIR)

    print(f"Pipeline complete for: {name}")


# ==========================================
#           ENGINE: KML BUILDERS
# ==========================================

def build_spikes_kml(scenario_id, date, lats, lons, values, thresholds,
                     intel_path, legend_risk_path, pin_stations=None,
                     name='', briefing=''):
    """Builds the vertical extrusion spikes KML layer.
    
    Spike colors and heights are driven by thresholds config.
    """
    kml_spikes = simplekml.Kml()
    kml_spikes.document.name = f"{scenario_id} Spikes ({date})"

    # Compact header overlay (upper-left, dropped below the mobile search bar)
    screen = kml_spikes.newscreenoverlay(name="Intel Card")
    screen.icon.href = os.path.basename(intel_path)
    screen.overlayxy = simplekml.OverlayXY(x=0, y=1, xunits=simplekml.Units.fraction,
                                            yunits=simplekml.Units.fraction)
    screen.screenxy = simplekml.ScreenXY(x=0.02, y=0.84, xunits=simplekml.Units.fraction,
                                          yunits=simplekml.Units.fraction)
    screen.size = simplekml.Size(x=0.22, y=0, xunits=simplekml.Units.fraction,
                                  yunits=simplekml.Units.fraction)

    # Risk scale legend (right edge, vertically centered -- clears the
    # bottom-right nav / 3D buttons that clipped it on mobile)
    screen_leg = kml_spikes.newscreenoverlay(name="Risk Scale")
    screen_leg.icon.href = os.path.basename(legend_risk_path)
    screen_leg.overlayxy = simplekml.OverlayXY(x=1, y=0.5, xunits=simplekml.Units.fraction,
                                                yunits=simplekml.Units.fraction)
    screen_leg.screenxy = simplekml.ScreenXY(x=0.99, y=0.5, xunits=simplekml.Units.fraction,
                                              yunits=simplekml.Units.fraction)
    screen_leg.size = simplekml.Size(x=0.15, y=0, xunits=simplekml.Units.fraction,
                                      yunits=simplekml.Units.fraction)

    # Tappable info balloon ("i" pin at the grid centroid) -- holds the full
    # briefing + population-exposure key, reflowing clear of GE chrome.
    if lats and lons:
        c_lat = sum(lats) / len(lats)
        c_lon = sum(lons) / len(lons)
        create_info_placemark(kml_spikes, scenario_id, name or scenario_id,
                              date, briefing, c_lat, c_lon)

    # Station pin mode: confirmed observations instead of grid stride
    if pin_stations:
        for station in pin_stations:
    #        label = f"{station['anomaly']:.1f}F"
            if 'air_temp_c' in station:
                label = f"{station['air_temp_c']:.1f}C"
            else:
                label = f"{station['air_temp_f']:.0f}F"
            pnt = kml_spikes.newpoint(name=label)
            pnt.coords = [(station['lon'], station['lat'], 0)]
            pnt.altitudemode = simplekml.AltitudeMode.clamptoground
            pnt.description = station.get('note', '')
            pnt.style.iconstyle.scale = 0.6

        spikes_filename = os.path.join(DATA_DIR, f"{date}_spikes_{scenario_id}.kml")
        kml_spikes.save(spikes_filename)
        return spikes_filename

    bands = thresholds['bands']
    height_multiplier = thresholds.get('height_multiplier', 50000)
    spike_floor = thresholds.get('spike_floor')
    spike_stride = thresholds.get('spike_stride', 1)

    for i, (lat, lon, val) in enumerate(zip(lats, lons, values)):
        # Stride: only process every Nth point (heatmap uses full data)
        if spike_stride > 1 and i % spike_stride != 0:
            continue

        # Determine spike floor: either explicit or per-scenario focus_val_min
        floor = spike_floor if spike_floor is not None else bands[0][0]
        if val < floor:
            continue

        # Height calculation
        if thresholds.get('height_base_subtract'):
            height = (val - floor) * height_multiplier
        else:
            height = val * height_multiplier

        # Color from bands (walk up until val < threshold)
        color = bands[-1][1]  # default to highest band
        for threshold_val, band_color, _label in bands:
            if val < threshold_val:
                color = band_color
                break

    #    pnt = kml_spikes.newpoint(name=f"{val:.1f}")
    #    pnt.coords = [(lon, lat, height)]
    #    pnt.extrude = 1
    #    pnt.altitudemode = simplekml.AltitudeMode.relativetoground

        pnt = kml_spikes.newpoint(name=f"{val:.1f}")
        pnt.coords = [(lon, lat, 0)]
        pnt.altitudemode = simplekml.AltitudeMode.clamptoground

        pnt.style.polystyle.color = color
        pnt.style.polystyle.fill = 1
        pnt.style.linestyle.width = 0

    spikes_filename = os.path.join(DATA_DIR, f"{date}_spikes_{scenario_id}.kml")
    kml_spikes.save(spikes_filename)
    return spikes_filename


def build_heatmap_kml(scenario_id, date, lats, lons, values, thresholds):
    """Builds the ground overlay heatmap KML layer with contour PNG."""
    # Generate contour PNG
    grid_x, grid_y = np.mgrid[min(lons):max(lons):100j, min(lats):max(lats):100j]
    grid_z = griddata((lons, lats), values, (grid_x, grid_y), method='linear')

    img_name = f"{date}_heatmap_{scenario_id}.png"
    img_path = os.path.join(DATA_DIR, img_name)

    dpi = 150
    fig = plt.figure(figsize=(10, 5), dpi=dpi, frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    levels_start = thresholds.get('contour_levels_start', 0)
    levels_stop = thresholds.get('contour_levels_stop', 38)
    levels_step = thresholds.get('contour_levels_step', 1)
    cmap = thresholds.get('contour_cmap', 'inferno_r')
    levels = np.arange(levels_start, levels_stop, levels_step)

    ax.contourf(grid_x, grid_y, grid_z, levels=levels, cmap=cmap, alpha=0.35)
    ax.contour(grid_x, grid_y, grid_z, levels=levels, colors='black', linewidths=0.5, alpha=0.5)
    plt.savefig(img_path, transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

    # Build KML with ground overlay
    kml_heat = simplekml.Kml()
    kml_heat.document.name = f"{scenario_id} Heatmap ({date})"
    ground = kml_heat.newgroundoverlay(name="Thermal Overlay")
    ground.icon.href = img_name
    ground.latlonbox.north = max(lats)
    ground.latlonbox.south = min(lats)
    ground.latlonbox.east = max(lons)
    ground.latlonbox.west = min(lons)

    heat_filename = os.path.join(DATA_DIR, f"{date}_heatmap_{scenario_id}.kml")
    kml_heat.save(heat_filename)
    return heat_filename


def build_impact_kml(scenario_id, date, populations, legend_pop_path, thresholds=None):
    """Builds the population impact circles KML layer.
    
    Returns None if no populations defined for this scenario.
    Pop circle radius controlled by thresholds['pop_radius_divisor']
    (default 250000 for heatwaves, 50000 for coral/coastal scenarios).
    """
    if not populations:
        return None

    kml_pop = simplekml.Kml()
    kml_pop.document.name = f"{scenario_id} Impact Zones"

    # Population Exposure key now lives in the tappable info balloon
    # (create_info_placemark), not a fixed ScreenOverlay -- frees the
    # bottom-left corner that collided with the mobile toolbar. The
    # legend_pop_path param is retained for call-site compatibility.

    for city in populations:
        pop = city['pop']
        radius_km = math.sqrt(pop) / 75

        # Tiered color by population size (KML AABBGGRR format)
        if pop > 5000000:
            color_fill = "660000ff"   # Red (40% opacity)
            color_line = "ff0000ff"   # Red (100% opacity)
        elif pop > 1000000:
            color_fill = "6600a5ff"   # Orange
            color_line = "ff00a5ff"
        elif pop > 500000:
            color_fill = "6600ffff"   # Yellow
            color_line = "ff00ffff"
        else:
            color_fill = "66ffffff"   # White
            color_line = "ffffffff"

        points = create_circle_polygon(city['lat'], city['lon'], radius_km)

        pol = kml_pop.newpolygon(name=f"{city['name']} ({pop:,})")
        pol.outerboundaryis = points
        pol.style.polystyle.color = color_fill
        pol.style.polystyle.fill = 1
        pol.style.linestyle.color = color_line
        pol.style.linestyle.width = 2

    impact_filename = os.path.join(DATA_DIR, f"{date}_impact_{scenario_id}.kml")
    kml_pop.save(impact_filename)
    return impact_filename


# ==========================================
#           ENGINE: PLOTLY TEASER
# ==========================================

def generate_plotly_teaser(scenario_id, title, lats, lons, values, output_dir,
                           thresholds, briefing="", description="",
                           mobile_briefing="", encyclopedia=""):    
    """Generates the fast-loading 2D Plotly Teaser for Web Gallery use.
    
    Colorscale, value range, and colorbar title are driven by thresholds config.
    """
    print("Building Plotly Teaser...")

    if briefing and values:
        briefing = briefing.replace('[TO-FETCH]', f"{max(values):.1f}")

    colorscale = thresholds.get('colorscale', 'YlOrRd')
    cmin = thresholds.get('cmin', 0)
    cmax = thresholds.get('cmax', 38)
    colorbar_title = thresholds.get('colorbar_title', 'Value')

    # Per-point transparency: low anomaly values become transparent so the
    # underlying map shows through; hot spots stay fully opaque. Plotly's
    # Scattermapbox marker.opacity is scalar-only, so we encode alpha into
    # RGBA marker colors directly. A separate invisible trace carries the
    # colorbar since RGBA color arrays don't support colorscale integration.
    opacity_midpoint = cmax / 2.0 if cmax > 0 else 15.0

    try:
        import plotly.express as px
        # Sample the colorscale at each value's normalized position
        normalized = [max(0.0, min(1.0, (v - cmin) / (cmax - cmin))) if cmax > cmin else 0.5
                      for v in values]
        sampled_colors = px.colors.sample_colorscale(colorscale, normalized)
        rgba_colors = []
        for rgb_str, v in zip(sampled_colors, values):
            rgb = rgb_str.replace('rgb(', '').replace(')', '').split(',')
            r, g, b = [int(x.strip()) for x in rgb]
            alpha = min(1.0, max(0.05, v / opacity_midpoint))
            rgba_colors.append(f'rgba({r},{g},{b},{alpha:.2f})')
        use_rgba = True
    except Exception:
        # Fallback: no transparency, plain colorscale
        rgba_colors = None
        use_rgba = False

    if use_rgba:
        # Trace 1: visible markers with RGBA per-point alpha
        fig = go.Figure(go.Scattermapbox(
            name=title,
            lat=lats,
            lon=lons,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=8,
                color=rgba_colors,
            ),
            text=[f"{colorbar_title}: {v:.1f}" for v in values],
            hoverinfo='text'
        ))
        # Trace 2: invisible point to carry the colorbar
        fig.add_trace(go.Scattermapbox(
            lat=[lats[0]], lon=[lons[0]],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=0.001,
                color=[cmin],
                colorscale=colorscale,
                cmin=cmin,
                cmax=cmax,
                opacity=0,
                showscale=True,
                colorbar=dict(title=colorbar_title)
            ),
            hoverinfo='skip',
            showlegend=False
        ))
    else:
        # Fallback: original scalar opacity approach
        fig = go.Figure(go.Scattermapbox(
            name=title,
            lat=lats,
            lon=lons,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=8,
                color=values,
                colorscale=colorscale,
                cmin=cmin,
                cmax=cmax,
                opacity=0.75,
                showscale=True,
                colorbar=dict(title=colorbar_title)
            ),
            text=[f"{colorbar_title}: {v:.1f}" for v in values],
            hoverinfo='text'
        ))

    center_lat = sum(lats) / len(lats) if lats else 0
    center_lon = sum(lons) / len(lons) if lons else 0

    # Build briefing annotation for bottom-left of map
    annotations = []
    if briefing:
        import textwrap
        # Render the FULL briefing -- station records, SOURCE and ATTRIBUTION
        # included -- word-wrapped so it stays inside the box. (Peak already
        # substituted upstream, before the mobile-briefing builder too.)
        wrapped = [textwrap.fill(ln, width=90) if ln.strip() else '' for ln in briefing.split('\n')]
        brief_text = '<br>'.join(wrapped).replace('\n', '<br>')
        brief_text += "<br><br><i>Click 3D Earth for full visualization in Google Earth</i>"

        annotations.append(dict(
            text=brief_text,
            showarrow=False,
            xref="paper", yref="paper",
            x=0.02, y=0.02,
            xanchor="left", yanchor="bottom",
            font=dict(size=11, color="#1a1a2e"),
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="rgba(0,0,0,0.15)",
            borderwidth=1,
            borderpad=8,
            align="left"
        ))

    fig.update_layout(
        title=title,
        mapbox=dict(
            style="white-bg",
            center=dict(lat=center_lat, lon=center_lon),
            zoom=3,
            layers=[dict(
                below='traces',
                sourcetype='raster',
                sourceattribution='ESRI',
                source=['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}']
            )]
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        annotations=annotations,
        showlegend=False       
    )

    # Build HTML manually to guarantee Gallery Studio compatibility
    fig_json = fig.to_json()
    fig_dict = json.loads(fig_json)

    # Embed mobile briefing for Studio to swap at export time
    # Use scenario's custom version if provided, else auto-generate
    effective_mobile = mobile_briefing or _build_auto_mobile_briefing(briefing)
    if effective_mobile:
        fig_dict['layout']['_mobile_briefing'] = effective_mobile

    # Embed encyclopedia for gallery viewer "i" card
    # Keyed to trace name so the viewer's hover/click lookup works
    if encyclopedia:
        fig_dict['layout']['_encyclopedia'] = {title: encyclopedia}

    data_str = json.dumps(fig_dict.get('data', []))
    layout_str = json.dumps(fig_dict.get('layout', {}))

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
</head>
<body style="background:#f5f5f0; margin:0;">
    <div id="plotly-graph" style="width:100vw; height:100vh;"></div>
    <script>
        var data = {data_str};
        var layout = {layout_str};
        Plotly.newPlot('plotly-graph', data, layout);
    </script>
</body>
</html>"""

    teaser_path = os.path.join(output_dir, f"{scenario_id}_teaser.html")
    with open(teaser_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Plotly Teaser saved: {teaser_path}")


# ==========================================
#           ENGINE: KMZ PACKAGING
# ==========================================

def package_and_cleanup(scenario_id, files_to_package, output_dir):
    """Zips the raw KML and PNG files into a single-document KMZ.
    
    Merges all KML layers into one doc.kml with <Folder> wrappers.
    Google Earth only reads the first KML in a KMZ archive, so separate
    KML files would result in only one layer loading. This approach
    puts everything in a single document with toggleable folders.
    
    Keeps original KML/PNG files on disk for the desktop Python orrery.
    """
    kmz_filename = f"{scenario_id}_blockbuster.kmz"
    kmz_path = os.path.join(output_dir, kmz_filename)
    print(f"Packaging {kmz_filename}...")

    # Separate KML files from asset files (PNG etc.)
    kml_files = [f for f in files_to_package if f.endswith('.kml') and os.path.exists(f)]
    asset_files = [f for f in files_to_package if not f.endswith('.kml') and os.path.exists(f)]

    # Merge all KML document bodies into folders within a single doc.kml
    folders = ""
    for kml_path in kml_files:
        basename = os.path.basename(kml_path)
        # Derive a readable layer name from the filename
        parts = basename.replace('.kml', '').split('_')
        layer_name = basename
        for part in parts:
            if part.lower() in ('spikes', 'heatmap', 'impact'):
                layer_name = part.capitalize()
                break

        with open(kml_path, 'r', encoding='utf-8') as f:
            kml_text = f.read()

        m = re.search(r'<Document[^>]*>(.*)</Document>', kml_text, re.DOTALL)
        body = m.group(1).strip() if m else ''

        if body:
            folders += f"""
        <Folder>
            <n>{layer_name}</n>
            {body}
        </Folder>"""

    doc_kml = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
    <Document>
        <n>{scenario_id}</n>{folders}
    </Document>
</kml>
"""

    with zipfile.ZipFile(kmz_path, 'w', zipfile.ZIP_DEFLATED) as kmz:
        kmz.writestr('doc.kml', doc_kml)
        for f in asset_files:
            kmz.write(f, arcname=os.path.basename(f))

    # NOTE: Raw KML/PNG files are NOT deleted.
    print(f"Packaged: {kmz_filename} ({len(kml_files)} layers merged)")
    return kmz_path


# ==========================================
#           ENGINE: CARD GENERATORS
# ==========================================

def create_legend_card(thresholds, scenario_id):
    """Creates the risk scale legend image from threshold bands.
    
    Supports two styles controlled by thresholds['legend_style']:
      'discrete'   (default) - colored patches per band
      'continuous' - matplotlib colorbar matching the contour colormap
    
    Figure height scales with the number of bands so labels never overlap.
    Visual style: white semi-transparent background, readable over terrain.
    """
    legend_style = thresholds.get('legend_style', 'discrete')
    legend_title = thresholds.get('legend_title', 'Bio-Limits')

    if legend_style == 'continuous':
        # Continuous colorbar matching the contour heatmap
        cmap_name = thresholds.get('contour_cmap', 'inferno_r')
        cmin = thresholds.get('contour_levels_start', 0)
        cmax = thresholds.get('contour_levels_stop', 35)

        fig = plt.figure(figsize=(1.8, 4.0), dpi=120)
        fig.patch.set_facecolor('white')
        fig.patch.set_alpha(0.7)

        ax = fig.add_axes([0.05, 0.08, 0.35, 0.78])
        norm = plt.Normalize(vmin=cmin, vmax=cmax)
        cb = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap_name),
                          cax=ax, orientation='vertical')
        cb.set_label(thresholds.get('unit_label', 'Value'), fontsize=9)
        cb.ax.tick_params(labelsize=8)

        fig.text(0.55, 0.93, legend_title, fontweight='bold', fontsize=9,
                 ha='center', va='center')

    else:
        # Discrete band patches (original behavior)
        bands = thresholds['bands']
        num_bands = len(bands)
        fig_height = 1.2 + num_bands * 0.7

        fig = plt.figure(figsize=(3.5, fig_height), dpi=120)
        fig.patch.set_facecolor('white')
        fig.patch.set_alpha(0.7)

        ax = fig.add_subplot(111)
        ax.axis('off')

        legend_elements = []
        for threshold_val, kml_color, label in reversed(bands):
            if threshold_val == float('inf'):
                display = f"> {bands[-2][0]:.0f}: {label}"
            else:
                display = f"{threshold_val:.0f}+: {label}"
            color = kml_to_mpl_color(kml_color)
            legend_elements.append(mpatches.Patch(color=color, label=display))

        ax.legend(handles=legend_elements, loc='upper center',
                  bbox_to_anchor=(0.5, 0.93), frameon=False, fontsize=9)
        plt.text(0.5, 0.97, legend_title, ha='center', va='center',
                 transform=ax.transAxes, fontweight='bold', fontsize=11)

    legend_path = os.path.join(DATA_DIR, f'legend_risk_{scenario_id}.png')
    plt.savefig(legend_path, bbox_inches='tight', pad_inches=0.1,
                transparent=False)
    plt.close()
    return legend_path


def create_pop_legend_card(scenario_id):
    """Creates the population circle key with tiered size/color."""
    fig = plt.figure(figsize=(2.5, 3.0), dpi=120)
    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(0.8)

    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)

    # Red Circle (Megacity) - matches KML '660000ff'/'ff0000ff'
    c_mega = mpatches.Circle((5, 9), 1.5, facecolor='#ff000066',
                              edgecolor='red', linewidth=1.5)
    ax.add_patch(c_mega)
    plt.text(5, 7.2, "Megacity (>5M)", ha='center', fontsize=7, fontweight='bold')

    # Orange Circle (Major) - matches KML '6600a5ff'/'ff00a5ff'
    c_major = mpatches.Circle((2.5, 5), 1.2, facecolor='#ffa50066',
                               edgecolor='orange', linewidth=1.5)
    ax.add_patch(c_major)
    plt.text(2.5, 3.5, "Major (>1M)", ha='center', fontsize=7)

    # Yellow Circle (Regional) - matches KML '6600ffff'/'ff00ffff'
    c_reg = mpatches.Circle((7.5, 5), 0.9, facecolor='#ffff0066',
                             edgecolor='#cccc00', linewidth=1.5)
    ax.add_patch(c_reg)
    plt.text(7.5, 3.5, "Region (>500k)", ha='center', fontsize=7)

    plt.text(5, 11, "Population Exposure", ha='center',
             fontweight='bold', fontsize=9)

    legend_path = os.path.join(DATA_DIR, f'legend_pop_{scenario_id}.png')
    plt.savefig(legend_path, bbox_inches='tight', pad_inches=0.1,
                transparent=False)
    plt.close()
    return legend_path


def create_intel_card(title, description, briefing, date, scenario_id):
    """Creates the compact always-on header card (title + date + hint).

    The full briefing now lives in the tappable info balloon
    (create_info_placemark); this header only identifies the scenario so the
    map reads at a glance without the long text block colliding with chrome.
    The description/briefing params are kept for call-site compatibility.
    """
    fig = plt.figure(figsize=(4, 0.9), dpi=120)
    fig.patch.set_facecolor('#f8f9fa')
    fig.patch.set_alpha(0.7)

    ax = fig.add_subplot(111)
    ax.axis('off')

    plt.text(0.04, 0.72, f"{scenario_id.upper()}",
             transform=ax.transAxes, fontsize=12, fontweight='bold', color='#222')
    plt.text(0.04, 0.40, f"DATE: {date}",
             transform=ax.transAxes, fontsize=9, fontfamily='monospace', color='#555')
    plt.text(0.04, 0.10, "Tap the (i) pin for the full briefing",
             transform=ax.transAxes, fontsize=7, color='#777', style='italic')

    intel_path = os.path.join(DATA_DIR, f'{date}_intel_{scenario_id}.png')
    plt.savefig(intel_path, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close()
    return intel_path


def _briefing_to_html(briefing):
    """Convert a plain-text briefing into safe, reflowing balloon HTML.

    Normalizes <br> to line breaks, strips any other markup, escapes the
    text, then re-emits paragraphs so the balloon wraps to the device width.
    """
    text = briefing.replace('<br>', '\n').replace('<BR>', '\n')
    text = re.sub(r'<[^>]+>', '', text)
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    out = []
    for p in paras:
        esc = html.escape(p).replace('\n', '<br>')
        out.append('<p style="margin:0 0 8px 0;">' + esc + '</p>')
    return ''.join(out)


def create_info_placemark(kml, scenario_id, title, date, briefing, lat, lon):
    """Add a tappable info "i" placemark whose balloon holds the full briefing.

    The balloon reflows to the device width and renders clear of Google Earth's
    search bar / toolbar, so the narrative no longer collides with chrome the
    way a fixed ScreenOverlay PNG does. The population-exposure key is folded
    in here as well. Default-closed; opens on tap.
    """
    balloon = (
        '<div style="max-width:340px; '
        'font-family:-apple-system,Helvetica,Arial,sans-serif; '
        'font-size:14px; line-height:1.4; color:#222;">'
        '<h3 style="margin:0 0 6px 0; font-size:16px;">'
        + html.escape(title) + '</h3>'
        '<div style="font:12px monospace; color:#666; margin-bottom:8px;">'
        'DATE: ' + html.escape(str(date)) + '</div>'
        + _briefing_to_html(briefing) +
        '<hr style="border:none; border-top:1px solid #ddd; margin:8px 0;">'
        '<div style="font-weight:bold; margin-bottom:4px;">'
        'Population Exposure</div>'
        '<div><span style="color:#e00; font-size:16px;">&#9679;</span> '
        'Megacity (&gt;5M)</div>'
        '<div><span style="color:#f80; font-size:16px;">&#9679;</span> '
        'Major (&gt;1M)</div>'
        '<div><span style="color:#cc0; font-size:16px;">&#9679;</span> '
        'Region (&gt;500k)</div>'
        '</div>'
    )

    pnt = kml.newpoint(name=f"{title} - tap for details")
    pnt.coords = [(lon, lat, 0)]
    pnt.altitudemode = simplekml.AltitudeMode.clamptoground
    # Wrap in CDATA so simplekml emits the HTML unescaped (base.py leaves
    # CDATA blocks untouched); GE then renders the balloon as HTML rather
    # than printing literal tags -- matching the proven desktop probe.
    pnt.description = '<![CDATA[' + balloon + ']]>'
    pnt.style.iconstyle.icon.href = \
        "http://maps.google.com/mapfiles/kml/shapes/info-i.png"
    pnt.style.iconstyle.scale = 1.3
    pnt.style.labelstyle.scale = 0.9
    pnt.style.balloonstyle.text = "$[description]"
    return pnt


# ==========================================
#           ENGINE: UTILITIES
# ==========================================

def create_circle_polygon(lat, lon, radius_km, num_points=32):
    """Generates a circle polygon for KML population impact layer."""
    R = 6371.0
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    points = []
    for i in range(num_points):
        theta = math.radians(float(i) / num_points * 360.0)
        dist_rad = radius_km / R
        pt_lat = math.asin(math.sin(lat_rad) * math.cos(dist_rad) +
                           math.cos(lat_rad) * math.sin(dist_rad) * math.cos(theta))
        pt_lon = lon_rad + math.atan2(
            math.sin(theta) * math.sin(dist_rad) * math.cos(lat_rad),
            math.cos(dist_rad) - math.sin(lat_rad) * math.sin(pt_lat))
        points.append((math.degrees(pt_lon), math.degrees(pt_lat)))
    points.append(points[0])
    return points


def kml_to_mpl_color(kml_color):
    """Converts KML AABBGGRR hex color to matplotlib-compatible hex.
    
    KML format: AABBGGRR (alpha, blue, green, red)
    Matplotlib:  #RRGGBB
    """
    if len(kml_color) != 8:
        return '#888888'
    r = kml_color[6:8]
    g = kml_color[4:6]
    b = kml_color[2:4]
    return f'#{r}{g}{b}'


# ==========================================
#           GUI SELECTOR
# ==========================================

class MissionSelector:
    """Tkinter GUI for selecting and running scenarios.
    
    Discovers scenario modules dynamically. Currently supports
    heatwaves; coral bleaching and other boundary types plug in
    by adding imports below.
    """
    def __init__(self):
        # Import scenario modules
        from scenarios_heatwaves import SCENARIOS as HEAT_SCENARIOS
        self.all_scenarios = []
        self.all_scenarios.extend(HEAT_SCENARIOS)

        from scenarios_coral_bleaching import SCENARIOS as CORAL_SCENARIOS
        self.all_scenarios.extend(CORAL_SCENARIOS)

        from scenarios_western_heatwave_march_2026 import SCENARIOS as WESTERN_SCENARIOS
        self.all_scenarios.extend(WESTERN_SCENARIOS)

        self.root = tk.Tk()
        self.root.title("Earth System Generator v6.0")
        self.root.geometry("500x550")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 11), padding=10)

        lbl = tk.Label(self.root, text="Select Simulation Scenario",
                       font=("Helvetica", 14, "bold"))
        lbl.pack(pady=15)

        self.listbox = tk.Listbox(self.root, height=14, font=("Helvetica", 11))
        self.listbox.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        for scenario in self.all_scenarios:
            display = f"[{scenario.get('boundary_type', '?').upper()[:4]}] {scenario['name']}"
            self.listbox.insert(tk.END, display)

        btn = ttk.Button(self.root, text="Generate Assets (Teaser + KMZ) in data/",
                         command=self.run_selected)
        btn.pack(pady=20)

        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_lbl = tk.Label(self.root, textvariable=self.status_var,
                              font=("Helvetica", 9), fg="gray")
        status_lbl.pack(pady=5)

    def _status_update(self, msg):
        """Thread-safe status update for the GUI."""
        self.status_var.set(msg)
        self.root.update()

    def run_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a scenario.")
            return

        scenario = self.all_scenarios[selection[0]]

        try:
            run_scenario(scenario, status_callback=self._status_update)
            self.status_var.set("Ready")
            messagebox.showinfo("Success",
                                f"Generated Teaser and KMZ Blockbuster for:\n"
                                f"{scenario['name']} in data/")
        except Exception as e:
            self.status_var.set("Ready")
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = MissionSelector()
    app.root.mainloop()
