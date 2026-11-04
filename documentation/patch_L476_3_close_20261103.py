"""
patch_L476_3_close_20261103.py -- L-476 (the orrery plots by the path
plan) closed; the unused date function marked obsolete; L-509 (obsolete
code) opened; Where We Are updated.

Built on orrery b09989e0d706b4454d7539bd4c392752b64c87bf at
https://github.com/tonylquintanilla/palomas_orrery (branch main), and
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read for
the Signals line only), both read live on Nov 3, 2026, evening.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

Type: RECORDS, with one code comment. Written by the coordinating
session (Claude Opus 5.5) from Tony's run record
WHERE_WE_ARE_11-3-26_1158_run_record.md and his words of 15:14:
"for documentation mark it as obsolete. we should discuss how we treat
this. we have other code that is marked as obsolete." and, on closing
L-476: "yes, thanks. good session."

WHAT IT CHANGES (three files, all or nothing)

    palomas_orrery.py   create_dates_list_for_object gets a DEPRECATED
                        banner, in the form the file already uses, and
                        its docstring says it is obsolete. No behaviour
                        changes: nothing calls it. Docstring stamp.
    LEDGER_CONSOLIDATED.md
                        L-476 DONE, its loose ends re-homed: L-509 new
                        (obsolete code); L-507 (Pioneer 10's line);
                        L-485 (the skill sentence on the daily tail);
                        L-484 (its line on the daily tail corrected).
    documentation/WHERE_WE_ARE.md
                        by section: the header, the box, the road's 5b
                        line, one Settled line, Signals, Waiting on you,
                        Where the details are. Nothing below the
                        run-record marker.

    The ledger and Where We Are are checked only at the lines this patch
    edits, so your own notes elsewhere in them never stop it.
    palomas_orrery.py is checked whole.

RUN COMMAND

    Save this file in the orrery's root folder
    (C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
    open it in VS Code and click Run. (python patch_L476_3_close_20261103.py)

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line, and nothing is written. Undo is Discard
    Changes in GitHub Desktop.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

WHOLE = {"palomas_orrery.py": "ab93ff69c5d548a2ed0e45ee5a15bf88"}

EDITS = {}

# ------------------------------------------------------------ palomas_orrery.py
EDITS["palomas_orrery.py"] = [
    (b"""not called from anywhere and was left as it is.)
""",
     b"""not called from anywhere and was left as it is.)
Module updated: November 3, 2026, evening, with Anthropic's Claude Opus
5.5 (L-476 closed: create_dates_list_for_object marked DEPRECATED,
obsolete, by Tony's word; how obsolete code is treated is L-509.)
"""),
    (b"""def create_dates_list_for_object(""",
     b"""# =============================================================================
# DEPRECATED: create_dates_list_for_object
# Obsolete since November 3, 2026 (L-476): called from nowhere. The live
# date lists are built in plot_objects' worker, and a planned path is drawn
# by path_drawing.py. Kept, marked, until L-509 (how obsolete code is
# treated) rules whether it goes.
# =============================================================================
def create_dates_list_for_object("""),
    (b"""center_object_name, max_date, settings):
    \"\"\"
    Create a list of dates for plotting based on object type.
""",
     b"""center_object_name, max_date, settings):
    \"\"\"
    DEPRECATED (obsolete, L-476): not called from anywhere; see the banner.
    Create a list of dates for plotting based on object type.
"""),
]

# -------------------------------------------------------- LEDGER_CONSOLIDATED.md
EDITS["LEDGER_CONSOLIDATED.md"] = [
    (b"""#### [L-508] A held body's alarm""",
     b"""#### [L-509] Obsolete code: how it is marked, and when it goes (orrery, housekeeping)
<!-- L:509 status:OPEN upd:2026-11-03 section:A flag: rice: -->
- **Tony, 2026-11-03, 15:14, in chat**, asked whether the orrery's
  unused date function `create_dates_list_for_object` goes (L-476's
  close): "for documentation mark it as obsolete. we should discuss how
  we treat this. we have other code that is marked as obsolete."
- **Marked the same evening** in `patch_L476_3_close_20261103.py`: a
  DEPRECATED banner over the function, in the form `palomas_orrery.py`
  already uses, saying it is obsolete, called from nowhere, and kept
  until this item rules.
- **The marks already there, in `palomas_orrery.py` alone at
  b09989e0** (a search for "DEPRECATED" and "obsolete"; the rest of the
  tree is not yet searched): `toggle_special_fetch_mode`, a stub kept
  since December 2024; the Special Fetch Mode and Interval Settings
  section (lines 11175 to 11249 at b09989e0); and now
  `create_dates_list_for_object`.
**Note:** questions for the talk, Claude's: whether a marked function
is removed, kept as a stub, or kept whole; how long it waits; whether
git's history is the record once it is gone; and whether the
maintenance run lists what is marked.
**Gap:** a design talk (Where We Are, at the next design talk); then a
search of the whole tree for marked code, which lists and fixes
nothing; then a housekeeping slice (5b on the road).
**Ref:** L-476; `palomas_orrery.py`.

#### [L-508] A held body's alarm"""),
    (b"""**Gap (replaces the one below, 2026-11-03, morning):** slice 2 waits""",
     b"""- **Received 2026-11-03, evening, from L-476 at its close:** Pioneer
  10 in the desktop orrery has no plan, and its typed end is
  2002-03-03, so its line stops at 79.8 AU while its marker is at
  today's 142.2 AU (Tony's look: "spacecraft is outline the filled
  line"). For the slice that takes up the orrery's other ended
  missions (Pioneer 10, Pioneer 11, Rosetta, DART).
**Gap (replaces the one below, 2026-11-03, morning):** slice 2 waits"""),
    (b"""**Gap (replaces the one below, 2026-11-02, evening):** the morning looks for the""",
     b"""- **Received 2026-11-03, evening, from L-476 at its close,** for
  horizons-orbital-mechanics' next version, beside the notes above: A
  Plan Draws a Path Only Around the Sun (1.15) says the orrery's
  drawing is the website's "without its daily tail and last-day pair";
  since `patch_L476_2` it keeps the tail and leaves out only the
  last-day pair.
**Gap (replaces the one below, 2026-11-02, evening):** the morning looks for the"""),
    (b"""the website as paths. Detail on
  L-476.
""",
     b"""the website as paths. Detail on
  L-476.
- **Corrected 2026-11-03, evening (L-476's close):** the line above
  says the orrery draws neither the website's daily tail nor its
  last-day pair. Since `patch_L476_2` the orrery draws the tail too; of
  those two, only the last-day pair is left, beside the three comets.
"""),
    (b"""<!-- L:476 status:OPEN upd:2026-11-03 section:A flag: rice: -->""",
     b"""<!-- L:476 status:DONE upd:2026-11-03 section:A flag: rice: -->"""),
    (b"""**Gap (replaces the one below, 2026-11-03, evening):** Tony's look at
Voyager 1""",
     b"""- **2026-11-03, evening: closed.** Tony's look after `patch_L476_2`
  (`documentation/WHERE_WE_ARE_11-3-26_1158_run_record.md`): Voyager 1
  and 3I/ATLAS centred on the Sun, each marker where the solid line
  turns dashed, "yes". The path drawing suite 7 of 7; the maintenance
  run "34 of 34 gating checkers passed", 0 Tier-1 on the gate path.
  Pushed at b09989e0, read back on GitHub with the patch filed in
  `documentation/`. Tony, 15:14, on the unused function: "for
  documentation mark it as obsolete. we should discuss how we treat
  this." On closing: "yes, thanks. good session."
- **Where the loose ends went** (A Closing Item Re-homes Its Loose
  Ends): `create_dates_list_for_object`, marked DEPRECATED in
  `patch_L476_3_close_20261103.py`, to L-509 (obsolete code); the
  skill sentence on the daily tail, to L-485, beside its other notes
  for horizons-orbital-mechanics' next version; Pioneer 10's line
  short of its marker, to L-507; the three comets drawn as ellipses
  and the last-day pair, to L-484, whose line on the daily tail is
  corrected there.
**Gap (replaces the one below, 2026-11-03, evening, at the close):**
none; closed.
**Gap (superseded above, 2026-11-03, evening, at the close; replaced the one below, 2026-11-03, evening):** Tony's look at
Voyager 1"""),
]

# ------------------------------------------------- documentation/WHERE_WE_ARE.md
WWA = "documentation/WHERE_WE_ARE.md"
EDITS[WWA] = [
    (b"""Last updated: November 3, 2026, afternoon: the orrery's Claude Code session (the desktop orrery draws spacecraft and comet paths by their plans).
- Written at orrery 81fa7b8a and gallery 3a211a8c, plus this session's uncommitted edits.
""",
     b"""Last updated: November 3, 2026, evening: the coordinating session (your look at the fixed paths passed; L-476 closed).
- Written at orrery b09989e0 and gallery 5abca2c6, plus this session's uncommitted edits.
"""),
    (b"""> - The desktop orrery now draws each spacecraft's and comet's whole
>   path the way the website does, from its path plan (L-476 (the
>   orrery plots by the plan)).
> - Around the Sun, the path is solid up to today and dashed after,
>   as on the website. Around any other body it is drawn as before.
> - Galileo now stops at its crash into Jupiter, as on the website.
>   Cassini ends on 15 September 2017.
> - The dates beside 25 spacecraft and comets in the orrery's window
>   are now read from the plans, so they match the website. No path's
>   end date is typed by hand any more, and a check fails if one comes
>   back.
> - Checked against JPL: Galileo's 303 points match the website's
>   point for point. The only difference is the website's two points
>   on its last day, which the orrery does not need.
> - Nothing the website serves changed, and none of its checks moves.
> - One skill and the protocol (v3.124) carry the rule that a plan
>   draws a path only around the Sun.
>
> **Do next:** *your look at six plots in the desktop orrery (the
> run order in this session's report); commit and push the orrery;
> then, in Settings > Skills, reinstall horizons-orbital-mechanics,
> and paste v3.124 into the Project's instructions on claude.ai. Then
> the design talk on L-484 (the two agree), from
> `HANDOFF_L484_consistency_talk_20261103.md`.*
""",
     b"""> - The desktop orrery draws each spacecraft's and comet's whole
>   path from its plan, as the website does: solid to today, dashed
>   after, around the Sun only. L-476 (the orrery plots by the plan)
>   is done and closed.
> - Your look passed: each marker sits where the solid line turns
>   dashed, for Voyager 1 and 3I/ATLAS.
> - The first build turned the line dashed years back on a straight
>   path. The brief had left out the website's daily points around
>   today; a second patch added them.
> - Galileo stops at its crash into Jupiter, and the dates beside 25
>   spacecraft and comets come from their plans.
> - The unused date function is marked obsolete, not deleted. How
>   obsolete code is treated is a talk of its own (L-509 (obsolete
>   code)).
>
> **Do next:** *the design talk on L-484 (the two agree), from
> `HANDOFF_L484_consistency_talk_20261103.md`.*
"""),
    (b"""               (L-476), Nov 3. << changed this session
""",
     b"""               (L-476), Nov 3.
"""),
    (b"""               the dates, is fixed (L-476, Nov 3).* << changed this session
  5b.  [beside] Housekeeping when a session has room: L-424, L-425,
               L-426; L-423 (the website's checks) item 3, L-357.
""",
     b"""               the dates, is fixed (L-476, Nov 3).*
  5b.  [beside] Housekeeping when a session has room: L-424, L-425,
               L-426; L-423 (the website's checks) item 3, L-357;
               L-509 (obsolete code), after its talk. << changed this session
"""),
    (b"""- A plan draws a path only around the Sun, in both the orrery and the
  website; around any other body the path is drawn as before (Nov 3,
  12:06). << new this session
""",
     b"""- Obsolete code is marked, not deleted, until a talk rules how it is
  treated (Nov 3, 15:14). << new this session
- A plan draws a path only around the Sun, in both the orrery and the
  website; around any other body the path is drawn as before (Nov 3,
  12:06).
"""),
    (b"""- Last cache build: 20261103T161740Z, ok, no retry (the website's swap
  log's last line at 1a79238c: the night run of Nov 3).
- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md,
  this session's orrery run).
""",
     b"""- Last cache build: 20261103T193343Z, ok, no retry (the website's swap
  log's last line at 5abca2c6: a nightly-mode build of Nov 3).
- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md
  at b09989e0, your maintenance run of the evening).
"""),
    (b"""- The shared link (ruled Oct 29) waits for its build.

Not urgent, in your order:
1. Whether the orrery's unused date function goes
   (`create_dates_list_for_object`; L-476 (the orrery plots by the plan)).
2. Whether the editor also edits the Solar System room's rows, and
   adds a new body as a form (L-489 (compositions)).
3. The website's second run makes a fresh build and a second commit
   most days: keep, or stand down after a clean 08:17 (L-485 (a nightly run)).
4. Earth's list (L-413 (Earth's list)): stays open as Earth's enhancements, or closes
""",
     b"""- How obsolete code is treated: removed, kept as a stub, or kept
  whole, and when (L-509 (obsolete code)). The first case is the
  orrery's unused date function, marked Nov 3. << new this session
- The shared link (ruled Oct 29) waits for its build.

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows, and
   adds a new body as a form (L-489 (compositions)).
2. The website's second run makes a fresh build and a second commit
   most days: keep, or stand down after a clean 08:17 (L-485 (a nightly run)).
3. Earth's list (L-413 (Earth's list)): stays open as Earth's enhancements, or closes
"""),
    (b"""- Today: L-476 (the orrery plots by the plan), with what was
  verified; the brief
  `COORD_L476_orrery_plots_by_path_plan_brief_20261103.md`.
""",
     b"""- Today: L-476 (the orrery plots by the plan), closed, with what was
  verified; the brief
  `COORD_L476_orrery_plots_by_path_plan_brief_20261103.md`; the fix
  `patch_L476_2_tail_at_today.py`.
"""),
]

ORDER = ["palomas_orrery.py", "LEDGER_CONSOLIDATED.md", WWA]
MARKER = b"--- Your run record below this line"


def main():
    if os.path.basename(ROOT) == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation/. NOTHING was written.")
        return 1
    out = {}
    for name in ORDER:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            print("ERROR: %s not found. Save the patch in the orrery's "
                  "root folder. NOTHING was written." % name)
            return 1
        raw = open(path, "rb").read()
        lf = raw.replace(b"\r\n", b"\n")
        if name in WHOLE:
            got = hashlib.md5(lf).hexdigest()
            if got != WHOLE[name]:
                print("ERROR: %s is not the file this patch was built on "
                      "(orrery b09989e0). Pull origin in GitHub Desktop, "
                      "or discard local edits to it, and run again. If "
                      "this patch already ran, there is nothing to do. "
                      "NOTHING was written." % name)
                return 1
        if name == WWA:
            below = lf[lf.index(MARKER):]
        for old, new in EDITS[name]:
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. "
                      "If this patch already ran, there is nothing to do. "
                      "NOTHING was written." % (name, n, old[:60]))
                return 1
            lf = lf.replace(old, new)
            print("ok  %s: %s" % (name, old.strip().splitlines()[0][:60]
                                  .decode("ascii")))
        if name == WWA and lf[lf.index(MARKER):] != below:
            print("ERROR: an edit reached below the run-record marker. "
                  "NOTHING was written.")
            return 1
        added = sum(1 for _o, new in EDITS[name] for c in new if c > 127)
        if added:
            print("ERROR: the inserted text holds non-ASCII. NOTHING was "
                  "written.")
            return 1
        out[name] = (path, lf, b"\r\n" in raw)
    total = 0
    for name in ORDER:
        path, lf, was_crlf = out[name]
        with open(path, "wb") as handle:
            handle.write(lf)
        total += len(lf)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("stamps updated: palomas_orrery.py (Module updated line); "
          "WHERE_WE_ARE.md (Last updated line)")
    print("patch applied (%d bytes, 3 files)" % total)
    print()
    print("Do next, in order:")
    print("  1. Run the maintenance run from the dashboard. Its Ledger index")
    print("     line should say it rewrote the index: L-476 moves to the closed")
    print("     section, and L-509 is new.")
    print("     Its last line: all gating checkers passed, Tier-1 0.")
    print("  2. Move this patch into documentation/, then commit and push")
    print("     the orrery in GitHub Desktop.")
    print("  3. Next session: the design talk on L-484 (the two agree).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
