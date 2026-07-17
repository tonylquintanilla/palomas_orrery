"""
Paloma's Orrery Dashboard
=========================
Central launch point for the Paloma's Orrery suite.

Project: Paloma's Orrery - Astronomical & Earth System Visualization
Author: Tony Quintanilla
Contact: tonyquintanilla@gmail.com

Philosophy: "Data Preservation is Climate Action"

AI Collaboration: Built with Claude (Anthropic) - conversational AI partnership

Updated 7/4/2026 with Opus 4.6

Classes:
    PalomasOrreryDashboardFrame - the dashboard UI as a ctk.CTkFrame. Takes
        a parent widget. Import this to embed the dashboard inside another
        Tkinter app (e.g. palomas_orrery.py's third GUI column).
    PalomasOrreryDashboard - standalone root window wrapper around
        PalomasOrreryDashboardFrame. Used when this file is run directly.

Module updated: July 2026 with Anthropic's Claude Sonnet 5.
July 2026: split the monolithic ctk.CTk dashboard into an embeddable
CTkFrame plus a thin standalone-window wrapper, so palomas_orrery.py can
import the dashboard into its own third GUI column without duplicating
the launch-card / status-log UI code.
July 2026: added Linux Button-4/5 wheel scrolling to match columns 1/2's
cross-platform coverage (CTkScrollableFrame's built-in handling only
covers Windows/Mac <MouseWheel>). Audited LAUNCH_GROUPS against both
repos at HEAD; added the 5 gallery_cache_builder-era tools from the
gallery repo's tools/ and 8 root-level devtools that were live but
unlisted.
"""

import os
import sys
import subprocess
import threading
import queue
import webbrowser
import customtkinter as ctk
from PIL import Image, ImageTk

# ============================================================
# CONFIGURATION
# ============================================================

# Resolve the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Gallery tools live in a sibling directory
GALLERY_TOOLS_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io", "tools")

# Window
WINDOW_TITLE = "Paloma's Orrery (palomas_orrery_dashboard.py)"
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720

# Colors - dark professional theme with gold accents
COLOR_BG = "#1a1a2e"           # Deep navy background
COLOR_SURFACE = "#16213e"       # Card surface
COLOR_SURFACE_HOVER = "#1a2744" # Card hover
COLOR_ACCENT = "#d4a843"        # Gold accent (brand)
COLOR_ACCENT_DIM = "#a68532"    # Dimmer gold
COLOR_TEXT = "#e8e8e8"          # Primary text
COLOR_TEXT_DIM = "#8899aa"      # Secondary text
COLOR_DIVIDER = "#2a3a5c"       # Subtle dividers
COLOR_BUTTON_BG = "#0f3460"     # Button background
COLOR_BUTTON_HOVER = "#1a4a7a"  # Button hover
COLOR_LINK = "#6ca0d4"          # Link color

# Fonts
FONT_TITLE = ("Segoe UI", 28, "bold")
FONT_SUBTITLE = ("Segoe UI", 13)
FONT_PHILOSOPHY = ("Georgia", 12, "italic")
FONT_SECTION = ("Segoe UI", 16, "bold")
FONT_BUTTON = ("Segoe UI", 13, "bold")
FONT_DESC = ("Segoe UI", 11)
FONT_LINK = ("Segoe UI", 11)
FONT_FOOTER = ("Segoe UI", 10)

# ============================================================
# LAUNCH TARGETS
# ============================================================
# Each entry: (display_name, script_filename, description,
#              [base_dir], [interactive])
# base_dir:    optional, defaults to SCRIPT_DIR
# interactive: optional, True = opens in its own console window
#              (for scripts that need terminal input)

LAUNCH_GROUPS = {
    "Solar System": [
        ("Paloma's Orrery",
         "palomas_orrery.py",
         "Interactive 3D solar system with comets, asteroids, and spacecraft"),
        ("Orbital Construction",
         "orbital_param_viz.py",
         "Visualize how orbital elements build an orbit"),
    ],
    "Earth System": [
        ("Earth System Viewer",
         "earth_system_visualization_gui.py",
         "Climate data visualization and planetary boundaries"),
        ("Google Earth Controller",
         "earth_system_controller.py",
         "Select and manage Google Earth KMZ layers"),
        ("Earth System Generator",
         "earth_system_generator.py",
         "Create new climate data layers and scenarios"),
        ("Food Insecurity Generator",
         "food_insecurity_generator.py",
         "Build the Sudan IPC food-insecurity KMZ layer "
         "(data/food_insecurity_sdn_blockbuster.kmz)"),
        ("Food Insecurity Controller",
         "earth_system_controller.py",
         "Launch the Food Insecurity KMZ family in Google Earth "
         "(preloads data/food_insecurity_*_blockbuster.kmz)",
         SCRIPT_DIR,
         False,
         ["--preload", "food_insecurity"]),
    ],
    "Stars": [
        ("Star Visualization",
         "star_visualization_gui.py",
         "HR diagrams, stellar neighborhoods, and the Milky Way"),
    ],

    "Gallery & Web": [
        ("Gallery Studio",
        "gallery_studio.py",
        "Curate and export plots for the web gallery",
        GALLERY_TOOLS_DIR),
        ("JSON Converter",
        "json_converter.py",
        "Convert HTML exports to gallery-ready JSON",
        GALLERY_TOOLS_DIR,
        True),  # interactive -- needs its own console
        ("Gallery Editor",
        "gallery_editor.py",
        "Edit gallery metadata, categories, and featured items",
        GALLERY_TOOLS_DIR),
        ("Gallery JSON Fixer",
        "gallery_json_fixer.py",
        "Fix older gallery JSON files for current viewer",
        GALLERY_TOOLS_DIR),
        ("Gallery Cache Builder",
        "gallery_cache_builder.py",
        "Nightly serving-cache builder (Phase 2 F1): fetch from Horizons, "
        "validate, atomic swap, commit. Needs flags -- opens a console so "
        "you can type --dry-run / --first-build / --nightly / --object etc.",
        GALLERY_TOOLS_DIR,
        True),
        ("Inspect Staging",
        "inspect_staging.py",
        "Read-only plain-language report on an existing dry-run staging "
        "folder. Takes one argument: the staging folder path printed at "
        "the end of a gallery_cache_builder.py --dry-run.",
        GALLERY_TOOLS_DIR,
        True),
        ("Debug Encke TP",
        "debug_encke_tp.py",
        "Run the exact live Horizons query the builder's fetch_solution_tp() "
        "makes for Encke and print the full raw response. No arguments.",
        GALLERY_TOOLS_DIR,
        True),
        ("Gallery Cleanup",
        "gallery_cleanup.py",
        "Find and (with confirmation) delete gallery JSON/KMZ files that "
        "aren't referenced by gallery_metadata.json, plus stray .json.bak files.",
        GALLERY_TOOLS_DIR,
        True),
        ("Gallery Builder Offline Tests",
        "test_gallery_cache_builder_offline.py",
        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network.",
        GALLERY_TOOLS_DIR,
        True),
    ],

    "Developer Tools": [
        ("Update Ledger Index",
         "ledger_index.py",
         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "
         "and migrate DONE items to section C. Run after editing any ledger block.",
         SCRIPT_DIR,
         True),
        ("Update Skill Manifest",
         "skills_index.py",
         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "
         "Run after adding, renaming, or versioning a skill.",
         SCRIPT_DIR,
         True),
        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True),
        ("Provenance Scanner",
         "provenance_scanner.py",
         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "
         "Run before/after edits to shared values, or when a value looks suspicious.",
         SCRIPT_DIR,
         True),
        ("Regenerate Module Atlas",
         "module_atlas.py",
         "Scan codebase, generate MODULE_ATLAS.md. "
         "Run after significant codebase changes (new modules, reorganizations).",
         SCRIPT_DIR,
         True),
        ("Dependency Trace",
         "dep_trace.py",
         "Map who depends on (and is consumed by) a module. "
         "Run before editing: python dep_trace.py <module_name> [hops]",
         SCRIPT_DIR,
         True),
        ("Animation HTML Tool",
         "measure_animation_html.py",
         "Measure a saved animation HTML: trace count, frame count, which traces "
         "are carried inside frames, and frames payload size. Run to compare a "
         "baseline against a patched export and quantify the frame-fence fix.",
         SCRIPT_DIR,
         True),
        ("Test Constants Provenance",
         "test_constants_provenance.py",
         "Pass/fail regression tests for constants_new.py. "
         "Run before committing changes to constants, or first if a plot looks wrong.",
         SCRIPT_DIR,
         True),
        ("Add Module Docstrings",
         "add_docstrings.py",
         "Add or improve module-level docstrings across the codebase; touches no code. "
         "Run after adding modules, before regenerating the Module Atlas.",
         SCRIPT_DIR,
         True),
        ("Verify Orbit Cache",
         "verify_orbit_cache.py",
         "Back up, validate, and repair orbit_paths.json, reporting any issues. "
         "Run if orbit plots look wrong or the cache may be corrupted.",
         SCRIPT_DIR,
         True),
        ("Test Orbit Cache",
         "test_orbit_cache.py",
         "Comprehensive test suite for orbit data caching, format conversion, "
         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",
         SCRIPT_DIR,
         True),
        ("Export Orbit Cache",
         "export_orbit_cache.py",
         "Phase 1b devtool: read the local orbit caches (read-only) and write "
         "web-servable orbit/position files for the interactive gallery.",
         SCRIPT_DIR,
         True),
        ("Test Reset Completeness",
         "test_reset_completeness.py",
         "Guard the Reset button against partial-reset drift: dirties every "
         "tracked control, calls the live reset handler, asserts everything "
         "returns to its startup default.",
         SCRIPT_DIR,
         True),
        ("Create Ephemeris Database",
         "create_ephemeris_database.py",
         "(Re)build satellite_ephemerides.json from idealized_orbits.py plus "
         "any downloaded Horizons ephemeris files.",
         SCRIPT_DIR,
         True),
        ("Climate Cache Manager",
         "climate_cache_manager.py",
         "Safely update the climate data caches, with validation and rollback.",
         SCRIPT_DIR,
         True),
        ("VOT Cache Manager",
         "vot_cache_manager.py",
         "Verify VizieR VOT cache file integrity.",
         SCRIPT_DIR,
         True),
        ("Osculating Cache Manager",
         "osculating_cache_manager.py",
         "Load and report on the osculating orbital elements cache "
         "(two-generation backup, always-prompt workflow).",
         SCRIPT_DIR,
         True),
        ("SIMBAD Query Manager",
         "simbad_manager.py",
         "Verify SIMBAD querying against a small sample of objects "
         "(rate limiting and retry logic).",
         SCRIPT_DIR,
         True),
    ],

}

# ============================================================
# EXTERNAL LINKS
# ============================================================
# (display_name, url)

EXTERNAL_LINKS = [
    ("palomasorrery.com", "https://palomasorrery.com"),
    ("GitHub", "https://github.com/tonylquintanilla/palomas_orrery"),
    ("Instagram", "https://www.instagram.com/palomas_orrery/"),
    ("YouTube", "https://www.youtube.com/@palomasorrery"),
    ("Google Drive", "https://drive.google.com/drive/folders/1hK0dBvFIx3rt0MFjkLbSqPBOvSYrharh"), 
    ("Horizons", "https://ssd.jpl.nasa.gov/horizons/app.html#/"),   
    ("Simbad", "https://simbad.u-strasbg.fr/simbad/"),
    ("Sky-Map", "https://www.wikisky.org/?locale=EN"),
    ("Sky View virtual telescope", "https://skyview.gsfc.nasa.gov/current/cgi/titlepage.pl"),  
    ("Copernicus", "https://climate.copernicus.eu/"), 
]

# ============================================================
# LOCAL DOCUMENTS
# ============================================================
# (display_name, filename_relative_to_SCRIPT_DIR)

LOCAL_DOCS = [
    ("README", "README.md"),
    ("Module Atlas", "MODULE_ATLAS.md"),
    ("Consolidated Ledger", "LEDGER_CONSOLIDATED.md"),
    ("Requirements", "requirements.txt"),
    ("Project Instructions", "PROJECT_INSTRUCTIONS.md"),
    ("Adding Objects Guide", "ADDING_OBJECTS_GUIDE.md"),
    ("Running a Patch File", "RUNNING_A_PATCH_FILE.md"),
    ("Color Reference", "Python_Color_Reference_v2.pdf"),    # or color_map.py    
]

# ============================================================
# SECTION ICONS (Unicode-free labels for group headers)
# ============================================================

SECTION_SYMBOLS = {
    "Solar System": "",
    "Earth System": "",
    "Stars": "",
    "Gallery & Web": "",
}


# ============================================================
# DASHBOARD APPLICATION
# ============================================================

class PalomasOrreryDashboardFrame(ctk.CTkFrame):
    """The dashboard UI, as an embeddable frame.

    Takes a parent widget (any Tkinter/CTk container) rather than being a
    root window itself. This is the class to import when embedding the
    dashboard inside another Tkinter app -- e.g.

        from palomas_orrery_dashboard import PalomasOrreryDashboardFrame
        panel = PalomasOrreryDashboardFrame(note_frame)
        panel.pack(expand=True, fill='both')

    Sets the global CTk appearance mode/theme itself on construction, so it
    renders correctly even when the host app never touches customtkinter
    (palomas_orrery.py's other GUI columns are plain tkinter and do not).
    """

    def __init__(self, parent, status_position="right", **kwargs):
        """
        status_position: "right" (default) -- status log as a fixed-width
            vertical panel beside the scrollable launch list. Matches the
            original 960px standalone design.
        status_position: "bottom" -- status log as a fixed-height
            horizontal strip below the launch list. Use this for narrow
            embeds (e.g. palomas_orrery.py's third GUI column).
        """
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        super().__init__(parent, fg_color=COLOR_BG, **kwargs)

        self._status_position = status_position

        # Load favicon as image for header display
        icon_path = os.path.join(SCRIPT_DIR, "favicon.ico")
        self._logo_image = None
        if os.path.exists(icon_path):
            try:
                pil_img = Image.open(icon_path)
                pil_img = pil_img.resize((48, 48), Image.LANCZOS)
                self._logo_image = ctk.CTkImage(
                    light_image=pil_img,
                    dark_image=pil_img,
                    size=(48, 48)
                )
            except Exception:
                pass

        # Track running processes
        self._processes = {}

        # Debounce guard: prevents double-fire from CTkButton
        self._last_launch = {}  # script -> timestamp

        # Thread-safe queue for subprocess output
        self._output_queue = queue.Queue()

        # Build UI
        self._build_ui()

        # Start polling the output queue (runs on main thread)
        self._poll_output()

    def _build_ui(self):
        """Construct the full dashboard layout.

        status_position="right" (default): horizontal split --
          Left  -- scrollable content (header, launch groups, resources, footer)
          Right -- fixed-width status panel (always visible, no scrolling needed)

        status_position="bottom": vertical stack --
          Top    -- scrollable content (same as above)
          Bottom -- fixed-height status strip (always visible)
        """

        self._outer_frame = ctk.CTkFrame(self, fg_color=COLOR_BG)
        self._outer_frame.pack(fill="both", expand=True)

        if self._status_position == "bottom":
            # Vertical stack: launch list on top, status strip below
            self._outer_frame.grid_rowconfigure(0, weight=1)    # top expands
            self._outer_frame.grid_rowconfigure(1, weight=0)    # bottom fixed
            self._outer_frame.grid_columnconfigure(0, weight=1)

            self._main_frame = ctk.CTkScrollableFrame(
                self._outer_frame,
                fg_color=COLOR_BG,
                scrollbar_button_color=COLOR_DIVIDER,
                scrollbar_button_hover_color=COLOR_ACCENT_DIM,
            )
            self._main_frame.grid(row=0, column=0, sticky="nsew")

            self._build_status_panel()
        else:
            # Horizontal split: launch list left, status panel right
            self._outer_frame.grid_columnconfigure(0, weight=1)   # left expands
            self._outer_frame.grid_columnconfigure(1, weight=0)   # right fixed
            self._outer_frame.grid_rowconfigure(0, weight=1)

            self._main_frame = ctk.CTkScrollableFrame(
                self._outer_frame,
                fg_color=COLOR_BG,
                scrollbar_button_color=COLOR_DIVIDER,
                scrollbar_button_hover_color=COLOR_ACCENT_DIM,
            )
            self._main_frame.grid(row=0, column=0, sticky="nsew")

            self._build_status_panel()

        # CTkScrollableFrame already binds <MouseWheel> globally (Windows/Mac)
        # with its own ancestor check (check_if_master_is_canvas), so wheel
        # scrolling over any card/button inside it already works there --
        # verified directly (measured pixel-for-pixel on a nested button).
        # What it does NOT bind is Linux's Button-4/Button-5, unlike columns
        # 1 and 2 in palomas_orrery.py, which explicitly support all three
        # platforms. Add that here, reusing the frame's own ancestor check
        # so this only fires for wheel events actually over this scrollable
        # area (not columns 1/2, and not the status panel).
        self._bind_linux_scroll(self._main_frame)

        # ---- SCROLLABLE PANEL CONTENTS (same either way) ----
        self._build_header()
        self._build_launch_section()
        self._build_resources_section()
        self._build_footer()

    def _bind_linux_scroll(self, scrollable_frame):
        """Add Button-4/Button-5 (Linux wheel) scrolling to a
        ctk.CTkScrollableFrame. Mirrors the platform branches already used
        for columns 1 and 2 in palomas_orrery.py's own mousewheel handlers.
        """
        canvas = scrollable_frame._parent_canvas

        def _on_linux_wheel(event):
            if not scrollable_frame.check_if_master_is_canvas(event.widget):
                return
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<Button-4>", _on_linux_wheel, add="+")
        canvas.bind_all("<Button-5>", _on_linux_wheel, add="+")

    # ----------------------------------------------------------
    # HEADER
    # ----------------------------------------------------------
    def _build_header(self):
        """Title bar with logo, project name, and philosophy."""
        header = ctk.CTkFrame(self._main_frame, fg_color=COLOR_SURFACE,
                              corner_radius=12)
        header.pack(fill="x", padx=20, pady=(20, 10))

        inner = ctk.CTkFrame(header, fg_color="transparent")
        inner.pack(padx=24, pady=20)

        # Logo + Title row
        title_row = ctk.CTkFrame(inner, fg_color="transparent")
        title_row.pack()

        if self._logo_image:
            logo_label = ctk.CTkLabel(title_row, image=self._logo_image,
                                      text="")
            logo_label.pack(side="left", padx=(0, 16))

        title_label = ctk.CTkLabel(
            title_row, text="Paloma's Orrery",
            font=FONT_TITLE, text_color=COLOR_ACCENT
        )
        title_label.pack(side="left")

        # Subtitle
        subtitle = ctk.CTkLabel(
            inner,
            text="Astronomical & Earth System Visualization Suite",
            font=FONT_SUBTITLE, text_color=COLOR_TEXT_DIM
        )
        subtitle.pack(pady=(6, 4))

        # Philosophy line
        philosophy = ctk.CTkLabel(
            inner,
            text='"Data Preservation is Climate Action"',
            font=FONT_PHILOSOPHY, text_color=COLOR_ACCENT_DIM
        )
        philosophy.pack(pady=(0, 4))

        # Author
        author = ctk.CTkLabel(
            inner,
            text="Tony Quintanilla",
            font=FONT_FOOTER, text_color=COLOR_TEXT_DIM
        )
        author.pack()

    # ----------------------------------------------------------
    # LAUNCH SECTION
    # ----------------------------------------------------------
    def _build_launch_section(self):
        """Four domain groups with launch buttons."""

        for group_name, entries in LAUNCH_GROUPS.items():
            # Section header
            section_frame = ctk.CTkFrame(self._main_frame,
                                         fg_color="transparent")
            section_frame.pack(fill="x", padx=20, pady=(16, 4))

            symbol = SECTION_SYMBOLS.get(group_name, "")
            ctk.CTkLabel(
                section_frame,
                text=f"{symbol}  {group_name}",
                font=FONT_SECTION, text_color=COLOR_TEXT,
                anchor="w"
            ).pack(side="left")

            # Developer Tools: remind the user which codebase directory
            # these tools should audit. Multiple copies of the repo exist
            # (sandbox, clean repo, Google Drive snapshots) and running
            # against the wrong one produces misleading results.
            if group_name == "Developer Tools":
                ctk.CTkLabel(
                    section_frame,
                    text=f"  Running from: {SCRIPT_DIR}",
                    font=FONT_DESC, text_color=COLOR_TEXT_DIM,
                    anchor="w"
                ).pack(side="left", padx=(8, 0))

            # Divider
            div = ctk.CTkFrame(self._main_frame, fg_color=COLOR_DIVIDER,
                               height=1)
            div.pack(fill="x", padx=20, pady=(0, 8))

            # Cards grid
            cards_frame = ctk.CTkFrame(self._main_frame,
                                       fg_color="transparent")
            cards_frame.pack(fill="x", padx=20, pady=(0, 4))

            for i, entry in enumerate(entries):
                name, script, desc = entry[0], entry[1], entry[2]
                base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR
                interactive = entry[4] if len(entry) > 4 else False
                args = entry[5] if len(entry) > 5 else None
                self._build_launch_card(cards_frame, name, script, desc,
                                        base_dir, interactive, args, i)

    def _build_launch_card(self, parent, name, script, desc, base_dir,
                           interactive, args, index):
        """Individual launch card with button and description."""
        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,
                            corner_radius=10)
        card.pack(fill="x", pady=4, ipady=6)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=8)

        # Left side: name + description
        text_frame = ctk.CTkFrame(inner, fg_color="transparent")
        text_frame.pack(side="left", fill="x", expand=True)

        ctk.CTkLabel(
            text_frame, text=name,
            font=FONT_BUTTON, text_color=COLOR_TEXT, anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame, text=desc,
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w"
        ).pack(anchor="w")

        # Right side: launch button
        script_path = os.path.join(base_dir, script)
        exists = os.path.exists(script_path)

        btn = ctk.CTkButton(
            inner,
            text="Launch" if exists else "Not Found",
            font=FONT_DESC,
            width=100,
            height=32,
            fg_color=COLOR_BUTTON_BG if exists else COLOR_DIVIDER,
            hover_color=COLOR_BUTTON_HOVER if exists else COLOR_DIVIDER,
            text_color=COLOR_TEXT if exists else COLOR_TEXT_DIM,
            corner_radius=8,
            command=lambda s=script, b=base_dir, ia=interactive, a=args: self._launch(s, b, ia, a),
            state="normal" if exists else "disabled"
        )
        btn.pack(side="right", padx=(12, 0))

    def _launch(self, script, base_dir=None, interactive=False, args=None):
        """Launch a Python script as a subprocess.

        Non-interactive: stdout/stderr piped to status panel.
        Interactive:      opens in its own console window.
        args:             optional CLI args appended to the script (e.g.
                          ["--preload", "food_insecurity"]). Tracking keys on
                          script+args so the same script launched in two modes
                          (generic vs preloaded controller) does not collide.
        """
        # Debounce: ignore if same script+args launched within 1 second
        import time
        now = time.time()
        launch_key = script if not args else script + " " + " ".join(args)
        if launch_key in self._last_launch and (now - self._last_launch[launch_key]) < 1.0:
            return
        self._last_launch[launch_key] = now

        if base_dir is None:
            base_dir = SCRIPT_DIR
        script_path = os.path.join(base_dir, script)
        if not os.path.exists(script_path):
            self._log_status(f"Not found: {script_path}")
            return

        # Short label for status messages (filename without .py)
        label = os.path.splitext(script)[0]
        if args:
            label = label + " [" + " ".join(args) + "]"

        try:
            python = sys.executable
            extra = list(args) if args else []

            if interactive:
                # ---- INTERACTIVE: open in its own console ----
                if sys.platform == "win32":
                    # cmd /k keeps the window open after script exits
                    proc = subprocess.Popen(
                        ["cmd", "/k", python, script_path] + extra,
                        cwd=base_dir,
                        creationflags=subprocess.CREATE_NEW_CONSOLE,
                    )
                else:
                    # Linux/macOS fallback: xterm or direct
                    proc = subprocess.Popen(
                        [python, script_path] + extra,
                        cwd=base_dir,
                    )
                self._processes[launch_key] = {"proc": proc, "label": label}
                self._log_status(
                    f"Launched in console: {script}  (PID {proc.pid})")
            else:
                # ---- NON-INTERACTIVE: pipe output to status ----
                # Use python.exe (not pythonw) so stdout is available
                proc = subprocess.Popen(
                    [python, "-u", script_path] + extra,  # -u = unbuffered
                    cwd=base_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    errors="replace",
                )
                self._processes[launch_key] = {"proc": proc, "label": label}
                self._log_status(
                    f"Launched: {script}  (PID {proc.pid})")

                # Background thread reads lines and queues them
                reader = threading.Thread(
                    target=self._read_output,
                    args=(proc, label),
                    daemon=True,
                )
                reader.start()

        except Exception as e:
            self._log_status(f"Error launching {script}: {e}")

    def _read_output(self, proc, label):
        """Read subprocess stdout line by line (runs in background thread).

        Puts messages into a thread-safe queue. The main thread
        picks them up via _poll_output().
        """
        try:
            for line in proc.stdout:
                line = line.rstrip("\n\r")
                if line:
                    self._output_queue.put(f"[{label}] {line}")
        except Exception:
            pass
        finally:
            returncode = proc.wait()
            if returncode == 0:
                self._output_queue.put(f"[{label}] Exited normally.")
            else:
                self._output_queue.put(
                    f"[{label}] Exited with code {returncode}.")

    def _poll_output(self):
        """Drain the output queue and update the status panel.

        Runs on the main thread via self.after(), called every 250ms.
        """
        try:
            while True:
                msg = self._output_queue.get_nowait()
                self._log_status(msg)
        except queue.Empty:
            pass
        # Schedule next poll
        self.after(250, self._poll_output)

    # ----------------------------------------------------------
    # RESOURCES & DOCUMENTATION
    # ----------------------------------------------------------
    def _build_resources_section(self):
        """External links and local documentation."""

        # Resources header
        res_frame = ctk.CTkFrame(self._main_frame, fg_color="transparent")
        res_frame.pack(fill="x", padx=20, pady=(20, 4))
        ctk.CTkLabel(
            res_frame, text="Resources",
            font=FONT_SECTION, text_color=COLOR_TEXT, anchor="w"
        ).pack(side="left")

        div = ctk.CTkFrame(self._main_frame, fg_color=COLOR_DIVIDER, height=1)
        div.pack(fill="x", padx=20, pady=(0, 8))

        # Two-column layout: External Links | Documentation
        columns = ctk.CTkFrame(self._main_frame, fg_color="transparent")
        columns.pack(fill="x", padx=20, pady=(0, 8))
        columns.grid_columnconfigure(0, weight=1)
        columns.grid_columnconfigure(1, weight=1)

        # --- External Links ---
        links_card = ctk.CTkFrame(columns, fg_color=COLOR_SURFACE,
                                  corner_radius=10)
        links_card.grid(row=0, column=0, sticky="nsew", padx=(0, 6), pady=4)

        ctk.CTkLabel(
            links_card, text="External Links",
            font=("Segoe UI", 13, "bold"), text_color=COLOR_ACCENT_DIM
        ).pack(anchor="w", padx=16, pady=(12, 4))

        for name, url in EXTERNAL_LINKS:
            if not url:
                continue
            link_btn = ctk.CTkButton(
                links_card, text=name,
                font=FONT_LINK,
                fg_color="transparent",
                hover_color=COLOR_SURFACE_HOVER,
                text_color=COLOR_LINK,
                anchor="w",
                height=28,
                command=lambda u=url: webbrowser.open(u)
            )
            link_btn.pack(fill="x", padx=12, pady=1)

        # Spacer at bottom of links card
        ctk.CTkFrame(links_card, fg_color="transparent",
                      height=8).pack()

        # --- Local Documents ---
        docs_card = ctk.CTkFrame(columns, fg_color=COLOR_SURFACE,
                                 corner_radius=10)
        docs_card.grid(row=0, column=1, sticky="nsew", padx=(6, 0), pady=4)

        ctk.CTkLabel(
            docs_card, text="Documentation",
            font=("Segoe UI", 13, "bold"), text_color=COLOR_ACCENT_DIM
        ).pack(anchor="w", padx=16, pady=(12, 4))

        for name, filename in LOCAL_DOCS:
            filepath = os.path.join(SCRIPT_DIR, filename)
            exists = os.path.exists(filepath)

            doc_btn = ctk.CTkButton(
                docs_card, text=name,
                font=FONT_LINK,
                fg_color="transparent",
                hover_color=COLOR_SURFACE_HOVER,
                text_color=COLOR_LINK if exists else COLOR_TEXT_DIM,
                anchor="w",
                height=28,
                command=lambda f=filepath: self._open_document(f),
                state="normal" if exists else "disabled"
            )
            doc_btn.pack(fill="x", padx=12, pady=1)

        # Spacer
        ctk.CTkFrame(docs_card, fg_color="transparent",
                      height=8).pack()

        # --- Open Project Folder button ---
        folder_btn = ctk.CTkButton(
            self._main_frame,
            text="Open Project Folder",
            font=FONT_DESC,
            width=180,
            height=32,
            fg_color=COLOR_BUTTON_BG,
            hover_color=COLOR_BUTTON_HOVER,
            text_color=COLOR_TEXT,
            corner_radius=8,
            command=self._open_project_folder
        )
        folder_btn.pack(pady=(4, 8))

    def _open_document(self, filepath):
        """Open a local document with the system default application."""
        if not os.path.exists(filepath):
            return
        try:
            if sys.platform == "win32":
                os.startfile(filepath)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", filepath])
            else:
                subprocess.Popen(["xdg-open", filepath])
        except Exception as e:
            print(f"[DASHBOARD] Error opening {filepath}: {e}")

    def _open_project_folder(self):
        """Open the project directory in the file manager."""
        try:
            if sys.platform == "win32":
                os.startfile(SCRIPT_DIR)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", SCRIPT_DIR])
            else:
                subprocess.Popen(["xdg-open", SCRIPT_DIR])
        except Exception as e:
            print(f"[DASHBOARD] Error opening folder: {e}")

    # ----------------------------------------------------------
    # STATUS PANEL (right side or bottom strip, fixed size either way)
    # ----------------------------------------------------------
    def _build_status_panel(self):
        """Panel showing launch activity.

        Docked right (fixed width) or bottom (fixed height) depending on
        self._status_position; internal contents are identical either way.
        """
        STATUS_WIDTH = 270
        STATUS_HEIGHT = 150

        panel = ctk.CTkFrame(
            self._outer_frame,
            fg_color=COLOR_SURFACE,
            corner_radius=0,
            **({"height": STATUS_HEIGHT} if self._status_position == "bottom"
               else {"width": STATUS_WIDTH}),
        )
        if self._status_position == "bottom":
            panel.grid(row=1, column=0, sticky="nsew")
            panel.grid_propagate(False)  # Keep fixed height (grid cell)
            panel.pack_propagate(False)  # Keep fixed height (packed children)
        else:
            panel.grid(row=0, column=1, sticky="nsew")
            panel.grid_propagate(False)  # Keep fixed width (grid cell)
            panel.pack_propagate(False)  # Keep fixed width (packed children)

        # Panel header
        ctk.CTkLabel(
            panel, text="Status",
            font=("Segoe UI", 14, "bold"),
            text_color=COLOR_ACCENT_DIM,
            anchor="w",
        ).pack(anchor="w", padx=16, pady=(16, 4) if self._status_position != "bottom" else (8, 2))

        div = ctk.CTkFrame(panel, fg_color=COLOR_DIVIDER, height=1)
        div.pack(fill="x", padx=12, pady=(0, 8) if self._status_position != "bottom" else (0, 4))

        # Status text box (fills remaining space)
        self._status_box = ctk.CTkTextbox(
            panel,
            fg_color=COLOR_BG,
            text_color=COLOR_TEXT_DIM,
            font=("Consolas", 10),
            corner_radius=8,
            state="disabled",
            wrap="word",
        )
        self._status_box.pack(fill="both", expand=True, padx=12,
                              pady=(0, 8) if self._status_position == "bottom" else (0, 12))

        self._log_status("Dashboard ready.")

    def _log_status(self, message):
        """Append a timestamped message to the status window."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}]  {message}\n"

        self._status_box.configure(state="normal")
        self._status_box.insert("end", line)
        self._status_box.see("end")
        self._status_box.configure(state="disabled")

        # Also print to console for batch-file users
        print(f"[DASHBOARD] {message}")

    # ----------------------------------------------------------
    # FOOTER
    # ----------------------------------------------------------
    def _build_footer(self):
        """Bottom bar with credits."""
        footer = ctk.CTkFrame(self._main_frame, fg_color="transparent")
        footer.pack(fill="x", padx=20, pady=(8, 20))

        ctk.CTkLabel(
            footer,
            text="Built with Claude (Anthropic) -- AI partnership in action",
            font=FONT_FOOTER, text_color=COLOR_TEXT_DIM
        ).pack()


# ============================================================
# STANDALONE WINDOW WRAPPER
# ============================================================

class PalomasOrreryDashboard(ctk.CTk):
    """Standalone root window around PalomasOrreryDashboardFrame.

    Used when palomas_orrery_dashboard.py is run directly (double-click or
    _run_dashboard.bat). Handles the things only a root window needs: title,
    geometry, icon, screen centering. All the actual dashboard UI lives in
    PalomasOrreryDashboardFrame -- import that class directly instead when
    embedding the dashboard inside another Tkinter app.
    """

    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(800, 600)

        icon_path = os.path.join(SCRIPT_DIR, "favicon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass  # Not all platforms support .ico

        self.frame = PalomasOrreryDashboardFrame(self)
        self.frame.pack(fill="both", expand=True)

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() - WINDOW_WIDTH) // 2
        y = (self.winfo_screenheight() - WINDOW_HEIGHT) // 2
        self.geometry(f"+{x}+{y}")


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    app = PalomasOrreryDashboard()
    app.mainloop()


if __name__ == "__main__":
    main()
