# HANDOFF ADDENDUM -- 2026-09-04: the two schemas for L-287 (editor and room tree)

**Built on** orrery `840dc7034814092963a350bb847baf59a72ebdf2` at
https://github.com/tonylquintanilla/palomas_orrery (branch main) --
the SHA that carries both ledger patches from today (L-280 retired,
L-282 rewritten to three doors, L-286 and L-287 opened, L-283 and the
master plan realigned). Gallery `e414af13d4c4c736a6c6d792d3fe7ad651f2fbdc`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
unchanged today. Both confirmed live.

**Type:** design addendum, zero code. Extends HANDOFF 2026-09-04 ("the
doors close, the rooms get four levels, the editor gets a design").
Settles the one design question that handoff left for the next
session: the shape of the two JSON files. Tony reviewed both examples
and made one addition (rooms carry a `sentence`, not only doors).

**Ruling on timing:** design now, build next session. The editor is a
Tkinter GUI and needs Tony's eyes on it, not py_compile; a build
delivered while he is away from the machine cannot be accepted.

---

## Schema 1: `gallery_config.json` becomes the room tree

Nested. The tree in the file IS the tree in the editor and the chain
in the breadcrumb. `version: 2` lets every consumer tell old from new.

```json
{
  "version": 2,
  "doors": [
    {
      "key": "solar_system",
      "label": "Solar System",
      "short": "solar",
      "color": "#c9a44a",
      "sentence": "One sentence for the door's placard.",
      "rooms": [
        {
          "key": "orbital_mechanics",
          "label": "Orbital Mechanics",
          "short": "orbits",
          "sentence": "One short line for this room.",
          "special": true,
          "rooms": []
        },
        {
          "key": "earth",
          "label": "Earth",
          "short": "Earth",
          "sentence": "One short line for this room.",
          "rooms": [
            {
              "key": "moon",
              "label": "The Moon",
              "short": "Moon",
              "sentence": "One short line.",
              "rooms": [
                { "key": "artemis_ii", "label": "Artemis II",
                  "short": "Artemis II", "sentence": "One short line.",
                  "rooms": [] }
              ]
            }
          ]
        }
      ]
    },
    {
      "key": "earth_system", "label": "Earth System", "short": "earth",
      "color": "#3f9a8a",
      "sentence": "Data preservation is climate action.",
      "rooms": [
        { "key": "heatdome", "label": "Heat Domes", "short": "heat domes",
          "sentence": "One short line.", "rooms": [] }
      ]
    },
    {
      "key": "stars", "label": "Stars", "short": "stars", "color": "#7a6bb5",
      "sentence": "One sentence for the door.",
      "rooms": [
        { "key": "exoplanets", "label": "Exoplanets", "short": "exoplanets",
          "sentence": "One short line.", "rooms": [] }
      ]
    }
  ],
  "storage": { "key": "other", "label": "Storage", "hidden": true }
}
```

Field rules:

- `key`: ASCII, lowercase, underscores; unique among siblings. A card's
  `room` is the keys joined with `/`: `solar_system/earth/moon/artemis_ii`.
- `label`: the full name, used in room headers and the editor tree.
- `short`: the breadcrumb name (L-286): `solar: Earth: Moon: Artemis II`.
- `sentence`: one short line for the placard. **On every level** --
  doors, rooms, special exhibits (Tony, 2026-09-04: "yes for short
  descriptors"). Cards keep their own `description`; a visitor reads
  the room's sentence at the top of the grid, each card's beneath it.
- `color`: doors ONLY. Rooms inherit their door's accent; a mission
  takes its body's room (L-283 as realigned).
- `special`: marks a side gallery (Orbital Mechanics). Rendering is
  the same; the flag exists so the editor and the overview can set it
  apart.
- `rooms`: always present, possibly empty. Four levels is the working
  ceiling (L-286); the schema does not enforce it, the editor warns.
- A room with no cards in it yet needs no flag: emptiness IS the
  "not yet reached" state, and it takes the construction material.
- `storage`: the one hidden room. `hidden: true` is what the lobby and
  breadcrumb test; the editor shows it at the bottom of the tree.
- The color values above are placeholders shaped like L-283's names
  (warm gold, blue-green, cool violet). L-283 sets the real ones.

## Schema 2: `gallery_metadata.json` -- one card per exhibit

```json
{
  "id": "earth_moon_magnetosphere",
  "title": "Earth and Moon with Magnetosphere",
  "description": "One-sentence placard for this card.",
  "room": "solar_system/earth",
  "shape": "16:9",
  "files": {
    "landscape": "earth_moon_magnetosphere_gallery.json",
    "portrait":  "earth_moon_magnetosphere_mobile.json"
  },
  "live": null,
  "featured": false,
  "sources": [],
  "converted": true,
  "size_kb": { "landscape": 812, "portrait": 640 }
}
```

Field rules:

- `room`: replaces `category`, `category_label`, `subcategory`,
  `subcategory_label`. A path into the tree, or `"other"` for storage.
  The labels are looked up from the tree, never stored on the card --
  that is what makes a rename land everywhere.
- `files`: replaces `filename` and `mode`. One or two keys,
  `landscape` and/or `portrait`. One key: the page shows that file in
  both orientations. Two keys: the page picks by screen width, which
  `index.html` already detects (line 1880 at gallery `e414af13`).
- `shape`: `"16:9"` or `"9:16"`. Governs the PHONE ONLY (L-286):
  16:9 sweeps for 2D and scales to fit for 3D; 9:16 shows as today.
  Desktop is unchanged.
- `live`: the URL of a live scene when this card is the doorway into
  an interactive room (`"interactive.html?exhibit=sun"`); `null`
  otherwise. This is the "live scene is one card in the grid" rule
  from L-282.
- `featured`: the flag the editor sets and What's New reads (L-287).
- `sources`: the citation list; empty is allowed and honest.
- `size_kb`: per file, keyed like `files`.
- `id`, `title`, `description`, `converted`: unchanged from today.
- The top-level file keeps `visualizations`, `last_updated`,
  `total_count` (the count is now cards, not files).

## The migration, mechanical half only

One-shot script (safe-file-editing fires; guards on both files' md5 at
the gallery SHA it is built against):

1. Pair the 33 duplicate exhibits (same title, one `_gallery.json`
   landscape card and one `_mobile.json` portrait card) into one card
   with two `files` keys. Print the 33 titles.
2. Rewrite the other 82 cards to one `files` key each. `mode: both`
   (28 cards) and absent `mode` (24 cards): one file, landscape key.
3. Set every card's `room` to `"other"`; set `shape` from the file's
   orientation (portrait file only -> `"9:16"`, else `"16:9"`) as a
   first guess Tony corrects in the editor; set `live` to `null`;
   carry `featured` as is.
4. Write the three doors with their body rooms, all empty, and the
   storage room. Sentences are placeholders Tony fills in the editor.
5. Print counts AND names for anything it could not pair or read.

Tony then remodels IN THE EDITOR: moves cards out of storage into
rooms, creates the level-2 rooms under Earth System from the nine
`climate` subcategories (one-for-one or regrouped -- his decision,
"very important"), fills in sentences, corrects shapes, sets `live` on
the Sun card. The category-to-room mapping is NOT a table in
conversation (Tony's ruling).

## Consumers to sweep before the schema changes (Check All Parallel Pipelines)

`index.html` (reads `category`, `subcategory`, `mode`, `filename`),
`tools/json_converter.py` (writes cards), `tools/gallery_editor.py`
(reads and writes both files), `tools/gallery_studio.py` (may write
cards on export -- grep before assuming), and `interactive.html` (will
read the tree for its breadcrumb; reads neither file today). Grep all
five for the four old field names before building. Two of the five are
in the gallery repo; all of these are.

## Tony-actions

- **(decide, at the machine)** Read both schemas back. Anything that
  reads wrong is cheaper to change now than after the migration runs.
- **(do, next session)** Build L-287: the migration script, then the
  editor changes (tree to depth four, move-to-room, two file slots,
  shape, sentence, featured, storage room, save prints what changed).
  Deliver the migration first and alone; the editor after it has run.
- **(decide)** The nine `climate` subcategories: level-2 rooms
  one-for-one, or regrouped. Can wait until the editor is in hand.

---

*Written September 4, 2026 with Anthropic's Claude Fable 5.1. Built on
orrery `840dc703`, gallery `e414af13`. No pushes after `840dc703` this
session.*
