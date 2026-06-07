### 🌊 Global Mean Sea Level Rise
- **Data**: NASA-SSH satellite altimetry (1993-2025)
- **Shows**: Sea level change vs 1993 baseline
- **Features**:
  - 60-day smoothed for clean trend
  - Current level marker (diamond)
  - Trend line showing acceleration
  - 32-year rise statistics
  - Zero baseline (1993 mean)
  - Threat warning about NASA budget
  - Impact context (coastal flooding, etc.)
  - Latest: ~+10.2 cm above 1993 baseline
  - Data format: Already in centimeters (no conversion)# Climate Data System - Quick Reference

**Data preservation is climate action.**

---

## Overview

A complete climate data visualization system integrated into Paloma's Orrery, featuring automated data fetching, safe cache management, and interactive visualizations for three critical climate indicators. All datasets now fetching automatically with full fail-safe protection.

---

## System Components

### 1. `fetch_climate_data.py`
**Automated data fetcher** - Downloads climate data from primary sources
- **CO₂ (Mauna Loa)**: Text file download from NOAA GML
- **Temperature (NASA GISS)**: Text file download from NASA
- **Arctic Ice (NSIDC)**: Excel file parsing (V4 format)
- **Fail-safe protection**: Never overwrites with smaller datasets
- **Atomic saves**: Backup → verify → move pattern
- **Emergency backups**: Created when dangerous saves detected
- Run anytime to update data

### 2. `earth_system_visualization_gui.py`
**Visualization hub** - Interactive Plotly charts with **5 active visualizations**:

**Active Visualizations:**
1. **🌡️ The Keeling Curve** - CO₂ concentration (1958-2025)
2. **🌡️ Global Temperature Anomalies** - Temperature vs baseline (1880-2025)
3. **📅 Monthly Temperature: Year-over-Year** - Seasonal patterns comparison
4. **🎨 Warming Stripes (Ed Hawkins Style)** - Visual temperature history
5. **🧊 Arctic Sea Ice Extent** - September minimum (1979-2025)

**Coming Soon:**
- 🌊 Sea Level Rise
- 🧪 Ocean Acidification

**Features:**
- **Update button**: One-click refresh for all 3 datasets
- **Time estimate**: Shows ~30 second warning before update
- **Detailed results**: Per-dataset success/failure reporting
- Launched from Earth checkbox in main orrery

### 3. `climate_cache_manager.py`
**Safe update manager** - Handles cache updates with validation
- Validates downloaded data before saving
- Prevents corruption with atomic writes
- **Returns 3 values**: (success, message, details)
- Updates all 3 datasets (CO₂, Temperature, Arctic Ice)
- Thread-safe for GUI integration
- Follows orbit_data_manager.py safety patterns

### 4. Modified Integration Files
**Main orrery integration**
- `palomas_orrery.py`: Earth System Visualization checkbox
- `palomas_orrery_helpers.py`: Earth URL button styling (ocean blue)

---

## Data Files

All stored in project root directory:

```
palomas_orrery/
├── co2_mauna_loa_monthly.json           (~177 KB, 810 records)
├── temperature_giss_monthly.json        (~139 KB, 1748 records)
├── arctic_ice_extent_monthly.json       (~51 KB, 561 records)
├── fetch_climate_data.py
├── earth_system_visualization_gui.py
├── climate_cache_manager.py
└── [other modules]
```

---

## Quick Start

### Initial Setup

**1. Install dependencies:**
```bash
pip install plotly numpy openpyxl
```

**2. Fetch data:**
```bash
python fetch_climate_data.py
```

**Expected output:**
- ✅ CO₂: ~810 records, latest ~425 ppm
- ✅ Temperature: ~1748 records, latest ~+1.14°C
- ✅ Arctic Ice: ~561 records (47 years × 12 months)

**3. Test visualizations:**
```bash
python earth_system_visualization_gui.py
```
- Click each button to open interactive Plotly charts
- Test the "🔄 Update Climate Data" button
- Confirm dialog shows ~30 second time estimate
- Verify success dialog shows all 3 datasets

**4. Launch from main orrery:**
```bash
python palomas_orrery.py
```
- Check "Earth" checkbox
- Expand to see shells
- Check "-- 🌍 Earth System Visualization" (green text)
- Hub window opens with all visualization buttons

---

## Visualizations

### 🌡️ The Keeling Curve
- **Data**: Mauna Loa CO₂ (1958-2025)
- **Shows**: Atmospheric CO₂ concentration trend
- **Features**: 
  - Current value marker (diamond)
  - Reference lines (350 ppm safe, 450 ppm danger)
  - 67-year increase statistics
  - Threat warning annotation
  - Seasonal oscillation visible

### 🌡️ Global Temperature Anomalies
- **Data**: NASA GISS (1880-2025)
- **Shows**: Temperature change vs 1951-1980 baseline
- **Features**:
  - Paris Agreement targets (1.5°C, 2.0°C)
  - Pre-industrial baseline reference (-0.3°C)
  - Progress bars showing warming
  - 145-year warming statistics
  - Data lag note (1-2 months for quality control)

### 📅 Monthly Temperature: Year-over-Year
- **Data**: NASA GISS monthly data (1880-2025)
- **Shows**: How each month has warmed over time
- **Features**:
  - 12 separate lines (one per month)
  - Color gradient showing warming progression
  - Seasonal patterns preserved
  - Pre-industrial baseline (-0.3°C)
  - Paris Agreement targets
  - Reveals which seasons warming fastest

### 🎨 Warming Stripes (Ed Hawkins Style)
- **Data**: NASA GISS annual average (1880-2025)
- **Shows**: Visual history of temperature change
- **Features**:
  - Ed Hawkins' iconic warming stripes design
  - Color scale: blue (cooler) → red (warmer)
  - No axes or labels (pure visual impact)
  - Each stripe = one year
  - Pre-industrial → present progression
  - 145 stripes showing accelerating warming

### 🧊 Arctic Sea Ice Extent
- **Data**: NSIDC monthly extent (1979-2025)
- **Shows**: September minimum sea ice area over time
- **Features**:
  - September minimum emphasis (annual low point)
  - Trend line showing decline (-12.1% per decade)
  - 2012 record low annotation (3.39 million km²)
  - 47-year decline statistics
  - **Green success box**: "Automated Data Retrieval Working"
  - Full monthly data available (561 records total)
  - Note: March maximum typically 15-16 million km²

---

## File Formats

### JSON Cache Structure
```json
{
  "metadata": {
    "dataset_name": "...",
    "description": "...",
    "source": {
      "organization": "...",
      "url": "...",
      "data_url": "...",
      "citation": "..."
    },
    "cached_date": "2025-10-15T...",
    "record_count": 561,
    "temporal_range": {
      "start": "1979-01",
      "end": "2025-09"
    },
    "units": "...",
    "measurement_method": "...",
    "threat_status": "...",
    "preservation_priority": "...",
    "version": "V4.0",
    "format": "Excel (XLSX) parsed to JSON",
    "migration_note": "..."
  },
  "data": [
    {
      "year": 2025,
      "month": 9,
      "extent_million_km2": 4.60,
      ...
    }
  ]
}
```

---

## Safety Features

### Cache Protection
- ✅ **Atomic saves**: temp → backup → move
- ✅ **Size validation**: Prevents >10% shrinkage
- ✅ **Record count tracking**: Warns if >5 records lost
- ✅ **Automatic rollback**: Restores backup on failure
- ✅ **Emergency backups**: Created when danger detected (`.emergency_TIMESTAMP`)
- ✅ **JSON validation**: Verifies structure before finalizing

### Data Validation
- ✅ JSON structure verification
- ✅ Minimum file size checks (CO₂: 30KB, Temp: 60KB, Ice: 20KB)
- ✅ Record count monitoring
- ✅ Date range validation
- ✅ Duplicate detection

### Thread Safety
- ✅ Background updates don't freeze GUI
- ✅ Confirmation dialog before starting
- ✅ Button state management (disabled during update)
- ✅ Thread-safe result dialogs using `window.after()`
- ✅ Console progress visibility

---

## Troubleshooting

### "openpyxl not found"
```bash
pip install openpyxl
```
Required for Arctic ice data (Excel parsing).

### "scipy not found"
```bash
pip install scipy
```
Required for sea level visualization (trend line calculation).

### "NASA sea level file not found"
```
✗ File not found: nasa_earthdata_sea_level_data.txt
  Please download from: https://science.nasa.gov/earth/explore/earth-indicators/sea-level/
```

**Solution:**
1. Register at NASA Earthdata: https://urs.earthdata.nasa.gov/
2. Download data from: https://science.nasa.gov/earth/explore/earth-indicators/sea-level/
3. Save as `nasa_earthdata_sea_level_data.txt` in project root
4. **OR** use the file included in the repository (updated periodically)

### "plotly not found"
```bash
pip install plotly
```
Required for all visualizations.

### "SAVE BLOCKED" Warning
**Good news!** This means fail-safe protection is working.

The system detected:
- File size shrinkage >10%
- Record count drop >5 records
- Potentially corrupted data

**What to do:**
1. Check your internet connection
2. Try updating again
3. Check console for specific error messages
4. Emergency backup was preserved automatically

### Empty/Corrupted Cache Files
If data files are corrupted:

```bash
# Delete corrupted files
rm co2_mauna_loa_monthly.json
rm temperature_giss_monthly.json
rm arctic_ice_extent_monthly.json

# Re-fetch from scratch
python fetch_climate_data.py
```

### Data Not Updating
**Check the update button workflow:**
1. Click "🔄 Update Climate Data"
2. Confirm dialog should appear (~30 sec warning)
3. Button should show "⏳ Updating..."
4. Console shows live progress
5. Success dialog shows per-dataset results

**If stuck:**
- Check console for errors
- Verify internet connection
- Check source URLs are accessible
- Try manual fetch: `python fetch_climate_data.py`

---

## GUI Update Workflow

### User Experience Flow

**Step 1: Click Update Button**
```
┌─────────────────────────────┐
│  🔄 Update Climate Data     │
└─────────────────────────────┘
```

**Step 2: Confirmation Dialog**
```
╔═══════════════════════════════════════╗
║  Update Climate Data                  ║
║                                       ║
║  This will download the latest data   ║
║  from NASA, NOAA, and NSIDC.         ║
║                                       ║
║  Estimated time: ~30 seconds          ║
║                                       ║
║  Continue?                            ║
║                                       ║
║  [  Yes  ]  [  No  ]                 ║
╚═══════════════════════════════════════╝
```

**Step 3: Progress (Console)**
```
Updating climate data...
Fetching Mauna Loa CO₂ data...
✓ CO₂: 810 records
Fetching NASA GISS temperature data...
✓ Temperature: 1748 records
Fetching NSIDC Arctic ice data...
Downloading Excel file...
Parsing monthly data...
✓ Arctic ice: 561 records
```

**Step 4: Results Dialog**
```
╔═══════════════════════════════════════╗
║  Update Complete!                     ║
║                                       ║
║  ✅ CO₂: 810 records                  ║
║  ✅ Temperature: 1748 records         ║
║  ✅ Arctic Ice: 561 records           ║
║                                       ║
║  All datasets updated successfully    ║
║                                       ║
║  [  OK  ]                             ║
╚═══════════════════════════════════════╝
```

---

## Architecture

### Data Flow

```
NOAA/NASA/NSIDC
      ↓
fetch_climate_data.py
      ↓
JSON cache files
      ↓
earth_system_visualization_gui.py
      ↓
Interactive Plotly charts
```

### Fail-Safe Protection Layers

```
1. Download → Verify integrity
2. Parse → Validate structure
3. Save to temp → JSON validation
4. Compare to existing → Size/count checks
5. Create backup → Store old version
6. Move temp to final → Atomic operation
7. If any step fails → Restore backup
8. If danger detected → Emergency backup
```

---

## Data Sources & Citations

**CO₂:**
> Keeling, C.D., S.C. Piper, R.B. Bacastow, et al. Atmospheric CO₂ concentrations from Mauna Loa Observatory. NOAA Global Monitoring Laboratory.

**Temperature:**
> GISTEMP Team, 2024: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies.

**Arctic Ice:**
> Fetterer, F., K. Knowles, W. N. Meier, M. Savoie, A. K. Windnagel, and T. Stafford. 2025. Sea Ice Index, Version 4. NSIDC: National Snow and Ice Data Center. doi:10.7265/a98x-0f50

**Sea Level:**
> NASA-SSH. 2025. Global Mean Sea Level from Simple Gridded Sea Surface Height from Standardized Reference Missions Only Version 1. PO.DAAC, CA, USA. Dataset accessed 2025-10-15 at https://doi.org/10.5067/NSIND-GMSV1.

---

## The Roadmap from Here

### **Phase 1: Keeling Curve** ✅ (Done!)
- `fetch_climate_data.py` ✅
- `co2_mauna_loa_monthly.json` ✅
- Visualization in hub ✅

### **Phase 2: Temperature** ✅ (Done!)
- NASA GISS dataset ✅
- Multiple temperature visualizations ✅
- Monthly lines and warming stripes ✅

### **Phase 3: Cryosphere** ✅ (Done!)
- Arctic sea ice extent ✅
- NSIDC V4 Excel parsing ✅
- September minimum visualization ✅

### **Phase 4: Oceans** ✅ (Done!)
- **Sea Level Rise** ✅
- Manual download approach (NASA Earthdata)
- 32-year satellite record preserved
- **Ocean Acidification** (Next priority)

### **Phase 5: Additional CO₂ Data** (Future)
**Goal:** Add redundancy and higher resolution for CO₂

**Datasets to add:**
- **Daily CO₂ data** (~1-2 MB)
  - Same Mauna Loa source, daily resolution
  - Shows short-term fluctuations
  - URL: `https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_daily_mlo.txt`
- **Global mean CO₂** (~30 KB)
  - Marine boundary layer average
  - Independent validation of Mauna Loa
  - URL: `https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.txt`

**Implementation:**
- Same fetch pattern as monthly CO₂
- Add new buttons to GUI (different colors)
- Expand `fetch_climate_data.py` with new functions

### **Phase 6: Temperature Enhancements** (Future)
**Current:** NASA GISS working ✅

**Future enhancements:**
- Add NOAA dataset (redundancy)
- Add HadCRUT5 (UK Met Office, longest record)
- Regional temperature breakdowns
- Comparison visualizations

### **Phase 7: Integration & Advanced Features** (Future)
**Multi-dataset comparisons:**
- CO₂ vs Temperature correlation
- Temperature vs Sea ice correlation
- Ocean pH vs CO₂ correlation (when pH added)

**Planetary boundaries framework:**
- Integrate all datasets into single framework
- Show safe operating space boundaries
- Display current status vs limits

**Interactive scenarios:**
- "What if we stopped emissions today?"
- Paris Agreement pathway comparison
- Business-as-usual projection

**Export capabilities:**
- Download full datasets as CSV
- Export visualizations as PNG/PDF
- Generate summary reports

---

## Next Immediate Steps

**Priority 1: Daily CO₂ Data**
1. Add `fetch_daily_co2()` function
2. Create `co2_mauna_loa_daily.json` cache
3. Add visualization button (different color)
4. Test full workflow

**Priority 2: Global Mean CO₂**
1. Add `fetch_global_co2()` function
2. Create `co2_global_mean_monthly.json` cache
3. Add visualization button
4. Create comparison chart (Mauna Loa vs Global)

**Priority 3: Sea Level Data**
1. Research best data sources (NOAA vs NASA)
2. Create `fetch_sea_level_data.py`
3. Design visualization (time series + trend)
4. Integrate into hub

---

## Development History

**October 15, 2025 - Current Status**
- ✅ All 3 core datasets fetching automatically
- ✅ 5 visualizations active and working
- ✅ NSIDC V3→V4 migration resolved
- ✅ Fail-safe cache protection implemented
- ✅ GUI update button with time estimates
- ✅ Detailed success/failure reporting
- ✅ All documentation current

**Key Milestones:**
1. Initial CO₂ and Temperature automation
2. Arctic ice "infrastructure crisis" discovered
3. Manual fallback implemented
4. V3→V4 migration investigation
5. V4 Excel parsing solution implemented
6. Fail-safe protection added
7. GUI integration completed
8. Monthly temperature and warming stripes added
9. All systems verified working

**The Pattern is Set:**

For each new dataset:
1. Create fetch function in `fetch_climate_data.py`
2. Generates `X_data.json` in root directory
3. Add `create_X_viz()` function to GUI file
4. Change button from gray to active
5. **Boom** - new visualization available!

---

## Support

**Questions?** Contact: tonyquintanilla@gmail.com

**Last Updated:** October 15, 2025

**Status:** 5 visualizations active, 3 datasets working! ✅🌍📊

---

**Not a moment to lose.** 🌍⚡