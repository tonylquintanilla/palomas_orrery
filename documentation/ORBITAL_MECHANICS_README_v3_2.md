# Orbital Mechanics - Paloma's Orrery

**Complete Guide: Educational Foundation + Technical Implementation**

**Last Updated:** March 10, 2026 (v3.2 - Comet Perihelion Osculating Orbits: Capability D, vis-viva perihelion velocity)  
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

## 11. Mean vs Osculating Orbits (v2.9)

### The Two Descriptions of Every Orbit

Every orbit has two complementary descriptions:

**Mean elements** (from `orbital_elements.py` as `ORIGINAL_planetary_params`): The long-term average orbit from JPL's epoch solution. These smooth out short-period perturbations and represent the object's "true" trajectory over time.

**Osculating elements** (from live Horizons pre-fetch as `planetary_params`): The instantaneous Keplerian orbit that "kisses" the actual trajectory at the current moment. These change daily as planetary perturbations shift the orbital parameters.

For most planets, the two are nearly identical -- their orbits are stable. For perturbed objects like comets near Jupiter, the Moon under solar perturbation, or near-Earth asteroids, the difference can be dramatic.

### The Wierzchos Case Study

Comet C/2024 E1 (Wierzchos) provides the most compelling demonstration of why both descriptions matter.

The osculating eccentricity evolves daily as Jupiter's gravity perturbs the comet:

| Date | Osculating e | Orbit Type | Semi-major axis |
|------|-------------|------------|-----------------|
| Jan 20 (perihelion) | 0.999907 | Elliptical | Huge but plottable |
| Feb 25 | 0.9999997 | Nearly parabolic | ~1.9 million AU |
| Feb 26 | 1.000002 | Hyperbolic | Negative |
| Apr 30 | 1.000088 | Hyperbolic | Settling toward mean |

The mean elements (epoch 2025-Apr-19) say e=1.000053 -- a clean hyperbola with q=0.566 AU. The comet is leaving the solar system. But on Feb 25, the osculating elements say "nearly parabolic ellipse with semi-major axis of 1.9 million AU" -- technically bound to the Sun in a gargantuan orbit.

Same comet, same moment, two very different stories. The truth is that the mean orbit represents the long-term reality, while the osculating orbit captures the instantaneous perturbation state.

### Implementation

The mean orbit trace is generated from `ORIGINAL_planetary_params` (never modified by the pre-fetch) and added as a hidden-by-default legendonly trace with a white longdash line style, distinct from the osculating orbit's dotted line in the object's color.

The architecture already separated mean from osculating elements:
- `ORIGINAL_planetary_params` = mean elements (imported once, never modified)
- `planetary_params` = osculating elements (updated each session by pre-fetch)

Both are imported in `idealized_orbits.py`. The feature adds two helper functions:
- `add_mean_orbit_trace()` -- generates elliptical or hyperbolic mean orbit and adds to figure
- `get_mean_vs_osculating_assessment()` -- computes delta-e, delta-a/q, delta-i with qualitative assessment

Perturbation assessment thresholds (percentage change in eccentricity):
- < 1% = minimal perturbation
- 1-5% = moderate perturbation
- 5-20% = strong perturbation
- > 20% = extreme perturbation

### The Unit Conversion Bug

During testing, the osculating orbit for Wierzchos appeared as a tiny dot at the Sun (a=0.013 AU) instead of a giant near-parabolic ellipse. Root cause: the unit conversion heuristic in `orbit_data_manager.py` used `abs(a) > 10000` to detect km units. For near-parabolic orbits, `a` in AU can be millions (a = q/(1-e) where 1-e is near zero), triggering a false conversion that divided by 149 million.

The fix: use perihelion distance `q` as the unit detector instead of `a`. No solar system object has q > 10,000 AU, but any value in km will exceed 10,000 km. The q-based detection is robust across all orbit types.

### For Paloma

*"Every object in space has two ways to describe its orbit. The 'mean orbit' is like an average -- it shows the path the object follows over long periods. The 'osculating orbit' is like a snapshot -- it shows the exact orbit at this instant, including all the little tugs from nearby planets.*

*For most planets, both orbits look the same because their paths are very stable. But for comets flying through the inner solar system, Jupiter's gravity tugs on them so hard that the snapshot orbit can look completely different from the average! Comet Wierzchos is a great example -- on one day its snapshot orbit says 'giant ellipse around the Sun' and the next day it says 'leaving the solar system forever.' The mean orbit calmly says 'leaving the solar system' the whole time."*

---

## 12. Sub-Day Temporal Resolution

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

## 13. Version History

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
| **2.9** | **Feb 25, 2026** | **Mean Orbit Traces: white longdash mean orbit alongside osculating, perturbation assessment on hover, unit conversion fix (q-based detection). Wierzchos case study.** |
| **3.0** | **Mar 4, 2026** | **Close Approach Infrastructure: JPL CAD API integration, precision perigee markers, hyperbolic osculating orbits. Apophis 2029 case study. Cache isolation fix (close_approach_cache.json).** |
| **3.1** | **Mar 4, 2026** | **Earth Orbital Shell Infrastructure: GEO belt and LEO shell for Apophis flyby context.** |
| **3.2** | **Mar 10, 2026** | **Comet Perihelion Osculating Orbits (Capability D): Sun-centered osculating conic at perihelion for all comets. Both hyperbolic and elliptical branches. Vis-viva perihelion velocity in hover text. Tested: 3I/ATLAS, MAPS, Halley 1986.** |

---

## 14. Patroclus-Menoetius Implementation (v2.6)

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

## 15. Lucy Flyby Visualization (v2.6)

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

## 17. Close Approach Infrastructure (v3.0)

### Motivation: Apophis 2029

On **Friday, April 13, 2029**, asteroid 99942 Apophis will pass Earth at **38,013 km center-to-center** -- below the geostationary orbit ring (42,164 km). Visible to the naked eye from Europe, Africa, and western Asia. Three spacecraft are converging on it: RAMSES (ESA), OSIRIS-APEX (NASA), DESTINY+ (JAXA).

This event motivated three composable capabilities that generalize to any small body flyby.

---

### Capability A: JPL CAD API Integration

**Module:** `close_approach_data.py`

The JPL Small Body Close Approach Data (CAD) API provides precision flyby data for any near-Earth object near any major body.

```
https://ssd-api.jpl.nasa.gov/cad.api?des=2004+MN4&body=Earth&...
```

**Apophis 2029 data from CAD API:**

| Parameter | Value |
|-----------|-------|
| Perigee time | 2029-Apr-13 21:46:12 TDB |
| Center-to-center distance | 38,011.5 km (0.000254091 AU) |
| Surface distance | 31,640.5 km |
| Relative velocity | 7.423 km/s |
| 3-sigma uncertainty | ±3.3 km |
| Orbit solution | #220 |

**Cache:** Stored in `data/close_approach_cache.json` -- separate from `orbit_paths.json`. The orbit path validator expects `data_points` or `x/y/z` arrays; close approach dicts have neither and would be flagged as "corrupted," triggering a false size-reduction alarm. Separate file = no collision.

---

### Capability B: Precision Perigee Marker

A white square-open marker placed at the JPL CAD perigee position, fetched from Horizons at the exact perigee Julian Date.

**Hover text includes:**
- Exact date/time from CAD API
- Center-to-center distance (AU and km)
- Surface distance (km)
- Relative velocity (km/s)
- 3-sigma uncertainty (km)
- JPL orbit solution ID

**Note:** The marker may sit slightly off the plotted trajectory line. This is expected -- the trajectory has ~13-hour time resolution (51 points over 28 days), while the CAD perigee is precise to seconds. The offset is informative, not a bug.

---

### Capability C: Hyperbolic Osculating Orbit

A white dotted arc showing the instantaneous Keplerian hyperbola at perigee -- "if only Earth's gravity existed, Apophis would follow this path."

**Physical meaning:**
- Near perigee: closely overlaps actual trajectory
- Farther out: solar gravity causes divergence -- this divergence is physically informative

**Key implementation decisions:**

**1. Epoch at perigee, not plot start.**
Elements are fetched at the CAD perigee time (Apr 13 21:46), not the plot start date (Apr 1). This is critical: osculating elements change continuously. Elements at Apr 1 describe a hyperbola with q=91,636 km (wrong). Elements at perigee give q=38,012 km (correct -- matches CAD to within 1 km).

**2. Bypass the osculating cache entirely.**
The osculating cache keys on `obj_name + center_body` with no date component. A cached Apr 1 entry would be returned even when requesting Apr 13, silently giving wrong elements. The hyperbolic fetch calls `fetch_osculating_elements()` directly, skipping both cache read and write.

**3. Arc bounded by the plotted cube.**
Binary search finds the theta where r = axis_range × 1.5. Arc is always fully visible regardless of eccentricity. Never flies off-screen.

**4. Sinh-spaced point density.**
Points are dense near periapsis (theta=0) and sparse near the asymptotes. 300 points per arm with scale=3 gives ~10x more density at closest approach, where curvature matters.

**Apophis at perigee (elements from JPL Horizons @399, 2029-Apr-13):**

| Element | Value |
|---------|-------|
| e | ~4.25 (hyperbolic) |
| a | negative (hyperbola convention) |
| q | ~38,012 km (matches CAD) |
| i | ~37 deg |
| Asymptotic half-angle | ~103 deg |

---

### For Paloma

*"Apophis is a space rock about the size of the Empire State Building. In April 2029, it will zoom past Earth so close that people in Europe can see it with their naked eyes -- no telescope needed! It will pass BELOW the ring of satellites that give us TV and GPS. Our orrery shows three things: exactly where it will be closest (the white square marker), the dotted curve it would follow if Earth were the only thing in the solar system pulling on it (the hyperbola), and the red line showing what it actually does with the Sun also pulling. The difference between the dotted curve and the red line is the Sun's gravity at work."*

---

### Cache Architecture Note

The size-reduction safety check in `orbit_data_manager.py` compares the file size of the existing cache to the serialized size of the new data. This can produce false alarms when the file on disk was written with `indent=2` (pretty-printed, ~150 MB) and the save writes compact JSON (~100 MB) -- same data, different formatting. The correct comparison is entry counts, not byte sizes. (Tracked for future fix.)

---


## 18. Earth Orbital Shell Infrastructure (v3.1)

### Motivation: Context for the Apophis Flyby

The hyperbolic osculating orbit (Section 17, Capability C) shows *where* Apophis goes. But "38,013 km" is an abstract number. Two new shells answer the question every viewer asks: *what is out there at that distance?*

The answer, rendered in the orrery: a thin equatorial ring of geostationary satellites that Apophis passes *inside*, and a spherical cloud of low-Earth-orbit objects hugging the planet far below. Together with the hyperbolic trajectory, these three layers tell the whole story at a glance.

---

### Shell A: Geostationary Belt (GEO)

**Module:** `earth_visualization_shells.py` — `create_earth_geostationary_belt_shell()`

**Physics:**

Geostationary orbit is the one altitude where a satellite's orbital period exactly matches Earth's rotation: 23 hours 56 minutes 4 seconds (one sidereal day). The required radius follows directly from Kepler's third law:

```
r = (GM * T^2 / 4pi^2)^(1/3) = 42,164 km from Earth's center
                               = 35,786 km altitude above the surface
                               = 6.62 Earth radii
```

At this exact radius, in the equatorial plane, a satellite appears stationary over a fixed point on Earth. This is why your TV dish points at a fixed spot in the sky.

**Why it's a ring, not a sphere:**

To appear stationary, a satellite must orbit in the equatorial plane. Any inclination causes it to trace a figure-eight (analemma) over the ground. So all ~550 active geostationary satellites are confined to a single thin equatorial ring. The ITU assigns longitude slots to prevent interference — the belt is a shared resource, not open space.

**Apophis context:**

| Altitude | Distance from center | Notes |
|----------|---------------------|-------|
| GEO | 42,164 km | The satellite ring |
| Apophis 2029 perigee | 38,013 km | 4,151 km INSIDE the ring |
| Surface | 6,371 km | Earth's surface |

Apophis passes ~4,150 km below the geostationary ring. No collision risk with satellites — the belt is thinly populated and Apophis is well-characterized — but the geometry is striking.

**Rendering:**

240 silver-white points (`rgb(220, 220, 255)`) in the equatorial plane at 42,164 km, with slight radial scatter (±~30 km) and z scatter (±~320 km) to suggest real station-keeping tolerances rather than a perfect geometric circle. Point density is uniform — GEO slots are distributed fairly evenly around the full 360° of longitude.

**Recommended scale:** 0.003 AU

---

### Shell B: Low Earth Orbit (LEO)

**Module:** `earth_visualization_shells.py` — `create_earth_leo_shell()`

**Physics:**

LEO spans roughly 200 km to 2,000 km altitude (1.03 to 1.31 Earth radii). At these altitudes, orbital periods range from 90 to 127 minutes. The atmosphere is still thin enough to permit long-lived orbits (with station-keeping), but dense enough that uncontrolled objects decay within years to decades.

**Why it's a sphere, not a ring:**

LEO satellites orbit at all inclinations — equatorial, polar, sun-synchronous, inclined. There is no single preferred plane. The result is a genuine spherical shell of objects surrounding Earth at all latitudes.

| Altitude | Object |
|----------|--------|
| ~400 km | International Space Station (51.6° inclination) |
| ~540 km | Hubble Space Telescope |
| ~550 km | Starlink (multiple inclination shells) |
| ~700 km | Many Earth observation satellites |

**The contrast with GEO:**

GEO is invisible to the naked eye — too faint, too far (42,164 km), and stationary. LEO objects are what most people have actually seen: the moving "stars" crossing the sky at dusk and dawn are LEO satellites, most commonly Starlink trains. GEO controls global communications; LEO is what you see.

GEO sits 5× farther from Earth's surface than the top of LEO. At the recommended 0.003 AU scale, both shells are visible simultaneously and the scale contrast is immediately readable.

**Current population:**

| Category | Count |
|----------|-------|
| Active satellites (LEO) | ~8,000 |
| Starlink alone | 6,000+ |
| Tracked debris objects | 20,000+ |
| Total objects >10 cm | ~36,000 |

**Rendering:**

300 warm-white points (`rgb(255, 248, 220)`) distributed across the full sphere using uniform angular sampling (`cos(theta)` uniform → uniform surface density). Radii drawn 60% uniformly across the full LEO band, 40% clustered near the Starlink altitude (550 km, σ=150 km) to reflect where the real population is densest. Opacity 0.35 — reads as a diffuse shell rather than a solid surface.

**Recommended scale:** 0.003 AU

---

### The Three-Layer Picture

With all three enabled at 0.003 AU scale, Earth-centered, April 2029:

```
Earth surface          6,371 km
  |
  |--- LEO shell       6,571 - 8,371 km  (warm white sphere, hugging Earth)
  |
  |    [Van Allen inner belt, magnetosphere above...]
  |
  |--- GEO ring       42,164 km           (cool silver ring, equatorial)
  |
Apophis perigee       38,013 km           (white square marker, inside GEO)
  |
Apophis trajectory    red line, cutting through GEO ring
Osculating hyperbola  white dotted arc, threading through
```

The LEO shell makes Earth look inhabited. The GEO ring marks the boundary Apophis crosses. The trajectory does the rest.

---

### For Paloma

*"Earth has two kinds of satellites. The ones you can actually see in the sky -- like Starlink trains at dusk -- are in Low Earth Orbit, flying just a few hundred kilometers up, going around Earth every 90 minutes. That's the warm white cloud close to Earth.*

*The ones that give us TV, weather maps, and GPS are much, much farther away -- 35,786 kilometers up -- in a special orbit where they hover perfectly still over the same spot on Earth, forever. They form a thin ring around the equator.*

*In April 2029, Apophis will pass BETWEEN those two layers: above all the LEO satellites, but below the geostationary ring. It will be 4,000 kilometers closer to Earth than your TV satellite. You'll be able to see it with your naked eyes from Europe."*

---

## 19. Comet Perihelion Osculating Orbits (v3.2) -- Capability D

### Motivation: Resolution at Perihelion

Comets race through perihelion. The standard ephemeris trace -- typically 51 points over a date range -- can be days apart through the most dynamic region of the orbit. Apsidal markers show *where* perihelion is, but the trajectory between marker points is coarse.

Capability D fills this gap with a high-resolution osculating arc at perihelion -- 300-500 points, sinh-spaced to be densest where it matters most. The white dotted curve shows the instantaneous Keplerian conic: "if only the Sun were pulling on this comet, this is the path it would follow."

### The Sun-Centered Counterpart to Capability C

| | Capability C (Asteroid Flyby) | Capability D (Comet Perihelion) |
|---|---|---|
| Center body | Planet (Earth, Mars, etc.) | Sun |
| Epoch source | CAD API perigee JD | Osculating cache Tp JD |
| Conic type | Hyperbolic only (e > 1) | Both hyperbolic AND elliptical |
| Trigger | Close approach found in plot window | Comet identified + Tp available |
| Function | `plot_hyperbolic_osculating_orbit` | `plot_perihelion_osculating_orbit` |

The two capabilities are mutually exclusive by center body and coexist without interference.

### Vis-Viva: Perihelion Velocity

The vis-viva equation, evaluated at r = q (perihelion distance):

```
v_perihelion = sqrt(GM_sun * (2/q - 1/a))
```

This single equation works for both hyperbolic (a negative) and elliptical orbits. It reveals dramatic velocity differences:

| Comet | q (AU) | v_perihelion | Context |
|-------|--------|-------------|---------|
| MAPS (C/2026 A1) | 0.005 | 557 km/s | Kreutz sungrazer, grazing the Sun |
| 3I/ATLAS | 1.356 | ~68 km/s | Interstellar, passing through |
| Halley | 0.587 | 54.5 km/s | Periodic, moderate approach |
| Earth (reference) | 0.983 | 30 km/s | Our orbital speed |

The closer the perihelion, the faster the comet moves. MAPS at 557 km/s is nearly 0.2% the speed of light.

### Comet Detection

Objects are identified as comets by Horizons ID pattern, not by eccentricity:
- `C/` designation (most comets)
- `nI/` in name (interstellar: 1I/Oumuamua, 2I/Borisov, 3I/ATLAS)
- `A/` designation (pre-reclassification interstellar)
- Numeric ID >= 90000000 (periodic comet record numbers, e.g., Halley = 90000030)

No eccentricity guard on the trigger. If it's a comet and has a Tp, the arc is drawn. Eccentricity only matters inside the function for choosing the conic type.

### Tp Resolution: Three-Path Fallback

The perihelion time (Tp) is resolved through:

1. **Path A: Osculating cache** -- preferred. The cache Tp matches the user's current plot context (e.g., Halley 1986 Tp when plotting the 1986 apparition).
2. **Path B: Analytical elements** -- fallback. Caution: may store a different apparition (e.g., Halley 2061 vs 1986).
3. **Path C: Horizons fetch** -- last resort. Fetches at plot start date, reads Tp from returned elements.

**Key insight from testing:** Halley's analytical elements store TP = 2061 (next perihelion), but when the user plots at 1986, the pre-fetch populates the cache with the 1986 Tp. Path A correctly returns the 1986 value.

### Conic Branches

**Hyperbolic (e > 1):** Asymptote angle, binary search for clip theta, sinh-spaced 300 points per arm. Identical to Capability C.

**Elliptical (e <= 1):** Standard conic equation `r = a(1-e^2)/(1+e*cos(theta))`. If aphelion fits within plot bounds, full ellipse is drawn. Otherwise, binary search clips the arc at the plot cube boundary. Sinh spacing for e > 0.95 (near-parabolic); uniform otherwise.

### Tested and Verified

| Comet | Type | e | Result |
|-------|------|---|--------|
| 3I/ATLAS | Hyperbolic | 6.14 | Dramatic open hyperbola |
| MAPS | Elliptical (near-parabolic) | 0.99996 | Tight perihelion hairpin |
| Halley (1986) | Elliptical | 0.967 | Complete elongated ellipse, retrograde tilt |

### For Paloma

*"When a comet swings around the Sun, there's a single moment when it's closest -- perihelion. The dotted white line shows what path the comet would follow if only the Sun existed. For 3I/ATLAS -- visiting from another star -- that's a hyperbola: it swings around and leaves forever. For Halley -- which comes back every 76 years -- it's a stretched-out ellipse.*

*The hover text tells you how fast each comet moves at perihelion. MAPS, a sungrazer that nearly touches the Sun, reaches 557 km/s -- almost 2 million kilometers per hour. Halley peaks at 54 km/s. Earth moves at 30 km/s. The closer you get, the faster you go. One equation -- vis-viva -- tells you the whole story."*

---

## 16. References

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
*"It passes BELOW the geostationary ring."* - On Apophis 2029 - Feb 25, 2026
*"Use q to detect units, not a -- perihelion distance is always well-behaved."* - Feb 25, 2026
*"Osculating elements must be fetched at the perigee epoch, not the plot start date."* - Mar 4, 2026
*"Bypassing the cache is correct for precision epoch-specific fetches."* - Mar 4, 2026
*"The offset between the marker and the trajectory is informative, not a bug."* - Mar 4, 2026
*"GEO is what controls the world. LEO is what you can see."* - Mar 4, 2026
*"The LEO shell makes Earth look inhabited. The GEO ring marks the boundary Apophis crosses."* - Mar 4, 2026
*"The osculating arc is a high-resolution perihelion detail overlay, not just a theoretical 'what if' curve."* - Mar 10, 2026
*"The eccentricity threshold is the wrong discriminator. The right test is: is it a comet, and does it have a Tp?"* - Mar 10, 2026
*"557 km/s at perihelion vs 44 km/s today -- that's what grazing the Sun does."* - Mar 10, 2026
*"The closer you get, the faster you go. One equation tells you the whole story."* - Mar 10, 2026
*"Plot the 1986 perihelion, not the 2061 one -- the data arc is what matters."* - Mar 10, 2026

---

**Document Version:** 3.2 (Comet Perihelion Osculating Orbits: Capability D + Vis-Viva)
**Date:** March 10, 2026
**Maintained By:** Tony
**Contributors:** Claude (AI assistant)

*"The closer you get, the faster you go. One equation tells you the whole story."*
