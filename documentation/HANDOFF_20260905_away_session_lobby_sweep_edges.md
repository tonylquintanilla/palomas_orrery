# HANDOFF -- 2026-09-05 (BUILD, away session): the lobby, the sweep, the twelve-edge labels -- built, tested headless, not run

**Built on** orrery `9652a43db8361a9d904002e6a4271a34281be8a1` at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery `503fa387068a176fa7e12d2ab8df3752c8ffe429` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both confirmed live with `git ls-remote` at session start; neither
moved during the session. Nothing was pushed: Tony was away from his
machine throughout. Every deliverable below is a file waiting at a repo
root.

**Type:** BUILD (patches delivered, unrun) with three design rulings.
Companion to HANDOFF 2026-09-05 (L-287 build), whose ledger patch
`patch_L287_6_ledger_close.py` was delivered there and is ALSO still
unrun. Reads that handoff's Tony-actions as still open.

**Skills loaded and checked against the manifest (all match):**
gallery-pipeline 1.2, safe-file-editing 1.10, ledger-and-session-records
1.9, gallery-assembler 1.2 (version line read). No skill changed.

---

## Rulings (Tony, by phone)

- **L-282, the lobby.** The section is FEATURED, from the existing
  `featured` flag; no dated feed. Live-scene cards read INTERACTIVE
  wherever a visitor sees them. Empty rooms read UNDER CONSTRUCTION.
  Arrangement approved from a portrait mockup: title, museum sentence,
  three door rows, Featured grid, guest book row, footer; doors above
  Featured. Door sentences are Tony's, entered through the editor.
- **L-286, room shape.** "No squeezed landscape." Landscape on the phone
  stays as it is; in portrait a 16:9 room sweeps sideways rather than
  compressing. (L-287's rule that every card shows in both orientations
  is confirmed; the shim's mode filter was a leftover.)
- **L-289, axis labels.** Labels on all TWELVE edges of the Sun's box,
  tick values and axis names; thinned to every second or third grid
  line; no label at a vertex; the axis name on the unlabeled grid line
  nearest the centre of each edge; no dimming with distance. Clutter is
  decided in Mode 5. Also noted: the phone's frame zoom (grid re-labels
  as you go in) is better information than the desktop's camera zoom.

## Delivered, all unrun -- run order

Orrery root, in this order:
1. `patch_L287_6_ledger_close.py` (prior handoff), then `ledger_index.py`.
2. `patch_L282_3_ledger_lobby_sweep_edges.py`, then `ledger_index.py`
   again. Guards on the PREDICTED ledger after step 1 -- predicted by
   re-running step 1 and the indexer here (the indexer is
   deterministic). If it refuses with "prediction missed", nothing is
   wrong with the files; the next session rebuilds it from the real
   ledger.
3. `patch_L282_4_master_plan_v24.py` (independent file; any time).
Commit all, push, report the orrery SHA.

Gallery root, in this order:
1. `patch_L282_1_lobby.py` -- guards on `index.html` at `503fa387`.
2. `patch_L282_2_sweep.py` -- guards on patch 1's output.
3. `patch_L289_1_edge_labels.py` -- guards on `interactive.html` at
   `503fa387`; independent of 1 and 2.
4. `patch_L289_2_name_on_skipped_tick.py` -- guards on patch 3's output.
Commit, push, report the gallery SHA. Then `gallery_maintenance_run.py
--live` as usual.

md5 of each delivered file, so a copy that did not land can be caught
the way one was caught last session:
- patch_L282_1_lobby.py `361c5aa67158f84d7a46e3add09d029d`
- patch_L282_2_sweep.py `525cc776792b8d15f40de4ed21e70993`
- patch_L289_1_edge_labels.py `6ebfdd1d31c8939041b8ef09fd1b2fbb`
- patch_L289_2_name_on_skipped_tick.py `59e542cd9a887055a6b68c1f84302f8a`
- patch_L282_3_ledger_lobby_sweep_edges.py `fe5ee322a2ae3daf4c356a75fd540d04`
- patch_L282_4_master_plan_v24.py `ee94d40e1c0cf56198d0c80bd58689be`

## What each patch does (one line each; detail in the ledger patch)

- **L282_1:** `index.html`'s first screen becomes the lobby; one writer
  (`renderLobby()`) replaces three; a door tap opens the existing menu
  at that door until L-286; "Live scene" -> "Interactive"; guest book
  row reads Under construction until L-281.
- **L282_2:** the mode filter is lifted (105 exhibits on the phone, not
  56); on a phone in portrait a 2D plot from a landscape-only card is
  drawn at its own width, full height, and `.viz-container` scrolls
  sideways with Plotly's `dragmode` off while swept; rotation
  restores; 3D scales to fit; desktop unchanged.
- **L289_1:** the Sun's tick values and axis names on all twelve edges
  as one text trace, rebuilt after every frame change; Plotly's own
  one-edge labels off on the Sun; `?ticks=N` for Mode 5.
- **L289_2:** the axis name takes the unlabeled grid line nearest the
  centre instead of displacing a tick label.

## How they were tested, and what that does and does not show

Every patch was applied to throwaway LF and CRLF copies, refused a
second run, and produced identical normalized output on both.

Lobby and sweep were exercised on the REAL patched `index.html` in
headless Chromium (Playwright) at 390x844 mobile and 1280x800, with the
served metadata and config at `503fa387`, a few figure JSON files pulled
from the repo, and Plotly served locally because the CDN is blocked in
the sandbox. Passed: lobby render; door tap opens the menu at Stars; a
Featured card draws its plot; Home returns to the lobby; the lobby's i
button opens About; the 66 Ma paleoclimate card swept to 1429 px in a
390 px room and a touch swipe scrolled it 288 px; rotation cleared and
restored the sweep; a 3D card and a two-slot card did not sweep; no
script errors. Not shown: fonts and the dove wall (blocked / not
cloned), and how the drag handoff feels in a hand.

Edge labels were exercised in a STAND-IN page, not the Sun page:
Pyodide's CDN is blocked here, so the Sun exhibit cannot start. The
stand-in loads Plotly, the new functions lifted from the patched file,
the Sun camera and arrival ranges. Passed: 36 labels installed; values
re-scaled with the grid on zoom; name placement for ticks=1, 2, 3 as
designed; no script errors. Not shown: how the labels read over the
real shells and the drawer.

## Discrepancies surfaced

- The reader shim (L-287) kept the page's mode filter, so 49 of 105
  exhibits were hidden from phone visitors, against L-287's own rule.
  Surfaced by the lobby's counts; recorded as a note on the closed
  L-287 and fixed under L-286.
- The mockup notes said the hamburger "goes away". It cannot yet: until
  L-286 the menu is the only way into a room. It stays one more step.
- The museum sentence has no editor field. The lobby reads a top-level
  `sentence` in `gallery_config.json` if present, else today's text.
- Warming Stripes is stored 1200x1400, so it sweeps only to 689 px. If
  a card should be wider than its file says, that is a Studio export
  question.
- One test run of mine copied a patch to only one of two test
  directories and I read the old code's output as the new code's for
  one message before catching it. Recorded because the shape matters:
  a test that ran on the wrong file passed.

## Tony-actions, rolled up

- **(do)** Orrery: run `patch_L287_6`, `ledger_index.py`,
  `patch_L282_3`, `ledger_index.py`, `patch_L282_4`; commit; push; SHA.
- **(do)** Gallery: run the four patches in the order above; commit;
  push; SHA; `gallery_maintenance_run.py --live`.
- **(do)** Mode 5 on the phone: the lobby (doors, a door tap, a
  Featured card, Home); one landscape-only 2D card in portrait (the
  sweep, the swipe, rotation); the Sun (rotate, +, -, Home; try
  `&ticks=3`).
- **(do)** Move spent scripts to `documentation/` in both repos: the
  L-287 set from the prior handoff, and these once run.
- **(do)** Enter the door sentences in the editor (Solar System, Stars).
- **(decide, after Mode 5)** L-289 tick density and label size; whether
  the Explorer room gets the same edges.
- **(decide, after Mode 5)** Whether the museum sentence gets an editor
  field or is set in the JSON by hand.
- **(decide)** Whether the nine empty rooms stay visible as Under
  construction on the door pages once L-286 draws them (the lobby
  today only counts them).

## Next session

Start: confirm orrery HEAD past `9652a43d` carrying the three ledger
and plan patches; gallery HEAD past `503fa387` carrying the four
patches; skills as above. Read Tony's Mode 5 results first -- they
decide what is DONE (L-289), what is amended (L-282, L-286), and what
is rebuilt. Then L-286: the rooms page per door, the four-level
drill-down and the short-name breadcrumb, which retires the hamburger
and the shim. The step order in the master plan is unchanged.

---

*Session written September 5, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `9652a43d` and gallery `503fa387`; nothing pushed.
Tony, for the record: "I enjoy speaking with Fable 5.1."*
