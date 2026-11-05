"""
patch_L510_3_session_close_20261105.py -- records for the coordinating
session of Nov 4, night, to Nov 5, noon. Records only.

Built on orrery 620b9149 at https://github.com/tonylquintanilla/palomas_orrery
(branch main) and gallery e605f56 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 5, 2026, 12:25 Chicago. Written by the coordinating session
(Claude Opus 5.5), under ledger-and-session-records 1.22 and
safe-file-editing 1.14. Tony's run record for the session:
documentation/WHERE_WE_ARE_11-4-26_2321_run_record.md.

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md
      - L-510 (the typed fields stop deciding): a dated note -- the
        website follows the e rule (Tony, Nov 4, 23:47), the four red
        nights and the two website patches, the green night e605f56 --
        and a new Gap whose first step is the road's quick win: the
        objects mirror follows the rule by itself.
      - L-485 (a nightly run): a dated note -- the red nights, and the
        night refused because the orrery was pushed while it ran -- and
        a new Gap.
      - both items' date stamps to 2026-11-05.
      Then it runs ledger_index.py, which rebuilds the index rows.

    documentation/WHERE_WE_ARE.md, by section: the header, the box (the
    green night; do next is the quick wins), the road's stage 12 done
    and 13 now, and two Signals read from files (the swap log at
    gallery e605f56; the ledger's newest stamp, now Nov 5).

    Each edit is checked only at the text it replaces, so your notes
    elsewhere never stop it. A file that already holds the result is
    accepted and reported. Independent of patch_L508_1, which touches
    L-508 and L-509 only: the two run in either order.

RUN COMMAND

    Save this file in the orrery's root folder
    (palomas_orrery_for_github), open it in VS Code and click Run.
    (python patch_L510_3_session_close_20261105.py)

    Success: one "ok" line per edit, the index tool's own report, then
    "patch applied". Failure: one ERROR or ANCHOR FAIL line, and nothing
    is written. Undo is Discard Changes in GitHub Desktop.

    Then move this file into documentation\\, commit and push the
    orrery -- after the website's night has finished, not while it runs.

Written November 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"

LEDGER_EDITS = [
    ('L-510: the Nov 5 note and new Gap',
     b"**Gap (replaces the one below, 2026-11-04):** Tony's Mode 5 look\n(Sun-centred: Tsuchinshan, Wierzchos, ATLAS each drawn as 3I/ATLAS is;",
     b'- **2026-11-05: THE WEBSITE FOLLOWS THE RULE** (the coordinating\n  session of Nov 4, night, to Nov 5, Claude Opus 5.5; Tony\'s run record\n  `WHERE_WE_ARE_11-4-26_2321_run_record.md`). Part 1 moved piece C of\n  C/2025 K1 to an orbit (its database e below 1), and the orrery\'s\n  export stopped serving it a path. The website\'s nights then went red\n  four times:\n  - Nov 4, runs 10 and 11, and Nov 5\'s first manual run: the objects\n    mirror refused to delete piece C\'s `path` and `open_path`\n    ("a person decides"). Tony, Nov 4, 23:47 Chicago: "the website\n    should follow the same rule as the orrery, based on eccentricity."\n    `patch_L510_1_piece_c_orbit_website.py` (gallery e5352a86): piece\n    C\'s entry as Hale-Bopp\'s (availability analytic, frame\n    heliocentric, trace none), and the builder\'s offline test given a\n    stand-in orbit for it and its open-path count 14 -> 13, named.\n  - Nov 5, 14:54 UTC: the builder stopped on #T. An orbit body takes\n    its newest saved position as today\'s, and piece C\'s saved positions\n    ran to 2027-10-19 from its plan.\n    `patch_L510_2_orbit_body_drops_future_points.py` (gallery\n    721b7cc6): a body that is not a path keeps no saved position after\n    today; the drop is named in the log; the offline test plants one on\n    Hale-Bopp and was seen to fail without the fix (508 checks).\n  - Nov 5, 17:50 UTC: built and passed, refused at the end because the\n    orrery moved mid-run (L-485, below).\n  - Nov 5, 18:12 UTC: green, committed e605f56; the log read\n    "c2025_k1_c: drawn as an orbit, not a path; 2 saved position(s)\n    after today dropped, and its old plan\'s stamps". The scheduled run\n    after it went green too (Tony).\n  Not yet done: the objects mirror still refuses a deletion, so the\n  next comet that changes side stops a night at the pulls again.\n**Gap (replaces the one below, 2026-11-05):** the road\'s quick win: the\nobjects mirror follows the e rule by itself (removes `path` and\n`open_path` when the export stops serving them, and sets the entry\'s\navailability, frame and trace as for an orbit, or the reverse), with\nplanted cases both ways; then Tony\'s Mode 5 look below; then part 2\'s\nbrief and build (Deferred on Where We Are, Nov 5).\n**Gap (superseded above, 2026-11-05; replaced the one below, 2026-11-04):** Tony\'s Mode 5 look\n(Sun-centred: Tsuchinshan, Wierzchos, ATLAS each drawn as 3I/ATLAS is;'),
    ('L-510: date stamp',
     b'<!-- L:510 status:OPEN upd:2026-11-04 section:A flag: rice: -->',
     b'<!-- L:510 status:OPEN upd:2026-11-05 section:A flag: rice: -->'),
    ('L-485: the Nov 5 note and new Gap',
     b'**Gap (replaces the one below, 2026-11-02, evening):** the morning looks for the\nrest of the week (P4),',
     b'- **2026-11-05, from the coordinating session of Nov 4 to 5** (Claude\n  Opus 5.5): the website\'s night was red on Nov 4 (runs 10 and 11) and\n  twice on Nov 5, and served Nov 3\'s cache meanwhile; the hold held\n  every time and nothing wrong was served. Causes and fixes on L-510\n  (the typed fields stop deciding). One cause is the night\'s own: a\n  manual run at 17:50 UTC read the orrery at 59ddb645, Tony pushed\n  620b9149 at 11:52 Chicago while it ran, and the night pass read the\n  newer commit and refused to save ("the pulled orrery commit moved\n  after the build"). Correct and safe; the habit it asks for is to let\n  the website\'s night finish before pushing the orrery. The orrery\'s\n  own night ran green twice on Nov 5 (711e0ea, 59ddb645).\n**Gap (replaces the one below, 2026-11-05):** the morning looks (P4), each\nstart time noted on both Actions tabs; a night stopped by a push\nmid-run is run again by hand; then the hold\'s website half (a gallery\nsession), with L-508\'s alarm on the night\'s side.\n**Gap (superseded above, 2026-11-05; replaced the one below, 2026-11-02, evening):** the morning looks for the\nrest of the week (P4),'),
    ('L-485: date stamp',
     b'<!-- L:485 status:OPEN upd:2026-11-01 section:A flag: rice: -->',
     b'<!-- L:485 status:OPEN upd:2026-11-05 section:A flag: rice: -->'),
]

PAGE_EDITS = [
    ("the page's header",
     b"Last updated: November 5, 2026, morning: the coordinating session (Opus) that read the website's red nights and turned the road to the symbols.\n- Written at orrery 59ddb645 and gallery e5352a86, read live.\n",
     b"Last updated: November 5, 2026, noon: the coordinating session (Opus) closed; the website's night green again.\n- Written at orrery 620b9149 and gallery e605f56, read live.\n"),
    ("the page's box",
     b"> - The road turns to the symbols, with the moons sooner.\n>\n> **Do next:** *run patch_L510_2 in the website folder, commit, push,\n> and run the website's night from the Actions tab; look for a green\n> NIGHT RUN line.*\n",
     b"> - The road turns to the symbols, with the moons sooner.\n> - The website's night went green on Nov 5 (e605f56), piece C an orbit.\n>\n> **Do next:** *the quick wins, starting with the copying tool\n> following the e rule by itself (stage 13).*\n"),
    ("the road's stage 12",
     b' 12.   [NOW]   *A green website night: patch_L510_2, then the night.* << new this session\n 13.   [next]  Quick wins:',
     b' 12.   [done]  A green website night, Nov 5 (e605f56). << moved this session\n 13.   [NOW]   *Quick wins:*'),
    ('Signals: the cache build',
     b"- Last cache build: 20261103T193343Z, ok, no retry (swap log at gallery\n  e5352a86); the website's nights of Nov 4 and 5 stopped before a swap.\n",
     b'- Last cache build: 20261105T181207Z, ok, no retry (swap log at gallery\n  e605f56).\n'),
    ('Signals: the page and the ledger',
     b"- Page Nov 5, ledger's newest stamp Nov 4: today's ledger lines come at the close.\n",
     b"- This page's date and the ledger's newest stamp: both Nov 5. Agree.\n"),
]


def plan(path, edits, top_only=False):
    if not os.path.isfile(path):
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
    if all(top.count(new) == 1 for _, _, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(old, new)
        print("ok %s" % label)
    out = top + marker + bottom
    if any(c > 127 for c in out):
        print("ERROR: %s would hold non-ASCII bytes. Nothing was written."
              % path)
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker. "
              "Nothing was written." % path)
        return False, None
    return True, out


def main():
    ok1, led = plan(LEDGER, LEDGER_EDITS)
    if not ok1:
        return 1
    ok2, page = plan(PAGE, PAGE_EDITS, top_only=True)
    if not ok2:
        return 1
    wrote = False
    for path, out, n in ((LEDGER, led, len(LEDGER_EDITS)),
                         (PAGE, page, len(PAGE_EDITS))):
        if out is None:
            continue
        with open(path, "wb") as f:
            f.write(out)
        wrote = True
        print("ok %s (%d edits)" % (path, n))
    if led is not None:
        print("Running ledger_index.py to rebuild the index rows ...")
        r = subprocess.run([sys.executable, "ledger_index.py"],
                           capture_output=True, text=True)
        tail = (r.stdout + r.stderr).strip().splitlines()[-6:]
        for line in tail:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: ledger_index.py exited %d. The edits above are "
                  "written; Discard Changes in GitHub Desktop undoes them."
                  % r.returncode)
            return 1
        print("ok ledger_index.py")
    print("patch applied" if wrote else "Nothing to do.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
