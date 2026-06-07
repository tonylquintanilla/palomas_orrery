
---

# Phase 2: Shell Checkbox Refactor

## Overview

Phase 2 extracts shell checkbox definitions (87 checkboxes across 12 bodies) into data-driven generation.

**Savings:** ~458 lines of repetitive checkbox code

## New Data in celestial_objects.py

- `SHELL_DEFINITIONS` - Data for all 87 shell checkboxes across 12 bodies
- `get_shell_var_names()` - Returns all shell IntVar names
- `get_shell_tooltip_names()` - Returns all tooltip info names
- `build_shell_checkboxes()` - Builds shell checkboxes for one body

## Integration Steps

### Step 1: Update imports

Change your existing import to:
```python
from celestial_objects import (
    OBJECT_DEFINITIONS, build_objects_list, get_all_var_names,
    SHELL_DEFINITIONS, build_shell_checkboxes
)
```

### Step 2: Replace shell checkbox blocks

For each body, **delete the lines shown** and **add one line** after the `create_celestial_checkbutton` call.

**IMPORTANT:** Work bottom-up (Planet 9 first, Mercury last) so line numbers don't shift!

| Body | Keep This Line | Delete Lines | Replace With |
|------|----------------|--------------|--------------|
| Planet 9 | 7708 | 7709-7721 (13 lines) | `build_shell_checkboxes('Planet 9', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Eris | 7669 | 7670-7697 (28 lines) | `build_shell_checkboxes('Eris', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Pluto | 7601 | 7602-7635 (34 lines) | `build_shell_checkboxes('Pluto', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Neptune | 7553 | 7554-7596 (43 lines) | `build_shell_checkboxes('Neptune', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Uranus | 7500 | 7501-7544 (44 lines) | `build_shell_checkboxes('Uranus', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Saturn | 7428 | 7429-7479 (51 lines) | `build_shell_checkboxes('Saturn', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Jupiter | 7366 | 7367-7417 (51 lines) | `build_shell_checkboxes('Jupiter', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Mars | 7310 | 7311-7345 (35 lines) | `build_shell_checkboxes('Mars', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Moon | 7240 | 7241-7273 (33 lines) | `build_shell_checkboxes('Moon', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Earth | 7173 | 7174-7238 (65 lines) | `build_shell_checkboxes('Earth', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Venus | 7135 | 7136-7170 (35 lines) | `build_shell_checkboxes('Venus', celestial_frame, globals(), globals(), tk, CreateToolTip)` |
| Mercury | 7098 | 7099-7133 (35 lines) | `build_shell_checkboxes('Mercury', celestial_frame, globals(), globals(), tk, CreateToolTip)` |

### Example: Mercury

**Before (lines 8145-8181):**
```python
create_celestial_checkbutton("Mercury", mercury_var)    # params
# Create a Frame specifically for the mercury shell options (indented)
mercury_shell_options_frame = tk.Frame(celestial_frame)
mercury_shell_options_frame.pack(padx=(20, 0), anchor='w')  # Indent by 20 pixels
# mercury inner core shell
mercury_inner_core_checkbutton = tk.Checkbutton(mercury_shell_options_frame, text="-- Inner Core", variable=mercury_inner_core_var)
mercury_inner_core_checkbutton.pack(anchor='w')
CreateToolTip(mercury_inner_core_checkbutton, mercury_inner_core_info)
# ... 27 more lines ...
```

**After (2 lines):**
```python
create_celestial_checkbutton("Mercury", mercury_var)    # params
build_shell_checkboxes('Mercury', celestial_frame, globals(), globals(), tk, CreateToolTip)
```

## What's NOT Automated (by design)

- **Sun shells** - Complex multi-section structure with asteroid belts, Oort cloud, etc.
- **Section headers/labels** - The bold text labels between groups
- **Special checkboxes** - Items with commands (like `toggle_all_shells`)

## Line Reduction Summary

| Body | Lines Deleted | 
|------|---------------|
| Mercury | 35 |
| Venus | 35 |
| Earth | 65 |
| Moon | 33 |
| Mars | 35 |
| Jupiter | 51 |
| Saturn | 51 |
| Uranus | 44 |
| Neptune | 43 |
| Pluto | 34 |
| Eris | 28 |
| Planet 9 | 13 |
| **Total** | **467 lines** |

## Testing

After integration, verify:
1. All shell checkboxes appear correctly indented under each planet
2. Tooltips display correct information on hover
3. Checking shells works with plot_objects and animate_objects
4. Test at least: Mercury shells, Earth shells, Jupiter shells
