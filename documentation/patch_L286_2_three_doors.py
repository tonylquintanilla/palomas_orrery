"""
patch_L286_2_three_doors.py -- LEDGER_CONSOLIDATED.md and
documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md

Second ledger patch from the 2026-09-04 design session. Built on
palomas_orrery d1b4d3ee1bab3b536145cdcd1e9715f67699625d at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
the SHA that carries patch_L286_1. Source: HANDOFF 2026-09-04 ("the
doors close, the rooms get four levels, the editor gets a design"),
decisions 10, 11, 12 and 14.

What it does (two files, one transaction):
  LEDGER_CONSOLIDATED.md
  1. Header stamp.
  2. L-282: door count TWO -> THREE. Earth System is a door, not a
     special exhibit under Earth. Recorded visibly as a correction.
  3. L-282: the L-283 consequences bullet, resolved.
  4. L-283: accent list realigned -- Missions and Interactive Wing
     accents dropped; construction material kept for rooms the braid
     has not reached.
  5. L-286: special-exhibit line corrected; room-shape rule restated
     as 16:9 / 9:16, phone only, desktop unchanged.
  6. L-287: `climate` routes to the Earth System DOOR; the shape field
     becomes 16:9 / 9:16; the desktop/mobile collapse (one card per
     exhibit, two file slots) added as a fourth change; the
     "table in conversation" replaced by "mapping in the editor"
     (Tony's ruling).
  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
  7. Section 5a step 2 and three other lines that name "the hall
     (L-280)" as the next step; now the lobby, rooms and editor
     (L-282, L-286, L-287). Status v22 -> v23; Last updated stamped.

HOW TO RUN: save this file into the palomas_orrery repo root, next to
LEDGER_CONSOLIDATED.md. Open it in VS Code and click Run.
    python patch_L286_2_three_doors.py
Success prints `base ok` for both files, one `ok` line per edit, and
`patch applied`. Failure prints one ERROR or ANCHOR FAIL line and
writes NOTHING to either file. Undo is Discard Changes in GitHub
Desktop.

AFTER IT RUNS: run ledger_index.py from the repo root, then archive
this script to documentation/.

Permanent part: the ledger and master plan text. The script is
one-shot and refuses to run twice.

Written September 4, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "8d073838c0367724a501600b64f8f792"     # LF-normalized @ d1b4d3ee
PLAN = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
PLAN_MD5 = "65f1c98c6c2f28fd579792b9ec8aace9"       # LF-normalized @ d1b4d3ee

# ===========================================================================
# LEDGER edits
# ===========================================================================

L_STAMP_OLD = b"""L-281 note; L-286 and L-287 opened), built on 5955a405.
Review and RICE update Tony 6-21-2026"""
L_STAMP_NEW = b"""L-281 note; L-286 and L-287 opened), built on 5955a405.
Module updated: September 4, 2026 with Anthropic's Claude Fable 5.1
(L-282 door count two -> three, Earth System is a door; L-283 accents
realigned; L-286 shape rule 16:9 / 9:16 phone only; L-287 gains the
desktop/mobile collapse), built on d1b4d3ee.
Review and RICE update Tony 6-21-2026"""

# --- L-282 -----------------------------------------------------------------

L282_DOORS_OLD = b"""  - **Doors are organized by SUBJECT, not by content type.** Two doors:
    SOLAR SYSTEM and STARS. No Missions door, no Earth System door, no
    Interactive Wing door. Tony: "modern museums blend permanent with
    interactive." Each door carries its static cards and whatever live
    scenes exist for that subject, together.
  - **Earth System is a SPECIAL EXHIBIT inside the Earth room**, under
    Solar System. **Orbital Mechanics is a special exhibit in the Solar
    System room.** A special exhibit is a room that hangs off its parent
    like a side gallery; same chrome, same breadcrumb (L-286)."""
L282_DOORS_NEW = b"""  - **Doors are organized by SUBJECT, not by content type.** THREE
    doors: SOLAR SYSTEM, EARTH SYSTEM and STARS. No Missions door, no
    Interactive Wing door. Tony: "modern museums blend permanent with
    interactive." Each door carries its static cards and whatever live
    scenes exist for that subject, together.
    [CORRECTED 2026-09-04, same day, later in the session. The first
    write said TWO doors, with Earth System as a special exhibit under
    the Earth room. Tony's concern: its rooms (heating, heatdome, food,
    ...) would sit at level 4 and get buried. The weight settled it:
    climate is 76 of 148 cards, half the collection, and carries the
    museum's only finished sentence. As a door its rooms land at level
    2, `earth: heatdome`, two taps from the lobby. The four-level rule
    is a navigation ceiling, not a taxonomy.]
  - **The Earth room under Solar System keeps its own content** --
    shells, the Moon, Artemis -- and carries ONE card that is a doorway
    into the Earth System wing. A cross-link, not a copy.
  - **Orbital Mechanics is a special exhibit in the Solar System
    room.** A special exhibit is a room that hangs off its parent like
    a side gallery; same chrome, same breadcrumb (L-286)."""

L282_L283_OLD = b"""  - **Consequences for L-283:** the accent list there still names
    Missions (steel grey) and an under-construction material for the
    Interactive Wing. Neither is a door now. Tony-action (decide):
    drop both accents, or keep the construction material for rooms the
    braid has not reached. Not changed by this patch."""
L282_L283_NEW = b"""  - **L-283 realigned 2026-09-04:** the Missions accent is dropped
    (missions live inside their body's room and take its accent); the
    Interactive Wing accent is dropped as a wing accent and KEPT as the
    material for a room the braid has not reached. Earth System's
    blue-green stands, since it is a door after all."""

# --- L-283 -----------------------------------------------------------------

L283_ACCENT_OLD = b"""  - One accent per wing, used sparingly -- a hairline on the door, the
    placard rule, the header position, nowhere else. Warm gold Solar
    System; blue-green Earth System; cool violet Stars and Exoplanets;
    steel grey Missions; an unfinished material (raw copper or
    hazard-tape ochre) for the Interactive Wing while under
    construction -- the scaffolding announces itself without a banner."""
L283_ACCENT_NEW = b"""  - One accent per DOOR, used sparingly -- a hairline on the door, the
    placard rule, the header position, nowhere else. Warm gold Solar
    System; blue-green Earth System; cool violet Stars. A room takes
    its door's accent; a mission takes its body's room. An unfinished
    material (raw copper or hazard-tape ochre) marks any ROOM the
    braid has not reached yet -- the scaffolding announces itself
    without a banner.
    [REALIGNED 2026-09-04 to the three-door design in L-282. The
    original read "one accent per wing" and listed steel grey for a
    Missions door and the construction material for an Interactive
    Wing door; neither is a door now. The construction material moves
    from a door to a room state.]"""

# --- L-286 -----------------------------------------------------------------

L286_SPECIAL_OLD = b"""- **Special exhibits are rooms too.** Earth System under Earth; Orbital
  Mechanics under the Solar System overview. Same chrome, same
  breadcrumb: `solar: Earth: Earth System`."""
L286_SPECIAL_NEW = b"""- **Special exhibits are rooms too.** Orbital Mechanics under the Solar
  System overview: `solar: Orbital Mechanics`. Same chrome, same
  breadcrumb. [CORRECTED 2026-09-04: the first write also listed Earth
  System under Earth. Earth System is a DOOR (L-282); its rooms are
  `earth: heating`, `earth: heatdome`, and so on, at level 2.]"""

L286_SHAPE_OLD = b"""  - Room-shape rule (Tony's breadcrumb 2026-09-03): Earth System
    exhibits need horizontal room; in portrait a wide room is SWEPT
    sideways while placard and drawer stay put. A room declares its
    shape (wide or square) in its config; the chrome never assumes the
    plot fits the viewport; in wide rooms the plot's own horizontal
    drag is given to the sweep."""
L286_SHAPE_NEW = b"""  - Room-shape rule (Tony's breadcrumb 2026-09-03; values and scope
    settled 2026-09-04): Earth System exhibits need horizontal room;
    in portrait a wide room is SWEPT sideways while placard and drawer
    stay put. Each CARD declares its shape, one of two values, 16:9 or
    9:16, and the shape governs the PHONE ONLY -- Tony: "the current
    view on desktop works," so desktop is unchanged whatever the card
    carries. On a phone: 16:9 sweeps sideways for a 2D plot and scales
    to fit for a 3D scene (a 3D file stores a camera, not a picture, so
    it re-frames without distortion); 9:16 shows as it does today.
    Sweep was chosen over an Instagram-style card flip because the
    exhibits that run out of room are time series, and sweeping along
    a time axis is a reading gesture; flip suits separate complete
    faces, which a continuous plot is not. The chrome never assumes
    the plot fits the viewport; in a swept room the plot's own
    horizontal drag is given to the sweep -- the one piece here that
    intercepts Plotly's drag layer and needs Mode 5 on a real phone
    before the rule is trusted."""

# --- L-287 -----------------------------------------------------------------

L287_CHANGES_OLD = b"""- **What changes.** Three things, one migration:
  - Each card gets a ROOM PATH in place of category + subcategory:
    `solar_system/earth`, `solar_system/earth/earth_system`,
    `stars/exoplanets`. One-time scripted migration of
    `gallery_metadata.json`, driven by an explicit table from the nine
    raw categories to rooms (Tony-action (decide): approve the table
    before it runs). `inner_planets` and `outer_planets` split by body;
    `missions` split by TARGET body (the phase rule, L-282); `climate`
    -> Earth System special exhibit; `stellar`, `exoplanets` -> Stars.
  - `gallery_config.json` becomes the ROOM TREE: doors, rooms, exhibits,
    each with full label, SHORT label (for the breadcrumb, L-286), color
    and shape (wide or square). Lobby, breadcrumb and editor all read
    the same tree, so a rename lands everywhere. `index.html` and
    `json_converter.py` keep reading the same two files."""
L287_CHANGES_NEW = b"""- **What changes.** Four things, one migration:
  - **Desktop and mobile collapse to ONE card per exhibit with two
    file slots** (landscape file, portrait file). Measured at gallery
    `e414af13`: 148 cards, 105 distinct titles; 33 exhibits appear
    twice, as a `_gallery.json` landscape card and a `_mobile.json`
    portrait card with the same title and category. Those 33 pairs
    become 33 cards with two slots; the rest become cards with one.
    Where a card has one file the page shows it in both orientations;
    where it has two the page picks by screen width, which
    `index.html` already detects (line 1880 at `e414af13`). The
    Desktop/Mobile toggle goes away (L-282 proposal 4). `mode` values
    today: portrait 58, landscape 38, both 28, absent 24 (absent reads
    as landscape, line 1912). [Added 2026-09-04, Tony's question "can
    we collapse them?"]
  - Each card gets a ROOM PATH in place of category + subcategory:
    `solar_system/earth`, `earth_system/heatdome`, `stars/exoplanets`.
    A one-shot script does the MECHANICAL half only: pairs the 33
    duplicates, moves every card into the storage room, and writes the
    three doors with their planet rooms, empty. **The category-to-room
    mapping is then done IN THE EDITOR, not as a table in
    conversation** -- Tony's ruling 2026-09-04, replacing the table
    the first write proposed. Guidance the editor session will follow:
    `inner_planets` and `outer_planets` go to their body's room;
    `missions` to the TARGET body (the phase rule, L-282); `climate`
    -> the Earth System DOOR, its nine subcategories (heating 31,
    heatdome 18, comets 20, climate 15, narrative 7, general 5,
    acidification 2, food 2, coral 1; 47 cards none) becoming level-2
    rooms one-for-one or regrouped -- Tony-action (decide), "very
    important"; `stellar`, `exoplanets` -> Stars.
  - `gallery_config.json` becomes the ROOM TREE: doors, rooms, exhibits,
    each with full label, SHORT label (for the breadcrumb, L-286) and
    color; each CARD carries its shape, 16:9 or 9:16 (L-286, phone
    only). Lobby, breadcrumb and editor all read the same tree, so a
    rename lands everywhere. `index.html` and `json_converter.py` keep
    reading the same two files; `interactive.html` will read the tree
    for its breadcrumb. Grep all three for `category`, `subcategory`
    and `mode` before changing the schema (Check All Parallel
    Pipelines)."""

L287_GAP_OLD = b"""**Gap:** the category-to-room table (decide); the room-tree schema for
`gallery_config.json`; the migration script; the editor's deeper tree
and move-to-room; the storage-room and featured behaviours; a run on
the real metadata with the result checked in the editor."""
L287_GAP_NEW = b"""**Gap:** the room-tree schema for `gallery_config.json` and the
two-slot card schema for `gallery_metadata.json`; the migration script
(pair, park in storage, write the empty tree); the editor's deeper
tree, move-to-room, two file slots, shape and featured fields; the
consumer sweep in `index.html`, `json_converter.py` and
`interactive.html`; a run on the real metadata with the result checked
in the editor; then Tony's remodel, moving cards out of storage.
Editor layout as designed: room tree on the left (doors, rooms,
exhibits, storage room at the bottom), one card per exhibit on the
right; save writes both files and prints what changed; git is the
backup."""

# ===========================================================================
# MASTER PLAN edits
# ===========================================================================

P_STATUS_OLD = b"""**Status:** v22 -- Phase 2 (solar system assembler) BUILD UNDERWAY;"""
P_STATUS_NEW = b"""**Status:** v23 -- Phase 2 (solar system assembler) BUILD UNDERWAY;"""

P_UPDATED_OLD = b"""**Last updated:** September 3, 2026"""
P_UPDATED_NEW = b"""**Last updated:** September 4, 2026 (v23: Section 5a step 2 realigned
from the hall to the lobby, rooms and editor -- L-280 retired, L-282
rewritten, L-286 and L-287 opened; with Anthropic's Claude Fable 5.1)"""

P_NEXT_OLD = b"""steps: the Sun room's phone controls, the hall (L-280), Earth into the
assembler,"""
P_NEXT_NEW = b"""steps: the Sun room's phone controls, the lobby with its rooms and
editor (L-282, L-286, L-287; the hall, L-280, was retired 2026-09-04),
Earth into the assembler,"""

P_WING_OLD = b"""is designed and recorded in L-280 (door, hall, two rooms, What's New),
L-281 (guest book), L-282 (lobby), L-283 (theme) and L-284 (retire the
social export). Nothing of the wing is built."""
P_WING_NEW = b"""is designed and recorded in L-282 (the lobby: three subject doors,
Solar System, Earth System, Stars, each blending static cards with
live scenes), L-286 (rooms in four levels, breadcrumb), L-287 (the
editor and room tree), L-281 (guest book), L-283 (theme) and L-284
(retire the social export). L-280 (door, hall, two rooms) was retired
2026-09-04: there is no separate interactive wing; live scenes are
cards inside their subject's rooms. Nothing of it is built."""

P_STEP2_OLD = b"""2. **The hall (L-280), designed in conversation first, portrait
   first.** The door card on the main page, the placard, the two
   rooms, the What's New JSON and the rule that shipping patches
   append to it. Until this exists the Sun room is a URL nobody can
   find. The chrome from step 1 is what the hall copies."""
P_STEP2_NEW = b"""2. **The lobby, its rooms and the editor (L-282, L-286, L-287),
   designed 2026-09-04, portrait first.** In build order: the editor
   and room tree first (L-287), so cards can be placed and Tony can
   remodel; then the lobby screen with three doors, What's New and the
   guest book (L-282); then the four-level drill-down and the
   short-name breadcrumb (L-286). Until this exists the Sun room is a
   URL nobody can find. The chrome from step 1 is what the rooms copy.
   [Until v23 this step read "The hall (L-280)": a door card, a hall
   listing interactive rooms, two rooms. Retired 2026-09-04 -- doors
   are by subject and blend static with live, so a hall had no job
   left; its What's New and guest book moved into the lobby.]"""

P_STEP5_OLD = b"""   System Explorer room starts being replaced by interactive planets
   as L-280 rules."""
P_STEP5_NEW = b"""   System Explorer room starts being replaced by interactive planets
   as L-286 rules (carried there from L-280)."""

LEDGER_EDITS = [
    ("ledger: header stamp",                      L_STAMP_OLD,       L_STAMP_NEW),
    ("ledger: L-282 doors two -> three",          L282_DOORS_OLD,    L282_DOORS_NEW),
    ("ledger: L-282 L-283 bullet resolved",       L282_L283_OLD,     L282_L283_NEW),
    ("ledger: L-283 accent list realigned",       L283_ACCENT_OLD,   L283_ACCENT_NEW),
    ("ledger: L-286 special exhibits corrected",  L286_SPECIAL_OLD,  L286_SPECIAL_NEW),
    ("ledger: L-286 shape rule 16:9 / 9:16",      L286_SHAPE_OLD,    L286_SHAPE_NEW),
    ("ledger: L-287 four changes + collapse",     L287_CHANGES_OLD,  L287_CHANGES_NEW),
    ("ledger: L-287 Gap",                         L287_GAP_OLD,      L287_GAP_NEW),
]
PLAN_EDITS = [
    ("plan: status v22 -> v23",                   P_STATUS_OLD,      P_STATUS_NEW),
    ("plan: last updated",                        P_UPDATED_OLD,     P_UPDATED_NEW),
    ("plan: next-steps line",                     P_NEXT_OLD,        P_NEXT_NEW),
    ("plan: wing-is-recorded paragraph",          P_WING_OLD,        P_WING_NEW),
    ("plan: Section 5a step 2",                   P_STEP2_OLD,       P_STEP2_NEW),
    ("plan: Section 5a step 5",                   P_STEP5_OLD,       P_STEP5_NEW),
]


def load(path, expected_md5, already_marker):
    if not os.path.exists(path):
        print(f"ERROR: {path} not found. Run from the palomas_orrery repo root. NOTHING written.")
        sys.exit(1)
    with open(path, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    actual = hashlib.md5(content).hexdigest()
    if actual != expected_md5:
        if already_marker in content:
            print(f"ERROR: patch already applied to {path}. NOTHING written.")
        else:
            print(f"ERROR: BASE MOVED for {path}. md5 {actual} != expected {expected_md5} "
                  f"(content compared LF-normalized). NOTHING written. "
                  f"Undo is Discard Changes in GitHub Desktop.")
        sys.exit(1)
    print(f"base ok: {path} matches d1b4d3ee"
          + (" (the working copy is CRLF)" if was_crlf else ""))
    return content, was_crlf


def check(content, edits):
    for name, old, new in edits:
        if any(b > 0x7F for b in new):
            print(f"ERROR: non-ASCII byte in inserted text for '{name}'. NOTHING written.")
            sys.exit(1)
        n = content.count(old)
        if n != 1:
            print(f"ANCHOR FAIL: '{name}' expected 1 match, got {n}. NOTHING written.")
            sys.exit(1)


def apply(content, edits):
    for name, old, new in edits:
        content = content.replace(old, new)
        print(f"ok  {name}")
    return content


def write(path, content, was_crlf):
    final = content.replace(b"\n", b"\r\n") if was_crlf else content
    with open(path, "wb") as f:
        f.write(final)
    return len(final)


def main():
    ledger, l_crlf = load(LEDGER, LEDGER_MD5, b"door count two -> three")
    plan, p_crlf = load(PLAN, PLAN_MD5, b"**Status:** v23")
    # Every anchor in both files is checked before either file is written.
    check(ledger, LEDGER_EDITS)
    check(plan, PLAN_EDITS)
    ledger = apply(ledger, LEDGER_EDITS)
    plan = apply(plan, PLAN_EDITS)
    n1 = write(LEDGER, ledger, l_crlf)
    n2 = write(PLAN, plan, p_crlf)
    print(f"patch applied ({LEDGER}: {n1} bytes; {PLAN}: {n2} bytes)")
    print("stamps updated: ledger header (built on d1b4d3ee); master plan Status v23 and Last updated")
    print("note: both files held 0 non-ASCII bytes before and after")
    print("not touched: MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md and MASTER_PLAN_CRITICAL_PATH_SUMMARY.md")
    print("  -- both read at d1b4d3ee; neither names the hall or L-280, so nothing there to realign")
    print("NEXT: run ledger_index.py (repo root), then archive this script to documentation/.")


if __name__ == "__main__":
    main()
