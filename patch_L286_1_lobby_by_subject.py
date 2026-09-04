"""
patch_L286_1_lobby_by_subject.py -- LEDGER_CONSOLIDATED.md

Carries the 2026-09-04 lobby design session into the ledger.
Built on palomas_orrery 5955a40550b1356d157460d3288aada900c712c1 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Source: HANDOFF 2026-09-04 (design session: the lobby splits by subject,
not by permanent vs. interactive) plus the same-day conversation that
closed its open questions (Earth System and Orbital Mechanics as special
exhibits, Stars as its own door, the editor as a separate item, the
storage room, short-name breadcrumbs, four levels).

What it does (five edits, one file):
  1. Header stamp for this patch.
  2. L-280 -> DONE. The hall is retired as a screen; its remaining
     scope is named and sent to L-282 and L-286.
  3. L-281 gets a Note: the guest book embeds in the lobby, not the hall.
  4. L-282 rewritten around subject doors (Solar System, Stars), with the
     phase rule, the mixed page model, and Pluto's promotion. Proposals
     2-8 stand as written.
  5. L-286 (rooms, drill-down, breadcrumb, Home) and L-287 (gallery
     editor: room tree, storage room, featured flag) opened.

HOW TO RUN: save this file into the palomas_orrery repo root, next to
LEDGER_CONSOLIDATED.md. Open it in VS Code and click Run.
    python patch_L286_1_lobby_by_subject.py
Success prints one `ok` line per edit and `patch applied (N bytes)`.
Failure prints one ERROR or ANCHOR FAIL line and writes NOTHING.
Undo is Discard Changes in GitHub Desktop.

AFTER IT RUNS: run ledger_index.py (repo root) to regenerate the INDEX zone,
then archive this script to documentation/.

Permanent part: the ledger text. This script is one-shot and refuses
to run twice.

Written September 4, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

FN = "LEDGER_CONSOLIDATED.md"
EXPECTED_MD5 = "2be464ba795d220a7a39ebbbd1532508"   # LF-normalized, @ 5955a405

# ---------------------------------------------------------------------------
# Edits: (anchor_old, new). Each anchor must match EXACTLY once.
# ---------------------------------------------------------------------------

STAMP_OLD = b"""built on af09de62.
Review and RICE update Tony 6-21-2026"""
STAMP_NEW = b"""built on af09de62.
Module updated: September 4, 2026 with Anthropic's Claude Fable 5.1
(L-280 DONE, retired as a screen; L-282 rewritten around subject doors;
L-281 note; L-286 and L-287 opened), built on 5955a405.
Review and RICE update Tony 6-21-2026"""

# --- L-280: retire ---------------------------------------------------------

L280_META_OLD = b"""<!-- L:280 status:OPEN upd:2026-09-03 section:A flag: rice:4/4/80/3 -->"""
L280_META_NEW = b"""<!-- L:280 status:DONE upd:2026-09-04 section:A flag: rice:4/4/80/3 -->
- **RETIRED AS A SCREEN 2026-09-04 (design session; nothing built).**
  Tony's ruling: "modern museums blend permanent with interactive."
  There is no separate Interactive Wing door and no hall. Doors are
  organized by SUBJECT, and a subject's door carries its static cards
  and its live scenes together. Every piece of this item that still
  matters moved rather than died:
  - The door card and the hall's room list -> replaced by the subject
    doors and the room drill-down in L-282 and L-286.
  - The placard in museum voice, the What's New feed and its JSON, and
    the rule that shipping patches append to it -> L-282 (the lobby).
  - The guest-book slot -> L-282; see the Note on L-281.
  - The growth rule (a shipped body appears as a room and in the Sun
    room's drawer) and the room-shape rule (wide rooms swept sideways
    in portrait) -> L-286, as rules of the room, unchanged in content.
  - The premade Solar System Explorer stays reachable under its own
    parameter and is still EVENTUALLY REPLACED as the braid reaches the
    planets; that ruling now lives in L-286.
  The text below is the record of the design this superseded.
"""

L280_GAP_OLD = b"""**Gap:** the door card; the hall (placard, room list, What's New,
guest-book slot); the What's New JSON and the rule that shipping
patches append to it; the room-shape field in the room config.
**Ref:** L-267 (Sun room), L-265 (i panel links), L-281 (guest book),
L-282 (lobby), L-283 (visual theme), L-268 (feature identity);
interactive.html; index.html; gallery_metadata.json;
MASTER_PLAN_INTERACTIVE_GALLERY.md."""
L280_GAP_NEW = b"""**Gap:** none -- move to section C. Scope carried by L-282 and L-286.
**Ref:** L-282 (lobby), L-286 (rooms and breadcrumb), L-287 (editor),
L-267 (Sun room), L-265 (i panel links), L-281 (guest book), L-283
(visual theme), L-268 (feature identity); HANDOFF 2026-09-04 (design
session: the lobby splits by subject); interactive.html; index.html;
gallery_metadata.json; MASTER_PLAN_INTERACTIVE_GALLERY.md."""

# --- L-281: note -----------------------------------------------------------

L281_GAP_OLD = b"""**Gap:** decision; then a Cusdis account, the two-line embed at the
bottom of the hall (L-280), and a line in the placard saying comments
are read before they appear.
**Ref:** L-280; https://cusdis.com/; https://github.com/djyde/cusdis."""
L281_GAP_NEW = b"""- **Note 2026-09-04:** the hall (L-280) was retired as a screen. The
  guest book embeds at the bottom of the LOBBY (L-282) instead. The
  decision above is unchanged.
**Gap:** decision; then a Cusdis account, the two-line embed at the
bottom of the lobby (L-282), and a line in the placard saying comments
are read before they appear.
**Ref:** L-282 (was L-280); https://cusdis.com/;
https://github.com/djyde/cusdis."""

# --- L-282: rewrite around subject doors -----------------------------------

L282_META_OLD = b"""<!-- L:282 status:OPEN upd:2026-09-03 section:A flag: rice:5/4/75/4 -->"""
L282_META_NEW = b"""<!-- L:282 status:OPEN upd:2026-09-04 section:A flag: rice:5/4/75/4 -->
- **DESIGN CLOSED 2026-09-04** (design session, zero code; the reasoning
  trail is HANDOFF 2026-09-04, "the lobby splits by subject"). Nine
  rounds, each simpler. What replaced proposal 1 below:
  - **Doors are organized by SUBJECT, not by content type.** Two doors:
    SOLAR SYSTEM and STARS. No Missions door, no Earth System door, no
    Interactive Wing door. Tony: "modern museums blend permanent with
    interactive." Each door carries its static cards and whatever live
    scenes exist for that subject, together.
  - **Earth System is a SPECIAL EXHIBIT inside the Earth room**, under
    Solar System. **Orbital Mechanics is a special exhibit in the Solar
    System room.** A special exhibit is a room that hangs off its parent
    like a side gallery; same chrome, same breadcrumb (L-286).
  - **Stars is its own door**, with exhibits for distance, magnitude,
    exoplanets and the galactic center. Exoplanet cards already exist
    and get their own room. The Stars door is BUILT NOW at final shape
    and filled in later; Tony: "build the final architecture and fill
    it in as we go."
  - **Missions live with the body they visit.** No Missions door;
    mission cards belong inside the room of their target body.
    Checked against `gallery_metadata.json` at gallery `e414af13`: 24
    `missions`-tagged cards resolve to FIVE missions -- Artemis II
    (Moon), New Horizons (Pluto), Psyche (16 Psyche), Voyager 1 and 2
    (four outer planets). Voyager lands whole in the planetary-missions
    phase; nothing needs splitting.
  - **Content is added to a door in PHASES, by the braid** -- a body's
    live room and its missions fold in when the rendering ladder
    reaches it. Tony's order: (1) planets and shells, (2) planetary
    missions, (3) the Moon and its missions, (4) the Sun and its
    missions, (5) planetary moons, (6) asteroids and their missions,
    (7) minor planets and their missions, (8) later: stars, exoplanets,
    galactic center.
  - **Pluto moves into the planet sequence**, "as people expect."
    Checked: Pluto already carries two cards tagged `outer_planets`, so
    this is a rendering-order decision with no reclassification cost.
    It also resolves New Horizons (Jupiter assist plus the Pluto flyby,
    its actual objective) into one phase.
  - **Pages.** A room is a card grid on `index.html`, filtered to the
    room the visitor is standing in. A LIVE scene is one card in that
    grid that opens `interactive.html?exhibit=...`. A room with no live
    scene yet is cards, and that is fine. (Tony leaned to this mixed
    model over all-cards or all-live, 2026-09-04.)
  - **The lobby keeps What's New and the guest book** (from L-280,
    retired): the dated one-line feed from one JSON file that shipping
    patches append to, and the Cusdis embed (L-281) at the bottom.
  - **Raw categories vs doors.** `gallery_config.json` carries NINE
    categories (solar_system, inner_planets, outer_planets, missions,
    stellar, exoplanets, climate, other, featured), not the four wings
    the earlier shorthand implied. The mapping to rooms is L-287's job
    (the config becomes the room tree). Two tags are not rooms at all:
    `other` is the STORAGE ROOM -- where a card lands when created,
    never shown to visitors, visible only in the editor; `featured` is
    a flag the editor sets and What's New reads.
  - **Consequences for L-283:** the accent list there still names
    Missions (steel grey) and an under-construction material for the
    Interactive Wing. Neither is a door now. Tony-action (decide):
    drop both accents, or keep the construction material for rooms the
    braid has not reached. Not changed by this patch.
"""

L282_P1_OLD = b"""  1. THE LOBBY. First screen: the name, one sentence, the wings laid
     out as doors -- Solar System, Missions, Stars and Exoplanets,
     Earth System, and the Interactive Wing with its construction
     notice. The categories already exist in the gallery config; the
     doors are a first screen, not new content. Today's landing plot
     becomes the first room of the Solar System wing."""
L282_P1_NEW = b"""  1. THE LOBBY. First screen: the name, one sentence, the doors, What's
     New, the guest book. [SUPERSEDED 2026-09-04 -- the original read
     "the wings laid out as doors -- Solar System, Missions, Stars and
     Exoplanets, Earth System, and the Interactive Wing with its
     construction notice." The door list is now the two subject doors
     in the design block above; the doors are still a first screen,
     not new content, and today's landing plot still becomes the
     Solar System overview room.]"""

L282_GAP_OLD = b"""**Gap:** design the lobby screen in conversation before building
(iterate; each round simpler); then the shared stylesheet; then the
placard format applied to existing cards; then the collections room.
**Ref:** L-280, L-283, L-266; index.html; gallery_config.json;
gallery_metadata.json; skills/gallery-pipeline."""
L282_GAP_NEW = b"""**Gap:** build order, Tony 2026-09-04: L-287 (editor and room tree)
first, so cards can be placed; then the lobby screen with its two
doors, What's New and guest book; then the drill-down and breadcrumb
(L-286); then the shared stylesheet (L-283); then the placard format on
existing cards; then the collections room. Mode 5 on phone first.
**Ref:** L-286 (rooms, drill-down, breadcrumb), L-287 (editor and room
tree), L-283, L-281, L-266; HANDOFF 2026-09-04 (design session: the
lobby splits by subject); index.html; interactive.html;
gallery_config.json; gallery_metadata.json; skills/gallery-pipeline."""

# --- L-286 and L-287: new items, inserted after L-285 -----------------------

INSERT_ANCHOR_OLD = b"""dolly, not of Plotly).

#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""
INSERT_ANCHOR_NEW = b"""dolly, not of Plotly).

#### [L-286] Rooms in four levels: drill-down, short-name breadcrumb, Home stays a scene reset
<!-- L:286 status:OPEN upd:2026-09-04 section:A flag: rice:5/4/70/4 -->
- **Opened 2026-09-04** from the lobby design session (HANDOFF
  2026-09-04, "the lobby splits by subject"; L-282 carries the doors,
  this item carries what is inside them). Nothing built.
- **Four levels, separate rooms, not a filtered grid.** Door -> body ->
  moon -> encounter. `solar: Earth: Moon: Artemis II`;
  `solar: Jupiter: Europa: Europa Clipper`; `solar: Pluto: New Horizons`
  (three, no moon); `stars: exoplanets: <system>`. Tony's ruling
  2026-09-04: four is needed -- "there are other satellite missions.
  Europa for example." No cap in the data; four is the working
  ceiling; anything wanting a fifth level is a sign the content wants a
  special exhibit instead. A mission's room hangs under the body it
  TARGETS (the phase rule, L-282), so New Horizons is under Pluto, not
  under Jupiter.
- **Special exhibits are rooms too.** Earth System under Earth; Orbital
  Mechanics under the Solar System overview. Same chrome, same
  breadcrumb: `solar: Earth: Earth System`.
- **Checked against real content** (gallery `e414af13`): three cards
  already blend a body with its shells (Earth-Moon with atmosphere and
  magnetosphere, twice; Sun photosphere and corona) and eleven already
  represent one encounter (Psyche-Mars assist, Artemis Moon flybys).
  The levels are a new STRUCTURAL distinction on content that exists,
  not a new content type.
- **Navigation: drill-down, not a level filter.** Tapping a planet in
  the overview opens its room; tapping a mission there opens the
  encounter. Tony chose the drill-down over a one-room level filter.
- **Breadcrumb in the header, tappable, SHORT NAMES with colons.**
  `solar: Earth: Moon`. Tony's ruling 2026-09-04, replacing full names
  so the chain fits a portrait header without truncation. Each room in
  the tree carries a short label beside its full one; the header uses
  the short one. Where a body has more than one encounter, the
  encounter's short label names the event (`solar: Psyche: Mars flyby`)
  -- a per-card choice in the editor, not a rule. The breadcrumb
  REPLACES the header's existing title slot; no new chrome element. It
  renders the same in `index.html` and `interactive.html`.
- **Home stays a scene reset.** Home shipped for the Sun room under
  L-267/L-285 and passed Mode 5 on phone and desktop. Tony: "if the
  chain is visible it's a scene reset." The breadcrumb's first crumb is
  what returns a visitor to the lobby. Nothing already shipped changes.
- **Rules carried from L-280 (retired), unchanged in content:**
  - Growth rule: when a body ships it appears as a room and in the Sun
    room's drawer as a body you can focus on. Bold means "can be the
    focus"; the date control appears only when something in the scene
    has a position to move.
  - Room-shape rule (Tony's breadcrumb 2026-09-03): Earth System
    exhibits need horizontal room; in portrait a wide room is SWEPT
    sideways while placard and drawer stay put. A room declares its
    shape (wide or square) in its config; the chrome never assumes the
    plot fits the viewport; in wide rooms the plot's own horizontal
    drag is given to the sweep.
  - The premade Solar System Explorer stays reachable under its own
    parameter and is EVENTUALLY REPLACED as the braid delivers
    interactive planets.
- **Note:** RICE 5/4/70/4 -> 3.5 proposed, not confirmed. Depends on
  L-287 (cards must carry a room path before rooms can be drawn).
**Gap:** the room-path reader in `index.html` (filter a grid to a room);
the breadcrumb component shared by both pages; the special-exhibit
placement; the room-shape field; Mode 5 on phone at all four levels.
**Ref:** L-282 (doors, phases, pages), L-287 (room tree and editor),
L-280 (retired; the record), L-267 and L-285 (Home and the nav
cluster), L-283 (theme); HANDOFF 2026-09-04 (design session: the lobby
splits by subject); index.html; interactive.html; gallery/nav_cluster.js;
gallery_config.json; gallery_metadata.json.

#### [L-287] Gallery editor: the room tree, the storage room, the featured flag
<!-- L:287 status:OPEN upd:2026-09-04 section:A flag: rice:3/3/85/2 -->
- **Opened 2026-09-04.** Tony's ruling: the editor is a SEPARATE item
  from the lobby. "It is there to edit the gallery (remodel?) -- it also
  allows highlighting special features like new exhibits."
- **What exists** (`tools/gallery_editor.py` at gallery `e414af13`, read
  2026-09-04): a Tkinter GUI over `gallery_metadata.json`. Each card
  carries a `category` key and an optional `subcategory`; the nine
  categories come from `gallery_config.json`, a FLAT list of key, label
  and color. The editor shows a two-level tree per mode, and offers
  move, edit, add, delete, reorder, duplicate to another category, set
  subcategory, and rename category. Run from `tools/` with the VS Code
  Run button.
- **What changes.** Three things, one migration:
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
    `json_converter.py` keep reading the same two files.
  - The editor's tree view grows to the depth of the room tree (four
    levels, L-286). "Change category" becomes "move to room"; "new
    category" becomes "new room" at any level. Move, edit, add, delete
    and reorder work as they do now.
- **The storage room.** `other` is where a new card lands and stays
  hidden from visitors until moved into a room. Tony: "like the storage
  room of a museum. Visitors don't see it. It only lives in the gallery
  editor list." The lobby and breadcrumb skip it.
- **The featured flag.** `featured` is not a room; it is a flag the
  editor sets on a card to highlight a new or special exhibit. What's
  New (L-282) reads it. Tony-action (decide): whether the flag alone
  drives What's New, or the dated JSON feed from L-280 does, or both.
- **Note:** RICE 3/3/85/2 -> 3.8 proposed, not confirmed. Build FIRST
  in the L-282 order -- rooms cannot be drawn until cards carry a room.
  gallery-pipeline skill fires; safe-file-editing for the migration.
**Gap:** the category-to-room table (decide); the room-tree schema for
`gallery_config.json`; the migration script; the editor's deeper tree
and move-to-room; the storage-room and featured behaviours; a run on
the real metadata with the result checked in the editor.
**Ref:** L-282, L-286; tools/gallery_editor.py; tools/json_converter.py;
gallery/gallery_config.json; gallery/gallery_metadata.json; index.html;
skills/gallery-pipeline.

#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""

EDITS = [
    ("header stamp",                 STAMP_OLD,         STAMP_NEW),
    ("L-280 meta -> DONE + record",  L280_META_OLD,     L280_META_NEW),
    ("L-280 Gap -> move to C",       L280_GAP_OLD,      L280_GAP_NEW),
    ("L-281 note: lobby not hall",   L281_GAP_OLD,      L281_GAP_NEW),
    ("L-282 meta + design block",    L282_META_OLD,     L282_META_NEW),
    ("L-282 proposal 1 superseded",  L282_P1_OLD,       L282_P1_NEW),
    ("L-282 Gap: build order",       L282_GAP_OLD,      L282_GAP_NEW),
    ("insert L-286, L-287",          INSERT_ANCHOR_OLD, INSERT_ANCHOR_NEW),
]


def main():
    if not os.path.exists(FN):
        print(f"ERROR: {FN} not found. Run from the palomas_orrery repo root. NOTHING written.")
        sys.exit(1)

    with open(FN, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    actual = hashlib.md5(content).hexdigest()
    if actual != EXPECTED_MD5:
        if b"[L-286] Rooms in four levels" in content:
            print("ERROR: patch already applied (L-286 present). NOTHING written.")
        else:
            print(f"ERROR: BASE MOVED. md5 {actual} != expected {EXPECTED_MD5} "
                  f"(content compared LF-normalized). NOTHING written. "
                  f"Undo is Discard Changes in GitHub Desktop.")
        sys.exit(1)
    print(f"base ok: {FN} matches 5955a405"
          + (" (the working copy is CRLF)" if was_crlf else ""))

    # Gate: inserted text must be ASCII.
    for name, _, new in EDITS:
        bad = [b for b in new if b > 0x7F]
        if bad:
            print(f"ERROR: non-ASCII byte in inserted text for '{name}'. NOTHING written.")
            sys.exit(1)

    # All-or-nothing: check every anchor before writing anything.
    for name, old, _ in EDITS:
        n = content.count(old)
        if n != 1:
            print(f"ANCHOR FAIL: '{name}' expected 1 match, got {n}. NOTHING written.")
            sys.exit(1)

    for name, old, new in EDITS:
        content = content.replace(old, new)
        print(f"ok  {name}")

    final = content.replace(b"\n", b"\r\n") if was_crlf else content
    with open(FN, "wb") as f:
        f.write(final)
    print(f"patch applied ({len(final)} bytes)")
    print("stamp updated: header 'Module updated: September 4, 2026 ... built on 5955a405'")
    print("note: LEDGER_CONSOLIDATED.md held 0 non-ASCII bytes before and after")
    print("still quotes the old design, NOT changed by this patch (Tony decides):")
    print("  - L-283 accent list names Missions and the Interactive Wing")
    print("  - MASTER_PLAN_INTERACTIVE_GALLERY.md, if it names the hall or the wing door")
    print("NEXT: run ledger_index.py (repo root), then archive this script to documentation/.")


if __name__ == "__main__":
    main()
