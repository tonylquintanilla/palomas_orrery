# Orbital Mechanics - Paloma's Orrery

**Complete Guide: Educational Foundation + Technical Implementation**

**Last Updated:** February 2, 2026 (v2.8 - TNO Barycenter Cleanup: The Barycenter Rule)  
**Project:** Paloma's Orrery - Astronomical Visualization Suite  
**Created by:** Tony (with Claude)

---

## About This Document

This guide serves two purposes:
1. **Educational Resource** - Understanding orbital mechanics concepts (for Paloma, students, educators)
2. **Technical Reference** - Implementation details and software architecture (for developers, contributors)

**Navigation:**
- Part I - Educational Foundation (concepts, physics, "why")
- Part II - Technical Implementation (code, architecture, "how")
- Part III - Validation & Accuracy (testing, limitations)

---

# PART I: EDUCATIONAL FOUNDATION

*Understanding the physics and concepts behind orbital mechanics*

---

## 1. Introduction

Orbital mechanics is the physics of how objects move through space under the influence of gravity. From the Moon's monthly journey around Earth to spacecraft trajectories to distant planets, the same fundamental principles apply.

This guide explains both the concepts and how Paloma's Orrery implements them.

---

## 2. The Six Orbital Elements

Every orbit can be described by six parameters - the **Keplerian orbital elements**:

| Element | Symbol | What It Describes |
|---------|--------|-------------------|
| Semi-major axis | a | Size of the orbit |
| Eccentricity | e | Shape (0=circle, 0-1=ellipse, 1=parabola, >1=hyperbola) |
| Inclination | i | Tilt relative to reference plane |
| Longitude of ascending node | Omega | Where orbit crosses reference plane going "up" |
| Argument of periapsis | omega | Orientation of ellipse in orbital plane |
| True anomaly | theta | Position along the orbit |

### For Paloma

*"Think of an orbit like a tilted hula hoop around a planet. The six numbers tell us: how big is the hoop (a), how squished (e), how tilted (i), which way it's tilted (Omega), where the closest point is (omega), and where on the hoop the object is right now (theta)!"*

---

## 3. Kepler's Laws of Planetary Motion

**First Law:** Orbits are ellipses with the central body at one focus.

**Second Law:** Equal areas in equal times - objects move faster when closer to the central body.

**Third Law:** P^2 = a^3 (for orbits around the Sun in years and AU)

---

## 4. Understanding Perturbations

In a perfect two-body system, orbits would be perfect ellipses forever. Reality is messier:

**Perturbations** are small deviations caused by:
- Other planets' gravity
- Non-spherical shapes (J2 oblateness)
- Solar radiation pressure
- Tidal forces
- Relativistic effects (Mercury!)

### Osculating vs Analytical Orbits

**Analytical orbit:** The idealized Keplerian ellipse from mean elements
**Osculating orbit:** The instantaneous ellipse that "kisses" the actual trajectory at a specific moment

*"Osculating means kissing - if the orbits don't touch, they're not osculating!"* - Dec 7, 2025

---

## 5. Binary Systems and Barycenters

### What is a Barycenter?

**The barycenter is the center of mass of a system** - the balance point around which all objects orbit.

Think of a see-saw:
- If two children weigh the same, the balance point is in the middle
- If one child is heavier, the balance point shifts toward them

### Most Systems Hide the Barycenter

**Sun-Jupiter:** Barycenter just outside Sun's surface - Sun barely wobbles
**Earth-Moon:** Barycenter 1,700 km inside Earth - not a true binary

### Pluto-Charon: A TRUE Binary System

- Charon is 12.2% of Pluto's mass
- Barycenter is 847 km ABOVE Pluto's surface!
- Neither object contains the barycenter

### Three Ways to View the Pluto System

1. **Heliocentric** - See Pluto's 248-year orbit around the Sun
2. **Pluto-centered** - Convenient local view (like geocentric thinking)
3. **Barycenter-centered** - Shows TRUE orbital mechanics!

*"Only the barycenter approach represents the actual orbital mechanics!"* - Nov 26, 2025

### The Barycenter Rule (v2.8)

Not every binary system needs a barycenter view. The test is simple: **is the barycenter outside the primary body?**

The barycenter offset from the primary is:

```
offset = separation * mass_ratio / (1 + mass_ratio)
```

If offset < primary radius, the primary barely wobbles and barycenter mode shows nothing useful.

| System | Mass Ratio | Bary Offset | Body Radius | Barycenter Mode? |
|--------|-----------|-------------|-------------|------------------|
| Pluto-Charon | 0.122 | 2,035 km | 1,188 km | **YES** - outside body |
| Orcus-Vanth | 0.16 | ~4,000 km | ~458 km | **YES** - outside body |
| Patroclus-Menoetius | ~0.28 | ~150 km | ~57 km | **YES** - outside body |
| Haumea system | 0.005 | ~244 km | ~861 km | No - inside body |
| Eris-Dysnomia | ~0.0085 | ~314 km | 1,163 km | No - inside body |
| Gonggong-Xiangliu | ~0.013 | ~312 km | ~615 km | No - inside body |
| Quaoar-Weywot | ~0.004 | ~7 km | ~545 km | No - inside body |

*"Just because Horizons has a barycenter solution doesn't mean you should use it!"* - Feb 2, 2026

### For Paloma

*"Imagine you and a friend holding hands and spinning around. The spot where your hands grip - that's the barycenter! If your friend is almost as big as you, you BOTH swing around that grip point. That's what Pluto and Charon do!*

*But if your friend is MUCH lighter than you, the balance point barely moves from where you're sitting -- you'd barely wobble! So we only show the 'balance point view' when the balance point is actually out in the open between the two dancers. For the others, we just show the big one sitting still with the little one orbiting around it."*

---

## 6. Trans-Neptunian Objects and Their Moons

### The Outer Realm

Beyond Neptune lies a vast region of icy bodies with their own satellite systems:

| System | Primary | Known Satellites |
|--------|---------|------------------|
| Pluto | Dwarf planet | Charon, Styx, Nix, Kerberos, Hydra |
| Eris | Dwarf planet | Dysnomia |
| Haumea | Dwarf planet | Hi'iaka, Namaka |
| Makemake | Dwarf planet | MK2 |
| Orcus | Plutino | Vanth |
| Quaoar | Cubewano | Weywot |
| Gonggong | Scattered disk | Xiangliu |

### MK2: The Moon Without an Ephemeris

MK2 is unique - JPL Horizons has **no ephemeris data** for it. We use analytical elements from the 2025 Hubble analysis:

| Parameter | Value |
|-----------|-------|
| Semi-major axis | 22,250 km |
| Orbital period | 18.023 days |
| Eccentricity | ~0 (circular) |
| Surface reflectivity | ~4% (darker than charcoal!) |

### For Paloma

*"MK2 is Makemake's shy little moon! It's so dark - like a piece of charcoal floating in space - that scientists didn't find it until 2015. We can show its orbit even though NASA's computers don't track it yet!"*

---

## 7. Orcus-Vanth: The Anti-Pluto Binary System

Orcus and Vanth form a remarkable binary - often called the "Anti-Pluto" because:
- Both are plutinos (3:2 resonance with Neptune)
- Orcus is at aphelion when Pluto is at perihelion (180 deg out of phase)
- Named after underworld deities

### The HIGHEST Mass Ratio Known!

| System | Mass Ratio (moon/primary) |
|--------|---------------------------|
| **Orcus-Vanth** | **0.16** |
| Pluto-Charon | 0.12 |
| Earth-Moon | 0.012 |

### Binary Orbit Parameters (Brown & Butler 2023, ALMA)

| Parameter | Value |
|-----------|-------|
| Total separation | 8,980 km |
| Orbital period | 9.54 days |
| Eccentricity | ~0.007 (nearly circular) |
| Barycenter location | 13.7% from Orcus |
| Orcus distance from BC | ~1,232 km |
| Vanth distance from BC | ~7,758 km |

**Key insight:** The barycenter is OUTSIDE Orcus's surface (~455 km radius). Both bodies visibly orbit a point in empty space between them.

### Barycenter Visualization: The JPL Resolution (v2.7)

The orrery visualizes the Orcus-Vanth system using **pure JPL Horizons data** from the satellite solution:

**The JPL ID Discovery:**

| Component | Horizons ID | Queryable at Barycenter? |
|-----------|------------|--------------------------|
| Barycenter | `20090482` | N/A (IS the center) |
| Orcus (primary) | `920090482` | **No** - returns "out of bounds" error |
| Vanth (satellite) | `120090482` | **Yes** - full ephemeris available |

Unlike Patroclus (`920000617` works fine), Orcus's primary body ID cannot be queried when centered on the barycenter. This is a JPL Horizons limitation, not a physics limitation.

**The Derivation Method:**

Since Vanth's positions are available, we derive Orcus's position using the mass ratio:

```
Orcus position = -Vanth position x 0.16 (mass ratio)
```

This works because in a two-body barycentric frame, the primary is always opposite the secondary, scaled by the mass ratio. The derivation is applied at five locations in the code: the Actual Orbit trace, position marker, hover text, plotted period overlay, and animation trajectory.

**Historical Note:** The original implementation (Jan 2026) used ALMA orbit circles with JPL providing only angular position (theta), projected onto the published radii. When we discovered that Vanth's ID (`120090482`) returns valid barycentric positions, we switched to pure JPL data. The ALMA circles were removed as redundant - they were a workaround for missing JPL barycentric data that is no longer missing.

### For Paloma

*"Orcus and Vanth are like a tiny version of Pluto and Charon, dancing around each other way out in the Kuiper Belt. Scientists used a giant telescope called ALMA to watch Orcus wobble back and forth, and from that wobble they figured out exactly how heavy both of them are! NASA's computers can track Vanth directly, but for Orcus we have to figure out where it is by knowing it's always on the opposite side of the dance from Vanth."*

---

## 8. Patroclus-Menoetius: The Binary Trojan

Among Jupiter's Trojan asteroids - ancient rocks sharing Jupiter's orbit - lies a unique binary system: **617 Patroclus and its moon Menoetius**.

### A Binary Among the Trojans

Unlike most asteroid "moons" which are tiny compared to their primaries, Patroclus and Menoetius are nearly equal in size:

| Body | Diameter | Mass Fraction |
|------|----------|---------------|
| Patroclus | ~113 km | 78% |
| Menoetius | ~104 km | 22% |

This makes them a **true binary system**, similar to Pluto-Charon but much smaller.

### Binary Orbit Parameters (Brozović et al. 2024, AJ 167:104)

| Parameter | Value |
|-----------|-------|
| Total separation | 692.5 km |
| Orbital period | 4.283 days |
| Eccentricity | 0.004 (nearly circular) |
| Inclination to ecliptic | 152.5° |
| Patroclus distance from BC | ~152 km |
| Menoetius distance from BC | ~540 km |

### Doubly Synchronous: A Cosmic Waltz

The system is **doubly synchronous** - both bodies are tidally locked, always showing the same face to each other as they orbit. Their rotation period equals their orbital period: 4.283 days = 102.8 hours.

### The Mythology

In Greek mythology, Patroclus was the beloved companion of Achilles in the Trojan War. Menoetius was Patroclus's father. The naming is fitting - a father and son locked in eternal embrace among the Trojans of the outer solar system.

### For Paloma

*"Patroclus and Menoetius are like two dancers holding hands and spinning together near Jupiter. They're almost the same size, so they both swing around their shared balance point. They always look at each other - never turning away - as they waltz through space together. In March 2033, a spacecraft named Lucy will fly past them to take pictures of this cosmic dance!"*

---

# PART II: TECHNICAL IMPLEMENTATION

*How the software implements orbital mechanics*

---

## 9. Data Sources & Architecture

### Primary Data Sources

| Source | Data Type | Usage |
|--------|-----------|-------|
| JPL Horizons | Ephemeris, osculating elements | Real-time positions |
| Project Pluto (Bill Gray) | Pseudo-MPEC orbital elements | Pre-Horizons discoveries |
| Minor Planet Center (MPC) | Discovery astrometry, NEOCP | New object confirmation |
| Hipparcos/Gaia | Stellar positions, parallax | Star visualization |
| SIMBAD | Stellar properties | Star classification |
| arXiv preprints | Latest orbital solutions | Cutting-edge objects |
| Published papers | Orbital elements | TNO moons, binaries |

### Pre-Horizons Data Pipeline

When new objects are discovered (comets, asteroids), they often don't appear in JPL Horizons for days or weeks. Paloma's Orrery can visualize them immediately using:

1. **Discovery reports** - Initial orbital elements from CBET/MPEC
2. **Project Pluto** - Bill Gray's rapid orbit solutions
3. **Analytical orbit plotting** - Direct Keplerian calculation from elements

---

## 10. Binary System Visualization Architecture

### The Three Barycenter Systems

Paloma's Orrery supports barycenter-centered visualization for three binary systems where the barycenter lies outside the primary body (see The Barycenter Rule, Section 5):

| System | Implementation | Data Source | Mass Ratio |
|--------|----------------|-------------|------------|
| Pluto-Charon | Horizons ephemeris | JPL satellite solution | 0.122 |
| Orcus-Vanth | Horizons (derived) | JPL satellite solution | 0.16 |
| Patroclus-Menoetius | Horizons + analytical | Brozovic et al. 2024 | ~0.28 |

Four additional TNO systems (Eris-Dysnomia, Haumea, Gonggong-Xiangliu, Quaoar-Weywot) have barycenter IDs in JPL Horizons but are visualized as primary-centered only because their barycenters fall inside the primary body.

### Dual Data Approach

Each binary system uses **two complementary data sources**:

1. **Horizons Ephemeris** (solid lines) - Actual computed positions including all perturbations
2. **Analytical Orbits** (dotted lines) - Idealized Keplerian ellipses from published parameters

This allows users to see both the "truth" (Horizons) and the "theory" (Kepler) simultaneously.

### Phase Alignment Challenge

For analytical orbits to match Horizons positions, we need to know **where on the orbit** each body is at any given time. This requires:

- **Time of periapsis (Tp)** - When the body was at periapsis
- **Mean anomaly at epoch (M₀)** - Angular position at reference time

For nearly circular orbits (like Patroclus-Menoetius with e=0.004), periapsis is poorly defined. Instead, we use a **reference position from Horizons** to establish the orbital phase.

### JPL Horizons Binary ID Scheme

JPL Horizons uses a systematic ID convention for binary asteroid/TNO systems. This was decoded from JPL's own Lucy trajectory documentation and validated empirically:

| Component | ID Pattern | Description |
|-----------|-----------|-------------|
| System barycenter | `20XXXXXX` | Center of mass of the system |
| Primary body center | `920XXXXXX` | Surface/center of the larger body |
| Secondary body | `120XXXXXX` | Satellite ephemeris solution |

Where `XXXXXX` is the minor planet number (e.g., `000617` for Patroclus, `090482` for Orcus, `003548` for Eurybates).

**Verified Systems:**

| System | Barycenter | Primary | Secondary | Bary Mode? |
|--------|-----------|---------|-----------|------------|
| Patroclus-Menoetius | `20000617` | `920000617` | `120000617` | **Yes** |
| Orcus-Vanth | `20090482` | `920090482` | `120090482` | **Yes** |
| Quaoar-Weywot | `20050000` | `920050000` | `120050000` | No (inside body) |
| Haumea system | `20136108` | `920136108` | `120136108` | No (inside body) |
| Eris-Dysnomia | `20136199` | `920136199` | `120136199` | No (inside body) |
| Gonggong-Xiangliu | `20225088` | `920225088` | `120225088` | No (inside body) |
| Eurybates-Queta | `20003548` | `920003548` | `120003548` (untested) | TBD |
| Polymele-Shaun | `20015094` | `920015094` | `120015094` (untested) | TBD |

### Universal Query Strategy for Binary Systems

Not all IDs are queryable in all configurations. Discovered empirically:

- `920000617` (Patroclus) works as query target at barycenter
- `920090482` (Orcus) does NOT work - returns "IOBJ out of bounds"
- `120XXXXXX` (secondary) IDs appear more reliable across systems

**The Universal Approach:**

```
1. TRY the direct ID (920XXXXXX for primary, 120XXXXXX for secondary)
2. IF query fails or returns all zeros:
   a. Fetch the OTHER component's positions (120XXXXXX is safest)
   b. Derive: primary_pos = -secondary_pos * mass_ratio
   c. Flag data as derived (for hover text transparency)
3. ALWAYS center queries on the barycenter ID (20XXXXXX)
```

The derivation works because in a two-body barycentric frame, the primary is always opposite the secondary, scaled by the mass ratio. This is not an approximation - it's exact for the two-body problem.

**Implementation Pattern (palomas_orrery.py):**

The derivation must be applied at **five locations** in the code wherever position/trajectory data is fetched:

1. `plot_actual_orbits()` - Orbit trace
2. First position loop - `positions` dict
3. Second position loop - Hover text data
4. Plotted Period overlay - Yellow trajectory highlight
5. Animation - Frame-by-frame positions

Missing any location causes that specific visualization element to show zeros while others work correctly.

### For Paloma

*"When NASA's computers can track both dancers in a binary, we just ask for their positions directly. But sometimes they can only track one dancer. No problem! If you know where one dancer is and how heavy they both are, you can figure out exactly where the other one must be - always on the opposite side of their shared balance point."*

---

## 11. Sub-Day Temporal Resolution

### The Problem

Spacecraft flybys happen in minutes, not days. The default 1-day time step misses all the action.

### The Solution

When `days_to_plot < 1.0`, the orrery automatically:

1. Switches to **minute-level resolution**
2. Preserves fractional day values through calculations
3. Generates timestamps at 1-minute intervals for animations

### Implementation

```python
# Detect sub-day range
if days_to_plot < 1.0:
    # Use minute stepping
    total_minutes = int(days_to_plot * 24 * 60)
    step_minutes = max(1, total_minutes // num_frames)
```

This enables visualization of events like the Lucy flyby of Patroclus-Menoetius at 2-minute resolution.

---

## 12. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Nov 20, 2025 | Initial consolidated document |
| 1.1 | Nov 22, 2025 | Mars dual-orbit, reference frame detection |
| 1.2 | Nov 23, 2025 | Apsidal marker enhancements |
| 1.3 | Nov 26, 2025 | Pluto-Charon binary system |
| 1.4 | Dec 4, 2025 | TNO satellites, dual ID architecture |
| 1.4.1 | Dec 7, 2025 | Barycenter reference frame fix |
| 1.5 | Dec 8, 2025 | MK2 analytical orbit fallback |
| 1.6 | Dec 12, 2025 | TNO dual-ID system documentation |
| 1.7 | Dec 23, 2025 | Center object refactoring, center_id pattern |
| 1.8 | Dec 25, 2025 | Trajectory two-layer system |
| 1.9 | Dec 25, 2025 | Static shells in animations |
| 2.0 | Jan 3, 2026 | TNO moon analytical fallback, vector subtraction |
| 2.1 | Jan 8, 2026 | Orcus-Vanth barycenter mode (initial) |
| 2.2 | Jan 8, 2026 | Orcus-Vanth orbit plane fitting |
| 2.3 | Jan 14, 2026 | Keplerian Position Marker (offline resilience) |
| 2.4 | Jan 20, 2026 | Near-parabolic orbit theta sampling fix |
| 2.5 | Jan 21, 2026 | Apsidal surface distance in hover text |
| **2.6** | **Jan 27, 2026** | **Patroclus-Menoetius binary system, Lucy flyby visualization** |
| **2.7** | **Jan 31, 2026** | **Orcus-Vanth JPL orbit resolution: pure JPL data, ALMA circles removed** |
| **2.8** | **Feb 2, 2026** | **TNO Barycenter Cleanup: The Barycenter Rule. Removed Eris, Haumea, Gonggong, Quaoar barycenters (inside body). Only Pluto-Charon, Orcus-Vanth, Patroclus-Menoetius remain.** |

---

## 13. Patroclus-Menoetius Implementation (v2.6)

### The Challenge

JPL Horizons provides positions for Patroclus and Menoetius relative to their barycenter, but when queried for **osculating elements**, returns mostly NaN values:

```
EC=-NaN  QR=-NaN  IN=152.53  OM=324.12  W=-NaN  Tp=NaN
```

This is because the orbit is so nearly circular (e=0.004) that eccentricity-dependent quantities are numerically unstable.

### The Solution: Hybrid Approach

We combine **three data sources**:

| Data | Source | Purpose |
|------|--------|---------|
| Physical parameters | Brozović et al. 2024 | a, e, P, mass fractions |
| Orbital plane | Horizons osculating | i=152.53°, Ω=324.12° |
| Phase reference | Horizons vectors | XYZ position at epoch |

### Phase Reference Method

Since Horizons can't give us Tp (time of periapsis), we use a **known position** to establish phase:

```python
# Reference: Patroclus position relative to barycenter
# 2033-Mar-03 00:00:00 TDB (JD 2463659.5)
PHASE_REFERENCE = {
    'jd_epoch': 2463659.5,
    'patroclus_x_km': 104.24,
    'patroclus_y_km': -109.12,
    'patroclus_z_km': 14.35,
}
```

From this position, we:
1. Transform from ecliptic to orbital plane coordinates
2. Calculate the true anomaly at reference epoch
3. Propagate phase forward/backward using the orbital period

### Keplerian Position Marker

For nearly circular orbits, "periapsis" is meaningless. Instead, the marker shows the **current calculated position** with explanatory hover text:

```
Patroclus Keplerian Position
Phase: 71.3 deg
r = 152.5 km (1.02e-06 AU)
e = 0.0040 (nearly circular)

Note: For nearly circular orbits, periapsis is undefined.
This marker shows the current calculated position,
which should match the Horizons actual position.
```

### Validation

The analytical orbit correctly predicts positions that match Horizons ephemeris:

| Body | Calculated Distance | Horizons Distance | Match |
|------|---------------------|-------------------|-------|
| Patroclus | 152.5 km | 151.9 km | ✓ |
| Menoetius | 540.0 km | 537.8 km | ✓ |

---

## 14. Lucy Flyby Visualization (v2.6)

### The Mission

NASA's Lucy spacecraft will fly past Patroclus-Menoetius on **March 3, 2033** - the final encounter of its 12-year mission to explore Jupiter's Trojan asteroids.

### Flyby Parameters

| Parameter | Value |
|-----------|-------|
| Closest approach | 2033-03-03 ~17:27 UTC |
| Minimum distance | ~1,276 km from barycenter |
| Flyby velocity | 8.815 km/sec (31,732 km/hr) |
| Encounter duration | ~1 hour within 15,000 km |

### Visualization Features

The orrery can display the Lucy flyby with:

1. **Sub-minute temporal resolution** - 2-minute animation steps
2. **Binary orbital motion** - Watch Patroclus and Menoetius orbit during approach
3. **Lucy trajectory overlay** - Yellow "plotted period" shows the flyby arc
4. **Full mission context** - Green line shows Lucy's complete 12-year journey

### Technical Implementation

```python
# Sub-day date range handling
if days_to_plot < 1.0:
    # For 1-hour window: 60 frames at 1-minute intervals
    num_frames = 61
    step = timedelta(minutes=1)
```

The `fractional_day` fix ensures that date ranges like "17:00 to 18:00" are preserved rather than truncated to whole days.

### For Paloma

*"In March 2033, a spacecraft named Lucy will zoom past Patroclus and Menoetius at almost 9 kilometers every second - that's like driving from home to school in less than a second! Lucy will only have about an hour to take pictures as it flies by, so every minute counts. Our orrery can show you exactly what that hour will look like, minute by minute!"*

---

## 15. References

### Binary System Papers

- Brozović, M. et al. (2024). "The Orbit and Density of the Jupiter Trojan Binary (617) Patroclus-Menoetius." *AJ* 167:104
- Brown, M.E. & Butler, B.J. (2023). "Masses and densities of dwarf planet satellites measured with ALMA." *PSJ* 4(10):193
- Grundy, W.M. et al. (2018). "Mutual orbit orientations of transneptunian binaries." *Icarus* 305

### Mission References

- Levison, H.F. et al. (2021). "Lucy Mission to the Trojan Asteroids: Science Goals." *PSJ* 2:171
- NASA Lucy Mission: https://lucy.swri.edu/

### Online Resources

- [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- [Project Pluto (Bill Gray)](https://www.projectpluto.com/)
- [Minor Planet Center](https://www.minorplanetcenter.net/)
- [Astropy](https://www.astropy.org/)

---

## Quotables

*"Data preservation is climate action."*
*"Sky's the limit! Or stars are the limit!"* - Tony
*"Only the barycenter approach represents the actual orbital mechanics!"* - Nov 26, 2025
*"An object's type is not the same as its orbital relationship."* - Dec 4, 2025
*"Osculating means kissing - if the orbits don't touch, they're not osculating!"* - Dec 7, 2025
*"No JPL ephemeris? No problem - calculate it yourself!"* - Dec 8, 2025
*"The data exists. The API doesn't serve it."* - Jan 3, 2026
*"We are moving beyond Horizons!"* - Tony, Jan 3, 2026
*"We are living science here and sharing it."* - Tony, Jan 8, 2026
*"Network down? Kepler still works."* - Jan 14, 2026
*"We have an orbit before JPL even has an object in Horizons!"* - Tony, Jan 20, 2026
*"Every tenth matters."* - On climate science, Jan 15, 2026
*"For nearly circular orbits, periapsis is undefined."* - Jan 27, 2026
*"Can't query the primary? Derive it from the secondary."* - Jan 31, 2026
*"Just because Horizons has a barycenter solution doesn't mean you should use it!"* - Feb 2, 2026

---

**Document Version:** 2.8 (TNO Barycenter Cleanup)  
**Date:** February 2, 2026  
**Maintained By:** Tony  
**Contributors:** Claude (AI assistant)

*"Just because Horizons has a barycenter solution doesn't mean you should use it!"*
