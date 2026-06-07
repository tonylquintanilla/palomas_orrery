# Session Handoff: Comet Additions & 3I/ATLAS Anti-tail
## February 24, 2026 (updated April 27, 2026)

---

## What Was Accomplished

### 1. Four New Comets Added (Inner Solar System, Feb 2026)

Added four comets currently active in the inner solar system. All entries complete across three files.

**Comets (discovery order):**

| Comet | ID | Period | Perihelion | Type |
|-------|-----|--------|-----------|------|
| 10P/Tempel 2 | `90000214` | 5.37 yr | Aug 2, 2026 at 1.42 AU | Jupiter-family |
| 24P/Schaumasse | `90000355` | 8.25 yr | Jan 8, 2026 at 1.18 AU | Jupiter-family |
| 88P/Howell | `90000897` | 5.5 yr | Mar 18, 2026 at 1.41 AU | Jupiter-family |
| C/2024 E1 Wierzchos | `C/2024 E1` | None (near-parabolic) | Jan 20, 2026 at 0.56 AU | Oort Cloud |

**Horizons ID fix (Feb 25):** Periodic comets `10P`, `24P`, `88P` are ambiguous -- Horizons has multiple epoch-specific records per designation (22 records for Tempel 2 alone). Switched to record numbers: `90000214` (2013 epoch), `90000355` (2021 epoch), `90000897` (2019 epoch). Each is the most recent apparition available.

**Files modified:**

- `celestial_objects.py` -- 4 new object entries. Tempel 2, Schaumasse, Howell at top of Comets section (discovery order). Wierzchos between NEOWISE and SWAN. Tony placed Wierzchos in the interstellar checkbutton section of the GUI (near-parabolic, Oort Cloud origin).
- `constants_new.py` -- Orbital periods in KNOWN_ORBITAL_PERIODS (Wierzchos = None), colors in color map, descriptions in descriptions block.
- `comet_visualization_shells.py` -- Nucleus sizes in COMET_NUCLEUS_SIZES, tail data in HISTORICAL_TAIL_DATA.
- `palomas_orrery.py` -- 4 new `tk.IntVar` declarations + 3 `create_comet_checkbutton` calls (Tempel 2, Schaumasse, Howell after NEOWISE). Wierzchos added by Tony as `create_interstellar_checkbutton` in the interstellar section.

**Status:** All files syntax-verified. Horizons IDs resolved. Ready to test with live Horizons data.

---

### 1b. Bug Fixes (Feb 25)

**Wierzchos multi-dust-tail** (`comet_visualization_shells.py`):
- APOD Feb 17, 2026 shows Wierzchos with 3 dust tails in a fan pattern + 1 narrow ion tail
- Added `dust_tail_count: 3` and `dust_tail_fan_angle: 40` to Wierzchos tail data
- Both call sites (~line 992 and ~1311) now check `dust_tail_count`
- When > 1: calls `create_comet_dust_tail` N times with fanned velocity vectors
- Edge tails: 60% length/brightness vs primary, perpendicular fan spread
- Default `dust_tail_count=1` -- all other comets unaffected

**Indentation fix** (`idealized_orbits.py`):
- `half_period_days = period_days / 2` was outside the `if period_days not in [None, 1e99]` guard
- Wierzchos has `period_days = None` (near-parabolic) -- crashed on aphelion date calculation
- Moved entire calculation block inside the guard (4-space indent)

---

### 2. 3I/ATLAS Anti-tail & Quad-jet Structure

Updated 3I/ATLAS with February 2026 observations and implemented visualization of its unique jet structure.

**New observations incorporated (comments + description updated):**
- Hubble Jan 7/14/22, 2026: Quad-jet structure (1 anti-tail + 3 mini-jets at 120 deg)
- Anti-tail: ~400,000 km sunward, tightly collimated 10:1, wobbles +/-20 deg with 7.2 hr period
- VLT polarimetry: 38% linear polarization (sub-micron silicates)
- SPHEREx Dec 2025: "Fully active" -- H2O, CO2, CO, organics
- Ni/Fe ratio converging toward solar values (3.2 -> 1.1)
- Opposition Jan 22, 2026 (0.69 deg alignment)
- Next: Jupiter flyby Mar 16, 2026 at 0.358 AU

**New data fields in HISTORICAL_TAIL_DATA['3I/ATLAS']:**
```python
'anti_tail_length_km': 400000,
'anti_tail_color': '#C0C0C8',       # Gray/faint silver
'anti_tail_collimation': 0.1,       # 10:1 length-to-width
'jet_count': 4,                     # Quad-jet (Hubble Jan 2026)
```

**New function: `create_comet_anti_tail()`**
- Renders dominant sunward jet (anti-tail) -- direction reversed from ion tail
- If `jet_count > 1`, renders mini-jets in perpendicular plane at equal angular spacing
- Mini-jets: 40% length, 60% brightness, fewer particles than dominant jet
- Triggered from `add_comet_tails_to_figure()` step 5 (between ion tail and sun indicator)
- Only activates for comets with `anti_tail_length_km > 0` -- inert for all others

**Visually verified:** Anti-tail and mini-jets visible when using "Fly to 3I/ATLAS" and zooming in. At orrery scale they're sub-pixel (physically accurate -- 400,000 km is tiny at AU scale).

---

### 3. Adaptive Grid for Fly-to Zoom

**Problem:** When using "Fly to" or manual zoom, grid lines disappear and axis labels are off-screen at the edge of the original bounding box.

**Solution in `visualization_utils.py`:**

New helper `_calculate_grid_dtick(axis_span)`:
- Picks clean round numbers (1, 2, 5 x 10^n) for ~6 gridlines across any span
- Works from 60 AU (full system) down to 0.003 AU (anti-tail scale)

Each Fly-to button now includes in its relayout args:
- `scene.xaxis.dtick` / `yaxis` / `zaxis` -- adaptive grid spacing
- `scene.xaxis.title` -- includes grid spacing in km when zoomed close
  - `< 0.01 AU dtick`: "X (AU) (grid: 299,196 km)"
  - `0.01-0.1 AU dtick`: "X (AU) (grid: 7.5M km)"
  - `> 0.1 AU dtick`: no suffix

"Return to Full View" restores original dtick and plain axis titles.

**Visually verified:** Grid lines with labels visible at all Fly-to zoom levels.

**Limitation:** Manual scroll-zoom doesn't trigger dtick update (Plotly 3D has no zoom callback). Fly-to is where it matters most.

---

## Files Delivered

| File | Changes |
|------|---------|
| `celestial_objects.py` | 4 new comet entries + 3 Horizons ID fixes (record numbers) |
| `constants_new.py` | Periods, colors, descriptions for 4 comets |
| `comet_visualization_shells.py` | Nucleus sizes, tail data, anti-tail function, 3I/ATLAS update, Wierzchos multi-dust-tail |
| `palomas_orrery.py` | 4 new tk.IntVar + checkbuttons |
| `visualization_utils.py` | Adaptive grid dtick for Fly-to |
| `idealized_orbits.py` | Indentation fix for near-parabolic objects |

---

## Comet Customization Architecture

The standard comet model (single dust tail + single ion tail + coma) now has extensible per-comet overrides. No central redesign needed -- each comet's unique features are added case-by-case as we design or revise individual comets.

**Customizations built so far:**

| Feature | Data Fields | Used By | Infrastructure |
|---------|------------|---------|----------------|
| Multi-dust-tail fan | `dust_tail_count`, `dust_tail_fan_angle` | Wierzchos | Loops `create_comet_dust_tail` with fanned vectors |
| Anti-tail (sunward jet) | `anti_tail_length_km`, `anti_tail_color`, `anti_tail_collimation` | 3I/ATLAS | `create_comet_anti_tail()` function |
| Quad-jet structure | `jet_count` | 3I/ATLAS | Mini-jets in perpendicular plane at equal spacing |

**Pattern for future comets:**
1. Add optional fields to that comet's `HISTORICAL_TAIL_DATA` entry
2. Extend the relevant call site(s) in `comet_visualization_shells.py` with a `.get()` check
3. Default values keep all other comets unchanged

**Candidates for future customization:**
- **De Cheseaux (C/1743 X1):** Six-tail fan (dust tails from differential radiation pressure, different from Wierzchos jets)
- **Activity asymmetry:** Some comets are more active post-perihelion -- could add `activity_peak_offset_days`
- **Outbursts:** Sudden brightness increases -- could add `outburst_dates` list with magnitude/coma changes
- **Unusual coma color:** Already supported via `coma_color` field
- **Disconnection events:** Ion tail detachment during solar wind disturbances

The philosophy: evolve the functions as each comet's story demands it. The infrastructure grows organically from real cases, not from anticipating every possibility.

---

## Not Yet Started / Next Session

### Mean Orbit Traces (see separate handoff: handoff_mean_orbit_traces.md)

New hidden-by-default trace showing mean orbital elements alongside osculating orbit. Perturbation assessment on hover. Single-file change in `idealized_orbits.py` -- architecture already separates mean (`ORIGINAL_planetary_params`) from osculating (`planetary_params`). Mode 6.

**Why it matters:** Wierzchos osculating orbit is invisible on Feb 25, 2026 (e=0.99999970, semi-major axis ~20,000 AU). Mean orbit (e=1.000053) is a clean hyperbola. The gap between them IS the perturbation story.

### Great Comet of 1744 (C/1743 X1) -- Comet de Cheseaux

Tony wants to add this historic comet. Key facts:

- **Designation:** C/1743 X1
- **Discovered:** Nov 29, 1743 by Jan de Munck; Dec 9 by Klinkenberg; Dec 13 by Cheseaux
- **Perihelion:** ~March 1, 1744 at 0.2 AU
- **Peak magnitude:** -7 (visible in daylight!)
- **Famous for:** SIX TAILS fanning out like a Japanese hand fan post-perihelion
- **Tail length:** ~90 degrees as seen from Southern Hemisphere
- **Orbit:** Assumed parabolic (long-period, possibly >100,000 years)
- **Chinese records:** Report audible sounds associated with the comet

**TODO:**
1. Check JPL Horizons availability for C/1743 X1
2. Add entries to celestial_objects.py, constants_new.py, comet_visualization_shells.py
3. Add to palomas_orrery.py GUI (interstellar/hyperbolic section -- similar to Ikeya-Seki placement)
4. Consider multi-tail visualization -- the anti-tail/jet infrastructure built for 3I/ATLAS could be the foundation for rendering the six-tail fan

**Design question:** The six tails are dust tails (not jets like 3I/ATLAS). They're in the orbital plane fanning anti-sunward, possibly from nucleus fragmentation or differential radiation pressure on different particle sizes. Different rendering approach than the quad-jet. Mode 5 territory.

---

## Technical Notes

- Periodic comets need epoch-specific record numbers in Horizons -- designation alone (10P, 24P) is ambiguous across apparitions. Use `90000XXX` format.
- Near-parabolic orbits (e very close to 1.0) have enormous semi-major axes that extend beyond plot range even when e < 1. The osculating orbit is technically there but visually meaningless.
- Osculating eccentricity fluctuates daily around mean elements due to planetary perturbations. For Wierzchos, e crosses from sub-1 to super-1 around Feb 25-26, 2026.
- All new comets use `'object_type': 'orbital'` (well-defined orbits in Horizons)
- Wierzchos period = None (near-parabolic, safer than encoding ~200,000 year outbound period)
- Anti-tail function uses `HISTORICAL_TAIL_DATA.get('jet_count', 1)` -- defaults to 1 (single anti-tail only) for any comet without the field
- The `_calculate_grid_dtick` function is prefixed with underscore (private helper, not part of public API)
- Adaptive grid also works at the second `add_fly_to_object_buttons` call site (line ~6788, same function)

---

*Session: Feb 24-25, 2026 | Mode: Targeted (existing code) + Agentic (new anti-tail function, multi-dust-tail)*


---

## Session Update: April 27, 2026

### 4. Hover Text Truncation Removed (`apsidal_markers.py`)

`mission_info` was hard-truncated at 300 characters with `...` in two functions:
- `add_closest_approach_marker()` -- closest plotted point hover text
- `add_encounter_marker()` -- spacecraft encounter hover text

PANSTARRS hover text was cut mid-word ("Earth closest approa..."). Removed the truncation in both spots -- full `mission_info` now flows through. Users can scroll the hover box as needed, consistent with all other hover text in the orrery.

### 5. Auto-Scaling Fix for Non-Sun Center Views (`palomas_orrery.py`)

**Bug:** When center is Earth (or any parent body in `parent_planets`), `calculate_axis_range_from_orbits()` found Moon as a child, computed Moon's apoapsis (0.00271 AU), multiplied by 1.5, and returned immediately -- never considering Sun, Mercury, Venus, or PANSTARRS at 0.49-1.46 AU. Result: 0.004 AU cube with nothing visible except Earth.

**Root cause:** The generic barycenter handler (line ~651) had an unconditional early return when `center_object_name in parent_planets`. Earth is in `parent_planets` because the Moon is its child, but this shouldn't lock the range to lunar orbit when non-child objects are selected.

**Fix:** Added a guard that checks whether ALL selected objects are children of the center. If any non-child object is selected (Sun, planets, comets, spacecraft), the children-based scaling is skipped and the general scaling logic takes over.

```python
selected_names = [obj['name'] for obj in selected_objects if obj['name'] != center_object_name]
has_non_children = any(name not in children for name in selected_names)
```

Affects both pipelines (both call `calculate_axis_range_from_orbits`). Also applies to Jupiter, Saturn, Mars, etc. when used as center with non-satellite objects selected.

**Secondary note:** `get_animation_axis_range()` still passes empty `{}` for positions, so the animation path uses heliocentric aphelions for planets instead of center-relative distances when falling through to general scaling. Objects are visible but range isn't perfectly optimized. Can address separately.

### 6. Comet Tail Direction Fix for Non-Sun Center Views

**Bug:** All three tail functions (`create_comet_dust_tail`, `create_comet_ion_tail`, `create_comet_anti_tail`) computed anti-sunward direction as `center_position / |center_position|` -- i.e., away from the coordinate origin. When center is Sun, origin IS the Sun, so this works. When center is Earth, tails point away from Earth instead of away from the Sun. Additionally, `distance_au` (used for feature visibility thresholds -- coma, tails) was computed as distance from center, not distance from Sun. Sublimation is solar-driven, so this gave wrong visibility decisions.

**Fix -- four layers:**

1. **`add_comet_tails_to_figure()`:** Added `sun_position=None` parameter. Computes `sun_rel = position - sun_position` for correct anti-sunward direction and Sun-relative distance. When `sun_position` is None or (0,0,0), behavior is unchanged (backward compatible).

2. **Three tail functions:** Each received `sun_relative_position=None` parameter. When provided, used for direction computation; `center_position` still used for particle rendering (positioning). Direction and rendering are now separated.

3. **`palomas_orrery.py` plot_objects caller:** Computes `_sun_pos_tuple` from `positions.get('Sun')` and passes as `sun_position`. Falls back to (0,0,0) if Sun not in positions.

4. **`palomas_orrery.py` animate_objects caller:** Same pattern using `positions_over_time.get('Sun')`.

Also fixed the inline anti-sun computation in the multi-dust-tail fan pattern (Wierzchos) to use `sun_rel`.

**Known remaining:** `create_sun_direction_indicator()` call (~line 1881 in comet_visualization_shells.py) still assumes origin = Sun for its small cosmetic arrow. Lower priority.

### Files Delivered (April 27, 2026)

| File | Changes |
|------|---------|
| `apsidal_markers.py` | Removed 300-char truncation in 2 functions |
| `palomas_orrery.py` | Auto-scaling guard + sun_position pass-through (2 callers) |
| `comet_visualization_shells.py` | sun_relative_position in 3 tail functions + coordinator + 7 call sites |

### Technical Notes (April 27, 2026)

- PANSTARRS (C/2025 R3) Earth-centered osculating elements show e=1,140,844 and a=-0.00000043 AU -- this is correct for a nearly-straight flyby hyperbola relative to Earth. The heliocentric orbit is barely hyperbolic (e just above 1.0 from Jupiter slingshot).
- The auto-scaling bug affected any parent body used as center (Earth, Jupiter, Saturn, Mars, Pluto, etc.) when non-satellite objects were also selected. Previously only satellite-only views (e.g. Earth+Moon, Jupiter+Galileans) would have given correct results.
- The comet tail direction bug was invisible in Sun-centered views (the common case) and only manifested when viewing from another body. The fix is backward-compatible: all existing Sun-centered behavior is unchanged.
- **Known behavior: duplicate Closest Plotted Point in portrait mode.** Trajectory objects get two CPP markers -- one from the Full Mission trace and one from the Plotted Period overlay -- both named "PANSTARRS Closest Plotted Point." When `show_legend: False` (portrait preset), Plotly.js deduplicates same-named traces and suppresses the first (Full Mission). The Plotted Period CPP survives -- it's the better trace anyway (carries `obj_info` / `mission_info` in hover text; the Full Mission CPP does not, because `plot_actual_orbits` line ~3381 doesn't pass `obj_info`). No fix needed: the informative trace wins. Does not occur in default/landscape presets where the legend is visible.

---

*Session: April 27, 2026 | Mode: Targeted (existing code) | Module updated: April 2026 with Anthropic's Claude Sonnet 4.6*
