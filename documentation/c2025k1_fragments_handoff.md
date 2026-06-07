# C/2025 K1 Fragment Implementation — Data Layer
## Handoff Document | March 21, 2026

---

## Summary

Add three comet fragment trajectory objects (B, C, D) for the breakup of C/2025 K1 (ATLAS). 
The parent record (C/2025 K1, Rec #90004912) IS Fragment A — it retains its full pre+post breakup 
arc with non-gravitational forces modeled. Fragments B, C, D have independent JPL orbital solutions.

### Key Science
- Breakup observed by Hubble ~Oct 16, 2025 (8 days post-perihelion at 0.33 AU)
- Fragment C (e=0.99999) is still gravitationally bound — siblings B and D escape
- Perihelion times nearly identical (Oct 8.44-8.46), divergence grows outbound
- Maximum convergence ~Nov 24 at ~70,000 km separation (less than half Earth-Moon distance)
- By Mar 2026, full spread A-to-D is ~910,000 km (0.006 AU)
- Published in Icarus, Feb 2026 (Auburn University, Hubble observations)

### Comet Structure Note
- Fragments should NOT get comet tail visualizations (they're small debris)
- Added `'show_tails': False` flag to each fragment entry
- The `is_comet` check in palomas_orrery.py (line ~5536) will need a guard:
  `is_comet = is_comet and obj.get('show_tails', True)`
- Sun-at-origin assumption in comet_visualization_shells.py confirmed (lines 490, 658, 799)
  - `center_object_name` is passed but never used (dead parameter)
  - Tails point wrong direction when center != Sun
  - Not a problem for this feature; logged for future fix

---

## Files Modified (3)

### 1. celestial_objects.py

**Change A: Update parent K1 mission_info (line 608)**

FIND:
```python
    'mission_info': 'Horizons: C/2025 K1. Retrograde. Hyperbolic. A notable comet for observation in late 2025. Retrograde (left-handed) orbit.', 
    'mission_url': 'https://theskylive.com/c2025k1-info'}, 
```

REPLACE WITH:
```python
    'mission_info': 'Horizons: C/2025 K1. Retrograde. Hyperbolic (e=1.00026). Perihelion Oct 8, 2025 at 0.33 AU. '
                    'Nucleus fragmented ~Oct 16 into at least 4 pieces (Hubble, published Icarus Feb 2026). '
                    'This record is Fragment A (main body, non-gravitational forces modeled). See K1-B, K1-C, K1-D.',
    'mission_url': 'https://theskylive.com/c2025k1-info'},
```

**Change B: Add three fragment entries (after line 609, before PANSTARRS)**

INSERT:
```python

    # C/2025 K1 FRAGMENTS - Hubble observed breakup ~Oct 16, 2025 (8 days post-perihelion)
    # Parent record (C/2025 K1, Rec #90004912) IS Fragment A - same SPK-ID, full arc with non-grav forces
    # Fragments B, C, D have independent orbital solutions starting from Nov 2025 observations
    # All four share nearly identical perihelion time (Oct 8.44-8.46) but diverge outbound
    # Fragment C is unique: e=0.99999 (bound!), while B and D are hyperbolic (escaping)
    # Convergence minimum ~Nov 24 (~70,000 km), then slow divergence outbound

    {'name': 'C/2025_K1-B', 'id': 'C/2025 K1-B', 'var_name': 'comet_2025k1b_var', 'color_key': 'C/2025_K1-B', 'symbol': 'diamond',
    # Rec #90004913, JPL#13, data arc: 2025-11-05 to 2026-01-06, 278 obs
    'object_type': 'trajectory', 'id_type': 'smallbody', 'show_tails': False,
    'mission_info': 'Horizons: C/2025 K1-B. Fragment B of comet C/2025 K1 (ATLAS). Hyperbolic (e=1.00203). '
                    'Breakup observed by Hubble ~Oct 16, 2025, 8 days post-perihelion. Escaping the solar system.',
    'mission_url': 'https://theskylive.com/c2025k1-info'},

    {'name': 'C/2025_K1-C', 'id': 'C/2025 K1-C', 'var_name': 'comet_2025k1c_var', 'color_key': 'C/2025_K1-C', 'symbol': 'diamond',
    # Rec #90004914, JPL#14, data arc: 2025-11-25 to 2026-01-10, 158 obs
    'object_type': 'trajectory', 'id_type': 'smallbody', 'show_tails': False,
    'mission_info': 'Horizons: C/2025 K1-C. Fragment C - the stubborn one. Elliptical (e=0.99999, still bound!). '
                    'While siblings escape, C remains gravitationally bound. Return period ~13 million years.',
    'mission_url': 'https://theskylive.com/c2025k1-info'},

    {'name': 'C/2025_K1-D', 'id': 'C/2025 K1-D', 'var_name': 'comet_2025k1d_var', 'color_key': 'C/2025_K1-D', 'symbol': 'diamond',
    # Rec #90004915, JPL#5, data arc: 2025-11-26 to 2025-12-29, 107 obs (shortest arc, 33 days)
    'object_type': 'trajectory', 'id_type': 'smallbody', 'show_tails': False,
    'mission_info': 'Horizons: C/2025 K1-D. Fragment D of comet C/2025 K1 (ATLAS). Hyperbolic (e=1.00246, most divergent). '
                    'Shortest observation arc (33 days). Escaping the solar system.',
    'mission_url': 'https://theskylive.com/c2025k1-info'},
```

---

### 2. constants_new.py

**Change A: Add fragment colors in color_map (after line 576)**

FIND:
```python
        'C/2025_K1': 'cyan',
        'Borisov': 'green',        
```

REPLACE WITH:
```python
        'C/2025_K1': 'cyan',
        'C/2025_K1-B': 'rgb(0, 200, 220)',         # Teal - darker cyan variant
        'C/2025_K1-C': 'rgb(255, 215, 0)',          # Gold - the bound fragment (special!)
        'C/2025_K1-D': 'rgb(100, 180, 255)',         # Sky blue - cooler variant
        'Borisov': 'green',        
```

**Change B: Add fragment orbital periods (after line 226)**

FIND:
```python
    'C/2025_K1': None,      # Hyperbolic comet - effectively infinite period
    'Borisov': None,        # Hyperbolic comet - effectively infinite period    
```

REPLACE WITH:
```python
    'C/2025_K1': None,      # Hyperbolic comet - effectively infinite period
    'C/2025_K1-B': None,    # Hyperbolic fragment - escaping solar system
    'C/2025_K1-C': None,    # Technically ~13M year period, effectively infinite
    'C/2025_K1-D': None,    # Hyperbolic fragment - escaping solar system
    'Borisov': None,        # Hyperbolic comet - effectively infinite period    
```

**Change C: Add fragment info text (after line 2112)**

FIND:
```python
        '* August: It will be faint (around magnitude 13) and visible only from the Southern Hemisphere through large telescopes.',
        
        'Borisov': 
```

REPLACE WITH:
```python
        '* August: It will be faint (around magnitude 13) and visible only from the Southern Hemisphere through large telescopes.',

        'C/2025_K1-B': 'Horizons: C/2025 K1-B. Fragment B of comet C/2025 K1 (ATLAS).\n'
        '* One of four fragments observed by Hubble Space Telescope in November 2025 (published Icarus, Feb 2026).\n'
        '* The breakup occurred ~October 16, 2025, approximately 8 days after perihelion at 0.33 AU.\n'
        '* Orbital characteristics: Hyperbolic (e=1.00203), escaping the solar system.\n'
        '* Perihelion: October 8.45, 2025, at 0.336 AU - nearly identical to parent.\n'
        '* No non-gravitational forces modeled (unlike parent Fragment A).\n'
        '* Data arc: 2025-11-05 to 2026-01-06 (278 observations, JPL solution #13).',

        'C/2025_K1-C': 'Horizons: C/2025 K1-C. Fragment C of comet C/2025 K1 (ATLAS) - the stubborn one.\n'
        '* The ONLY fragment that remains gravitationally bound to the Sun (e=0.99999).\n'
        '* While fragments A, B, and D escape the solar system on hyperbolic orbits,\n'
        '  Fragment C is on an extremely long-period elliptical orbit (~13 million years).\n'
        '* Its orbital elements are closest to the parent body, suggesting it may be\n'
        '  the most massive fragment or the one least affected by outgassing forces.\n'
        '* Perihelion: October 8.44, 2025, at 0.334 AU.\n'
        '* Chemically unusual: ground-based observations show extreme depletion of carbon-bearing species.\n'
        '* Data arc: 2025-11-25 to 2026-01-10 (158 observations, JPL solution #14).',

        'C/2025_K1-D': 'Horizons: C/2025 K1-D. Fragment D of comet C/2025 K1 (ATLAS).\n'
        '* The most divergent fragment - highest eccentricity (e=1.00246) of all four pieces.\n'
        '* Also the faintest and least observed, with the shortest data arc (33 days).\n'
        '* Perihelion: October 8.46, 2025, at 0.336 AU.\n'
        '* By March 2026, Fragment D leads the divergence at ~911,000 km from Fragment A.\n'
        '* No non-gravitational forces modeled.\n'
        '* Data arc: 2025-11-26 to 2025-12-29 (107 observations, JPL solution #5).',

        'Borisov': 
```

---

### 3. palomas_orrery.py

**Change: Guard comet tail visualization against show_tails flag (line ~5536)**

FIND:
```python
                    is_comet = (
                        obj.get('object_type') in ['orbital', 'trajectory'] and  # Allow both types
                        obj.get('id_type') == 'smallbody' and
                        obj.get('symbol') == 'diamond'
                    )
```

REPLACE WITH:
```python
                    is_comet = (
                        obj.get('object_type') in ['orbital', 'trajectory'] and  # Allow both types
                        obj.get('id_type') == 'smallbody' and
                        obj.get('symbol') == 'diamond' and
                        obj.get('show_tails', True)  # Fragments: show_tails=False suppresses tail viz
                    )
```

**ALSO: Same change in the animation path (line ~6816)**

FIND the second `is_comet` check (around line 6816-6821) and add the same `show_tails` guard.

---

## Verification Checklist

- [ ] All three fragments appear in object selection menu
- [ ] Fragments plot as trajectory traces with correct colors
- [ ] Parent K1 still works normally with comet tails
- [ ] Fragments do NOT generate comet tail visualizations
- [ ] Fragment C (gold) is visually distinct from B and D
- [ ] Horizons fetch succeeds for all three fragment IDs
- [ ] Info text displays correctly for each fragment
- [ ] No interference with existing comet visualizations

## Data Summary (from ephemeris analysis)

| Property | Parent/A | Fragment B | Fragment C | Fragment D |
|----------|----------|------------|------------|------------|
| SPK-ID | 90004912 | 90004913 | 90004914 | 90004915 |
| Horizons ID | C/2025 K1 | C/2025 K1-B | C/2025 K1-C | C/2025 K1-D |
| Eccentricity | 1.00026 | 1.00203 | 0.99999 | 1.00246 |
| QR (AU) | 0.3342 | 0.3358 | 0.3339 | 0.3363 |
| Tp | Oct 8.440 | Oct 8.452 | Oct 8.440 | Oct 8.455 |
| Non-grav (A1/A2/A3) | YES | no | no | no |
| Obs count | 2395 | 278 | 158 | 107 |
| Data arc | Apr 8 - Jan 10 | Nov 5 - Jan 6 | Nov 25 - Jan 10 | Nov 26 - Dec 29 |
| JPL soln | #31 | #13 | #14 | #5 |
| Bound? | Hyperbolic | Hyperbolic | **ELLIPTICAL** | Hyperbolic |
| Color | cyan | teal | **gold** | sky blue |

## Separation Timeline

| Date | B-A (km) | C-A (km) | D-A (km) |
|------|----------|----------|----------|
| Oct 7 (pre-perihelion) | 308,513 | 72,857 | 408,123 |
| Oct 8 (perihelion) | 282,993 | 67,049 | 374,456 |
| Nov 24 (min convergence) | 69,487 | 10,865 | 86,357 |
| Jan 15 | 310,379 | 47,806 | 386,927 |
| Mar 21 (today) | 729,588 | 111,322 | 910,797 |

## Future Work

- **UI grouping**: Fragment checkboxes subordinate to parent K1
- **Go: Breakup preset**: Frame the convergence/divergence at encounter scale
- **Comet structure sun-direction fix**: center_object_name is dead code in comet_visualization_shells.py
- **Hover text**: Fragment separation distances, eccentricity, bound/unbound status
- **Gallery piece**: The breakup story as a curated visualization
