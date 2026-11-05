"""
patch_road_symbols_20261105.py -- Where We Are: the road turns to the
symbols, on Tony's order of Nov 5, 2026, and the page catches up with
the website's red nights of Nov 4 and 5. Records only.

Built on orrery 59ddb645 at https://github.com/tonylquintanilla/palomas_orrery
(branch main) and gallery e5352a86 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 5, 2026, 10:45 Chicago. Written by the coordinating session
(Claude Opus 5.5), under ledger-and-session-records 1.22 (Where We Are --
Tony's page) and safe-file-editing 1.14.

WHAT IT CHANGES (one file: documentation/WHERE_WE_ARE.md)

    Section by section, at each section's own text, never the whole
    page. Nothing below the run-record marker is touched.
      - the header: date and the SHAs it was written at
      - the box: what changed, do next, needs you now
      - the road: Tony's order of Nov 5 -- a green night; quick wins
        (the copying tool follows the e rule, the ended missions);
        standards (the Moon, the Pluto row); the planet rooms in order
        from Mars, moons first, shells later; then the Earth room's
        neighbourhood, the small-body systems, stars and exoplanets
      - Settled: the e rule line says the website follows it (Tony,
        Nov 4, 23:47); four lines out that are habit (Oct 28 to Nov 2)
      - Deferred: what the road set aside on Nov 5 (L-512 b and c,
        L-484, L-504, L-510 part 2; the Earth System layers)
      - Signals, read from files: the swap log, PROVENANCE_AUDIT.md,
        the ledger's newest stamp
      - Waiting on you: the Pluto row's ruling; Planet 9 for the talk
      - Where the details are

    130 lines above the marker, the page's limit. Each section is
    checked only at the text it replaces; a section that holds your
    notes is refused by name, with nothing written.

RUN COMMAND

    Save this file in the orrery's root folder
    (palomas_orrery_for_github), open it in VS Code and click Run.
    (python patch_road_symbols_20261105.py)

    Success: one "ok" line per section, then "patch applied". Failure:
    one ERROR or ANCHOR FAIL line, and nothing is written. Undo is
    Discard Changes in GitHub Desktop. A second run says "already
    there" and writes nothing.

    Then move this file into documentation\\ and commit and push the
    orrery. No maintenance run is needed: no status changes.

Written November 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

TARGET = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"

EDITS = [
    ('the header',
     b"Last updated: November 4, 2026, night: the Claude Code session that built L-512 (fallbacks when JPL cannot answer), slice a, part A2.\n- Written at orrery e7ea3294 and gallery 5abca2c6, plus this session's uncommitted edits.\n",
     b"Last updated: November 5, 2026, morning: the coordinating session (Opus) that read the website's red nights and turned the road to the symbols.\n- Written at orrery 59ddb645 and gallery e5352a86, read live.\n"),
    ('the box',
     b'> **Changed since you last read this:**\n> - The orrery now tells "JPL has no such body" from "JPL cannot be\n>   reached", and says which (L-512 (fallbacks when JPL cannot answer)).\n> - By your ruling, MK2, Xiangliu and 6AC4721 keep their drawings from\n>   their papers. The saved-path files are gone from the repository.\n>\n> **Do next:** *your look at A2, wifi on and off (the report\'s run\n> order); then commit.*\n>\n> **Needs you now:**\n> - *(do) Each morning, Pull origin on both, orrery then website, first;\n>   do not wait for the night, which GitHub starts hours late or drops.*\n',
     b"> **Changed since you last read this:**\n> - The website's nights stopped on Nov 4 and 5 over piece C of comet\n>   C/2025 K1, which the orrery now draws as an orbit. Two website\n>   patches fix it; the first is pushed (e5352a86).\n> - By your ruling, the website follows the orrery's rule: path or\n>   orbit by the e in JPL's database.\n> - The road turns to the symbols, with the moons sooner.\n>\n> **Do next:** *run patch_L510_2 in the website folder, commit, push,\n> and run the website's night from the Actions tab; look for a green\n> NIGHT RUN line.*\n>\n> **Needs you now:**\n> - *(do) Each morning, Pull origin on both, orrery then website, first;\n>   do not wait for the night, which GitHub starts hours late or drops.*\n"),
    ('the road',
     b"## The road  **>> UPDATED THIS SESSION**\n\nOct 27's order, changed Oct 29 (`DESIGN_L314_solar_wind_rulings_20261029.md`).\n  1-11.[done]  All but 5b and 9, through Nov 4: the three rooms, the\n               objects, the Sun's and Earth's slices, historical\n               missions' slice 1, the orrery's paths by the plan (L-476),\n               L-510 part 1 (Nov 4).\n 12f.  [NOW]   *L-512 (fallbacks when JPL cannot answer): A1 committed\n               Nov 4; A2 built and ruled on; then b and c.* << moved this session\n 5d.   [NOW]   *The orrery's clock (L-504 (the orrery's clock)): the\n               data path done Oct 29, the website's date fix Oct 31;\n               Earth System, stamps, tools next.*\n 11b.  [NOW]   *The nightly run (L-485 (a nightly run)): both halves run\n               on GitHub; the hold built Oct 31; both second times built\n               (11:17 and 12:17 UTC, Nov 1); a week of mornings now.*\n 12c.  [next]  *The two agree (L-484 (the two agree)): its brief, then\n               its build; piece C is its first open difference. The\n               words wait for L-511 (the export carries the words).*\n 12e.  [later] L-510 (the typed fields stop deciding), part 2: the path\n               plan asked from before any launch.\n  5b.  [beside] Housekeeping when a session has room: L-424, L-425,\n               L-426; L-423 (the website's checks) item 3, L-357;\n               L-509 (obsolete code), after its talk.\n 12b.  [later] Historical missions, slice 2: encounters, the room off\n               today's date; Artemis II in the Earth room.\n 12.   [later] Compositions (L-489 (compositions)): encounters in\n               rooms of their own; Artemis II first (Nov 1).\n 13.   [later] The inner planets' rooms, from the template; Jupiter and\n               Saturn follow (L-433).\n 14.   [later] The Earth System layers, beside 13; cards meanwhile.\n 15.   [goal]  The website does what the desktop orrery does, with a date\n               to choose, within the range the data covers.\n\n",
     b"## The road  **>> UPDATED THIS SESSION**\n\nYour order of Nov 5 (run record `WHERE_WE_ARE_11-4-26_2321_run_record.md`).\n  1-11.[done]  Through Nov 4: the three rooms, the objects, the Sun's and\n               Earth's slices, historical missions' slice 1, the paths by\n               the plan (L-476), path or orbit by e (L-510), A1 and A2\n               of JPL's fallbacks (L-512).\n 12.   [NOW]   *A green website night: patch_L510_2, then the night.* << new this session\n 13.   [next]  Quick wins: the copying tool follows the e rule by itself\n               (L-510 (the typed fields stop deciding)); the ended\n               missions Pioneer 10 and 11, Rosetta, DART, Akatsuki and\n               Apollo 11's S-IVB (L-507 (historical missions)). << new this session\n 14.   [next]  Standards: the Moon gets the orrery's words, link, period\n               and uncertainty; the Pluto row's drawing and name, your ruling. << new this session\n 15.   [later] The planet rooms in order, each opening with the planet\n               and its moons, shells later: Mars (Phobos, Deimos),\n               Jupiter, Saturn, Uranus, Neptune, Pluto. Io, Titan,\n               Charon and Pluto come to standard in their rooms. << new this session\n 16.   [later] The Earth room: L-297 (the Lagrange points), the Earth-Moon\n               barycentre, SOHO, Gaia, James Webb, Artemis II.\n 17.   [later] Small-body systems' moons; then stars and exoplanets.\n 18.   [goal]  The website does what the desktop orrery does, with a date\n               to choose, within the range the data covers.\n  b.   [beside] Housekeeping: L-424, L-425, L-426 (the checkers' three);\n               L-423 (the website's checks) item 3; L-357 (stale gallery\n               artifacts); L-509 (obsolete code), after its talk.\n\n"),
    ('Settled: the e rule line',
     b"once a skill or the protocol carries it (trimmed Nov 3, night).\n- No saved-path file (July copy kept outside); an outage is met by propagation and a record (Nov 4).\n- A small body is a path at or above e 1 in JPL's database, every 30\n  days, else an orbit; two sides of 1 refuse the drawing (Nov 4).\n",
     b"once a skill or the protocol carries it (trimmed Nov 3, night).\n- No saved-path file (July copy kept outside); an outage is met by propagation and a record (Nov 4).\n- A small body is a path at or above e 1 in JPL's database, every 30\n  days, else an orbit; two sides of 1 refuse the drawing; the website\n  follows the same rule (Nov 4; the website, Nov 4, 23:47).\n"),
    ('Settled: comet switch line out',
     b'- The comet switch is off the road: the six record numbers stay (Nov 2).\n',
     b''),
    ('Settled: ticks line out',
     b'- The ticks stay as built, 3 and 6, and so do the ruler and the halo (Nov 2).\n',
     b''),
    ('Settled: Oct 31 line out',
     b'- A night takes a value JPL changed, holds only an identity (Oct 31).\n',
     b''),
    ('Settled: main belt line out',
     b"- The main belt: random dots in JPL's spread (Oct 28).\n",
     b''),
    ('Deferred',
     b'## Deferred\n\nWaiting behind other work; a line leaves when picked up.\n',
     b"## Deferred  **>> UPDATED THIS SESSION**\n\nWaiting behind other work; a line leaves when picked up.\n- When the road turned to the symbols (Nov 5): L-512 (fallbacks when\n  JPL cannot answer) slices b and c; L-484 (the two agree), its brief\n  and build; L-504 (the orrery's clock), the Earth System, stamps and\n  tools; L-510 part 2, the path plan asked from before any launch.\n- The Earth System layers, with cards meanwhile (Nov 5, off the road).\n"),
    ('Signals',
     b"## Signals  **>> UPDATED THIS SESSION**\n\nRead from files when this page was written, not typed from memory.\n- Last cache build: 20261103T193343Z, ok, no retry (swap log at 5abca2c6).\n- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, this session's maintenance run, Nov 4 afternoon).\n- This page's date and the ledger's newest stamp: both Nov 4. Agree.\n\n",
     b"## Signals  **>> UPDATED THIS SESSION**\n\nRead from files when this page was written, not typed from memory.\n- Last cache build: 20261103T193343Z, ok, no retry (swap log at gallery\n  e5352a86); the website's nights of Nov 4 and 5 stopped before a swap.\n- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, generated Nov 4).\n- Page Nov 5, ledger's newest stamp Nov 4: today's ledger lines come at the close.\n\n"),
    ('Waiting on you',
     b"## Waiting on you  **>> UPDATED THIS SESSION**\n\nDecisions, one at a time:\n- None today. Later: which ended missions come next (Pioneer 10,\n  Pioneer 11, Rosetta and DART).\n\nAt the next design talk:\n- How obsolete code is treated, and when it goes (L-509 (obsolete\n  code)); the first case is the orrery's unused date function.\n- The shared link (ruled Oct 29) waits for its build.\n\nNot urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows, and\n   adds a new body as a form (L-489 (compositions)).\n2. The website's second run: keep, or stand down after a clean 08:17\n   (L-485 (a nightly run)).\n3. Earth's list (L-413 (Earth's list)): open as enhancements, or closed\n   with its seven pieces moved to their own items.\n\n",
     b"## Waiting on you  **>> UPDATED THIS SESSION**\n\nDecisions, one at a time:\n- At the standards slice: the Pluto row, what it shows (Pluto or the\n  barycentre) and what it is called (L-150 (trusting a near-equal pair)).\n\nAt the next design talk:\n- How obsolete code is treated, and when it goes (L-509 (obsolete\n  code)); the first case is the orrery's unused date function.\n- The shared link (ruled Oct 29) waits for its build.\n- Planet 9: how to show a body that may not exist.\n\nNot urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows, and\n   adds a new body as a form (L-489 (compositions)).\n2. The website's second run: keep, or stand down after a clean 08:17\n   (L-485 (a nightly run)).\n3. Earth's list (L-413 (Earth's list)): open as enhancements, or closed\n   with its seven pieces moved to their own items.\n\n"),
    ('Where the details are',
     b"## Where the details are  **>> UPDATED THIS SESSION**\n\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- This session: L-512; the map and your rulings; `COORD_L512_slice_a_prompt_20261104.md`.\n- The talk's rulings: `DESIGN_L484_consistency_rulings_20261103.md`.\n- The door: `documentation/python_work_door/`, and L-499.\n- Your run record: `WHERE_WE_ARE_11-4-26_1735_run_record.md`.\n\n",
     b"## Where the details are  **>> UPDATED THIS SESSION**\n\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- This session: your run record `WHERE_WE_ARE_11-4-26_2321_run_record.md`;\n  the website's `patch_L510_1_piece_c_orbit_website.py` and\n  `patch_L510_2_orbit_body_drops_future_points.py`.\n- The talk's rulings: `DESIGN_L484_consistency_rulings_20261103.md`.\n- The door: `documentation/python_work_door/`, and L-499 (kinds of session).\n\n"),
]


def main():
    if not os.path.isfile(TARGET):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % TARGET)
        return 1
    raw = open(TARGET, "rb").read()
    was_crlf = b"\r\n" in raw
    text = raw.replace(b"\r\n", b"\n")
    if text.count(MARKER) != 1:
        print("ERROR: the run-record marker is not on the page once. "
              "Nothing was written.")
        return 1
    top, marker, bottom = text.partition(MARKER)
    if all(new == b"" or top.count(new) == 1 for _, _, new in EDITS) and \
            all(top.count(old) == 0 for _, old, new in EDITS if new == b""):
        print("already there, identical: %s. Nothing to do." % TARGET)
        return 0
    for label, old, new in EDITS:
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s -- expected its text once, found %d. "
                  "If you wrote a note in that section, move it below the "
                  "run-record marker and run again. Nothing was written."
                  % (label, n))
            return 1
        top = top.replace(old, new)
        print("ok %s" % label)
    lines = top.count(b"\n")
    if lines > 130:
        print("ERROR: %d lines above the marker, over the page's 130. "
              "Nothing was written." % lines)
        return 1
    out = top + marker + bottom
    if any(c > 127 for c in out):
        print("ERROR: the result holds non-ASCII bytes. Nothing was written.")
        return 1
    with open(TARGET, "wb") as f:
        f.write(out)
    if was_crlf:
        print("note: %s was CRLF in the working copy; written LF" % TARGET)
    print("ok %s (%d edits; %d lines above the marker)"
          % (TARGET, len(EDITS), lines))
    print("patch applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
