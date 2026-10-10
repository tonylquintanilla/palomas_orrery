"""patch_L429_2_records_20261010.py -- records for L-428 round 2 and L-429.

Built on orrery 04d17331203e07dfdc2e1be303bbbf9f82bfc667 at
https://github.com/tonylquintanilla/palomas_orrery, with gallery
2aab10fdead213ade0cc9c8bdbfe1a6bc03c30b5 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written October 10, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    Save this file in the orrery repo's ROOT folder (the folder that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L429_2_records_20261010.py
    Then run orrery_maintenance_run.py: its Skill manifest step writes
    interactive-exhibit's read plan and its manifest row, and it
    rebuilds the ledger's index. Move this script into documentation/,
    commit and push. Then reinstall interactive-exhibit from a ZIP of
    skills/interactive-exhibit, and replace the Project's instructions
    with PROJECT_INSTRUCTIONS.md (now v3.88).

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- a header stamp; L-428 (the lobby's way
        in) gains round 2, quoting Tony's verdicts from his copy;
        L-429 (the room button on the row) opened; one line on L-363.
    skills/interactive-exhibit/SKILL.md -- 1.12 -> 1.13: the Solar
        System room's drawer bullet says what is now built; the read
        plan's seed line; the v1.10 entry moves out; the install note.
    skills_index.py -- interactive-exhibit leaves PLAN_NOT_YET.
    documentation/SKILL_HISTORIES.md -- receives the v1.10 entry.
    PROJECT_INSTRUCTIONS.md -- v3.87 -> v3.88: header and anchor; the
        v3.88 entry; v3.85 moves to the history file.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md -- receives v3.85.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker.
    documentation/HANDOFF_L428_L429_round2_20261010.md -- created.

SAFETY
    Each file is checked only at the lines this patch edits. Every
    anchor must match exactly once, and a moved entry must arrive word
    for word. If any check fails, NOTHING is written. Undo after a run
    is Discard Changes in GitHub Desktop (and delete the new handoff).
    Success prints one "ok" line per edit and "patch applied".
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
LEDGER = P("LEDGER_CONSOLIDATED.md")
SKILL = P("skills", "interactive-exhibit", "SKILL.md")
INDEX = P("skills_index.py")
SKHIST = P("documentation", "SKILL_HISTORIES.md")
PROTO = P("PROJECT_INSTRUCTIONS.md")
PHIST = P("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
PAGE = P("documentation", "WHERE_WE_ARE.md")
HANDOFF = P("documentation", "HANDOFF_L428_L429_round2_20261010.md")

HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record, round 2: the lobby\'s contrast and see-through card (L-428), and the room button on the Solar System room\'s row (L-429), with interactive-exhibit 1.13 and protocol v3.88. Written October 10, 2026. -->\n# Handoff: the lobby, round 2, and the room button on the row\n\nBuilt on orrery 04d17331203e07dfdc2e1be303bbbf9f82bfc667 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("Update\nWHERE_WE_ARE_10-9-26_2307_run_record.md") and gallery\n2aab10fdead213ade0cc9c8bdbfe1a6bc03c30b5 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("L428_1\nlobby option E"). Pinned with `git ls-remote` when the round began.\nPushed at: not yet. The next session reads both HEADs and writes them\non L-428 and L-429.\n\n- Type: BUILD (gallery), with a records patch (orrery) that also bumps\n  one skill and the protocol.\n- Supersedes: nothing. Follows `documentation/HANDOFF_lobby_option_E_20261009.md`,\n  the same session\'s first round.\n- Skills loaded: gallery-pipeline 1.2, safe-file-editing 1.13,\n  ledger-and-session-records 1.18, and for this round\n  interactive-exhibit 1.12. Each matched its manifest row.\n- Ledger: L-428 (the lobby\'s way in) gains round 2; L-429 (the room\n  button on the row) opened. L-429 was the next free handle at 04d1733.\n\n## Read this first\n\n- *Three changes on the website, one gallery patch: the start card is\n  see-through, the lobby\'s grey type is brighter, and in the Solar\n  System room\'s list the Sun and Earth show their room button on their\n  own row.*\n- *interactive-exhibit goes to 1.13, because it described the old list.\n  The protocol goes to v3.88 to record it. Reinstall, and replace the\n  Project\'s instructions, after the push.*\n\n## 1. Where the asks came from\n\n- Tony\'s copy `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`,\n  read 2026-10-10. His verdicts on round 1: the card once, the door\n  counts, the door\'s page, and Enter all "correct" or "yes". Two asks:\n  - "could you give this card the same semi-transparent opacity that\n    the other interactive cards have? The doves allude to \'Paloma\'."\n  - "Brighten the grey type to white or blue or another color if you\n    need contrast with the existing white type. grey is too dim." On\n    the heading over the doves: "yes, see my note above."\n- Tony, 2026-10-10 00:08, with a phone screenshot of the Solar System\n  room: "Can we put the \'Enter the ___ room\' button on the same row\n  with the Go button rather than below? So the visitor does not need\n  to tap the row to see the button then tap again to enter the room."\n\n## 2. What was built\n\n`patch_L428_3_L429_1_lobby_contrast_drawer_button.py`, run from the\ngallery root. Each file is checked against its content at 2aab10f.\n\n- `index.html` (L-428)\n  - The start card\'s background is the other lobby cards\'\n    see-through blue, `rgba(9, 20, 38, 0.78)`, in place of a near-solid\n    black. The room\'s picture stays solid: its own background is\n    black, and dimming it would dim the planets.\n  - In the lobby only, the headings are blue (`#9db0ff`), and the grey\n    lines are near white (`#d6d4d0`): the welcome line, the doors\'\n    sentences, counts and arrows, the card labels, the count line, the\n    guest book\'s dates and note, the footer. Each carries the guest\n    book\'s soft dark shadow. A door\'s own page keeps its colours; it\n    has no dove wall.\n- `interactive.html` (L-429)\n  - In the Solar System room\'s list, a body whose slug is a key in\n    `EXHIBITS` shows "Enter the <name> room" on its own row, before GO,\n    always, on every screen. Today that is the Sun and Earth; the next\n    room lights its row by itself.\n  - A body with no room still opens to "No room or cards yet", under\n    the row upright and on the name\'s line sideways, as before.\n  - The Sun\'s row keeps an empty space where GO would be, so its\n    button lines up with Earth\'s. The hidden GO takes no taps.\n  - The info panel\'s line now reads: "Tap a body\'s name to select it. A\n    body with a room of its own has a button on its row to enter it."\n    It is a sentence about using the page, so it stays typed.\n- `tools/headless/walk_solar_system_drawer.js`: the walk now checks the\n  new behaviour.\n\n## 3. Verification\n\nOn a throwaway copy of the gallery at 2aab10f with the patch applied.\n\n- **The drawer walk** (`tools/headless/walk_solar_system_drawer.js`):\n  PASS, 67 checks. The same walk on the unpatched page fails 7, so it\n  can tell the two apart.\n- **The drawer smoke** (`documentation/smoke_solar_system_drawer.js`):\n  PASS.\n- **A real render**, Playwright with Plotly 2.35.2 from npm and the\n  room\'s real driver run in CPython (`tools/headless/run_room_driver.py`)\n  standing in for Pyodide. Phone 390 x 844: Earth\'s button 191 to 345\n  px, GO 355 to 374; the Sun\'s button 200 to 345, so the two line up;\n  no name cut short; no page error. Sideways 844 x 390 and desktop\n  1280 x 800 the same. One tap on "Enter the Earth room" opened\n  `interactive.html?exhibit=earth`.\n- **The lobby render**: Enter still ends at 573 px on the phone; the\n  headings and grey lines are the new colours.\n- **The gallery maintenance run** (offline): the same verdicts, row\n  for row, on the patched copy and the base. Two rows fail both ways\n  here: Pole of date, for want of pyerfa in this sandbox, and\n  Artifact 1 assembler, the date that left the served window (L-237,\n  recorded in round 1).\n- Not seen: the phone itself. Mode 5 is Tony\'s.\n\n## 4. The records patch\n\n`patch_L429_2_records_20261010.py`, run from the orrery root. Each\nfile is checked only at the lines it edits.\n\n- `LEDGER_CONSOLIDATED.md`: a header stamp; L-428 gains round 2 (his\n  verdicts quoted from his copy; patch_L428_1 left at the gallery\n  root); L-429 opened; one line on L-363.\n- `skills/interactive-exhibit/SKILL.md` 1.12 -> 1.13: the drawer\n  bullet corrected; the read plan\'s seed line; the v1.10 entry moved to\n  `documentation/SKILL_HISTORIES.md`; the install note.\n- `skills_index.py`: interactive-exhibit leaves `PLAN_NOT_YET`, by\n  Tony\'s ruling of 2026-10-08 (a long skill gets its plan at its next\n  version). The maintenance run\'s Skill manifest step writes the plan\n  and the manifest row.\n- `PROJECT_INSTRUCTIONS.md` v3.87 -> v3.88: header and anchor, a\n  v3.88 entry; v3.85 moves to\n  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1.\n- `documentation/WHERE_WE_ARE.md`, by section; nothing below the\n  marker.\n- This file.\n\n## 5. Tony\'s steps\n\n1. **(do)** Gallery: save\n   `patch_L428_3_L429_1_lobby_contrast_drawer_button.py` in the gallery\n   root, press Run (expect 17 "ok" lines and "patch applied"), run\n   `gallery_maintenance_run.py`, commit and push.\n2. **(do)** In the same or the next gallery commit, move\n   `patch_L428_1_lobby_option_e.py` and this patch from the gallery\n   root into the gallery\'s `documentation/` folder.\n3. **(do)** Look on the phone, with the Home Screen clip\'s tab closed\n   first: the lobby (see-through card, brighter type) and the Solar\n   System room\'s list (the Sun\'s and Earth\'s buttons on their rows).\n4. **(do)** Orrery: save `patch_L429_2_records_20261010.py` in the\n   orrery root, press Run, run `orrery_maintenance_run.py` (it writes\n   the skill\'s read plan and the manifest row), move the script into\n   `documentation/`, commit and push.\n5. **(do)** Reinstall interactive-exhibit from a ZIP of\n   `skills/interactive-exhibit`, and replace the Project\'s instructions\n   with `PROJECT_INSTRUCTIONS.md` (v3.88).\n6. **(decide, after the look)** Whether L-428 and L-429 close.\n\n## 6. What travels\n\n- interactive-exhibit went to 1.13 in a session that loaded 1.12. The\n  next session confirms its loaded copy reads 1.13 before any exhibit\n  work.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

# ---------------------------------------------------------------- ledger

L_EDITS = []

L_EDITS.append(("LEDGER_CONSOLIDATED.md      L-363 line", (
b"""- **2026-10-09, the card moves, under L-428 (the lobby's way in):** the
""",
b"""- **2026-10-10, the drawer's room button moves onto its row, under
  L-429 (the room button on the row):** a body with a room shows
  "Enter the ... room" beside GO, always.
- **2026-10-09, the card moves, under L-428 (the lobby's way in):** the
""")))

L_EDITS.append(("LEDGER_CONSOLIDATED.md      L-428 round 2", (
b"""- Tony-action (decide), after the look: close, or change first.
**Gap:** Tony's run and his look on the phone. Then this item closes.
""",
b"""- Tony-action (decide), after the look: close, or change first.
- **Round 1 run and looked at, 2026-10-09**, read from Tony's copy
  `documentation/WHERE_WE_ARE_10-9-26_2307_run_record.md`: gallery
  pushed at 2aab10f; the card drawn once, the door counts, the door's
  page, Enter and the picture all "correct" or "yes". His gallery
  maintenance run: 1 of 24 failed, Artifact 1 assembler, recorded on
  L-237. Two asks: "could you give this card the same semi-transparent
  opacity that the other interactive cards have? The doves allude to
  'Paloma'"; and "Brighten the grey type to white or blue or another
  color if you need contrast with the existing white type. grey is too
  dim", which also answers the heading over the doves ("yes, see my
  note above").
- **Round 2 built 2026-10-10, NOT yet run** [render-gated]: gallery
  `patch_L428_3_L429_1_lobby_contrast_drawer_button.py`, on 2aab10f.
  The start card takes the other lobby cards' see-through blue; the
  picture stays solid. In the lobby only, the headings are blue and the
  grey lines near white, with the guest book's soft shadow. Record:
  `documentation/HANDOFF_L428_L429_round2_20261010.md`.
- Tony-action (do): `patch_L428_1_lobby_option_e.py` was committed at
  the gallery's root; move it, and round 2's patch, into the gallery's
  `documentation/`.
**Gap:** Tony's look on the phone after round 2. Then this item closes.
""")))

L_EDITS.append(("LEDGER_CONSOLIDATED.md      L-428 date", (
b"""<!-- L:428 status:OPEN upd:2026-10-09 section:A flag: rice: -->""",
b"""<!-- L:428 status:OPEN upd:2026-10-10 section:A flag: rice: -->""")))

L_EDITS.append(("LEDGER_CONSOLIDATED.md      L-429 opened", (
b"""#### [L-428] The lobby's way in: the Solar System room first (gallery, lobby)
""",
b"""#### [L-429] The room button on the row, in the Solar System room's list (gallery, exhibits)
<!-- L:429 status:OPEN upd:2026-10-10 section:A flag: rice: -->
- **Asked 2026-10-10, 00:08,** by Tony with a phone screenshot of the
  Solar System room: "Can we put the 'Enter the ___ room' button on the
  same row with the Go button rather than below? So the visitor does
  not need to tap the row to see the button then tap again to enter the
  room."
- **Built 2026-10-10, NOT yet run** [render-gated]: gallery
  `patch_L428_3_L429_1_lobby_contrast_drawer_button.py`, on 2aab10f.
  A body with a room in `EXHIBITS` (today the Sun and Earth) shows
  "Enter the <name> room" on its own row, before GO, always, on every
  screen. A body with none still opens to "No room or cards yet". The
  Sun's row keeps GO's space, hidden, so the two buttons line up. The
  info panel's line: "Tap a body's name to select it. A body with a
  room of its own has a button on its row to enter it." The Claude-only
  walk, `tools/headless/walk_solar_system_drawer.js`, checks it.
- Verified on a throwaway copy: the walk passes 67 checks and fails 7
  on the old page; the drawer smoke passes; a real render at 390 x
  844, 844 x 390 and 1280 x 800 lines the buttons up before GO with no
  name cut; one tap on "Enter the Earth room" opens the Earth room.
- **interactive-exhibit 1.12 -> 1.13**, its drawer bullet corrected,
  by the rule for a wrong sentence in a skill: a session following the
  old one would have told Tony the button shows only on an opened row.
  It gets its read plan at this version, as Tony ruled on 2026-10-08.
  Protocol v3.88 records it.
- Tony-action (do): run the gallery patch, the maintenance run, push;
  look on the phone; reinstall interactive-exhibit; replace the
  Project's instructions with v3.88.
**Gap:** Tony's look on the phone. Then this item closes. The next
session confirms its loaded interactive-exhibit reads 1.13.
**Ref:** L-363 (the Solar System room's drawer, step 3b); L-428 (the
lobby's way in); gallery `interactive.html`;
`documentation/HANDOFF_L428_L429_round2_20261010.md`.

#### [L-428] The lobby's way in: the Solar System room first (gallery, lobby)
""")))

L_EDITS.append(("LEDGER_CONSOLIDATED.md      header stamp", (
b"""
Review and RICE update Tony 6-21-2026
""",
b"""
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-428 round 2, from Tony's run record of 2026-10-09; L-429 opened
and built, the room button on the row; interactive-exhibit 1.13,
protocol v3.88; L-363 updated), built on 04d17331.
Review and RICE update Tony 6-21-2026
""")))

# ----------------------------------------------------------------- skill

OLD_110 = b"""Earlier: 1.10 | 2026-10-02, with Anthropic's Claude Opus 5.5, from
orrery @ 5e42b00b and gallery @ 0ffa4518. v1.10 (L-406) writes down
Tony's rule for a feature's info link, which lived only on L-265: a
NASA page where one is specific to the feature, otherwise English
Wikipedia, with the corona the one named exception. Asked on
2026-10-02, while the galactic tide was being redrawn, whether the
skills covered how a feature's hover, info panel and drawing are
written; the hover and the drawing were covered and the link was not.
The same day Settings refused the first copy ("malformed YAML
frontmatter"): the new fires_when words sat on a line of their own.
They are back on the one line, and the version stays 1.10, which never
loaded anywhere (L-406, L-407).
"""

S_EDITS = []

S_EDITS.append(("interactive-exhibit SKILL   install note", (
b"""session that wrote it, which loaded 1.8; the next session confirms its
loaded copy reads 1.9 before exhibit work.""",
b"""session that wrote it, which loaded 1.8; the next session confirms its
loaded copy reads 1.9 before exhibit work. 1.13 was cut in a session
that loaded 1.12; the next session confirms its loaded copy reads 1.13
before exhibit work.""")))

S_EDITS.append(("interactive-exhibit SKILL   drawer bullet", (
b"""- **A row opens.** Tapping a name highlights the row and opens it; a
  second tap closes it. Ticking a body opens its row too (Tony,
  2026-09-30). An open row links "Enter the <name> room" where the
  row's slug is a key in `EXHIBITS`, and says "No room or cards yet"
  where it is not -- read from the page's own table, so the next room
  lights its row by itself.""",
b"""- **A row opens, and a room is one tap away.** Tapping a name
  highlights the row and opens it; a second tap closes it. Ticking a
  body opens its row too (Tony, 2026-09-30). A body whose slug is a key
  in `EXHIBITS` shows "Enter the <name> room" on its OWN row, before
  GO, always and on every screen, so one tap enters the room (L-429;
  Tony, 2026-10-10: "so the visitor does not need to tap the row to see
  the button then tap again"). The Sun's row keeps GO's space, hidden,
  so its button lines up. A body with no room opens to "No room or
  cards yet": under the row upright, on the name's line with the phone
  sideways (Tony, 2026-10-03). Both are read from the page's own table,
  so the next room lights its row by itself.""")))

S_EDITS.append(("interactive-exhibit SKILL   older-entries line", (
b"""Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 (L-418).""",
b"""Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 (L-418) and 2026-10-10 (L-429).""")))

S_EDITS.append(("interactive-exhibit SKILL   v1.10 entry moved out", (OLD_110, b"")))

S_EDITS.append(("interactive-exhibit SKILL   version line 1.13", (
b"""# Interactive Exhibit

Skill version: 1.12 | 2026-10-06, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 51436054 and gallery @ ed48d078. v1.12 (L-421, L-349)""",
b"""# Interactive Exhibit

Read this file in parts.

Skill version: 1.13 | 2026-10-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 04d17331 and gallery @ 2aab10fd. v1.13 (L-429)
corrects the Solar System room's drawer as built: a body with a room
shows its "Enter the <name> room" button on its own row, before GO,
always, on every screen; a body with none still opens to "No room or
cards yet". Tony, 2026-10-10: "so the visitor does not need to tap the
row to see the button then tap again to enter the room." The skill
also gets its read plan, at its next version as Tony ruled on
2026-10-08 (L-418).
Earlier: 1.12 | 2026-10-06, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 51436054 and gallery @ ed48d078. v1.12 (L-421, L-349)""")))

I_EDITS = [("skills_index.py             PLAN_NOT_YET", (
b"""    'gallery-cache-builder',
    'interactive-exhibit',
    'orrery-coding-conventions',""",
b"""    'gallery-cache-builder',
    # interactive-exhibit left on 2026-10-10 with its 1.13 (L-429).
    'orrery-coding-conventions',"""))]

H_EDITS = [("SKILL_HISTORIES.md          v1.10 entry received", (
b"""Plotly, and the other rooms compared before and after (tools/headless/).

## safe-file-editing
""",
b"""Plotly, and the other rooms compared before and after (tools/headless/).
""" + OLD_110 + b"""
## safe-file-editing
"""))]

# -------------------------------------------------------------- protocol

V388 = b"""v3.88 (October 10, 2026): No rule changed in this document. ONE
skill bump, one version (L-429): interactive-exhibit 1.12 -> 1.13. A
ROOM IS ONE TAP AWAY IN THE SOLAR SYSTEM ROOM'S LIST.

WHAT PROMPTED IT. Tony, on the phone, 2026-10-10: "Can we put the
'Enter the ___ room' button on the same row with the Go button rather
than below? So the visitor does not need to tap the row to see the
button then tap again to enter the room." Gallery patch_L428_3_L429_1
builds it. The skill described the old list, where the button showed
only on an opened row, so a session following it would have told Tony
the wrong thing about the room.

WHAT CHANGED. interactive-exhibit, under The Solar System room's
drawer: a body with a room shows its button on its own row, before GO,
always, on every screen; a body with none still opens to "No room or
cards yet". The skill gets its read plan, at its next version as Tony
ruled on 2026-10-08, and leaves skills_index.py's PLAN_NOT_YET list.
Its v1.10 entry moved to documentation/SKILL_HISTORIES.md, by the
three-entry rule.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
interactive-exhibit 1.13 before any exhibit work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.85 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V385_START = b"v3.85 (October 7, 2026): No rule changed in this document. ONE\n"
V385_END = b"""Version history: v3.82 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""
PROTO_TAIL = b"Functional for Claude, readable for human, signal preserved."

P_EDITS = [
    ("PROJECT_INSTRUCTIONS.md     v3.88 entry", (
        b"v3.87 (October 9, 2026): No rule changed in this document. ONE\n",
        V388 + b"v3.87 (October 9, 2026): No rule changed in this document. ONE\n")),
    ("PROJECT_INSTRUCTIONS.md     header and anchor", (
        b"""Tony Quintanilla, PE | Claude | v3.87 | October 9, 2026

Cut from aa46bb10 at https://github.com/tonylquintanilla/palomas_orrery""",
        b"""Tony Quintanilla, PE | Claude | v3.88 | October 10, 2026

Cut from 04d17331 at https://github.com/tonylquintanilla/palomas_orrery""")),
]

# ---------------------------------------------------------- Where We Are

W_EDITS = []

W_EDITS.append(("WHERE_WE_ARE.md             where the details are", (
b"""- The lobby: L-428 (its way in); `HANDOFF_lobby_option_E_20261009.md`
""",
b"""- The lobby, the room button: L-428, L-429; `HANDOFF_L428_L429_round2_20261010.md`
""")))

W_EDITS.append(("WHERE_WE_ARE.md             signals", (
b"""- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  b6652f9. Whole tree: 293.
- This page's date and the ledger's newest stamp: both Oct 9. Agree.
""",
b"""- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  04d1733. Whole tree: 293.
- This page's date and the ledger's newest stamp: both Oct 10. Agree.
""")))

W_EDITS.append(("WHERE_WE_ARE.md             settled", (
b"""- The lobby opens on the Solar System room, then the subjects. (Oct 9)
""",
b"""- The lobby opens on the Solar System room, then the subjects. In
  that room's list a room's button sits on its row. (Oct 9, Oct 10)
""")))

W_EDITS.append(("WHERE_WE_ARE.md             needs you now", (
b"""> - *Gallery: run patch_L428_1, push, look on the phone (close the
>   Home Screen clip's tab first). Orrery: run patch_L428_2, then the
>   maintenance run, and push.*
> - Reinstall provenance-discipline 2.28, if not done yet.
""",
b"""> - *Gallery: run patch_L428_3_L429_1, the maintenance run, push; look
>   on the phone. Orrery: run patch_L429_2, the maintenance run, push.*
> - Reinstall interactive-exhibit (1.13), and provenance-discipline
>   (2.28) if not done yet; the Project's instructions to v3.88.
""")))

W_EDITS.append(("WHERE_WE_ARE.md             changed since", (
b"""> - L-428 (the lobby's way in) is built: the lobby opens on the Solar
>   System room's picture and one Enter button. Not pushed yet.
> - "Doors" is now "Or explore by subject". The Solar System card left
>   Featured, since it now opens the page.
""",
b"""> - L-428 (the lobby's way in) is live. Your two asks are built: the
>   start card is see-through, and the grey type is brighter.
> - L-429 (the room button on the row): the Sun and Earth show "Enter
>   the ... room" on their own row in the Solar System room's list.
""")))

W_EDITS.append(("WHERE_WE_ARE.md             date line", (
b"""Last updated: October 9, 2026, at the lobby build.
- Written at orrery b6652f9 and gallery 5ec4739, before your runs.
""",
b"""Last updated: October 10, 2026, at the lobby's second round.
- Written at orrery 04d1733 and gallery 2aab10f, before your runs.
""")))

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


def apply(label, text, edits):
    for name, (old, new) in edits:
        n = text.count(old)
        if n != 1:
            fail("ANCHOR FAIL, %s: expected 1 match, found %d. Has that "
                 "part changed since 04d1733?" % (name, n))
        text = text.replace(old, new)
        print("ok  " + name)
    return text


def main():
    files = {}
    for path in (LEDGER, SKILL, INDEX, SKHIST, PROTO, PHIST, PAGE):
        files[path] = read_lf(path)

    if b"#### [L-429]" in files[LEDGER][0]:
        print("already applied: the ledger already holds L-429. Nothing written.")
        return
    if os.path.exists(HANDOFF):
        fail("documentation/HANDOFF_L428_L429_round2_20261010.md already exists.")

    out = {}
    out[LEDGER] = apply("ledger", files[LEDGER][0], L_EDITS)
    out[SKILL] = apply("skill", files[SKILL][0], S_EDITS)
    out[INDEX] = apply("index", files[INDEX][0], I_EDITS)
    out[SKHIST] = apply("skill history", files[SKHIST][0], H_EDITS)

    # The protocol: add v3.88, then move v3.85 down, word for word.
    proto = apply("protocol", files[PROTO][0], P_EDITS)
    a = proto.find(V385_START)
    if a < 0 or proto.count(V385_START) != 1:
        fail("PROJECT_INSTRUCTIONS.md: the v3.85 entry was not found once.")
    b = proto.find(V385_END, a)
    if b < 0 or not proto[b + len(V385_END):].startswith(PROTO_TAIL):
        fail("PROJECT_INSTRUCTIONS.md: the v3.85 entry does not end where expected.")
    entry = proto[a:b + len(V385_END)]
    proto = proto[:a] + proto[b + len(V385_END):]
    print("ok  PROJECT_INSTRUCTIONS.md     v3.85 moved out (%d lines)" % entry.count(b"\n"))
    if proto.count(b"\nv3.8") != 3:
        fail("PROJECT_INSTRUCTIONS.md: expected three resident entries, found %d."
             % proto.count(b"\nv3.8"))
    out[PROTO] = proto

    hist = files[PHIST][0]
    part2 = b"\n================================================================\nPART 2 -- LESSONS REMOVED"
    if hist.count(part2) != 1:
        fail("PROJECT_INSTRUCTIONS_HISTORY.md: the PART 2 banner was not found once.")
    moved = (b"\n" + entry + b"(Moved down from the resident protocol on 2026-10-10 when\n"
             b"v3.88 made a fourth entry.)\n")
    hist = hist.replace(part2, moved + part2)
    if hist.count(entry) != 1:
        fail("PROJECT_INSTRUCTIONS_HISTORY.md: v3.85 did not arrive word for word.")
    print("ok  PROJECT_INSTRUCTIONS_HISTORY.md  v3.85 received")
    out[PHIST] = hist

    page = files[PAGE][0]
    if page.count(MARKER) != 1:
        fail("WHERE_WE_ARE.md: the run-record marker line was not found once.")
    below = page[page.index(MARKER):]
    page = apply("page", page, W_EDITS)
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
    print("ok  documentation/HANDOFF_L428_L429_round2_20261010.md created")
    above = page[:page.index(MARKER)].count(b"\n")
    print("note: WHERE_WE_ARE.md has %d lines above the run-record marker "
          "(the cap is 130)" % above)
    print("stamps updated: LEDGER_CONSOLIDATED.md header; interactive-exhibit "
          "version line; PROJECT_INSTRUCTIONS.md header and anchor; "
          "WHERE_WE_ARE.md date line")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py -- it writes interactive-exhibit's")
    print("     read plan and manifest row, and rebuilds the ledger's index.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Reinstall interactive-exhibit from a ZIP of skills/interactive-exhibit")
    print("     (keep the ZIP outside the repo), and replace the Project's")
    print("     instructions with PROJECT_INSTRUCTIONS.md (v3.88).")


if __name__ == "__main__":
    main()
