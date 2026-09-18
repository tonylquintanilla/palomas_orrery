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

Role: gui
Domain: orrery

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
September 12, 2026 with Anthropic's Claude Opus 5 (L-325): added the Test
Derived Figures button, in the indented group under CHECKERS.
September 12, 2026 with Anthropic's Claude Opus 5 (L-324): added the two
missing indented buttons, Test Status Lines and Test Row Shape --
test_status_lines.py had been in the maintenance runner since L-305 with
no button here. Reordered Developer Tools on Tony's instruction: the
indented group is GENERATORS then CHECKERS, each alphabetical, and the
standalone tools below are alphabetical too. A bare string in a
LAUNCH_GROUPS list is now drawn as a heading.
September 16, 2026 with Anthropic's Claude Opus 5 (L-322): added
Constants Export under GENERATORS and Test Constants Export and Test
Dimensions under CHECKERS, matching the maintenance runner, and rewrote
Test Derived Figures' description for its Rule 8 rewrite.
September 17, 2026 with Anthropic's Claude Opus 5 (L-322, the gallery
half): added the five gallery tools the shared dashboard was missing --
Constants Export Pull, Config Mirror (report only), Mirror Suite,
Config Mirror Check and Pointer Join -- and corrected both Gallery
Maintenance Run descriptions, which still described a runner without
them and a Store drift that examined every link.
September 17, 2026 with Anthropic's Claude Fable 5.1 (L-334 session):
added Cache In Step, the gallery check that the served cache holds what
data/objects_config.json says, written after a config change reached
the live site ahead of the cache. The Gallery Maintenance Run
description said three Node smoke suites; it now names all six.
September 18, 2026 with Anthropic's Claude Opus 5 (L-334): added
Exhibit Store Editor to Developer Tools, under Gallery Cache Builder --
Manual Run, so the two by-hand gallery tools sit together. It is a
window rather than a console tool, so it is declared the way Gallery
Studio is, with no interactive flag.
September 18, 2026 with Anthropic's Claude Opus 5 (L-334), same day, on
Tony's second thought: MOVED Exhibit Store Editor to Gallery & Web,
beside the other gallery content tools, and sorted that group the way
Developer Tools was sorted on 2026-09-12 -- the offline runner, then
its indented checkers alphabetically, then the live runner, then the
standalone tools alphabetically. Added Store Writer Suite and Store
Editor Suite, two of the six gallery checkers that had no button. The
other four, and Feature renderers, Page framing, Sun shells and Earth
scene geometry, are Node and this dashboard launches everything with
Python; Hover Budget has a button only because someone wrote
documentation/run_hover_budget.py to wrap it.
"""

import os
import sys
import subprocess
import threading
import queue
import webbrowser
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

# ============================================================
# CONFIGURATION
# ============================================================

# Resolve the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Gallery tools live in a sibling directory
GALLERY_TOOLS_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io", "tools")

# The cache builder must run from the gallery REPO ROOT, not from tools/:
# its --config and --output-dir defaults are relative to the working
# directory. Launching it from GALLERY_TOOLS_DIR fails on load_config().
GALLERY_REPO_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io")

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
        ("Gallery Maintenance Run -- offline",
        "gallery_maintenance_run.py",
        "The gallery repo's own runner (L-236), before you commit. "
        "Regenerates the module atlas, pulls the orrery's constants "
        "export at its HEAD SHA and mirrors the served numbers into "
        "data/objects_config.json, then runs the cache builder suite, "
        "the mirror suite, the config mirror check, the pointer join, "
        "the cache-in-step check, the six Node suites (feature "
        "renderers, page framing, Sun shells, Earth scene geometry, "
        "hover budget, arrival), and the artifact-1 assembler "
        "test. Three states rather than two: a suite that could "
        "not run -- Node missing, say -- reports UNREACHABLE and is "
        "never counted as a pass. Everything indented below is included "
        "in it.",
        GALLERY_REPO_DIR,
        True),
        ("Artifact 1 Assembler Pin",
        os.path.join("documentation", "pin_artifact1_known_failure.py"),
        "Runs the Artifact 1 assembler test and compares its five verdicts, "
        "and T3's feature set, against the 2026-08-31 pin. It GATES the "
        "gallery runner. Before the pin (L-237) the row printed FAIL every "
        "single run for a known reason, which made a real regression "
        "indistinguishable from the old one -- a row that always fails hides "
        "the next change behind the last. Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Cache In Step",
        os.path.join("tools", "check_cache_in_step.py"),
        "Checks that the served cache holds the same shells as "
        "data/objects_config.json, value for value. The rooms draw from "
        "the cache, not from the config, so a config change reaches a "
        "visitor only after the cache builder has run. When this fails, "
        "run the cache builder and commit its output with the config; do "
        "not push the config alone. Names each difference by its path. "
        "GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Cache Siblings",
        os.path.join("documentation", "check_cache_siblings.py"),
        "Reports the served cache's sibling directories -- the .staging_* "
        "and .quarantine_* remnants -- with each one's age taken from the "
        "run id in its NAME, and names those the builder's next run should "
        "reap. Report-only: it exits 0 whatever it finds. It exists because "
        "the builder's sweep failed silently for six weeks and nothing said "
        "so (L-274); if it goes quiet again this says so within a day. "
        "Runs from the gallery repo ROOT and deletes nothing.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Config Mirror -- report only",
        os.path.join("tools", "mirror_constants.py"),
        "Lists what the mirror WOULD write into data/objects_config.json "
        "from the pulled export, field by field, and writes nothing. This "
        "is the report to read before a maintenance run does the writing. "
        "It names every link the export cannot serve yet with the reason, "
        "every link pointing outside the store, and any link it refuses: a "
        "relabel, where the number is the same and only the unit's name "
        "moved, and a unit conflict, where the number changes too and "
        "nothing here converts.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Config Mirror Check",
        os.path.join("tools", "check_constants_links.py"),
        "Checks that every served link in data/objects_config.json holds "
        "exactly what the export says -- value, unit and figure count -- "
        "and prints how many it compared. A difference is a hand edit or a "
        "pull without a mirror run, and it says which. GATES the gallery "
        "runner.",
        GALLERY_REPO_DIR,
        True,
        ["--mirror"],
        True),
        ("Constants Export Pull",
        os.path.join("tools", "pull_constants_export.py"),
        "Fetches the orrery's data/constants_export.json at the orrery's "
        "HEAD SHA and writes it, with that SHA, into the gallery's data/. "
        "This is how the orrery's numbers reach the page: the gallery "
        "reads the export and never parses orrery source (L-322). With no "
        "network it reports N-A and leaves the previous pull alone. If the "
        "orrery does not yet carry the two slice lists it says so and "
        "writes nothing.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Gallery Builder Offline Tests",
        "test_gallery_cache_builder_offline.py",
        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network.",
        GALLERY_TOOLS_DIR,
        True,
        None,
        True),
        ("Hover Budget",
        os.path.join("documentation", "run_hover_budget.py"),
        "Counts the LINES in every hover the renderers produce -- 78 of "
        "them, across the composed Earth room, Earth's features on their "
        "own, and the two ringed planets -- and prints the longest ten so "
        "the offender is named rather than implied. It GATES the gallery "
        "runner. It exists because its sibling checks hover WIDTH, no line "
        "over 90 characters, and on 2026-09-15 a 32-line bow shock hover "
        "passed that comfortably while the box ran off the bottom of the "
        "phone: a hover can be perfectly narrow and still overflow. The "
        "ceiling is a RATCHET -- lower it when the worst hover comes down, "
        "never raise it to admit a new one, which is how the old ones "
        "reached 32. The suite is Node; this is the Python wrapper the "
        "dashboard needs, the same shape as the Artifact 1 pin. Runs from "
        "the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Mirror Suite",
        os.path.join("tools", "test_mirror_constants.py"),
        "42 checks over the mirror, on made-up configs and exports rather "
        "than the real ones. It exists because no link in the real config "
        "can produce a relabel, a conflict or a definition until those "
        "rows are exported, so a run over the real file would exercise one "
        "path and say nothing about the other five. GATES the gallery "
        "runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Pointer Join",
        os.path.join("tools", "check_constants_links.py"),
        "Classifies all 70 of the config's links into the store: served "
        "from the export, waiting for their row's slice visit, or pointing "
        "outside the store. The waiting count is the measure of the store "
        "walk's progress, and when it reaches zero Store drift has nothing "
        "left to examine. Fails on a link waiting inside a CLOSED slice, "
        "and on a blocked transmission whatever the slice. GATES the "
        "gallery runner.",
        GALLERY_REPO_DIR,
        True,
        ["--join"],
        True),
        ("Store Editor Suite",
        os.path.join("tools", "test_exhibit_store_editor.py"),
        "Checks the editor window's logic WITHOUT opening the window: "
        "that every box the form offers is a path the writer will "
        "accept, that Earth's word list and its tick list differ by the "
        "two radiation belts on purpose, that nothing typed saves "
        "nothing, that the save message never claims a visitor sees what "
        "they cannot yet, and that a red Cache in step is explained "
        "rather than just shown. Run it by hand with --window to also "
        "open a real window and walk every row and every tick; the "
        "runner does not, because that would put a window on your screen "
        "in the middle of a check. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Store Writer Suite",
        os.path.join("tools", "test_store_writer.py"),
        "Checks the writer that the Exhibit Store Editor saves through: "
        "that it changes only the one line it was asked to, that it ADDS "
        "a word a shell does not carry yet, and that it refuses "
        "everything outside a served shell's words, a belt's words and "
        "the arrival settings -- slugs, colours and every number among "
        "them. Its own fixtures run first each time, so a pass means each "
        "refusal actually ran rather than merely being declared; then "
        "every shell and every word field of the real config, both "
        "rooms. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Gallery Maintenance Run -- live, AFTER a push",
        "gallery_maintenance_run.py",
        "The two checks that can only mean something once GitHub Pages "
        "has deployed. Fetches seven files from palomasorrery.com and "
        "requires each to be served -- this is what catches Jekyll "
        "dropping every .py in the repo, which no local test can see. "
        "Then refetches the orrery's constants export at the SHA the "
        "pull recorded, and fails if the served copy differs. Store "
        "drift then follows objects_config.json's pointers into "
        "constants_new.py at the orrery HEAD, but ONLY for the links "
        "the export cannot serve yet (L-322): it prints how many of the "
        "70 it is examining, and when that reaches zero it says so and "
        "can be retired. If the site is still serving the previous "
        "deploy it says NOT YET DEPLOYED rather than passing.",
        GALLERY_REPO_DIR,
        True,
        ["--live"]),
        ("Exhibit Store Editor",
         "exhibit_store_editor.py",
         "Edit the words a visitor reads in the exhibit rooms, and tick "
         "what each room opens on. A window: pick a room, pick a shell, "
         "type. It writes data/objects_config.json IN PLACE, changing "
         "only the line it was asked to, so the diff stays readable. It "
         "will write a shell's name, description, about, note, source "
         "and link, a radiation belt's words, and the arrival block's "
         "shells and Moon -- and nothing else. Numbers, their units, "
         "their figure counts and their orrery_constant links are shown "
         "in grey and cannot be typed into; a number changes in "
         "constants_new.py and arrives here through the export and the "
         "mirror. SAVING IS NOT DEPLOYING: words reach a visitor only "
         "after the cache builder has run, because the rooms draw their "
         "shells from the served cache, while the opening-view ticks are "
         "read from the config by the page itself and need only the "
         "push. The window says which after every save. It does NOT "
         "start the cache builder -- that stays a hand run with OneDrive "
         "paused (L-216).",
         GALLERY_TOOLS_DIR),
        ("Gallery Cleanup",
        "gallery_cleanup.py",
        "Find and (with confirmation) delete gallery JSON/KMZ files that "
        "aren't referenced by gallery_metadata.json, plus stray .json.bak files.",
        GALLERY_TOOLS_DIR,
        True),
        ("Gallery Editor",
        "gallery_editor.py",
        "Edit gallery metadata, categories, and featured items",
        GALLERY_TOOLS_DIR),
        ("Gallery JSON Fixer",
        "gallery_json_fixer.py",
        "Fix older gallery JSON files for current viewer",
        GALLERY_TOOLS_DIR),
        ("Gallery Studio",
        "gallery_studio.py",
        "Curate and export plots for the web gallery",
        GALLERY_TOOLS_DIR),
        ("Inspect Staging",
        "inspect_staging.py",
        "Plain-language report on a dry-run staging folder: real dates "
        "instead of Julian days, TP values, and point counts per object, "
        "so a dry-run can be judged without opening the raw JSON. "
        "Read-only -- fetches nothing, changes nothing, promotes nothing. "
        "Opens a console and asks for the staging folder path, which the "
        "builder prints on the last line of a --dry-run.",
        GALLERY_TOOLS_DIR,
        True),
        ("JSON Converter",
        "json_converter.py",
        "Convert HTML exports to gallery-ready JSON",
        GALLERY_TOOLS_DIR,
        True),  # interactive -- needs its own console
        ("Serve Gallery Locally",
        "serve_gallery.py",
        "Serve the gallery repo at http://localhost:8000 and open the "
        "assembler dev page, where Artifact 1 and the Artifact 2 candidate "
        "render in the browser. The page fetches the assembler files and "
        "the served cache, and browsers refuse fetch() from a file:// "
        "page, so it cannot be opened by double-clicking the HTML. Runs in "
        "its own console and keeps running -- one line per request is the "
        "server working, not a hang. Ctrl+C or close the window to stop.",
        GALLERY_TOOLS_DIR,
        True),
    ],

    "Developer Tools": [
        ("Gallery Cache Builder -- Manual Run",
         os.path.join("tools", "gallery_cache_builder.py"),
         "Manual serving-cache build. Runs from the gallery repo ROOT: the "
         "builder resolves its data/ paths from the working directory, so "
         "launching it from tools/ cannot find data/objects_config.json. "
         "With no flags it fetches from Horizons, validates, atomic-swaps "
         "the new cache into data/solar-system, and STOPS -- it does not "
         "commit or push. Commit it yourself in GitHub Desktop after the "
         "run finishes. Do not commit while it is still running: mid-build "
         "the working tree shows deletions only, which is the swap in "
         "progress, not data loss. The console stays open at the repo root "
         "if you want a flagged re-run (--dry-run --object <slug>, "
         "--first-build).",
         GALLERY_REPO_DIR,
         True),
        ("MAINTENANCE RUN -- everything indented below",
         "orrery_maintenance_run.py",
         "One command for the whole routine: regenerates the generated "
         "documents, then runs every checker, then prints one summary. It "
         "reports and continues rather than stopping at the first failure, "
         "and says which generated files actually moved. About ten seconds. "
         "Run after an edit session and before a push. Everything indented "
         "below is included in it and can still be launched on its own.",
         SCRIPT_DIR,
         True),
        "GENERATORS -- regenerated every run; a no-op when nothing moved",
        ("Constants Export",
         "export_constants.py",
         "Write data/constants_export.json from constants_new.py: every "
         "row that declares a unit, with its value rounded to the figures "
         "it declares, its unit, its figure count and its status, plus the "
         "table saying what each unit means. The gallery reads this file "
         "instead of parsing orrery source. Rows not exported yet are "
         "listed by name with the reason. Writes nothing if the store has "
         "a problem, and nothing if the content would not change.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Document Index",
         "doc_index.py",
         "Regenerate the key-documents table in README.md from the "
         "one-line Doc-Kind tag each root document carries. The purpose "
         "text lives in the document it describes, not in this tool and "
         "not in the README, so the wording stays yours while the table "
         "stays generated. Three kinds: generated (never hand-edit -- the "
         "next run destroys the edit), zoned (hand-written prose around a "
         "marker zone a tool rewrites), and hand. A document with no tag "
         "is listed as untagged and named in the summary rather than "
         "quietly dropped. Run after adding, renaming, or retiring a root "
         "document; --check reports staleness without writing.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Regenerate Module Atlas",
         "module_atlas.py",
         "Scan codebase, generate MODULE_ATLAS.md. "
         "Run after significant codebase changes (new modules, reorganizations).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Update Ledger Index",
         "ledger_index.py",
         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "
         "and migrate DONE items to section C. Run after editing any ledger block.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Update Skill Manifest",
         "skills_index.py",
         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "
         "Run after adding, renaming, or versioning a skill.",
         SCRIPT_DIR,
         True,
         None,
         True),
        "CHECKERS -- these decide the push call",
        ("Builder Marker Join",
         "test_worksheet_request_builder.py",
         "Test that a citation continued onto a marked second line "
         "(`# Source+:` under `# Source:`) is joined back before the "
         "request quotes it. Every behaviour is exercised twice, once "
         "with input that should join and once with input that must NOT: "
         "a join firing on everything is indistinguishable from a join "
         "firing correctly, and both report zero problems, so the "
         "negative cases are the test. The last check runs against the "
         "real corpus. Run after editing the builder or relabeling a "
         "continuation.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Constants Change Report",
         "constants_change_report.py",
         "Ask git what changed in constants_new.py since the last commit "
         "and report each moved value in words. The line that matters "
         "says whether the provenance moved WITH the number: a deliberate "
         "correction edits the value and its comment block together, "
         "while corruption -- a bad merge, a stray keystroke, a copied "
         "stale value -- moves the number alone and leaves the evidence "
         "describing the old one. Run before committing a change to "
         "constants_new.py.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Extractor Pins",
         "test_extractor_pins.py",
         "Pin the instruction filter's kept-and-dropped set at "
         "LOOKBACK 30 / LOOKAHEAD 25, frozen 2026-08-14. The claim "
         "ordinal in every issued key -- the `::c2` -- counts claims "
         "AFTER this filter runs, so extending the instruction pattern "
         "by one phrase lets a formerly-dropped number join the sequence "
         "and shifts every ordinal after it with no prose edit at all. A "
         "worksheet returned against the old ordinals would then bind to "
         "the wrong claim. It does not decide whether a change is wrong; "
         "it reports that the extractor no longer means what the issued "
         "keys assume, and prints the replacement pin file.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Provenance Scanner",
         "provenance_scanner.py",
         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "
         "Run before/after edits to shared values, or when a value looks suspicious.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Citation Inheritance",
         "test_citation_inheritance.py",
         "Pass/fail tests for block-scoped citation inheritance in the "
         "provenance scanner.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Constants Export",
         "test_constants_export.py",
         "Check that data/constants_export.json matches constants_new.py: "
         "the store hash it was made from, every exported row re-read, the "
         "list of rows not exported, the rows that define each unit, and "
         "the per-slice gate. Prints both hashes, so a pass shows what it "
         "compared. Run after editing the store; Constants Export first.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Constants Provenance",
         "test_constants_provenance.py",
         "Pass/fail regression tests for constants_new.py. "
         "Run before committing changes to constants, or first if a plot looks wrong.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Cross-Check Annotations",
         "test_cross_checked.py",
         "Pass/fail tests for the cross-check annotation grammar and V2 "
         "scoring. Run after editing annotations or the scanner's parser.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Derived Figures",
         "test_derived_figures.py",
         "Check that no derived constant declares more significant "
         "figures than its inputs support: fewest figures for products "
         "and quotients, coarsest decimal place for sums and "
         "differences. Names every derived row it cannot judge yet, "
         "found both by its arithmetic and by its # Derived: line. A "
         "built-in set of test rows runs first and must give every "
         "verdict, so a pass means the check can fail.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Dimensions",
         "test_dimensions.py",
         "Check that each derived constant's unit follows from its "
         "arithmetic, in dimension and in size, using astropy inside the "
         "check. Dividing by the row that defines a unit counts as "
         "converting into it. Rows with no unit yet are named, not "
         "failed, outside a finished slice. A built-in set of test rows "
         "runs first and must give every verdict.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Orbit Cache",
         "test_orbit_cache.py",
         "Comprehensive test suite for orbit data caching, format conversion, "
         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Reset Completeness",
         "test_reset_completeness.py",
         "Guard the Reset button against partial-reset drift: dirties every "
         "tracked control, calls the live reset handler, asserts everything "
         "returns to its startup default.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Row Shape",
         "test_status_lines.py",
         "The row-shape guard by itself. A value that is not a container "
         "literal must fit on the assignment's own line, because "
         "constants_change_report.py reads values line by line off a git "
         "diff and once reported a constant REMOVED that was only unreadable. "
         "Dicts and lists are exempt: a lookup table cannot fit on one line. "
         "Same script as Test Status Lines, run with --shape-only so it ends "
         "on its own verdict.",
         SCRIPT_DIR,
         True,
         ["--shape-only"],
         True),
        ("Test Scanner Recognition",
         "test_provenance_1d.py",
         "Proves the provenance scanner still recognizes a real citation "
         "and still refuses a fake one. Covers shadow constants (a local "
         "copy of a value already defined and cited in constants_new.py), "
         "author-year forms like (Nolan et al. 2013), F/C units, and tier "
         "labels. Half the tests are written backwards on purpose: a regex "
         "that is too loose clears findings by matching what it should "
         "not, and the Tier-1 count then falls, which looks like progress. "
         "Ledger L-156, sub-steps 1d and 1e.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Status Lines",
         "test_status_lines.py",
         "Pass/fail tests for the Status Line grammar on every "
         "constants_new.py row that carries one, plus coverage on the rows "
         "that carry none. Runs the row-shape guard as well; Test Row Shape "
         "below runs that half on its own.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Worksheet Checker",
         "test_worksheet_checker.py",
         "Pass/fail tests for the worksheet checker. Every layer is "
         "exercised twice, once with evidence that clears it and once "
         "with an injected violation that must not, because zero "
         "findings and a broken check look identical. Run after editing "
         "the checker or the worksheet schema.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Worksheet Checker",
         "worksheet_checker.py",
         "Open the worksheet each cross-check annotation names and report "
         "whether that worksheet records the check the annotation claims. "
         "Catches a value edited AFTER its check, which no diff-based tool "
         "can see once the edit is committed. Report-only -- it writes "
         "WORKSHEET_CHECK.md and never gates a push. Run after writing "
         "annotations, after a value moves, or before a gallery build.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Worksheet Key Round Trip",
         "test_worksheet_keys.py",
         "Assert that every annotated site mints a key that resolves back "
         "to it, on every run. A rename breaks it, a split implementation "
         "between the builder and the checker breaks it, and a change to "
         "the enclosing-name rule breaks it -- all three loudly, at the "
         "commit that introduced them, rather than months later when a "
         "returned worksheet will not bind.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Add Module Docstrings",
         "add_docstrings.py",
         "Add or improve module-level docstrings across the codebase; touches no code. "
         "Run after adding modules, before regenerating the Module Atlas.",
         SCRIPT_DIR,
         True),
        ("Animation HTML Tool",
         "measure_animation_html.py",
         "Measure a saved animation HTML: trace count, frame count, which traces "
         "are carried inside frames, and frames payload size. Run to compare a "
         "baseline against a patched export and quantify the frame-fence fix.",
         SCRIPT_DIR,
         True),
        ("Climate Cache Manager",
         "climate_cache_manager.py",
         "Safely update the climate data caches, with validation and rollback.",
         SCRIPT_DIR,
         True),
        ("Create Ephemeris Database",
         "create_ephemeris_database.py",
         "(Re)build satellite_ephemerides.json from idealized_orbits.py plus "
         "any downloaded Horizons ephemeris files.",
         SCRIPT_DIR,
         True),
        ("Dependency Trace",
         "dep_trace.py",
         "Map who depends on (and is consumed by) a module. "
         "Run before editing: python dep_trace.py <module_name> [hops]",
         SCRIPT_DIR,
         True),
        ("Export Orbit Cache",
         "export_orbit_cache.py",
         "Phase 1b devtool: read the local orbit caches (read-only) and write "
         "web-servable orbit/position files for the interactive gallery.",
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
        ("Verify Orbit Cache",
         "verify_orbit_cache.py",
         "Back up, validate, and repair orbit_paths.json, reporting any issues. "
         "Run if orbit plots look wrong or the cache may be corrupted.",
         SCRIPT_DIR,
         True),
        ("VOT Cache Manager",
         "vot_cache_manager.py",
         "Verify VizieR VOT cache file integrity.",
         SCRIPT_DIR,
         True),
        ("Worksheet Request Builder",
         "worksheet_request_builder.py",
         "Write the cross-check request that goes OUT to a reader. The "
         "checker reads what comes back; this writes what is sent. Opens "
         "in its own console because it asks three questions, in this "
         "order. WHICH ROWS -- a numbered list of named selections; it "
         "DEFAULTS TO 1, the whole corpus, so type the number you want "
         "rather than pressing Enter (2 is constants_new.py, the 23-row "
         "pilot slice). BATCH NAME -- becomes the filename. ANCHOR SHA -- "
         "the commit the request describes; use current HEAD, and re-run "
         "if you commit anything before sending it, because a returned "
         "row is checked against this SHA. It writes "
         "REQUEST_<batch>.jsonl and REQUEST_<batch>.md into "
         "documentation/worksheets/ and refuses rather than overwriting "
         "if either name is taken. Send the .jsonl; the .md is the "
         "fallback if a return will not parse. It judges nothing -- "
         "reading the returns is Worksheet Checker, above.",
         SCRIPT_DIR,
         True),
    ],

}

# ============================================================
# LAUNCH TARGET LABELS AND HOVER TEXT
# ============================================================

# Longest path first: a nested repo must be tested before its parent,
# or the parent claims every file under it.
REPO_ROOTS = (
    (GALLERY_REPO_DIR, "Gallery"),
    (SCRIPT_DIR, "Orrery"),
)

TOOLTIP_DELAY_MS = 400


def launch_target_label(script, base_dir=None, args=None):
    """'Orrery: palomas_orrery.py' -- which repo, and the path inside it.

    The dashboard launches some tools with a working directory already
    inside the repo (gallery tools run from tools/), so the path is
    rebuilt relative to the repo ROOT rather than shown as handed to
    the subprocess. A target outside both repos falls back to its full
    path, which is also what an unresolvable one shows.
    """
    full = os.path.abspath(os.path.join(base_dir or SCRIPT_DIR, script))
    shown = full
    for root, label in REPO_ROOTS:
        try:
            rel = os.path.relpath(full, os.path.abspath(root))
        except ValueError:
            # Different drive on Windows. Not this repo.
            continue
        if not rel.startswith(os.pardir):
            shown = "%s: %s" % (label, rel.replace(os.sep, "/"))
            break
    if args:
        shown = "%s %s" % (shown, " ".join(args))
    return shown


class Tooltip(object):
    """Hover text for a customtkinter widget.

    Bound to the widget AND every descendant. A CTkButton is a frame
    holding a canvas and a label; those sit on top of the frame and
    receive the enter event instead of it, so binding the frame alone
    shows nothing on the widget it was asked for.
    """

    def __init__(self, widget, text):
        self.text = text
        self.window = None
        self.after_id = None
        self.widget = widget
        self._bind_tree(widget)

    def _bind_tree(self, widget):
        widget.bind("<Enter>", self._schedule, add="+")
        widget.bind("<Leave>", self._hide, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")
        for child in widget.winfo_children():
            self._bind_tree(child)

    def _schedule(self, _event=None):
        self._cancel()
        self.after_id = self.widget.after(TOOLTIP_DELAY_MS, self._show)

    def _cancel(self):
        if self.after_id is not None:
            try:
                self.widget.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

    def _show(self):
        if self.window is not None or not self.text:
            return
        try:
            x = self.widget.winfo_rootx()
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        except Exception:
            return
        self.window = tk.Toplevel(self.widget)
        self.window.wm_overrideredirect(True)
        self.window.wm_geometry("+%d+%d" % (x, y))
        try:
            self.window.wm_attributes("-topmost", True)
        except Exception:
            # Not supported everywhere; the tooltip still shows.
            pass
        tk.Label(
            self.window, text=self.text, justify="left",
            background=COLOR_SURFACE_HOVER, foreground=COLOR_TEXT,
            relief="solid", borderwidth=1,
            font=("Consolas", 10), padx=8, pady=4
        ).pack()

    def _hide(self, _event=None):
        self._cancel()
        if self.window is not None:
            self.window.destroy()
            self.window = None


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
                # A bare string is a HEADING inside the group, not a
                # card. The maintenance runner prints GENERATORS then
                # CHECKERS, and the indented list here is that same
                # list, so it reads the same way. Alphabetical order
                # within each half is Tony's, 2026-09-12: without the
                # two labels a sorted run of twenty buttons gives no
                # clue where one kind stops and the other starts.
                if isinstance(entry, str):
                    self._build_indent_heading(cards_frame, entry)
                    continue
                name, script, desc = entry[0], entry[1], entry[2]
                base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR
                interactive = entry[4] if len(entry) > 4 else False
                args = entry[5] if len(entry) > 5 else None
                indent = entry[6] if len(entry) > 6 else False
                self._build_launch_card(cards_frame, name, script, desc,
                                        base_dir, interactive, args, i,
                                        indent)

    def _build_indent_heading(self, parent, text):
        """A dim heading inside the indented maintenance-run group.

        Drawn for a bare string in a LAUNCH_GROUPS list. Not a card and
        not clickable: it names which half of the runner the buttons
        below it belong to.
        """
        ctk.CTkLabel(
            parent, text=text,
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w"
        ).pack(anchor="w", padx=(28, 0), pady=(10, 2))

    def _build_launch_card(self, parent, name, script, desc, base_dir,
                           interactive, args, index, indent=False):
        """Individual launch card with button and description.

        `indent` marks a tool that the maintenance runner already covers.
        Indenting rather than removing was Tony's ruling of 2026-08-12:
        the individual entries stay launchable, and staying visible is how
        the automation's contents remain known instead of disappearing
        behind one button. The runner sits directly above its indented
        group.
        """
        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,
                            corner_radius=10)
        card.pack(fill="x", pady=4, ipady=6,
                  padx=(28, 0) if indent else 0)

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
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w",
            wraplength=600, justify="left"
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

        # Name the repo and file this button runs. A missing script shows
        # the full path instead, so "Not Found" says where it looked.
        if exists:
            hover = launch_target_label(script, base_dir, args)
        else:
            hover = "Not found: %s" % script_path
        Tooltip(btn, hover)

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
