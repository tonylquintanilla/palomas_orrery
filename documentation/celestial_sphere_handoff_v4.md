# Celestial Sphere Star Background — Handoff v4
## Paloma's Orrery | Tony + Claude | April 14, 2026

---

## Status

**Piece 1 COMPLETE**: `star_sphere_builder.py` built, tested, generates JSON.
**Piece 2 COMPLETE**: Targeted changes integrated into `palomas_orrery.py`.
**Visual check PASSED**: Screenshot confirmed — stars, grid, zodiac labels all rendering.
**Refinement round COMPLETE**: Label density, tick markers, coordinate text box, marker convention.
**Renderer refactor COMPLETE**: All rendering code moved from orrery into `star_sphere_builder.py`.
**animate_objects integration COMPLETE**: Same function call, zero divergence risk.
**Constellation Names COMPLETE**: 60 constellations with persistent centroid labels.
**Asterism Lines REMOVED**: Code and data cleaned out. Deferred to Option C planetarium.

---

## What We Built

A celestial sphere behind the solar system scene with five toggles:
- **Star Background**: ~288 stars at vmag <= 3.5 as uniform dots (size=1.0)
- **Star Names**: hover text showing SIMBAD designations (e.g. "* alf Ori")
- **Constellation Names**: persistent text labels at brightness-weighted centroids
- **Celestial Grid**: ecliptic, celestial equator, prime meridian, poles, zodiac labels
- **Labels**: dense hover labels on tick markers and zodiac constellation names

The sphere scales to `axis_range` — always fills the scene. Solar system objects
are completely unchanged. Stars are in ecliptic coordinates (the orrery's native frame).

---

## Current GUI Layout

```
Celestial Sphere [LabelFrame]
  [ ] Star Background
      [ ] Star Names          (indented sub-checkbox)
      [ ] Constellation Names (indented sub-checkbox)
  [ ] Celestial Grid
      [ ] Labels              (indented sub-checkbox)
```

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
| JSON format | Indented (human-readable) | ~75 KB, readability over compression |
| Unicode in JSON | Yes (degree symbol) | Rendered by Plotly in browser, safe |
| Underscore trace names | _star_background, _ecliptic, etc. | Gallery Studio convention |
| Tick markers | + (cross) symbol | Marker convention: + for non-structural hover targets |
| Persistent tick labels | Quarters only (0/90/180/270 deg, 0h/6h/12h/18h) | Reduces clutter |
| Dense labels | Via customdata/hovertemplate on existing ticks | No duplicate markers |
| Zodiac dense labels | Separate + markers at midpoints (1.03R) | Different positions than ticks |
| Renderer location | `star_sphere_builder.py` | One file owns build + load + render |
| Constellation name markers | + at 1.03R, persistent text, faint blue-white | Same offset as zodiac labels |
| Constellation centroids | Brightness-weighted, parsed from SIMBAD designations | No HIP pair data needed |

---

## Architecture

### Files

| File | Status | Notes |
|------|--------|-------|
| `star_sphere_builder.py` | COMPLETE (1053 lines) | Build + cache loader + renderer |
| `star_data/star_sphere_vmag35.json` | COMPLETE (generated, 75 KB) | Stars + grid + constellations |
| `palomas_orrery.py` | COMPLETE (targeted changes) | Import + calls + toggles + GUI |

### star_sphere_builder.py — Current State (1053 lines)

**Builder (offline, standalone):**
- `build_grid_data()` — generates all grid geometry as unit vectors
- `build_star_data()` — filters Hipparcos to vmag <= 3.5, converts to ecliptic.
  Returns `(stars, hip_to_index)` tuple.
- `build_centroid_data()` — computes brightness-weighted centroids by parsing
  constellation abbreviations from SIMBAD designations (e.g. "* alf Ori" -> ORI).
  No HIP pair lookup needed — works purely from star designations.
- `build_json()` — writes star_data/star_sphere_vmag35.json
- Run: `python star_sphere_builder.py`

**Renderer (runtime, imported by orrery):**
- `load_star_sphere_data()` — JSON cache loader (module-level cache)
- `add_celestial_sphere_traces(fig, axis_range, show_stars, show_names,
   show_grid, show_labels, show_constellation_names)` — all trace building
- Lazy-imports plotly so builder can run standalone without it
- Called identically by both `plot_objects` and `animate_objects`

**Embedded Data:**
- `CONSTELLATION_NAMES` — 88 IAU constellation names (used by `build_centroid_data`)

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
    "ecliptic": [[x,y,z], ...],
    "equator": [[x,y,z], ...],
    "prime_meridian": [[x,y,z], ...],
    "ecliptic_north_pole": [0, 0, 1],
    "ecliptic_south_pole": [0, 0, -1],
    "celestial_north_pole": [0, 0.398, 0.917],
    "celestial_south_pole": [0, -0.398, -0.917],
    "vernal_equinox": [1, 0, 0],
    "zodiac_labels": [...],
    "degree_markers": [...],
    "equator_tick_markers": [...],
    "pm_tick_markers": [...],
    "ra_hour_markers": [...],
    "dec_degree_markers": [...]
  },
  "constellations": {
    "ORI": {"name": "Orion", "abbr": "ORI", "centroid": [x,y,z], "star_count": 8},
    ...
  }
}
```

### palomas_orrery.py Integration

1. **Import** (~line 290): `from star_sphere_builder import add_celestial_sphere_traces`
2. **IntVars** (~line 2356): `celestial_grid_labels_var`, `constellation_names_var`
3. **plot_objects** (~line 5259): Function call with 7 parameters.
   Trigger condition: `star_background_var or celestial_grid_var or constellation_names_var`
4. **animate_objects** (~line 7210): Same function call.
5. **GUI** (~line 7968+): Star Names and Constellation Names sub-checkboxes
   under Star Background. Labels sub-checkbox under Celestial Grid.

### Renderer Flow

The renderer handles the `not show_grid` case by rendering constellation names
before the early return (they don't depend on grid data). The `show_labels`
check wraps only the zodiac labels block, not the constellation names.

---

## Marker Convention (Standing)

| Symbol | Plotly name | Used for |
|--------|-----------|----------|
| Filled circle | `circle` | Major bodies (planets, minor planets, moons) |
| Open circle | `circle-open` | Minor bodies (asteroids) |
| Filled diamond | `diamond` | Comets |
| Open diamond | `diamond-open` | Spacecraft |
| Open square | `square-open` | Structural positions (Lagrange points) |
| + (cross) | `cross` | Non-structural hover targets (coordinate ticks, info markers) |
| Filled square | `square` | Not currently used |

---

## Two-Tier Label System

**Always visible (when Celestial Grid is on):**
- Three great circles (ecliptic, equator, prime meridian) as lines
- + tick markers at every 30 deg on all three circles
- Persistent text labels at quarters only (0/90/180/270 or 0h/6h/12h/18h)
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
- Constellation centroids: 60 constellations (parsed from SIMBAD designations)
- 28 constellations skipped (no stars brighter than vmag 3.5)

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
  drove a systematic marker vocabulary across the entire orrery.
- **Refactor to reduce bloat**: Tony noticed ~180 lines duplicated across plot_objects and
  animate_objects. Moving rendering into star_sphere_builder.py eliminated the parallel
  pipeline and reduced orrery by ~350 lines net.
- **Confabulated data is the dominant risk when embedding lookup tables from training
  knowledge.** The CONSTELLATION_LINES dictionary had plausible-looking HIP pairs that
  connected wrong stars. Verified by visual inspection of Orion — "this figure is
  unrecognizable." Always verify against source data.
- **Constellation names (centroids) provide the orientation value** without data source
  complexity. Asterism lines require ~400 extra stars from a new data source (HYG) —
  disproportionate complexity for the orrery's purpose.
- **Stay within the vision**: the orrery is the god's-eye heliocentric view. Duplicating
  Stellarium's observatory view isn't the point. The celestial sphere orients the user
  in the heliocentric frame — limited, good perspective, done.

---

## Deferred (Not Planned)

- Asterism lines (stick figures) — removed. Would need HYG database (~14MB CSV from
  codeberg.org/astronexus/hyg) for ~400 extra stars beyond vmag 3.5. Correct Stellarium
  topology data was parsed and verified (674 segments, 691 stars, all 88 constellations)
  from stellarium-skycultures western/index.json but not implemented. May revisit for
  Option C planetarium if ever built.
- Additional magnitude presets (vmag 4.5 suburban, vmag 5.5 dark sky)
- Option C (observatory/sky dome view)

---

*Handoff v4: Feature complete. 60 constellation names, 288 stars, coordinate grid.
Asterism code removed. Builder 1053 lines, JSON 75 KB. Within the vision.*
