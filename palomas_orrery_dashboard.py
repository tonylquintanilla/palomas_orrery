"""
Paloma's Orrery Dashboard
=========================
Central launch point for the Paloma's Orrery suite.

Project: Paloma's Orrery - Astronomical & Earth System Visualization
Author: Tony Quintanilla
Contact: tonyquintanilla@gmail.com

Philosophy: "Data Preservation is Climate Action"

AI Collaboration: Built with Claude (Anthropic) - conversational AI partnership
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
WINDOW_TITLE = "Paloma's Orrery"
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
    ("Google Drive", ""),  # Tony can fill in the URL
]

# ============================================================
# LOCAL DOCUMENTS
# ============================================================
# (display_name, filename_relative_to_SCRIPT_DIR)

LOCAL_DOCS = [
    ("README", "README.md"),
    ("Requirements", "requirements.txt"),
    ("Project Instructions", "project_instructions_with_claude_ai.md"),
    ("Web Gallery Handoff", "web_gallery_handoff.md"),
    ("Climate Data Handoff", "climate_data_preservation_handoff.md"),
    ("Module Index", "coordinate_system_guide.py"),
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

class PalomasOrreryDashboard(ctk.CTk):
    """Main dashboard window."""

    def __init__(self):
        super().__init__()

        # Window setup
        self.title(WINDOW_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(800, 600)
        self.configure(fg_color=COLOR_BG)

        # Set window icon
        icon_path = os.path.join(SCRIPT_DIR, "favicon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass  # Not all platforms support .ico

        # Load favicon as image for header display
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

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() - WINDOW_WIDTH) // 2
        y = (self.winfo_screenheight() - WINDOW_HEIGHT) // 2
        self.geometry(f"+{x}+{y}")

    def _build_ui(self):
        """Construct the full dashboard layout.

        Two-panel design:
          Left  -- scrollable content (header, launch groups, resources, footer)
          Right -- fixed status panel (always visible, no scrolling needed)
        """

        # Top-level container: horizontal split
        self._outer_frame = ctk.CTkFrame(self, fg_color=COLOR_BG)
        self._outer_frame.pack(fill="both", expand=True)
        self._outer_frame.grid_columnconfigure(0, weight=1)   # left expands
        self._outer_frame.grid_columnconfigure(1, weight=0)   # right fixed
        self._outer_frame.grid_rowconfigure(0, weight=1)

        # ---- LEFT PANEL (scrollable) ----
        self._main_frame = ctk.CTkScrollableFrame(
            self._outer_frame,
            fg_color=COLOR_BG,
            scrollbar_button_color=COLOR_DIVIDER,
            scrollbar_button_hover_color=COLOR_ACCENT_DIM,
        )
        self._main_frame.grid(row=0, column=0, sticky="nsew")

        # ---- RIGHT PANEL (fixed status) ----
        self._build_status_panel()

        # ---- LEFT PANEL CONTENTS ----
        self._build_header()
        self._build_launch_section()
        self._build_resources_section()
        self._build_footer()

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
                self._build_launch_card(cards_frame, name, script, desc,
                                        base_dir, interactive, i)

    def _build_launch_card(self, parent, name, script, desc, base_dir,
                           interactive, index):
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
            command=lambda s=script, b=base_dir, ia=interactive: self._launch(s, b, ia),
            state="normal" if exists else "disabled"
        )
        btn.pack(side="right", padx=(12, 0))

    def _launch(self, script, base_dir=None, interactive=False):
        """Launch a Python script as a subprocess.

        Non-interactive: stdout/stderr piped to status panel.
        Interactive:      opens in its own console window.
        """
        # Debounce: ignore if same script launched within 1 second
        import time
        now = time.time()
        if script in self._last_launch and (now - self._last_launch[script]) < 1.0:
            return
        self._last_launch[script] = now

        if base_dir is None:
            base_dir = SCRIPT_DIR
        script_path = os.path.join(base_dir, script)
        if not os.path.exists(script_path):
            self._log_status(f"Not found: {script_path}")
            return

        # Short label for status messages (filename without .py)
        label = os.path.splitext(script)[0]

        try:
            python = sys.executable

            if interactive:
                # ---- INTERACTIVE: open in its own console ----
                if sys.platform == "win32":
                    proc = subprocess.Popen(
                        [python, script_path],
                        cwd=base_dir,
                        creationflags=subprocess.CREATE_NEW_CONSOLE,
                    )
                else:
                    # Linux/macOS fallback: xterm or direct
                    proc = subprocess.Popen(
                        [python, script_path],
                        cwd=base_dir,
                    )
                self._processes[script] = {"proc": proc, "label": label}
                self._log_status(
                    f"Launched in console: {script}  (PID {proc.pid})")
            else:
                # ---- NON-INTERACTIVE: pipe output to status ----
                # Use python.exe (not pythonw) so stdout is available
                proc = subprocess.Popen(
                    [python, "-u", script_path],  # -u = unbuffered
                    cwd=base_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    errors="replace",
                )
                self._processes[script] = {"proc": proc, "label": label}
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
    # STATUS PANEL (right side, fixed)
    # ----------------------------------------------------------
    def _build_status_panel(self):
        """Fixed right-side panel showing launch activity."""
        STATUS_WIDTH = 270

        panel = ctk.CTkFrame(
            self._outer_frame,
            fg_color=COLOR_SURFACE,
            width=STATUS_WIDTH,
            corner_radius=0,
        )
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_propagate(False)  # Keep fixed width

        # Panel header
        ctk.CTkLabel(
            panel, text="Status",
            font=("Segoe UI", 14, "bold"),
            text_color=COLOR_ACCENT_DIM,
            anchor="w",
        ).pack(anchor="w", padx=16, pady=(16, 4))

        div = ctk.CTkFrame(panel, fg_color=COLOR_DIVIDER, height=1)
        div.pack(fill="x", padx=12, pady=(0, 8))

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
        self._status_box.pack(fill="both", expand=True, padx=12, pady=(0, 12))

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
# ENTRY POINT
# ============================================================

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = PalomasOrreryDashboard()
    app.mainloop()


if __name__ == "__main__":
    main()
