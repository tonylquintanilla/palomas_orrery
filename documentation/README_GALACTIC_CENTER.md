# Galactic Center: S-Stars Orbiting Sagittarius A*

## Overview

This module visualizes the S-stars - a group of young, fast-moving stars that orbit **Sagittarius A* (Sgr A*)**, the supermassive black hole at the center of our Milky Way galaxy. These stars serve as nature's most extreme test of Einstein's General Relativity, reaching speeds up to 8% the speed of light.

**Part of Paloma's Orrery**  
*Data Preservation is Climate Action*

---

## The Science

### What is Sagittarius A*?

Sagittarius A* is a supermassive black hole with a mass of approximately **4.154 million solar masses**. Its event horizon (Schwarzschild radius) is about 0.08 AU - roughly 12 million kilometers, or 40 times the Earth-Moon distance.

### What are S-Stars?

The S-stars are a cluster of young, hot B-type stars orbiting extremely close to Sgr A*. Their existence presents a paradox: these young stars shouldn't be able to form so close to a black hole (the tidal forces would shred any gas clouds), yet there they are. Approximately 50 S-stars have measured orbits; this visualization shows four representative examples.

### The "Fantastic Four"

| Star | Period | Max Velocity | Eccentricity | Significance |
|------|--------|--------------|--------------|--------------|
| **S2** | 16.05 yr | 7,631 km/s (2.5% c) | 0.884 | The King - most studied, confirmed GR in 2018/2020 |
| **S62** | 9.9 yr | 20,252 km/s (6.8% c) | 0.976 | Former record holder for closest approach |
| **S4711** | 7.6 yr | 7,008 km/s (2.3% c) | 0.768 | The Hummingbird - shortest known orbital period |
| **S4714** | 12.0 yr | 24,693 km/s (8.2% c) | 0.985 | The Speed Demon - extreme eccentricity, potential "squeezar" |

### Einstein's Laboratory

These stars have confirmed two key predictions of General Relativity:

1. **Gravitational Redshift (2018)**: As S2 passed closest to the black hole, its light was stretched to longer wavelengths - gravity was literally holding the light back.

2. **Schwarzschild Precession (2020)**: Unlike Newtonian predictions where orbits close perfectly, S2's orbit was observed to rotate (precess) over time, creating a "rosette" pattern exactly as Einstein's equations predict.

---

## Features

### Two Visualization Modes

**1. Orbital Dynamics (Animation)**
- Watch stars orbit the black hole in real-time animation
- Experience the "whoosh" effect - stars speed up dramatically at periapsis (closest approach) and slow down at apoapsis (farthest point)
- This demonstrates **Kepler's Second Law**: equal areas in equal times

**2. Einstein's Laboratory (Rosette)**
- View the accumulated effect of relativistic precession over decades/centuries
- See the "spirograph" pattern that proves General Relativity
- Compare precession rates: S4714's dramatic spiral vs S2's subtle fan
- **Unified Time Spectrum**: Dark purple = now, bright yellow = far future

### Sagittarius A* Black Hole Representation

The visualization includes a detailed representation of the supermassive black hole:

- **Artistic Black Hole (50x scale)**: Purple sphere showing event horizon location, scaled up for visibility
- **Actual Scale Black Hole**: Tiny red sphere at true Schwarzschild radius (~0.08 AU) - toggle off the artistic version to see it!
- **Accretion Disk**: Orange gradient surface based on EHT 2022 and ALMA 2019 observations
- **Photon Ring**: Bright ring at 1.5x Schwarzschild radius where light can orbit the black hole
- **Gravitational Lensing**: Dome of rings above/below the disk showing how light from the far side bends around the black hole

### Periapsis Zoom Views

Jump directly to see stars at their closest approach to the black hole:

| Zoom Target | Distance | Velocity | View Size |
|-------------|----------|----------|-----------|
| S4714 at Periapsis | 12 AU | 8% c | +/-50 AU |
| S62 at Periapsis | 18 AU | 6.7% c | +/-50 AU |
| S2 at Periapsis | 120 AU | 2.5% c | +/-100 AU |
| S4711 at Periapsis | 133 AU | 4.5% c | +/-150 AU |
| Sgr A* Black Hole | - | - | +/-100 AU (4x zoom) |

### Observational Fidelity

- Orbital phases calculated from **observed periapsis times** (not arbitrary)
- Data sourced from GRAVITY Collaboration and Peissker et al.
- Positions accurate for the reference year (2025)
- Temperature-based star colors matching spectral types

### Interactive Controls

- **View Dropdown**: Switch between Animation and Rosette modes
- **Play/Pause**: Control the animation (starts paused)
- **Zoom Dropdown**: Jump to periapsis events or black hole detail view
- **Legend**: Toggle individual elements on/off (orbits, stars, lensing, etc.)
- **Drag/Scroll**: Rotate and zoom the 3D view

---

## Files

| File | Description |
|------|-------------|
| `sgr_a_star_data.py` | S-star orbital elements, physical constants, Kepler solver, hover text |
| `sgr_a_visualization_core.py` | Orbit generation, black hole rendering, gravitational lensing |
| `sgr_a_visualization_animation.py` | Stage 2: Keplerian animation engine |
| `sgr_a_visualization_precession.py` | Stage 3: Relativistic rosette traces |
| `sgr_a_grand_tour.py` | Stage 4: Unified dashboard combining all features |
| `sgr_a_grand_tour.html` | Pre-generated interactive visualization (~7 MB) |

---

## Installation

### Prerequisites

```bash
pip install numpy plotly
```

### Quick Start

1. Place all `sgr_a_*.py` files in the same directory
2. Run the grand tour generator:

```bash
python sgr_a_grand_tour.py
```

3. Open `sgr_a_grand_tour.html` in your web browser

### Integration with Paloma's Orrery

The visualization can be launched from the main orrery GUI. See `GALACTIC_CENTER_INTEGRATION_SNIPPET.py` for the code to add to `palomas_orrery.py`.

---

## Usage

### Standalone

```python
from sgr_a_grand_tour import create_grand_tour_dashboard

fig = create_grand_tour_dashboard()
fig.write_html("my_visualization.html")
```

### Exploring Individual Stars

```python
from sgr_a_star_data import get_star_summary, print_catalog_summary

# Get details for one star
print(get_star_summary('S2'))

# Print all stars
print_catalog_summary()
```

### Custom Rosette Visualization

```python
from sgr_a_visualization_precession import create_rosette_visualization

# Show only S2 and S4714
fig = create_rosette_visualization(stars_to_show=['S2', 'S4714'])
fig.show()
```

---

## The Physics

### Kepler's Second Law (Animation Mode)

The animation uses **mean anomaly stepping** rather than time stepping. This means each frame advances by a fixed angle, and the physics automatically produces:
- Fast motion at periapsis (close to black hole)
- Slow motion at apoapsis (far from black hole)

This is Kepler's "equal areas in equal times" made visceral.

### Schwarzschild Precession (Rosette Mode)

In Newtonian gravity, orbits close perfectly - an ellipse traces the same path forever. In General Relativity, the intense gravity near a black hole causes the orbit to **precess** (rotate) slightly each revolution.

**What determines precession rate:**
- Black hole mass (more mass = more spacetime curvature)
- How close the orbit gets (1/a dependence)
- Eccentricity (elongated orbits dip closer at periapsis)

The formula: `delta_phi = 3 * pi * Rs / (a * (1 - e^2))`

| Star | Precession Rate | Total Rotation (simulated) |
|------|-----------------|---------------------------|
| S2 | 0.20 deg/orbit | 16 deg over 80 orbits (1,284 years) |
| S4714 | 1.86 deg/orbit | 74 deg over 40 orbits (480 years) |

This is why S4714 shows a dramatic spiral while S2 shows a subtle fan.

### Gravitational Lensing

Light from the far side of the accretion disk bends around the black hole due to extreme spacetime curvature. The visualization shows this as concentric rings (domes) above and below the disk plane. Key features:

- **Photon Sphere** (1.5x Schwarzschild radius): Where light can orbit the black hole
- **Lensing Rings**: Represent light paths bent over the top and bottom of the black hole
- The effect is view-independent - looks similar from any horizontal viewing angle

---

## Data Sources

- **GRAVITY Collaboration** (2018, 2019, 2020) - S2 orbital elements and GR confirmation
- **Gillessen et al.** (2017) - Comprehensive S-star catalog
- **Peissker et al.** (2020) - S62, S4711, S4714 discoveries
- **Event Horizon Telescope** (2022) - First image of Sgr A*, accretion disk structure
- **ALMA/Murchikova et al.** (2019) - Cool accretion disk extends to ~1000 AU

### Accuracy Note

S4714's semi-major axis has been adjusted from 520 AU to **800 AU** to match the literature periapsis velocity (~8% c). This gives a periapsis of 12 AU, consistent with Peissker et al.

---

## What to Watch For

### In Animation Mode
- **S4714 (orange)**: Hangs lazily at apoapsis, then *SNAPS* through periapsis in just a few frames
- **S4711 (blue-white)**: Completes orbits fastest (7.6 year period)
- **All stars in 2025**: Currently near apoapsis (the slow phase)
- **S4714's next periapsis**: ~2029 (12 years after 2017)

### In Rosette Mode
- **S4714**: Dramatic spiral - the orbit rotates visibly with each pass
- **S2**: Subtle fan - this is what took 27 years of observations to measure
- **Color gradient**: Dark purple (now) -> Bright yellow (centuries in the future)

### Black Hole Detail View
- Toggle off "Sgr A* (Black Hole)" to reveal the tiny red actual-scale sphere
- Compare the artistic 50x representation with the true Schwarzschild radius
- Even S4714 at periapsis (12 AU) is still ~150x the event horizon size!

---

## Future Enhancements

Potential additions for future development:

- [ ] Historical event playback ("Jump to S2 Periapsis 2018")
- [ ] Gravitational redshift visualization at periapsis
- [ ] G-objects (gas clouds / possible merging binaries)
- [ ] Comparison with Mercury's precession (43 arcsec/century)
- [ ] Integration with stellar visualization module
- [ ] Additional S-stars (S38, S55, etc.)

---

## Collaboration

This module was developed through a three-way collaboration:

- **Tony Quintanilla** - Vision, scientific requirements, observational fidelity
- **Claude (Opus 4.5)** - Implementation, testing, documentation
- **Gemini (2.5 Pro)** - Architecture review, physics validation, refinements

*December 31, 2025 - January 2, 2026*

---

## References

1. GRAVITY Collaboration (2018). "Detection of the gravitational redshift in the orbit of the star S2 near the Galactic centre massive black hole." *Astronomy & Astrophysics*, 615, L15.

2. GRAVITY Collaboration (2020). "Detection of the Schwarzschild precession in the orbit of the star S2 near the Galactic centre massive black hole." *Astronomy & Astrophysics*, 636, L5.

3. Peissker, F., et al. (2020). "S62 and S4711: Indications of a Population of Faint Fast-moving Stars inside the S2 Orbit." *The Astrophysical Journal*, 899(1), 50.

4. Gillessen, S., et al. (2017). "An Update on Monitoring Stellar Orbits in the Galactic Center." *The Astrophysical Journal*, 837(1), 30.

5. Event Horizon Telescope Collaboration (2022). "First Sagittarius A* Event Horizon Telescope Results." *The Astrophysical Journal Letters*, 930, L12-L17.

6. Murchikova, E. M., et al. (2019). "A cool accretion disk around the Galactic Centre black hole." *Nature*, 570, 83-86.

---

## License

Part of Paloma's Orrery  
*For Paloma*

---

*"The S-stars are Einstein's messengers - racing around a monster we cannot see, tracing patterns that prove spacetime bends exactly as he predicted over a century ago."*
