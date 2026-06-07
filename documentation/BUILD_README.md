# Paloma's Orrery - PyInstaller Build Package

**Created:** November 26, 2025  
**Phase:** 1 - Core Solar System Executable

---

## Files Included

| File | Purpose |
|------|---------|
| `build_executable.bat` | **Start here!** Automated build script for Windows |
| `BUILD_GUIDE.txt` | Step-by-step manual commands if you prefer |
| `palomas_orrery.spec` | Advanced PyInstaller spec file (optional) |

---

## Quick Start

### Option A: Automated (Recommended)

1. Copy all three files to your project root (where `palomas_orrery.py` lives)
2. Open Command Prompt
3. Navigate to your project folder:
   ```
   cd C:\Users\YourName\path\to\palomas_orrery
   ```
4. Run:
   ```
   build_executable.bat
   ```
5. Wait 5-15 minutes for the build
6. Find your executable in `dist\palomas_orrery\`

### Option B: Manual Step-by-Step

Follow the commands in `BUILD_GUIDE.txt` to run PyInstaller manually.

---

## What Gets Built

```
dist/
└── palomas_orrery/
    ├── palomas_orrery.exe    # The main executable
    ├── _internal/            # Python runtime & libraries
    ├── data/                 # Your data files (copied by script)
    │   ├── orbit_paths.json
    │   ├── osculating_cache.json
    │   └── ... (climate data, etc.)
    ├── star_data/            # Stellar cache files (copied by script)
    │   ├── *.pkl
    │   └── *.vot
    └── reports/              # For generated outputs
```

---

## Expected Sizes

| Component | Size |
|-----------|------|
| Executable + dependencies | 200-400 MB |
| data/ folder | ~100 MB |
| star_data/ folder | ~330 MB |
| **Total (uncompressed)** | **600-900 MB** |
| **Zipped for distribution** | **200-400 MB** |

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'xxx'"

Add `--hidden-import=xxx` to the pyinstaller command in the batch file.

### "FileNotFoundError: data/orbit_paths.json"

The script copies your data folder automatically. If it wasn't copied:
```
xcopy /E /I data dist\palomas_orrery\data
```

### Blank window / GUI doesn't appear

CustomTkinter theme files may not have been collected properly. The batch file includes `--collect-data=customtkinter` which should handle this.

### Can't save plots as images (kaleido error)

Make sure `--collect-data=kaleido` is in the build command.

### Very slow first startup

Normal! PyInstaller extracts files on first run. Subsequent starts are faster.

### "DLL load failed"

Install Visual C++ Redistributable:
https://aka.ms/vs/17/release/vc_redist.x64.exe

---

## Phase 2 Preview

Once Phase 1 works reliably, we can:
- Add application icon
- Switch from console to windowed mode
- Optimize startup time
- Create an installer (NSIS or Inno Setup)
- Add version info and metadata

---

## Distribution

To share the executable:

1. Zip the entire `dist\palomas_orrery\` folder
2. Share the zip file
3. Recipients unzip and run `palomas_orrery.exe`

**Note:** Recipients may need Visual C++ Redistributable if they haven't installed it before.

---

## Questions?

If you hit issues, run the exe from command prompt to see error messages:
```
cd dist\palomas_orrery
palomas_orrery.exe
```

The console output will show exactly what's failing.
