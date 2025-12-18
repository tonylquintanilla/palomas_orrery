# MODULE_INDEX.md Update Document

**Date:** December 8, 2025  
**Based on:** Flowchart v15 architecture

---

## Summary of Changes Needed

| Line(s) | Current | Update To |
|---------|---------|-----------|
| 4 | November 26, 2025 | December 8, 2025 |
| 32 | 8,289 lines | 8,700+ lines |
| 72 | Basic description | Add `get_cache_key()`, center-body awareness |
| 148 | Basic description | Add TNO satellites, MK2 analytical params |
| 150 | Missing TNO/fallback | Add `plot_tno_satellite_orbit()`, `ANALYTICAL_FALLBACK` |
| 157-158 | Basic description | Add center-body keys, `get_cache_key()` |
| 376 | `refined_orbits.py` | `idealized_orbits.py` (refined is obsolete) |
| 392, 420 | flowchart v13 | flowchart v15 |
| 425 | November 26, 2025 | December 8, 2025 |

---

## 1. UPDATE HEADER (Line 4)

**Replace:**
```
**Last Updated:** November 26, 2025
```

**With:**
```
**Last Updated:** December 8, 2025
```

---

## 2. UPDATE CORE APPLICATION - palomas_orrery.py (Line 32)

**Replace:**
```
| `palomas_orrery.py` | **Primary GUI and solar system visualization engine** (404KB, 8,289 lines). Main application with three-column tkinter layout: object selection panels for celestial bodies/missions/comets/exoplanets (left), scrollable control panels for date/time/animation/scale settings (center), and notes panel (right). Core visualization functions: `plot_objects()` generates static 3D views using JPL Horizons data, `animate_objects()` creates frame-by-frame animations. Launches three specialized GUIs: `star_visualization_gui.py` (HR diagrams and stellar neighborhoods), `earth_system_visualization_gui.py` (climate data hub), and `orbital_param_viz.py` (orbital mechanics visualization). *Note: In retrospect, plot_objects and animate_objects could have been separate modules but remain as core 1,200+ line functions.* |
```

**With:**
```
| `palomas_orrery.py` | **Primary GUI and solar system visualization engine** (~420KB, 8,700+ lines). Main application with three-column tkinter layout: object selection panels for celestial bodies/missions/comets/exoplanets (left), scrollable control panels for date/time/animation/scale settings (center), and notes panel (right). Core visualization functions: `plot_objects()` generates static 3D views using JPL Horizons data, `animate_objects()` creates frame-by-frame animations. Supports TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2) with `ANALYTICAL_ANIMATION_FALLBACK` for objects without JPL ephemeris. Launches three specialized GUIs: `star_visualization_gui.py` (HR diagrams and stellar neighborhoods), `earth_system_visualization_gui.py` (climate data hub), and `orbital_param_viz.py` (orbital mechanics visualization). *Note: In retrospect, plot_objects and animate_objects could have been separate modules but remain as core 1,200+ line functions.* |
```

---

## 3. UPDATE CACHE MANAGEMENT - osculating_cache_manager.py (Line 72)

**Replace:**
```
| `osculating_cache_manager.py` | Osculating orbital elements cache with epoch tracking, auto-refresh intervals, and atomic saves. Stores JPL Horizons osculating elements for 40+ objects with per-object refresh policies |
```

**With:**
```
| `osculating_cache_manager.py` | Osculating orbital elements cache with epoch tracking, auto-refresh intervals, and atomic saves. Stores JPL Horizons osculating elements for 40+ objects with per-object refresh policies. Includes `get_cache_key()` helper for center-body aware caching (e.g., `"Charon@9"` for barycenter view vs `"Charon"` for Pluto-centered view) |
```

---

## 4. UPDATE CRITICAL DATA FILE - osculating_cache.json (Line 80)

**Replace:**
```
| `osculating_cache.json` | **Backbone of the osculating orbit system.** Contains JPL Horizons orbital elements (a, e, i, ω, Ω, TP) for 40+ objects including planets, moons, asteroids, and comets. Provides epoch tracking and per-object refresh intervals. Used by `idealized_orbits.py` for Keplerian orbit calculations, apsidal markers, dual-orbit visualizations, and the Pluto-Charon barycenter system. Managed by `osculating_cache_manager.py`. |
```

**With:**
```
| `osculating_cache.json` | **Backbone of the osculating orbit system.** Contains JPL Horizons orbital elements (a, e, i, ω, Ω, TP) for 40+ objects including planets, moons, asteroids, and comets. Provides epoch tracking and per-object refresh intervals. Supports center-body aware cache keys (e.g., `"Charon@9"` for barycenter-relative elements). Used by `idealized_orbits.py` for Keplerian orbit calculations, apsidal markers, dual-orbit visualizations, TNO satellite systems, and the Pluto-Charon barycenter system. Managed by `osculating_cache_manager.py`. |
```

---

## 5. UPDATE COORDINATE SYSTEMS & ORBITAL MECHANICS - orbital_elements.py (Line 148)

**Replace:**
```
| `orbital_elements.py` | Central repository for orbital parameters, parent-satellite relationships (`parent_planets` dictionary), and planet tilts. Includes Pluto-Charon barycenter for binary planet mode |
```

**With:**
```
| `orbital_elements.py` | Central repository for orbital parameters, parent-satellite relationships (`parent_planets` dictionary), and planet tilts. Includes Pluto-Charon barycenter for binary planet mode, TNO satellite orbital elements (Dysnomia, Hi'iaka, Namaka, MK2), and analytical parameters for objects without JPL ephemeris (MK2 from arXiv:2509.05880) |
```

---

## 6. UPDATE COORDINATE SYSTEMS & ORBITAL MECHANICS - idealized_orbits.py (Line 150)

**Replace:**
```
| `idealized_orbits.py` | **Core orbit visualization engine.** Keplerian orbit calculations using osculating elements from `osculating_cache.json`. Supports dual-orbit systems, apsidal markers, and multi-center modes (including Pluto-Charon barycenter) |
```

**With:**
```
| `idealized_orbits.py` | **Core orbit visualization engine.** Keplerian orbit calculations using osculating elements from `osculating_cache.json`. Supports dual-orbit systems, apsidal markers, and multi-center modes (including Pluto-Charon barycenter). Includes `plot_tno_satellite_orbit()` for TNO moon visualization and `ANALYTICAL_FALLBACK_SATELLITES` list for objects without JPL ephemeris (e.g., MK2 calculated from published orbital elements) |
```

---

## 7. UPDATE CRITICAL DATA INFRASTRUCTURE - osculating_cache_manager.py (Line 158)

**Replace:**
```
| `osculating_cache_manager.py` | Cache manager with atomic saves, epoch tracking, and configurable refresh intervals (weekly for planets, daily for active moons) |
```

**With:**
```
| `osculating_cache_manager.py` | Cache manager with atomic saves, epoch tracking, and configurable refresh intervals (weekly for planets, daily for active moons). Includes `get_cache_key(object_name, center_body)` for center-body aware caching to support barycenter views |
```

---

## 8. ADD NEW SECTION: TNO Satellite Systems (After Line 161, before Exoplanet Systems)

**Insert new section:**

```markdown
---

## TNO Satellite Systems 🆕

The orrery visualizes Trans-Neptunian Object satellite systems with full orbital mechanics:

| System | Satellites | Data Source |
|--------|------------|-------------|
| Eris | Dysnomia | JPL Horizons osculating elements |
| Haumea | Hi'iaka, Namaka | JPL Horizons osculating elements |
| Makemake | MK2 | Analytical fallback (arXiv:2509.05880) |

**Analytical Fallback Architecture:**

For satellites without JPL Horizons ephemeris (like MK2), the system calculates orbits from published orbital elements:

```
ANALYTICAL_FALLBACK_SATELLITES = ['MK2']  # In idealized_orbits.py
ANALYTICAL_ANIMATION_FALLBACK = ['MK2']   # In palomas_orrery.py
```

**Data Flow (MK2 example):**
```
User selects MK2 → fetch_trajectory() → JPL returns empty
    ↓
Check ANALYTICAL_ANIMATION_FALLBACK → MK2 listed
    ↓
Load elements from orbital_elements.py (arXiv source)
    ↓
Calculate Keplerian orbit analytically
    ↓
Display with "Analytical Orbit" attribution
```

**Key Files:**
- `orbital_elements.py` - MK2 orbital parameters (a, e, i, P)
- `idealized_orbits.py` - `plot_tno_satellite_orbit()`, fallback logic
- `palomas_orrery.py` - Animation fallback with velocity calculation
- `constants_new.py` - TNO moon descriptions and metadata
```

---

## 9. FIX DATA FLOW EXAMPLE (Lines 373-381)

**Replace:**
```
*Example Data Flow (Mars Visualization):*
```
User clicks "Mars" → palomas_orrery.py (L6) → orbit_data_manager (L2) 
→ [check cache] → orbit_cache/mars.json (L3) → refined_orbits.py (L4) 
→ planet_visualization.py (L5) → plot_objects() (L6) → Plotly render 
→ save_utils.py (L8) → PNG/HTML output (L10)

Time: Milliseconds (cached) or 1-2 seconds (fresh API call)
```
```

**With:**
```
*Example Data Flow (Mars Visualization):*
```
User clicks "Mars" → palomas_orrery.py (L6) → orbit_data_manager (L2) 
→ [check cache] → orbit_cache/mars.json (L3) → idealized_orbits.py (L4) 
→ planet_visualization.py (L5) → plot_objects() (L6) → Plotly render 
→ save_utils.py (L8) → PNG/HTML output (L10)

Time: Milliseconds (cached) or 1-2 seconds (fresh API call)
```

*Example Data Flow (MK2 - Analytical Fallback):* 🆕
```
User selects "MK2" → palomas_orrery.py (L6) → fetch_trajectory() (L2)
→ JPL Horizons returns empty → Check ANALYTICAL_FALLBACK list
→ Load from orbital_elements.py (L4) → Calculate Keplerian orbit
→ idealized_orbits.py plot_tno_satellite_orbit() (L4)
→ plot_objects() (L6) → Plotly render with "Analytical" attribution

Time: Milliseconds (no API call - calculated from stored elements)
```
```

---

## 10. UPDATE FLOWCHART REFERENCES (Lines 392, 420)

**Replace (Line 392):**
```
Also available: `palomas_orrery_flowchart_v13_vertical.md` for Mermaid flowchart with detailed module-level connections.
```

**With:**
```
Also available: `palomas_orrery_flowchart_v15_vertical.md` for Mermaid flowchart with detailed module-level connections including TNO satellites, center-body aware caching, and analytical fallback architecture.
```

**Replace (Line 420):**
```
- [palomas_orrery_flowchart_v13_vertical.md](palomas_orrery_flowchart_v13_vertical.md) - Vertical Mermaid flowchart with detailed connections
```

**With:**
```
- [palomas_orrery_flowchart_v15_vertical.md](palomas_orrery_flowchart_v15_vertical.md) - Vertical Mermaid flowchart with detailed connections (TNO satellites, analytical fallback)
```

---

## 11. UPDATE GENERATED DATE (Line 425)

**Replace:**
```
Generated November 26, 2025 for Paloma's Orrery project
```

**With:**
```
Generated December 8, 2025 for Paloma's Orrery project
```

---

## 12. UPDATE MODULE COUNTS (Line 21-24)

**Replace:**
```
**Module Organization:**

- Total modules: 81 Python files
- Active production modules: 75
- Development/testing modules: 3
- Obsolete/reference modules: 3 (retained for historical reference)
```

**With:**
```
**Module Organization:**

- Total modules: 81 Python files
- Active production modules: 75
- Development/testing modules: 3
- Obsolete/reference modules: 3 (retained for historical reference)

**Recent Architectural Additions (Dec 2025):**
- TNO satellite visualization system
- Center-body aware osculating cache
- Analytical orbit fallback for objects without JPL ephemeris
```

---

## Summary of All Changes

| Section | Changes |
|---------|---------|
| Header | Date updated to Dec 8, 2025 |
| Core Application | palomas_orrery.py size/lines updated, TNO systems added |
| Cache Management | `get_cache_key()` and center-body awareness documented |
| Critical Data | osculating_cache.json center-body keys documented |
| Orbital Mechanics | orbital_elements.py TNO/MK2 params added |
| Orbital Mechanics | idealized_orbits.py TNO function and fallback added |
| **New Section** | TNO Satellite Systems with fallback architecture |
| Data Flow | Fixed obsolete refined_orbits.py reference, added MK2 example |
| References | Flowchart v13 → v15 |
| Footer | Generated date updated |
| Module Organization | Added recent architectural additions note |

---

## Validation Against Flowchart v15

| Flowchart Element | MODULE_INDEX Coverage |
|-------------------|----------------------|
| arXiv as data source | ✅ TNO section mentions arXiv:2509.05880 |
| `get_cache_key()` | ✅ osculating_cache_manager.py description |
| Center-body aware keys | ✅ Both cache manager and JSON file descriptions |
| `plot_tno_satellite_orbit()` | ✅ idealized_orbits.py description |
| `ANALYTICAL_FALLBACK_SATELLITES` | ✅ New TNO section + idealized_orbits.py |
| `ANALYTICAL_ANIMATION_FALLBACK` | ✅ palomas_orrery.py description + TNO section |
| TNO satellite systems | ✅ New dedicated section |
| Updated line counts | ✅ 8,700+ lines noted |

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 8, 2025*
