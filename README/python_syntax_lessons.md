# Python Syntax Lessons
## Learning Python by Annotating Paloma's Orrery

*Tony working with Claude | Started January 23, 2026*

---

## Session 1: The Imports (January 23, 2026)

### What Are Libraries?

Libraries are **toolboxes other people built**. Instead of writing code to do math, create windows, or talk to NASA's servers, you *import* someone else's well-tested code and use it.

Without libraries, you'd write everything from scratch. With them, you stand on the shoulders of giants.

---

### Import Syntax Patterns

```python
import tkinter as tk          # Import whole library, give it a nickname
from tkinter import ttk       # Import just ONE thing from a library
import numpy as np            # Import whole library with nickname (np is universal convention)
import os                     # Import whole library, no nickname
import orbit_data_manager     # Import YOUR OWN module (a .py file you wrote)
```

**Why nicknames?** `tkinter.Button()` is tedious. `tk.Button()` is shorter.

---

### Packages, Subpackages, Classes, Instances

**The dot (`.`) means "go inside"** - navigating a hierarchy:

```
astroquery/                    # Package (folder)
    jplhorizons/               # Subpackage (subfolder)
        Horizons               # Class (blueprint for objects)
```

So `from astroquery.jplhorizons import Horizons` means:
1. Go into the `astroquery` package
2. Go into its `jplhorizons` subpackage  
3. Bring me the `Horizons` class

**Class vs Instance:**
- **Class** = blueprint (capitalized: `Horizons`, `Scatter3d`, `Time`)
- **Instance** = actual object built from blueprint

```python
# Horizons is the CLASS (blueprint)
# obj is an INSTANCE (actual object configured with your data)
obj = Horizons(id='499', location='500@0', epochs=2460000.5)
```

---

### The Core Imports Explained

#### GUI (Graphical User Interface)
```python
import tkinter as tk              # Python's built-in GUI toolkit
from tkinter import ttk           # "Themed" widgets - modern-looking elements
from tkinter import messagebox    # Pop-up dialog boxes
from tkinter import scrolledtext  # Text box with built-in scrollbar
```

#### Astronomy & Science
```python
from astroquery.jplhorizons import Horizons  # Queries NASA JPL - mission-grade ephemeris data
from astropy.time import Time                # Converts human dates to Julian Dates
from erfa import ErfaWarning                 # Warning type (so we can suppress it)
```

**Horizons** is the heart of the program. It talks to NASA's JPL system - the same ephemeris data used to navigate actual spacecraft. One import gives you access to positions of all planets, moons, asteroids, comets, and spacecraft.

**Time** is the bridge between human-readable dates and astronomical Julian Dates that Horizons requires.

#### Data & Math
```python
import numpy as np                # Fast math on arrays - foundation of scientific Python
from datetime import datetime     # A specific moment in time
from datetime import timedelta    # A duration - used for TIME STEPPING
```

**NumPy** operates on entire arrays at once. Instead of looping through 10,000 orbital positions, you do `distances = np.sqrt(x**2 + y**2 + z**2)` and it calculates all of them in one fast operation.

**timedelta** is critical for animation:
```python
current_time = datetime(2026, 1, 1)
step = timedelta(days=1)
current_time = current_time + step  # Now it's January 2nd
```

#### Visualization
```python
import plotly.graph_objs as go    # Interactive 3D plots - the orrery visualization
import webbrowser                 # Opens HTML files in browser
```

**Plotly** creates interactive 3D visualizations that output to HTML. Anyone can view them in a browser - no Python needed. The `go.Scatter3d` class draws points and lines in 3D space (orbits, planets, stars).

---

### The Data Flow

```
User picks date in GUI
        |
        v
datetime object (human-readable)
        |
        v
astropy Time object
        |
        v
.jd property (Julian Date)
        |
        v
Horizons query to NASA
        |
        v
Planetary positions (numpy arrays)
        |
        v
Plotly visualization (go.Scatter3d)
        |
        v
HTML file in browser
```

---

### Error Handling Pattern: try/except

```python
try:
    from erfa.core import ErfaWarning    # Try the NEW way first
except ImportError:
    from erfa import ErfaWarning          # If that fails, use OLD way
```

This is **defensive coding**:
1. Try your preferred approach
2. If it fails with a specific error, have a backup plan
3. Either way, keep going - don't crash

We use `except ImportError` (not bare `except`) to catch only "module not found" errors, not hide other bugs.

---

### Lessons Learned

1. **Libraries = other people's work you get for free** - one `import` inherits years of expertise

2. **Dot notation = hierarchy** - packages contain subpackages contain classes

3. **Classes are blueprints, instances are objects** - `Horizons` is the blueprint, `obj = Horizons(...)` creates an actual query object

4. **Convention matters** - `np` for numpy, `go` for graph_objs, `tk` for tkinter. Everyone uses these.

5. **Import order can matter** - warnings must be filtered before the code that triggers them loads

6. **Not your bug? Not your problem** - astropy's internal deprecation warnings are theirs to fix

---

## Session 2: Import Archaeology & Constants (January 24, 2026)

### VS Code Import Colors

VS Code tells you about import usage through colors:

| Color | Meaning |
|-------|---------|
| **Blue** | Definitely used in this file |
| **Yellow** | Uncertain - imported but can't confirm direct usage |
| **Grey** | Definitely NOT used in this file |

**Important:** Grey doesn't always mean "safe to delete"! The import might be:
- Passed to another function
- Used by another module that imports from this file
- Planned for future use
- Documentation of available capabilities

---

### Import Archaeology - Fossils Tell Stories

Unused imports often reveal the **evolution** of the codebase:

#### `import threading` (Grey - unused but kept)
```python
# CROSS-PLATFORM ISSUE: macOS Tkinter crashes if GUI updated from background threads!
# We DON'T use threading directly anymore.
# Instead: create_monitored_thread() from shutdown_handler.py wraps it safely.
# Kept as documentation of an important architectural decision.
```

#### `import time` (Grey - unused)
```python
# Low-level time functions (sleep, timestamps, benchmarking).
# NOT the same as datetime!
# Was used for rate-limiting during SIMBAD debugging.
# Now handled by simbad_manager.py - this import is a fossil.
```

#### `import subprocess` (Grey - unused)
```python
# Runs external programs from Python.
# HISTORICAL: palomas_orrery.py was once the ENTIRE application.
# When star_visualization split off, subprocess went with it.
# This marks the beginning of multi-module architecture.
```

#### `import math` (Grey - unused)
```python
# Python's built-in math (sqrt, sin, cos, pi).
# Works on ONE value at a time.
# SUPERSEDED by NumPy which works on entire arrays.
# Fossil from early development before full NumPy adoption.
```

#### `import shutil` (Grey - unused)
```python
# High-level file operations (copy, move, delete trees).
# Now used in orbit_data_manager.py for cache backup/recovery.
# Moved there when cache handling became its own module.
```

---

### Naming Conventions

Python naming tells you what something IS:

| Style | Meaning | Example |
|-------|---------|---------|
| `ALL_CAPS` | Constant - data that doesn't change | `KM_PER_AU = 149597870.7` |
| `lowercase_snake` | Function or variable | `def calculate_orbit():` |
| `CapitalizedWords` | Class (blueprint for objects) | `class Horizons:` |

Example import showing all three:
```python
from module import (
    PLANET_DATA,        # Data constant (ALL_CAPS)
    calculate_orbit,    # Function (lowercase)
    OrbitVisualizer     # Class (Capitalized)
)
```

---

### Module Imports - Refactoring in Progress

When you see mixed blue/grey in module imports, it often means **migration in progress**:

```python
from celestial_objects import (
    OBJECT_DEFINITIONS,      # Blue - USED
    build_objects_list,      # Blue - USED
    SHELL_DEFINITIONS,       # Grey - defined but not yet integrated
    build_shell_checkboxes   # Grey - Phase 2 planned
)
```

This shows intentional **incremental refactoring** - move code piece by piece, test as you go.

---

### traceback Module

```python
import traceback  # Captures detailed error information for debugging
```

When something crashes, `traceback` shows the trail of function calls:
```python
try:
    risky_operation()
except Exception as e:
    traceback.print_exc()  # Print full error trail
    error_details = traceback.format_exc()  # Or capture as string
```

Useful for GUI apps - log the error but keep running instead of crashing.

---

### copy Module

```python
import copy  # For making true copies of complex objects
```

**Critical distinction:**
```python
# WITHOUT deepcopy - both point to SAME data
list_b = list_a
list_b[0] = 999  # Also changes list_a!

# WITH deepcopy - completely independent copy
list_b = copy.deepcopy(list_a)
list_b[0] = 999  # list_a unchanged
```

Used in animation: each frame needs its own independent copy of trace data.

---

### Constants Module - Single Source of Truth

**Problem:** Same value defined in multiple files = inconsistency risk.

**Solution:** Centralize in `constants_new.py`:

```python
from constants_new import (
    # Unit conversions
    KM_PER_AU,                  # 149,597,870.7 km per AU
    LIGHT_MINUTES_PER_AU,       # 8.3167 light-minutes per AU
    
    # Solar structure
    SOLAR_RADIUS_AU,            # Sun's radius in AU
    CORE_AU,                    # Solar core radius
    CHROMOSPHERE_RADII,         # In solar radii
    
    # Heliosphere
    TERMINATION_SHOCK_AU,       # Where solar wind slows
    HELIOPAUSE_RADII,           # Edge of solar wind
    
    # Display
    DEFAULT_MARKER_SIZE,        # Consistent marker size (= 7)
    color_map,                  # Object colors
    
    # Data
    KNOWN_ORBITAL_PERIODS,      # 100+ objects' periods in days
    CENTER_BODY_RADII,          # Physical radii in km
    INFO,                       # Tooltip text for all objects
)
```

**Benefits:**
- One place to update values
- No inconsistency between files
- Documents where numbers come from
- Self-documenting code (`KM_PER_AU` vs magic number)

---

### Cleanup Accomplished

During this session, we consolidated constants:

| Before | After |
|--------|-------|
| `DEFAULT_MARKER_SIZE = 7` in palomas_orrery.py | Imported from constants_new.py |
| `DEFAULT_MARKER_SIZE = 6` in palomas_orrery_helpers.py | Imported from constants_new.py |
| `DEFAULT_MARKER_SIZE = 6` in constants_new.py | Changed to `= 7` (single source) |
| Solar constants scattered in main file | Moved to constants_new.py |
| Oort cloud constants in main file | Moved to constants_new.py |

---

### Initialization Code

After imports, before functions - environment setup:

```python
# Fix Windows console encoding for Unicode symbols
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')           # Set console to UTF-8
    sys.stdout.reconfigure(encoding='utf-8') # Python stdout
    sys.stderr.reconfigure(encoding='utf-8') # Python stderr

# Set working directory to script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Working directory set to: {os.getcwd()}", flush=True)
```

**Why Windows encoding fix?** Windows consoles use old encodings. Astronomical data has Unicode (degree symbols, Greek letters). Without the fix, printing "45deg" crashes.

**Why working directory?** The program might be launched from anywhere. This ensures it finds its data files (`data/orbit_paths.json`, etc.).

**Why `flush=True`?** Forces immediate print (no buffering). If program crashes, you still see the message.

---

### Identified for Future

- [ ] Cache architecture refactoring (documented, deferred - "if it ain't broke...")
- [ ] Finish `celestial_objects.py` migration (Earth shells still using old system)
- [ ] Clean up remaining unused imports (or keep as documentation)

---

## Sessions To Come

- [ ] Class definitions and `__init__`
- [ ] Function definitions and arguments
- [ ] The main GUI structure
- [ ] Event handling (buttons, menus)
- [ ] How visualization functions work

---

## Key Quotes

*"The conversation IS where the magic happens."*

*"Not your bug? Not your problem."* - On astropy's internal deprecation warnings

*"We may find out!"* - On keeping unused imports as archaeological clues

*"If it ain't broke, don't fix it."* - On deferring cache refactoring

*"Single source of truth."* - On consolidating constants

---

*Learning Python by understanding the code you've already written.*
