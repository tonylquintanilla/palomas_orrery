# Pluto-Charon Binary System Implementation

**Date:** November 24, 2025  
**Status:** Ready to implement  
**Approach:** Barycenter-centered binary planet system (like TOI-1338)  
**Pattern:** Osculating-only orbits (like Saturn)

---

## The Binary Planet Discovery

**Charon is NOT just a moon - Pluto-Charon is a binary planet system!**

| Property | Earth-Moon | Pluto-Charon |
|----------|------------|--------------|
| Mass ratio | Moon/Earth = 0.0123 (1.2%) | Charon/Pluto = 0.117 (11.7%) |
| Barycenter location | 1,700 km from Earth center (**inside Earth**) | 960 km from Pluto center (**outside Pluto!**) |
| System type | Planet with large moon | **Binary planet** |

**This is THE defining characteristic of the Pluto system - we should show it!**

---

## Educational Vision

**For Paloma (and everyone):**
- "Pluto and Charon dance around each other!"
- "They both move - watch them orbit together"
- "The point they orbit is between them - that's the barycenter"
- "No other planet in our solar system does this"

**Educational value:**
- Demonstrates barycenter physics (not widely known)
- Shows real orbital mechanics
- Unique in our solar system
- Perfect teachable moment

---

## Why Osculating-Only for Pluto

**Pluto pole orientation:**
- RA: 132.99° (vs ecliptic pole ~270°)
- Angular separation: ~137° from ecliptic pole
- **Conclusion:** Even worse than Saturn - analytical transformations will fail

**Additional complexity:**
- Extreme axial tilt: 122.53° (retrograde rotation like Uranus)
- Binary planet system (Charon is 1/8 Pluto's mass)
- All moons co-planar in Pluto's equator

**Solution:** Skip analytical orbits, use osculating only (like Saturn)

---

## Pluto's Five Moons

| Moon | Horizons ID | Discovery | Size | Period (days) | Notes |
|------|-------------|-----------|------|---------------|-------|
| Charon | 901 | 1978 | ~1,212 km | 6.387 | Largest, binary partner |
| Styx | 905 | 2012 | ~10-25 km | 20.162 | Tiny, irregular |
| Nix | 902 | 2005 | ~40 km | 24.856 | Elongated |
| Kerberos | 904 | 2011 | ~12-30 km | 32.168 | Dark surface |
| Hydra | 903 | 2005 | ~55 km | 38.202 | Most distant |

**All discovered/refined by Hubble and New Horizons (2015 flyby)**

---

## Three Viewing Modes (All Supported!)

### Mode 1: Sun-Centered (Normal Solar System View)
```
Center: Sun
Objects: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
```
**What happens:** Pluto orbits the Sun (standard planet behavior)

**Code path:** Main orbital plotting loop (lines 3156+)
- Pluto is NOT in any `parent_planets` satellite lists
- Passes satellite check → plots as normal orbital object
- Uses standard Keplerian mechanics around Sun
- **Already works! No special code needed!**

### Mode 2: Pluto-Centered (Traditional Satellite View)
```
Center: Pluto
Objects: Charon, Styx, Nix, Kerberos, Hydra (satellites)
```
**What happens:** Moons orbit Pluto (standard satellite system)

**Code path:** Satellite loop with `center_id == 'Pluto'`
- Pluto is center (stationary)
- Only moons in `PLUTO_MOONS` list are plotted
- Osculating-only orbits (no analytical due to pole orientation)

### Mode 3: Barycenter-Centered (Binary Planet View) ⭐
```
Center: Pluto-Charon Barycenter
Objects: Pluto, Charon, Styx, Nix, Kerberos, Hydra (all orbit barycenter)
```
**What happens:** Pluto and all moons orbit the barycenter (binary system)

**Code path:** Satellite loop with `center_id == 'Pluto-Charon Barycenter'`
- Barycenter is center (stationary)
- ALL objects in `PLUTO_BARYCENTER_ORBITERS` list are plotted
- **Including Pluto itself!** (becomes an orbiting object)
- Shows the "dance" of Pluto and Charon

---

## Implementation Strategy

Following the **TOI-1338 barycenter pattern** for binary mode:


### Barycenter Mode Implementation

When user selects **"Pluto-Charon Barycenter"** from center dropdown:
- Center: Pluto-Charon Barycenter (stationary)
- **Pluto orbits barycenter** (tight orbit, 6.387 day period)
- **Charon orbits barycenter** (larger orbit, same 6.387 day period)
- **Other moons orbit barycenter** (wider orbits)
- Both Pluto and Charon are moving!

### Traditional Mode Implementation

When user selects **"Pluto"** from center dropdown:
- Center: Pluto (stationary)
- Moons orbit Pluto
- Standard satellite system behavior

### Sun-Centered Mode (Automatic)

When user selects **"Sun"** from center dropdown:
- Pluto orbits Sun (standard planet)
- No special code needed - works automatically!
- Uses main orbital plotting loop, not satellite loop

**User gets to choose which view in the center dropdown menu!**

---

## JPL Horizons IDs

```python
# Pluto system components
PLUTO_BARYCENTER = '9'     # Pluto system barycenter (center for binary mode)
PLUTO_BODY = '999'         # Pluto body center (orbits barycenter in binary mode)

# Moons (always relative to current center)
CHARON = '901'
NIX = '902'
HYDRA = '903'
KERBEROS = '904'
STYX = '905'
```

**Query pattern for barycenter mode:**
- Center: `@9` (Pluto system barycenter)
- Objects: `999, 901, 902, 903, 904, 905` (all relative to `@9`)

---

## Implementation Steps

### Step 1: Add Barycenter Object

**File:** `palomas_orrery.py`  
**Location:** Around line 2290 (with other checkbox variables)

**Add variable:**
```python
pluto_barycenter_var = tk.IntVar(value=0)
```

**Location:** Around line 2392 (in objects list, near Pluto)

**Add barycenter object:**
```python
# Pluto-Charon Binary System
{'name': 'Pluto-Charon Barycenter', 'id': '9', 'var': pluto_barycenter_var, 
 'color': color_map('Pluto'), 'symbol': 'diamond', 'object_type': 'barycenter',
 'description': 'Center of mass for Pluto-Charon binary planet system'},
```

**Update Pluto object** (mark as can orbit barycenter):
```python
{'name': 'Pluto', 'id': '999', 'var': pluto_var, 
 'color': color_map('Pluto'), 'symbol': 'circle', 
 'object_type': 'dwarf_planet',
 'barycenter_system': True,  # Can orbit barycenter
 'barycenter_id': '9',       # Which barycenter
 'description': 'Dwarf planet; in binary system with Charon'},
```

---

### Step 2: Create Pluto Moon Lists

**File:** `idealized_orbits.py`  
**Location:** Near line 48 (after SATURN_MOONS)

**Add:**
```python
# Pluto moons - osculating-only display (pole RA=132.99° far from ecliptic ~270°)
# Note: When "Pluto-Charon Barycenter" is center, Charon and Pluto both orbit the barycenter
PLUTO_MOONS = ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']

# For barycenter mode: objects that orbit the Pluto system barycenter
PLUTO_BARYCENTER_ORBITERS = ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra']
```

---

### Step 3: Create Barycenter Orbit Function

**File:** `idealized_orbits.py`  
**Location:** After Saturn functions (around line 1190)

**Add:**
```python
def plot_pluto_barycenter_orbit(fig, object_name, date, color, show_apsidal_markers=False):
    """
    Plot osculating orbit for objects in Pluto binary system (barycenter-centered).
    
    When "Pluto-Charon Barycenter" is the center:
    - Pluto orbits the barycenter (tight orbit)
    - Charon orbits the barycenter (larger orbit, same period)
    - Other moons orbit the barycenter (wider orbits)
    
    All osculating elements from JPL Horizons are in ECLIPTIC frame (J2000.0).
    """
    
    PLUTO_BARYCENTER_IDS = {
        'Pluto': '999',    # Body center (orbits barycenter)
        'Charon': '901',   # Largest moon (binary partner)
        'Styx': '905',     # Tiny irregular
        'Nix': '902',      # Elongated
        'Kerberos': '904', # Dark surface
        'Hydra': '903'     # Most distant
    }

    horizons_id = PLUTO_BARYCENTER_IDS.get(object_name)
    if not horizons_id:
        print(f"Warning: No Horizons ID for {object_name}", flush=True)
        return fig
    
    try:
        from osculating_cache_manager import load_cache
        
        print(f"\n[OSCULATING] Loading cached elements for {object_name}...", flush=True)
        cache = load_cache()
        
        if object_name in cache:
            elements = cache[object_name]['elements']
            print(f"  ✓ Using cached osculating elements", flush=True)
        else:
            print(f"  Warning: No osculating elements in cache for {object_name}", flush=True)
            return fig
        
        a = elements.get('a', 0)
        e = elements.get('e', 0)
        i = elements.get('i', 0)
        omega = elements.get('omega', 0)
        Omega = elements.get('Omega', 0)
        epoch = elements.get('epoch', 'unknown')
       
        print(f"  Plotting osculating: i={i:.4f}° (ecliptic), epoch={epoch}", flush=True)
        
        theta = np.linspace(0, 2*np.pi, 360)
        r = a * (1 - e**2) / (1 + e * np.cos(theta))
        
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        
        i_rad = np.radians(i)
        omega_rad = np.radians(omega)
        Omega_rad = np.radians(Omega)
        
        # Standard Keplerian rotation sequence
        x_temp, y_temp, z_temp = rotate_points(x_orbit, y_orbit, z_orbit, omega_rad, 'z')
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        x_final, y_final, z_final = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Build hover text with object-specific details
        if object_name == 'Pluto':
            hover_text_osc = (
                f"<b>Pluto Osculating Orbit</b><br>"
                f"<i>(around Pluto-Charon barycenter)</i><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"Period: 6.387 days (tidally locked with Charon)<br>"
                f"<br><i>Binary planet system: Pluto and Charon<br>"
                f"both orbit their mutual center of mass.<br>"
                f"Barycenter is 960 km from Pluto's center<br>"
                f"(outside Pluto's surface!).</i>"
            )
        elif object_name == 'Charon':
            hover_text_osc = (
                f"<b>Charon Osculating Orbit</b><br>"
                f"<i>(around Pluto-Charon barycenter)</i><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"Period: 6.387 days (same as Pluto)<br>"
                f"<br><i>Charon: Pluto's binary partner<br>"
                f"Mass: 11.7% of Pluto's mass<br>"
                f"Discovered 1978 | Diameter: ~1,212 km<br>"
                f"Both Pluto and Charon are tidally locked.</i>"
            )
        else:
            hover_text_osc = (
                f"<b>{object_name} Osculating Orbit</b><br>"
                f"<i>(around Pluto-Charon barycenter)</i><br>"
                f"Epoch: {epoch}<br>"
                f"a={a:.6f} AU, e={e:.6f}<br>"
                f"i={i:.4f}° (J2000 ecliptic)<br>"
                f"<br><i>Osculating = instantaneous Keplerian fit<br>"
                f"from JPL Horizons orbital elements.<br>"
                f"All Pluto moons orbit the barycenter<br>"
                f"of the Pluto-Charon binary system.</i>"
            )

        fig.add_trace(go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='lines',
            line=dict(color=color, width=2, dash='dash'),
            name=f'{object_name} Osculating Orbit (Epoch: {epoch})',
            text=[hover_text_osc] * len(x_final),
            customdata=[hover_text_osc] * len(x_final),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
        
        print(f"  ✓ Osculating orbit plotted (ecliptic frame)", flush=True)
        return fig
        
    except Exception as e:
        print(f"Error plotting osculating orbit for {object_name}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return fig
```

---

### Step 4: Add Logic to Main Plotting Loop

**File:** `idealized_orbits.py`  
**Location:** In main loop (around line 2550)

**Add after Saturn block:**

```python
            # Special handling for Pluto-Charon BINARY SYSTEM
            # Two modes: traditional Pluto-centered, or barycenter-centered
            
            # Mode 1: Barycenter-centered (binary planet mode)
            if center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:
                # In barycenter mode, BOTH Pluto and Charon orbit the barycenter
                # Plus the four smaller moons (Styx, Nix, Kerberos, Hydra)
                if date:
                    fig = plot_pluto_barycenter_orbit(
                        fig,
                        moon_name,  # Can be 'Pluto', 'Charon', or other moons
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)
            
            # Mode 2: Traditional Pluto-centered (for compatibility)
            elif moon_name in PLUTO_MOONS and center_id == 'Pluto':
                # Skip analytical orbit - only plot osculating
                # (Pluto pole RA=132.99° far from ecliptic, analytical transformations fail)
                if date:
                    fig = plot_pluto_barycenter_orbit(  # Same function works for both modes!
                        fig,
                        moon_name,
                        date,
                        color_map(moon_name),
                        show_apsidal_markers=show_apsidal_markers
                    )
                else:
                    print(f"  Warning: Could not plot osculating orbit for {moon_name} (missing date)", flush=True)
```

---

## Testing Checklist

### Mode 1: Sun-Centered (Center = "Sun")
- [ ] Pluto orbits Sun normally
- [ ] Pluto's orbital elements used (a=39.5 AU, e=0.25, etc.)
- [ ] Pluto position matches ephemeris
- [ ] No satellites visible (Charon, etc. are not Sun satellites)
- [ ] **Should work without any code changes!**

### Mode 2: Traditional Pluto-Centered (Center = "Pluto")
- [ ] Pluto is center (stationary)
- [ ] Charon orbits Pluto
- [ ] Four small moons orbit Pluto
- [ ] All show osculating orbits (dashed) vs actual (solid)
- [ ] No analytical orbits (pole orientation issue)

### Mode 3: Binary System (Center = "Pluto-Charon Barycenter")
- [ ] Barycenter is center (stationary, diamond marker)
- [ ] **Pluto orbits barycenter** (small orbit)
- [ ] **Charon orbits barycenter** (larger orbit, same period as Pluto)
- [ ] Four small moons orbit barycenter (wider orbits)
- [ ] All show osculating orbits (dashed) vs actual (solid)
- [ ] Hover texts explain binary system
- [ ] "Dancing" motion visible in animation

### Data Requirements
- [ ] Fetch osculating elements for all objects relative to `@9`:
  - Pluto (999)
  - Charon (901)
  - Styx (905)
  - Nix (902)
  - Kerberos (904)
  - Hydra (903)

---

## Expected Visual Results

### Sun-Centered Mode (Center = Sun)
```
                 Pluto
                  o  (orbiting Sun)
                /
              /
    Sun · (center)
      \
       \
        Neptune  Uranus
```
**Standard solar system view - Pluto as planet**

### Traditional Mode (Center = Pluto)
```
        Pluto (center, stationary)
         /  |  \
    Charon  |   Hydra
    Styx   Nix  Kerberos
```
**Standard satellite system - moons orbit Pluto**

### Binary Mode (Center = Barycenter) ⭐
```
           Hydra
          /
    Pluto · Charon  (both moving!)
         /  |  \
      Styx Nix Kerberos
      
    · = barycenter (center, stationary)
```
**Binary planet system - everyone orbits barycenter**

**The "dance":**
- Pluto and Charon orbit opposite sides of barycenter
- Period: 6.387 days (both synchronized)
- Pluto's orbit: smaller (closer to barycenter)
- Charon's orbit: larger (farther from barycenter)
- Mass ratio determines orbit sizes!

---

## Educational Story Points

### For Paloma (Age 7-8)
- "Pluto and Charon dance around each other!"
- "They both move in circles around a point between them"
- "That point is called the barycenter - it's like a balance point"
- "Watch them orbit together - they never let go of each other"
- "No other planet in our solar system does this special dance"

### For Students/Public
- Binary planet system (barycenter outside Pluto)

- Mass ratio determines orbit size (Charon has larger orbit)
- Tidal locking (both always show same face to each other)
- Unique in our solar system
- New Horizons mission (2015) refined our understanding

### For Advanced
- Barycenter calculation: r_Pluto/r_Charon = M_Charon/M_Pluto = 0.117
- Barycenter location: 960 km from Pluto center (1,186 km radius, so outside!)
- Reduced mass system dynamics
- L1/L2 Lagrange points between them

---

## Physics Details

### Barycenter Location
```
Mass ratio: m_Charon/m_Pluto = 0.117
Distance ratio: r_Pluto/r_Charon = 0.117

Total separation: ~19,600 km
Pluto's orbit radius: ~2,100 km
Charon's orbit radius: ~17,500 km
Barycenter: 960 km from Pluto's center (outside Pluto!)
```

### Tidal Locking
- Both Pluto and Charon are tidally locked
- Period: 6.387 days for both
- They always show the same face to each other
- Like a cosmic waltz!

### System Formation
- Likely formed from giant impact (like Earth-Moon)
- Impact debris coalesced into Charon
- Four small moons formed from leftover material
- All coplanar suggests single formation event

---

## Files to Modify

| File | Change | Lines |
|------|--------|-------|
| `palomas_orrery.py` | Add pluto_barycenter_var | ~2290 |
| `palomas_orrery.py` | Add barycenter object | ~2392 |
| `palomas_orrery.py` | Update Pluto object | ~2392 |
| `idealized_orbits.py` | Add PLUTO_MOONS lists | ~49 |
| `idealized_orbits.py` | Add plot_pluto_barycenter_orbit() | ~1190+ |
| `idealized_orbits.py` | Add Pluto cases to main loop | ~2555+ |

---

## Token Budget

| Metric | Value |
|--------|-------|
| **Used** | ~121,000 (64%) |
| **Remaining** | ~69,000 (36%) |
| **Status** | ✅ Good runway |

---

## Summary

**Pluto-Charon binary system implementation supports three modes:**

1. **Sun-centered mode (automatic):**
   - Pluto orbits Sun normally
   - Standard planet behavior
   - Already works - no code changes needed!

2. **Traditional Pluto-centered:**
   - Pluto is center (stationary)
   - Moons orbit Pluto (standard satellites)
   - Osculating-only (pole orientation issue)

3. **Binary barycenter mode (NEW!):**
   - Barycenter is center
   - Pluto + moons orbit barycenter
   - Shows the "dance"
   - Educational gold!

**Educational gold:**
- Shows barycenter physics
- Demonstrates binary planet system
- Unique in solar system
- Perfect for Paloma!

**Technical approach:**
- Follow TOI-1338 barycenter pattern
- Osculating-only orbits (pole orientation issue)
- Three modes supported automatically
- User chooses in center dropdown

**Recommendation:** Implement binary mode - it's what makes Pluto special! 🪐✨

---

*"Pluto and Charon dance around each other - watch them orbit together!"*

*"The barycenter is outside Pluto - that's what makes it a binary planet system!"*

*"And when you view from the Sun, Pluto is just a planet doing its thing around the solar system!"*
