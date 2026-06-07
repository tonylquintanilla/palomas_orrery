# HANDOFF: HTML Export Mode (CDN vs Portable)

## Date: January 2, 2026
## Origin: Galactic Center visualization session
## Suggested by: Gemini 2.5 Pro

---

## The Problem

Plotly HTML exports bundle the entire Plotly.js library (~3.5 MB) inside each HTML file. This makes files large (~7 MB for Galactic Center) which:
- Slows down web hosting (Google Sites, etc.)
- Takes more storage space
- Slower to email/share
- **Google Drive shows scary "file too large to scan for viruses" warning**
- **Not practical for mobile users**

## The Solution

Plotly's `write_html()` supports `include_plotlyjs='cdn'` which:
- Loads Plotly.js from cdn.plot.ly instead of bundling it
- Reduces file size from ~7 MB to ~500 KB
- **Trade-off**: Requires active internet connection when viewing the file

---

## Google Drive & Mobile Benefits (Key Motivation!)

### Current Workflow (Portable Mode ~7 MB)

```
Upload to Google Drive 
    → "File too large to scan for viruses" warning 
    → User scared 
    → Downloads anyway (PC only)
    → Opens locally
```

**Problems:**
- Scary virus warning discourages users
- Mobile users can't practically download/view large HTML files
- Only works for PC users willing to ignore warnings

### With CDN Mode (~500 KB)

```
Upload to Google Drive 
    → File small enough to scan 
    → No warning!
    → May preview directly in browser (no download needed!)
    → Works on mobile!
```

**Benefits:**
- No virus scanning warning (file under scan threshold)
- Google Drive may allow **direct preview** in browser
- Mobile users can view without downloading
- Much faster download if needed

### Test This!

1. Generate Galactic Center HTML with CDN mode (already done)
2. Upload to Google Drive
3. Set sharing to "Anyone with link can view"
4. Try opening the link on mobile - see if it previews in browser
5. Check if virus warning is gone

---

## Comparison Table

| Aspect | Portable (~7 MB) | CDN (~500 KB) |
|--------|------------------|---------------|
| File size | Large | Small |
| Works offline | ✅ Yes | ❌ No (needs internet) |
| Google Drive warning | ⚠️ "Too large to scan" | ✅ No warning |
| Mobile friendly | ❌ Not practical | ✅ Possibly! |
| USB sharing | ✅ Perfect | ⚠️ Needs internet |
| Web hosting | ⚠️ Slow to load | ✅ Fast |
| Email attachment | ❌ Too large | ✅ Works |

---

## Current State

`sgr_a_grand_tour.py` now uses CDN mode:

```python
fig.write_html(
    output_file,
    auto_play=False,
    include_plotlyjs='cdn',  # Load from CDN (smaller file)
    full_html=True,
    config={'displayModeBar': True}
)
```

## Proposed Feature

Add a user-selectable option in the main Paloma's Orrery GUI to choose export mode.

### GUI Element

In settings or as a visible toggle:

```
HTML Export Mode:
  ( ) Portable (larger files, works offline) 
  (•) Web-optimized (smaller files, requires internet to view)
  
  [?] CDN = Content Delivery Network. Web-optimized files load the 
      Plotly graphics library from the internet each time you open them.
```

### Implementation Steps

1. **Add setting to main GUI** (`palomas_orrery.py`)
   - Add a BooleanVar or StringVar for the preference
   - Add radio buttons or checkbox in settings area
   - Persist the setting (optional - could use a simple config file)

2. **Create shared config module** (new file: `html_export_config.py`)
   ```python
   # html_export_config.py
   
   # Default: Portable for maximum compatibility
   USE_CDN = False
   
   def get_plotlyjs_setting():
       """Returns 'cdn' or True based on user preference."""
       return 'cdn' if USE_CDN else True
   
   def set_cdn_mode(enabled: bool):
       """Set the export mode. Called from GUI."""
       global USE_CDN
       USE_CDN = enabled
   ```

3. **Update all visualization modules** that generate HTML:
   - `sgr_a_grand_tour.py`
   - `visualization_3d.py` (if applicable)
   - `paleoclimate_visualization.py` (if applicable)
   - Any other modules with `write_html()` calls

   Change pattern:
   ```python
   # Before
   fig.write_html(output_file)
   
   # After
   from html_export_config import get_plotlyjs_setting
   fig.write_html(output_file, include_plotlyjs=get_plotlyjs_setting())
   ```

4. **Update README/documentation**
   - Explain the two modes
   - Note which mode is active by default

### Files to Modify

| File | Change |
|------|--------|
| `palomas_orrery.py` | Add GUI toggle, wire to config |
| `html_export_config.py` | NEW - shared config module |
| `sgr_a_grand_tour.py` | Import config, use setting |
| `visualization_3d.py` | Import config, use setting (if has write_html) |
| Other viz modules | Same pattern |

### Default Recommendation

**Default to Portable mode** because:
- Works for all users regardless of internet
- Better for USB/offline sharing (common use case for Tony)
- Users who want smaller files can opt-in

### Testing

1. Generate HTML in both modes
2. Verify CDN version works with internet
3. Verify CDN version fails gracefully without internet (shows error, not blank)
4. Verify Portable version works offline
5. Check file sizes match expectations (~500 KB vs ~7 MB)

---

## Quick Reference

```python
# CDN mode (small file, needs internet)
fig.write_html(file, include_plotlyjs='cdn')

# Portable mode (large file, works offline)
fig.write_html(file, include_plotlyjs=True)

# Current Plotly CDN URL (for reference)
# https://cdn.plot.ly/plotly-latest.min.js
```

---

## Session Context

This came up during the Galactic Center S-star visualization session where the HTML file was ~7 MB. Gemini suggested the CDN optimization. Tony liked the idea but wanted user control rather than hardcoding one approach.

The Galactic Center module (`sgr_a_grand_tour.py`) is currently set to CDN mode as a test. Revert to `include_plotlyjs=True` if needed before the full refactor.
