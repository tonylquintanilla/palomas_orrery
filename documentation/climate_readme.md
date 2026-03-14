# Earth System Visualization - Climate Data Hub

**Data Preservation is Climate Action**

This system preserves and visualizes **critical climate indicators** from threatened data sources, now including an **integrated Planetary Boundaries framework** showing Earth system health holistically. All datasets are cached locally to ensure long-term availability regardless of institutional funding changes.

---

## Overview

The Earth System Visualization Hub provides interactive visualizations of critical climate measurements:

1. **The Keeling Curve** - Atmospheric CO₂ (Mauna Loa Observatory, 1958-2025)
2. **Global Temperature Anomaly** - NASA GISS surface temperature (1880-2025)
3. **Monthly Temperature Progression** - Year-over-year comparison (1880-2025)
4. **Warming Stripes** - Ed Hawkins style heatmap (1880-2025)
5. **Arctic Sea Ice Extent** - NSIDC satellite observations (1979-2025)
6. **Global Sea Level Rise** - NASA sea surface height (1993-2025)
7. **Ocean Acidification** - Hawaii Ocean Time-series (1991-2023)
8. **Planetary Boundaries** - Stockholm Resilience Centre framework ⭐ **NEW!**

### Current Status: ✅ 8 of 8 Working!

- ✅ **CO₂**: 810 records, automated fetch
- ✅ **Temperature**: 1,748 records, automated fetch
- ✅ **Arctic Ice**: 559 records, automated fetch
- ✅ **Sea Level**: 1,699 records, manual download (file included)
- ✅ **Ocean pH**: 257 records, manual download
- ✅ **Planetary Boundaries**: 2/9 boundaries with live data ⭐ **NEW!**

---

## Why This Matters

Critical climate monitoring infrastructure faces unprecedented threats:

- **Mauna Loa Observatory**: Lease expires August 2025, closure possible
- **NASA Earth Science**: 52% budget cuts proposed (FY2026)
- **NSIDC**: Downgraded to "Basic" service, reduced data processing
- **NOAA**: Budget uncertainty, service reductions

**This system ensures these irreplaceable datasets remain accessible** regardless of institutional changes.

---

## Planetary Boundaries Visualization ⭐ NEW!

### What It Shows

An interactive radial visualization based on the **Stockholm Resilience Centre's Planetary Boundaries framework**, showing 9 critical Earth system processes that regulate planetary stability.

**Key Features:**
- **Gradient coloring**: Green (safe) → Yellow → Orange → Red (transgressed)
- **2 live boundaries** integrated with your climate data cache
- **7 placeholder boundaries** ready for future data integration
- **Professional SRC-style design** with proper attribution
- **Educational context** about each boundary

### Live Data Integration (2/9 Boundaries)

**Currently Active:**

1. **Climate Change**
   - Data: NASA GISTEMP temperature anomaly
   - Current: ~1.14°C above baseline
   - Status: Zone of uncertainty (approaching 1.5°C Paris target)
   - Updates: Automatically with temperature data

2. **Ocean Acidification**
   - Data: HOT Station ALOHA pH measurements
   - Current: ~0.15-0.18 pH units decline from pre-industrial
   - Status: High risk (transgressed 0.10 threshold)
   - Updates: Automatically with pH data

**Ready for Integration (7 Boundaries):**

3. **Stratospheric Ozone Depletion** - (placeholder)
4. **Atmospheric Aerosol Loading** - (placeholder)
5. **Novel Entities** - (placeholder)
6. **Biogeochemical Flows (P & N)** - (placeholder)
7. **Freshwater Change** - (placeholder)
8. **Land-System Change** - (placeholder)
9. **Biosphere Integrity** - (placeholder)

### Attribution & License

The Planetary Boundaries framework is used under proper attribution:

```
The 2025 update to the Planetary boundaries.
Licensed under CC BY-NC-ND 3.0.
Credit: Azote for Stockholm Resilience Centre,
based on analysis in Sakschewski and Caesar et al. 2025
```

**Reference:**
- Richardson et al. (2023). "Earth beyond six of nine planetary boundaries." *Science Advances*, 9(37), eadh2458.
- Stockholm Resilience Centre: https://www.stockholmresilience.org/research/planetary-boundaries.html

**License Compliance:**
- ✅ Attribution provided to SRC and original creators
- ✅ Non-commercial educational use
- ✅ Adapts framework without modifying original image
- ✅ CC BY-NC-ND 3.0 requirements met

### Future Expansion Possibilities

Additional boundaries can be integrated as data becomes available:

- **CO₂ levels** → Feed into Climate Change boundary
- **Sea ice extent** → Climate/cryosphere indicator
- **Sea level rise** → Climate impact indicator
- **Land use data** → Land-System Change
- **Water usage data** → Freshwater Change
- **Biodiversity metrics** → Biosphere Integrity

---

## System Components

### Core Files

**1. `fetch_climate_data.py`**
**Climate data fetcher** - Downloads and caches datasets from NOAA, NASA, NSIDC
- Fetches CO₂, temperature, Arctic ice, sea level data
- Atomic writes with fail-safe protection
- Emergency backups on dangerous saves
- Auto-validates data integrity
- Handles format migrations (V3→V4)
- User-Agent headers for blocked servers

**2. `earth_system_visualization_gui.py`**
**Interactive visualization hub** - 8 Plotly visualizations with update button
- The Keeling Curve (CO₂ 1958-2025)
- Global Temperature Anomaly (1880-2025)
- Monthly Temperature Progression (year-over-year)
- Warming Stripes (Ed Hawkins style)
- Arctic Sea Ice Extent (1979-2025)
- Global Sea Level Rise (1993-2025)
- Ocean Acidification (1991-2023)
- **Planetary Boundaries (SRC framework)** ⭐ NEW!
- "Update Climate Data" button (updates 4 automated datasets)

**3. `climate_cache_manager.py`**
**Thread-safe data updater** - Manages background updates from GUI
- Runs fetch_climate_data.py as subprocess
- Validates downloaded data (file sizes, record counts)
- Reports detailed success/failure status
- Thread-safe for GUI integration

**4. `convert_sea_level_txt_to_json_onetime.py`**
**Sea level data converter** - One-time conversion utility
- Converts NASA text file to JSON format
- Parses year+fraction format to year/month
- Extracts GMSL and smoothed values
- Run once after downloading NASA data file
- Generates `sea_level_gmsl_monthly.json`

**5. `convert_hot_ph_to_json.py`**
**Ocean pH data converter** - Converts BCO-DMO HOT data to JSON
- Parses BCO-DMO CSV format (auto-detects multiple filenames)
- Filters for surface measurements (< 50m depth)
- Aggregates multiple measurements to monthly averages
- Handles ISO datetime format parsing
- Generates `ocean_ph_hot_monthly.json`
- Run after downloading BCO-DMO data file

### Integration Files
**Main orrery integration**
- `palomas_orrery.py`: Earth System Visualization checkbox
- `palomas_orrery_helpers.py`: Earth URL button styling (ocean blue)

---

## Data Files

**All climate data now stored in `data/` subdirectory** (as of November 2025):

```
palomas_orrery/
├── data/                                      # Climate data directory 
│   ├── co2_mauna_loa_monthly.json            (~177 KB, 810 records)
│   ├── temperature_giss_monthly.json         (~139 KB, 1748 records)
│   ├── arctic_ice_extent_monthly.json        (~68 KB, 559 records)
│   ├── sea_level_gmsl_monthly.json           (~252 KB, 1699 records)
│   ├── ocean_ph_hot_monthly.json             (~35 KB, 257 records)
│   ├── 3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv  (raw HOT data)
│   └── nasa_earthdata_sea_level_data.txt     (source file - included)
├── fetch_climate_data.py                     (saves to data/)
├── earth_system_visualization_gui.py         (loads from data/)
├── climate_cache_manager.py                  (manages data/)
├── convert_sea_level_txt_to_json_onetime.py  (saves to data/)
├── convert_hot_ph_to_json.py                 (saves to data/)
└── [other modules]
```

**Benefits of unified data/ directory:**

- Clean separation of code and data
- Easier project copying (copy *.py and data/)
- Clear data preservation structure
- Consistent with paleoclimate data organization

---

## Quick Start

### Initial Setup

**1. Install dependencies:**
```bash
pip install plotly numpy openpyxl scipy requests
```

**2. Fetch automated data (CO₂, Temperature, Arctic Ice):**
```bash
python fetch_climate_data.py
```

**Expected output:**
- CO₂: ~810 records, latest ~425 ppm
- Temperature: ~1748 records, latest ~+1.14°C
- Arctic Ice: ~559 records (47 years × 12 months)
- Sea Level: Finds local file, creates JSON

**3. Sea level data (already included!):**

The `nasa_earthdata_sea_level_data.txt` file is **already in your repository**. If you need to update it:

1. Register (free) at https://urs.earthdata.nasa.gov/
2. Download from NASA Earth Indicators: https://science.nasa.gov/earth/explore/earth-indicators/sea-level/
3. Save as `nasa_earthdata_sea_level_data.txt`
4. Run converter: `python convert_sea_level_txt_to_json_onetime.py`

**4. Ocean pH data (manual download):**

1. Go to: https://www.bco-dmo.org/dataset/3773
2. Click the download button for the CSV file
3. 3Save to your orrery/data/ subdirectory (or root - converter finds either location)
4. Run converter: `python convert_hot_ph_to_json.py`

**5. Test visualizations:**
```bash
python earth_system_visualization_gui.py
```
- Click each button to open interactive Plotly charts
- Test the "Update Climate Data" button (updates 4 automated datasets)
- Test all 8 working visualizations including **Planetary Boundaries**!

**6. Integration with Paloma's Orrery:**
- Launch main orrery: `python palomas_orrery.py`
- Check "Earth System Visualization" box
- Click Earth URL button (ocean blue)
- Hub opens automatically

---

## Available Visualizations

### 1. The Keeling Curve (CO₂)
- **What**: Atmospheric CO₂ concentration at Mauna Loa Observatory
- **Timespan**: March 1958 - Present (~67 years)
- **Records**: 810 monthly measurements
- **Current**: ~425 ppm (October 2025)
- **Trend**: +2.5 ppm/year (accelerating)
- **Threat**: Observatory lease expires August 2025

### 2. Global Temperature Anomaly
- **What**: NASA GISS surface temperature vs 1951-1980 baseline
- **Timespan**: 1880 - Present (145 years)
- **Records**: 1,748 monthly measurements
- **Current**: ~+1.14°C above baseline (~+1.44°C vs pre-industrial)
- **Features**: Paris Agreement targets shown (1.5°C, 2.0°C)
- **Threat**: NASA GISS faces 52% budget cuts

### 3. Monthly Temperature Progression
- **What**: Year-over-year monthly temperature comparison
- **Style**: All years shown as colored lines (blue→red gradient)
- **Timespan**: 1880-2025
- **Features**: Visual warming trend, seasonal patterns visible
- **Educational**: Shows how recent years dominate warming

### 4. Warming Stripes
- **What**: Ed Hawkins style heatmap (#ShowYourStripes)
- **Style**: Monthly grid colored by temperature anomaly
- **Colors**: Blue (cool) to Red (hot)
- **Timespan**: 1880-2025 (145 years × 12 months)
- **Impact**: Immediate visual of acceleration

### 5. Arctic Sea Ice Extent
- **What**: September minimum ice extent (annual low point)
- **Timespan**: 1979-2025 (47 years)
- **Records**: 559 monthly records (all 12 months available)
- **Current**: Declining ~12.1% per decade
- **Record Low**: 3.39 million km² (September 2012)
- **Status**: ✅ Automated fetch working (V4 Excel format)

### 6. Global Sea Level Rise
- **What**: NASA satellite altimetry (60-day smoothed)
- **Timespan**: 1993-2025 (32 years)
- **Records**: 1,699 biweekly measurements
- **Current**: ~+10 cm above 1993 baseline
- **Trend**: Accelerating rise
- **Update**: Manual download required (file included)

### 7. Ocean Acidification
- **What**: Surface pH measurements at HOT Station ALOHA
- **Timespan**: 1991-2023 (32 years)
- **Records**: 257 monthly averages
- **Current**: pH ~8.05 (vs ~8.20 pre-industrial)
- **Decline**: -0.18 pH units over 32 years
- **Impact**: 30% increase in acidity (logarithmic scale)
- **Update**: Manual download (BCO-DMO data)

### 8. Planetary Boundaries ⭐ NEW!
- **What**: SRC framework showing 9 Earth system boundaries
- **Style**: Radial wedge chart with gradient coloring
- **Live Data**: 2/9 boundaries (Climate Change, Ocean Acidification)
- **Placeholders**: 7 boundaries ready for integration
- **Features**: 
  - Gradient risk zones (green→yellow→orange→red)
  - Hover tooltips with detailed boundary info
  - Links to existing temperature and pH visualizations
  - Professional SRC-style design
  - Full attribution to Stockholm Resilience Centre
- **Educational**: Shows holistic Earth system health
- **Framework**: Richardson et al. (2023) Science Advances

---

## Data Sources & Details

### 1. CO₂ (Mauna Loa) - 🟢 Automated

**Source**: NOAA Global Monitoring Laboratory
**URL**: https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt
**Update frequency**: Monthly (typically 1 week after month end)
**Coverage**: March 1958 - present
**Records**: ~810 monthly measurements

**Threat**: Mauna Loa Observatory lease expires August 2025. Observatory may close, ending the world's longest continuous atmospheric CO₂ record.

---

### 2. Temperature (NASA GISS) - 🟢 Automated

**Source**: NASA Goddard Institute for Space Studies
**URL**: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt
**Update frequency**: Monthly (1-2 month lag for quality control)
**Coverage**: 1880 - present (145 years)
**Records**: ~1,748 monthly measurements

**Threat**: NASA GISS faces 52% budget cuts and institutional uncertainty. James Hansen's 145-year legacy dataset at risk.

---

### 3. Arctic Ice (NSIDC) - 🟢 Automated

**Source**: NSIDC Sea Ice Index V4.0
**URL**: https://noaadata.apps.nsidc.org/NOAA/G02135/seaice_analysis/
**Format**: Excel (XLSX) - Changed from V3 CSV in October 2024
**Update frequency**: Daily/Monthly
**Coverage**: November 1978 - present
**Records**: 559 monthly values (47 years × 12 months)

**Migration Note**: Automated fetch successfully migrated from V3 (CSV/FTP) to V4 (XLSX/HTTPS) in October 2024.

**Threat**: NSIDC downgraded to "Basic" service level with reduced data processing capabilities.

---

### 4. Sea Level (NASA) - 🔵 Manual Download

**Source**: NASA Earth Indicators / PO.DAAC
**URL**: https://science.nasa.gov/earth/explore/earth-indicators/sea-level/
**Update frequency**: Quarterly updates
**Coverage**: 1993 - present (32 years)
**Records**: 1,699 biweekly measurements

**Why manual?**: NASA Earthdata requires authentication. File is **included in repository** so users don't need to download it. Update quarterly as needed.

**Threat**: NASA Earth Science budget uncertainty. Satellite missions expensive and politically vulnerable.

---

### 5. Ocean pH (HOT) - 🔵 Manual Download

**Source**: BCO-DMO (Biological and Chemical Oceanography Data Management Office)
**Data Source**: Hawaii Ocean Time-series (HOT) Program
**URL**: https://www.bco-dmo.org/dataset/3773
**Update frequency**: Annual or biannual major version releases (1-2 year data lag)
**Coverage**: Station ALOHA (22°45'N, 158°W), February 1991 - December 2023
**Records**: 257 monthly averages (surface measurements only)

**Latest Version**: Version 3, released April 22, 2025
**Data Lag**: ~1-2 years between sampling and public release

**Why manual?**: BCO-DMO uses dynamic web pages (not direct CSV API). The download link returns HTML instead of CSV data, so automated fetching doesn't work reliably.

---

### 7. Ocean Heat Content (NOAA NCEI) - 🔵 Manual Download

**Source**: NOAA National Centers for Environmental Information (NCEI)
**URL**: https://www.ncei.noaa.gov/access/global-ocean-heat-content/
**Data**: Ocean Heat Content 0-2000m (Levitus et al.)
**Format**: CSV (quarterly data)
**Citation**: Levitus et al. (2012). "World ocean heat content and thermosteric sea level change (0-2000 m), 1955-2010." Geophysical Research Letters, 39(10).

**What it shows**:
- Cumulative ocean heat content in the upper 2000m
- Units: 10²² Joules (Zettajoules, ZJ)
- Time range: 2005-2025 (quarterly updates)
- Used to calculate Earth's energy imbalance (derivative)

**How to download**:
1. Visit https://www.ncei.noaa.gov/access/global-ocean-heat-content/
2. Navigate to "0-2000m" dataset
3. Download CSV file (quarterly data)
4. Save as `data/ohc2000m_levitus_climdash_seasonal.csv`
5. Format: Two columns, no header: `YYYY-Q,value_in_zj`

**Why manual?**: NOAA provides data via web interface with dynamic content. Direct CSV download link may change.

**Data usage**:
- Direct plot: Cumulative ocean heat (blue dotted line)
- Calculated: Energy imbalance = rate of change (W/m²)
- Key insight: Ocean absorbs ~90% of Earth's excess energy

---

### 8. Planetary Boundaries Framework - 🎓 Educational

**Source**: Stockholm Resilience Centre
**URL**: https://www.stockholmresilience.org/research/planetary-boundaries.html
**License**: CC BY-NC-ND 3.0
**Attribution**: Azote for Stockholm Resilience Centre, based on Sakschewski and Caesar et al. 2025
**Reference**: Richardson et al. (2023) Science Advances 9(37): eadh2458

**What we integrate**:
- Framework structure (9 boundaries)
- Risk zone concepts (safe → uncertainty → transgressed)
- Boundary names and definitions
- Visual design inspiration (gradient radial chart)

**What we add**:
- Live data from our climate cache (2/9 boundaries)
- Interactive hover tooltips
- Links to detailed visualizations
- Educational context

---

## Development History

### October 15, 2025 - Phase 1: The Keeling Curve
- ✅ Created `fetch_climate_data.py` with Mauna Loa CO₂ fetcher
- ✅ Built first Plotly visualization (Keeling Curve)
- ✅ Created Earth System Visualization GUI hub
- ✅ Integrated with main orrery (Earth checkbox)
- ✅ Added data caching with JSON format
- ✅ Documented Mauna Loa closure threat

### October 15, 2025 - Phase 2: Temperature Added
- ✅ Added NASA GISS temperature data fetcher
- ✅ Created temperature anomaly visualization
- ✅ Activated temperature button in GUI
- ✅ Updated cache manager for 2 datasets
- ✅ Documented NASA budget threat

### October 15, 2025 - Phase 3: Arctic Ice Crisis & Resolution
- ⚠️ NSIDC data fetch initially failed (404 errors)
- 🔍 Discovered V3→V4 migration (December 2023)
- 🔍 Found new V4 Excel format in seaice_analysis/ folder
- ✅ Updated to V4 URLs and Excel parsing
- ✅ Added openpyxl dependency
- ✅ Successfully fetching all 12 months of data
- ✅ Created Arctic ice visualization (September minimum)
- ✅ Activated ice button in GUI
- 📋 Documented migration for future reference

### October 16, 2025 - Phase 4: Comprehensive Fail-Safe Protection
- ✅ Implemented atomic save operations (temp → backup → move)
- ✅ Added file size validation (blocks >10% shrinkage)
- ✅ Added record count monitoring (warns >5 record loss)
- ✅ Created emergency backup system (`.emergency_TIMESTAMP`)
- ✅ Added automatic rollback on save failures
- ✅ JSON validation before finalization
- ✅ CO₂ field name fixes (`co2_ppm`, `co2_deseasonalized`)
- ✅ Temperature field name fixes (`anomaly_c`)
- ✅ NASA GISS User-Agent header fix (403 error)
- ✅ All 3 automated datasets working perfectly!

### October 18, 2025 - Phase 5: Sea Level & Ocean pH Complete
- ✅ Added NASA sea level data (manual download)
- ✅ Created sea level converter script
- ✅ Built sea level visualization
- ✅ Fixed sea level field names (`gmsl_cm`)
- ✅ Documented NASA Earthdata authentication
- ✅ Included data file in repository
- ✅ **Ocean pH implementation complete!**
- ✅ Created `convert_hot_ph_to_json.py` converter
- ✅ Built ocean pH visualization with reversed y-axis
- ✅ Added educational annotations (logarithmic scale impact)
- ✅ Tested with BCO-DMO HOT dataset (257 monthly records)
- ✅ Documented manual download workflow
- ✅ All 5 climate datasets now operational!
- ✅ **257 ocean pH measurements** spanning 32 years (1991-2023)
- ✅ Shows -0.18 pH unit decline (unprecedented rate)
- ✅ Added Monthly Temperature Progression visualization
- ✅ Added Warming Stripes (Ed Hawkins style) visualization

### October 18, 2025 - Phase 6: Planetary Boundaries Integration ⭐ NEW!
- ✅ **Planetary Boundaries visualization implemented**
- ✅ Integrated Stockholm Resilience Centre framework
- ✅ Connected 2/9 boundaries to live climate data:
  - Climate Change (NASA GISTEMP temperature)
  - Ocean Acidification (HOT pH measurements)
- ✅ Created SRC-style radial visualization with gradient coloring
- ✅ Implemented proper CC BY-NC-ND 3.0 attribution
- ✅ Added all 9 boundary labels with connecting lines
- ✅ Created gradient risk zones (green→yellow→orange→red)
- ✅ Added interactive hover tooltips with boundary details
- ✅ Linked to existing temperature and pH visualizations
- ✅ Added 7 placeholder boundaries ready for future integration
- ✅ Updated GUI with new "Earth System" section
- ✅ Added green 🌍 Planetary Boundaries button
- ✅ Updated footer to "8 of 8 visualizations active"
- ✅ Full documentation and attribution added
- ✅ Educational context about framework significance

### Current Milestones (13 total)
1. ✅ Keeling Curve visualization (67-year CO₂ record)
2. ✅ Temperature anomaly visualization (145-year warming record)
3. ✅ Monthly temperature progression visualization
4. ✅ Warming stripes heatmap
5. ✅ Arctic ice visualization (47-year decline)
6. ✅ Sea level visualization (32-year rise)
7. ✅ Ocean pH visualization (32-year acidification)
8. ✅ **Planetary Boundaries framework integration** ⭐ NEW!
9. ✅ GUI update button (updates all 4 automated datasets)
10. ✅ Comprehensive fail-safe protection
11. ✅ NSIDC V3→V4 migration handled
12. ✅ NASA authentication documented
13. ✅ **All 8 visualizations operational!** 🎉

---

## The Roadmap

### **Phase 1: Keeling Curve** ✅ Done!
- `fetch_climate_data.py`
- `co2_mauna_loa_monthly.json`
- Visualization in hub

### **Phase 2: Temperature** ✅ Done!
- NASA GISS dataset
- Temperature anomaly visualization
- Monthly data and trend lines
- Monthly progression and warming stripes

### **Phase 3: Cryosphere** ✅ Done!
- Arctic sea ice extent
- NSIDC V4 Excel parsing
- September minimum visualization
- V3→V4 migration documented

### **Phase 4: Oceans** ✅ COMPLETE!
- **Sea Level Rise** ✅ COMPLETE
- **Ocean Acidification** ✅ COMPLETE

### **Phase 5: Earth System Integration** ✅ COMPLETE! ⭐
- **Planetary Boundaries Framework** ✅ COMPLETE
  - SRC-style radial visualization
  - 2/9 boundaries with live data
  - 7 placeholders for future integration
  - Proper attribution and licensing
  - Educational context included


### **Phase 6: Energy Imbalance (2005-2025)** ✅ COMPLETE! 🔥
**Status**: Working visualization with comprehensive annotations and context
**Date Completed**: November 10, 2025
**Goal**: Show the relationship between Earth's energy imbalance and temperature change

**What we're visualizing**:
- **Air Temperature** (NASA GISS): Surface atmospheric warming
- **Energy Imbalance** (calculated from NOAA ocean heat): Rate of energy accumulation (W/m²)
- **Ocean Heat Content** (NOAA 0-2000m): Cumulative energy storage (Zettajoules)
- **Polynomial Trend**: Shows acceleration in ocean heat accumulation
- **ENSO Events**: El Niño/La Niña context bands (8 events, 2006-2024)

**Key Features Implemented**:
1. **Dual Y-Axis Display**: Temperature (left) and Energy/Ocean Heat (right)
2. **Visual Integration**: Red/blue shading shows warming/cooling periods
3. **Polynomial Acceleration Trend**: Subtle dashed line showing "increasing at increasing rate"
4. **Scale Comparison Annotation**: 
   - Humanity's energy use: ~0.6 ZJ/yr
   - Ocean heat accumulation: ~1.2 ZJ/yr
   - Ocean absorbs ~2× human energy use!
5. **Pipeline Warming**: ~0.4°C committed warming from stored ocean heat
6. **Integration Baseline**: Shows 9.0 ZJ starting point (2005) and 23.8 ZJ accumulated over 20 years
7. **Instantaneous Rate Display**: 0.95→0.97 ZJ/yr (calculated at mid-decade intervals)
8. **ENSO Event Bands**: Orange (El Niño) and Blue (La Niña) background bands with labels
9. **Climate Events**: Paris Agreement (2015) annotation
10. **Organized Legend**: Grouped by "Measurements" and "Ocean Heat (0-2000m)"
11. **Clickable Citations**: Direct links to NASA GISS and NOAA NCEI data sources
12. **Educational Bottom Note**: Complete causal chain explanation

**The Conceptual Framework** (Resolved):
Initial logic chain:
1. Temperature is rising → What's the driver? → Energy imbalance
2. Earth receives more energy than it radiates → Excess accumulates
3. Where does it go? → 90% into oceans
4. Ocean heat content = time integral of Earth's energy imbalance

**The physics**:
- **Primary driver**: Greenhouse effect (CO₂, CH₄ trap outgoing radiation)
- **Primary sink**: Ocean (0-2000m absorbs ~90% of excess energy)
- **What we calculate**: Rate of ocean heat uptake (derivative of NOAA data)
- **Key insight**: Ocean heat uptake rate ≈ proxy for Earth's total energy imbalance (since ocean = 90% of budget)

**Current framing**: "Earth's Energy Imbalance & Temperature"
- Ocean heat uptake rate divided by Earth's total surface area
- This gives W/m² over entire planet (not just ocean area)
- Since ocean = 90% of Earth's energy budget, this approximates total imbalance
- ✅ Title accurately reflects the physics

**Technical implementation**:
- Data: NOAA NCEI ocean heat content (0-2000m, seasonal)
- Calculation: `np.gradient(ohc_data)` to get instantaneous rate of change
- Conversion: ZJ/year → W/m² over Earth's surface area
- Visualization: Dual y-axis (temperature left, energy/ocean heat right)
- Shading: Red = ocean warming periods, Blue = cooling periods
- Trend: 2nd order polynomial showing acceleration
- ENSO: Vertical bands from 2006-2024 with simplified labels

**What makes this compelling**:
Shows the **ocean as Earth's heat reservoir** - absorbing energy at twice the rate of all human energy use, creating lag between forcing and atmospheric response. The polynomial trend reveals acceleration: ocean heat is increasing at an increasing rate. The cumulative line (blue dotted) rising + stored heat = committed future warming as energy eventually releases to atmosphere.

**Open Issue**: 
- Early ENSO bands (2006-2008) not displaying despite being within data range (2005.17-2025.42)
- Later bands (2009-2024) display correctly
- Likely Plotly rendering issue with shapes near left edge - investigation ongoing
- **Key insight**: Ocean heat uptake rate ≈ proxy for Earth's total energy imbalance

**Current framing**: "Earth's Energy Imbalance & Temperature"
- Ocean heat uptake rate divided by Earth's total surface area
- This gives W/m² over entire planet (not just ocean area)
- Since ocean = 90% of Earth's energy budget, this approximates total imbalance

**Open questions for tomorrow's discussion**:
1. Is "Earth's Energy Imbalance" accurate if we're only measuring ocean component?
2. Should we clarify "from ocean heat uptake" in the trace name?
3. How do we best explain the relationship: greenhouse forcing → energy imbalance → ocean storage + atmospheric warming?

**Technical implementation**:
- Data: NOAA NCEI ocean heat content (0-2000m, seasonal)
- Calculation: `np.gradient(ohc_data)` to get rate of change
- Conversion: ZJ/year → W/m² over Earth's surface area
- Visualization: Dual y-axis (temperature left, energy right)
- Shading: Red = ocean warming periods, Blue = cooling periods

**What makes this interesting**:
Shows the **ocean as Earth's thermal battery** - absorbing energy and creating lag between forcing and atmospheric response. The blue dotted line (cumulative heat) rising = committed future warming as stored energy eventually releases.

**Files**:
- `paleoclimate_energy_imbalance.py` - Working visualization
- Data source: `data/ohc2000m_levitus_climdash_seasonal.csv` (to be acquired)

### **Phase 7: Enhancement** (Future)
- Complete the Energy Imbalance conceptual framework
- Expand Planetary Boundaries with additional data:
  - CO₂ concentration boundary
  - Biodiversity/extinction data (Biosphere Integrity)
  - Land use data (Land-System Change)
  - Freshwater consumption data
  - Nitrogen/Phosphorus flows
- Additional climate datasets (glacier mass, permafrost, atmospheric methane)
- Historical data exploration tools
- Export/sharing features
- Animation capabilities
- Automated update checking for manual datasets
- Mobile-responsive design

---

## Summary

**Current Status: 8 of 8 Visualizations Working!**

This Earth System Visualization hub now provides:
- **5 individual climate indicators** with detailed time-series data
- **2 temperature visualization styles** (progression + stripes)
- **1 integrative framework** (Planetary Boundaries) showing holistic Earth system health
- **Automated updates** for 4 datasets
- **Manual workflows** for 2 datasets (with files included)
- **Comprehensive documentation** and proper attribution
- **Data preservation** ensuring climate records remain accessible

The system successfully combines detailed individual metrics with a holistic planetary view, making it both scientifically rigorous and educationally powerful.

**Next steps**: Consider adding more data sources to complete the Planetary Boundaries framework (7 boundaries remaining) or enhance existing visualizations with additional analysis tools.

==================

here is my indexing/(graphic hovertext)
green: 0 to 2.5 cm: 1.0
high-risk line: 4.0 cm: 1.6 (add  a circle here) 
ozone depletion: 1.2 cm: 0.48 (0.3)
aerosol loading: 2.0 cm: 0.80 (0.5)
ocean acidification: 2.6 cm: 1.04 (1.5)
freshwater change, blue and green water: 2.9 cm: 1.16 (0.72)
land system change: 3.65 cm: 1.46 (0.91)
co2: 3.6 cm: 1.44 (1.14)
radiative forcing: 6.4 cm: 2.56 (1.14)
biogeochemical flows, phosphorus: 5.35 cm: 2.14 (1.55)
nitrogen cycle: 7.05: 2.82 (1.55)
novel entities: 1.80 (1.2)
biosphere integrity, functional: 5.0 cm: 2.0 (1.25)
genetic diversity: not defined (1.25)
