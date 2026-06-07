# Jupiter vs Mars Satellite Implementation Comparison

**Project:** Paloma's Orrery  
**Date:** November 22, 2025  
**Status:** Gap Analysis Complete  
**Context Window:** 43% used (81K/190K tokens)

---

## The Problem: Jupiter Missing Time-Varying Elements

### Mars Implementation (WORKING) ✅

**Location:** `idealized_orbits.py` lines 1083-1126

```python
if parent_planet == 'Mars':
    if date is not None:
        # Override static orbital elements with time-varying ones
        orbital_params = calculate_mars_satellite_elements(date, satellite_name)
        print(f"Using time-varying elements for {satellite_name} at {date}")
        
        # Re-extract the updated orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Regenerate the orbit with new elements
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        # Convert updated angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Apply standard orbital rotations with updated elements
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
    
    # Transform from Mars equatorial to ecliptic coordinates
    mars_y_rotation = np.radians(25.19)
    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, mars_y_rotation, 'y')
    print(f"Transformation applied: Mars with Y-axis rotation of 25.19°")
```

**Key features:**
1. ✅ Checks if `date is not None`
2. ✅ Calls `calculate_mars_satellite_elements(date, satellite_name)`
3. ✅ Regenerates orbit with time-varying elements
4. ✅ Re-applies rotations with updated values
5. ✅ Applies Mars equatorial → ecliptic transformation (25.19° Y-rotation)

---

### Jupiter Implementation (INCOMPLETE) ❌

**Location:** `idealized_orbits.py` lines 1131-1139

```python
elif parent_planet == 'Jupiter':
    # Use simple tilt for Jupiter (which works well)
    if 'Jupiter' in planet_tilts:
        tilt_rad = np.radians(planet_tilts['Jupiter'])
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, tilt_rad, 'x')
        print(f"Transformation applied: Jupiter with tilt={planet_tilts['Jupiter']}°")
    else:
        x_final, y_final, z_final = x_temp, y_temp, z_temp
        print("No transformation applied for Jupiter (missing tilt data)")
```

**What's missing:**
1. ❌ No time-varying element calculation
2. ❌ No regeneration of orbit with updated elements
3. ❌ No re-application of rotations
4. ✅ HAS transformation (but too simple)

---

## The Root Cause

**Jupiter satellites are using STATIC elements from `planetary_params`**, which:
- Likely contains osculating elements from last cache update
- NOT mean elements from `orbital_elements.py`
- NOT time-varying perturbation calculations

**This means:**
- Both "analytical" and "osculating" orbits use same elements
- No visible difference between the two
- No educational value from dual-orbit system

---

## What Jupiter Needs

### 1. Create `calculate_jupiter_satellite_elements()` Function

**Pattern from Mars:**

```python
def calculate_jupiter_satellite_elements(date, satellite_name):
    """
    Calculate time-varying orbital elements for Jupiter satellites
    Similar to Mars satellites but with Jupiter-specific perturbations
    """
    # Base epoch for elements
    base_epoch = datetime(2025, 6, 2, 0, 0, 0)  # Or appropriate epoch
    
    # Days since base epoch
    d = (date - base_epoch).days
    
    # Base elements (Jupiter equatorial frame)
    if satellite_name == 'Io':
        a_base = 0.002821  # AU
        e_base = 0.0041
        i_base = 0.050  # degrees (Jupiter equatorial!)
        omega_base = 43.977
        Omega_base = 337.840
        
        # Jupiter J2-induced precession rates
        # (Need to calculate these for Galilean moons)
        omega_rate = ??? / 365.25  # degrees/day
        Omega_rate = ??? / 365.25  # degrees/day
        
    elif satellite_name == 'Europa':
        a_base = 0.004486  # AU
        e_base = 0.0094
        i_base = 0.47  # degrees (Jupiter equatorial!)
        omega_base = 219.106
        Omega_base = 337.810
        
        omega_rate = ??? / 365.25
        Omega_rate = ??? / 365.25
        
    # ... (Ganymede, Callisto, others)
    
    # Apply secular changes
    omega = (omega_base + omega_rate * d) % 360.0
    Omega = (Omega_base + Omega_rate * d) % 360.0
    
    return {
        'a': a_base,
        'e': e_base,
        'i': i_base,
        'omega': omega,
        'Omega': Omega
    }
```

### 2. Update Jupiter Block in `plot_satellite_orbit()`

**Replace lines 1131-1139 with:**

```python
elif parent_planet == 'Jupiter':
    # Check if this is a Galilean moon that needs time-varying elements
    JUPITER_MOONS = ['Io', 'Europa', 'Ganymede', 'Callisto', 
                     'Metis', 'Adrastea', 'Amalthea', 'Thebe']
    
    if satellite_name in JUPITER_MOONS and date is not None:
        # Override static orbital elements with time-varying ones
        orbital_params = calculate_jupiter_satellite_elements(date, satellite_name)
        print(f"Using time-varying elements for {satellite_name} at {date}")
        
        # Re-extract the updated orbital elements
        a = orbital_params.get('a', 0)
        e = orbital_params.get('e', 0)
        i = orbital_params.get('i', 0)
        omega = orbital_params.get('omega', 0)
        Omega = orbital_params.get('Omega', 0)
        
        # Regenerate the orbit with new elements
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        # Convert updated angles to radians
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Apply standard orbital rotations with updated elements
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, Omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, omega_rad, 'z')
    
    # Transform from Jupiter equatorial to ecliptic coordinates
    # Jupiter's axial tilt is 3.13° (much smaller than Mars's 25.19°)
    jupiter_tilt = np.radians(3.13)
    x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, jupiter_tilt, 'x')
    print(f"Transformation applied: Jupiter equatorial → ecliptic (3.13° X-rotation)")
```

---

## Base Elements Needed

### Where to Get Jupiter Moon Mean Elements (Jupiter Equatorial Frame)

**Option 1: Horizons Batch Query**
- Query JPL Horizons for mean elements
- Specify Jupiter equatorial frame explicitly
- Get i ~ 0.05° for Io (not 2.2°!)

**Option 2: Calculate from osculating**
- Use osculating i = 2.2° (ecliptic)
- Subtract Jupiter tilt: 2.2° - 3.13° ≈ -0.93°
- Issue: Gets sign wrong, should be ~0.05°

**Option 3: Reference ephemeris**
- Check JPL satellite ephemeris documentation
- Use published mean elements
- Ensure Jupiter equatorial frame

**CRITICAL:** Base inclinations must be in **Jupiter equatorial frame**:
- Io: i ≈ 0.05° (nearly in Jupiter's equator)
- Europa: i ≈ 0.47°
- Ganymede: i ≈ 0.18°
- Callisto: i ≈ 0.19°

**NOT ecliptic values:**
- Io: i ≈ 2.2° ❌ (this is after transformation!)

---

## Precession Rates Needed

For Jupiter satellites, need to calculate:

**Nodal precession (Ω̇):**
- Caused by Jupiter's J2 (oblateness)
- Io has fastest rate (closest to Jupiter)
- Much faster than Mars moons

**Apsidal precession (ω̇):**
- Also from J2 effect
- Proportional to 1/a^(3.5)

**Reference:**
- Burns (1977): "Orbital Evolution"
- Murray & Dermott: "Solar System Dynamics"
- Or empirically from Horizons queries over time

---

## Expected Visual Result After Fix

### Current (Broken)

- **One orbit visible:** Dashed line (osculating)
- **One orbit missing:** Dotted line (analytical) - not showing or identical
- **Both have i ≈ 2.2°** (ecliptic frame)
- **No educational value**

### After Fix

- **Two orbits visible:**
  - Dotted line: Analytical (time-varying mean elements)
  - Dashed line: Osculating (JPL Horizons snapshot)
- **Analytical:** i ≈ 0.05° in Jupiter eq → ~3.13° after transform
- **Osculating:** i ≈ 2.2° in ecliptic (no transform needed)
- **Small separation** (~1° difference due to subtle tilt)
- **Educational value restored!**

---

## Implementation Priority

### Phase 1: Get Base Elements Right ⭐

1. Query JPL Horizons for mean elements in Jupiter equatorial frame
2. Verify Io has i ≈ 0.05° (not 2.2°)
3. Store in `orbital_elements.py` or new function

### Phase 2: Add Time-Varying Function

1. Create `calculate_jupiter_satellite_elements()`
2. Start with static elements (no precession)
3. Test that transformation works

### Phase 3: Add Precession

1. Calculate or look up Ω̇ and ω̇ for each moon
2. Add time-varying updates
3. Test over months/years

### Phase 4: Verify All Moons

1. Test Galilean moons (Io, Europa, Ganymede, Callisto)
2. Test inner moons if needed
3. Document behavior

---

## Testing Strategy

### Visual Tests

1. **Io analytical orbit should:**
   - Be dotted line
   - Show i ≈ 0.05° + 3.13° transform
   - Be slightly offset from osculating
   - Center at Jupiter

2. **Io osculating orbit should:**
   - Be dashed line
   - Show i ≈ 2.2° (ecliptic)
   - No transform applied
   - Center at Jupiter

3. **Separation should:**
   - Be visible but subtle (~1°)
   - Be much smaller than Mars (3° vs 25°)
   - Be consistent across Galilean moons

### Numerical Tests

```python
# Test element sources
analytical = calculate_jupiter_satellite_elements(date, 'Io')
osculating = load_osculating_cache('Io')

print(f"Analytical i: {analytical['i']:.2f}° (Jupiter eq)")
print(f"Osculating i: {osculating['i']:.2f}° (ecliptic)")
print(f"Expected difference: ~3.13° (Jupiter tilt)")
```

---

## Questions for Tony

1. **Do you want time-varying precession?**
   - Mars has it (fast precession, educational)
   - Jupiter could have it (even faster for Io)
   - Or start with static mean elements?

2. **Which moons to prioritize?**
   - Just Galilean Four?
   - Or all eight in cache?

3. **Where should base elements come from?**
   - Query fresh from Horizons?
   - Use existing reference?
   - Create lookup table?

---

## Summary

**The gap:** Jupiter is missing the time-varying element calculation that Mars has

**The fix:** Add `calculate_jupiter_satellite_elements()` function and update Jupiter block

**The pattern:** Follow Mars implementation exactly

**The result:** Dual-orbit system that shows Jupiter equatorial → ecliptic transformation

**Next session:** Implement `calculate_jupiter_satellite_elements()` following Mars pattern

---

*"Follow the working Mars pattern. Time-varying analytical elements are the standard."*

*"Jupiter's 3.13° tilt is subtle but real - make it visible!"*

---

**Context Window: 43% used (81K/190K tokens) - Plenty of room to continue**
