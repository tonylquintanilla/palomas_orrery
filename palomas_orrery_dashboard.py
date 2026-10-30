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
September 19, 2026 with Anthropic's Claude Opus 5 (L-341): a Find a tool
search box above the groups, and the two oversized groups split. Tony
had just run a tool from a terminal that this dashboard already carried
a button for, and asked for both. The search filters on NAME AND
DESCRIPTION and draws each match under its own group heading rather
than in one flat list, so it answers "where does this live" as well as
"where is it" -- his choice, because he prefers a visual check and
because the second answer is the one that makes the search unnecessary
next time. Gallery & Web became Gallery -- checks and data and Gallery
-- authoring; Developer Tools became Maintenance Run and Tools and
Caches; Gallery Cache Builder -- Manual Run moved to the gallery group,
where its GALLERY_REPO_DIR base always said it belonged. NO entry was
reordered and no description was touched: in particular the twenty
checkers under the maintenance runner stay in one alphabetical run,
because that arrangement is Tony's ruling of 2026-09-12 and re-sorting
them by kind would overturn it silently. The groups now draw into their
own container frame so a search can rebuild them without disturbing the
header, the resources section or the footer.
September 19, 2026 with Anthropic's Claude Opus 5 (L-341), same day, on
Tony's suggestion: a FIND button beside Clear, and the search now runs
on demand rather than on every keystroke. Enter in the box does the
same thing. Typing now changes one short label, which says "press Find,
or Enter" whenever the box and the drawn list disagree -- without it a
typed-but-unsearched box would sit above a list that silently did not
match it. Clear empties the box and brings every group back in one
action.
September 20, 2026 with Anthropic's Claude Opus 5 (L-216): rewrote three
descriptions the L-216 build had made stale, and put Tony's four-step
cache-build routine on Gallery Cache Builder -- Manual Run, which is the
screen he launches the build from. Gallery Cache Builder now carries the
routine and what the hardened swap does; Cache Siblings says it names
every other directory in data/, not only the builder's own leftovers;
Gallery Builder Offline Tests says 190 checks and what the new 23 cover.
No button added, removed or reordered, and no code path touched. The
dashboard was not in that build's manifest and the build never opened
it, which is how three descriptions came to describe tools as they were
the morning before.
September 21, 2026 with Anthropic's Claude Opus 5 (L-216, patch 8b): the
builder button's routine now matches what the builder prints -- a [SWAP]
line, then its own numbered steps, the maintenance run BEFORE the commit
-- and Gallery Builder Offline Tests no longer carries a check count,
which went stale the day after it was written.
September 23, 2026 with Anthropic's Claude Opus 5.5 (L-322 Stage D, patch
D4), on Tony's request: added Earth Pole Live Check to Tools and Caches,
the script that fetches Earth's pole and orbit from Horizons and checks
the tilt against ERFA; and Test Earth Pole of Date to the checkers under
the maintenance runner, which patch D3 put in the runner with no button
here. Both in alphabetical place.
September 25, 2026 with Anthropic's Claude Opus 5.5 (L-322 Stage D, patch
D12), on Tony's request: added Exact Rows Report beside the other
generators, in alphabetical place. It writes EXACT_ROWS_PRINTED.md in the
orrery root. No other entry touched.
September 27, 2026 with Anthropic's Claude Opus 5.5 (L-322 Stage D, patch
D15): added Test Exact Rows By The Count to the checkers, in alphabetical
place, matching the maintenance runner's new checker; and Exact Rows
Report's description no longer says it is report-only.
September 27, 2026 with Anthropic's Claude Opus 5.5 (L-281, patch 4),
on Tony's design: a Daily Run group above the gallery groups. Its top
button runs daily_run.py in the gallery repo -- the guest book updater,
then the cache build after the OneDrive pause, then the offline
maintenance run -- and the three are indented under it. Gallery Cache
Builder -- Manual Run MOVED here from Gallery -- checks and data, its
description unchanged; the offline runner appears in both groups, the
full description staying in the gallery group. Guest Book Checks added
to the checkers in alphabetical place, on Tony's request. The offline
runner's description now names all it runs: it said "six Node suites"
while the runner had eight.
October 1, 2026 with Anthropic's Claude Opus 5.5 (L-395): added the five
tools L-395 put in the two maintenance runs, on Tony's question -- Objects
Export under GENERATORS and Test Objects Export under CHECKERS, and in
the gallery checks Objects Export Pull, Objects Mirror Check and
Objects Mirror Suite, each in alphabetical place.
October 5, 2026 with Anthropic's Claude Opus 5.5 (L-416), on Tony's
question and approval: every step of the two maintenance runs now has
a button. Added in alphabetical place, under the orrery's checkers,
Test Skill Headers (skills_index.py --check, L-407); and under the
gallery checks Arrival, Daily Run Steps, Display Figures, Earth Scene
Geometry, Feature Renderers, Gallery Module Atlas, Page Framing, Pole
of Date, Solar System Drawer and Sun Shells. The seven Node checks run
through the gallery's documentation/run_offline_check.py, which reads
each command from the gallery runner's own list. The offline runner's
description names the Solar System drawer, which it had left out.
October 6, 2026 with Anthropic's Claude Opus 5.5 (L-300): added
Collapsed Features under the gallery checks, in alphabetical place,
for the checker the gallery runner gained that day; the offline
runner's description names it.
October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395), on Tony's
request: Horizons Check in the Daily Run group, after the guest book,
as the Daily Run's step 2; Horizons Check Suite and Horizons
Confirmations under the gallery checks, in alphabetical place; the
offline runner's description names both. Fixed in passing, because they
no longer said what the code does: the Daily Run button and the cache
builder's routine still told Tony to pause OneDrive (retired 2026-10-10,
L-216), Daily Run Steps still said three scripts, and Objects Export
did not name the export's two new fields.
October 11, 2026 with Anthropic's Claude Opus 5.5 (L-416, on Tony's
note in his run record: "add new checks to the dashboard"): Test Hills
Cloud Sampler (L-421) and Test Scanner Row Run (L-414) under the
orrery's checkers, in alphabetical place. Both checkers were in the
maintenance run with no button.
October 11, 2026 with Anthropic's Claude Opus 5.5 (L-421, the website
half): Drawings Export under the generators and Test Drawings Export
under the checkers, in the same patch as the two scripts, so the new
check has its button from the start.
October 11, 2026 with Anthropic's Claude Opus 5.5 (L-421, the close, on
Tony's note in his run record: "please add this and any other new checks
to the dashboard"): Drawings Check and Drawings Pull under the gallery's
checks and data, in alphabetical place, for tools/check_drawings.py and
tools/pull_drawings.py; the offline runner's description names both.
October 12, 2026 with Anthropic's Claude Opus 5.5 (L-401, build 1): Test
Position Digits under the orrery's checkers, in alphabetical place, in
the same patch as the checker, so it has its button from the start.
October 12, 2026 with Anthropic's Claude Opus 5.5 (L-431, build 2): Orbit
Markers under the orrery's checkers, in the same patch as the checker.
Its label carries no "Test", by Tony's ruling 5 of 2026-10-12; it sits
after Test Orbit Cache, which is its alphabetical place once the other
labels lose the word.
October 13, 2026 with Anthropic's Claude Opus 5.5 (L-431, after build 2's
look): Orbit Markers' description counts twelve planted faults, not nine.
October 13, 2026 with Anthropic's Claude Opus 5.5 (L-437): Domain Split
under the orrery's checkers, in the same patch as its checker
test_domain_split.py, with the same name as its maintenance-run row (the
button is named what the run prints). It sits before Drawings Export,
its alphabetical place once the labels lose "Test".
October 13, 2026 with Anthropic's Claude Opus 5.5 (L-269): Maintenance
Report under the orrery's checkers, in the same patch as its checker
test_maintenance_report.py, with the same name as its maintenance-run
row. It sits before Test Objects Export, its alphabetical place once
the labels lose "Test".
October 13, 2026 with Anthropic's Claude Opus 5.5 (L-440, the dashboard's
labels, descriptions and findability; Tony's request of 2026-10-12). Each
card shows its name, the repository and script it runs in small type, and
one short line of at most twelve words saying what the tool does; the
paragraph opens in place under "+ more" (Tony's choice of 2026-10-13,
option B). The lines are in CARD_LINES, keyed by group and label, each
written from its script's own docstring. Text wraps to the window's width
and the Launch button is packed first, so a narrow window no longer pushes
the button off the card, as the fixed 600-pixel wrap did. A heading inside
a group now folds the cards under it; every heading starts open, so what a
runner runs stays visible (Tony's ruling of 2026-08-12), and a search keeps
a heading that holds a match. The website checks group gains six headings
in Tony's order of 2026-10-13: tools you run by hand, the module atlas,
JPL's check, the served cache, from the orrery, the rooms -- the manual
tools first, then the generated report, then the checks in the order the
data flows. A button under a runner now carries the name that run prints
(Tony's ruling, 2026-10-12, DESIGN_rulings_20261012.md; ruling 5 took
"Test" off), and the orrery's generators and checkers are re-sorted
alphabetically under the new names. Dashboard Parity
(test_dashboard_parity.py), a checker of the orrery's maintenance run,
holds all of it. Paloma's Orrery now opens in its own console window, as
the maintenance run does, so its printed output shows (Tony, 2026-10-13);
on macOS and Linux no new window opens and the output goes to the terminal
the dashboard was started from. Every other button runs as before.
Standing rules, carried here so the next builder reads them in the file:
the Maintenance Run group is GENERATORS then CHECKERS, each alphabetical
(2026-09-12, L-324); the search filters name, short line and paragraph and
draws each match under its own headings (2026-09-19, L-341); every check
keeps its own button, the two guest book checks excepted (L-281); a
runner's card sits directly above its indented group; and nothing written
in a description is cut, only moved behind "+ more".
October 14, 2026 with Anthropic's Claude Opus 5.5 (L-269): Maintenance
Report's description counts four planted faults, one of them the
scanner's output with Windows line endings.
October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431 build 3, with
L-395's move): the Horizons check moved from the website's Daily Run into
the orrery's maintenance run, and its buttons follow it, each named what
the run prints: Horizons Check under the orrery's generators, Horizons
Check Suite and Horizons Confirmations under its checkers, each in
alphabetical place, with their short lines. The website's own Horizons
buttons leave in a second patch, patch_L431_13, run after the website's
patch has removed their scripts, so Dashboard Parity holds at every step.
October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431 build 3, its
third patch, patch_L431_13, run after the website's): the Daily Run
group loses Horizons Check and says three steps; the website checks lose
Horizons Check Suite, whose script went to the orrery; the website's
Horizons Confirmations says it reads the dates from the pulled export;
and Drawn Orbit, the website's new checker, gets its button under the
served cache, in alphabetical place, with its short line.
October 14, 2026 with Anthropic's Claude Opus 5.5 (L-440, Tony's request
of the same day: "can we make the dashboard search be word order
insensitive? for example: objects export pull = pull objects export"):
the search matches each typed word on its own, so a card shows when every
word appears somewhere on it -- the group's name, the card's name, its
short line or its paragraph -- in any order. One word finds what it found
before; each word added narrows the list (Tony: "with order insensitive,
i would actually narrow the search but still find results"). Until now
the typed text had to appear as one phrase. matching_groups() holds the
rule at module level, so Dashboard Parity can test it and plant the old
phrase match as a fault.
October 15, 2026 with Anthropic's Claude Opus 5.5 (L-444): Period Fetch
under the orrery's generators and Period Fetch Suite under its checkers,
each named what the run prints, in alphabetical place, with its short
line.
October 15, 2026 with Anthropic's Claude Opus 5.5 (L-446, with L-380 and
L-388): the Daily Run is four steps. Pulls From The Orrery, the website's
gallery_maintenance_run.py --pull, joins the Daily Run group between the
Guest Book Updater and the Cache Builder, named what the Daily Run prints;
the Daily Run button says the pulls run first and that a failed pull
stops it before the builder (Tony's option A of 2026-10-15); Daily Run
Steps says four scripts; the offline runner's Daily Run card says fourth
step. Pull Failures, the website's new checker, gets its button under the
gallery checks, in alphabetical place. Each has its short line. Fixed in
passing: the Daily Run's short line still named the JPL check, which left
it on 2026-10-14.
October 16, 2026 with Anthropic's Claude Opus 5.5 (L-421 parts 2 and 3):
Typed Facts, the website's new checker, gets its button under the gallery
checks' rooms, in alphabetical place, with its short line, running
through documentation/run_offline_check.py. The offline runner's
description names it; Config Mirror Check says it compares the citation
too. Fixed in passing: Mirror Suite said 42 checks, and it holds 77.
October 18, 2026 with Anthropic's Claude Opus 5.5 (L-455): Typed Numbers,
the website's new checker, gets its button after Typed Facts, with its
short line, running through documentation/run_offline_check.py; the
offline runner's description names it.
October 20, 2026 with Anthropic's Claude Opus 5.5 (L-456, L-266): Source
List, the website's new checker, gets its button after Solar System
Figures, with its short line, running through
documentation/run_offline_check.py. And Horizons Check -- everything,
now, in Tools and Caches: horizons_check.py --all, which confirms every
object and data sheet today rather than only what is due (Tony,
2026-10-20).
October 21, 2026 with Anthropic's Claude Opus 5.5 (L-460): Drawer
Order, the website's new checker, gets its button after Display
Figures, with its short line, running through
documentation/run_offline_check.py.
October 21, 2026, night, with Anthropic's Claude Opus 5.5 (L-460,
L-466): Drawn Ends, the website's new checker, gets its button after
Drawer Order, with its short line, running through
documentation/run_offline_check.py.
October 22, 2026 with Anthropic's Claude Opus 5.5 (L-468, L-465): Label
Words, the website's new checker (gallery patch L434_3), gets its button
after Hover Budget, with its short line; the Far Lines text says what
that check holds since the same patch, and the Arrival text names the
Sun's rotation axis, a drawn guide that must carry no shell key.
October 24, 2026 with Anthropic's Claude Opus 5.5 (L-443, slice 2): Path
Plan, the orrery's new generator, gets its button after Horizons Check,
and Path Plan Suite, its new checker, after Orbit Markers, each with its
short line. And Path Plan -- preview of slice 2, in Tools and Caches:
path_plan.py --preview, which plans the twelve spacecraft by name before
they are keyed; temporary, it goes when they are keyed.
October 24, 2026, late night, with Anthropic's Claude Opus 5.5 (L-443):
the preview runs with --no-limit, and both Path Plan texts say it prints
a line as it goes, saves each plan as it is made, and, without
--no-limit, starts nothing new after 10 minutes.
October 25, 2026 with Anthropic's Claude Opus 5.5 (L-443, build B): the
twelve spacecraft are keyed, so Path Plan -- preview of slice 2 goes;
Path Plan -- every path, now takes its place in Tools and Caches,
path_plan.py --all --no-limit, for a full plan when a spacecraft is
newly keyed or the rule changes.
October 27, 2026 with Anthropic's Claude Opus 5.5 (L-495): Direction
Arrows, the website's new checker (gallery patch L494_3), gets its
button after Collapsed Features, with its short line, running through
documentation/run_offline_check.py. The Dashboard parity check had
found it missing on the run after patch_L494_4.
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
FONT_SCRIPT = ("Consolas", 10)     # the script a card runs (L-440)

# ============================================================
# LAUNCH TARGETS
# ============================================================
# Each entry: (display_name, script_filename, description,
#              [base_dir], [interactive], [args], [indent])
# base_dir:    optional, defaults to SCRIPT_DIR
# interactive: optional, True = opens in its own console window
#              (for scripts that need terminal input, and for the
#              orrery, whose printed output shows there; L-440)
# args:        optional list of arguments passed to the script
# indent:      optional, True = a step the runner above it runs
# A bare string is a heading inside its group; it folds the cards
# under it. Each card's short line is in CARD_LINES, below, keyed by
# (group, display_name): add one with every new button. A button
# under a runner is named what that run prints (Tony, 2026-10-12).
# Dashboard Parity holds both rules on every maintenance run (L-440).

LAUNCH_GROUPS = {
    "Solar System": [
        ("Paloma's Orrery",
         "palomas_orrery.py",
         "Interactive 3D solar system with comets, asteroids, and spacecraft",
         SCRIPT_DIR,
         True),
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

    "Daily Run": [
        ("Daily Run -- everything indented below",
         "daily_run.py",
         "What the gallery needs once a day, in one window, in this order "
         "(L-281, Tony's design of 2026-09-27). First the Guest Book "
         "Updater: approve or decline each new message, and write entries "
         "or replies if you like. Then the Pulls From The Orrery: the "
         "orrery's exports and drawings, at its HEAD, copied into the "
         "website's config BEFORE the build, so the build uses what the "
         "orrery exported today (L-446). If a pull cannot reach the "
         "orrery, the Daily Run STOPS there and names it: nothing is built "
         "on yesterday's export, and you run it again later (Tony's option "
         "A, 2026-10-15). Then the Cache "
         "Builder, with no OneDrive pause since 2026-10-10 (L-216: "
         "the retry is sufficient). Then the Gallery Maintenance Run, "
         "offline, which the builder's own next steps ask for before a "
         "commit; its pull rows print \"no change\". Apart from the pulls, "
         "a step that reports a problem does not stop the next "
         "one. It ends with one summary naming each step's result and "
         "what is left for you: commit and push in GitHub Desktop, and "
         "the live maintenance run. It opens by saying when the last "
         "cache build was, so a missed day shows. It never commits or "
         "pushes. Everything indented below is included in it and can "
         "still be run on its own.",
         GALLERY_REPO_DIR,
         True),
        ("Guest Book Updater",
         os.path.join("tools", "guestbook_updater.py"),
         "The lobby's guest book (L-281). Fetches the messages visitors "
         "sent through the Google Form and shows each one you have not "
         "decided on: a to approve, d to decline, l to decide later. A "
         "rating or other answer the form collects is shown to you beside "
         "the message and never published. Then a menu: write an entry of "
         "your own, reply under an entry, remove an entry, or set the "
         "form's address, which turns on the lobby's Sign the guest book "
         "link. Your entries and replies can link to gallery pages -- type "
         "a room such as solar_system/earth, a card's id, or an exhibit "
         "such as earth -- and a misspelt one is refused. It changes only "
         "data/guestbook.json and says when that needs a commit. Run it "
         "alone as often as you like; it is also the Daily Run's first "
         "step. The private address of the form's responses is kept in "
         "tools/guestbook_local.json, which git ignores.",
         GALLERY_REPO_DIR,
         True,
         None,
         True),
        ("Pulls From The Orrery",
         "gallery_maintenance_run.py",
         "The Daily Run's second step (L-446): gallery_maintenance_run.py "
         "--pull. Runs only the five pull-and-mirror rows -- Constants "
         "Export Pull, Config Mirror, Objects Export Pull, Objects Mirror, "
         "Drawings Pull -- before the Cache Builder, so the build reads "
         "what the orrery exported today. Everything they bring was "
         "already checked against JPL in the orrery's maintenance run. A "
         "pull that cannot reach the orrery prints FAIL with the address "
         "it tried and writes nothing, and the mirror after it does not "
         "run (L-388). Ends on a line starting \"=== PULLS:\" that names "
         "any row that failed; the Daily Run stops there when one did.",
         GALLERY_REPO_DIR,
         True,
         ["--pull"],
         True),
        ("Cache Builder",
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
         "--first-build).\n"
         "\n"
         "THE ROUTINE (L-216). Run the build: no OneDrive pause since "
         "2026-10-10, the retry is sufficient. It ends with a "
         "[SWAP] line saying how the swap went, and then prints its own "
         "numbered next steps. Follow them: run Gallery Maintenance Run -- "
         "offline BEFORE you commit, and check that its last line agrees "
         "with the [SWAP] line; then look at GitHub Desktop's change list, "
         "commit and push. The swap retries a refused rename for about "
         "fifty seconds and puts the PREVIOUS cache back if it still "
         "cannot finish, so you are never left without one. A swap that "
         "took more than one attempt is a refusal the builder absorbed, "
         "and those two lines are the only way you will know.",
         GALLERY_REPO_DIR,
         True,
         None,
         True),
        ("Gallery Maintenance Run -- offline",
         "gallery_maintenance_run.py",
         "The Daily Run's fourth step: the same button as Gallery "
         "Maintenance Run -- offline under Gallery -- checks and data, "
         "which describes it in full. Run after the build and before you "
         "commit.",
         GALLERY_REPO_DIR,
         True,
         None,
         True),
    ],

    "Gallery -- checks and data": [
        ("Gallery Maintenance Run -- offline",
        "gallery_maintenance_run.py",
        "The gallery repo's own runner (L-236), before you commit. "
        "Regenerates the module atlas, pulls the orrery's constants "
        "export at its HEAD SHA and mirrors the served numbers into "
        "data/objects_config.json, pulls the orrery's stored drawings, "
        "then runs every checker and prints "
        "one line each. Python: the cache builder suite, pole of date, "
        "the mirror suite, the store writer and store editor suites, "
        "the config mirror check, pull failures, Horizons "
        "confirmations, the pointer join, cache in step, drawn orbit, the drawings "
        "check, the collapsed-features sweep, the "
        "guest book updater, the Daily Run's steps, the artifact-1 "
        "assembler pin, and cache siblings (report only). Node: feature "
        "renderers, page framing, Sun shells, Earth scene geometry, "
        "hover budget, typed facts, typed numbers, arrival, display figures, Solar "
        "System figures, the Solar System drawer, and the guest book. "
        "Three states rather than two: a suite that could not run -- "
        "Node missing, say -- reports UNREACHABLE and is never counted "
        "as a pass. Every checker named here also has its own indented "
        "button below, to run it alone.",
        GALLERY_REPO_DIR,
        True),
        "TOOLS YOU RUN BY HAND -- each tests a tool you use yourself",
        ("Daily Run Steps",
        "daily_run.py",
        "daily_run.py --check: fails if any of the four scripts the "
        "Daily Run calls is missing, say after a rename, and names it. "
        "Runs nothing else. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        ["--check"],
        True),
        ("Guest Book Checks",
        os.path.join("documentation", "run_guestbook_checks.py"),
        "Both checks for the lobby's guest book (L-281), which the "
        "gallery runner also runs. Guest book: the page's own drawing "
        "code on the real data/guestbook.json -- newest first, every "
        "piece of text escaped so nothing a visitor types can become part "
        "of the page, no link ever drawn on a visitor's entry, and only "
        "links to this gallery's own pages. Guest book updater: the tool "
        "in three scripted runs on made-up messages, including the case "
        "where the form has no message or note column, which it must "
        "refuse rather than guess. Each suite first proves it can fail. "
        "The first is Node; this is the Python wrapper the dashboard "
        "needs. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
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
        "THE MODULE ATLAS -- the website's map of its own modules",
        ("Module Atlas",
        "module_atlas.py",
        "The gallery repo's own module atlas: regenerates its "
        "MODULE_ATLAS.md and MODULE_INDEX.md. The gallery runner does "
        "this first on every run, as a generator. Not the orrery's "
        "atlas, which has its own button under the maintenance run.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        "JPL'S CHECK OF THE OBJECTS",
        ("Horizons Confirmations",
        os.path.join("tools", "check_horizons_confirmations.py"),
        "The website's own check of JPL's confirmations, offline: it reads "
        "the dates in the pulled data/objects_export.json and fails on any "
        "served object never confirmed against JPL, confirmed 30 or more "
        "days ago, or changed since -- and on a fetched period the same "
        "way -- so the website shows it when the orrery's Horizons Check "
        "has not run (L-395; the check itself moved into the orrery's "
        "Maintenance Run on 2026-10-14, L-431). GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        "THE SERVED CACHE -- what the website serves, and its builder",
        ("Artifact 1 Assembler",
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
        ("Cache Builder Suite",
        "test_gallery_cache_builder_offline.py",
        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network. Since L-216 it also covers the swap's retries, the "
        "roll-back that puts the previous cache back, the swap log, a dry "
        "run leaving that log alone, the sibling report naming folders the "
        "builder did not make, the builder SAYING how each swap went, the "
        "maintenance run reading every rename, and the next steps printing "
        "only after a good hand run. The lock itself cannot be produced in "
        "a sandbox, so a refused rename is simulated through the builder's "
        "own _rename seam -- the same name the real build path goes "
        "through. The run itself prints the current count of checks.",
        GALLERY_TOOLS_DIR,
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
        "Runs from the gallery repo ROOT and deletes nothing.\n"
        "\n"
        "SINCE 2026-09-20 (L-216) it also names every OTHER directory in "
        "data/, under its own heading -- OneDrive's conflict copies land "
        "there and the sweep will never touch them. It used to look only "
        "for the builder's own name shapes, so four of them printed as "
        "\"no sibling directories\". One had been published by accident "
        "and held the only copy of 38 days of run history, now kept at "
        "documentation/cache_run_history/. Judge a copy by what is inside "
        "it, not by its name.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Drawn Orbit",
        os.path.join("tools", "test_drawn_orbit.py"),
        "An orbit whose period JPL gives around the solar system's "
        "barycentre is drawn around the barycentre, moved to where it sits "
        "seen from the Sun (L-431 build 3). Checks the cache builder serves "
        "those elements only for such a body and only at the date of its "
        "Sun-centred ones, refuses a set from another date, and that the "
        "room draws the ellipse in the right place, on Sedna's real numbers. "
        "Planted faults, among them an orbit drawn around the Sun, are each "
        "caught. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        "FROM THE ORRERY -- its numbers, drawings and pole",
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
        "exactly what the export says -- value, unit, figure count, and "
        "since L-421 the citation beside it, word for word -- and prints "
        "how many it compared. A difference is a hand edit or a "
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
        ("Drawings",
        os.path.join("tools", "check_drawings.py"),
        "Every stored drawing the config names -- today the Hills cloud's "
        "3,600 dots, placed by the orrery -- is pulled into data/drawings/, "
        "served byte for byte in data/solar-system/drawings/, and tilted as "
        "its file records: the plane through the served dots is fitted "
        "again here, by this check's own arithmetic. Three faults are "
        "planted first and each must be caught. Red right after a pull that "
        "moved the dots, until the cache builder runs (L-421). GATES the "
        "gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Drawings Pull",
        os.path.join("tools", "pull_drawings.py"),
        "Fetches each stored drawing the config names from the orrery's "
        "data/drawings/ at the orrery's HEAD SHA and writes it, with that "
        "SHA, into the gallery's data/drawings/. This is how the Hills "
        "cloud's dots reach the website: the orrery places them and the "
        "website draws them as given (L-421, Tony's option A). The cache "
        "builder then serves them. With no network it reports N-A and "
        "leaves the previous pull alone.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Mirror Suite",
        os.path.join("tools", "test_mirror_constants.py"),
        "77 checks over the mirror, on made-up configs and exports rather "
        "than the real ones. It exists because no link in the real config "
        "can produce a relabel, a conflict or a definition until those "
        "rows are exported, so a run over the real file would exercise one "
        "path and say nothing about the other five. GATES the gallery "
        "runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Objects Export Pull",
        os.path.join("tools", "pull_objects_export.py"),
        "Fetches the orrery's data/objects_export.json at the orrery's "
        "HEAD SHA and writes it, with that SHA, into the gallery's data/. "
        "This is how each body's name, Horizons id, description and NASA "
        "link reach the website from the orrery's object list (L-395). With "
        "no network it reports N-A and leaves the previous pull alone.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Objects Mirror Check",
        os.path.join("tools", "mirror_objects.py"),
        "Lists every field of every linked object in data/objects_config.json "
        "that differs from the pulled export -- name, Horizons id, id type, "
        "description, NASA link -- and writes nothing. A difference is a "
        "hand edit or a pull without a mirror run; the maintenance run's "
        "Objects mirror writes them. Also refuses a Solar System drawer row "
        "with no key in the export. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Objects Mirror Suite",
        os.path.join("tools", "test_mirror_objects.py"),
        "Forces each of the objects mirror's writes and refusals on made-up "
        "configs -- an insert that keeps the file's layout, an id change "
        "reported, a blank id type left alone, a row without a key, a key "
        "without an object, a null over held words -- then reads the real "
        "config. GATES the gallery runner.",
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
        ("Pole of Date",
        os.path.join("tools", "test_pole_of_date.py"),
        "Holds the cache builder's copy of the orrery's tilt geometry "
        "(tools/pole_of_date.py) to the frame angle in the constants "
        "export, to the orrery's own results on two real Horizons days, "
        "and to ERFA, the IAU's routines; then reruns each check with "
        "one input altered, where it must fail. Needs astropy. GATES "
        "the gallery runner. Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Pull Failures",
        os.path.join("tools", "test_pull_failures.py"),
        "Runs each of the three pulls in a throwaway copy with its "
        "network replaced by one that fails three ways -- the orrery's "
        "HEAD unreachable, its answer unreadable, the file missing at "
        "HEAD. Each must exit 1, print FAIL naming the address, and leave "
        "every file as it was; and the mirror after a failed pull must "
        "not run (L-388, L-446). Plants three faults first, each caught. "
        "Edits nothing in the repository. GATES the gallery runner.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        "THE ROOMS -- as the page draws them",
        ("Arrival",
        os.path.join("documentation", "run_offline_check.py"),
        "Both rooms open on the right things (L-334). Builds the Sun "
        "room's shells and the Earth room's scene with the real "
        "renderers, applies gallery/arrival.js with the real "
        "data/objects_config.json, and compares what is drawn on "
        "opening against its list; it also fails on any shell trace with "
        "no shell key, and on a drawn guide (the Sun's rotation axis) "
        "that carries one. It first makes itself fail on purpose four ways. "
        "GATES the gallery runner. The check is Node, so this button "
        "runs it through documentation/run_offline_check.py, which "
        "reads its command from the gallery runner's own list: the two "
        "cannot drift. Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Arrival"],
        True),
        ("Collapsed Features",
        "sweep_collapsed_features.py",
        "Sorts every served feature group: a shell stored as itself, or a "
        "known group collapsed into parallel lists (belts, rings), each "
        "named. It exits 2 only on a group it cannot classify, which is "
        "the case that should stop a push. GATES the gallery runner "
        "(L-300). Runs from the gallery repo ROOT and changes nothing.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Direction Arrows",
        os.path.join("documentation", "run_offline_check.py"),
        "The small arrowhead on each body's orbit or path in the Solar "
        "System room, pointing the way the body travels (L-495). It sits "
        "five arrowhead lengths ahead of the body, its direction read from "
        "the order the served points come in, and is not drawn when its "
        "tip falls outside the view or the line is too short for it at "
        "that scale. Works six cases by hand and checks the page gives "
        "each body one arrow with no hover. It breaks its own file three "
        "ways first, to show it can fail. GATES the gallery runner. The "
        "check is Node, so this button runs it through "
        "documentation/run_offline_check.py. Runs from the gallery repo "
        "ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Direction arrows"],
        True),
        ("Display Figures",
        os.path.join("documentation", "run_offline_check.py"),
        "Every number in an Earth hover shows the figures its source "
        "supports (L-342). Reads the BUILT hovers from the served "
        "cache, not the formatting helpers, and fails on any number it "
        "cannot account for, or if the config and the cache would print "
        "differently. GATES the gallery runner. The check is Node, so "
        "this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Display figures"],
        True),
        ("Drawer Order",
        os.path.join("documentation", "run_offline_check.py"),
        "Each room's drawer lists its shells at the nearest part of "
        "each as drawn, read from its served row (L-460). Builds the Sun "
        "and Earth rooms with the real renderers and holds the page's "
        "order to one it works out from the same rows, each stored "
        "drawing's nearest dot read from its file. Moves one row's "
        "edge and breaks its own file first, to show it can fail. GATES "
        "the gallery runner. The check is Node, so this button runs it "
        "through documentation/run_offline_check.py. Runs from the "
        "gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Drawer order"],
        True),
        ("Drawn Ends",
        os.path.join("documentation", "run_offline_check.py"),
        "Every drawing in the Sun and Earth rooms starts and stops where "
        "its served row says (L-460, L-466). Builds both rooms with the "
        "real renderers and the served drawings, measures each drawing's "
        "nearest and farthest point, and fails on an end no row explains "
        "unless it is held by name with its reason; prints every held "
        "end. Plants a corona dot at the Sun's surface and a Hills cloud "
        "dot at 257 AU first, to show it can fail. GATES the gallery "
        "runner. The check is Node, so this button runs it through "
        "documentation/run_offline_check.py. Runs from the gallery repo "
        "ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Drawn ends"],
        True),
        ("Earth Scene Geometry",
        os.path.join("documentation", "run_offline_check.py"),
        "The Earth room's composed scene, headless, on the recorded "
        "payload documentation/payload_earth_scene.json: the axis tilt "
        "against the served pole of date, the equator and geostationary "
        "ring in one plane, the terminator, the subsolar point, the "
        "Moon's arc and what the room opens on. Every number compared "
        "is read from the served rows. GATES the gallery runner. The "
        "check is Node, so this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Earth scene geometry"],
        True),
        ("Far Lines",
        os.path.join("documentation", "run_offline_check.py"),
        "A drawn line that reaches far past the view is cut to the view's "
        "edge before a phone draws it (L-463). The Galactic Plane's ring "
        "and pole line, at 100,000 AU, drew as a wide pink band on Tony's "
        "phone whenever the Sun room was zoomed in close. It works six "
        "cases by hand, builds the Sun room from the served config and "
        "names the lines it looks after, and checks every line that "
        "reaches far past the view is cut to the box and every other line "
        "is left as served. It breaks its own file three ways first, to "
        "show it can fail. GATES the gallery runner. The check is Node, so "
        "this button runs it through documentation/run_offline_check.py. "
        "Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Far lines"],
        True),
        ("Feature Renderers",
        os.path.join("documentation", "run_offline_check.py"),
        "Smoke test for gallery/feature_renderers.js, the code that "
        "draws every shell, ring, belt and magnetosphere on the "
        "website. The geometry checks measure the drawn points, not the "
        "inputs, so a wrong answer fails. GATES the gallery runner. The "
        "check is Node, so this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Feature renderers"],
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
        ("Label Words",
        os.path.join("documentation", "run_offline_check.py"),
        "Naming a shell in a room's drawer opens that shell's own words "
        "(L-468). Builds the Sun and Earth rooms with the real renderers "
        "and checks, for every shell row, that the marker the drawer "
        "opens is the row's own: the corona's row had opened the streamer "
        "belt's words, because the two are drawn as one feature. It "
        "breaks its own pick first, to show it can fail. GATES the "
        "gallery runner. The check is Node, so this button runs it "
        "through documentation/run_offline_check.py. Runs from the "
        "gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Label words"],
        True),
        ("Page Framing",
        os.path.join("documentation", "run_offline_check.py"),
        "The page's own framing helpers, taken out of the page and run "
        "against real feature traces; the checks measure the axis "
        "ranges that result, so a wrong range fails. GATES the gallery "
        "runner. The check is Node, so this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Page framing"],
        True),
        ("Solar System Drawer",
        os.path.join("documentation", "run_offline_check.py"),
        "The Solar System room's drawer does what Tony's design says "
        "(L-363): worked cases on the real "
        "gallery/solar_system_drawer.js, the real "
        "data/objects_config.json's rows, and interactive.html loading "
        "the file and calling each function it must. GATES the gallery "
        "runner. The check is Node, so this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Solar System drawer"],
        True),
        ("Solar System Figures",
        os.path.join("documentation", "run_solar_system_figures.py"),
        "Checks the distances the Solar System room prints (L-398). Each "
        "prints to the place the larger of two errors earns: how far the "
        "page's arithmetic may have drifted from JPL Horizons, and how "
        "well JPL knows where the body is at all, from its 2014 ephemeris "
        "report. Works six distances by hand, matches every body in the "
        "room's drawer to its group's row, and prints each body's "
        "distance from the served cache with what set its figures. Fails "
        "unless Uranus, Neptune and Pluto print to JPL's ten-thousands "
        "place, and if the page stops using gallery/solar_system_figures.js. "
        "It breaks that file three ways first, so a pass has shown it can "
        "fail. The check is Node; this is the Python wrapper the dashboard "
        "needs. GATES the gallery runner. Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Source List",
        os.path.join("documentation", "run_offline_check.py"),
        "The i panel lists each feature's sources one to a line, every web "
        "address a link a visitor can tap (L-456). It works where an "
        "address ends and what the list holds, builds the Sun room and "
        "Earth's recorded scene, and names for every feature how many "
        "citations it lists and how many carry a link. It fails if a "
        "listed citation disagrees with the joined line, or an address is "
        "lost from the list. It breaks its own file two ways first, to "
        "show it can fail. GATES the gallery runner. The check is Node, so "
        "this button runs it through documentation/run_offline_check.py. "
        "Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Source list"],
        True),
        ("Sun Shells",
        os.path.join("documentation", "run_offline_check.py"),
        "The Sun room's shells, built by the real renderers from the "
        "real data/objects_config.json: no input left unread, the "
        "expected geometry traces, and the shapes that must be thinned "
        "or tilted measured where they are drawn. GATES the gallery "
        "runner. The check is Node, so this button runs it through "
        "documentation/run_offline_check.py, which reads its command "
        "from the gallery runner's own list: the two cannot drift. Runs "
        "from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Sun shells"],
        True),
        ("Typed Facts",
        os.path.join("documentation", "run_offline_check.py"),
        "No fact about nature is typed in the rooms' code (L-421): a fact "
        "is served with its feature's words and its source. It builds the "
        "Sun and Earth rooms three ways -- as served, with every served "
        "word replaced by a marker, and with every served number scaled "
        "-- and names, by room, feature and sentence, anything still "
        "printed that is not the pointer line, a served number's own "
        "label, or on its short allowed list, which it prints in full. It "
        "reads each room's description sentence by sentence too. "
        "Sentences held for your ruling (L-451) are printed every run and "
        "do not fail. GATES the gallery runner. The check is Node, so this "
        "button runs it through documentation/run_offline_check.py, which "
        "reads its command from the gallery runner's own list. Runs from "
        "the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Typed facts"],
        True),
        ("Typed Numbers",
        os.path.join("documentation", "run_offline_check.py"),
        "Every number a visitor reads in the served words comes from a row "
        "(L-455). It builds the Sun and Earth rooms from the config with "
        "every served number scaled, and fails on any number in a served "
        "word that did not move with its row, naming the room, the feature "
        "and the sentence with the digit in brackets. A digit in a name, a "
        "citation's page or year, or a date whose source is named beside "
        "it is allowed, and each list prints in full. Findings already on "
        "a ledger row are held and printed every run; they do not fail. "
        "GATES the gallery runner. The check is Node, so this button runs "
        "it through documentation/run_offline_check.py, which reads its "
        "command from the gallery runner's own list. Runs from the gallery "
        "repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        ["Typed numbers"],
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
    ],
    "Gallery -- authoring": [
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

    "Maintenance Run": [
        ("MAINTENANCE RUN -- everything indented below",
         "orrery_maintenance_run.py",
         "One command for the whole routine: regenerates the generated "
         "documents, then runs every checker, then prints one summary. It "
         "reports and continues rather than stopping at the first failure, "
         "and says which generated files actually moved. About ten seconds; "
         "on a day something is due for JPL, its Horizons Check needs the "
         "internet and a couple of minutes more. "
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
        ("Drawings Export",
         "export_drawings.py",
         "Write data/drawings/: the dots the orrery places and the website "
         "draws as given -- the Hills cloud (hills_cloud_sampler.py), Earth's "
         "radiation belts (van_allen_belt_sampler.py), Earth's hydrogen "
         "exosphere (earth_exosphere_sampler.py), the Sun's corona "
         "(sun_corona_sampler.py) and the zodiacal dust cloud "
         "(zodiacal_dust_sampler.py), each from its rows with a "
         "fixed seed, the same dots the orrery window draws (L-421, Tony's "
         "option A). Writes only when the dots change.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Exact Rows Report",
         "exact_rows_report.py",
         "List every place the orrery or the gallery prints an exact row of "
         "constants_new.py -- a definition or a stated rule, such as a cut "
         "angle -- with the code on each line, so the width it prints at "
         "can be read. Rule 7 of provenance-discipline says such a row "
         "prints by a print count it states, not a width chosen where it "
         "is printed; this is the list that work moves from. Reads the "
         "gallery folder beside the orrery and says so at the top if it is "
         "missing. Writes EXACT_ROWS_PRINTED.md and prints whether every "
         "printed exact row prints by its count; this button never fails. "
         "Exact Rows by the Count is the same check as a pass/fail.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Horizons Check",
         "horizons_check.py",
         "Asks JPL Horizons about what the website serves, for whatever is "
         "due, so on most runs it asks nothing (L-395, moved here from the "
         "website's Daily Run on 2026-10-14, L-431). Each keyed object: the "
         "same id, the same index, JPL's exact name, and a pinned comet "
         "still JPL's newest record. Each fetched orbital period: JPL's "
         "period at the same date and centre, within the period's own "
         "error. Both are asked again from day 25, before the website's "
         "own check goes red at day 30. Each spacecraft's data sheet: "
         "re-read every 30 days, and red where a row of constants_new.py "
         "quotes a figure the sheet no longer gives. One line per thing "
         "asked; each disagreement with the query to paste into a browser. "
         "Records the confirmations and the sheets, and never edits the "
         "list or a row. Needs the internet only on a day something is "
         "due; if JPL cannot be reached it says UNREACHABLE and asks "
         "nothing more.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Ledger Index",
         "ledger_index.py",
         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "
         "and migrate DONE items to section C. Run after editing any ledger block.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Module Atlas",
         "module_atlas.py",
         "Scan codebase, generate MODULE_ATLAS.md. "
         "Run after significant codebase changes (new modules, reorganizations).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Path Plan",
         "path_plan.py",
         "Makes the plan for drawing each spacecraft path the website "
         "serves (L-443, slice 2): the span JPL has positions for, and each "
         "flyby that needs finer steps than the path's weekly backbone -- a "
         "nearest approach inside a body's Hill sphere, found in JPL's own "
         "positions, with its moment, distance and speed, and the window "
         "and step to fetch around it. Writes data/path_plans.json. On a "
         "30-day cycle, so most runs ask JPL nothing; --all asks for every "
         "path now. It prints a line as it goes, saves each plan as it is "
         "made, and starts nothing new after 10 minutes: what is left is "
         "named and taken up by the next run, or by pressing this again. "
         "If JPL cannot be reached it keeps each plan as it was and says "
         "UNREACHABLE.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Objects Export",
         "export_objects.py",
         "Write data/objects_export.json from the object list in "
         "celestial_objects.py: every entry carrying a 'key', the website's "
         "name for it, with its name, Horizons id, JPL's exact name, id "
         "type, object type, description (without its opening "
         "\"Horizons:\" sentence) and NASA link. The website pulls this "
         "file and never reads orrery source (L-395). Lists every number in "
         "an exported description. Writes nothing if an entry writes a "
         "field twice, a key repeats, or a keyed entry has no JPL name.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Period Fetch",
         "period_fetch.py",
         "Asks JPL Horizons for the orbital period of each object the "
         "website serves that has none fetched yet -- a typed period, none, "
         "or a new object -- so on most runs it asks nothing (L-444). It "
         "uses the orrery's own fetch, the one plotting makes when you say "
         "yes to the update dialog, without the dialog: the orbit's "
         "elements and its period together, saved to "
         "data/osculating_cache.json, naming each body whose elements it "
         "refreshed. It runs just before the Horizons Check, which then "
         "compares the new periods with JPL the same day. The Sun and the "
         "Pluto-Charon barycentre are named and skipped, as plotting skips "
         "them. If JPL cannot be reached it saves nothing for that body, "
         "says UNREACHABLE and asks nothing more.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Skill Manifest",
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
        ("Citation Inheritance",
         "test_citation_inheritance.py",
         "Pass/fail tests for block-scoped citation inheritance in the "
         "provenance scanner.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Constants Change",
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
        ("Constants Export Check",
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
        ("Constants Relations",
         "test_constants_provenance.py",
         "Pass/fail regression tests for constants_new.py. "
         "Run before committing changes to constants, or first if a plot looks wrong.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Cross-Check Annotations",
         "test_cross_checked.py",
         "Pass/fail tests for the cross-check annotation grammar and V2 "
         "scoring. Run after editing annotations or the scanner's parser.",
         SCRIPT_DIR,
         True,
         None,
         True),
                ("Dashboard Parity",
         "test_dashboard_parity.py",
         "Check that every row of the orrery's maintenance run, the website's "
         "offline maintenance run and the Daily Run has a button here with "
         "the same name and the same script, that every indented button "
         "names a row, that every button's script is on disk, and that every "
         "card carries its short line of twelve words or fewer; and that the "
         "search finds a card by its words in any order. It reads "
         "both repositories and edits neither. Ten faults are planted "
         "first, each caught by name. Ends on \"DASHBOARD PARITY: PASS\" "
         "(L-440).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Derived Figures",
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
        ("Dimensions",
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
        ("Domain Split",
         "test_domain_split.py",
         "Check that the provenance scanner's whole-tree Tier-1 total prints "
         "with its split by domain (orrery, Earth System, stars, ...), the "
         "same on the console, in PROVENANCE_AUDIT.md and in the run history; "
         "that each module's domain is read from the Domain: tag in its own "
         "docstring; and that a file with no tag is named, not counted as "
         "orrery. Scans small made-up modules in a temporary folder and writes "
         "nothing in the project. Six faults are planted first, each caught by "
         "name. Ends on \"DOMAIN SPLIT: PASS\" (L-437).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Drawings Export Check",
         "test_drawings_export.py",
         "Check that each stored drawing in data/drawings/ (today the Hills "
         "cloud's dots, which the website draws) is exactly the drawing its "
         "rows in constants_new.py give, that git does not ignore it, and "
         "that its plane's tilt matches. Three faults are planted first -- "
         "a dot moved, the eccentricity row changed, the file reported "
         "ignored -- and each must be caught. Ends on \"DRAWINGS EXPORT: "
         "PASS\" (L-421). Run after Drawings Export.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Earth Pole of Date",
         "test_earth_pole_of_date.py",
         "Offline checks of Earth's pole and tilt of the plot's date: the "
         "build manifest's worked case, the geometry against ERFA's true "
         "obliquity for 2000, 2026 and 2100, the fall-back to the frame's "
         "year-2000 axis when Horizons cannot be reached, the cache, the "
         "hover words, and that Earth's axis really uses the pole of date. "
         "Never contacts Horizons; Earth Pole Live Check does.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Exact Rows by the Count",
         "exact_rows_report.py",
         "Fails when a printed exact row of constants_new.py states no "
         "print count, when an orrery line prints one by a width of its "
         "own instead of through exact_text(), or when the gallery does not "
         "serve the count beside it. Names every failing item. The same "
         "script as Exact Rows Report, run with --check.",
         SCRIPT_DIR,
         True,
         ["--check"],
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
        ("Hills Cloud Sampler",
         "test_hills_cloud_sampler.py",
         "The Hills cloud's three checks, each first shown able to fail: "
         "four faults are planted (the galactic pole's RA and Dec swapped, "
         "the ecliptic node set to 0, the paper's Fig. 3 reading moved, the "
         "tilt pushed to 60 degrees) and each must be caught, then the real "
         "rows must pass. Ends on \"HILLS CLOUD: PASS\" (L-421).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Horizons Check Suite",
         "test_horizons_check.py",
         "The Horizons Check on recorded answers, with no network "
         "(documentation/worksheets/horizons_answers_L395.json, each answer "
         "with its source; the period and data-sheet answers were written "
         "in JPL's format on 2026-10-14 and say so, and the inputs the test "
         "runs on are frozen beside them). Every served entry agrees, and "
         "each planted mistake is caught by name: a wrong id, the wrong "
         "index, a name off by one letter, a stale pin, a period JPL "
         "disagrees with, a changed data sheet, JPL unreachable (L-395, "
         "L-431).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Horizons Confirmations",
         "check_horizons_confirmations.py",
         "What today's Horizons Check found, read offline: fails on any "
         "keyed object or fetched period never confirmed against JPL, "
         "confirmed 30 or more days ago, or changed since; on a data sheet "
         "a row quotes that no longer gives the row's figure; and on a "
         "check that could not reach JPL today, named UNREACHABLE (L-395, "
         "L-431).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Maintenance Report",
         "test_maintenance_report.py",
         "Check that the maintenance run's summary names, under the "
         "provenance scanner's verdict, every file whose Tier-1 count rose "
         "since the scanner's previous run, and says so when it cannot read "
         "that. Runs the run's real summary on recorded scanner output, once "
         "with Windows line endings, as it reaches the run on Windows. Four "
         "faults are planted first, each in a copy of the real code, and each "
         "must be caught by name. "
         "Ends on \"MAINTENANCE REPORT: PASS\" (L-269).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Objects Export Check",
         "test_objects_export.py",
         "Check that data/objects_export.json matches celestial_objects.py, "
         "entry by entry, and that no entry among all 182 writes a field "
         "twice -- Python keeps only the second, silently. It first shows "
         "both checks can fail. Prints the keys it compared and every "
         "number in an exported description. Run after editing the object "
         "list; Objects Export first.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Orbit Cache",
         "test_orbit_cache.py",
         "Comprehensive test suite for orbit data caching, format conversion, "
         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Orbit Markers",
         "test_orbit_markers.py",
         "Check that each orbit is drawn around the same center as its period "
         "(Sedna's around the solar system's center of mass, Mercury's and "
         "Encke's around the Sun), that each perihelion and aphelion marker is "
         "dated from the period JPL gave, with that period's uncertainty where "
         "it is more than a day, and that every orbit and marker hover prints "
         "its distances to the digits JPL's errors earn. Runs the real orbit "
         "drawing offline on recorded inputs and judges it with arithmetic of "
         "its own. Twelve faults are planted first, each in a copy of the real "
         "code, and each must be caught by name. "
         "Ends on \"ORBIT MARKERS: PASS\" (L-431, L-401).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Path Plan Suite",
         "test_path_plan.py",
         "The Path Plan against a made-up solar system answered in JPL's "
         "own format, with no network: two flybys found to the minute, "
         "distance and speed, no distant body called a pass, the 30-day "
         "cycle asking nothing when nothing is due, an outage keeping the "
         "old plans, and two planted faults caught. "
         "Ends on \"PATH PLAN SUITE: 15 of 15 checks passed\" (L-443).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Period Fetch Suite",
         "test_period_fetch.py",
         "The Period Fetch on recorded answers, with no network "
         "(documentation/worksheets/period_fetch_answers_L444.json, taken "
         "from the periods plotting saved for Mercury, Jupiter and Encke). "
         "Twelve faults are planted, each in a copy of period_fetch.py or "
         "of plotting's filter, and each must be caught by name: a fetched "
         "period asked again, the list not printed first, a new object "
         "missed, a record made another way than plotting's, a failed "
         "fetch read as a pass, and more. Then the real step must ask only "
         "for what is missing, with plotting's call, and save the record "
         "plotting saves, field by field. "
         "Ends on \"PERIOD FETCH SUITE: pass\" (L-444).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Position Digits",
         "test_position_digits.py",
         "Check that the orrery's body hover prints each distance and speed "
         "to the digits JPL's errors earn: a planet by its published row, a "
         "small body by JPL's own uncertainty for the date, anything else at "
         "whole kilometers with a sentence saying JPL states none. Builds its "
         "hovers offline and judges them against errors it works out itself, "
         "checks each pair prints the same from either end, and hovers every "
         "listed object from the Sun, Earth and Neptune. Eleven faults are "
         "planted first and each must be caught by name. "
         "Ends on \"POSITION DIGITS: PASS\" (L-401).",
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
        ("Reset Completeness",
         "test_reset_completeness.py",
         "Guard the Reset button against partial-reset drift: dirties every "
         "tracked control, calls the live reset handler, asserts everything "
         "returns to its startup default.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Row Shape",
         "test_status_lines.py",
         "The row-shape guard by itself. A value that is not a container "
         "literal must fit on the assignment's own line, because "
         "constants_change_report.py reads values line by line off a git "
         "diff and once reported a constant REMOVED that was only unreadable. "
         "Dicts and lists are exempt: a lookup table cannot fit on one line. "
         "Same script as Status Lines, run with --shape-only so it ends "
         "on its own verdict.",
         SCRIPT_DIR,
         True,
         ["--shape-only"],
         True),
        ("Scanner Recognition 1d/1e",
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
        ("Scanner Row Run",
         "test_row_run.py",
         "Pins for the provenance scanner (L-414): a row's citation is read "
         "from its own comment run, declared rows are named as their own "
         "kind, and the gate-path figure is computed and recorded by name. "
         "Run after editing provenance_scanner.py.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Skill Headers",
         "skills_index.py",
         "skills_index.py --check: reads every skill's header as YAML, "
         "the way Settings > Skills does, and fails on a header YAML "
         "refuses, a name or description that is not text, or a value "
         "YAML would cut short at a space before a # (L-407). The Skill "
         "Manifest button runs the same script without the check, "
         "and writes the protocol's table.",
         SCRIPT_DIR,
         True,
         ["--check"],
         True),
        ("Status Lines",
         "test_status_lines.py",
         "Pass/fail tests for the Status Line grammar on every "
         "constants_new.py row that carries one, plus coverage on the rows "
         "that carry none. Runs the row-shape guard as well; Row Shape "
         "below runs that half on its own.",
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
        ("Worksheet Checker Tests",
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
    ],
    "Tools and Caches": [
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
        ("Earth Pole Live Check",
         "earth_pole_live_check.py",
         "Fetch Earth's pole and the orbit of the Earth-Moon barycenter from "
         "Horizons for five "
         "dates, 2000 to 2100, and check the tilt of date against ERFA's "
         "true obliquity (1 arcsecond allowance), then measure the monthly "
         "wobble of Earth's own orbit. Needs the internet, takes a minute or "
         "two, writes nothing. Run after any change to earth_pole_of_date.py "
         "or when Horizons may have changed; paste its output into the chat.",
         SCRIPT_DIR,
         True),
        ("Export Orbit Cache",
         "export_orbit_cache.py",
         "Phase 1b devtool: read the local orbit caches (read-only) and write "
         "web-servable orbit/position files for the interactive gallery.",
         SCRIPT_DIR,
         True),
        ("Horizons Check -- everything, now",
         "horizons_check.py",
         "The Horizons Check for EVERY keyed object, fetched period and "
         "spacecraft data sheet at once, whatever their dates (L-266, "
         "Tony's request of 2026-10-20). The Horizons Check in the "
         "maintenance run asks only what is due, each part every 30 days, "
         "so on most days it asks JPL nothing; this button is for when you "
         "want everything confirmed today. It records the answers the same "
         "way, so each date starts again from today. Needs the internet "
         "and takes a few minutes; if JPL cannot be reached it says "
         "UNREACHABLE and asks nothing more.",
         SCRIPT_DIR,
         True,
         ["--all"]),
        ("Path Plan -- every path, now",
         "path_plan.py",
         "The Path Plan for EVERY served spacecraft at once, whatever its "
         "date, with no time limit (L-443). The Path Plan in the "
         "maintenance run makes only what is due, every 30 days, and "
         "starts nothing new after 10 minutes, so a long first plan is "
         "spread over several runs; this button makes them all now: when "
         "a spacecraft is newly keyed, or the rule plans are made by "
         "changes. It prints every flyby, arrival, departure and pass of "
         "the Sun it finds in JPL's positions, a line as it goes, and saves "
         "each plan as it is made. Needs the internet; making all twelve "
         "asks JPL a few hundred questions and takes about half an hour.",
         SCRIPT_DIR,
         True,
         ["--all", "--no-limit"]),
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
# CARD LINES (L-440)
# ============================================================
# One short line per card, at most twelve words, saying what the
# tool does. The card shows it; the paragraph above opens under
# "+ more" (Tony's choice, 2026-10-13). Keyed (group, label), so a
# button added to LAUNCH_GROUPS needs its line added here too.
# Dashboard Parity (test_dashboard_parity.py) fails on a card with
# no line, a line over twelve words, and a line for no card. Each
# line was written from the script's own docstring, not from the
# paragraph alone.

CARD_LINES = {
    ("Solar System",
     "Paloma's Orrery"):
        "The 3D solar system: planets, comets, asteroids and spacecraft, by date.",
    ("Solar System",
     "Orbital Construction"):
        "Shows step by step how six orbital elements build an orbit.",
    ("Earth System",
     "Earth System Viewer"):
        "A hub window of climate data plots and planetary boundaries.",
    ("Earth System",
     "Google Earth Controller"):
        "Pick and open the climate KMZ layers in Google Earth Pro.",
    ("Earth System",
     "Earth System Generator"):
        "Builds the climate layers: a Plotly preview and a Google Earth KMZ.",
    ("Earth System",
     "Food Insecurity Generator"):
        "Builds Sudan's IPC food-insecurity layer for Google Earth from IPC data.",
    ("Earth System",
     "Food Insecurity Controller"):
        "The Google Earth controller, opened with the food-insecurity layers loaded.",
    ("Stars",
     "Star Visualization"):
        "HR diagrams, 3D stellar neighborhoods and planetarium views of nearby stars.",
    ("Daily Run",
     "Daily Run -- everything indented below"):
        "The website's daily routine: guest book, pulls, cache build, checks.",
    ("Daily Run",
     "Guest Book Updater"):
        "Approve, decline or defer each new guest book message; write entries.",
    ("Daily Run",
     "Pulls From The Orrery"):
        "Brings the orrery's exports in before the build; stops if one fails.",
    ("Daily Run",
     "Cache Builder"):
        "Fetches from JPL, checks, and swaps in the website's new served cache.",
    ("Daily Run",
     "Gallery Maintenance Run -- offline"):
        "Every website check that needs no network; run before you commit.",
    ("Gallery -- checks and data",
     "Gallery Maintenance Run -- offline"):
        "Every website generator and check that needs no network, in one run.",
    ("Gallery -- checks and data",
     "Daily Run Steps"):
        "Fails if any script the Daily Run calls is missing.",
    ("Gallery -- checks and data",
     "Guest Book Checks"):
        "Both guest book checks: the page's drawing of it and its updater.",
    ("Gallery -- checks and data",
     "Store Editor Suite"):
        "Checks the room-words editor's logic without opening its window.",
    ("Gallery -- checks and data",
     "Store Writer Suite"):
        "Checks the words writer changes only the line asked, refuses the rest.",
    ("Gallery -- checks and data",
     "Module Atlas"):
        "Regenerates the website repo's own module atlas and index.",
    ("Gallery -- checks and data",
     "Horizons Confirmations"):
        "Fails on any served object JPL has not confirmed within 30 days.",
    ("Gallery -- checks and data",
     "Drawn Orbit"):
        "Checks a barycentre orbit is served and drawn around the barycentre.",
    ("Gallery -- checks and data",
     "Artifact 1 Assembler"):
        "Compares the Artifact 1 assembler test's verdicts with their recorded pin.",
    ("Gallery -- checks and data",
     "Cache Builder Suite"):
        "The cache builder's offline tests, JPL mocked: build, swap, roll back.",
    ("Gallery -- checks and data",
     "Cache In Step"):
        "Checks the served cache holds what data/objects_config.json says.",
    ("Gallery -- checks and data",
     "Cache Siblings"):
        "Reports leftover staging and quarantine folders beside the served cache.",
    ("Gallery -- checks and data",
     "Config Mirror -- report only"):
        "Lists what the mirror would write into the config; writes nothing.",
    ("Gallery -- checks and data",
     "Config Mirror Check"):
        "Checks every served number in the config matches the orrery's export.",
    ("Gallery -- checks and data",
     "Constants Export Pull"):
        "Copies the orrery's constants export into the website, noting its commit.",
    ("Gallery -- checks and data",
     "Drawings"):
        "Checks each stored drawing is pulled, served, and tilted as recorded.",
    ("Gallery -- checks and data",
     "Drawings Pull"):
        "Copies the orrery's stored drawings, the Hills cloud's dots, into the website.",
    ("Gallery -- checks and data",
     "Mirror Suite"):
        "Checks the constants mirror's writes and refusals on made-up files.",
    ("Gallery -- checks and data",
     "Objects Export Pull"):
        "Copies the orrery's objects export (names, JPL ids, links) into the website.",
    ("Gallery -- checks and data",
     "Objects Mirror Check"):
        "Lists every object field in the config that differs from the export.",
    ("Gallery -- checks and data",
     "Objects Mirror Suite"):
        "Checks the objects mirror's writes and refusals on made-up files.",
    ("Gallery -- checks and data",
     "Pointer Join"):
        "Sorts the config's links into the orrery's store: served, waiting, outside.",
    ("Gallery -- checks and data",
     "Pole of Date"):
        "Checks the website's copy of Earth's tilt geometry against the orrery's.",
    ("Gallery -- checks and data",
     "Pull Failures"):
        "Proves each pull fails by name with no network, writing nothing.",
    ("Gallery -- checks and data",
     "Arrival"):
        "Checks the Sun and Earth rooms open on the right things.",
    ("Gallery -- checks and data",
     "Collapsed Features"):
        "Sorts every served feature group; fails on one it cannot classify.",
    ("Gallery -- checks and data",
     "Direction Arrows"):
        "Checks each body's direction arrow points its way, inside the view.",
    ("Gallery -- checks and data",
     "Display Figures"):
        "Checks every number in an Earth hover shows only the figures earned.",
    ("Gallery -- checks and data",
     "Drawer Order"):
        "Checks each room's drawer lists shells where each begins.",
    ("Gallery -- checks and data",
     "Drawn Ends"):
        "Checks every drawing starts and stops where its rows say.",
    ("Gallery -- checks and data",
     "Earth Scene Geometry"):
        "Checks the Earth room's tilt, rings, terminator and Moon on recorded data.",
    ("Gallery -- checks and data",
     "Far Lines"):
        "Checks lines far past the view are cut to its edge.",
    ("Gallery -- checks and data",
     "Feature Renderers"):
        "Checks the code that draws every shell, ring, belt and magnetosphere.",
    ("Gallery -- checks and data",
     "Hover Budget"):
        "Counts the lines in every room hover and names the ten longest.",
    ("Gallery -- checks and data",
     "Label Words"):
        "Checks naming a drawer row opens that shell's own words.",
    ("Gallery -- checks and data",
     "Page Framing"):
        "Checks the page's framing helpers give the right axis ranges.",
    ("Gallery -- checks and data",
     "Solar System Drawer"):
        "Checks the Solar System room's drawer does what your design says.",
    ("Gallery -- checks and data",
     "Solar System Figures"):
        "Checks the Solar System room prints distances only to earned digits.",
    ("Gallery -- checks and data",
     "Source List"):
        "Checks the i panel lists sources one to a line, with links.",
    ("Gallery -- checks and data",
     "Sun Shells"):
        "Checks the Sun room's shells are built and shaped as configured.",
    ("Gallery -- checks and data",
     "Typed Facts"):
        "Checks no fact about nature is typed in the rooms' code.",
    ("Gallery -- checks and data",
     "Typed Numbers"):
        "Checks every number in the served words comes from a row.",
    ("Gallery -- checks and data",
     "Gallery Maintenance Run -- live, AFTER a push"):
        "After a push: checks what palomasorrery.com actually serves.",
    ("Gallery -- authoring",
     "Exhibit Store Editor"):
        "A window to edit the words visitors read in each room.",
    ("Gallery -- authoring",
     "Gallery Cleanup"):
        "Finds gallery files no card uses, and deletes them after you confirm.",
    ("Gallery -- authoring",
     "Gallery Editor"):
        "Arrange the gallery's rooms and cards, and edit their details.",
    ("Gallery -- authoring",
     "Gallery JSON Fixer"):
        "Updates older gallery JSON files so the current viewer reads them.",
    ("Gallery -- authoring",
     "Gallery Studio"):
        "Curate an orrery Plotly plot and export it for the gallery.",
    ("Gallery -- authoring",
     "Inspect Staging"):
        "A plain-language report on a dry-run cache build; changes nothing.",
    ("Gallery -- authoring",
     "JSON Converter"):
        "Converts saved orrery HTML plots into lightweight gallery JSON files.",
    ("Gallery -- authoring",
     "Serve Gallery Locally"):
        "Serves the website at localhost:8000 and opens the assembler dev page.",
    ("Maintenance Run",
     "MAINTENANCE RUN -- everything indented below"):
        "Every orrery generator, then every check, with one summary at the end.",
    ("Maintenance Run",
     "Constants Export"):
        "Writes the constants export the website reads, from constants_new.py.",
    ("Maintenance Run",
     "Data Inventory"):
        "Lists the large local data stores in DATA_INVENTORY.md.",
    ("Maintenance Run",
     "Document Index"):
        "Regenerates README.md's table of key documents from their own tags.",
    ("Maintenance Run",
     "Drawings Export"):
        "Writes the Hills cloud's dots to data/drawings/ for the website.",
    ("Maintenance Run",
     "Exact Rows Report"):
        "Lists every place an exact row of constants_new.py is printed.",
    ("Maintenance Run",
     "Horizons Check"):
        "Asks JPL about served objects and periods when due; re-reads sheets.",
    ("Maintenance Run",
     "Ledger Index"):
        "Regenerates the ledger's index from its detail blocks.",
    ("Maintenance Run",
     "Module Atlas"):
        "Regenerates MODULE_ATLAS.md and MODULE_INDEX.md from each module's docstring.",
    ("Maintenance Run",
     "Objects Export"):
        "Writes the objects export the website reads, from celestial_objects.py.",
    ("Maintenance Run",
     "Period Fetch"):
        "Fetches from JPL each served object's missing orbital period.",
    ("Maintenance Run",
     "Path Plan"):
        "Finds each spacecraft path's flybys in JPL's positions, every 30 days.",
    ("Maintenance Run",
     "Path Plan Suite"):
        "Checks the path plan on a made-up solar system; two planted faults.",
    ("Maintenance Run",
     "Skill Manifest"):
        "Regenerates the protocol's skill table from skills/*/SKILL.md.",
    ("Maintenance Run",
     "Builder Marker Join"):
        "Checks the worksheet request builder joins a continued citation line.",
    ("Maintenance Run",
     "Citation Inheritance"):
        "Checks the scanner's rule that a block's citation covers its strings.",
    ("Maintenance Run",
     "Constants Change"):
        "Reports what moved in constants_new.py, and whether its source moved too.",
    ("Maintenance Run",
     "Constants Export Check"):
        "Checks the constants export matches constants_new.py, row by row.",
    ("Maintenance Run",
     "Constants Relations"):
        "Checks how constants relate: derivations, orderings, completeness.",
    ("Maintenance Run",
     "Cross-Check Annotations"):
        "Checks the grammar and scoring of cross-check annotations.",
    ("Maintenance Run",
     "Dashboard Parity"):
        "Checks run steps against buttons, short lines, and the search.",
    ("Maintenance Run",
     "Derived Figures"):
        "Checks a derived constant claims no more figures than its inputs.",
    ("Maintenance Run",
     "Dimensions"):
        "Checks each derived constant's unit follows from its arithmetic.",
    ("Maintenance Run",
     "Domain Split"):
        "Checks the scanner's Tier-1 total prints with its split by domain.",
    ("Maintenance Run",
     "Drawings Export Check"):
        "Checks each stored drawing is exactly what its rows give today.",
    ("Maintenance Run",
     "Earth Pole of Date"):
        "Checks Earth's tilt of date offline, against ERFA, with its fallback.",
    ("Maintenance Run",
     "Exact Rows by the Count"):
        "Fails where a printed exact row gives no print count.",
    ("Maintenance Run",
     "Extractor Pins"):
        "Checks the citation filter still keeps and drops the same numbers.",
    ("Maintenance Run",
     "Hills Cloud Sampler"):
        "Checks the Hills cloud's frame, Fig. 3 reading and tilt, faults planted.",
    ("Maintenance Run",
     "Horizons Check Suite"):
        "The Horizons Check on recorded answers, planted mistakes caught.",
    ("Maintenance Run",
     "Horizons Confirmations"):
        "Fails on anything JPL has not confirmed within 30 days.",
    ("Maintenance Run",
     "Maintenance Report"):
        "Checks the run's summary names each file whose Tier-1 count rose.",
    ("Maintenance Run",
     "Objects Export Check"):
        "Checks the objects export matches celestial_objects.py, entry by entry.",
    ("Maintenance Run",
     "Orbit Cache"):
        "Tests orbit cache loading, saving, conversion and repair.",
    ("Maintenance Run",
     "Orbit Markers"):
        "Checks each orbit's centre, its marker dates, and its hover digits.",
    ("Maintenance Run",
     "Period Fetch Suite"):
        "Checks the period fetch on recorded answers; twelve planted faults.",
    ("Maintenance Run",
     "Position Digits"):
        "Checks the body hover prints only the digits JPL's errors earn.",
    ("Maintenance Run",
     "Provenance Scanner"):
        "Scans for numbers that need a source; writes PROVENANCE_AUDIT.md.",
    ("Maintenance Run",
     "Reset Completeness"):
        "Checks the orrery's Reset button returns every control to its default.",
    ("Maintenance Run",
     "Row Shape"):
        "Checks each constants_new.py value fits on its assignment's own line.",
    ("Maintenance Run",
     "Scanner Recognition 1d/1e"):
        "Checks the scanner accepts a real citation and refuses a fake one.",
    ("Maintenance Run",
     "Scanner Row Run"):
        "Checks the scanner reads each row's citation from its own comments.",
    ("Maintenance Run",
     "Skill Headers"):
        "Checks every skill header reads the way the Settings uploader reads it.",
    ("Maintenance Run",
     "Status Lines"):
        "Checks the Status line grammar on every constants_new.py row.",
    ("Maintenance Run",
     "Worksheet Checker"):
        "Reports whether each worksheet records what its cross-check annotation claims.",
    ("Maintenance Run",
     "Worksheet Checker Tests"):
        "Checks each layer of the worksheet checker can actually fail.",
    ("Maintenance Run",
     "Worksheet Key Round Trip"):
        "Checks every annotated site's key resolves back to that site.",
    ("Tools and Caches",
     "Add Module Docstrings"):
        "Adds the Role and Domain tags to module docstrings; touches no code.",
    ("Tools and Caches",
     "Animation HTML Tool"):
        "Measures a saved animation's traces, frames and payload size.",
    ("Tools and Caches",
     "Climate Cache Manager"):
        "Updates the climate data caches safely, with validation and rollback.",
    ("Tools and Caches",
     "Create Ephemeris Database"):
        "Rebuilds satellite_ephemerides.json from idealized_orbits.py and Horizons files.",
    ("Tools and Caches",
     "Dependency Trace"):
        "Shows which modules a module uses, and which use it.",
    ("Tools and Caches",
     "Earth Pole Live Check"):
        "Asks Horizons for Earth's pole on five dates and checks the tilt.",
    ("Tools and Caches",
     "Export Orbit Cache"):
        "Writes web-servable orbit files from the local orbit caches.",
    ("Tools and Caches",
     "Horizons Check -- everything, now"):
        "Asks Horizons about every served object now, not only what's due.",
    ("Tools and Caches",
     "Path Plan -- every path, now"):
        "Makes every spacecraft's path plan now, with no time limit.",
    ("Tools and Caches",
     "Osculating Cache Manager"):
        "Loads and reports on the osculating orbital elements cache.",
    ("Tools and Caches",
     "SIMBAD Query Manager"):
        "Tests SIMBAD queries on a few stars, with rate limits and retries.",
    ("Tools and Caches",
     "Verify Orbit Cache"):
        "Backs up, validates and repairs orbit_paths.json.",
    ("Tools and Caches",
     "VOT Cache Manager"):
        "Checks the VizieR VOT cache files are intact.",
    ("Tools and Caches",
     "Worksheet Request Builder"):
        "Writes the cross-check request sent out to another model.",
}


def card_line(group_name, label):
    """The short line for a card, or "" when it has none yet."""
    return CARD_LINES.get((group_name, label), "")


def search_words(query):
    """The words of a search, case folded, in the order typed."""
    return (query or "").casefold().split()


def words_in(words, *texts):
    """True when every word appears somewhere in the texts, in any order.

    Each word is matched on its own, as a piece of text, so "pull" also
    finds "pulls" and the order the words are typed in does not matter
    (Tony, 2026-10-14: "objects export pull = pull objects export").
    No words matches nothing; the caller shows everything for an empty
    box.
    """
    if not words:
        return False
    hay = " ".join(t.casefold() for t in texts if t)
    return all(w in hay for w in words)


def card_matches(query, group_name, entry):
    """True when every word of `query` is on the card: its group's name,
    its own name, its short line (L-440) or its "+ more" paragraph."""
    return words_in(search_words(query), group_name, entry[0],
                    card_line(group_name, entry[0]), entry[2])


def matching_groups(query, groups):
    """What a search draws: [(group name, entries)], headings kept.

    Each word is matched on its own, anywhere on the card, in any order
    (Tony, 2026-10-14). So one word finds exactly what it found before,
    and each word added narrows the list rather than emptying it: "I
    usually use only one word to avoid getting no results with word
    combinations. With order insensitive, I would actually narrow the
    search but still find results."

    A group whose own name holds every word comes whole: somebody typing
    a category name means the category ("stars", 2026-09-19).
    """
    words = search_words(query)
    out = []
    for name, entries in groups.items():
        if not words or words_in(words, name):
            drawn = list(entries)
        else:
            drawn = filter_entries(
                entries, lambda e, g=name: card_matches(query, g, e))
        if drawn:
            out.append((name, drawn))
    return out


def entry_indented(entry):
    """True for a card the runner above it already runs."""
    return (not isinstance(entry, str) and len(entry) > 6
            and bool(entry[6]))


def filter_entries(entries, keep):
    """The entries for which keep() is true, with their headings.

    A heading is kept when a kept card falls under it: its cards
    run to the next heading or to the first card that is not
    indented. So a search shows a match under its own heading,
    and a heading with no match is not drawn (L-440).
    """
    out = []
    pending = None
    for entry in entries:
        if isinstance(entry, str):
            pending = entry
            continue
        if not entry_indented(entry):
            pending = None
        if keep(entry):
            if pending is not None:
                out.append(pending)
                pending = None
            out.append(entry)
    return out


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
    "Daily Run": "",
    "Gallery -- checks and data": "",
    "Gallery -- authoring": "",
    "Maintenance Run": "",
    "Tools and Caches": "",
}

# The groups whose buttons audit THIS repository. The heading carries a
# "Running from:" reminder for these, because several copies of the repo
# exist -- sandbox, clean repo, cloud snapshots -- and running against
# the wrong one produces misleading results. Split out of the single
# "Developer Tools" test when that group became two (L-341).
REPO_AUDIT_GROUPS = ("Maintenance Run", "Tools and Caches")


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
        """The search row, then the launch groups under it.

        The groups are drawn into their own container frame so that a
        search can throw them away and draw them again without touching
        the header, the resources section or the footer, which are
        packed into _main_frame before and after this.
        """
        self._build_launch_search()

        self._launch_container = ctk.CTkFrame(self._main_frame,
                                              fg_color="transparent")
        self._launch_container.pack(fill="x")

        self._render_launch("")

    def _build_launch_search(self):
        """A search box above the groups, and a line saying what it found.

        It searches ON DEMAND -- Find, or Enter -- and not while you
        type. See _search_hint for why.

        WHY A FILTER AND NOT A FLAT RESULT LIST. A match is shown in its
        own group, under that group's own heading, rather than in one
        undifferentiated list. Finding the button is half the job; the
        other half is learning WHERE it lives, so that the next time you
        do not need the search at all. A flat list answers the first
        question every time and never answers the second. (Tony's
        choice, 2026-09-19, L-341.)

        It searches the description as well as the name. The
        descriptions in this file are long and specific, which makes
        them the part worth searching: the tool that pulls the orrery's
        export is called "Constants Export Pull", and somebody looking
        for it is at least as likely to type "gallery numbers" or
        "sha" as to type its name.
        """
        row = ctk.CTkFrame(self._main_frame, fg_color="transparent")
        row.pack(fill="x", padx=20, pady=(16, 0))

        ctk.CTkLabel(
            row, text="Find a tool",
            font=FONT_SECTION, text_color=COLOR_TEXT, anchor="w"
        ).pack(side="left")

        self._search_var = ctk.StringVar()
        entry = ctk.CTkEntry(
            row, textvariable=self._search_var, width=280,
            placeholder_text="name or description, e.g. export"
        )
        entry.pack(side="left", padx=(12, 0))
        entry.bind("<Return>", lambda _event: self._run_search())

        find = ctk.CTkButton(
            row, text="Find", width=64, font=FONT_DESC,
            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,
            command=self._run_search
        )
        find.pack(side="left", padx=(8, 0))

        clear = ctk.CTkButton(
            row, text="Clear", width=64, font=FONT_DESC,
            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,
            command=self._clear_search
        )
        clear.pack(side="left", padx=(8, 0))

        self._search_status = ctk.CTkLabel(
            row, text="", font=FONT_DESC, text_color=COLOR_TEXT_DIM,
            anchor="w"
        )
        self._search_status.pack(side="left", padx=(12, 0))

        self._rendered_query = ""
        self._search_var.trace_add("write", lambda *_: self._search_hint())

    def _run_search(self):
        """Filter the groups to what is in the box. Find, or Enter."""
        self._render_launch(self._search_var.get())

    def _clear_search(self):
        """Empty the box and bring every group back."""
        self._search_var.set("")
        self._render_launch("")

    def _search_hint(self):
        """Typing changes the box; it does not redraw the list.

        The list is redrawn on Find or on Enter, not on every keystroke
        -- Tony's ruling of 2026-09-19. Two reasons, and the second is
        the one that matters to him. A redraw destroys and rebuilds all
        sixty-odd cards, which is real work to do once per letter. And
        the groups shuffle and vanish under the cursor while a word is
        still half typed, which is the opposite of a page you can scan.

        What this leaves is a screen that can disagree with the box, so
        this says so. It is the only thing a keystroke changes, and it
        is one short label rather than the whole section.
        """
        if self._search_var.get().strip().lower() == self._rendered_query:
            return
        self._search_status.configure(text="press Find, or Enter")

    def _launch_entry_total(self):
        """How many launchable buttons exist. Bare strings are headings."""
        return sum(1 for entries in LAUNCH_GROUPS.values()
                   for entry in entries if not isinstance(entry, str))

    def _render_launch(self, query):
        """Draw the groups, filtered by `query`.

        An empty query draws everything, which is the ordinary view. A
        non-empty one draws only the groups that still have a match, and
        only the matching buttons inside them. A group with nothing left
        is not drawn at all, so the headings that remain are themselves
        the answer to "where does this live". A heading inside a group
        is kept when a card under it matches, so a match is also shown
        under its own heading (L-440).
        """
        for child in self._launch_container.winfo_children():
            child.destroy()

        needle = (query or "").strip().lower()
        self._rendered_query = needle
        shown = 0

        # The matching itself is matching_groups(), at module level,
        # where Dashboard Parity tests it (L-440, 2026-10-14): each word
        # on its own, anywhere on the card, in any order; a group whose
        # name holds every word comes whole (the GROUP NAME rule: typing
        # "stars" found nothing before it, 2026-09-19).
        for group_name, drawn in matching_groups(needle, LAUNCH_GROUPS):
            shown += sum(1 for e in drawn if not isinstance(e, str))
            self._build_group(group_name, drawn)

        if not needle:
            self._search_status.configure(
                text="%d buttons in %d groups"
                     % (self._launch_entry_total(), len(LAUNCH_GROUPS)))
        elif shown:
            self._search_status.configure(
                text="%d of %d match \u2014 shown under their own headings"
                     % (shown, self._launch_entry_total()))
        else:
            self._search_status.configure(
                text="nothing matches \u2014 try fewer letters, or Clear")

    def _build_group(self, group_name, entries):
        """One group heading, its divider, and its cards."""
        section_frame = ctk.CTkFrame(self._launch_container,
                                     fg_color="transparent")
        section_frame.pack(fill="x", padx=20, pady=(16, 4))

        symbol = SECTION_SYMBOLS.get(group_name, "")
        ctk.CTkLabel(
            section_frame,
            text=f"{symbol}  {group_name}",
            font=FONT_SECTION, text_color=COLOR_TEXT,
            anchor="w"
        ).pack(side="left")

        # The repo-auditing groups remind the user which codebase
        # directory these tools examine. Multiple copies of the repo
        # exist (sandbox, clean repo, cloud snapshots) and running
        # against the wrong one produces misleading results.
        if group_name in REPO_AUDIT_GROUPS:
            ctk.CTkLabel(
                section_frame,
                text=f"  Running from: {SCRIPT_DIR}",
                font=FONT_DESC, text_color=COLOR_TEXT_DIM,
                anchor="w"
            ).pack(side="left", padx=(8, 0))

        div = ctk.CTkFrame(self._launch_container, fg_color=COLOR_DIVIDER,
                           height=1)
        div.pack(fill="x", padx=20, pady=(0, 8))

        cards_frame = ctk.CTkFrame(self._launch_container,
                                   fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 4))

        # The frame holding the cards under the current heading, or None
        # outside any heading. A heading's cards run to the next heading
        # or to the first card that is not indented (the live runner at
        # the foot of the website group), whichever comes first.
        section = None
        for i, entry in enumerate(entries):
            # A bare string is a HEADING inside the group, not a
            # card. The maintenance runner prints GENERATORS then
            # CHECKERS, and the indented list here is that same
            # list, so it reads the same way. Alphabetical order
            # within each half is Tony's, 2026-09-12: without the
            # two labels a sorted run of twenty buttons gives no
            # clue where one kind stops and the other starts.
            if isinstance(entry, str):
                section = self._build_indent_heading(cards_frame, entry)
                continue
            name, script, desc = entry[0], entry[1], entry[2]
            base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR
            interactive = entry[4] if len(entry) > 4 else False
            args = entry[5] if len(entry) > 5 else None
            indent = entry[6] if len(entry) > 6 else False
            if not indent:
                section = None
            parent = section if section is not None else cards_frame
            self._build_launch_card(parent, group_name, name, script, desc,
                                    base_dir, interactive, args, i,
                                    indent)

    def _build_indent_heading(self, parent, text):
        """A heading inside a group, which folds the cards under it.

        Drawn for a bare string in a LAUNCH_GROUPS list. Not a card: it
        names which part of the group the buttons below it belong to,
        and clicking it hides or shows them (Tony, 2026-10-13, L-440).
        "-" in front means open, "+" means folded. Every heading starts
        OPEN when the dashboard launches, so what a runner runs stays
        visible, which is Tony's ruling of 2026-08-12; folding is for
        the moment, and is not remembered. Returns the frame the cards
        under it are drawn into.
        """
        state = {"open": True}
        heading = ctk.CTkButton(
            parent, text="-  " + text, anchor="w",
            font=FONT_DESC, text_color=COLOR_TEXT_DIM,
            fg_color="transparent", hover_color=COLOR_SURFACE_HOVER,
            height=24, corner_radius=6
        )
        heading.pack(anchor="w", padx=(22, 0), pady=(10, 2))
        section = ctk.CTkFrame(parent, fg_color="transparent")
        section.pack(fill="x")

        def toggle():
            if state["open"]:
                section.pack_forget()
                heading.configure(text="+  " + text)
            else:
                section.pack(fill="x", after=heading)
                heading.configure(text="-  " + text)
            state["open"] = not state["open"]

        heading.configure(command=toggle)
        return section

    def _build_launch_card(self, parent, group_name, name, script, desc,
                           base_dir, interactive, args, index,
                           indent=False):
        """Individual launch card: name, script, short line, paragraph.

        `indent` marks a tool that the maintenance runner already covers.
        Indenting rather than removing was Tony's ruling of 2026-08-12:
        the individual entries stay launchable, and staying visible is how
        the automation's contents remain known instead of disappearing
        behind one button. The runner sits directly above its indented
        group.

        The card (L-440, Tony's choice of option B, 2026-10-13): the name;
        the repository and script it runs, in small type, so the mapping
        is visible without hovering; the short line from CARD_LINES; and
        the paragraph, opened in place by "+ more". A card with no short
        line yet shows its paragraph, as every card did before, so
        nothing is hidden, and Dashboard Parity names the card. Text
        wraps to the column's width, and the Launch button is packed
        first, so a narrow window never pushes the button off the card.
        """
        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,
                            corner_radius=10)
        card.pack(fill="x", pady=4, ipady=4,
                  padx=(28, 0) if indent else 0)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=6)

        # Right side first: the launch button keeps its place whatever
        # the window's width.
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
            target = launch_target_label(script, base_dir, args)
        else:
            target = "Not found: %s" % script_path
        Tooltip(btn, target)

        # Left side: name, script, short line, paragraph.
        text_frame = ctk.CTkFrame(inner, fg_color="transparent")
        text_frame.pack(side="left", fill="x", expand=True)

        title_row = ctk.CTkFrame(text_frame, fg_color="transparent")
        title_row.pack(anchor="w", fill="x")
        ctk.CTkLabel(
            title_row, text=name,
            font=FONT_BUTTON, text_color=COLOR_TEXT, anchor="w"
        ).pack(side="left")

        ctk.CTkLabel(
            text_frame, text=target,
            font=FONT_SCRIPT, text_color=COLOR_TEXT_DIM, anchor="w",
            justify="left"
        ).pack(anchor="w")

        wrapped = []
        short = card_line(group_name, name)
        para = ctk.CTkLabel(
            text_frame, text=desc,
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w",
            wraplength=600, justify="left"
        )
        wrapped.append(para)
        if short:
            line = ctk.CTkLabel(
                text_frame, text=short,
                font=FONT_DESC, text_color=COLOR_TEXT, anchor="w",
                wraplength=600, justify="left"
            )
            line.pack(anchor="w")
            wrapped.insert(0, line)
            state = {"open": False}
            more = ctk.CTkButton(
                title_row, text="+ more", width=60, height=22,
                font=FONT_DESC, fg_color="transparent",
                hover_color=COLOR_BUTTON_HOVER, text_color=COLOR_LINK
            )

            def toggle(p=para, s=state, m=more):
                if s["open"]:
                    p.pack_forget()
                    m.configure(text="+ more")
                else:
                    p.pack(anchor="w", pady=(4, 0))
                    m.configure(text="- less")
                s["open"] = not s["open"]

            more.configure(command=toggle)
            more.pack(side="left", padx=(10, 0))
        else:
            para.pack(anchor="w")

        last = {"width": None}

        def rewrap(event, labels=wrapped, last=last):
            # CTk scales a wraplength by the display's scaling, while the
            # event gives real pixels, so divide the scaling back out.
            if event.width == last["width"]:
                return
            last["width"] = event.width
            for lab in labels:
                try:
                    scale = lab._get_widget_scaling()
                except Exception:
                    scale = 1.0
                lab.configure(wraplength=max(200, int((event.width - 8)
                                                      / scale)))

        text_frame.bind("<Configure>", rewrap, add="+")

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
        from utc_clock import utc_now   # L-504: the clock read as UTC
        timestamp = utc_now().strftime("%H:%M:%S UTC")
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
