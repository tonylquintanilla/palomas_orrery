# Orbital Mechanics - Paloma's Orrery

**Complete Guide: Educational Foundation + Technical Implementation**

**Last Updated:** November 26, 2025 (v1.3 - Pluto-Charon Binary System)  
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

## 5. Binary Systems and Barycenters 🆕

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

[... previous Part I sections 6-8 (Reference Frames, Coordinate Systems, etc.) unchanged ...]

---

# PART II: TECHNICAL IMPLEMENTATION 💻

*How the software implements orbital mechanics concepts*

[... previous Part II sections 9 (Apsidal Marker Implementation) unchanged ...]

---

## 10. Pluto-Charon Binary System Implementation 🆕

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

#### 2. Scaling Special Case

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

#### 3. Barycenter Object Definition

**File:** `palomas_orrery.py`

```python
{'name': 'Pluto-Charon Barycenter', 'id': '9', 'var': pluto_barycenter_var, 
 'color': 'yellow', 'symbol': 'square-open', 'object_type': 'barycenter',
 'description': 'Center of mass for Pluto-Charon binary planet system'},
```

**JPL Horizons ID @9:** The Pluto system barycenter

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

---

### Lessons Learned

**1. Angular Elements Are Frame-Independent**

The orbital plane orientation (i, ω, Ω) is the same whether measured from Pluto or the barycenter. This is why we can use Charon's cached osculating elements for both bodies.

**2. Visual Verification Catches Physics Errors**

The angular mismatch between calculated orbit and JPL trajectory was immediately visible - code review wouldn't have caught it.

**3. Osculating Elements Are Gold**

JPL's osculating elements provide real, current orbital plane orientation that hardcoded approximations cannot match.

---

[... previous Part II sections 11 (Known Issues) unchanged ...]

---

# PART III: VALIDATION & ACCURACY ✅

[... previous Part III sections unchanged ...]

---

## Conclusion

Paloma's Orrery combines educational clarity with technical accuracy to visualize the intricate dance of celestial mechanics. From Kepler's elegant laws to the complex perturbations that govern the Moon's orbit, every feature serves both learning and precision.

**Version 1.3 introduces the Pluto-Charon binary system visualization**, demonstrating true barycentric orbital mechanics through a three-mode viewing system. The shift from Pluto-centered to barycenter-centered view mirrors the historical shift from geocentric to heliocentric thinking - revealing that Pluto itself orbits!

**For Educators & Students:** Part I now includes comprehensive coverage of binary systems, barycenters, and what makes Pluto-Charon unique in our solar system.

**For Developers & Contributors:** Part II documents the dual-mode orbit function, the critical fix for angular elements, and the complete implementation architecture.

**For Scientists:** Part III validates accuracy through visual alignment testing and acknowledges the elegant solution of using cached osculating elements for orbital plane orientation.

This document will evolve with the project. Contributions, corrections, and suggestions are welcome!

---

## References & Further Reading

[... previous references unchanged ...]

### Additional References (v1.3)

- Stern, S.A. et al. (2015) "The Pluto system: Initial results from its exploration by New Horizons" - Science 350(6258)
- Buie, M.W. et al. (2006) "Orbits and photometry of Pluto's satellites" - Astronomical Journal 132(1)
- Tholen, D.J. & Buie, M.W. (1997) "The Orbit of Charon" - Icarus 125(2)
- Weaver, H.A. et al. (2016) "The small satellites of Pluto" - Science 351(6279)

---

[... previous Project Links unchanged ...]

---

**Document Version:** 1.3 (Pluto-Charon Binary System)  
**Date:** November 26, 2025  
**Maintained By:** Tony  
**Contributors:** Claude (AI assistant)

**Version History:**
- **v1.0** (Nov 20, 2025): Initial consolidated document with Moon dual-orbit system
- **v1.1** (Nov 22, 2025): Mars dual-orbit implementation complete, smart reference frame detection documented, performance metrics added
- **v1.2** (Nov 23, 2025): Apsidal marker enhancements with intelligent perturbation analysis, orbit stability measurements, Keplerian vs actual position comparison system, epoch-labeled legends, parent-specific terminology throughout
- **v1.3** (Nov 26, 2025): Pluto-Charon binary system with three-mode visualization (heliocentric, Pluto-centered, barycenter-centered), true barycentric orbital mechanics demonstration, educational content on binary systems and mass ratios

*"Data preservation is climate action."*  
*"Sky's the limit! Or stars are the limit!" - Tony*
*"Only the barycenter approach represents the actual orbital mechanics!" - Nov 26, 2025*

---

## What's New in v1.3 (November 26, 2025) 🆕

### Major Features Added

1. **Pluto-Charon Binary System Visualization**
   - Three viewing modes: Heliocentric, Pluto-centered, Barycenter-centered
   - TRUE barycentric orbital mechanics demonstration
   - Both Pluto and Charon visible orbiting the barycenter

2. **Binary System Educational Content**
   - New section explaining barycenters and mass ratios
   - See-saw analogy for understanding orbital distances
   - Comparison with Earth-Moon (not a true binary)
   - Why Pluto-Charon is unique in our solar system

3. **Technical Implementation**
   - Dual-mode orbit function with center_id parameter
   - Critical fix: Angular elements from cache, semi-major axis calculated
   - Barycenter marker for Pluto-centered view
   - Animation support for both viewing modes

4. **Enhanced Hover Text**
   - [calculated] and [osculating] tags clarify element sources
   - Educational content about tidal locking and "the dance"
   - Mass ratio explanations in see-saw terms

### Educational Highlights

**The Geocentric/Heliocentric Analogy:**
- Pluto-centered = Geocentric (convenient, Pluto stationary)
- Barycenter-centered = Heliocentric (true mechanics, Pluto moves!)

**The Key Insight:**
Switch views and watch Pluto gain an orbit! This is exactly like the historical shift from "Earth is the center" to "Earth orbits the Sun."

**For Paloma:**
*"The see-saw doesn't just have Charon moving - Pluto moves too! They dance together around the balance point."*

### Technical Highlights

**The Critical Fix:**
Initially, hardcoded angular elements caused orbit/trajectory misalignment. Solution: Use cached osculating elements for orbital plane orientation (i, ω, Ω), calculate only semi-major axis from mass ratio.

**Visual Verification Principle:**
The angular mismatch was caught by eye, not code review. For scientific visualization, visual inspection is a feature, not a workaround.

### Lessons Learned

1. Angular elements are frame-independent (same orbital plane)
2. Osculating elements from JPL are more accurate than approximations
3. Visual verification catches physics errors code review misses
4. The shift from convenient to accurate views mirrors scientific history

---

**Total additions:** ~400 lines of new educational content, ~200 lines of technical documentation
**Focus areas:** Binary systems, barycenters, true orbital mechanics
**Educational value:** Demonstrates why reference frame choice matters
**Quotable:** *"Only the barycenter approach represents the actual orbital mechanics!"*

---
