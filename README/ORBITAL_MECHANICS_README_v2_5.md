# Orbital Mechanics - Paloma's Orrery

**Complete Guide: Educational Foundation + Technical Implementation**

**Last Updated:** January 21, 2026 (v2.5 - Apsidal Surface Distance)  
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

### For Paloma

*"Imagine you and a friend holding hands and spinning around. The spot where your hands grip - that's the barycenter! If your friend is almost as big as you, you BOTH swing around that grip point. That's what Pluto and Charon do!"*

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

### For Paloma

*"Orcus and Vanth are like a tiny version of Pluto and Charon, dancing around each other way out in the Kuiper Belt. Scientists used a giant telescope called ALMA to watch Orcus wobble back and forth, and from that wobble they figured out exactly how heavy both of them are!"*

---

# PART II: TECHNICAL IMPLEMENTATION

*How the software implements orbital mechanics*

---

## 8. Data Sources & Architecture

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

When JPL Horizons hasn't yet generated an entry (often 48-72 hours after discovery), authoritative sources are:

1. **Project Pluto Pseudo-MPEC** - Bill Gray's service computes orbit solutions immediately from raw observatory astrometry, often days before official MPECs
2. **Minor Planet Center NEOCP** - Lists raw observations; experts refine orbits on mailing lists like Comets-ML

**Example: 6AC4721 (C/2026 A1)**
- Discovered: January 13, 2026 (station W94, Chile)
- Project Pluto solution available: January 14, 2026
- Paloma's Orrery visualization: January 14, 2026
- JPL Horizons entry: Pending

**Caveat:** Always verify coordinate frame. Project Pluto may provide Equatorial or Ecliptic J2000 - check before importing. The 6AC4721 elements (i=144.51°, Ω=9.28°) were confirmed Ecliptic J2000.

### The Dual ID Pattern

TNOs with moons have two IDs with different ephemeris coverage:

```python
# System barycenter ID - limited ephemeris (~2030)
'id': '20136108'

# Small body designation - extended ephemeris (~2500)
'helio_id': '2003 EL61'
```

---

## 9. Cache Management

### Orbit Cache Architecture

| Cache | Contents | Purpose |
|-------|----------|---------|
| `orbit_paths.json` | Position trajectories | Actual orbit traces |
| `osculating_cache.json` | Orbital elements at epoch | Osculating ellipses |
| `incremental_cache/` | Stellar data | Star visualization |
| `climate_cache/` | Paleoclimate data | Earth system viz |

### Center-Body Aware Caching

Osculating elements must match the viewing center:

```python
# Cache key includes center body
cache_key = get_cache_key("Charon", center_body="9")  # -> "Charon@9"
```

*"Osculating means kissing - if the orbits don't touch, they're not osculating!"*

---

## 10. Barycenter Reference Frame Fix (Dec 7, 2025)

### The Problem

Osculating orbits didn't "kiss" actual trajectories in Pluto-Charon barycenter view.

### Root Cause

Reference frame mismatch:
- Elements fetched @999 (Pluto body center)
- Trajectories plotted @9 (system barycenter)

### Solution

Center-body aware caching with keys like "Charon@9":

```python
def get_cache_key(obj_name, center_body):
    if center_body and center_body != 'Sun':
        return f"{obj_name}@{center_body}"
    return obj_name
```

---

## 11. TNO Satellite Detection Logic

### The Problem

Checking `object_type == 'satellite'` fails for binary systems.

### Solution

Check orbital relationship, not classification:

```python
# OLD: Checks classification
if obj_type == 'satellite':

# NEW: Checks orbital relationship to center
if obj['name'] in parent_planets.get(center_object_name, []):
```

*"An object's type is not the same as its orbital relationship."* - Dec 4, 2025

---

## 12. Outer Planet Moon Visualization

### Osculating-Only Architecture

Neptune, Saturn, Uranus, and Pluto system moons display **only osculating orbits**.

**Rationale:**
- Osculating elements from JPL Horizons = actual current state
- Analytical elements = approximations
- Reduces visual clutter

| System | Dual Orbit? | Osculating Only? |
|--------|-------------|------------------|
| Earth (Moon) | Yes | - |
| Mars (Phobos, Deimos) | Yes | - |
| Jupiter (Galilean) | Yes | - |
| Saturn, Uranus, Neptune | - | Yes |
| Pluto system | - | Yes |

---

## 13. Analytical Orbit Fallback System (v1.5)

### The Problem

Some satellites have no JPL Horizons ephemeris data.

### Solution

Calculate orbits analytically from published elements:

```python
ANALYTICAL_FALLBACK_SATELLITES = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']
```

### Circular Orbit Physics

For e = 0:
- Mean anomaly = true anomaly (no Kepler's equation needed!)
- Constant velocity: v = 2*pi*a / P

### Hover Text Differentiation

| Data Source | Epoch String |
|-------------|--------------|
| JPL Horizons | `"2026-01-08 (osculating)"` |
| Analytical | `"analytical (J2000, theta=0)"` |

---

## 14. Keplerian Position Marker (v2.3)

### The Problem

When the network fails (JPL Horizons unreachable), the orrery cannot fetch:
- Current position (single point for "today")
- Actual orbit trajectory (vector data)

But we still have **cached osculating elements** with everything needed to calculate position analytically.

### The Solution

Calculate current position from cached osculating elements using Kepler's equation:

```
Cached: a, e, i, omega, Omega, MA (at epoch), epoch date
Current MA = epoch MA + (2*pi / period) * days_since_epoch
Solve: MA -> Eccentric Anomaly -> True Anomaly -> 3D Position
```

### The Math Pipeline

```python
# 1. Propagate mean anomaly
n = 2 * pi / period_days           # Mean motion
MA_now = MA_epoch + n * delta_t    # Current mean anomaly

# 2. Solve Kepler's equation (Newton-Raphson)
E = solve_kepler_equation(MA_now, e)

# 3. Convert to true anomaly
theta = 2 * arctan2(sqrt(1+e)*sin(E/2), sqrt(1-e)*cos(E/2))

# 4. Calculate radius
r = a * (1 - e^2) / (1 + e * cos(theta))

# 5. Apply orbital rotations (omega, i, Omega)
position = rotate_to_3d(r, theta, omega, i, Omega)
```

### Marker Appearance

| Property | Value | Reason |
|----------|-------|--------|
| Color | White | Distinguishes from object's actual color |
| Symbol | Circle | Consistent with other position markers |
| Default | Hidden (`legendonly`) | Doesn't clutter plot |
| Label | `"{Object} Keplerian Position (Epoch: {date})"` | Matches apsidal pattern |

### Use Cases

1. **Network failure** - Toggle on to see estimated position when JPL is unreachable
2. **Educational** - Compare Keplerian vs actual position to visualize perturbation effects
3. **Offline demos** - Show "where things are now" without internet

### Hover Text Details

The marker provides comprehensive calculation details:
- Current time
- Distance from center
- Days since epoch
- Mean anomaly (propagated)
- True anomaly (calculated)
- Note explaining this is two-body approximation

### For Paloma

*"When we can't reach NASA's computers to ask 'where is Earth right now?', we can figure it out ourselves using math! We know Earth's orbit shape from a few days ago, and we know how fast it moves, so we can calculate where it should be today. It's like knowing your friend walks one block per minute - even if you can't see them, you can guess where they are!"*

### Implementation

**New functions in `apsidal_markers.py`:**
- `solve_kepler_equation()` - Newton-Raphson solver
- `eccentric_to_true_anomaly()` - Anomaly conversion
- `calculate_keplerian_position()` - Full position calculation
- `add_keplerian_position_marker()` - Adds trace to plot

**Integration in `idealized_orbits.py`:**
- Called after apsidal markers, when `MA` and `epoch` exist in params
- Uses same rotation sequence as `calculate_exact_apsides()`

---

## 15. TNO Moon Analytical Fallback: Why It's Needed (v2.0)

### The Core Problem

JPL Horizons **cannot provide parent-centered ephemeris** for TNO moons because their parent bodies are not valid coordinate centers.

When you query Vanth relative to Orcus, Horizons returns **heliocentric data**:
- Expected: a = 0.00006 AU (9,000 km)
- Actual: a = 38.3 AU (Orcus's distance from Sun!)

### Detection

```python
if elements['a'] > 1.0:  # Semi-major axis > 1 AU
    print("WARNING: Data appears heliocentric!")
```

### The Frustrating Truth

| Source | Vanth Position Accuracy |
|--------|------------------------|
| JPL internal | 67 km |
| Our analytical | ~28,000 km worst case |

*"The data exists. The API doesn't serve it."* - Jan 3, 2026

---

## 16. Vector Subtraction Experiment (v2.0)

### The Idea

Could we compute moon position by subtracting:
`moon_helio - parent_helio = moon_relative`?

### The Attempt

```python
# Theory: Get barycenter vector, subtract to get relative position
barycenter_pos = horizons_query("20090482", "@sun")
vanth_helio = horizons_query("120090482", "@sun")
vanth_relative = vanth_helio - barycenter_pos
```

### Why It Failed

JPL returns the **combined barycenter** position, not separate satellite + primary vectors. The moon's motion is already baked into the barycenter - you can't extract it.

*"Theory vs practice: Sound algorithm + missing data = failure"* - Jan 3, 2026

---

## 17. Trajectory Two-Layer System (v1.8)

### The Problem

Spacecraft missions have two time scales:
1. **Full Mission** - Years of trajectory
2. **Plotted Period** - GUI-selected dates

### Solution

Two separate, toggleable traces:

| Trace | Color | Purpose |
|-------|-------|---------|
| Full Mission | Base color | Complete trajectory |
| Plotted Period | Yellow | Selected date range |

### Key Principle

Both static and animated plots should look identical; only animation differs.

---

## 18. Static Shells in Animations (v1.9)

### The Problem

Including planetary shells in every animation frame causes memory explosion.

### Solution

Shells are static (center object at origin) - add once, don't duplicate:

```python
# Frames only update dynamic traces
frame = go.Frame(
    data=[...dynamic traces...],
    traces=list(range(static_trace_count, total_traces))
)
```

### Memory Savings

| Approach | Trace Data |
|----------|------------|
| Old (all traces per frame) | 31 x 25 = 775 |
| New (dynamic only) | 16 x 25 + 15 = 415 |

**45% reduction!**

---

## 19. Orcus-Vanth Orbit Plane Fitting (v2.2)

### The Multi-Source Data Challenge

We have THREE data sources:

| Source | Provides | Best For |
|--------|----------|----------|
| JPL Horizons | Vanth's real-time 3D position | "Where is it NOW" |
| Brown & Butler 2023 (ALMA) | Orbit radii, mass ratio | Physical measurements |
| Published elements | Orbit plane orientation | Reference frames vary |

### The Problem

When we drew orbits using published elements and plotted JPL positions, **Vanth wasn't on the orbit!** It was 20-25% of its orbital radius off.

### The Solution: Fit the Orbit Plane to JPL Data

Rather than reconcile different reference frames, we **fitted the orbit plane directly**:

| Source | i (deg) | Omega (deg) | Error |
|--------|---------|-------------|-------|
| Published | 119.6 | 223.0 | 29 deg off! |
| Simple face-on | 90.0 | 0.0 | ~30 deg off |
| **Fitted to JPL** | **83.0** | **216.0** | **< 0.01 deg** |

### Position Calculation

```python
# Orbit plane normal from fitted elements
orbit_normal = np.array([
    np.sin(i_rad) * np.sin(Omega_rad),
    -np.sin(i_rad) * np.cos(Omega_rad),
    np.cos(i_rad)
])

# Project Vanth onto orbit plane
vanth_in_plane = vanth_vec - np.dot(vanth_vec, orbit_normal) * orbit_normal
vanth_unit = vanth_in_plane / np.linalg.norm(vanth_in_plane)

# Scale to ALMA radii
vanth_position = vanth_unit * VANTH_DIST_ALMA_AU
orcus_position = -vanth_unit * ORCUS_DIST_ALMA_AU  # 180 deg opposite
```

### Who's Right? Everyone!

| Source | What They Got Right |
|--------|---------------------|
| JPL | Real-time position direction |
| ALMA | Orbit size measurements |
| Claude's fit | Making visualization consistent |

### The Final Parameters

```python
BINARY_PARAMS = {
    'separation_au': 0.0000601,       # 9,000 km
    'period_days': 9.54,
    'mass_ratio': 0.16,               # HIGHEST KNOWN!
    'eccentricity': 0.007,
    'inclination_ecliptic': 83.0,     # Fitted to JPL
    'Omega_ecliptic': 216.0,          # Fitted to JPL
    'omega': 65.0,                    # Fitted alignment
}
```

---

## 20. Lessons Learned: Multi-Source Data Integration

### The Problem Pattern

Multiple data sources may use:
- Different reference frames (ecliptic J2000, equatorial, body-fixed)
- Different epochs
- Different conventions

### The Solution Pattern

1. Pick one source as "ground truth" for positions (JPL)
2. Pick another for physical parameters (ALMA for radii)
3. Fit remaining parameters to make visualization consistent
4. Document everything

### Visual Verification

*"Looks right"* is the ultimate test. Trust your eyes over the math until you find the error.

---

# PART III: VALIDATION & ACCURACY

---

## 21. Scientific Validation

### Accuracy by Object Type

| Object Type | Position Accuracy | Source |
|-------------|-------------------|--------|
| Inner planets | < 1 km | JPL DE ephemeris |
| Outer planets | < 10 km | JPL DE ephemeris |
| Major moons | < 100 km | JPL satellite ephemeris |
| TNO moons (analytical) | Unknown phase | Literature elements |
| Orcus-Vanth | ~20 km out-of-plane | Fitted + projected |

### Known Limitations

1. **TNO moon phases** - J2000/theta=0 assumption is arbitrary
2. **Reference frame mismatches** - Fitting may be needed
3. **API limitations** - Some data exists but isn't served
4. **Ephemeris coverage** - Barycenter IDs end ~2030

---

## 22. Living Science Philosophy

Paloma's Orrery deliberately shows the **edge of scientific knowledge**:

| Object | What We Show | What We're Honest About |
|--------|--------------|-------------------------|
| Inner planets | Full JPL ephemeris | Essentially perfect |
| Pluto system | Full JPL ephemeris | New Horizons revolutionized this |
| Orcus-Vanth | JPL + ALMA hybrid | Fitted orbit plane |
| TNO moons | Analytical orbits | Arbitrary phase |
| Planet 9 | Hypothetical shell | May not exist! |

### Design Principles

1. **Show what we know** - Use the best available data
2. **Acknowledge what we don't** - Explicit limitations
3. **Cite sources** - Let people dig deeper
4. **Make it work visually** - Fitting is okay when documented

*"We are living science here and sharing it."* - Tony, Jan 8, 2026

---

## Conclusion

Paloma's Orrery combines educational clarity with technical accuracy to visualize the intricate dance of celestial mechanics.

**For Educators & Students:** Part I provides conceptual understanding.
**For Developers:** Part II documents implementation decisions.
**For Scientists:** Part III validates accuracy honestly.

---

## References & Further Reading

### Books
- Jean Meeus, *Astronomical Algorithms* (1998)
- William Smart, *Textbook on Spherical Astronomy* (1977)

### Online Resources
- [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- [Project Pluto (Bill Gray)](https://www.projectpluto.com/) - Pseudo-MPECs for new discoveries
- [Minor Planet Center](https://www.minorplanetcenter.net/) - NEOCP and official designations
- [Astropy](https://www.astropy.org/)

### Key Papers
- Brown, M.E. & Butler, B.J. (2023). "Masses and densities of dwarf planet satellites measured with ALMA." *PSJ* 4(10):193
- Brown, M.E. et al. (2010). "The Size, Density, and Formation of the Orcus-Vanth System"
- Sickafoose, A.A. et al. (2019). "A stellar occultation by Vanth." *Icarus* 319

---

## Version History

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

---

## 23. Near-Parabolic Orbit Theta Sampling (v2.4)

### The Problem

For the newly discovered sungrazer comet 6AC4721 (C/2026 A1), the Keplerian apoapsis marker wasn't on the orbit trace - it was floating 70+ AU away!

### Root Cause: Missing θ=π in Orbit Array

The standard orbit generation used:
```python
theta = np.linspace(0, 2*np.pi, 360)  # 360 points
```

This creates 360 points from 0 to 2π **inclusive**, meaning:
- theta[0] = 0
- theta[180] ≈ 3.15 radians (NOT π = 3.14159...)
- theta[359] = 2π

For normal orbits, this is fine. But for near-parabolic orbits (e > 0.99), the radius changes **dramatically** near θ=π:

| True Anomaly | Radius (6AC4721) |
|--------------|------------------|
| θ = 179.5° | ~110 AU |
| θ = 180.0° (exactly) | ~180 AU |

The orbit trace was sampling at θ=179.5° but the apoapsis marker was correctly calculated at θ=π exactly!

### The Fix

For near-parabolic orbits (e > 0.99), explicitly include θ=π:

```python
if e > 0.99:
    # Ensure theta=pi is included for near-parabolic orbits
    theta_first_half = np.linspace(0, np.pi, 181)  # 0 to π inclusive
    theta_second_half = np.linspace(np.pi, 2*np.pi, 181)[1:]  # π to 2π, excluding π
    theta = np.concatenate([theta_first_half, theta_second_half])
else:
    theta = np.linspace(0, 2*np.pi, 360)
```

### Result

The Keplerian orbit trace now passes through the exact apoapsis point, and the apoapsis marker sits correctly on the orbit line.

### Broader Application: TNO Satellites

The same fix was applied to `plot_tno_satellite_orbit` for eccentric moons like Xiangliu (e=0.29):

```python
# For eccentric orbits (e > 0.1), ensure theta=pi is included
if e > 0.1:
    theta_first_half = np.linspace(0, np.pi, 181)
    theta_second_half = np.linspace(np.pi, 2*np.pi, 181)[1:]
    theta = np.concatenate([theta_first_half, theta_second_half])
else:
    theta = np.linspace(0, 2*np.pi, 360)
```

| Satellite | e | Benefits from fix? |
|-----------|------|-------------------|
| Xiangliu | 0.29 | Yes - significant eccentricity |
| Weywot | 0.011 | No - nearly circular |
| Vanth | 0.007 | No - nearly circular |
| MK2 | 0.0 | No - circular |

**Why different thresholds?**
- **e > 0.99** for comets: Only extreme near-parabolic orbits have dramatic radius jumps
- **e > 0.1** for TNO satellites: More conservative for small-scale orbits where precision matters

### The Bigger Picture: Orbits Before Horizons

With this fix plus the analytical orbit fallback system, Paloma's Orrery can now visualize objects that **don't yet exist in JPL Horizons**. When 6AC4721 was discovered on January 13, 2026, we had orbital elements from the discovery report within days - but JPL won't add it to Horizons until it receives an official designation. 

We're no longer limited by API availability. If you have orbital elements, you have an orbit.

### For Paloma

*"Imagine drawing a circle by connecting 360 dots. If you skip the dot at exactly 6 o'clock, you won't notice. But if you're drawing a REALLY stretched oval and skip the dot at the far end, you might miss the tip entirely! That's what happened with 6AC4721 - we fixed it by making sure we always include that important dot."*

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

---

## 24. Apsidal Surface Distance (v2.5)

### The Feature

Apsidal markers (perihelion, aphelion, periapsis, apoapsis) now display **distance from the center body's surface** in addition to distance from center. This makes close approaches viscerally meaningful - especially for sun-grazing comets where the difference between "0.005 AU" and "50,000 km from the solar surface" tells a very different story.

### Implementation

The hover text for all apsidal markers now includes:
```
Distance from center: 0.307498 AU
Distance from surface: 0.302839 AU (45,298,123 km)
```

Surface distance is calculated using the `CENTER_BODY_RADII` dictionary in `constants_new.py`:

| Body | Radius (km) |
|------|-------------|
| Sun | 696,340 |
| Mercury | 2,440 |
| Venus | 6,052 |
| Earth | 6,371 |
| Moon | 1,737 |
| Mars | 3,396 |
| Jupiter | 71,492 |
| Saturn | 58,232 |
| Uranus | 25,362 |
| Neptune | 24,622 |
| Pluto | 1,188 |

### Osculating vs Keplerian: Visible Differences

An interesting educational outcome: the surface distance reveals differences between orbital calculation methods.

For Mercury at perihelion:
- **Keplerian Perihelion** (osculating elements at epoch): Shows the instantaneous orbit including perturbation effects
- **Keplerian Periapsis** (pure θ=0 calculation): Shows the idealized two-body solution

These produce slightly different perihelion distances. For Mercury, the difference is small (~100 km). For sun-grazing comets, the difference can be dramatic - and seeing it in kilometers from the solar surface makes the distinction tangible.

### Where It Appears

Surface distance is shown in hover text for:

| Marker Type | Source Function | File |
|-------------|-----------------|------|
| Keplerian Perihelion (with epoch) | `create_enhanced_apsidal_hover_text` | apsidal_markers.py |
| Keplerian Periapsis | inline hover text | idealized_orbits.py |
| Keplerian Apoapsis | inline hover text | idealized_orbits.py |

### For Paloma

*"When a comet flies past the Sun, saying it passed at '0.005 AU' doesn't mean much. But saying it flew just 50,000 kilometers above the Sun's surface - that's close enough to feel the heat! The new hover text shows both numbers so you can really understand how close 'close' is."*

### Technical Note

The conversion uses the IAU definition: **1 AU = 149,597,870.7 km**

```python
center_radius_au = center_radius_km / 149597870.7
surface_distance_au = perihelion_distance - center_radius_au
surface_distance_km = surface_distance_au * 149597870.7
```

---

**Document Version:** 2.5 (Apsidal Surface Distance)  
**Date:** January 21, 2026  
**Maintained By:** Tony  
**Contributors:** Claude (AI assistant)

*"We have an orbit before JPL even has an object in Horizons!"*
