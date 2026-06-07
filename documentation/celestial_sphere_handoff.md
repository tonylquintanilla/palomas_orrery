# Celestial Sphere Star Background — Handoff v1
## Paloma's Orrery | Tony + Claude | March 30, 2026

---

## What We Are Building

A "Star Background" toggle in the existing orrery GUI that renders a static celestial sphere
behind the solar system scene. Stars sit at their real RA/Dec directions on a sphere scaled
to the current plot's axis range (grid cube distance). The solar system objects are completely
unchanged — the sphere is pure backdrop.

This is **Option B** from the design conversation: the heliocentric/god's-eye view, stars as
a fixed dome of directions, planets and other objects moving inside it. The ancient geocentric
celestial sphere, now with a modern center.

---

## Design Decisions (Locked)

| Decision | Choice | Reason |
|----------|--------|--------|
| Integration point | Toggle inside existing orrery | No scale problem — sphere scales to grid cube |
| Sphere radius R | = current axis_range magnitude | Always fills the scene, no fixed value needed |
| Magnitude limit | vmag ≤ 3.5 (Chicago sky) | ~170 stars, readable, not cluttered |
| Hover on stars | None (hoverinfo='skip') | Stars are backdrop; solar system is foreground |
| Star labels | Constellation region labels only, faint static text | Orientation, not identification |
| Asterisms | Phase 2, separate toggle | Clean incremental build |
| Solar system objects | Completely unchanged | No rescaling needed; sphere is cosmetic |
| Works from any center | Yes | Displacement within solar system is negligible vs R |
| Prebuilt asset | star_sphere_vmag35.json | One-time build, cached, loaded at runtime |

---

## Architecture

### Two-piece implementation

**Piece 1: `star_sphere_builder.py` (new, standalone script)**
- Runs once to build the static asset
- Reads Hipparcos/Gaia data via existing pipeline (same data as planetarium_apparent_magnitude.py)
- Filters to vmag ≤ 3.5
- Converts RA/Dec → unit vectors (XYZ on unit sphere)
- Serializes to `star_data/star_sphere_vmag35.json`
- Also builds constellation label positions (RA/Dec centroids for ~88 IAU constellations)
- Future: additional magnitude presets (vmag 4.5, 5.5) same script, different output files

**Piece 2: Star background toggle in `palomas_orrery.py` (targeted changes)**
- New `tk.IntVar`: `star_background_var`
- New checkbox in GUI (location TBD — near shell checkboxes or display options)
- In `plot_objects()`: if `star_background_var.get()`:
  - Load `star_sphere_vmag35.json` (cache in memory after first load)
  - Scale unit vectors by current `axis_range` magnitude
  - Add star scatter3d trace (silent, small markers, low opacity)
  - Add constellation label scatter3d trace (faint text, static)
- No changes to any existing trace generation

### Data flow

```
star_sphere_builder.py (one-time)
  → Hipparcos/Gaia via existing data_acquisition.py
  → filter vmag ≤ 3.5
  → RA/Dec → unit vectors
  → star_data/star_sphere_vmag35.json
      {
        "stars": [
          {"x": 0.123, "y": 0.456, "z": 0.789, "name": "Sirius", "vmag": -1.46},
          ...
        ],
        "constellation_labels": [
          {"x": 0.1, "y": 0.5, "z": 0.3, "label": "ORI"},
          ...
        ]
      }

palomas_orrery.py (runtime)
  → load JSON once, cache in module-level variable
  → scale unit vectors by axis_range at plot time
  → add as traces to existing fig
```

---

## Key Technical Points

### Sphere radius scaling
```python
# axis_range is already computed as [-max_range, max_range]
# R is just the magnitude of that
R = abs(axis_range[1])  # e.g. 35.0 AU for outer solar system view

# Scale precomputed unit vectors
star_x = [ux * R for ux in unit_x]
star_y = [uy * R for uy in unit_y]
star_z = [uz * R for uz in unit_z]
```

### RA/Dec → unit vector (same math as exoplanet_coordinates.py)
```python
import numpy as np
ra_rad = np.radians(ra_deg)
dec_rad = np.radians(dec_deg)
ux = np.cos(dec_rad) * np.cos(ra_rad)
uy = np.cos(dec_rad) * np.sin(ra_rad)
uz = np.sin(dec_rad)
# Store ux, uy, uz in JSON. R applied at render time.
```

### Star trace (silent backdrop)
```python
fig.add_trace(go.Scatter3d(
    x=star_x, y=star_y, z=star_z,
    mode='markers',
    marker=dict(
        size=star_sizes,       # scaled by vmag: brighter = larger
        color='rgba(200,210,255,0.6)',
        opacity=0.7
    ),
    hoverinfo='skip',
    showlegend=False,
    name='_star_background'    # underscore prefix = internal trace
))
```

### Constellation label trace (faint, static)
```python
fig.add_trace(go.Scatter3d(
    x=label_x, y=label_y, z=label_z,
    mode='text',
    text=label_names,          # e.g. ['ORI', 'SCO', 'UMA', ...]
    textfont=dict(color='rgba(100,120,160,0.4)', size=9),
    hoverinfo='skip',
    showlegend=False,
    name='_constellation_labels'
))
```

### Works from any center object
The star sphere is heliocentric by construction (unit vectors from Sun). For non-Sun center
objects, the displacement is negligible: even Sedna at ~500 AU is only 50% of a 1000 AU sphere
radius — and at vmag 3.5 scale (R = typical 30-50 AU for solar system views) the displacement
of any center object is a fraction of a percent. Constellation patterns are visually identical
from any solar system vantage point.

---

## Files Touched

| File | Change type | Notes |
|------|-------------|-------|
| `star_sphere_builder.py` | NEW | One-time build script |
| `star_data/star_sphere_vmag35.json` | NEW (generated) | Static asset, ~50KB |
| `palomas_orrery.py` | TARGETED | Toggle var + checkbox + trace injection in plot_objects() |

**Files NOT touched:**
- `planetarium_apparent_magnitude.py` — star data pipeline unchanged
- `visualization_utils.py` — no changes
- `earth_visualization_shells.py` — no changes
- All other modules — no changes

---

## Existing Infrastructure Reused

| What | Where | How used |
|------|-------|----------|
| Star RA/Dec data | `data_acquisition.py`, Hipparcos/Gaia VOT files | Builder reads existing cached VOT files |
| `radec_to_cartesian()` math | `exoplanet_coordinates.py` | Builder uses same formula |
| `calculate_axis_range_from_orbits()` | `palomas_orrery.py` line ~588 | Already computed; R = abs(axis_range[1]) |
| Shell checkbox pattern | `palomas_orrery.py` ~line 2769+ | Same IntVar + checkbox pattern |
| Underscore trace naming | Gallery Studio convention | `_star_background`, `_constellation_labels` |
| `star_data/` directory | Existing | JSON goes here alongside VOT files |

---

## GUI Placement (To Decide with Tony)

Options for checkbox location:
- Near existing shell checkboxes (consistent with "background elements" group)
- New "Display" section in the scrollable frame
- Bottom of the main checkbox area

Recommendation: near shells — conceptually it's another background/context layer.

---

## Phase 2 (Deferred)

- Asterism lines: static line traces connecting RA/Dec pairs per constellation
  (IAU standard line lists, small lookup table, same JSON cache approach)
- Additional magnitude presets: "Suburban sky" vmag 4.5, "Dark sky" vmag 5.5
- Option C (Observatory/sky dome view): separate design session after B is working

---

## Build Sequence

```
Session 1 (this session or next):
  1. Build star_sphere_builder.py
  2. Run it → generates star_sphere_vmag35.json
  3. Add toggle + traces to palomas_orrery.py
  4. Tony visual verification: does it look right?
  5. Iterate opacity/size if needed (Mode 5)

Session 2 (if desired):
  1. Add asterism lines (Phase 2)
  2. Visual check — do constellations read clearly?
```

---

## Open Questions (Non-blocking)

1. **Checkbox label**: "Star Background", "Celestial Sphere", "Sky Background"?
2. **Default state**: on or off? Recommendation: off (preserves current behavior)
3. **Opacity**: 0.6-0.7 is a starting guess — Tony judges visually
4. **Constellation label format**: 3-letter IAU codes (ORI, SCO) or full names (Orion, Scorpius)?
   Recommendation: 3-letter, less visual weight

---

*Handoff written before any code. Ready to build on verification.*
