# Orbital Mechanics Guide - Paloma's Orrery

**Last Updated:** November 20, 2025  
**Purpose:** Educational reference for understanding orbital elements, coordinate systems, and perturbations

---

## Table of Contents

1. [Keplerian Orbital Elements](#keplerian-orbital-elements)
2. [J2 Oblateness Effect](#j2-oblateness-effect)
3. [Perturbations and Osculating Elements](#perturbations-and-osculating-elements)
4. [Coordinate Systems](#coordinate-systems)
5. [Visualizing Orbital Mechanics](#visualizing-orbital-mechanics)

---

## Keplerian Orbital Elements

The six classical orbital elements completely describe an orbit in space:

### Shape and Size
- **a (Semi-major axis):** Half the longest diameter of the ellipse. Defines orbit size.
- **e (Eccentricity):** How "stretched" the ellipse is
  - e = 0: Perfect circle
  - 0 < e < 1: Ellipse
  - e = 1: Parabola (escape trajectory)
  - e > 1: Hyperbola (unbound orbit)

### Orientation in Space
- **i (Inclination):** Tilt of orbital plane relative to reference plane (ecliptic)
  - i = 0°: Orbit in ecliptic plane
  - i = 90°: Polar orbit
  - i = 180°: Retrograde orbit
  
- **Ω (Longitude of Ascending Node):** Where orbit crosses reference plane going "up"
  - Measured from vernal equinox direction
  - Defines the "rotation" of the orbital plane
  
- **ω (Argument of Periapsis):** Where the closest approach occurs within the orbital plane
  - Measured from ascending node
  - Defines orientation of ellipse within its plane

### Position in Orbit
- **M (Mean Anomaly)** or **ν (True Anomaly):** Where the object is in its orbit at a specific time

---

## J2 Oblateness Effect

### What is J2?

**J2 is a dimensionless number that describes how non-spherical a planet is.**

When a planet rotates, centrifugal force causes it to bulge at the equator and flatten at the poles. This makes the planet **oblate** (wider than it is tall).

**J2 measures this oblateness:**
- J2 = 0 → Perfect sphere (no bulge)
- Larger J2 → More oblate (more squashed/bulged)

### Why Planets Have J2

1. **Rotation creates centrifugal force**
   - Material at equator experiences outward force
   - Material at poles has no centrifugal force
   - Planet bulges at equator

2. **Balance between forces**
   - Gravity tries to pull everything to center
   - Rotation tries to fling equator outward
   - Final shape is an equilibrium: oblate spheroid

### Real Values

| Planet | J2 Value | Equatorial Bulge | Visual |
|--------|----------|------------------|--------|
| **Earth** | 0.00108263 | 21 km (0.3%) | Barely visible |
| **Mars** | 0.00196 | 21 km (0.6%) | Slightly visible |
| **Jupiter** | 0.01475 | 4,638 km (6.5%) | **Clearly visible!** |
| **Saturn** | 0.01645 | 5,750 km (9.8%) | **Very obvious!** |
| Sun | 0.00000218 | 10 km (0.001%) | Essentially zero |

**Note:** You can actually **see** Jupiter and Saturn's oblateness through a telescope! Their equators visibly bulge.

### Why J2 Matters for Orbits

When a planet has a bulge, satellites don't experience uniform gravity:

**Non-uniform gravity field:**
- **At equator:** Extra mass from bulge → stronger gravity
- **At poles:** Less mass (flattened) → weaker gravity
- **Result:** Gravity varies with latitude

**This causes orbital perturbations:**

1. **Nodal Precession** (Ω changes over time)
   - The orbital plane rotates around the planet's axis
   - Like a spinning top precessing
   - Rate depends on: J2, altitude, inclination

2. **Apsidal Precession** (ω changes over time)
   - The ellipse rotates within its plane
   - Periapsis location moves
   - Rate depends on: J2, altitude, eccentricity

### J2 Effects on Earth's Satellites

**For the Moon:**
- Earth's J2 = 0.00108263
- Causes nodal precession: **Ω rotates ~19.3° per year**
- Combined with solar perturbations creates complex orbit
- One of several perturbation sources

**For Low Earth Orbit satellites:**
- Much closer to Earth → stronger J2 effects
- ISS orbit: Ω precesses ~5° per day!
- Critical for mission planning (sun angle, coverage)

**For GPS satellites (~20,000 km):**
- J2 still significant
- Must be accounted for in orbital predictions
- Affects timing and positioning accuracy

### J2 Effects on Mars' Satellites

**Phobos:**
- Mars' J2 = 0.00196 (1.8× Earth's)
- Extremely close: 9,376 km (only 1.4× Mars radii)
- **Very strong J2 effects**
- Rapid nodal precession
- Combined with solar perturbations, orbit changes quickly

**Deimos:**
- Same J2, but farther away (23,458 km)
- Weaker effects due to distance (1/r³ dependence)
- Still significant compared to distant moons

### The Mathematics (For the Curious)

The gravitational potential of an oblate planet:

```
U = -GM/r [1 - J2(R/r)² P2(sin φ) + higher terms...]
```

Where:
- **G** = Gravitational constant
- **M** = Planet mass
- **r** = Distance from planet center
- **R** = Planet's equatorial radius
- **φ** = Latitude
- **P2** = Second Legendre polynomial = (3sin²φ - 1)/2

**Key insight:** J2 effect scales as **(R/r)²**
- Closer satellites → much stronger J2 effects
- Effect drops as **1/r²** (inverse square)

**Precession rates (approximate):**

Nodal precession:
```
dΩ/dt ≈ -1.5 * (R/a)² * J2 * n * cos(i)
```

Apsidal precession:
```
dω/dt ≈ 0.75 * (R/a)² * J2 * n * (4 - 5sin²i)
```

Where:
- **n** = mean motion (orbital angular velocity)
- **a** = semi-major axis
- **i** = inclination

**This explains why:**
- Phobos precesses faster (smaller **a**)
- ISS precesses faster (smaller **a**)
- Inclination matters (cos i, sin²i terms)

### Other Perturbations Beyond J2

While J2 is the largest non-spherical gravity effect, there are others:

**Higher-order terms (J3, J4, J6...):**
- J3: North-south asymmetry (pear shape)
- J4, J6: Additional equatorial bulge refinements
- Generally much smaller than J2

**For Earth:** J2 ≈ 1000× larger than J4

### Visualizing J2 Effects

**In Paloma's Orrery:**
1. Open "Orbital Parameter Visualization"
2. Observe how Ω (ascending node) is defined
3. Imagine this rotating over time due to J2
4. For Moon: ~19.3° per year
5. For ISS: ~5° per day!

**See it in action:**
- Plot Moon orbit over weeks → see precession
- Plot Phobos orbit → even faster precession
- Compare to distant satellites → slower effects

---

## Perturbations and Osculating Elements

### What Are Perturbations?

**Perturbations are forces that cause an orbit to deviate from a perfect Keplerian ellipse.**

In an ideal universe with only two bodies:
- Planet orbits Sun in perfect ellipse
- Moon orbits Earth in perfect ellipse
- Orbit elements (a, e, i, ω, Ω) stay constant forever

**Real universe:**
- Sun pulls on Moon (while Moon orbits Earth)
- Earth isn't perfectly round (J2 effect)
- Tidal forces between bodies
- Other planets' gravity affects everyone
- **Result:** Orbital elements change continuously

### Types of Perturbations

**1. Third-body effects (N-body dynamics):**
- Primary example: Sun's gravity affecting Moon
- Secondary: Jupiter affecting asteroid belt
- Creates periodic variations in orbit

**2. Oblateness effects (J2, J4, etc.):**
- Non-spherical planet gravity
- Causes secular (long-term) precession
- Dominant for close satellites

**3. Tidal effects:**
- Energy dissipation through flexing
- Causes orbital evolution over long timescales
- Moon spiraling outward from Earth (~3.8 cm/year)

**4. Atmospheric drag (for low orbits):**
- Only affects very low satellites
- Causes orbit to decay
- Eventually leads to reentry

**5. Radiation pressure:**
- Solar wind and light pressure
- Significant for small objects, dust
- Minor for large satellites

### What Are Osculating Elements?

**"Osculating" comes from Latin *osculare* meaning "to kiss."**

**Osculating elements are the Keplerian orbit that "kisses" (exactly matches) the actual orbit at one specific moment.**

**The concept:**
1. At time T₀, the satellite has position **r** and velocity **v**
2. Calculate: "What Keplerian orbit has this exact r and v?"
3. Those orbital elements (a, e, i, ω, Ω, M) are the **osculating elements**
4. They describe the orbit the satellite **would** follow if all perturbations stopped

**Why "kissing"?**
- The osculating ellipse touches the real orbit at one point
- Like two curves kissing - they're tangent at that instant
- Then they diverge as perturbations continue

### How Long Are Osculating Elements Valid?

**It depends on perturbation strength!**

| Object | Orbit Period | Perturbations | Osculating Validity |
|--------|-------------|---------------|---------------------|
| **Moon** | 27.3 days | Strong (Sun + J2) | ~1-3 days |
| **Phobos** | 7.65 hours | Very strong | ~hours to 1 day |
| **ISS** | 90 minutes | Strong (J2 + drag) | ~hours |
| **GPS** | 12 hours | Moderate (J2) | ~days to weeks |
| **Io** | 1.77 days | Strong (tides + Jupiter J2) | ~1-2 days |
| **Titan** | 15.9 days | Weak (distant) | ~weeks |
| **Mars** | 687 days | Very weak | ~months to years |
| **Pluto** | 248 years | Extremely weak | ~decades |

**General rule:** Closer to primary + stronger perturbations = shorter validity

### Visualizing Osculating Behavior

**What you see in Paloma's Orrery:**

1. **At epoch (the "kiss"):**
   - Osculating orbit perfectly matches actual position
   - Both curves are tangent at this point
   - Zero difference

2. **After some time:**
   - Osculating orbit shows where satellite **would be** without perturbations
   - Actual orbit shows where satellite **actually is** with perturbations
   - Difference grows with time

3. **The divergence:**
   - **Moon:** Visible divergence after ~2 weeks
   - **Phobos:** Visible divergence after ~3-5 days (predicted)
   - **Distant objects:** Divergence takes much longer

### Why Use Osculating Elements?

**Advantages:**
1. Compact representation (6 numbers instead of 3D trajectory)
2. Physically meaningful (describes instantaneous orbit)
3. Updated frequently by JPL Horizons
4. Good for short-term predictions
5. Educational - shows perturbation effects

**When not to use:**
1. Long-term predictions (use integrated ephemerides)
2. Objects with non-gravitational forces (spacecraft propulsion)
3. When high accuracy needed over time

### Moon Perturbations - Detailed

**The Moon has three main perturbation sources:**

**1. Solar Gravity (Largest effect)**
- Sun pulls on Moon directly
- Creates **evection** - periodic variation in eccentricity
- Creates **variation** - another periodic effect
- Causes both e and i to oscillate
- Period: ~monthly (related to Moon's synodic period)

**2. Earth's Oblateness (J2 effect)**
- Earth's equatorial bulge
- Causes nodal precession: **Ω rotates 19.3° per year**
- Also causes apsidal precession (ω rotates)
- Secular (long-term, non-periodic) effect

**3. Tidal Forces**
- Moon raises tides on Earth
- Earth raises tides on Moon (Moon is tidally locked)
- Energy dissipation
- **Long-term:** Moon spiraling outward at 3.8 cm/year
- **Short-term:** Causes small oscillations

**Combined result:**
- Moon's orbital elements constantly changing
- Need frequent updates (JPL provides daily)
- Osculating orbit diverges within days
- Perfect example for teaching orbital mechanics!

### Phobos Perturbations - Predicted

**Phobos should have even stronger perturbations:**

**1. Mars' J2 (1.8× Earth's J2)**
- Larger oblateness effect
- Much closer to Mars (1.4× Mars radii vs Moon at 60× Earth radii)
- J2 effect scales as (R/r)² → **~2000× stronger for Phobos!**
- Very rapid precession expected

**2. Solar Gravity**
- Mars is farther from Sun
- But Phobos is much closer to Mars
- Sun's perturbation still significant
- Causes periodic variations

**3. Tidal Effects**
- Phobos is spiraling **inward** (opposite of Moon!)
- Will eventually crash into Mars (50 million years)
- Creates small oscillations

**Prediction:** Osculating elements valid for **hours to 1 day** only

### Testing Osculating Elements

**Our systematic approach:**

1. **Moon (COMPLETE)** ✅
   - Result: Perfect match at epoch
   - Diverges after ~2 weeks
   - Proves osculating concept works

2. **Phobos (NEXT)** 🔄
   - Prediction: Faster divergence than Moon
   - Will show extreme perturbation effects
   - Test of osculating validity for highly perturbed systems

3. **Deimos** 🔄
   - Prediction: Similar to Moon
   - More distant, less perturbed

4. **Jovian/Saturnian moons** (FUTURE)
   - Range of perturbation environments
   - Compare behavior across different systems

---

## Coordinate Systems

### J2000 Ecliptic Frame (Used by Paloma's Orrery)

**Reference plane:** Earth's orbital plane (ecliptic) at J2000 epoch (January 1, 2000, 12:00 TT)

**Axes:**
- **+X:** Points toward vernal equinox (where Sun crosses equator going north)
- **+Y:** 90° ahead of X in ecliptic plane (toward summer solstice direction)
- **+Z:** Perpendicular to ecliptic, toward ecliptic north pole

**Why J2000?**
- Standard epoch for astronomy
- Fixed reference (doesn't precess with Earth's axis)
- Used by JPL Horizons and most astronomical databases

### Orbital Elements in J2000 Ecliptic

**When JPL Horizons returns osculating elements:**
- Inclination (i) is relative to **ecliptic plane**
- Longitude of ascending node (Ω) measured from **vernal equinox**
- All coordinates in **J2000 Ecliptic frame**

**Example - Moon:**
- i = 5.00° means 5° from ecliptic (not from Earth's equator!)
- Earth's equator is tilted 23.4° from ecliptic
- Moon actually orbits ~5° from ecliptic, which is ~18-28° from Earth's equator

### Visualizing Coordinate Systems

**In Paloma's Orrery:**
1. Use "Coordinate System Reference Guide" visualization
2. See +X, +Y, +Z axes clearly labeled
3. Understand ecliptic plane orientation
4. See how orbital elements relate to these axes

**In "Orbital Parameter Visualization":**
1. See how inclination (i) tilts orbit from ecliptic
2. See how Ω rotates the orbital plane
3. See how ω orients the ellipse within the plane
4. Watch transformation from perifocal → J2000 Ecliptic

---

## Visualizing Orbital Mechanics

### Available Tools in Paloma's Orrery

**1. Orbital Parameter Visualization** (`orbital_param_viz.py`)
- Interactive 3D demonstration of Keplerian elements
- Shows inclination, Ω, and ω transformations
- Demonstrates perifocal → J2000 Ecliptic transformation
- **Educational value:** See how elements define orbit orientation

**2. Coordinate System Reference Guide**
- Shows J2000 Ecliptic axes clearly
- +X toward vernal equinox
- +Y 90° ahead in ecliptic
- +Z toward ecliptic north
- **Educational value:** Understand reference frame

**3. Interactive Eccentricity Demo**
- Explore orbit shapes from circles to hyperbolas
- See how e changes orbit from ellipse to escape trajectory
- **Educational value:** Understand eccentricity intuitively

**4. Main Orrery Visualization**
- **Actual orbits** (white/colored lines): Real trajectories from JPL vectors
- **Ideal orbits** (dotted lines): Osculating Keplerian orbits
- **Compare them:** See perturbation effects over time
- **Educational value:** Watch osculating orbits "kiss" and diverge

### How to Use These Tools for Learning

**Understanding J2:**
1. Plot Moon orbit in main orrery
2. Watch over weeks/months
3. Notice how actual orbit deviates from ideal
4. Read hover text about perturbations
5. Understand: J2 causes Ω to rotate 19.3°/year

**Understanding Osculating Elements:**
1. Plot Moon with ideal orbit enabled
2. Hover over ideal orbit → see "osculating" explanation
3. Watch how ideal orbit matches at epoch
4. See divergence over time
5. Understand: Perturbations accumulate continuously

**Understanding Coordinate Systems:**
1. Open Orbital Parameter Visualization
2. See how i, Ω, ω work together
3. Open Coordinate System Reference Guide
4. Understand J2000 Ecliptic frame
5. Connect: Elements → Orientation in space

---

## Educational Philosophy

**Paloma's Orrery aims to make orbital mechanics accessible through:**

1. **Visual learning:** See concepts, don't just read about them
2. **Interactive exploration:** Change parameters, see results
3. **Real data:** Use actual JPL calculations, not simplified models
4. **Clear explanations:** Hover text, documentation, guides
5. **Progressive complexity:** Simple views first, detailed later

**For students:**
- Start with main orrery visualization
- Read hover text on ideal orbits
- Explore orbital parameter visualization
- Read this guide for deeper understanding

**For educators:**
- Use visualizations in classroom
- Reference this guide for technical details
- Show real examples (Moon, Phobos) of concepts
- Connect theory to observable phenomena

**For enthusiasts:**
- Dive deep into coordinate systems
- Compare osculating vs actual orbits
- Test predictions (Phobos divergence rate)
- Contribute to understanding

---

## References and Further Reading

**Orbital Mechanics Textbooks:**
- Vallado, D.A. "Fundamentals of Astrodynamics and Applications" (2013)
- Curtis, H.D. "Orbital Mechanics for Engineering Students" (2020)
- Roy, A.E. "Orbital Motion" (2005)

**Online Resources:**
- [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/app.html) - Source of our ephemeris data
- [NASA Solar System Dynamics](https://ssd.jpl.nasa.gov/) - Technical documentation
- [Celestrak](https://celestrak.org/) - Satellite tracking and orbital mechanics

**Papers on Perturbations:**
- Chapront, J., et al. "A new determination of lunar orbital parameters, precession constant and tidal acceleration from LLR measurements" (2002)
- Emelyanov, N.V. "Influence of J2 on Orbits of Satellites" (2016)

**Historical Context:**
- Kepler's laws (1609, 1619) - Foundation of orbital mechanics
- Newton's *Principia* (1687) - Gravitational theory
- Laplace (1799-1825) - Perturbation theory development
- Modern numerical integration - JPL Development Ephemeris (DE)

---

## Glossary

**Apsidal precession:** Rotation of the ellipse within its plane (ω changes)
**Ascending node:** Point where orbit crosses reference plane going "up" (northward)
**Ecliptic:** Earth's orbital plane around the Sun
**J2000:** Standard epoch (Jan 1, 2000, 12:00 TT) for astronomical coordinates
**Keplerian orbit:** Perfect two-body elliptical orbit (no perturbations)
**Nodal precession:** Rotation of orbital plane around planet's axis (Ω changes)
**Oblateness:** Flattening at poles, bulging at equator
**Osculating elements:** Keplerian elements that "kiss" actual orbit at one instant
**Periapsis:** Closest point in orbit to central body
**Perturbation:** Force causing deviation from Keplerian orbit
**Vernal equinox:** Direction where Sun crosses equator going north (March ~20)

---

*"Understanding how orbits deviate from perfect ellipses teaches us about the real complexity of celestial mechanics."*

*"J2 reminds us: Planets aren't perfect spheres, and neither are their orbits!"*

*"Osculating elements 'kiss' reality at one moment, then show us how perturbations accumulate over time."*

---

**Last updated:** November 20, 2025  
**Author:** Tony Quintanilla (with Claude)  
**Project:** Paloma's Orrery  
**Website:** https://tonylquintanilla.github.io/palomas_orrery/
