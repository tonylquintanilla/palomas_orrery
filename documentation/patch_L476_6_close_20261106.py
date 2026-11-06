"""
patch_L476_6_close_20261106.py -- L-476 (the paths by the plan) closed
on Tony's look; its one loose end, the horizons-orbital-mechanics
sentence on the last-day pair, carried to L-485 (a nightly run) for
that skill's next version; Where We Are updated by section.

Built on orrery dc52cbe71d325a0e027d3284f025e5203fbd1677 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), and
gallery 6c93d0a24dca06457759e38dc03da2f70e7bcf1a at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read for
the Signals line only), both read live on Nov 6, 2026, 16:27 Chicago.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

Type: RECORDS. Written by the coordinating session of Nov 6, evening
(Claude Opus 5.5, through the python_work door), from Tony's words of
16:27: "Close L-476 (the paths by the plan): my look of Nov 6 passed
(animation at 98.6 AU). Re-home its loose end, the
horizons-orbital-mechanics sentence on the last-day pair, to the open
item that carries that skill's next-version notes." His maintenance
run is read from his run record
documentation/WHERE_WE_ARE_11-6-26_1010_run_record.md.

WHAT IT CHANGES (two files, all or nothing)

    LEDGER_CONSOLIDATED.md
                        L-476 DONE, with the close and where its loose
                        end went; L-485 receives the skill sentence.
    documentation/WHERE_WE_ARE.md
                        by section: the header, the box, the road's
                        stages 13 and 14, Signals, Where the details
                        are. Nothing below the run-record marker.

    Both files are checked only at the lines this patch edits, so your
    own notes elsewhere in them never stop it. Then it runs
    ledger_index.py, which moves L-476 to the closed rows of the index.

RUN COMMAND

    Save this file in the orrery's root folder
    (C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
    open it in VS Code and click Run. (python patch_L476_6_close_20261106.py)

    Success: one "ok" line per file, the indexer's last lines, then
    "patch applied". Failure: one ERROR or ANCHOR FAIL line, and
    nothing is written. Undo is Discard Changes in GitHub Desktop.

Written November 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"

EDITS = {}

# ------------------------------------------------------------ the ledger
EDITS[LEDGER] = [
    (b"""<!-- L:476 status:OPEN upd:2026-11-06 section:A flag: rice: -->""",
     b"""<!-- L:476 status:DONE upd:2026-11-06 section:A flag: rice: -->"""),
    (b"""**Gap (replaces the one below, 2026-11-06, afternoon):** Tony's look at
the same animation with Auto scale""",
     b"""- **2026-11-06, evening: closed.** Tony's look after
  `patch_L476_5_animation_scale_and_settings.py`, in his words to the
  coordinating session of Nov 6, evening (Claude Opus 5.5, through the
  python_work door, on orrery dc52cbe and gallery 6c93d0a): "my look of
  Nov 6 passed (animation at 98.6 AU)." The same animation (Pioneer 10,
  Galileo and Jupiter, Sun-centred, from 2000 by year, Auto scale)
  opened at 98.6 AU, where the patch expected about 98 (Pioneer 10's
  82.1 AU plus 20 percent). His maintenance run, in his run record
  `documentation/WHERE_WE_ARE_11-6-26_1010_run_record.md`: "35 of 35
  gating checkers passed", the Horizons check among them (it had been
  red only in the session's copy, which could not reach JPL). Pushed at
  dc52cbe.
- **Where the loose ends went** (A Closing Item Re-homes Its Loose
  Ends): the horizons-orbital-mechanics sentence on the last-day pair,
  to L-485 (a nightly run), beside its other notes for that skill's
  next version, as its sentence on the daily tail went on Nov 3.
  Struck, with the reason: "No permanent check covers the scale or the
  boxes" (above). The scale is judged by Tony's eyes (Visual
  Verification), and a box that cannot be read now names itself when it
  fails, so no item is opened for it. Nothing else here is recorded as
  not done: `--galileo` ran on his machine (305 drawn, 305 served), and
  the earlier loose ends went at the close of Nov 3.
**Gap (replaces the one below, 2026-11-06, evening, at the close):**
none; closed.
**Gap (superseded above, 2026-11-06, evening, at the close; replaced the one below, 2026-11-06, afternoon):** Tony's look at
the same animation with Auto scale"""),
    (b"""  since `patch_L476_2` it keeps the tail and leaves out only the
  last-day pair.
""",
     b"""  since `patch_L476_2` it keeps the tail and leaves out only the
  last-day pair.
- **Received 2026-11-06, evening, from L-476 at its close,** for
  horizons-orbital-mechanics' next version. The sentence received above
  rode 1.16 and has gone out of date again. A Plan Draws a Path Only
  Around the Sun (1.18) says the orrery's drawing is the website's
  `fetch_path_by_plan` point for point, "leaving out only its last-day
  pair", and that `test_path_drawing.py --galileo` finds "Galileo's 303
  points equal the website's served file but for its last-day pair".
  Since `patch_L476_4_ended_markers.py` (Nov 6), `draw_plan` also adds
  the website's last-day pair, 00:00 and 00:01 UTC of the span's last
  day, to a path whose last day is already past, so an ended mission's
  line ends at its marker; a path whose span runs on past today gets no
  pair. Tony's `--galileo` run of Nov 6: "305 drawn, 305 served". Carried,
  not bumped, on Tony's word of Nov 6: a session following the old
  sentence would describe the drawing wrongly, and the test itself
  already expects the pair.
"""),
    (b"""<!-- L:485 status:OPEN upd:2026-11-05 section:A flag: rice: -->""",
     b"""<!-- L:485 status:OPEN upd:2026-11-06 section:A flag: rice: -->"""),
]

# ------------------------------------------------------------ Where We Are
EDITS[WWA] = [
    (b"""Last updated: November 6, 2026, late afternoon: the coordinating session (Opus), after your look.
- Written at orrery d9db340 and gallery 6c93d0a, plus this session's third patch.""",
     b"""Last updated: November 6, 2026, evening: the coordinating session (Opus), at L-476's close.
- Written at orrery dc52cbe and gallery 6c93d0a, plus this session's close patch."""),
    (b"""> - Both fixes are pushed and your look passed: the live check, and
>   ended missions' markers on their last day.
> - The animation's Auto scale now counts spacecraft; an unreadable
>   settings box is named instead of a silent stop. Patch, not run.
>
> **Do next:** *steps 1 to 4 below, in order.*
>
> **Needs you now:**
> - *1. (do) Orrery: run `patch_L476_5_animation_scale_and_settings.py`,
>   then the maintenance run from the dashboard: all gating checkers passed.*
> - *2. (do) Look: the same animation on Auto scale: about 98 AU.*
> - *3. (do) Commit and push the orrery, not during the website's night.*
> - *4. Then L-476 (the paths by the plan) closes.*
""",
     b"""> - Your look passed (98.6 AU on Auto scale): L-476 (the paths by the
>   plan) is closed.
> - Its loose end, a Horizons skill sentence on the drawing's last day,
>   waits on L-485 (a nightly run) for that skill's next version.
>
> **Do next:** *stage 14: your ruling on the Pluto row, then the Moon.*
>
> **Needs you now:**
> - *(do) Orrery: run `patch_L476_6_close_20261106.py`, then commit and
>   push the orrery, not during the website's night.*
> - *(decide) The Pluto row: what it draws and what it is called.*
"""),
    (b"""  1-12.[done]  Through Nov 5: the three rooms, the objects, the Sun's and
               Earth's slices, historical missions' slice 1, the paths by
               the plan (L-476), path or orbit by e (L-510), A1 and A2
               of JPL's fallbacks (L-512), a green website night.
 13.   [NOW]   *Quick wins:* the live check's list, done (L-423 (the
               website's checks)); the ended markers, done, and the
               animation's scale, for your look (L-476 (the paths by the plan)).
 14.   [next]  Standards: the Moon gets the orrery's words, link, period
               and uncertainty; the Pluto row's drawing and name, your ruling.""",
     b"""  1-13.[done]  Through Nov 6: the three rooms, the objects, the Sun's and
               Earth's slices, historical missions' slice 1, the paths by
               the plan (L-476, closed), path or orbit by e (L-510), A1
               and A2 of JPL's fallbacks (L-512), a green website night,
               the quick wins with L-423 (the website's checks). << moved
 14.   [NOW]   *Standards: the Moon gets the orrery's words, link, period
               and uncertainty; the Pluto row's drawing and name, your
               ruling.* << moved this session"""),
    (b"""- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at d9db340, Nov 6).""",
     b"""- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at dc52cbe, Nov 6)."""),
    (b"""  `patch_L476_4_ended_markers.py` and `patch_L476_5_...` (orrery).""",
     b"""  `patch_L476_4_ended_markers.py`, `patch_L476_5_...` and the close,
  `patch_L476_6_close_20261106.py` (orrery)."""),
]

ORDER = [LEDGER, WWA]


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
        below = lf[lf.index(MARKER):] if name == WWA else None
        for old, new in EDITS[name]:
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. "
                      "If this patch already ran, there is nothing to do. "
                      "NOTHING was written." % (name, n, old[:60]))
                return 1
            lf = lf.replace(old, new)
        if name == WWA and lf[lf.index(MARKER):] != below:
            print("ERROR: an edit reached below the run-record marker. "
                  "NOTHING was written.")
            return 1
        if any(c > 127 for _o, new in EDITS[name] for c in new):
            print("ERROR: the inserted text holds non-ASCII. NOTHING was "
                  "written.")
            return 1
        if name == WWA:
            above = lf[:lf.index(MARKER)].count(b"\n")
            if above > 130:
                print("ERROR: the page would stand %d lines above the "
                      "run-record marker, over its 130. NOTHING was "
                      "written." % above)
                return 1
        out[name] = (path, lf, b"\r\n" in raw)
    for name in ORDER:
        path, lf, was_crlf = out[name]
        with open(path, "wb") as handle:
            handle.write(lf)
        print("ok %s (%d edits)" % (name, len(EDITS[name])))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("stamps updated: the page's Last updated line; L-476's and "
          "L-485's upd dates")
    print("Running ledger_index.py ...")
    r = subprocess.run([sys.executable, "ledger_index.py"], cwd=ROOT,
                       capture_output=True, text=True)
    for line in (r.stdout + r.stderr).strip().splitlines()[-4:]:
        print("  " + line)
    if r.returncode != 0:
        print("ERROR: ledger_index.py exited %d. The edits above are "
              "written; Discard Changes in GitHub Desktop undoes them. "
              "Paste these lines to the session." % r.returncode)
        return 1
    print("patch applied")
    print("")
    print("Do next, in order:")
    print("  1. Move this patch, and patch_L476_5_animation_scale_and_"
          "settings.py,")
    print("     which is still in the root folder, into documentation\\.")
    print("  2. Commit and push the orrery in GitHub Desktop, not during")
    print("     the website's night.")
    print("Not changed, and named: skills/horizons-orbital-mechanics/"
          "SKILL.md still says")
    print("the drawing leaves out the last-day pair; carried on L-485 for "
          "its next version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
