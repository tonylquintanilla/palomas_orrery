# Celestial Sphere Star Background — Handoff v2
## Paloma's Orrery | Tony + Claude | April 12, 2026

---

## Status

**Piece 1 COMPLETE**: `star_sphere_builder.py` built, tested, generates JSON.
**Piece 2 COMPLETE**: Targeted changes integrated into `palomas_orrery.py`.
**Visual check PASSED**: Screenshot confirmed — stars, grid, zodiac labels all rendering.
**Refinement round in progress**: Label density, RA/Dec markers, coordinate text box.

---

## What We Built

A celestial sphere behind the solar system scene with three independent toggles:
- **Star Background**: ~288 stars at vmag <= 3.5 as uniform dots (size=1.0)
- **Star Names**: hover text showing SIMBAD designations (e.g. "* alf Ori")
- **Celestial Grid**: ecliptic, celestial equator, prime meridian, poles, zodiac labels

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
| Zodiac labels | At 1.03R (slightly outside sphere) | Float above ecliptic circle |
| Default state | All off | Preserves current behavior |
| JSON format | Indented (human-readable) | ~58 KB, readability over compression |
| Unicode in JSON | Yes (degree symbol) | Rendered by Plotly in browser, safe |
| Underscore trace names | _star_background, _ecliptic, etc. | Gallery Studio convention |

---

## Architecture

### Files

| File | Status | Notes |
|------|--------|-------|
| `star_sphere_builder.py` | COMPLETE | Standalone build script |
| `star_data/star_sphere_vmag35.json` | COMPLETE (generated) | 58 KB static asset |
| `palomas_orrery.py` | COMPLETE (4 targeted insertions) | Toggle + traces |

### JSON Structure (current)

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
    "ecliptic": [[x,y,z], ...],           // 120 points, z=0 plane
    "equator": [[x,y,z], ...],            // 120 points, tilted 23.4 deg
    "prime_meridian": [[x,y,z], ...],     // 120 points (Tony's addition)
    "ecliptic_north_pole": [0, 0, 1],
    "ecliptic_south_pole": [0, 0, -1],
    "celestial_north_pole": [0, 0.398, 0.917],
    "celestial_south_pole": [0, -0.398, -0.917],
    "vernal_equinox": [1, 0, 0],
    "zodiac_labels": [{"x":..., "y":..., "z":..., "abbr":"ARI", "name":"Aries", "lon_deg":0}, ...],
    "degree_markers": [{"x":..., "y":..., "z":..., "deg":0}, ...]
  }
}
```

### GUI Layout (current)

```
Celestial Sphere [LabelFrame]
  [ ] Star Background
      [ ] Star Names          (indented sub-checkbox)
  [ ] Celestial Grid
      [ ] Labels              (indented sub-checkbox) -- TO ADD
```

### palomas_orrery.py Integration Points

Four insertions (all additions, no modifications):

1. **Cache loader** (~before plot_objects): `_load_star_sphere_data()` with module-level cache
2. **IntVar declarations** (~line 2348): `star_background_var`, `star_names_var`, `celestial_grid_var`, `celestial_grid_labels_var` (TO ADD)
3. **Trace injection** (~line 5241 in plot_objects): star dots + grid circles + labels
4. **GUI checkboxes** (~line 8004): LabelFrame with checkboxes before Sun

---

## Next Session: Refinement Round

### 1. Zodiac label format change
**Current**: `"VIR 150deg"` (abbreviation + degrees)
**New**: Full names without degrees: `"Virgo"`
Degrees are already shown by the tick markers — no need to repeat them in the zodiac labels.
Change in: `star_sphere_builder.py` (zodiac_labels output) and `palomas_orrery.py` (label rendering)

### 2. Two-tier label system (grid labels checkbox)
**Always visible** (when Celestial Grid is on): circles + tick marks + select labels only
- Ecliptic: ticks every 30 deg, labels only at 0 deg, 90 deg, 180 deg, 270 deg
- Equator: ticks every 30 deg (= 2h), labels only at 0h, 6h, 12h, 18h
- Prime meridian: ticks every 30 deg, labels only at 0 deg, +/-90 deg (poles)

**Dense labels** (when Labels sub-checkbox is also on): display as hovertext not persistent text
- Ecliptic: all 12 zodiac constellation names (full names: "Aries", "Taurus", ...)
- Equator: RA labels every 2h (0h, 2h, 4h, ... 22h) -- 12 labels
- Prime meridian: Dec labels every 30 deg (0 deg, +/-30 deg, +/-60 deg, +/-90 deg) -- 7 labels
- Pole labels (NCP, SCP, NEP, SEP) -- spell out in hovertext

### 3. RA hour markers on celestial equator
New data in JSON: 12 labeled points along the equator at RA = 0h, 2h, 4h, ... 22h.
Builder computes equatorial positions, rotates to ecliptic frame (same math as equator circle).
Rendered as small tick markers with text labels.

### 4. Dec tick markers on prime meridian
New data in JSON: labeled points along the prime meridian at Dec = 0 deg, +/-30 deg, +/-60 deg, +/-90 deg.
Builder computes positions on the RA=0h meridian circle.
Rendered as small tick markers with text labels.

### 5. Unicode degree markers
Replace "deg" with degree symbol in JSON output:
- `"150deg"` becomes `"150°"`
- `"30deg"` becomes `"30°"`
- RA uses `"h"`: `"6h"`, `"12h"`
Safe because these strings are in JSON, rendered by Plotly in the browser. Never touch
the Windows console or Python source encoding.

### 6. Coordinate system text box update
Current text is abstract ("XY plane: Ecliptic, Earth's orbital plane").
New text should reference the visible grid elements:
```
Ecliptic coordinates (J2000)
Amber circle: Ecliptic (planet orbital plane)
Teal circle: Celestial equator (tilted 23.4 deg)
VE marker: Vernal equinox (+X direction, RA=0h): display on the zodiac circle
```
Shorter, connects words to what the user sees.
Change in: `palomas_orrery.py` coordinate system annotation.

### 7. New checkbox: Labels sub-checkbox under Celestial Grid
Add `celestial_grid_labels_var = tk.IntVar(value=0)` and corresponding checkbox.
Grid without Labels: circles + ticks + quarter labels (minimal).
Grid with Labels: adds all zodiac names, all RA hours, all Dec degrees, pole labels.

### 8. additional
- Integration in animate_objects and update the existing checkbutton hovertext accordingly now

---

## Builder Changes Needed (next session)

`star_sphere_builder.py` updates:

1. Add `ra_hour_markers` to grid data: 12 points on equator at 0h-22h
2. Add `dec_markers` to grid data: 7 points on prime meridian at 0 deg, +/-30, +/-60, +/-90
3. Change zodiac labels: `abbr` field unused; use `name` field (full names)
4. Separate quarter labels from dense labels in JSON structure:
   - `quarter_labels_ecliptic`: 4 labels at 0, 90, 180, 270
   - `quarter_labels_equator`: 4 labels at 0h, 6h, 12h, 18h
   - `quarter_labels_meridian`: 3 labels at 0 deg, +90 deg, -90 deg (or include +/-30, +/-60)
   - `dense_labels_zodiac`: 12 full constellation names
   - `dense_labels_ra`: 12 RA hour labels
   - `dense_labels_dec`: 7 Dec degree labels
5. Use Unicode degree symbol in all degree strings
6. Tick marks (small diamonds) at every 30 deg on all three circles -- always visible

### Orrery Changes Needed (next session)

`palomas_orrery.py` updates:

1. Add `celestial_grid_labels_var` IntVar
2. Add Labels sub-checkbox under Celestial Grid
3. Split grid trace rendering: always-visible (ticks + quarter labels) vs labels-enabled (dense)
4. Update coordinate system text box
5. Zodiac labels render full names from `name` field

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

---

## Key Lessons from This Session

- **Design before build**: the JSON spec conversation (star data, grid data, label hierarchy)
  prevented rework. Each design round simplified rather than complicated.
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

---

## Phase 2+ (Deferred)

- Asterism lines (constellation stick figures)
- Additional magnitude presets (vmag 4.5 suburban, vmag 5.5 dark sky)
- Option C (observatory/sky dome view)
- Coordinate system text box refinement (after grid labels are finalized)


---

*Handoff updated after successful build + visual check. Ready for refinement round.*
