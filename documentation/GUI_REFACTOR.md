# Celestial Objects Module Integration Guide

## Overview

This refactor extracts the `objects` list (~1,070 lines) from `palomas_orrery.py` into a separate data module `celestial_objects.py`. 

**Benefits:**
- Cleaner separation of data and GUI code
- Easier to add/modify objects without touching GUI code
- Reduces palomas_orrery.py by ~1,070 lines
- Object data is now easily testable independently

## Files

1. **celestial_objects.py** - New module with object definitions
2. **palomas_orrery.py** - Needs modifications (see below)

## Integration Steps

### Step 1: Add celestial_objects.py to your project folder

Copy `celestial_objects.py` to the same directory as `palomas_orrery.py`.

### Step 2: Add import statement

Near the top of `palomas_orrery.py`, around line 38 (after other imports), add:

```python
from celestial_objects import OBJECT_DEFINITIONS, build_objects_list, get_all_var_names
```

### Step 3: Replace the objects list

Find and delete the entire `objects = [...]` block (lines 2559-3630).

Replace it with these ~5 lines:

```python
# Build vars_dict from all IntVar variables defined above
_var_names = get_all_var_names()
vars_dict = {name: globals()[name] for name in _var_names if name in globals()}

# Build objects list from definitions
objects = build_objects_list(OBJECT_DEFINITIONS, vars_dict, color_map)
```

## Verification

After making changes, verify the integration:

1. Run `palomas_orrery.py` - it should start normally
2. Check that all objects appear in the selection list
3. Test plotting a few objects to ensure colors and data are correct

## Rollback

If issues occur, simply:
1. Remove the new import line
2. Restore the original `objects = [...]` block from git or backup
3. Remove `celestial_objects.py` from the project folder

## Technical Notes

- The `build_objects_list()` function converts `var_name` strings to actual `tk.IntVar` references
- The `color_key` field is converted to actual colors via `color_map()`
- All other fields pass through unchanged
- The module has no tkinter dependency - it's pure data

## Future Improvements (Phase 2)

The checkbox UI generation (~800 lines) could also be data-driven using the same pattern. This would involve:
1. Adding `display` metadata to OBJECT_DEFINITIONS (bold, indent level, group)
2. Creating a `build_checkbox_ui()` function
3. Replacing manual checkbox creation with a loop

This is left for a future refactor if the current integration works well.
