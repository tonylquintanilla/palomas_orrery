"""patch_L429_4_records_20261010.py -- records for round 3 of L-429,
with L-428 closed, L-237 and L-216 updated, interactive-exhibit 1.14,
gallery-cache-builder 1.8 and protocol v3.89.

Built on orrery a6678b0f02f588d31c86ef09d9635834272cea12 at
https://github.com/tonylquintanilla/palomas_orrery, with gallery
cb9038ccb7aa9747194b330e49c8a52d70598ce8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written October 10, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    Save this file in the orrery repo's ROOT folder (the folder that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L429_4_records_20261010.py
    Then run orrery_maintenance_run.py: it writes the two skills' read
    plans and manifest rows, and rebuilds the ledger's index. Move this
    script into documentation/, commit and push. Then reinstall
    interactive-exhibit and gallery-cache-builder (each is one file:
    upload its SKILL.md), and replace the Project's instructions with
    PROJECT_INSTRUCTIONS.md (now v3.89).

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- header stamp; L-428 DONE; L-429 round 3;
        L-237 and L-216 one dated line each.
    skills/interactive-exhibit/SKILL.md -- 1.13 -> 1.14.
    skills/gallery-cache-builder/SKILL.md -- 1.7 -> 1.8.
    skills_index.py -- gallery-cache-builder leaves PLAN_NOT_YET.
    documentation/SKILL_HISTORIES.md -- receives interactive-exhibit
        v1.11 and gallery-cache-builder v1.5, word for word.
    PROJECT_INSTRUCTIONS.md -- v3.88 -> v3.89; v3.86 moves down.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md -- receives v3.86.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker.
    documentation/HANDOFF_L429_round3_20261010.md -- created.

SAFETY
    Each file is checked only at the lines this patch edits; every
    anchor must match exactly once, and a moved entry must arrive word
    for word. If any check fails, NOTHING is written. Undo after a run
    is Discard Changes in GitHub Desktop (and delete the new handoff).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
LEDGER = P("LEDGER_CONSOLIDATED.md")
IE = P("skills", "interactive-exhibit", "SKILL.md")
CB = P("skills", "gallery-cache-builder", "SKILL.md")
INDEX = P("skills_index.py")
SKHIST = P("documentation", "SKILL_HISTORIES.md")
PROTO = P("PROJECT_INSTRUCTIONS.md")
PHIST = P("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
PAGE = P("documentation", "WHERE_WE_ARE.md")
HANDOFF = P("documentation", "HANDOFF_L429_round3_20261010.md")

HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record, round 3: Go To in the middle of every room\'s list (L-429), the Artifact 1 test\'s date (L-237), and the OneDrive pause retired (L-216), with interactive-exhibit 1.14, gallery-cache-builder 1.8 and protocol v3.89. Written October 10, 2026. -->\n# Handoff: Go To in the middle, the Artifact 1 date, no OneDrive pause\n\nBuilt on orrery a6678b0f02f588d31c86ef09d9635834272cea12 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L429") and gallery\ncb9038ccb7aa9747194b330e49c8a52d70598ce8 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("L428").\nPinned with `git ls-remote` when the round began. Pushed at: not yet.\nThe next session reads both HEADs and writes them on L-429.\n\n- Type: BUILD (gallery), with a records patch (orrery) that bumps two\n  skills and the protocol.\n- Follows `documentation/HANDOFF_L428_L429_round2_20261010.md`, the\n  same session\'s second round.\n- Skills loaded this session: gallery-pipeline 1.2, safe-file-editing\n  1.13, ledger-and-session-records 1.18, interactive-exhibit 1.12.\n  Each matched its manifest row when loaded.\n- Ledger: L-428 (the lobby\'s way in) closes on Tony\'s look; L-429 (the\n  room button on the row) gains round 3; L-237 (Artifact 1\'s record)\n  and L-216 (the swap under a lock) gain a dated line each.\n\n## Read this first\n\n- *In every room\'s list, GO is now GO TO in the middle of the row; in\n  the Solar System room the room button follows it. Long names wrap\n  instead of being cut.*\n- *The Artifact 1 check passes again: the test reads its date from the\n  served cache.*\n- *The Daily Run no longer stops to pause OneDrive.*\n\n## 1. Where the asks came from\n\nTony\'s copy `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`,\nread 2026-10-10:\n- Round 2 on the phone: the see-through card "correct"; the brighter\n  type "correct"; the room button on the row "correct, and suggestion:\n  move the Go button center and re-label "Go To" and "Enter the ___\n  room" to the right. the idea is that when the visitor opens the row,\n  they have a better idea of what to do, Go To, takes them the orbit\n  and hovertext. if there is a room, it opens the room. in that order";\n  the info-panel line "correct".\n- On the Artifact 1 row: "why are we getting this?"\n- On the Daily Run\'s "Resume OneDrive": "not paused. you can remove the\n  pause check from the daily run. the retry is sufficient."\n- On reinstalling: "note that with only the skill file a zip was not\n  required." A skill that is one file can be uploaded as its SKILL.md;\n  a ZIP is needed only for a skill with a references/ folder.\n\nHis answers in this session, 2026-10-10:\n- Where Go To applies: "all rows in the drawer with a Go button,\n  including the sun"; then "For uniformity rename the Go buttons in all\n  rooms to Go To and center."\n- Shown that this cut most names short on an upright phone in the Sun\n  and Earth rooms, and offered wrapping: "Confirmed as recommended."\n\n## 2. What was built\n\n`patch_L429_3_goto_centre_L237_date_L216_no_pause.py`, gallery root.\nEach file checked against its content at cb9038c.\n\n- `interactive.html`: every room\'s row is a three-column grid -- the\n  left end and the name, then GO TO in the true middle, then (Solar\n  System room) the room button on the right. The left end still ticks\n  from the row\'s edge. A long name wraps onto more lines. A layer the\n  page cannot draw yet keeps the full row for its words. The Solar\n  System room\'s info panel says "Go To".\n- `tools/headless/walk_solar_system_drawer.js`: checks the word and\n  that the room button follows Go To.\n- `gallery/assembler/tests/test_artifact1_earth.py`: the scene\'s date\n  is Earth\'s stored "today" in the served cache. The fixed 2026-07-13\n  had fallen before the served window\'s start (2026-07-13 19:49 UTC)\n  with the build of 2026-10-09.\n- `daily_run.py`: no pause stop and no "Resume OneDrive". The cache\n  build follows the guest book at once. The old prompt\'s "s to skip"\n  went with it; the dashboard\'s separate buttons cover a day without a\n  build.\n- `tools/exhibit_store_editor.py`: its save message no longer says to\n  pause OneDrive; `tools/test_exhibit_store_editor.py` now requires\n  that.\n\n## 3. Verification\n\nOn a throwaway copy of the gallery at cb9038c with the patch applied.\n\n- Real renders (Playwright, Plotly 2.35.2, the rooms\' real drivers in\n  CPython for Pyodide), all three rooms at 390 x 844, 844 x 390 and\n  1280 x 800: Go To exactly centred on every row (0 px off), no name\n  cut on any of the nine views, no page error.\n- A real tap 6 px from the row\'s left edge ticked Jupiter; a tap on its\n  name selected it and left it ticked.\n- The drawer walk: PASS, 68 checks. The drawer smoke: PASS. The store\n  editor suite: all 305 pass. `daily_run.py --check`: all 3 steps found.\n- `documentation/pin_artifact1_known_failure.py`: "ALL CHECKS PASSED --\n  5 verdicts and T3\'s feature set match the 2026-08-31 pin".\n- The gallery maintenance run: the same verdicts as the base except\n  Artifact 1 assembler, FAIL before, PASS after. Pole of date fails in\n  this sandbox both ways, for want of pyerfa; on Tony\'s machine it\n  passes.\n- Not seen: the phone itself.\n\n## 4. The records patch\n\n`patch_L429_4_records_20261010.py`, orrery root.\n\n- `LEDGER_CONSOLIDATED.md`: a header stamp; L-428 closes (DONE) on\n  Tony\'s look; L-429 gains round 3; L-237 gains the date fix and the\n  failure\'s cause (the round-1 note meant for it never landed: Tony\'s\n  run of patch_L428_2 shows no L-237 line, so the copy he ran was the\n  one before that note was added); L-216 gains the pause\'s retirement.\n- `skills/interactive-exhibit/SKILL.md` 1.13 -> 1.14: Go To\'s word and\n  place, the room button after it, names that wrap; the v1.11 entry\n  moves out. A second version in one session, against One Session,\n  One Bump, because 1.13 was already installed when the ruling came.\n- `skills/gallery-cache-builder/SKILL.md` 1.7 -> 1.8: the routine\'s\n  pause step is retired; its read plan\'s seed line; the v1.5 entry\n  moves out. `skills_index.py`: it leaves PLAN_NOT_YET.\n- `PROJECT_INSTRUCTIONS.md` v3.88 -> v3.89; v3.86 moves to the history.\n- `documentation/WHERE_WE_ARE.md`, by section.\n- This file.\n\n## 5. Tony\'s steps\n\n1. **(do)** Gallery: run\n   `patch_L429_3_goto_centre_L237_date_L216_no_pause.py` (25 "ok"\n   lines, "patch applied"), then `gallery_maintenance_run.py` -- every\n   gating row should pass, Artifact 1 included -- commit and push, and\n   move the script into `documentation/`.\n2. **(do)** Look on the phone, with the Home Screen clip\'s tab closed\n   first: the three rooms\' lists.\n3. **(do)** Orrery: run `patch_L429_4_records_20261010.py`, then\n   `orrery_maintenance_run.py`; move the script into `documentation/`;\n   commit and push.\n4. **(do)** Reinstall interactive-exhibit (upload its SKILL.md) and\n   gallery-cache-builder (its SKILL.md); replace the Project\'s\n   instructions with `PROJECT_INSTRUCTIONS.md` (v3.89).\n5. **(decide, after the look)** Whether L-429 closes.\n\n## 6. What travels\n\n- interactive-exhibit went to 1.14 and gallery-cache-builder to 1.8 in\n  a session that loaded 1.12 and none. The next session confirms its\n  loaded copies read 1.14 and 1.8 before exhibit or cache-builder work.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

# ---------------------------------------------------------------- ledger

L = []

L.append(("LEDGER                 L-216 line", (
b"""**Gap:** none. CLOSED 2026-10-08 in the decisions session of
2026-10-08, on the evidence below (the retry proven twice,""",
b"""- **2026-10-10, the OneDrive pause retired**, on Tony's word in his
  run record (`documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`):
  "not paused. you can remove the pause check from the daily run. the
  retry is sufficient." Gallery
  `patch_L429_3_goto_centre_L237_date_L216_no_pause.py` takes the stop
  out of `daily_run.py` and the pause line out of the store editor's
  save message; gallery-cache-builder 1.8 retires the routine's step 1.
**Gap:** none. CLOSED 2026-10-08 in the decisions session of
2026-10-08, on the evidence below (the retry proven twice,""")))

L.append(("LEDGER                 L-237 line", (
b"""**Gap:** re-cut it, with the planetocentric test above. Pair with the
""",
b"""- **2026-10-09/10, red on every run, then the date fixed.** Tony's
  gallery maintenance runs of 2026-10-09 and 2026-10-10: "1 of 24
  gating checkers FAILED -- Artifact 1 assembler", T1 OK and T2 to T5
  not printed. Tony: "why are we getting this?" The test's scene date,
  fixed at 2026-07-13 00:00 UTC, fell before the served window's start
  (2026-07-13 19:49 UTC) with the cache build of 2026-10-09, so T2
  raised OutOfServedWindowError. Built 2026-10-10 in gallery
  `patch_L429_3_goto_centre_L237_date_L216_no_pause.py`: the date is
  Earth's stored "today" in the served cache. On a copy the pin reads
  "ALL CHECKS PASSED -- 5 verdicts and T3's feature set match the
  2026-08-31 pin". The re-cut below is still owed; T3 is still the
  known failure. (A note meant for this item on 2026-10-09 never
  landed: the copy of patch_L428_2 Tony ran predates it.)
**Gap:** re-cut it, with the planetocentric test above. Pair with the
""")))

L.append(("LEDGER                 L-237 date", (
b"""<!-- L:237 status:OPEN upd:2026-10-08 section:A flag: rice: -->""",
b"""<!-- L:237 status:OPEN upd:2026-10-10 section:A flag: rice: -->""")))

L.append(("LEDGER                 L-429 round 3", (
b"""**Gap:** Tony's look on the phone. Then this item closes. The next
session confirms its loaded interactive-exhibit reads 1.13.
""",
b"""- **Round 2 looked at, 2026-10-10**, from Tony's copy
  `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`: the button on
  the row "correct, and suggestion: move the Go button center and
  re-label "Go To" and "Enter the ___ room" to the right ... Go To,
  takes them the orbit and hovertext. if there is a room, it opens the
  room. in that order"; the info-panel line "correct". Gallery pushed
  at e327df3, 96d9816 and cb9038c; orrery at a6678b0.
- **Rulings 2026-10-10:** "For uniformity rename the Go buttons in all
  rooms to Go To and center." Shown that a middle Go To cut 17 of 19
  names in the Sun room and 20 of 21 in Earth's on an upright phone,
  and offered wrapping: "Confirmed as recommended."
- **Round 3 built 2026-10-10, NOT yet run** [render-gated]: gallery
  `patch_L429_3_goto_centre_L237_date_L216_no_pause.py`, on cb9038c.
  Every room's row is a three-column grid: the left end and the name,
  GO TO in the true middle, then the room button (Solar System room).
  Names wrap. Verified in real renders of all three rooms at three
  sizes: Go To 0 px off centre, no name cut, a tap at the left edge
  ticks. interactive-exhibit 1.14 records it.
**Gap:** Tony's look on the phone. Then this item closes. The next
session confirms its loaded interactive-exhibit reads 1.14 and
gallery-cache-builder 1.8.
""")))

L.append(("LEDGER                 L-428 closed", (
b"""**Gap:** Tony's look on the phone after round 2. Then this item closes.
""",
b"""- **Closed 2026-10-10** on Tony's look at round 2, from his copy
  `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`: the
  see-through card "correct", the brighter type "correct"; both lobby
  patches moved into the gallery's documentation/ ("done"). No loose
  ends: the round-1 notes went to L-237, L-282, L-363, L-367 and L-414.
**Gap:** none. DONE 2026-10-10.
""")))

L.append(("LEDGER                 L-428 status", (
b"""<!-- L:428 status:OPEN upd:2026-10-10 section:A flag: rice: -->""",
b"""<!-- L:428 status:DONE upd:2026-10-10 section:A flag: rice: -->""")))

L.append(("LEDGER                 header stamp", (
b"""
Review and RICE update Tony 6-21-2026
""",
b"""
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-429 round 3: Go To in the middle of every room's list; L-428
closed; L-237 the Artifact 1 date; L-216 the OneDrive pause retired;
interactive-exhibit 1.14, gallery-cache-builder 1.8, protocol v3.89),
built on a6678b0f.
Review and RICE update Tony 6-21-2026
""")))

# ----------------------------------------------------- interactive-exhibit

OLD_111 = b"""Earlier: 1.11 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 72e3b558. v1.11 (L-418) changes no rule. A contents
list now opens the skill, generated from its headings, and
skills_index.py --check fails if the two disagree. Version history
older than the two entries below moved to
documentation/SKILL_HISTORIES.md. Both because a plain read of a
long file shows its start and end and leaves out its middle, where
the rules are (Tony, 2026-10-05).
"""

IEE = []

IEE.append(("interactive-exhibit    install note", (
b"""that loaded 1.12; the next session confirms its loaded copy reads 1.13
before exhibit work.""",
b"""that loaded 1.12; the next session confirms its loaded copy reads 1.13
before exhibit work. 1.14 followed in the same session, after 1.13 was
installed; the next session confirms its loaded copy reads 1.14.""")))

IEE.append(("interactive-exhibit    drawer bullet", (
b"""  in `EXHIBITS` shows "Enter the <name> room" on its OWN row, before
  GO, always and on every screen, so one tap enters the room (L-429;
  Tony, 2026-10-10: "so the visitor does not need to tap the row to see
  the button then tap again"). The Sun's row keeps GO's space, hidden,
  so its button lines up.""",
b"""  in `EXHIBITS` shows "Enter the <name> room" on its OWN row, to the
  right of Go To, always and on every screen, so one tap enters the
  room (L-429; Tony, 2026-10-10: "so the visitor does not need to tap
  the row to see the button then tap again"; and "Go To, takes them
  the orbit and hovertext. if there is a room, it opens the room. in
  that order"). The Sun's row keeps Go To's space, hidden, so its
  button lines up.""")))

IEE.append(("interactive-exhibit    anatomy row", (
b"""(L-318 round 3, amending L-267's G2 in that one case; GO still never hides anything).""",
b"""(L-318 round 3, amending L-267's G2 in that one case; GO still never hides anything). Since L-429 (Tony, 2026-10-10: "For uniformity rename the Go buttons in all rooms to Go To and center") the button reads GO TO and sits in the true middle of every room's row: the row is a three-column grid, the left end and the name in the first, Go To in the second, the room button (Solar System room) in the third; a long name wraps onto more lines rather than being cut.""")))

IEE.append(("interactive-exhibit    v1.11 entry moved out", (OLD_111, b"")))

IEE.append(("interactive-exhibit    version line 1.14", (
b"""Skill version: 1.13 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 04d17331 and gallery @ 2aab10fd. v1.13 (L-429)""",
b"""Skill version: 1.14 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a6678b0f and gallery @ cb9038cc. v1.14 (L-429) records
Tony's rulings of the same day, after 1.13 was installed: every room's
row puts GO TO in its true middle, the Solar System room's room button
to its right, and a long name wraps rather than being cut. A second
version in one session, against One Session, One Bump, because the
ruling came after 1.13 was in use.
Earlier: 1.13 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 04d17331 and gallery @ 2aab10fd. v1.13 (L-429)""")))

# ---------------------------------------------------- gallery-cache-builder

OLD_15 = b"""v1.5 adds the rule the project did not have written down anywhere until
a config change reached the live site ahead of the cache and broke both
exhibit rooms: A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS
REBUILT (L-336). It also corrects this skill's own claim that the failed
`staging -> live` rename was "one data point" -- there have been three,
the third on 2026-09-17 -- and writes down the hand routine Tony
actually uses now.
"""

CBE = []

CBE.append(("gallery-cache-builder  note-the-time sentence", (
b"""second run reached its swap. That is why step 1 of the routine above says
to note the time.""",
b"""second run reached its swap. That is why step 1 of the routine above said
to note the time, until the pause was retired on 2026-10-10.""")))

CBE.append(("gallery-cache-builder  routine step 1", (
b"""  1. Pause OneDrive syncing, and NOTE THE TIME. A pause lasts 2 hours.
""",
b"""  1. RETIRED 2026-10-10: no OneDrive pause. Tony: "the retry is
     sufficient." The builder retries a refused rename and the swap log
     records it; the Daily Run no longer asks (L-216).
""")))

CBE.append(("gallery-cache-builder  v1.5 entry moved out", (OLD_15, b"")))

CBE.append(("gallery-cache-builder  version line 1.8", (
b"""# Gallery Cache Builder (Phase 1b data serving)

Skill version: 1.7 | 2026-10-05, with Anthropic's Claude Opus 5.5, at""",
b"""# Gallery Cache Builder (Phase 1b data serving)

Read this file in parts.

Skill version: 1.8 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a6678b0f and gallery @ cb9038cc. v1.8 (L-216) retires
the hand routine's OneDrive pause, on Tony's word of 2026-10-10: "you
can remove the pause check from the daily run. the retry is
sufficient." A session following the old step would have told him to
pause. The skill also gets its read plan, at its next version as Tony
ruled on 2026-10-08 (L-418).
Earlier: 1.7 | 2026-10-05, with Anthropic's Claude Opus 5.5, at""")))

I_EDITS = [("skills_index.py        PLAN_NOT_YET", (
b"""    'gallery-cache-builder',
    # interactive-exhibit left on 2026-10-10 with its 1.13 (L-429).""",
b"""    # gallery-cache-builder left on 2026-10-10 with its 1.8 (L-216).
    # interactive-exhibit left on 2026-10-10 with its 1.13 (L-429)."""))]

H_EDITS = [
    ("SKILL_HISTORIES.md     interactive-exhibit v1.11 received", (
b"""loaded anywhere (L-406, L-407).

## safe-file-editing
""",
b"""loaded anywhere (L-406, L-407).
""" + OLD_111 + b"""
## safe-file-editing
""")),
]

# -------------------------------------------------------------- protocol

V389 = b"""v3.89 (October 10, 2026): No rule changed in this document. TWO
skills, one version each: interactive-exhibit 1.13 -> 1.14 (L-429) and
gallery-cache-builder 1.7 -> 1.8 (L-216). GO TO IN THE MIDDLE OF EVERY
ROW, AND NO ONEDRIVE PAUSE.

WHAT PROMPTED IT. Tony, after a look on the phone, 2026-10-10: "For
uniformity rename the Go buttons in all rooms to Go To and center",
with the room button to its right; shown that this cut most layer
names on an upright phone, he confirmed letting them wrap. And on the
Daily Run: "you can remove the pause check from the daily run. the
retry is sufficient." Gallery patch_L429_3 builds both, with the
Artifact 1 test's date (L-237).

WHAT CHANGED. interactive-exhibit, in the drawer's anatomy row and the
Solar System room's drawer: the three-column row, Go To in the true
middle, the room button after it, names that wrap. A second version in
one session, against One Session, One Bump, because 1.13 was installed
before the ruling came. gallery-cache-builder: the routine's pause step
is retired, and the skill gets its read plan and leaves PLAN_NOT_YET.
Their v1.11 and v1.5 entries moved to documentation/SKILL_HISTORIES.md,
by the three-entry rule.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copies read
interactive-exhibit 1.14 and gallery-cache-builder 1.8 before exhibit
or cache-builder work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.86 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V386_START = b"v3.86 (October 8, 2026): No rule changed in this document. THREE\n"
V386_END = b"""Version history: v3.83 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""
PROTO_TAIL = b"Functional for Claude, readable for human, signal preserved."

P_EDITS = [
    ("PROJECT_INSTRUCTIONS   v3.89 entry", (
        b"v3.88 (October 10, 2026): No rule changed in this document. ONE\n",
        V389 + b"v3.88 (October 10, 2026): No rule changed in this document. ONE\n")),
    ("PROJECT_INSTRUCTIONS   header and anchor", (
        b"""Tony Quintanilla, PE | Claude | v3.88 | October 10, 2026

Cut from 04d17331 at https://github.com/tonylquintanilla/palomas_orrery""",
        b"""Tony Quintanilla, PE | Claude | v3.89 | October 10, 2026

Cut from a6678b0f at https://github.com/tonylquintanilla/palomas_orrery""")),
]

# ---------------------------------------------------------- Where We Are

W = []

W.append(("WHERE_WE_ARE           where the details are", (
b"""- The lobby, the room button: L-428, L-429; `HANDOFF_L428_L429_round2_20261010.md`
""",
b"""- The lobby, the room button: L-428, L-429; `HANDOFF_L429_round3_20261010.md`
""")))

W.append(("WHERE_WE_ARE           signals", (
b"""- Last cache build: 20261009T190335Z, ok, no retry.
- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  04d1733. Whole tree: 293.""",
b"""- Last cache build: 20261010T135737Z, ok, no retry.
- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  a6678b0. Whole tree: 293.""")))

W.append(("WHERE_WE_ARE           settled", (
b"""- OneDrive: you are trying builds without the pause; the retry absorbs
  the lock, and the swap log shows any retry. Empty "solar-system (N)"
  folders are harmless; delete by hand. (Oct 8)""",
b"""- OneDrive: no pause before a build; the retry is sufficient, and the
  swap log shows any retry. Empty "solar-system (N)" folders are
  harmless; delete by hand. (Oct 8, Oct 10)""")))

W.append(("WHERE_WE_ARE           settled: the lists", (
b"""- The lobby opens on the Solar System room, then the subjects. In
  that room's list a room's button sits on its row. (Oct 9, Oct 10)""",
b"""- The lobby opens on the Solar System room, then the subjects. Every
  room's list: Go To in the middle, then the room's button. (Oct 10)""")))

W.append(("WHERE_WE_ARE           needs you now", (
b"""> - *Gallery: run patch_L428_3_L429_1, the maintenance run, push; look
>   on the phone. Orrery: run patch_L429_2, the maintenance run, push.*
> - Reinstall interactive-exhibit (1.13), and provenance-discipline
>   (2.28) if not done yet; the Project's instructions to v3.88.""",
b"""> - *Gallery: run patch_L429_3, the maintenance run, push; look on the
>   phone. Orrery: run patch_L429_4, the maintenance run, push.*
> - Upload interactive-exhibit (1.14) and gallery-cache-builder (1.8);
>   the Project's instructions to v3.89.""")))

W.append(("WHERE_WE_ARE           changed since", (
b"""> - L-428 (the lobby's way in) is live. Your two asks are built: the
>   start card is see-through, and the grey type is brighter.
> - L-429 (the room button on the row): the Sun and Earth show "Enter
>   the ... room" on their own row in the Solar System room's list.""",
b"""> - L-429 (the room button on the row): Go To sits in the middle of
>   every room's list, the room button after it; long names wrap.
> - Artifact 1 passes again; the Daily Run no longer pauses OneDrive.
>   L-428 (the lobby's way in) is closed.""")))

W.append(("WHERE_WE_ARE           date line", (
b"""Last updated: October 10, 2026, at the lobby's second round.
- Written at orrery 04d1733 and gallery 2aab10f, before your runs.""",
b"""Last updated: October 10, 2026, at the lobby's third round.
- Written at orrery a6678b0 and gallery cb9038c, before your runs.""")))

MARKER = b"--- Your run record below this line"


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def read_lf(path):
    if not os.path.isfile(path):
        fail("%s not found. Save this script in the orrery repo root." % path)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n"), (b"\r\n" in raw)


def apply(text, edits):
    for name, (old, new) in edits:
        n = text.count(old)
        if n != 1:
            fail("ANCHOR FAIL, %s: expected 1 match, found %d. Has that "
                 "part changed since a6678b0?" % (name, n))
        text = text.replace(old, new)
        print("ok  " + name)
    return text


def main():
    files = {}
    for path in (LEDGER, IE, CB, INDEX, SKHIST, PROTO, PHIST, PAGE):
        files[path] = read_lf(path)

    if b"<!-- L:428 status:DONE" in files[LEDGER][0]:
        print("already applied: L-428 is already closed. Nothing written.")
        return
    if os.path.exists(HANDOFF):
        fail("documentation/HANDOFF_L429_round3_20261010.md already exists.")

    out = {}
    out[LEDGER] = apply(files[LEDGER][0], L)
    out[IE] = apply(files[IE][0], IEE)
    out[CB] = apply(files[CB][0], CBE)
    out[INDEX] = apply(files[INDEX][0], I_EDITS)

    hist = apply(files[SKHIST][0], H_EDITS)
    if not hist.endswith(b"\n"):
        hist += b"\n"
    hist += OLD_15
    if hist.count(OLD_111) != 1 or hist.count(OLD_15) != 1:
        fail("SKILL_HISTORIES.md: a moved entry did not arrive word for word.")
    print("ok  SKILL_HISTORIES.md     gallery-cache-builder v1.5 received")
    out[SKHIST] = hist

    proto = apply(files[PROTO][0], P_EDITS)
    a = proto.find(V386_START)
    if a < 0 or proto.count(V386_START) != 1:
        fail("PROJECT_INSTRUCTIONS.md: the v3.86 entry was not found once.")
    b = proto.find(V386_END, a)
    if b < 0 or not proto[b + len(V386_END):].startswith(PROTO_TAIL):
        fail("PROJECT_INSTRUCTIONS.md: the v3.86 entry does not end where expected.")
    entry = proto[a:b + len(V386_END)]
    proto = proto[:a] + proto[b + len(V386_END):]
    print("ok  PROJECT_INSTRUCTIONS   v3.86 moved out (%d lines)" % entry.count(b"\n"))
    out[PROTO] = proto

    ph = files[PHIST][0]
    part2 = b"\n================================================================\nPART 2 -- LESSONS REMOVED"
    if ph.count(part2) != 1:
        fail("PROJECT_INSTRUCTIONS_HISTORY.md: the PART 2 banner was not found once.")
    ph = ph.replace(part2, b"\n" + entry +
                    b"(Moved down from the resident protocol on 2026-10-10 when\n"
                    b"v3.89 made a fourth entry.)\n" + part2)
    if ph.count(entry) != 1:
        fail("PROJECT_INSTRUCTIONS_HISTORY.md: v3.86 did not arrive word for word.")
    print("ok  PROJECT_INSTRUCTIONS_HISTORY.md  v3.86 received")
    out[PHIST] = ph

    page = files[PAGE][0]
    if page.count(MARKER) != 1:
        fail("WHERE_WE_ARE.md: the run-record marker line was not found once.")
    below = page[page.index(MARKER):]
    page = apply(page, W)
    if page[page.index(MARKER):] != below:
        fail("WHERE_WE_ARE.md: an edit reached below the run-record marker.")
    out[PAGE] = page

    handoff = HANDOFF_TEXT.encode("ascii")
    for path, data in list(out.items()) + [(HANDOFF, handoff)]:
        bad = sum(1 for ch in data if ch > 127)
        if bad:
            fail("%s would hold %d non-ASCII byte(s)." % (os.path.basename(path), bad))

    for path, data in out.items():
        open(path, "wb").write(data)
        if files[path][1]:
            print("note: %s was CRLF in the working copy; written LF"
                  % os.path.relpath(path, ROOT))
    open(HANDOFF, "wb").write(handoff)
    print("ok  documentation/HANDOFF_L429_round3_20261010.md created")
    above = page[:page.index(MARKER)].count(b"\n")
    print("note: WHERE_WE_ARE.md has %d lines above the run-record marker "
          "(the cap is 130)" % above)
    print("stamps updated: LEDGER_CONSOLIDATED.md header; both skills' version "
          "lines; PROJECT_INSTRUCTIONS.md header and anchor; WHERE_WE_ARE.md date line")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py -- it writes both skills' read plans")
    print("     and manifest rows, and rebuilds the ledger's index.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Upload interactive-exhibit's and gallery-cache-builder's SKILL.md")
    print("     (Settings > Skills), and replace the Project's instructions with")
    print("     PROJECT_INSTRUCTIONS.md (v3.89).")


if __name__ == "__main__":
    main()
