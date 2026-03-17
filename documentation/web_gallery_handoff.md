# Paloma's Orrery - Web Gallery Initiative

## Session Handoff | February 5 - March 8, 2026 | Claude Opus 4.6

---

## The Vision

Transform Paloma's Orrery from a local Python application into a shareable
web experience. What was a complex desktop environment becomes a link anyone
can tap -- in a text message, on Instagram, in an email -- and instantly
explore interactive astronomical visualizations in their browser.

**The moment that crystallized it**: Tony texted Paloma a screenshot of
Earth's orbit on her birthday. The vision is: next time, send a link. She
taps it, and the 3D solar system opens on her phone, rotatable, zoomable,
alive. No download, no install, no "is this safe?"

## Architecture Decided

Current pipeline (as of Session 27):
```
Desktop App (Python/Plotly)
    |
    v
Gallery Studio (per-plot curation, preview, presets)
    |
    v
json_converter.py (HTML -> JSON extraction, reads gallery_config.json,
                   detects Studio features: toggle annotations, nav controls, frames)
    |
    v
JSON files + gallery_metadata.json (with optional subcategory fields)
    |
    v
GitHub Repository (tonyquintanilla.github.io)
    |
    v
index.html Gallery Viewer (Plotly.js, reads gallery_config.json for colors,
                           renders collapsible subcategory groups)
    |
    v
Anyone with a browser, any device

Gallery management:
    gallery_config.json  <-- single source of truth for categories
    gallery_editor.py    <-- GUI for editing metadata, categories, subcategories, ordering
```

Target pipeline (Session 12 refactor):
```
Desktop App (Python/Plotly)
    |
    v
Gallery Studio (ALL curation decisions -- WYSIWYG authority)
    |-- Preview as Studio (portrait/social output)
    |-- Preview as Gallery (simulates index rendering)
    |
    v
json_converter.py (HTML -> JSON extraction, no transforms)
    |
    v
JSON files + gallery_metadata.json
    |
    v
index.html (dumb renderer -- structural viewer only, no content opinions)
    |
    v
Anyone with a browser, any device
```

### Key Design Decisions

1. **GitHub Pages over Dash hosting** - No server to maintain, free forever,
   always on, no sleeping apps, no monthly fees. The gallery viewer runs
   entirely in the browser using Plotly.js from CDN.

2. **GitHub Pages as main website** - Replaces Google Sites. Consolidates
   website + code repo + releases + gallery into one platform with one
   workflow (GitHub Desktop). No user base to migrate -- just update
   Instagram bio and redirect.

3. **Responsive design** - Desktop (16:9) shows sidebar + visualization.
   Mobile (9:16) collapses sidebar into hamburger menu, visualization goes
   full screen. Critical because Instagram audience arrives on phones.
   Inspired by social_media_export.py's portrait-first approach.

4. **Shareable URLs per visualization** - Each visualization gets a direct
   link (e.g., tonyquintanilla.github.io/#earth-birthday-2025).
   Links unfurl with preview thumbnail in iMessage/WhatsApp. Every
   visualization becomes a shareable moment.

5. **JSON pipeline stays identical** - json_converter.py output works for
   both local preview and GitHub Pages deployment. No format changes needed.

6. **Separate repositories** - App and website are separate repos. The app
   repo stays pure for users who download it. The website repo holds the
   gallery viewer, data, and publishing tools. Both are public (required
   for free GitHub Pages). The tools folder is the "kitchen behind the
   restaurant" -- visible if you look, but visitors see the dining room.

7. **Standard HTML save format** - When exporting from the desktop app, use
   "Interactive HTML - Standard (~10 KB, needs internet)" not Offline.
   The converter extracts just the figure data from either format, but
   Standard produces smaller source files. The gallery viewer loads
   Plotly.js from CDN independently.

## What Was Built

### Session 1 (Feb 5-6): Pipeline + Local Preview

**json_converter.py** (was dash_converter.py)

HTML-to-JSON converter for the Plotly figure pipeline.

- Extracts figure data from Plotly write_html() output using bracket-matching
  (not regex -- handles Plotly's heavy whitespace padding reliably)
- Strips Plotly template from layout (halves file size, avoids version
  mismatches between Plotly versions)
- Interactive mode with file picker and category selection
- Batch mode for folder conversion
- Maintains gallery_metadata.json with titles, categories, descriptions
- Also provides save_figure_for_dash() for direct figure object export

**Conversion results**: 8 of 12 HTML files converted successfully. 4 failures
were older files from a previous code structure -- re-exporting from the
current app would fix them.

**Size reduction examples**:
- Earth-Moon system: 15.2 KB HTML -> 7.6 KB JSON (50% reduction)
- Earth barycenter shells: 18.5 MB HTML -> 5 MB JSON (73% reduction)
- All reductions are from stripping embedded Plotly.js library and template

**json_gallery.py** (was dash_gallery.py)

Local Dash web gallery for development and preview.

- Dark space theme with gold accent (#c9a84c) matching astronomical aesthetic
- Sidebar with category-grouped navigation (color-coded)
- Loads Plotly figures from JSON with template stripping for compatibility
- Links to website and Instagram in footer
- Serves on localhost:8050

**Validated with 9 visualizations across 5 categories**: Earth System, Inner
Planets, Solar System, Stellar Neighborhood, Missions. All load instantly.

### Session 2 (Feb 6-7): GitHub Pages Gallery Viewer

**index.html** - Complete gallery viewer (Phase 1)

Single-file HTML/CSS/JS gallery viewer for GitHub Pages deployment. No build
step, no server, no dependencies beyond Plotly.js CDN.

Features implemented:
- Dark space theme matching json_gallery.py (gold accent #c9a84c)
- Responsive layout:
  - Desktop: 320px sidebar + full visualization area
  - Mobile (<1024px): hamburger menu overlay, full-screen visualization
- Category-grouped navigation with color-coded headers
- URL hash routing for shareable deep links (#earth-birthday-2025)
- Share button copies direct link to clipboard (desktop + mobile)
- Toast notifications for user feedback
- Loading states with animated dots
- Welcome state for first-time visitors
- Error handling for missing/failed JSON loads
- Open Graph meta tags for link preview unfurling
- Plotly modebar styled to match dark theme
- Keyboard support (Escape closes mobile sidebar)
- Plotly responsive resize on window change
- Template stripping on load (same as json_gallery.py)
- Dark theme overrides applied to all loaded figures
- Autosize forced (removes fixed width/height from desktop exports)
- 3D scene aspect override for mobile (cube mode)
- Scaled annotations and title fonts for small screens
- Post-render resize to ensure container fill

**Deployed live** at https://tonyquintanilla.github.io/

### Session 3 (Feb 7): Gallery UX Refinements

Systematic review of the deployed gallery with a fresh static Earth orbit
export. Compared gallery rendering against original HTML side by side.

**Changes made to index.html** (1,267 lines, ASCII clean, LF):

1. **Home navigation** - Sidebar header ("Paloma's Orrery") is now clickable,
   returns to welcome state. Clears URL hash, hides plot, deselects active
   card. Hover effect signals clickability. Users can now share the root
   gallery URL, not just individual visualization links.

2. **Fullscreen toggle** - "Expand" button in viz header hides sidebar +
   header, gives plot the full browser window. Floating "Exit" button
   (top-left, semi-transparent) restores gallery view. Escape key also
   exits. Plotly auto-resizes to fill. Solves the "squished plot" problem
   in gallery view where the 320px sidebar compresses the visualization.

3. **Preserved original layout** - Removed forced tight margins
   (l:10, r:10, t:40, b:10) that were clipping the title, legend, Earth
   button, and annotations. Now preserves the export's original margins.
   Title stays left-justified as in the original HTML.

4. **Fixed dropdown overlap** - Removed updatemenus repositioning code that
   was forcing both dropdowns to y:0.95, stacking them on top of each
   other. They now keep their original staggered positions from the export.

5. **Restored Plotly modebar** - Removed CSS rule hiding
   `.modebar-group:last-child` which was suppressing camera reset buttons.
   Changed `displaylogo: false` to `true` to show Plotly logomark.

6. **Updated file references** - All four `dash_gallery.py` references in
   comments/code updated to `json_gallery.py`.

**Result**: Expanded (fullscreen) view now matches the original HTML
rendering closely. Gallery view is compressed by the sidebar but the
Expand button gives users an immediate path to the full experience.

### Session 3 continued (Feb 7-8): Desktop Validation Sweep

Completed full desktop 16:9 validation of all visualization types.

**Bugs fixed in index.html** (1,305 lines, ASCII clean, LF):

1. **Persistent dropdown menus** - When switching between visualizations,
   updatemenus from the previous plot (e.g., inner planets dropdowns)
   persisted and could affect the new plot. Fixed by changing from
   `Plotly.react()` to `Plotly.purge()` + `Plotly.newPlot()`. Purge
   clears all previous figure state including menus, sliders, and
   event listeners before rendering the new figure.

2. **Auto-detect light vs dark theme** - The paleoclimate chart (white
   background, colored annotations) was rendered with dark theme overrides,
   making text boxes blank and colors wrong. Added auto-detection that
   checks `paper_bgcolor` and `plot_bgcolor` at the top level AND inside
   the template object (before template stripping) to determine if a plot
   was designed for a light background. Light-themed plots skip all dark
   overrides (transparent bg, light font color, scene bgcolor). Detection
   checks for: 'white', '#ffffff', '#fff', 'rgb(255...', '#e5ecf6'.

   **Debugging note**: First attempt checked only `paper_bgcolor` after
   template stripping -- failed because json_converter already strips
   templates during conversion, so `paper_bgcolor` was gone. Second
   attempt checked template before stripping -- failed because the JSON
   had no template at all. Final fix: check `plot_bgcolor` at top level
   (which survived conversion as `"white"`). The detection cascade is:
   `layout.paper_bgcolor` -> `layout.plot_bgcolor` -> `template.layout.*`.

3. **Title rescue for zero-margin plots** - Social view exports have all
   margins set to 0 (designed for their own HTML wrapper). The Plotly
   title was clipped. Added detection: if all margins are 0 and a title
   exists, inject `margin.t: 40` so the title renders.

4. **json_gallery.py path fix** - Gallery data folder resolved relative
   to cwd, broke when running from tools/ subfolder. Fixed to resolve
   relative to script location using `os.path.dirname(os.path.abspath())`.

**Desktop validation results** (all 7 visualizations tested):

| # | Visualization | Size | Type | Status |
|---|---|---|---|---|
| 1 | Earth Heliocentric | 147 KB | 3D planetary | Desktop OK |
| 2 | Earth Barycenter Shells | 9.3 MB | 3D planetary + shells | Desktop OK |
| 3 | Inner Planets + Comets + Solar Corona | 31.4 MB | 3D complex | Desktop OK |
| 4 | 3D Stars Distance 20Ly | 77 KB | 3D stellar | Desktop OK |
| 5 | Paleoclimate Human Origins | 116 KB | 2D light-themed chart | Desktop OK |
| 6 | Near Earth Asteroids | 1.9 MB | 3D planetary | Desktop OK |
| 7 | Orbital Transformation Mercury | 70 KB | 3D orbital elements | Desktop OK |

**Social view decision**: Near Earth Asteroids social view was tested and
renders correctly, but removed from gallery -- too thin on information
without the HTML wrapper's hover-driven info panel. The full view has all
the same orbits plus dropdowns, annotations, and legend. Social views may
return when the gallery can replicate the info panel.

**Local testing workflow established**:
```
cd C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
python -m http.server 8080
```
Opens http://localhost:8080 -- serves the real gallery viewer (not Dash),
reads from gallery/ folder, enables testing all features before pushing.

### Session 4 Design (Feb 8): Mobile Strategy

Desktop 16:9 gallery is unreadable on phones -- plots squished, text too
small. Social view exports (9:16) are phone-native but lose their info
panel in the JSON pipeline. After four rounds of open-ended design
discussion, converged on a unified approach.

**Key insight**: The social view's hover data IS already in the JSON --
`social_media_export.py` parses `trace.text` into structured `customdata`
(name/subtitle/body) on each trace. `json_converter.py` captures this
automatically since `customdata` is part of the Plotly figure data. What's
missing is the JavaScript event handlers and UI to display it.

**Second insight**: One interaction pattern for everything. Instead of a
persistent 60/40 info panel (stays in `social_media_export.py` for
Instagram/YouTube production), the gallery uses a floating info card that
appears on tap and dismisses on tap-away. Works for both 3D social-view
content and 2D standard content. One component, all content types.

### Architecture: Gallery v2

```
Gallery Viewer v2 (index.html)
|
+-- Mode toggle: [Desktop] [Mobile]
|   (defaults based on screen width, user can switch)
|
+-- Visualization selector (non-persistent overlay)
|   +-- Desktop entries (standard 16:9 exports)
|   +-- Mobile entries (social exports + pinch-friendly standards)
|
+-- Full-screen plot area (ALWAYS full width, no sidebar)
|   +-- Desktop: Plotly figure with standard hover tooltips
|   +-- Mobile: Full-screen with floating info card on tap
|
+-- Floating info card (appears on tap, dismisses on tap-away)
|   +-- 3D social content: reads pre-parsed customdata
|   +-- 2D/standard content: parses trace.text (pre-parsed by converter)
|   +-- Same component for all content types
|
+-- Zoom controls (mobile 3D only)
    +-- + / - buttons dispatch synthetic wheel events
    +-- Solves Plotly.js touch pinch-zoom limitation
```

### Navigation: Non-Persistent Overlay Selector

Replaces the current permanent 320px sidebar with a floating button +
overlay. This is a significant simplification that benefits all devices.

- Floating button (top-left) shows current visualization name
- Tap button -> overlay appears with mode toggle + category-grouped list
- Visualization lists differ between Desktop and Mobile modes
- Select visualization -> overlay closes, plot loads full-screen
- Same interaction on phone, tablet, and desktop
- No expand/exit toggle needed -- everything is always full-screen
- No sidebar compression problem -- plot always has full width

**Mode toggle**: Desktop / Mobile
- Defaults based on screen width (<1024px -> Mobile)
- User can switch freely on any device
- Some visualizations appear in both modes (e.g., paleoclimate)
- Some only in one mode (complex orrery = desktop, social 3D = mobile)

### Desktop Mode (current desktop experience, refined)

- Full-screen Plotly figure (no sidebar)
- Standard hover tooltips on desktop
- Pinch-zoom and pan via native Plotly touch
- All current functionality preserved: dropdowns, legends, annotations
- No info card (landscape uses standard Plotly hover tooltips)

### Mobile Mode (new)

- ALL content renders full-screen (no 60/40 split in gallery)
- Tap any object or data point -> floating info card slides up
- Card shows name/subtitle/body parsed from customdata
- Card dismisses on tap-away
- Zoom buttons (+ / -) for 3D scenes (Plotly lacks pinch-zoom on 3D)
- Non-persistent hint on first load: "Tap any object for details"
- Figure title suppressed (nav button label shows viz name instead)

### Info Card vs. Persistent Panel

| Context | UI | Why |
|---------|-----|-----|
| Gallery viewer (mobile mode) | Floating info card | Maximizes screen for plot; appears on demand |
| social_media_export.py HTML | Persistent 60/40 panel | Designed for screen recording; stays visible in video |

The gallery and social export serve different audiences. The gallery is
for browsing; the social HTML is for Instagram/YouTube production. The
persistent panel stays in social_media_export.py where it was designed.

### Metadata: Mode Tagging

```json
{
  "id": "earth_heliocentric",
  "mode": "landscape",
  "title": "Earth Heliocentric Orbit"
}
{
  "id": "earth_heliocentric_portrait",
  "mode": "portrait",
  "title": "Earth Heliocentric (Portrait)"
}
{
  "id": "paleoclimate_human_origins",
  "mode": "both",
  "title": "Paleoclimate Human Origins"
}
```

Mode values:
- `"landscape"` -- only in Desktop list (complex desktop exports)
- `"portrait"` -- only in Mobile list (social-export JSONs)
- `"both"` -- appears in both lists, same JSON file (2D charts, etc.)

Developer tags mode manually during conversion. No auto-detection needed.

Note: Internal JS variables still use `landscape`/`portrait` for mode
values. The UI labels were renamed to Desktop/Mobile in Session 7 for
clarity. The metadata `mode` field remains landscape/portrait/both.

### Data Pipeline (updated Session 12 planning)

Current workflow:
1. Create visualization in desktop app
2. Export HTML (standard or social view, as appropriate)
3. Open in Gallery Studio -- curate (presets, adjustments, preview)
4. Export from studio
5. Run json_converter.py -> JSON
6. Tag mode in gallery_metadata.json (landscape / portrait / both)
7. Drop JSON into website repo's gallery/ folder
8. Push with GitHub Desktop
9. Live at public URL within minutes

Target workflow (after Session 12 refactor):
1. Create visualization in desktop app
2. Export HTML
3. Open in Gallery Studio -- curate (presets, trace selection, preview)
4. Preview as Studio (social/portrait output) AND Preview as Gallery
   (what palomasorrery.com will show) -- iterate until both are right
5. Export from studio
6. Run json_converter.py -> JSON
7. gallery_editor.py for metadata (category, mode, ordering)
8. Push with GitHub Desktop
9. Live at public URL -- matches gallery preview exactly

### Hover Text Parsing: Python at Conversion Time

Decision: json_converter.py pre-parses trace.text into structured
customdata during conversion, rather than parsing in JavaScript at runtime.

Rationale:
- _parse_hover_html() already works in Python (social_media_export.py)
- Gallery viewer JavaScript stays simple -- just reads structured data
- Runs once at conversion time, not every page load
- If parsing logic changes, reconvert (would happen anyway)

For social exports: customdata already pre-parsed by social_media_export.py.
For standard exports: json_converter.py does the same parsing during
conversion. Either way, the gallery viewer always gets structured customdata.

### Session 5 (Feb 9): Earth System Save Pipeline + Theme/Aspect Fixes

Gallery content validation completed for stellar visualizations -- all
stellar views (HR diagrams, 3D star maps by distance and magnitude)
render correctly in the gallery. This clears the stellar converter
testing item from the Session 4 implementation sequence.

Systematic review of the Earth System Visualization GUI's save pipeline
and gallery rendering fidelity. Three issues identified and resolved.

**Problem 1: Missing save dialogs in Earth System visualizations**

Only 5 of 14 Earth System visualizations had `save_plot()` calls after
`fig.show()`. The other 9 opened in the browser but offered no save
dialog -- the only way to capture them was Plotly's modebar "Download
plot as PNG" button. PNG images cannot be converted by json_converter.py
(it extracts Plotly figure data from HTML, not pixels), so these 9
visualizations had no path to the web gallery.

**Fix**: Added `save_plot(fig, "descriptive_name")` to all 9 missing
`open_*` functions in earth_system_visualization_gui.py. Pattern matches
the existing 5 functions exactly: `fig.show()` then `save_plot()`.

| Function | Default filename |
|---|---|
| open_monthly_temp_lines | monthly_temperature_year_over_year |
| open_warming_stripes | warming_stripes_hawkins |
| open_ph_viz | ocean_acidification_ph |
| open_planetary_boundaries | planetary_boundaries_src |
| open_sea_level_viz | global_sea_level_rise |
| open_keeling_curve | keeling_curve_co2 |
| open_temperature_viz | global_temperature_anomalies |
| open_ice_viz | arctic_sea_ice_extent |
| open_energy_imbalance | energy_imbalance_climate_mechanism |

All 14 Earth System visualizations now go through the save dialog,
producing HTML files that feed into json_converter.py for the gallery.

**Problem 2: Light-themed plots rendered with dark theme in gallery**

Four climate visualizations (Keeling Curve, Temperature Anomalies, Sea
Level Rise, Ocean Acidification) appeared with dark overrides in the
gallery -- transparent backgrounds and light text on the dark gallery
page. These plots use `template="plotly_white"` which sets
`paper_bgcolor: white` inside the template object, not at the top level.

Root cause chain:
1. Plotly `write_html()` embeds bgcolor only inside the template object
2. `json_converter.py` strips the template (for size + version compat)
3. bgcolor is lost -- no `paper_bgcolor` at top level
4. Gallery viewer's theme detector sees empty bgcolor, concludes "dark"
5. Dark overrides applied: transparent bg + light text = unreadable

**Fix (json_converter.py)**: New `_strip_template_preserve_theme()`
helper. Before deleting the template, promotes `paper_bgcolor` and
`plot_bgcolor` from `template.layout` to top-level `layout` if not
already set there. Applied to both conversion paths:
`convert_html_to_gallery_json()` and `save_figure_json()`.

**Fix (existing JSONs)**: Patched the 4 affected JSON files by adding
`"paper_bgcolor": "white"` to their layout. Future conversions handled
automatically by the converter fix.

**Problem 3: Planetary Boundaries chart squished in gallery**

The Planetary Boundaries polar chart (1200x1100, aspect ratio 0.917) was
compressed into a wide landscape container, making wedge labels overlap
and the chart unreadable. The gallery viewer deletes `width` and `height`
from all figures and sets `autosize: true`, which works for landscape
plots but squishes tall/square ones.

**Fix (index.html)**:
1. Capture original aspect ratio (`height / width`) before deleting dims
2. After rendering, if ratio >= 0.8 (tall or square), set `min-height`
   on the plotly-graph div based on container width times original ratio
3. Clear `min-height` for landscape plots (ratio < 0.8) -- no change
4. Recalculate on window resize so the constraint adapts
5. Changed viz-container `overflow: hidden` to `overflow: auto` so tall
   plots can scroll if they exceed viewport height

Most plots (landscape, ratio ~0.58) are completely unaffected. Only
plots designed tall or square get the min-height protection.

**Files changed**:
- earth_system_visualization_gui.py (9 save_plot additions)
- json_converter.py (new _strip_template_preserve_theme function)
- index.html (aspect ratio preservation + overflow fix)
- 4 JSON files patched (keeling_curve, temperature, sea_level, ocean_ph)

### Session 6 (Feb 9): Gallery v2 -- Non-Persistent Overlay Selector

Implemented Step 2 of the Gallery v2 implementation sequence: replaced
the permanent 320px sidebar with a non-persistent overlay selector.
Everything is now full-screen, always. No more sidebar compression
problem, no more fullscreen toggle needed.

**Architecture change (index.html rewrite, 1,197 lines -> replaces 1,332)**:

Removed:
- Permanent sidebar (`.sidebar`, 320px fixed)
- Fullscreen toggle / exit buttons (everything is fullscreen now)
- Separate mobile hamburger + desktop sidebar logic
- `.viz-header` bar (title moved to nav button)
- Separate mobile share button element

Added:
- `.nav-btn` -- floating button (top-left) with hamburger icon + label
  text showing current viz name or "Paloma's Orrery" on welcome
- `.overlay-selector` -- slide-out panel with same content as old sidebar
  (category-grouped cards, footer links, header -> home)
- `.overlay-backdrop` -- click/tap to dismiss
- Mode toggle buttons (Desktop / Mobile) with list filtering --
  entries show based on metadata `mode` field (landscape/portrait/both)
- Auto-detect default mode from screen width (<1024px -> Mobile)
- Floating share button (top-right at top:52px, below Plotly modebar,
  appears only when a viz is loaded)
- Floating info card (mobile mode) -- slides up from bottom on
  plotly_click, shows name/subtitle/body from customdata JSON
- "Tap any object for details" hint on first mobile load (3s fade)
- `json_converter.py` mode tagging (L/P/B prompt during conversion)

Preserved unchanged:
- All Plotly rendering logic (theme detection, template stripping,
  aspect ratio, mobile overrides, title rescue, annotation scaling)
- URL hash routing and deep links
- Toast notifications
- Category colors and typography
- Share/copy link functionality
- Error handling

**Interaction model (same on all devices)**:
1. Floating button (top-left) shows current context
2. Tap button -> overlay slides in from left with backdrop
3. Select visualization -> overlay closes, plot loads full-screen
4. Tap button again to browse more
5. Click header title in overlay -> return to welcome state
6. Escape key closes overlay

**Info card interaction model** (discovered, not designed):
- Left-click + hold: card appears while button held, drops on release
- Right-click: card pins, persists until left-click release
- Right-click another object: card updates, stays pinned
- Escape key: dismisses card
- On touch devices: tap = persistent until tap-away

The peek/pin split is an emergent behavior from event propagation:
`plotly_click` fires on mousedown (shows card), document `click` fires
on mouseup (dismisses). Right-click triggers `plotly_click` but not
document `click` (contextmenu instead), so the card persists. No
custom code needed -- the browser event model produces the interaction.

**Files changed**:
- index.html (full rewrite -- overlay architecture replaces sidebar,
  mode filtering added, floating info card for mobile mode)

### Session 7 (Feb 10): iPhone Testing + Mobile Fixes

First real device testing on iPhone 17 Pro Max. Identified and resolved
multiple mobile-specific issues through iterative testing and debugging.

**Testing device**: iPhone 17 Pro Max, iOS Safari (via home screen bookmark)

**Issues found and fixed**:

1. **Viewport meta blocking Plotly touch** - Original viewport tag had
   `maximum-scale=1.0, user-scalable=no` which blocked native browser
   zoom. Changed to `width=device-width, initial-scale=1.0` only.
   Allows Plotly's native touch handling to work.

2. **Figure title overlapping browser chrome** - On mobile, the Plotly
   figure's `layout.title` rendered on top of the nav button and browser
   address bar. Title rescue code was adding `margin.t: 40` for social
   views, pushing the orbit down. Fix: on screens <1024px, delete
   `layout.title` entirely -- the nav button label already shows the
   visualization name. Desktop keeps title rescue unchanged.

3. **Plotly config scoped to mobile** - `scrollZoom: true` and
   `doubleClick: false` applied only when `'ontouchstart' in window` or
   `innerWidth < 1024`. Desktop behavior completely unchanged.

4. **Info card click handler with trace.text fallback** - Enhanced the
   portrait-mode click handler with three-tier data extraction:
   - Primary: `point.customdata` (social view exports with JSON strings)
   - Fallback: parse `point.data.text` HTML (standard exports)
   - Last resort: `point.data.name`
   Scoped to portrait/mobile mode only per handoff decision (desktop
   uses standard Plotly hover tooltips).

5. **Mode labels renamed** - "Landscape/Portrait" -> "Desktop/Mobile"
   for clarity. Internal JS variables (`modeLandscape`, `modePortrait`,
   `currentMode = 'landscape'`) unchanged -- they're internal identifiers.

6. **3D zoom buttons for mobile** - Plotly.js has a known limitation:
   pinch-zoom does not work on 3D WebGL scenes (GitHub issue #1858,
   open since 2017). Single-finger orbit/rotation works, but two-finger
   pinch does not trigger zoom. Solved with floating + / - buttons.

   **The debugging journey** (important for future reference):
   - Attempt 1: `Plotly.relayout()` with `scene.camera.eye` -- clipped
     traces instead of zooming (orthographic projection ignores eye
     distance for apparent size)
   - Attempt 2: Direct `glplot.camera.distance` assignment -- property
     is read-only (getter/setter bounces back to original value)
   - Attempt 3: `glplot.camera.lookAt()` with scaled eye -- also
     read-only, eye values unchanged after call
   - Attempt 4: Scale axis ranges -- same clipping behavior
   - **Key discovery via DevTools**: scroll-wheel zoom DOES work on
     desktop even with orthographic projection. But `camera.distance`,
     `camera.eye`, and `camera.matrix` all report identical values
     before and after scroll zoom. Plotly's internal handler does
     something we can't replicate through the public API.
   - **Solution**: Dispatch synthetic `WheelEvent` to the WebGL canvas.
     This piggybacks on Plotly's own internal zoom handler -- whatever
     magic it does for orthographic projection, we reuse it.

   **Implementation**:
   - Floating + / - buttons, bottom-right, dark glass style (44px
     touch targets, `backdrop-filter: blur`)
   - `touchstart` events with `preventDefault` (not `click` -- Plotly's
     WebGL canvas swallows click events on iOS)
   - `mousedown` fallback for desktop responsive testing
   - Synthetic `WheelEvent` dispatched to `.gl-canvas-focus` canvas at
     center point, `deltaY: +/-100`
   - Visible only in mobile mode + 3D scenes (`currentMode === 'portrait'`
     AND `layout.scene` exists)
   - Hidden on 2D plots, desktop mode, and welcome screen

   **Lesson**: Plotly's 3D camera is fully locked down from external
   manipulation. The only way to zoom programmatically is to simulate
   the user interaction that Plotly already handles (wheel events).
   This applies to both perspective and orthographic projections.

**iOS testing notes**:
- Home screen bookmarks cache aggressively. Swipe away from app
  switcher and reopen to force refresh. If that fails, delete bookmark,
  reload in Safari with `?v=N` cache buster, re-add to home screen.
- In-app browsers (WKWebView from Claude app, etc.) don't expose
  browser controls. Long-press URL to "Open in Safari" for cache
  management, or copy URL and paste with `?v=N` appended.
- Claude iOS app syncs desktop -> phone but NOT phone -> desktop in
  project conversations. Messages sent from phone don't appear on
  desktop. Artifacts generated in response to phone messages exist in
  the file system but aren't visible on desktop. Workaround: test on
  phone, review/download artifacts on desktop.

**Files changed**:
- index.html (viewport fix, title suppression, scoped Plotly config,
  enhanced click handler, mode label rename, zoom buttons with
  synthetic wheel events)

### Session 8 (Feb 12): Gallery Management Tooling

Late-night session focused on gallery curation infrastructure. Editing
gallery_metadata.json by hand was the only way to change titles, reorder
visualizations, or reorganize categories. Built a GUI editor and unified
category definitions across all gallery components.

**Problem**: Three independent category definitions existed:
1. `json_converter.py` -- hardcoded `CATEGORIES` dict (used during conversion)
2. `gallery_editor.py` -- hardcoded `KNOWN_CATEGORIES` (used in editor UI)
3. `index.html` -- hardcoded `CATEGORY_COLORS` JS object + CSS variables

Adding or renaming a category meant editing all three files. Colors could
drift between them. New categories had no path to the gallery viewer's
color scheme.

**Solution**: `gallery/gallery_config.json` -- single source of truth.

```json
{
  "categories": [
    { "key": "solar_system", "label": "Solar System", "color": "#f4a261" },
    { "key": "inner_planets", "label": "Inner Planets", "color": "#e76f51" },
    ...
  ]
}
```

All three consumers read from it:
- **json_converter.py**: loads config for category labels during conversion,
  falls back to hardcoded dict if config missing
- **gallery_editor.py**: reads config for category list, writes config
  when categories are added/renamed/recolored
- **index.html**: fetches config at init, merges into `CATEGORY_COLORS` JS
  object. Falls back to hardcoded defaults if fetch fails.

**gallery_editor.py** -- new tkinter GUI (run from `tools/`):

Visualization editing:
- Edit Title (double-click or button)
- Edit Description (multi-line dialog)
- Change Category (from config-driven list)
- Move Up / Move Down (within mode+category group)
- Copy To... (duplicate viz to another category/mode with `_copy` ID)
- Delete (removes from metadata; JSON data file not touched)

Category management (Categories menu):
- New Category -- prompts for label + color, generates snake_case key
- Rename Category -- changes key + label, updates all vizs with old key
- Edit Category Color -- updates config

Tree display:
- Mode -> Category -> Visualization hierarchy
- Category order derived from JSON sequence (matches gallery exactly)
- Empty categories from config shown at bottom (e.g., Missions in
  landscape when no mission landscape exports exist yet)
- Move Up/Down works on both individual vizs AND entire categories
  (swaps category blocks within a mode)
- Unsaved changes tracked (`*` in title bar), Ctrl+S saves both files
- Auto-backup with timestamp before every metadata save

**Category reorder algorithm**: Non-contiguous category blocks (vizs from
the same category scattered across the JSON array) are handled by
extracting all vizs for the mode, regrouping by category, swapping the
two adjacent groups, and reinserting. This also normalizes scattered
entries as a side effect.

**Data pipeline updated**:

```
Desktop App (Python/Plotly)
    |
    v
json_converter.py (HTML -> JSON, reads gallery_config.json)
    |
    v
JSON files + gallery_metadata.json
    |                |
    v                v
gallery_editor.py   index.html
(edits metadata     (reads config for
 + config)           category colors)
    |
    v
gallery_config.json (shared category definitions)
```

**Files created**:
- gallery/gallery_config.json (category definitions: key, label, color)
- tools/gallery_editor.py (metadata + config editor GUI)

**Files changed**:
- tools/json_converter.py (reads categories from config with fallback)
- index.html (loads config at init for category colors; mobile bottom
  toolbar fix: 100dvh, viewport-fit=cover, 80px nav padding)

### Session 9 (Feb 14): 2D Mobile Optimization + Cross-Browser Testing

Valentine's Day session focused on making complex 2D visualizations
(HR diagrams) work well on mobile, and cross-browser testing across
five iOS browsers. Also added zoom buttons to desktop mode and refined
desktop overlay behavior.

**Testing devices**: iPad landscape (Safari), iPhone (Safari, Chrome,
DuckDuckGo, Arc), Android (Samsung Internet)

**Changes made to index.html**:

1. **Footer annotation stripping on mobile** -- HR diagrams include a
   lengthy text footer (description + star counts) positioned below the
   plot area at `yref: 'paper', y < 0`. This consumed 15-20% of vertical
   space on mobile. Fix: filter out annotations with `yref === 'paper'`
   and `y < 0` on screens <1024px. Desktop unchanged.

2. **Hover toggle buttons stripped on mobile** -- "Full Object Info" /
   "Object Names Only" updatemenus overlapped axis labels on small screens.
   Fix: remove non-animation updatemenus on mobile and default all traces
   with `customdata` to names-only hover (`%{customdata}<extra></extra>`).
   Animation play/pause controls preserved (filtered by `method === 'animate'`).

3. **X-axis title stripped on mobile** -- For HR diagrams, the spectral
   type labels (O, B, A, F, G, K, M, L) across the top plus temperature
   numbers at the bottom are self-explanatory. Deleting `xaxis.title` on
   mobile saves vertical space without losing information.

4. **Mobile margin overrides** -- Desktop exports use generous margins
   (t:125, b:155) for title and footer. With those elements removed on
   mobile, margins are clamped: `t` to 10px, `b` to 95px (room for
   x-axis tick labels), `l` to 80px (room for y-axis title).

5. **Modebar hidden on mobile** -- Instead of the earlier attempt to move
   the modebar into the toolbar (which caused vertical icon stacking),
   modebar is now hidden entirely via `config.displayModeBar = false` on
   touch/mobile devices. Zoom buttons + pinch/pan + tap-for-info cover
   all needed interactions.

6. **2D zoom buttons** -- New `zoom2D()` function scales axis ranges
   around their center point using `Plotly.relayout()`. Same styled +/-
   buttons as 3D scenes. Button handler dispatches to `zoom2D` or `zoom3D`
   based on a `data-scene` attribute set when the visualization loads.

7. **Zoom buttons on all devices** -- Previously only shown in mobile
   mode for 3D scenes. Now visible for both 2D and 3D, on both desktop
   and mobile. Especially useful for trackpad users on desktop who find
   Plotly's scroll-zoom awkward.

8. **Desktop nav button label hidden** -- On screens >1024px, the nav
   button label (visualization title text) is hidden via CSS, leaving
   only the compact hamburger icon. This prevents the wide nav button
   from overlapping Plotly's title, updatemenus dropdowns, and hover
   toggle buttons in the top-left of the figure.

9. **Phone-only forced portrait mode** -- CSS `@media (max-width: 767px)`
   hides the Desktop/Mobile mode toggle entirely. Phones only see Mobile
   (portrait) content. Tablets (768-1023px) retain the toggle. Rationale:
   Desktop mode visualizations cannot reproduce the desktop experience
   on phone screens -- they're distorted and the controls are too small.

10. **Safari viewport height fix** -- `100vh` on iOS Safari includes the
    area behind the bottom toolbar, clipping content. Changed
    `.app-container` from `height: 100vh` to `height: 100vh` (fallback)
    then `height: 100dvh` (dynamic viewport height, excludes toolbar).
    CSS cascade means browsers supporting `dvh` use it; others fall back
    to `vh`. Also added `padding-bottom: env(safe-area-inset-bottom)` to
    `.viz-container` as belt-and-suspenders for safe area insets.

**Cross-browser testing results** (HR Diagram Distance 20Ly):

| Browser | Device | Result |
|---------|--------|--------|
| Safari | iPad landscape | Full labels visible, clean layout |
| Chrome | iPad landscape | Full labels visible, slightly more compact |
| Safari | iPhone landscape | "Luminosit..." left-clipped (Safari-specific) |
| DuckDuckGo | iPhone landscape | Full labels, clean |
| Arc | iPhone landscape | Full labels, clean |
| Samsung Internet | Android | Compact but complete, even with bottom nav bar |

Safari iPhone clipping is a known Safari rendering quirk where a few
pixels are lost on the left edge. Increasing `margin.l` beyond 80 would
fix it but waste space on all other browsers. Acceptable tradeoff.

**Key insight: "both" mode for 2D plots** -- HR diagrams work in both
Desktop and Mobile modes because they're 2D scatter plots that render
well at any aspect ratio. The mobile overrides (footer strip, button
strip, margin clamp) make them excellent on phones. Mode field = "both".

**Files changed**:
- index.html (all 10 changes above -- footer/button stripping, 2D zoom,
  margin clamping, modebar hiding, nav label hiding, phone mode lock,
  Safari dvh fix)

### Session 9 continued (Feb 14): Generic Mobile Overrides + Welcome Hints

Extended mobile optimization to handle Earth System climate visualizations
(Keeling Curve, Temperature Anomalies, Sea Level, Energy Imbalance,
Planetary Boundaries). Three generic problems identified and solved.

**Problem 1: Annotation boxes block data on small screens**

Desktop exports use bordered, semi-opaque annotation boxes (bgcolor +
bordercolor) for info callouts. On mobile these become opaque blocks
covering the data. Removing annotations entirely loses useful info.

**Fix**: On mobile, make annotation boxes transparent -- strip `bgcolor`,
`bordercolor`, `borderwidth`, and `borderpad` from all annotations but
keep the text. The text scales down via existing font reduction, and
without the opaque background it floats over the data unobtrusively.
Generic: works for any visualization without per-chart logic.

**Problem 2: Legend boxes obstruct data**

Some visualizations have legends with `bgcolor` and `bordercolor`
creating opaque containers. On mobile these block data.

**Fix**: On mobile, set `legend.bgcolor` to transparent and delete
`bordercolor` / `borderwidth`. Legend markers and labels remain visible;
only the opaque container is removed.

**Problem 3: Axis title fonts don't scale**

Axis titles (xaxis.title, yaxis.title) use fixed font sizes from
desktop exports that are too large on mobile. Unlike annotations, these
weren't covered by the existing font scaling.

**Fix**: On mobile, iterate all xaxis*/yaxis* entries. If title font
size > 12, scale to 75% (minimum 10). Same pattern as annotation scaling.

**Also fixed: Duplicate mobile override block** -- Two separate
`<1024px` blocks had accumulated from iterative edits with slightly
different margin values (95 vs 100 for bottom). Consolidated into one
clean block.

**Also fixed: X-axis title deletion reverted** -- The blanket deletion
of `xaxis.title` on mobile was too aggressive. HR diagrams don't need
it (spectral types are self-explanatory), but climate charts need "Year"
and other axis labels. Replaced with font scaling instead.

**Content curation pattern emerged**:

| Content Type | Mode | Why |
|---|---|---|
| 2D line/scatter (Keeling, HR) | both | Adapts well to any aspect ratio |
| Complex charts (Planetary Boundaries, paleoclimate) | landscape | Too busy/square for portrait |
| 3D plots (orrery, stellar) | landscape for desktop exports, portrait for social views |

Landscape-only charts that need scrolling can use title hints like
"(swipe to explore)" set via gallery_editor.py.

**Welcome screen device hints** -- Phone users only see Mobile content
and don't know Desktop mode exists on larger screens. Added CSS-only
device-aware hints to the welcome screen:

- Phones (<768px): "More visualizations with full interactive controls
  available on tablet or desktop."
- Tablets (768-1024px): "Switch between Desktop and Mobile modes for
  different experiences."
- Desktop (>1024px): nothing shown (toggle is visible)

Implementation uses CSS `::after` content with media queries -- no
JavaScript needed. Styled in accent color, italic, smaller font.
Present in both the static HTML and the goHome() JS rebuild.

**Files changed**:
- index.html (consolidated mobile block, transparent annotation/legend
  boxes, axis title scaling, welcome device hints)

### Implementation Sequence

| Step | What | Notes |
|------|------|-------|
| 1 | Stellar converter testing | DONE (Session 5) - all stellar views pass |
| 2 | Non-persistent selector prototype | DONE (Session 6) - overlay replaces sidebar |
| 3 | Floating info card component | DONE (Session 6) - mobile mode, peek/pin interaction |
| -- | Mode filtering + converter tagging | DONE (Session 6) - pulled forward from Step 5 |
| 4 | ~~json_converter.py hover parsing~~ | DROPPED - desktop uses native hover; mobile uses social customdata |
| 5 | Content population + validation | IN PROGRESS - 31 vizs (23 landscape, 8 portrait) |
| 6 | Gallery management tooling | DONE (Session 8) - editor GUI + shared config |
| 7 | 2D mobile optimization + cross-browser | DONE (Session 9) - HR diagrams on 5 iOS browsers |
| 8 | Gallery Studio | DONE (Session 10) - per-plot curation tool |
| 9 | Studio/index integration | DONE (Session 10) - _studio flag, pan arrows |
| 10 | Portrait preset | DONE (Session 11) - click-to-panel + encyclopedia |
| 11 | Studio WYSIWYG refactor | DONE (Session 12) - studio sole authority, index dumb renderer, trace visibility, gallery preview |
| 12 | Content re-population | NEXT - re-export all through studio, validate |
| 13 | Font standardization | DONE (Session 16) - all font controls use 100%=keep convention |
| 14 | Polish | Version stamp, hints, nudges |

### Session 10 (Feb 15): Gallery Export Studio

Built gallery_studio.py -- a Tkinter GUI tool for per-plot configuration
of Plotly HTML transformations before the gallery pipeline. Solves the
fundamental problem that index.html's generic cleanup can't make good
per-plot decisions (legend font size for 9-entry paleoclimate chart vs
3D planet view with no legend).

**gallery_studio.py** (1,835 lines, ASCII clean, LF)

The studio sits between source HTML and the gallery pipeline:

```
Source GUI -> raw Plotly HTML -> Gallery Studio -> tailored HTML
    -> json_converter -> index.html
```

Studio does:
- Load any Plotly HTML (raw exports, social views, prior studio exports)
- Configure transformations via GUI (title, background, margins, 3D scene,
  legend, annotations, traces, chrome/controls, hover, 2D axes, navigation)
- Preview in browser via temp file (iterate until right)
- Export tailored HTML with per-plot settings
- Auto-save/restore configs per source filename (gallery_studio_configs.json)

Studio does NOT:
- Modify source plots
- Create new visualizations
- Handle animation creation

**Session 12 completed**: The studio is now the sole WYSIWYG authority
for all content transforms. The index.html viewer was stripped of all
16 content overrides and renders exactly what the studio exports.
See Session 12 for the full implementation record.

**Key features**:

1. **Tooltip documentation** -- Every control has a hover tooltip explaining
   what it does, when to use it, and practical examples from the project.
   Self-documenting GUI.

2. **Background presets** -- Dark/Light/Plotly one-click buttons plus a
   color spectrum picker (tkinter.colorchooser). Live color swatch previews
   the selected color. Auto-detects text color based on background brightness
   (ITU-R BT.601 formula).

3. **2D axis font controls** -- Axis title font size and tick label font
   size. Essential for paleoclimate charts where desktop-sized axis titles
   overflow on mobile. Set to 0 to keep original sizes.

4. **Pan/zoom navigation arrows** -- Embeds a D-pad (up/down/left/right)
   plus zoom (+/-) and reset button in the exported HTML. Essential for
   2D charts on touch devices where you need to navigate to specific data
   points (e.g., finding a particular year on a paleoclimate chart to
   read its hover text).

5. **_studio flag** -- The studio marks its exports with `_studio: true`
   in the Plotly layout. This flag survives json_converter extraction.
   index.html detects it and skips ALL generic cleanup (legend overrides,
   margin capping, font scaling, colorbar hiding, annotation stripping,
   title removal, hover mode changes). The studio's settings pass through
   untouched.

6. **_studio_nav flag** -- When pan arrows are enabled, `_studio_nav: true`
   is added to the layout. index.html reads this and shows the full D-pad
   control panel instead of the basic zoom-only buttons.

**index.html changes** (1,080 lines -> ~2,080 lines):

- Studio detection: reads `_studio` flag, skips generic overrides
- Pan controls: full D-pad HTML/CSS/JS alongside existing zoom controls
- `_studio_nav` switches between D-pad (studio) and zoom-only (non-studio)
- Pan functions for 2D (axis range shifting) and 3D (camera manipulation)
- Reset button captures original ranges on first interaction
- Pan controls hidden when returning to welcome/home state

**Testing validated**:
- Paleoclimate Wet Bulb chart: legend font 9, axis title 9, pan arrows
- Planetary Boundaries: studio export with light background, clean rendering
- Cross-browser: Home Screen, Chrome, Safari on iPhone landscape
- _studio flag survives full round-trip (studio -> HTML -> json_converter
  -> JSON -> index.html)
- Pan arrows work correctly for 2D chart navigation

**Architecture (Session 10, completed Session 12)**: The studio is the
sole WYSIWYG authority for all content curation. The index is a dumb
renderer -- structural viewer only. What you preview in studio is what
users see in the gallery. The _studio flag is no longer needed for
branching; it's cleaned up on read but the index applies no content
transforms regardless.

**Paleoclimate charts reinstated**: Previously removed from gallery as
"too busy for mobile view." The studio's per-plot font sizing and pan
arrows make them viable gallery content again.

**Social view relationship clarified**: Social views (9:16 portrait with
info panel) remain their own output for Instagram/YouTube. The studio can
load a social view HTML as input and further tailor it for gallery. The
studio doesn't replace social_media_export.py -- it's a different tool
for a different purpose. The gallery can also reload its own prior exports
for iterative refinement.

### Session 11 (Feb 16): Portrait Preset -- Click-to-Panel + Encyclopedia

Added portrait preset to Gallery Studio, bringing social_media_export.py's
9:16 info panel directly into the studio as a one-click configuration.
Users can now load any Plotly HTML, select "Portrait (9:16 social)", and
get the full social media view with click-to-panel and encyclopedia cards.

**Portrait preset features**:
- 60/40 layout (scene top, info panel bottom)
- Hover routing: trace.text parsed into structured customdata (name/subtitle/body)
- Click-to-panel: tapping a planet updates the info panel immediately
- Hover-to-panel: hovering updates with 800ms delay (desktop)
- Encyclopedia card overlay: "i" button shows extended object info from
  constants_new.py INFO dict, with dismiss via X, Escape, or click-outside
- Font auto-sizing in panel body text
- Branding watermark in bottom-right
- All standard studio controls still available for fine-tuning

**Bugs found and fixed (stacked -- both had to be solved)**:

1. **Import path resolution** -- gallery_studio.py lives in
   `tonyquintanilla.github.io/tools/` but social_media_export.py and
   constants_new.py live in `orrery/` (a sibling directory two levels up).
   The `from social_media_export import _parse_hover_html` failed silently
   because the try/except caught ImportError and disabled routing entirely.
   Fixed by walking up the directory tree and checking candidate paths
   (parent, grandparent, grandparent/orrery/).

2. **JS crash in debug logging killed event handlers** -- Debug code
   `JSON.stringify(t.text).substring(0, 60)` crashed when orbit traces
   had `text: undefined` (not null, not empty array -- undefined). The
   TypeError aborted `initEventListeners()` before it could wire up the
   plotly_click and plotly_hover handlers. Events never registered, so
   clicking planets did nothing. The panel code itself was fine.

**Debugging methodology**: Console logging at every stage of the pipeline:
- Python routing log: confirmed import success/failure, which traces routed
- JS trace inspection: confirmed customdata presence/absence per trace
- JS event logging: confirmed click events fire but find no customdata
- The stacked nature meant fixing bug 1 (import) revealed bug 2 (JS crash)
  which had been invisible because there was no data to crash on before

**Key architectural insight**: The portrait preset reuses
social_media_export.py's `_parse_hover_html()` function rather than
reimplementing parsing. This keeps one parser for hover text decomposition.
The studio imports it at apply_config() time, not at module load, so the
import path resolution only runs when the portrait preset is active.

**gallery_studio.py** (2,972 lines, up from 1,835 in Session 10)

Growth reflects: portrait HTML builder (build_social_html), encyclopedia
overlay system, hover routing engine, cross-directory import resolution,
three-column GUI layout for portrait-specific controls.

### Session 12 (Feb 16): Studio WYSIWYG Refactor -- Implementation

Refactored the gallery pipeline so the studio is the single source of
truth for ALL content curation. The index becomes a dumb renderer with
no content opinions. Follows the static site generator pattern.

**Approach**: Audit first, build second. Cataloged all 16 content
transforms in the index's `!isStudio` block, mapped each to existing
or needed studio controls, then implemented in one agentic pass.

**Index transform audit** (index_transform_audit.md):
- Category A: 10 structural transforms that STAY in index (template
  strip, autosize, min-height, resize, Plotly config, click handler,
  tap hint, control panel selection)
- Category B: 16 content transforms MOVED to studio (title handling,
  dark theme, scene bgcolor, aspect mode, legend reposition, colorbar
  hiding, footer stripping, annotation transparency, axis font scaling,
  margin clamping, updatemenus stripping, names-only hover, annotation
  font scaling, title font scaling)
- Category C: Info card rendering stays in index (reads structured
  data the studio prepared)

**Design decision**: Option 3 from the audit -- structural device
adaptations (mobile Plotly config: scrollZoom, no modebar) stay in
index as they're like CSS media queries. All CONTENT transforms moved
to studio. Reduces hidden transforms from 16 to 0 content + ~3
structural.

**gallery_studio.py** (2,972 -> 3,418 lines, +446)

New config keys (6):
- `scene_aspectmode`: auto/cube/data/manual (was index's mobile cube)
- `legend_font_color`: explicit color (was index's #9a9a9a)
- `legend_border_transparent`: checkbox (was index's bordercolor delete)
- `legend_position`: original/top-center-h/bottom-h (was index's mobile)
- `annotation_font_scale`: 0-100% (was index's 70% on <900px) -- updated to 100=keep in Session 16
- `trace_visibility` + `strip_hidden_traces`: non-destructive filtering

New GUI controls:
- 3D aspect mode dropdown (Scene section)
- Legend position dropdown, font color entry, border checkbox (Legend)
- Annotation font scale spinbox (Annotations)
- Trace Visibility panel: scrollable checkboxes per trace on file load,
  Select All/None buttons, Strip Hidden on export checkbox
- "Gallery Preview" button: renders through minimal viewer with NO
  content transforms, gold banner labels it as gallery preview

GUI column layout (reorganized Session 12, refined Session 16):
- Left: Title, Background, Margins, Legend, Navigation Controls
- Center: Annotations, Trace Visibility, Trace Appearance, Chrome
- Right: Portrait / Social, Hover, 3D Scene, 2D Axes

3D navigation fix: Reset button captures initial camera on first
render (in Plotly.newPlot .then() callback) and restores via
Plotly.relayout. Pan steps are relative to camera distance (8% of
eye-to-center) instead of absolute. Prevents "launched into space".

Preset updates:
- PORTRAIT_CONFIG now includes scene_aspectmode='cube',
  legend_position='top-center-h', legend_font_color='#9a9a9a',
  annotation_font_scale=70 -- all the mobile transforms that index
  used to apply silently
- DEFAULT_CONFIG has new keys with "keep original" defaults (auto,
  empty color, original position, 0% scale)

apply_config() additions:
- Scene aspectmode application
- Legend position presets (top-center-h, bottom-h)
- Legend font color override
- Legend border transparency
- Annotation font scaling (percentage, min 10pt, only fonts >12pt)
- Trace visibility (visible:false, non-destructive)
- Strip hidden traces (optional, removes from data array on export)

**index.html** (2,080 -> 1,898 lines, -182)

Removed: The entire `if (!isStudio) { ... }` block (was lines
1292-1454). This contained all 16 content transforms. Also removed
isStudio variable, isLightTheme detection (no longer needed for
branching), and the theme-dependent override cascade.

Added: Comment block explaining the Session 12 refactor and the
studio WYSIWYG authority principle.

Kept (structural viewer, unchanged):
- Template stripping (safety net for version mismatch)
- Fixed dimension removal + autosize
- Tall plot min-height (aspect >= 0.8)
- Post-render resize
- Mobile Plotly config (scrollZoom:true, doubleClick:false,
  displayModeBar:false on touch/small screens)
- Portrait click handler + info card parsing
- Tap hint for first portrait load
- D-pad / zoom control selection via _studio_nav flag
- All gallery chrome (navigation, share, URL routing, categories)

**json_converter.py**: No changes needed. The converter extracts
the full figure dict via bracket-matching, including all `_` prefixed
keys (_studio, _studio_nav, _encyclopedia, _routing_log). The index
cleans up the markers on read.

**Migration note**: Existing gallery content exported before this
refactor (without studio curation) will now render "raw" in the
gallery -- no dark theme overrides, no font scaling, no legend
repositioning. Those items need re-export through the studio with
the landscape preset to get equivalent treatment. This is by design:
the studio is now the authority, and the gallery should show exactly
what the studio previewed.

**Testing pass (Feb 16-17)**:

Bug found and fixed: `_apply_config_to_gui` referenced 4 new GUI
variables (`var_scene_aspect`, `var_legend_position`, `var_legend_color`,
`var_legend_border`) that were never created in `_build_config_sections`.
Root cause: agentic patch script matched tooltip strings that had
different wording in the actual file -- insertions silently failed.
Fixed by inserting controls with correct match targets.

GUI layout refined per Tony's feedback: Annotations moved from left
column to center; Hover, 2D Axes moved from center to right column
(below Portrait). Navigation Controls moved to column 1 (Session 16).
Final layout:
- Left: Title, Background, Margins, Legend, Navigation Controls
- Center: Annotations, Trace Visibility, Trace Appearance, Chrome
- Right: Portrait / Social, Hover, 3D Scene, 2D Axes

3D nav reset fix: original `Plotly.relayout(gd, {'scene.camera': null})`
launched camera into void. Fixed to capture initial camera in
`Plotly.newPlot().then()` callback and restore on reset. Pan step
changed from absolute 0.15 to relative 8% of camera distance. Zoom
reset not possible (WebGL limitation -- see Known Issues #29).

Landscape preset margins: top 40->80, left 20->80 for better spacing.

Nav arrows tooltip clarified as landscape-only (portrait uses touch).

Encyclopedia matching explained: exact trace-name-to-INFO-key lookup.
TOI-1338 A/B has no encyclopedia because INFO key is 'TOI-1338 Binary'
(name mismatch). Fix is in constants_new.py, not the studio.

All features confirmed working: encyclopedia "i" button (both modes),
trace visibility panel, Gallery Preview button, all 5 new controls,
saved config backward compatibility.

### Deferred Items (future phases)

- ~~Animation frame extraction in converter (Plotly.addFrames support)~~ DONE (Session 13)
- ~~Legend handling for high-trace-count figures~~ SOLVED (Session 10)
- ~~Studio social/portrait preset~~ SOLVED (Session 11)
- ~~Studio WYSIWYG authority~~ DONE (Session 12)
- ~~Trace visibility in studio~~ DONE (Session 12)
- ~~Gallery preview button~~ DONE (Session 12)
- ~~Encyclopedia data in JSON pipeline (studio embeds, index displays)~~ DONE (Session 12)
- ~~Version/update date in gallery footer~~ DONE (Session 12)
- ~~Custom pinch-to-zoom handler for 3D~~ SOLVED (Session 9 -- +/- buttons with synthetic WheelEvent)
- ~~Extract _parse_hover_html into shared hover_utils.py~~ DONE (Session 14 -- moved directly into gallery_studio.py)
- ~~Retire social_media_export.py export functions~~ DONE (Session 14 -- no remaining dependents)
- Thumbnail generation for gallery cards
- Link preview images for social sharing (og:image)
- Website content pages (About, Downloads, Contact)

### Immediate Next: Content Re-Population

The studio WYSIWYG refactor is complete. All content transforms now
live in the studio. Remaining work:

1. Re-export ALL existing gallery content through studio (landscape
   preset for standard views, portrait preset for social views) --
   required because the index no longer applies any content transforms
2. Validate each re-exported item: studio preview vs gallery preview
   vs live index (all three should match for Plotly content area)
3. Continue populating gallery with new content
4. Test on devices: iPhone Safari, Chrome, home screen bookmark
5. Polish: version stamp, first-visit hints

## Known Issues & Lessons

1. **3D plots in gallery view**: The 320px sidebar compresses the plot
   horizontally. This is inherent to the sidebar layout. The Expand button
   solves this -- users learn quickly. Not a bug, just a tradeoff.
   **Note**: Session 6 replaced the sidebar with a non-persistent overlay,
   eliminating this issue entirely.

2. **3D plots on mobile**: Desktop-exported 3D scenes preserve fixed aspect
   ratios that compress on portrait screens. The aspectmode override helps
   but needs per-visualization-type testing. Social view exports (built for
   portrait) look great on mobile; standard 3D exports need more work.

3. **Arbitrary test data**: Initial gallery was populated with old exports
   from various app versions. Some weren't generated by the current app.
   Testing with inconsistent data made it hard to distinguish gallery viewer
   bugs from data format issues. Decision: rebuild gallery systematically.

4. **Animation not yet supported**: json_converter.py extracts only `data`
   and `layout`. Plotly animated figures also have `frames` (injected via
   `Plotly.addFrames()` in the HTML). The gallery viewer's `Plotly.newPlot()`
   call does not pass frames. Both need targeted additions -- a few lines
   each. Deferred until static plots are solid.

5. **Mobile legend repositioning**: ~~The horizontal legend override
   (orientation: 'h', y: 1.02) on screens <1024px may conflict with titles
   on some visualizations.~~ **Session 12 resolved**: legend position is
   now a studio control (legend_position preset), not a hidden index
   override. Developer sees and adjusts per plot.

6. **Don't override what the export got right**: Lesson from Session 3,
   now the core principle of Session 12 -- the gallery viewer should apply
   NO content overrides. The studio makes all curation decisions. The
   index is a dumb renderer. Every forced layout change that was hidden
   from the developer has been moved to a visible studio control.

7. **Theme detection order matters** (Session 3 cont., resolved Session 5)
   -- json_converter strips templates during conversion. Any detection that
   relies on template contents must either (a) check before stripping, or
   (b) check what survives at the top level. **Session 5 fix**: the
   converter now promotes `paper_bgcolor` / `plot_bgcolor` from the template
   to top-level layout before stripping. This is the correct fix -- the
   theme signal is preserved at the source rather than requiring the viewer
   to guess.

8. **GitHub Pages deployment pattern** (Session 3 cont.) -- First deploy
   after adding a large file sometimes fails with "multiple artifacts"
   error. Re-running the failed workflow doesn't help (stale artifacts
   collide). Pushing a new commit creates a clean workflow run that
   succeeds. Rule: if deploy fails, don't re-run -- push a new commit.
   The handoff update serves as a natural second push.

9. **Social views lose context in gallery** (Session 3 cont.) -- Social
   HTML wraps the Plotly figure with a hover-driven info panel and
   branding. json_converter extracts only the figure. Without the wrapper,
   the plot has no title, no legend, no annotations. Title rescue (margin
   fix) helps minimally. **Session 6 resolved this** with the floating
   info card that reads social view customdata.

10. **Aspect ratio preservation for non-landscape plots** (Session 5) --
    Deleting `width` and `height` and setting `autosize: true` works for
    landscape plots but squishes tall/square ones (e.g., Planetary
    Boundaries at 1200x1100). The fix captures the original aspect ratio
    before deleting dimensions and applies a `min-height` constraint for
    plots with ratio >= 0.8. The container uses `overflow: auto` so tall
    plots can scroll.

11. **PNG cannot feed the gallery pipeline** (Session 5) -- Plotly's
    modebar "Download plot as PNG" produces a raster image with no figure
    data. json_converter.py requires HTML with embedded `Plotly.newPlot()`
    calls to extract traces and layout. Every visualization must go through
    `save_plot()` to produce HTML for the converter. No PNG shortcut exists.

12. **Plotly 3D camera is read-only** (Session 7) -- gl-plot3d's camera
    object (`distance`, `eye`, `lookAt`) cannot be modified externally.
    Direct assignment silently fails (getter/setter returns original).
    `Plotly.relayout` with `scene.camera.eye` causes clipping in
    orthographic projection rather than visual zoom. The only reliable
    zoom mechanism is dispatching synthetic `WheelEvent` to the canvas,
    piggybacking on Plotly's internal scroll handler.

13. **iOS home screen bookmark caching** (Session 7) -- Web apps added
    to iOS home screen have their own cache separate from Safari. Normal
    cache-clearing (Settings -> Safari) may not affect them. Swipe away
    from app switcher and reopen usually forces refresh. For persistent
    cache issues, delete the bookmark and re-add.

14. **Claude iOS sync is one-directional** (Session 7) -- In project
    conversations, messages sync desktop -> phone but not phone -> desktop.
    Artifacts generated in response to phone messages exist but aren't
    visible on desktop. Work around by testing on phone, downloading on
    desktop.

15. **Category definitions must be centralized** (Session 8) -- Three
    independent category lists (converter, editor, viewer) drifted. The
    converter had "Galactic Center" for sgr_a while the config had "Sgr A*".
    `gallery_config.json` is the single source of truth. All consumers
    read from it with hardcoded fallbacks for robustness.

16. **Non-contiguous category blocks in JSON** (Session 8) -- When vizs
    from the same category are scattered in gallery_metadata.json (e.g.,
    solar_system at indices 25, 26, and 29 with other categories between),
    simple block-swap reordering fails. The editor extracts all vizs for
    the mode, regroups by category, and reinserts -- also normalizing
    scattered entries as a side effect.

17. **Renaming categories changes keys too** (Session 8) -- Initially
    considered label-only rename, but Tony caught that misaligned keys
    and labels would be confusing. Rename now updates both `category`
    (key) and `category_label` on all affected vizs, plus the config
    entry. CSS color mapping in the gallery uses keys, so renamed
    categories fall back to the default color until the config color
    propagates on next page load.

18. **Mobile browser bottom toolbar clips content** (Session 8) --
    `100vh` on iOS Safari includes the area behind the toolbar, so
    content at the bottom of a `fixed` panel gets hidden. Fix requires
    two parts: (a) `viewport-fit=cover` in the meta tag to activate
    `env(safe-area-inset-bottom)`, (b) `height: 100dvh` on the overlay
    (dynamic viewport height adjusts for toolbar), and (c) generous
    bottom padding on the scrollable nav list (`calc(80px + env(...))`).
    Tested on iOS Safari, home screen bookmark, Chrome, and Bing --
    all clear after hard refresh. Chrome was initially cached and
    appeared unchanged until manually reloaded.

19. **2D plots need different zoom than 3D** (Session 9) -- 3D zoom
    dispatches synthetic `WheelEvent` to Plotly's WebGL canvas. 2D plots
    have no canvas; zoom is via `xaxis.range` / `yaxis.range` manipulation
    through `Plotly.relayout()`. Same UI buttons, different backend
    function, selected by a `data-scene` attribute on the button container.

20. **Plotly modebar is a problem on mobile** (Session 9) -- Moving the
    modebar DOM element to the toolbar row caused vertical icon stacking
    (icons designed to be horizontal in the chart corner). Hiding it
    entirely is cleaner -- mobile users have zoom buttons, pinch/pan,
    and tap-for-info which cover all needed interactions.

21. **Desktop nav button width causes overlap** (Session 9) -- The nav
    button shows the full visualization title, making it 200-400px wide.
    This overlaps Plotly's title, dropdown filters, and hover toggle
    buttons in the top-left. Hiding the label on desktop (CSS media query)
    reduces it to a ~40px hamburger icon. Full label shows on mobile
    where it's in the toolbar above the chart.

22. **Phone vs tablet breakpoint** (Session 9) -- 768px separates phones
    from tablets. Phones in landscape are typically 700-850px; tablets
    start at 768px. Below 768px, hide the Desktop/Mobile toggle and
    force portrait mode. Tablets (768-1023px) keep the toggle. Desktop
    mode on phones provides no value -- visualizations are distorted.

23. **dvh vs vh for Safari** (Session 9) -- `100vh` includes Safari's
    bottom toolbar area; `100dvh` (dynamic viewport height) excludes it.
    Use both: `height: 100vh` first (fallback), then `height: 100dvh`
    (override). CSS cascade means browsers supporting dvh use it; others
    silently ignore it and use vh. This is the proper fix for Safari
    bottom clipping on the app container.

24. **Annotation boxes need transparency, not removal** (Session 9 cont.)
    -- First instinct was to strip bordered annotations in the upper plot
    area. Too aggressive -- unknowable what future visualizations put
    there. Instead, make ALL annotation boxes transparent on mobile (strip
    bgcolor/bordercolor) but keep the text. The text scales via existing
    font reduction, and without the opaque background it doesn't block
    data. Generic solution that works for any content.

25. **Polar/radial charts are landscape-only** (Session 9 cont.) --
    Planetary Boundaries (1200x1100) needs width for wedge labels.
    Portrait mode crushes labels into overlapping mess. The min-height
    fix makes landscape scrollable (swipe to see full chart), but
    portrait is fundamentally unusable. Content curation (mode tagging)
    is the right tool, not code.

26. **Duplicate code blocks accumulate in iterative sessions** (Session 9
    cont.) -- Two mobile override blocks with slightly different margin
    values (95 vs 100) existed from separate edit sessions. Consolidated.
    Lesson: when editing index.html across multiple sessions, grep for
    existing blocks before adding new ones.

27. **Hidden transformations create developer-user gap** (Session 12
    planning) -- The studio preview shows curated output, but the index
    applies ~20 additional transforms the developer never sees (mobile
    font scaling, margin clamping, annotation stripping, etc.). The
    developer's last visual checkpoint before pushing doesn't match what
    the public sees. Solution: move all content transforms to studio,
    make index a dumb renderer. The _studio flag approach was a partial
    fix; full WYSIWYG authority is the complete solution.

28. **social_media_export.py is mostly superseded** (Session 12 planning)
    -- Gallery Studio now does everything the social export module did
    (hover routing, figure preparation, portrait HTML building) plus
    more (encyclopedia, configurable controls, landscape mode). The
    remaining unique value is the trace selection dialog. Plan: add
    non-destructive trace visibility to studio, then social export's
    export functions can be retired. Keep _parse_hover_html() as shared
    utility.

29. **3D zoom reset is not possible** (Session 12) -- Plotly's scroll
    wheel zoom modifies the WebGL projection matrix directly, below the
    level accessible via `getCamera()`/`setCamera()` or
    `Plotly.relayout()`. The reset button successfully restores camera
    orientation and pan position, but cannot restore zoom level. This is
    a Plotly.js limitation, not a bug in the nav controls. Users can
    scroll/pinch to rezoom manually. Pan and rotation reset work
    correctly.

30. **Agentic string matching can silently fail** (Session 12 testing)
    -- When patching files programmatically via string replacement, if
    the "old" string doesn't exactly match (e.g., tooltip text was
    reworded in an earlier session), the replacement silently succeeds
    with 0 matches. Variables get added to collection/application
    functions but never created as GUI widgets. Always verify new
    variables exist in the GUI builder, not just in the functions that
    read them.

31. **Encyclopedia matching is exact by trace name** (Session 12) --
    `extract_encyclopedia_for_figure` does `if name in INFO` with no
    fuzzy matching. Trace name must exactly match the INFO dict key.
    Mismatches like 'TOI-1338 A/B' vs 'TOI-1338 Binary' produce no
    entry. Fix in constants_new.py (add alias key), not in the studio.

32. **Nav arrows are landscape-only by design** (Session 12) --
    `build_social_html` (portrait) doesn't include nav controls.
    Portrait mode is for touch interaction (pinch/swipe). The nav
    checkbox tooltip now documents this.

## File Renaming Summary

| Old Name | New Name | Reason |
|----------|----------|--------|
| dash_converter.py | json_converter.py | Not Dash-specific; converts to JSON |
| dash_gallery.py | json_gallery.py | Local preview, not Dash-branded |
| /dash/ folder | /gallery/ folder | Distinct from app's data/, descriptive |

Note: The files in the app repo (/mnt/project/) still have old names
(dash_converter.py, dash_gallery.py). These should be renamed when
convenient, or left as-is since they'll live in the website repo anyway.

## Repository Structure

```
C:\Users\tonyq\OneDrive\Desktop\python_work\

    palomas_orrery_for_github\          (existing app repo)
        data\                           App cache/data
        images\                         HTML exports
        star_data\                      Stellar catalogs
        palomas_orrery.py
        ...

    tonyquintanilla.github.io\          (NEW website repo)
        index.html                      Gallery viewer (IS the homepage)
        gallery/                        JSON files + metadata + config
            gallery_metadata.json       Visualization index
            gallery_config.json         Category definitions (shared)
            earth_birthday_2025.json
            inner_planets_2025.json
            voyager_trajectories.json
            ...
        tools/                          Publishing infrastructure
            json_converter.py           HTML -> JSON converter
            json_gallery.py             Local Dash preview
            gallery_editor.py           Metadata + config editor GUI
```

Both repos appear side by side in GitHub Desktop's repo dropdown.
Switch between them to commit/push independently.

## Technical Notes

### Plotly Template Stripping

Both json_gallery.py (local) and index.html (GitHub Pages) strip the
embedded Plotly template on load. This prevents ValueError from version
mismatches (e.g., heatmapgl in newer Plotly) and reduces rendered size.

**Session 5 addition**: json_converter.py now promotes `paper_bgcolor`
and `plot_bgcolor` from the template to top-level layout before stripping.
This preserves the theme signal for the gallery viewer's light/dark
auto-detection. Without this, plots using `template="plotly_white"` lose
their bgcolor and get dark overrides applied incorrectly.

### HTML Extraction Method (json_converter.py)

Plotly.newPlot() calls in write_html output use heavy whitespace padding.
Regex fails. The reliable method is bracket-matching: find opening [,
count brackets accounting for strings/escapes, find matching ]. Same
for layout object.

### Minimal Override Principle (Session 3, refined Session 3 cont.)

The gallery viewer should apply the minimum overrides needed for the dark
theme and responsive sizing. The original Plotly exports contain carefully
placed margins, dropdown positions, title alignment, and element spacing.
Each forced layout change risks a visual regression.

**Theme auto-detection**: Before applying overrides, the viewer checks
whether the original plot was designed for a light background by examining
`layout.paper_bgcolor`, `layout.plot_bgcolor`, and (if present)
`template.layout.*` for light color values (white, #ffffff, #e5ecf6, etc.).
Light-themed plots skip ALL dark overrides and render with original colors.

Current overrides (dark-themed plots only):
- paper_bgcolor / plot_bgcolor: transparent (dark theme)
- font color: #e8e6e3 (light text for dark background)
- scene.bgcolor: transparent (3D dark theme)

Current overrides (all plots):
- autosize: true (fill container instead of fixed desktop dimensions)
- template: deleted (prevents version mismatch errors)
- width/height: deleted (let container control size)
- min-height: set for tall/square plots with aspect ratio >= 0.8 (Session 5)
- scene.aspectmode: 'cube' on mobile <1024px (fill portrait screen)
- legend: horizontal on mobile <1024px (dark-themed only)

Current overrides (mobile only, Session 7, expanded Session 9):
- layout.title: deleted (nav button shows viz name instead)
- scrollZoom: true (enables scroll/pinch zoom)
- doubleClick: false (prevents accidental double-tap reset)
- displayModeBar: false (zoom buttons + touch sufficient)
- Annotations with yref='paper' and y<0: removed (footer text)
- Annotation bgcolor/bordercolor/borderwidth/borderpad: stripped (transparent boxes, text kept)
- Legend bgcolor/bordercolor/borderwidth: stripped (transparent, markers kept)
- Non-animation updatemenus: removed (hover toggle buttons)
- Traces with customdata: default to names-only hovertemplate
- Axis title fonts >12: scaled to 75% (minimum 10)
- margin.t: clamped to 10 (title removed, modebar hidden)
- margin.b: clamped to 95 (room for x-axis tick labels)
- margin.l: clamped to 80 (room for y-axis title)
- colorbar/showscale: hidden (reclaim screen width)

NOT overridden (preserve from export):
- margins on desktop (export knows its element placement)
- updatemenus positions on desktop (staggered by the app)
- title alignment (left-justified by default)
- annotation positions and sizes (except font scaling on mobile <900px,
  and footer removal on mobile <1024px)
- light-themed plot colors (no dark overrides applied)

### 3D Zoom via Synthetic Wheel Events (Session 7)

Plotly.js 3D scenes (gl-plot3d) handle zoom internally through scroll
wheel events, but the camera API is completely read-only from JavaScript.
Neither `camera.distance`, `camera.eye`, `camera.lookAt()`, nor
`Plotly.relayout()` with camera parameters produces visual zoom on
orthographic projections -- they clip traces instead.

The solution dispatches synthetic `WheelEvent` to the WebGL canvas:
```javascript
var canvas = graphDiv.querySelector('.gl-canvas-focus') || graphDiv.querySelector('canvas');
var rect = canvas.getBoundingClientRect();
var evt = new WheelEvent('wheel', {
    deltaY: direction * 100,  // negative = zoom in
    clientX: rect.left + rect.width / 2,
    clientY: rect.top + rect.height / 2,
    bubbles: true, cancelable: true
});
canvas.dispatchEvent(evt);
```

This works because Plotly's internal wheel listener on the canvas does
whatever internal state manipulation is needed -- we don't need to know
the mechanism, just trigger it.

**Limitation discovered (Session 12)**: This same opacity -- the zoom
operating at WebGL level below the Plotly API -- means we cannot
programmatically read or restore the zoom level. `getCamera()` returns
eye/center/up but not the projection zoom factor. The reset button
restores orientation and pan but not zoom. Acceptable tradeoff: users
scroll/pinch to rezoom.

### 2D Zoom via Axis Range Scaling (Session 9)

2D plots have no WebGL canvas, so synthetic wheel events don't apply.
Instead, zoom scales axis ranges around their center point:
```javascript
function zoom2D(direction) {
    var factor = (direction > 0) ? 1.3 : 1 / 1.3;
    var update = {};
    // For each xaxis/yaxis in the layout:
    var center = (lo + hi) / 2;
    var half = (hi - lo) / 2 * factor;
    update[axisName + '.range'] = [center - half, center + half];
    Plotly.relayout(graphDiv, update);
}
```

The same +/- buttons dispatch to `zoom3D` or `zoom2D` based on a
`data-scene` attribute set when the visualization loads (`'3d'` if
`layout.scene` exists, `'2d'` otherwise). Buttons are now visible on
all devices and plot types (Session 9).

### Older HTML Files

Files generated by earlier app versions may use different HTML structures.
Rather than adding extraction patterns for every historical format,
re-export from the current app.

### GitHub Pages Notes

- Both repos must be public for free GitHub Pages
- The website repo source is visible but nobody browses it -- they visit the URL
- GitHub Pages serves from the main branch root by default
- Changes go live within minutes of pushing
- Custom 404.html can redirect to index.html for cleaner routing (future)

### Instagram Reel Workflow (9:16 on Laptop)

Portrait/social HTML previews render at 16:9 on a laptop browser by
default. To capture 9:16 content for Instagram Reels in Clipchamp
without using a phone:

1. Open portrait preview HTML in Chrome or Edge
2. Press **F12** to open DevTools
3. Click the **device toolbar icon** (phone+tablet icon, top-left of
   DevTools) or press **Ctrl+Shift+M**
4. Select a device preset (e.g., "iPhone 14 Pro Max") or set custom
   dimensions like **430 x 932** for 9:16
5. The page renders at phone proportions on the laptop screen --
   touch interactions become clicks, portrait layout activates
6. Screen-record that browser window in Clipchamp

This gives the exact phone rendering without needing the phone.
DevTools responsive mode is a phone simulator built into every
Chromium browser. Works for both gallery viewer testing and
Reel production.

## Session Decisions Log

| Question | Decision | Rationale |
|----------|----------|-----------|
| Homepage = gallery? | Yes | Gallery IS the site for Phase 1 |
| Data folder name | /gallery/ | Distinct from app's /data/, descriptive |
| File renaming | json_converter.py, json_gallery.py | Clearer purpose |
| Separate repos | Yes | App stays pure, website is publishing |
| Repo visibility | Both public | Required for free GitHub Pages; fine |
| Mobile approach | Responsive breakpoints (<1024px) | One page adapts; Plotly handles resize |
| Plotly.js source | CDN | Keeps HTML small, always current |
| Gallery content | Rebuild systematically | Old exports caused false-positive bugs |
| Custom domain | Future (Phase 4) | Get gallery working first |
| URL rename | Keep as-is (tonyquintanilla.github.io) | Save branding for custom domain later |
| Save format | Standard HTML (~10 KB) | Smaller source; converter strips JS anyway |
| Squished gallery view | Fullscreen toggle, not hover-hide | Predictable UX, no accidental triggers |
| Layout overrides | Minimal -- preserve export | Every override risks visual regression |
| Static before animation | Yes | Stable baseline before adding complexity |
| Theme detection | Auto-detect from bgcolor | No metadata flags needed; zero maintenance |
| Social views in gallery | Removed for now | Info panel can't be replicated from JSON alone |
| Failed deploy fix | Push new commit, not re-run | Re-run inherits stale artifacts; fresh push is clean |
| Local testing | python -m http.server 8080 | Tests real viewer, not Dash; instant feedback |
| Mobile strategy | Desktop/Mobile modes | One gallery, two modes, user-selectable |
| Info panel in gallery | Floating card, not persistent panel | Maximizes screen; panel stays in social_media_export.py |
| Navigation | Non-persistent overlay selector | Full-screen always; no sidebar compression |
| Mode naming (UI) | Desktop / Mobile | Cross-platform intuitive; not device-specific |
| Mode naming (internal) | landscape / portrait | Backward compatible with metadata |
| Mode default | Auto-detect from screen width | <1024px defaults Mobile; user can switch |
| Hover parsing location | Python at conversion time | Proven code; gallery JS stays simple |
| Social view pipeline | Same JSON pipeline, tagged | social_media_export.py stays for video production |
| Save dialog for all plots | Add save_plot to all open_ functions | Every viz needs HTML path for gallery pipeline |
| Theme preservation | Promote bgcolor before template strip | Fix at source (converter), not destination (viewer) |
| Tall plot handling | min-height from aspect ratio >= 0.8 | Landscape plots unaffected; square/tall get protection |
| viz-container overflow | auto instead of hidden | Tall plots can scroll; landscape plots unchanged |
| Sidebar removal | Non-persistent overlay replaces 320px sidebar | Full-screen always; no compression problem |
| Fullscreen toggle | Removed (no longer needed) | Everything is fullscreen by default |
| Nav button label | Shows current viz name or app title | Context always visible; replaces viz-header bar |
| Share button position | top:52px to clear Plotly modebar | Avoids icon overlap |
| One interaction model | Same overlay on phone + tablet + desktop | No device-specific code paths |
| Info card interaction | Peek (left-click) + Pin (right-click) | Emergent from event propagation; no custom code |
| Info card scope | Mobile mode only (for now) | Desktop uses standard Plotly hover tooltips |
| Mode filtering | Filter nav list by metadata mode field | Items without mode default to landscape |
| Converter mode prompt | L/P/B during interactive conversion | Defaults to landscape; backward compatible |
| Converter hover parsing | Dropped (Step 4) | Desktop = native hover; mobile = social customdata; no conflict |
| 3D zoom on mobile | Synthetic wheel event buttons | Plotly camera API is read-only; wheel events work |
| Zoom button visibility | Mobile mode + 3D scenes only | Desktop has scroll wheel; 2D has native pinch |
| Mobile title suppression | Delete layout.title on <1024px | Nav button already shows name; avoids overlap |
| Plotly config scoping | scrollZoom/doubleClick mobile only | Desktop behavior completely unchanged |
| Click handler scoping | Mobile mode only | Desktop uses standard Plotly hover tooltips |
| Category definitions | gallery_config.json | One source of truth for converter, editor, and viewer |
| Config fallback | Hardcoded dict in each consumer | gallery_config.json not found = still works |
| Category colors at runtime | JS loads from config, falls back to defaults | New categories get colors without editing HTML |
| Gallery editor | Tkinter GUI in tools/ | Consistent with orrery's GUI style; no new deps |
| Category order in editor | Derived from JSON sequence | Matches gallery rendering exactly; no hardcoded order |
| Category reorder mechanism | Extract mode vizs, regroup, reinsert | Handles non-contiguous category blocks correctly |
| Copy visualization | Deep copy with _copy ID suffix | Same viz can appear in multiple categories/modes |
| Rename category | Changes both key and label | Keys aligned with labels; no confusion |
| Empty categories in editor | Shown from config, even with no vizs | Can see all available categories per mode |
| Mobile bottom toolbar fix | 100dvh + 80px padding + viewport-fit=cover | Tested on Safari, Chrome, Bing, home screen |
| Footer strip on mobile | Remove annotations below plot (y<0) | Reclaims 15-20% vertical space |
| Hover toggle strip on mobile | Remove non-animate updatemenus | Default names-only; full hover unreadable on touch |
| X-axis title strip on mobile | Delete xaxis.title | Spectral types + numbers self-explanatory |
| Modebar on mobile | Hide entirely (displayModeBar: false) | Zoom buttons + touch gestures are sufficient |
| 2D zoom buttons | Scale axis ranges via Plotly.relayout | Same UI as 3D; consistent interaction model |
| Zoom buttons on desktop | Show for all modes and plot types | Useful for trackpad users |
| Desktop nav button label | CSS hide >1024px (icon only) | Prevents overlap with Plotly title + updatemenus |
| Phone mode lock | Hide mode toggle <768px | Desktop viz distorted on phones; no benefit |
| Safari dvh fix | 100vh fallback + 100dvh override | CSS cascade; dvh-capable browsers use it, others ignore |
| HR diagrams mode | "both" (works landscape + portrait) | 2D plots adapt well to any aspect ratio |
| Annotation boxes on mobile | Strip bgcolor/border, keep text | Text scales; opaque boxes block data |
| Legend boxes on mobile | Make transparent, keep markers | Markers readable; boxes obstruct |
| Axis title scaling | Font 75% on mobile (min 10) | Same pattern as annotation scaling |
| X-axis title deletion | Reverted (too aggressive) | HR diagrams ok without; climate charts need "Year" |
| Complex chart mode | Landscape with title hint | Polar/busy charts need width; "(swipe to explore)" |
| Welcome device hints | CSS-only per breakpoint | Phone users learn about desktop; no JS needed |
| Paleoclimate charts | Removed from gallery | Too busy for any mobile view; revisit later |
| Per-plot curation | Gallery Studio (gallery_studio.py) | Generic cleanup can't make per-plot decisions |
| Studio override mechanism | _studio flag in layout | Survives JSON extraction; index skips overrides |
| Pan arrows in gallery | _studio_nav flag + D-pad in index | Arrows embedded in studio HTML lost by json_converter |
| Background presets | Dark/Light/Plotly buttons + color picker | Typing hex codes is error-prone |
| Auto text color | ITU-R BT.601 brightness detection | Dark bg = light text, light bg = dark text |
| Paleoclimate charts | Reinstated via studio | Per-plot font sizing + pan arrows make them viable |
| Social view relationship | Studio complements, not replaces | Social = 9:16 Instagram; Studio = gallery curation |
| Studio re-export | Studio can reload its own output | Iterative refinement without re-exporting from source |
| Portrait preset | One-click 9:16 with info panel | Absorbs social_media_export.py layout into studio workflow |
| Cross-dir import | Walk up tree, check candidates | gallery_studio in tools/ needs orrery/ modules two levels up |
| Reuse _parse_hover_html | Import, don't reimplement | One parser for hover decomposition; tested pattern |
| Debug logging in HTML | Console.log routing + trace state | Stacked bugs need pipeline-wide visibility |
| Studio as WYSIWYG authority | Studio makes ALL curation decisions; index is dumb renderer | Developer sees what user sees; no hidden transformations |
| Index role after refactor | Structural viewer only (nav, container, share) | No content opinions; static site generator pattern |
| Trace selection in studio | Non-destructive visibility toggles (visible:false) | Replaces social_media_export.py dependency; reversible |
| Preview as Gallery | Simulates index rendering in studio | Closes developer visibility gap before GitHub push |
| One pipeline for web + social | Gallery mobile view IS the Instagram reel source | No bifurcated workflows; one pipeline, one output |
| Landscape default preset | Applies what index did silently, but visibly | Studio is non-burdensome; presets handle 90% of cases |
| social_media_export.py future | Keep _parse_hover_html + trace selection; export functions superseded | Studio does everything the export module did, plus more |
| Device adaptation in index | Mobile Plotly config stays (scrollZoom, no modebar) | Structural like CSS media queries, not content decisions |
| Trace visibility mechanism | visible:false (non-destructive) | Data stays in file; can re-enable in studio |
| Strip hidden traces | Optional checkbox on export | File size reduction when traces definitely unneeded |
| Gallery Preview viewer | Minimal HTML with NO content transforms + gold banner | WYSIWYG verification before GitHub push |
| Old gallery content | Must re-export through studio | Index no longer provides any content safety net |
| Annotation font scale | Percentage-based (100=keep, 70=typical mobile) | More flexible than index's hardcoded 70% on <900px |
| Scene aspectmode | Studio control, not device detection | Developer chooses cube/auto per plot, not per screen size |
| GUI column reorg | Annotations->center, Hover/2D/Nav->right | Better visibility; left column was too long |
| 3D nav reset | Capture camera on render, restore via relayout | setCamera alone doesn't reset zoom; relayout resets orientation+pan |
| 3D zoom reset | Accept limitation | WebGL projection matrix below Plotly API reach; not worth chasing |
| 3D pan step | Relative to camera distance (8%) | Prevents absolute step launching camera into space at close zoom |

### Session 13 (Feb 17): Animation Support -- Frames Pipeline

Animations from the desktop app (play/pause slider, frame-by-frame stepping)
now flow through the entire gallery pipeline. This unlocks both
`animate_objects` exports (planetary system animations) and the Sgr A*
Grand Tour for the web gallery.

**The problem**: Plotly animations consist of three parts: `data` (traces),
`layout` (axes, UI controls, sliders), and `frames` (per-step updates to
trace positions). The existing pipeline extracted data and layout but silently
dropped frames. The slider rendered (it lives in layout) but pressing Play
did nothing because the frame data it referenced wasn't loaded.

**Three files changed**:

1. **index.html** (+4 lines) -- After `Plotly.newPlot()`, checks for
   `figDict.frames` and calls `Plotly.addFrames()` if present. Non-animated
   visualizations unaffected (no frames key = no action).

2. **json_converter.py** (new `_extract_frames` function) -- Extracts
   animation frames from HTML during conversion to JSON. Handles two formats:
   - `var frames = [...]` -- from Gallery Studio re-exports
   - `Plotly.addFrames('id', [...])` -- from Plotly `write_html()` output

3. **gallery_studio.py** (frames extraction in `extract_figure_from_html`) --
   Same dual-format extraction, applied after any successful data/layout
   extraction method (newPlot, react, or variables). Frames flow through
   `apply_config`, into `build_gallery_html` / `build_social_html` templates,
   and render in the Studio preview.

**Bugs encountered and fixed**:

1. **Single vs double quotes** -- Plotly's `write_html()` wraps the div ID
   in single quotes (`'uuid-string'`), not double quotes. The initial
   extraction looked for `",` to find the end of the div ID, which scanned
   past it into the frame data JSON. Fix: skip directly to the first `[`
   after `Plotly.addFrames(` regardless of quote style.

2. **Early return in Studio extraction** -- `extract_figure_from_html` tried
   `_extract_newplot` first, which returned `{data, layout}` without frames.
   Since it succeeded, the function returned immediately -- the frames
   extraction code (added to `_extract_variables`) was never reached. Fix:
   restructured to extract data/layout first via any method, then always
   attempt frames extraction afterward.

3. **Two frame formats** -- Plotly `write_html()` uses
   `Plotly.addFrames('id', [...])`. Gallery Studio re-exports use
   `var frames = [...]`. The converter initially only handled the first
   format, but Studio-exported HTML (the primary input to the converter)
   uses the second. Fix: check both formats in both extractors.

**Validation**: Tested with Paloma's Birthday animation (21 years,
year-by-year, inner solar system). Animation plays in Studio preview,
gallery landscape mode, and gallery portrait/mobile mode. Slider, Play/Pause,
and manual frame stepping all functional.

**Pipeline with frames**:
```
Desktop App (animate_objects / Sgr A* Grand Tour)
    |
    v
save_utils.py -> write_html() with frames as Plotly.addFrames('id', [...])
    |
    v
Gallery Studio (extracts frames, includes in preview and re-export)
    |-- Preview: frames loaded via Plotly.addFrames in template JS
    |-- Export: frames embedded as var frames = [...] in output HTML
    |
    v
json_converter.py (extracts frames from either format, includes in JSON)
    |
    v
JSON files with "data", "layout", AND "frames" keys
    |
    v
index.html (Plotly.newPlot + Plotly.addFrames if frames present)
    |
    v
Animated visualizations in the browser
```

**What this enables**:
- Any `animate_objects` export (day/week/month/year stepping) in the gallery
- Sgr A* Grand Tour with mode switching and animated orbital motion
- Paloma's Birthday animation as a shareable link
- All existing static visualizations completely unaffected

**File sizes**: The Paloma's Birthday animation JSON (21 frames, 25 traces
per frame) is a reasonable gallery item. The Sgr A* Grand Tour (140 frames,
mode-switched visibility arrays) will be larger but should be manageable --
to be tested next.

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Animation in gallery | Extract and load frames through full pipeline | One pipeline handles static and animated content |
| Frame extraction format | Support both `Plotly.addFrames()` and `var frames` | Two producers (write_html vs Studio) use different formats |
| Div ID quote handling | Find first `[` instead of parsing quotes | Quote-agnostic; simpler and more robust |
| Extraction architecture | Frames extracted after data/layout, not inside individual methods | Runs regardless of which extraction method (newPlot/react/variables) succeeds |
| Sgr A* approach | Start with Grand Tour through standard pipeline | Test animation support before adding category content |

### Session 14 (Feb 19): Pipeline Bridge -- Annotation Toggle + Nav Controls

Two Studio features that worked in standalone HTML exports were silently
lost in the gallery viewer. Both had the same root cause: `json_converter`
extracted only Plotly `data` and `layout`, discarding the HTML wrapper
where Studio embeds interactive controls as CSS/HTML/JS.

**Feature 1: Annotation Toggle Button**

Climate visualizations have dense text annotations (data labels, status
boxes, attribution) that help on desktop but obscure the graphic on
phones. Studio already had "remove annotations" but that was all-or-nothing.

Solution: A "Show Labels / Hide Labels" button that lets viewers toggle
annotations at runtime via `Plotly.relayout()`.

- `gallery_studio.py`: New `annotation_toggle_button` config option and
  GUI checkbox. When enabled, processed annotations are stored in
  `layout['_toggle_annotations']` (underscore prefix = stripped before
  Plotly sees it). Button CSS/HTML/JS embedded in standalone HTML export.
  Initial state respects `show_annotations` setting (hidden or visible).
  Also: `_parse_hover_html` moved in from `social_media_export.py`,
  eliminating the cross-directory import machinery (~30 lines removed).
- `json_converter.py`: New `_extract_toggle_annotations()` finds
  `var _annStored = [...]` in source HTML using bracket-matching. Saved
  as top-level `toggle_annotations` key in gallery JSON.
- `index.html`: New `.ann-toggle` button with gallery control styling.
  Uses `touchstart` + `mousedown` (same pattern as zoom/pan) for iOS
  WebGL compatibility. Button resets on viz load and home navigation.
  On mobile (<=1024px), moves into toolbar via JS alongside nav/share
  buttons to prevent overlap.

**Feature 2: Nav Controls (Pan/Zoom Arrows)**

Studio's "Show nav arrows" checkbox produced a D-pad in preview and
standalone HTML, but the arrows disappeared in the gallery viewer.

Solution: Converter now detects nav controls in source HTML and signals
the gallery viewer.

- `json_converter.py`: Detects `class="nav-controls"` + `function panPlot`
  in HTML, sets `layout._studio_nav = true` in JSON output.
- `index.html`: Already had `_studio_nav` reading logic (line 1459) --
  it switches from simple +/- zoom to the full pan/zoom D-pad. The code
  was there; it just never received the signal.

**The Pipeline Bridge Pattern**

Both fixes follow the same pattern that emerged from Session 13's
animation work:

```
Studio embeds feature in HTML wrapper
    |
    v
json_converter detects it in source HTML (content signatures, not config)
    |
    v
Converter preserves signal in JSON (top-level key or layout flag)
    |
    v
index.html reads signal and renders the feature
```

This is now the standard approach for any Studio feature that needs to
survive the JSON pipeline. Detection uses content signatures in the HTML
(class names, function names, variable declarations) rather than config
file lookups -- more robust, works even if configs are missing.

**Testing**: Verified on desktop browser (landscape), iPhone Safari,
iPhone Chrome, iPhone Home Screen (PWA mode). Toolbar layout prevents
button overlap on all mobile configurations.

**Cleanup: _parse_hover_html moved into gallery_studio.py**

The hover text parser was the last functional dependency on
`social_media_export.py`. Moved the ~60-line function directly into
`gallery_studio.py` (before `apply_config`) and removed ~30 lines of
cross-directory import machinery that hunted for the old file. Studio
no longer imports from `social_media_export.py` at all.

This retires two deferred items at once: the function extraction and
the `social_media_export.py` retirement. The old file can remain in
the repo for reference but has no dependents.

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Annotation toggle in gallery | Extract stored annotations, render button in viewer | Same content, viewer chooses visibility |
| Nav controls in gallery | Detect in HTML, signal via `_studio_nav` flag | Viewer already had rendering code; just needed the signal |
| Detection method | Content signatures in HTML, not config lookup | Robust; works without config file; self-documenting |
| Mobile button layout | Move toggle into toolbar alongside nav/share | Prevents overlap; consistent with existing mobile pattern |
| Toggle initial state | Respects `show_annotations` setting | Phone-first exports start hidden; desktop-first start visible |
| _parse_hover_html location | Move into gallery_studio.py directly | Simpler than shared module; eliminates cross-directory import; retires social_media_export dependency |

### Session 15 (Feb 20): Polar Chart Support + Label Font Scaling

The Planetary Boundaries radar chart (polar/barpolar) exposed two gaps
in the gallery infrastructure: pan/zoom controls didn't work, and the
text labels were too large for mobile.

**Bug: Pan/Zoom Buttons Had No Effect on Polar Charts**

The D-pad and zoom buttons worked for cartesian (xaxis/yaxis) and 3D
(scene.camera) charts, but did nothing on polar charts. Same bug in
two places: the gallery viewer (`index.html`) and the studio preview
HTML builder (`gallery_studio.py`).

Root cause (zoom): `zoom2D()` searched for `xaxis`/`yaxis` in the
layout -- polar charts use `polar.radialaxis.range` instead. Even
after fixing the key path, Plotly still ignored the range update
because `radialaxis.autorange` defaults to `true` and overrides
explicit range values.

Root cause (pan): Same xaxis/yaxis assumption. For polar charts,
"panning" maps to rotating the angular axis -- left/right change
`polar.angularaxis.rotation`, up/down map to zoom in/out (since
vertical translation doesn't apply to radial layouts).

Fix in `index.html`:
- Scene type detection now distinguishes `'3d'`, `'polar'`, and `'2d'`
- `zoom2D()`: detects `layout.polar`, scales `radialaxis.range[1]`,
  sets `autorange: false` to prevent Plotly from overriding
- `pan2D()`: detects `layout.polar`, rotates `angularaxis.rotation`
  by 15 deg per tap (left/right), delegates up/down to zoom
- `captureOriginalRanges()`: captures polar radial range, rotation,
  and autorange state for reset
- `resetPanZoom()`: restores all three polar properties

Fix in `gallery_studio.py` (parallel pipeline):
- Added `has_polar` detection alongside `has_scene`
- New `elif has_polar:` branch in `build_gallery_html()` generates
  polar-aware `panPlot()`/`zoomPlot()` JS with the same autorange fix
- Preview HTML now matches gallery viewer behavior for polar charts

**Lesson**: Parallel pipeline problem (protocol anti-pattern). The same
pan/zoom logic existed in two places -- `index.html` for the gallery
viewer and `gallery_studio.py` for the preview HTML. Fixing one didn't
fix the other. Both needed the polar branch and the `autorange: false`
fix independently.

**Feature: Label Font Scaling (`label_font_scale`)**

Polar chart text labels (boundary names like "CLIMATE CHANGE",
"BIOSPHERE INTEGRITY") were sized for desktop and too large on phones.
The existing `annotation_font_scale` only affects layout annotations,
not trace `textfont` labels.

New `label_font_scale` config option in `gallery_studio.py`:
- Same pattern as `annotation_font_scale`: 100 = keep original,
  50-200 = percentage of original size (standardized Session 16)
- Scales `textfont.size` on all traces that have it
- Also regex-scans trace `text` HTML strings for inline
  `font-size:Npx` patterns and scales those too -- this catches
  secondary labels (grey subtext like "Radiative forcing",
  "CO2 concentration") that use inline CSS rather than textfont
- GUI spinbox in the Annotations section of the studio
- Baked into JSON at export time (not a runtime viewer control)

The font scaling question initially surfaced as "add A+/A- buttons to
the viewer" but Tony caught it: this is a studio curation decision,
not a viewer runtime control. Follows the WYSIWYG principle -- what
you configure in studio is what the viewer renders.

**Feature: Per-Axis Title and Tick Label Scaling**

The Global Temperature Anomalies chart on mobile had an x axis title
("Year (decimal notation: 2024.96 = late December)") crowding the
plot. The tick labels (years) were sufficient -- the title was
redundant on a small screen. But the existing `axis_title_font_size`
was a single absolute-pixel control applied to all axes at once.

Replaced the two old fields (`axis_title_font_size`,
`axis_tick_font_size`) with four new percentage-based controls:

| Field | 0 | 1-99 | 100 (default) |
|-------|---|------|---------------|
| `x_title_scale` | Remove x axis title | Scale % | Keep original |
| `y_title_scale` | Remove y axis title | Scale % | Keep original |
| `x_tick_scale` | Hide x tick labels | Scale % | Keep original |
| `y_tick_scale` | Hide y tick labels | Scale % | Keep original |

Design notes:
- 0/100 pattern for axis titles (0=remove, 100=keep) is specific to
  axis controls where 0 means "actively remove the title" -- distinct
  from the font scaling convention where 100=keep (Session 16 standard)
- Separate X/Y because the common case is asymmetric: remove x title
  (redundant with tick labels) but keep y title (describes the units)
- GUI puts X and Y on the same row to keep the section compact
- Old fields still read as backward-compat fallback
- Social preset sets both titles to 0 (remove) since portrait charts
  need maximum plot area

**Feature: Secondary Y Axis Controls**

Extended axis scaling to support secondary Y axes (`yaxis2`, `yaxis3`,
etc.) independently from the primary Y axis. Common in dual-axis
climate charts where temperature and CO2 share an X axis but have
different Y scales.

GUI reorganized from two rows (X title + Y title, X ticks + Y ticks)
to a three-row grid with column headers:

```
          Title %   Ticks %
X axis:   [100]     [100]
Y axis:   [100]     [100]
Y2 axis:  [100]     [100]
```

The apply logic uses `key != 'yaxis'` to distinguish primary from
secondary -- all numbered Y axes (yaxis2, yaxis3, ...) share the Y2
controls.

**Bug Fix: Colorbar Not Hiding on Heatmap Traces**

The "Show colorbar" checkbox had no effect on heatmap-type traces
(warming stripes, contour plots). The colorbar removal code only
checked `trace.marker.colorbar` (scatter-style traces with colormapped
markers) and existing `showscale` keys. Heatmaps put the `colorbar`
dict directly on the trace -- no `marker` wrapper -- and `showscale`
isn't present until explicitly set.

Fix: Added check `if 'colorbar' in trace: trace['showscale'] = False`.
Covers heatmaps, contour plots, and any trace type with a top-level
colorbar.

Discovery path: Tony unchecked the legend expecting the color scale
to disappear. It didn't. Investigation revealed it was actually a
colorbar (not a legend), and the colorbar checkbox was also broken.
Two insights from one symptom -- legend vs colorbar distinction, plus
the heatmap colorbar bug.

**Bug Fix: Welcome Screen Visualization Count**

The gallery welcome screen showed the total count across all modes
(e.g., "46 visualizations") regardless of whether the user was in
Desktop or Mobile mode. On mobile, where only 21 of 46 visualizations
are available, this was confusing -- especially alongside the hint
"More visualizations available on desktop."

Fix: New `updateWelcomeCount()` function counts only visualizations
matching the current mode (portrait+both or landscape+both). Called
on init, on `setMode()`, and on home navigation reset. The home reset
was also missing the `welcomeVersion` div entirely -- the count
disappeared when navigating home via the logo.

**Feature: Chlorophyll Green Background Preset**

Added a "Green" button to the background color presets row:
`#2d6a2d` with warm light title text `#f0f4e8`. Designed for Earth
system and climate visualizations -- planetary boundaries, biosphere
integrity, ecology themes. The warming stripes on chlorophyll green
is a striking combination.

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Polar pan/zoom | Detect `layout.polar`, use radialaxis.range + angularaxis.rotation | Polar charts have no xaxis/yaxis; need native polar axis manipulation |
| autorange override | Set `autorange: false` alongside range update | Plotly default `autorange: true` silently overrides explicit range values |
| Pan mapping for polar | Left/right = rotate, up/down = zoom | Rotation is the natural "pan" for radial layouts; vertical shift doesn't apply |
| Label font control | Studio config (`label_font_scale`), not viewer runtime | Curation decision belongs in studio; WYSIWYG principle |
| Secondary label scaling | Regex inline `font-size:Npx` in trace text HTML | Some labels use inline CSS rather than textfont.size; both must scale together |
| Parallel pipeline fix | Both index.html and gallery_studio.py need polar branches | Preview and gallery viewer generate pan/zoom JS independently |
| Axis control granularity | Separate X/Y, percentage scale (0-100) | Common case is asymmetric (remove x title, keep y); consistent pattern across studio |
| Checkboxes vs spinboxes | Spinboxes (0-100) | Consistent with other font controls; scaling occasionally useful; checkboxes would be one-off |
| Secondary Y axis | Separate Y2 controls, shared across yaxis2+ | Common dual-axis charts need independent control; primary vs numbered distinction is clean |
| Heatmap colorbar removal | Check `'colorbar' in trace` at trace level | Heatmaps don't use `marker.colorbar`; need top-level check |
| Welcome count | Filter by current mode, update on mode switch | Total count misleading when mobile shows subset; "more on desktop" hint needs matching number |
| BG color presets | Add chlorophyll green (#2d6a2d) | Earth system content benefits from thematic background; warming stripes + green is striking |

### Session 16 (Feb 23): Font Scale Standardization + Original Preview

Standardized all font controls in Gallery Studio to use a consistent
percent scale (100% = keep original), added an "Original" preview
button, and reorganized the GUI column layout.

**Font Scale Standardization**

Previously, font controls used three different conventions:
- `legend_font_size: 11` -- absolute pixel override
- `annotation_font_scale: 0` -- 0=keep, 50-100=percentage
- `label_font_scale: 0` -- 0=keep, 50-100=percentage
- Title font was always absolute pixel

This was confusing: "0" meant "keep original" for annotations but
would mean "zero pixels" intuitively. And the legend control
hardcoded 11px regardless of what the source plot used.

All font controls now use the same convention:

| Control | Config Key | Default | What it scales |
|---------|-----------|---------|----------------|
| Title font % | `title_font_scale` | 100 | `layout.title.font.size` |
| Legend trace font % | `legend_font_scale` | 100 | `layout.legend.font.size` |
| Legend category font % | `legend_grouptitle_font_scale` | 100 | `trace.legendgrouptitle.font.size` |
| Annotation font % | `annotation_font_scale` | 100 | `annotation.font.size` |
| Label font % | `label_font_scale` | 100 | `trace.textfont.size` + inline |

All use: 100% = keep original, range 50-200, spinbox increment 5.
Fallback to sensible defaults (e.g., 18px for title) when the source
plot has no value to scale from.

**New: Legend Group Title Scaling**

The energy imbalance chart uses `legendgrouptitle` for category
headers ("Measurements", "Ocean Heat (0-2000m)"). These weren't
affected by the existing legend font size control because they're
per-trace properties, not layout-level. New `legend_grouptitle_font_scale`
scales these independently.

**New: Title Font Scaling**

Title was previously an absolute pixel override (`title_font_size: 18`)
that ignored the source plot's title size. Now uses percent scale
like all other font controls. Custom titles just swap the text --
the percent scale applies to whatever the source title's font size
was (or 18px default if no source title exists).

**New: "Original" Preview Button**

Three preset buttons now in the Portrait section:
- **Portrait Preset** (was "Apply Portrait Preset") -- social media settings
- **Landscape Preset** (was "Back to Landscape") -- gallery-ready defaults
- **Original** -- opens browser preview of the raw figure with zero
  studio transforms. No margin changes, no font scaling, no legend
  adjustments. Useful for A/B comparison against configured settings.

The rename from "Apply Portrait Preset" / "Back to Landscape" to
"Portrait Preset" / "Landscape Preset" clarifies that both are
opinionated presets, not restores. "Original" is the true restore.

**GUI Column Reorganization**

Moved 3D Scene from column 1 to column 3 (above 2D Axes) and
Navigation Controls from column 3 to column 1 (after Legend):
- Left: Title, Background, Margins, Legend, Navigation Controls
- Center: Annotations, Trace Visibility, Trace Appearance, Chrome
- Right: Portrait / Social, Hover, 3D Scene, 2D Axes

Rationale: 3D Scene and 2D Axes are rendering-type controls that
belong together. Navigation Controls is a layout decision that
belongs with Title, Margins, and Legend.

**Config Migration**

`_load_config_store()` now migrates old-format saved configs:
- `legend_font_size` (absolute) -> `legend_font_scale: 100`
- `title_font_size` (absolute) -> `title_font_scale: 100`
- `annotation_font_scale: 0` -> `annotation_font_scale: 100`
- `label_font_scale: 0` -> `label_font_scale: 100`
- Missing `legend_grouptitle_font_scale` -> added at 100

Existing `gallery_studio_configs.json` files load without issues.

**Portrait preset** uses 85% for legend fonts (trace + grouptitle)
and 70% for annotations.

**gallery_studio.py** (~3,900 lines, up from ~3,500 in Session 15)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Font scale convention | 100% = keep original (not 0=keep) | Intuitive; matches what percent means; consistent across all controls |
| Font scale range | 50-200, increment 5 | Allows both shrink and enlarge; 5% steps are fine-grained enough |
| Legend font approach | Percent of original (not absolute px) | Source plot chose its font for a reason; scaling preserves proportions |
| Legend group titles | Separate control from trace labels | Category headers and trace names have different visual roles |
| Title font approach | Percent scale, custom title just swaps text | One control, not two; simpler; custom title doesn't imply different font logic |
| "Original" button | Preview from raw figure, no transforms | Developer needs A/B reference; "Landscape Preset" isn't original |
| Preset button naming | "Portrait Preset" / "Landscape Preset" / "Original" | Clear hierarchy: two presets + one true restore |
| 3D Scene column | Move to column 3 above 2D Axes | Rendering-type controls together |
| Navigation column | Move to column 1 after Legend | Layout decisions together |
| Config migration | Auto-detect and convert old keys on load | Backward compatible; no manual editing needed |

---

*"What was a hard Python environment becomes a modern easy shareable
moment."* -- Tony, February 6, 2026

*"Exciting prospects!"* -- Tony, on the road ahead

*"We'll get there. We always do."* -- Tony, February 7, 2026

*"One gallery, two modes, one interaction pattern."* -- Design Session 4,
February 8, 2026

*"If scroll wheel works, just fake a scroll wheel."* -- The synthetic
WheelEvent solution, February 10, 2026

*"One config to rule them all."* -- On gallery_config.json unifying
categories across converter, editor, and viewer, February 12, 2026

*"The bottom axis is almost self-explanatory."* -- On stripping axis
titles for mobile, February 14, 2026

*"Compare the before and after! What we did with the index vs the
studio."* -- Tony, on the Planetary Boundaries transformation,
February 15, 2026

*"We should always override index when studio has created a setting."*
-- Tony, on the _studio flag design, February 15, 2026

*"Pan and zoom work perfectly."* -- Tony, validating D-pad on iPhone,
February 15, 2026

*"What a session."* -- Tony, after two stacked bugs fell to systematic
console logging, February 16, 2026

*"The discomfort is that the index is creating its own filters that are
not visible to the developer in the studio GUI."* -- Tony, the insight
that triggered the WYSIWYG refactor, February 16, 2026

*"What you see is what you get logic."* -- Tony, on the studio becoming
the single source of truth, February 16, 2026

*"A dual pipeline is confusing."* -- Tony, February 16, 2026

*"We did the hard work up front."* -- Tony, on the audit-first approach
to the WYSIWYG refactor, February 16, 2026

*"Single quotes!"* -- The three-bug hunt that unlocked animation,
February 17, 2026

*"Works great."* -- Tony, on the annotation toggle across all platforms,
February 19, 2026

*"Shouldn't these controls be options in studio?"* -- Tony, catching
the WYSIWYG violation before it shipped, February 20, 2026

*"Works great!"* -- Tony, on polar pan/zoom + label scaling,
February 20, 2026

*"I love the spinning planetary boundaries!"* -- Tony, on the angular
rotation pan control, February 22, 2026

*"Edits work great."* -- Tony, on the axis scale + colorbar fixes,
February 22, 2026

### Session 17 (Feb 26): Portrait WYSIWYG -- Frame Containment + Encyclopedia Fix

Resolved the core WYSIWYG discrepancy: studio portrait preview showed
the old 60/40 social HTML layout while the gallery rendered full-screen
Plotly with floating card. Unified the pipeline so both preview and
export always use `build_gallery_html()`. Then contained all UI
overlays inside the aspect ratio frame and fixed encyclopedia button
behavior.

**Unified Pipeline**

Portrait is now a preset (configuration), not a separate pipeline.
Both Preview and Export always call `build_gallery_html()` regardless
of landscape/portrait. Removed the output_format branching from
`_preview()` and `_export()`. Export filename is always `_gallery.html`.
`build_social_html()` remains in the codebase but studio no longer
calls it -- social views are created through the main GUI's existing
export path.

**Aspect Ratio Preview Framing**

Output format controls preview aspect ratio on desktop:
- Landscape (16:9): width 100vw, height capped at 9/16 ratio
- Portrait (9:16): width capped at 9/16 of height, 100vh tall
- Thin white border (1px, 40% opacity) shows viewport boundary
- Gallery index.html unaffected (device provides the aspect ratio)

**Frame Containment**

All UI overlays now live inside `#aspect-frame` with `position:
absolute` instead of `position: fixed`:
- Navigation controls (pan/zoom arrows)
- Encyclopedia "i" button and overlay
- Annotation toggle button
- Info card (portrait mode)
- Modebar (Plotly native, already inside plotly-graph div)

This means everything stays inside the 9:16 frame boundary in
portrait preview. On a real phone the frame IS the viewport, so
behavior is identical.

**Encyclopedia Button Fix**

The "i" button had inconsistent show/hide behavior -- sometimes
sticking, sometimes disappearing immediately on cursor move. Root
cause: no unhover handler, no click-lock mechanism.

New behavior:
- Hover: button appears if object has encyclopedia entry, hides on
  unhover
- Click: button "locks" visible (persists when cursor moves away)
- Click object without entry: unlocks and hides
- No entry: button never appears

Three functions: `encShowButton()` (hover, respects lock),
`encLock()` (click, sets sticky state), `encHide()` (unhover,
respects lock).

**Branding Field Removed**

Since gallery viewer provides its own "Paloma's Orrery" chrome,
per-plot branding is redundant. Removed `info_panel_branding` from:
defaults (landscape, portrait, profile), GUI entry row, config
collector, config applier. Only reference remaining is inside
`build_social_html()` which the main GUI may still use.

**Portrait Preset Revised**

Updated PORTRAIT_CONFIG to preserve plot content rather than strip
it down. The 9:16 frame and info card handle mobile adaptation:

| Setting | Old | New |
|---------|-----|-----|
| Margins | 0/0/0/0 | 10/75/10/10 |
| Show axes | False | True |
| Show grid | False | True |
| Marker size boost | +4 | 0 |
| Line width min | 4 | 0 |
| Show modebar | False | True |
| Show colorbar | False | True |
| Hover mode | none | default |
| Show nav arrows | False | True |
| Marker opacity fix | True | False |
| Legend orientation | horizontal | vertical |
| Legend font scales | 85% | 100% |
| Annotation font scale | 70% | 100% |
| Strip footer | True | False |

Philosophy: let the frame do the work, not aggressive stripping.
Good baseline for standard 3D orrery views. 2D graphics will
require their own preset when the time comes.

**Original Preset Fix**

Original button now works like Landscape/Portrait: reads source
figure values, populates GUI controls, waits for Preview. Previously
bypassed `apply_config()` and launched preview directly.

**Scene Domain Reset**

`apply_config()` now resets `scene.domain` to `{x:[0,1], y:[0,1]}`
when elements affecting domain are stripped (updatemenus, legend,
colorbar). Fixes portrait centering where 3D grid was shifted left
in narrow viewport.

**Future: Custom Presets**

The profile system (`gallery_studio_configs.json`) already saves
per-plot configs as JSON dicts. Named user presets (e.g., "Stellar
HR Diagram", "2D Paleoclimate") could reuse the same mechanism with
a save/load UI. Not needed yet -- dedicated buttons suffice while
the preset count is small.

**gallery_studio.py** (~4,230 lines, up from ~3,900 in Session 16)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Portrait pipeline | Always build_gallery_html(), never build_social_html() | WYSIWYG -- preview must match gallery rendering |
| UI overlay positioning | position: absolute inside #aspect-frame | Frame is the world; everything stays inside it |
| Encyclopedia on hover | Show on hover, lock on click, hide on unhover (unless locked) | Consistent: hover = peek, click = commit |
| Per-plot branding | Removed from studio | Gallery viewer provides chrome; redundant in individual plots |
| Portrait preset philosophy | Preserve content, let frame adapt | Less aggressive; axes/grid/modebar visible; frame does the work |
| Custom presets | Defer until needed | Two presets + Original sufficient for now |

---

*"Can we put the pan/zoom buttons inside the frame too?"* -- Tony,
the question that triggered frame containment review, February 26

*"If the gallery viewer has the branding, branding in the plot is
redundant."* -- Tony, on removing dead UI, February 26

*"Good for this standard orrery view. 2D graphics will require
special changes."* -- Tony, on the revised portrait preset,
February 26

### Session 18 (Feb 26): Featured Labels + Gallery Badges + Git Attribution

Two-level "featured" system: trace-level labels guide users within
a plot, gallery-level badges guide users to a plot. Plus mobile
modebar fix and git co-author research.

**Featured Trace Labels (gallery_studio.py)**

New gold star checkbox per trace in the Trace Visibility list.
Checking it marks that trace as "featured." On export,
`apply_config()` injects a Plotly annotation anchored to trace data
-- gold Georgia serif text on transparent background, with
`_featured: true` marker.

3D traces: annotation on `scene.annotations` (rotates with scene).
Anchor: closest point to origin (avoids hyperbolic trajectories
placing labels millions of AU away).
2D traces: annotation on `layout.annotations` (axis-anchored).
Anchor: closest point to data centroid.

Config: `featured_traces: []` (list of trace names). Stored in
config alongside `trace_visibility`. Cleared by presets. Refreshed
by `_apply_config_to_gui`.

**Gallery Featured Badges (gallery_editor.py + index.html)**

"Toggle Featured" button in gallery_editor.py toolbar. Sets
`featured: true` on visualization metadata. Tree view shows star
character next to featured titles.

index.html renders a gold "Featured" pill badge on gallery cards
with subtle pulse animation (2.5s ease-in-out cycle on opacity and
border). Uses existing `--accent` color scheme (#c9a84c gold,
`--accent-glow` background, `--accent-dim` border).

Use case: new comet arrives, mark it featured. Month later when it's
old news, uncheck it. Guides users to timely or noteworthy content.

**Mobile Modebar Fix (index.html)**

Gallery viewer was overriding `displayModeBar: false` on all mobile
devices, ignoring studio's explicit choice. Now respects `_studio`
flag: curated plots keep modebar on mobile, non-studio plots still
get the touch-optimized hidden modebar.

**Git Co-Author Attribution (Mode 7 -- Gemini)**

Researched proper git co-author tagging for AI collaborators.
`noreply@anthropic.com` resolves to a random GitHub user
("Panchajanya1999") -- known issue, no official Anthropic account.

Gemini recommended using the commit description field with a blank
line separator: `Co-authored-by: Claude <support@anthropic.com>`.
Same pattern works for Gemini (`gemini@google.com`) and ChatGPT
(`support@openai.com`). GitHub Desktop's co-author search field
only finds real users; the description trailer approach is more
reliable for AI attribution.

### Session 19 (Feb 27): Featured Label Refinements + Lossless Re-Export

Iterative refinement of featured labels through debugging with real
data (Wierzchos comet 125-trace plot, Earth 3-planet plot). Plus
lossless round-trip for studio re-export workflow.

**3D/2D Split for Featured Click Behavior**

Critical discovery: Plotly 3D scene annotations don't support
`plotly_clickannotation`. Setting `captureevents: true` on 3D
annotations causes them to eat click events without providing a
handler -- worse than no interaction at all. Competing
`plotly_click` handlers (featured removal vs info card) cause
hangs from `Plotly.relayout` triggering full 3D re-renders on
heavy plots.

Solution: clean separation by dimension.
- 3D: Featured labels are persistent wayfinding. No click handler.
  Info card `plotly_click` runs uncontested. Remove labels only
  by re-exporting from studio.
- 2D: Featured labels removable via `plotly_clickannotation` (click
  directly on gold text). Separate event from `plotly_click`, so
  info cards work independently.

**Smart Anchor Placement**

Original midpoint anchor placed Wierzchos Keplerian Orbit label at
(-1.3M, 1.3M, 3.3M) AU -- millions of AU off screen on the
hyperbolic trajectory. Fixed with dimension-appropriate strategies:
- 3D: closest point to origin (inner solar system = visible area)
- 2D: closest point to data centroid (center of visual mass)
- Single-point traces: use the point directly

**Transparent Label Background**

Changed from `rgba(15, 23, 42, 0.7)` (dark overlay) to
`rgba(0,0,0,0)` (fully transparent). Gold text floats directly on
the plot background.

**Lossless Studio Re-Export (_studio_config)**

Original preset was hardcoding `output_format: "landscape"` and
other defaults when loading a portrait-exported file. Root cause:
studio-level config (output format, route hover, encyclopedia,
nav arrows) isn't stored in Plotly layout values.

Fix: `apply_config()` now embeds `_studio_config` dict in the
layout alongside `_studio: true`. Contains full config minus
large/transient fields (trace_visibility, plotly_js_source,
output_mode).

`_apply_original_preset()` checks for `_studio_config` first
(new exports: perfect round-trip). Falls back to heuristic
detection for older exports (customdata -> route_hover,
_encyclopedia, _studio_nav, slider bgcolor, _featured annotations).

**Performance Insight: Strip Hidden Traces**

With 125 traces in Wierzchos plot, the exported HTML is heavy even
when most traces are hidden via visibility toggle. The existing
"Strip hidden" checkbox in studio physically removes hidden traces
from the export, dramatically reducing file size and viewer
rendering load. This is the recommended workflow for complex plots:
hide unnecessary traces, check "Strip hidden," then export.

**Files Modified:**
- `gallery_studio.py` (~4,480 lines): _studio_config embedding,
  smart anchor placement, 3D/2D click split, transparent bg,
  heuristic Original preset detection, debug logging (added/removed)
- `index.html` (~2,160 lines): simplified featured handler
  (2D clickannotation only, no plotly_click for featured)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Featured click: 3D | Display-only, no handler | plotly_clickannotation unsupported; competing handlers cause hangs |
| Featured click: 2D | plotly_clickannotation | Separate event, doesn't compete with info card |
| 3D label anchor | Closest to origin | Hyperbolic orbits place midpoints millions of AU away |
| 2D label anchor | Closest to data centroid | Center of visual mass, visible in default view |
| Label background | Fully transparent | Gold text floats cleanly on any background |
| Re-export config | _studio_config in layout | Lossless round-trip; heuristic fallback for old exports |
| Heavy plots | Strip hidden traces | Physical removal beats visibility toggle for performance |

---

*"Handoff this idea to a junior programmer: get back the product
a day later. Handoff to Claude Opus 4.6: one minute later, done
perfectly. Crazy."* -- Tony, February 27

*"Where are junior programmers going to cut their teeth if everyone
is using Code?"* -- Tony, on the workforce implications of AI
coding tools, February 27

*"3D scene annotations are display-only constructs. Don't try to
make them interactive."* -- The Plotly 3D annotation lesson, Feb 27

*Data Preservation is Climate Action. Sharing is Astronomy Action.*

### Session 20 (Feb 28): KMZ Integration Fixes (Mode 7 -- Gemini + Claude)

Gemini drafted initial fixes for three KMZ integration issues. Tony
brought them to Claude for implementation and validation. Session
expanded to fix six issues total, several discovered during testing.

**Fix 1: _kmz_handoff Underscore Stripping (gallery_studio.py)**

`gallery_studio.py` strips all underscore-prefixed keys from Plotly
JSON at three locations (lines 1628, 2386, 3954) to avoid polluting
the Plotly figure with internal markers. This killed `_kmz_handoff`
before it reached the exported HTML.

Gemini recommended dropping the underscore (renaming to
`kmz_handoff`). Claude diverged: kept `_kmz_handoff` and whitelisted
it through all three filters, following the existing `_encyclopedia`
pattern. This preserves the convention that underscore marks
non-Plotly keys and avoids Plotly.js console warnings about unknown
layout attributes.

**Fix 2: Featured Trace Label Regression (index.html)**

Gemini's prior session had removed the `plotly_click` handler that
powered featured label click-to-dismiss. Restored the original
handler. 3D featured labels are now clickable again.

**Fix 3: Mobile Intent URL (index.html)**

Adopted Gemini's `googleearth://url=` intent scheme. Desktop gets a
standard download link. Mobile devices (detected via user agent)
get `googleearth://url=<absoluteURL>` which prompts the OS to open
Google Earth directly. Absolute URL constructed via
`new URL(relativePath, window.location.href).href`. Needs
real-device testing -- if Google Earth isn't installed, the OS
should show an error or app store prompt.

**Fix 4: KMZ 404 Error (index.html + _gitattributes)**

Browser requesting `palomasorrery.com/assets/<file>.kmz` returned
404. File actually located at
`palomasorrery.com/gallery/assets/<file>.kmz`. Root cause:
`index.html` served from root, JS built relative path as `assets/`
which resolved to `/assets/` instead of `/gallery/assets/`.

Fix: changed JS path from `'assets/'` to `'gallery/assets/'`.

Secondary concern: `.gitattributes` had `* text=auto` which could
corrupt binary KMZ files. Added explicit binary markers:
```
*.kmz binary
*.kml binary
*.png binary
```

**Fix 5: Button Positioning (index.html)**

Share and 3D Earth buttons positioned at `right: 12px` obscured
Plotly colorbar/legend on mapbox plots. Moved both to `left: 62px`
(just right of hamburger menu). Updated CSS and inline styles.
Mobile responsive override updated from `right: auto` to
`left: auto`.

**Fix 6: Mapbox Zoom Controls (index.html)**

Zoom controls appeared but didn't work on mapbox plots. `zoom2D()`
operates on xaxis/yaxis ranges; mapbox uses `mapbox.zoom` instead.
Added mapbox detection to scene type logic. When
`figDict.layout.mapbox` is detected, zoom controls hidden entirely
(mapbox has built-in scroll/pinch zoom).

**Fix 7: Missing Briefing Context on Teaser (earth_system_generator.py)**

Web teaser lacked the briefing information present in the KMZ intel
card. Added `briefing` and `description` parameters to
`generate_plotly_teaser()`. Renders first paragraph of briefing as
bottom-left annotation (200 char max, semi-transparent background,
white text) plus hint: "Click 3D Earth for full visualization in
Google Earth."

**Fix 8: Raw File Deletion (earth_system_generator.py)**

`package_and_cleanup()` deleted KML/PNG files after zipping to KMZ.
Desktop Python orrery needs raw files in `data/`. Removed
`os.remove()` loop. KMZ and raw files now coexist.

**Fix 9: KMZ Multi-Layer Loading (earth_system_generator.py)**

KMZ contained three separate KML files (spikes, heatmap, impact).
Google Earth only reads the first KML in an archive. Attempted
NetworkLink wrapper -- failed (Google Earth doesn't resolve
relative NetworkLinks inside KMZ).

Final fix: merged approach. `package_and_cleanup()` now reads all
KML files, extracts `<Document>` body using regex, wraps each in a
`<Folder>` with layer name, generates a single `doc.kml` containing
all folders. Writes only `doc.kml` + PNG assets to KMZ.

Result: single-document KMZ with toggleable folders in Google
Earth's layer panel.

**Files Modified:**
- `gallery_studio.py` (~4,500 lines): whitelisted `_kmz_handoff`
  through three underscore filters
- `index.html` (~2,200 lines): button positioning, mapbox zoom
  detection, KMZ path fix, mobile intent URL, featured label restore
- `earth_system_generator.py` (~850 lines): briefing annotation,
  no-delete policy, merged KML approach, `import re`
- `_gitattributes`: binary markers for KMZ/KML/PNG

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Underscore convention | Keep `_kmz_handoff`, whitelist | Consistent with `_encyclopedia`; avoids Plotly.js warnings |
| Gemini vs Claude approach | Claude diverged on underscore | Whitelist preserves convention; rename would break it |
| Delete raw files? | No | Desktop orrery needs them in data/ |
| Multi-KML in KMZ | Merge into single doc.kml | Google Earth only loads first KML; NetworkLinks don't resolve |
| Button position | Left side (left: 62px) | Right side obscures legend/colorbar |
| Mapbox zoom | Hide controls entirely | Mapbox has native pinch/scroll zoom; custom controls don't work |
| Mobile KMZ | googleearth:// intent URL | Direct app launch vs download-to-Files |
| KMZ asset path | gallery/assets/ not assets/ | index.html served from root, not gallery/ |

---

*"I am more comfortable working with you."* -- Tony, on bringing
Gemini's fixes to Claude for implementation, February 28

*"Fixing bug one reveals bug two."* -- The stacked bugs lesson
continues: fixing the underscore stripping revealed the path bug,
which revealed the button positioning bug, February 28

### Session 21 (Mar 2): Earth-Like Basemap & Studio UX (Claude Opus 4.6)

Tony identified a visual inconsistency: the dark `carto-darkmatter`
basemap (space aesthetic) was wrong for Earth System teasers. "The
dark theme is not a general choice -- it's consistent with the orrery
or stellar views, but the earth-based files should have an earth-like
theme, more blue and green not black (space)."

**Basemap Investigation**

Built an interactive comparison tool testing all available Plotly
mapbox styles. Discovery: the Stamen tile styles (terrain, watercolor,
toner) are dead -- Stamen Maps moved to Stadia Maps in July 2023
and now require an API key. Only three built-in no-token styles
work: `carto-darkmatter`, `open-street-map`, `carto-positron`.

Solution: `white-bg` style with custom ESRI raster tile layer
overlay. Tested five ESRI tile services. Selected **ESRI World Topo
Map** -- green land, blue ocean, topographic shading, geographic
labels. Free, no API key, well-maintained.

**Basemap Change (earth_system_generator.py)**

Six targeted changes to `generate_plotly_teaser()`:

| Setting | Was | Now | Why |
|---------|-----|-----|-----|
| mapbox style | `carto-darkmatter` | `white-bg` + ESRI layer | Earth looks like Earth |
| colorscale | `Inferno` | `YlOrRd` | Inferno's dark purples vanish on light maps |
| marker opacity | 0.6 | 0.75 | Visibility on detailed basemap |
| annotation font | `#e2e8f0` (light) | `#1a1a2e` (dark) | Readability on light map |
| annotation bg | `rgba(0,0,0,0.7)` | `rgba(255,255,255,0.85)` | Light-on-light context |
| body background | `#000` | `#f5f5f0` | HTML body matches light map |

ESRI tile URL:
`https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}`

**Gallery Studio UX Improvements (gallery_studio.py)**

Three improvements to the studio workflow:

1. **Moved "3D Handoff (Google Earth)" to column 3** -- was buried
   in column 1 below Legend. Now the first section in the right
   column, immediately visible when loading Earth System teasers.

2. **Auto-detect KMZ filename from teaser filename** -- when loading
   `*_teaser*.html`, the 3D Handoff field auto-populates with
   `*_blockbuster.kmz`. Uses `basename.split('_teaser')[0]` to
   derive the KMZ name. Guards: only fires when field is empty,
   runs AFTER saved config restore (so saved values aren't
   overwritten). This was the root cause of the missing Google
   Earth button -- the field was empty because no one filled it in.

   Ordering bug caught during testing: auto-detect initially ran
   BEFORE saved config restore. A previously saved empty `kmz_link`
   would overwrite the auto-detected value. Fix: moved auto-detect
   to run AFTER `_apply_config_to_gui()`.

3. **Remember last Load HTML directory** -- saves `_last_load_dir`
   in `gallery_studio_configs.json` after each successful load.
   Next "Load HTML..." dialog opens to that directory instead of
   falling back to `images/` or `~/Documents`. Stored as a
   top-level key in the config store (alongside per-file configs).

**Files Modified:**
- `earth_system_generator.py` (~925 lines): basemap, colorscale,
  opacity, annotation colors, body background
- `gallery_studio.py` (~4,515 lines): KMZ field moved to column 3,
  auto-detect KMZ filename, last-used directory persistence

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Basemap for Earth views | ESRI World Topo via white-bg | Green/blue Earth colors, free, no API key |
| Stamen tiles | Dead (require Stadia API key) | Moved to paid service July 2023 |
| Colorscale on light map | YlOrRd | Inferno dark purples invisible on light backgrounds |
| KMZ field placement | Column 3 (top) | Visibility -- was buried in column 1 |
| KMZ auto-detect | Split on `_teaser`, append `_blockbuster.kmz` | Eliminates manual filename entry |
| Auto-detect ordering | After saved config restore | Prevents saved empty value from overwriting |
| Last directory | `_last_load_dir` in config store | Opens dialog where user left off |

---

**Technical Lessons Learned:**

- Stamen tile styles in Plotly (`stamen-terrain`, `stamen-toner`,
  `stamen-watercolor`) are defunct. They silently fail to render
  (blank map, no error). Use `white-bg` with custom raster layers.

- ESRI ArcGIS tile servers are free for direct use without API keys:
  World_Topo_Map, World_Imagery, NatGeo_World_Map, World_Physical_Map.
  Added via Plotly `mapbox.layers` with `sourcetype: 'raster'`.

- Config restore ordering matters: auto-populated defaults must run
  AFTER saved config is applied, not before. Otherwise saved empty
  values overwrite the auto-detected values.

- "Space views get dark, Earth views get Earth" -- visual theme
  should match content domain, not be applied uniformly.

---

*"Data Preservation is Climate Action. Sharing is Astronomy Action."*

### Session 22: March 3, 2026 - iOS KMZ Handoff Workaround
* **Issue Identified:** Downloading `.kmz` files on iOS resulted in severe friction. Apple's strict file sandboxing and the deprecation of custom URL schemes caused fatal black screens (especially in Home Screen PWAs) or trapped users in hidden download managers without clear paths to open the file in Google Earth.
* **Button HTML Update:** Added the `download` attribute to the `kmz-handoff-btn` anchor tag to ensure desktop browsers and standard mobile environments handle the file as a download rather than attempting a page navigation.
* **JavaScript Interception & Browser Sniffing:** Abandoned the Web Share API (which stripped third-party app associations for `.kmz` files) in favor of a targeted alert system. Used `navigator.userAgent` to detect specific iOS browsers (Safari, Chrome, Edge, Bing, Firefox).
* **Expectation Management (The iOS Tour Guide):** Fired tailored, step-by-step `alert()` instructions *before* triggering `window.open(href, '_blank')`. This gives users a specific roadmap for navigating their browser's unique download UI to find the "Open In..." or "Share" sheet.
* **PWA Black Screen Fix:** Implemented `window.navigator.standalone` detection to completely block downloads within iOS Home Screen apps. Replaced the action with an alert instructing the user to open the gallery in the native Safari app, effectively preventing the dead-end black screen trap.

### Session 23 (Mar 4): Annotation Word-Wrap Fix (Claude Sonnet 4.6)

**Problem:** Briefing annotation text on the Delhi heat wave teaser was
truncating on both desktop and mobile. Two separate root causes, fixed
in sequence.

**Root Cause 1 -- Upstream truncation (earth_system_generator.py)**

`generate_plotly_teaser()` had a hard 200-character cap on the briefing
text: `brief_text[:197] + "..."`. The Delhi first paragraph is 208
characters, so it was cut mid-word to `populati...`. This was baked
into the exported JSON at generation time.

Fix: removed the `[:197]` truncation entirely. The first-paragraph
split (`briefing.split('\n\n')[0]`) is already a natural stopping point.
No character limit needed -- word-wrap handles length at display time.

**Root Cause 2 -- Plotly SVG text does not reflow (index.html)**

The initial fix attempted to inject a pixel `width` into each annotation
via a `_sizeAnnotations()` helper. This was wrong: Plotly annotation
`width` constrains the box border but **SVG `<text>` elements do not
reflow around it**. Annotations are not HTML divs. The box gets smaller
but the text just clips.

Fix: replaced `_sizeAnnotations` with `_wrapAnnotations`, which inserts
explicit `<br>` tags at word boundaries at render time. Splits on
existing `<br>` tags first (preserving intentional line breaks and the
italic hint line), then wraps each plain-text segment independently.

```
Desktop: ~55 chars/line  (sized for annotation occupying ~35% viewport)
Mobile:  ~38 chars/line  (sized for narrow screens)
```

The `<i>Click 3D Earth...</i>` hint segment matches the
`/^<tag>...</tag>$/` regex and passes through unwrapped.

**Files Modified:**
- `earth_system_generator.py`: removed `[:197] + "..."` truncation
  from `generate_plotly_teaser()`
- `index.html`: replaced `_sizeAnnotations()` with `_wrapAnnotations()`
  at definition and both call sites (initial render + toggle-on)

**Deployment note:** The two Delhi JSON files also needed the full text
patched in directly (the truncated string was already baked in from the
previous export). Re-exporting through the updated generator produces
correct output for all future teasers.

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Truncation cap | Remove entirely | First paragraph is natural stop; word-wrap handles length |
| Plotly annotation width | Not usable for text reflow | SVG text doesn't reflow; width only constrains box border |
| Word-wrap method | Explicit `<br>` injection at render time | Only reliable method for Plotly annotation text wrapping |
| Existing `<br>` tags | Split on them, wrap each segment | Preserves intentional breaks; protects italic hint line |
| Chars per line | 55 desktop / 38 mobile | ~6.5px per char at font-size 11; tuned to annotation width |

---

**Technical Lessons Learned:**

- Plotly annotation `width` constrains the box border but SVG `<text>`
  elements do not reflow. To wrap text in a Plotly annotation, you must
  use explicit `<br>` tags. There is no layout engine.

- Upstream truncation baked into JSON is invisible until you look at
  the raw data. When text looks cut off, check the source JSON first
  before debugging the renderer.

- Two-bug stacks again: fixing the generator truncation revealed that
  the renderer still wouldn't wrap (wrong approach). Both had to be
  fixed independently.
### Session 24 (Mar 5, 2026): Featured Annotation Fixes + Studio Workflow Redesign

Two threads in this session: completing the featured trace label bug fixes
(duplicate labels, stale annotation persistence, white box rendering), and
a broader studio workflow redesign that eliminates `gallery_studio_configs.json`
dependency in favor of reading config directly from the figure.

**Featured Annotation Bug Fixes (gallery_studio.py)**

Three bugs fixed in sequence, each revealing the next.

*Bug 1: Duplicate Labels*

Featured trace for Moon Keplerian Apogee with custom label "Apogee"
produced two superimposed labels: one white with grey arrow (Plotly's
default 3D annotation box), one gold. Root cause: Plotly's 3D annotation
default box (white background + grey border) renders even when
`bgcolor: rgba(0,0,0,0)` is set. Must also set `bordercolor: rgba(0,0,0,0)`
and `borderwidth: 0` to suppress the box entirely.

Fix: Added explicit `bordercolor: 'rgba(0,0,0,0)'` and `borderwidth: 0`
to both 3D and 2D featured annotations. 3D uses `showarrow: False`
(Plotly 3D ignores arrows anyway). 2D retains gold arrow.

*Bug 2: Annotation_bg_transparent Stripping Featured Annotations*

The `annotation_bg_transparent` pass was stripping `bgcolor` from
`_featured` annotations along with regular annotations, defeating the
transparent background fix.

Fix: Added `_featured` check to the annotation strip pass -- skip any
annotation with `_featured: true` marker.

*Bug 3: Stale Annotations Persist Across Load/Reload*

Loading a gallery export that had `_featured` annotations baked in, then
unchecking all featured traces, then pressing Original -- labels persisted.
Root cause: the stale annotation strip was inside `if featured:`, so it
never ran when `featured_traces = []`.

Fix: Moved the stale `_featured` annotation strip **unconditionally** to
before the `if featured:` guard. Strips from both `scene.annotations` and
`layout.annotations` on every `apply_config()` call, regardless of whether
new featured annotations will be added.

Rule derived: guards like `if list:` that control cleanup let stale
embedded data persist when the list is emptied. Strip unconditionally
before the guard.

**Studio Workflow Redesign: Source vs Gallery Export Distinction**

The original studio loaded configs from `gallery_studio_configs.json` --
a separate file keyed by filename. This created hidden state: the config
store was a second source of truth that could drift from the actual figure.

New architecture:
- `_read_config_from_figure(fig)`: reads 16 layout values directly from
  the figure (margins, bg color, title font, legend settings, etc.)
- Source HTML load: calls `_read_config_from_figure` to populate GUI
  from the raw figure's values
- Gallery export load (file with `_studio_config` in layout): reads that
  embedded config dict back into the GUI for perfect round-trip
- `gallery_studio_configs.json` still saved for backward compat but is
  no longer the authoritative source

The key conceptual distinction: **source file = raw figure data; gallery
export = curated artifact with `_studio_config` overlay**. These are
different "originals" requiring different restore strategies.

`_apply_original_preset()` respects this: checks for `_studio_config`
first (gallery exports), falls back to heuristic detection for older
exports, reads native figure values for true source files.

Also fixed: `layout_json` NameError in both `build_gallery_html()` and
`build_social_html()` -- variable referenced before assignment in error
handling paths.

**Two New Standing Conventions (orrery-wide)**

*3D Axis dtick + range:*
Close-approach and flyby plots require both `dtick` (tick spacing) and
`range` (axis extent) overridden on all three scene axes. The default
AU-scale axes make Apophis/GEO geometry completely invisible -- everything
interesting is happening at ~0.001 AU while the grid shows at ~1 AU scale.
Both properties should be set at generation time in the orrery GUI, with
Studio providing a refinement layer for per-export adjustment.

*Hover text AU convention:*
All distance hover text must include AU alongside km. GEO altitude is the
immediate example -- currently shows km and Earth radii but not AU.
The AU figure enables cross-plot comparison: GEO ~0.000285 AU, Moon
~0.00257 AU, Apophis perigee ~0.000245 AU. Conversion: `km / 149597870.7`.
Standing convention for all new hover text in orrery modules.

**Files Modified:**
- `gallery_studio.py` (~4,520 lines): featured annotation white-box
  suppression, `_featured` protection in annotation_bg_transparent,
  unconditional stale annotation strip, `_read_config_from_figure`,
  workflow redesign, `layout_json` NameError fix

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Plotly 3D annotation box | Set bordercolor + borderwidth: 0 explicitly | bgcolor alone insufficient; default box always renders |
| annotation_bg_transparent + featured | Skip _featured annotations | Featured bg is intentionally transparent; strip pass must not undo it |
| Stale strip guard | Strip unconditionally before `if featured:` | List can be emptied; strip must run regardless |
| Studio config source | Read from figure (_read_config_from_figure) | Figure is the truth; config store was a second source that could drift |
| Source vs gallery export | Different restore strategies | Source = raw values; gallery export = _studio_config overlay |
| 3D axis scale | dtick + range both needed | Tick spacing without range correction leaves axes at wrong scale |
| Hover text AU | Required alongside km for all distances | Enables cross-plot comparison; GEO/Moon/Apophis comparison only works with AU |

---

*"The source file and the gallery file are different originals. Treat them that way."*
-- Studio workflow redesign insight, March 5, 2026

*"All hovertext should include figures in AU, not just km, so we can compare distances on that basis."*
-- Tony, March 5, 2026

*"Especially in these fraught times."*
-- Tony, on the partnership and what's at stake, March 5, 2026

### Session 25 (Mar 6, 2026): 3D Axis Control + Hover/Routing Matrix Fix

Two threads: implementing the 3D axis control feature (Studio side), and
discovering and fixing a cascade of hover/routing bugs exposed during testing.

**3D Axis Control -- Studio Side (gallery_studio.py)**

Added manual axis range and dtick override fields to Studio for close-approach
and flyby plot curation. This is Part 1 of the 3D Axis Control handoff;
Part 2 (orrery GUI auto-range at generation time) remains for next session.

Changes:
- 4th column (`col_3d`) added to Studio layout. 3D Scene section moved
  from crowded column 2 (portrait) to dedicated column 3. Gives room for
  the new fields and future 3D controls.
- `scene_axis_range` and `scene_dtick` config keys added to DEFAULT_CONFIG,
  PORTRAIT_CONFIG, GUI widgets (6-decimal entry fields with reference-value
  tooltips), `_collect_config()`, `apply_config()`, `_apply_config_to_gui()`.
- `apply_config()` range/dtick override: when range > 0, sets symmetric
  +/- range on all three scene axes. Auto-calculates dtick from range
  (~6 gridlines) if dtick is 0. Appends km-equivalent suffix to axis
  titles at small scales (< 0.01 AU shows km, < 0.1 AU shows millions of km,
  >= 0.1 AU shows AU only).
- Fallback `_calculate_grid_dtick` inline if visualization_utils import fails.

Tested at range=2 AU / dtick=0.25 AU (solar system scale) -- clean grid,
correct axis titles. Km suffix verified to trigger only at close-approach
scales per the threshold logic.

**Show Axes Bug Fix (pre-existing)**

The `show_axes` toggle only had a code path to *hide* axes (set
`visible: False`, clear title, etc.). No code path to *restore* them.
When a source file had axes previously hidden (e.g., from a prior Studio
export), checking Show axes did nothing.

Fix: Added `else` branch that sets `visible: True`, `showticklabels: True`,
and restores grid/background based on the Show grid setting.

**Hover/Routing Matrix -- Complete Rewrite**

Testing the axis control exposed inconsistent hover behavior across the
6 combinations of hover mode (default/names_only/none) x routing (on/off).
Root causes traced through 5 iterations:

*Round 1: Routing destroyed tooltip text unconditionally*
The routing block blanked `trace['text']` regardless of hover_mode.
Initial fix: preserve text when hover_mode is "default".

*Round 2: Wrong routed-trace detection*
Code used `if trace.get('customdata')` to detect routed traces. But the
orrery source already puts customdata on traces for its own purposes.
Every trace looked "routed" even when routing was OFF.
Fix: Use `config.get('route_hover_to_panel', False)` instead.

*Round 3: Clearing hovertemplate exposed Plotly defaults*
Source orrery sets `hovertemplate='%{text}<extra></extra>'` to show only
the text field. Setting `hovertemplate = None` fell back to Plotly's
default 3D hover (trace name + x + y + z). Fix: Keep the text-only
template; only set `hoverinfo='none'` when truly suppressing all hover.

*Round 4: `_hover_mode` stripped from layout JSON*
The `layout_for_json` filter removes all underscore-prefixed keys. The
`_hover_mode` flag wasn't in the preserve list, so JS always defaulted
to 'default'. Fix: Added to preserve list in both landscape and portrait
builders.

*Round 5: Corrected semantic model*
Final insight from Tony: routing ON means the card REPLACES the tooltip,
not supplements it. The card content respects hover_mode.

Final behavior matrix (all 6 cases verified):

| | Route OFF | Route ON |
|---|---|---|
| **Default hover** | Full tooltip, no card | No tooltip, full card |
| **Names only** | Name tooltip, no card | No tooltip, name card |
| **No hover** | Nothing | Nothing |

Implementation:
- Routing block always suppresses tooltip (blank text + invisible
  hovertemplate). Always populates customdata with full parsed hover
  data. Stores `_hover_mode` in layout for JS.
- Hover mode block handles tooltip independently: "none" suppresses
  hover entirely (routed: blank text + template; non-routed: hoverinfo=none).
  "Names only" replaces text with trace name, keeps text-only template.
  "Default" leaves everything as-is.
- JS card handler reads `_hover_mode` from layout: "default" shows full
  card, "names_only" shows name only, "none" returns early (no card).
- Card HTML/JS only injected when both portrait format AND
  route_hover_to_panel are enabled.
- Hoverlabel made transparent when routing is on (suppresses the arrow
  pointer that rendered even with empty text).
- Tap hint suppressed when hover_mode is "none".

**Files Modified:**
- `gallery_studio.py` (~4,700 lines): 4th column layout, axis control
  fields + apply logic, show_axes restore, hover/routing matrix rewrite,
  `_hover_mode` layout flag, card JS hover_mode awareness, hoverlabel
  transparency, card injection gating

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Studio column layout | 4 columns (added col_3d) | Right column was crowded; 3D controls get dedicated space |
| Axis field precision | 6 decimal places | Covers GEO scale (0.0000426 AU) through solar system (1+ AU) |
| Km suffix threshold | < 0.01 AU shows km, < 0.1 shows M km | Solar system scale doesn't need km; close-approach scale does |
| Dynamic grid on zoom | Not feasible in Plotly 3D | 3D dtick is fixed; Fly-To buttons handle per-target rescaling |
| Routing + tooltip | Card replaces tooltip, not supplements | Tony's rule: routing moves hover to card, tooltip suppressed |
| `_hover_mode` in layout | Preserved through JSON filter | JS needs it to filter card content; was being stripped |
| Card without routing | Don't inject card HTML/JS | Card is the routing destination; no routing = no card |
| Routed-trace detection | Use config flag, not customdata | Orrery source has customdata for its own purposes |
| hovertemplate clearing | Keep text-only template | Clearing falls back to Plotly default (name + xyz) |

---

**Technical Lessons Learned:**

- Plotly 3D `hovertemplate` takes priority over `hoverinfo`. Clearing
  hovertemplate to None doesn't suppress hover -- it falls back to
  Plotly's default display (trace name + x + y + z coordinates).

- The orrery source already puts customdata on traces (for encyclopedia
  lookups, etc.). Using customdata presence to detect "routed" traces is
  wrong -- use the config flag that controls routing instead.

- The `layout_for_json` filter strips all underscore-prefixed keys, then
  selectively preserves specific ones. New underscore keys need to be
  added to the preserve list in BOTH builders (landscape and portrait).

- Plotly's hoverlabel renders a tiny arrow pointer even with empty text.
  Making the hoverlabel background, border, and font transparent
  suppresses this visual artifact.

- Testing hover behavior requires a clean orrery source file, not a
  previous Studio export. Studio exports have already been through the
  routing pipeline -- trace.text may be blanked, making route-OFF tests
  meaningless. Source = raw data; export = curated artifact.

---

*"The logic is inconsistent."*
-- Tony, the observation that triggered the hover/routing matrix rewrite

*"The card replaces the tooltip, not supplements it."*
-- Tony, the semantic insight that simplified everything

### Session 26 (Mar 7, 2026): Trace Visibility Round-Trip Verification

Focused testing session to verify the trace visibility persistence fix
from Session 24's workflow redesign. The previous implementation failed
at step 7 of the round-trip test (restored traces reverted to hidden on
reload). This session confirmed the fix works correctly.

**Test Protocol (second run, fresh source file)**

Source: Venus, Earth, and Mars orbits with markers (raw orrery export,
not a prior Studio file). Landscape preset.

| Step | Action | Result |
|------|--------|--------|
| 1 | Load fresh raw source file | Clean load, all traces visible |
| 2 | Uncheck Venus and Earth in Trace Visibility panel | Confirmed hidden in preview |
| 3 | Export | Exported with Venus and Earth removed |
| 4 | Reload that export | Venus and Earth still hidden -- correct |
| 5 | Re-check Venus and Earth (restore to visible) | Restored and verified in preview |
| 6 | Export again | Exported with all traces visible |
| 7 | Reload second export | All traces visible -- **PASS** |

**Minor observation (accepted):** On restore (step 5), Venus and Earth's
Keplerian position and mean orbit sub-traces came back as visible
(checked), even though they are normally hidden by default. Mars's
sub-traces stayed in their default-hidden state because Mars was never
removed/restored. The restore operation sets all sub-traces of a restored
parent to visible rather than restoring them to their default visibility
state. This is cosmetic and easily recoverable by unchecking the
sub-traces -- not worth tracking down.

**Conclusion:** The `_read_config_from_figure` approach (Session 24) and
the unconditional stale annotation strip fix correctly persist trace
visibility through the full export -> reload -> modify -> export ->
reload cycle. The bug that failed this test before Session 24 is
resolved.

**Strip Hidden Traces Test**

Verified that the "Strip hidden" checkbox physically removes hidden
traces from the export (not just sets visibility to false).

| Step | Action | Result |
|------|--------|--------|
| 1 | Load fresh Venus/Earth/Mars source | All traces visible |
| 2 | Hide Venus and Earth | Confirmed hidden in preview |
| 3 | Check "Strip hidden," export | Exported with Venus and Earth stripped |
| 4 | Reload that export | Venus and Earth absent from Trace Visibility panel entirely -- not hidden, gone |
| 5 | Preview | Only Mars plottable -- **PASS** |

This confirms the two complementary workflows: hide traces with
visibility toggle (non-destructive, reversible on reload) vs strip
hidden traces (destructive, reduces file size permanently). Both work
as designed. File size reduction: 915 KB -> 314 KB (66% reduction from
stripping 2-3 traces worth of Venus and Earth orbit data).

**No files modified.** This was a verification-only session.

---

*"That's such a minor detail that is not worth tracking down. It's easily
recoverable."*
-- Tony, on sub-trace default visibility after restore, March 7, 2026

### Session 27 (Mar 8, 2026): Earth System Subcategories + Gallery Architecture Design

Design session that evolved from open-ended exploration ("how would you
approach extending the earth system generator to other planetary
boundaries?") into a concrete architectural plan and first implementation
of subcategory support for the gallery.

**Design Evolution (conversation-first, 4 phases):**

1. *Boundary extension options* -- Three approaches proposed: tipping
   points forensics (extend KML teaser pattern), polar chart as hub
   (each wedge becomes navigable), unified transgression timeline (all
   boundaries on one time axis). Tony unified all three as different
   scales of the same story.

2. *Data fragility prioritization* -- Ranked data sources by institutional
   risk and measurement irreplaceability: NOAA Coral Reef Watch SST
   (vulnerable agency, unique product), NASA GRACE-FO ice mass
   (irreplaceable measurement), MODIS NDVI (aging satellite), NOAA CPC
   drought indices (reconstructable). Build order follows fragility,
   not visual drama. "Data Preservation is Climate Action."

3. *Gallery as communicator* -- Tony's insight: the app is the generator,
   the gallery is the communicator, Instagram is the teaser. Start at
   the gallery end because it constrains upstream design. Explored
   scrollytelling (NYT, Guardian, Pudding) vs open-world (museum)
   models. Tony's bias: "a map more than a channel."

4. *Museum model* -- Research into Met, Smithsonian, museum UX revealed
   the key principle: objects first, interpretation available. Layered
   interpretation (object -> label -> wall text -> catalog). Three
   modes of traversal: Browse (card catalog, open world), Explore
   (connections on objects, follow threads), Read (curated scroll feed,
   guided narrative). Tony chose evolutionary implementation: build the
   rooms first, add wall text later.

**Second-order effects framework:** Tony identified the gap between
physical climate measurement and human consequence -- the chain from
ecological to economic to demographic to political impacts. Attribution
weakens along the chain but the connections matter. Tony's anthropologist
background is the right lens. Honest approach: present physical data
rigorously, document human chain separately with explicit attribution
strength labels (strong / moderate / contested / interpretive). The
interpretive layer is Tony-authored, not auto-generated.

**Media research findings:**
- The Pudding: closest overall match (data-forward, sparse prose,
  personal voice, open-source tools)
- Bloomberg/Climate Impact Lab: closest to content (heat mortality,
  inequality mapping)
- Pew Research: closest to mobile discipline (one idea per viewport)
- Guardian: closest to cross-disciplinary narrative (following threads
  through systems)
- Key difference: none attempt the full causal chain with explicit
  attribution strength. That's genuinely new.

**Implementation: Subcategory Support (3 files)**

Added `subcategory` and `subcategory_label` optional fields to
gallery_metadata.json for Earth System entries. Non-climate categories
are unaffected.

**gallery_editor.py** changes (~380 lines added, 1,452 total):

- "Set Subcategory" toolbar button with dialog: listbox of existing
  subcategories + create-new fields (key + label). Supports removing
  subcategories.
- "Edit Labels" toolbar button: select a category or subcategory node
  in the tree, rename the label across ALL entries sharing that key.
  Category renames also update gallery_config.json.
- Tree display: subcategory-aware grouping within categories that have
  them. Shows Mode -> Category -> Subcategory -> Visualization hierarchy.
  Categories without subcategories render flat as before.
- "Copy To..." dialog: added subcategory selection alongside existing
  category and mode pickers. Fixed `exportselection=False` on both
  listboxes (Tkinter gotcha: clicking one listbox deselected the other).
- Move Up/Down: now respects subcategory boundaries. Vizs stay within
  their subcategory when reordering. New `_move_subcategory` method
  reorders entire subcategory groups within a category. Status bar
  feedback when moves fail ("Already at top of climate_change").
- Selection helpers: recognize `sub_` prefixed tree nodes.
- Move algorithm: extract-reorder-reinsert instead of direct swap.
  Handles non-contiguous entries safely (portrait entries interspersed
  between landscape entries of the same subcategory).

**index.html** changes (~105 lines added, 2,400 total):

- CSS: `.subcategory-header`, `.subcategory-label`, `.subcategory-arrow`,
  `.subcategory-items` with collapsible animation. Arrow rotates 90deg
  when collapsed, items container animates max-height to 0.
- JS `renderVizCard()`: extracted card HTML into reusable function
  (shared by flat and subcategory layouts, eliminates duplication).
- JS `renderNavList()`: checks `hasSubs` per category. If any item has
  a subcategory field, groups into collapsible subcategory sections.
  Falls back to flat list for non-subcategory categories.
- JS click handler: subcategory header click toggles collapsed state.
  Falls through to viz-card handler for non-header clicks.

**assign_subcategories.py**: one-time bootstrap script (or use gallery
editor GUI). Maps 26 existing Earth System entries to subcategories.

**Initial subcategory structure:**

```
Earth System
  +-- Overview (Planetary Boundaries polar chart)
  +-- Climate Change (14 entries)
  |     Keeling Curve, Energy Imbalance, Temperature Anomalies,
  |     Monthly Temperature, Warming Stripes, Sea Level Rise,
  |     Arctic Ice Extent, Paleoclimate Cenozoic 66Ma,
  |     Paleoclimate 540Ma, Paleoclimate Human Origins
  +-- Extreme Heating Events (5 entries)
  |     Paleoclimate Wet-Bulb, NYC 1948, Delhi 2024
  +-- Ocean Acidification (2 entries)
        Ocean pH Trend
```

**Future subcategories (keys reserved, unpopulated):**
biochemical_flows, biosphere_integrity, land_system_change,
freshwater_change, aerosol_loading, ozone_depletion, novel_entities

**Metadata schema addition:**

```json
{
    "id": "keeling_curve_co2_concentration",
    "category": "climate",
    "category_label": "Earth System",
    "subcategory": "climate_change",
    "subcategory_label": "Climate Change",
    ...
}
```

**What doesn't change:** gallery_config.json (subcategories live in
metadata, not config), json_converter.py, gallery_studio.py, any
non-climate gallery entries, the _studio flag system, the JSON pipeline.

**Design artifacts produced (for future reference):**
- `earth_system_exhibit_wireframe.md`: 13-screen scrollytelling mockup
  for "The Heat Chain" (energy imbalance -> temperature -> heat events ->
  human impacts). Now archived as future "Read mode" reference.
- `gallery_navigation_flowchart.mermaid`: three-mode architecture
  (Browse/Explore/Read) showing how all modes lead to same visualizations.
- `subcategory_handoff.md`: detailed implementation guide with targeted
  code snippets.

**Files modified:**
- `gallery_editor.py` (1,069 -> 1,452 lines)
- `index.html` (2,295 -> 2,400 lines)

**Files created:**
- `assign_subcategories.py` (one-time bootstrap, optional)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Scrollytelling vs open world | Open world (museum model) | Tony's bias: "a map more than a channel." Gallery is already a gallery |
| Where do paleoclimate charts go? | Under Climate Change | They're an interpretive layer explaining climate through deep time |
| Where does wet-bulb chart go? | Extreme Heating Events | It's a focused bridge between deep time and specific heat events |
| Subcategories in config or metadata? | Metadata only | Lighter touch; grows organically; config stays for top-level categories |
| Linear exhibits or connections? | Connections on objects (future) | Museum model: "see also" links, not forced paths |
| Curated feeds? | Future "Read mode" | Build rooms first, add audio guide later |
| Data caching priority | Fragility-first: Coral Reef Watch SST, GRACE-FO, MODIS, CPC | Preserve what might disappear, not what's most visual |
| Second-order effects | Tony-authored interpretive layer with attribution strength | Not auto-generated; anthropologist's synthesis with honest uncertainty |

---

**Technical Lessons Learned:**

- Tkinter `exportselection=True` (default) causes multiple Listbox
  widgets in the same dialog to steal selection from each other. Set
  `exportselection=False` on each Listbox when multiple coexist.

- Move Up/Down with direct array swap (`vizs[idx], vizs[other_idx] =
  ...`) fails intermittently when sibling entries are non-contiguous in
  the master array. Extract-reorder-reinsert is more robust: pull out
  the sibling group, swap within the extracted list, write back to
  original slot positions.

- Subcategory boundaries must be enforced in move operations. Without
  subcategory matching in the sibling filter, vizs can jump across
  boundary groups.

- Museum UX principle: "layered interpretation" -- visitors choose their
  depth of engagement. Object (viz) -> label (card metadata) -> wall
  text (interpretation) -> catalog (citations). Each layer is opt-in.

- Gallery navigation structure: max 3 levels deep (category ->
  subcategory -> visualization). Deeper hierarchies frustrate mobile
  users.

---

*"Let the facts speak but don't shy from the connections."*
-- Tony, on the interpretive approach, March 8, 2026

*"A map more than a channel."*
-- Tony, choosing open-world exploration over scrollytelling, March 8, 2026

*"The gallery is the communicator."*
-- Tony, on why to start at the audience end, March 8, 2026

*"I am also an anthropologist, besides artist and engineer."*
-- Tony, claiming the interpretive layer, March 8, 2026

*"Data Preservation is Climate Action."*
-- Standing project principle, applied to fragility-first prioritization

### Session 28 (Mar 9, 2026): Status Log, Tooltip Overhaul, Routing Bug

Three threads: adding a status log widget to Gallery Studio, updating
all button tooltips for current behavior, and discovering/diagnosing
a hover routing data loss bug.

**Status Log Widget (gallery_studio.py)**

Added a multi-line scrolled text log at the bottom of column 4 (col_3d),
below the 3D Scene section. Dark-themed (`#1a1a2e` background, light
grey text), 10 lines, read-only with auto-scroll.

New `_log_status(msg)` method replaces all 18 `status_var.set()` calls.
Prepends `HH:MM:SS` timestamp, appends to scrolled log, syncs to the
single-line status bar at bottom border. Both displays update together.

Additional logging beyond existing status messages:
- Trace visibility checkbox toggles: "Trace shown/hidden: {name}"
- Featured trace toggles: "Featured on/off: {name}"
- Select All / Select None: logs count
- Config diff on Preview/Export: compares against `_prev_config`
  snapshot, reports up to 5 changed keys with old->new values

**Tooltip Overhaul**

Updated tooltips on 9 controls to document current reload behavior,
especially the limitations around routed exports:

- Load: notes route resets to OFF, stripped traces are gone, blank
  hover stash means reload from raw source
- Reload: same semantics, explains hover text recovery
- Preview: clarifies non-destructive (loaded figure not modified)
- Export: explains destructive transforms baked in, reload recovers
- Reset: notes it doesn't affect trace visibility or featured traces
- Portrait Preset: mentions routing is destructive, reload reverts
- Landscape Preset: explicit about route OFF
- Original: distinguishes gallery export vs source file behavior
- Route hover: explains destructive pipeline, reload resets to OFF

**Route Hover Reset on Reload**

When loading a gallery export with `_studio_config` containing
`route_hover_to_panel: True`, the GUI now forces the route checkbox
to OFF after config restore. Routing is destructive (blanks trace
text), and the restore code recovers `_original_text` back to text,
so the figure is in a pre-routed state. Leaving the checkbox ON
would be misleading.

**Hover Routing Data Loss Bug -- Diagnosed**

Testing with the Apophis Closest Approach plot revealed that reloading
a gallery export and turning route back ON produces cards with names
only (no subtitle, no body). The hover mode was correctly set to
"Default" in the GUI and correctly injected as `var _hoverMode =
'default'` in the JS.

Root cause: the `_original_text` stash in the exported file contained
blank strings. The hover text was already gone. The routing pipeline
in `apply_config()` blanks `trace['text']` and stashes the original
in `_original_text`. If the source file was itself a gallery export
that had already been through routing, `_original_text` captures
blanks. The restore on reload recovers blanks. Data permanently lost.

Secondary bug found during diagnosis: the JS card handler was reading
`_hover_mode` from `_plotDiv.layout._hover_mode` (the rendered Plotly
DOM). Plotly's `newPlot()` can strip underscore-prefixed layout keys.
Fixed by injecting `_hoverMode` as a JS string literal via string
concatenation, bypassing the Plotly layout entirely.

Blank stash detection added to `_do_load()`: status log now warns
"WARNING: N traces had blank hover stash -- reload from raw orrery
source for full hover" when it detects the condition.

**Non-Destructive Routing -- Designed, Not Yet Implemented**

Tony's insight: "Keep all the information in the export, but only
display what's selected. With the option to strip globally, not just
for traces." This unifies the pattern:

- Non-destructive (default): routing ON means JS suppresses tooltips
  and shows cards, but `trace['text']` stays intact in the data.
  Full round-trip editing. No `_original_text` stash needed.
- Destructive (opt-in): generalize "Strip hidden" to "Strip
  suppressed data" -- strip hidden traces AND strip routed hover
  text. On reload of stripped file, grey out the controls for
  stripped content with status log warning.

Detailed implementation plan in `non_destructive_routing_handoff.md`.

**Bonus: Pre-existing em dash on line 4535 fixed to ASCII `--`.**

**Files Modified:**
- `gallery_studio.py` (~4,830 lines): status log widget, _log_status
  method, all status_var.set -> _log_status, trace/featured/config
  logging, tooltip overhaul, route reset on reload, blank stash
  detection, _hoverMode JS injection fix, em dash fix

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Status log placement | Bottom of col_3d | Natural reading flow: 3D controls above, activity log below |
| Timestamp format | HH:MM:SS | Enough precision for session tracking, compact |
| Config diff logging | On Preview/Export only | When `_collect_config` runs -- the natural "applying changes" moments |
| Route reset on reload | Force OFF | Routing is destructive; restored figure is pre-routed state |
| `_hoverMode` JS source | String literal injection | Plotly strips underscore layout keys; can't rely on DOM |
| Non-destructive routing | Design approved, build next session | Separates curation (what to show) from optimization (what to strip) |

---

**Technical Lessons Learned:**

- Plotly's `newPlot()` may strip underscore-prefixed layout keys from
  the rendered layout object. Never rely on `_plotDiv.layout._key`
  surviving render. Inject values as JS literals instead.

- Destructive transforms in a round-trip pipeline compound across
  cycles. If transform A blanks data and stashes it, and transform A
  runs again on the stashed version, the stash captures blanks. The
  safe pattern: keep data intact by default, strip on explicit request.

- "Source file = raw data. Gallery file = curated artifact" is correct
  but insufficient for full round-trip editing. The curated artifact
  should be fully re-editable, not just re-displayable. Non-destructive
  transforms make this possible.

---

*"Keep all the information in the export, but only display what's been
selected."*
-- Tony, the design insight that unifies non-destructive editing with
explicit stripping, March 9, 2026

*"The agentic drumbeat..."*
-- Tony, on Anthropic's Skills guide optimizing for removing humans
from the loop, March 9, 2026

### Session 29 (Mar 9, 2026): Non-Destructive Routing -- Phase 1 Shipped

Implemented the non-destructive routing architecture designed in
Session 28. Eight targeted changes to `gallery_studio.py`.

**Core change:** Routing no longer blanks `trace['text']`. Customdata
is still parsed from hover HTML for the info card, but the original
text stays intact in the figure data. Tooltip suppression is handled
by transparent hoverlabel (visual layer) instead of text destruction
(data layer).

**Changes made to `gallery_studio.py`:**

1. Routing block in `apply_config()`: removed `_original_text` stash
   and `trace['text'] = ['' for ...]` blanking. Kept customdata
   parsing, hovertemplate, and hoverinfo settings.

2. Animation frames routing: same removal pattern.

3. Hoverlabel config: moved `route_hover_to_panel` check outside the
   `output_format == 'portrait'` guard. Transparent hoverlabel now
   applies to all output formats when routing is active.

4. `_do_load()` restore block: simplified. Removed blank-stash
   detection and warnings. Kept backward-compat `_original_text`
   restore for older exports (pop and restore if present).

5. Three tooltip updates: Load, Reload, Route hover checkbox --
   updated language from "destructive" to "non-destructive."

6. Routing section comment updated.

**Test results:** Full 6-cell matrix (3 hover modes x route on/off)
passed. Round-trip export -> reload -> re-export with different
settings (dtick change) confirmed text intact throughout.

**Known cosmetic issue:** Route ON + Default hover shows a large grey
arrow pointer (Plotly tooltip arrow renders even with transparent
hoverlabel box). Diagnosed fix: change hovertemplate from
`'%{text}<extra></extra>'` to `'<extra></extra>'`. Deferred.

**Phase 2 (generalized "Strip suppressed data" UI) designed but
deferred.** May not be needed -- the main WYSIWYG objective is
accomplished with Phase 1.

**Files modified:**
- `gallery_studio.py` (~4,830 lines): 8 targeted changes

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Non-destructive routing | Shipped (Phase 1) | WYSIWYG round-trip editing is the Studio promise |
| Grey arrow pointer | Deferred cosmetic fix | `<extra></extra>` template eliminates it |
| Phase 2 strip UI | Designed, deferred | May not be needed; WYSIWYG accomplished |
| Backward compat for old exports | Pop `_original_text` on load | Simple, no version flags needed |
| Hoverlabel scope | All formats when routed | Text no longer blanked; visual suppression needed everywhere |

---

**Technical Lessons Learned:**

- Transparent hoverlabel suppresses the tooltip box but not the arrow
  pointer. The arrow is a separate SVG element. To fully suppress,
  use an empty hovertemplate (`'<extra></extra>'`) that references no
  data fields.

- Non-destructive routing cleanly separates data layer (keep
  everything) from display layer (show selectively). The previous
  approach conflated them by using text blanking for visual
  suppression.

- The hover_mode block runs AFTER routing and overwrites the
  hovertemplate. This means `names_only` and `none` modes override
  routing's template. For `default` mode, routing's template
  survives. Correct but must be understood when changing either block.

---

*"The main objective, WYSIWYG, is accomplished."*
-- Tony, confirming Phase 1 success, March 9, 2026

---

### Session 30: Encyclopedia "i" Button Missing in Gallery (March 13, 2026)

**Problem:** The encyclopedia "i" info button appeared in Studio preview and in
standalone exported HTML, but disappeared in the web gallery after
`json_converter.py` processing.

**Investigation path:**
1. `test_gallery.html` (Studio export) had 17 encyclopedia references including
   `enc-btn`, `encLock`, `encShowButton` functions -- the standalone export worked.
2. `test_gallery.json` (converter output) had zero `_encyclopedia` references.
3. The `_encyclopedia` data was present in `fig_dict['layout']` (added by
   `apply_config` when `embed_encyclopedia` is True), and `_build_encyclopedia_overlay`
   read it from there to generate the standalone HTML overlay.
4. But `build_gallery_html()` strips all underscore-prefixed keys from
   `layout_for_json` (line ~1800), then selectively preserves specific ones.
   `_encyclopedia` was NOT in the preserve list.
5. The standalone export worked because `_build_encyclopedia_overlay` reads from
   the original `fig_dict['layout']` (which still has it), not from `layout_for_json`.
   But `json_converter.py` extracts from `var layout = {...}` in the HTML, which
   uses `layout_for_json` -- so the data was lost.
6. Key finding: `_preview_as_gallery()` (line ~4362) ALREADY had the `_encyclopedia`
   preservation. Only `build_gallery_html()` was missing it. Classic parallel
   pipeline bug -- preview path worked, export path didn't.

**Root cause:** `_encyclopedia` missing from the underscore-key preserve list in
`build_gallery_html()`. Same bug pattern as `_kmz_handoff` (Session 27) and
`_hover_mode` (Session 29 Round 4).

**Fix 1: `gallery_studio.py` -- 2 lines added (~line 1819):**
```python
# Preserve _encyclopedia for gallery viewer info button
if '_encyclopedia' in layout_dict:
    layout_for_json['_encyclopedia'] = layout_dict['_encyclopedia']
```
Same pattern as `_studio`, `_kmz_handoff`, `_studio_nav`, `_hover_mode`.

**Fix 2: `index.html` -- encyclopedia overlay support (4 touchpoints):**

- **CSS** (~line 836): `.enc-btn` (circular "i" button), `.enc-overlay` (backdrop),
  `.enc-card` / `.enc-card-header` / `.enc-card-body` (modal card). Dark theme,
  scrollable body, close button.

- **HTML** (~line 1206): `<button class="enc-btn">i</button>` and
  `<div class="enc-overlay">` with card structure. Placed after info card div,
  before tap hint.

- **JS state + functions** (~line 1297 refs, ~line 2287 functions):
  - State: `_encData` (dict from layout), `_encCurrentName`, `_encLocked`
  - `encShowButton(name)`: show "i" on hover if entry exists
  - `encLock(name)`: lock "i" visible on click
  - `encHideButton()`: hide on unhover (unless locked)
  - `encOpenCard()` / `encCloseCard()`: modal open/close
  - `encReset()`: clear state when switching plots
  - Button events wired once (persistent elements); Escape key dismisses

- **JS wiring** (~line 1780): On plot load, reads `figDict.layout._encyclopedia`.
  If present, wires `plotly_hover` -> `encShowButton`, `plotly_click` -> `encLock`,
  `plotly_unhover` -> `encHideButton`. Then deletes `_encyclopedia` from layout
  before Plotly.newPlot (avoids Plotly console warnings about unknown keys).

- **JS reset** (~line 1524): `encReset()` called when switching plots (alongside
  `dismissInfoCard()` and annotation toggle reset).

- **Mobile toolbar** (~line 1402): `encBtn` appended to `vizToolbar` on screens
  < 1024px, between annotation toggle and share button.

**Positioning:** Desktop: `position: fixed; top: 92px; left: 62px` (below Share
button, clear of hamburger menu). Mobile: `position: relative` flows into toolbar
flexbox. Overlay: `position: fixed` for full-viewport coverage.

**Pipeline flow after fix:**
```
Studio (apply_config: embed_encyclopedia=true)
  -> _encyclopedia added to layout
  -> build_gallery_html preserves _encyclopedia in layout_for_json  [NEW]
  -> var layout = {...} in exported HTML includes _encyclopedia
  -> json_converter.py extracts layout including _encyclopedia
  -> gallery_metadata.json references the JSON file
  -> index.html loads JSON, reads layout._encyclopedia
  -> Creates "i" button + card overlay, wires plotly events
  -> Deletes _encyclopedia from layout before Plotly.newPlot
```

**Underscore-key preserve list (current complete list in `build_gallery_html`):**
- `_kmz_handoff` -- KMZ download handoff button (Session 27)
- `_studio` -- studio curation flag
- `_studio_config` -- full config for lossless round-trip re-export
- `_studio_nav` -- pan/zoom control flag
- `_hover_mode` -- hover mode for JS card handler (Session 29)
- `_encyclopedia` -- object encyclopedia data for info button (Session 30) [NEW]

**Test protocol:**
1. Load orrery source HTML in Studio with "Embed encyclopedia" checked
2. Export -> new gallery HTML
3. Run `json_converter.py` on the export
4. Verify `_encyclopedia` present in output JSON layout
5. Deploy to gallery, tap/click object -> "i" button appears
6. Click "i" -> encyclopedia card opens with object info
7. Switch to plot without encyclopedia -> "i" disappears, no errors

**Files modified:**
- `gallery_studio.py`: 1 change (underscore preserve line)
- `index.html`: 4 changes (CSS, HTML, JS functions, JS wiring + mobile toolbar)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Where to position "i" button (desktop) | Below Share button (top: 92px, left: 62px) | Original position (top: 12px, left: 12px) overlapped hamburger menu |
| Mobile "i" button | Flows into toolbar flexbox | Same pattern as nav, share, annotation toggle buttons |
| Encyclopedia overlay position | `position: fixed` | Must cover full viewport regardless of button position |
| When to delete _encyclopedia from layout | After reading, before Plotly.newPlot | Avoids Plotly console warnings; data already captured in JS variable |
| Encyclopedia + info card coexistence | Both work independently | "i" button is for encyclopedia deep-dive; info card is for hover data in portrait mode |

---

**Technical Lessons Learned:**

- The underscore-key preserve list in `build_gallery_html()` is now 6
  entries long and growing. Each new underscore key that needs to survive
  into the gallery must be added here. The pattern is consistent but the
  list is manual -- easy to miss.

- `_preview_as_gallery()` and `build_gallery_html()` have SEPARATE
  underscore-key preserve lists. A key present in one but not the other
  creates a preview-vs-export divergence that's hard to diagnose (preview
  works, export doesn't). Always check both when adding a new key.

- The standalone HTML export works differently from the gallery pipeline:
  `_build_encyclopedia_overlay()` reads from `fig_dict['layout']` directly
  (before stripping), so it always has the data. The gallery pipeline
  reads from `layout_for_json` (after stripping), so it needs the
  preserve line. Two paths, same data, different access points.

- `json_converter.py` doesn't need changes for new underscore keys --
  it does a raw JSON parse of `var layout = {...}`, so whatever keys
  are in `layout_for_json` survive automatically into the JSON file.

---

*"The preview worked but the export didn't -- parallel pipeline bug."*
-- On the encyclopedia fix, March 13, 2026

### Session 31 (Mar 16-17, 2026): Fly-to Mobile Buttons

**Problem:** The desktop "Fly to" dropdown menu (Plotly updatemenu annotation)
allows users to snap the 3D camera to a close-up heliocentric view of a
specific object with tight axis ranges. Essential for perihelion geometry,
close approaches, and flyby detail. But the portrait preset strips all
annotation-based menus ("Strip update menus"), removing fly-to functionality
entirely on mobile.

**Design session (Mar 16):** Zero-code session -- four rounds of iterative
design. Explored dropdown alternatives, evaluated mobile screen constraints,
designed data architecture, resolved reset-view dependency. Key insight:
compact buttons (bottom-left, opposite pan/zoom controls) with colored dots
matching trace colors. Maximum 4 targets. Existing "Reset View" in pan/zoom
D-pad handles return to full view -- no dedicated "Full View" button needed.

**Implementation (Mar 17):** Three files modified.

**gallery_studio.py (~210 lines added):**

- Studio UI: green fly-to checkbox column in Trace Visibility panel (alongside
  existing gold featured checkbox). Green-themed (`#2d8a4e`) to distinguish.
- `_on_flyto_toggle()`: max 4 enforcement, auto-enables pan/zoom arrows when
  any fly-to target checked (safety net -- guarantees Reset View exists).
- `_collect_flyto_targets()`: extracts position from trace data (last point of
  x/y/z arrays), computes camera + axis ranges matching desktop fly-to math
  from `visualization_utils.add_fly_to_object_buttons()`. Adaptive dtick via
  same algorithm as `_calculate_grid_dtick`. Extracts trace color for button
  styling.
- `flyto_targets` wired into `_collect_studio_config()` and stored in
  `_studio_config` blob.
- Preview/export: `flyto_css`, `flyto_html`, `flyto_js` embedded in
  `build_gallery_html()` following the nav arrows dual-path pattern. Uses
  `position: absolute` (inside aspect-frame) vs gallery viewer's
  `position: fixed`.

**index.html (~140 lines added):**

- CSS: `.flyto-controls` positioned `bottom: 24px; left: 16px` (opposite
  pan/zoom on right). Dark glass aesthetic matching existing controls.
- HTML: empty `<div class="flyto-controls" id="flytoControls"></div>`.
- JS: reads `_studio_config.flyto_targets` (with `_flyto_targets` fallback).
  Dynamically creates buttons with colored dots + name labels. Click handler
  calls `Plotly.relayout()` with camera, axis ranges, dtick, aspectmode.
  Captures original camera + ranges for reset. Stores originals as data
  attributes on the container element.
- `resetPanZoom()` 3D handler expanded to restore original axis ranges and
  recalculate original dtick when fly-to targets present.
- Added `title="Reset view"` to panReset button for desktop hover text.
- Card switch cleanup: clears fly-to buttons and innerHTML.

**json_converter.py -- no changes.** `_studio_config` passes through as blob.

**Data architecture:**

```python
layout['_studio_config']['flyto_targets'] = [
    {
        'name': '3I/ATLAS',
        'trace_index': 5,
        'color': '#ff0000',
        'camera': {'eye': {'x': 1.5, 'y': 1.5, 'z': 1.2},
                   'center': {'x': 0, 'y': 0, 'z': 0},
                   'up': {'x': 0, 'y': 0, 'z': 1}},
        'axis_ranges': {'xaxis': [min, max],
                        'yaxis': [min, max],
                        'zaxis': [min, max]},
        'dtick': 0.05
    }
]
```

**Data flow:**
```
Studio: green checkbox -> _collect_flyto_targets() -> config -> _studio_config
  build_gallery_html(): preserves in _studio_config blob AND renders inline buttons
JSON converter: _studio_config passes through as blob
Gallery viewer: reads flyto_targets, renders buttons, Plotly.relayout() on tap
Preview: embedded buttons, reset piggybacks on existing panPlot('reset')
```

**Note:** `flyto_targets` lives INSIDE `_studio_config`, not as a separate
underscore key. No addition to the underscore-key preserve list needed --
the `_studio_config` blob already survives.

**Verified working:**
- Studio loads, green checkboxes appear, max enforcement works
- Auto pan/zoom enable on fly-to check
- Full pipeline: Studio -> JSON converter -> gallery viewer -> buttons -> fly-to -> reset
- Preview: buttons appear with correct styling and navigation
- Multiple targets (3 tested), each flies to correct position
- Reset View restores original view including axis ranges and dtick

**Known limitations (accepted):**
- Fly-to checkboxes don't round-trip (same as trace visibility/featured)
- Auto pan/zoom enable is one-way nudge (user can disable after)
- Animation deferred (instant snap; Plotly transitions need broader testing)

**Files modified:**
- `gallery_studio.py`: ~210 lines (UI, methods, config, preview embed)
- `index.html`: ~140 lines (CSS, HTML, JS rendering, reset, cleanup)

---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Dropdown vs buttons | Buttons | Dropdown too space-heavy for mobile |
| Max targets | 4 | Limited mobile screen space |
| Reset View | Existing pan/zoom D-pad center button | No new UI needed |
| Camera data | Static at export | No JS math, consistent with Studio philosophy |
| Preview buttons | Embedded in `build_gallery_html()` | Same dual-path pattern as nav arrows |
| Feature C (preset export) | Not needed | Fly-to buttons give direct access to close-up |
| Gallery viewer positioning | `position: fixed` | Matches existing controls |
| Preview positioning | `position: absolute` | Stays inside aspect-frame container |

---

**Technical Lessons Learned:**

- Dual rendering paths (preview vs gallery viewer) require features in both
  places. Nav arrows established this pattern; fly-to buttons follow it. The
  preview uses `position: absolute` (aspect-frame containment) while the
  gallery viewer uses `position: fixed` (full-screen context).

- The preview's fly-to reset piggybacks on the existing `panPlot('reset')`
  which already captures `_initCamera` and `_initScene`. No duplicate reset
  logic needed -- just a different click handler for the fly-to, same restore
  mechanism.

- Config keys inside `_studio_config` use plain names (no leading underscore).
  Underscore prefix is reserved for layout-level flags (`_studio`, `_studio_nav`,
  `_kmz_handoff`). The JS defensively checks both forms.

- Feature C (fly-to preset export for standalone gallery cards) was designed
  but deemed unnecessary once fly-to buttons worked in both contexts. The
  buttons give users interactive access to the close-up view without needing
  a separate export.

---

*"Is this what they call 'software engineering' as distinct from 'coding'?"*
-- Tony, after a zero-code design session moved the project further than
most coding sessions, March 16, 2026
