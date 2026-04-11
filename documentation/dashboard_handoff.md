# Dashboard Handoff
## Paloma's Orrery Dashboard -- `palomas_orrery_dashboard.py`
### Version 1.0 | March 30, 2026

---

## Purpose

Central launch point for the Paloma's Orrery suite. Replaces the
three individual batch files (`__run_palomas_orrery.bat`,
`_run_palomas_orrery_python.bat`, `_run_star_visualization_python.bat`)
with a single dashboard that shows all tools, resources, and
documentation in one place.

**Key benefits:**
- Launch multiple GUIs simultaneously (subprocess-based)
- Live subprocess output in the right-side status panel
- External links (GitHub, website, Instagram, YouTube) open in browser
- Local documentation opens with system default application
- Single batch file entry point: `_run_dashboard.bat`

---

## Architecture

### Layout: Two-Panel Design

```
+------------------------------------------+----------------+
|                                          |    Status      |
|  Header (logo, title, philosophy)        |    Panel       |
|                                          |  (fixed,       |
|  [SS] Solar System                       |   270px,       |
|    - Paloma's Orrery         [Launch]    |   always       |
|    - Orbital Construction    [Launch]    |   visible)     |
|                                          |                |
|  [ES] Earth System                       |  Shows live    |
|    - Earth System Viewer     [Launch]    |  subprocess    |
|    - Google Earth Controller [Launch]    |  output with   |
|    - Earth System Generator  [Launch]    |  timestamps    |
|                                          |  and script    |
|  [ST] Stars                              |  labels        |
|    - Star Visualization      [Launch]    |                |
|                                          |                |
|  [GW] Gallery & Web                      |                |
|    - Gallery Studio          [Launch]    |                |
|    - JSON Converter          [Launch]    |                |
|    - Gallery Editor          [Launch]    |                |
|                                          |                |
|  Resources                               |                |
|    External Links | Documentation        |                |
|                                          |                |
|  [Open Project Folder]                   |                |
|                                          |                |
|  Footer                                  |                |
+------------------------------------------+----------------+
  Left panel: scrollable                    Right: fixed
```

### File Structure

| File | Role |
|------|------|
| `palomas_orrery_dashboard.py` | Dashboard application (~690 lines) |
| `_run_dashboard.bat` | Windows launcher (auto-installs CustomTkinter) |
| `favicon.ico` | Brand icon (256x256 RGBA, used in titlebar + header) |

### Dependencies

- **CustomTkinter** (`pip install customtkinter`) -- modern Tkinter wrapper
- **Pillow** -- image handling for favicon display
- Both already in `requirements.txt`

---

## Configuration Block (Lines 24-151)

All editable configuration is front-loaded at the top of the file,
separated from the layout engine below. Tony can edit this block
without touching the class.

### Directory Paths

```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GALLERY_TOOLS_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io", "tools")
```

- `SCRIPT_DIR`: auto-resolved to wherever the dashboard lives (the orrery root)
- `GALLERY_TOOLS_DIR`: sibling directory for gallery tools
- Add more directory constants here if tools move to other locations

### LAUNCH_GROUPS

Dictionary of domain groups. Each entry is a tuple:

```python
(display_name, script_filename, description, [base_dir], [interactive])
```

- `base_dir`: optional, defaults to `SCRIPT_DIR`
- `interactive`: optional, `True` = opens in its own console window
  (for scripts that need terminal input, like `json_converter.py`)

**To add a new tool:**
```python
"New Group": [
    ("Tool Name",
     "tool_script.py",
     "One-line description"),
]
```

**To add a tool in a different directory:**
```python
("Tool Name",
 "tool_script.py",
 "Description",
 SOME_OTHER_DIR),
```

**To mark a tool as interactive (needs its own console):**
```python
("Tool Name",
 "tool_script.py",
 "Description",
 SOME_DIR,
 True),
```

### EXTERNAL_LINKS

List of `(display_name, url)` tuples. Empty URL hides the entry.
Opens in default browser.

### LOCAL_DOCS

List of `(display_name, filename)` tuples. Paths relative to
`SCRIPT_DIR`. Opens with system default application (VS Code for
`.md`/`.py` if file associations are set).

### SECTION_SYMBOLS

Optional bracketed labels before group headers. Set to `""` to hide.

### Colors and Fonts

All named constants. Change one value, it propagates everywhere.

```python
COLOR_ACCENT = "#d4a843"    # Gold accent (brand)
COLOR_BG = "#1a1a2e"        # Deep navy background
FONT_TITLE = ("Segoe UI", 28, "bold")
```

---

## Launch Mechanics

### Non-Interactive Tools (default)

- Launched with `python -u script.py` (`-u` = unbuffered stdout)
- stdout/stderr piped to status panel via background thread
- Uses `python.exe` (not `pythonw`) so output is capturable
- Each tool's output prefixed with `[script_name]` in status panel
- Exit code logged when process terminates

### Interactive Tools (`interactive=True`)

- Launched with `subprocess.CREATE_NEW_CONSOLE` on Windows
- Opens in its own cmd window for keyboard input
- Status panel logs "Launched in console: ..." but doesn't capture output
- Currently only `json_converter.py` uses this mode

### Debounce Guard

CustomTkinter on Windows can fire button commands twice per click.
A 1-second debounce guard in `_launch()` prevents duplicate process
spawns. The `_last_launch` dictionary tracks per-script timestamps.

### Output Pipeline

```
Subprocess stdout --> background thread (_read_output)
                      --> thread-safe queue (_output_queue)
                      --> main thread poll (_poll_output, 250ms interval)
                      --> status panel textbox (_log_status)
```

The threading/queue pattern avoids Tkinter's thread-safety constraints.
Background threads never touch GUI widgets directly; they only put
messages in the queue. The main thread drains the queue on a timer.

---

## Key Methods

| Method | Purpose |
|--------|---------|
| `_build_ui()` | Two-panel grid layout (left scrollable, right fixed) |
| `_build_header()` | Logo, title, philosophy, author |
| `_build_launch_section()` | Domain groups with launch cards |
| `_build_launch_card()` | Individual card: name + desc + Launch button |
| `_launch()` | Subprocess spawner (interactive vs piped) |
| `_read_output()` | Background thread: reads stdout lines into queue |
| `_poll_output()` | Main thread: drains queue to status panel (250ms) |
| `_log_status()` | Appends timestamped message to status textbox |
| `_build_status_panel()` | Right-side fixed panel with textbox |
| `_build_resources_section()` | External links + local docs (two columns) |
| `_open_document()` | Opens file with OS default (`os.startfile` on Win) |
| `_open_project_folder()` | Opens project dir in Explorer |
| `_build_footer()` | Credit line |

---

## Directory Layout on Tony's Machine

```
C:\Users\tonyq\OneDrive\Desktop\python_work\
  orrery\                          <-- SCRIPT_DIR
    palomas_orrery_dashboard.py
    _run_dashboard.bat
    favicon.ico
    palomas_orrery.py
    star_visualization_gui.py
    earth_system_visualization_gui.py
    earth_system_controller.py
    earth_system_generator.py
    orbital_param_viz.py
    README.md
    requirements.txt
    project_instructions_with_claude_ai.md
    web_gallery_handoff.md
    climate_data_preservation_handoff.md
    coordinate_system_guide.py
    ...

  tonyquintanilla.github.io\      <-- sibling repo
    tools\                         <-- GALLERY_TOOLS_DIR
      gallery_studio.py
      json_converter.py
      gallery_editor.py
```

---

## Known Issues & Lessons

1. **CTkButton double-fire on Windows**: CustomTkinter buttons can
   trigger their command callback twice per click on some Windows
   configurations. Fixed with a 1-second debounce guard in `_launch()`.
   If this reoccurs with a different symptom, check `_last_launch`.

2. **pythonw vs python for piped output**: `pythonw.exe` has no
   console, so stdout piping doesn't work reliably. Non-interactive
   launches use `python.exe` since we're capturing output ourselves.
   The subprocess window is hidden by the piping -- no visible console
   appears.

3. **Interactive tools can't pipe to status panel**: Scripts that
   need keyboard input (like `json_converter.py`) must open in their
   own console. The status panel only logs that they were launched,
   not their output. This is a fundamental constraint -- stdin requires
   a real terminal.

4. **Gallery tools in sibling directory**: Gallery tools live in
   `tonyquintanilla.github.io/tools/`, not in the orrery root. The
   `GALLERY_TOOLS_DIR` constant resolves this. The `cwd` for gallery
   tool subprocesses is set to `GALLERY_TOOLS_DIR` so their relative
   imports and file paths work correctly.

5. **Favicon loading**: The `.ico` file is loaded via Pillow and
   displayed as a 48x48 image in the header. `self.iconbitmap()` sets
   the Windows titlebar icon. Both fail silently if the file is missing
   -- the dashboard works fine without the favicon, just without the
   brand image.

6. **Font fallback**: Fonts are set to "Segoe UI" (Windows) and
   "Georgia" (philosophy line). On non-Windows systems these fall back
   to system defaults. The dashboard was designed for Windows but runs
   on any platform.

---

## Future Possibilities

- **Visual feedback on running state**: Change Launch button text to
  "Running" (or add a colored indicator) while a subprocess is active.
  The `_processes` dict already tracks PIDs -- just needs UI wiring.

- **Status panel clear button**: Long sessions accumulate output.
  A "Clear" button on the status panel header would reset the textbox.

- **Process management**: Stop/kill buttons for running subprocesses.
  The `_processes` dict has the `proc` objects with `.terminate()`.

- **Additional tool groups**: As the project grows, new domain groups
  can be added to `LAUNCH_GROUPS` with no code changes.

- **Status panel width**: Currently 270px. If output lines are too
  long to read, increase `STATUS_WIDTH` in `_build_status_panel()`.

---

## Design Decisions

| Question | Decision | Rationale |
|----------|----------|-----------|
| Platform | CustomTkinter | Professional look, Tkinter-compatible, low risk, one pip install |
| Layout | Two-panel (scroll + fixed) | Status always visible without scrolling |
| Grouping | By domain, not pipeline | Matches how Tony thinks about the project |
| Subprocess output | Piped to status panel | See what tools are doing without switching windows |
| Interactive tools | Own console window | stdin requires a real terminal |
| Config placement | Top of file | Tony can edit without touching layout engine |
| Batch files | Single `_run_dashboard.bat` | Replaces three separate launchers |

---

*"Is this what they call 'software engineering' as distinct from 'coding'?"*
-- Tony, after a zero-code design session, Mar 14, 2026
