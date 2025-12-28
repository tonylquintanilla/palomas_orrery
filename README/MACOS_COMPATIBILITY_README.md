# macOS Compatibility README

## Paloma's Orrery | Cross-Platform Support

**Date:** December 27, 2025
**Status:** Fully functional - Python source AND standalone executable

---

## Summary

Paloma's Orrery was originally developed on Windows 10/11 with Python 3.12. As of December 27, 2025, the application runs natively on macOS both as Python source code and as a standalone PyInstaller executable.

**Milestone:** First successful macOS executable build - December 27, 2025

---

## Distribution Options

### Option 1: Standalone Executable (No Python Required)

Download `Palomas_Orrery_v1.0.0_macOS.zip` from the GitHub releases page. Includes:
- `palomas_orrery` - Solar system visualization
- `star_visualization` - Stellar neighborhood viewer
- `start_orrery.command` - Menu launcher (double-click to run)
- All required dependencies bundled

**First launch:** Right-click -> Open -> Open (to bypass Gatekeeper)

### Option 2: Python Source Code

Clone the repository and run with Python 3.11+:
```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
pip3 install -r requirements.txt
python3 palomas_orrery.py
```

---

## Files Modified for Cross-Platform Support

| File | Changes |
|------|---------|
| `palomas_orrery.py` | Platform-aware mousewheel, threading fixes, Unicode->ASCII |
| `apsidal_markers.py` | Unicode->ASCII fixes |
| `shutdown_handler.py` | macOS thread safety for save dialogs |
| `palomas_orrery_helpers.py` | macOS thread safety for animation save dialogs |

---

## Issues Fixed

### 1. Mousewheel Scrolling (Middle Column)

**Problem:** macOS returns delta of +/-1 for scroll events; Windows returns +/-120. The original code divided by 120, making macOS scroll 120x slower (effectively not scrolling).

**Solution:** Platform detection in `_on_mousewheel()` functions:
```python
import platform
if platform.system() == 'Darwin':
    # macOS: delta is already small (+/-1 to +/-3)
    scroll_amount = -1 * (event.delta)
else:
    # Windows: delta is large (+/-120)
    scroll_amount = -1 * (event.delta // 120)
```

**Files:** `palomas_orrery.py` (lines ~1665 and ~3385)

---

### 2. Threading Crash on Plot/Animation

**Problem:** macOS Tkinter crashes with `NSInternalInconsistencyException` when GUI widgets are updated from background threads. Error: "NSWindow drag regions should only be invalidated on the Main Thread!"

**Solution A - GUI Updates:** Wrap widget updates in `root.after(0, lambda: ...)`:
```python
# Before (crashes on macOS)
output_label.config(text="Done")
progress_bar.stop()

# After (thread-safe)
root.after(0, lambda: output_label.config(text="Done"))
root.after(0, lambda: progress_bar.stop())
```

**Files:** `palomas_orrery.py` (lines ~5415-5423 and ~6907-6920)

**Solution B - Save Dialogs:** Skip Tk dialogs entirely when in worker thread on macOS:
```python
import threading
import platform

in_main_thread = threading.current_thread() is threading.main_thread()

if not in_main_thread and platform.system() == 'Darwin':
    # Show in browser, skip dialog
    webbrowser.open(f'file://{temp_path}')
    print("Save dialog skipped (macOS thread safety) - use File menu in browser to save")
    return
```

**Files:** `shutdown_handler.py` (lines ~91-102), `palomas_orrery_helpers.py` (lines ~844-857)

---

### 3. Unicode Character Corruption

**Problem:** Files with Unicode characters (arrows, degree symbols, checkmarks, etc.) get corrupted when processed through certain tools, displaying as `?` or `??`.

**Solution:** Replace Unicode with ASCII equivalents:

| Unicode | ASCII Replacement |
|---------|-------------------|
| -> (arrow) | `->` |
| degree symbol | ` deg` |
| checkmark | `OK:` or `[x]` |
| bullet | `-` |
| warning symbol | `WARNING:` |
| info symbol | `INFO:` |
| <= symbol | `<=` |
| Earth symbol | `Earth` |
| Sun symbol | `sun` |
| box drawing | `===` |

**Safe editing method:** Use Python binary mode to preserve line endings:
```python
with open(filename, 'rb') as f:
    content = f.read()
content = content.replace(b'old', b'new')
with open(filename, 'wb') as f:
    f.write(content)
```

---

## Known Limitations

### 1. No Save Dialog on macOS

**Behavior:** After plotting, users see "Save dialog skipped (macOS thread safety)" message instead of a save prompt.

**Workaround:** Use browser's File > Save As to save the HTML file. The file is self-contained and fully functional.

**Future fix:** Implement a "Save Plot" button in the GUI that runs on the main thread.

---

### 2. Complex Shell Animations Are Slow

**Behavior:** Animations with solar shells (thousands of mesh points) take much longer on macOS than Windows.

**Cause:** Older Mac hardware (tested on MacBookPro10,1 from 2012-2013) has significantly less CPU power than modern Windows machines.

**Workaround:** 
- Use static plots with shells (fast)
- Use simple animations without shells (fast)
- Avoid complex shell animations on older Macs

**Future fix:** Consider shell LOD (level of detail) reduction for animations.

---

### 3. Middle Column Scrollbar Invisible

**Behavior:** The scrollbar in the middle column doesn't appear visually on macOS, though mousewheel scrolling works.

**Cause:** macOS uses overlay scrollbars by default that only appear during active scrolling.

**Status:** Cosmetic only. Functionality is preserved.

---

### 4. Network Fetches Can Hang

**Behavior:** Animations requiring new JPL Horizons data can hang indefinitely if the network request doesn't complete.

**Cause:** No timeout on Horizons API calls. Rate limiting or network issues cause infinite wait.

**Workaround:** 
- Use cached objects that don't need updates
- Press Ctrl+C to kill hung process

**Future fix:** Add timeout to all Horizons fetch calls.

---

## PyInstaller Build

### Build Scripts

| Script | Purpose |
|--------|---------|
| `build_executable_macos.sh` | Builds main orrery executable |
| `build_star_visualization_macos.sh` | Builds star visualization (run second) |
| `start_orrery.command` | Menu launcher for distribution |

### Build Process

```bash
cd ~/path/to/palomas_orrery
chmod +x build_executable_macos.sh build_star_visualization_macos.sh
./build_executable_macos.sh      # 5-15 minutes
./build_star_visualization_macos.sh  # 5-10 minutes
```

### Distribution Structure

```
dist/palomas_orrery/
    palomas_orrery          # Unix executable (~45 MB)
    star_visualization      # Unix executable (~43 MB)
    start_orrery.command    # Menu launcher
    README.txt              # User guide
    _internal/              # Dependencies + data (~500 MB)
        data/               # Orbit cache, climate data
        star_data/          # Stellar catalogs
        reports/            # Output folder
```

### Gatekeeper Bypass

macOS shows a security warning for unsigned apps:

> "palomas_orrery" cannot be opened because the developer cannot be verified.

**To bypass (only needed once per executable):**
1. Right-click (or Control-click) the file
2. Choose "Open" from the context menu
3. Click "Open" in the dialog
4. The app launches and is remembered as safe

---

## Testing Checklist for macOS

- [x] GUI opens without errors
- [x] All three columns scroll with mousewheel
- [x] `plot_objects` completes without crash
- [x] `animate_objects` (simple) completes without crash
- [x] Shells display correctly in static plots
- [x] Earth-centered view with Moon works
- [x] Sun-centered view with planets works
- [x] Exoplanet systems display
- [x] No `??` characters in terminal output
- [x] PyInstaller executable launches cleanly
- [x] Star visualization executable works
- [x] Menu launcher opens both apps

---

## Platform Detection Reference

```python
import platform
import sys

# Operating system
platform.system()      # 'Darwin' (macOS), 'Windows', 'Linux'
platform.release()     # '19.6.0' (Catalina), '10' (Windows 10)
platform.machine()     # 'x86_64', 'arm64'

# Python
sys.version           # '3.12.0 (...)'
sys.platform          # 'darwin', 'win32', 'linux'

# Useful checks
is_macos = platform.system() == 'Darwin'
is_windows = platform.system() == 'Windows'
is_linux = platform.system() == 'Linux'
```

---

## Linux Compatibility (Untested)

The cross-platform code should work on Linux with minimal changes:
- Mousewheel behavior matches macOS (small deltas)
- Threading behavior similar to macOS (POSIX-based)
- May require: `sudo apt install python3-tk`

Linux has not been tested but the architecture supports it.

---

## Version History

| Date | Change |
|------|--------|
| 2025-12-27 | Initial macOS compatibility work |
| 2025-12-27 | Fixed mousewheel scrolling |
| 2025-12-27 | Fixed threading crashes |
| 2025-12-27 | Fixed Unicode corruption |
| 2025-12-27 | Documented known limitations |
| 2025-12-27 | **First successful PyInstaller build for macOS** |
| 2025-12-27 | Both executables launch cleanly from menu |

---

## Contributors

- Tony Quintanilla - Testing, requirements, validation, vision
- Claude (Anthropic) - Implementation, debugging, documentation

---

*Paloma's Orrery - Cross-platform astronomical visualization*

*"The sky's the limit! Or the stars are the limit!"*
