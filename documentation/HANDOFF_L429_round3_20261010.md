<!-- Doc-Kind: hand | Session record, round 3: Go To in the middle of every room's list (L-429), the Artifact 1 test's date (L-237), and the OneDrive pause retired (L-216), with interactive-exhibit 1.14, gallery-cache-builder 1.8 and protocol v3.89. Written October 10, 2026. -->
# Handoff: Go To in the middle, the Artifact 1 date, no OneDrive pause

Built on orrery a6678b0f02f588d31c86ef09d9635834272cea12 at
https://github.com/tonylquintanilla/palomas_orrery ("L429") and gallery
cb9038ccb7aa9747194b330e49c8a52d70598ce8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("L428").
Pinned with `git ls-remote` when the round began. Pushed at: not yet.
The next session reads both HEADs and writes them on L-429.

- Type: BUILD (gallery), with a records patch (orrery) that bumps two
  skills and the protocol.
- Follows `documentation/HANDOFF_L428_L429_round2_20261010.md`, the
  same session's second round.
- Skills loaded this session: gallery-pipeline 1.2, safe-file-editing
  1.13, ledger-and-session-records 1.18, interactive-exhibit 1.12.
  Each matched its manifest row when loaded.
- Ledger: L-428 (the lobby's way in) closes on Tony's look; L-429 (the
  room button on the row) gains round 3; L-237 (Artifact 1's record)
  and L-216 (the swap under a lock) gain a dated line each.

## Read this first

- *In every room's list, GO is now GO TO in the middle of the row; in
  the Solar System room the room button follows it. Long names wrap
  instead of being cut.*
- *The Artifact 1 check passes again: the test reads its date from the
  served cache.*
- *The Daily Run no longer stops to pause OneDrive.*

## 1. Where the asks came from

Tony's copy `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`,
read 2026-10-10:
- Round 2 on the phone: the see-through card "correct"; the brighter
  type "correct"; the room button on the row "correct, and suggestion:
  move the Go button center and re-label "Go To" and "Enter the ___
  room" to the right. the idea is that when the visitor opens the row,
  they have a better idea of what to do, Go To, takes them the orbit
  and hovertext. if there is a room, it opens the room. in that order";
  the info-panel line "correct".
- On the Artifact 1 row: "why are we getting this?"
- On the Daily Run's "Resume OneDrive": "not paused. you can remove the
  pause check from the daily run. the retry is sufficient."
- On reinstalling: "note that with only the skill file a zip was not
  required." A skill that is one file can be uploaded as its SKILL.md;
  a ZIP is needed only for a skill with a references/ folder.

His answers in this session, 2026-10-10:
- Where Go To applies: "all rows in the drawer with a Go button,
  including the sun"; then "For uniformity rename the Go buttons in all
  rooms to Go To and center."
- Shown that this cut most names short on an upright phone in the Sun
  and Earth rooms, and offered wrapping: "Confirmed as recommended."

## 2. What was built

`patch_L429_3_goto_centre_L237_date_L216_no_pause.py`, gallery root.
Each file checked against its content at cb9038c.

- `interactive.html`: every room's row is a three-column grid -- the
  left end and the name, then GO TO in the true middle, then (Solar
  System room) the room button on the right. The left end still ticks
  from the row's edge. A long name wraps onto more lines. A layer the
  page cannot draw yet keeps the full row for its words. The Solar
  System room's info panel says "Go To".
- `tools/headless/walk_solar_system_drawer.js`: checks the word and
  that the room button follows Go To.
- `gallery/assembler/tests/test_artifact1_earth.py`: the scene's date
  is Earth's stored "today" in the served cache. The fixed 2026-07-13
  had fallen before the served window's start (2026-07-13 19:49 UTC)
  with the build of 2026-10-09.
- `daily_run.py`: no pause stop and no "Resume OneDrive". The cache
  build follows the guest book at once. The old prompt's "s to skip"
  went with it; the dashboard's separate buttons cover a day without a
  build.
- `tools/exhibit_store_editor.py`: its save message no longer says to
  pause OneDrive; `tools/test_exhibit_store_editor.py` now requires
  that.

## 3. Verification

On a throwaway copy of the gallery at cb9038c with the patch applied.

- Real renders (Playwright, Plotly 2.35.2, the rooms' real drivers in
  CPython for Pyodide), all three rooms at 390 x 844, 844 x 390 and
  1280 x 800: Go To exactly centred on every row (0 px off), no name
  cut on any of the nine views, no page error.
- A real tap 6 px from the row's left edge ticked Jupiter; a tap on its
  name selected it and left it ticked.
- The drawer walk: PASS, 68 checks. The drawer smoke: PASS. The store
  editor suite: all 305 pass. `daily_run.py --check`: all 3 steps found.
- `documentation/pin_artifact1_known_failure.py`: "ALL CHECKS PASSED --
  5 verdicts and T3's feature set match the 2026-08-31 pin".
- The gallery maintenance run: the same verdicts as the base except
  Artifact 1 assembler, FAIL before, PASS after. Pole of date fails in
  this sandbox both ways, for want of pyerfa; on Tony's machine it
  passes.
- Not seen: the phone itself.

## 4. The records patch

`patch_L429_4_records_20261010.py`, orrery root.

- `LEDGER_CONSOLIDATED.md`: a header stamp; L-428 closes (DONE) on
  Tony's look; L-429 gains round 3; L-237 gains the date fix and the
  failure's cause (the round-1 note meant for it never landed: Tony's
  run of patch_L428_2 shows no L-237 line, so the copy he ran was the
  one before that note was added); L-216 gains the pause's retirement.
- `skills/interactive-exhibit/SKILL.md` 1.13 -> 1.14: Go To's word and
  place, the room button after it, names that wrap; the v1.11 entry
  moves out. A second version in one session, against One Session,
  One Bump, because 1.13 was already installed when the ruling came.
- `skills/gallery-cache-builder/SKILL.md` 1.7 -> 1.8: the routine's
  pause step is retired; its read plan's seed line; the v1.5 entry
  moves out. `skills_index.py`: it leaves PLAN_NOT_YET.
- `PROJECT_INSTRUCTIONS.md` v3.88 -> v3.89; v3.86 moves to the history.
- `documentation/WHERE_WE_ARE.md`, by section.
- This file.

## 5. Tony's steps

1. **(do)** Gallery: run
   `patch_L429_3_goto_centre_L237_date_L216_no_pause.py` (25 "ok"
   lines, "patch applied"), then `gallery_maintenance_run.py` -- every
   gating row should pass, Artifact 1 included -- commit and push, and
   move the script into `documentation/`.
2. **(do)** Look on the phone, with the Home Screen clip's tab closed
   first: the three rooms' lists.
3. **(do)** Orrery: run `patch_L429_4_records_20261010.py`, then
   `orrery_maintenance_run.py`; move the script into `documentation/`;
   commit and push.
4. **(do)** Reinstall interactive-exhibit (upload its SKILL.md) and
   gallery-cache-builder (its SKILL.md); replace the Project's
   instructions with `PROJECT_INSTRUCTIONS.md` (v3.89).
5. **(decide, after the look)** Whether L-429 closes.

## 6. What travels

- interactive-exhibit went to 1.14 and gallery-cache-builder to 1.8 in
  a session that loaded 1.12 and none. The next session confirms its
  loaded copies read 1.14 and 1.8 before exhibit or cache-builder work.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
