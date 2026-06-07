# Ocean pH Implementation - Current Status & Next Steps

## Context
Implementing ocean acidification visualization for Paloma's Orrery Earth System Visualization hub. This would be the 7th climate visualization alongside CO2, temperature (3 views), ice, and sea level.

## Current Working System (Verified)
User has tested and confirmed working:
- ✅ CO2 visualization (Keeling Curve)
- ✅ Temperature visualizations (3 types)
- ✅ Arctic ice visualization
- ✅ Sea level visualization
- ✅ fetch_climate_data.py successfully creates JSON files
- ✅ earth_system_visualization_gui.py successfully loads and displays all existing data

## What Was Added (Untested)

### 1. fetch_climate_data.py - Ocean pH Functions
**Added:** Lines ~40-280
- `fetch_ocean_ph_bcodmo()` - Try BCO-DMO data source
- `fetch_ocean_ph_hot_direct()` - Try HOT direct URLs
- `parse_carbonate_data()` - Flexible parser for carbonate chemistry data
- `create_ph_metadata()` - Generate metadata for pH dataset
- `fetch_ocean_ph()` - Main function with multiple fallback sources
- Integration into `main()` - Added pH as 5th dataset to fetch

**Key Decision:** Uses automated fetch with BCO-DMO/HOT sources, falls back to manual download instructions if automated fails.

### 2. earth_system_visualization_gui.py - Ocean pH Visualization
**Added:** Lines ~810-960
- `load_ph_data()` - Load ocean_ph_hot_monthly.json
- `create_ph_viz()` - Create Plotly visualization with:
  - Reversed y-axis (pH decline goes down visually)
  - Pre-industrial reference line (pH 8.2)
  - Baseline reference line (first year)
  - Trend line (uses scipy.stats)
  - Ocean blue theme (#0077BE)
  - Educational annotations about pH logarithmic scale
- `open_ph_viz()` - Error handling wrapper
- Updated pH button from disabled to active (ocean blue)
- Updated footer to "7 of 7 visualizations active"
- **CONFIRMED:** Button is packed, footer is packed

### 3. convert_hot_ph_to_json.py (Optional Manual Fallback)
**Created:** Complete standalone script
- Manual download workflow (like sea level)
- Flexible HOT data parser
- Generates ocean_ph_hot_monthly.json
- Only needed if automated fetch fails

## Key Design Decisions Made

### Data Source Strategy
**Hybrid approach:**
1. **Primary:** BCO-DMO (https://www.bco-dmo.org/dataset/3773)
2. **Secondary:** HOT direct URLs
3. **Fallback:** Manual download + conversion script

**Why hybrid:** BCO-DMO may not have direct CSV API, HOT URLs may 404, but manual download always works.

### Visualization Design
- **Reversed y-axis:** Makes pH decline visually intuitive (goes down)
- **Dual reference lines:** Pre-industrial AND baseline for context
- **Ocean blue color:** Matches ocean theme (#0077BE)
- **Educational focus:** Explains "0.1 drop = 30% more acidic"
- **Same pattern:** Matches existing visualizations (CO2, temp, ice, sea level)

## Files Modified

### fetch_climate_data.py
**Status:** pH functions added, integrated into main()
**Location:** Root directory
**Changes:**
- Added ocean pH constants (lines ~25-35)
- Added 5 new functions for pH fetching (lines ~40-280)
- Integrated pH fetch into main() after sea level (line ~786)

### earth_system_visualization_gui.py
**Status:** Complete pH visualization added
**Location:** Root directory
**Changes:**
- Added load_ph_data() function
- Added create_ph_viz() function (complete, ~150 lines)
- Added open_ph_viz() function
- Updated pH button from disabled to active
- Updated footer from "6 of 7" to "7 of 7"
- Both button and footer ARE packed

### convert_hot_ph_to_json.py
**Status:** Created as backup option
**Location:** Root directory (new file)
**Purpose:** Manual conversion if automated fetch fails

## Potential Issues Identified (Not Verified)

### Issue 1: Data Structure Inconsistency Question
**Question raised:** Do CO2 records use `'trend'` or `'co2_ppm'`?
**User says:** Visualizations work, so current structure is correct
**Resolution needed:** Verify actual JSON structure vs fetch script output

### Issue 2: Sea Level gmsl_mm Key
**Potential issue:** fetch_climate_data.py line 726 creates `'gmsl_cm'` but line 772 may try to access `'gmsl_mm'`
**User says:** Sea level visualization works
**Resolution needed:** Verify if this is actually a problem

### Issue 3: climate_cache_manager.py
**Status:** Has several potential issues with function signatures and return values
**User question:** "What about the cache manager?"
**Needs:** Full review of cache manager against working fetch_climate_data.py

## Next Steps for New Instance

### Immediate Actions
1. **Ask user:** Do you have working JSON files? Which ones?
2. **Ask user:** Have you tried running fetch_climate_data.py to create pH data?
3. **Ask user:** Have you tested the pH visualization button?

### Testing Workflow
```bash
# Test 1: Run fetch script
python fetch_climate_data.py

# Should see:
# 5. Fetching ocean pH data...
# [Success or failure with clear instructions]

# Test 2: Check if JSON created
# Look for: ocean_ph_hot_monthly.json

# Test 3: Test GUI
python earth_system_visualization_gui.py
# Click "🧪 Ocean Acidification" button

# Test 4: If automated fetch failed
python convert_hot_ph_to_json.py
# After manually downloading HOT data
```

### Files to Review in New Instance
1. **fetch_climate_data.py** - Check actual data structure created
2. **Existing JSON files** - Verify key names used
3. **climate_cache_manager.py** - Review against working fetch script
4. **earth_system_visualization_gui.py** - Only if visualization fails

## What's Working (Don't Touch)
- CO2 fetch and visualization ✅
- Temperature fetch and visualization ✅
- Ice fetch and visualization ✅
- Sea level fetch and visualization ✅
- GUI window and button layout ✅
- Update button and climate_cache_manager ✅ (if tested)

## What's New (Test These)
- Ocean pH fetch functions ⚠️
- Ocean pH visualization ⚠️
- Ocean pH button activation ⚠️

## Critical Context for Next Instance

**User has working system** - Don't assume bugs in existing code!

**Focus areas:**
1. Ocean pH automated fetch - will it work?
2. Ocean pH visualization - does it display correctly?
3. Data structure consistency - verify actual JSON vs expected

**Don't fix:**
- Anything in CO2/temp/ice/sea level that's currently working
- GUI layout (user confirmed it works)
- Cache manager (unless user reports issues)

## Quick Reference

### Ocean pH Expected Data Structure
```json
{
  "metadata": { ... },
  "records": [
    {
      "year": 1988,
      "month": 10,
      "date": "1988-10",
      "ph_total": 8.0856,
      "source": "HOT Station ALOHA"
    }
  ]
}
```

### Expected Behavior
- Button shows: "🧪 Ocean Acidification" (ocean blue, active)
- Click opens Plotly chart with reversed y-axis
- Chart shows pH declining over time
- Reference lines at pH 8.2 (pre-industrial) and baseline

### If Automated Fetch Fails
User should see clear instructions:
```
✗ Automated fetch failed

MANUAL DOWNLOAD OPTION:
1. Visit: https://www.bco-dmo.org/dataset/3773
2. Click 'Get Data' → Download CSV
3. Save as 'hot_carbonate_data.txt'
4. Run: python convert_hot_ph_to_json.py
```

## Summary
Implementation is **complete but untested**. User has working system for other datasets. Focus on testing NEW ocean pH code only, don't assume bugs in working code.
