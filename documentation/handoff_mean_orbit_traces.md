# Feature Handoff: Mean Orbit Traces
## February 25, 2026 | Mode 6 (Build + Teach)

---

## The Problem

When plotting Wierzchos (C/2024 E1) on Feb 25, 2026, the osculating Keplerian orbit is invisible. The osculating eccentricity is e=0.99999970 -- so close to parabolic that the semi-major axis is ~3 trillion km (~20,000 AU). The ellipse is technically there but extends far beyond any reasonable plot range.

By Feb 26, the osculating e crosses 1.0 and becomes hyperbolic. This happens because planetary perturbations (mainly Jupiter) shift the instantaneous orbital elements daily. The mean elements from JPL (e=1.000053) represent the stable long-term orbit.

This is educational: the difference between mean and osculating elements IS the perturbation story.

## The Feature

**New trace: "Mean Orbit"** for any object that has entries in `orbital_elements.py`.

### Behavior:
- Plotted from `orbital_elements.py` mean elements (JPL epoch solution)
- Defaults to **hidden** (like Keplerian Position), togglable via legend
- Works alongside the osculating orbit so you can visually compare
- Uses distinct line style (e.g., long-dash vs osculating's dot)
- Labeled: "{name} Mean Orbit (Epoch: {date})"

### Perturbation Assessment on Osculating Hover:
- Show delta on key elements: e, a, i
- Both quantitative and qualitative:
  - "Delta-e: -0.000054 (minimal perturbation)" 
  - "Delta-e: +0.15 (strong perturbation)"
- Qualitative thresholds TBD -- maybe: < 1% = minimal, 1-5% = moderate, > 5% = strong

### Scope: All Objects
- For most planets/moons, mean and osculating orbits will nearly overlap (educational: shows orbital stability)
- For perturbed objects (Wierzchos, Moon, trojans, near-Earth asteroids), the difference will be visible
- The Moon is an especially interesting case -- its osculating elements vary significantly

## Current Architecture

### Where mean elements live:
- `orbital_elements.py` -- `planetary_params` dictionary
- Already imported in `idealized_orbits.py` line 10: `from orbital_elements import planetary_params as ORIGINAL_planetary_params`
- Also imported line 28: `from orbital_elements import planetary_params, parent_planets, planet_tilts`

### Where osculating elements are used:
- `idealized_orbits.py` line 5053: `params = planetary_params[obj_name]`
- At this point, `planetary_params` has been updated with fresh osculating data from the pre-fetch in `palomas_orrery.py`
- The ORIGINAL import (`ORIGINAL_planetary_params`) preserves the mean elements!

### Key insight: The architecture already separates them!
- `ORIGINAL_planetary_params` = mean elements from `orbital_elements.py` (never modified)
- `planetary_params` = osculating elements (updated by pre-fetch each session)
- Both are already imported in `idealized_orbits.py`

### Rendering functions available:
- `generate_hyperbolic_orbit_points(a, e, i, omega, Omega, rotate_points)` -- for e > 1
- Regular elliptical orbit rendering -- for e < 1
- Both already work and are tested

## Implementation Plan

### Step 1: Add mean orbit trace (idealized_orbits.py)
After the existing osculating orbit is plotted (either elliptical or hyperbolic), check if `obj_name` is in `ORIGINAL_planetary_params`. If so:

1. Extract mean elements: a, e, i, omega, Omega from `ORIGINAL_planetary_params[obj_name]`
2. If mean e > 1: call `generate_hyperbolic_orbit_points()`
3. If mean e < 1: use existing elliptical orbit generation
4. Add trace with:
   - `visible='legendonly'` (hidden by default)
   - `line=dict(dash='longdash', width=1.5, color=color_map(obj_name))`
   - `name=f"{obj_name} Mean Orbit (Epoch: {epoch})"`

### Step 2: Add perturbation assessment to osculating hover text
Where the osculating orbit hover text is built, compare osculating vs mean elements:

```python
mean_params = ORIGINAL_planetary_params.get(obj_name, {})
if mean_params:
    mean_e = mean_params.get('e', e)
    delta_e = e - mean_e
    pct_e = abs(delta_e / mean_e * 100) if mean_e != 0 else 0
    
    if pct_e < 1:
        qual = "minimal perturbation"
    elif pct_e < 5:
        qual = "moderate perturbation"
    else:
        qual = "strong perturbation"
    
    perturbation_text = (
        f"<br><br><b>Perturbation (osculating vs mean):</b>"
        f"<br>Delta-e: {delta_e:+.6f} ({qual})"
        f"<br>Mean e: {mean_e:.6f} (Epoch: {mean_params.get('epoch', 'N/A')})"
    )
```

### Step 3: Handle edge cases
- Objects not in `ORIGINAL_planetary_params`: skip (no mean orbit available)
- Objects where mean and osculating are identical (first plot before pre-fetch updates): skip or note
- Near-parabolic objects where osculating e < 1 but mean e > 1 (like Wierzchos on Feb 25): this is the most educational case -- elliptical osculating vs hyperbolic mean
- Very long period objects (a = -10594 AU for Wierzchos): `generate_hyperbolic_orbit_points` already handles this with `max_distance` parameter

## Data Available in orbital_elements.py

Tony has already added Wierzchos mean elements:
```python
'Wierzchos': {
    'a': -10594.89311322137,        # Hyperbolic (negative a)
    'e': 1.000053413285714,         # Slightly hyperbolic
    'i': 75.23843302846508,
    'omega': 243.6365239065296,
    'Omega': 108.0828131320636,
    'epoch': '2025-Apr-19',
    'TP': 2461061.2622142192
}
```

Many other objects also have entries -- planets, moons, comets, asteroids, TNOs. The feature works for all of them.

## What This Session Discovered

The osculating eccentricity of Wierzchos evolves daily:
- Jan 20 (perihelion): e = 0.999907 (barely elliptical, huge but plottable)
- Jan 21: e = 0.999907 (minimum -- closest to circular)
- Feb 25: e = 0.999999704 (nearly parabolic, a ~ 20,000 AU, invisible)
- Feb 26: e = 1.000002 (crosses to hyperbolic!)
- Apr 30: e = 1.000088 (settling toward mean value of 1.000053)

The eccentricity will drop below 1 again by November 2027 as it leaves the planetary region. This is a textbook example of why mean elements matter.

## Files to Modify

| File | What |
|------|------|
| `idealized_orbits.py` | Add mean orbit trace after osculating orbit, add perturbation hover text |

That's it -- single file change. `ORIGINAL_planetary_params` is already imported.

## Educational Value

This feature teaches:
1. **Mean vs osculating elements** -- what they are and why they differ
2. **Perturbation effects** -- visible in the gap between the two orbits
3. **Near-parabolic sensitivity** -- tiny changes in e near 1.0 produce wildly different orbits
4. **Orbital stability** -- most planets show nearly identical mean/osculating (stable), while comets and Moon show significant differences (perturbed)

The Wierzchos case is especially compelling: on Feb 25, the osculating orbit says "giant ellipse" while the mean orbit says "hyperbola leaving the solar system." Same comet, same moment, two very different stories depending on which elements you use.

---

*Estimated scope: ~50-80 lines in idealized_orbits.py. Mode 6 recommended for educational documentation alongside implementation.*
