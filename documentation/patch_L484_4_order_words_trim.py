"""
patch_L484_4_order_words_trim.py -- the night review's four gaps:
L-510 goes before the check (Tony, Nov 3, 21:23: "yes"); the words get
their own item, L-511; interactive-exhibit's next version gets an owner;
Where We Are trimmed back under its cap.

Built on orrery 3a01b250bd5061e0d3f7c4c26a08ab50d2c45d4f at
https://github.com/tonylquintanilla/palomas_orrery (branch main), and
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read
only: the swap log's last line), both read live on Nov 3, 2026, night.
Written by the coordinating session (Claude Opus 5.5) from a review by
Claude Fable 5.1 that Tony carried.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT IT CHANGES (two files, all or nothing)

    LEDGER_CONSOLIDATED.md
      L-511 (the export carries the words), new.
      L-510 (the typed fields stop deciding): next on the road, before
        the check.
      L-484 (the two agree): the review's four points; a new Gap.
    documentation/WHERE_WE_ARE.md, section by section, above the
      marker only: the box, the road (12d new, 12c after it), Settled,
      Deferred, Signals, Waiting on you, Where the details are. It goes
      from 186 lines above the marker to 129.

    The trim: Settled lines whose rule is now written in a skill or the
    protocol left the page (the plan drawing only around the Sun, an
    ended mission stopping at mission_end and its marker on its last
    day, past voyages on today's date, the x marks, UTC and Pluto's
    period, the token economy); others were shortened. Every line
    replaced is held in this file's edits below, so the archived patch
    is their record, beside git.

    The ledger and Where We Are are checked only at the sections this
    patch edits, so your notes elsewhere never stop it.

RUN COMMAND

    Save this file in the orrery's root folder, open it in VS Code and
    click Run. (python patch_L484_4_order_words_trim.py)

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line, and nothing is written. Undo is Discard
    Changes in GitHub Desktop.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = b"--- Your run record below this line"
CAP = 130

EDITS = [
    ("LEDGER_CONSOLIDATED.md", [(b"#### [L-510] The object list's typed fields", b"#### [L-511] The orrery's export carries the words the website prints (orrery + gallery, the words)\n<!-- L:511 status:OPEN upd:2026-11-03 section:A flag: rice: -->\n- **Opened 2026-11-03, night**, from a review of the day's records\n  (L-484 (the two agree)). The design talk ruled that the words have one\n  home, the orrery's export\n  (`documentation/DESIGN_L484_consistency_rulings_20261103.md`). The\n  website's hovers, tooltips, text boxes and i panel then print from\n  that export. At 3a01b250 the export carries only the mirrored\n  description, so L-484's check can test the words only for that.\n- One row for the class: every kind of words the website prints that\n  the export does not yet carry. Which kinds move, and the cutting rule\n  for each (interactive-exhibit's next version, L-484), are this\n  item's design.\n**Gap:** behind L-484's check; a design of which words move, then the\nbuild.\n**Ref:** L-484; `export_objects.py`; gallery `interactive.html`;\n`documentation/DESIGN_L484_consistency_rulings_20261103.md`.\n\n#### [L-510] The object list's typed fields"), (b"**Gap:** behind the brief for L-484's check (the road's order); then\npart 1's Code session from its brief; then part 2's brief and build.", b'**Gap (replaces the one below, 2026-11-03, night):** next on the road,\nbefore L-484\'s check (Tony, Nov 3, 21:23: "yes"): part 1\'s Claude Code\nsession from its brief; then part 2\'s brief and build.\n**Gap (superseded above, 2026-11-03, night):** behind the brief for L-484\'s check (the road\'s order); then\npart 1\'s Code session from its brief; then part 2\'s brief and build.'), (b"**Gap (replaces the one below, 2026-11-03, late evening):** the brief\nfor the check's build", b'- **2026-11-03, night: a review of the day\'s records** (Claude Fable\n  5.1, at orrery 3a01b250, carried by Tony) found four gaps, placed by\n  `patch_L484_4_order_words_trim.py`:\n  - The words (layer 4) have no build. The words rule means the\n    website\'s hovers, tooltips, text boxes and i panel print from the\n    orrery\'s export, which carries only the mirrored description. So\n    this item\'s brief slices: layers 1, 2, 3 and 5 now, layer 4 for the\n    mirrored description only. The rest of the words is L-511 (the\n    export carries the words).\n  - The order. Asked whether L-510 (the typed fields stop deciding)\n    part 1 is built before this check, Tony, 21:23: "yes". Its brief is\n    written, and the check\'s first run then has no comet differences to\n    record and later delete.\n  - interactive-exhibit\'s bump has an owner. The check is built in the\n    website repository, and a gallery session does not edit the\n    orrery\'s skills. So the coordinating session that writes this\n    item\'s brief also writes interactive-exhibit\'s next version (Rulings\n    1, 3 and 5 as method, Ruling 4 as the check\'s bound, the cutting\n    rule) as an orrery records patch, run before the check\'s build.\n  - Where We Are stood at 187 lines above its marker against a cap of\n    130; trimmed in the same patch.\n**Gap (replaces the one below, 2026-11-03, night):** after L-510 part 1\n(Tony, 21:23): this item\'s brief, sliced as above, with\ninteractive-exhibit\'s next version written beside it as an orrery\nrecords patch; then the build with a planted fault.\n**Gap (superseded above, 2026-11-03, night; replaced the one below, 2026-11-03, late evening):** the brief\nfor the check\'s build')]),
    ("documentation/WHERE_WE_ARE.md", [(b"Last updated: November 3, 2026, late evening: the coordinating session (the L-484 talk and your comet ruling recorded; they had not landed).\n- Written at orrery dd84308e and gallery 5abca2c6, plus this session's uncommitted edits.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - The design talk on L-484 (the two agree) is recorded: its rulings\n>   are in the ledger and under Settled below\n>   (`DESIGN_L484_consistency_rulings_20261103.md`).\n> - *Your ruling on the three comets: a small body is drawn by its\n>   eccentricity as of today, fetched on the 30-day cycle. Above 1 it\n>   is a path, below 1 an orbit. The hand-typed type stops deciding.*\n>   JPL agrees today: all three are hyperbolic.\n> - New: L-510 (the typed fields stop deciding) carries that build,\n>   and a second change: the path plan's start date stops being typed\n>   by hand. Its brief is\n>   `COORD_L510_drawn_by_eccentricity_brief_20261103.md`.\n> - These were written this afternoon in a patch that could not run,\n>   because the L-476 close ran first on the same base. This patch\n>   places them; the brief was renamed from L509 to L510.\n> - L-476 (the orrery plots by the plan) is closed. Obsolete code is\n>   L-509 (obsolete code), a talk.\n>\n> **Do next:** *the brief for the check's build (L-484 (the two\n> agree)), written when that build is next. Then L-510's Code session\n> from its brief.*\n>\n> **Needs you now:**\n> - *(do) Each morning, Pull origin on both, orrery then website, first;\n>   do not wait for the night, which GitHub starts hours late or drops.*\n\n*Italic* lines are the must-reads. Marks reset at every update.\n\n", b"Last updated: November 3, 2026, night: the coordinating session (L-510 goes before the check; the words get their own item; this page trimmed).\n- Written at orrery 3a01b250 and gallery 5abca2c6, plus this session's uncommitted edits.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - L-510 (the typed fields stop deciding) is built before the check,\n>   by your word of Nov 3, 21:23. Its brief is ready.\n> - New: L-511 (the export carries the words). Until it is built, the\n>   check tests the words only for the mirrored description.\n> - The check's brief session also writes interactive-exhibit's next\n>   version, as an orrery patch run before the check is built.\n> - This page is back under its length cap. Settled lines whose rule is\n>   now written in a skill or the protocol have left it.\n>\n> **Do next:** *L-510's Claude Code session (Opus, high effort), from\n> `COORD_L510_drawn_by_eccentricity_brief_20261103.md`; then the\n> check's brief (L-484 (the two agree)).*\n>\n> **Needs you now:**\n> - *(do) Each morning, Pull origin on both, orrery then website, first;\n>   do not wait for the night, which GitHub starts hours late or drops.*\n\n*Italic* lines are the must-reads. Marks reset at every update.\n\n"), (b"## The road  **>> UPDATED THIS SESSION**\n\nOct 27's order, changed Oct 29 (`DESIGN_L314_solar_wind_rulings_20261029.md`).\n  1-11.[done]  All but 5b and 9: the three rooms live; typed facts\n               and periods checked (Oct 14-16); the Sun's slice (Oct 27);\n               the objects (L-443 (the objects)), the small builds and\n               2026 ED138 (Oct 28); the belt's cloud (L-503, Nov 1);\n               Earth's list (L-413), the ruler build (L-505) and the\n               Sun's eight (L-411), Nov 2; historical missions' slice 1\n               (L-507), Nov 2; the orrery's paths by the plan\n               (L-476), Nov 3.\n 5d.   [NOW]   *The orrery's clock (L-504 (the orrery's clock)): the\n               data path done Oct 29, the website's date fix Oct 31;\n               Earth System, stamps, tools next.*\n 11b.  [NOW]   *The nightly run (L-485 (a nightly run)): both halves run\n               on GitHub; the hold built Oct 31; both second times built\n               (11:17 and 12:17 UTC, Nov 1); a week of mornings now.*\n 12c.  [next]  *The two agree (L-484 (the two agree)): talk done\n               Nov 3, rulings in DESIGN_L484_consistency_rulings_20261103.md;\n               the three comets ruled Nov 3. Next, the check's brief,\n               then its build; then L-510 (the typed fields stop\n               deciding).* << changed this session\n  5b.  [beside] Housekeeping when a session has room: L-424, L-425,\n               L-426; L-423 (the website's checks) item 3, L-357;\n               L-509 (obsolete code), after its talk.\n 12b.  [later] Historical missions, slice 2: encounters, the planet\n               where it was when the spacecraft arrived; the room moves\n               off today's date; Artemis II in the Earth room.\n 12.   [later] Compositions (L-489 (compositions)). Encounters\n               are both: the Solar System room as today, and a room of\n               their own; Artemis II first (Nov 1).\n 13.   [later] The inner planets' rooms, from the template; Jupiter and\n               Saturn follow (L-433).\n 14.   [later] The Earth System layers, beside 13; cards meanwhile.\n 15.   [goal]  The website does what the desktop orrery does, with a date\n               to choose, within the range the data covers.\n\n", b"## The road  **>> UPDATED THIS SESSION**\n\nOct 27's order, changed Oct 29 (`DESIGN_L314_solar_wind_rulings_20261029.md`).\n  1-11.[done]  All but 5b and 9, through Nov 3: the three rooms, the\n               objects, the Sun's and Earth's slices, historical\n               missions' slice 1, the orrery's paths by the plan (L-476).\n 5d.   [NOW]   *The orrery's clock (L-504 (the orrery's clock)): the\n               data path done Oct 29, the website's date fix Oct 31;\n               Earth System, stamps, tools next.*\n 11b.  [NOW]   *The nightly run (L-485 (a nightly run)): both halves run\n               on GitHub; the hold built Oct 31; both second times built\n               (11:17 and 12:17 UTC, Nov 1); a week of mornings now.*\n 12d.  [next]  *L-510 (the typed fields stop deciding), part 1: a small\n               body drawn by its eccentricity. Brief ready.* << new this session\n 12c.  [next]  *Then the two agree (L-484 (the two agree)): talk done\n               Nov 3; its brief, then its build. The words wait for\n               L-511 (the export carries the words).* << changed this session\n  5b.  [beside] Housekeeping when a session has room: L-424, L-425,\n               L-426; L-423 (the website's checks) item 3, L-357;\n               L-509 (obsolete code), after its talk.\n 12b.  [later] Historical missions, slice 2: encounters, the room off\n               today's date; Artemis II in the Earth room.\n 12.   [later] Compositions (L-489 (compositions)): encounters in\n               rooms of their own; Artemis II first (Nov 1).\n 13.   [later] The inner planets' rooms, from the template; Jupiter and\n               Saturn follow (L-433).\n 14.   [later] The Earth System layers, beside 13; cards meanwhile.\n 15.   [goal]  The website does what the desktop orrery does, with a date\n               to choose, within the range the data covers.\n\n"), (b"## Settled  **>> UPDATED THIS SESSION**\n\nStanding rulings. A line leaves after a few weeks, once it is habit.\n- A small body is drawn by its eccentricity today, fetched every 30\n  days: above 1 a path, below 1 an orbit (Nov 3, 15:55). << new this session\n- The words have one home, the orrery's export (Nov 3, the talk). << new this session\n- A difference is chosen (a reason, no end) or open (an end and an\n  item), the two kept apart (Nov 3, the talk). << new this session\n- The check covers only what both draw (Nov 3, the talk). << new this session\n- A spacecraft's span is JPL's first and last day; an ended mission\n  stops at its end (Nov 3, the talk). << new this session\n- Obsolete code is marked, not deleted, until a talk rules how it is\n  treated (Nov 3, 15:14).\n- A plan draws a path only around the Sun, in both the orrery and the\n  website; around any other body the path is drawn as before (Nov 3,\n  12:06).\n- An ended mission's line stays solid, like a flown path (Nov 3, your\n  look).\n- An ended mission's path stops on the day NASA gives as its end, not\n  where JPL's data runs out: Galileo at its impact (Nov 2).\n- The Sun and Earth slices are closed: your phone look passed all seven\n  (Nov 2, evening; ruled 13:47). What is left is enhancements.\n- The comet switch is off the road: the six record numbers stay, and\n  the Horizons check is relied on (Nov 2, evening).\n- A held body is loud until a ledger item names it, then quiet with the\n  item's number; it clears when the item is done, and is loud again if\n  JPL still disagrees. Every held body, not only comets (Nov 2, evening).\n- Past voyages are drawn on today's date, their path over the\n  mission's own dates; only encounters move the room's date (Nov 2, 14:32).\n- An ended mission's marker sits where it was on its last day, the\n  line solid; its text box says when it ended (Nov 2, the Fable talk).\n- The ticks stay as built, 3 and 6, and so do the ruler and the halo (Nov 2).\n- Tokens are spent where they buy verification or a decision: the\n  smallest instrument, no document before its session, a skill read in\n  the parts the job needs, and a token count in every Code report (Nov 2).\n- The ticks are x marks, not dots: an x means nothing in the scene,\n  circles are bodies, crosses are hover points (Oct 31, 20:43; restored Nov 2).\n- Encounters are both: shown in the Solar System room as today, and in\n  a room centred on the body met, with its shells and fuller words (Nov 1).\n- A night takes a value JPL changed, holds only an identity (the index\n  and the kind included); the guest book stays out of it (Oct 31).\n- UTC everywhere; the orbit's date stays on JPL's clock; Pluto's period\n  is its centre of mass's, as Earth's is (Oct 28-29).\n- The main belt: random dots in JPL's spread; a new body's hover prints its orbit numbers (Oct 28).\n\n", b"## Settled  **>> UPDATED THIS SESSION**\n\nStanding rulings. A line leaves after a few weeks, once it is habit, or\nonce a skill or the protocol carries it (trimmed Nov 3, night).\n- A small body is drawn by its eccentricity today, fetched every 30\n  days: above 1 a path, below 1 an orbit (Nov 3, 15:55).\n- From the talk (Nov 3): the words have one home, the orrery's export;\n  a difference is chosen (a reason, no end) or open (an end and an\n  item); the check covers only what both draw; a spacecraft's span is\n  JPL's first and last day.\n- Obsolete code is marked, not deleted, until a talk rules (Nov 3).\n- An ended mission's line stays solid, like a flown path (Nov 3).\n- The Sun and Earth slices are closed; what is left is enhancements\n  (Nov 2).\n- The comet switch is off the road: the six record numbers stay (Nov 2).\n- A held body is loud until a ledger item names it, then quiet with the\n  item's number; loud again if JPL still disagrees (Nov 2).\n- The ticks stay as built, 3 and 6, and so do the ruler and the halo (Nov 2).\n- Encounters are both: shown in the Solar System room, and in a room\n  centred on the body met (Nov 1).\n- A night takes a value JPL changed, holds only an identity (Oct 31).\n- The main belt: random dots in JPL's spread (Oct 28).\n\n"), (b"## Deferred  **>> UPDATED THIS SESSION**\n\nWaiting behind other work; a line leaves when picked up.\n- L-510 (the typed fields stop deciding): the drawing by eccentricity,\n  the three comets first, then the path plan asked from before any\n  launch. Behind the check's brief (Nov 3). << new this session\n- L-508 (a held body's alarm): the records skill's next version, with\n  provenance-discipline's pointer; then its build, with the hold's\n  website half (Nov 2).\n- L-485 (a nightly run): the hold's website half, with its asking by\n  name and its six notes; a gallery session (Oct 31).\n- L-462 (a shorter run): whether it stays, now the night exists; L-128\n  (the ice lines), already waiting.\n- L-500 (eyeballed numbers): the belt's seven, the clumps' five (Oct 27).\n- L-471 (a delivered patch is final): safe-file-editing's next version.\n- L-483 (a comet room), after slice 2; L-484 (the two agree): its check.\n- L-489 (compositions), with L-486 (a view carried into a room) and\n  L-488 (the heliopause) under it: Artemis II in the Earth room first,\n  its entry served before its room, with historical missions' slice 2\n  (L-507 (historical missions)).\n- L-490 (the legacy list): who holds the accounts; L-499 (kinds of session), Oct 27.\n\n", b"## Deferred  **>> UPDATED THIS SESSION**\n\nWaiting behind other work; a line leaves when picked up.\n- L-511 (the export carries the words): behind the check (Nov 3). << new this session\n- L-508 (a held body's alarm): the records skill's next version, then\n  its build, with the hold's website half (Nov 2).\n- L-485 (a nightly run): the hold's website half; a gallery session (Oct 31).\n- L-462 (a shorter run); L-128 (the ice lines); L-500 (eyeballed numbers).\n- L-483 (a comet room), after historical missions' slice 2.\n- L-489 (compositions), with L-486 and L-488 under it: Artemis II in\n  the Earth room first, with slice 2 (L-507 (historical missions)).\n- L-490 (the legacy list); L-499 (kinds of session); L-471 (a delivered\n  patch is final), for safe-file-editing's next version.\n\n"), (b"## Signals  **>> UPDATED THIS SESSION**\n\nRead from files when this page was written, not typed from memory.\n- Last cache build: 20261103T193343Z, ok, no retry (the website's swap\n  log's last line at 5abca2c6: a nightly-mode build of Nov 3).\n- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md\n  at b09989e0, your maintenance run of the evening).\n- This page's date and the ledger's newest stamp: both Nov 3. Agree.\n\n", b"## Signals  **>> UPDATED THIS SESSION**\n\nRead from files when this page was written, not typed from memory.\n- Last cache build: 20261103T193343Z, ok, no retry (swap log at 5abca2c6).\n- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at dd84308e).\n- This page's date and the ledger's newest stamp: both Nov 3. Agree.\n\n"), (b"## Waiting on you  **>> UPDATED THIS SESSION**\n\nDecisions, one at a time:\n- None today. Later, not now: which ended missions come next. The orrery also\n  lists Pioneer 10, Pioneer 11, Rosetta and DART.\n\nAt the next design talk:\n- How obsolete code is treated: removed, kept as a stub, or kept\n  whole, and when (L-509 (obsolete code)). The first case is the\n  orrery's unused date function, marked Nov 3.\n- The shared link (ruled Oct 29) waits for its build.\n\nNot urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows, and\n   adds a new body as a form (L-489 (compositions)).\n2. The website's second run makes a fresh build and a second commit\n   most days: keep, or stand down after a clean 08:17 (L-485 (a nightly run)).\n3. Earth's list (L-413 (Earth's list)): stays open as Earth's enhancements, or closes\n   with its seven pieces moved to their own items.\n\n", b"## Waiting on you\n\nDecisions, one at a time:\n- None today. Later: which ended missions come next (the orrery also\n  lists Pioneer 10, Pioneer 11, Rosetta and DART).\n\nAt the next design talk:\n- How obsolete code is treated, and when it goes (L-509 (obsolete\n  code)); the first case is the orrery's unused date function.\n- The shared link (ruled Oct 29) waits for its build.\n\nNot urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows, and\n   adds a new body as a form (L-489 (compositions)).\n2. The website's second run: keep, or stand down after a clean 08:17\n   (L-485 (a nightly run)).\n3. Earth's list (L-413 (Earth's list)): open as enhancements, or closed\n   with its seven pieces moved to their own items.\n\n"), (b"## Where the details are\n\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- The talk's rulings: `DESIGN_L484_consistency_rulings_20261103.md`\n  (L-484 (the two agree)); the afternoon's handoff,\n  `HANDOFF_L484_after_talk_20261103.md`.\n- The next build after the check: L-510's brief,\n  `COORD_L510_drawn_by_eccentricity_brief_20261103.md`.\n- Today: L-476 (the orrery plots by the plan), closed, with what was\n  verified; the brief\n  `COORD_L476_orrery_plots_by_path_plan_brief_20261103.md`; the fix\n  `patch_L476_2_tail_at_today.py`.\n- The door: `documentation/python_work_door/`, and L-499.\n- The Sun's eight: `COORD_L411_sun_eight_held_numbers_brief_20261102.md`\n  and `WORDS_L411_sun_eight_20261102.md`.\n- Your run record: `WHERE_WE_ARE_11-3-26_1158_run_record.md`.\n\n", b"## Where the details are\n\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- Next: L-510's brief, `COORD_L510_drawn_by_eccentricity_brief_20261103.md`.\n- The talk's rulings: `DESIGN_L484_consistency_rulings_20261103.md`.\n- The door: `documentation/python_work_door/`, and L-499.\n- Your run record: `WHERE_WE_ARE_11-3-26_1158_run_record.md`.\n\n")]),
]


def main():
    if os.path.basename(ROOT) == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation/. NOTHING was written.")
        return 1
    staged = []
    for name, edits in EDITS:
        path = os.path.join(ROOT, *name.split("/"))
        if not os.path.exists(path):
            print("ERROR: %s not found. Save the patch in the orrery's root "
                  "folder. NOTHING was written." % name)
            return 1
        raw = open(path, "rb").read()
        lf = raw.replace(b"\r\n", b"\n")
        page = name.endswith("WHERE_WE_ARE.md")
        below = lf[lf.index(MARKER):] if page else None
        for old, new in edits:
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. If "
                      "this patch already ran, there is nothing to do. "
                      "NOTHING was written." % (name, n, old[:60]))
                return 1
            lf = lf.replace(old, new)
            print("ok  %s: %s" % (name, old.strip().splitlines()[0][:60]
                                  .decode("ascii")))
            if any(c > 127 for c in new):
                print("ERROR: inserted text holds non-ASCII. NOTHING was "
                      "written.")
                return 1
        if page:
            if lf[lf.index(MARKER):] != below:
                print("ERROR: an edit reached below the run-record marker. "
                      "NOTHING was written.")
                return 1
            above = lf[:lf.index(MARKER)].count(b"\n")
            if above > CAP:
                print("ERROR: the page would have %d lines above its marker, "
                      "over its cap of %d. NOTHING was written." % (above, CAP))
                return 1
            print("ok  the page: %d lines above the marker (cap %d)"
                  % (above, CAP))
        staged.append((name, path, lf, b"\r\n" in raw))
    total = 0
    for name, path, lf, was_crlf in staged:
        with open(path, "wb") as handle:
            handle.write(lf)
        total += len(lf)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("stamps updated: WHERE_WE_ARE.md (Last updated line)")
    print("patch applied (%d bytes, 2 files)" % total)
    print()
    print("Do next, in order:")
    print("  1. Run the maintenance run from the dashboard. Its Ledger index")
    print("     line should say it rewrote the index (L-511 is new). Its last")
    print("     line: all gating checkers passed, Tier-1 0 on the gate path.")
    print("  2. Move this patch into documentation/, then commit and push the")
    print("     orrery in GitHub Desktop.")
    print("  3. Next: L-510's Claude Code session, from")
    print("     COORD_L510_drawn_by_eccentricity_brief_20261103.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
