# Index.html Transformation Audit

## Purpose

Map every transformation index.html applies to Plotly figure data,
categorize each as "move to studio" or "keep in index," and identify
which studio controls already exist.

---

## Category A: ALWAYS applied (regardless of _studio flag)

These run for every visualization, studio-curated or not.

| # | Transform | Line(s) | What it does | Disposition |
|---|-----------|---------|--------------|-------------|
| A1 | Theme auto-detection | 1262-1275 | Reads paper_bgcolor/plot_bgcolor/template to detect light vs dark | KEEP in index -- viewer needs to know theme for its own CSS; also move to studio as preview context |
| A2 | Template stripping | 1277-1280 | `delete figDict.layout.template` | KEEP in index -- safety net for version mismatch; studio already does this too |
| A3 | Remove fixed dimensions | 1283-1290 | Delete width/height, set autosize:true | KEEP in index -- container sizing is structural |
| A4 | Tall plot min-height | 1480-1487 | If aspect >= 0.8, set minHeight on container | KEEP in index -- responsive container behavior |
| A5 | Post-render resize | 1489-1492 | setTimeout -> Plotly.Plots.resize | KEEP in index -- structural |
| A6 | Portrait click handler | 1494-1549 | Wire plotly_click -> info card (portrait mode only) | KEEP in index -- viewer interaction, BUT info card content/format is a studio concern (see C6) |
| A7 | Tap hint | 1539-1548 | Show "tap any object" hint on first portrait load | KEEP in index -- viewer UX |
| A8 | Control panel selection | 1551-1568 | _studio_nav -> D-pad; else -> zoom only | KEEP in index -- but _studio_nav flag comes from studio |
| A9 | Plotly config (desktop) | 1464-1469 | displayModeBar:true, displaylogo:true, responsive:true | KEEP in index -- viewer config |
| A10 | Plotly config (mobile) | 1471-1476 | scrollZoom:true, doubleClick:false, displayModeBar:false | KEEP in index -- device-dependent viewer config |

---

## Category B: Applied ONLY when !isStudio (the override block)

These are the transforms that the _studio flag currently skips.
Lines 1292-1454 (inside `if (!isStudio) { ... }`).

### B1: Desktop-only transforms

| # | Transform | Line(s) | What it does | Studio control exists? | Disposition |
|---|-----------|---------|--------------|----------------------|-------------|
| B1a | Title deletion (mobile) | 1300-1301 | `delete figDict.layout.title` on <1024px | YES: show_title | MOVE to studio |
| B1b | Title rescue (desktop) | 1303-1311 | If all margins=0 and title exists, set margin.t=40 | PARTIAL: margin controls exist | MOVE to studio (preset handles zero-margin social views) |
| B1c | Dark theme overrides | 1316-1324 | paper/plot_bgcolor transparent, font color #e8e6e3 | YES: bg_color, title_color | MOVE to studio |
| B1d | 3D scene bgcolor | 1327-1330 | scene.bgcolor transparent (dark only) | YES: scene_bgcolor | MOVE to studio |

### B2: Mobile-only transforms (inside `window.innerWidth < 1024` block)

| # | Transform | Line(s) | What it does | Studio control exists? | Disposition |
|---|-----------|---------|--------------|----------------------|-------------|
| B2a | 3D aspect mode | 1331-1334 | scene.aspectmode = 'cube' on mobile | NO | MOVE to studio -- new control needed |
| B2b | Legend reposition | 1337-1349 | Horizontal legend at top, font 10, color #9a9a9a (dark only) | PARTIAL: legend_orientation, legend_font_size exist but not position/color | MOVE to studio -- extend existing controls |
| B2c | Hide colorbars | 1351-1366 | showscale=false on all traces + coloraxis | YES: show_colorbar | MOVE to studio |
| B2d | Strip footer annotations | 1368-1375 | Remove annotations with yref=paper and y<0 | YES: strip_footer_annotations | MOVE to studio |
| B2e | Annotation box transparency | 1377-1388 | bgcolor -> transparent, delete border* | YES: annotation_bg_transparent | MOVE to studio |
| B2f | Legend box transparency | 1390-1396 | bgcolor -> transparent, delete border* | PARTIAL: legend_bgcolor exists | MOVE to studio -- extend |
| B2g | Axis title font scaling | 1398-1409 | Font > 12 -> scaled to 75% (min 10) | YES: axis_title_font_size | MOVE to studio |
| B2h | Margin clamping | 1411-1416 | b clamped to 95, t to 10, l to 80 | YES: margin controls | MOVE to studio |
| B2i | Strip non-animate updatemenus | 1418-1428 | Keep only animation menus, remove hover toggles | YES: strip_updatemenus, keep_animation_controls | MOVE to studio |
| B2j | Default to names-only hover | 1429-1434 | Traces with customdata get names-only hovertemplate | YES: hover_mode | MOVE to studio |

### B3: Small-screen transforms (outside the <1024 mobile block but still inside !isStudio)

| # | Transform | Line(s) | What it does | Studio control exists? | Disposition |
|---|-----------|---------|--------------|----------------------|-------------|
| B3a | Annotation font scaling | 1437-1444 | <900px: font > 12 -> 70% (min 10) | PARTIAL: axis font controls exist but not annotation-specific | MOVE to studio -- new control or fold into existing |
| B3b | Title font scaling | 1446-1452 | <900px: font > 14 -> 70% (min 12) | YES: title_font_size | MOVE to studio |

---

## Category C: Info card rendering (portrait mode)

The click handler (A6) builds info card content from customdata or
trace.text. This is viewer-side rendering of content the studio prepared.

| # | Aspect | Current behavior | Studio role | Index role after refactor |
|---|--------|-----------------|-------------|-------------------------|
| C1 | customdata parsing | Tries JSON.parse on customdata | Studio prepares via hover routing | Index reads structured data -- KEEP |
| C2 | trace.text fallback | Parses <b>name</b> from raw HTML | Shouldn't be needed if studio routes all hover | KEEP as fallback but rarely triggered |
| C3 | Info card HTML/CSS | Hardcoded card styling in index | N/A -- viewer chrome | KEEP |
| C4 | Card show/dismiss | Click to show, click-away to dismiss | N/A -- viewer interaction | KEEP |
| C5 | Encyclopedia data | NOT PRESENT in index | Studio has it but it doesn't survive JSON | MOVE: studio embeds in JSON, index displays if present |
| C6 | Info card content format | Index decides line breaks, font sizes | Should match studio preview | Studio should control content format; index renders as-is |

---

## Summary: What moves, what stays

### MOVE to studio (content curation -- 16 transforms)

1. B1a - Title deletion (mobile)
2. B1b - Title rescue (zero-margin)
3. B1c - Dark theme overrides (bg + font color)
4. B1d - 3D scene bgcolor
5. B2a - 3D aspect mode (NEW control needed)
6. B2b - Legend reposition + styling (EXTEND existing)
7. B2c - Hide colorbars
8. B2d - Strip footer annotations
9. B2e - Annotation box transparency
10. B2f - Legend box transparency (EXTEND existing)
11. B2g - Axis title font scaling
12. B2h - Margin clamping
13. B2i - Strip non-animate updatemenus
14. B2j - Default to names-only hover
15. B3a - Annotation font scaling (NEW or fold in)
16. B3b - Title font scaling
+ C5 - Encyclopedia data embedding
+ C6 - Info card content format

### KEEP in index (structural viewer -- 10 items)

1. A1 - Theme auto-detection (for viewer CSS, not content transforms)
2. A2 - Template stripping (safety net)
3. A3 - Remove fixed dimensions + autosize
4. A4 - Tall plot min-height
5. A5 - Post-render resize
6. A6 - Portrait click handler (reads data, doesn't transform it)
7. A7 - Tap hint
8. A8 - Control panel selection (_studio_nav flag)
9. A9/A10 - Plotly config (desktop/mobile)
+ C1-C4 - Info card parsing and interaction

---

## New studio controls needed

| Control | Type | Default (landscape) | Default (portrait) |
|---------|------|--------------------|--------------------|
| 3D aspect mode | Dropdown: auto/cube/data/manual | auto | cube |
| Legend position preset | Dropdown: original/top-center-h/bottom-h | original | top-center-h |
| Legend text color | Color picker | (keep original) | #9a9a9a |
| Legend border transparent | Checkbox | unchecked | checked |
| Annotation font scale | Slider or spinbox (0=keep, 50-100%) | 0 (keep) | 70% |

All other transforms already have studio controls that just need their
defaults adjusted in the landscape/portrait presets.

---

## Preset updates needed

### Landscape preset (currently DEFAULT_CONFIG)

Add to defaults:
- Most B2 transforms should NOT be active (they're mobile-specific)
- B1c (dark bg) and B1d (scene bg) should be active for dark plots
- Keep current landscape defaults mostly as-is
- Add 3D aspectmode: 'auto' (leave original)

### Portrait preset (currently PORTRAIT_CONFIG)

Add to defaults:
- B2a: aspectmode = 'cube'
- B2b: legend horizontal, top-center, font 10, color #9a9a9a
- B2c: show_colorbar = False (already set)
- B2d: strip_footer_annotations = True (already set)
- B2e: annotation_bg_transparent = True (already set)
- B2f: legend bg transparent (already set via legend_bgcolor)
- B2g: axis font scaling (already set via axis_title_font_size)
- B2h: margin clamping -- margins already 0 in portrait preset
- B2i: strip_updatemenus = True (already set)
- B2j: hover_mode = 'none' (already set)
- B3a: annotation font scaling -- new, add at 70%
- B3b: title font scaling -- title already hidden in portrait

### "Gallery Mobile" preset (NEW -- for landscape content viewed on mobile)

This is the interesting case: landscape-exported content that needs
mobile optimization. Currently the index handles this automatically.
After refactor, the developer would need to create a second studio
export for mobile, OR we need a way to embed "mobile overrides" in
the JSON that the index applies based on device.

**This is the key design decision remaining.** Options:

Option 1: Developer creates two exports per viz (landscape + portrait)
- Pro: Full WYSIWYG control over both views
- Con: Double the work, double the gallery entries

Option 2: Studio embeds a "mobile_overrides" dict in the JSON
- Pro: One export serves both devices
- Con: Studio needs device simulation preview; overrides are still
  "hidden" (just hidden in JSON instead of index.js)

Option 3: Accept that structural device adaptation stays in index
- Pro: Simplest, least change
- Con: Some transforms (margin clamping, font scaling) are still
  invisible to developer

**Recommendation:** Option 3 with transparency. The index keeps
device-adaptive transforms (margin clamping, font scaling, aspect
mode) but these become DOCUMENTED behaviors, not hidden surprises.
The studio removes all CONTENT transforms (theme, legend styling,
annotation handling, hover mode, colorbar). The remaining device
transforms are structural (like CSS media queries) and predictable.

This reduces the "hidden transforms" from 16 to ~5, all of which
are responsive layout adjustments rather than content decisions.
