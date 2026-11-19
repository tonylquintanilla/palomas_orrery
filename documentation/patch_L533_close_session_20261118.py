"""
patch_L533_close_session_20261118.py -- closes the coordinating session
of Nov 18 (L-533, ESCAPADE's path): the build live and looked at, Tony's
withdrawal of the Moons group, the Lagrange points as the next round, his
two misses from the phone look carried to the design talk, and the skills
page that moved.

Built on orrery 342d2bc4bb8cff10e0be5d45b7d5ea51c291323e at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 133dbd21930d39b66283b820ce71bc705a640855 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read
Nov 18, 2026, 18:05 Chicago. Written by the coordinating session (Claude
Opus 5.5) under safe-file-editing 1.14 and ledger-and-session-records 1.23.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\,
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md
      L-533 (ESCAPADE): its title; a dated note (live, your phone look,
        the overlapping names, the box's last day, the session's size);
        a new Gap in place of the one the Code session wrote.
      L-534 (missions by destination): a dated note (the Moons group
        withdrawn, the destination in the box, the order); a new Gap;
        its date stamp.
      L-529 (guided encounters): a dated note (each event's date in the
        box); a new Gap; its date stamp.
      L-297 (the Lagrange points): a dated note (next, and its two
        riders); a new Gap; its date stamp.
      L-537 (the skills page moved), new.
      Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md, by section, above the run-record
      marker only: the header; the box; road stage 15; Settled (two
      lines in, the loiter's line out, as the skill now carries it);
      Deferred (L-529's line out, as the design-talk list has it; the
      loops near L2 in; L-489 on one line, same words); the design-talk
      line; Signals; the
      marks. It stays within 130 lines.

    Each edit is checked at the text it replaces; your notes elsewhere
    are left alone. Nothing is written unless every edit finds its text.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L533_close_session_20261118.py)

    Success: "ok" lines, then "patch applied". Failure: one ERROR or
    ANCHOR FAIL line, and nothing is written.

Written November 18, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"


def b(s):
    return s.encode("ascii")


# ---------------------------------------------------------------- L-533

TITLE533_OLD = ("#### [L-533] ESCAPADE, Blue and Gold, on their way to Mars "
                "(orrery + gallery; recorded, after the Mars build)\n")
TITLE533_NEW = ("#### [L-533] ESCAPADE, Blue and Gold, on their way to Mars "
                "(orrery + gallery; path live Nov 18, the row under Mars "
                "waits for L-534)\n")

GAP533_OLD = (
    "**Gap:** the orrery pushed, then the website's Daily Run green, then\n"
    "the website pushed, the same evening and\n"
    "not while a night runs; his phone look (both ticked from Spacecraft,\n"
    "their boxes, the flyby and the loiter seen with Go To Earth and Earth's\n"
    "frame zoom). The row under Mars (L-534) and the encounters (L-529)\n"
    "untouched; L2 drawn at L-297. One later item: a Mars arrival counts as\n"
    "an arrival only because JPL's data runs three days past orbit insertion.\n"
)

GAP533_NEW = (
    "- **2026-11-18, evening, LIVE AND LOOKED AT** (the coordinating\n"
    "  session, Claude Opus 5.5, through the python_work door).\n"
    "  - Pushed: the orrery at 342d2bc4; the website's build at deae684 and\n"
    "    its Daily Run at 133dbd21 (49 of 49 checks, the swap first time,\n"
    "    run 20261118T230303Z). horizons-orbital-mechanics 1.19 reinstalled\n"
    "    and v3.142 pasted into the Project's instructions, Tony's \"done\";\n"
    "    the next session's load confirms 1.19.\n"
    "  - Tony's phone look, 17:44 to 17:48, four pictures: both craft just\n"
    "    past Earth, where JPL has them; the boxes as approved. His words,\n"
    "    17:52: \"The only thing I miss are the dates of flybys. For example\n"
    "    it seems that the two craft are near earth right now. I assume this\n"
    "    can be shown with the encounters. We also don't say what the\n"
    "    destination or basic mission objective is.\" Carried: each event's\n"
    "    date to L-529, the destination and purpose to L-534. Accepted as\n"
    "    done, 17:58, \"Yes\", with those carried.\n"
    "  - THE TWO NAMES OVERLAP. The twins fly side by side, so their labels\n"
    "    print on each other (\"ESCAPADE-Gbld\" in his pictures), all the\n"
    "    way to Mars. Tony, 17:57: \"On the names overlap consider putting\n"
    "    one of the names on the opposite side of its symbol.\" It rides\n"
    "    L-297's round (17:58, \"Yes\"): a label side per body, which also\n"
    "    serves the Lagrange points beside Earth and the Moon. Every craft's\n"
    "    label is set \"top center\" in gallery/assembler/render_spacecraft.py\n"
    "    at 133dbd21.\n"
    "  - THE BOX'S LAST DAY STOPS SHORT OF THE PLAN. Gold's box: \"as far as\n"
    "    7 September 2027\", its plan's span to 2027-09-10; Blue's: \"10\n"
    "    September 2027\", its span to 2027-09-12 (data/objects_config.json\n"
    "    at 133dbd21). Cause not found; explained before anything is\n"
    "    changed, in the next website session (rides L-297).\n"
    "  - THE LOOPS ARE NOT VISIBLE ON THE WEBSITE. Tony's picture of 18:01,\n"
    "    zoomed on today's Earth (0.01 AU scale): the twins' outbound lines\n"
    "    and their lines of a year ago, no loops. A Sun-centred view spreads\n"
    "    the year near Earth along Earth's whole orbit (about 2.6 million km\n"
    "    a day), the flyby sits where Earth was ten days ago, and at the\n"
    "    Solar System's scale the loops are too small to see. The loops\n"
    "    show only in a view centred on Earth (the orrery's picture of\n"
    "    14:11); the website draws a planned path around the Sun alone\n"
    "    (L-476, Tony, 2026-11-03). Tony, 18:05, \"Yes\": the box's words\n"
    "    stay, as they state what the craft did, and the loops wait for an\n"
    "    Earth-centred path view, with Earth's fold (road stage 16: SOHO,\n"
    "    Gaia and JWST need it too). The coordinator's own run order had\n"
    "    asked for the loiter to be looked at with Go To Earth, which no\n"
    "    Sun-centred view can show.\n"
    "  - SESSION SIZE: the Code session reported its context at 525,685\n"
    "    tokens of 1,000,000 at its end, compacted once, no /cost figure.\n"
    "    The coordinator's suggestion, not ruled: a build across both\n"
    "    repositories gives the website half a session of its own.\n"
    "**Gap:** the row under Mars, by L-534's rule once it is designed. The\n"
    "label side and the box's last day ride L-297. The loops near L2, with\n"
    "an Earth-centred path view in Earth's fold. One later item: a Mars\n"
    "arrival counts as one only because JPL's data runs three days past\n"
    "orbit insertion; the plan's 30-day remake shows it if JPL trims that.\n"
)

# ---------------------------------------------------------------- L-534

GAP534_OLD = (
    "**Gap:** the design round, with L-529 (guided encounters), after\n"
    "ESCAPADE's path (L-533) and the Lagrange points (L-297).\n"
)

GAP534_NEW = (
    "- **2026-11-18, the coordinating session** (Claude Opus 5.5, through\n"
    "  the python_work door, on orrery 0d2b5eb to 342d2bc4).\n"
    "  - THE MOONS GROUP WITHDRAWN. Tony, 10:08: \"On note, I withdraw the\n"
    "    moons group idea, moons should be placed with the shells by\n"
    "    distance like earths moon.\" So a planet's fold lists its moons\n"
    "    among its shells by distance, as Earth's Moon is, and the round\n"
    "    designs the Missions rows only. The coordinator's question above\n"
    "    (Moons in this round or sooner) goes with it.\n"
    "  - THE DESTINATION IN THE BOX. From ESCAPADE's phone look, 17:52: \"We\n"
    "    also don't say what the destination or basic mission objective\n"
    "    is.\" The box names neither; the i panel has the purpose. ESCAPADE\n"
    "    is the worked example: a line read from the plan's arrival event,\n"
    "    such as the day it arrives at Mars.\n"
    "  - A LAGRANGE POINT AS A DESTINATION. JWST, Gaia and SOHO (road stage\n"
    "    16) sit at L1 or L2 for their whole missions, so the rule meets a\n"
    "    destination that is a point, not a body (L-297), and the loiter\n"
    "    rule (L-533) would read each mission as one long loiter.\n"
    "  - THE ORDER. Tony, 13:31: \"Keep as planned after escapade\": the\n"
    "    Lagrange points' round first, then this one.\n"
    "**Gap:** the design round, with L-529 (guided encounters), after the\n"
    "Lagrange points (L-297); ESCAPADE (L-533) the worked example.\n"
)

# ---------------------------------------------------------------- L-529

GAP529_OLD = (
    "**Gap:** one design round with L-534, after ESCAPADE's path (L-533) and\n"
    "the Lagrange points (L-297), by the road's order; then which encounter\n"
    "first.\n"
)

GAP529_NEW = (
    "- **2026-11-18, from ESCAPADE's phone look** (the coordinating session,\n"
    "  Claude Opus 5.5). Tony, 17:52: \"The only thing I miss are the dates\n"
    "  of flybys. For example it seems that the two craft are near earth\n"
    "  right now. I assume this can be shown with the encounters.\" Each\n"
    "  flyby and arrival has its moment in the plan (`path.events`); the\n"
    "  box gives one only inside ESCAPADE's loiter sentence. ESCAPADE is\n"
    "  the worked example, and its loiter the new kind of event the round\n"
    "  reads (L-533).\n"
    "**Gap:** one design round with L-534, after the Lagrange points\n"
    "(L-297), by the road's order; then which encounter first.\n"
)

# ---------------------------------------------------------------- L-297

GAP297_OLD = (
    "**Gap:** the round of its own, after ESCAPADE's path (L-533): the orrery\n"
    "keys the ten in NASA's words; the website's builder gains the serving\n"
    "shape sized above; the ten drawn, re-sized as the Note says.\n"
)

GAP297_NEW = (
    "- **2026-11-18, NEXT** (the coordinating session, Claude Opus 5.5).\n"
    "  ESCAPADE's path went live without L2 drawn; its box names L2 in\n"
    "  words (L-533). Tony, 13:28: \"We should also add L2 as an object to\n"
    "  the website for this loiter and later uses\"; reminded of the ruling\n"
    "  of Nov 15 above, 13:31: \"Keep as planned after escapade\". So this\n"
    "  round is next, all ten together, before the design round (L-534,\n"
    "  L-529).\n"
    "  - TWO RIDERS from ESCAPADE, Tony's \"Yes\" of 17:58: a label side per\n"
    "    body (17:57, \"consider putting one of the names on the opposite\n"
    "    side of its symbol\"), for the twins and for the points beside\n"
    "    Earth and the Moon; and the box's last day, 2 or 3 days short of\n"
    "    the plan's span for each twin, explained before it is changed.\n"
    "  - A third, if this round bumps interactive-exhibit: the skills\n"
    "    page's new place (L-537).\n"
    "**Gap:** the round of its own, next: the orrery keys the ten in NASA's\n"
    "words; the website's builder gains the serving shape sized above; the\n"
    "ten drawn, re-sized as the Note says; the two riders above.\n"
)

# ---------------------------------------------------------------- L-537

L537 = (
    "#### [L-537] The skills page moved: Settings > Skills is now Plugins in the sidebar (records; carried to the next protocol or skill bump)\n"
    "<!-- L:537 status:OPEN upd:2026-11-18 section:A flag: rice: -->\n"
    "- **Found 2026-11-18, evening**, reinstalling horizons-orbital-mechanics\n"
    "  1.19, in the coordinating session (Claude Opus 5.5). Tony: \"where\n"
    "  has skills management gone?\" Anthropic's help pages, read that\n"
    "  evening: skills had moved from Settings to Customize > Skills, and\n"
    "  Customize is renamed Plugins in the sidebar, one Plugins page in\n"
    "  place of the separate Skills, Connectors and Plugins tabs\n"
    "  (support.claude.com, article 17740565, \"Manage plugins, skills and\n"
    "  connectors from one Plugins page\"). Tony found it and reinstalled;\n"
    "  17:30: \"i had to down vote this new buried method.\"\n"
    "- **Where the old words stand**, at orrery 342d2bc4:\n"
    "  PROJECT_INSTRUCTIONS.md five times (the Stale Skill gate among them)\n"
    "  and skills/interactive-exhibit/SKILL.md once. Each would send Tony\n"
    "  to a place that no longer exists. By the records skill's rule a\n"
    "  wrong instruction is corrected in the session that finds it; it is\n"
    "  carried instead, so as not to ask a second reinstall and protocol\n"
    "  paste of Tony the same night, and he knows the new place. Read the\n"
    "  help page again when correcting: the page was moving that week.\n"
    "**Gap:** the correction, at the next protocol version and at\n"
    "interactive-exhibit's next version (L-297's round, if it bumps it).\n"
    "**Ref:** ledger-and-session-records (a wrong sentence in a skill: bump\n"
    "now, or carry it); the protocol's Stale Skill = Stop.\n"
    "\n"
)

L529_HEAD = ("#### [L-529] Guided encounters: the guide's way of telling, "
             "used for a flyby (gallery; an idea, for a design talk after "
             "Mars)\n")

LEDGER_TEXT_EDITS = [
    ("L-533: title", TITLE533_OLD, TITLE533_NEW),
    ("L-533: the note and new Gap", GAP533_OLD, GAP533_NEW),
    ("L-534: the note and new Gap", GAP534_OLD, GAP534_NEW),
    ("L-534: date stamp",
     "<!-- L:534 status:OPEN upd:2026-11-15 ",
     "<!-- L:534 status:OPEN upd:2026-11-18 "),
    ("L-529: the note and new Gap", GAP529_OLD, GAP529_NEW),
    ("L-529: date stamp",
     "<!-- L:529 status:OPEN upd:2026-11-13 ",
     "<!-- L:529 status:OPEN upd:2026-11-18 "),
    ("L-297: the note and new Gap", GAP297_OLD, GAP297_NEW),
    ("L-297: date stamp",
     "<!-- L:297 status:OPEN upd:2026-11-15 ",
     "<!-- L:297 status:OPEN upd:2026-11-18 "),
    ("L-537: new item", L529_HEAD, L537 + L529_HEAD),
]

# ---------------------------------------------------------------- the page

PAGE_TEXT_EDITS = [
    ("header: date",
     "Last updated: November 18, 2026, evening: ESCAPADE's path built and its words approved, waiting on your pushes (Opus).\n",
     "Last updated: November 18, 2026, night: ESCAPADE's path live and looked at; the coordinating session of Nov 18 closed (Opus).\n"),
    ("header: SHAs",
     "- Written at orrery 00c89ef0 and gallery 1d3090bc, with this session's edits on your disk.\n",
     "- Written at orrery 342d2bc4 and gallery 133dbd21, with this patch's edits on your disk.\n"),
    ("box: changed, the twins",
     "> - ESCAPADE's twins are drawn by their plans: each a loiter near L2 to its flyby of Earth, the flyby, and its arrival at Mars, NASA's list; the plan's false June flyby and its passes of the Sun are gone (L-533 (ESCAPADE)).\n",
     "> - ESCAPADE's twins are live, on the website and in the orrery: each a year of loops near L2, its flyby of Earth (Blue Nov 7, Gold Nov 9), and its arrival at Mars next September, drawn from JPL by their plans (L-533 (ESCAPADE)).\n"),
    ("box: changed, the look",
     "> - The website half is built and tested in a copy: both craft in Spacecraft, the box naming L2 in words only, and a check that Blue's -9 is never read as Pluto's centre.\n",
     "> - Your phone look accepted it. Your two misses, each event's date and the destination in the box, go to the design talk; the overlapping names ride the Lagrange round.\n"),
    ("box: do next",
     "> **Do next:** *Push the orrery, run the website's Daily Run, push the website, the same evening; then your phone look (L-533 (ESCAPADE)). The words are approved.*\n",
     "> **Do next:** *The ten Lagrange points in one round (L-297 (the Lagrange points)), with a label side for ESCAPADE's twins; then the design talk on destinations and encounters.*\n"),
    ("road: stage 15",
     "               page (L-060 (El Nino)) live Nov 17; ESCAPADE's path (L-533)\n"
     "               built Nov 18, your look next; the Lagrange points (L-297), the\n",
     "               page (L-060 (El Nino)) live Nov 17; ESCAPADE's path (L-533)\n"
     "               live Nov 18; next, the Lagrange points (L-297), the\n"),
    ("Settled: two lines in, the loiter's out",
     "- A craft riding near a Lagrange point for 60 days or more is one event, a loiter, ending at its flyby; a pass inside it is a flyby only when the craft leaves within 15 days (Nov 18; L-533 (ESCAPADE); horizons-orbital-mechanics 1.19).\n",
     "- Moons sit with their planet's shells by distance, as Earth's Moon does; there is no Moons group (Nov 18; L-534 (missions by destination)).\n"
     "- ESCAPADE's words leave out NASA's \"kidney-bean\": it is the loop seen from a view that turns with Earth, and no room turns (Nov 18; L-533 (ESCAPADE)).\n"),
    ("Deferred: L-529's line out, the loops in",
     "- Guided encounters, the guide's way of telling used for a flyby: a design talk after Mars (Nov 12; L-529 (guided encounters)).\n",
     "- ESCAPADE's loops near L2 show only in a view centred on Earth, and the website draws a planned path around the Sun alone: with Earth's fold, where SOHO, Gaia and JWST need it too (Nov 18; L-533 (ESCAPADE)).\n"),
    ("Deferred: L-489 on one line",
     "- L-489 (compositions), with L-486 and L-488 under it: Artemis II in\n"
     "  the Earth room first, with slice 2 (L-507 (historical missions));\n"
     "  Apollo 11's S-IVB with them (Nov 5).\n",
     "- L-489 (compositions), with L-486 and L-488 under it: Artemis II in the Earth room first, with slice 2 (L-507 (historical missions)); Apollo 11's S-IVB with them (Nov 5).\n"),
    ("design talk: destinations and encounters",
     "- Missions by destination and encounters at every flyby and destination, one round, with your Moons group under a planet (Nov 15; L-534 (missions by destination), L-529 (guided encounters)).\n",
     "- Missions by destination and encounters at every flyby and destination, one round, after the Lagrange points, ESCAPADE the worked example. Your words of Nov 18: \"The only thing I miss are the dates of flybys\"; \"We also don't say what the destination or basic mission objective is\" (L-534 (missions by destination), L-529 (guided encounters)).\n"),
    ("Signals: the cache build",
     "- Last cache build: 20261118T171805Z, ok, no retry on the swap (your local gallery's swap log at 1d3090bc, read Nov 18).\n",
     "- Last cache build: 20261118T230303Z, ok, no retry on the swap (the website's swap log at 133dbd21, read Nov 18).\n"),
    ("Signals: Tier-1",
     "- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, run of 20261118T210633Z on orrery 00c89ef, read Nov 18).\n",
     "- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at orrery 342d2bc4, generated Nov 18, read Nov 18).\n"),
    ("marks: Waiting on you", "## Waiting on you\n",
     "## Waiting on you  **>> UPDATED THIS SESSION**\n"),
]


def plan(path, edits, top_only=False):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. Nothing "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""
    sentinel = b(edits[1][2] if path == LEDGER else edits[0][2])
    if top.count(sentinel) == 1:
        print("already there: %s" % path)
        return True, None
    for label, old, new in edits:
        n = top.count(b(old))
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(b(old), b(new))
        print("ok %s" % label)
    if any(c > 127 for _, _, new in edits for c in b(new)):
        print("ERROR: non-ASCII in this patch's text. Nothing was written.")
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker (%d). "
              "Nothing was written." % (path, top.count(b"\n")))
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, top + marker + bottom


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok, led = plan(LEDGER, LEDGER_TEXT_EDITS)
    if not ok:
        return 1
    ok, page = plan(PAGE, PAGE_TEXT_EDITS, top_only=True)
    if not ok:
        return 1
    if led is None and page is None:
        print("Nothing to do.")
        return 0
    if led is not None:
        with open(LEDGER, "wb") as f:
            f.write(led)
        print("ok %s written" % LEDGER)
    if page is not None:
        with open(PAGE, "wb") as f:
            f.write(page)
        print("ok %s written" % PAGE)
    if led is not None:
        print("Running ledger_index.py ...")
        r = subprocess.run([sys.executable, "ledger_index.py"],
                           capture_output=True, text=True)
        for line in (r.stdout + r.stderr).strip().splitlines()[-6:]:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: ledger_index.py exited %d. The edits above are "
                  "written; Discard Changes in GitHub Desktop undoes them. "
                  "Paste these lines to the session." % r.returncode)
            return 1
        print("ok ledger_index.py")
    print("patch applied")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): commit and push the ledger,")
    print("     Where We Are, this file and the next coordinator's prompt.")
    print("     Not while the night is running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
