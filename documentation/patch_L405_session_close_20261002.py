#!/usr/bin/env python3
"""
patch_L405_session_close_20261002.py -- ORRERY repo.
Closes the session of 2026-10-02: L-404 done; Tony's phone check of the
Solar System room's drawer recorded on L-363, with the open question
about Home and his three suggestions; L-405 pushed, its install checked
next session; and Tony's page, documentation/WHERE_WE_ARE.md, rewritten
with his notes and his order for the not-urgent items.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L405_session_close_20261002.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery bb1b1314c843ca4e47989cbe39ce2550e403214f
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 0ffa451838dd5753710b3ec77d0d6f2f052f3d96
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch)

WHAT IT DOES.

  LEDGER_CONSOLIDATED.md          L-404 marked done, with what closed it
                                  and where its loose ends went. L-363:
                                  the phone check. L-405: the push and
                                  reinstall. A header stamp. The index is
                                  rebuilt by the maintenance run, so this
                                  patch's guard does not look inside it.
  documentation/WHERE_WE_ARE.md   rewritten; your run-record notes are
                                  folded into it and the ledger.

Everything is written or nothing is.

SUCCESS looks like: one "ok" line per edit and per file, then "patch
applied". FAILURE looks like one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

SPEC = {'BASE': {'LEDGER_CONSOLIDATED.md': '110631c7b1e6810c357450e70cb3f18e',
          'documentation/WHERE_WE_ARE.md': 'f0baa7190e8924c32617bac67ccc1e03'},
 'EDITS': {'LEDGER_CONSOLIDATED.md': [('L-405 opened and built: interactive-exhibit 1.9,\n'
                                       'ledger-and-session-records 1.14, protocol v3.77), built on '
                                       'b3cfc780.\n',
                                       'L-405 opened and built: interactive-exhibit 1.9,\n'
                                       'ledger-and-session-records 1.14, protocol v3.77), built on '
                                       'b3cfc780.\n'
                                       "Module updated: October 2, 2026 with Anthropic's Claude "
                                       'Opus 5.5\n'
                                       '(session close: L-404 done; L-363 phone check of step 3b '
                                       'and the Home\n'
                                       'question; L-405 pushed, its install confirmed next '
                                       'session), built on\n'
                                       'bb1b1314.\n',
                                       'header stamp'),
                                      ('<!-- L:404 status:OPEN upd:2026-10-01 section:A flag: '
                                       'rice: -->',
                                       '<!-- L:404 status:DONE upd:2026-10-02 section:A flag: '
                                       'rice: -->',
                                       'L-404 done'),
                                      ('- Closes when the room opens on the inner planets on the '
                                       'site. The\n'
                                       '  skill sentence above already lives on L-405.\n'
                                       '**Ref:** tools/store_writer.py, '
                                       'tools/exhibit_store_editor.py and their',
                                       '- Closes when the room opens on the inner planets on the '
                                       'site. The\n'
                                       '  skill sentence above already lives on L-405.\n'
                                       '- **Done 2026-10-02.** Tony ran the gallery patch and both '
                                       'suites passed\n'
                                       '  on his machine (store writer 289 checks, store editor '
                                       '269), with 23 of\n'
                                       '  23 gating checkers; pushed at 555150f1. In the editor he '
                                       'picked\n'
                                       '  solar-system, ticked Mercury, Venus and Mars, and saved: '
                                       'one line of\n'
                                       '  data/objects_config.json, pushed at 0ffa4518. His '
                                       'checks: the room\n'
                                       '  list shows sun, earth and solar-system; the middle panel '
                                       'says why it\n'
                                       '  is empty; ten bodies to tick with Apophis marked, and '
                                       'the highlighted\n'
                                       '  row picker -- "yes" to each. On his phone the room opens '
                                       'on the four\n'
                                       '  inner planets with Earth named.\n'
                                       '- **Loose ends re-homed** (A Closing Item Re-homes Its '
                                       'Loose Ends):\n'
                                       '  the skill sentence was corrected in interactive-exhibit '
                                       '1.9 (L-405);\n'
                                       "  whether the editor should edit the rows' own words is on "
                                       "L-363, Tony's\n"
                                       '  second "not urgent" item.\n'
                                       '**Ref:** tools/store_writer.py, '
                                       'tools/exhibit_store_editor.py and their',
                                       'L-404 close block'),
                                      ('**Gap:** The next session confirms its loaded copies read\n'
                                       'interactive-exhibit 1.9 and ledger-and-session-records '
                                       '1.14, then\n'
                                       'closes this item.',
                                       '- **Pushed 2026-10-02** at orrery f7ad52db, with 19 of 19 '
                                       'gating\n'
                                       "  checkers on Tony's machine; Tony reinstalled both skills "
                                       'and replaced\n'
                                       "  the Project's instructions with v3.77. The harness "
                                       'reached the gallery\n'
                                       "  at 3ed96777. Tony was shown the bump rule's wording and "
                                       'asked to\n'
                                       '  confirm it; he pushed it as written and has not '
                                       'commented on it.\n'
                                       '**Gap:** The next session confirms its loaded copies read\n'
                                       'interactive-exhibit 1.9 and ledger-and-session-records '
                                       '1.14, then\n'
                                       'closes this item.',
                                       'L-405 pushed'),
                                      ('<!-- L:363 status:OPEN upd:2026-10-02 section:A flag: '
                                       'rice: -->\n'
                                       '- **2026-10-02, step 3b built: the drawer.**',
                                       '<!-- L:363 status:OPEN upd:2026-10-02 section:A flag: '
                                       'rice: -->\n'
                                       "- **2026-10-02, step 3b on Tony's phone (Mode 5).** Pushed "
                                       'at gallery\n'
                                       '  3ed96777 with 23 of 23 gating checkers; the live run '
                                       'read all 15\n'
                                       '  served files SERVED and matching, solar_system_drawer.js '
                                       'among them.\n'
                                       '  Tony, phone upright, then sideways, then desktop:\n'
                                       '  - Passed: the opening on the four inner planets with '
                                       'Earth named;\n'
                                       '    the Sun\'s row ("great idea! thanks. and earth too"); '
                                       'ticking\n'
                                       '    Jupiter; Pluto with its orbit cut at the box edge and '
                                       '- showing the\n'
                                       '    whole orbit (the 20% ruling, accepted); name taps open '
                                       'and close\n'
                                       '    rows without moving the view; See more and See fewer '
                                       'with a ticked\n'
                                       '    Apophis staying; a tap on a body highlights its row; '
                                       'GO; Home with\n'
                                       '    nothing ticked puts back the inner planets; the Sun '
                                       'and Earth rooms\n'
                                       '    as before. The two info paragraphs: approved, as '
                                       'bullet lists.\n'
                                       '  - FAILED as Tony saw it: Home\'s fallback. "No, previous '
                                       'ticks do not\n'
                                       "    register. let's discuss. one option might be that a "
                                       'second Home tap\n'
                                       '    returns to the original view." Claude\'s reading, to '
                                       'confirm with\n'
                                       '    Tony and not yet tested: Home frames EVERYTHING DRAWN '
                                       'and only NAMES\n'
                                       '    the last body ticked (design 4.3 as built), so falling '
                                       'back changes\n'
                                       "    only the name on the closed drawer's handle -- nothing "
                                       'in the view.\n'
                                       '    The headless walk checked the name and the frame and '
                                       'passed, which\n'
                                       '    is the mechanism working and the meaning missed. A '
                                       'design question,\n'
                                       '    not yet a bug.\n'
                                       '  - Not judged: an opened row on a small screen ("not '
                                       'clear").\n'
                                       "  - Tony's suggestions, for the design talk: move the "
                                       'highlighted row\n'
                                       '    to the top of the list (the list is ordered outward '
                                       'from the Sun,\n'
                                       "    so this changes that order); an arrow from GO's text "
                                       'box to its\n'
                                       '    body (on an upright phone the text box has no arrow '
                                       'and sits\n'
                                       "    mid-view by Tony's L-318 ruling, so this would amend "
                                       'it).\n'
                                       '  - Small fixes for the next build: the info paragraphs as '
                                       'bullet\n'
                                       "    lists (Tony); the solar-system arrival block's "
                                       '`_declared`\n'
                                       '    sentence still says the opening view fits 1.1 times '
                                       'the largest\n'
                                       '    distance -- it is 1.2 times the distance now, a simple '
                                       'error to fix\n'
                                       '    and report (provenance-discipline 2.24); re-check the '
                                       'opened row on\n'
                                       '    the phone.\n'
                                       '  - Re-homed from L-404 at its close: whether the editor '
                                       'should edit\n'
                                       "    the rows' own words (`label`, `about`, `source_note`). "
                                       "Tony's order\n"
                                       '    for the not-urgent items, 2026-10-02: first the full '
                                       'check of the\n'
                                       "    orrery's object list against Horizons, second this, "
                                       'third choosing\n'
                                       '    a date and animation.\n'
                                       '- **2026-10-02, step 3b built: the drawer.**',
                                       'L-363 phone check')]},
 'REPLACE': {'documentation/WHERE_WE_ARE.md': '<!-- Doc-Kind: hand | Where the project is and '
                                              'where it is going, in plain words. One file, '
                                              'rewritten in place; read it at the end of every '
                                              'session. -->\n'
                                              '# Where We Are\n'
                                              '\n'
                                              'Last updated: October 2, 2026, end of session\n'
                                              '- Written at orrery bb1b1314 and gallery 0ffa4518.\n'
                                              '\n'
                                              '> **READ THIS FIRST**\n'
                                              '>\n'
                                              '> **Changed this session:**\n'
                                              "> - The Solar System room's drawer is on the "
                                              'website, and your phone\n'
                                              '>   check passed nearly everything.\n'
                                              '> - The room opens on the four inner planets, set '
                                              'in the editor, which\n'
                                              '>   now lists every room.\n'
                                              '> - The room frames where each body is now, plus '
                                              '20%: your ruling.\n'
                                              '> - Two skills and the protocol are updated for '
                                              'this work.\n'
                                              '>\n'
                                              '> **Do next:**\n'
                                              "> - *The Sun's numbers get the same checking "
                                              "Earth's got.*\n"
                                              '>\n'
                                              '> **Needs you now:**\n'
                                              '> - *Nothing. At the next design talk: what Home '
                                              'should do.*\n'
                                              '\n'
                                              'How to read the marks:\n'
                                              '- *Italic* lines are the must-reads.\n'
                                              '- **>> UPDATED THIS SESSION** beside a heading '
                                              'means that section\n'
                                              '  changed in the latest session.\n'
                                              '- "<< new this session" beside a road stage marks a '
                                              'change to the road.\n'
                                              '- Sections without a mark are as they were.\n'
                                              '- The marks are cleared and reset at every '
                                              "session's update, so they\n"
                                              '  always mean "new since you last read this."\n'
                                              '\n'
                                              '## The goal\n'
                                              '\n'
                                              "- Paloma's Orrery on the web.\n"
                                              '- The website does what the desktop orrery does, in '
                                              'the browser, from\n'
                                              '  data fetched from JPL each night, so a visitor '
                                              'never waits on JPL.\n'
                                              '- Anyone can open it, with nothing to install.\n'
                                              '- Built from the same code and the same checked '
                                              'numbers as the desktop\n'
                                              '  orrery.\n'
                                              '- The one real limit: the browser can show only the '
                                              'dates the saved\n'
                                              '  data covers.\n'
                                              '- Within that range, a visitor will be able to '
                                              'choose a date, and\n'
                                              '  perhaps play time forward.\n'
                                              '\n'
                                              '## The road  **>> UPDATED THIS SESSION**\n'
                                              '\n'
                                              "  1. [done]   The Sun's room is live on the "
                                              'website.\n'
                                              "  2. [done]   Earth's room is live, with every "
                                              'number traced to its source.\n'
                                              '  3. [done]   The numbers come from one place: the '
                                              'orrery feeds the\n'
                                              '              website, and nothing is typed twice.\n'
                                              '  4. [NOW]    The Solar System room becomes a '
                                              'second way in: all the\n'
                                              '              planets, a drawer to pick them, and a '
                                              'way into each\n'
                                              "              body's own room. << new this session: "
                                              'built and on the\n'
                                              '              website; what Home does is still to '
                                              'settle.\n'
                                              "  5. [next]   *The Sun's numbers get the same "
                                              "checking Earth's got.*\n"
                                              "  6. [next]   The Solar System room's card becomes "
                                              'the top featured\n'
                                              '              card in the lobby. A bare '
                                              'interactive.html link opens\n'
                                              '              the Solar System room, and the '
                                              'Explorer gets its own\n'
                                              '              address.\n'
                                              "  7. [later]  The rest of the orrery's objects come "
                                              'to the website --\n'
                                              '              dwarf planets, asteroids, moons -- '
                                              'through the same\n'
                                              '              connection that now carries the '
                                              "room's eleven bodies,\n"
                                              '              checked against JPL Horizons.\n'
                                              '  8. [later]  Encounters: comets and spacecraft '
                                              'shown at the dates\n'
                                              '              that matter.\n'
                                              '  9. [later]  The planets get their details -- '
                                              'layers, rings, magnetic\n'
                                              '              fields -- Jupiter and Saturn first.\n'
                                              ' 10. [goal]   The website does what the desktop '
                                              'orrery does, from data\n'
                                              '              fetched from JPL each night, with a '
                                              'date to choose and\n'
                                              '              time to play within the range the '
                                              'data covers.\n'
                                              '\n'
                                              '## Right now  **>> UPDATED THIS SESSION**\n'
                                              '\n'
                                              '- The Solar System room opens on the Sun and the '
                                              'four inner planets,\n'
                                              '  with Earth named on the closed drawer.\n'
                                              "- Its drawer is live: the Sun's row is fixed, rows "
                                              'open with "Enter\n'
                                              '  the Sun room" or "Enter the Earth room", Apophis '
                                              'waits under See\n'
                                              '  more, and a tap on a body finds its row.\n'
                                              '- The view holds every body drawn, where it is now, '
                                              "plus 20%. Pluto's\n"
                                              '  orbit runs past the edge until you press -.\n'
                                              '- Home works, but falling back to an earlier body '
                                              'shows no visible\n'
                                              '  change. That is the open design question below.\n'
                                              "- Each body's info panel shows a description and a "
                                              'NASA link, copied\n'
                                              "  from the orrery's own object list.\n"
                                              '- The editor can set what any room opens on. It '
                                              'cannot yet change the\n'
                                              "  words on the Solar System room's rows, such as "
                                              "Pluto's sentence.\n"
                                              "- The rest of the orrery's objects are not "
                                              'connected yet.\n'
                                              '\n'
                                              '## The next three steps  **>> UPDATED THIS '
                                              'SESSION**\n'
                                              '\n'
                                              "1. *The Sun's numbers get the same checking Earth's "
                                              'got.*\n'
                                              "2. The drawer's small fixes:\n"
                                              "   - The info panel's two paragraphs become bullet "
                                              'lists, as you\n'
                                              '     asked.\n'
                                              "   - One sentence in the room's settings still says "
                                              'the view fits\n'
                                              '     1.1 times what is drawn; it is 1.2 now.\n'
                                              '   - You look again at an opened row on the phone: '
                                              'does the drawer\n'
                                              '     still fit and scroll, and is "Enter" easy to '
                                              'hit?\n'
                                              '3. What Home should do, settled in conversation, '
                                              'then built.\n'
                                              '\n'
                                              '## Waiting on you  **>> UPDATED THIS SESSION**\n'
                                              '\n'
                                              'Now:\n'
                                              '- Nothing.\n'
                                              '\n'
                                              'At the next design talk:\n'
                                              '- *Home.* My reading of your phone note: Home '
                                              'already names the last\n'
                                              '  body ticked, but it frames everything drawn, so '
                                              'falling back to an\n'
                                              '  earlier body only changes the name on the '
                                              "drawer's handle. You may\n"
                                              '  have expected Home to take the view to that body. '
                                              'Your idea: a\n'
                                              '  second Home tap returns to the opening view.\n'
                                              '- Moving the highlighted row to the top of the '
                                              'list. The list is now\n'
                                              '  in order outward from the Sun, so this changes '
                                              'that order.\n'
                                              "- An arrow from GO's text box to its body. On a "
                                              'phone held upright the\n'
                                              '  text box has no arrow and sits mid-view, by your '
                                              'earlier ruling, so\n'
                                              '  this would change that ruling.\n'
                                              '\n'
                                              'Not urgent, in your order:\n'
                                              "1. The full check of the orrery's object list "
                                              'against JPL Horizons.\n'
                                              '   - Its first run lists what disagrees; simple '
                                              'errors get fixed and\n'
                                              '     listed, the rest come to you.\n'
                                              '2. Whether the editor should also edit the words on '
                                              'the Solar System\n'
                                              "   room's rows, such as Pluto's sentence.\n"
                                              '   - Today a change to them comes as a patch from a '
                                              'session.\n'
                                              '3. Choosing a date, and animation, your idea of '
                                              'October 1.\n'
                                              '   - The range would follow only the bodies you '
                                              'tick.\n'
                                              '\n'
                                              '## Where the details are  **>> UPDATED THIS '
                                              'SESSION**\n'
                                              '\n'
                                              '- Every item, done and open: '
                                              '`LEDGER_CONSOLIDATED.md`\n'
                                              '  - This session: L-404 (done), L-405, and the '
                                              'newest notes on L-363.\n'
                                              '- The reasoning behind the order:\n'
                                              '  '
                                              '`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
                                              '- The latest session record: those ledger items. '
                                              'This session wrote no\n'
                                              '  separate handoff.\n'}}


def fingerprint(path, raw):
    """The content, line endings aside. For the ledger and the protocol,
    the content OUTSIDE the zone a generator rewrites (ledger_index.py's
    index; skills_index.py's manifest)."""
    lf = raw.replace(b"\r\n", b"\n")
    if path == "LEDGER_CONSOLIDATED.md":
        a = lf.index(b"<!-- INDEX:START")
        b = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
        lf = lf[:a] + lf[b:]
    if path == "PROJECT_INSTRUCTIONS.md":
        a = lf.index(b"<!-- SKILL-MANIFEST:START")
        b = lf.index(b"<!-- SKILL-MANIFEST:END -->") + len(b"<!-- SKILL-MANIFEST:END -->")
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    raws = {}
    for path in list(SPEC['EDITS']) + list(SPEC['REPLACE']):
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(path, raws[path])
        if got != SPEC['BASE'][path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written. Undo is Discard Changes in\n"
                "       GitHub Desktop." % (path, SPEC['BASE'][path], got))

    results = []
    for path, edits in sorted(SPEC['EDITS'].items()):
        raw = raws[path]
        nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
        text = raw.decode("utf-8")
        before = sum(1 for ch in text if ord(ch) > 127)
        done = []
        for old, new, label in edits:
            o = old.replace("\n", nl)
            n = new.replace("\n", nl)
            count = text.count(o)
            if count != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, count))
            text = text.replace(o, n)
            done.append(label)
        if sum(1 for ch in text if ord(ch) > 127) > before:
            raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                             "NOTHING was written." % path)
        results.append((path, text.encode("utf-8"), done))
    for path, content in sorted(SPEC['REPLACE'].items()):
        nl = "\r\n" if raws[path].count(b"\r\n") > 0 else "\n"
        results.append((path, content.replace("\n", nl).encode("ascii"),
                        ["rewritten"]))

    for path, data, done in results:
        with open(path, "wb") as handle:
            handle.write(data)
        for label in done:
            print("ok  %-34s %s" % (path, label))

    print("")
    print("Stamps updated: the ledger's header; Where We Are's date and SHAs.")
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py -- the ledger index moves")
    print("     L-404 to the closed section.")
    print("  2. Move this script into documentation/; commit and push.")

if __name__ == "__main__":
    main()
