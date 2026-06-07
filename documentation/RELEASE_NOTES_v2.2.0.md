# Release Notes v2.2.0

**Paloma's Orrery v2.2.0 - January 10, 2026**

This release adds significant new features, cross-platform support, and quality-of-life improvements.

---

## New Features

### Galactic Center Visualization (Sagittarius A*)
- **S-Star visualization:** Watch stars orbit the 4-million solar mass black hole at speeds up to 8% the speed of light
- **The Fantastic Four:** S2, S62, S4711, S4714 - stars with the most extreme orbits in our galaxy
- **Relativistic precession:** See Einstein's General Relativity in action - rosette patterns from Schwarzschild precession
- **Newton vs Einstein mode:** Visual comparison showing how orbits differ between classical and relativistic physics
- **Observational fidelity:** Orbital phases calculated from actual periapsis measurements (GRAVITY Collaboration)
- **Unified colorscale:** Compare precession rates visually across different stars
- **Five new modules:** sgr_a_star_data.py, sgr_a_visualization_core.py, sgr_a_visualization_animation.py, sgr_a_visualization_precession.py, sgr_a_grand_tour.py

### Orcus-Vanth Binary System
- **New barycenter mode:** View both Orcus and Vanth orbiting their common center of mass
- **Highest mass ratio:** Orcus-Vanth has the highest mass ratio (16%) of any known dwarf planet system - even higher than Pluto-Charon!
- **The "Anti-Pluto":** Orcus is a plutino 180° out of phase with Pluto in its orbit
- **ALMA 2016 data:** Binary orbit parameters from Brown & Butler 2023 (Planetary Science Journal)

### Unified Save System
- **Three save options:** CDN HTML (~10 KB), Offline HTML (~5 MB), or PNG image
- **Session memory:** Remembers your last save directory within each session
- **17 modules unified:** Consistent save experience across all visualizations
- **Cross-platform dialogs:** Works correctly on Windows, macOS, and Linux

---

## Cross-Platform Support

### Linux Support (NEW)
- Tested and verified on Linux Mint (Ubuntu/Debian-based)
- Cross-platform color fix: SystemButtonFace → gray90 for Linux compatibility
- New launcher: `start_orrery.desktop` for double-click launching
- New updater: `update_code.desktop` for easy code updates
- Documentation updated with Linux installation instructions

### macOS Improvements
- Thread safety fixes for Tkinter GUI updates
- Mousewheel scrolling fixed (delta detection for macOS vs Windows)
- Save dialog handling improved for worker thread contexts

### New Launcher & Updater Scripts
- `START_HERE.bat` (Windows launcher)
- `start_orrery.command` (macOS launcher)
- `start_orrery.desktop` (Linux launcher)
- `UPDATE_CODE.bat` (Windows updater)
- `update_code.sh` (macOS/Linux updater script)
- `update_code.desktop` (Linux updater launcher)

All scripts include safety checks to prevent running from wrong directory.

---

## Documentation Updates

- README moved to root folder for standard Python project structure
- requirements.txt moved to root folder
- Comprehensive "Staying Up to Date" section with update scripts
- Linux installation instructions for Ubuntu/Debian, Fedora, and Arch
- Galactic Center module documentation
- Module index updated with new save utilities

---

## Downloads

- `palomas_orrery_2_2_zip.zip` - Python source + data files (Windows, macOS, Linux)

**Executables (separate downloads):**
- Windows executable: Available from Google Drive
- macOS executable: Available from [Tony's webpage](https://sites.google.com/view/tony-quintanilla) (iCloud link)

---

## Technical Notes

- Python 3.11-3.13 supported
- gray90 color used universally for cross-platform GUI compatibility
- Update scripts use `git reset --hard origin/main` for clean updates
- Data files (orbit cache, stellar catalogs) preserved during updates

---

**Full Changelog:** v2.1.0 (December 18, 2025) → v2.2.0 (January 10, 2026)

Tony Quintanilla | tonyquintanilla@gmail.com
