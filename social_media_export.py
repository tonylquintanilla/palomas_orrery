# social_media_export.py

"""
Social Media Export for Paloma's Orrery

Generates a second HTML file from an existing Plotly figure, optimized
for screen recording Instagram Reels and YouTube Shorts (9:16 portrait).

Layout:
  - Top 60%: Interactive 3D Plotly scene (no legend, axes, chrome)
  - Bottom 40%: Persistent info panel (object name + full hovertext)

The info panel displays the same rich hovertext that normally appears
in ephemeral Plotly tooltips, making it readable in video recordings.

Interaction model:
  - Hover (800ms delay): Primary in 16:9 landscape
  - Click (instant): Primary/backup in 9:16 portrait
  - Panel is "sticky" - stays on last object until new selection
  - Name-only Plotly tooltip serves as object pointer

Usage:
    from social_media_export import export_social_html
    fig = plot_objects()  # existing Plotly figure
    export_social_html(fig, output_path='my_orrery_social.html')

Author: Tony Quintanilla / Paloma's Orrery
"""

import json
import os
import re
import copy
import webbrowser
import platform
import tkinter as tk
from tkinter import filedialog


def _parse_hover_html(hover_html):
    """
    Parse a Plotly hover HTML string into structured panel data.

    The existing hover text follows this pattern:
      <b>ObjectName</b><br>
      optional RA/Dec line<br><br>
      Distance from Center: 1.234 AU<br>
      Velocity: 0.123 AU/day<br>
      ...

    Returns:
        dict with keys: name, subtitle, body
    """
    if not hover_html or not isinstance(hover_html, str):
        return None

    text = str(hover_html).strip()
    if not text:
        return None

    # Extract the bold name: <b>Name</b>
    name_match = re.match(r'<b>([^<]+)</b>', text)
    if name_match:
        name = name_match.group(1).strip()
        # Everything after the name tag is potential body content
        remainder = text[name_match.end():]
    else:
        # No bold tag - use first line as name
        lines = text.split('<br>')
        name = lines[0].strip()
        remainder = '<br>'.join(lines[1:])

    # Clean leading <br> tags from remainder
    remainder = re.sub(r'^(\s*<br>\s*)+', '', remainder, flags=re.IGNORECASE)

    # Try to extract a subtitle from RA/Dec line or first italic line
    subtitle = ''
    body = remainder

    # Check for RA/Dec as subtitle (common pattern)
    radec_match = re.match(r'\s*(RA\s*[^<]+Dec\s*[^<]+?)(<br>|$)', remainder, re.IGNORECASE)
    if radec_match:
        subtitle = radec_match.group(1).strip()
        body = remainder[radec_match.end():]
    else:
        # Check for italic subtitle: <i>text</i>
        italic_match = re.match(r'\s*<i>([^<]+)</i>', remainder)
        if italic_match:
            subtitle = italic_match.group(1).strip()
            body = remainder[italic_match.end():]

    # Clean leading <br> tags from body
    body = re.sub(r'^(\s*<br>\s*)+', '', body, flags=re.IGNORECASE)

    # Clean trailing <br> tags from body
    body = re.sub(r'(\s*<br>\s*)+$', '', body, flags=re.IGNORECASE)

    return {
        'name': name,
        'subtitle': subtitle,
        'body': body
    }


def _extract_trace_hover_data(trace):
    """
    Extract hover content from a single Plotly trace.

    Traces store hover content in the 'text' field as HTML strings.
    Returns a list of JSON strings (one per point) for customdata,
    plus a list of name-only strings for the simplified tooltip.

    Returns:
        tuple: (customdata_list, tooltip_text_list) or (None, None)
            if trace has no hover content
    """
    # Get the text field - could be a list or single value
    text_data = None
    if hasattr(trace, 'text'):
        text_data = trace.text
    elif isinstance(trace, dict):
        text_data = trace.get('text')

    if text_data is None:
        return None, None

    # Normalize to list
    if isinstance(text_data, str):
        text_list = [text_data]
    elif isinstance(text_data, (list, tuple)):
        text_list = list(text_data)
    else:
        return None, None

    customdata_list = []
    tooltip_list = []

    for hover_html in text_list:
        parsed = _parse_hover_html(hover_html)
        if parsed:
            customdata_list.append(json.dumps(parsed))
            tooltip_list.append(parsed['name'])
        else:
            # Keep original text as fallback
            customdata_list.append(json.dumps({
                'name': str(hover_html)[:50],
                'subtitle': '',
                'body': str(hover_html)
            }))
            tooltip_list.append(str(hover_html)[:50])

    return customdata_list, tooltip_list


def _prepare_social_figure(fig):
    """
    Create a modified copy of the Plotly figure optimized for social media.

    Modifications:
      - Routes hover content to customdata (JSON for panel)
      - Simplifies tooltip to name-only
      - Strips annotations, non-animation updatemenus, legend
      - Preserves animation play/pause buttons and date slider
      - Removes axis labels, grid, background
      - Increases marker size and orbit line width for visibility
      - Sets marker opacity to 0.99 (Plotly hover detection bug workaround)
      - Configures hoverlabel for minimal name-only tooltip

    Returns:
        dict: Modified figure as a dictionary (for JSON serialization)
    """
    # Deep copy the figure data as dict
    fig_dict = json.loads(fig.to_json())

    # ---- Modify traces ----
    for trace in fig_dict.get('data', []):

        # Check if this trace has hover content to route
        hoverinfo = trace.get('hoverinfo', '')
        hovertemplate = trace.get('hovertemplate', '')

        # Skip traces that explicitly skip hover
        if hoverinfo == 'skip' or hoverinfo == 'none':
            continue

        # Get text content for hover-enabled traces
        text_data = trace.get('text')
        if text_data is not None:
            # Normalize to list
            if isinstance(text_data, str):
                text_list = [text_data]
            else:
                text_list = list(text_data)

            customdata_list = []
            tooltip_list = []

            for hover_html in text_list:
                parsed = _parse_hover_html(hover_html)
                if parsed:
                    customdata_list.append(json.dumps(parsed))
                    tooltip_list.append(parsed['name'])
                else:
                    fallback = str(hover_html)[:80] if hover_html else ''
                    customdata_list.append(json.dumps({
                        'name': fallback,
                        'subtitle': '',
                        'body': str(hover_html) if hover_html else ''
                    }))
                    tooltip_list.append(fallback)

            # Route: customdata has full content for info panel click handler.
            # Hover tooltip is disabled - the panel is the only display.
            # text is cleared to prevent any fallback tooltip rendering.
            trace['customdata'] = customdata_list
            trace['text'] = ['' for _ in tooltip_list]
            trace['hoverinfo'] = 'none'
            trace['hovertemplate'] = None

        # ---- Visual enhancements for small screens ----
        marker = trace.get('marker', {})
        if marker:
            # Increase marker size
            size = marker.get('size')
            if isinstance(size, (int, float)):
                marker['size'] = size + 4
            elif isinstance(size, list):
                marker['size'] = [s + 4 if isinstance(s, (int, float)) else s for s in size]

            # Opacity 0.99 workaround for Plotly hover detection bug
            marker['opacity'] = 0.99
            trace['marker'] = marker

        # Thicker orbit lines
        line = trace.get('line', {})
        if line and trace.get('mode', '') in ('lines', 'lines+markers'):
            width = line.get('width', 2)
            if isinstance(width, (int, float)):
                line['width'] = max(width, 4)
            trace['line'] = line

    # ---- Modify layout ----
    layout = fig_dict.get('layout', {})

    # Strip legend
    layout['showlegend'] = False

    # Strip annotations (coordinate system box, etc.)
    layout['annotations'] = []

    # Filter updatemenus: KEEP animation controls (play/pause),
    # STRIP UI chrome (hover toggle, camera buttons, URL buttons)
    existing_menus = layout.get('updatemenus', [])
    animation_menus = []
    for menu in existing_menus:
        buttons = menu.get('buttons', [])
        # Animation menus have buttons with method='animate'
        has_animate = any(
            b.get('method') == 'animate' for b in buttons
        )
        if has_animate:
            # Restyle for social view - white text on dark background
            menu['font'] = {'color': '#f8fafc', 'size': 11}
            menu['bgcolor'] = '#1e293b'
            menu['bordercolor'] = '#334155'
            # Position in top-left of the scene
            menu['x'] = 0.02
            menu['y'] = 0.98
            menu['xanchor'] = 'left'
            menu['yanchor'] = 'top'
            # NOTE: redraw stays True so frames actually render.
            # Camera preservation is handled via JavaScript in
            # the HTML template (continuous layout.scene.camera sync).
            animation_menus.append(menu)
    layout['updatemenus'] = animation_menus

    # Keep sliders for animations (date scrubber), strip otherwise
    existing_sliders = layout.get('sliders', [])
    if existing_sliders and animation_menus:
        # Restyle sliders for social view
        for slider in existing_sliders:
            # Step label font: transparent + tiny so tick text is invisible,
            # but labels must remain as real date strings because Plotly's
            # currentvalue display reads them.
            slider['font'] = {'color': 'rgba(0,0,0,0)', 'size': 1}
            # Hide tick marks
            slider['tickcolor'] = 'rgba(0,0,0,0)'
            slider['ticklen'] = 0
            slider['bordercolor'] = '#334155'
            slider['borderwidth'] = 1
            slider['activebgcolor'] = '#475569'
            slider['bgcolor'] = '#1e293b'
            # Ensure currentvalue (date display above slider) is visible
            if 'currentvalue' not in slider:
                slider['currentvalue'] = {}
            slider['currentvalue']['visible'] = True
            slider['currentvalue']['prefix'] = 'Date: '
            slider['currentvalue']['font'] = {
                'color': '#f8fafc', 'size': 12
            }
            slider['currentvalue']['xanchor'] = 'left'
            # Keep step labels as real dates (required for currentvalue)
            # They are hidden by the transparent font above.
        layout['sliders'] = existing_sliders
    else:
        layout['sliders'] = []

    # Minimal margins - add bottom space if animation slider present
    has_slider = len(layout.get('sliders', [])) > 0
    layout['margin'] = {'l': 0, 'r': 0, 't': 0, 'b': 40 if has_slider else 0}

    # Dark background
    layout['paper_bgcolor'] = '#000000'
    layout['plot_bgcolor'] = '#000000'

    # Configure hoverlabel for name-only tooltip (small, unobtrusive)
    layout['hoverlabel'] = {
        'bgcolor': '#0f172a',
        'bordercolor': '#f8fafc',
        'font': {
            'family': 'Consolas, SF Mono, Fira Code, Courier New, monospace',
            'size': 16,
            'color': '#f8fafc'
        },
        'align': 'left'
    }

    # Clean up scene axes
    scene = layout.get('scene', {})
    for axis_key in ('xaxis', 'yaxis', 'zaxis'):
        axis = scene.get(axis_key, {})
        axis['showgrid'] = False
        axis['zeroline'] = False
        axis['showticklabels'] = False
        axis['showspikes'] = False
        axis['title'] = ''
        axis['showbackground'] = False
        axis['visible'] = False
        scene[axis_key] = axis

    scene['bgcolor'] = '#000000'
    scene['domain'] = {'x': [0, 1], 'y': [0, 1]}  # Full width (orrery offsets for UI buttons)    
    layout['scene'] = scene

    fig_dict['layout'] = layout

    # ---- Modify frame traces ----
    # Animation frames carry their own trace data that REPLACES the base
    # traces when a frame renders. Without this, the original hovertemplate
    # and full text content come back on every frame advance.
    for frame in fig_dict.get('frames', []):
        for trace in frame.get('data', []):
            text_data = trace.get('text')
            if text_data is not None:
                if isinstance(text_data, str):
                    text_list = [text_data]
                else:
                    text_list = list(text_data)

                customdata_list = []
                tooltip_list = []
                for hover_html in text_list:
                    parsed = _parse_hover_html(hover_html)
                    if parsed:
                        customdata_list.append(json.dumps(parsed))
                        tooltip_list.append(parsed['name'])
                    else:
                        fallback = str(hover_html)[:80] if hover_html else ''
                        customdata_list.append(json.dumps({
                            'name': fallback,
                            'subtitle': '',
                            'body': str(hover_html) if hover_html else ''
                        }))
                        tooltip_list.append(fallback)

                trace['customdata'] = customdata_list
                trace['text'] = ['' for _ in tooltip_list]
                trace['hoverinfo'] = 'none'
                trace['hovertemplate'] = None

    return fig_dict


def _build_social_html(fig_dict, plotly_js_src='cdn'):
    """
    Build the complete HTML string for the social media view.

    Parameters:
        fig_dict: Modified Plotly figure as dictionary
        plotly_js_src: 'cdn' for CDN link, 'offline' for embedded (larger file)

    Returns:
        str: Complete HTML document
    """
    # Plotly.js source
    if plotly_js_src == 'cdn':
        plotly_script = '<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>'
    else:
        # For offline, we'd need to embed - for now use CDN
        plotly_script = '<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>'

    # Serialize figure data
    fig_json = json.dumps(fig_dict, separators=(',', ':'))

    # Extract data, layout, and frames separately
    data_json = json.dumps(fig_dict.get('data', []), separators=(',', ':'))
    layout_json = json.dumps(fig_dict.get('layout', {}), separators=(',', ':'))
    frames_json = json.dumps(fig_dict.get('frames', []), separators=(',', ':'))

    # Build the HTML template
    # Using validated prototype design from prototyping session
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Paloma's Orrery - Social Media View</title>
{plotly_script}
<style>
  /* ===== RESET & BASE ===== */
  *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

  html, body {{
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: #000;
    color: #f8fafc;
    font-family: 'Consolas', 'SF Mono', 'Fira Code', 'Courier New', monospace;
    -webkit-font-smoothing: antialiased;
  }}

  /* ===== LAYOUT: 60/40 split, locked to 9:16 portrait ===== */
  .container {{
    /* Lock to 9:16 aspect ratio: width = height * 9/16 */
    height: 100vh;
    width: min(100vw, calc(100vh * 9 / 16));
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    background: #000;
  }}

  /* ===== 3D SCENE (top 60%) ===== */
  .scene-area {{
    flex: 6;
    position: relative;
    min-height: 0;
  }}

    #plotly-scene {{
    width: 100%;
    height: 100%;
  }}

  /* ===== DIVIDER ===== */
  .divider {{
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg,
      transparent 0%,
      #334155 15%,
      #64748b 50%,
      #334155 85%,
      transparent 100%
    );
    flex-shrink: 0;
  }}

  /* ===== INFO PANEL (bottom 40%) ===== */
  .info-panel {{
    flex: 4;
    display: flex;
    flex-direction: column;
    padding: 28px 40px 20px 40px;
    position: relative;
    overflow: hidden;
    min-height: 0;
  }}

  /* Header zone - object name */
  .panel-header {{
    flex-shrink: 0;
    margin-bottom: 16px;
    min-height: 60px;
  }}

  .object-name {{
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: 1px;
    line-height: 1.2;
    transition: opacity 0.18s ease;
  }}

  .object-subtitle {{
    font-size: clamp(16px, 2.2vw, 22px);
    font-weight: 400;
    color: #f8fafc;
    margin-top: 4px;
    font-style: italic;
    line-height: 1.3;
    transition: opacity 0.18s ease;
  }}

  /* Body zone - full content */
  .panel-body {{
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    font-size: clamp(16px, 2.4vw, 24px);
    line-height: 1.5;
    color: #f8fafc;
    padding-right: 8px;
    transition: opacity 0.18s ease;

    /* Scrollbar styling - subtle */
    scrollbar-width: thin;
    scrollbar-color: #334155 transparent;
  }}

  .panel-body::-webkit-scrollbar {{
    width: 4px;
  }}
  .panel-body::-webkit-scrollbar-track {{
    background: transparent;
  }}
  .panel-body::-webkit-scrollbar-thumb {{
    background: #334155;
    border-radius: 2px;
  }}

  /* Style HTML content in panel */
  .panel-body b {{
    color: #f8fafc;
    font-weight: 600;
  }}

  .panel-body i {{
    color: #cbd5e1;
  }}

  .panel-body br + br {{
    display: block;
    content: '';
    margin-top: 8px;
  }}

  /* ===== BRANDING ===== */
  .branding {{
    position: absolute;
    bottom: 16px;
    right: 40px;
    font-size: 16px;
    color: #334155;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
  }}

  /* ===== INITIAL STATE ===== */
  .panel-empty-state {{
    color: #475569;
    font-size: clamp(16px, 2.2vw, 22px);
    font-style: italic;
    margin-top: 40px;
    text-align: center;
  }}

  /* ===== FADE TRANSITION ===== */
  .fading {{
    opacity: 0.3;
  }}

  /* ===== HIDE PLOTLY CHROME ===== */
  .modebar-container {{ display: none !important; }}

</style>
</head>
<body>

<div class="container">
  <!-- 3D Scene -->
  <div class="scene-area">
    <div id="plotly-scene"></div>
  </div>

  <!-- Divider -->
  <div class="divider"></div>

  <!-- Info Panel -->
  <div class="info-panel">
    <div class="panel-header">
      <div class="object-name" id="obj-name">Paloma's Orrery</div>
      <div class="object-subtitle" id="obj-subtitle">Hover over an object to explore</div>
    </div>
    <div class="panel-body" id="obj-body">
      <div class="panel-empty-state">
        Point at any planet, moon, or orbit to see its data here.
      </div>
    </div>
    <div class="branding">Paloma's Orrery</div>
  </div>
</div>

<script>
// ===== RENDER PLOTLY FIGURE =====
document.addEventListener('DOMContentLoaded', function() {{

  var data = {data_json};
  var layout = {layout_json};
  var frames = {frames_json};

  var config = {{
    displayModeBar: false,
    scrollZoom: true,
    responsive: true,
    doubleClick: false
  }};

  // Force layout to fill the scene container
  layout.autosize = true;

  Plotly.newPlot('plotly-scene', data, layout, config).then(function() {{
    // Add frames if animation
    if (frames && frames.length > 0) {{
      Plotly.addFrames('plotly-scene', frames);

      // ===== CAMERA PRESERVATION FOR ANIMATIONS =====
      // Plotly 3D redraw rebuilds WebGL from layout.scene.camera,
      // resetting the user's view. We continuously track the camera
      // and inject it back into the layout before each frame renders,
      // then restore it after each redraw completes.
      var plotDiv = document.getElementById('plotly-scene');
      var lastCamera = null;

      // Continuously track camera position (100ms poll)
      setInterval(function() {{
        try {{
          var scene = plotDiv._fullLayout.scene._scene;
          if (scene) {{
            lastCamera = scene.getCamera();
          }}
        }} catch(e) {{}}
      }}, 100);

      // Before each frame renders, inject our camera into the layout
      plotDiv.on('plotly_animatingframe', function(eventData) {{
        if (lastCamera) {{
          try {{
            plotDiv._fullLayout.scene.camera = lastCamera;
            plotDiv.layout.scene.camera = lastCamera;
          }} catch(e) {{}}
        }}
      }});

      // After each frame, restore camera if it got reset
      plotDiv.on('plotly_afterplot', function() {{
        if (lastCamera) {{
          try {{
            var scene = plotDiv._fullLayout.scene._scene;
            if (scene) {{
              scene.setCamera(lastCamera);
            }}
          }} catch(e) {{}}
        }}
      }});
    }}
    initEventListeners();
  }});

  // ===== RESIZE HANDLER =====
  // Forces Plotly to recalculate WebGL hover coordinates after window resize.
  // Critical for 9:16 where resize can break hover detection.
  var resizeTimer = null;
  window.addEventListener('resize', function() {{
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {{
      var plotDiv = document.getElementById('plotly-scene');
      Plotly.relayout(plotDiv, {{
        'scene.camera': plotDiv._fullLayout.scene._scene.getCamera()
      }});
    }}, 250);
  }});

}});

// ===== PANEL UPDATE LOGIC =====
var hoverTimer = null;
var currentObjectData = null;
var HOVER_DELAY = 800; // ms - throttle for smooth experience

var nameEl, subtitleEl, bodyEl;

function initEventListeners() {{
  nameEl = document.getElementById('obj-name');
  subtitleEl = document.getElementById('obj-subtitle');
  bodyEl = document.getElementById('obj-body');

  var plotlyDiv = document.getElementById('plotly-scene');

  // Hover: throttled panel update (primary in 16:9)
  plotlyDiv.on('plotly_hover', function(data) {{
    var point = data.points[0];
    if (!point.customdata) return;

    var objectData = point.customdata;

    // Same object - don't restart timer
    if (objectData === currentObjectData) return;

    // Clear pending timer
    if (hoverTimer) clearTimeout(hoverTimer);

    // New timer
    hoverTimer = setTimeout(function() {{
      currentObjectData = objectData;
      updatePanel(objectData);
    }}, HOVER_DELAY);
  }});

  plotlyDiv.on('plotly_unhover', function() {{
    if (hoverTimer) {{
      clearTimeout(hoverTimer);
      hoverTimer = null;
    }}
    // Panel stays showing last object (sticky)
  }});

  // Click: immediate panel update (backup, essential for 9:16
  // where hover detection is unreliable after resize)
  plotlyDiv.on('plotly_click', function(data) {{
    var point = data.points[0];
    if (!point.customdata) return;

    // Clear any pending hover timer
    if (hoverTimer) {{
      clearTimeout(hoverTimer);
      hoverTimer = null;
    }}

    var objectData = point.customdata;
    currentObjectData = objectData;
    updatePanel(objectData);
  }});
}}

function updatePanel(data) {{
  try {{
    var parsed = (typeof data === 'string') ? JSON.parse(data) : data;

    // Fade out
    nameEl.classList.add('fading');
    subtitleEl.classList.add('fading');
    bodyEl.classList.add('fading');

    setTimeout(function() {{
      nameEl.textContent = parsed.name || '';
      subtitleEl.textContent = parsed.subtitle || '';
      bodyEl.innerHTML = parsed.body || '';

      // Auto-size font for body
      autoSizeFont();

      // Fade in
      nameEl.classList.remove('fading');
      subtitleEl.classList.remove('fading');
      bodyEl.classList.remove('fading');
    }}, 180);

  }} catch(e) {{
    // Fallback: display raw content
    bodyEl.innerHTML = String(data);
  }}
}}

function autoSizeFont() {{
  // Start at base size, shrink if content overflows
  var baseFontSize = 24;
  var minFontSize = 16;
  var fontSize = baseFontSize;

  bodyEl.style.fontSize = fontSize + 'px';

  // Check overflow against available panel height
  var panelEl = bodyEl.parentElement;
  var headerEl = document.querySelector('.panel-header');
  var maxHeight = panelEl.offsetHeight - headerEl.offsetHeight - 80;

  while (bodyEl.scrollHeight > maxHeight && fontSize > minFontSize) {{
    fontSize -= 1;
    bodyEl.style.fontSize = fontSize + 'px';
  }}
}}
</script>
</body>
</html>
"""
    return html


def get_trace_names(fig):
    """
    Get a list of trace names from a Plotly figure.

    Returns a list of (index, name) tuples for all traces.
    Traces without a name get a generated label.

    Parameters:
        fig: Plotly figure object

    Returns:
        list of (int, str): (trace_index, trace_name) pairs
    """
    names = []
    for i, trace in enumerate(fig.data):
        name = getattr(trace, 'name', None) or ''
        if not name:
            # Generate a label from trace type and index
            trace_type = getattr(trace, 'type', 'trace')
            name = f"{trace_type} #{i}"
        names.append((i, name))
    return names


def show_trace_selection_dialog(fig, parent=None):
    """
    Show a dialog with checkboxes for each trace in the figure.

    All traces are checked by default. The user unchecks traces
    they want excluded from the social media export.

    Parameters:
        fig: Plotly figure object
        parent: Parent Tk window (optional, for proper stacking)

    Returns:
        list of str: Names of selected traces, or None if cancelled.
    """
    import tkinter as tk
    import platform

    trace_names = get_trace_names(fig)
    if not trace_names:
        return None

    result = {'confirmed': False, 'selected': []}

    # Create dialog window
    if parent:
        dialog = tk.Toplevel(parent)
    else:
        dialog = tk.Tk()

    dialog.title("Social Media View - Select Traces")
    dialog.geometry("500x600")
    dialog.resizable(True, True)

    # Try to keep on top
    try:
        dialog.attributes('-topmost', True)
    except Exception:
        pass

    # Instructions
    instructions = tk.Label(
        dialog,
        text="Select which traces to include in the social media view.\n"
             "Uncheck traces you want to hide.",
        justify='left',
        wraplength=460,
        pady=10,
        padx=10
    )
    instructions.pack(fill='x')

    # Scrollable frame for checkboxes
    container = tk.Frame(dialog)
    container.pack(fill='both', expand=True, padx=10)

    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        '<Configure>',
        lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    # Mouse wheel scrolling
    def on_mousewheel(event):
        if platform.system() == 'Darwin':
            canvas.yview_scroll(-1 * event.delta, 'units')
        else:
            canvas.yview_scroll(-1 * (event.delta // 120), 'units')

    canvas.bind_all('<MouseWheel>', on_mousewheel)

    # Create checkbox variables
    check_vars = []
    for idx, name in trace_names:
        var = tk.IntVar(value=1)  # All checked by default
        check_vars.append((idx, name, var))

        cb = tk.Checkbutton(
            scrollable_frame,
            text=name,
            variable=var,
            anchor='w'
        )
        cb.pack(fill='x', padx=5, pady=1)

    # Select All / Deselect All buttons
    toggle_frame = tk.Frame(dialog)
    toggle_frame.pack(fill='x', padx=10, pady=(5, 0))

    def select_all():
        for _, _, var in check_vars:
            var.set(1)

    def deselect_all():
        for _, _, var in check_vars:
            var.set(0)

    tk.Button(toggle_frame, text="Select All", command=select_all, width=12).pack(side='left', padx=5)
    tk.Button(toggle_frame, text="Deselect All", command=deselect_all, width=12).pack(side='left', padx=5)

    # Count label
    count_label = tk.Label(toggle_frame, text=f"{len(trace_names)} traces")
    count_label.pack(side='right', padx=5)

    # OK / Cancel buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack(fill='x', padx=10, pady=10)

    def on_ok():
        result['confirmed'] = True
        result['selected'] = [
            name for _, name, var in check_vars if var.get() == 1
        ]
        dialog.destroy()

    def on_cancel():
        result['confirmed'] = False
        dialog.destroy()

    tk.Button(button_frame, text="Export", command=on_ok, width=12,
              bg='gray90', fg='blue').pack(side='left', padx=5)
    tk.Button(button_frame, text="Cancel", command=on_cancel, width=12).pack(side='left', padx=5)

    # Handle window close
    dialog.protocol('WM_DELETE_WINDOW', on_cancel)

    # Unbind mousewheel on close to avoid errors
    def cleanup():
        try:
            canvas.unbind_all('<MouseWheel>')
        except Exception:
            pass

    dialog.bind('<Destroy>', lambda e: cleanup())

    # Wait for dialog
    dialog.wait_window()

    if result['confirmed']:
        return result['selected']
    return None


def _show_social_save_dialog():
    """
    Show a save-as dialog for the social media HTML export.

    Uses the same pattern as save_utils: remembers last directory,
    defaults to Documents folder, provides a timestamped default name.

    Returns:
        str or None: Chosen file path, or None if cancelled.
    """
    import threading as _threading

    # macOS thread safety: skip dialog if not main thread
    if platform.system() == 'Darwin' and _threading.current_thread() is not _threading.main_thread():
        # Fall back to timestamped name in current directory
        from datetime import datetime as _dt
        ts = _dt.now().strftime('%Y%m%d_%H%M')
        fallback = f"social_view_{ts}.html"
        print(f"[SOCIAL MEDIA] macOS thread safety: saving as {fallback}")
        return fallback

    root = None
    try:
        from datetime import datetime as _dt
        ts = _dt.now().strftime('%Y%m%d_%H%M')
        default_name = f"social_view_{ts}.html"

        # Try to use save_utils initial directory if available
        try:
            from save_utils import _get_initial_directory, _update_last_directory
            initial_dir = _get_initial_directory()
        except ImportError:
            # Fallback: Documents folder
            if platform.system() == 'Windows':
                initial_dir = os.path.join(os.path.expanduser('~'), 'Documents')
            else:
                initial_dir = os.path.expanduser('~')
            _update_last_directory = None

        if not os.path.isdir(initial_dir):
            initial_dir = os.getcwd()

        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)

        file_path = filedialog.asksaveasfilename(
            parent=root,
            title="Save Social Media View",
            initialdir=initial_dir,
            initialfile=default_name,
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )

        if file_path:
            # Update save_utils directory memory if available
            if _update_last_directory is not None:
                _update_last_directory(file_path)
            return file_path

        return None

    except Exception as e:
        print(f"[SOCIAL MEDIA] Save dialog error: {e}", flush=True)
        # Fall back to timestamped name in current directory
        from datetime import datetime as _dt
        ts = _dt.now().strftime('%Y%m%d_%H%M')
        return f"social_view_{ts}.html"

    finally:
        try:
            if root:
                root.destroy()
        except Exception:
            pass


def export_social_html(fig, output_path=None, open_browser=True,
                       plotly_js='cdn', trace_names=None):
    """
    Export a Plotly figure as a social-media-optimized HTML file.

    Creates a 9:16 portrait layout with:
      - Top 60%: Interactive 3D scene (stripped of UI chrome)
      - Bottom 40%: Persistent info panel (displays full hovertext)

    The resulting HTML is designed for screen recording with Clipchamp
    or similar tools, producing Instagram Reels or YouTube Shorts.

    Save behavior:
      - If output_path is provided: saves directly (no dialog)
      - If output_path is None: shows save dialog via save_utils pattern

    Parameters:
        fig: Plotly figure object (from plot_objects() or animate_objects())
        output_path: Output file path. If None, shows save dialog.
        open_browser: If True, opens the file in the default browser.
        plotly_js: 'cdn' for CDN-hosted Plotly.js (~10KB file),
                   'offline' for embedded (~5MB file, works without internet)
        trace_names: List of trace names to include. If None, all traces
                     are included. Use show_trace_selection_dialog() to
                     get this list from a GUI dialog.

    Returns:
        str: Path to the generated HTML file, or None on error/cancel.

    Example:
        from social_media_export import export_social_html

        fig = plot_objects()  # existing Plotly figure
        path = export_social_html(fig)
        # Shows save dialog, then opens in browser

        # Direct save (no dialog):
        export_social_html(fig, output_path='my_social.html')

        # With trace filtering:
        selected = show_trace_selection_dialog(fig)
        if selected is not None:
            export_social_html(fig, trace_names=selected)
    """
    try:
        print(f"[SOCIAL MEDIA] Preparing social media view...", flush=True)

        # Filter traces if trace_names provided
        if trace_names is not None:
            import plotly.graph_objects as go
            filtered_data = [
                t for t in fig.data
                if (getattr(t, 'name', '') or '') in trace_names
            ]
            fig_filtered = go.Figure(data=filtered_data, layout=fig.layout)
            # Preserve frames if animation
            if hasattr(fig, 'frames') and fig.frames:
                fig_filtered.frames = fig.frames
            kept = len(filtered_data)
            total = len(fig.data)
            print(f"[SOCIAL MEDIA] Trace filter: {kept}/{total} traces selected", flush=True)
        else:
            fig_filtered = fig

        # Prepare the modified figure
        fig_dict = _prepare_social_figure(fig_filtered)

        # Count traces with panel data
        panel_traces = sum(
            1 for t in fig_dict.get('data', [])
            if t.get('customdata') and t.get('hoverinfo') != 'skip'
        )
        total_traces = len(fig_dict.get('data', []))
        print(f"[SOCIAL MEDIA] {panel_traces}/{total_traces} traces routed to info panel", flush=True)

        # Build HTML
        html_content = _build_social_html(fig_dict, plotly_js_src=plotly_js)

        # ---- Save: dialog or direct ----
        if output_path is not None:
            # Direct save (no dialog) - for programmatic use
            if not output_path.endswith('.html'):
                output_path += '.html'
            save_path = output_path
        else:
            # Show save dialog - matches save_utils pattern
            save_path = _show_social_save_dialog()
            if save_path is None:
                print("[SOCIAL MEDIA] Save cancelled by user.", flush=True)
                return None

        # Write file
        with open(save_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html_content)

        file_size_kb = os.path.getsize(save_path) / 1024
        print(f"[SOCIAL MEDIA] Saved: {save_path} ({file_size_kb:.0f} KB)", flush=True)
        print(f"[SOCIAL MEDIA] Open in Chrome, resize to 9:16, screen record.", flush=True)

        # Open in browser
        if open_browser:
            webbrowser.open('file://' + os.path.abspath(save_path))

        return save_path

    except Exception as e:
        print(f"[SOCIAL MEDIA] Error: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return None
