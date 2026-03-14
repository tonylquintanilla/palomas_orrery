# Social Media Export

Export interactive Paloma's Orrery visualizations as portrait-format HTML files optimized for Instagram Reels and YouTube Shorts.

## Overview

The Social Media Export creates a standalone HTML file from any existing orrery plot. The layout is designed for 9:16 portrait screen recording: the top 60% shows the interactive 3D scene (stripped of UI chrome), and the bottom 40% shows a persistent info panel that displays the same rich data normally hidden in ephemeral Plotly tooltips.

This solves a fundamental problem with sharing 3D visualizations on social media: hover text disappears too fast for video, and landscape plots waste most of the portrait frame. The social view makes both the visuals and the data readable in a vertical recording.

## How to Use

1. Plot any solar system view in Paloma's Orrery (static or animated)
2. Click **Social Media Export** in the GUI
3. A trace selection dialog appears -- choose which objects to include
4. A save dialog opens with a timestamped default name (e.g., `social_view_20260204_1530.html`)
5. The HTML opens automatically in your default browser

The exported HTML is a self-contained file. No Python or special software needed to view it -- just a web browser.

## Recording a Reel

The HTML layout is locked to 9:16 portrait aspect ratio. When the browser window is wider than 9:16, the content column centers itself with invisible black margins on the sides. To record:

1. Open the exported HTML in Chrome
2. Start your screen recording tool (Clipchamp, OBS, etc.) set to 1080x1920 or any 9:16 resolution
3. Record the browser window -- the black margins blend seamlessly into the portrait frame
4. For animated plots, use Play/Pause buttons or the date slider to control playback
5. Click or hover over objects to populate the info panel during recording

No cropping needed. The margins are pure black, identical to Instagram's letterbox color.

## Layout

The 9:16 view has two sections:

**Scene area (top 60%)** -- The 3D Plotly visualization with all UI chrome removed: no legend, no axis labels, no grid lines, no Plotly toolbar. Markers are enlarged and orbit lines thickened for visibility at portrait resolution. The camera angle from your original plot is preserved.

**Info panel (bottom 40%)** -- Displays object name, coordinates, distance, velocity, and other data from the selected object. The panel is "sticky" -- it holds the last selected object until you choose a new one. Font sizes auto-scale to fit the panel height. Content that exceeds the panel area becomes scrollable.

A subtle gradient divider separates the two sections.

## Interaction

Two input methods populate the info panel:

**Click (instant)** -- Primary method for portrait/touch recording. Tap any object marker and the panel updates immediately.

**Hover (800ms delay)** -- Secondary method. Hovering over an object for 800 milliseconds updates the panel. The delay prevents accidental updates while navigating the 3D scene.

The panel stays on the last object until you interact with a new one. This means you can rotate the 3D view, zoom in and out, and the panel keeps showing your selected object's data.

## Animation Support

If the original plot was animated (time-stepping), the social view preserves the animation with simplified controls:

**Play / Pause buttons** -- Large, readable text buttons (no icons) positioned in the top-left corner of the scene area. The currently active button is highlighted.

**Date slider** -- A styled range slider below the scene shows the current animation date. Drag to scrub through time.

**Camera preservation** -- The camera angle is locked during animation playback. Plotly's default behavior resets the camera on each frame; the social view overrides this so your chosen viewing angle stays fixed throughout the animation.

## Trace Selection

The trace selection dialog lets you choose which objects appear in the social view. This is useful for focusing on specific planets, spacecraft, or features without the clutter of the full plot. The dialog shows all named traces from the current plot as checkboxes with Select All / Deselect All controls.

Objects not selected are removed entirely from the exported HTML, keeping the file size smaller and the scene cleaner.

## Technical Details

**Module:** `social_media_export.py` (1,165 lines)

**Dependencies:** Only standard Plotly and Python libraries. No additional packages required beyond what Paloma's Orrery already uses.

**File size:** Approximately 10 KB with CDN-hosted Plotly.js, or approximately 5 MB with offline embedded Plotly.js. The CDN version requires internet to view; the offline version works anywhere.

**CSS layout:** The 9:16 constraint uses `width: min(100vw, calc(100vh * 9 / 16))` with `margin: 0 auto`, centering the content column regardless of browser window dimensions.

**Hover suppression:** Native Plotly tooltips are suppressed on both base traces and animation frame traces. Hover and click events still fire for panel updates via `plotly_hover` and `plotly_click` JavaScript listeners.

**Save integration:** Uses the same directory memory as the rest of Paloma's Orrery via `save_utils`. The save dialog remembers your last save location within each session. macOS thread safety is handled with automatic fallback.

## Programmatic Use

The module can be used directly from Python:

```python
from social_media_export import export_social_html, show_trace_selection_dialog

fig = plot_objects()  # any Plotly figure from the orrery

# With trace selection dialog:
selected = show_trace_selection_dialog(fig)
if selected is not None:
    export_social_html(fig, trace_names=selected)

# Direct save (no dialogs):
export_social_html(fig, output_path='my_social.html')

# Offline version (no internet needed to view):
export_social_html(fig, output_path='my_social.html', plotly_js='offline')
```

## Author

Created by Tony Quintanilla with Claude AI assistance, February 2026.
