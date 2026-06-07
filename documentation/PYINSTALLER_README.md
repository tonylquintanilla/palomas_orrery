# Paloma's Orrery - PyInstaller Build Guide

**Created:** November 26-29, 2025  
**Status:** Phase 2 Complete ✅  
**Result:** Combined distribution with two executables, launcher, and documentation

---

## Overview

This guide documents how to build Paloma's Orrery as standalone Windows executables using PyInstaller. The process was developed through iterative testing and troubleshooting via "vibe coding" with AI assistance.

### What Gets Built

**Combined distribution package:**

```
dist\palomas_orrery\
├── START_HERE.bat           ← Menu launcher
├── README.txt               ← User guide
├── palomas_orrery.exe       ← Solar system (~44 MB)
├── star_visualization.exe   ← Stars (~43 MB)
├── reports/                 ← Generated outputs
└── _internal/               ← Shared dependencies & data
    ├── data/                ← Orbit cache, climate data
    ├── star_data/           ← Stellar catalogs (ONE copy)
    └── ...                  ← Python runtime, DLLs
```

- **Input:** 75+ Python modules, ~15,000 lines of code
- **Output:** Single folder distribution with shared dependencies
- **Target:** Windows 10/11 (64-bit)
- **Total Size:** ~500-600 MB (uncompressed)

### Why Two Executables?

The Star Visualization GUI uses a separate tkinter root window which conflicts with the main orrery when run in the same process. Separating them provides:
- Clean, independent operation
- No GUI conflicts or freezing
- Each can be run standalone
- Simpler troubleshooting
- Shared `_internal` folder saves ~330 MB vs separate distributions

---

## Prerequisites

- **Python 3.11-3.13** (tested with 3.13)
- **All requirements.txt packages installed**
- **PyInstaller 6.x** (`pip install pyinstaller`)

### Optional Files (in project root):
- `palomas_orrery_logo_enhanced_ico.ico` - Custom application icon
- `version_info_orrery.txt` - Executable metadata (main orrery)
- `version_info_stars.txt` - Executable metadata (star visualization)
- `Palomas_Orrery_Launcher.bat` - Menu launcher (copied as START_HERE.bat)
- `README_DISTRIBUTION.txt` - User guide (copied as README.txt)

---

## Quick Start

### Build Process (Two Steps)

From your project root (where `palomas_orrery.py` lives):

```cmd
REM Step 1: Build main orrery (10-15 minutes)
build_executable_v3.bat

REM Step 2: Build star visualization + finalize distribution (5-10 minutes)
build_star_visualization.bat
```

**Important:** Run in this order! Step 2 requires Step 1 to complete first.

### Test the Distribution

```cmd
cd dist\palomas_orrery
START_HERE.bat
```

Or run executables directly:
```cmd
palomas_orrery.exe
star_visualization.exe
```

---

## Build Files Required

Copy these files to your project root before building:

| File | Purpose |
|------|---------|
| `build_executable_v3.bat` | Builds main orrery |
| `build_star_visualization.bat` | Builds stars + adds launcher/README |
| `palomas_orrery_logo_enhanced_ico.ico` | Custom icon (optional) |
| `version_info_orrery.txt` | Exe metadata (optional) |
| `version_info_stars.txt` | Exe metadata (optional) |
| `Palomas_Orrery_Launcher.bat` | Menu launcher |
| `README_DISTRIBUTION.txt` | User guide for distribution |

---

## What the Build Scripts Do

### build_executable_v3.bat (Run First)

1. Checks Python installation
2. Cleans previous build artifacts
3. Runs PyInstaller with all hidden imports and data collection
4. Copies `data/` folder to `_internal/`
5. Copies `star_data/` folder to `_internal/`
6. Creates `reports/` folder in `_internal/`
7. Copies astroquery CITATION file

### build_star_visualization.bat (Run Second)

1. Verifies main orrery was built first
2. Builds star_visualization.exe to temporary location
3. Copies exe to `dist\palomas_orrery\`
4. Merges any unique files into shared `_internal/`
5. Cleans up temporary build folder
6. Copies `START_HERE.bat` launcher
7. Copies `README.txt` user guide

---

## Final Distribution Structure

```
dist\palomas_orrery\
├── START_HERE.bat              ← Menu launcher (users start here)
├── README.txt                  ← User guide
├── palomas_orrery.exe          ← Main orrery (44 MB)
├── star_visualization.exe      ← Star visualization (43 MB)
├── reports/                    ← Generated outputs (created on first use)
└── _internal/
    ├── astroquery/
    │   └── CITATION
    ├── data/                   ← Solar system data
    │   ├── orbit_paths.json    ← Orbit cache (~94 MB)
    │   ├── osculating_cache.json
    │   ├── co2_mauna_loa_monthly.json
    │   ├── temperature_giss_monthly.json
    │   ├── arctic_ice_extent_monthly.json
    │   ├── sea_level_gmsl_monthly.json
    │   ├── epica_co2_800kyr.json
    │   ├── lr04_benthic_stack.json
    │   └── ... (other climate/paleo data)
    ├── star_data/              ← Stellar catalogs (ONE shared copy)
    │   ├── star_properties_distance.pkl
    │   ├── star_properties_magnitude.pkl
    │   ├── hipparcos_*.vot
    │   ├── gaia_*.vot
    │   └── *_metadata.json
    └── ... (Python runtime, DLLs, packages)
```

---

## Features by Executable

### palomas_orrery.exe

- ✅ Solar system visualization (planets, moons, asteroids)
- ✅ Spacecraft and mission trajectories
- ✅ Comet visualization with dual ion/dust tails
- ✅ Exoplanet systems with habitable zones
- ✅ Animations (days, weeks, months, years)
- ✅ Earth System Visualization GUI (climate data)
- ✅ Orbital Parameter Visualization GUI
- ✅ Pluto-Charon barycenter mode
- ✅ JPL Horizons live data fetching
- ✅ Keplerian orbit overlays with apsidal markers
- ✅ Paleoclimate data (EPICA, LR04, Temp12k, Phanerozoic)

### star_visualization.exe

- ✅ 3D stellar neighborhood (up to 100 light-years)
- ✅ 2D Hertzsprung-Russell diagrams (distance and magnitude modes)
- ✅ Star search by name, distance, or magnitude
- ✅ 123,000+ stars from Hipparcos and Gaia catalogs
- ✅ Notable star descriptions and astronomical notes
- ✅ Planetarium-style visualizations
- ✅ Spectral classification display

---

## START_HERE.bat Launcher

The launcher provides a text-based menu:

```
  ============================================================

     PALOMA'S ORRERY - Version 1.0.0
     Created by Tony Quintanilla for Paloma

     "Data Preservation is Climate Action"

  ============================================================

     [1]  SOLAR SYSTEM ORRERY
     [2]  STAR VISUALIZATION
     [3]  OPEN DOCUMENTATION
     [4]  EXIT

  ============================================================
```

Users select an option (1-4) and the appropriate executable launches.

---

## Troubleshooting

### Issue: Plotting buttons spawn new GUI windows instead of creating plots

**Cause:** In frozen executables, `sys.executable` points to the `.exe` file, not Python. When code uses `subprocess.run([sys.executable, 'script.py', ...])`, it launches another instance of the exe instead of running the script.

**Solution (implemented in Phase 2):**
1. Detect frozen state with `is_frozen()` helper
2. Import plotting modules directly when frozen
3. Call `module.main()` with `sys.argv` manipulation instead of subprocess
4. Use `__file__` for working directory (same as main orrery)

**Code pattern:**
```python
def is_frozen():
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

if is_frozen() and PLOTTING_MODULES_AVAILABLE:
    old_argv = sys.argv
    sys.argv = ['script.py', str(value)]
    try:
        module_name.main()
    finally:
        sys.argv = old_argv
else:
    subprocess.run([sys.executable, script_path, str(value)])
```

### Issue: `FileNotFoundError: astroquery\CITATION`

**Cause:** PyInstaller didn't bundle the CITATION file.

**Solution:** Build scripts now handle this automatically. If manual fix needed:
```cmd
mkdir dist\palomas_orrery\_internal\astroquery
copy "PATH_TO_SITE_PACKAGES\astroquery\CITATION" dist\palomas_orrery\_internal\astroquery\
```

### Issue: `FileNotFoundError: data/orbit_paths.json`

**Cause:** Working directory is `_internal/`, but data folder was placed alongside the exe.

**Solution:** Build scripts now copy data INTO `_internal/`. This is handled automatically.

### Issue: `ModuleNotFoundError: No module named 'xxx'`

**Cause:** PyInstaller missed a dynamically imported module.

**Solution:** Add to the build command:
```cmd
--hidden-import=xxx
```

### Issue: "Access is denied" during build

**Cause:** Previous executable is still running or files are locked.

**Solution:** 
1. Close any running executables
2. Check Task Manager for `palomas_orrery.exe` or `star_visualization.exe`
3. If needed, restart computer to release file locks

### Issue: Blank GUI window / CustomTkinter not rendering

**Cause:** CustomTkinter theme assets not bundled.

**Solution:** Ensure this is in the build command:
```cmd
--collect-data=customtkinter
```

### Issue: Can't save plots as images (kaleido error)

**Cause:** Kaleido executable/assets not bundled.

**Solution:** Ensure this is in the build command:
```cmd
--collect-data=kaleido
```

### Issue: Very slow first startup

**Cause:** Normal PyInstaller behavior - extracts/loads files on first run.

**Solution:** Subsequent runs are faster. No fix needed.

### Issue: "DLL load failed"

**Cause:** Missing Visual C++ Redistributable on target machine.

**Solution:** Install from: https://aka.ms/vs/17/release/vc_redist.x64.exe

### Issue: "Windows protected your PC" warning

**Cause:** Executable is not code-signed.

**Solution:** Click "More info" → "Run anyway". This is normal for unsigned applications.

---

## Hidden Imports Explained

PyInstaller analyzes static imports but misses dynamically loaded modules:

| Hidden Import | Why Needed |
|---------------|------------|
| `astropy.units.format.*` | Loaded dynamically based on unit format |
| `astropy.coordinates.builtin_frames` | Loaded when coordinate transforms requested |
| `astropy.time.formats` | Time format handlers loaded on demand |
| `erfa`, `erfa.ufunc` | ERFA library for astronomical calculations |
| `astroquery.*` | Query modules loaded based on data source |
| `keyring`, `keyring.backends` | Used by astroquery for credential storage |
| `plotly.validators.*` | Validators loaded per trace type |
| `plotly.graph_objs` | Graph object constructors |
| `kaleido.scopes.plotly` | Plotly rendering scope for static export |
| `customtkinter` | Modern tkinter widgets |
| `darkdetect` | OS theme detection for customtkinter |
| `scipy.special._ufuncs_cxx` | C++ ufuncs loaded at runtime |
| `PIL._tkinter_finder` | Pillow's tkinter integration |

---

## Collect Data Explained

Some packages include non-Python files that must be explicitly bundled:

| Package | What's Collected |
|---------|------------------|
| `customtkinter` | Theme JSON files, widget assets |
| `plotly` | Plot templates, colorscales |
| `kaleido` | Chromium-based rendering executable |
| `astropy` | IERS data tables, unit definitions |
| `astroquery` | CITATION file, query templates |

---

## Size Breakdown

| Component | Approximate Size |
|-----------|------------------|
| `palomas_orrery.exe` | 44 MB |
| `star_visualization.exe` | 43 MB |
| `_internal/` (shared) | 350-400 MB |
| `data/` folder | 100 MB |
| `star_data/` folder | 330 MB |
| **Total (combined distribution)** | **~500-600 MB uncompressed** |
| **Zipped for distribution** | **~250-350 MB** |

**Note:** Combined distribution saves ~330 MB by sharing `star_data/` instead of duplicating it.

---

## Distribution

To share the application:

1. Zip the entire `dist\palomas_orrery\` folder
2. Name it `Palomas_Orrery_v1.0.0.zip` (or similar)
3. Share the zip file
4. Recipients unzip and run `START_HERE.bat`

**Note:** Recipients may need Visual C++ Redistributable if not already installed.

---

## Data Files: Python vs Executable

The Python source and executables use **separate data copies**:

| Location | Used By |
|----------|---------|
| `palomas_orrery/data/` | Python development (`python palomas_orrery.py`) |
| `palomas_orrery/star_data/` | Python development |
| `dist/palomas_orrery/_internal/data/` | Executable (both apps) |
| `dist/palomas_orrery/_internal/star_data/` | Executable (both apps) |

**Important:** When you rebuild, the batch scripts copy fresh data from your development folders into `_internal/`. Any data changes made while running the executable will be overwritten on rebuild.

---

## Single Codebase: No Fork Required

The PyInstaller-compatible code works identically for both Python and executable deployment. **You don't need separate codebases.**

### How It Works

The `is_frozen()` pattern detects the runtime environment:

```python
def is_frozen():
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

if is_frozen():
    # Exe mode: call module.main() directly
else:
    # Python mode: use subprocess (original behavior)
```

### Runtime Behavior

| Running as... | `is_frozen()` | Behavior |
|---------------|---------------|----------|
| `python star_visualization_gui.py` | `False` | Uses subprocess (original) |
| `star_visualization.exe` | `True` | Uses direct module calls |

### Key Compatibility Patterns

1. **Working directory resolution** (works for both):
   ```python
   script_dir = os.path.dirname(os.path.abspath(__file__))
   os.chdir(script_dir)
   ```

2. **Conditional imports** (only loads when frozen):
   ```python
   if is_frozen():
       import hr_diagram_distance
       # ... other plotting modules
   ```

3. **Conditional execution** (subprocess vs direct call):
   ```python
   if is_frozen() and PLOTTING_MODULES_AVAILABLE:
       old_argv = sys.argv
       sys.argv = ['script.py', str(value)]
       try:
           module_name.main()
       finally:
           sys.argv = old_argv
   else:
       subprocess.run([sys.executable, script_path, str(value)])
   ```

### Benefits

- ✅ **One codebase** - no maintenance of separate forks
- ✅ **No breaking changes** - Python behavior unchanged
- ✅ **Runtime detection** - automatically adapts to environment
- ✅ **Easy testing** - develop in Python, deploy as exe

---

## Phase 2 Complete ✅

### Phase 1 (Nov 26-28):
- [x] Working `palomas_orrery.exe` with all features
- [x] Working `star_visualization.exe` with all features
- [x] Custom application icon
- [x] Version info and metadata (right-click → Properties → Details)
- [x] Combined distribution with shared `_internal/`
- [x] Menu launcher (`START_HERE.bat`)
- [x] User documentation (`README.txt`)
- [x] Automated build scripts

### Phase 2 (Nov 29):
- [x] Fixed subprocess issue in frozen exe (plotting buttons spawning new GUIs)
- [x] Added PyInstaller detection with `is_frozen()` helper
- [x] Direct module imports for plotting when frozen (hr_diagram_*, planetarium_*)
- [x] Fixed working directory resolution using `__file__` (same pattern as main orrery)
- [x] Fixed `star_data/` path references throughout star_visualization_gui.py
- [x] Added `multiprocessing.freeze_support()` for frozen exe compatibility

### Phase 3 Improvements (Future):
- [ ] Switch from console to windowed mode (`--noconsole`)
- [ ] Create proper Windows installer (NSIS or Inno Setup)
- [ ] Code signing certificate (removes "Windows protected your PC" warning)
- [ ] Optimize startup time
- [ ] Auto-update mechanism for data files
- [ ] Mac build for Paloma (requires building on Mac hardware)

---

## Python Launcher Scripts

For developers running from Python source, two launcher scripts are available:

- `run_palomas_orrery.bat` - Launches main GUI from Python
- `run_star_visualization.bat` - Launches star GUI from Python

These check for Python installation, display version info, and provide helpful error messages.

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-26 | 1.0 | Initial working build of palomas_orrery.exe |
| 2025-11-27 | 1.1 | Added star_visualization.exe as separate executable |
| 2025-11-27 | 1.2 | Documented both build scripts and distribution options |
| 2025-11-27 | 1.3 | Added custom icon support |
| 2025-11-28 | 1.4 | Added version info/metadata for exe properties |
| 2025-11-28 | 2.0 | **Combined distribution** - both exes share one `_internal/` folder |
| 2025-11-28 | 2.1 | Added START_HERE.bat launcher and README.txt |
| 2025-11-29 | 2.2 | **Phase 2** - Fixed frozen exe subprocess/path issues, direct module calls |

---

## Acknowledgments

- **PyInstaller Team** - Making Python executables possible
- **Anthropic Claude** - AI partner for architecture, coding, debugging, batch script development, documentation, and iterative problem-solving (this is a "vibe coding" project!)
- **NASA JPL Horizons** - Ephemeris and astronomical data
- **ESA Gaia/Hipparcos** - Stellar catalogs
- **NOAA, NASA GISS, NSIDC, BCO-DMO** - Climate data sources

---

## Project Philosophy

**"Data Preservation is Climate Action"**

Every dataset cached in this application is insurance against potential loss of access to critical scientific information. The orrery preserves astronomical ephemerides, stellar catalogs, and climate records spanning from real-time measurements to 800,000-year ice cores.

---

*"From 75+ Python modules to a beautiful standalone distribution!"*

*"The sky's the limit! Or the stars are the limit!"* ⭐🚀
