"""
patch_L060_5_session_close_20261118.py -- closes the coordinating session
of Nov 16 to 18 (L-060, El Nino): the reel, the night's flag confirmed,
step 5's wording and the ocean heat page as design-talk items.

Built on orrery a84394e at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 20e13fd1 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read
Nov 18, 2026, 08:40 Chicago. Written by the coordinating session (Claude
Opus 5.5) under safe-file-editing 1.14 and ledger-and-session-records 1.23.

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md
      L-060 (El Nino): a dated note (the reel, the night of Nov 17, the
        step 5 wording in Tony's words); the Gap of Nov 17 marked
        superseded and a new Gap; its date stamp.
      L-531 (the Earth Science room): the ocean heat page as an idea, in
        Tony's words; its date stamp.
      Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md, by section, above the run-record
      marker only: the header; the box; one Settled line (the reel);
      two design-talk lines; two Deferred entries joined onto one line
      each (same words), to stay within 130 lines; the marks.

    Each edit is checked at the text it replaces; your notes elsewhere
    are left alone. Nothing is written unless every edit finds its text.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L060_5_session_close_20261118.py)

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


NOTE = (
    "- **2026-11-17 and 18, THE REEL, AND STEP 5 AGAIN** (the coordinating\n"
    "  session, Claude Opus 5.5, from Tony's phone).\n"
    "  - The reel: Tony, 14:26, \"you do the initial reel and then give it\n"
    "    to Muse to resize and filter and post\"; 14:29, \"No music and\n"
    "    only the Boost filter if we need it.\" The session built it from\n"
    "    the live page (gallery 20e13fd1): seven cards in the page's look,\n"
    "    1080 x 1920, every sentence, chart caption and source name checked\n"
    "    word for word against the page by the build, which stops on any\n"
    "    that is not there. Tony's readings: 21:41, the map full width (La\n"
    "    Nina's panel dropped, its key kept); 21:53 and 21:58, the intro\n"
    "    card the title alone in the body font, steps 2 and 4 without\n"
    "    their first sentence, step 5's second paragraph fading in. Draft\n"
    "    3, 63 seconds, posted through Muse, 23:10, with a caption whose\n"
    "    every figure is on the page; #ClimateCrisis and #GlobalWarming\n"
    "    left out, as the page leaves the question open. The card builder\n"
    "    was not kept; the method is above.\n"
    "  - The night of Nov 17 (95f9f7c) carried no EL NINO DUE in its\n"
    "    title: the fix of f8a1229 holds.\n"
    "  - STEP 5'S LAST SENTENCE, for a design talk. Tony, 22:52: \"the\n"
    "    distinction between the slosh and the heating is hard to grasp.\n"
    "    The heating is what people see not the slosh.\" 23:12: \"Most\n"
    "    people think of enso as a heating even more than as an\n"
    "    oscillation.\" 23:19: \"in today's political environment the hedge\n"
    "    can read as ideological not just scientific\". Claude's proposal,\n"
    "    not ruled: name NOAA as the source of the open question, and say\n"
    "    it is the swing on NOAA's index that is being studied, each half\n"
    "    re-read against NOAA Climate.gov, Has climate change already\n"
    "    affected ENSO? (2023), before it goes in.\n"
    "  - Tony, Nov 18, 08:22: \"Our last slide also suggests an overturning\n"
    "    not just an oscillation. And a heat sink.\" 08:24: \"That may be a\n"
    "    separate page.\" Recorded on L-531 (the Earth Science room).\n"
)

NEW_GAP = (
    "**Gap (replaces the one above, 2026-11-18):** step 5's last sentence at\n"
    "a design talk. Each month, when the night's title starts EL NINO DUE\n"
    "(NOAA's next update is expected 10 December 2026), Tony rebuilds the\n"
    "page from the dashboard, reads it on his phone, and pushes. Then\n"
    "ESCAPADE's path (L-533).\n"
)

REF060 = ("**Ref:** ENSO_chart_spec.md v2 (design spec, this session); "
          "cross-ref L-001")

IDEA531 = (
    "- **An idea, Tony, 2026-11-18** (on El Nino's step 5, which draws La\n"
    "  Nina storing heat at depth and El Nino releasing it): \"Our last\n"
    "  slide also suggests an overturning not just an oscillation. And a\n"
    "  heat sink.\" 08:24: \"That may be a separate page.\" A page on where\n"
    "  the planet's extra heat goes, the ocean as the sink, El Nino's\n"
    "  breathing in and out one of its steps; the energy imbalance card\n"
    "  (energy_imbalance.py), which El Nino's step 5 links to, is its\n"
    "  nearest relative. For this room's design talk; not designed.\n"
)

GAP531 = "**Gap:** a design talk after Mars and the rest of the moons.\n"

LEDGER_TEXT_EDITS = [
    ("L-060: the Gap of Nov 17 marked superseded",
     "**Gap (replaces the one above, 2026-11-17, close):** Tony's Mode 5\n",
     "**Gap (superseded below, 2026-11-17, close):** Tony's Mode 5\n"),
    ("L-060: the note and new Gap", REF060, NOTE + NEW_GAP + REF060),
    ("L-060: date stamp",
     "<!-- L:060 status:OPEN upd:2026-11-17 ",
     "<!-- L:060 status:OPEN upd:2026-11-18 "),
    ("L-531: the idea", GAP531, IDEA531 + GAP531),
    ("L-531: date stamp",
     "<!-- L:531 status:OPEN upd:2026-11-13 ",
     "<!-- L:531 status:OPEN upd:2026-11-18 "),
]

PAGE_TEXT_EDITS = [
    ("header: date",
     "Last updated: November 17, 2026: El Nino's page live, and the night's flag fixed (coordinating session, Opus).\n",
     "Last updated: November 18, 2026: El Nino's reel posted; the coordinating session of Nov 16 to 18 closed (Opus).\n"),
    ("header: SHAs",
     "- Written at orrery f8a12290 and gallery 20e13fd1, with this patch's edits on your disk.\n",
     "- Written at orrery a84394e and gallery 20e13fd1, with this patch's edits on your disk.\n"),
    ("box: the page",
     "> - El Nino's page is live: the lobby's Featured card opens it, and the dashboard's Earth System group rebuilds it (L-060 (El Nino)).\n",
     "> - El Nino's reel is on Instagram: made from the page's own words and pictures, every sentence checked against the page; Muse only posted it. The page is live in the lobby's Featured (L-060 (El Nino)).\n"),
    ("box: the night",
     "> - The night's \"EL NINO DUE\" title is fixed: it is read from the El Nino check's own row only. The night of Nov 17 said it by mistake; its row said CURRENT.\n",
     "> - The night of Nov 17 had no \"EL NINO DUE\" in its title: the fix holds. It will say it when NOAA updates, expected 10 December.\n"),
    ("box: needs you now",
     "> - *(do) Your phone look at the live El Nino page (the list in today's chat). Tomorrow, the orrery's night title should not start with \"EL NINO DUE\"; if it does, tell the next session.*\n",
     "> - *(do) When the orrery's night title starts \"EL NINO DUE\": rebuild El Nino's page from the dashboard's Earth System group, read it on your phone, then push both.*\n"),
    ("Settled: the reel",
     "Standing rulings; a line leaves once it is habit, or a skill carries it.\n",
     "Standing rulings; a line leaves once it is habit, or a skill carries it.\n"
     "- A page's reel is made by the session from the page's own words and pictures, each sentence checked against the page; Muse adds only the Boost filter if needed, no music, and posts (Nov 17; L-060 (El Nino)).\n"),
    ("marks: Settled", "## Settled\n", "## Settled  **>> UPDATED THIS SESSION**\n"),
    ("Deferred: Charon on one line",
     "- Charon's period is asked around Pluto's centre, not the barycentre;\n"
     "  fix it before Pluto's room (L-150 (trusting a near-equal pair), Nov 6).\n",
     "- Charon's period is asked around Pluto's centre, not the barycentre; fix it before Pluto's room (L-150 (trusting a near-equal pair), Nov 6).\n"),
    ("Deferred: the symbols on one line",
     "- When the road turned to the symbols (Nov 5): L-512 (fallbacks when\n"
     "  JPL cannot answer) slices b and c; L-484 (the two agree), its brief\n"
     "  and build; L-504 (the orrery's clock), the Earth System, stamps and\n"
     "  tools; L-510 part 2, the path plan asked from before any launch.\n",
     "- When the road turned to the symbols (Nov 5): L-512 (fallbacks when JPL cannot answer) slices b and c; L-484 (the two agree), its brief and build; L-504 (the orrery's clock), the Earth System, stamps and tools; L-510 part 2, the path plan asked from before any launch.\n"),
    ("design talk: two items",
     "At the next design talk:\n",
     "At the next design talk:\n"
     "- El Nino's step 5, its last sentence: name NOAA as the source of the open question, and say it is the swing on NOAA's index that is studied. Your words: \"in today's political environment the hedge can read as ideological not just scientific\" (Nov 17; L-060 (El Nino)).\n"
     "- A page on where the planet's extra heat goes, the ocean as a heat sink, El Nino's breathing in and out one step. Your words: \"That may be a separate page\" (Nov 18; L-531 (the Earth Science room)).\n"),
    ("marks: Waiting on you", "## Waiting on you\n", "## Waiting on you  **>> UPDATED THIS SESSION**\n"),
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
