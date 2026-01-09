# Earth System Visualization - Climate Data Hub

**Data Preservation is Climate Action**

This system preserves and visualizes **critical climate indicators** from threatened data sources, now including an **integrated Planetary Boundaries framework** showing Earth system health holistically. All datasets are cached locally to ensure long-term availability regardless of institutional funding changes.

---

## Overview

The Earth System Visualization Hub provides interactive visualizations of critical climate measurements:

1. **The Keeling Curve** - Atmospheric CO2 (Mauna Loa Observatory, 1958-2025)
2. **Global Temperature Anomaly** - NASA GISS surface temperature (1880-2025)
3. **Monthly Temperature Progression** - Year-over-year comparison (1880-2025)
4. **Warming Stripes** - Ed Hawkins style heatmap (1880-2025)
5. **Arctic Sea Ice Extent** - NSIDC satellite observations (1979-2025)
6. **Global Sea Level Rise** - NASA sea surface height (1993-2025)
7. **Ocean Acidification** - Hawaii Ocean Time-series (1991-2023)
8. **Planetary Boundaries** - Stockholm Resilience Centre framework

### Current Status: [OK] 8 of 8 Working!

- [OK] **CO2**: 813+ records, automated fetch
- [OK] **Temperature**: 1,751+ records, automated fetch
- [OK] **Arctic Ice**: 561+ records, automated fetch
- [OK] **Sea Level**: 1,699 records, manual download (file included)
- [OK] **Ocean pH**: 257 records, manual download
- [OK] **Planetary Boundaries**: 2/9 boundaries with live data

---

## Recent Updates (December 2025)

### API Compatibility Fixes (v2.2.0)

The `climate_cache_manager.py` was updated to match `fetch_climate_data.py` function signatures:

**Fixed issues:**
1. `fetch_mauna_loa_co2()` - Returns records only (not a tuple)
2. `fetch_arctic_ice()` - Returns records only (not a tuple)  
3. `save_cache()` - Expects metadata function, not dict

**Before (broken):**
```python
co2_records, co2_metadata = fetch_climate_data.fetch_mauna_loa_co2()  # Wrong!
ice_records, ice_metadata = fetch_climate_data.fetch_arctic_sea_ice()  # Wrong function name!
save_cache(file, records, metadata_dict)  # Wrong parameter type!
```

**After (fixed):**
```python
co2_records = fetch_climate_data.fetch_mauna_loa_co2()  # Returns records only
ice_records = fetch_climate_data.fetch_arctic_ice()     # Correct function name
save_cache(file, records, create_metadata_func)         # Pass function, not dict
```

### Cross-Platform GUI Fixes

Button colors updated for macOS/Windows compatibility:
- Changed from dark backgrounds + white text to pastel backgrounds + black text
- Buttons grouped by section with consistent colors:
  - Update: Light green (#90EE90)
  - Atmosphere: Light coral (#FFB6A3)  
  - Paleoclimate: Burlywood (#DEB887)
  - Ocean/Ice: Sky blue (#87CEEB)
  - Systems: Pale green (#98FB98)

---

## Why This Matters

Critical climate monitoring infrastructure faces unprecedented threats:

- **Mauna Loa Observatory**: Lease expires August 2025, closure possible
- **NASA Earth Science**: 52% budget cuts proposed (FY2026)
- **NSIDC**: Downgraded to "Basic" service, reduced data processing
- **NOAA**: Budget uncertainty, service reductions

**This system ensures these irreplaceable datasets remain accessible** regardless of institutional changes.

---

## System Components

### Core Files

**1. `fetch_climate_data.py`**
**Climate data fetcher** - Downloads and caches datasets from NOAA, NASA, NSIDC

Key functions and return values:
- `fetch_mauna_loa_co2()` -> returns `records` (list)
- `fetch_nasa_giss_temperature()` -> returns `(records, metadata)` (tuple)
- `fetch_arctic_ice()` -> returns `records` (list)
- `save_cache(filename, records, metadata_func)` -> metadata_func is a callable

Features:
- Atomic writes with fail-safe protection
- Emergency backups on dangerous saves
- Auto-validates data integrity
- Handles format migrations (V3->V4)
- User-Agent headers for blocked servers

**2. `earth_system_visualization_gui.py`**
**Interactive visualization hub** - 8 Plotly visualizations with update button
- Cross-platform button styling (pastel colors + black text)
- "Update Climate Data" button (updates 3 automated datasets)

**3. `climate_cache_manager.py`**
**Data updater** - Manages updates from GUI
- Calls fetch_climate_data functions with correct signatures
- Validates downloaded data (file sizes, record counts)
- Reports detailed success/failure status

**Important**: This file must match the API signatures in fetch_climate_data.py. If you modify fetch functions, update climate_cache_manager.py accordingly.

---

## Quick Start

### Initial Setup

**1. Install dependencies:**
```bash
pip install plotly numpy openpyxl scipy requests
```

**2. Fetch automated data (CO2, Temperature, Arctic Ice):**
```bash
python fetch_climate_data.py
```

**Expected output:**
- CO2: ~813 records, latest ~426 ppm
- Temperature: ~1751 records, latest ~+1.22 deg C
- Arctic Ice: ~561 records (47 years x 12 months)

**3. Test the GUI update button:**
```bash
python earth_system_visualization_gui.py
```
Click "Update Climate Data" - should show:
```
[OK] CO2: SUCCESS - 813 records
[OK] TEMPERATURE: SUCCESS - 1751 records  
[OK] ICE: SUCCESS - 561 records
```

---

## Troubleshooting

### "too many values to unpack" Error

This means `climate_cache_manager.py` is out of sync with `fetch_climate_data.py`.

**Solution**: Use the updated `climate_cache_manager.py` from v2.2.0 which has correct API calls.

### "'dict' object is not callable" Error

The `save_cache()` function expects a metadata function, not a dictionary.

**Wrong:**
```python
save_cache(file, records, {'source': 'NOAA'})
```

**Right:**
```python
save_cache(file, records, create_co2_metadata)  # Pass the function itself
# Or for inline:
save_cache(file, records, lambda r: {'source': 'NOAA', 'records': len(r)})
```

### "fetch_arctic_sea_ice" AttributeError

The function was renamed. Use `fetch_arctic_ice()` (not `fetch_arctic_sea_ice`).

---
