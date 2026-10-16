#!/usr/bin/env python3
"""
patch_L446_1_rulings_20261015.py -- records the coordination session of
October 15, 2026 (evening): L-446 (the Daily Run's order) takes in
L-380 (the pull after the build) and L-388 (a pull that prints success
when it could not fetch), which were item 2 of L-423 (the website's
checks); L-448 (the test file in the tracked tree) rides L-445's
session (Earth's period); and the two build briefs are written.

Tony's ruling of 2026-10-15: "yes, confirmed as recommended." No code
changes.

Built on orrery b4105c0 ("Update WHERE_WE_ARE_10-14-26_2250_run_record.md";
the code is 802e5bd's) at
https://github.com/tonylquintanilla/palomas_orrery; the gallery read at
95713f4 ("daily run again") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and not
touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Fable 5.1.

RUN COMMAND

    python patch_L446_1_rulings_20261015.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in two files

    LEDGER_CONSOLIDATED.md    L-446: the ruling, the brief, L-380 and
                              L-388 folded in; L-380, L-388: folded into
                              L-446; L-423: item 2 points at L-446;
                              L-445: the brief, L-448 rides; L-448:
                              rides L-445; header stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only:
                              the date and SHAs, the box, road stages
                              5, 8c and 9, the marks reset, the details

    The two briefs are separate files, saved beside this script's
    records in documentation/:
      documentation/HANDOFF_L445_earth_period_brief_20261015.md
      documentation/HANDOFF_L446_daily_run_order_brief_20261015.md
    This patch checks that both are present and refuses if either is
    missing, so Where We Are never points at a file that is not there.

    Each edited file is checked only at the lines edited, so Tony's
    notes anywhere else are kept.

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
BRIEFS = ("documentation/HANDOFF_L445_earth_period_brief_20261015.md",
          "documentation/HANDOFF_L446_daily_run_order_brief_20261015.md")
MARKER = "--- Your run record below this line"
WWA_CAP = 130


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the orrery folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def rep(text, old, new, label, log, rel):
    n = text.count(old)
    if n != 1:
        raise PatchError("ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r"
                         % (rel, label, n, old[:70]))
    log.append("ok  %-34s %s" % (rel, label))
    return text.replace(old, new)


# ---------------------------------------------------------------- ledger

DONE_MARK = "- **2026-10-15, L-380 and L-388 folded in**"

LEDGER_EDITS = [
    ("L-446 the ruling, the brief",
     """**Gap:** a small gallery build, its own session: the pulls and copies
ahead of the builder;""",
     """- **2026-10-15, L-380 and L-388 folded in** (Tony's ruling in the
  coordination session of 2026-10-15, "yes, confirmed as recommended").
  This item was opened without reference to two older ones that are
  the same build: L-380 (the gallery pulls the constants export AFTER
  the cache build, so the cache's stamp is one step behind; its Gap is
  pull first, then build) and L-388 (a pull that cannot fetch prints
  success and exits 0, and the mirror then writes from the old export;
  its Gap is fail by name, and no mirror after a failed pull). Tony had
  made them item 2 of L-423 (the website's checks) on 2026-10-08, "one
  patch". So: this item carries the build; L-380 and L-388 close at its
  close; L-423's item 2 is done by it, and building this item advances
  road stage 9 as well as 8c. The fail-by-name half belongs in the same
  patch anyway: once the pull runs before the build, a pull that fails
  quietly would feed the builder stale data in the same run.
- **The brief:** `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`,
  written in that session at b4105c0. It carries the one decision for
  Tony (what the Daily Run does after a failed pull: stop, or build on
  the previous pull and say so) and the planted faults.
**Gap:** a small gallery build, its own session, from the brief: the
pulls and copies ahead of the builder;"""),

    ("L-446 Ref",
     """`tools/pull_drawings.py`, `tools/gallery_cache_builder.py`; L-444;
L-445; L-431; L-395; skills/gallery-cache-builder/SKILL.md, The Daily
Run's Steps.
""",
     """`tools/pull_drawings.py`, `tools/gallery_cache_builder.py`; L-380;
L-388; L-423 (item 2); L-444; L-445; L-431; L-395;
skills/gallery-cache-builder/SKILL.md, The Daily Run's Steps;
`documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.
"""),

    ("L-380 date",
     "<!-- L:380 status:OPEN upd:2026-10-08 section:A flag: rice: -->",
     "<!-- L:380 status:OPEN upd:2026-10-15 section:A flag: rice: -->"),

    ("L-380 folded into L-446",
     """- **2026-10-08:** item 2 of L-423 (the website's checks), one
  patch with L-388.
- **Found 2026-09-25** at gallery `ce09f789`.""",
     """- **2026-10-08:** item 2 of L-423 (the website's checks), one
  patch with L-388.
- **2026-10-15, folded into L-446** (the Daily Run's order; Tony's
  ruling in the coordination session of 2026-10-15). L-446's build is
  this fix: the pulls run before the builder. This item closes at that
  build's close; its brief is
  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.
- **Found 2026-09-25** at gallery `ce09f789`."""),

    ("L-388 date",
     "<!-- L:388 status:OPEN upd:2026-10-08 section:A flag: rice: -->",
     "<!-- L:388 status:OPEN upd:2026-10-15 section:A flag: rice: -->"),

    ("L-388 folded into L-446",
     """- **2026-10-08:** item 2 of L-423 (the website's checks), one
  patch with L-380.
- **Found 2026-09-28** building the L-345 gallery patch.""",
     """- **2026-10-08:** item 2 of L-423 (the website's checks), one
  patch with L-380.
- **2026-10-15, folded into L-446** (the Daily Run's order; Tony's
  ruling in the coordination session of 2026-10-15). The fail-by-name
  half of L-446's build is this item's Gap, and its brief carries the
  network-off test as the planted fault that matters most. This item
  closes at that build's close; the brief is
  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.
- **Found 2026-09-28** building the L-345 gallery patch."""),

    ("L-423 date",
     "<!-- L:423 status:OPEN upd:2026-10-08 section:A flag: rice: -->",
     "<!-- L:423 status:OPEN upd:2026-10-15 section:A flag: rice: -->"),

    ("L-423 item 2 points at L-446",
     """  2. L-380 and L-388, the export pull, as one patch: pull before the
     cache build, and fail by name when the pull cannot fetch.
""",
     """  2. L-380 and L-388, the export pull, as one patch: pull before the
     cache build, and fail by name when the pull cannot fetch.
     2026-10-15: L-446 (the Daily Run's order) carries this item, by
     Tony's ruling in the coordination session; its brief is written.
     Done when L-446 closes.
"""),

    ("L-445 the brief, L-448 rides",
     """**Gap:** a small build, its own session: the target for Earth's period,
the check asking the same target, the hover's words, a planted fault
(Earth's period taken for 399 again) and a live run; then the website
look above.
""",
     """- **The brief, 2026-10-15:**
  `documentation/HANDOFF_L445_earth_period_brief_20261015.md`, written
  in the coordination session of that evening at b4105c0. It maps where
  the target reaches (one home for the map in `orbital_period.py`; the
  record carries the target and every reader takes it from the record;
  `period_fetch.py` re-fetches a body whose record's target is not the
  map's, which is how Earth is re-fetched without plotting) and the
  planted faults. L-448 (the test file in the tracked tree) rides this
  session, Tony's ruling of 2026-10-15.
**Gap:** a small build, its own session, from the brief: the target for
Earth's period, the check asking the same target, the hover's words in
the orrery and on the website, the planted faults and a live run; then
the website look above. L-448 rides.
"""),

    ("L-448 rides L-445",
     """**Gap:** stop tracking it: the test writes it into a folder git ignores
(or a temporary folder), and the file leaves the repository in the same
patch. Small; ride a session already touching the maintenance run.
""",
     """- **2026-10-15, rides L-445** (Earth's period; Tony's ruling in the
  coordination session of 2026-10-15). L-445's brief carries it: the
  test writes its fixture into a temporary folder, `.gitignore` gains
  `test_output/`, and the patch deletes the tracked file so the
  deletion is what Tony commits.
**Gap:** stop tracking it: the test writes it into a folder git ignores
(or a temporary folder), and the file leaves the repository in the same
patch. Rides L-445's session.
"""),

    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     """Module updated: October 15, 2026 with Anthropic's Claude Fable 5.1
(coordination: L-446 takes in L-380 and L-388, item 2 of L-423; L-448
rides L-445; the two briefs written), built on b4105c0.
Review and RICE update Tony 6-21-2026
"""),
]

# --------------------------------------------------------- where we are

WWA_EDITS = [
    ("header",
     """Last updated: October 15, 2026, late night: L-401 build 3 parked.
- Written at orrery 45085c4 and gallery 95713f4.
""",
     """Last updated: October 15, 2026, late night: the two briefs written.
- Written at orrery b4105c0 and gallery 95713f4.
"""),

    ("changed since you last read this",
     """> - Parked: L-401 build 3 (the distance digits), your ruling of Oct 15:
>   each part waits for its feature. Earth's list now starts at L-445.
""",
     """> - Briefs written for L-445 (Earth's period) and L-446 (the Daily
>   Run's order); L-446 takes in L-380 and L-388 (the export pull).
"""),

    ("do next",
     """> **Do next:** *Build L-445 (Earth's period). Then finish Earth's
> list, then the Sun's; the objects come after (your ruling, Oct 15).*
""",
     """> **Do next:** *Start the L-445 (Earth's period) build session from
> its brief; L-446 (the Daily Run's order) from its brief, either order.*
"""),

    ("needs you now",
     """> - *Run patch_L401_5, then the maintenance run; commit; push.*
""",
     """> - *Run patch_L446_1, then the maintenance run; commit; push.*
"""),

    ("road stage 5 mark reset",
     """               design talks.*  << moved this session
""",
     """               design talks.*
"""),

    ("road stage 8c",
     """  8c.  [next]  L-446 (the daily run's order): the website pulls the
               orrery's checked data before it builds.
""",
     """  8c.  [next]  L-446 (the Daily Run's order): the website pulls the
               orrery's data before it builds; takes in L-380, L-388.
"""),

    ("road stage 9",
     """  9.   [next]  The website's checks, in the order you confirmed:
               L-423 (the website's checks).
""",
     """  9.   [next]  The website's checks, in the order you confirmed:
               L-423 (the website's checks); its item 2 is stage 8c.
"""),

    ("settled mark reset",
     "## Settled  **>> UPDATED THIS SESSION**\n",
     "## Settled\n"),

    ("signals mark reset",
     "## Signals  **>> UPDATED THIS SESSION**\n",
     "## Signals\n"),

    ("details: next",
     """- *Next: L-445 (Earth's period) in the ledger*
""",
     """- *Next: `HANDOFF_L445_earth_period_brief_20261015.md` and
  `HANDOFF_L446_daily_run_order_brief_20261015.md`, the two briefs*
"""),

    ("details: the distance digits, shorter",
     """- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;
  reviews `REVIEW_L401_..._comparison_20261011.md`; build 1
  `HANDOFF_L401_distance_build1_20261012.md`; build 3 parked: L-401.
""",
     """- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;
  build 1 `HANDOFF_L401_distance_build1_20261012.md`; build 3 parked: L-401.
"""),
]


def main():
    log = []
    try:
        for rel in BRIEFS:
            if not os.path.exists(os.path.join(ROOT, rel)):
                raise PatchError("the brief %s is not in documentation/; "
                                 "save both briefs there first" % rel)
            log.append("ok  %-34s present" % rel)

        led, led_crlf = read(LEDGER)
        if DONE_MARK in led:
            raise PatchError("L-446 already records L-380 and L-388 folded "
                             "in; this patch has run")
        for label, old, new in LEDGER_EDITS:
            led = rep(led, old, new, label, log, LEDGER)

        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError("ANCHOR FAIL [%s run-record marker]" % WWA)
        cut = wwa.index(MARKER)
        top, bottom = wwa[:cut], wwa[cut:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new, label, log, WWA)
        above = top.count("\n")
        if above > WWA_CAP:
            raise PatchError("%s would stand %d lines above the marker (cap %d)"
                             % (WWA, above, WWA_CAP))
        log.append("ok  %s: %d lines above the marker (cap %d)"
                   % (WWA, above, WWA_CAP))
        wwa = top + bottom

        out = {LEDGER: (led, led_crlf), WWA: (wwa, wwa_crlf)}
        for rel, (text, _c) in out.items():
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s)" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    notes = []
    for rel, (text, crlf) in out.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log + notes:
        print(line)
    print("stamps updated: the ledger's header; L-380's, L-388's and "
          "L-423's dates; Where We Are's date and SHAs")
    print("patch applied (2 files edited; 2 briefs confirmed present)")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/; then run")
    print("     orrery_maintenance_run.py (it rebuilds the ledger's index);")
    print("     commit and push the orrery.")
    print("  2. Start the L-445 build session from its brief, or the L-446")
    print("     session from its brief; either order.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
