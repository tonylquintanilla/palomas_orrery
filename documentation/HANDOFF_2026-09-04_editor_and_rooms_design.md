# HANDOFF -- 2026-09-04 (design session + one ledger patch): the doors close, the rooms get four levels, the editor gets a design

**Built on** orrery `5955a40550b1356d157460d3288aada900c712c1` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `e414af13d4c4c736a6c6d792d3fe7ad651f2fbdc` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both read live at session start with `git ls-remote`; both match the
anchors on the prior handoff exactly. No pushes this session. Tony was
away from his machine throughout.

**Type:** DESIGN SESSION, with ONE deliverable written and tested but
NOT run: `patch_L286_1_lobby_by_subject.py`, a fingerprint-guarded
patch to `LEDGER_CONSOLIDATED.md` (details below). Nothing else was
built. Companion to HANDOFF 2026-09-04 ("the lobby splits by subject,
not by permanent vs. interactive"), which this session reviewed first
and then closed the questions it left open.

**Skills loaded and checked against the manifest:**
ledger-and-session-records 1.9 (matches), safe-file-editing 1.10
(matches). gallery-pipeline was NOT loaded; the editor and metadata
facts below were read directly from the files at `e414af13`.

---

## What was decided, in the order it was decided

Each of these is Tony's ruling unless marked otherwise. Plain
statement first, reasoning after.

1. **Build order: ledger first, code second.** The prior handoff's
   decisions go into the ledger before any gallery code is written.
   Claude's proposal; Tony agreed.

2. **Rooms are card grids on `index.html`; a live scene is one card
   that opens `interactive.html`.** Of the three options (all cards,
   all live, mixed) Tony leaned to the mixed model on Claude's view.
   A room with no live scene yet is cards, and that is fine; the braid
   decides when a room gets its live card.

3. **Earth System is a special exhibit inside the Earth room. Orbital
   Mechanics is a special exhibit in the Solar System room.** A
   special exhibit is a room that hangs off its parent like a side
   gallery, with the same chrome and breadcrumb.

4. **Stars is its own door**, with exhibits for distance, magnitude,
   exoplanets and the galactic center. Exoplanet cards already exist
   (three) and get their own room. Deferred in content, built now in
   structure: "build the final architecture and fill it in as we go."

   Consequence, flagged plainly: **Earth System is no longer a lobby
   door.** The lobby has TWO doors, Solar System and Stars.

5. **The gallery editor is a separate ledger item** (L-287). "It is
   there to edit the gallery (remodel?) -- it also allows highlighting
   special features like new exhibits."

6. **`other` is the storage room.** A new card lands there and stays
   hidden from visitors until moved into a room. "Like the storage
   room of a museum. Visitors don't see it. It only lives in the
   gallery editor list."

7. **`featured` is a flag, not a room.** The editor sets it; What's
   New reads it. (Open sub-question recorded on L-287: whether the
   flag alone drives What's New, or the dated JSON feed from L-280
   does, or both.)

8. **The breadcrumb uses short names with colons.** `solar: Earth:
   Moon`. Replaces full names so the chain fits a portrait header
   without truncation. Each room carries a short label beside its
   full one. Where a body has more than one encounter, the
   encounter's short label names the event (`solar: Psyche: Mars
   flyby`) -- a per-card choice in the editor, not a rule.

9. **Four levels: door -> body -> moon -> encounter.** "There are
   other satellite missions. Europa for example." `solar: Earth: Moon:
   Artemis II`, `solar: Jupiter: Europa: Europa Clipper`. No cap in
   the data; four is the working ceiling; a fifth level wanted is a
   sign the content wants a special exhibit. A mission's room hangs
   under the body it TARGETS, so New Horizons is `solar: Pluto: New
   Horizons`, not under Jupiter.

10. **Desktop and mobile collapse to one card per exhibit with two
    file slots** (landscape file, portrait file). Where an exhibit has
    one file, the page shows it in both orientations; where it has
    two, the page picks by screen width, which `index.html` already
    detects. The Desktop/Mobile toggle goes away (L-282 proposal 4
    already asked for this).

11. **Shape is a per-card field with two values, 16:9 and 9:16, and it
    governs the PHONE only. Desktop is unchanged.** "The current view
    on desktop works." On a phone: 16:9 sweeps sideways for 2D and
    scales to fit for 3D; 9:16 shows as today. Sweep was chosen over
    an Instagram-style card flip because the exhibits that run out of
    horizontal room are time series, and sweeping along a time axis
    is a reading gesture; flip suits separate complete faces, which a
    continuous plot is not. 3D scenes need neither -- a 3D file stores
    a camera, not a picture, so it re-frames without distortion.

12. **Realignment of L-283's accent list and the master plan waits
    for next round.** Both still name Missions and the Interactive
    Wing as doors. Recorded, not chased.

13. **Next deliverable: this handoff first, then decide on the build.**

14. **Earth System is promoted to a DOOR. Three doors: Solar System,
    Earth System, Stars.** Made after this handoff was first written;
    it AMENDS decisions 3 and 4 above. Tony's concern: with Earth
    System as a special exhibit under Earth, its rooms (heating,
    heatdome, food, ...) sit at level 4 and get buried. The weight
    settles it: climate is 76 of 148 cards, half the collection, and
    carries the museum's only finished sentence. As a door its rooms
    land at level 2 (`earth: heatdome`), two taps from the lobby. The
    Earth room under Solar System keeps its own content (shells, Moon,
    Artemis) and carries ONE card that is a doorway into the Earth
    System wing -- a cross-link, not a copy. Orbital Mechanics stays a
    special exhibit in the Solar System room. The four-level rule is a
    navigation ceiling, not a taxonomy; Earth System is a subject with
    its own audience.

    Consequence: the ledger patch below writes TWO doors into L-282.
    That text is superseded by this decision and the NEXT patch
    corrects it. L-283's Earth System accent (blue-green) stands.

---

## Findings from the real files (read at gallery `e414af13`)

- `gallery_metadata.json`: one list, 148 cards, top-level keys
  `visualizations`, `last_updated` (2026-06-30), `total_count`. Card
  keys: id, title, description, filename, category, category_label,
  subcategory, subcategory_label, mode, featured, converted, size_kb.
- `mode` values: portrait 58, landscape 38, both 28, absent 24.
  `index.html` shows a card when its mode matches the toggle or is
  `both`; absent is treated as landscape (line 1912 at `e414af13`).
- 105 distinct titles. 33 exhibits appear twice, as a `_gallery.json`
  landscape card and a `_mobile.json` portrait card. This is what
  makes the collapse clean: those 33 pairs become 33 cards with two
  file slots; the rest become cards with one.
- Categories in use: climate 76, solar_system 25, missions 24,
  inner_planets 10, stellar 7, outer_planets 3, exoplanets 3. `other`
  and `featured` appear in `gallery_config.json` but no card carries
  them as a category. 10 cards carry `featured: true`.
- Subcategories in use: heating 31, comets 20, heatdome 18, climate 15,
  narrative 7, general 5, acidification 2, food 2, coral 1; 47 cards
  have none. These are the Earth System special exhibit's internal
  structure and will need rooms of their own under it.
- `tools/gallery_editor.py` (1619 lines): Tkinter GUI over the two
  files. Two-level tree (category, optional subcategory) per mode.
  Offers move, edit, add, delete, reorder, duplicate to another
  category or mode, set subcategory, rename category. Categories are
  a flat list of key, label, color. Run from `tools/`.
- `ledger_index.py` lives at the orrery REPO ROOT, not under `tools/`
  (a first draft of the patch said `tools/`; corrected before
  delivery).

---

## The editor design (L-287), as it stands for Tony to read

One window, two panes.

**Left pane: the room tree.** Doors (Solar System, Earth System,
Stars), rooms
under them, exhibits under those, four levels deep; the storage room
at the bottom. Actions: move a card to a room (drag, or a picker);
add, rename, reorder, delete rooms; set a room's full label, short
label, color, and shape. The tree IS `gallery_config.json` in its new
form.

**Right pane: the card.** One card per exhibit. Title, one-sentence
placard, the two file slots (landscape, portrait), the sources,
shape (16:9 or 9:16), the featured flag, and -- if the card is itself
a room, e.g. a body with an encounter under it -- its short label.
The same fields edited today, once instead of twice.

**First open after the migration.** A one-shot script (safe-file-
editing fires) does the mechanical half: pairs the 33 duplicate
cards into one card each, moves every card into the storage room,
and writes the three doors with their planet rooms, empty. Tony then
remodels by moving cards out of storage in the editor. **The
category-to-room mapping is done IN THE EDITOR, not as a table in
conversation** -- Tony's ruling, replacing Claude's proposal to draft
the table.

**Save writes both files** -- the tree to `gallery_config.json`, the
cards to `gallery_metadata.json` -- and prints what changed. Git is
the backup; no `.bak`.

Consumers to check before building (Check All Parallel Pipelines):
`index.html` and `tools/json_converter.py` both read the two files;
`interactive.html` will read the room tree for its breadcrumb. Grep
for `category`, `subcategory` and `mode` in all three before changing
the schema.

---

## The ledger patch, delivered and tested, not yet run

`patch_L286_1_lobby_by_subject.py`. Save to the orrery repo root next
to `LEDGER_CONSOLIDATED.md`, open in VS Code, Run. Then run
`ledger_index.py` from the repo root, commit both, push.

Guards on the LF-normalized md5 of the ledger at `5955a405`; handles
a CRLF working copy; refuses a second run; all inserted text ASCII.
Tested on LF and CRLF throwaway copies; the real `ledger_index.py`
parsed the result and moved L-280 into section C on its own.

What it writes:
- Header stamp.
- L-280 -> DONE, retired as a screen, with each piece of its scope
  named and sent to L-282 or L-286.
- L-281: a Note that the guest book embeds in the lobby, not the hall.
- L-282: the closed design (two subject doors -- SUPERSEDED by
  decision 14, three doors; corrected in the next patch), phase order,
  missions
  by target body, Pluto in the planet sequence, mixed page model,
  storage room, featured flag) and a build order in its Gap: L-287,
  then the lobby, then L-286, then L-283, then placards, then the
  collections room.
- L-286 opened: four levels, drill-down, short-name breadcrumb, Home
  stays a scene reset, the growth and room-shape rules carried from
  L-280.
- L-287 opened: editor, room tree, storage room, featured flag.

Decisions 10, 11 and 14 above (the collapse; 16:9 / 9:16 phone-only;
Earth System as a door) were made AFTER the patch was written and are
NOT in it. They go in the
next ledger patch, on L-286 and L-287, together with the L-283 and
master-plan realignment.

---

## Tony-actions, rolled up

- **(do)** Run `patch_L286_1_lobby_by_subject.py`, then
  `ledger_index.py`, commit, push. Report the new orrery SHA; the next
  session confirms it live before building on it.
- **(do)** Archive the spent patch script to `documentation/`.
- **(decide)** The build: start L-287 (editor + migration) as the
  next session's work, or another round of design first.
- **(decide)** What's New: driven by the `featured` flag, the dated
  JSON feed, or both (L-287 Note).
- **(decide)** L-283's accent list: drop the Missions and Interactive
  Wing accents, or keep the construction material for rooms the braid
  has not reached. Next round, with the master plan realignment.
- **(decide)** Whether the subcategories under `climate` (heating,
  heatdome, comets, narrative, ...) become level-2 rooms under the
  Earth System door one-for-one, or get regrouped in the editor as
  part of the remodel. Tony: "very important."
- **(do, next session)** Second ledger patch: L-282 door count two ->
  three; L-286 and L-287 gain the collapse and the phone-only shape
  rule; L-283 accent list and the master plan realigned.

---

*Session written September 4, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `5955a405`, gallery `e414af13`. No pushes this
session.*
