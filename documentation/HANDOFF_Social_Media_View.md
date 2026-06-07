# HANDOFF: Social Media Presentation View for Paloma's Orrery

## Project Overview

Paloma's Orrery is a Python-based astronomical visualization application that generates interactive 3D plots using Plotly. The plots open in a browser as HTML files. Tony shares visualizations on Instagram (@palomas_orrery) and is exploring YouTube Shorts.

**The problem:** Tony currently screen-records the Plotly visualizations and crops them for social media (Instagram posts/reels, YouTube Shorts). The 3D visuals work great, but the **hovertext is the educational payload** -- rich astronomical data, physics explanations, storytelling -- and it's trapped in ephemeral tooltips that are hard to read, get truncated, block the view, and are lost in video recordings.

**The solution:** An optional "Social Media View" that generates a second HTML file alongside the normal visualization. Same Plotly figure, different presentation -- optimized for screen recording in portrait format with the hovertext displayed in a persistent, readable text panel.

## What This Is NOT

- NOT a replacement for the existing visualization interface
- NOT a Dash web app (too heavy for this purpose)
- NOT a video rendering pipeline (Tony already has a screen recording workflow with Clipchamp)
- NOT a mobile app

## What This IS

A **presentation mode** -- a custom HTML wrapper around the existing Plotly figure that:

1. Sets the page to **9:16 (1080x1920)** or **1:1 (1080x1080)** dimensions
2. Places the **3D scene in the top portion**, filling the width
3. Places a **styled text panel below** the scene
4. **Strips chrome** -- no legend, no coordinate system box, no URL buttons, no title (or minimal title)
5. When user hovers/clicks any object, the **text panel updates** with the full hovertext content -- properly formatted, readable font, no truncation
6. Dark background throughout (matches existing aesthetic)
7. Tony opens this in Chrome, screen records, done

## Visual Layout (9:16)

```
+------------------------+  1080px wide
|                        |
|     3D Plotly Scene    |  ~60% height
|     (interactive)      |
|                        |
|                        |
+------------------------+
|                        |
|  Object Name (large)   |  ~40% height
|  Distance: 0.002 AU   |
|  Velocity: 3,734 km/hr |
|  Period: 27.32 days    |
|                        |
|  (full hover content,  |
|   formatted, readable) |
|                        |
+------------------------+  1920px tall
```

## Technical Approach

### Architecture

The existing code flow:
1. `plot_objects()` or `animate_objects()` builds a Plotly `fig` object
2. `fig.to_html()` generates an HTML file
3. Browser opens it

The new flow (additive, not replacing):
1. Same `fig` object is built (no changes to visualization code)
2. If "Social Media View" is enabled (checkbox/button in GUI), call `export_social_html(fig, format='9:16')`
3. This function writes a SECOND HTML file using a custom template
4. Browser opens it alongside or instead of the normal view

### Key Technical Details

**Plotly hover event capture (JavaScript):**
```javascript
// Plotly emits hover events with the trace data
plotlyDiv.on('plotly_hover', function(data) {
    var point = data.points[0];
    var hoverText = point.customdata || point.text;
    document.getElementById('info-panel').innerHTML = hoverText;
});

// Also capture click for "sticky" selection
plotlyDiv.on('plotly_click', function(data) {
    var point = data.points[0];
    var hoverText = point.customdata || point.text;
    document.getElementById('info-panel').innerHTML = hoverText;
});
```

**The hovertext is already built.** Every trace in the Plotly figure has rich HTML hover content stored in `text` and `customdata` fields. The text panel just needs to display it in a different location. No new content generation required.

**Plotly layout modifications for the social view:**
- `showlegend: false`
- Remove annotations (coordinate system box, URL buttons)
- Set `margin` to minimal values
- Set figure height to ~60% of container
- Hide modebar or make it minimal
- Keep `hovermode` active but set `hoverinfo: 'none'` on traces (suppress tooltip, route to panel instead)

**Or alternatively:** Keep hover tooltips AND populate the panel. The tooltip gives quick context while interacting; the panel gives the full readable version for the recording.

### Hovertext Format

The existing hovertext is HTML-formatted (Plotly supports HTML in hover). Example from the Earth-Moon Barycenter marker:

```html
<b>Earth-Moon Barycenter</b><br>
<i>The balance point of the Earth-Moon system</i><br><br>
<b>Location:</b><br>
~4,670 km from Earth's center (~0.0000312 AU)<br>
~1,700 km below the surface<br>
Between the outer core and lower mantle<br><br>
<b>Earth wobbles around this point every 27.32 days</b><br>
...
```

This HTML renders directly in a div -- no parsing needed. The text panel just receives it via innerHTML.

### Implementation Options

**Option 1: Pure HTML/JS template (recommended)**
- A single HTML template string embedded in the Python code
- The Plotly figure JSON is injected into the template
- JavaScript handles hover-to-panel routing
- No additional dependencies
- Simplest to maintain

**Option 2: Dash app**
- More framework overhead
- Tony has considered Dash for a future web interface
- Overkill for this specific use case
- But could be a stepping stone if the web interface becomes a priority

### Where to Add the Code

**New function in the codebase:**
A function like `export_social_html(fig, format='9:16', output_path=None)` that:
1. Takes the existing Plotly figure object
2. Serializes it to JSON (`fig.to_json()`)
3. Injects it into an HTML template with the text panel layout
4. Writes the HTML file
5. Optionally opens it in browser

**GUI integration:**
- A checkbox or button in the GUI panel (near the existing "Plot" button)
- Could be "Social Media View" checkbox that, when checked, generates the social HTML alongside the normal one
- Or a separate button "Export Social View" that generates it on demand from the current figure
- A radio button or dropdown for format: "9:16 (Reels/Shorts)" vs "1:1 (Instagram Post)"

### Files That Would Be Modified

- `palomas_orrery.py` -- GUI checkbox/button, call to export function
- NEW file: `social_media_export.py` (or similar) -- the export function and HTML template
- No changes to any visualization, data, or orbital mechanics code

## Existing Codebase Context

### Key Files to Understand
- `palomas_orrery.py` -- Main GUI application (~8800 lines). Contains `plot_objects()` and `animate_objects()` functions that build the Plotly figure
- `visualization_core.py` -- Core Plotly figure setup, layout, formatting
- `planet_visualization.py` -- Planet-specific visualization
- `idealized_orbits.py` -- Osculating orbit plotting (where hover text is built for orbital elements)

### How Hover Text Is Built
Hover text is constructed throughout the codebase in various places:
- Object position hover: built in `palomas_orrery.py` during `plot_objects()` (distance, velocity, RA/Dec, mission info)
- Osculating orbit hover: built in `idealized_orbits.py` (orbital elements, educational text)
- Apsidal markers hover: built in `apsidal_markers.py` (perihelion/aphelion data)
- Shell hover: built in various `*_visualization_shells.py` files (planetary interior layers)

All hover text is stored in the trace's `text` and/or `customdata` fields as HTML strings.

### Animation Considerations
The existing animation system uses Plotly's built-in animation frames (`fig.frames`). In the social view:
- Animation should still work (Plotly handles it in-browser)
- The text panel would need to update during animation when user hovers
- The play/pause controls could be kept or simplified
- Frame-by-frame hover updates might need the `plotly_animated` or `plotly_animating` events

### Tony's Recording Workflow
1. Sets up visualization in the orrery GUI
2. Plots or animates
3. Screen records with Clipchamp (previously OBS)
4. Crops to 1:1 or 9:16
5. Uploads to Instagram or YouTube Shorts

The social view eliminates step 4 (cropping) and solves the hovertext readability problem.

## Design Preferences

- **Dark background** -- consistent with existing visualizations (black/dark gray)
- **Clean, minimal** -- the 3D scene is the star
- **Readable text** -- the whole point is making the data legible on a phone screen
- **No emoji or decorative elements** -- scientific aesthetic
- **ASCII only in code** -- Windows compatibility requirement
- **LF line endings** -- cross-platform standard for the project

## What Success Looks Like

Tony can:
1. Create a visualization as normal
2. Click one button to get a social-media-ready view
3. Open it in Chrome
4. Screen record while interacting with the 3D scene
5. The hovertext/data is always visible and readable in the recording
6. Upload directly to Instagram/YouTube Shorts with minimal post-processing

## Questions to Resolve in Implementation

1. **Suppress hover tooltip or keep both?** Show tooltip AND panel, or route exclusively to panel?
2. **Click-to-lock behavior?** Click an object to "lock" its info in the panel, hover others to preview?
3. **Animation text updates:** How to handle text panel during automated animation playback?
4. **Font sizing:** What size makes text readable on a phone screen when recorded at 1080px wide?
5. **Transition effects:** Smooth fade when text panel content changes, or instant swap?
6. **Title/branding:** Include "Paloma's Orrery" watermark or title in the social view?
7. **Object name highlighting:** When hovering, should the object name be larger/highlighted in the panel?

## Reference: Protocol Principles That Apply

From the project protocol (v3.8):
- This is a NEW feature -- **agentic mode** is appropriate
- **Optional, not replacement** -- additive to existing functionality  
- **Zero changes to core visualization code** -- the social view wraps what already exists
- **Test empirically** -- screen record the result and verify it looks right on a phone
- **ASCII only** in Python source code
- **LF line endings** preferred
