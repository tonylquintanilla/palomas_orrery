# Exoplanet Integration - Code Structure Map
## Phase 1, Week 1 Complete

```
┌─────────────────────────────────────────────────────────────────────┐
│                     EXOPLANET MODULES (NEW)                         │
│                     Week 1 Implementation                            │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ exoplanet_systems.py (24 KB, 890 lines)                         │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                   │
│ 📚 HARDCODED CATALOG (Phase 1)                                   │
│                                                                   │
│ TRAPPIST1_SYSTEM                                                 │
│   ├─ host_star: {                                                │
│   │    name, ra, dec, distance_pc,                               │
│   │    pmra, pmdec, spectral_type,                               │
│   │    mass_solar, radius_solar, teff_k,                         │
│   │    habitable_zone_inner/outer_au                             │
│   │  }                                                            │
│   └─ planets: [                                                  │
│        {name, period_days, semi_major_axis_au,                   │
│         eccentricity, inclination_deg,                           │
│         mass_earth, radius_earth, equilibrium_temp_k,            │
│         in_habitable_zone, discovery_method, ...}                │
│        × 7 planets                                                │
│      ]                                                            │
│                                                                   │
│ TOI1338_SYSTEM (Binary!)                                         │
│   ├─ host_star: {                                                │
│   │    is_binary: True,                                          │
│   │    binary_period_days, binary_separation_au,                 │
│   │    star_A: {mass, radius, spectral_type, ...}                │
│   │    star_B: {mass, radius, spectral_type, ...}                │
│   │  }                                                            │
│   └─ planets: [× 2 circumbinary planets]                         │
│                                                                   │
│ PROXIMA_SYSTEM (Nearest!)                                        │
│   └─ High proper motion: 3853 mas/yr                             │
│                                                                   │
│ 🔧 UTILITIES:                                                     │
│   • get_system(id)                                               │
│   • get_all_systems()                                            │
│   • get_planets_in_hz(id)                                        │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ exoplanet_orbits.py (21 KB, 697 lines)                          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                   │
│ 🧮 KEPLERIAN MECHANICS                                            │
│                                                                   │
│ solve_kepler_equation(M, e)                                      │
│   └─ Newton-Raphson: M = E - e·sin(E)                            │
│                                                                   │
│ calculate_true_anomaly(E, e)                                     │
│   └─ ν = 2·arctan2(√(1+e)·sin(E/2), √(1-e)·cos(E/2))            │
│                                                                   │
│ calculate_keplerian_orbit(a, e, i, ω, Ω, P, epoch, date)        │
│   ├─ Generate ellipse in orbital plane                           │
│   ├─ Rotate by ω (argument of periastron)                        │
│   ├─ Rotate by i (inclination)                                   │
│   ├─ Rotate by Ω (longitude of ascending node)                   │
│   └─ Returns: (x, y, z) arrays [360 points]                      │
│                                                                   │
│ calculate_planet_position(a, e, i, ω, Ω, P, epoch, date)        │
│   └─ Single point at specific date                               │
│                                                                   │
│ 🌟 BINARY STAR DYNAMICS                                           │
│                                                                   │
│ calculate_binary_star_orbits(m_A, m_B, sep, period)             │
│   ├─ a_A = sep × (m_B / total_mass)                              │
│   ├─ a_B = sep × (m_A / total_mass)                              │
│   └─ Returns: {star_A: {...}, star_B: {...}}                     │
│                                                                   │
│ 🎨 VISUALIZATION                                                   │
│                                                                   │
│ plot_exoplanet_orbits(fig, planets, system, date)               │
│   ├─ For each planet:                                            │
│   │   ├─ Calculate orbit path                                    │
│   │   ├─ Add orbit trace (Plotly Scatter3d)                      │
│   │   ├─ Calculate current position                              │
│   │   └─ Add position marker                                     │
│   └─ Return updated figure                                       │
│                                                                   │
│ plot_binary_host_stars(fig, system, date)                       │
│   ├─ Calculate stellar orbits around barycenter                  │
│   ├─ Plot Star A (yellow, larger)                                │
│   ├─ Plot Star B (orange, smaller, 180° phase)                   │
│   └─ Plot barycenter (white X)                                   │
│                                                                   │
│ calculate_exoplanet_axis_range(planets)                         │
│   └─ max(apastron) × 1.2 (same logic as Solar System)           │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ exoplanet_coordinates.py (18 KB, 562 lines)                     │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                   │
│ 📍 PROPER MOTION                                                  │
│                                                                   │
│ apply_proper_motion(ra, dec, pmra, pmdec, epoch, date)          │
│   ├─ Δt = (date - epoch) in years                                │
│   ├─ ΔRA = (pmra / 3,600,000) × Δt degrees                       │
│   ├─ ΔDec = (pmdec / 3,600,000) × Δt degrees                     │
│   └─ Returns: (ra_new, dec_new)                                  │
│                                                                   │
│ get_star_position_at_date(star_data, date)                      │
│   └─ Applies proper motion if significant                        │
│                                                                   │
│ calculate_tangential_velocity(pmra, pmdec, distance)            │
│   └─ Returns: v_tan in km/s                                      │
│                                                                   │
│ 🌐 COORDINATE TRANSFORMS (For Phase 4 context)                    │
│                                                                   │
│ radec_to_cartesian(ra, dec, distance)                           │
│   ├─ x = d × cos(dec) × cos(ra)                                  │
│   ├─ y = d × cos(dec) × sin(ra)                                  │
│   ├─ z = d × sin(dec)                                            │
│   └─ Used ONLY for stellar neighborhood maps                     │
│                                                                   │
│ cartesian_to_radec(x, y, z)                                     │
│   └─ Inverse transformation                                      │
│                                                                   │
│ get_star_3d_position(star_data, date)                           │
│   └─ Returns: (x, y, z) in parsecs (J2000 equatorial)           │
│                                                                   │
│ 📏 DISTANCE CONVERSIONS                                            │
│                                                                   │
│   • parsecs ↔ light-years (1 pc = 3.26156 ly)                   │
│   • parsecs ↔ AU (1 pc = 206,265 AU)                             │
│   • parallax ↔ distance (d = 1000/π_mas)                         │
│                                                                   │
│ 🎯 LOCAL FRAMES                                                    │
│                                                                   │
│ create_local_frame_description(star_data)                       │
│   └─ Documents independent coordinate system for each system    │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                    INTEGRATION POINTS                           │
│              (Ready for Week 2 - GUI Integration)               │
└────────────────────────────────────────────────────────────────┘

palomas_orrery.py
  │
  ├─ objects = [...]
  │    │
  │    └─── ADD EXOPLANET OBJECTS ◄─── exoplanet_systems.py
  │         {
  │           'name': 'TRAPPIST-1 b',
  │           'id': 'trappist1b',
  │           'object_type': 'exoplanet',
  │           'semi_major_axis_au': 0.01154,
  │           ...
  │         }
  │
  ├─ plot_objects()
  │    │
  │    └─── IF exoplanets selected:
  │         plot_exoplanet_orbits() ◄─── exoplanet_orbits.py
  │         plot_binary_host_stars()
  │
  ├─ animate_objects()
  │    │
  │    └─── Same integration as plot_objects()
  │
  └─ GUI Section: "Exoplanetary Systems"
       │
       ├─ System dropdown: [TRAPPIST-1, TOI-1338, Proxima]
       ├─ Planet checkboxes (auto-populated)
       └─ Info labels (distance, # planets)

```

## Data Flow

```
User selects "TRAPPIST-1" from dropdown
         ↓
GUI populates 7 planet checkboxes
         ↓
User checks: [✓] e, [✓] f, [✓] g (habitable zone planets)
         ↓
User clicks "Plot Entered Date"
         ↓
plot_objects() called
         ↓
Detects exoplanet objects in selection
         ↓
Calls plot_exoplanet_orbits(fig, planets, system, date)
         ↓
For each planet:
  1. calculate_keplerian_orbit() → orbit path (360 points)
  2. calculate_planet_position() → current position
  3. fig.add_trace() → orbit line (blue)
  4. fig.add_trace() → planet marker (green if HZ)
         ↓
plot_binary_host_stars() if binary system
         ↓
calculate_exoplanet_axis_range() → ±0.074 AU
         ↓
Display interactive 3D plot
         ↓
User rotates, zooms, hovers (standard Plotly controls)
```

## Module Dependencies

```
exoplanet_systems.py
  └─ No dependencies (pure data)

exoplanet_orbits.py
  ├─ import numpy
  ├─ import plotly.graph_objs (when available)
  └─ from exoplanet_systems import get_system

exoplanet_coordinates.py
  ├─ import numpy
  └─ from exoplanet_systems import get_system (for testing)

palomas_orrery.py (Week 2)
  ├─ from exoplanet_systems import EXOPLANET_CATALOG
  ├─ from exoplanet_orbits import plot_exoplanet_orbits
  ├─ from exoplanet_orbits import plot_binary_host_stars
  └─ from exoplanet_orbits import calculate_exoplanet_axis_range
```

## Test Coverage

✅ **exoplanet_systems.py:**
   - All 3 systems load correctly
   - 11 planets across all systems
   - Habitable zone flags accurate
   - Helper functions working

✅ **exoplanet_orbits.py:**
   - Kepler equation solver validated
   - TRAPPIST-1 e position: (0.0291, 0, 0) AU at epoch ✓
   - Binary orbits: Star A=0.0189 AU, Star B=0.0691 AU ✓
   - Rotation mathematics verified

✅ **exoplanet_coordinates.py:**
   - Proxima proper motion: 192.7" over 50 years ✓
   - Coordinate round-trip error: <1e-6° ✓
   - Tangential velocities calculated: 24-61 km/s ✓
   - Local frame descriptions generated ✓

## Performance Estimates

**TRAPPIST-1 (7 planets):**
- 7 planets × 360 points = 2,520 orbit points
- 7 position markers
- Total traces: ~14
- Expected FPS: >60

**TOI-1338 (2 planets + 2 stars):**
- 2 planets × 360 points = 720 points
- 2 stellar orbits × 360 points = 720 points
- 4 position markers
- Total traces: ~8
- Expected FPS: >60

**All 3 systems simultaneously:**
- 11 planets × 360 = 3,960 points
- 2 stars × 360 = 720 points
- Total: ~4,680 points across ~24 traces
- Expected FPS: >30 ✓

## Files Delivered

📄 **Code Modules:**
1. exoplanet_systems.py (24 KB)
2. exoplanet_orbits.py (21 KB)
3. exoplanet_coordinates.py (18 KB)

📄 **Documentation:**
4. exoplanet_integration_framework.md (38 KB)
5. exoplanet_implementation_quickstart.md (15 KB)
6. phase1_week1_complete.md (10 KB)

**Total:** 6 files, ~126 KB

## Next Session

**Week 2, Day 6-7:** GUI Integration
- Add objects to palomas_orrery.py
- Create tkinter variables
- Test object selection

Ready to proceed! 🚀
