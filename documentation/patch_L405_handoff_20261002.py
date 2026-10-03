#!/usr/bin/env python3
"""
patch_L405_handoff_20261002.py -- ORRERY repo.
Adds the session handoff of 2026-10-02 and points Where We Are at it.

The first close patch already ran and was pushed at 5e42b00b, so the
second copy of it, which also carried this handoff, rightly refused:
the ledger had already moved. This patch carries ONLY what that second
copy added. Delete patch_L405_session_close_20261002.py if a second
copy of it is still in the repo root.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L405_handoff_20261002.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 5e42b00bdce82e895cc4b5a8d0aaa4d14283e9cb
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 0ffa451838dd5753710b3ec77d0d6f2f052f3d96
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch)

WHAT IT DOES.

  documentation/HANDOFF_L363_L404_L405_session_20261002.md
                                  NEW: the session record for the next
                                  session.
  documentation/WHERE_WE_ARE.md   one line: the latest session record is
                                  that handoff.

Everything is written or nothing is.

SUCCESS looks like: two "ok" lines, then "patch applied". FAILURE looks
like one ERROR: or ANCHOR FAIL: line, and NOTHING is written. Undo is
Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

SPEC = {'BASE': {'documentation/WHERE_WE_ARE.md': 'df47e6c85de1634998ac6fb84a98e62a'},
 'EDITS': {'documentation/WHERE_WE_ARE.md': [('- The latest session record: those ledger items. '
                                              'This session wrote no\n'
                                              '  separate handoff.',
                                              '- The latest session record:\n'
                                              '  '
                                              '`documentation/HANDOFF_L363_L404_L405_session_20261002.md`',
                                              'points at the handoff')]},
 'NEW': {'documentation/HANDOFF_L363_L404_L405_session_20261002.md': '<!-- Doc-Kind: hand | '
                                                                     'Session record of '
                                                                     '2026-10-02: the editor lists '
                                                                     'every room, the Solar System '
                                                                     "room's drawer, two skills. "
                                                                     "Read at the next session's "
                                                                     'start. -->\n'
                                                                     '# Handoff -- 2026-10-02: the '
                                                                     'editor, the drawer, two '
                                                                     'skills\n'
                                                                     '\n'
                                                                     'Built on orrery '
                                                                     'bb1b1314c843ca4e47989cbe39ce2550e403214f '
                                                                     'at\n'
                                                                     'https://github.com/tonylquintanilla/palomas_orrery '
                                                                     'and gallery\n'
                                                                     '0ffa451838dd5753710b3ec77d0d6f2f052f3d96 '
                                                                     'at\n'
                                                                     'https://github.com/tonylquintanilla/tonyquintanilla.github.io '
                                                                     '-- the\n'
                                                                     'state after every build push '
                                                                     "of the session. The ledger's "
                                                                     'close\n'
                                                                     'followed at orrery '
                                                                     '5e42b00bdce82e895cc4b5a8d0aaa4d14283e9cb.\n'
                                                                     '\n'
                                                                     '- **Type:** BUILD, with a '
                                                                     'documentation part (two '
                                                                     'skill versions).\n'
                                                                     '- **Supersedes:** nothing. '
                                                                     '**Companions:**\n'
                                                                     '  '
                                                                     '`patch_L405_session_close_20261002.py` '
                                                                     "(the ledger's close and "
                                                                     'Where\n'
                                                                     '  We Are, pushed at '
                                                                     '5e42b00b) and '
                                                                     '`patch_L405_handoff_20261002.py`,\n'
                                                                     '  which carries this file.\n'
                                                                     '- **Ledger items:** L-404 '
                                                                     '(done), L-405 (open, closes '
                                                                     'next session),\n'
                                                                     '  L-363 (open: step 3b built '
                                                                     'and seen on the phone).\n'
                                                                     '\n'
                                                                     '## 1. Check first, before '
                                                                     'any exhibit or ledger work\n'
                                                                     '\n'
                                                                     '- **Your loaded skills.** '
                                                                     '`interactive-exhibit` must '
                                                                     'read 1.9 and\n'
                                                                     '  '
                                                                     '`ledger-and-session-records` '
                                                                     'must read 1.14. This session '
                                                                     'loaded 1.8\n'
                                                                     '  and 1.13, wrote the new '
                                                                     'versions, and Tony '
                                                                     'reinstalled them after the\n'
                                                                     '  push (Stale Skill = Stop: '
                                                                     'the session that installs '
                                                                     'cannot verify).\n'
                                                                     '  If they match, close '
                                                                     'L-405. If not, STOP and ask '
                                                                     'Tony to push and\n'
                                                                     '  reinstall.\n'
                                                                     '- **HEAD.** The orrery '
                                                                     'should be at 5e42b00b, or '
                                                                     'ahead by this\n'
                                                                     "  handoff's patch only; the "
                                                                     'gallery at 0ffa4518. '
                                                                     'Anything else:\n'
                                                                     '  reconcile before '
                                                                     'building.\n'
                                                                     '\n'
                                                                     '## 2. What was done\n'
                                                                     '\n'
                                                                     'Each line says whether it '
                                                                     'was VERIFIED, and by what, '
                                                                     'or is a CLAIM.\n'
                                                                     '\n'
                                                                     '- **The editor lists every '
                                                                     'room (L-404, done).** '
                                                                     '`tools/store_writer.py`\n'
                                                                     '  gained `room_ids()` and '
                                                                     'may change a rooms-section '
                                                                     "room's `drawn` and\n"
                                                                     '  `highlight`; '
                                                                     '`tools/exhibit_store_editor.py` '
                                                                     'lists rooms from both\n'
                                                                     '  places a room can live. '
                                                                     'VERIFIED: both suites on '
                                                                     "Tony's machine (289\n"
                                                                     '  and 269 checks), 23 of 23 '
                                                                     'gating checkers, his own '
                                                                     'look at the editor.\n'
                                                                     '  Pushed at gallery '
                                                                     '555150f1. He then ticked '
                                                                     'Mercury, Venus and Mars:\n'
                                                                     '  one line of '
                                                                     '`data/objects_config.json`, '
                                                                     'pushed at 0ffa4518.\n'
                                                                     "- **The Solar System room's "
                                                                     'drawer (L-363 step 3b).** '
                                                                     "The Sun's fixed\n"
                                                                     '  row; rows that open with '
                                                                     '"Enter the Sun room" / '
                                                                     '"Enter the Earth room"\n'
                                                                     '  or "No room or cards yet"; '
                                                                     'See more / See fewer; a tap '
                                                                     'on a body\n'
                                                                     '  highlights its row and '
                                                                     "moves nothing; Home's tick "
                                                                     'order; All / none\n'
                                                                     '  leaving the Sun. Logic in '
                                                                     '`gallery/solar_system_drawer.js`, '
                                                                     'checked by\n'
                                                                     '  '
                                                                     '`documentation/smoke_solar_system_drawer.js` '
                                                                     '(gating). VERIFIED: a\n'
                                                                     '  55-check headless walk on '
                                                                     'the real driver payload, '
                                                                     'shown failing on a\n'
                                                                     '  broken copy; the Sun and '
                                                                     'Earth rooms identical before '
                                                                     'and after; 23 of\n'
                                                                     "  23 on Tony's machine; the "
                                                                     'live run reads the new file '
                                                                     "SERVED; Tony's\n"
                                                                     '  phone (section 3). Pushed '
                                                                     'at gallery 3ed96777.\n'
                                                                     "- **Framing, Tony's ruling** "
                                                                     '("B but with a buffer of '
                                                                     '20%"): the room\n'
                                                                     "  frames on each body's "
                                                                     'distance from the Sun now, '
                                                                     'times 1.2; the\n'
                                                                     '  farthest ticked body sets '
                                                                     'it; opening, Home and GO '
                                                                     'follow. VERIFIED on\n'
                                                                     "  the phone: Pluto's orbit "
                                                                     'cut at the box edge, - shows '
                                                                     'it whole.\n'
                                                                     '- **Five calls Claude made '
                                                                     'in the build, confirmed by '
                                                                     'Tony:** a tap in\n'
                                                                     '  the picture moves nothing; '
                                                                     'a name tap moves nothing, '
                                                                     'only GO does;\n'
                                                                     '  Home with nothing ticked '
                                                                     'restores the served opening; '
                                                                     'no GO on the\n'
                                                                     "  Sun's row; the opening "
                                                                     'frame has no 1.2 AU '
                                                                     'minimum.\n'
                                                                     '- **Skills (L-405):** '
                                                                     'interactive-exhibit 1.9 (the '
                                                                     'rooms-section\n'
                                                                     '  sentence corrected; what '
                                                                     'is editable there; the body '
                                                                     'drawer and its\n'
                                                                     '  framing; the headless '
                                                                     'recipe); '
                                                                     'ledger-and-session-records '
                                                                     '1.14 (A\n'
                                                                     '  Wrong Sentence in a Skill: '
                                                                     'Bump Now, or Carry It); '
                                                                     'protocol v3.77.\n'
                                                                     '  Pushed at orrery f7ad52db, '
                                                                     '19 of 19. CLAIM, not yet '
                                                                     'checked: that the\n'
                                                                     '  reinstalled copies load as '
                                                                     '1.9 and 1.14 (section 1).\n'
                                                                     '- **The headless harness** '
                                                                     'is filed in the gallery at '
                                                                     '`tools/headless/`\n'
                                                                     '  (four files, Claude-only). '
                                                                     'VERIFIED here, from the '
                                                                     'gallery root.\n'
                                                                     '\n'
                                                                     "## 3. Tony's phone check, "
                                                                     'and what it left open\n'
                                                                     '\n'
                                                                     'Phone upright, then '
                                                                     'sideways, then desktop. '
                                                                     'Everything passed except:\n'
                                                                     '\n'
                                                                     "- **Home's fallback -- "
                                                                     'failed as Tony saw it.** His '
                                                                     'words: "No, previous\n'
                                                                     '  ticks do not register. '
                                                                     "let's discuss. one option "
                                                                     'might be that a\n'
                                                                     '  second Home tap returns to '
                                                                     'the original view." '
                                                                     "Claude's reading, not\n"
                                                                     '  yet put to him: Home '
                                                                     'frames EVERYTHING DRAWN and '
                                                                     'only NAMES the last\n'
                                                                     '  ticked body, so falling '
                                                                     'back changes only the name '
                                                                     'on the closed\n'
                                                                     "  drawer's handle. The "
                                                                     'headless walk checked the '
                                                                     'name and the frame and\n'
                                                                     '  passed -- the mechanism '
                                                                     'right, the meaning missed. A '
                                                                     'design question\n'
                                                                     '  for the next design talk, '
                                                                     'not a bug to patch on '
                                                                     'sight.\n'
                                                                     '- **An opened row on a small '
                                                                     'screen:** "not clear". Look '
                                                                     'again.\n'
                                                                     '\n'
                                                                     '## 4. Open, in the order to '
                                                                     'take them\n'
                                                                     '\n'
                                                                     "1. **The Sun's slice -- the "
                                                                     "next session's work, by "
                                                                     "Tony's choice.**\n"
                                                                     '   Where We Are calls it '
                                                                     '"the Sun\'s numbers get the '
                                                                     'same checking\n'
                                                                     '   Earth\'s got". It is '
                                                                     'defined by L-371 (the Sun '
                                                                     "room's 43 served\n"
                                                                     '   numbers with no link, '
                                                                     'sorted into measurements and '
                                                                     'drawing choices,\n'
                                                                     '   each measured one given a '
                                                                     'row and a count and printed '
                                                                     'by it) and\n'
                                                                     "   L-386 (the Sun's rows "
                                                                     'that are another row in a '
                                                                     'different unit --\n'
                                                                     '   `SOLAR_RADIUS_AU`, '
                                                                     '`CORE_AU`, '
                                                                     '`RADIATIVE_ZONE_AU` and '
                                                                     'their\n'
                                                                     '   neighbours -- re-homed '
                                                                     'and served as conversions); '
                                                                     "the master plan's\n"
                                                                     '   executive summary, step '
                                                                     "2; L-322's Gap (3). "
                                                                     'provenance-discipline\n'
                                                                     '   2.24 fires. The swap (a '
                                                                     'bare interactive.html '
                                                                     'opening the Solar\n'
                                                                     '   System room) waits for '
                                                                     'it.\n'
                                                                     "2. **The drawer's small "
                                                                     'fixes, one gallery patch:** '
                                                                     "the info panel's\n"
                                                                     '   two paragraphs as bullet '
                                                                     'lists (Tony approved the '
                                                                     'words); the\n'
                                                                     '   solar-system arrival '
                                                                     "block's `_declared` sentence "
                                                                     'says the opening\n'
                                                                     '   fits 1.1 times the '
                                                                     'largest distance -- it is '
                                                                     '1.2 times the distance\n'
                                                                     '   now, a simple error to '
                                                                     'fix and report (the store '
                                                                     'writer does not\n'
                                                                     '   edit `_declared`, so it '
                                                                     "is a patch); then Tony's "
                                                                     'second look at an\n'
                                                                     '   opened row.\n'
                                                                     '3. **At the next design '
                                                                     'talk:** Home (section 3); '
                                                                     'moving the\n'
                                                                     '   highlighted row to the '
                                                                     'top of the list, which '
                                                                     'changes the order\n'
                                                                     '   outward from the Sun; an '
                                                                     "arrow from GO's text box to "
                                                                     'its body, which\n'
                                                                     "   would amend Tony's L-318 "
                                                                     'ruling that an upright phone '
                                                                     'shows no arrow.\n'
                                                                     "4. **Not urgent, in Tony's "
                                                                     'order of 2026-10-02:** the '
                                                                     'full check of the\n'
                                                                     "   orrery's object list "
                                                                     'against Horizons; whether '
                                                                     'the editor should edit\n'
                                                                     "   the rows' own words; "
                                                                     'choosing a date and '
                                                                     'animation.\n'
                                                                     '\n'
                                                                     '## 5. Discrepancies surfaced '
                                                                     'this session\n'
                                                                     '\n'
                                                                     "- Claude's first summary of "
                                                                     'the framing choice said the '
                                                                     'two rules\n'
                                                                     '  differ only for stretched '
                                                                     'orbits. Wrong: in a square '
                                                                     'box they also\n'
                                                                     '  differ wherever a body '
                                                                     'sits toward a corner '
                                                                     '(Jupiter, by about a\n'
                                                                     '  third, under the tightest '
                                                                     'rule). Corrected before Tony '
                                                                     'ruled.\n'
                                                                     '- The orrery ledger patch '
                                                                     'was replaced twice before it '
                                                                     'was run, each\n'
                                                                     '  time under a new name, and '
                                                                     'the gallery drawer patch was '
                                                                     'regenerated\n'
                                                                     '  three times under one name '
                                                                     'before Tony ran it. Nothing '
                                                                     'ran on a stale\n'
                                                                     '  copy; the run record shows '
                                                                     'the final files.\n'
                                                                     '- Tony was shown the 1.14 '
                                                                     "bump rule's wording and "
                                                                     'asked to confirm it.\n'
                                                                     '  He pushed it as written '
                                                                     'and has not commented on '
                                                                     'it.\n'
                                                                     '\n'
                                                                     'Session/entry written '
                                                                     'October 2026 with '
                                                                     "Anthropic's Claude Opus "
                                                                     '5.5.\n'}}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    for path in SPEC['NEW']:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If you already ran "
                             "this patch, it has nothing left to do. NOTHING "
                             "was written." % path)
    results = []
    for path, edits in sorted(SPEC['EDITS'].items()):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != SPEC['BASE'][path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written. Undo is Discard Changes in\n"
                "       GitHub Desktop." % (path, SPEC['BASE'][path], got))
        nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
        text = raw.decode("utf-8")
        done = []
        for old, new, label in edits:
            o = old.replace("\n", nl)
            n = new.replace("\n", nl)
            if text.count(o) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(o)))
            text = text.replace(o, n)
            done.append(label)
        results.append((path, text, done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-34s %s" % (path, label))
    for path, content in sorted(SPEC['NEW'].items()):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print("ok  %s created" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/; commit and push.")
    print("     No maintenance run is needed: no generated file changes.")


if __name__ == "__main__":
    main()
