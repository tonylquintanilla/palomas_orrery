# Orbital Mechanics - Paloma's Orrery

**Complete Guide: Educational Foundation + Technical Implementation**

**Last Updated:** December 4, 2025 (v1.4 - TNO Satellites & Barycenter Logic)  
**Project:** Paloma's Orrery - Astronomical Visualization Suite  
**Created by:** Tony (with Claude)

---

## About This Document

This guide serves two purposes:
1. **Educational Resource** - Understanding orbital mechanics concepts (for Paloma, students, educators)
2. **Technical Reference** - Implementation details and software architecture (for developers, contributors)

**Navigation:**
- 📚 **Part I** - Educational Foundation (concepts, physics, "why")
- 💻 **Part II** - Technical Implementation (code, architecture, "how")
- ✅ **Part III** - Validation & Accuracy (testing, limitations)

---

# PART I: EDUCATIONAL FOUNDATION 📚

*Understanding the physics and concepts behind orbital mechanics*

[... previous Part I sections 1-4 unchanged through Understanding Perturbations ...]

---

## 5. Binary Systems and Barycenters

### What is a Barycenter?

**The barycenter is the center of mass of a system** - the balance point around which all objects orbit.

Think of a see-saw:
- If two children weigh the same, the balance point is in the middle
- If one child is heavier, the balance point shifts toward them
- The heavier child sits closer to the pivot, the lighter one sits farther

**In orbital mechanics:**
- Two objects orbit their common center of mass
- The more massive object orbits closer to the barycenter
- The less massive object orbits farther from the barycenter
- Both complete their orbits in the same period!

### Most Systems Hide the Barycenter

**Sun-Jupiter example:**
- Jupiter is 1/1000th of the Sun's mass
- Barycenter is ~742,000 km from Sun's center
- But Sun's radius is 696,000 km
- **Result:** Barycenter is just outside Sun's surface, Sun barely wobbles
- We typically ignore this and say "Jupiter orbits the Sun"

**Earth-Moon example:**
- Moon is 1/81st of Earth's mass
- Barycenter is 4,671 km from Earth's center
- Earth's radius is 6,371 km
- **Result:** Barycenter is 1,700 km INSIDE Earth
- Earth wobbles, but the barycenter is underground
- **Not a true binary** - barycenter inside the primary

### Pluto-Charon: A TRUE Binary System ⭐

**What makes Pluto-Charon special:**
- Charon is 12.2% of Pluto's mass (huge ratio!)
- Barycenter is 2,035 km from Pluto's center
- But Pluto's radius is only 1,188 km
- **Result:** Barycenter is 847 km ABOVE Pluto's surface!

**This makes Pluto-Charon a true binary system** - neither object contains the barycenter!

### Binary System Parameters (New Horizons Data)

| Parameter | Value |
|-----------|-------|
| Total separation | 19,596 km (0.000131 AU) |
| Orbital period | 6.387 days |
| Mass ratio (M_Charon/M_Pluto) | 0.122 |
| Pluto orbit radius around barycenter | ~2,100 km |
| Charon orbit radius around barycenter | ~17,500 km |
| System inclination to ecliptic | ~112.9° (retrograde) |

### The See-Saw Physics

**Pluto's smaller orbit:**
- Pluto is ~8× more massive than Charon
- Like a heavy adult on a see-saw
- Sits closer to the pivot (barycenter)
- Orbit radius: ~2,100 km

**Charon's larger orbit:**
- Charon is only 12% of Pluto's mass
- Like a child on the opposite side
- Sits farther from the pivot
- Orbit radius: ~17,500 km

**The math:**
```
a_Pluto = separation × (M_Charon / M_total)
a_Charon = separation × (M_Pluto / M_total)

a_Pluto + a_Charon = total separation ✓
```

### The Tidal Lock Dance

Pluto and Charon are **mutually tidally locked**:
- They always show the same face to each other
- Both rotate with the same 6.387-day period as their orbit
- Always on opposite sides of the barycenter
- Like two dancers holding hands, spinning around their clasped grip

**No other large bodies in our solar system do this!**

### Three Ways to View the Pluto System

**Paloma's Orrery now offers three viewing modes:**

#### 1. Heliocentric (Sun-centered)
- Shows Pluto's 248-year orbit around the Sun
- Good for: Understanding Pluto's place in the solar system
- Barycenter: Not visible at this scale

#### 2. Pluto-centered
- Shows moons orbiting Pluto (which sits at origin)
- Good for: Convenient local view, "what do I see from Pluto"
- Barycenter: Yellow square marker shows offset from Pluto
- **Analogy:** Like geocentric model - convenient but hides real mechanics
- Pluto appears stationary (but it's not!)

#### 3. Barycenter-centered ⭐
- Shows TRUE orbital mechanics
- Good for: Understanding binary planet physics
- Barycenter: At the origin (the actual gravitational center!)
- **Analogy:** Like heliocentric model - shows actual physics
- **You can see Pluto's orbit!** It's not stationary!

### The Educational Revelation

**Switch from Pluto-centered to Barycenter-centered and watch what happens:**

In Pluto-centered view:
- Pluto sits still at the center
- Everything orbits around it
- Looks like traditional planet + moons

In Barycenter-centered view:
- Pluto has a visible orbit (small loop near center)
- Charon has a larger orbit (always opposite Pluto)
- They dance together around the true center of mass!

**This is exactly like the shift from geocentric to heliocentric thinking!**

### Why This Matters for Outer Moons

In Pluto-centered view:
- Styx, Nix, Kerberos, Hydra appear to orbit Pluto
- Orbits look centered on Pluto

In Barycenter-centered view:
- Outer moons orbit the barycenter (not Pluto!)
- This is the TRUE gravitational center of the system
- Their orbits are in orbital resonances with Charon:
  - Styx: ~3:1 (~20.2 days)
  - Nix: ~4:1 (~24.9 days)
  - Kerberos: ~5:1 (~32.2 days)
  - Hydra: ~6:1 (~38.2 days)

### Comparison: Binary Systems

| System | Mass Ratio | Barycenter Location | Binary? |
|--------|------------|---------------------|---------|
| Sun-Jupiter | 1:1000 | Just outside Sun | No |
| Earth-Moon | 1:81 | Inside Earth | No |
| **Pluto-Charon** | **1:8.2** | **Outside Pluto!** | **YES** |
| Alpha Centauri A-B | 1:1.2 | Between stars | Yes |

### For Paloma

*"Imagine you and a friend holding hands and spinning around. The spot where your hands grip - that's the barycenter! If your friend is much smaller than you, you barely move while they swing around you. But if your friend is almost as big as you, you BOTH swing around that grip point. That's what Pluto and Charon do - they're like two friends the same size, dancing together around their handhold!"*

---

## 6. Trans-Neptunian Objects and Their Moons 🆕

### The Outer Realm

Beyond Neptune lies a vast region of icy bodies - Trans-Neptunian Objects (TNOs). The largest of these are dwarf planets with their own satellite systems:

| System | Primary | Known Satellites |
|--------|---------|------------------|
| Pluto | Dwarf planet | Charon, Styx, Nix, Kerberos, Hydra |
| Eris | Dwarf planet | Dysnomia |
| Haumea | Dwarf planet | Hi'iaka, Namaka |
| Makemake | Dwarf planet | MK2 (S/2015 (136472) 1) |

### Why TNO Satellites Matter

**Educational value:**
- Demonstrates gravitational binding at extreme distances
- Shows diversity of small body systems
- Reveals formation history through satellite properties

**Scientific value:**
- Satellite orbits reveal primary mass
- Multiple satellites show gravitational interactions
- Haumea's moons reveal its rapid rotation history

### Viewing TNO Satellite Systems

**From the Sun (Heliocentric):**
- See the dwarf planet's orbit around the Sun
- Satellites not visible at solar system scale
- Use for comparing TNO orbits to planets

**From the Primary (e.g., Eris-centered):**
- See satellites orbiting the dwarf planet
- Osculating orbits show current orbital elements
- Actual orbits show JPL ephemeris positions

### For Paloma

*"Way out past Neptune, there are icy worlds with their own tiny moons! Eris has Dysnomia (named after the goddess of lawlessness - Eris's daughter!), Haumea has Hi'iaka and Namaka (named after Hawaiian goddesses), and Makemake has a tiny dark moon we just call MK2 because we haven't given it a proper name yet!"*

---

[... previous Part I sections 7-8 (Reference Frames, Coordinate Systems, etc.) unchanged ...]

---

# PART II: TECHNICAL IMPLEMENTATION 💻

*How the software implements orbital mechanics concepts*

[... previous Part II sections 9 (Apsidal Marker Implementation) unchanged ...]

---

## 10. Pluto-Charon Binary System Implementation

### Overview

The Pluto-Charon binary system visualization demonstrates true barycentric orbital mechanics through a three-mode viewing system.

### Architecture

```python
# Core components:
# 1. orbital_elements.py - parent_planets entry for barycenter
# 2. palomas_orrery.py - Scaling, object definition, animation
# 3. idealized_orbits.py - plot_pluto_barycenter_orbit() function
# 4. osculating_cache.json - Cached orbital elements for Pluto system
```

### Implementation Details

#### 1. Parent Planets Entry

**File:** `orbital_elements.py`

```python
parent_planets = {
    # ... other entries ...
    'Pluto': ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
    'Pluto-Charon Barycenter': ['Pluto', 'Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
    # ... other entries ...
}
```

**Key insight:** In barycenter mode, Pluto itself becomes an orbiting body!

---

#### 2. Satellite Detection Logic 🆕 (v1.4)

**The Problem:**

Pluto has `object_type='orbital'` (it's a dwarf planet orbiting the Sun), but when viewing from Pluto-Charon Barycenter, it should be treated as a satellite of that center.

**The Wrong Approach:**
```python
# DON'T DO THIS - fails for Pluto in barycenter mode
if obj_type == 'satellite' and obj['name'] in parent_planets.get(center_object_name, []):
    # Use satellite settings...
```

**The Correct Approach:**
```python
# Check parent_planets relationship, NOT object_type
if obj['name'] in parent_planets.get(center_object_name, []):
    # Use satellite settings - works for Pluto in barycenter mode!
```

**Why This Matters:**

| Object | object_type | In parent_planets['Pluto-Charon Barycenter'] | Should use satellite settings? |
|--------|-------------|----------------------------------------------|-------------------------------|
| Charon | satellite | Yes | Yes ✓ |
| Pluto | **orbital** | Yes | **Yes** ✓ |
| Neptune | orbital | No | No ✓ |

**The key insight:** An object's relationship to the current center (parent_planets) is different from its solar system classification (object_type).

**File:** `palomas_orrery.py` (plot_objects and animate_objects)

```python
# Check if this object is a satellite of the current center
# (regardless of object_type - e.g., Pluto is 'orbital' but orbits the barycenter)
elif obj['name'] in parent_planets.get(center_object_name, []):
    # Moons/orbiters of the center object - use satellite settings
    num_points = int(satellite_points) + 1
    actual_days_to_plot = settings['days_to_plot'] 
    dates_list = [date_obj + timedelta(days=float(d)) 
                for d in np.linspace(0, actual_days_to_plot, num=num_points)]
```

---

#### 3. Scaling Special Case

**File:** `palomas_orrery.py` (in `calculate_axis_range_from_orbits`)

```python
# Special case: Pluto-Charon Barycenter centered view
if center_object_name == 'Pluto-Charon Barycenter':
    max_range = 0.00065  # ~1.5x Hydra's orbit
    return [-max_range, max_range]
```

**Why this is needed:**
- Without this, scaling uses Pluto's solar orbit (~39 AU)
- Barycentric orbits are tiny (~0.0001 AU)
- Fixed scaling ensures proper visualization

---

#### 4. Dual-Mode Orbit Function

**File:** `idealized_orbits.py`

```python
def plot_pluto_barycenter_orbit(fig, object_name, date, color, 
                                 show_apsidal_markers=False, center_id='Pluto'):
    """
    Plot orbit for objects in Pluto binary system.
    
    Supports TWO center modes:
    1. center_id='Pluto' - Traditional view, moons orbit Pluto
    2. center_id='Pluto-Charon Barycenter' - Binary view, ALL objects orbit barycenter
    """
```

**The Critical Logic:**

For **Pluto-centered mode:**
- Use cached osculating elements directly
- All elements (a, e, i, ω, Ω) from JPL cache
- Standard visualization

For **Barycenter-centered mode** (Pluto/Charon):
- **Semi-major axis:** CALCULATED from mass ratio
- **Angular elements (i, ω, Ω):** FROM CACHE (same orbital plane)

```python
if is_barycenter_mode and object_name in ['Pluto', 'Charon']:
    # Calculate semi-major axis from mass ratio
    if object_name == 'Pluto':
        a = separation * mass_ratio / (1 + mass_ratio)  # ~0.0000142 AU
    else:  # Charon
        a = separation * 1.0 / (1 + mass_ratio)  # ~0.000117 AU
    
    # Get angular elements from Charon's cache (same orbital plane)
    if 'Charon' in cache:
        cached_elements = cache['Charon']['elements']
        i = cached_elements.get('i', ...)
        omega = cached_elements.get('omega', ...)
        Omega = cached_elements.get('Omega', ...)
```

**Why angular elements from cache?**

The orbital plane orientation is the same whether measured from Pluto or the barycenter. Only the semi-major axis differs. Using hardcoded approximations caused the calculated orbit to misalign with the JPL trajectory.

| Parameter | Source | Why |
|-----------|--------|-----|
| **a** | Calculated | Different distance from barycenter |
| **e** | Fixed ~0.0002 | Nearly circular, doesn't change |
| **i, ω, Ω** | Cache | Same plane regardless of center |

---

#### 5. Barycenter Marker (Pluto-centered view)

**File:** `idealized_orbits.py`

```python
def add_pluto_barycenter_marker(fig, date, charon_position=None):
    """
    Add the Pluto-Charon barycenter marker to Pluto-centered view.
    
    The barycenter is ~2,035 km from Pluto's center toward Charon.
    This is OUTSIDE Pluto's surface (radius ~1,188 km)!
    """
    BARYCENTER_DIST_AU = 0.0000137  # ~2,050 km
    
    # Calculate position along Pluto→Charon line
    if charon_position:
        # Unit vector toward Charon × barycenter distance
        ...
```

**Visual:** Yellow open square showing the barycenter offset from Pluto

---

#### 6. Animation Support

**File:** `palomas_orrery.py` (animation section)

```python
# Update Pluto-Charon Barycenter position (derived from Charon)
if 'Pluto-Charon Barycenter' in trace_indices and center_object_name == 'Pluto':
    # Barycenter is always along Pluto→Charon line at fixed distance
    BARYCENTER_DIST_AU = 0.0000137
    
    # Calculate from Charon's animated position
    bary_x = BARYCENTER_DIST_AU * (cx / charon_dist)
    bary_y = BARYCENTER_DIST_AU * (cy / charon_dist)
    bary_z = BARYCENTER_DIST_AU * (cz / charon_dist)
```

**Result:** In animated Pluto-centered view, the barycenter marker moves with Charon, showing the system's rotation.

---

### Hover Text Design

**Barycenter mode - Pluto:**
```
Pluto's Osculating Orbit around Barycenter
The smaller orbit of the binary pair

Orbital Elements (Epoch: 2025-11-26):
a = 0.0000142 AU (2131 km) [calculated]
e = 0.0002 (nearly circular)
i = 112.9° to ecliptic [osculating]

Why Pluto's orbit is smaller:
Pluto is ~8× more massive than Charon,
so it orbits closer to the barycenter.

Note: Semi-major axis calculated from
mass ratio; angles from Charon's osculating
elements (same orbital plane).
```

**Barycenter mode - Charon:**
```
Charon's Osculating Orbit around Barycenter
The larger orbit of the binary pair

Why Charon's orbit is larger:
Charon is only 12% of Pluto's mass,
so it orbits farther from the barycenter.

The Dance:
Watch Pluto and Charon orbit together,
always on opposite sides of their
mutual center of mass. Tidally locked,
they always show the same face to each other.
```

---

### Testing & Validation

**Visual alignment test:**
- Charon orbit line must align with JPL trajectory
- Initially failed due to hardcoded angular elements
- Fixed by using cached osculating elements for i, ω, Ω

**Verification checklist:**
| Test | Status |
|------|--------|
| Pluto-centered: orbits align | ✅ |
| Barycenter-centered: orbits align | ✅ |
| Pluto visible orbit in barycenter mode | ✅ |
| Correct semi-major axis ratio | ✅ |
| Barycenter marker position | ✅ |
| Animation (Pluto-centered) | ✅ |
| Animation (Barycenter-centered) | ✅ |

---

### Lessons Learned

**1. Angular Elements Are Frame-Independent**

The orbital plane orientation (i, ω, Ω) is the same whether measured from Pluto or the barycenter. This is why we can use Charon's cached osculating elements for both bodies.

**2. Visual Verification Catches Physics Errors**

The angular mismatch between calculated orbit and JPL trajectory was immediately visible - code review wouldn't have caught it.

**3. Osculating Elements Are Gold**

JPL's osculating elements provide real, current orbital plane orientation that hardcoded approximations cannot match.

**4. object_type ≠ Orbital Relationship**

An object's `object_type` classification ('orbital', 'satellite') is its solar system role. Its relationship to the current viewing center is determined by `parent_planets`. These are independent!

---

## 11. TNO Satellite System Implementation 🆕

### Overview

Trans-Neptunian Objects with satellites require special handling due to JPL Horizons ephemeris coverage limitations and the dual nature of their identifiers.

### The Dual ID Architecture

**Problem:** TNO system barycenter IDs have limited ephemeris coverage (~2030), but heliocentric IDs extend much further (~2500).

**Solution:** Objects have two IDs with different purposes:

```python
{
    'name': 'Haumea',
    'id': '20136108',           # System barycenter - for satellite-centered views
    'helio_id': '2003 EL61',    # Heliocentric - for Sun-centered views
    'id_type': 'majorbody',
    ...
}
```

### JPL Horizons ID Types and Coverage

| ID Type | Example | Ephemeris Coverage | Use Case |
|---------|---------|-------------------|----------|
| System Barycenter | `20136108` | ~2030 | Viewing from the TNO |
| Heliocentric | `2003 EL61` | ~2500 | Viewing from Sun |
| Satellite | `20136108` (child) | ~2030 | Moon orbits |

### Implementation

**File:** `palomas_orrery.py`

```python
# Use helio_id for Sun-centered plots if available (longer ephemeris coverage)
# System barycenter IDs (e.g., 20136108) only have data to ~2030
# Heliocentric IDs (e.g., 2003 EL61) have data to ~2500
fetch_id = obj['id']
fetch_id_type = obj.get('id_type')
if center_object_name == 'Sun' and 'helio_id' in obj:
    fetch_id = obj['helio_id']
    fetch_id_type = 'smallbody'  # helio_ids are smallbody designations
```

**Applied in three locations:**
1. `plot_actual_orbits()` - Static orbit plotting
2. Animation trajectory fetch - Object positions over time
3. `pad_trajectory()` call - Animation trajectory padding

### TNO Object Definitions

**File:** `palomas_orrery.py`

```python
# Eris system
{'name': 'Eris', 'id': '20136199', 'helio_id': '2003 UB313', ...},
{'name': 'Dysnomia', 'id': '20136199', 'id_type': 'majorbody', ...},

# Haumea system  
{'name': 'Haumea', 'id': '20136108', 'helio_id': '2003 EL61', ...},
{'name': "Hi'iaka", 'id': '20136108', 'id_type': 'majorbody', ...},
{'name': 'Namaka', 'id': '20136108', 'id_type': 'majorbody', ...},

# Makemake system
{'name': 'Makemake', 'id': '20136472', 'helio_id': '2005 FY9', ...},
{'name': 'MK2', 'id': '20136472', 'id_type': 'majorbody', ...},
```

### Parent Planets Registry

**File:** `orbital_elements.py`

```python
parent_planets = {
    # ... other entries ...
    'Eris': ['Dysnomia'],
    'Haumea': ["Hi'iaka", 'Namaka'],
    'Makemake': ['MK2'],
    # ... other entries ...
}
```

### Why Short Names for Satellites

**Problem:** Long official designations don't fit in UI elements.

| Official Designation | Short Name | Why |
|---------------------|------------|-----|
| (136199) Eris I Dysnomia | Dysnomia | Fits in legend |
| (136108) Haumea I Hi'iaka | Hi'iaka | Fits in checkbox |
| S/2015 (136472) 1 | MK2 | Only practical option |

---

## 12. Outer Planet Moon Visualization 🆕

### Osculating-Only Architecture

**Decision:** Neptune, Saturn, Uranus, and Pluto system moons display **only osculating orbits** - analytical orbits are not shown.

**Rationale:**
1. **Osculating elements** come from JPL Horizons - actual current orbital state
2. **Analytical elements** are mean/reference values - approximations
3. For outer planet moons, osculating provides more accurate visualization
4. Reduces visual clutter (no dual-orbit system needed)

### Implementation

**File:** `idealized_orbits.py`

The if/elif chain for moon orbit plotting:

```python
# Neptune moons - osculating only
if moon_name in NEPTUNE_MOON_NAMES:
    plot_neptune_moon_osculating_orbit(...)
    return  # Don't fall through to analytical

# Saturn moons - osculating only  
elif moon_name in SATURN_MOON_NAMES:
    plot_saturn_moon_osculating_orbit(...)
    return

# Uranus moons - osculating only
elif moon_name in URANUS_MOON_NAMES:
    plot_uranus_moon_osculating_orbit(...)
    return

# Pluto system - osculating only (barycenter mode)
elif center_id == 'Pluto-Charon Barycenter' and moon_name in PLUTO_BARYCENTER_ORBITERS:
    plot_pluto_barycenter_orbit(...)
    return

# Other moons - may have dual orbit system
else:
    # Analytical orbit plotting...
```

**Critical:** The `elif` chain ensures each moon type is handled once and returns, preventing fall-through to analytical orbit plotting.

### Which Moons Show Dual Orbits?

| System | Dual Orbit (Analytical + Osculating) | Osculating Only |
|--------|--------------------------------------|-----------------|
| Earth | Moon ✓ | - |
| Mars | Phobos ✓, Deimos ✓ | - |
| Jupiter | Galilean moons ✓ | - |
| Saturn | - | All moons |
| Uranus | - | All moons |
| Neptune | - | All moons |
| Pluto | - | All moons (barycenter mode) |

**Why the difference?**
- Inner system moons: Educational value in showing analytical vs osculating
- Outer system moons: Osculating sufficient, reduces complexity

---

[... previous Part II sections (Known Issues) unchanged ...]

---

# PART III: VALIDATION & ACCURACY ✅

[... previous Part III sections unchanged ...]

---

## Conclusion

Paloma's Orrery combines educational clarity with technical accuracy to visualize the intricate dance of celestial mechanics. From Kepler's elegant laws to the complex perturbations that govern the Moon's orbit, every feature serves both learning and precision.

**Version 1.4 extends TNO satellite support** with proper ephemeris ID selection and documents the architectural decisions for satellite detection and outer planet moon visualization.

**For Educators & Students:** Part I now includes TNO satellite systems and their educational value.

**For Developers & Contributors:** Part II documents the dual ID architecture, parent_planets logic, and osculating-only decisions for outer moons.

**For Scientists:** Part III validates accuracy through visual alignment testing and documents ephemeris coverage limitations.

This document will evolve with the project. Contributions, corrections, and suggestions are welcome!

---

## References & Further Reading

[... previous references unchanged ...]

### Additional References (v1.4)

- Brown, M.E. et al. (2006) "Satellites of the largest Kuiper belt objects" - ApJ 639(1)
- Ragozzine, D. & Brown, M.E. (2009) "Orbits and Masses of the Satellites of the Dwarf Planet Haumea" - AJ 137(6)
- Parker, A.H. et al. (2016) "Discovery of a Makemakean Moon" - ApJ 825(1)

---

[... previous Project Links unchanged ...]

---

**Document Version:** 1.4 (TNO Satellites & Barycenter Logic)  
**Date:** December 4, 2025  
**Maintained By:** Tony  
**Contributors:** Claude (AI assistant)

**Version History:**
- **v1.0** (Nov 20, 2025): Initial consolidated document with Moon dual-orbit system
- **v1.1** (Nov 22, 2025): Mars dual-orbit implementation complete, smart reference frame detection documented, performance metrics added
- **v1.2** (Nov 23, 2025): Apsidal marker enhancements with intelligent perturbation analysis, orbit stability measurements, Keplerian vs actual position comparison system, epoch-labeled legends, parent-specific terminology throughout
- **v1.3** (Nov 26, 2025): Pluto-Charon binary system with three-mode visualization (heliocentric, Pluto-centered, barycenter-centered), true barycentric orbital mechanics demonstration, educational content on binary systems and mass ratios
- **v1.4** (Dec 4, 2025): TNO satellite systems (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2), dual ID architecture for ephemeris coverage, parent_planets satellite detection logic, osculating-only visualization for outer planet moons

*"Data preservation is climate action."*  
*"Sky's the limit! Or stars are the limit!" - Tony*
*"Only the barycenter approach represents the actual orbital mechanics!" - Nov 26, 2025*
*"An object's type is not the same as its orbital relationship." - Dec 4, 2025*

---

## What's New in v1.4 (December 4, 2025) 🆕

### Major Features Added

1. **TNO Satellite Systems**
   - Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2
   - Full support for viewing from Sun or from TNO
   - Educational content about outer solar system moons

2. **Dual ID Architecture**
   - Objects have `id` (system barycenter) and `helio_id` (heliocentric)
   - Automatic selection based on viewing center
   - Extends animation capability from 2030 to ~2500 for Sun-centered views

3. **Satellite Detection Logic Fix**
   - Changed from `object_type == 'satellite'` to `parent_planets[center]` check
   - Pluto now correctly treated as satellite when viewing from barycenter
   - Architectural fix that applies to any future binary/complex systems

4. **Outer Planet Moon Visualization**
   - Neptune, Saturn, Uranus, Pluto moons show osculating orbits only
   - Documented decision rationale
   - Clear if/elif chain prevents fall-through to analytical orbits

### Architectural Highlights

**The Dual ID Pattern:**
```python
# System barycenter ID - limited ephemeris
'id': '20136108'  # Only to ~2030

# Heliocentric ID - extended ephemeris  
'helio_id': '2003 EL61'  # To ~2500
```

**The Satellite Detection Fix:**
```python
# OLD: Checks object classification
if obj_type == 'satellite' and obj['name'] in parent_planets[center]:

# NEW: Checks orbital relationship to center
if obj['name'] in parent_planets.get(center_object_name, []):
```

### Educational Highlights

**For Paloma:**
*"Way out past Neptune, there are icy worlds with their own tiny moons! Eris has Dysnomia, Haumea has Hi'iaka and Namaka, and Makemake has a tiny dark moon we just call MK2!"*

**Key Insight:**
An object's solar system classification (planet, dwarf planet, moon) is different from its relationship to your current viewing center. Pluto is a dwarf planet, but when you view from the Pluto-Charon barycenter, Pluto becomes an orbiting body!

### Lessons Learned

1. JPL Horizons has different ephemeris coverage for different ID types
2. `object_type` is classification, `parent_planets` is orbital relationship
3. Outer planet moons don't need dual orbits - osculating is sufficient
4. Short names matter for UI - "MK2" fits where "S/2015 (136472) 1" doesn't

---

**Total additions:** ~200 lines of technical documentation
**Focus areas:** TNO satellites, ID architecture, satellite detection logic
**Educational value:** Extends visualization to outer solar system moons
**Quotable:** *"An object's type is not the same as its orbital relationship."*

---
