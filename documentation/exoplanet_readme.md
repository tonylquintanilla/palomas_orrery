# Exoplanet Integration for Paloma's Orrery
## Complete Documentation & User Guide

**Version:** 2.7  
**Date:** October 28, 2025  
**Status:** FULLY INTEGRATED & OPERATIONAL  
**Author:** Tony Quintanilla with Claude AI

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Start Guide](#quick-start-guide)
3. [User Interface](#user-interface)
4. [Systems Included](#systems-included)
5. [How to Use](#how-to-use)
6. [Animation Guide](#animation-guide-new-in-v25) NEW!
7. [Architecture & Design](#architecture--design)
8. [Module Documentation](#module-documentation)
9. [Technical Reference](#technical-reference)
10. [Troubleshooting](#troubleshooting)
11. [Future Enhancements](#future-enhancements)

---

## Overview

### What's New in Version 2.7

**Comet Visualization & Animation Fix (October 28, 2025):**
- **Comet Tail Rendering** - Scientific visualization of comets with dual-tail structures
  - Dust tails (Type II): Curved, golden/yellow from reflected sunlight
  - Ion tails (Type I): Straight blue streamers from CO+ emissions
  - Green coma from C2 (dicarbon) emissions
  - Activity scaling based on solar distance
- **Astrophotography Color Accuracy** - Tail colors match long-exposure photography appearance
  - Dust tails: Whitish-yellow/gold (reflects full visible spectrum 400-700nm)
  - Ion tails: Blue from CO+ emissions (400-460nm)
  - Historical comet data: Halley, Hale-Bopp, NEOWISE, Lemmon, Hyakutake, Ikeya-Seki
- **Animation Bug Fix** - Fixed `UnboundLocalError` preventing solar system object animation
  - `binary_star_positions_over_time` now initialized before conditional blocks
  - Animations of comets, planets, and other objects work correctly
  - Exoplanet and solar system animations fully operational

### What's New in Version 2.6

**Binary Star Opposition Fix (October 25, 2025):**
- **Critical Physics Bug Fixed** - Binary stars now maintain perfect 180° opposition throughout entire orbit
- **Proper Orbital Mechanics** - Phase offset now applied to true anomaly in orbital plane (not post-processed rotation)
- **Identical Angular Velocities** - Both stars rotate at exactly the same rate around barycenter
- **Realistic Motion** - Stars "dance" directly across from each other, maintaining opposite sides
- **Same Direction Rotation** - Both stars orbit counter-clockwise together (as real binary systems do)
- **Verified Accuracy** - Tested across multiple dates confirming 180.0° separation at all times

**What Was Wrong (v2.1-2.5):**
- Stars were calculated from same orbital phase, then Star B rotated statically
- This caused stars to move in nearly the same direction
- Angular separation varied (170°-147°) instead of constant 180°
- Violated fundamental binary star physics

**What's Fixed:**
- Both stars share same mean anomaly (orbit together)
- Both stars share same true anomaly (same orbital phase)
- Phase offset (180°) applied to true anomaly before Cartesian conversion
- Results in perfect opposition with identical angular velocities
- TOI-1338 binary now displays physically accurate dynamics!

**Visual Result:**
```
Before Fix: Oct 25-27 showed stars getting CLOSER (170.6° → 156.5° → 147.3°)
After Fix:  Oct 25-27 shows perfect opposition (180.0° → 180.0° → 180.0°)
```

### What's New in Version 2.5

**Exoplanet Animation Support (October 24, 2025):**
- **Full Animation Integration** - `animate_objects()` now supports exoplanet systems with Keplerian orbit calculations
- **Time-Evolving Visualizations** - Watch planets move along their orbits over days, months, or years
- **Automatic Mode Detection** - Animation system automatically detects exoplanet objects and switches to appropriate coordinate system
- **Keplerian Position Calculation** - Positions calculated for each frame using analytical orbital mechanics (no JPL Horizons needed)
- **Dynamic Axis Scaling** - Automatically adjusts view range for compact exoplanet systems (0.01-5 AU typical)
- **Coordinate System Labeling** - Animation displays correct coordinate system (Sky Plane for exoplanets, J2000 Ecliptic for solar system)
- **Binary Star Motion** - Animate both stars orbiting their barycenter in binary systems
- **Performance Optimized** - Efficient position calculation for hundreds of frames
- **Feature Parity** - Animation now has same exoplanet support as static plotting

**What You Can Animate:**
- TRAPPIST-1's 7 planets completing multiple orbits
- Kepler-16 binary stars with circumbinary planet
- Proxima Centauri's rapid orbital motion (11-day period)
- Multiple systems simultaneously
- Custom date ranges and time steps

### What's New in Version 2.4

**Center Marker Suppression (October 24, 2025):**
- **Transparent Center Markers** - Exoplanet host stars can now be selected as center objects without displaying a redundant marker
- **Clean Legend** - Transparent center objects automatically hidden from legend (no blank entries)
- **Dual Star Representation** - When Proxima Centauri is selected as center, no red marker appears; when checkbox is selected, orange stellar-properties-based marker displays
- **Intelligent Color Detection** - Center marker code detects `rgba(0,0,0,0)` transparent colors and suppresses legend entries
- **Visual Clarity** - Eliminates confusing dual markers (red center + orange system) for the same object
- **Maintained Functionality** - Center object still functions normally for coordinate system origin and view centering

### What's New in Version 2.3

**Enhanced Stellar Visualization (October 24, 2025):**
- **Temperature-Based Star Colors** - Exoplanet host stars now display realistic colors based on their effective temperature (continuous interpolation from red M-dwarfs to blue hot stars)
- **Rich Hover Information** - Host stars show comprehensive stellar properties matching the quality of stellar neighborhood visualizations
- **Stellar Classification** - Full spectral type parsing with luminosity class descriptions (Main-sequence, Giant, Supergiant, etc.)
- **Integrated Stellar Module** - New `exoplanet_stellar_properties.py` reuses proven calculation functions from star visualization pipeline
- **Luminosity-Based Sizing** - Star marker sizes scaled by luminosity for visual hierarchy
- **Binary Star Support** - Enhanced hover text for both components in binary systems (TOI-1338 A & B)
- **Consistency Across Orrery** - Exoplanet host stars use same color scale and temperature calculations as stellar neighborhood visualizations

### What's New in Version 2.2

**Coplanar Orbits & Performance Fix (October 23, 2025):**
- **Fixed Binary Orbit Geometry** - Binary stars now orbit in the same plane as planets (coplanar)
- **Correct Inclination** - TOI-1338 binary orbit set to i=89° matching planet orbital plane
- **No JPL Horizons Errors** - Stopped attempting to fetch exoplanet data from JPL (not available)
- **Improved Performance** - No wasted API calls, faster loading
- **Physical Accuracy** - System now matches real TOI-1338 geometry (edge-on, coplanar)
- **Enhanced Coordinate Legend** - Context-aware explanations appear when viewing exoplanets, clarifying viewing geometry and sky plane concept

### What Was New in Version 2.1

**Binary System Fix (October 22, 2025):**
- **Fixed Plotly Symbol Errors** - Changed invalid `symbol='star'` to `symbol='circle'`
- **TOI-1338 Barycenter Support** - Added proper barycenter object for binary star systems
- **Fixed Binary Star Plotting** - Both stars now correctly orbit the system's center of mass
- **Fixed Planet Visibility** - Circumbinary planets (TOI-1338 b & c) now plot correctly
- **Improved Center Selection** - "TOI-1338 A/B (Barycenter)" option added to dropdown
- **Clean Legend** - Orbit paths hidden from legend, showing only objects

### What Was New in Version 2.0

Paloma's Orrery now includes **fully integrated exoplanet system visualization**, allowing you to explore confirmed exoplanet systems with accurate 3D orbital mechanics. This is a **complete end-to-end implementation** - not a prototype!

### Key Features

- **3 Exoplanet Systems** with 11 planets total
- **Seamless UI Integration** - exoplanets appear alongside Solar System objects
- **System-Specific Centering** - select host stars as center objects
- **Binary Star Support** - circumbinary planets (real "Tatooine" systems!)
- **Habitable Zone Highlighting** - 5 planets in habitable zones
- **Accurate Orbital Mechanics** - Keplerian orbits with proper inclinations
- **Animation Support** - watch exoplanet systems evolve over time
- **Proper Motion Corrections** - stellar positions updated for nearby stars
- **Discovery Metadata** - methods, dates, discoverers included

### What You Can Do Now

- **Visualize TRAPPIST-1** and its 7 Earth-sized planets
- **Explore TOI-1338** circumbinary system (planets orbiting two stars!)
- **Examine Proxima Centauri** - the nearest exoplanet to Earth
- **Compare systems** - view multiple exoplanet systems simultaneously
- **Animate orbits** - watch planets move in their orbits over time (fully supported in v2.5!)
- **Create time-lapse animations** - see orbital motion over days, months, or years
- **Animate binary stars** - watch stellar pairs orbit their common center of mass
- **Learn about discoveries** - hover over objects for detailed information

---

## Quick Start Guide

### For First-Time Users

**1. Launch Paloma's Orrery:**
```bash
python palomas_orrery.py
```

**2. Select an Exoplanet System:**
- Scroll down in the **"Select Objects to Plot"** panel
- Find the **"EXOPLANET SYSTEMS"** section (green separator)
- Check the boxes for planets you want to see
 - Example: Check **TRAPPIST-1 b**, **TRAPPIST-1 e**, **TRAPPIST-1 g**

**3. Set the Center:**
- In the **"Center Object"** dropdown (top of window)
- Select **"TRAPPIST-1"** as the center
 - This puts the host star at the origin (0, 0, 0)

**4. Click "Plot Objects"**
- A new browser window will open showing your visualization!
- You'll see the TRAPPIST-1 star at center (yellow)
- Selected planets will orbit around it with their actual paths

**5. Interact with the Plot:**
- **Rotate:** Click and drag
- **Zoom:** Scroll wheel or pinch
- **Pan:** Right-click and drag
- **Toggle objects:** Click legend entries to show/hide
- **Hover:** Mouse over objects for detailed information

### Quick Examples

**Example 1: TRAPPIST-1 Habitable Zone**
```
Center: TRAPPIST-1
Select: TRAPPIST-1 d, e, f, g (the habitable zone planets)
Result: See the 4 potentially habitable planets in green/blue
```

**Example 2: TOI-1338 Binary System**
```
Center: TOI-1338 A/B (Barycenter)
Select: TOI-1338 A/B (Barycenter), TOI-1338 A, TOI-1338 B, TOI-1338 b, TOI-1338 c
Result: Watch both stars orbit the barycenter, planets orbit around both!
```

**Example 3: Proxima Centauri (Nearest)**
```
Center: Proxima Centauri
Select: Proxima Centauri b, Proxima Centauri d
Result: View the nearest exoplanet system - just 4.24 light-years away!
```

**Example 4: TRAPPIST-1 Animation (NEW in v2.5)**
```
Center: TRAPPIST-1
Select: TRAPPIST-1 (star), TRAPPIST-1 b, e, f, g
Frames: 100
Step: Daily
Click: "Animate Daily"
Result: Watch 4 planets orbit over 100 days, habitable zone planets highlighted in green!
```

**Example 5: TOI-1338 Binary Animation (NEW in v2.5)**
```
Center: TOI-1338 A/B (Barycenter)
Select: TOI-1338 A, TOI-1338 B, TOI-1338 b
Frames: 50
Step: Daily
Click: "Animate Daily"
Result: Watch binary stars orbit barycenter while planet orbits both stars!
```

**Example 6: Proxima b Rapid Orbit (NEW in v2.5)**
```
Center: Proxima Centauri
Select: Proxima Centauri (star), Proxima Centauri b
Frames: 30
Step: Daily
Click: "Animate Daily"
Result: See Proxima b complete nearly 3 full orbits in 30 days (11.2-day period)!
```

---

## User Interface

### Checkbox Organization

The **"Select Objects to Plot"** panel now includes:

```
[ ] SOLAR SYSTEM OBJECTS
 [x] Mercury
 [x] Venus
 [x] Earth
 ... (Solar System continues)

[ ] EXOPLANET SYSTEMS New Section!

 TRAPPIST-1 System (40.5 ly)
 [x] TRAPPIST-1 b Individual planets
 [x] TRAPPIST-1 c
 [x] TRAPPIST-1 d (HZ) (HZ) = Habitable Zone
 [x] TRAPPIST-1 e (HZ)
 [x] TRAPPIST-1 f (HZ)
 [x] TRAPPIST-1 g (HZ)
 [x] TRAPPIST-1 h

 TOI-1338 System (1,292 ly)
 [x] TOI-1338 A/B (Barycenter) System center of mass
 [x] TOI-1338 A (G-type) Binary star primary
 [x] TOI-1338 B (M-type) Binary star secondary
 [x] TOI-1338 b
 [x] TOI-1338 c

 Proxima Centauri System (4.24 ly)
 [x] Proxima Centauri b (HZ)
 [x] Proxima Centauri d
```

### Center Object Dropdown

The **"Center Object"** dropdown now includes:

```
 Center Object:
 Sun Solar System centers
 Mercury
 Venus
 Earth
 ...
 Planet 9

 TRAPPIST-1 Exoplanet host stars (NEW!)
 TOI-1338 A/B (Barycenter) Binary system center (NEW in v2.1!)
 Proxima Centauri
```

**Important:** When you select an exoplanet host star as center:
- That star appears at the origin (0, 0, 0)
- Only objects from that system are visible
- Solar System objects are automatically filtered out
- The visualization focuses on that single exoplanet system

### Legend and Hover Information

**Legend Shows:**
- Object names with system identifier
- Color-coded by object type
- Clickable to toggle visibility

**Coordinate System Legend (New in v2.2):**
- Shows J2000 Ecliptic coordinate system information
- **Context-aware:** Automatically adds explanatory text when viewing exoplanets
- Clarifies that +X always points toward vernal equinox ()
- Explains +Z points toward Earth for exoplanet observations
- Helps understand viewing geometry and "sky plane" concept
- Makes inclination angles intuitive (i=0° face-on, i=90° edge-on)

**Hover Information Includes:**
- Object name and designation
- Orbital period (days/years)
- Semi-major axis (AU)
- Eccentricity
- Mass (Earth masses for planets)
- Radius (Earth radii for planets)
- Distance from star
- Discovery method and year
- Habitable zone status (if applicable)

---

## Systems Included

### 1. TRAPPIST-1 System

**"The Jewel" - 7 Earth-sized planets, 4 in habitable zone**

```
Distance: 40.5 light-years (12.43 pc)
Star Type: M8V ultracool red dwarf
Star Mass: 0.09 M (9% of Sun's mass)
Temperature: 2,566 K (dim and cool)
Planets: 7 terrestrial worlds (all transiting)
HZ Planets: d, e, f, g (4 potentially habitable!)
Discovery: 2017 (TRAPPIST telescope + Spitzer Space Telescope)
Notable: Orbital resonances, JWST atmospheric observations ongoing
```

**Why TRAPPIST-1 is Special:**
- **Most potentially habitable planets ever found** in a single system
- **TRAPPIST-1 e** is considered the most likely to have liquid water
- All 7 planets are roughly Earth-sized (0.76 - 1.13 R)
- Complex orbital resonances stabilize the system
- Prime target for JWST atmospheric characterization
- Nearest multi-planet system to Earth

**Planets in Detail:**

| Planet | Period | Distance | Mass | Radius | Temperature | Status |
|--------|--------|----------|------|--------|-------------|--------|
| **b** | 1.51 d | 0.0115 AU | 1.37 M | 1.12 R | ~400 K | Too hot |
| **c** | 2.42 d | 0.0158 AU | 1.31 M | 1.10 R | ~342 K | Too hot |
| **d** ° | 4.05 d | 0.0223 AU | 0.39 M | 0.79 R | ~288 K | **HZ (inner edge)** |
| **e** ° | 6.10 d | 0.0293 AU | 0.69 M | 0.92 R | ~251 K | **HZ (optimal!)** |
| **f** ° | 9.21 d | 0.0385 AU | 1.04 M | 1.05 R | ~219 K | **HZ** |
| **g** ° | 12.35 d | 0.0468 AU | 1.32 M | 1.13 R | ~198 K | **HZ (outer edge)** |
| **h** | 18.77 d | 0.0619 AU | 0.33 M | 0.76 R | ~173 K | Too cold |

° = In habitable zone (liquid water possible)

**Educational Value:**
- Demonstrates how many Earth-sized planets can form around small stars
- Shows orbital resonances in action (8:5, 5:3, 3:2, 3:2, 4:3 period ratios)
- Illustrates habitable zone scaling with stellar luminosity
- Real-world example of transit photometry method

---

### 2. TOI-1338 System °° (Circumbinary)

**"Real Tatooine" - Planets orbiting two stars in coplanar configuration**

```
Distance: 1,292 light-years (396 pc)
Star A: G-type (1.1 M, 6100 K) - like our Sun
Star B: M-type (0.3 M, 3450 K) - red dwarf
Binary Period: 14.6 days (stars orbit each other)
Separation: 0.088 AU between stars
Binary Inc.: 89° (edge-on, coplanar with planets) Fixed in v2.2!
Planets: 2 circumbinary (orbit both stars)
Discovery: 2020 (TESS), by Wolf Cukier (17-year-old NASA intern!)
Notable: Only second known multi-planet circumbinary system
```

**Why TOI-1338 is Special:**
- **Student discovery story** - discovered by high school intern Wolf Cukier on his third day at NASA!
- **Real "Tatooine"** - planets that experience sunsets from two different suns
- **Coplanar system** - stars and planets all orbit in same nearly edge-on plane (v2.2 fix)
- **Edge-on view** (i 89°) allows observation of transits across both stars
- Tests planet formation theories in binary star environments
- Shows that planets can survive in dynamically complex systems
- Both planets orbit outside the "instability zone" where tidal forces would tear them apart

**Binary Star System:**
- **Primary (Star A):** G2V star, 1.1 solar masses, 6100 K (yellow, Sun-like)
- **Secondary (Star B):** M0V star, 0.3 solar masses, 3450 K (red dwarf)
- **Binary orbit:** 14.6-day period, 0.088 AU separation
- **Barycenter:** Both stars orbit their common center of mass
 - Star A orbits at 0.019 AU from barycenter
 - Star B orbits at 0.069 AU from barycenter

**Circumbinary Planets:**

| Planet | Period | Distance | Type | Discovery Method |
|--------|--------|----------|------|------------------|
| **b** | 95.2 d | 0.461 AU | Neptune-size (6.9 R) | Transit, 2020 |
| **c** | 215.5 d | 0.76 AU | Jupiter-mass | Radial velocity, 2023 |

**What You'll See in Paloma's Orrery:**
- Both stars shown orbiting around the barycenter (center point)
- Stars appear to "dance" around each other in 14.6-day period
- Planets orbit far outside, circling both stars together
- Educational demonstration of three-body dynamics

**Educational Value:**
- Shows binary star orbital mechanics
- Demonstrates stability zones in circumbinary systems
- Illustrates multiple discovery methods (transit + radial velocity)
- Relatable "Tatooine" pop culture connection

**Binary System Visualization (v2.1 Enhancement):**

In version 2.1, TOI-1338's binary star system is now correctly visualized with **proper barycentric dynamics**:

**The Barycenter (Center of Mass):**
- Appears as a white 'X' marker at the origin (0, 0, 0)
- This is the point both stars orbit around
- Represents the system's center of mass - the balance point
- Physically accurate representation of binary star dynamics

**How the Stars Move:**
- **Star A (yellow, 1.1 M)** orbits **0.019 AU** from barycenter
 - More massive, so orbits closer to the center
- **Star B (orange, 0.3 M)** orbits **0.069 AU** from barycenter
 - Less massive, so orbits farther from the center
- Both stars always on **opposite sides** of the barycenter
- Complete one orbit every **14.6 days**

**How the Planets Move:**
- Both planets orbit the **barycenter** (not individual stars!)
- Planet b: 0.461 AU from barycenter, 95-day period
- Planet c: 0.76 AU from barycenter, 216-day period
- These circumbinary orbits are stable because they're far enough from the central stars

**To View This Correctly:**
1. Select **"TOI-1338 A/B (Barycenter)"** as the center object
2. Check boxes for:
 - TOI-1338 A/B (Barycenter)
 - TOI-1338 A (G-type)
 - TOI-1338 B (M-type)
 - TOI-1338 b
 - TOI-1338 c
3. Set scale to **1 AU** for best view
4. Watch the binary "dance" with both planets orbiting the system!

**Why This Matters:**
- Shows real physics - stars don't orbit each other; they orbit their common center of mass
- Demonstrates conservation of momentum in binary systems
- Educational for understanding multi-body orbital dynamics
- Accurate representation of how circumbinary planets actually work

---

### 3. Proxima Centauri System ° (Nearest Exoplanet!)

**"The Neighbor" - Closest confirmed exoplanet to Earth**

```
Distance: 4.24 light-years (1.30 pc) - NEAREST STAR!
Star Type: M5.5V red dwarf
Star Mass: 0.12 M (12% of Sun's mass)
Temperature: 3,042 K (cool and dim)
Planets: 2 confirmed (Proxima b and d)
Proper Motion: 3.85 arcsec/year (VERY HIGH - closest star moves noticeably!)
Discovery: 2016 (Proxima b), 2022 (Proxima d)
Notable: Target for future interstellar missions (Breakthrough Starshot)
```

**Why Proxima Centauri is Special:**
- **NEAREST EXOPLANET** - just 4.24 light-years away!
- Part of the **Alpha Centauri triple star system** (our nearest stellar neighbors)
- **Proxima b** potentially habitable, but stellar flares are a challenge
- **Proxima d** is one of the lightest exoplanets ever detected (0.26 M)
- **Highest proper motion** of any exoplanet host star - moves 3.85 arcsec/year!
- Prime target for proposed interstellar probes (Project Starshot aims to reach it in 20-30 years)

**Planets in Detail:**

| Planet | Period | Distance | Mass | Status | Discovery |
|--------|--------|----------|------|--------|-----------|
| **d** | 5.1 d | 0.029 AU | 0.26 M | Too hot | 2022, VLT ESPRESSO (lightest RV planet!) |
| **b** ° | 11.2 d | 0.049 AU | 1.27 M | **HZ** | 2016, ESO 3.6m (historic discovery!) |

° = In habitable zone

**Proxima b - The Nearest Potentially Habitable World:**
- Orbital period: 11.2 days (very short "year"!)
- Likely tidally locked (one side always faces the star)
- Temperature estimate: 234 K (with atmosphere, could be habitable)
- **Challenge:** Proxima Centauri is a flare star - frequent radiation bursts
- **Possibility:** Thick atmosphere or magnetic field could protect life
- **JWST observations:** Planned to search for atmospheric signatures

**Educational Value:**
- Nearest exoplanet makes distance scales tangible
- Demonstrates radial velocity detection method
- Shows challenges of M-dwarf habitability (tidal locking, flares)
- Tests proper motion correction code (star moves noticeably across sky)
- Connects to real space mission proposals

---

## How to Use

### Workflow 1: Visualize a Single Exoplanet System

**Goal:** View the TRAPPIST-1 system and its habitable zone planets

**Steps:**

1. **Launch the application:**
 ```bash
 python palomas_orrery.py
 ```

2. **Scroll to Exoplanet Systems section:**
 - In the "Select Objects to Plot" panel
 - Scroll down past Solar System objects
 - Look for green "EXOPLANET SYSTEMS" separator

3. **Select TRAPPIST-1 planets:**
 - Check: [ ] TRAPPIST-1 d (HZ)
 - Check: [ ] TRAPPIST-1 e (HZ)
 - Check: [ ] TRAPPIST-1 f (HZ)
 - Check: [ ] TRAPPIST-1 g (HZ)
 - (The four habitable zone planets)

4. **Set center to TRAPPIST-1:**
 - Find "Center Object" dropdown at top
 - Select: **TRAPPIST-1**

5. **Click "Plot Objects"**
 - 3D visualization opens in browser
 - TRAPPIST-1 star at center (yellow marker)
 - Four planets shown in their orbits (green/blue markers)
 - Orbital paths visible as thin lines

6. **Explore the visualization:**
 - Rotate the view to see orbit inclinations
 - Hover over planets for detailed information
 - Note the orbital resonances (spacing patterns)
 - Compare planet sizes and distances

**Expected Result:**
- Beautiful 3D view of TRAPPIST-1 habitable zone
- Planets color-coded (green = habitable zone)
- Orbit paths show true 3D orientation
- Hovering shows: period, mass, radius, discovery method

---

### Workflow 2: Animate an Exoplanet System

**Goal:** Watch TOI-1338 binary star system orbit over time

**Steps:**

1. **Select TOI-1338 objects:**
 - Check: [ ] TOI-1338 (binary star)
 - Check: [ ] TOI-1338 b
 - Check: [ ] TOI-1338 c

2. **Set center to TOI-1338:**
 - Center Object dropdown **TOI-1338**

3. **Configure animation:**
 - Set time range: Start date and end date
 - Set time step: Recommend 1-2 days for smooth motion
 - Number of frames: 50-100 for good resolution

4. **Click "Animate Objects"**
 - Animation renders (may take 30-60 seconds)
 - Browser opens with playback controls

5. **Play the animation:**
 - Click Play button
 - Watch both stars orbit the barycenter
 - See planets circling around both stars
 - Note the 14.6-day binary period

**Tips:**
- Use short time ranges for binary dynamics (30-60 days)
- Increase time range to see planet motion (200-500 days)
- Rotate view while animation plays for 3D perspective

---

### Workflow 3: Compare Solar System and Exoplanet Scales

**Goal:** Understand size differences between systems

**Steps:**

1. **First, plot Solar System inner planets:**
 - Center: **Sun**
 - Select: Mercury, Venus, Earth, Mars
 - Click "Plot Objects"
 - Note the scale (Mercury at 0.39 AU, Mars at 1.52 AU)

2. **Then, plot TRAPPIST-1 system:**
 - Center: **TRAPPIST-1**
 - Select: TRAPPIST-1 b through h (all 7 planets)
 - Click "Plot Objects"
 - Note: ALL 7 planets fit inside Mercury's orbit!

3. **Compare:**
 - TRAPPIST-1 h (outermost) at 0.062 AU
 - Mercury (innermost in Solar System) at 0.39 AU
 - TRAPPIST-1's entire system is 6 more compact!

**Why the difference?**
- TRAPPIST-1 is a dim M-dwarf (2566 K)
- Sun is a bright G-dwarf (5778 K)
- Habitable zone scales with star luminosity
- Dimmer stars planets must be closer to stay warm

---

### Workflow 4: Study Orbital Inclinations

**Goal:** See how orbits are tilted relative to line of sight

**Steps:**

1. **Plot TRAPPIST-1 system:**
 - Center: TRAPPIST-1
 - Select: All 7 planets (b through h)
 - Click "Plot Objects"

2. **Set view to edge-on:**
 - Rotate plot so you're looking at orbits edge-on
 - Notice: Orbits appear as thin ellipses
 - This is the view we see from Earth (transiting systems)

3. **Rotate to face-on view:**
 - Rotate 90° to see orbits from "above"
 - Notice: Orbits now appear as circles/ellipses
 - This shows true orbital geometry

4. **Observe inclinations:**
 - TRAPPIST-1 planets: ~89.7° (nearly edge-on)
 - That's why we see transits from Earth!
 - Slight variations cause different transit depths

**Educational insight:**
- We only detect transiting planets when orbit is edge-on from Earth
- Face-on systems (inclination near 0°) don't transit
- TRAPPIST-1's edge-on orientation is lucky for science!

---

### Workflow 5: Explore Proper Motion (Proxima Centauri)

**Goal:** See how nearby stars move across the sky over decades

**Steps:**

1. **Animate Proxima Centauri over 50 years:**
 - Center: Proxima Centauri
 - Select: Proxima Centauri b, Proxima Centauri d
 - Set start date: January 1, 2000
 - Set end date: January 1, 2050
 - Time step: 365 days (annual)
 - Click "Animate Objects"

2. **Watch the animation:**
 - **Planets orbit the star** (11.2 and 5.1 day periods)
 - **Star itself doesn't move** (stays at origin)
 - This is correct! Local coordinates centered on star

3. **Compare to distant systems:**
 - Try same animation for TOI-1338 (1292 light-years away)
 - Notice: Proper motion negligible for distant stars
 - Proxima's proper motion (3.85 arcsec/year) only matters for stellar neighborhood visualization

**Technical note:**
- Proper motion is encoded in stellar position data
- Not directly visible in single-system plots
- Will be important for Phase 4 (stellar neighborhood in galactic coordinates)

---

---

## Animation Guide (New in v2.5!)

### Animation Overview

Paloma's Orrery now supports full animation of exoplanet systems! Watch planets orbit their host stars over time with accurate Keplerian mechanics. The animation system is fully integrated into the `animate_objects()` function with specialized support for exoplanet orbital calculations.

### What You Can Animate

1. **Individual Exoplanet Systems**
   - TRAPPIST-1's 7 planets completing orbits
   - Proxima Centauri's rapid orbital motion (11-day periods)
   - TOI-1338 circumbinary system with binary stars

2. **Binary Star Dynamics**
   - Watch stellar pairs orbit their common center of mass
   - TOI-1338 A & B with 14.6-day binary period
   - Coplanar orbits (stars and planets in same plane)

3. **Time-Lapse Sequences**
   - Daily steps for rapid orbits (Proxima Centauri b)
   - Monthly steps for medium periods (TRAPPIST-1)
   - Yearly steps for longer comparisons

### How to Create Animations

**Basic Steps:**

1. **Select Objects** - Check boxes for exoplanets, host stars, or entire systems
2. **Set Time Range** - Use "Days to Plot" and "Number of Frames" 
3. **Choose Step Size** - "Animate Daily", "Animate Monthly", or "Animate Yearly"
4. **Click Animate** - Browser opens with time-evolving visualization

**Example Workflow - TRAPPIST-1:**

```
1. Center: TRAPPIST-1
2. Select: TRAPPIST-1 b, d, e, f, g (5 planets)
3. Days to Plot: 90 (3 months)
4. Number of Frames: 90
5. Click: "Animate Daily"
6. Result: 90 frames showing planets complete 1-7 orbits over 3 months
```

---

    print(f"\n[EXOPLANET ANIMATION MODE] Detected {len(exo_objects)} exoplanets and {len(exo_host_stars)} host stars")
```

**What This Does:**
- Scans all selected objects for exoplanet object types
- Sets `is_exoplanet_mode` flag for subsequent phases
- Enables conditional behavior (skip JPL, use Keplerian orbits, dynamic scaling)

#### Phase 2: Date Generation (line 5094)

```python
# Generate animation frame dates based on step size
dates_list = create_animation_dates(current_date, step, N)
# Returns: [datetime1, datetime2, ..., datetimeN]
```

**Time Step Mapping:**
- `'daily'` → 1 day increments
- `'monthly'` → ~30.4 day increments
- `'yearly'` → 365.25 day increments

**Example Output:**
```python
# For N=5 frames, daily step, starting 2025-01-01:
dates_list = [
    datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc),
    datetime(2025, 1, 2, 12, 0, tzinfo=timezone.utc),
    datetime(2025, 1, 3, 12, 0, tzinfo=timezone.utc),
    datetime(2025, 1, 4, 12, 0, tzinfo=timezone.utc),
    datetime(2025, 1, 5, 12, 0, tzinfo=timezone.utc)
]
```

#### Phase 3: Exoplanet Position Calculation (lines 5150-5205)

```python
exoplanet_positions_over_time = {}
if is_exoplanet_mode:
    from exoplanet_orbits import calculate_planet_position
    from exoplanet_systems import get_system
    
    # Get unique exoplanet systems
    exo_systems = set()
    for obj in exo_objects + exo_host_stars:
        system_id = obj.get('system_id')
        if system_id:
            exo_systems.add(system_id)
    
    # Process each system
    for system_id in exo_systems:
        system = get_system(system_id)
        if not system:
            continue
        
        print(f"[EXOPLANET ANIMATION] Processing {system['system_name']}")
        
        # For each selected exoplanet in this system
        for obj in exo_objects:
            if obj.get('system_id') == system_id and obj['var'].get() == 1:
                obj_name = obj['name']
                planet_id = obj.get('id')
                
                # Find planet data in catalog
                planet_data = None
                for catalog_planet in system['planets']:
                    if catalog_planet.get('planet_id') == planet_id:
                        planet_data = catalog_planet
                        break
                
                if planet_data:
                    print(f"[EXOPLANET ANIMATION] Generating positions for {obj_name} (period: {planet_data['period_days']:.2f} days)")
                    
                    # Calculate position at each animation date
                    positions = []
                    for date in dates_list:
                        x, y, z = calculate_planet_position(
                            a=planet_data['semi_major_axis_au'],
                            e=planet_data['eccentricity'],
                            i_deg=planet_data['inclination_deg'],
                            omega_deg=planet_data['arg_periapsis_deg'],
                            Omega_deg=planet_data['long_ascending_node_deg'],
                            period_days=planet_data['period_days'],
                            epoch=system['host_star']['epoch'],
                            date=date
                        )
                        positions.append({'x': x, 'y': y, 'z': z, 'date': date})
                    
                    exoplanet_positions_over_time[obj_name] = positions
                    print(f"[EXOPLANET ANIMATION] Generated {len(positions)} positions for {obj_name}")
```

**Key Insights:**
- Positions pre-calculated for ALL frames BEFORE animation generation
- Each planet gets its own position list (independent calculation)
- Uses Keplerian mechanics (analytical solution, no numerical integration)
- Fast execution: ~0.1 ms per position calculation

#### Phase 4: Binary Star Calculation (lines 5207-5266)

```python
binary_star_positions_over_time = {}

# Process each exoplanet system that has planets or barycenter selected
processed_systems = set()
for obj in exo_objects + exo_host_stars:
    if obj['var'].get() == 1:
        system_id = obj.get('system_id')
        
        # Skip if we've already processed this system
        if system_id in processed_systems or not system_id:
            continue
            
        system = get_system(system_id)
        if system and system['host_star'].get('is_binary'):
            print(f"[BINARY ANIMATION] Detected binary system: {system['system_name']}")

            from exoplanet_orbits import calculate_binary_star_orbits, calculate_binary_star_position
            
            host_star_system = system['host_star']
            star_A = host_star_system['star_A']
            star_B = host_star_system['star_B']
            
            # Calculate orbital parameters for both stars
            binary_params = calculate_binary_star_orbits(
                star_A['mass_solar'],
                star_B['mass_solar'],
                host_star_system['binary_separation_au'],
                host_star_system['binary_period_days'],
                host_star_system.get('binary_eccentricity', 0.0)
            )
            
            epoch = host_star_system['epoch']
            binary_i = host_star_system.get('binary_inclination_deg', 0.0)
            binary_Omega = host_star_system.get('binary_Omega_deg', 0.0)
            
            # Calculate Star A positions over time
            star_A_positions = []
            for date in dates_list:
                x_A, y_A, z_A = calculate_binary_star_position(
                    binary_params['star_A'], date, epoch, binary_i, binary_Omega
                )
                star_A_positions.append({'x': x_A, 'y': y_A, 'z': z_A, 'date': date})
            
            binary_star_positions_over_time[star_A['name']] = star_A_positions
            print(f"[BINARY ANIMATION] Generated {len(star_A_positions)} positions for {star_A['name']}")
            
            # Calculate Star B positions (similar pattern)
            star_B_positions = []
            for date in dates_list:
                x_B, y_B, z_B = calculate_binary_star_position(
                    binary_params['star_B'], date, epoch, binary_i, binary_Omega
                )
                star_B_positions.append({'x': x_B, 'y': y_B, 'z': z_B, 'date': date})
            
            binary_star_positions_over_time[star_B['name']] = star_B_positions
            print(f"[BINARY ANIMATION] Generated {len(star_B_positions)} positions for {star_B['name']}")
            
            # Mark this system as processed
            processed_systems.add(system_id)
```

**Binary Star Physics:**
- Both stars orbit their common center of mass (barycenter)
- More massive star has smaller orbit radius
- Less massive star has larger orbit radius
- Phase offset (180°) keeps stars on opposite sides

#### Phase 5: Trace Creation (lines 5508-5666)

```python
trace_indices = {}  # Map object names to trace indices

# Add initial position markers for exoplanets
if is_exoplanet_mode:
    for obj in exo_objects:
        obj_name = obj['name']
        if obj_name in exoplanet_positions_over_time:
            positions = exoplanet_positions_over_time[obj_name]
            if positions and len(positions) > 0:
                first_pos = positions[0]
                
                # Get planet data for hover text
                system_id = obj.get('system_id')
                system = get_system(system_id)
                planet_data = None
                if system:
                    planet_id = obj.get('id')
                    for catalog_planet in system['planets']:
                        if catalog_planet.get('planet_id') == planet_id:
                            planet_data = catalog_planet
                            break
                
                hover_text = f"<b>{obj_name}</b><br>"
                if planet_data:
                    from formatting_utils import format_maybe_float
                    hover_text += f"Period: {planet_data['period_days']:.2f} days<br>"
                    hover_text += f"Semi-major axis: {planet_data['semi_major_axis_au']:.4f} AU<br>"
                    hover_text += f"Mass: {format_maybe_float(planet_data.get('mass_earth'))} M⊕<br>"
                    if planet_data.get('in_habitable_zone'):
                        hover_text += "<br><b>☀ IN HABITABLE ZONE ☀</b>"
                
                trace = go.Scatter3d(
                    x=[first_pos['x']],
                    y=[first_pos['y']],
                    z=[first_pos['z']],
                    mode='markers',
                    marker=dict(
                        symbol='circle',
                        color=obj.get('color', 'lightblue'),
                        size=8 if planet_data and planet_data.get('in_habitable_zone') else 6
                    ),
                    name=obj_name,
                    text=[hover_text],
                    hoverinfo='text',
                    showlegend=True
                )
                fig.add_trace(trace)
                trace_indices[obj_name] = len(fig.data) - 1
    
    print(f"[EXOPLANET ANIMATION] Added {len([k for k in trace_indices if k in exoplanet_positions_over_time])} exoplanet traces")
```

**Trace Management:**
- Each animated object gets ONE trace (Scatter3d marker)
- `trace_indices` dict maps object name → trace index in fig.data
- Initial position set from first frame (positions[0])
- Hover text includes orbital parameters and habitable zone status

#### Phase 6: Frame Generation (lines 5732-5821)

```python
frames = []  # List of Plotly frames

for i in range(N):
    frame_data = list(fig.data)  # Start with base traces (shallow copy)
    current_date = dates_list[i]
    
    print(f"[ANIMATION DEBUG] Creating frame {i+1}/{N} for date {current_date}")
    
    # Update exoplanet positions
    for obj_name in exoplanet_positions_over_time:
        if obj_name in trace_indices:
            trace_idx = trace_indices[obj_name]
            positions = exoplanet_positions_over_time[obj_name]
            
            if i < len(positions):
                pos = positions[i]
                # Update trace position for this frame
                frame_data[trace_idx].x = [pos['x']]
                frame_data[trace_idx].y = [pos['y']]
                frame_data[trace_idx].z = [pos['z']]
                frame_data[trace_idx].visible = True
            else:
                frame_data[trace_idx].visible = False
    
    # Update binary star positions (similar pattern)
    for star_name in binary_star_positions_over_time:
        if star_name in trace_indices:
            trace_idx = trace_indices[star_name]
            positions = binary_star_positions_over_time[star_name]
            
            if i < len(positions):
                pos = positions[i]
                frame_data[trace_idx].x = [pos['x']]
                frame_data[trace_idx].y = [pos['y']]
                frame_data[trace_idx].z = [pos['z']]
                frame_data[trace_idx].visible = True
            else:
                frame_data[trace_idx].visible = False
    
    # Create frame with updated trace data
    frames.append(go.Frame(
        data=frame_data,
        name=str(dates_list[i].strftime('%Y-%m-%d %H:%M'))
    ))

print(f"[ANIMATION DEBUG] Created {len(frames)} frames")
```

**Frame Structure:**
- Each frame is a snapshot at specific date
- Contains full copy of all traces with updated positions
- Only position coordinates change between frames
- Frame name = date stamp for slider display

#### Phase 7: Dynamic Axis Scaling (lines 5826-5858)

```python
if is_exoplanet_mode and exo_objects:
    # Use exoplanet-specific axis range calculation
    from exoplanet_orbits import calculate_exoplanet_axis_range
    from exoplanet_systems import get_system
    
    # Collect all selected exoplanet data
    all_exo_planets = []
    for obj in exo_objects:
        system_id = obj.get('system_id')
        if system_id:
            system = get_system(system_id)
            if system:
                planet_id = obj.get('id')
                for catalog_planet in system['planets']:
                    if catalog_planet.get('planet_id') == planet_id:
                        all_exo_planets.append(catalog_planet)
                        break
    
    if all_exo_planets:
        axis_range = calculate_exoplanet_axis_range(all_exo_planets)
        # Convert to list for Plotly: [min, max]
        axis_range = [-axis_range, axis_range]
        print(f"[EXOPLANET ANIMATION] Using exoplanet axis range: ±{axis_range[1]:.4f} AU")
    else:
        # Fallback to standard scaling
        axis_range = get_animation_axis_range(
            scale_var, custom_scale_entry, objects, planetary_params, 
            parent_planets, center_object_name
        )
else:
    # Use standard solar system scaling
    axis_range = get_animation_axis_range(
        scale_var, custom_scale_entry, objects, planetary_params, 
        parent_planets, center_object_name
    )
```

**Scaling Logic:**
- Exoplanet systems: Use `calculate_exoplanet_axis_range()` (finds max orbital radius, adds 20% margin)
- Solar system: Use standard scaling based on outermost selected object
- Typical exoplanet ranges: 0.01-5 AU
- Typical solar system ranges: 5-40 AU

---

## Keplerian Orbit Calculations

### Function: `calculate_planet_position()`

**Location:** `exoplanet_orbits.py`, line 170  
**Purpose:** Calculate 3D position of exoplanet at specific date using Keplerian orbital mechanics

**Function Signature:**
```python
def calculate_planet_position(a, e, i_deg, omega_deg, Omega_deg,
                             period_days, epoch, date):
    """
    Parameters:
        a: float - Semi-major axis (AU)
        e: float - Eccentricity (0-1)
        i_deg: float - Inclination (degrees)
        omega_deg: float - Argument of periapsis (degrees)
        Omega_deg: float - Longitude of ascending node (degrees)
        period_days: float - Orbital period (days)
        epoch: datetime - Reference epoch (J2000)
        date: datetime - Date for position calculation
        
    Returns:
        x, y, z: floats - 3D position in Sky Plane coordinates (AU)
    """
```

### Algorithm Steps

**Step 1: Time Since Epoch**
```python
# Convert dates to UTC if needed
if epoch.tzinfo is None:
    epoch = epoch.replace(tzinfo=timezone.utc)
if date.tzinfo is None:
    date = date.replace(tzinfo=timezone.utc)

# Calculate time difference
dt_seconds = (date - epoch).total_seconds()
dt_days = dt_seconds / 86400.0
```

**Step 2: Mean Motion & Mean Anomaly**
```python
# Mean motion (radians per day)
n = 2 * np.pi / period_days

# Mean anomaly at given date
M = n * dt_days
M = M % (2 * np.pi)  # Wrap to [0, 2π]
```

**Step 3: Solve Kepler's Equation (Numerical)**
```python
def solve_kepler_equation(M, e, tolerance=1e-6, max_iterations=50):
    """
    Solve Kepler's equation: M = E - e*sin(E)
    Using Newton-Raphson iteration
    """
    E = M  # Initial guess
    for i in range(max_iterations):
        f = E - e * np.sin(E) - M
        f_prime = 1 - e * np.cos(E)
        E_new = E - f / f_prime
        
        if abs(E_new - E) < tolerance:
            return E_new
        E = E_new
    
    return E  # Return best estimate

E = solve_kepler_equation(M, e)
```

**Step 4: True Anomaly**
```python
def calculate_true_anomaly(E, e):
    """
    Convert eccentric anomaly to true anomaly
    """
    nu = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))
    return nu

nu = calculate_true_anomaly(E, e)
```

**Step 5: Orbital Radius**
```python
# Distance from focus (host star)
r = a * (1 - e**2) / (1 + e * np.cos(nu))
```

**Step 6: Position in Orbital Plane**
```python
# 2D coordinates in orbital plane
x_orb = r * np.cos(nu)
y_orb = r * np.sin(nu)
z_orb = 0.0
```

**Step 7: 3D Rotations (Orbital Plane → Sky Plane)**
```python
# Convert angles to radians
i_rad = np.radians(i_deg)
omega_rad = np.radians(omega_deg)
Omega_rad = np.radians(Omega_deg)

# Rotation by ω (argument of periapsis)
x1 = x_orb * np.cos(omega_rad) - y_orb * np.sin(omega_rad)
y1 = x_orb * np.sin(omega_rad) + y_orb * np.cos(omega_rad)
z1 = z_orb

# Rotation by i (inclination)
x2 = x1
y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)

# Rotation by Ω (longitude of ascending node)
x = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
y = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
z = z2

return x, y, z
```

### Coordinate System: Sky Plane

The sky plane coordinate system is observer-centric:

- **X-axis:** Points toward observer (negative = away from Earth)
- **Y-axis:** East direction in sky
- **Z-axis:** North celestial pole direction

**Why Sky Plane?**
- Natural for transiting exoplanets (often viewed edge-on)
- Matches observational data conventions
- Independent from Solar System ecliptic
- Simplifies interpretation of inclination angles

**Inclination Examples:**
- `i = 0°`: Face-on orbit (see full circular path)
- `i = 45°`: Tilted orbit
- `i = 90°`: Edge-on orbit (transits visible)

---

## Binary Star Orbital Mechanics

### Function: `calculate_binary_star_orbits()`

**Location:** `exoplanet_orbits.py`, line 239  
**Purpose:** Calculate orbital parameters for both stars around barycenter

```python
def calculate_binary_star_orbits(star_A_mass, star_B_mass, 
                                 binary_separation, binary_period,
                                 binary_eccentricity=0.0):
    """
    Both stars orbit their common center of mass (barycenter).
    For visualization, barycenter is at origin (0, 0, 0).
    
    Parameters:
        star_A_mass: float - Primary star mass (solar masses)
        star_B_mass: float - Secondary star mass (solar masses)
        binary_separation: float - Semi-major axis of binary orbit (AU)
        binary_period: float - Binary orbital period (days)
        binary_eccentricity: float - Binary orbit eccentricity (default 0)
        
    Returns:
        dict: Orbital parameters for both stars
            {
                'star_A': {'a': ..., 'e': ..., 'period': ..., 'phase': 0.0},
                'star_B': {'a': ..., 'e': ..., 'period': ..., 'phase': 180.0}
            }
    """
    total_mass = star_A_mass + star_B_mass
    
    # Semi-major axes from barycenter (using center of mass formula)
    # Star A (more massive, closer to barycenter)
    a_A = binary_separation * (star_B_mass / total_mass)
    
    # Star B (less massive, farther from barycenter)
    a_B = binary_separation * (star_A_mass / total_mass)
    
    return {
        'star_A': {
            'a': a_A,
            'e': binary_eccentricity,
            'period': binary_period,
            'phase': 0.0  # Arbitrary starting phase
        },
        'star_B': {
            'a': a_B,
            'e': binary_eccentricity,
            'period': binary_period,
            'phase': 180.0  # Opposite side of orbit
        }
    }
```

### Physical Principle

**Center of Mass Formula:**
```
m_A * r_A = m_B * r_B
r_A + r_B = separation

Solving:
r_A = separation * (m_B / (m_A + m_B))
r_B = separation * (m_A / (m_A + m_B))
```

**Example - TOI-1338:**
```python
star_A_mass = 1.1  # M☉
star_B_mass = 0.3  # M☉
binary_separation = 0.598  # AU
binary_period = 14.6  # days

total_mass = 1.1 + 0.3 = 1.4 M☉

# Star A orbit (more massive, smaller orbit)
a_A = 0.598 * (0.3 / 1.4) = 0.128 AU

# Star B orbit (less massive, larger orbit)
a_B = 0.598 * (1.1 / 1.4) = 0.470 AU

# Verify: 0.128 + 0.470 = 0.598 ✓
```

### Function: `calculate_binary_star_position()`

**Location:** `exoplanet_orbits.py`, line 286  
**Purpose:** Calculate position of one star at specific date

```python
def calculate_binary_star_position(star_params, date, epoch, 
                                  i_deg=0.0, Omega_deg=0.0):
    """
    Calculate position of one star in binary system at given date
    
    Parameters:
        star_params: dict - From calculate_binary_star_orbits()
            {'a': ..., 'e': ..., 'period': ..., 'phase': ...}
        date: datetime - Date for calculation
        epoch: datetime - Reference epoch
        i_deg: float - Inclination of binary orbit (degrees)
        Omega_deg: float - Orientation of binary orbit (degrees)
        
    Returns:
        x, y, z: floats - Star position (AU)
    """
    a = star_params['a']
    e = star_params['e']
    period = star_params['period']
    phase_offset = np.radians(star_params['phase'])
    
    # For simplicity, assume omega = 0 for binary orbit
    omega_deg = 0.0
    
    # Calculate position using planet position function
    x, y, z = calculate_planet_position(
        a, e, i_deg, omega_deg, Omega_deg,
        period, epoch, date
    )
    
    # Apply phase offset by rotating around origin
    # This ensures stars stay on opposite sides
    angle = phase_offset
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    
    return x_rot, y_rot, z
```

**Phase Offset Logic:**
- Star A: `phase = 0°` (starting position)
- Star B: `phase = 180°` (opposite side)
- Rotation by phase angle keeps stars opposite each other at all times

---

## Data Structures

### exoplanet_positions_over_time

**Type:** `dict[str, list[dict]]`  
**Purpose:** Store pre-calculated positions for all animation frames

**Structure:**
```python
exoplanet_positions_over_time = {
    'TRAPPIST-1 b': [
        {'x': 0.0111, 'y': 0.0003, 'z': 0.0001, 'date': datetime(2025, 1, 1)},
        {'x': 0.0109, 'y': 0.0015, 'z': 0.0002, 'date': datetime(2025, 1, 2)},
        {'x': 0.0105, 'y': 0.0025, 'z': 0.0003, 'date': datetime(2025, 1, 3)},
        # ... N frames total
    ],
    'TRAPPIST-1 e': [
        {'x': 0.0287, 'y': 0.0011, 'z': 0.0003, 'date': datetime(2025, 1, 1)},
        {'x': 0.0285, 'y': 0.0022, 'z': 0.0005, 'date': datetime(2025, 1, 2)},
        # ... N frames total
    ],
    # ... all selected exoplanets
}
```

**Properties:**
- Keys: Object names (strings)
- Values: Lists of position dictionaries (one per frame)
- Each position: `{'x': float, 'y': float, 'z': float, 'date': datetime}`
- Length of each list = number of animation frames
- Created in Phase 3 (lines 5150-5205)
- Used in Phase 6 (frame generation)

**Memory Usage:**
```
One position entry ≈ 64 bytes (4 floats, 1 datetime)
100 frames × 7 planets × 64 bytes = 44.8 KB
```

### binary_star_positions_over_time

**Type:** `dict[str, list[dict]]`  
**Purpose:** Store binary star positions for animation

**Structure:** (same format as exoplanet_positions_over_time)
```python
binary_star_positions_over_time = {
    'TOI-1338 A': [
        {'x': 0.128, 'y': 0.000, 'z': 0.000, 'date': datetime(2025, 1, 1)},
        {'x': 0.125, 'y': 0.030, 'z': 0.002, 'date': datetime(2025, 1, 2)},
        # ... N frames
    ],
    'TOI-1338 B': [
        {'x': -0.470, 'y': 0.000, 'z': 0.000, 'date': datetime(2025, 1, 1)},
        {'x': -0.460, 'y': -0.110, 'z': -0.008, 'date': datetime(2025, 1, 2)},
        # ... N frames
    ]
}
```

**Created:** Phase 4 (lines 5207-5266)

### trace_indices

**Type:** `dict[str, int]`  
**Purpose:** Map object names to Plotly trace indices for efficient frame updates

**Structure:**
```python
trace_indices = {
    'TRAPPIST-1 b': 5,    # trace 5 in fig.data
    'TRAPPIST-1 e': 6,    # trace 6 in fig.data
    'TRAPPIST-1 g': 7,    # trace 7 in fig.data
    'TOI-1338 A': 8,      # trace 8 in fig.data
    'TOI-1338 B': 9,      # trace 9 in fig.data
    # ...
}
```

**Usage in Frame Generation:**
```python
# Get trace index for object
trace_idx = trace_indices['TRAPPIST-1 b']

# Update position in frame
frame_data[trace_idx].x = [new_x]
frame_data[trace_idx].y = [new_y]
frame_data[trace_idx].z = [new_z]
```

**Why This Matters:**
- Direct index lookup (O(1) access)
- No searching through fig.data list
- Essential for performance with many frames
- Created in Phase 5 (lines 5506-5666)

---

## Frame Generation Process

### Overview

Each animation frame is a complete snapshot of the visualization at a specific date. The frame contains all traces (orbit paths, markers, annotations) with updated positions for animated objects.

### Frame Structure

```python
frame = go.Frame(
    data=[
        trace_0,  # Static orbit paths (unchanged)
        trace_1,  # Static orbit paths (unchanged)
        trace_2,  # Exoplanet marker (UPDATED position)
        trace_3,  # Exoplanet marker (UPDATED position)
        trace_4,  # Binary star marker (UPDATED position)
        # ... all traces
    ],
    name='2025-01-15 12:00'  # Date stamp for slider
)
```

### Static vs. Dynamic Elements

**Static (same in all frames):**
- Orbital path ellipses
- Host star/barycenter position (at origin)
- Coordinate system annotations
- Legend
- Axis ranges

**Dynamic (updated per frame):**
- Planet marker positions (x, y, z coordinates)
- Binary star positions (if binary system)
- Hover text (could include date-specific info)
- Visibility flags (for objects appearing/disappearing)

### Frame Creation Loop

```python
frames = []  # List to store all frames

for i in range(N):  # N = number of frames
    # Start with copy of all base traces
    frame_data = list(fig.data)
    
    # Get current date for this frame
    current_date = dates_list[i]
    
    # Update each animated object's position
    for obj_name in exoplanet_positions_over_time:
        if obj_name in trace_indices:
            trace_idx = trace_indices[obj_name]
            positions = exoplanet_positions_over_time[obj_name]
            
            if i < len(positions):
                pos = positions[i]
                # Update x, y, z coordinates
                frame_data[trace_idx].x = [pos['x']]
                frame_data[trace_idx].y = [pos['y']]
                frame_data[trace_idx].z = [pos['z']]
                frame_data[trace_idx].visible = True
            else:
                # Hide if no position for this frame
                frame_data[trace_idx].visible = False
    
    # Similar updates for binary stars...
    
    # Create frame object
    frame = go.Frame(
        data=frame_data,
        name=str(current_date.strftime('%Y-%m-%d %H:%M'))
    )
    frames.append(frame)
```

### Memory Efficiency

**Strategy:** Shallow copy for static traces, direct reference for dynamic traces

```python
frame_data = list(fig.data)  # Shallow copy - references, not copies
```

**Why This Works:**
- Static traces (orbit paths) don't change → reference original
- Dynamic traces (markers) DO change → modify in-place
- Avoids deep copying large orbit path arrays
- Only marker coordinates are modified

**Memory Savings:**
```
Deep copy approach: 100 frames × 50 traces × 100 points × 8 bytes = 4 MB
Shallow copy approach: 100 frames × 10 markers × 1 point × 8 bytes = 8 KB
Savings: ~99.8%
```

---

## Dynamic Axis Scaling

### Function: `calculate_exoplanet_axis_range()`

**Location:** `exoplanet_orbits.py`  
**Purpose:** Determine optimal viewing range for compact exoplanet systems

**Algorithm:**
```python
def calculate_exoplanet_axis_range(exoplanet_objects):
    """
    Find maximum orbital radius among selected planets and add margin
    
    Parameters:
        exoplanet_objects: list of planet dicts
        
    Returns:
        float: Axis range in AU (use as ±range)
    """
    max_radius = 0
    
    # Find largest orbital distance
    for planet in exoplanet_objects:
        a = planet['semi_major_axis_au']
        e = planet['eccentricity']
        
        # Maximum distance = aphelion
        aphelion = a * (1 + e)
        
        max_radius = max(max_radius, aphelion)
    
    # Add 20% margin for visibility
    axis_range = max_radius * 1.2
    
    # Set minimum range for very compact systems
    if axis_range < 0.01:
        axis_range = 0.01
    
    return axis_range
```

### Typical Ranges by System

| System | Outermost Planet | Aphelion | Axis Range | Scale Factor vs Solar System |
|--------|-----------------|----------|------------|------------------------------|
| Proxima Centauri | Prox b | 0.050 AU | ±0.06 AU | 1/667 |
| TRAPPIST-1 | TRAPPIST-1 h | 0.062 AU | ±0.08 AU | 1/500 |
| TOI-1338 | TOI-1338 c | 0.76 AU | ±0.91 AU | 1/44 |
| Solar System (for comparison) | Neptune | 30.4 AU | ±40 AU | 1 |

### Why Dynamic Scaling Matters

**Without Dynamic Scaling:**
```
Solar System range: ±40 AU
TRAPPIST-1 system: 0.062 AU maximum distance
Visual size: 0.062 / 40 = 0.16% of plot area
Result: Planets appear as tiny dots in vast empty space
```

**With Dynamic Scaling:**
```
TRAPPIST-1 range: ±0.08 AU (auto-calculated)
TRAPPIST-1 system: 0.062 AU maximum distance
Visual size: 0.062 / 0.08 = 78% of plot area
Result: System fills visualization, planets clearly visible
```

### Implementation in Animation

```python
if is_exoplanet_mode and exo_objects:
    # Gather planet data
    all_exo_planets = []
    for obj in exo_objects:
        system_id = obj.get('system_id')
        if system_id:
            system = get_system(system_id)
            if system:
                planet_id = obj.get('id')
                for catalog_planet in system['planets']:
                    if catalog_planet.get('planet_id') == planet_id:
                        all_exo_planets.append(catalog_planet)
                        break
    
    # Calculate and apply range
    if all_exo_planets:
        axis_range = calculate_exoplanet_axis_range(all_exo_planets)
        axis_range = [-axis_range, axis_range]  # ±range for Plotly
        
        print(f"[EXOPLANET ANIMATION] Using exoplanet axis range: ±{axis_range[1]:.4f} AU")
        
        # Apply to all three axes
        fig.update_layout(
            scene=dict(
                xaxis=dict(range=axis_range),
                yaxis=dict(range=axis_range),
                zaxis=dict(range=axis_range),
                aspectmode='cube'  # Maintain equal scaling
            )
        )
```

---

## Performance & Optimization

### Position Pre-Calculation Strategy

**Approach:** Calculate all positions BEFORE frame generation

**Advantages:**
1. Single calculation per planet per frame (no redundant calculations)
2. Predictable memory usage (fixed size for position lists)
3. Fast frame generation (just copy pre-calculated values)
4. Easy debugging (inspect position lists independently)

**Timing Breakdown (100 frames, 7 planets):**
```
Phase 3 - Position calculation:
  7 planets × 100 frames × 0.1 ms = 70 ms

Phase 6 - Frame generation:
  100 frames × (10 trace updates) × 0.5 ms = 500 ms

Total animation creation time: ~600 ms
```

### Keplerian Calculation Performance

**Why Keplerian Orbits Are Fast:**

1. **Analytical Solution** - No numerical integration needed
2. **Independent Frames** - Each position calculated independently (parallelizable)
3. **Simple Math** - Basic trig, no complex physics simulations
4. **No API Calls** - All calculations local (vs JPL Horizons queries)

**Comparison: Keplerian vs JPL Horizons**

| Method | Time per Position | 700 Positions |
|--------|------------------|---------------|
| Keplerian (local) | 0.1 ms | 70 ms |
| JPL Horizons (API) | 100-500 ms | 70-350 seconds |
| **Speedup** | **1000-5000×** | **1000-5000×** |

### JPL Horizons Skip for Exoplanets

**Critical Optimization:** Skip JPL queries entirely for exoplanet mode

```python
# Skip orbit data updates for exoplanet systems
if not is_exoplanet_mode:
    # Call the incremental update for selected objects only
    updated, current, total, time_saved = orbit_data_manager.update_orbit_paths_incrementally(
        object_list=selected_objects,
        center_object_name=center_object_name,
        days_ahead=max(days_ahead, 365),
        planetary_params=planetary_params,
        parent_planets=parent_planets,
        root_widget=root
    )
else:
    # Exoplanet mode - skip JPL data update
    output_label.config(text="Exoplanet mode: Using Keplerian orbits. Creating animation...")
    root.update_idletasks()
```

**Why:**
- Exoplanets are NOT in JPL Horizons database
- Attempting to query would cause errors
- Wastes time on failed API calls
- Keplerian orbits are more accurate for exoplanets anyway

### Memory-Efficient Frame Structure

**Pattern:** Shallow copy base traces, modify only what changes

```python
# Shallow copy - creates references to existing traces
frame_data = list(fig.data)

# Direct modification of specific traces
frame_data[trace_idx].x = [new_x]  # Only updates this one value
frame_data[trace_idx].y = [new_y]
frame_data[trace_idx].z = [new_z]
```

**Memory Impact:**
```
100 frames × (5 exoplanets + 2 binary stars) × 3 coordinates × 8 bytes
= 100 × 7 × 3 × 8 = 16.8 KB

(vs. deep copying all traces: ~4-10 MB)
```

### Optimization Results

**Typical Animation Creation Times:**

| Frames | Planets | Binary Stars | Time (seconds) |
|--------|---------|--------------|----------------|
| 30 | 3 | 0 | 0.3 |
| 50 | 5 | 0 | 0.5 |
| 100 | 7 | 0 | 1.0 |
| 100 | 7 | 2 | 1.5 |
| 200 | 7 | 2 | 2.5 |
| 500 | 7 | 2 | 5.0 |

**Bottleneck Analysis:**
- Position calculation: 10-15% of time
- Frame generation: 70-80% of time (Plotly overhead)
- Figure rendering: 5-10% of time

---

## Troubleshooting & Debugging

### Console Debug Messages

The animation system provides detailed logging:

```
[EXOPLANET ANIMATION MODE] Detected 5 exoplanets and 1 host stars
[ANIMATION DEBUG] ====== ANIMATION SETTINGS ======
Days to Plot: 90
Number of Frames: 90
Animation Step: daily
==================================================
[ANIMATION DEBUG] Created 90 animation dates
[ANIMATION DEBUG] From 2025-01-01 00:00:00+00:00 to 2025-03-31 00:00:00+00:00
[EXOPLANET ANIMATION] Processing TRAPPIST-1
[EXOPLANET ANIMATION] Generating positions for TRAPPIST-1 b (period: 1.51 days)
[EXOPLANET ANIMATION] Generated 90 positions for TRAPPIST-1 b
[EXOPLANET ANIMATION] Generating positions for TRAPPIST-1 e (period: 6.10 days)
[EXOPLANET ANIMATION] Generated 90 positions for TRAPPIST-1 e
[BINARY ANIMATION] Detected binary system: TOI-1338
[BINARY ANIMATION] Generated 90 positions for TOI-1338 A
[BINARY ANIMATION] Generated 90 positions for TOI-1338 B
[EXOPLANET ANIMATION] Added 5 exoplanet traces
[BINARY ANIMATION] Added 2 binary star traces
[ANIMATION DEBUG] Created 7 initial traces
[ANIMATION DEBUG] Creating frames...
[ANIMATION DEBUG] Creating frame 1/90 for date 2025-01-01 00:00:00+00:00
[ANIMATION DEBUG] Creating frame 2/90 for date 2025-01-02 00:00:00+00:00
...
[ANIMATION DEBUG] Created 90 frames
[EXOPLANET ANIMATION] Using exoplanet axis range: ±0.0800 AU
```

### Interpreting Debug Messages

**Look For:**

1. **`[EXOPLANET ANIMATION MODE]`** - Confirms mode detection
   - Should appear if ANY exoplanet objects selected
   - If missing, check object_type in objects list

2. **`Generated N positions for ...`** - Confirms position calculation
   - N should equal number of frames
   - If missing, planet data not found in catalog

3. **`Added N exoplanet traces`** - Confirms trace creation
   - Should match number of selected exoplanets
   - If 0, check if objects in trace_indices

4. **`axis range: ±X AU`** - Confirms dynamic scaling
   - Should be appropriate for system scale
   - Proxima: ~0.06 AU, TRAPPIST-1: ~0.08 AU, TOI-1338: ~1.0 AU

5. **`Created N frames`** - Confirms successful frame generation
   - Should match "Number of Frames" setting
   - If 0, check for errors in frame loop

### Common Issues & Solutions

#### Issue: "Animation plays too fast"

**Symptoms:**
- Frames flash by rapidly
- Difficult to see orbital motion
- Animation completes in seconds

**Cause:** Too few frames for time range

**Solution:**
```
Increase "Number of Frames" to match time scale

Examples:
- 90 days → 90 frames (1 day/frame)
- 180 days → 180 frames (1 day/frame)
- 1 year → 365 frames (1 day/frame)
```

#### Issue: "Exoplanets don't move"

**Symptoms:**
- Static visualization even during animation
- All frames look identical
- No position changes visible

**Cause:** Object selection or date range problem

**Check:**
1. Console for `[EXOPLANET ANIMATION MODE]` message
   - If missing: exoplanet object_type not detected
2. "Days to Plot" setting
   - Must be > 0
   - Should span multiple orbital periods
3. Exoplanet checkbox selection
   - Verify boxes are actually checked
   - Check `obj['var'].get() == 1`

**Debug:**
```python
# In console, check:
print(f"exo_objects: {[obj['name'] for obj in exo_objects]}")
print(f"days_to_plot: {settings['days_to_plot']}")
print(f"dates_list length: {len(dates_list)}")
```

#### Issue: "Binary stars don't appear"

**Symptoms:**
- Only barycenter visible
- No stellar orbit animation
- Missing star markers

**Cause:** Incomplete object selection

**Solution:**
```
Select ALL THREE objects:
☑ TOI-1338 A (primary star)
☑ TOI-1338 B (secondary star)
☑ TOI-1338 A/B (Barycenter)

Without all three, binary animation won't work properly.
```

**Technical Reason:**
- Barycenter establishes coordinate origin
- Star A/B objects needed for binary_star_positions_over_time
- Missing any component breaks animation chain

#### Issue: "Planets appear as tiny dots"

**Symptoms:**
- Very small visual scale
- System appears compressed
- Hard to distinguish individual planets

**Cause:** Axis range too large (wrong scaling)

**Check:**
1. Console for axis range message
   - Should show appropriate AU value for system
2. Mixed solar system + exoplanet selection
   - Can cause scaling conflicts
   
**Solution:**
```
Select ONLY exoplanet objects (no solar system)

For TRAPPIST-1:
☑ TRAPPIST-1 (star)
☑ TRAPPIST-1 b, e, f, g (planets)
☐ Earth, Mars, etc. (uncheck solar system)

System should auto-detect and use ±0.08 AU range.
```

#### Issue: "Wrong coordinate system displayed"

**Symptoms:**
- J2000 Ecliptic shown instead of Sky Plane
- Coordinate labels don't match exoplanet geometry
- Inclination angles seem inverted

**Cause:** Mode detection failure

**Check:**
1. Console for mode detection message
2. Object type assignments in objects list

**Solution:**
```python
# Verify object has correct object_type
obj = {
    'name': 'TRAPPIST-1 b',
    'object_type': 'exoplanet',  # Must be 'exoplanet'
    'id_type': 'exoplanet',
    'system_id': 'trappist1'
}

# Not 'planet', 'orbital', or other types
```

#### Issue: "Animation taking too long to create"

**Symptoms:**
- Several minutes to generate animation
- Browser doesn't open
- App appears frozen

**Cause:** Too many frames or complex system

**Solution:**
```
Reduce computational load:

1. Decrease frame count
   - Start with 30-50 frames for testing
   - Increase gradually if needed

2. Select fewer planets
   - Try 2-3 planets first
   - Add more after verifying works

3. Check for infinite loops
   - Look for ERROR messages in console
   - Verify dates_list has finite length
```

**Normal Timings:**
- 30 frames, 3 planets: <1 second
- 100 frames, 7 planets: 1-2 seconds
- 500 frames, 7 planets: 5-10 seconds

**If longer:** Check for errors or infinite loops

---

## Code Integration Examples

### Complete Workflow: Adding a New Exoplanet System

This example shows how to add a complete new exoplanet system with full animation support.

#### Step 1: Define System in `exoplanet_systems.py`

```python
from datetime import datetime, timezone

# Add to EXOPLANET_SYSTEMS list
EXOPLANET_SYSTEMS.append({
    'system_name': 'Kepler-186',
    'system_id': 'kepler186',
    'discovery_year': 2014,
    'distance_pc': 151.0,  # parsecs
    'distance_ly': 493.0,  # light-years
    'constellation': 'Cygnus',
    'notable_features': [
        'First Earth-sized planet in habitable zone',
        '5 planets total',
        'M-dwarf host star'
    ],
    
    'host_star': {
        'name': 'Kepler-186',
        'star_id': 'kepler186_star',
        'is_binary': False,
        
        # Position (J2000.0)
        'ra_deg': 287.0958,  # Right ascension
        'dec_deg': 43.9397,  # Declination
        'distance_pc': 151.0,
        
        # Proper motion (mas/year)
        'pmra_mas_yr': 5.2,
        'pmdec_mas_yr': -12.1,
        
        # Stellar properties
        'spectral_type': 'M1V',
        'mass_solar': 0.478,
        'radius_solar': 0.472,
        'teff_k': 3788,
        'luminosity_solar': 0.032,
        
        # Habitable zone
        'habitable_zone_inner_au': 0.23,
        'habitable_zone_outer_au': 0.42,
        
        # Epoch for orbital calculations
        'epoch': datetime(2000, 1, 1, 12, 0, tzinfo=timezone.utc)
    },
    
    'planets': [
        {
            'name': 'Kepler-186 f',
            'planet_id': 'kepler186f',
            
            # Orbital elements
            'period_days': 129.9441,
            'semi_major_axis_au': 0.432,
            'eccentricity': 0.0,  # Unknown, assume circular
            'inclination_deg': 89.9,  # Edge-on (transiting)
            'arg_periapsis_deg': 0.0,
            'long_ascending_node_deg': 0.0,
            'epoch': datetime(2000, 1, 1, 12, 0, tzinfo=timezone.utc),
            
            # Physical properties
            'mass_earth': 1.71,  # Estimated
            'radius_earth': 1.17,
            'density_gcc': None,  # Unknown
            'temperature_k': 188,  # Equilibrium temp
            
            # Discovery metadata
            'discovery_year': 2014,
            'discovery_method': 'Transit',
            'discovery_facility': 'Kepler Space Telescope',
            'discoverer': 'Quintana et al.',
            
            # Status flags
            'in_habitable_zone': True,
            'is_transiting': True
        },
        # Add more planets (b, c, d, e) similarly...
    ]
})
```

#### Step 2: Add GUI Objects in `palomas_orrery.py`

```python
# Create Tkinter variable
kepler186f_var = tk.IntVar()

# Add to objects list (around line 3100+)
objects.append({
    'name': 'Kepler-186 f',
    'id': 'kepler186f',
    'var': kepler186f_var,
    'color': 'green',  # Habitable zone planet
    'symbol': 'circle',
    'object_type': 'exoplanet',  # CRITICAL for animation
    'id_type': 'exoplanet',
    'system_id': 'kepler186',  # Links to system catalog
    'semi_major_axis_au': 0.432,
    'period_days': 129.9441,
    'in_habitable_zone': True,
    'mission_info': '☀ IN HABITABLE ZONE ☀ First Earth-sized planet in HZ!',
    'mission_url': 'https://exoplanets.nasa.gov/exoplanet-catalog/1886/kepler-186-f/'
})

# Add host star
kepler186_star_var = tk.IntVar()
objects.append({
    'name': 'Kepler-186',
    'id': 'kepler186_star',
    'var': kepler186_star_var,
    'color': 'rgba(0,0,0,0)',  # Transparent (no redundant marker)
    'symbol': 'circle',
    'object_type': 'exo_host_star',  # CRITICAL
    'id_type': 'host_star',
    'system_id': 'kepler186',
    'mission_info': 'M1V red dwarf, 493 light-years away',
    'mission_url': 'https://exoplanets.nasa.gov/eyes-on-exoplanets/#/planet/Kepler-186_f/'
})
```

#### Step 3: Add to Center Dropdown

```python
# In center object dropdown section (around line 2800+)
center_objects = [
    'Sun',
    'Mercury',
    # ... other solar system objects
    'TRAPPIST-1',
    'TOI-1338 A/B (Barycenter)',
    'Proxima Centauri',
    'Kepler-186'  # ADD THIS
]
```

#### Step 4: Animation System Handles It Automatically!

No additional code needed in `animate_objects()` - the system:

1. **Detects exoplanet mode** (Phase 1)
   ```python
   # Automatically finds 'Kepler-186 f' with object_type='exoplanet'
   exo_objects = [obj for obj in objects 
                 if obj['var'].get() == 1 and obj.get('object_type') == 'exoplanet']
   ```

2. **Fetches system data** (Phase 3)
   ```python
   system = get_system('kepler186')  # Uses system_id
   ```

3. **Calculates positions** (Phase 3)
   ```python
   for date in dates_list:
       x, y, z = calculate_planet_position(
           a=0.432,  # From planet_data
           e=0.0,
           i_deg=89.9,
           omega_deg=0.0,
           Omega_deg=0.0,
           period_days=129.9441,
           epoch=system['host_star']['epoch'],
           date=date
       )
   ```

4. **Creates traces** (Phase 5)
   ```python
   # Automatically creates Scatter3d trace with initial position
   trace = go.Scatter3d(...)
   fig.add_trace(trace)
   trace_indices['Kepler-186 f'] = len(fig.data) - 1
   ```

5. **Generates frames** (Phase 6)
   ```python
   # Updates position in each frame
   for i in range(N):
       pos = exoplanet_positions_over_time['Kepler-186 f'][i]
       frame_data[trace_idx].x = [pos['x']]
       frame_data[trace_idx].y = [pos['y']]
       frame_data[trace_idx].z = [pos['z']]
   ```

6. **Sets axis range** (Phase 7)
   ```python
   # Automatically calculates appropriate range
   axis_range = calculate_exoplanet_axis_range([planet_data])
   # Returns ~±0.5 AU for Kepler-186 f
   ```

### Result

User can now:
- ☑ Check "Kepler-186 f" box
- Select "Kepler-186" as center
- Click "Animate Monthly"
- Watch planet complete ~3 orbits over 1 year
- System automatically uses Sky Plane coordinates
- Axis range auto-scales to ±0.5 AU

**No animation-specific code needed!** The unified architecture handles everything.

---

## Summary

### Key Takeaways

1. **Unified Architecture**
   - Single `animate_objects()` function handles both solar system and exoplanets
   - Mode detection automatically switches between JPL and Keplerian
   - No separate animation pipelines needed

2. **Keplerian Position Calculation**
   - Analytical solution (no numerical integration)
   - Fast: ~0.1 ms per position
   - Accurate for exoplanet orbital mechanics
   - 1000-5000× faster than JPL Horizons

3. **Pre-calculation Strategy**
   - All positions computed BEFORE frame generation
   - Stored in lightweight dictionaries
   - Enables fast, memory-efficient frame creation

4. **Dynamic Scaling**
   - Axis ranges adapt to compact exoplanet systems
   - Prevents "lost in space" visualization
   - Typical ranges: 0.01-5 AU (vs 40 AU for solar system)

5. **Binary Star Support**
   - Both stars orbit common barycenter
   - Mass-dependent semi-major axes
   - Phase offset (180°) keeps stars opposite
   - Reuses planet position calculation code

6. **Performance Optimization**
   - Typical animation: <1-2 seconds for 100 frames
   - Position calculation: 10-15% of time
   - Frame generation: 70-80% of time
   - Memory efficient: ~50 KB for typical animation

7. **Extensibility**
   - Adding new systems requires NO animation code changes
   - System automatically detects and handles exoplanets
   - Unified object selection and rendering pipeline
   - Easy integration of future features

### Animation Workflow Summary

```
User Action → Mode Detection → Position Pre-calculation → 
Trace Creation → Frame Generation → Dynamic Scaling → Display
   ↓              ↓                    ↓                   ↓
Select      Exoplanet/        Keplerian Calc       Plotly Frames
Objects     Solar System      (all dates)          (updated positions)
```

### Best Practices for Animation

1. **Start Small** - Test with 30-50 frames first
2. **Match Time Steps** - Daily for <30 day periods, monthly for <1 year
3. **Check Console** - Debug messages show exactly what's happening
4. **Single System** - Clearest visualization, avoid mixing systems
5. **Appropriate Frame Count** - More frames = smoother but slower

### Technical Achievement

The exoplanet animation system demonstrates:
- ✓ Seamless integration with existing codebase
- ✓ Minimal code duplication (reuses planet rendering)
- ✓ Automatic mode detection and switching
- ✓ High performance (sub-second animations)
- ✓ Extensible architecture (easy to add systems)
- ✓ Robust error handling and debugging
- ✓ User-friendly (no manual configuration needed)

---

*"From static snapshots to dynamic visualizations - watching exoplanets orbit their distant suns brings the universe to life."*

**End of Technical Documentation**
## Architecture & Design

### Design Philosophy: "Minimal Surgery, Maximal Reuse"

The exoplanet integration extends existing functionality without major architectural changes:

 **Reuses existing rendering pipeline** - `plot_objects()` and `animate_objects()`
 **System-specific coordinate frames** - each system independent
 **Shared object selection UI** - exoplanets alongside Solar System
 **Center dropdown expanded** - includes exoplanet host stars
 **System-scoped filtering** - automatic isolation by system_id

### Core Principle: Independent Coordinate Frames

Each exoplanet system has its **own local coordinate frame**, completely independent from the Solar System.

**Local Frame (per system):**
```
Origin: Host star barycenter at (0, 0, 0)
XY plane: Sky plane (perpendicular to Earth line of sight)
Z-axis: Toward Earth (positive = toward observer)
Units: Astronomical Units (AU)
```

**Why independent frames?**
- No artificial connection to Solar System ecliptic
- Natural orientation for transiting systems (edge-on by default)
- Simplifies calculations (no ecliptic coordinate transforms)
- Each system stands alone as separate visualization
- First Point of Aries is Earth/Solar-System-centric (not meaningful for exoplanets)

**User view:**
- Default: Face-on view (XY plane visible)
- User can rotate to any desired perspective
- Edge-on view shows transit geometry
- Z-axis always points toward Earth (line of sight)

### System Separation Logic

**How the code prevents mixing Solar System and exoplanet objects:**

```python
# 1. Every object has a system_id
solar_objects: system_id = 'solar' (default)
exoplanet_objects: system_id = 'trappist1', 'toi1338', 'proxima', etc.

# 2. Center object determines active system
center = user_dropdown.get() # e.g., "TRAPPIST-1"
center_system_id = get_system_id(center) # 'trappist1'

# 3. All loops filter by system
for obj in objects:
 if obj.get('system_id', 'solar') != center_system_id:
 continue # Skip objects from other systems
 # ... plot this object
```

**Result:**
- When center = "Sun" Only Solar System objects visible
- When center = "TRAPPIST-1" Only TRAPPIST-1 objects visible
- Clean separation, no mixing, no phantom objects!

### Binary Star Handling: Hybrid Approach

TOI-1338 binary system uses a **functional + visual hybrid**:

**Functional (for calculations):**
```python
# Barycenter at origin (0, 0, 0)
# Planets orbit the barycenter
# Simplifies planet orbital calculations
```

**Visual (for rendering):**
```python
# Both stars shown as orbiting objects
star_A_orbit = {'a': 0.019 AU, 'period': 14.6 d, 'phase': 0°}
star_B_orbit = {'a': 0.069 AU, 'period': 14.6 d, 'phase': 180°}
# Treat stars like "special planets"
```

**Advantages:**
- Planet calculations stay simple (circular barycenter reference)
- Users see binary dynamics (educational!)
- Reuses existing orbit rendering code
- Stars treated like orbital objects in the visualization
- Scales to triple stars if needed

### Time System: UTC Throughout

**Decision:** Use UTC consistently, no TDB conversion

```python
from datetime import datetime, timezone

date = datetime(2025, 10, 22, 12, 0, 0, tzinfo=timezone.utc)
```

**Rationale:**
- Exoplanet systems independent from Solar System
- Not mixing JPL Horizons (TDB) with exoplanet data (UTC)
- Proper motion precision doesn't require TDB
- Simplicity: UTC throughout

---

## Module Documentation

### Module Overview

| Module | Purpose | Lines | Size |
|--------|---------|-------|------|
| `exoplanet_systems.py` | Hardcoded catalog of systems | 688 | 24 KB |
| `exoplanet_orbits.py` | Keplerian mechanics & orbit calculation | 734 | 21 KB |
| `exoplanet_coordinates.py` | Stellar positioning & proper motion | 498 | 18 KB |

**Total:** 3 modules, 1,920 lines, 63 KB

### 1. exoplanet_systems.py

**Purpose:** Hardcoded catalog of exoplanet systems with complete metadata

**Data Structure:**
```python
SYSTEM = {
 'system_name': str, # "TRAPPIST-1"
 'system_id': str, # "trappist1" (unique key)
 'discovery_year': int, # 2017
 'distance_pc': float, # 12.43 parsecs
 'distance_ly': float, # 40.5 light-years
 'constellation': str, # "Aquarius"
 'notable_features': list, # ["7 planets", "3 in HZ", ...]

 'host_star': {
 'name': str, # "TRAPPIST-1"
 'star_id': str, # "trappist1_star"
 'is_binary': bool, # False (single) or True (binary)

 # Position (J2000.0)
 'ra': float, # Right ascension (degrees)
 'dec': float, # Declination (degrees)
 'distance_pc': float, # Distance (parsecs)

 # Proper motion
 'pmra': float, # RA proper motion (mas/year)
 'pmdec': float, # Dec proper motion (mas/year)

 # Stellar properties
 'spectral_type': str, # "M8V"
 'mass_solar': float, # 0.0898 M
 'radius_solar': float, # 0.1192 R
 'teff_k': float, # 2566 K
 'luminosity_solar': float, # 0.000525 L

 # Habitable zone
 'habitable_zone_inner_au': float,
 'habitable_zone_outer_au': float
 },

 'planets': [
 {
 'name': str, # "TRAPPIST-1 b"
 'planet_id': str, # "trappist1b"

 # Orbital elements
 'period_days': float, # 1.51087081
 'semi_major_axis_au': float, # 0.01154
 'eccentricity': float, # 0.00622
 'inclination_deg': float, # 89.728
 'omega_deg': float, # Argument of periapsis
 'Omega_deg': float, # Longitude of ascending node
 'epoch': datetime, # Reference epoch

 # Physical properties
 'mass_earth': float, # 1.374 M
 'radius_earth': float, # 1.116 R
 'density_gcc': float, # 3.92 g/cm³
 'temperature_k': float, # 400 K

 # Discovery metadata
 'discovery_year': int, # 2017
 'discovery_method': str, # "Transit"
 'discovery_facility': str, # "TRAPPIST telescope"

 # Status flags
 'in_habitable_zone': bool, # False
 'is_transiting': bool # True
 },
 # ... more planets
 ]
}
```

**Key Functions:**
```python
get_system(system_id: str) -> dict:
 """Retrieve system data by system_id"""

list_available_systems() -> list:
 """Get list of all system IDs"""

get_all_systems() -> list:
 """Get all system dictionaries"""
```

**Example Usage:**
```python
from exoplanet_systems import get_system

system = get_system('trappist1')
print(f"Star: {system['host_star']['name']}")
print(f"Planets: {len(system['planets'])}")
print(f"Distance: {system['distance_ly']} ly")

for planet in system['planets']:
 hz_status = "HZ" if planet['in_habitable_zone'] else ""
 print(f" {planet['name']}: {planet['period_days']:.2f} d {hz_status}")
```

---

### 2. exoplanet_orbits.py

**Purpose:** Keplerian orbital mechanics and 3D orbit calculation

**Key Functions:**

```python
calculate_keplerian_orbit(
 a, e, i, omega, Omega, period, epoch, date, num_points=100
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
 """
 Calculate complete 3D orbit path

 Parameters:
 a: Semi-major axis (AU)
 e: Eccentricity (0-1)
 i: Inclination (degrees)
 omega: Argument of periapsis (degrees)
 Omega: Longitude of ascending node (degrees)
 period: Orbital period (days)
 epoch: Reference epoch (datetime)
 date: Current date (datetime)
 num_points: Number of points in orbit path

 Returns:
 x, y, z: Arrays of positions (AU) in 3D space
 """

calculate_planet_position(
 a, e, i, omega, Omega, period, epoch, date
) -> tuple[float, float, float]:
 """
 Calculate planet position at specific date

 Returns:
 x, y, z: Position (AU) at given date
 """

plot_exoplanet_system(
 system_id, date, show_orbits=True, show_labels=True
) -> go.Figure:
 """
 Create standalone Plotly figure for an exoplanet system

 Parameters:
 system_id: System identifier ('trappist1', 'toi1338', 'proxima')
 date: Observation date
 show_orbits: Whether to show orbital paths
 show_labels: Whether to show object labels

 Returns:
 Plotly Figure object
 """

plot_binary_host_stars(
 fig, binary_star_data, date, show_orbits=True
) -> go.Figure:
 """
 Add binary star system to existing figure

 Handles:
 - Star A and Star B orbits around barycenter
 - Proper phasing (180° apart)
 - Synchronized periods

 Parameters:
 fig: Existing Plotly figure
 binary_star_data: Host star dictionary with binary info
 date: Current date
 show_orbits: Show stellar orbits

 Returns:
 Modified figure with binary stars added
 """
```

**Coordinate Transform Math:**

The code implements standard Keplerian orbit transformation from perifocal frame to 3D space:

```python
# 1. Solve Kepler's equation for eccentric anomaly E
M = mean_anomaly(t, period, epoch) # Mean anomaly
E = solve_kepler(M, e) # Eccentric anomaly (iterative)

# 2. Calculate true anomaly 1/2
1/2 = 2 * arctan(sqrt((1+e)/(1-e)) * tan(E/2))

# 3. Compute position in orbital plane (perifocal frame)
r = a * (1 - e*cos(E)) # Distance from focus
x_orb = r * cos(1/2)
y_orb = r * sin(1/2)

# 4. Rotate to 3D space using Euler angles
# Rz(Omega) · Rx(i) · Rz(omega)
x_3d, y_3d, z_3d = rotate(x_orb, y_orb, Omega, i, omega)
```

---

### 3. exoplanet_coordinates.py

**Purpose:** Stellar positioning and proper motion corrections

**Key Functions:**

```python
calculate_stellar_position(
 ra, dec, distance_pc, pmra, pmdec, epoch, target_date
) -> tuple[float, float, float]:
 """
 Calculate stellar position accounting for proper motion

 Parameters:
 ra, dec: Right ascension, declination (degrees, J2000)
 distance_pc: Distance (parsecs)
 pmra, pmdec: Proper motion (mas/year)
 epoch: Reference epoch
 target_date: Target date for calculation

 Returns:
 x, y, z: 3D Cartesian position (parsecs)
 """

apply_proper_motion(
 ra, dec, pmra, pmdec, epoch, target_date
) -> tuple[float, float]:
 """
 Apply proper motion correction to RA/Dec

 Returns:
 ra_new, dec_new: Updated coordinates (degrees)
 """

calculate_tangential_velocity(
 pmra, pmdec, distance_pc
) -> float:
 """
 Calculate tangential velocity from proper motion

 Returns:
 v_tan: Tangential velocity (km/s)
 """
```

**Proper Motion Math:**

```python
# Time elapsed since epoch
years_elapsed = (target_date - epoch).days / 365.25

# Apply proper motion
ra_new = ra + (pmra / 3600000) * years_elapsed / cos(dec)
dec_new = dec + (pmdec / 3600000) * years_elapsed

# Convert to 3D Cartesian
x = distance * cos(dec) * cos(ra)
y = distance * cos(dec) * sin(ra)
z = distance * sin(dec)
```

**When Proper Motion Matters:**

| Star | Distance | PM (mas/yr) | Years to 1" | Significant? |
|------|----------|-------------|-------------|--------------|
| Proxima | 1.3 pc | 3854 | 0.26 years | YES - moves fast! |
| TRAPPIST-1 | 12.4 pc | 1032 | 0.97 years | Noticeable over years |
| TOI-1338 | 396 pc | 5.6 | 179 years | Negligible for viz |

**Rule of thumb:** Proper motion significant if PM > 100 mas/yr OR distance < 10 pc

---

## Technical Reference

### Data Sources

**Primary Sources:**
- **NASA Exoplanet Archive:** https://exoplanetarchive.ipac.caltech.edu/
 - Comprehensive planetary parameters
 - Regular updates as new discoveries are made
 - TAP service for programmatic access (Phase 2)

- **SIMBAD Astronomical Database:** http://simbad.u-strasbg.fr/
 - Stellar positions (RA, Dec)
 - Proper motions
 - Spectral types
 - Distance measurements

- **Published Papers:**
 - Discovery announcements (Nature, Science, A&A, AJ)
 - Follow-up characterization studies
 - Mass/radius refinements

**Specific References:**

**TRAPPIST-1:**
- Gillon et al. 2017, Nature 542, 456-460 (discovery)
- Grimm et al. 2018, A&A 613, A68 (system architecture)
- Agol et al. 2021, Planet. Sci. J. 2, 1 (refined masses)

**TOI-1338:**
- Kostov et al. 2020, AJ 159, 253 (discovery)
- Standing et al. 2023, Nature Astronomy (TOI-1338 c discovery)

**Proxima Centauri:**
- Anglada-Escude et al. 2016, Nature 536, 437-440 (Proxima b)
- Faria et al. 2022, A&A 658, A115 (Proxima d)

### Binary System Implementation (v2.6)

**TOI-1338 Barycentric Dynamics:**

The v2.6 update fixes a critical bug in binary star orbital mechanics, ensuring stars maintain perfect 180° opposition throughout their orbit.

**Key Implementation Details:**

1. **Barycenter Object:**
 - New object type: `'exo_barycenter'`
 - Placed at origin (0, 0, 0) in system coordinate frame
 - Represents center of mass of binary system

2. **Stellar Orbital Calculations:**
 ```python
 # Center of mass formula
 a_A = binary_separation * (M_B / (M_A + M_B))
 a_B = binary_separation * (M_A / (M_A + M_B))

 # For TOI-1338:
 # M_A = 1.1 M☉, M_B = 0.3 M☉
 # binary_separation = 0.088 AU
 # Result: a_A = 0.019 AU, a_B = 0.069 AU
 ```

3. **Phase Relationship (FIXED in v2.6):**
 - Stars maintain **perfect 180° phase offset** (opposite sides) at all times ✓
 - Both complete orbit in 14.6 days ✓
 - Both have **identical angular velocity** (19.95°/day) ✓
 - Binary eccentricity: e = 0.16
 - Both orbit in **same direction** (counter-clockwise) ✓

4. **Opposition Fix (v2.6):**
 ```python
 # Calculate shared orbital phase
 M = n * dt_days                      # Same mean anomaly for both stars
 E = solve_kepler_equation(M, e)      # Same eccentric anomaly  
 nu = calculate_true_anomaly(E, e)    # Same true anomaly
 
 # Apply phase offset to TRUE ANOMALY (key fix!)
 nu_with_offset = nu + np.radians(phase_offset_deg)  # 0° for A, 180° for B
 x_orb = r * np.cos(nu_with_offset)
 y_orb = r * np.sin(nu_with_offset)
 ```
 
 **Why this works:**
 - Both stars share same orbital phase (mean & true anomaly)
 - Phase offset applied in orbital plane before Cartesian conversion
 - Maintains perfect 180° spatial separation throughout orbit
 - Preserves identical angular velocities

5. **Planet Orbital Reference:**
 - Planets orbit the barycenter, not individual stars
 - Stable circumbinary zone: distance > ~3 binary separation
 - TOI-1338 b: 0.461 AU (5.2 separation) stable
 - TOI-1338 c: 0.76 AU (8.6 separation) stable

**Physical Accuracy:**
- Obeys conservation of momentum (M₁r₁ = M₂r₂) ✓
- Stars orbit common center of mass ✓
- Barycenter remains at inertial frame origin ✓
- Matches observed binary star dynamics ✓
- **Perfect 180° opposition at all times (v2.6)** ✓

---

### Version 2.1, 2.2 & 2.6 Technical Fixes

**Critical Bug Fixes (October 22-25, 2025)**

#### v2.6: Binary Star Opposition Fix (October 25, 2025)

**Problem: Stars Not Maintaining 180° Opposition**
- Binary stars were moving in nearly the same direction instead of opposite sides
- Angular separation varied over time (170.6° → 156.5° → 147.3° over 3 days)
- Stars appeared to be getting closer together
- Violated fundamental binary star physics

**Root Cause:**
```python
# OLD (BROKEN) - v2.1 through v2.5:
x, y, z = calculate_planet_position(a, e, i_deg, omega_deg, Omega_deg,
                                   period, epoch, date)
# Apply static rotation (WRONG!)
x_rot = x * np.cos(phase_offset) - y * np.sin(phase_offset)
y_rot = x * np.sin(phase_offset) + y * np.cos(phase_offset)
```

The phase offset was applied as a **post-processing rotation** of the final position, not as an offset in the orbital phase. Both stars started from the same orbital phase, so they moved in the same direction.

**Solution (v2.6):**
```python
# NEW (FIXED) - v2.6+:
# Both stars share same mean & true anomaly (orbit together)
M = n * dt_days
E = solve_kepler_equation(M, e)
nu = calculate_true_anomaly(E, e)

# Apply offset to TRUE ANOMALY in orbital plane
nu_with_offset = nu + np.radians(phase_offset_deg)  # 0° for A, 180° for B
x_orb = r * np.cos(nu_with_offset)
y_orb = r * np.sin(nu_with_offset)
```

**Key Insight:**
- Can't add 180° to mean anomaly and solve separately (gives different true anomaly with eccentricity!)
- Must add 180° to true anomaly in the orbital plane
- Both stars share orbital phase but are spatially separated

**Results:**
```
Before Fix (v2.5):
  Oct 25: θ_A = -169.4°, θ_B = +20.0°,  Δθ = 170.6° ✗
  Oct 26: θ_A = -150.9°, θ_B = +52.6°,  Δθ = 156.5° ✗  
  Oct 27: θ_A = -131.2°, θ_B = +81.5°,  Δθ = 147.3° ✗

After Fix (v2.6):
  Oct 25: θ_A = -169.4°, θ_B = +10.6°,  Δθ = 180.0° ✓
  Oct 26: θ_A = -150.9°, θ_B = +29.1°,  Δθ = 180.0° ✓
  Oct 27: θ_A = -131.2°, θ_B = +48.8°,  Δθ = 180.0° ✓
```

**Angular Velocity Verification:**
```
Before Fix: Star A: +33.9°/day, Star B: +18.2°/day ✗ Different!
After Fix:  Star A: +19.95°/day, Star B: +19.95°/day ✓ Identical!
```

**File Modified:** `exoplanet_orbits.py` (function: `calculate_binary_star_position`)

#### v2.1: Plotly Symbol and Legend Fixes

**Problem 1: Invalid Plotly 3D Symbols**
- Plotly 3D scatter only supports: `'circle'`, `'square'`, `'diamond'`, `'cross'`, `'x'`, and `-open` variants
- Code used `symbol='star'` (valid in 2D, invalid in 3D)
- Caused: `ValueError: Invalid value 'star' received for symbol`

**Solution:**
```python
# Before (CRASH):
marker=dict(size=10, color='yellow', symbol='star')

# After (WORKS):
marker=dict(size=10, color='yellow', symbol='circle')
```

**Files modified:** `exoplanet_orbits.py` (3 locations - lines 432, 480, 516)

**Problem 2: Cluttered Legend**
- Orbital path traces appeared in legend with `showlegend=True`
- Legend showed "TOI-1338 A orbit" instead of star names

**Solution:**
```python
# Before:
fig.add_trace(go.Scatter3d(..., showlegend=True)) # Orbit path

# After:
fig.add_trace(go.Scatter3d(..., showlegend=False)) # Hidden from legend
```

**Files modified:** `exoplanet_orbits.py` (2 locations - lines 468, 504)

#### v2.2: Coplanar Orbits and JPL Horizons Fix

**Problem 1: Non-Coplanar Binary System**
- Binary stars had inclination i=0° (XY plane, horizontal)
- Planets had inclination i=89° (XZ plane, vertical)
- Result: 90° misalignment - physically impossible for circumbinary system!

**Why this matters:**
```
Real TOI-1338 (Kostov et al. 2020):
- Binary inclination: 89.0° ± 0.2°
- Planet b inclination: 89.0° ± 0.5°
- i < 1° COPLANAR (formed from same disk)

Our code before fix:
- Binary inclination: 0°
- Planet inclination: 89°
- i = 89° PERPENDICULAR (impossible!)
```

**Solution:**
```python
# In exoplanet_systems.py (line ~357):
'binary_inclination_deg': 89.0, # Match planet inclination
'binary_Omega_deg': 0.0, # Longitude of ascending node

# In exoplanet_orbits.py (read from system data):
binary_i = host_star_system.get('binary_inclination_deg', 0.0)
binary_Omega = host_star_system.get('binary_Omega_deg', 0.0)

# Use in orbit calculations:
x, y, z = calculate_keplerian_orbit(
 a, e,
 binary_i, binary_omega, binary_Omega, # Use system values
 period, epoch, date
)
```

**Files modified:**
- `exoplanet_systems.py` (2 lines added)
- `exoplanet_orbits.py` (6 changes in orbit and position calculations)

**Problem 2: JPL Horizons Query Errors**
- Code attempted to fetch exoplanet data from JPL Horizons
- JPL Horizons only contains Solar System objects
- Caused: `ValueError: id_type (exoplanet) not allowed` (repeated every frame)

**Solution:**
```python
# In orbit_data_manager.py (lines ~567-571):
# Skip JPL Horizons for exoplanets - they use Keplerian calculations
if obj_info.get('object_type') in ['exoplanet', 'exo_host_star']:
 return None
if id_type in ['exoplanet', 'binary_star_a', 'binary_star_b', 'barycenter']:
 return None
```

**Files modified:** `orbit_data_manager.py` (6 lines added)

**Impact:**
- Clean console output (no error messages)
- Faster execution (no wasted API calls to JPL)
- Proper separation: Solar System uses JPL, exoplanets use Keplerian

**Problem 3: Coordinate System Legend Clarity**
- Base legend didn't explain exoplanet viewing geometry
- Users confused about "sky plane" and viewing direction
- Unclear why inclination matters for transit observations

**Solution:**
```python
# In palomas_orrery.py (line ~3802):
is_exoplanet_mode = bool(exo_objects or exo_host_stars)

# Conditional legend text (lines ~4703-4712):
text=(
 "+X: Sun's direction from Earth at the vernal equinox ()"
 + ("(Same for exoplanets: vernal equinox direction)"
 if is_exoplanet_mode else "")
 + "+Z: Ecliptic North perpendicular to Earth's orbit"
 + ("(For exoplanets: toward Earth from star)"
 if is_exoplanet_mode else "")
 + "XY plane: Ecliptic, Earth's orbital plane"
 + ("(For exoplanets: sky plane, +X toward , +Z toward Earth)"
 if is_exoplanet_mode else "")
)
```

**Files modified:** `palomas_orrery.py` (~20 lines added at 3 locations)

**Impact:**
- Context-aware legend (adapts to Solar System vs exoplanet mode)
- Clear explanation of viewing geometry and sky plane
- Users understand +X is fixed (toward vernal equinox )
- No rotation ambiguity (both +X and +Z directions specified)
- Connection between edge-on orbits (i90°) and transit detection

#### Physical Consequences of Coplanar Fix

**Before (Perpendicular):**
- Unrealistic geometry
- Doesn't match observations
- Inconsistent with formation models
- User confusion about system structure

**After (Coplanar):**
- Physically accurate (matches Kostov et al. 2020)
- Edge-on view explains transit detections
- Consistent with disk formation theory
- Clear, understandable visualization

**Educational Value:**
- Shows why transits are observable (edge-on system)
- Demonstrates coplanar nature of circumbinary systems
- Illustrates disk formation and planet migration
- Matches real astronomical data

---

### Orbital Elements Explained

**Keplerian Elements (6 parameters define an orbit):**

1. **Semi-major axis (a)** - Size of orbit (AU)
 - Distance from center to farthest point along major axis
 - Determines orbital period via Kepler's 3rd law

2. **Eccentricity (e)** - Shape of orbit (0 = circle, 0-1 = ellipse)
 - e=0: Perfect circle
 - e=0.1: Slightly elliptical (most exoplanets)
 - e=0.5: Very elliptical (some comets)
 - e1: Hyperbola (not bound)

3. **Inclination (i)** - Tilt of orbit (degrees)
 - i=0°: Face-on (orbit in XY plane)
 - i=90°: Edge-on (orbit perpendicular to XY, we see transits!)
 - i=89.7°: Typical for TRAPPIST-1 (edge-on, transiting)

4. **Longitude of Ascending Node (©)** - Where orbit crosses sky plane (degrees)
 - Defines orientation of orbital plane in space
 - Measured counterclockwise from reference direction

5. **Argument of Periapsis ()** - Where orbit is closest to star (degrees)
 - Angle from ascending node to closest approach point
 - =0°: Periapsis at ascending node

6. **Mean Anomaly (M) at Epoch** - Where planet is at reference time
 - M=0°: At periapsis (closest)
 - M=180°: At apoapsis (farthest)
 - Increases linearly with time

**Epoch:** Reference date when elements are measured (e.g., J2000 = Jan 1, 2000)

### Distance Conversions

```python
# Fundamental conversions
1 parsec (pc) = 3.26156 light-years (ly)
1 parsec = 206,265 Astronomical Units (AU)
1 AU = 149,597,870.7 kilometers

# Examples:
TRAPPIST-1: 12.43 pc = 40.5 ly = 2,564,115 AU
TOI-1338: 396 pc = 1,292 ly = 81,680,940 AU
Proxima Centauri: 1.30 pc = 4.24 ly = 268,145 AU
```

### Angular Measurements

```python
# Angular units
1 degree = 60 arcminutes (arcmin, ²)
1 arcminute = 60 arcseconds (arcsec, ³)
1 arcsecond = 1000 milliarcseconds (mas)

# Proper motion examples:
Proxima Centauri: 3854 mas/year = 3.854 arcsec/year
 Moves 1 degree across sky in 933 years
 Noticeable change in decades!

TRAPPIST-1: 1032 mas/year = 1.032 arcsec/year
 Moves 1 degree in 3,489 years
 Visible in long-term observations

TOI-1338: 5.6 mas/year = 0.0056 arcsec/year
 Moves 1 degree in 642,857 years
 Essentially fixed for visualization purposes
```

### Coordinate Systems

**Local Exoplanet Frame (used in Paloma's Orrery):**
```
Origin: Host star at (0, 0, 0)
X-axis: Arbitrary in sky plane (perpendicular to line of sight)
Y-axis: 90° from X in sky plane
Z-axis: Toward Earth (line of sight direction)
Units: Astronomical Units (AU)
Reference: Local to each system (independent)
```

**J2000 Equatorial Frame (stellar positions):**
```
Origin: Solar System barycenter
X-axis: Vernal equinox (RA=0h, Dec=0°)
Y-axis: RA=6h, Dec=0°
Z-axis: North celestial pole (Dec=+90°)
Units: Parsecs, light-years, or AU
Epoch: J2000.0 (Jan 1, 2000, 12:00 TT)
```

**Sky Plane (observational):**
```
Plane perpendicular to Earth-star line of sight
X-axis: Typically aligned with RA (east)
Y-axis: Typically aligned with Dec (north)
Used for: Astrometry, proper motion, transit observations
```

### Understanding Epochs: Solar System vs Exoplanets

**The Key Question:** What does "epoch" mean for exoplanets, and how does it differ from J2000.0 used in solar system calculations?

#### Solar System: J2000.0 as Coordinate Frame Reference

**J2000.0 (January 1, 2000, 12:00:00 UTC):**
- **Purpose:** Defines the reference orientation of the ecliptic coordinate system
- **What it means:** Earth's orbital plane at this specific moment in time
- **How we use it:** All positions are transformed TO this fixed frame
- **Data source:** JPL Horizons provides real-time positions already in J2000.0 frame
- **Frame definition:**
 - **+Z:** Ecliptic North (perpendicular to Earth's orbit at J2000.0)
 - **+X:** Toward vernal equinox () at J2000.0
 - **XY Plane:** Earth's orbital plane at J2000.0

**Why J2000.0?** Standard astronomical epoch for consistency. The ecliptic slowly precesses, so we need a fixed reference date.

#### Exoplanets: Discovery Date as Orbital Phase Reference

**Discovery Epochs (TRAPPIST1_DISCOVERY_EPOCH, etc.):**
- **Purpose:** Defines when planet was at a known position in its orbit
- **What it means:** Reference time for calculating orbital phase
- **How we use it:** Calculate where planet should be at any other time
- **Data source:** We calculate positions using Keplerian math with measured parameters
- **Frame definition:**
 - **+Z:** Line of sight from star toward Earth (toward us!)
 - **+X:** Toward RA=0° () - same as solar system for consistency
 - **XY Plane:** Sky plane (perpendicular to line of sight)

**Why Discovery Date?** This is when orbital parameters were measured from observations!

#### The Critical Difference

| Aspect | Solar System (J2000.0) | Exoplanets (Discovery Date) |
|--------|------------------------|----------------------------|
| **Epoch Purpose** | Coordinate frame reference | Orbital phase reference |
| **What It Defines** | Orientation of ecliptic plane | When planet was at known position |
| **Frame Type** | Ecliptic (Earth's orbit) | Sky Plane (perpendicular to sight) |
| **Data Source** | JPL Horizons (ephemeris) | Keplerian calculations |
| **Position Updates** | Fetched at any time | Calculated from epoch |
| **Reference Date Changes?** | No (fixed at year 2000) | Yes (unique per system) |

#### How Exoplanet Positions Are Calculated

**Step 1: Calculate Mean Anomaly (Orbital Phase)**
```python
# Time elapsed since observation
dt_days = (current_date - epoch).total_seconds() / 86400.0

# Mean motion (how fast planet orbits)
n = 2 / period_days

# Where planet should be in its orbit
M = n * dt_days # Mean anomaly since epoch
```

The epoch tells us: "At this moment, the planet was HERE in its orbit." We use this to calculate where it is NOW.

**Step 2: Convert to Position**
```python
# Solve Kepler's equation: M = E - e*sin(E)
E = solve_kepler_equation(M, e) # Eccentric anomaly

# Convert to true position in orbit
1/2 = calculate_true_anomaly(E, e) # True anomaly
r = a * (1 - e²) / (1 + e*cos(1/2)) # Distance from star

# 3D position in orbital plane
x_orb = r * cos(1/2)
y_orb = r * sin(1/2)

# Rotate to sky plane frame using , i, ©
x, y, z = apply_rotations(x_orb, y_orb, , i, ©)
```

#### Are Exoplanet Positions "Real" or Arbitrary?

**Real (Based on Observations):**
- **Period** - Measured from repeated transits (very precise!)
- **Semi-major axis** - Calculated from period using Kepler's 3rd law
- **Eccentricity** - Measured from transit timing variations
- **Inclination** - Edge-on (~90°) for transiting planets
- **Epoch** - Time of mid-transit observation (when we saw it!)

**Assumed (Cannot Be Measured from Earth):**
- ** (omega)** - Argument of periapsis
 - Set to 0° because it's poorly constrained
 - Doesn't matter much for nearly circular orbits (e0)
 - Only affects highly eccentric orbits

- **© (Omega)** - Longitude of ascending node
 - Set to 0° by convention
 - **Cannot measure from Earth!** (degeneracy in 2D projection)
 - Defines rotation around Z-axis (line of sight)
 - Choosing ©=0° is just picking an orientation in the sky plane

#### Example: TRAPPIST-1 b Orbital Elements

```python
'period_days': 1.51087081, # ±0.00000060 MEASURED (very precise!)
'semi_major_axis_au': 0.01154, # ±0.00004 CALCULATED from period
'eccentricity': 0.00622, # ±0.00304 MEASURED (from transits)
'inclination_deg': 89.728, # ±0.087 MEASURED (edge-on)
'omega_deg': 0.0, # NOT MEASURED (assumed)
'Omega_deg': 0.0, # CANNOT MEASURE (arbitrary choice)
'epoch': TRAPPIST1_DISCOVERY_EPOCH # Feb 22, 2017 When transit observed
```

**What the epoch means for TRAPPIST-1 b:**
- On February 22, 2017, this planet crossed in front of its star (mid-transit)
- At that moment, we could measure its orbital phase
- Now we can calculate where it should be at any other time!

#### Why We DON'T Use J2000.0 for Exoplanets

**Key insight:** Exoplanet systems are light-years away - they're NOT in our solar system!

- We're not putting them in the J2000.0 ecliptic frame (that wouldn't make sense)
- We're showing them in their own **local coordinate system** as seen from Earth
- The "sky plane" is the natural viewing frame for distant objects
- Each system has its own independent coordinate frame

**Visual Summary:**

```
Solar System:
 Frame: J2000.0 Ecliptic (Earth's orbit at year 2000)
 Reference: Coordinate system orientation
 +Z Direction: Ecliptic North
 Data: Real-time from JPL Horizons

Exoplanet Systems:
 Frame: Sky Plane (perpendicular to line of sight)
 Reference: Orbital phase (when planet was observed)
 +Z Direction: Toward Earth (line of sight)
 Data: Calculated from Keplerian elements
 Epoch: Discovery date (when parameters measured)
```

#### Physical Meaning of Orbital Parameters

**For transiting exoplanets like TRAPPIST-1:**

1. **Why i90°?**
 - We see transits (planet crosses in front of star)
 - Only possible if orbit is edge-on
 - i=90° means we're looking along the orbital plane

2. **Why ©=0°?**
 - From Earth, we can't measure rotation around line of sight
 - It's a degeneracy - all values of © look the same!
 - Setting ©=0° is just choosing a reference orientation

3. **Why =0° for circular orbits?**
 - When e0, the orbit is nearly circular
 - "Closest point" (periapsis) is poorly defined
 - The choice doesn't affect the visualization

**The Bottom Line:**
- Positions are **physically meaningful** based on measured orbits
- We know **when** each planet passes in front of its star (epoch)
- We calculate **where** it should be at any other time
- The viewing geometry is **observer-centric** (sky plane)
- Some angles are **arbitrary** (©, ) but don't affect what we see from Earth

### Key Constants

```python
# Physical constants
SPEED_OF_LIGHT = 299792.458 # km/s
AU_TO_KM = 149597870.7 # km per AU
PC_TO_AU = 206264.806 # AU per parsec
PC_TO_LY = 3.26156 # light-years per parsec

# Time constants
JULIAN_YEAR = 365.25 # days
SECONDS_PER_DAY = 86400 # seconds

# Solar values (reference)
SOLAR_MASS = 1.9885e30 # kg
SOLAR_RADIUS = 6.95700e5 # km
SOLAR_LUMINOSITY = 3.828e26 # watts
SOLAR_TEMPERATURE = 5778 # K (effective)

# Earth values (reference for exoplanets)
EARTH_MASS = 5.9722e24 # kg = 1 M
EARTH_RADIUS = 6371.0 # km = 1 R
EARTH_DENSITY = 5.514 # g/cm³
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Sun still appears when viewing TRAPPIST-1"

**Problem:** Sun marker or legend entry shows up even when centered on exoplanet system

**Cause:** System filtering not working correctly

**Solution:**
1. Check that you've selected the exoplanet host star in the **Center Object** dropdown
2. Verify dropdown shows: "TRAPPIST-1" (not "Sun")
3. If Sun checkbox is still visible/checked, uncheck it
4. The center object should automatically filter out objects from other systems

**Technical fix (if problem persists):**
- Ensure `center_system_id` is correctly set from center object
- Verify all plotting loops include system_id filter:
 ```python
 if obj.get('system_id', 'solar') != center_system_id:
 continue
 ```

---

#### Issue 2: "No exoplanet host stars in Center Object dropdown"

**Problem:** Dropdown only shows Solar System objects

**Cause:** Exoplanet host stars not added to center_options list

**Solution:**
Check that `center_options` is built dynamically:

```python
# In palomas_orrery.py, around line 7260:
solar_system_centers = ['Sun', 'Mercury', 'Venus', ...]

# Add exoplanet host stars
exoplanet_host_stars = [obj['name'] for obj in objects
 if obj.get('object_type') == 'exo_host_star']

center_options = solar_system_centers + exoplanet_host_stars
```

If missing, the dropdown won't include exoplanet stars.

---

#### Issue 3: "Exoplanet checkboxes not appearing"

**Problem:** No exoplanet systems in the "Select Objects" panel

**Cause:** Objects list doesn't include exoplanet entries

**Solution:**
Verify exoplanet objects are added to the `objects` list in GUI setup:

```python
# Should see sections like:
TRAPPIST1_SYSTEM = get_system('trappist1')
for planet in TRAPPIST1_SYSTEM['planets']:
 planet_var = tk.IntVar()
 objects.append({
 'name': planet['name'],
 'id': planet['planet_id'],
 'var': planet_var,
 'color': 'lightblue',
 'object_type': 'exoplanet',
 'system_id': 'trappist1',
 'id_type': 'exoplanet'
 })
```

---

#### Issue 4: "Planets not orbiting, just sitting still"

**Problem:** Orbit paths don't appear or planets don't move in animation

**Cause:** Orbital parameters not properly fetched or calculated

**Solutions:**
1. **Check orbital parameter availability:**
 - Verify planet has all 6 Keplerian elements (a, e, i, Omega, omega, period)
 - Check epoch is defined

2. **Verify orbit plotting is enabled:**
 - Look for "Plot Actual Orbits" checkbox
 - Ensure it's checked (should be default)

3. **Check animation settings:**
 - Verify time range is set (start and end dates)
 - Check time step is reasonable (1-10 days for exoplanets)
 - Ensure number of frames > 1

4. **Inspect console output:**
 - Look for error messages about orbit calculation
 - Check if `plot_actual_orbits()` is being called

---

#### Issue 5: "TOI-1338 Binary System Issues (FIXED in v2.1)"

**Problems that existed before v2.1:**
1. Two "TOI-1338 A" entries appeared in center object dropdown
2. When selecting a star as center, only that star appeared at origin (not both stars orbiting)
3. Planets (TOI-1338 b and c) didn't appear when plotting

**Root causes:**
- No barycenter object existed for selection
- Binary star plotting logic wasn't triggered when individual stars were selected
- System wasn't recognized as binary when centered on a star component

** Solution (v2.1):**
The system now includes a proper **barycenter object**:

1. **New center option:** "TOI-1338 A/B (Barycenter)" now appears in dropdown
2. **Correct visualization:** Both stars orbit the barycenter (center of mass at origin)
3. **Planets visible:** Both circumbinary planets now plot correctly
4. **Stars orbit correctly:**
 - Star A (yellow) orbits ~0.019 AU from barycenter
 - Star B (orange) orbits ~0.069 AU from barycenter
 - Both stars on opposite sides, 14.6-day period

**How to use (v2.1+):**
```
1. Select "TOI-1338 A/B (Barycenter)" as center object
2. Check these boxes in the Exoplanet Systems panel:
 [ ] TOI-1338 A/B (Barycenter)
 [ ] TOI-1338 A (G-type)
 [ ] TOI-1338 B (M-type)
 [ ] TOI-1338 b (95d)
 [ ] TOI-1338 c (216d)
3. Set scale to 1 AU
4. Plot!
```

**Expected result:**
- White X marker at center (barycenter)
- Yellow star (A) and orange star (B) with dotted orbital paths
- Both planets with solid orbital paths
- All objects hoverable with detailed info

**If you're still experiencing issues:**
- Ensure you have version 2.1 or later
- Check that `toi1338_barycenter_var` exists in the code
- Verify barycenter object is in the objects list
- See the code changes document for implementation details

---

#### Issue 6: "Binary stars not visible in TOI-1338"

**Problem:** Only planets show up, stars missing

**Cause:** Binary star plotting code not triggered

**Solution:**
1. **Ensure TOI-1338 checkbox is selected** (not just the planets)
2. **Verify binary star data is complete:**
 ```python
 system['host_star']['is_binary'] == True
 system['host_star']['binary_orbit'] is defined
 ```
3. **Check plotting code:**
 - `plot_binary_host_stars()` should be called when `is_binary == True`
 - Both Star A and Star B should have orbit definitions

---

#### Issue 7: "ValueError: Invalid value 'star' received for symbol" (Fixed in v2.1)

**Problem:** Plotly crashes with "Invalid value of type 'builtins.str' received for the 'symbol' property"

**Cause:** Using `symbol='star'` which is not supported in Plotly 3D scatter plots

**Solution (Applied in v2.1):**
- Changed to `symbol='circle'` for all stars
- Plotly 3D only supports: `'circle'`, `'square'`, `'diamond'`, `'cross'`, `'x'`, and their `-open` variants
- For reference, see `plotly_3d_symbols_reference.md` documentation

**If you encounter this:**
1. Check that all `marker=dict(symbol=...)` use valid 3D symbols
2. Never use `'star'` in 3D plots (it works in 2D but not 3D)
3. Use `'circle'` or `'diamond'` for star-like objects

---

---

#### Issue 9: "Binary stars not maintaining opposition" (Fixed in v2.6)

**Problem:** Binary stars appear to move in nearly the same direction instead of orbiting on opposite sides of the barycenter. Angular separation between stars changes over time instead of maintaining constant 180°.

**Symptoms:**
- Stars appear to be getting closer together or moving apart
- Animation shows stars "chasing" each other rather than "dancing" opposite
- Angular separation varies (e.g., 170° → 156° → 147° over a few days)
- Different angular velocities for each star

**Verification:**
Track star positions over 2-3 days and measure angles:
```python
angle_A = arctan2(y_A, x_A)
angle_B = arctan2(y_B, x_B)
separation = |angle_A - angle_B|
```

If separation varies significantly from 180°, the bug is present.

**Root Cause (v2.1-2.5):**
The phase offset was applied as a geometric rotation of the final position, not as an offset in the orbital phase:
```python
# BROKEN approach:
x, y, z = calculate_planet_position(...)  # Both stars from same phase
x_rot = x * cos(180°) - y * sin(180°)     # Static rotation
```

This meant both stars started from the same orbital phase and moved together, with Star B's position just rotated.

**Solution (v2.6):**
Apply the 180° offset to the true anomaly in the orbital plane:
```python
# FIXED approach:
M = n * dt_days                    # Same mean anomaly for both
nu = calculate_true_anomaly(...)   # Same true anomaly
nu_B = nu + π                      # Add 180° to Star B's true anomaly
x_B = r * cos(nu_B)                # Calculate from offset true anomaly
```

**Verification After Fix:**
```
Perfect 180° separation at all times:
  Day 0:  θ_A = 0.0°,    θ_B = 180.0°,  Δθ = 180.0° ✓
  Day 1:  θ_A = 48.7°,   θ_B = -131.3°, Δθ = 180.0° ✓
  Day 7:  θ_A = 180.0°,  θ_B = 0.0°,    Δθ = 180.0° ✓
  Day 14: θ_A = 0.0°,    θ_B = 180.0°,  Δθ = 180.0° ✓

Identical angular velocities:
  Star A: +19.95°/day ✓
  Star B: +19.95°/day ✓
```

**How to Update:**
- Upgrade to v2.6 or later
- Replace `calculate_binary_star_position()` function in `exoplanet_orbits.py`
- No changes needed to data files or GUI code

---

#### Issue 8: "Binary star orbits perpendicular to planets" (Fixed in v2.2)

**Problem:** TOI-1338 binary stars orbit horizontally while planets orbit vertically (90° apart)

**Cause:** Binary orbit inclination was hardcoded to 0° instead of matching planet inclination

**Solution (Applied in v2.2):**
- Added `binary_inclination_deg: 89.0` to TOI-1338 system definition
- Modified orbit calculations to use system inclination
- All objects now coplanar (same orbital plane)

**Physical reasoning:**
- Circumbinary systems form from single disk coplanar
- TOI-1338 observed edge-on (i 89°) all components should have same inclination
- Coplanar configuration is dynamically stable

---

#### Issue 9: "JPL Horizons errors for exoplanet objects" (Fixed in v2.2)

**Problem:** Console flooded with "ValueError: id_type (exoplanet) not allowed" messages

**Cause:** Code attempting to query JPL Horizons for exoplanet data (not in database)

**Solution (Applied in v2.2):**
- Added skip logic in `fetch_orbit_path()` for exoplanet objects
- Exoplanets use Keplerian calculations, not JPL ephemerides
- Skip `object_type` in `['exoplanet', 'exo_host_star']`
- Skip `id_type` in `['exoplanet', 'binary_star_a', 'binary_star_b', 'barycenter']`

**Result:**
- Clean console output
- Faster execution (no wasted API calls)
- Proper separation: Solar system objects use JPL, exoplanets use Keplerian

---

#### Issue 10: "Orbits look weird or incorrect"

**Problem:** Orbital paths don't match expected geometry

**Possible causes and solutions:**

1. **Inclination issues:**
 - Check inclination value (should be 0-180°)
 - Edge-on systems: i 90°
 - Face-on systems: i 0° or 180°

2. **Eccentricity problems:**
 - Verify 0 e < 1 for bound orbits
 - High eccentricity (e > 0.5) creates very elliptical orbits
 - Check if eccentricity is mistakenly in radians instead of 0-1 scale

3. **Angular units:**
 - All angles should be in degrees (not radians)
 - omega, Omega should be 0-360°

4. **Period mismatch:**
 - Check period is in days (not years)
 - Verify semi-major axis is in AU (not other units)

---

#### Issue 11: "Proper motion not working for Proxima Centauri"

**Problem:** Star position doesn't change over time in animations

**Cause:** Proper motion corrections not applied or date not changing

**Solution:**
1. **Verify proper motion data is present:**
 ```python
 system['host_star']['pmra'] # Should be ~922.88 mas/yr
 system['host_star']['pmdec'] # Should be ~-469.24 mas/yr
 ```

2. **Check animation date range:**
 - Need significant time span (years/decades) to see proper motion
 - Short time ranges (days/weeks) won't show noticeable change

3. **Note:** Proper motion moves the star in galactic coordinates, not in the local frame
 - In single-system plots, star stays at origin (correct behavior)
 - Proper motion will be visible in Phase 4 stellar neighborhood visualization

---

### Performance Optimization

#### Slow plotting/animation

**Symptoms:** Long wait times when clicking "Plot" or "Animate"

**Solutions:**

1. **Reduce number of objects:**
 - Uncheck unnecessary objects
 - Focus on 1-2 systems at a time

2. **Decrease animation frames:**
 - Reduce number of frames from 100 to 50
 - Increase time step

3. **Simplify orbits:**
 - Reduce `num_points` in orbit calculation (default 100, try 50)

4. **Check network connection:**
 - If code tries to fetch data from APIs, slow network causes delays
 - Use cached data when possible

---

### Reporting Issues

If you encounter problems not covered here:

**Include in your report:**
1. **What you were trying to do** (step-by-step)
2. **What happened** (actual result)
3. **What you expected** (desired result)
4. **Error messages** (if any - check console/terminal)
5. **System info:**
 - Python version: `python --version`
 - Operating system
 - Plotly version: `pip show plotly`
6. **Screenshots** (if visual issue)

**Contact:**
- Email: tonyquintanilla@gmail.com
- GitHub Issues: https://github.com/tonylquintanilla/palomas_orrery/issues

---

## Future Enhancements

### Phase 2: NASA Exoplanet Archive Integration

**Goal:** Dynamic data fetching from live database

**Features:**
- Query NASA Exoplanet Archive TAP service
- Download orbital parameters automatically
- Filter by:
 - Distance (nearest systems)
 - Discovery method
 - Discovery year
 - Planet size/mass
 - Habitable zone status
- Update catalog as new discoveries are made

**Implementation timeline:** 2-3 months after Phase 1 stabilizes

**Technical approach:**
```python
from astroquery.nasa_exoplanet_archive import NasaExoplanetArchive

# Query all planets within 100 pc
planets = NasaExoplanetArchive.query_criteria(
 table='pscomppars',
 where='sy_dist < 100',
 select='pl_name,hostname,pl_orbper,pl_orbsmax,pl_bmasse'
)
```

---

### Phase 3: Additional Systems

**Candidate systems for inclusion:**

**High Priority:**
1. **Kepler-90** - 8 planets (most planets in a system)
2. **HR 8799** - 4 directly imaged giant planets
3. **WASP-12** - Ultra-hot Jupiter, inflated
4. **55 Cancri** - 5 planets, dense super-Earth
5. **HD 189733** - "Blue marble" hot Jupiter

**Educational Value:**
6. **51 Pegasi** - First exoplanet around Sun-like star (historical)
7. **LHS 1140** - Super-Earth in HZ, good for JWST
8. **Kepler-452** - "Earth's cousin", Sun-like star

**Extreme Cases:**
9. **PSR B1257+12** - Pulsar planets (first exoplanets ever!)
10. **OGLE-2005-BLG-390L** - Microlensing discovery

**Selection criteria:**
- Well-characterized orbits (all 6 Keplerian elements known)
- Scientific or historical significance
- Educational value (demonstrates different discovery methods)
- Diverse system types (hot Jupiters, super-Earths, sub-Neptunes)

---

### Phase 4: Stellar Neighborhood Visualization

**Goal:** 3D map showing all exoplanet host stars in galactic context

**Features:**
- Plot host stars in 3D galactic coordinates (X, Y, Z from Sun)
- Show Solar System at origin
- Distance scale: 0-100 light-years
- Color-code by:
 - Spectral type (blue = hot, red = cool)
 - Number of planets
 - Habitable zone planets present
- Click stars to load their planetary systems
- Animate stellar proper motions over centuries

**Visualization concept:**
```
User sees:
- Sun at center
- TRAPPIST-1 at (X=31.2, Y=-24.8, Z=13.7) ly
- Proxima Centauri at (X=-1.5, Y=3.8, Z=-0.9) ly
- TOI-1338 at (X=805, Y=-962, Z=241) ly
- ...

User can:
- Zoom out to see distribution of exoplanet hosts
- Rotate to see 3D structure
- Click star load that system in detailed view
- Play animation see stars move with proper motion
```

**Implementation challenges:**
- Need accurate 3D positions (RA, Dec, Distance)
- Proper motion corrections critical for nearby stars
- Coordinate transforms: Equatorial Galactic
- Scale range: 4 ly (Proxima) to 1000+ ly (distant systems)
- Performance: Rendering hundreds of stars + orbits

**Technical approach:**
```python
from astropy.coordinates import SkyCoord
import astropy.units as u

# Convert RA/Dec/Distance to 3D Cartesian
coord = SkyCoord(
 ra=ra*u.degree,
 dec=dec*u.degree,
 distance=distance*u.pc,
 frame='icrs'
)

# Transform to galactic frame (X,Y,Z from Sun)
galactic = coord.galactocentric
x, y, z = galactic.x.value, galactic.y.value, galactic.z.value
```

---

### Phase 5: Advanced Features

**1. Transit Light Curves**
- Simulate transit observations
- Show brightness dips as planets cross star
- Educational tool for understanding transit photometry method

**2. Radial Velocity Curves**
- Animate stellar wobble caused by planets
- Show velocity vs. time graph
- Demonstrate mass-determination method

**3. Habitable Zone Visualization**
- Shaded region showing HZ boundaries
- Update dynamically based on stellar properties
- Compare Earth's HZ position to exoplanets

**4. Atmospheric Composition (if data available)**
- Overlay spectroscopy results from JWST
- Show detected molecules (H2O, CH4, CO2, etc.)
- Link to NASA press releases

**5. Multi-System Comparison**
- Side-by-side view of multiple systems
- Scale comparison tool
- Statistical analysis (period distributions, mass-radius plots)

**6. Time Travel**
- Set date to past or future
- See system evolution
- Historical context (discovery dates, mission observations)

**7. Mission Planning Mode**
- Show when planets are observable from Earth
- Transit prediction calendars
- Optimal observation windows

---

## Summary

### What You Have Now

- **3 fully integrated exoplanet systems** (TRAPPIST-1, TOI-1338, Proxima Centauri)
- **11 exoplanets** with accurate orbital mechanics
- **Seamless UI** - exoplanets alongside Solar System objects
- **System-specific centering** - view each system independently
- **Full animation support** - watch systems evolve over time with Keplerian orbit calculations (v2.5)
- **Time-lapse animations** - daily, monthly, or yearly time steps for orbital motion visualization (v2.5)
- **Binary star dynamics** - TOI-1338 circumbinary system with proper barycentric mechanics (v2.1, fixed v2.6)
- **Animated binary motion** - watch stellar pairs orbit their common center of mass (v2.5)
- **Temperature-based star colors** - realistic host star coloring from red M-dwarfs to blue hot stars (v2.3)
- **Rich stellar properties** - comprehensive hover information matching stellar neighborhood quality (v2.3)
- **Transparent center markers** - exoplanet hosts can be centered without redundant visual markers (v2.4)
- **Automatic mode detection** - animation system switches to exoplanet mode seamlessly (v2.5)
- **Comet visualization** - scientifically accurate dual-tail rendering with astrophotography-based colors (v2.7)
- **Animation bug fixes** - solar system object animations now work reliably (v2.7)
- **Habitable zone planets** - 5 potentially habitable worlds
- **Proper motion support** - accurate stellar positions over time
- **Complete documentation** - this guide!

### What's New in v2.2

- **Coplanar Binary Orbits** - TOI-1338 stars now orbit in same plane as planets (physically accurate!)
- **Correct Inclination** - Binary orbital inclination set to 89° (edge-on, matches planets)
- **No JPL Errors** - Exoplanet objects no longer query JPL Horizons (not in database)
- **Performance Boost** - Faster loading, no wasted API calls
- **Physical Accuracy** - System geometry now matches real TOI-1338 observations

### What Was New in v2.1

- **TOI-1338 Barycenter** - Proper center-of-mass visualization for binary stars
- **Fixed Binary Plotting** - Both stars now orbit the barycenter correctly
- **Fixed Planet Visibility** - Circumbinary planets now appear when plotting
- **Enhanced Physics** - Accurate representation of binary star orbital dynamics
- **Fixed Plotly Symbols** - Corrected invalid 'star' symbol causing crashes
- **Clean Legend** - Orbit paths hidden from legend

### How to Get Started

1. **Launch Paloma's Orrery:** `python palomas_orrery.py`
2. **Scroll to exoplanet section** in object selection panel
3. **Check boxes** for planets you want to see
4. **Set center** to the host star (dropdown at top)
5. **Click "Plot Objects"** to visualize!

### Resources

**Documentation:**
- This guide (exoplanet_readme.md)
- Inline code comments (comprehensive docstrings)
- Main README.md (general Paloma's Orrery info)
- **v2.2 Complete Fixes** (complete_toi1338_fixes_summary.md) - All Oct 22-23 fixes
- **v2.2 Coplanar Orbits** (coplanar_orbits_and_jpl_fix.md) - Geometry & JPL fixes
- **v2.2 Visual Comparison** (orbital_plane_visual_comparison.md) - Before/after diagrams
- **v2.1 Code Changes** (code_changes_detailed.md) - Symbol & legend fixes
- **v2.1 Plotly Reference** (plotly_3d_symbols_reference.md) - Valid 3D symbols guide

**Code Files:**
- `exoplanet_systems.py` - System catalog
- `exoplanet_orbits.py` - Orbital mechanics
- `exoplanet_coordinates.py` - Stellar positions
- `exoplanet_stellar_properties.py` - Stellar property calculations, temperature-based coloring, hover text generation
- `palomas_orrery.py` - Main application with GUI integration

**External Resources:**
- NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/
- SIMBAD Database: http://simbad.u-strasbg.fr/
- Project Website: https://tonylquintanilla.github.io/palomas_orrery/
- GitHub Repository: https://github.com/tonylquintanilla/palomas_orrery

**Support:**
- Email: tonyquintanilla@gmail.com
- GitHub Issues: https://github.com/tonylquintanilla/palomas_orrery/issues

---

### Acknowledgments

**Data Sources:**
- NASA Exoplanet Archive
- SIMBAD Astronomical Database (CDS, Strasbourg)
- Published scientific papers (Nature, Science, A&A, AJ)
- ESO HARPS/ESPRESSO, TESS, Spitzer, Kepler missions

**Development:**
- Tony Quintanilla (creator, Paloma's Orrery)
- Claude AI (implementation assistance)
- Anthropic (Claude)
- Python community (NumPy, Plotly, Astropy)

**Discoveries:**
- TRAPPIST-1 team (Gillon et al., 2017)
- TOI-1338 discoverer Wolf Cukier (NASA intern, 2020)
- Proxima Centauri b team (Anglada-Escude et al., 2016)
- All exoplanet researchers worldwide

---

**Version History:**

- **v1.0** (October 21-22, 2025) - Initial implementation, 3 systems, module documentation
- **v2.0** (October 22, 2025) - Full GUI integration, system-scoped filtering, comprehensive user guide
- **v2.1** (October 22, 2025) - TOI-1338 binary system fix: Plotly symbol errors fixed, barycenter object added, binary star plotting corrected, planet visibility fixed, legend cleaned
- **v2.2** (October 23, 2025) - Coplanar orbits: Binary stars now orbit in same plane as planets (i=89°), JPL Horizons queries skipped for exoplanets, performance improved, physical accuracy achieved
- **v2.3** (October 24, 2025) - Enhanced stellar visualization: Temperature-based star colors, rich hover text with stellar properties, new exoplanet_stellar_properties.py module, binary star hover text support, visual consistency with stellar neighborhood visualizations
- **v2.4** (October 24, 2025) - Center marker suppression: Transparent color support for exoplanet host stars as center objects, intelligent legend hiding for transparent markers, eliminates dual marker confusion
- **v2.5** (October 24, 2025) - Full animation support: animate_objects() now supports exoplanet systems, Keplerian orbit calculations for time-evolving visualizations, automatic mode detection, dynamic axis scaling, coordinate system labeling, binary star motion animation, feature parity with static plotting
- **v2.6** (October 25, 2025) - Binary star opposition fix: Critical physics correction for TOI-1338, phase offset now applied to true anomaly (not rotation), perfect 180° separation maintained throughout orbit, identical angular velocities for both stars, physically accurate "dance" across barycenter
- **v2.7** (October 28, 2025) - Comet visualization and animation fixes: Scientific dual-tail comet rendering (dust/ion tails), astrophotography-accurate colors based on spectroscopy, historical comet data (Halley, Lemmon, etc.), animation bug fix for `UnboundLocalError` in solar system animations

**Last Updated:** October 28, 2025

---

*"From worlds orbiting distant suns to understanding our place in the cosmos - Paloma's Orrery brings the universe to your screen."*

**Explore. Discover. Learn.** °
