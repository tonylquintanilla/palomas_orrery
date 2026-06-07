# Jupiter Satellite Implementation Status

**Project:** Paloma's Orrery  
**Date:** November 22, 2025  
**Author:** Claude (with Tony)  
**Context Window:** 44% used (85K/190K tokens) - Plenty of room remaining

---

## Executive Summary

Jupiter's Galilean moons have **PARTIAL dual-orbit implementation** - missing time-varying elements:

- ✅ **Osculating orbits:** WORKING (dashed lines visible in plots)
- ❌ **Analytical orbits:** INCOMPLETE (using wrong element source)
- ✅ **Integration code:** EXISTS in idealized_orbits.py
- ⭐ **ROOT CAUSE FOUND:** Jupiter missing time-varying element calculation that Mars has

**Status:** Gap identified - need to add `calculate_jupiter_satellite_elements()` following Mars pattern

---

## ⭐ ROOT CAUSE IDENTIFIED

**Jupiter is missing time-varying element calculation that Mars has!**

**Mars implementation (lines 1083-1126):**
```python
if parent_planet == 'Mars':
    if date is not None:
        # Override static orbital elements with time-varying ones
        orbital_params = calculate_mars_satellite_elements(date, satellite_name)
        # Regenerate orbit with updated elements
        # Apply rotations
        # Transform to ecliptic
```

**Jupiter implementation (lines 1131-1139):**
```python
elif parent_planet == 'Jupiter':
    # Just applies simple tilt transformation
    # NO time-varying element calculation ❌
    # NO orbit regeneration ❌
```

**Result:** Both "analytical" and "osculating" use same cached elements → orbits overlap perfectly → no visual distinction

**See:** [JUPITER_VS_MARS_IMPLEMENTATION_GAP.md](computer:///mnt/user-data/outputs/JUPITER_VS_MARS_IMPLEMENTATION_GAP.md) for detailed comparison

---

## Current Implementation Status

### What's Working ✅

1. **Osculating Orbit Function (`plot_jupiter_moon_osculating_orbit`)**
   - Location: `idealized_orbits.py` ~line 819
   - Fetches JPL Horizons instantaneous elements from cache
   - Correctly handles ecliptic reference frame
   - No Jupiter rotation applied (elements already in ecliptic)
   - Produces dashed line traces that ARE visible in plots

2. **Integration Wiring**
   - Location: `idealized_orbits.py` ~line 2091-2111
   - Special handling block exists for Jupiter moons
   - Calls both `plot_satellite_orbit()` and `plot_jupiter_moon_osculating_orbit()`
   - Pattern matches Mars moons (Phobos/Deimos)

3. **Cache System**
   - Jupiter moon osculating elements cached properly
   - Eight moons supported: Metis, Adrastea, Amalthea, Thebe, Io, Europa, Ganymede, Callisto
   - Horizons IDs mapped correctly

### What's Not Working ❌

1. **Analytical Orbits Missing**
   - `plot_satellite_orbit()` being called but produces no visible trace
   - Should show dotted line for mean/time-varying orbital elements
   - Expected to show Jupiter equatorial → ecliptic transformation

2. **Possible Root Causes:**
   - Function silently failing (no error, no trace)
   - Trace created but invisible (wrong scale, alpha=0, etc)
   - Elements missing from `planetary_params` dict
   - Wrong reference frame causing off-screen plotting

---

## Reference Frame Architecture

### Expected Pattern (from Mars Moons)

**Analytical Orbit (mean elements):**
- Source: `orbital_elements.py` or `refined_orbits.py`
- Frame: Parent equatorial (Jupiter equatorial)
- Transformation: Apply Jupiter's 3.13° axial tilt to rotate to ecliptic
- Visual: Dotted line, shows time-averaged orbit

**Osculating Orbit (instantaneous snapshot):**
- Source: JPL Horizons via `osculating_cache_manager`
- Frame: Already in ecliptic (J2000.0)
- Transformation: None needed (already in target frame)
- Visual: Dashed line, shows precise orbital state at epoch

**Educational Value:**
- Separation between orbits shows reference frame difference
- ~3° tilt for Jupiter (vs ~25° for Mars, ~23.4° for Earth)
- Demonstrates how coordinate system choice affects orbital description

---

## Investigation from Previous Session

### Tony's Observation (Critical!)

From plot inspection:
- **Dashed lines visible:** Osculating orbits ARE plotting ✅
- **Dotted lines missing:** Analytical orbits NOT plotting ❌
- Initial diagnosis said "osculating missing" - **this was backwards!**

### Console Output Analysis

```
Plotting Io orbit around Jupiter
Orbital elements: a=0.002821, e=0.004797, i=2.2038°...
  Skipping Jupiter rotation (elements already ecliptic, i=2.2038°)

[OSCULATING] Loading cached elements for Io...
  ✓ Using cached osculating elements

Plotting osculating orbit for Io
  Inclination: 2.2038° (ecliptic frame)
  Epoch: 2025-11-21
  ✓ Osculating orbit plotted
```

**Key finding:** Both analytical and osculating show i=2.2°, suggesting:
1. Analytical elements might already be in ecliptic frame (not Jupiter equatorial)
2. Or transformation not being applied when it should be
3. This causes both orbits to overlap perfectly

### Expected vs. Actual Inclinations

| Moon | Analytical (Expected) | Osculating (Actual) | Difference |
|------|----------------------|---------------------|------------|
| Io | 0.05° (Jup eq) | 2.20° (ecliptic) | ~2.15° |
| Europa | 0.47° (Jup eq) | 3.58° (ecliptic) | ~3.11° |
| Ganymede | 0.18° (Jup eq) | 3.31° (ecliptic) | ~3.13° |
| Callisto | 0.19° (Jup eq) | 3.32° (ecliptic) | ~3.13° |

**Pattern:** Difference should equal Jupiter's 3.13° axial tilt

**Actual from console:** Both showing i=2.2° (no difference!)

---

## Next Steps (Prioritized)

### Immediate Debugging (Session 1)

1. **Verify `plot_satellite_orbit()` is actually running**
   - Add diagnostic print statements
   - Confirm function entry and trace creation
   - Check if trace gets added to figure

2. **Check analytical orbital elements source**
   - Where do Jupiter moon elements come from?
   - Are they in `refined_orbits.py`?
   - What inclination values are stored?
   - Should be ~0.05° for Io (Jupiter equatorial)

3. **Verify transformation logic**
   - Is Jupiter rotation being applied to analytical?
   - Check the i > 1° detection logic
   - May need to force rotation for Jupiter moons

### Root Cause Investigation (Session 2)

4. **Compare with working Mars implementation**
   - Mars analytical orbits DO show up
   - What's different about Jupiter path?
   - Check `plot_satellite_orbit()` conditional logic

5. **Test with single moon (Io)**
   - Isolate to simplest case
   - Add extensive debug output
   - Verify each calculation step
   - Check coordinate transforms

6. **Verify `planetary_params` dict structure**
   - Does it contain Jupiter moon data?
   - Is the data in correct format?
   - Are time-varying calculations working?

### Implementation Fixes (Session 3)

7. **Fix analytical orbit source**
   - Ensure mean elements from `orbital_elements.py`
   - NOT osculating elements from cache
   - Verify Jupiter equatorial frame data

8. **Fix reference frame transformation**
   - Apply Jupiter 3.13° tilt consistently
   - Don't skip rotation based on i > 1° check
   - Special handling for Jupiter moons if needed

9. **Add time-varying element support**
   - If not present, implement for Jupiter moons
   - Pattern exists for Moon (nodal precession, apsidal advance)
   - May be simpler for Jupiter (less perturbation)

### Testing & Documentation (Session 4)

10. **Visual verification**
    - Both orbits visible (dotted + dashed)
    - ~3° separation between planes
    - Correct centering at Jupiter
    - Hover text shows different epochs/sources

11. **Update documentation**
    - Create Jupiter handoff document (like Mars)
    - Document reference frames clearly
    - Note differences from Mars (smaller tilt)
    - Include Thebe anomaly if relevant

12. **Test all eight moons**
    - Galilean moons (Io, Europa, Ganymede, Callisto)
    - Inner moons (Metis, Adrastea, Amalthea, Thebe)
    - Verify consistent behavior

---

## Technical Architecture Notes

### File Locations

**Main implementation:**
- `idealized_orbits.py`: Lines 819-915 (osculating function)
- `idealized_orbits.py`: Lines 2091-2111 (integration code)
- `osculating_cache_manager.py`: Cache storage/retrieval

**Element sources:**
- `orbital_elements.py`: Static mean elements (analytical source)
- `refined_orbits.py`: Possibly time-varying elements
- JPL Horizons cache: Osculating elements

**Related systems:**
- `jupiter_visualization_shells.py`: Jupiter-specific visualization
- `constants_new.py`: Jupiter moon definitions
- `palomas_orrery.py`: Main integration point

### Key Functions

```python
# Osculating orbit (WORKING)
plot_jupiter_moon_osculating_orbit(fig, satellite_name, date, color, show_apsidal_markers)
    └─> Loads from osculating_cache_manager
    └─> No transformation (already ecliptic)
    └─> Creates dashed trace ✅

# Analytical orbit (NOT WORKING) 
plot_satellite_orbit(moon_name, planetary_params, center_id, color, fig, ...)
    └─> Should load from orbital_elements.py
    └─> Should apply Jupiter rotation
    └─> Should create dotted trace ❌
```

### Integration Code Block

```python
# Lines 2091-2111 in idealized_orbits.py
elif moon_name in JUPITER_MOONS and center_id == 'Jupiter':
    # Plot analytical orbit (time-varying elements - dotted line)
    fig = plot_satellite_orbit(
        moon_name, 
        planetary_params,
        center_id, 
        color_map(moon_name), 
        fig,
        date=date,
        days_to_plot=days_to_plot,
        current_position=satellite_current_pos,
        show_apsidal_markers=show_apsidal_markers
    )
    
    # Plot osculating orbit (JPL elements - dashed line)
    if date:
        fig = plot_jupiter_moon_osculating_orbit(
            fig,
            moon_name,
            date,
            color_map(moon_name),
            show_apsidal_markers=show_apsidal_markers
        )
```

---

## Comparison with Working Systems

### Moon (Reference Implementation)

- ✅ Analytical: Time-varying elements with perturbations
- ✅ Osculating: JPL Horizons cache
- ✅ Clear visual separation
- ✅ Educational hover text
- ✅ Both orbits visible

### Mars Moons (Working Pattern)

- ✅ Analytical: Mars equatorial → ecliptic transform
- ✅ Osculating: Already in ecliptic
- ✅ ~25° separation (Mars tilt)
- ✅ "Fear falling into War" educational story
- ✅ Both orbits visible

### Jupiter Moons (Current State)

- ❌ Analytical: Function called but no visible trace
- ✅ Osculating: Working perfectly
- ❌ No visual separation (analytical missing)
- ⚠️ Should show ~3° separation (Jupiter tilt)
- ❌ Only one orbit visible (osculating)

---

## Questions to Answer

1. **Where do Jupiter analytical elements come from?**
   - Static file? Time-varying calculation?
   - What inclination values are stored?
   
2. **Why isn't `plot_satellite_orbit()` creating visible trace?**
   - Silent failure? Wrong parameters?
   - Coordinate issue putting it off-screen?

3. **Is Jupiter rotation being applied?**
   - Should transform from Jupiter equatorial to ecliptic
   - Detection logic might be skipping it

4. **Do we need time-varying elements for Jupiter?**
   - Moon has them (nodal precession)
   - Mars moons use static elements
   - What's appropriate for Jupiter?

---

## Educational Goals (Why This Matters)

### For Paloma (Age 7-8)

"Jupiter's moons dance around the giant planet! We can see where they are RIGHT NOW (dashed line) and where they usually are on average (dotted line). The difference shows us that Jupiter is tilted a little bit!"

### For Students/General Public

- Reference frames: How coordinate system choice changes orbital description
- Perturbations: Why real orbits differ from perfect ellipses  
- Observational astronomy: Comparing predictions to measurements
- System hierarchy: Moons orbit planets (equatorial), planets orbit Sun (ecliptic)

### For Developers/Scientists

- Coordinate transformations: Parent equatorial ↔ ecliptic
- Mean vs. osculating elements: Time-averaged vs. instantaneous
- JPL Horizons integration: Using authoritative ephemeris data
- Educational software design: Multiple abstraction levels simultaneously

---

## Session Summary

**Current context window: 36% used (68K/190K tokens)**

**What we learned today:**
- Osculating orbits ARE working (visible dashed lines)
- Analytical orbits NOT working (missing dotted lines)
- Integration code exists and looks correct
- Issue is likely in `plot_satellite_orbit()` function or its data source
- Both orbits showing same inclination suggests frame issue

**What we need to do:**
- Add diagnostic output to `plot_satellite_orbit()`
- Verify analytical element source and values
- Check Jupiter rotation transformation logic
- Compare with working Mars implementation

**Status:** Ready for collaborative debugging session following working protocol principles

---

## References

- Mars Moons Implementation: Working pattern to follow
- Moon Implementation: Time-varying element example  
- `osculating_cache_manager.py`: Cache system documentation
- Working Protocol v2.3: Collaboration methodology

---

*"The inclination tells you the reference frame." - Nov 21, 2025*

*"If orbits are in wrong place, check reference frame first."*

*"Trust your eyes - if it looks wrong, it probably IS wrong."*

---

**Next Session Start:**
"Let's debug why Jupiter analytical orbits aren't showing up. I'll add diagnostic output to `plot_satellite_orbit()` and trace the execution path."
