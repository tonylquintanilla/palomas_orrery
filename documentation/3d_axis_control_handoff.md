# Handoff: 3D Axis Control (dtick + range)
## Paloma's Orrery | March 6, 2026 (updated)

---

## The Problem

Close-approach and flyby plots are currently unreadable because the axes
default to AU scale (~1 AU range, dtick=1) while all the interesting
geometry happens at ~0.001 AU. The Apophis screenshot is the canonical
example: grid lines only at the origin, no meaningful tick labels,
Earth/Moon/GEO/Apophis all clustered invisibly at the center.

This affects any Earth-centered view: Apophis perigee, Moon orbit,
GEO belt, LEO belt. The scale mismatch is 3 orders of magnitude.

---

## Status

### Part 1: Gallery Studio -- COMPLETE (March 6, 2026)

All Studio changes implemented, tested, and verified.

**What was built:**
- 4th column added to Studio layout (`col_3d`) for 3D Scene section
- `scene_axis_range` and `scene_dtick` config keys in DEFAULT_CONFIG,
  PORTRAIT_CONFIG, GUI widgets, `_collect_config()`, `apply_config()`,
  and `_apply_config_to_gui()`
- `apply_config()` range/dtick override with auto-dtick calculation
  (uses `_calculate_grid_dtick`) and km-equivalent suffix in axis titles
  for small scales (dtick < 0.01 shows km, < 0.1 shows millions of km)
- Fallback `_calculate_grid_dtick` inline if visualization_utils import fails
- 6-decimal precision entry fields with reference-value tooltips

**Tested at**: range=2 AU / dtick=0.25 AU (solar system scale) -- clean grid,
AU-only axis titles (km suffix correctly suppressed at this scale).

**Bug fixes discovered during Studio testing (also delivered):**
- Show axes not restoring: added `else` branch to set `visible: True`
  when show_axes is checked (source files with previously hidden axes
  stayed hidden -- pre-existing bug)
- Hover/routing matrix completely rewritten (see below)

---

### Part 2: Orrery GUI -- REMAINING

When the user generates a 3D orrery plot with a non-Sun center body
(Earth, Moon, Mars, etc.), the initial axis ranges should auto-fit to the
data extent, and dtick should be calculated from that range.

**Hook points confirmed (both call sites):**

Call site 1 (static plot, line ~5312):
```
plot_idealized_orbits()          # line 5133
_add_close_approach_extras()     # line 5148
[exoplanet stuff]                # line 5209
add_url_buttons()                # line 5314
>>> NEW: axis auto-fit HERE <<<  # BEFORE fly-to buttons
add_look_at_object_buttons()     # line 5317
add_fly_to_object_buttons()      # line 5319  (reads axis range for baseline)
```

Call site 2 (animation plot, line ~6971):
```
plot_idealized_orbits()          # line 6297
_add_close_approach_extras()     # line 6315
[exoplanet stuff]                # line 6348
add_hover_toggle_buttons()       # line 6972
>>> NEW: axis auto-fit HERE <<<  # BEFORE fly-to buttons
add_look_at_object_buttons()     # line 6975
add_fly_to_object_buttons()      # line 6977  (reads axis range for baseline)
```

**Auto-range logic:**

```python
# After all traces added, before fly-to buttons -- for non-Sun center views
if center_object_name != 'Sun':
    all_x, all_y, all_z = [], [], []
    for trace in fig.data:
        if hasattr(trace, 'x') and trace.x is not None:
            all_x.extend([v for v in trace.x if v is not None])
        if hasattr(trace, 'y') and trace.y is not None:
            all_y.extend([v for v in trace.y if v is not None])
        if hasattr(trace, 'z') and trace.z is not None:
            all_z.extend([v for v in trace.z if v is not None])

    if all_x and all_y and all_z:
        from visualization_utils import _calculate_grid_dtick
        max_extent = max(
            max(abs(v) for v in all_x),
            max(abs(v) for v in all_y),
            max(abs(v) for v in all_z)
        )
        # Cap at 1.5x farthest child orbit to exclude visitor trajectories
        # (e.g., Apophis's full heliocentric arc in an Earth-centered plot)
        # TODO: determine cap value from child objects, not raw data
        axis_range = [-max_extent * 1.1, max_extent * 1.1]
        axis_span = axis_range[1] - axis_range[0]
        dtick = _calculate_grid_dtick(axis_span)

        dtick_km = dtick * 149597870.7
        if dtick < 0.01:
            suffix = f" (grid: {dtick_km:,.0f} km)"
        elif dtick < 0.1:
            suffix = f" (grid: {dtick_km/1e6:.1f}M km)"
        else:
            suffix = ""

        fig.update_layout(scene=dict(
            xaxis=dict(range=axis_range, dtick=dtick,
                       title=f"X (AU){suffix}"),
            yaxis=dict(range=axis_range, dtick=dtick,
                       title=f"Y (AU){suffix}"),
            zaxis=dict(range=axis_range, dtick=dtick,
                       title=f"Z (AU){suffix}"),
        ))
        print(f"[AxisControl] Non-Sun center: range={axis_range[0]:.4f} to "
              f"{axis_range[1]:.4f} AU, dtick={dtick:.4f} AU ({dtick_km:,.0f} km)")
```

**Critical ordering:** This block MUST run BEFORE `add_fly_to_object_buttons()`
because that function reads `fig.layout.scene.xaxis.range` to save the
baseline for the "Return to Full View" button.

**Trace filtering (Issue #1):** Traces for visitor objects (e.g., Apophis
heliocentric arc) extend far beyond the center body's neighborhood. The
auto-range should cap at ~1.5x the farthest child object's orbit. Need to
determine which traces are children vs visitors -- check trace naming
conventions or metadata during implementation.

**Sun-centered guard:** `if center_object_name != 'Sun':` -- do NOT apply
to Sun-centered plots. Existing AU-scale handling is correct there.

---

## What Already Exists (Do Not Rebuild)

`visualization_utils.py` already contains `_calculate_grid_dtick(axis_span)`:

```python
def _calculate_grid_dtick(axis_span):
    """
    Aims for ~6 gridlines across the span using clean round numbers.
    Works from AU (full solar system) down to fractions of AU (close flyby).
    Returns: float dtick in AU
    """
    import math
    if axis_span <= 0:
        return 1.0
    raw_tick = axis_span / 6.0
    exponent = math.floor(math.log10(raw_tick))
    mantissa = raw_tick / (10 ** exponent)
    if mantissa < 1.5:   clean_mantissa = 1.0
    elif mantissa < 3.5: clean_mantissa = 2.0
    elif mantissa < 7.5: clean_mantissa = 5.0
    else:                clean_mantissa = 10.0
    return clean_mantissa * (10 ** exponent)
```

Already used by `add_fly_to_object_buttons()` and
`add_look_at_object_buttons()` for per-button axis scaling.

---

## Reference Values

Key distances for Apophis close approach plots (Earth center):

| Object | Distance from Earth center | AU |
|--------|---------------------------|-----|
| Earth surface | 6,371 km | 0.0000426 AU |
| LEO | ~400 km altitude = 6,771 km | 0.0000453 AU |
| GEO | 42,164 km | 0.000282 AU |
| Moon | ~384,400 km | 0.00257 AU |
| Apophis perigee (2029) | ~38,013 km | 0.000254 AU |

Suggested starting values for Apophis close approach view:
- `scene_axis_range`: 0.003 AU (shows Moon + Apophis + GEO in frame)
- `scene_dtick`: 0.0005 AU (~74,800 km per grid division)

For GEO-only view:
- `scene_axis_range`: 0.0005 AU
- `scene_dtick`: 0.0001 AU (~15,000 km per division)

**Km suffix trigger thresholds:**
- dtick < 0.01 AU: shows exact km (e.g., "grid: 74,799 km")
- dtick < 0.1 AU: shows millions of km (e.g., "grid: 14.96M km")
- dtick >= 0.1 AU: AU only (no km suffix)

---

## Known Issues / Watch Out For

1. **Auto-range vs visitor trajectories:** Cap at ~1.5x farthest child
   orbit. Need to identify child vs visitor traces during implementation.

2. **Fly-To button ordering:** Auto-fit MUST run before
   `add_fly_to_object_buttons()` which captures the baseline range.

3. **Return to Full View:** Captures whatever range is set at call time.
   If auto-fit is wrong, Return button is also wrong.

4. **Sun-centered plots:** Do NOT apply. Guard with
   `if center_object_name != 'Sun':`.

5. **Studio symmetric assumption:** Stores range as single positive value.
   Fine for origin-centered plots. Would lose asymmetry if any existed.

---

## Files to Touch (Remaining)

| File | Change |
|------|--------|
| `palomas_orrery.py` | Add auto-range/dtick block at both call sites (static ~5312, animation ~6971), guarded by non-Sun center |
| `visualization_utils.py` | No changes needed |
| `gallery_studio.py` | DONE -- no further changes |

---

## Success Criteria (Remaining)

- Apophis close approach plot: grid lines visible at ~0.001 AU spacing,
  Moon orbit fits in frame, Apophis trajectory arc visible
- GEO belt plot: ring visible with tick labels in AU and km equivalent
  in axis title
- Sun-centered plots: completely unchanged
- "Return to Full View" button target is correct after fly-to buttons added

---

*Created: March 5, 2026*
*Updated: March 6, 2026 -- Part 1 (Studio) complete, Part 2 (orrery GUI) remaining*
*Context: Protocol v3.13*
