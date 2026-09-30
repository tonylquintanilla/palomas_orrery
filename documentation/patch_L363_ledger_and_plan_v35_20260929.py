#!/usr/bin/env python3
"""
patch_L363_ledger_and_plan_v35_20260929.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L363_ledger_and_plan_v35_20260929.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery e5c3f92a2ad1dd47ad8cb35d17c159e07f1a9cf9
at https://github.com/tonylquintanilla/palomas_orrery
(gallery f46cf299c2b6e93e5f3ba405c4ad62032e7666ae
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

WHAT IT DOES. It records three things: Half 1 of the Solar System room
as finished, the front-door design of 2026-09-29, and Tony's ruling of
the same day on the order of work (option C, "confirmed as
recommended"). Two files, both written or neither.

LEDGER_CONSOLIDATED.md
  L-363  rewritten: Half 1's patches 2 to 6 and the card, the Half 1
         rulings, the lost card, the front-door design, the ruling on
         the order, and a new Gap pointing at the integrated handoff.
  L-322  a note: the Sun's slice follows L-363 Half 2's Mode 5, and the
         two are never in progress at once.
  L-371  a note: the same order.
  L-364, L-365, L-367, L-378  one line each.
  L-391 to L-394  four new rows, one per class the design left open:
         group clouds; the drawer's list as served data; encounter
         data; a card that names its body.
  L-395  the direction after the Sun, in outline: the orrery's objects
         rebuilt in the gallery from its own dictionary, exported the
         way the constants are and checked against Horizons.
  The header stamp.

documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md -> v35
  The executive summary rewritten, the status and "Last updated" stamps
  moved to v35 (v32's entry drops off, keeping three), Claude Sonnet
  5.5 added to the participants, and a new Section 5a subsection,
  2026-09-29.

IF IT REFUSES because a file moved: another session may have filed
first and taken these handles. Tell Claude; nothing was written.

AFTER IT RUNS:
  1. python orrery_maintenance_run.py (it runs ledger_index.py, which
     rebuilds the ledger's INDEX; this patch does not touch the INDEX
     and does not fingerprint it).
  2. Move this script into documentation/.
  3. Commit and push, with the design document and the integrated
     handoff in documentation/.
  4. Tell Claude the new orrery SHA.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written to either file. Undo is Discard Changes in GitHub Desktop.

Written September 29, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PLAN = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")

# Content fingerprints at orrery e5c3f92a, line endings normalized to LF.
# The ledger's is taken OUTSIDE its INDEX zone, which ledger_index.py
# regenerates (safe-file-editing, A Guard Must Not Fence What a Generator
# Rewrites). The plan has no generated zone.
BASE = {
    LEDGER: "d2eacdbdeb407b023d95b9974595f14b",
    PLAN: "b4e3dc97234f59ddbf88de13139f352e",
}

INDEX_START = "<!-- INDEX:START"
INDEX_END = "<!-- INDEX:END -->"


# ====================================================================
# THE LEDGER
# ====================================================================

LEDGER_STAMP = """\
Module updated: September 29, 2026 with Anthropic's Claude Opus 5.5
(L-363: Half 1 recorded as finished, the front-door design, and Tony's
ruling C on the order -- Half 2 through his Mode 5, then the Sun's
slice, then the swap; after the Sun, in outline, the orrery's objects
rebuilt from its own dictionary and checked against Horizons; L-391 to
L-395 opened; L-322, L-364, L-365, L-367, L-371 and L-378 noted; master
plan v35), built on e5c3f92a.
"""

NEW_ROWS = """\
#### [L-395] The gallery's objects are hand-copied from the orrery's dictionary: export them, and check them against Horizons (orrery, gallery, objects)
<!-- L:395 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **The direction after the Sun, Tony 2026-09-29, in outline.** After
  the Sun's slice and the Solar System room's swap, the gallery grows
  the way the orrery did: symbols with positions from Horizons and
  osculating orbits first, moons with them; then encounters (comets and
  spacecraft); then shells and slices for the graphical detail. Tony:
  "In the original orrery the shells came late."
- **The source of truth, Tony 2026-09-29: "an excellent improvement."**
  `OBJECT_DEFINITIONS` in `celestial_objects.py` becomes the one
  definition of each object. An export written on every orrery
  maintenance run is pulled by the gallery, the way `constants_new.py`
  reaches it (`export_constants.py`, `pull_constants_export.py`,
  `mirror_constants.py`). The gallery keeps only its serving choices:
  which objects it serves, how it fetches them, trust tuning, shells
  and arrival views. A checker fails when the two disagree.
- **Horizons as the outside authority, Tony 2026-09-29.** The dictionary
  can go stale -- legacy entries, the orrery's own evolution, errors --
  so the check includes cross-checking JPL Horizons, not only the
  gallery against the dictionary.
- **Revisit the dictionary's structure and role, Tony 2026-09-29.** It
  is one of the oldest parts of the orrery, dating from the move from
  the Keplerian model to Horizons. So the round is not only an export
  of what is there. Found in a first look [verified @ orrery
  e5c3f92a]: an object's facts are spread across several tables keyed
  by name strings -- `OBJECT_DEFINITIONS` (182; identity, symbol, hover
  text, link, dates), `orbital_elements.planetary_params` (120; typed
  mean elements from the Keplerian era),
  `orbital_elements.parent_planets` (17 parents; the satellite-to-planet
  link the dictionary lacks), `KNOWN_ORBITAL_PERIODS` (133) and
  `CENTER_BODY_RADII` (18) in `constants_new.py`, and
  `export_orbit_cache.CENTER_SLUG_MAP`. The dictionary also carries two
  GUI concerns, the Tk variable name (`var_name`) and the colour key.
- **The orrery already draws osculating orbits; the mean elements are
  not the drawing source** [traced @ orrery e5c3f92a]. Before a plot,
  `palomas_orrery.py` copies `planetary_params` into
  `active_planetary_params` and replaces each selected object's entry
  with osculating elements from Horizons for the plot date
  (`get_elements_with_prompt`); `plot_idealized_orbits` receives the
  working copy. The mean table remains as: the seed and the fallback
  when a fetch fails; the mean orbit drawn beside the osculating one
  to show perturbation (`ORIGINAL_planetary_params`); and the only
  source for the moons the prefetch skips (`SKIP_HORIZONS_PREFETCH`:
  MK2, Xiangliu, Vanth, Gonggong) and the analytic orbits labelled as
  from Hubble or occultation observations. What the table is still
  for, and what replaces it where, is the round's question -- not
  whether the orrery migrated, which it did. (Claude first reported
  the table as widely read without saying for what; Tony caught it.)
- **Found comparing the two copies** [verified @ orrery e5c3f92a,
  gallery f46cf299]: Apophis is `'2004 MN4'` in the dictionary and
  `'99942'` in the gallery; Pluto has no ID type in the dictionary and
  is a major body measured from the Pluto-Charon barycentre in the
  gallery; Voyager 1's gallery note says "confirm against the object
  definition", a hand sync; Earth's dictionary entry carries
  `mission_info` twice, and Python keeps the second. The dictionary
  holds 182 entries: 66 orbital, 46 satellites, 38 trajectories, 11
  exoplanets, 10 Lagrange points, 4 barycentres and 7 others (exoplanet
  hosts, the Sun, one hypothetical). The gallery serves 13.
- **Questions for its design round:**
  - Which facts belong to the object (its ID, its parent body, its
    kind) and which to the gallery (fetch cadence, trace style, trust
    anchors).
  - Fields the dictionary lacks: a satellite does not name its planet,
    and comets share `object_type 'orbital'` with asteroids, told apart
    only by their symbol. And one stable key: the gallery says
    `apophis`, the dictionary `Apophis` and `apophis_var`.
  - What Horizons can confirm -- that an ID resolves to exactly one
    object, its name and designation, its kind -- and what it cannot:
    the project's modelling choices, such as drawing Pluto about its
    barycentre. For small bodies, JPL's Small-Body Database may give an
    orbit class that could source the drawer's groups; to be verified
    before it is relied on.
  - Where the Horizons check runs. It needs the network, so when it
    cannot reach Horizons it says so and does not pass. It records the
    date each object was last confirmed, the way a store row records
    who read its source, and re-confirms on a cadence rather than
    querying every object on every run.
  - Pinned records (Halley `90000030`, Encke `90000091`): flagged when
    JPL has a newer solution, for a person to decide.
- **Discovery before remediation** (The Braid): the first run lists
  every disagreement and fixes nothing; each gets a ruling; fixes land
  in slices.
**Gap:** Its design round, after the Solar System room's swap; it takes in L-391 to L-394.
**Ref:** `celestial_objects.py`; gallery `data/objects_config.json`; `export_constants.py`; gallery `tools/pull_constants_export.py` and `tools/mirror_constants.py` (the model); skills/horizons-orbital-mechanics/SKILL.md; L-363; L-364; L-391 to L-394.

#### [L-394] A card cannot say which body it belongs to (gallery, Studio)
<!-- L:394 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **From the front-door design, 2026-09-29** (question 15 of
  `documentation/DESIGN_solar_system_room_front_door_20260929.md`). In
  the Solar System room each drawer row shows whether its body has a
  room and whether it has cards, and expands to their titles. The
  design rules that this is READ from the exhibits table and the card
  metadata, so a new room or card lights up its row and nothing is kept
  in two places; and that each thing has one address, the same one the
  taxonomy uses.
- "Has a room" can be read from `EXHIBITS` in `interactive.html` today.
  "Has cards" cannot: nothing in `gallery/gallery_metadata.json` says
  which body a card belongs to. "Earth science" cards, for example, are
  to be listed under Earth.
- It may ship inside L-363's Half 2 if the field is small, or as the
  first round after it. Not a gate on the swap. [per the integrated
  handoff, section 4 step 6]
**Gap:** A field on each card naming its body, Studio writing it, and the drawer reading it.
**Ref:** gallery `gallery/gallery_metadata.json`; gallery `tools/gallery_studio.py`; gallery `interactive.html` (`EXHIBITS`); skills/gallery-pipeline/SKILL.md; L-363.

#### [L-393] Encounter data: dates, spacecraft records centred on their targets, and how far the cache reaches in time (gallery, cache)
<!-- L:393 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **From the front-door design, 2026-09-29** (its section 5 and
  questions 9 to 11). An encounter is a dated event: ticking it moves
  the whole Solar System room to the flyby date, and unticking returns
  it to now. One record is listed in the room of each body involved,
  the target's room centres the view, and each encounter carries its
  own opening view, modelled on the arrival block.
- Three things the design did not read, each to be read before the
  encounter round is designed:
  - How far the assembler's dates reach. A 1979 flyby needs served
    positions for every body drawn at that date.
  - How the cache holds spacecraft. The assembler never translates
    between centres, so one mission may need a record centred on each
    target.
  - The trust check per encounter: each drawn body's own window must
    cover the encounter's date, not only the cache's overall window
    (the L-364 class).
**Gap:** Read the three, then the encounter design round (Voyager 1 first, with L-365).
**Ref:** gallery `gallery/assembler/`; gallery `tools/gallery_cache_builder.py`; skills/gallery-assembler/SKILL.md; skills/horizons-orbital-mechanics/SKILL.md; L-363; L-364; L-365.

#### [L-392] The Solar System room's drawer list is page code, not served data (gallery, exhibits)
<!-- L:392 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **From the front-door design, 2026-09-29** (question 3). The drawer
  lists the Sun, the eight planets and Pluto, with a "See more" that
  adds the groups in place along the spine, outward from the Sun
  (design section 3, item 4). Today the room's bodies are one list in
  the page, `SOLAR_SYSTEM_BODIES` in `interactive.html`, and the room
  has no entry in `data/objects_config.json`. Left that way, every new
  group means editing the page.
- L-363's Half 2 needs at least the ten rows, so the shape is chosen
  there, with room for the spine to grow; whatever Half 2 does not take
  stays here. Who may write `data/objects_config.json` is in
  interactive-exhibit.
**Gap:** A served shape for the spine, groups and "See more"; the page reads it.
**Ref:** gallery `interactive.html`; gallery `data/objects_config.json`; skills/interactive-exhibit/SKILL.md; L-363.

#### [L-391] Group clouds: the Trojans' sources, and the shapes of the three other groups (gallery, exhibits)
<!-- L:391 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **From the front-door design, 2026-09-29** (its section 5 and
  questions 2, 4 to 6 and 12). A group is its own room with a cloud,
  served once and drawn like a shell: off when a room opens, ticked by
  the visitor, translucent, stackable. A cloud is a portrait, not data:
  its points come from a seed, its hover says its proportions are
  approximate, and its extents are sourced or left out. The Oort cloud
  is the served model.
- **The Jupiter Trojans are the settled pattern**, still to be sourced:
  which camp leads Jupiter and which trails it, each body's camp, and
  the lobes' extent. None is to be served from memory.
  **Tony-action (decide), in the Trojans round:** Patroclus and
  Menoetius, a binary that overlaps at this scale -- one row for the
  pair, or two rows that say they overlap.
- **The three other groups**, each its own design round: the main
  asteroid belt, the near-Earth asteroids and the trans-Neptunian
  objects -- shape, extents, sources.
- To read first: how the orrery defines its group shells; and whether
  the + and - buttons reach hundreds of AU with orbits drawn at full
  length (Sedna would need a served orbit with its own trust window).
**Gap:** The Trojans round, then one round per group.
**Ref:** gallery `data/objects_config.json` (the Oort cloud's shapes); skills/provenance-discipline/SKILL.md; skills/interactive-exhibit/SKILL.md; L-363.

"""

L378_LINE = """\
- **2026-09-29, from L-363's Half 1:** the sandbox cannot load Google
  Fonts, so whether a line of text fits a phone is settled only on the
  phone.
"""

L371_LINE = """\
- **Note (2026-09-29, the order):** the Sun's slice now follows L-363's
  Half 2 through Tony's Mode 5, on his ruling C; see L-322's note of
  the same date.
"""

L367_LINE = """\
- **2026-09-29:** meanwhile the rooms were checked by the headless
  recipe in `documentation/HANDOFF_L363_half1_done_half2_after_stage_d_20260928.md`,
  section 7. L-363's Half 2 drawer enters the same blind spot.
"""

L365_LINE = """\
- **2026-09-29:** part of the Solar System room's future under the
  front-door design: space missions get their own drawer, by launch
  date, and Voyager 1's Jupiter and Saturn flybys are among the first
  encounters (L-393).
"""

L364_LINE = """\
- **2026-09-29:** part of the Solar System room's future under the
  front-door design: each comet apparition becomes a room that opens on
  its perihelion, so this check becomes per apparition (L-393).
"""

L322_NOTE = """\
- **Note (2026-09-29, the order):** Tony's ruling C on L-363, "confirmed
  as recommended": the Solar System room's Half 2 goes through his Mode
  5 first, then point (3), the Sun's slice, then the room's swap to the
  default. Half 2 adds object entries to gallery
  `data/objects_config.json`; the Sun's slice rewrites the Sun's served
  values in the same file through the mirror; both end in a cache
  rebuild. So the two are never in progress at once: one is pushed and
  live-checked before the other starts. Master plan v35.
"""

L363_START = "#### [L-363] The Solar System room"
L363_END = "L-322; L-364 to L-367.\n"

L363_BLOCK = """\
#### [L-363] The Solar System room: the bodies as symbols, and the gallery's front door (gallery, exhibits)
<!-- L:363 status:OPEN upd:2026-09-29 section:A flag: rice: -->
- **What it is.** A third room in `interactive.html`,
  `?exhibit=solar-system`, titled "The Solar System". It draws the
  bodies as their symbols on their orbits, from the served cache, on
  today's date, with no shells. Tony, 2026-09-26: symbols first, the
  way the orrery itself grew, as a quick win while each body's shells
  wait for its own room. It is the top level L-286's drill-down needs.
  Since 2026-09-29 it is also designed as the gallery's front door
  (below).
- **Tony's rulings, 2026-09-26:**
  - Two halves, because L-322 Stage D shares `data/objects_config.json`
    and the cache rebuild. Half 1 touches only `interactive.html`.
    Half 2 waits for L-322's manifest section 6 to push. [Superseded
    2026-09-28: after Stage D COMPLETES. It completed at orrery
    `2a7d26b9`, and D20 landed at `e5c3f92a`, so the gate is open.]
  - Plan B for the key: `solar-system` is permanent. The Explorer keeps
    `solar-system-explorer` and stays the default until Half 2 and
    Tony's acceptance; then the default switches, and the Explorer
    card's live link is changed in Studio. [Superseded 2026-09-29 by
    the swap in the front-door design, below.]
  - Only bodies the cache stands behind today: the Sun, Earth, Jupiter,
    Saturn and Apophis. The Moon, Io, Titan and Charon are left out;
    at this scale each sits on its planet, and they belong in their
    planets' rooms.
  - Today's date, the method every room uses (`resolver.py` checks the
    served window once for the scene). No date control: adding one is
    a decision for all rooms at once.
  - The opening view is the rooms' rule, 1.1 x the largest thing drawn.
    Claude first cited 25 percent, the static artifacts' rule, and
    corrected it before delivery.
  - Shells are kept out by the room's compose using the assembler's
    figure only and building no features. No arrival block.
- **Half 1 shipped at gallery `8545cbd7`** from
  `patch_solar_system_room_half1_20260926.py`, built on `a5c35f5f`.
  The pushed `interactive.html` is byte-identical to the tested file
  [verified @8545cbd7]. Beyond the plan, naming a body opens its text
  box at the body, not at its orbit's info cross (L-366). Two shared
  changes that alter nothing in the Sun or Earth rooms, confirmed
  identical before and after in the headless run: the info panel shows
  a source when there is no link, and a room can name the marker a
  text box belongs to. Tony's Mode 5 on the phone: "correct for our
  scope."
- **Seen in the headless phone run, not ruled:** on an upright phone
  the in-scene title "Paloma's Orrery -- The Solar System" runs under
  the arrow buttons. [Resolved by patch 5 below.]
- **Half 1 finished, 2026-09-26 to 29: five more gallery patches and
  the card.** Each was run by Tony, followed by the gallery maintenance
  run, pushed, and checked on his phone. The scripts are in the
  gallery's `documentation/`; the SHAs are the commits that carried
  each script [verified @f46cf299 from the gallery's history].
  - Patch 2, `patch_L363_2_studio_lists_quoted_room_keys_20260926.py`
    (gallery `5a534d7`): Studio's New Interactive Card list, and the
    editor's live-link list, read a room key written in quotes. The
    room's key has a hyphen, so it needs the quotes, and the list had
    skipped it without saying so.
  - Patch 3, `patch_L363_3_date_line_and_editor_save_check_20260926.py`
    (`74624c0`): the room draws now, the minute it is opened, and says
    so under its title; the gallery editor refuses to save over a file
    that changed on disk since it loaded it.
  - Patch 4, `patch_L363_4_date_line_every_room_20260927.py`
    (`70a7734`): every room carries the line; the Earth room draws now
    too; the Sun room's line says it has no date.
  - Patch 5, `patch_L363_5_short_scene_titles_20260927.py`
    (`a484172f`): the scene titles drop "Paloma's Orrery --", and on an
    upright phone the title and line clear the buttons. Tony's phone:
    all three rooms correct.
  - Patch 6, `patch_L363_6_site_credit_and_camera_20260928.py`
    (`f46cf299`): every relayout the rooms and the Explorer make carries
    the live camera -- the + and - buttons had snapped a turned view
    back to its opening angle -- and a small palomasorrery.com link
    sits under the grid chip, drawn in the scene so the camera's
    picture carries it. Tony's phone and desktop: "correct". The
    live-camera rule was already in interactive-exhibit; the zoom caller
    had missed it. Worth a line naming every caller in that skill's
    touch-path section at its next bump.
  - The card "Solar System", 9:16, in the `solar_system` door, live
    link `interactive.html?exhibit=solar-system`, placard "Live data
    from JPL Horizons. Work in progress." Made in Studio once patch 2
    let Studio list the room; pushed at gallery `3f7f50ab`.
- **Tony's rulings in Half 1, 2026-09-27 and 28.** The line under the
  title is the reason for the exhibits: "it is the reason for the
  exhibit at all." The rooms draw now, not at midnight, in UTC only.
  Every room has the line; the Sun room's says it has no date, since it
  draws nothing that changes with time. Scene titles drop "Paloma's
  Orrery --", which the top bar and the address already say. The
  camera's picture is what the scene shows: "why would the camera
  button snapshot something that is not displayed?" So the site credit
  went into the scene rather than into the download alone. The full
  list is section 2 of
  `documentation/HANDOFF_L363_half1_done_half2_after_stage_d_20260928.md`.
- **The lost card, 2026-09-26.** Studio wrote the card into
  `gallery/gallery_metadata.json` at 22:03 and Tony's commit at 22:05
  captured it. At 22:06 the file was rewritten from an older copy
  without the card, carrying the gallery editor's save signature,
  though Tony had answered No to its save prompt. The cause was not
  found; Tony restored the card with Discard changes. Patch 3 closed
  how it could happen: Save All compares both files on disk with what
  it loaded and saves nothing if either changed. [tested headless, per
  that handoff, section 3]
- **The front door: design session, 2026-09-29** (zero code;
  `documentation/DESIGN_solar_system_room_front_door_20260929.md`,
  written with Claude Sonnet 5.5). The room becomes a second way into
  the gallery beside the card taxonomy, which stays the complete index.
  Tony's rulings are in that document's sections 3 to 5 and 7 and are
  not restated here. In short: the scene stays a clean orrery and
  everything about where to go next lives in the drawer; the room opens
  on the Sun and Earth with Earth's row highlighted; the drawer opens
  on ten rows (the Sun, the eight planets, Pluto) with "See more" for
  the groups; tapping a body selects it and ticking a row draws it;
  Home follows the last ticked body; groups are rooms with a cloud
  (L-391); encounters draw the room at their date (L-393); only what
  JPL Horizons can place is in scope.
  - **The swap** (design section 7) replaces plan B's last step. The
    room becomes the default once its nine bodies are in, not waiting
    for a date picker. In one commit: the Explorer card's live link
    becomes `interactive.html?exhibit=solar-system-explorer`; the
    page's fallback key becomes `solar-system` -- it occurs TWICE in
    `interactive.html`, lines 1091 and 1589 at gallery `f46cf299`
    [verified @f46cf299], and the swap patch counts two; the README's
    bare `interactive.html` link is checked. The Explorer stays a card
    in the `solar_system` door.
- **Three strands integrated, 2026-09-29.** D20 finishing Stage D,
  patch 6 finishing Half 1, and the design changing what Half 2 is,
  were reviewed against both repositories by two sessions in parallel,
  Claude Fable 5.1 and Claude Opus 5.5, which agreed on the substance.
  The filed result is
  `documentation/HANDOFF_L363_three_strands_integrated_20260929.md`; it
  supersedes the Half 1 handoff's sections 5 and 6.
- **Tony's ruling on the order, 2026-09-29: option C, "confirmed as
  recommended."** Half 2 is built through Tony's Mode 5 first; then the
  Sun's slice (L-322 point 3, L-371, L-386); then the swap, as a small
  patch of its own. After the Sun, in outline: the orrery's objects
  rebuilt in the gallery from its own dictionary, then encounters, then
  shells and slices (L-395). The reason: as the front
  door, the room sends visitors into the other rooms, so it becomes the
  default only once every room it leads into prints numbers served from
  the export. Half 2 and the Sun's slice both write
  `data/objects_config.json`, so they are never in progress at once.
  The master plan restamped to v35 at Tony's direction, which also
  answers the design's question whether it counted as a design build.
- **Half 2 as listed on 2026-09-26, superseded.** The card is done
  (`3f7f50ab`). "A link for each body" is replaced by the design's rule
  that a row's links are read from the exhibits and the card metadata
  (L-394). The five planets and Pluto remain, inside the design's list,
  Pluto last. The comets and Voyager 1 are part of the room's future
  (L-364, L-365).
- **Tony-action (decide), at Half 2:** whether ticking a drawer row
  also opens it (design question 13).
- **Tony-action (decide), at Half 2:** Apophis is drawn today but has
  no place in the ten-row drawer: one row under "See more" until the
  near-Earth asteroids round, or out of Half 2 until then.
- **For Half 2's Mode 5:** on a phone with many bodies ticked, a tap
  may pick the wrong one (design question 7).
**Gap (2026-09-26; SUPERSEDED):** Half 2 (above), after L-322 section 6 pushes; then Tony's decision on the default.
**Gap (2026-09-29):** Half 2 as section 4 of `documentation/HANDOFF_L363_three_strands_integrated_20260929.md` sets it out, from step 1 (step 0 was this entry): a short design round, the five planets and one cache rebuild, the drawer, Tony's Mode 5. The swap after the Sun's slice closes.
**Ref:** `documentation/HANDOFF_L363_three_strands_integrated_20260929.md`; `documentation/DESIGN_solar_system_room_front_door_20260929.md`; `documentation/HANDOFF_L363_half1_done_half2_after_stage_d_20260928.md`; `documentation/HANDOFF_explorer_symbols_half1_20260926.md` (rev 2); gallery `documentation/patch_solar_system_room_half1_20260926.py` and `patch_L363_2` to `_6`; L-286; L-099; L-322; L-364 to L-367; L-391 to L-395.
"""

# (kind, anchor, text[, end_anchor])
#   before  : insert text immediately before anchor
#   after   : insert text immediately after anchor
#   replace : replace anchor with text
#   span    : replace from the start of anchor through the end of end_anchor
LEDGER_EDITS = [
    ("before", "Review and RICE update Tony 6-21-2026\n", LEDGER_STAMP,
     "header stamp"),
    ("before", "#### [L-390] provenance-discipline does not yet name", NEW_ROWS,
     "L-391 to L-395 added"),
    ("replace",
     "<!-- L:378 status:OPEN upd:2026-09-28 section:A flag: rice: -->",
     "<!-- L:378 status:OPEN upd:2026-09-29 section:A flag: rice: -->",
     "L-378 date"),
    ("before", "**Gap:** A phone-sized headless run", L378_LINE,
     "L-378 line"),
    ("replace",
     "<!-- L:371 status:OPEN upd:2026-09-28 section:A flag: rice: -->",
     "<!-- L:371 status:OPEN upd:2026-09-29 section:A flag: rice: -->",
     "L-371 date"),
    ("after", "- The Sun is the next body's slice, since its room is published.\n",
     L371_LINE, "L-371 note"),
    ("replace",
     "<!-- L:367 status:OPEN upd:2026-09-26 section:A flag: rice: -->",
     "<!-- L:367 status:OPEN upd:2026-09-29 section:A flag: rice: -->",
     "L-367 date"),
    ("before", "**Gap:** A check that lists `EXHIBITS`", L367_LINE,
     "L-367 line"),
    ("replace",
     "<!-- L:365 status:OPEN upd:2026-09-26 section:A flag: rice: -->",
     "<!-- L:365 status:OPEN upd:2026-09-29 section:A flag: rice: -->",
     "L-365 date"),
    ("before", "**Gap:** `assemble_scene` warns", L365_LINE, "L-365 line"),
    ("replace",
     "<!-- L:364 status:OPEN upd:2026-09-26 section:A flag: rice: -->",
     "<!-- L:364 status:OPEN upd:2026-09-29 section:A flag: rice: -->",
     "L-364 date"),
    ("before", "**Gap:** The scene date checked against", L364_LINE,
     "L-364 line"),
    ("span", L363_START, L363_BLOCK, "L-363 rewritten", L363_END),
    ("replace",
     "<!-- L:322 status:OPEN upd:2026-09-28 section:A flag: rice:4/5/70/6 -->",
     "<!-- L:322 status:OPEN upd:2026-09-29 section:A flag: rice:4/5/70/6 -->",
     "L-322 date"),
    ("before", "**Ref:** L-305, L-306 (approximations", L322_NOTE,
     "L-322 note"),
]


# ====================================================================
# THE MASTER PLAN
# ====================================================================

SUMMARY_START = "## Executive summary -- v34, September 28, 2026\n"
SUMMARY_END = ("restamps have kept since July; this summary is the short "
               "form of it.\n")

SUMMARY = """\
## Executive summary -- v35, September 29, 2026

Built on orrery `e5c3f92a2ad1dd47ad8cb35d17c159e07f1a9cf9` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`f46cf299c2b6e93e5f3ba405c4ad62032e7666ae` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on 2026-09-29. This summary is rewritten at every restamp. It replaces
`MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`, and Section 5a of this
document replaces `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`; both are kept
as dated records (Tony's ruling of 2026-09-28, L-333 and L-362).

**What this plan is for.** It is the roadmap for the interactive
gallery at palomasorrery.com. The end goal is the orrery's own Python,
running in the browser, serving interactive rooms that anyone can open
without installing anything (Section 5a, The end goal). The ledger says
what is done; this plan says what order the work goes in.

**Where we are.**

- Two rooms are live and complete in `interactive.html`: the Sun,
  since 2026-08-29, and Earth, since 2026-09-10, each accepted on
  Tony's phone and desktop check (Mode 5).
- A third, the Solar System room, draws the Sun, Earth, Jupiter, Saturn
  and Apophis as symbols on their orbits, at the minute it is opened,
  and says so under its title (L-363). Its first half is finished: six
  gallery patches and its card, the last at gallery `f46cf299`.
- On 2026-09-29 a design session made the Solar System room the
  gallery's FRONT DOOR: a second way in beside the card taxonomy, which
  stays the complete index. A visitor sees the Sun and Earth, opens a
  drawer of the planets, ticks one to draw it, and reaches that body's
  room and cards. The record is
  `documentation/DESIGN_solar_system_room_front_door_20260929.md`.
- The numbers reach the gallery through one route. The orrery exports
  them from `constants_new.py` into `constants_export.json`, with each
  number's unit and figure count; the gallery pulls that file and writes
  each number into `objects_config.json` from it. Nobody types a
  constant into the gallery.
- Earth is the store's first CLOSED SLICE (2026-09-22). Every number
  its room prints has a unit, a status, a figure count, and a record of
  who opened its source. A missing field on an Earth row fails the
  maintenance run.
- L-322 Stage D finished on 2026-09-28, and L-345 closed with patch D20
  at orrery `e5c3f92a`: a value in another unit is computed from its
  one source row instead of being stored twice. Earth's crust is drawn
  at the mean radius in both the orrery and the gallery.

**What comes next, in order** (Tony's ruling of 2026-09-29, option C:
"confirmed as recommended").

1. **The Solar System room's second half, up to Tony's phone check**
   (L-363). Mercury, Venus, Mars, Uranus, Neptune and then Pluto join
   the room; the drawer gets its ten rows with tick boxes; the room
   opens on the Sun and Earth; Home follows the design's rule. It is
   built and accepted, but not yet the page a bare link opens.
2. **The Sun's slice** (L-371, L-386). Its rows are walked the way
   Earth's were: each gets its unit, status and figure count, and each
   value the Sun's store keeps in a second unit becomes a conversion of
   its source row.
3. **The swap.** The Solar System room becomes the page
   `interactive.html` opens when no room is named, and the Explorer
   stays a card with its own link. It waits for step 2 so that the front
   door leads only into rooms whose numbers are served from the export.
4. **After the Sun: the orrery's objects, rebuilt in the gallery**
   (Tony's direction of 2026-09-29, in outline; L-395). The gallery
   grows the way the orrery did: symbols with positions from Horizons
   and osculating orbits first, moons with them; then encounters,
   comets and spacecraft; then shells and slices for the graphical
   detail, which is where Jupiter and Saturn's Artifact 2 now falls.
   The objects come from the orrery's own dictionary,
   `celestial_objects.py`, exported the way the constants are and
   checked against JPL Horizons. It opens with its own design round.

Steps 1 and 2 are never in progress at the same time: both write
`data/objects_config.json` and both end in a cache rebuild. Step 4's
design round takes in the questions the front-door design left open:
groups, the drawer's list, encounters and cards (L-391 to L-394, with
L-364 and L-365).

**Open decisions for Tony.** Two at Half 2: whether ticking a drawer
row also opens it, and whether Apophis keeps a row until the near-Earth
asteroids round (L-363). Two in the orrery, neither on the critical
path: the Sun's Auto view opens about 31 times wider since Stage D
(L-385), and whether Earth's atmosphere tops are measured from the
equatorial or the mean radius (L-389).

**How to read the rest.** Section 5a is the critical path: the end
goal, the five segments, the order they are worked in, and a dated
subsection for each design build. Sections 1 to 4 are the architecture.
Section 6 is the history of every ruling. Section 7 lists the open
decisions. The long status block below is the running record the
restamps have kept since July; this summary is the short form of it.
"""

LAST_UPDATED_OLD = ("**Last updated:** September 28, 2026 (v34: a DESIGN "
                    "BUILD, L-345,")
LAST_UPDATED_NEW = """\
**Last updated:** September 29, 2026 (v35: a DESIGN BUILD, L-363. The
Solar System room becomes the gallery's front door (the design session
of 2026-09-29), and the order changes on Tony's ruling C: the room's
second half through his Mode 5 first, then the Sun's slice, then the
swap that makes the room the default. After the Sun, in outline: the
orrery's objects rebuilt in the gallery from its own dictionary and
checked against Horizons, then encounters, then shells and slices. The
executive summary is rewritten and Section 5a gains the 2026-09-29
subsection; with Anthropic's Claude Opus 5.5, from a review Claude
Fable 5.1 did in parallel. v34, September 28, 2026: a DESIGN BUILD, L-345,"""

V32_START = "Opus 5.5 (the gallery half and this update). v32, September 16, 2026:\n"
V32_END = "gains the 2026-09-15/16 subsection; with Anthropic's Claude Opus 5.)\n"
V32_REPLACEMENT = "Opus 5.5 (the gallery half and this update).)\n"

SUBSECTION_ANCHOR = "### What this section deliberately does not carry\n"

SUBSECTION = """\
### 2026-09-29 -- the Solar System room becomes the front door, and the order changes

**A design session made the room the gallery's front door.** Zero
code, recorded in
`documentation/DESIGN_solar_system_room_front_door_20260929.md`. Until
now the gallery had one way in, the card taxonomy of doors, rooms and
cards. Tony's idea is a second, more intuitive one: the solar system
itself. The taxonomy stays the complete index; nothing is removed. The
rulings, in short:

- The scene stays a clean orrery. Everything about where to go next
  lives in the drawer.
- The room opens on the Sun and Earth, the drawer closed and Earth's
  row highlighted, the view fitting 1.1 times Earth's distance. The aim
  is curiosity, not the whole system at once.
- The drawer opens on ten rows: the Sun, the eight planets and Pluto.
  "See more" adds the groups in place along the spine, outward from the
  Sun.
- Tapping a body selects it and highlights its row; ticking a row draws
  it and reframes the view. Everything ticks except the Sun.
- Groups (the main belt, the Trojans, near-Earth asteroids,
  trans-Neptunian objects) become rooms with a cloud, served once and
  drawn like a shell. Encounters draw the whole room at their date.
  Only what JPL Horizons can place is in scope.
- The swap: the room becomes the default once its nine bodies are in,
  without waiting for a date picker. The Explorer stays a card.

**Three strands met the same day.** Stage D had finished and patch D20
had landed (orrery `e5c3f92a`), which opened the gate the room's second
half had waited on. Patch 6 had finished the first half (gallery
`f46cf299`). And the design had changed what the second half is. Two
sessions, Claude Fable 5.1 and Claude Opus 5.5, reviewed the three
records against both repositories independently and agreed on the
substance. The filed result is
`documentation/HANDOFF_L363_three_strands_integrated_20260929.md`.

**The order changed, on Tony's ruling.** v34 put the room's second
half third, beside the Sun's slice and Artifact 2, when the room had no
purpose beyond itself. As the front door it sends visitors into the
other rooms, and the Sun room still prints numbers typed into the
gallery rather than served from the export (L-371). Three options went
to Tony: the second half next, swap included; the v34 order; or the
second half next with the swap held until the Sun's slice closes. Tony,
2026-09-29: "C. Confirmed as recommended." So the room is built and
accepted now, and becomes the default only when every room it leads
into prints served numbers.

**One constraint travels with the order.** The second half adds object
entries to `data/objects_config.json`; the Sun's slice rewrites the
Sun's served values in the same file through the gallery's mirror. Both
end in a cache rebuild. They are never in progress at once: one is
pushed and live-checked before the other starts.

**After the Sun, a direction in outline** (Tony, 2026-09-29, L-395).
"In the original orrery the shells came late." The gallery grows the
same way: symbols with positions from Horizons and osculating orbits
first, moons with them; then encounters; then shells and slices. The
objects come from the orrery's own dictionary, `celestial_objects.py`,
exported the way the constants are, so the gallery stops keeping a
hand-copied list; already the two copies disagree on Apophis's ID.
And because the dictionary itself can go stale, the check reaches past
it to JPL Horizons. Jupiter and Saturn's Artifact 2, v34's next step,
now falls in the shells phase. The details are that design round's.

**This restamp is at Tony's direction.** The design asked whether it
counted as a design build for the plan's restamp (L-296); Tony answered
by asking for the plan to reflect the ruling.

**Next.** The second half of L-363, from the integrated handoff's
section 4, step 1: a short design round, the five planets and one cache
rebuild, the drawer, and Tony's Mode 5. Then the Sun's slice, then the
swap, then the design round for the orrery's objects (L-395).

"""

PLAN_EDITS = [
    ("span", SUMMARY_START, SUMMARY, "executive summary rewritten (v35)",
     SUMMARY_END),
    ("replace", "**Status:** v34 --", "**Status:** v35 --", "status stamp"),
    ("replace", "5a's newest subsection, 2026-09-23 to 28.**",
     "5a's newest subsection, 2026-09-29.**", "status block's pointer"),
    ("replace", LAST_UPDATED_OLD, LAST_UPDATED_NEW, "Last updated: v35 added"),
    ("span", V32_START, V32_REPLACEMENT,
     "Last updated: v32 entry dropped (three kept)", V32_END),
    ("replace",
     "Claude Opus 5, Claude Opus 5.5, Claude Fable 5, Claude Fable 5.1,\n"
     "Claude Sonnet 5, GPT\n",
     "Claude Opus 5, Claude Opus 5.5, Claude Fable 5, Claude Fable 5.1,\n"
     "Claude Sonnet 5, Claude Sonnet 5.5, GPT\n",
     "participants"),
    ("before", SUBSECTION_ANCHOR, SUBSECTION, "Section 5a: 2026-09-29 added"),
]


# ====================================================================
# THE HARNESS
# ====================================================================

def outside_index(text):
    if INDEX_START in text and INDEX_END in text:
        a = text.index(INDEX_START)
        b = text.index(INDEX_END) + len(INDEX_END)
        return text[:a] + text[b:]
    return text


def fingerprint(path, raw):
    text = raw.replace(b"\r\n", b"\n").decode("utf-8")
    if path == LEDGER:
        text = outside_index(text)
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def once(text, anchor, path, label):
    n = text.count(anchor)
    if n != 1:
        raise SystemExit(
            "ANCHOR FAIL (%s): expected 1 match in %s, found %d:\n  %r\n"
            "NOTHING was written to either file." % (label, path, n,
                                                     anchor[:70]))


def apply_edits(path, text, edits, nl):
    done = []
    for edit in edits:
        kind, anchor, new, label = edit[0], edit[1], edit[2], edit[3]
        a = anchor.replace("\n", nl)
        n = new.replace("\n", nl)
        once(text, a, path, label)
        if kind == "before":
            text = text.replace(a, n + a)
        elif kind == "after":
            text = text.replace(a, a + n)
        elif kind == "replace":
            text = text.replace(a, n)
        elif kind == "span":
            end = edit[4].replace("\n", nl)
            once(text, end, path, label + " (end)")
            i = text.index(a)
            j = text.index(end, i)
            if j < i:
                raise SystemExit("ANCHOR FAIL (%s): the end comes before "
                                 "the start. NOTHING was written." % label)
            text = text[:i] + n + text[j + len(end):]
        else:
            raise SystemExit("ERROR: unknown edit kind %r" % kind)
        done.append(label)
    return text, done


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit(
            "ERROR: run this from the ORRERY repo ROOT, next to "
            "palomas_orrery.py -- not from documentation/. NOTHING was "
            "written.")
    for path in (LEDGER, PLAN):
        if not os.path.isfile(path):
            raise SystemExit(
                "ERROR: %s is not here, so this is not the orrery root. "
                "NOTHING was written." % path)

    results = {}
    for path, edits in ((LEDGER, LEDGER_EDITS), (PLAN, PLAN_EDITS)):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(path, raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s.\n"
                "       (Line endings and the ledger's INDEX zone are "
                "excluded, so neither is the cause.)\n"
                "       NOTHING was written to either file. Undo is "
                "Discard Changes in GitHub Desktop."
                % (path, BASE[path], got))
        nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
        text, done = apply_edits(path, raw.decode("utf-8"), edits, nl)
        bad = sum(1 for ch in text if ord(ch) > 127)
        if bad:
            raise SystemExit(
                "ERROR: %s would hold %d non-ASCII character(s) after the "
                "patch. NOTHING was written." % (path, bad))
        results[path] = (text, done)

    # Both files passed every check; only now is anything written.
    for path in (LEDGER, PLAN):
        text, done = results[path]
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-48s %s" % (path, label))
    print("")
    print("Stamps updated: the ledger's header (Module updated, "
          "September 29, 2026);")
    print("the master plan's executive summary, Status and Last updated "
          "(v35).")
    print("")
    print("patch applied (%d edits in %s, %d in %s)"
          % (len(LEDGER_EDITS), LEDGER, len(PLAN_EDITS), PLAN))
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py")
    print("  2. Move this script into documentation/.")
    print("  3. Put DESIGN_solar_system_room_front_door_20260929.md and")
    print("     HANDOFF_L363_three_strands_integrated_20260929.md in")
    print("     documentation/, with your local copies of the two")
    print("     2026-09-28 handoffs. Commit and push.")
    print("  4. Tell Claude the new orrery SHA.")


if __name__ == "__main__":
    main()
