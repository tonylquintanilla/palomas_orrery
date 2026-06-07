# ORBITAL_MECHANICS_README v1.7 Update

## Documentation Changes for Center Object Refactoring and Fly-To Camera Feature

**Date:** December 23, 2025  
**Version:** 1.7 (Center Object Refactoring, center_id Pattern & Fly-To Camera)

---

## 1. UPDATE HEADER

**Replace:**
```
**Last Updated:** December 12, 2025 (v1.6 - TNO Dual-ID System, JPL Limits & Satellite Interval Fix)  
```

**With:**
```
**Last Updated:** December 23, 2025 (v1.7 - Center Object Refactoring, center_id Pattern & Fly-To Camera)  
```

---

## 2. ADD NEW SECTION TO PART II (After Section 15 "The Satellite Interval Bug")

### Insert new sections:

```markdown
---

## 16. Horizons Center Body Rules: What Can Be a Coordinate Origin?

### The Discovery

While implementing dynamic center object selection, we discovered a fundamental JPL Horizons limitation:

**Only major bodies can be coordinate centers (observing sites) in Horizons.**

From the official documentation:
> "In some special cases, an asteroid or comet can be defined as a major body. An example might be a particular asteroid solution used for a spacecraft mission flyby or other historically 'fixed' purpose."

### The Rule: Numeric IDs Only

| ID Format | Example | Can Be Center? |
|-----------|---------|----------------|
| Numeric (planets) | `499` (Mars), `10` (Sun) | Yes |
| Numeric (moons) | `301` (Moon), `501` (Io) | Yes |
| Numeric (spacecraft) | `-61` (Juno), `-31` (Voyager 1) | Yes |
| Numeric (Lagrange points) | `31` (L1), `32` (L2) | Yes |
| Numeric (mission targets) | `2101955` (Bennu for OSIRIS-REx) | Yes |
| Designation (smallbodies) | `1999 RQ36`, `C/2025 N1` | **No** |

### Testing Confirmed

| Object | ID | id_type | Works as Center? |
|--------|-----|---------|------------------|
| Earth | `399` | None | Yes |
| Juno | `-61` | id | Yes |
| L1 | `31` | id | Yes |
| Bennu/OSIRIS | `2101955` | smallbody | Yes (numeric!) |
| 3I/ATLAS | `C/2025 N1` | smallbody | **No** (designation) |
| Makemake | `2005 FY9` | smallbody | **No** (designation) |

### Why Mission Targets Work

JPL creates special "major body" entries for spacecraft mission targets:

- **Bennu** (`2101955`) - OSIRIS-REx
- **Ryugu** (`2162173`) - Hayabusa2
- **Ceres** (`2000001`) - Dawn
- **Vesta** (`2000004`) - Dawn
- **Eros** (`2000433`) - NEAR Shoemaker
- **Itokawa** (`2025143`) - Hayabusa
- **Arrokoth** (`2486958`) - New Horizons
- **67P/Churyumov** (`90000699`) - Rosetta

These numeric IDs allow centering even though the objects are technically "smallbodies."

### Implementation

The center object dropdown is now built dynamically:

```python
def can_be_horizons_center(obj):
    """Check if object can be used as Horizons coordinate center."""
    excluded_object_types = {'hypothetical', 'exoplanet', 'exo_host_star', 
                             'exo_barycenter', 'exo_binary_star'}
    if obj.get('object_type') in excluded_object_types:
        return False
    
    # Has explicit center_id? Can be centered
    if obj.get('center_id'):
        return True
    
    # Otherwise check if main ID is numeric (negative allowed for spacecraft)
    obj_id = str(obj.get('id', ''))
    id_to_check = obj_id.lstrip('-')
    return id_to_check.isdigit()

center_options = [obj['name'] for obj in objects if can_be_horizons_center(obj)]
```

### For Paloma

*"NASA's space computer can only put you 'at' certain places to look around. You can stand on planets, moons, or even spacecraft like Voyager! But you can't stand on most asteroids or comets - unless NASA sent a mission there. When a spacecraft visits an asteroid, NASA makes a special entry so we CAN stand there and watch the spacecraft arrive!"*

---

## 17. The center_id Pattern: Dual Identity for Smallbodies

### The Problem

Some objects need BOTH:
1. **Designation ID** (`1999 RQ36`) - For plotting with best ephemeris coverage
2. **Numeric ID** (`2101955`) - For use as coordinate center

Previously, we created duplicate objects (Bennu vs Bennu/OSIRIS). This cluttered the interface.

### The Solution: center_id Field

Add an optional `center_id` field to objects that have numeric alternatives:

```python
{'name': 'Bennu', 
 'id': '1999 RQ36',           # Designation - used for normal plotting
 'id_type': 'smallbody',
 'center_id': '2101955',      # Numeric - used when this object is the center
 'mission_info': 'Horizons: 1999 RQ36. Studied by NASA OSIRIS-REx mission.',
 ...}
```

### How It Works

When determining the center ID for Horizons queries:

```python
# In plot_objects, animate_objects, update_orbit_paths:
center_id = center_object_info.get('center_id', center_object_info['id'])
```

This pattern:
- Uses `center_id` if present (numeric, works as center)
- Falls back to `id` otherwise (for objects that are already numeric)

### Code Locations Updated

Three places needed the `center_id` fallback:

| Line | Function | Purpose |
|------|----------|---------|
| 3621 | `update_orbit_paths()` | Orbit cache updates |
| 4139 | `plot_objects()` | Static plots |
| 5379 | `animate_objects()` | Animations |

### Objects with center_id Potential

Mission targets that could benefit from `center_id`:

| Object | Current ID | center_id | Mission |
|--------|-----------|-----------|---------|
| Bennu | `1999 RQ36` | `2101955` | OSIRIS-REx (done) |
| Ceres | `A801 AA` | `2000001` | Dawn |
| Vesta | `A807 FA` | `2000004` | Dawn |
| Eros | `A898 PA` | `2000433` | NEAR Shoemaker |
| Itokawa | `1998 SF36` | `2025143` | Hayabusa |
| Ryugu | `1999 JU3` | `2162173` | Hayabusa2 |
| Dinkinesh | `1999 VD57` | `2152830` | Lucy |
| Apophis | `2004 MN4` | `2099942` | OSIRIS-APEX (future) |

### Comparison: helio_id vs center_id

Two similar but opposite patterns:

| Field | Purpose | Direction |
|-------|---------|-----------|
| `helio_id` | Extended ephemeris for Sun-centered plots | Numeric -> Designation |
| `center_id` | Enable object as coordinate center | Designation -> Numeric |

Both solve JPL ID limitations but for different use cases.

### For Paloma

*"Bennu has two names in NASA's computer - like having a nickname and a formal name. When we want to see Bennu's path around the Sun, we use its nickname '1999 RQ36' because that has more data. But when we want to stand ON Bennu and watch OSIRIS-REx arrive, we use its formal number '2101955' because only numbered objects can be places you stand!"*

---

## 18. Fly-To Camera Feature: Zooming to Objects

### The Problem

Plotly's mouse wheel zoom is imprecise. To see small details on a distant object (like 3I/ATLAS at 2.4 AU), users had to scroll repeatedly and often overshot.

### The Solution

A "Fly To" dropdown that instantly repositions the camera near any plotted object.

### How It Works

```python
def add_fly_to_object_buttons(fig, positions, center_object_name='Sun', ...):
    # For each object:
    # 1. Calculate view radius based on distance
    view_radius = fly_distance + (distance_from_center * distance_scale_factor)
    
    # 2. Set axis ranges centered on target
    new_x_range = [target_pos[0] - view_radius, target_pos[0] + view_radius]
    new_y_range = [target_pos[1] - view_radius, target_pos[1] + view_radius]
    new_z_range = [target_pos[2] - view_radius, target_pos[2] + view_radius]
    
    # 3. Set camera with standard viewing angle
    button_args = {
        "scene.camera": {"eye": {"x": 1.5, "y": 1.5, "z": 1.2}, ...},
        "scene.xaxis.range": new_x_range,
        "scene.yaxis.range": new_y_range,
        "scene.zaxis.range": new_z_range,
        "scene.aspectmode": "cube",
        "scene.aspectratio": {"x": 1, "y": 1, "z": 1}
    }
```

### Key Insight

Plotly camera positioning uses **normalized coordinates relative to axis ranges**, not absolute AU. The solution isn't moving the camera closer - it's **changing the axis ranges** to zoom in on the target.

### Features

| Feature | Implementation |
|---------|----------------|
| Sorted by distance | Nearest objects first in dropdown |
| "Return to Full View" | First button restores original axis ranges |
| Cubic aspect | `aspectmode: "cube"` prevents distortion |
| Visual distinction | Yellow background, green text (vs blue "View from" dropdown) |

### Dropdown Appearance

```
[View +X axis (Aries) from Sun  v]  <- Existing: camera direction
[Fly to Mercury (0.39 AU)       v]  <- New: zoom to object
```

The two dropdowns serve different purposes:
- **View from**: Changes camera direction (where you look)
- **Fly to**: Changes zoom level (how close you are)

### Limitations Discovered

1. **Can't escape with Plotly reset** - Once axis ranges change, Plotly's "Reset camera" only resets within those ranges. Solution: "Return to Full View" button.

2. **Non-cubic viewport** - Browser windows are wider than tall, so the view looks stretched. The data is correct; it's just the viewport shape.

### For Paloma

*"The 'Fly To' button is like a magic telescope! Instead of slowly zooming with the mouse wheel and maybe going too far, you just pick an object from the list and - whoosh! - you're right there looking at it. And if you want to see everything again, just click 'Return to Full View' to zoom back out."*

---
```

---

## 3. ADD TO QUOTATIONS SECTION

**Add:**

```markdown
*"Only major bodies can be coordinate centers in Horizons."* - JPL Documentation
*"The magic is really just changing the axis ranges."* - Dec 23, 2025 (fly-to camera insight)
```

---

## 4. ADD TO "WHAT'S NEW" SECTION

**Add after v1.6 section:**

```markdown
---

## What's New in v1.7 (December 23, 2025)

### Center Object Selection Refactoring

Replaced hardcoded center object list with dynamic generation from the `objects` list.

**Rule discovered:** Only objects with numeric IDs can be Horizons coordinate centers:
- Planets, moons, spacecraft, Lagrange points: Yes
- Comets, asteroids with designation IDs: No
- Mission target asteroids with numeric IDs: Yes!

**Implementation:**
```python
def can_be_horizons_center(obj):
    if obj.get('center_id'):
        return True
    obj_id = str(obj.get('id', '')).lstrip('-')
    return id_to_check.isdigit()
```

### The center_id Pattern

New optional field for smallbodies that have numeric mission target IDs:

```python
{'name': 'Bennu', 'id': '1999 RQ36', 'center_id': '2101955', ...}
```

- `id`: Used for normal plotting (best ephemeris coverage)
- `center_id`: Used when object is the coordinate center

**Updated in 3 locations:** `plot_objects()`, `animate_objects()`, `update_orbit_paths()`

### Fly-To Camera Feature

New dropdown to instantly zoom to any plotted object.

**Key insight:** Plotly camera uses normalized coordinates. Zooming requires changing axis ranges, not camera position.

**Features:**
- Sorted by distance (nearest first)
- "Return to Full View" button to escape
- Cubic aspect ratio to prevent distortion

**File modified:** `visualization_utils.py` - added `add_fly_to_object_buttons()`

### Testing: Bennu/OSIRIS-REx

Validated the center_id pattern by centering on Bennu and viewing OSIRIS-REx approach:
- Static plot: Working
- Animation: Working (after fixing all 3 center_id locations)

### Lessons Documented

| Topic | Insight |
|-------|---------|
| Horizons centers | Only numeric IDs work - JPL creates special entries for mission targets |
| Dual-ID pattern | helio_id (plot coverage) vs center_id (centering capability) |
| Plotly zoom | Axis ranges control zoom, not camera distance |
| Dropdown escape | Need explicit "Return to Full View" - Plotly reset doesn't restore ranges |

---

**Focus areas:** Refactoring, new feature, documentation  
**Files modified:** `palomas_orrery.py`, `visualization_utils.py`  
**Educational value:** Explains JPL center body rules and Plotly camera mechanics  
**Quotable:** *"Only major bodies can be coordinate centers in Horizons."*

---
```

---

## 5. UPDATE VERSION HISTORY

**Add entry:**

```markdown
| 1.7 | Dec 23, 2025 | Center Object Refactoring, center_id Pattern & Fly-To Camera |
```

---

## Summary of Changes

| Section | Action |
|---------|--------|
| Header | Update to v1.7, Dec 23, 2025 |
| Part II, Section 16 | Add "Horizons Center Body Rules: What Can Be a Coordinate Origin?" |
| Part II, Section 17 | Add "The center_id Pattern: Dual Identity for Smallbodies" |
| Part II, Section 18 | Add "Fly-To Camera Feature: Zooming to Objects" |
| Quotations | Add JPL documentation quote and fly-to insight |
| What's New | Add v1.7 section |
| Version History | Add v1.7 entry |

---

*Document prepared by Claude for Tony's Paloma's Orrery project*  
*December 23, 2025*
