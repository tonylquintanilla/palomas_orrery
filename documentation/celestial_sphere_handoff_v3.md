# Celestial Sphere Star Background — Handoff v3
## Paloma's Orrery | Tony + Claude | April 13, 2026

---

## Status

**Piece 1 COMPLETE**: `star_sphere_builder.py` built, tested, generates JSON.
**Piece 2 COMPLETE**: Targeted changes integrated into `palomas_orrery.py`.
**Visual check PASSED**: Screenshot confirmed — stars, grid, zodiac labels all rendering.
**Refinement round COMPLETE**: Label density, tick markers, coordinate text box, marker convention.
**Renderer refactor COMPLETE**: All rendering code moved from orrery into `star_sphere_builder.py`.
**animate_objects integration COMPLETE**: Same function call, zero divergence risk.

---

## What We Built

A celestial sphere behind the solar system scene with four independent toggles:
- **Star Background**: ~288 stars at vmag <= 3.5 as uniform dots (size=1.0)
- **Star Names**: hover text showing SIMBAD designations (e.g. "* alf Ori")
- **Celestial Grid**: ecliptic, celestial equator, prime meridian, poles, zodiac labels
- **Labels**: dense hover labels on tick markers and zodiac constellation names

The sphere scales to `axis_range` — always fills the scene. Solar system objects
are completely unchanged. Stars are in ecliptic coordinates (the orrery's native frame).

---

## Design Decisions (Locked)

| Decision | Choice | Reason |
|----------|--------|--------|
| Sphere radius R | = abs(axis_range[1]) | Always fills the scene |
| Magnitude limit | vmag <= 3.5 | 288 stars, readable, not cluttered |
| Star marker size | 1.0 (uniform) | Backdrop, not feature. Tony's visual judgment |
| Star color | rgba(180, 195, 230, 0.55) | Faint blue-white, recedes behind solar system |
| Coordinate frame | Ecliptic J2000 | Matches orrery's native frame |
| Hover on stars | Off by default, toggle enables | Star Names sub-checkbox |
| Grid colors | Ecliptic=amber, Equator=teal, PM=gray | Distinct, low opacity |
| Zodiac labels | At 1.03R (slightly outside sphere) | Float above ecliptic circle at midpoints |
| Default state | All off | Preserves current behavior |
| JSON format | Indented (human-readable) | ~58 KB, readability over compression |
| Unicode in JSON | Yes (degree symbol) | Rendered by Plotly in browser, safe |
| Underscore trace names | _star_background, _ecliptic, etc. | Gallery Studio convention |
| Tick markers | + (cross) symbol | Marker convention: + for non-structural hover targets |
| Persistent tick labels | Quarters only (0/90/180/270 deg, 0h/6h/12h/18h) | Reduces clutter |
| Dense labels | Via customdata/hovertemplate on existing ticks | No duplicate markers |
| Zodiac dense labels | Separate + markers at midpoints (1.03R) | Different positions than ticks |
| Renderer location | `star_sphere_builder.py` | One file owns build + load + render |

---

## Architecture

### Files

| File | Status | Notes |
|------|--------|-------|
| `star_sphere_builder.py` | COMPLETE | Build script + cache loader + renderer |
| `star_data/star_sphere_vmag35.json` | COMPLETE (generated) | 58 KB static asset |
| `palomas_orrery.py` | COMPLETE (7 targeted changes) | Import + calls + toggle + GUI |

### star_sphere_builder.py — Dual Role

**Builder (offline, standalone):**
- `build_grid_data()` — generates all grid geometry as unit vectors
- `build_star_data()` — filters Hipparcos to vmag <= 3.5, converts to ecliptic
- `build_json()` — writes star_data/star_sphere_vmag35.json
- Run: `python star_sphere_builder.py`

**Renderer (runtime, imported by orrery):**
- `load_star_sphere_data()` — JSON cache loader (module-level cache)
- `add_celestial_sphere_traces(fig, axis_range, show_stars, show_names, show_grid, show_labels)` — all trace building
- Lazy-imports plotly so builder can run standalone without it
- Called identically by both `plot_objects` and `animate_objects` — zero parallel-pipeline divergence

### JSON Structure

```json
{
  "meta": {
    "vmag_limit": 3.5,
    "star_count": 288,
    "obliquity_deg": 23.4393,
    "coordinate_frame": "ecliptic_J2000",
    "source": "Hipparcos via VizieR VOT cache",
    "format": "[x, y, z, vmag, designation]"
  },
  "stars": [
    [-0.187, 0.747, -0.637, -1.44, "* alf CMa"],
    ...
  ],
  "grid": {
    "ecliptic": [[x,y,z], ...],              // 120 points, z=0 plane
    "equator": [[x,y,z], ...],               // 120 points, tilted 23.4 deg
    "prime_meridian": [[x,y,z], ...],         // 120 points (Tony's addition)
    "ecliptic_north_pole": [0, 0, 1],
    "ecliptic_south_pole": [0, 0, -1],
    "celestial_north_pole": [0, 0.398, 0.917],
    "celestial_south_pole": [0, -0.398, -0.917],
    "vernal_equinox": [1, 0, 0],
    "zodiac_labels": [{"x":..., "y":..., "z":..., "abbr":"ARI", "name":"Aries", "lon_deg":0}, ...],
    "degree_markers": [{"x":..., "y":..., "z":..., "deg":0, "label":"0°"}, ...],
    "equator_tick_markers": [{"x":..., "y":..., "z":..., "label":"0h"}, ...],
    "pm_tick_markers": [{"x":..., "y":..., "z":..., "label":"0°", "arc_deg":0.0}, ...],
    "ra_hour_markers": [{"x":..., "y":..., "z":..., "label":"RA 0h", "ra_h":0}, ...],
    "dec_degree_markers": [{"x":..., "y":..., "z":..., "label":"Dec 0° (VE)", "dec_deg":0}, ...]
  }
}
```

### GUI Layout

```
Celestial Sphere [LabelFrame]
  [ ] Star Background
      [ ] Star Names          (indented sub-checkbox)
  [ ] Celestial Grid
      [ ] Labels              (indented sub-checkbox)
```

### palomas_orrery.py Integration (7 targeted changes)

1. **Import** (~line 290): `from star_sphere_builder import add_celestial_sphere_traces`
   (replaces old `_star_sphere_cache` + `_load_star_sphere_data()`)
2. **IntVar** (~line 2381): `celestial_grid_labels_var = tk.IntVar(value=0)`
3. **plot_objects** (~line 5282): 6-line function call replaces ~180 lines of inline rendering
4. **plot_objects coord text** (~line 5552): Updated to reference visible grid elements
5. **animate_objects** (~line 7403): Same 6-line function call (inserted before layout update)
6. **animate_objects coord text** (~line 7444): Updated to match plot_objects
7. **GUI** (~line 8159): Labels sub-checkbox + updated Celestial Grid tooltip

---

## Marker Convention (NEW — Standing)

Standardized across the entire orrery:

| Symbol | Plotly name | Used for |
|--------|-----------|----------|
| Filled circle | `circle` | Major bodies (planets, minor planets, moons) |
| Open circle | `circle-open` | Minor bodies (asteroids) |
| Filled diamond | `diamond` | Comets |
| Open diamond | `diamond-open` | Spacecraft |
| Open square | `square-open` | Structural positions (Lagrange points) |
| + (cross) | `cross` | Non-structural hover targets (coordinate ticks, info markers) |
| Filled square | `square` | Not currently used |

All markers above usually carry hovertext. Circles for stars in the star background
are the exception — they are purely visual backdrop (hoverinfo='skip' unless Star Names is on).

---

## Two-Tier Label System

**Always visible (when Celestial Grid is on):**
- Three great circles (ecliptic, equator, prime meridian) as lines
- + tick markers at every 30 deg on all three circles
- Persistent text labels at quarters only (0°/90°/180°/270° or 0h/6h/12h/18h)
- VE marker (cross), pole abbreviations (NCP, SCP, NEP, SEP)

**Dense hover (when Labels sub-checkbox is also on):**
- All tick markers become hoverable (customdata shows degree/hour value)
- Zodiac constellation names at + markers slightly outside ecliptic (1.03R)
- Pole full names on hover ("North Celestial Pole (NCP)")

---

## Verified Data

- Unit vectors: all |r| = 1.000000 (within float precision)
- Ecliptic: exactly in z=0 plane
- Equator tilt: +/-0.397777 = +/-sin(23.4393 deg) -- correct
- Celestial north pole: (0, 0.398, 0.917) -- tilted from ecliptic pole by obliquity
- Vernal equinox: (1, 0, 0) -- X axis in ecliptic frame
- Star count: 288 at vmag <= 3.5
- All 288 stars matched to SIMBAD designations (0 fallbacks)
- Brightest: * alf CMa (Sirius, vmag -1.44)
- Faintest: * iot Cep (vmag 3.5)
- RA 0h = VE = (+1, 0, 0) -- confirmed
- RA 6h = (0, +0.9175, -0.3978) -- on tilted equator, confirmed
- Dec +90 = NCP = (0, +0.3978, +0.9175) -- confirmed
- Dec -90 = SCP = (0, -0.3978, -0.9175) -- confirmed

---

## Key Lessons from This Feature

- **Design before build**: the JSON spec conversation prevented rework.
  Each design round simplified rather than complicated.
- **The visual check is irreducible**: star marker size 2.0 looked fine in theory;
  Tony judged 1.0 on sight. Mode 5.
- **The astronomer's eye drives the feature**: RA/Dec markers, tick density, label hierarchy
  all emerged from Tony looking at the grid and knowing what he wanted to read off it.
- **Unicode is safe in JSON/Plotly context**: the ASCII rule applies to Python source files
  that touch the Windows console, not to data files rendered in the browser.
- **Prime meridian was Tony's addition**: not in the original handoff or the initial builder.
  Emerged during integration. The conversation is generative.
- **Two-tier labeling (always-visible quarters + optional dense)**: emerged from the tension
  between "I want to read coordinates" and "I don't want clutter." Checkbox solves it.
- **Marker convention formalized**: Tony's visual feedback on circle vs cross vs diamond
  drove a systematic marker vocabulary across the entire orrery. + for hover targets,
  circles reserved for celestial objects.
- **Refactor to reduce bloat**: Tony noticed ~180 lines duplicated across plot_objects and
  animate_objects. Moving rendering into star_sphere_builder.py eliminated the parallel
  pipeline and reduced orrery by ~350 lines net. The conversation caught the anti-pattern.
- **Reuse existing markers for hover**: instead of adding duplicate markers at the same
  position, make the tick markers carry hovertext via customdata. Fewer traces, cleaner.

---

## Phase 2+ (Deferred)

- Asterism lines (constellation stick figures)
- Additional magnitude presets (vmag 4.5 suburban, vmag 5.5 dark sky)
- Option C (observatory/sky dome view)

---

*Handoff v3: Refinement round complete. Builder + renderer unified. Marker convention established.*
