#!/usr/bin/env python3
"""
patch_L408_L363_phone_rulings_20261003.py -- ORRERY repo. Records what
Tony settled from his phone on 2026-10-03, after the session closed:
the Galactic Plane toggle and its approved words (L-408), the tide's
look moved into that build (L-406), Home and the lobby's Solar System
card (L-363). Nothing is built; the next session builds from these.

THIS REPLACES patch_L408_galactic_plane_note_20261003.py and the
earlier patch_L408_galactic_plane_words_20261003.py. Run this one and
neither of those. It starts from the same files they did. If either
has already run, this one refuses and writes nothing -- tell the next
session, which adds the rest by hand.

RUN IT AFTER patch_L371_session_close_20261003.py AND ITS MAINTENANCE
RUN. It was built on the files those two leave, from orrery
fd508f9c7794e3a51b22a4e1e3aa3a54c3e339ef
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 52659e04b38dd773aa14b6e6e9e1a533bff114e7
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   L-408 opened: the toggle as Tony confirmed
        it, and its words as he approved them on 2026-10-03 -- row name,
        description, info panel, note, link, and the rule that the
        angle is worked out from the pole rows, not typed. L-406: the
        Mode 5 look at the tide moves to L-408 (the X cannot be found
        without the ring as a reference), and the reinstall of
        interactive-exhibit 1.10 is recorded as confirmed.
    documentation/HANDOFF_L406_L407_L371_session_20261003.md   section
        4, item 2: the toggle, words approved, with the look folded in;
        item 3 takes Home as settled, and a new item 4 the lobby card.
        L-363: Home settled (fit every body ticked; no second tap), and
        the lobby's wide Solar System card, in Featured and behind the
        Solar System door, from a Design canvas Tony chose from.
    documentation/WHERE_WE_ARE.md   the toggle in "Do next" and in the
        next three steps; "Needs you now" and "Waiting on you, now" say
        nothing -- the reinstall was checked on October 3 and the look
        waits on the toggle; Home and the lobby card on the road and in
        the next steps, and Home off the design-talk list.

No code changes.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L408_L363_phone_rulings_20261003.py

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

# The same three fingerprints as the patch this replaces: the files as
# patch_L371_session_close_20261003.py and its maintenance run leave them.
BASE = {'LEDGER_CONSOLIDATED.md': 'b5406cf114c24e7af6da0838265271ab',
        'documentation/HANDOFF_L406_L407_L371_session_20261003.md':
            '0e14d53bf5c190bfb7bd0b5105b80b58',
        'documentation/WHERE_WE_ARE.md': '8d29dd2f80cf5f4bf71ebebf34741c9b'}

L407_HEADING = ("#### [L-407] A skill's header is checked as YAML "
                "(orrery, skills)\n")

L408_BLOCK = """\
#### [L-408] A Galactic Plane toggle in the Sun room (gallery, the Sun's slice)
<!-- L:408 status:OPEN upd:2026-10-03 section:A flag: rice: -->
- **Asked 2026-10-03** by Tony, looking for the galactic tide's X on
  the phone and not finding it at the angle he had: "Could we toggle on
  the galactic plane and axis?" Claude agreed it earns its place: it
  makes the tide's tilt legible at a glance, and teaches on its own
  that the solar system is tipped steeply against the galaxy.
- **The design Tony confirmed ("Yes please"):** one new row in the
  Oort Cloud group, "Galactic Plane", off by default; a faint ring in
  the galaxy's plane at the tide's outer edge (`OUTER_OORT_CLOUD_AU`,
  100,000 AU) and a line along the galactic pole axis through the Sun;
  no new numbers -- it reads the same two pole rows the tide reads
  (`GALACTIC_NORTH_POLE_RA_J2000_DEG`, `_DEC_J2000_DEG`), so the ring
  and the tide cannot disagree. Left out for now: the direction to the
  galaxy's centre, which needs one more sourced number.
- **Words approved 2026-10-03** (Tony: "Approved"), to be served as
  written:
  - Row name: "Galactic Plane"
  - Description: "The plane of the Milky Way's disk, drawn as a ring
    around the Sun, with a line along the galaxy's north-south axis."
  - Info panel: "The Milky Way is a flat disk of stars, gas and dust,
    and the Sun lies inside it. Seen from Earth, that disk is the pale
    band of the Milky Way across the night sky. The ring shows the
    disk's plane, and the line through the Sun points to the galaxy's
    north pole, in the constellation Coma Berenices. The planets'
    orbits are tipped steeply against it: the two planes meet at
    [ANGLE] degrees. That tilt is why the galactic tide looks tipped
    against the Hills cloud, which lies close to the planets' plane."
  - Note: "The ring is drawn at the outer edge of the Oort cloud, where
    the tide is drawn, to show the plane's direction. The galaxy's disk
    reaches far beyond it."
  - Link: https://en.wikipedia.org/wiki/Galactic_coordinate_system,
    shown as "Read more at Wikipedia". A search on 2026-10-03 found no
    NASA page specific to the galactic plane, so Wikipedia applies by
    the L-265 rule. The article's table also places the north galactic
    pole in Coma Berenices, which backs that sentence.
  - [ANGLE] is NOT typed (a hover string that types a number is a
    store). The renderer works out the angle between the galactic plane
    and the ecliptic from the two pole rows and the frame angle the
    tide already uses, and prints it to the nearest degree. The rows
    give 60.19, so it prints 60; Portegies Zwart et al. 2021 (A&A 652,
    A144, sec. 3.2) give 60 as the cross-check.
**Gap:** Build it next session, with the Sun's distance cards (L-371):
gallery first; whether the orrery gets the same toggle is asked then.
**Ref:** L-406, L-265; gallery `gallery/feature_renderers.js`,
`data/objects_config.json`.

"""

L363_OLD = """\
<!-- L:363 status:OPEN upd:2026-10-02 section:A flag: rice: -->
- **2026-10-02, step 3b on Tony's phone (Mode 5).**"""

L363_NEW = """\
<!-- L:363 status:OPEN upd:2026-10-03 section:A flag: rice: -->
- **2026-10-03, Home settled (Tony, from his phone).** Of three ways,
  option 2 "as recommended": Home fits every body ticked, by the room's
  framing rule (where each body is now, plus 20%), at the opening
  angle, drawer closed. The order bodies were ticked in no longer
  matters to Home; the drawer's handle keeps naming the last body
  ticked. With nothing ticked, Home still puts back the served opening.
  No second tap (Tony: "No"): the way back to the opening is to untick
  everything and press Home, or reload. GO goes in, Home backs out.
  interactive-exhibit 1.10's "Home remembers the tick order" describes
  today's Home; the build corrects it in the skill.
- **2026-10-03, the lobby's way in (Tony, from his phone).** From a
  Design canvas of three sketches -- a hero card above the doors; one
  Solar System door with two buttons; a wide card first in Featured --
  Tony chose the third: "The Solar System, live", full width at the top
  of Featured with a picture of the room, above the Sun and Earth cards.
  His addition: the Solar System door's own page shows the same wide
  card first under "Exhibits here" (Tony: "Yes, exactly"). This is the
  2026-10-01 ruling's "highlighted in some other way too". The canvas,
  private to Tony: https://claude.ai/artifact/ELfZfhvvyHjckJPY9829Ks
  - In all three sketches but not ruled on separately, so Tony confirms
    them at the build: the doors' arrow (U+25B6, which iOS draws as a
    blue emoji button, as his screenshot shows) drawn as a plain SVG
    chevron; and the door's line dropping "N rooms under construction".
  - The picture is a still of the room, not the sketch's drawing; Tony
    judges it at Mode 5.
- **Found 2026-10-03, recorded, not chased:** gallery_config.json gives
  the solar_system door a child room keyed `solar_system`, labelled
  "solar_system", holding no cards, so the door page lists it under
  construction. Looked at when the lobby card is built.
- **2026-10-02, step 3b on Tony's phone (Mode 5).**"""

L406_OLD_GAP = """\
  redrawn tide's stored pole gives 60.19 degrees.
**Gap:** Tony: reinstall interactive-exhibit 1.10, and look at the tide
on the phone and in the orrery (Mode 5). The next session confirms its
loaded interactive-exhibit reads 1.10.
"""

L406_NEW_GAP = """\
  redrawn tide's stored pole gives 60.19 degrees.
- **The look moves to L-408, 2026-10-03.** Tony had already turned the
  tide on the phone looking for the X and could not find it without a
  reference; that is why he asked for the Galactic Plane toggle. His
  screenshot of 2026-10-03 shows an even cloud around the torus, which
  is what the drawing should look like from most angles. The look is
  made once L-408's ring is drawn: turn until the ring is edge-on.
- **Reinstall confirmed, 2026-10-03:** the session of that day loaded
  interactive-exhibit 1.10.
**Gap:** The look, on the phone and in the orrery (Mode 5), waits on
L-408's ring as its reference.
"""

EDITS = {
    'LEDGER_CONSOLIDATED.md': [
        ('L-406: the look moves to L-408',
         L406_OLD_GAP,
         L406_NEW_GAP),
        ('L-363: Home settled, and the lobby card',
         L363_OLD,
         L363_NEW),
        ('L-408 new item, with its approved words',
         L407_HEADING,
         L408_BLOCK + L407_HEADING),
    ],
    'documentation/HANDOFF_L406_L407_L371_session_20261003.md': [
        ('section 4: the toggle, with the look folded in',
         "2. **Tony's Mode 5 look at the tide**, if not done: in the Sun"
         " room,\n"
         "   tick the tide and the Hills torus, turn until the tide shows"
         " an X;\n"
         "   its centre line should be tilted about 60 degrees against the"
         " torus,\n"
         "   and the ends of its axis thin.\n",
         "2. **The Galactic Plane toggle (L-408)**, added at the session's"
         " end\n"
         "   at Tony's request: a ring in the galaxy's plane at 100,000 AU"
         " and\n"
         "   the galactic pole axis, one row, off by default, from the"
         " tide's own\n"
         "   pole rows. Its words are approved and recorded on L-408.\n"
         "   Tony's Mode 5 look at the tide moves here: he could not find"
         " the X\n"
         "   without a reference, which is why he asked for the toggle."
         " Once it\n"
         "   is built, turn until the ring is edge-on; the tide should show"
         " an X,\n"
         "   its empty middle along the ring, tilted about 60 degrees"
         " against the\n"
         "   Hills torus, with the ends of the axis thin.\n"),
        ('section 4: Home settled, and the lobby card',
         "3. The drawer's small fixes and the Home design talk, as the\n"
         "   2026-10-02 handoff lists them.\n",
         "3. The drawer's small fixes, as the 2026-10-02 handoff lists"
         " them,\n"
         "   and Home as Tony settled it from his phone on 2026-10-03"
         " (L-363).\n"
         "4. The lobby's wide Solar System card, in Featured and behind"
         " the\n"
         "   Solar System door (L-363, 2026-10-03), with road stage 6.\n"),
    ],
    'documentation/WHERE_WE_ARE.md': [
        ('needs you now: nothing',
         "> - *If not done yet: reinstall the three skills and the v3.79\n"
         ">   instructions, and look for the tide's X on the phone.*\n",
         "> - *Nothing. The skills and instructions were reinstalled and"
         " checked\n"
         ">   on October 3.*\n"),
        ('waiting on you now: nothing',
         "Now, if not done yet:\n"
         "- Reinstall three skills in Settings > Skills:"
         " interactive-exhibit,\n"
         "  earth-system-pipeline and provenance-discipline.\n"
         "- Replace the Project's instructions with"
         " PROJECT_INSTRUCTIONS.md\n"
         "  v3.79.\n"
         "- Look at the galactic tide on the phone: tick it and the Hills\n"
         "  torus, and turn the view until the tide shows an X tilted"
         " against\n"
         "  the torus.\n",
         "Now:\n"
         "- Nothing.\n"),
        ('next steps: the Galactic Plane',
         "2. The drawer's small fixes: the info panel's bullet lists,"
         " the 1.1",
         "2. *A Galactic Plane toggle in the Sun room, your idea:* a"
         " faint ring\n"
         "   in the galaxy's plane and the galaxy's pole axis, so the"
         " tide's\n"
         "   tilt and its X can be seen at a glance. You look for the X"
         " then.\n"
         "3. The drawer's small fixes: the info panel's bullet lists,"
         " the 1.1"),
        ('next steps: Home and the lobby card into step 3',
         "3. What Home should do, settled in conversation, then built.",
         "   Then Home as you settled it on October 3, and the lobby's"
         " new\n"
         "   Solar System card."),
        ('changed this session: Home and the lobby',
         "> - The sources for the Sun's distance cards are read, and you"
         " ruled on\n"
         ">   how to show the ones given as a range.\n",
         "> - The sources for the Sun's distance cards are read, and you"
         " ruled on\n"
         ">   how to show the ones given as a range.\n"
         "> - From your phone afterwards: the Galactic Plane toggle's"
         " words,\n"
         ">   what Home does, and the lobby's new Solar System card.\n"),
        ('road 4: Home settled',
         "              body's own room. Built and on the website; what"
         " Home\n"
         "              does is still to settle.\n",
         "              body's own room. Built and on the website. Home"
         " was\n"
         "              settled on October 3; it is built next.\n"),
        ('road 6: the card chosen',
         "              card in the lobby. A bare interactive.html link"
         " opens\n",
         "              card in the lobby, full width with a picture of"
         " the\n"
         "              room, and first behind the Solar System door"
         " too.\n"
         "              << new this session: its look chosen on October"
         " 3.\n"
         "              A bare interactive.html link opens\n"),
        ('design talk: Home settled',
         "- *Home.* Home names the last body ticked but frames everything"
         " drawn,\n"
         "  so falling back only changes the name on the drawer's handle."
         " Your\n"
         "  idea: a second Home tap returns to the opening view.\n",
         ""),
        ('do next: the toggle too',
         "> - *Build the Sun's distance cards so every number prints at"
         " its\n"
         ">   source's figures.*\n",
         "> - *Build the Sun's distance cards so every number prints at"
         " its\n"
         ">   source's figures.*\n"
         "> - *Then the Galactic Plane toggle you asked for.*\n"),
    ],
}


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
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. Either\n"
                "       patch_L371_session_close and its maintenance run\n"
                "       have not run yet, or this patch -- or the older\n"
                "       a patch_L408 it replaces -- has\n"
                "       already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
            if text.count(old) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(old)))
            text = text.replace(old, new)
            done.append(label)
        if any(ord(ch) > 127 for ch in text):
            raise SystemExit("ERROR: %s would hold non-ASCII text. NOTHING "
                             "was written." % path)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-40s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). It adds")
    print("     L-408 to the ledger's index. Expect 20 of 20.")
    print("  2. Move this script into documentation/; commit and push --")
    print("     in the same commit as the closing patch is fine. Delete")
    print("     the two older patch_L408 files unrun.")


if __name__ == "__main__":
    main()
