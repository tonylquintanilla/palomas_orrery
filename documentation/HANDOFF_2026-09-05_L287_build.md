# HANDOFF -- 2026-09-05 (BUILD): L-287 built and live -- migration, readers, editor, remodel

**Built on** orrery `9652a43db8361a9d904002e6a4271a34281be8a1` at
https://github.com/tonylquintanilla/palomas_orrery (branch main) --
unchanged all session; one ledger patch is delivered and NOT yet run.
Gallery started at `e414af13d4c4c736a6c6d792d3fe7ad651f2fbdc` and ends at
`503fa387068a176fa7e12d2ab8df3752c8ffe429` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, after six
pushes by Tony, each confirmed live with `git ls-remote` before the next
build step.

**Type:** BUILD. Companion to HANDOFF 2026-09-04 (design) and its
ADDENDUM (the two schemas), which this session executed. Tony was at his
machine for the build and remodel and away at the close.

**Skills loaded and checked against the manifest (all match):**
safe-file-editing 1.10, gallery-pipeline 1.2, ledger-and-session-records
1.9, agentic-pre-test 1.2. No skill changed this session.

---

## What is live at gallery `503fa387` [verified: files read at that SHA]

- `gallery_config.json` and `gallery_metadata.json` are schema version 2
  (room tree; one card per exhibit with `room`, `files`, `shape`,
  `live`, `featured`, `sources`). 105 cards, 0 in storage, every card's
  room path resolves. One live card: the Sun, `interactive.html?exhibit=sun`.
  7 featured. 52 cards have no sources yet.
- Rooms with cards: Solar System (3 loose, Orbital Mechanics 1, Sun 1,
  Earth 5, Moon 7, Jupiter 2, Pluto 2, Comets 11, Asteroids 5, Space
  Missions 2); Earth System (11 loose, Extreme Heating Events 39,
  Paleoclimate 5, Food Insecurity 1, Coral Bleaching 1); Stars (Distance
  3, Magnitude 4, Exoplanets 2). Empty, showing as under construction:
  Mercury, Venus, Mars, Saturn, Uranus, Neptune, Galactic Center, and
  the Stars door itself has no loose cards. Tony added Comets, Asteroids,
  Space Missions and the four Earth System rooms in the editor.
- `index.html` carries a READER SHIM, not the lobby: it maps a card's
  room to today's category headers, serves the file by the
  Landscape/Portrait toggle, hides storage, shows room sentences under
  headers and sources under cards, opens a live card's scene on click.
  L-282 / L-286 replace this UI; the shim exists so the schema could
  ship first.
- `tools/gallery_editor.py` is the schema-v2 editor (1,100 lines,
  complete rewrite; the v1 editor could not read the new files). Two
  panes; the room tree with storage at the bottom; move / copy / reorder
  / new room / delete (empty rooms only); two file slots; shape; live
  URL picker read from `interactive.html`; featured; sources; Preview
  through `index.html?preview=` (local server if `serve_gallery.py`
  answers, else palomasorrery.com); fields apply on focus-out; Save All
  prints changes by name; no `.bak`.
- `tools/json_converter.py` writes v2 cards into storage and skips the
  category prompt when the config is v2. `tools/gallery_cleanup.py`
  counts both file slots as referenced (it DELETES orphans; patched
  before it was next run).

Mode 5 by Tony, on the live site and on the phone: card counts correct
after migration (90 landscape, 58 portrait); storage hidden; sentence
and sources shown; live Sun card opens the scene. All passed.

## Discrepancies surfaced (the record was wrong; the file was right)

- The addendum said 33 landscape/portrait pairs. Pairing by EFFECTIVE
  mode (absent = landscape) gives 38; the filename suffix is not the
  rule. Four titles were duplicated in the same orientation (9 cards);
  left separate and named by the migration; Tony has since deleted some.
- The addendum listed five consumers. There are seven: add
  `tools/gallery_cleanup.py` (dangerous -- deletes unreferenced files)
  and `tools/gallery_json_fixer.py` (reads figure JSON only; clear).
- The shim's first version printed "NaN KB" for the per-slot size dict;
  fixed in patch 4. My own bug, found while reading the render code.
- One delivery did not land: the second editor file was downloaded but
  not saved over the repo copy, and the following push carried the old
  version. Caught by comparing the repo copy's md5 to the delivered
  file, not by the commit message. Redelivered; the copy at `503fa387`
  matches.

## Sequencing ruling worth keeping

Rewriting the index files in place would have blanked the live page
until the lobby existed, blocking every gallery push meanwhile. Tony
chose to widen L-287: migration plus a small reader shim plus the two
tool patches, all in one push. The lobby replaces the shim later. The
general form: a schema change and its readers land together, or not at
all.

## Delivered, not yet run

`patch_L287_6_ledger_close.py` -- orrery repo root, VS Code Run, then
`ledger_index.py`, commit both, push. Guards on the ledger at
`9652a43d` (CRLF-safe; refuses a second run; tested on LF and CRLF
copies and through the real indexer, which moved L-287 to section C and
placed L-288 at 3.1 and L-289 at 4.8 on the board). It writes:
- header stamp;
- L-287 -> DONE with the built-and-live record, the two corrections
  above, Gap none;
- L-288 opened: Gallery Studio creates and edits live-scene cards
  (Tony's request 2026-09-05);
- L-289 opened: Sun exhibit on the phone, 3D axis labels not visible
  (Tony's phone-pass finding 2026-09-04, with his suggested fix: labels
  on the top view for x, y and the back view for z);
- L-282 Gap: L-287 marked done, "two doors" corrected to three, and the
  What's New decision (flag / dated feed / both) carried here from L-287.

## Tony-actions, rolled up

- **(do)** Run `patch_L287_6_ledger_close.py`, then `ledger_index.py`,
  commit, push; report the orrery SHA.
- **(do)** Move the spent scripts to `documentation/` in the gallery
  repo: `patch_L287_2..5_*.py` at the root, `gallery/patch_L287_1_*.py`
  and `gallery/patch_L287_1_test_output.txt`; and this handoff and the
  ledger patch to the orrery `documentation/` once run.
- **(do)** Keep testing the editor; report what feels wrong.
- **(decide)** What's New: `featured` flag, dated feed, or both (L-282).
- **(decide)** Whether the nine empty rooms stay visible as under
  construction on the lobby, or hide until they have a card. Not ruled
  yet; the shim shows them only in the editor today because the old
  category view lists cards, not rooms.

## Next session, per L-282's build order

The lobby screen with its three doors, What's New and the guest book
(L-281 -- Tony, 2026-09-05: "don't forget the visitor guestbook"), then
drill-down and breadcrumb (L-286), then the stylesheet (L-283). L-289
(phone axis labels) is small and independent; L-288 (Studio live cards)
waits on the lobby's decision about how a live card looks in a grid.

Session start: confirm orrery HEAD past `9652a43d` carries the ledger
patch; gallery HEAD at or past `503fa387`; skills as above.

---

*Session written September 5, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `9652a43d`, gallery `e414af13` -> `503fa387`.*
