#!/usr/bin/env python3
"""
patch_L363_ledger_tony_notes_20261001.py -- ORRERY repo. Records Tony's
notes on Where We Are of 2026-10-01.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L363_ledger_tony_notes_20261001.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 7a47269c09acd4d2f875f6c8d49070659c4c2ee9
at https://github.com/tonylquintanilla/palomas_orrery
(gallery c48f9a92e6d6094a8d25ae9413a94c17503ee50c
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

WHAT IT DOES.

  LEDGER_CONSOLIDATED.md
      - header stamp;
      - L-363: the lobby stays the website's front page; the Solar
        System room becomes the top featured card; the orbit marker's
        words stay as they are;
      - L-389: which radius the atmosphere is measured from is decided
        by the provenance skill, not by Tony;
      - L-396: the goal line, reworded and confirmed; skill 1.13
        confirmed loaded;
      - L-398: Tony's question about JPL's precision, and the answer;
      - L-400: done -- the stray folder is deleted, and why it happens.
  documentation/WHERE_WE_ARE.md
      rewritten for this session. Your annotated copy, or the copy in
      the repo, may be there; either is replaced. Any other content
      makes the patch refuse.

No code, no skill changes, no handoff. Everything is written or
nothing is.

AFTER IT RUNS:
  1. python orrery_maintenance_run.py -- it rebuilds the ledger index
     and moves L-400 into the closed section.
  2. Move this script into documentation/.
  3. Commit and push.

SUCCESS looks like: one "ok" line per edit and per file, then "patch
applied". FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 1, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_FP = "cce02d34f1f53bcc9fa7cd7bb46e4ab3"
INDEX = ("<!-- INDEX:START", "<!-- INDEX:END -->")
PAGE = "documentation/WHERE_WE_ARE.md"
PAGE_FPS = ("1fe58ae7dbc0a2e1aa021d4c9b42fb28",   # the repo's copy at 7a47269c
            "3781a0bdbf5d29616f5293a067b8a336")   # Tony's annotated copy

EDITS = [
    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     "Module updated: October 1, 2026 with Anthropic's Claude Opus 5.5\n"
     "(Tony's notes on Where We Are: L-363 front door and orbit marker,\n"
     "L-389, L-396 goal line, L-398; L-400 done), built on 7a47269c.\n"
     "Review and RICE update Tony 6-21-2026\n"),

    ("L-400 done",
     "<!-- L:400 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n",
     "<!-- L:400 status:DONE upd:2026-10-01 section:A flag: rice: -->\n"),
    ("L-400 body",
     "- Tony-action (do): look inside, then delete it.\n"
     "**Gap:** the deletion.\n",
     "- **Done 2026-10-01.** Tony deleted it.\n"
     "- **Why it happens** (Tony asked). Most likely OneDrive. The cache\n"
     "  builder swaps folders by renaming them. If OneDrive is still\n"
     "  syncing the old folder at that moment, it cannot follow the\n"
     "  rename, so it keeps both and names the second copy\n"
     "  \"solar-system (1)\". Pausing OneDrive before the build, as the\n"
     "  Daily Run asks, prevents it. This copy probably came from a run\n"
     "  made while OneDrive was still syncing. The class is L-216's.\n"
     "- No loose ends.\n"),

    ("L-398 Tony note",
     "<!-- L:398 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n",
     "<!-- L:398 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n"
     "**Tony:** (on Where We Are, 2026-10-01, beside \"with only the\n"
     "figures its accuracy earns\") \"confirm that this is consistent with\n"
     "JPL precision\"\n"
     "**Claude:** Not yet. Today the figures reflect only how closely the\n"
     "page matches Horizons. This item's build is what makes them\n"
     "consistent with JPL's own accuracy.\n"),

    ("L-396 goal line and 1.13",
     "**Gap:** the next session confirms 1.13 is loaded; then the check "
     "above, or a ruling that the skill rule is enough.\n",
     "- **1.13 confirmed loaded** by the session of 2026-09-30 to 10-01 and\n"
     "  again on 2026-10-01. The obligation is discharged.\n"
     "- **The goal line, 2026-10-01.** Tony, beside the page's goal stage\n"
     "  \"The orrery's own Python runs in the browser\": \"this is not\n"
     "  clear. One major hurdle is that Horizons cannot be called on\n"
     "  demand by a user.\" Reworded, and confirmed as recommended: \"The\n"
     "  website does what the desktop orrery does, in the browser, from\n"
     "  data fetched from JPL each night, so a visitor never waits on\n"
     "  JPL.\" It is the plain form of the master plan's end goal (Section\n"
     "  5a: the Python orrery running in the browser under Pyodide). A\n"
     "  visitor's browser cannot call Horizons; the nightly cache builder\n"
     "  fetches, and the browser does the orrery's arithmetic on the saved\n"
     "  data. The real limit is time: the browser can show only the dates\n"
     "  the saved data covers.\n"
     "**Gap:** the check above, or a ruling that the skill rule is enough.\n"),
    ("L-396 date",
     "<!-- L:396 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n",
     "<!-- L:396 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n"),

    ("L-389 decide struck",
     "- **Tony-action (decide):** leave the altitudes on the equatorial\n"
     "  radius, or measure them from the mean radius as the crust now is.\n"
     "  Not on the critical path; recorded so it is not rediscovered.\n"
     "**Gap:** the decision above.\n",
     "- **No longer a Tony decision (2026-10-01).** Which radius the\n"
     "  altitudes are measured from is a sourcing question, so the\n"
     "  provenance skill's rules decide it when this item is worked\n"
     "  (Method Belongs to the Skill). Not on the critical path; recorded\n"
     "  so it is not rediscovered.\n"
     "**Gap:** worked by provenance-discipline's rules when the two\n"
     "atmosphere rows are next opened.\n"),
    ("L-389 Tony note",
     "<!-- L:389 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n",
     "<!-- L:389 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n"
     "**Tony:** (on Where We Are, 2026-10-01) \"i don't recall this note.\n"
     "the sourcing should follow our skill.\"\n"
     "**Claude:** The note below is Tony's annotation on the page of\n"
     "2026-09-30, quoted as written.\n"),

    ("L-363 front door and orbit marker",
     "<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n",
     "<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n"
     "**Tony:** (on Where We Are, 2026-10-01, beside \"The Solar System\n"
     "room becomes the front door\") \"it is an alternate front door. the\n"
     "front page or lobby is the same. we will switch this room to be the\n"
     "top featured card. we may want to highlight it in some other way\n"
     "too.\" Beside \"The front door becomes the page the website opens\n"
     "on\": \"to be determined; see above.\"\n"
     "**Tony:** (same page, on the orbit crosses) \"the new solar system\n"
     "interactive hover text has the name of the planet and its distance.\n"
     "this is okay. do not change. there is no cross. the hover text\n"
     "opens when clicking the body. are you adding a cross with the orbit\n"
     "name?\"\n"
     "- **The front door, 2026-10-01.** The lobby (index.html) stays the\n"
     "  website's front page. The room's card becomes the top featured\n"
     "  card in the lobby, and may be highlighted in some other way too.\n"
     "  Where We Are had described the master plan's \"swap\" as making the\n"
     "  room \"the page the website opens on\". The plan meant something\n"
     "  narrower: the page `interactive.html` opens when no room is named,\n"
     "  in place of the Explorer. Whether that bare link also switches is\n"
     "  open (Tony: \"to be determined\"). The plan's summary and Section\n"
     "  5a take this ruling at its next restamp.\n"
     "- **The orbit marker, 2026-10-01.** No cross was added. The\n"
     "  assembler has always drawn one tiny info marker on each orbit, by\n"
     "  the orrery's one-info-marker convention: size 3, in the orbit's\n"
     "  own colour, practically invisible. Step 3a changed only its words,\n"
     "  to \"Mercury's orbit\" and so on. Those words stay; the body's own\n"
     "  text box stays as it is. The optional rewording is struck.\n"),
]

PAGE_TEXT = '<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->\n# Where We Are\n\nLast updated: October 1, 2026, afternoon\n- Written at orrery 7a47269c plus this session\'s patch, and gallery\n  c48f9a92.\n\n> **READ THIS FIRST**\n>\n> **Changed this session:**\n> - Your notes on this page are recorded in the ledger.\n> - The lobby stays the website\'s front page. The Solar System room\'s\n>   card becomes the top featured card there.\n> - The goal now says what the website really does: the orrery\'s work\n>   in a browser, from data fetched from JPL each night.\n> - The stray "solar-system (1)" folder is gone. It was most likely a\n>   OneDrive copy.\n> - Earth\'s atmosphere is off your list. Its sourcing follows the skill.\n> - The orbit markers keep their words. Nothing in the room changes.\n>\n> **Do next:**\n> - *Claude adds JPL\'s own accuracy to the distance figures, so Pluto,\n>   Uranus and Neptune stop showing more figures than JPL knows.*\n>\n> **Needs you now:**\n> - *Run this session\'s patch in the orrery folder, then the\n>   maintenance run, then commit and push.*\n\nHow to read the marks:\n- *Italic* lines are the must-reads.\n- **>> UPDATED THIS SESSION** beside a heading means that section\n  changed in the latest session.\n- "<< reworded this session" or "<< new this session" beside a road\n  stage means that stage changed.\n- Sections without a mark are as they were.\n- The marks are cleared and reset at every session\'s update, so they\n  always mean "new since you last read this."\n\n## The goal  **>> UPDATED THIS SESSION**\n\n- Paloma\'s Orrery on the web.\n- The website does what the desktop orrery does, in the browser, from\n  data fetched from JPL each night, so a visitor never waits on JPL.\n- Anyone can open it, with nothing to install.\n- Built from the same code and the same checked numbers as the desktop\n  orrery.\n- The one real limit: the browser can show only the dates the saved\n  data covers.\n\n## The road  **>> UPDATED THIS SESSION**\n\n  1. [done]   The Sun\'s room is live on the website.\n  2. [done]   Earth\'s room is live, with every number traced to its source.\n  3. [done]   The numbers come from one place: the orrery feeds the\n              website, and nothing is typed twice.\n  4. [NOW]    *The Solar System room becomes a second way in: all the\n              planets, a drawer to pick them, and a way into each\n              body\'s own room.*  << reworded this session\n  5. [next]   The Sun\'s numbers get the same checking Earth\'s got.\n  6. [next]   The Solar System room\'s card becomes the top featured\n              card in the lobby. The lobby stays the front page.\n              << new this session\n  7. [later]  The rest of the orrery\'s objects come to the website --\n              dwarf planets, asteroids, moons -- from the orrery\'s own\n              object list, checked against JPL Horizons.\n  8. [later]  Encounters: comets and spacecraft shown at the dates\n              that matter.\n  9. [later]  The planets get their details -- layers, rings, magnetic\n              fields -- Jupiter and Saturn first.\n 10. [goal]   The website does what the desktop orrery does, from data\n              fetched from JPL each night.  << reworded this session\n\n## Right now\n\n- The Solar System room shows the Sun, all eight planets, Pluto and\n  the asteroid Apophis, where they are when you open it.\n- It opens on the Sun and Earth, with Earth\'s row highlighted.\n- The drawer lists every body in order outward from the Sun.\n- Each text box gives the body\'s distance in AU and in km, written out.\n- Still to fix: Pluto, Uranus and Neptune show more figures than JPL\n  actually knows.\n- The drawer\'s new behaviours have not been built yet.\n\n## The next three steps\n\n1. *The distance figures get JPL\'s own accuracy.*\n   - Claude writes two patches: three accuracy rows for the orrery,\n     taken from JPL\'s own report, and the website change that uses\n     them.\n   - You run both.\n2. Each body gets its NASA description and link, taken from the\n   orrery\'s own object list.\n   - Pluto\'s row links to NASA\'s Pluto page.\n3. The drawer\'s new behaviours are built.\n   - "See more", "Enter the Sun room", tapping a body to find its row,\n     and Home remembering what you ticked.\n   - You check them on your phone and desktop.\n\n## Waiting on you  **>> UPDATED THIS SESSION**\n\nNow:\n- *Run this session\'s patch in the orrery folder, then the maintenance\n  run, then commit and push.*\n\nAt the next design talk:\n- Nothing is waiting.\n\nNot urgent:\n- Whether a bare interactive.html link should open the Solar System\n  room instead of the Explorer.\n  - You said "to be determined".\n  - It comes up again after the Sun\'s numbers are done.\n\n## Where the details are\n\n- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n  - This session: L-363, L-389, L-396, L-398, L-400.\n- The reasoning behind the order:\n  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n- The latest session record:\n  `documentation/HANDOFF_L363_half2_step3a_20260930.md`\n'


def norm(raw):
    return raw.replace(b"\r\n", b"\n").decode("utf-8")


def ledger_fp(text):
    start, end = INDEX
    if start in text and end in text:
        a = text.index(start)
        b = text.index(end) + len(end)
        text = text[:a] + text[b:]
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def write(path, text, crlf):
    data = text.replace("\n", "\r\n") if crlf else text
    with open(path, "wb") as f:
        f.write(data.encode("utf-8"))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")

    with open(LEDGER, "rb") as f:
        raw = f.read()
    crlf = b"\r\n" in raw
    text = norm(raw)
    fp = ledger_fp(text)
    if fp != LEDGER_FP:
        raise SystemExit("ERROR: %s is not the file this patch was built "
                         "against (fingerprint %s, expected %s). It has "
                         "changed since 7a47269c, or this patch has already "
                         "run. NOTHING was written." % (LEDGER, fp, LEDGER_FP))
    for label, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            raise SystemExit("ANCHOR FAIL: %s -- %s: expected 1 match, found "
                             "%d. NOTHING was written." % (LEDGER, label, n))
        text = text.replace(old, new)

    page_crlf = False
    if os.path.exists(PAGE):
        with open(PAGE, "rb") as f:
            praw = f.read()
        page_crlf = b"\r\n" in praw
        pfp = hashlib.md5(norm(praw).encode("utf-8")).hexdigest()
        if pfp not in PAGE_FPS:
            raise SystemExit("ERROR: %s holds content this patch does not "
                             "know (fingerprint %s). NOTHING was written."
                             % (PAGE, pfp))

    write(LEDGER, text, crlf)
    for label, _old, _new in EDITS:
        print("ok  %s  %s" % (LEDGER, label))
    write(PAGE, PAGE_TEXT, page_crlf)
    print("ok  %s  rewritten" % PAGE)
    print("")
    print("Stamps updated: the ledger's header line; Where We Are's date.")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py  (rebuilds the ledger index,")
    print("     and moves L-400 into the closed section)")
    print("  2. Move this script into documentation/.")
    print("  3. Commit and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
