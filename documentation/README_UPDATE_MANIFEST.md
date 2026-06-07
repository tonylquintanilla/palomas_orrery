# README.md Update Manifest

**Date:** December 8, 2025  
**Version:** v1.5 (TNO Satellites & Analytical Fallback)

---

## Summary

Updated README.md from November 26, 2025 to December 8, 2025 with:
- New TNO satellite features
- Fixed encoding issues throughout
- Corrected module references
- Removed obsolete modules
- Added missing cache manager
- Updated statistics

---

## Changes by Category

### 1. DATE UPDATES

| Location | Old | New |
|----------|-----|-----|
| Line 1 | November 26, 2025 | December 8, 2025 |
| Last Updated (footer) | November 2025 (v1.3) | December 2025 (v1.5) |

### 2. ENCODING FIXES

Fixed corrupted Unicode characters throughout:

| Line | Old (Corrupted) | New (Fixed) |
|------|-----------------|-------------|
| ~71 | `Ã¢â€ â€œ` | `↓` |
| ~98 | `Ã¢â€ â€™` | `→` |
| ~151 | `Ã¢â€ â€™` | `→` |
| ~594 | `Ã‚Â°` | `°` |
| Various | `Ã¢Å"â€¦` | `✓` |
| Various | `Câ‚‚` | `C₂` |
| Various | `COâ‚‚` | `CO₂` |

### 3. NEW FEATURES ADDED

**Key Capabilities section - added:**
```markdown
- TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2)
```

**Advanced Features - added:**
```markdown
- **TNO-centered:** View Eris, Haumea, or Makemake with their moons
```

**Solar System Visualization table - updated:**
- Reference Frames: Added "TNO-centered views"
- Orbit Calculation: Changed to "using osculating elements"

**New subsection added - TNO Satellite Systems:**
```markdown
**TNO Satellite Systems:**

- **Eris/Dysnomia:** Distant dwarf planet with its moon (JPL ephemeris)
- **Haumea/Hi'iaka/Namaka:** Elongated dwarf planet with two moons (JPL ephemeris)
- **Makemake/MK2:** Dwarf planet with dark, recently-discovered moon (analytical orbit from 2025 Hubble analysis - no JPL ephemeris yet!)
- **View modes:** See satellites from heliocentric or TNO-centered perspectives
- **Analytical fallback:** Objects without JPL data calculated from published orbital elements
```

**Educational Tools table - added:**
```markdown
| **TNO Satellite Systems** | Visualize distant dwarf planet moons, including MK2 using cutting-edge 2025 Hubble orbital analysis |
```

**Data Sources - added:**
```markdown
- [arXiv preprints](https://arxiv.org/) - Latest orbital solutions for newly-discovered objects
```

**Architecture - Performance Optimizations - added:**
```markdown
- **Analytical fallback:** Calculate orbits locally when API data unavailable
```

### 4. MODULE REFERENCE CORRECTIONS

**Removed non-existent modules:**

| Old (Incorrect) | Status |
|-----------------|--------|
| `gui_main.py` | Never existed - functionality is in palomas_orrery.py |
| `planetary_shells.py` | Never existed - there are 12 individual shell modules |
| `refined_orbits.py` | Obsolete - superseded by osculating approach |

**Updated module descriptions:**

| Module | Old Description | New Description |
|--------|-----------------|-----------------|
| `palomas_orrery.py` | "Main application launcher and entry point" | "Main application (~420KB, 8,700+ lines) - GUI, plot_objects(), animate_objects()" |
| `idealized_orbits.py` | "Simplified circular/elliptical orbits" | "Core orbit visualization - Keplerian calculations, osculating elements, TNO satellites, analytical fallback" |
| `*_visualization_shells.py` | Listed as single `planetary_shells.py` | "Planetary interior cross-sections (12 modules)" |

**Added missing modules:**

| Module | Purpose |
|--------|---------|
| `osculating_cache_manager.py` | Osculating elements cache with center-body aware keys |
| `orbital_elements.py` | Orbital parameters, parent_planets dictionary, TNO moon elements |
| `apsidal_markers.py` | Perihelion/aphelion markers with perturbation analysis |

**Module count corrected:**
- Old: 79 Python modules
- New: 81 Python modules

### 5. DATA FILES UPDATES

**Added osculating_cache.json documentation:**
```markdown
**osculating_cache.json**

- JPL Horizons orbital elements (a, e, i, ω, Ω, TP) for 40+ objects
- Epoch tracking and per-object refresh intervals
- Center-body aware keys for barycenter views
```

**Cache File Sizes table - added:**
```markdown
| Osculating cache | <1 MB | Orbital elements |
```

### 6. STRUCTURAL IMPROVEMENTS

**Orbital Calculations section reorganized:**

Old structure (incorrect):
```
- idealized_orbits.py - Simplified circular/elliptical orbits
- refined_orbits.py - High-precision orbital mechanics  ← OBSOLETE
- orrery_integration.py
- create_ephemeris_database.py
```

New structure (correct):
```
- idealized_orbits.py - Core orbit visualization (full description)
- orbital_elements.py - Orbital parameters, parent_planets
- orrery_integration.py
- apsidal_markers.py - Perihelion/aphelion markers
```

**Removed `create_ephemeris_database.py`** from primary listing (it's a utility script, not core orbital calculations)

### 7. CONSISTENCY FIXES

- Changed "CO2" references to proper subscript "CO₂"
- Changed degree symbols from corrupted encoding to proper "°"
- Fixed arrow symbols throughout installation guide
- Standardized checkbox symbols

---

## Files Referenced

| Document | Status |
|----------|--------|
| `MODULE_INDEX.md` | Referenced, count updated to 81 |
| `climate_readme.md` | Referenced (unchanged) |
| `exoplanet_readme.md` | Referenced (unchanged) |
| `palomas_orrery_flowchart_v15_vertical.md` | New flowchart version |

---

## Validation Checklist

- [x] All dates updated to December 8, 2025
- [x] Version updated to v1.5
- [x] TNO satellite systems documented
- [x] Analytical fallback mentioned
- [x] Encoding issues fixed
- [x] Non-existent modules removed (gui_main.py, planetary_shells.py)
- [x] Obsolete modules removed (refined_orbits.py)
- [x] Missing modules added (osculating_cache_manager.py, orbital_elements.py, apsidal_markers.py)
- [x] Module count corrected (79 → 81)
- [x] osculating_cache.json documented
- [x] Style maintained (non-verbose, table-based)
- [x] No new sections beyond what was needed
- [x] arXiv added as data source

---

## Line Count Comparison

| Metric | Old | New | Change |
|--------|-----|-----|--------|
| Total lines | 913 | ~920 | +7 |
| New content lines | - | ~40 | TNO features |
| Removed lines | - | ~25 | Obsolete modules, encoding artifacts |
| Net change | - | ~15 | Minimal growth |

---

*Manifest prepared by Claude for Tony's Paloma's Orrery project*  
*December 8, 2025*
