# ORBITAL_MECHANICS_README v2.1 Update

## Documentation Changes for Orcus-Vanth Barycenter Visualization

**Date:** January 8, 2026  
**Version:** 2.1 (Orcus-Vanth Barycenter System & Living Science Philosophy)

---

## 1. UPDATE HEADER

**Replace:**
```
**Last Updated:** January 3, 2026 (v2.0 - TNO Moon Analytical Fallback System)  
```

**With:**
```
**Last Updated:** January 8, 2026 (v2.1 - Orcus-Vanth Barycenter System)  
```

---

## 2. ADD NEW SECTION (After Section 22 "Vector Subtraction Experiment")

### Insert new section:

```markdown
---

## 23. Orcus-Vanth Barycenter System (January 8, 2026)

### The "Anti-Pluto" Binary System

Orcus and Vanth form a remarkable binary system in the Kuiper Belt - often called the "Anti-Pluto" because:

- Both are **plutinos** (3:2 orbital resonance with Neptune)
- Orcus is at aphelion when Pluto is at perihelion (180 deg out of phase)
- Both have large moons forming true binary systems
- Named after underworld deities (Orcus is the Etruscan equivalent of Pluto)

**But Orcus-Vanth has the HIGHEST mass ratio of any known planet or dwarf planet system!**

| System | Mass Ratio (moon/primary) | Notes |
|--------|---------------------------|-------|
| **Orcus-Vanth** | **0.16 +/- 0.02** | **Highest known!** |
| Pluto-Charon | 0.12 | Second highest |
| Earth-Moon | 0.012 | Order of magnitude smaller |

### Binary Orbit Parameters

From Brown & Butler 2023 (ALMA observations Oct/Nov 2016):

| Parameter | Value | Notes |
|-----------|-------|-------|
| Total separation | 8,980 +/- 20 km | Center to center |
| Orbital period | 9.54 days | Both bodies tidally locked |
| Eccentricity | ~0.007 | Nearly circular |
| Inclination | 90 deg to ecliptic | **Face-on from Earth!** |
| Barycenter location | 13.7% from Orcus | Outside Orcus's surface! |
| Orcus distance from BC | ~1,230 km | Orcus radius is ~455 km |
| Vanth distance from BC | ~7,770 km | |

**Key insight:** The barycenter is **outside Orcus's surface**. Both bodies visibly orbit around a point in empty space between them.

### The JPL Horizons Challenge

JPL's satellite solution for the Orcus system uses specific IDs:

| ID | Object | Notes |
|----|--------|-------|
| `90482;` | Current barycenter | General solution |
| `20090482` | Satellite solution barycenter | Use as center for queries |
| `920090482` | Orcus PRIMARY body | **Defined AT the barycenter position!** |
| `120090482` | Vanth satellite | Works for relative queries |

**The problem:** When you query Orcus PRIMARY (920090482) relative to the barycenter (20090482), JPL returns **zero** - because in their solution, Orcus PRIMARY *is* the barycenter position.

```
Processing trajectory for 920090482:
-> Added closest plotted marker for Orcus to Orcus-Vanth Barycenter: 0.000000 AU
```

This is fundamentally different from Pluto-Charon where:
- Pluto (999) is a major body with its own ephemeris
- The barycenter (@9) is computed from Pluto + Charon positions
- Both can be queried independently

### Our Solution: Analytical Binary Orbits Only

For the Orcus-Vanth Barycenter view, we:

1. **Skip actual orbit traces** - JPL data doesn't give meaningful positions
2. **Skip position markers** - Would show Orcus at 0,0,0 (misleading)
3. **Show analytical osculating orbits** - Calculated from ALMA parameters
4. **Show the barycenter marker** - The center of the visualization
5. **Provide full citations in hovertext** - So viewers can learn more

```python
# In plot_actual_orbits():
if center_object_name == 'Orcus-Vanth Barycenter' and planet in ['Orcus', 'Vanth']:
    print(f"[ORCUS-VANTH] Skipping actual orbit for {planet} - using analytical binary orbit only")
    continue

# In position marker plotting:
if center_object_name == 'Orcus-Vanth Barycenter' and obj['name'] in ['Orcus', 'Vanth']:
    continue  # Skip - JPL data unavailable for this view
```

### What the Visualization Shows

**Included:**
- Barycenter marker (diamond at origin)
- Orcus analytical orbit (dashed, inner, ~1,230 km radius)
- Vanth analytical orbit (dashed, outer, ~7,770 km radius)
- Face-on view (both orbits appear circular due to i=90 deg)
- Full scientific citations in hovertext

**Explicitly excluded (with explanation):**
- Position markers for Orcus and Vanth
- Actual orbit traces
- Animation of positions

### Hovertext Information

The osculating orbit hovertext now includes:

```
Orcus Barycentric Orbit
Epoch: 2026-01-08 (binary orbit)

Orbital radius: 0.0000083 AU (1240.1 km)
Period: 9.54 days
Eccentricity: ~0.007 (nearly circular)
Inclination: 90 deg (face-on from Earth)

Binary System - Highest Mass Ratio Known!
Mass ratio (Vanth/Orcus): 0.16 +/- 0.02
(Charon/Pluto is only 0.12)
Orcus orbits 13.7% of separation from barycenter
Barycenter is OUTSIDE Orcus surface (~455 km radius)!

ANALYTICAL ORBIT ONLY
JPL Horizons satellite solution defines Orcus PRIMARY
(ID 920090482) at the barycenter position, so real-time
position markers are unavailable for this view.

Data Source:
Brown & Butler 2023, Planetary Science Journal 4(10):193
'Masses and densities of dwarf planet satellites
measured with ALMA' (arXiv:2307.04848)
ALMA observations Oct/Nov 2016
```

### The Science Story

This visualization demonstrates **living science** - showing both what we know and the limits of our knowledge:

**What ALMA achieved:**
- Resolved the **wobble** of Orcus around the barycenter from 47 AU away (7 billion km!)
- Measured positions to milliarcsecond precision
- Determined the mass ratio to 12% precision
- Confirmed Vanth is likely an intact impactor from a giant collision

**What we're honest about:**
- JPL's ephemeris structure doesn't support this specific view
- Real-time positions aren't available for barycenter-centered visualization
- The orbit geometry is from published research, not live computation

**Why this matters:**
- Science is a process, not a finished product
- Showing uncertainties is more honest than false precision
- The data that exists is still remarkable!
- Someone seeing this might ask: "What observations could improve this?"

### Comparison: Pluto-Charon vs Orcus-Vanth

| Feature | Pluto-Charon | Orcus-Vanth |
|---------|--------------|-------------|
| JPL support | Full ephemeris | Satellite solution only |
| Query Pluto/Orcus relative to BC | Works (returns ~2,000 km offset) | Returns 0,0,0 |
| Query Charon/Vanth relative to BC | Works | Works |
| Real-time positions | Yes | No (Vanth only) |
| Visualization approach | Full JPL data | Analytical orbits |
| Mass ratio | 0.12 | **0.16** (higher!) |

### Files Modified

| File | Change |
|------|--------|
| `palomas_orrery.py` | Skip actual orbits and position markers for Orcus-Vanth BC mode |
| `idealized_orbits.py` | Enhanced hovertext with full citations and explanation |
| `constants_new.py` | ORCUS_VANTH_BINARY_PARAMS with ALMA-derived values |

### Console Output

```
[SYSTEM SCOPE] Center: Orcus-Vanth Barycenter, System: solar
[NORMAL MODE] Using dates_lists for plot_actual_orbits
[NORMAL MODE] Orcus: 51 dates from 2026-01-08 to 2026-02-05
[ORCUS-VANTH] Skipping actual orbit for Orcus - using analytical binary orbit only
[NORMAL MODE] Vanth: 51 dates from 2026-01-08 to 2026-02-05
[ORCUS-VANTH] Skipping actual orbit for Vanth - using analytical binary orbit only

[ORCUS BARYCENTER MODE] Orcus: using analytical binary orbit elements
  (NOTE: Binary orbit is face-on from Earth, i=90 deg to ecliptic)
  a=0.0000083 AU (1240.1 km from barycenter)
  i=90.00 deg (face-on!), Omega=0.00 deg, omega=0.00 deg
  [OK] Added Orcus orbit (center: Orcus-Vanth Barycenter)

[ORCUS BARYCENTER MODE] Vanth: using analytical binary orbit elements
  a=0.0000518 AU (7750.7 km from barycenter)
  [OK] Added Vanth orbit (center: Orcus-Vanth Barycenter)
```

### Key Citations

**Primary source for binary parameters:**
- Brown, M.E. & Butler, B.J. (2023). "Masses and densities of dwarf planet satellites measured with ALMA." *The Planetary Science Journal*, 4(10), 193. [arXiv:2307.04848](https://arxiv.org/abs/2307.04848)

**Earlier orbital determination:**
- Brown, M.E., Ragozzine, D., Stansberry, J., & Fraser, W.C. (2010). "The Size, Density, and Formation of the Orcus-Vanth System in the Kuiper Belt." *The Astronomical Journal*. [arXiv:0910.4784](https://arxiv.org/abs/0910.4784)

**Vanth diameter from stellar occultation:**
- Sickafoose, A.A. et al. (2019). "A stellar occultation by Vanth, a satellite of (90482) Orcus." *Icarus*, 319, 657-668.

### For Paloma

*"Orcus and Vanth are like a tiny version of Pluto and Charon, dancing around each other way out in the Kuiper Belt. But here's what's amazing: Vanth is actually heavier compared to Orcus than Charon is compared to Pluto! They're so close in size that they don't orbit around Orcus - they both orbit around an invisible point floating in space between them. Scientists used a giant telescope called ALMA to watch Orcus wobble back and forth, and from that wobble they figured out exactly how heavy both of them are. We can't show you exactly where they are right now (the computers don't have that information yet), but we CAN show you the shape of their dance - two circles, one small for Orcus, one bigger for Vanth, going around that invisible point together."*

---

## 24. Living Science Philosophy

### Science at the Edge

Paloma's Orrery deliberately shows the **edge of scientific knowledge**, not just polished results:

| Object | What We Show | What We're Honest About |
|--------|--------------|-------------------------|
| Inner planets | Full JPL ephemeris | Essentially perfect |
| Pluto system | Full JPL ephemeris | New Horizons revolutionized this |
| Orcus-Vanth BC | Analytical orbits only | JPL structure limitation |
| TNO moons | Analytical orbits | Arbitrary orbital phase |
| Planet 9 | Hypothetical shell | May not exist! |

**This is intentional.** Science communication often presents a false sense of certainty. By showing:
- Where data comes from (citations in hovertext)
- What limitations exist (explanatory notes)
- What's calculated vs measured

...we invite curiosity rather than passive acceptance.

### The Instagram Connection

When sharing these visualizations on Instagram (@palomas_orrery), we're not just showing pretty pictures - we're showing **the process of science**:

- "Here's what ALMA measured from 7 billion km away"
- "Here's what JPL's computers can and can't tell us"
- "Here's what scientists are still working on"

This turns viewers into participants. Someone might ask:
- "When's the next stellar occultation of Vanth?"
- "Could we get better data from James Webb?"
- "What would it take to visit this system?"

**That's the point.** Science is a conversation, not a lecture.

### Design Principles

1. **Show what we know** - Use the best available data
2. **Acknowledge what we don't** - Explicit notes on limitations
3. **Cite sources** - Let people dig deeper
4. **Invite questions** - Uncertainty is interesting, not embarrassing
5. **Update as science advances** - The orrery evolves with knowledge

---

*"We are living science here and sharing it."* - Tony, January 8, 2026

---

## Summary: The Complete TNO Moon Story (Updated)

1. **Problem discovered:** TNO moons plot at 38-43 AU instead of ~0.00006 AU
2. **Root cause identified:** Horizons returns heliocentric data, not parent-centered
3. **Solution implemented:** Analytical fallback with literature-sourced elements
4. **Enhancement attempted:** Vector subtraction to get real-time positions
5. **Enhancement failed:** API doesn't expose separate satellite vectors
6. **Barycenter mode added:** Orcus-Vanth system with analytical orbits only
7. **Philosophy articulated:** Living science - showing the edge of knowledge

**The orbit visualization is accurate. The limitations are documented. The science is shared.**

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*January 8, 2026*
```

---

## 3. UPDATED TABLE OF CONTENTS

Add to the main document's table of contents:

```markdown
## Table of Contents (Updated)

...existing sections 1-22...

23. Orcus-Vanth Barycenter System (January 8, 2026)
    - The "Anti-Pluto" Binary System
    - Binary Orbit Parameters
    - The JPL Horizons Challenge
    - Our Solution: Analytical Binary Orbits Only
    - What the Visualization Shows
    - The Science Story
    - Comparison: Pluto-Charon vs Orcus-Vanth
    - Key Citations
    - For Paloma

24. Living Science Philosophy
    - Science at the Edge
    - The Instagram Connection
    - Design Principles
```

---

*End of v2.1 Update Document*
