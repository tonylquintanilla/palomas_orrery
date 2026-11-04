"""
patch_L484_3_records_carried.py -- the records patch_L484_2 could not
place: L-484's design talk and Tony's ruling on the three comets, the
eccentricity build's item as L-510, its brief renamed to match, and
Where We Are.

Built on orrery dd84308ed779d288f2a92a7439f8804da2e3bfb7 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), and
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read
only), both read live on Nov 3, 2026, late evening. Written by the
coordinating session (Claude Opus 5.5).

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHY

    Two records patches were written on b09989e0 the same afternoon:
    patch_L476_3_close_20261103.py (L-476 closed, L-509 obsolete code)
    and patch_L484_2_talk_records.py (the talk, the three comets, L-509
    the eccentricity build, L-510 obsolete code). The first ran; the
    second then matched none of its anchors and wrote nothing. Both are
    in documentation/ at dd84308e. L-509 is pushed as obsolete code and
    stays so: a handle is never renumbered. So the eccentricity build
    takes L-510, and its brief, written as L-509, is renamed.

WHAT IT CHANGES (all or nothing)

    LEDGER_CONSOLIDATED.md
      L-484 (the two agree): the talk's rulings, dated; what goes to
        interactive-exhibit's next version (from the record's section
        6, carried by neither patch); Tony's ruling on the three comets,
        in his words, with JPL's answers as the afternoon session read
        them; a records note; a new Gap; its Ref.
      L-510 (the typed fields stop deciding), new.
      L-476 (closed): Ruling 6's line, its start half re-homed to L-510.
    documentation/COORD_L509_drawn_by_eccentricity_brief_20261103.md
      L-509 read as L-510 throughout, its base line moved to this
      patch's push, then RENAMED to
      COORD_L510_drawn_by_eccentricity_brief_20261103.md.
    documentation/WHERE_WE_ARE.md, by section, nothing below the marker.

    Not edited: the design record (history once its rulings are moved
    out) and patch_L484_2 (a delivered patch is final; it stays as the
    record of what was meant).

    The ledger, the brief and Where We Are are checked only at the lines
    this patch edits, so your notes elsewhere never stop it.

RUN COMMAND

    Save this file in the orrery's root folder, open it in VS Code and
    click Run. (python patch_L484_3_records_carried.py)

    Success: one "ok" line per edit, the rename, then "patch applied".
    Failure: one ERROR or ANCHOR FAIL line, and nothing is written.
    Undo is Discard Changes in GitHub Desktop.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
BRIEF_OLD = "documentation/COORD_L509_drawn_by_eccentricity_brief_20261103.md"
BRIEF_NEW = "documentation/COORD_L510_drawn_by_eccentricity_brief_20261103.md"
MARKER = b"--- Your run record below this line"

EDITS = {}

# -------------------------------------------------------------------- ledger
EDITS[LEDGER] = [
    # L-484: the talk, the comets, a records note, the Gap.
    (b"""**Gap (replaces the one below, 2026-11-03, morning):** the design talk:
what consistency means beyond JPL's parameters""",
     b"""- **2026-11-03, 09:06 to 10:13, the design talk's rulings** (Claude
  Fable 5.1; `documentation/DESIGN_L484_consistency_rulings_20261103.md`):
  the words have one home, the orrery's export; the orrery is the
  authority on every layer; exceptions are two kinds kept apart, chosen
  (reason, date, no end) and open (end condition, handle), in a file
  the check reads; the check is bounded by what both draw; five layers
  (object, numbers, span, words, picture meaning) and the unkeyed class
  beside them. Ruling 6 (the typed dates) is on L-476, and its start
  half on L-510.
- **For interactive-exhibit's next version** (the record's section 6):
  Rulings 1, 3 and 5 are method (the same-home test for words, the
  cutting rule, the two kinds of exception and how each is printed,
  the five layers); Ruling 4 joins its Provenance bullet as the
  check's bound.
- **2026-11-03, 15:33 to 15:55 Chicago: TONY'S RULING ON THE THREE
  COMETS** (a coordinating session, Claude Opus 5.5, on orrery
  b09989e0). Tsuchinshan (C/2023 A3), Wierzchos (C/2024 E1) and ATLAS
  (C/2024 G3) are typed 'orbital' in `celestial_objects.py`, so the
  orrery draws an orbit, while the website draws their paths. In his
  words: "They should be drawn as all the Hyperbolic objects." "This is
  not a special class." "The typed class is a legacy of my manual
  method." "I would say e and JPL should agree. And as far as fetching
  we should update with the 30-day check." And, on a comparison with
  JPL's class: "How does JPL determine the class? By e."
  - The ruling as confirmed: each small body's drawing follows its
    eccentricity as of today, fetched on the 30-day cycle; above 1 it
    is drawn as a path, below 1 as an orbit; the typed 'object_type'
    and 'open_path' stop deciding it. No comparison with JPL's class:
    for a comet the class is set by e, so that comparison could not
    fail. Built on L-510; no longer a difference for this item's check.
  - JPL, asked 2026-11-03 by that session: class HYP (hyperbolic
    comet) for all three (the small-body database); eccentricity at
    2026-11-03 00:00 TDB around the Sun (Horizons, ELEMENTS, CENTER
    500@10): Tsuchinshan 1.000186673 (JPL#113), Wierzchos 1.000362756
    (JPL#70), ATLAS 1.000009308 (JPL#29).
- **Records note, 2026-11-03, late evening:** the three lines above
  were written that afternoon in `patch_L484_2_talk_records.py`, which
  wrote nothing: `patch_L476_3_close_20261103.py` had run first on the
  same base, and L-509 went to obsolete code. Placed here by
  `patch_L484_3_records_carried.py`; the eccentricity build is L-510,
  and its brief is
  `documentation/COORD_L510_drawn_by_eccentricity_brief_20261103.md`.
**Gap (replaces the one below, 2026-11-03, late evening):** the brief
for the check's build, then the build with a planted fault. Where its
exceptions live is ruled (two kinds, a file the check reads). The three
comets are ruled and go to L-510.
**Gap (superseded above, 2026-11-03, late evening; replaced the one below, 2026-11-03, morning):** the design talk:
what consistency means beyond JPL's parameters"""),
    (b"""**Ref:** L-443; L-470; L-476; `export_objects.py`; gallery
`data/objects_config.json`.

#### [L-483]""",
     b"""**Ref:** L-443; L-470; L-476; L-510; `export_objects.py`; gallery
`data/objects_config.json`;
`documentation/DESIGN_L484_consistency_rulings_20261103.md`;
`documentation/HANDOFF_L484_after_talk_20261103.md`.

#### [L-483]"""),
    # L-510, new, above L-509.
    (b"""#### [L-509] Obsolete code""",
     b"""#### [L-510] The object list's typed fields stop deciding: a small body drawn by today's eccentricity, a plan asked from before any launch (orrery, the object list and the path plan)
<!-- L:510 status:OPEN upd:2026-11-03 section:A flag: rice: -->
- **Opened 2026-11-03** to carry two rulings that open the same two
  files, `celestial_objects.py` and `path_plan.py`. Both retire a field
  typed by hand, which Tony calls "a legacy of my manual method."
  (Written first as L-509 in `patch_L484_2_talk_records.py`, which never
  applied; see L-484's records note.)
- **1. The drawing follows eccentricity** (Tony's ruling of Nov 3,
  15:33 to 15:55, in his words on L-484 (the two agree)). Each small
  body's drawing follows its eccentricity as of today, fetched on the
  30-day cycle: above 1 a path, below 1 an orbit. The typed
  'object_type' and 'open_path' stop deciding it. The three planned
  comets drawn today as orbits (Tsuchinshan, Wierzchos, ATLAS C/2024
  G3) are the first case, drawn as 3I/ATLAS is.
  - Found that afternoon, for the build: nothing fetches eccentricity on
    the 30-day cycle at b09989e0. The orbital-elements cache
    (`data/osculating_cache.json`) holds e only as of each body's last
    plot: Wierzchos 0.9999997 at 2026-02-25 (below 1, where today's is
    above), ATLAS 1.0000066 at 2026-02-10; Tsuchinshan is not in it. So
    the cached figure cannot decide the drawing; the fetch on the cycle
    does.
  - The bound: 65 small bodies in `celestial_objects.py`, by the
    afternoon session's count. Wierzchos's comment there,
    "near-parabolic, outbound period ~200,000 years", disagrees with
    JPL's class; corrected or removed with the build.
  - Its brief:
    `documentation/COORD_L510_drawn_by_eccentricity_brief_20261103.md`
    (part 1 only), a Claude Code session, Opus, high effort.
- **2. The plan is asked from before any launch** (Ruling 6's start
  half, re-homed from L-476): the plan asks JPL from a date before any
  launch and lets JPL clip the front; the no-dates guard changes; the
  typed start_date fields stop deciding. Its first question is what JPL
  returns when asked from before its data begins. Its own brief, when
  it is next.
- **The skill sentence** on the daily tail (horizons-orbital-mechanics,
  A Plan Draws a Path Only Around the Sun) is carried on L-485; this
  item's build bumps that skill, so it rides that bump.
**Gap:** behind the brief for L-484's check (the road's order); then
part 1's Code session from its brief; then part 2's brief and build.
**Ref:** L-476; L-484; L-485; `documentation/DESIGN_L484_consistency_rulings_20261103.md`,
Ruling 6; `celestial_objects.py`; `path_plan.py`; `period_fetch.py`;
`data/osculating_cache.json`.

#### [L-509] Obsolete code"""),
    # L-476 (closed): Ruling 6 and its start half.
    (b"""**Gap (replaces the one below, 2026-11-03, evening, at the close):**
none; closed.""",
     b"""- **Added after the close, 2026-11-03, late evening: Ruling 6** of
  L-484's design talk (`documentation/DESIGN_L484_consistency_rulings_20261103.md`):
  the typed start_date and end_date come out of the object list; a
  path's span is JPL's first and last day of positions, an ended
  mission stopping at mission_end; the plan asks JPL from a date before
  any launch and lets JPL clip the front; the no-dates guard changes.
  The END half is built here (`test_path_plan.py` check 19: no planned
  entry carries a typed end). The START half is not: it goes to L-510.
  The close above missed it, because the patch that carried it,
  `patch_L484_2_talk_records.py`, could not apply (L-484's records
  note). The three comets, sent to L-484 above, were ruled there and
  are built on L-510.
**Gap (replaces the one below, 2026-11-03, evening, at the close):**
none; closed."""),
]

# --------------------------------------------------------------------- brief
BRIEF_HEADER_OLD = b"""Built on orrery b09989e0d706b4454d7539bd4c392752b64c87bf at
https://github.com/tonylquintanilla/palomas_orrery (branch main), plus
`patch_L484_2_talk_records.py`, which writes L-510 into the ledger;
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read only).
The session starts after Tony's push of that patch, and its first step
confirms HEAD is that push and that L-510 is in the ledger.
"""
BRIEF_HEADER_NEW = b"""Built on orrery b09989e0d706b4454d7539bd4c392752b64c87bf at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read only).
Its item is L-510, placed in the ledger by
`patch_L484_3_records_carried.py` on orrery dd84308e. (Written as L-509;
that handle went to obsolete code the same evening, so this brief was
renamed and its handle changed by that patch.) The session's first step
confirms HEAD is Tony's push of that patch or later, and that L-510 is
in the ledger.
"""

# --------------------------------------------------------- Where We Are page
EDITS[WWA] = [
    (b"""Last updated: November 3, 2026, evening: the coordinating session (your look at the fixed paths passed; L-476 closed).
- Written at orrery b09989e0 and gallery 5abca2c6, plus this session's uncommitted edits.
""",
     b"""Last updated: November 3, 2026, late evening: the coordinating session (the L-484 talk and your comet ruling recorded; they had not landed).
- Written at orrery dd84308e and gallery 5abca2c6, plus this session's uncommitted edits.
"""),
    (b"""> - The desktop orrery draws each spacecraft's and comet's whole
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
""",
     b"""> - The design talk on L-484 (the two agree) is recorded: its rulings
>   are in the ledger and under Settled below
>   (`DESIGN_L484_consistency_rulings_20261103.md`).
> - *Your ruling on the three comets: a small body is drawn by its
>   eccentricity as of today, fetched on the 30-day cycle. Above 1 it
>   is a path, below 1 an orbit. The hand-typed type stops deciding.*
>   JPL agrees today: all three are hyperbolic.
> - New: L-510 (the typed fields stop deciding) carries that build,
>   and a second change: the path plan's start date stops being typed
>   by hand. Its brief is
>   `COORD_L510_drawn_by_eccentricity_brief_20261103.md`.
> - These were written this afternoon in a patch that could not run,
>   because the L-476 close ran first on the same base. This patch
>   places them; the brief was renamed from L509 to L510.
> - L-476 (the orrery plots by the plan) is closed. Obsolete code is
>   L-509 (obsolete code), a talk.
>
> **Do next:** *the brief for the check's build (L-484 (the two
> agree)), written when that build is next. Then L-510's Code session
> from its brief.*
"""),
    (b""" 12c.  [next]  *The two agree (L-484 (the two agree)): every object
               both draw agrees, or the difference is written down.
               A design talk first, on what consistency means beyond
               JPL's numbers; then the check. Its first finding,
               the dates, is fixed (L-476, Nov 3).*
  5b.  [beside] Housekeeping when a session has room: L-424, L-425,
               L-426; L-423 (the website's checks) item 3, L-357;
               L-509 (obsolete code), after its talk. << changed this session
""",
     b""" 12c.  [next]  *The two agree (L-484 (the two agree)): talk done
               Nov 3, rulings in DESIGN_L484_consistency_rulings_20261103.md;
               the three comets ruled Nov 3. Next, the check's brief,
               then its build; then L-510 (the typed fields stop
               deciding).* << changed this session
  5b.  [beside] Housekeeping when a session has room: L-424, L-425,
               L-426; L-423 (the website's checks) item 3, L-357;
               L-509 (obsolete code), after its talk.
"""),
    (b"""- Obsolete code is marked, not deleted, until a talk rules how it is
  treated (Nov 3, 15:14). << new this session
""",
     b"""- A small body is drawn by its eccentricity today, fetched every 30
  days: above 1 a path, below 1 an orbit (Nov 3, 15:55). << new this session
- The words have one home, the orrery's export (Nov 3, the talk). << new this session
- A difference is chosen (a reason, no end) or open (an end and an
  item), the two kept apart (Nov 3, the talk). << new this session
- The check covers only what both draw (Nov 3, the talk). << new this session
- A spacecraft's span is JPL's first and last day; an ended mission
  stops at its end (Nov 3, the talk). << new this session
- Obsolete code is marked, not deleted, until a talk rules how it is
  treated (Nov 3, 15:14).
"""),
    (b"""## Deferred

Waiting behind other work; a line leaves when picked up.
""",
     b"""## Deferred  **>> UPDATED THIS SESSION**

Waiting behind other work; a line leaves when picked up.
- L-510 (the typed fields stop deciding): the drawing by eccentricity,
  the three comets first, then the path plan asked from before any
  launch. Behind the check's brief (Nov 3). << new this session
"""),
    (b"""- *What consistency means between the orrery and the website, beyond
  JPL's numbers (L-484 (the two agree)).* Two differences are left for
  it: three comets the orrery draws as ellipses and the website as
  paths, and the website's extra points on a path's last day.
- How obsolete code is treated: removed, kept as a stub, or kept
  whole, and when (L-509 (obsolete code)). The first case is the
  orrery's unused date function, marked Nov 3. << new this session
""",
     b"""- How obsolete code is treated: removed, kept as a stub, or kept
  whole, and when (L-509 (obsolete code)). The first case is the
  orrery's unused date function, marked Nov 3.
"""),
    (b"""- The next talk: `HANDOFF_L484_consistency_talk_20261103.md` (L-484
  (the two agree)).
""",
     b"""- The talk's rulings: `DESIGN_L484_consistency_rulings_20261103.md`
  (L-484 (the two agree)); the afternoon's handoff,
  `HANDOFF_L484_after_talk_20261103.md`.
- The next build after the check: L-510's brief,
  `COORD_L510_drawn_by_eccentricity_brief_20261103.md`.
"""),
]


def main():
    if os.path.basename(ROOT) == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation/. NOTHING was written.")
        return 1
    new_brief = os.path.join(ROOT, *BRIEF_NEW.split("/"))
    old_brief = os.path.join(ROOT, *BRIEF_OLD.split("/"))
    if os.path.exists(new_brief) and not os.path.exists(old_brief):
        print("ERROR: %s already exists and the L509 brief is gone: this "
              "patch has run. Nothing more to do. NOTHING was written."
              % BRIEF_NEW)
        return 1
    if os.path.exists(new_brief):
        print("ERROR: %s already exists beside the L509 brief. If it is a "
              "copy you saved by hand, delete it and run again. NOTHING was "
              "written." % BRIEF_NEW)
        return 1
    staged = []
    for name in (LEDGER, WWA):
        path = os.path.join(ROOT, *name.split("/"))
        if not os.path.exists(path):
            print("ERROR: %s not found. Save the patch in the orrery's root "
                  "folder. NOTHING was written." % name)
            return 1
        raw = open(path, "rb").read()
        lf = raw.replace(b"\r\n", b"\n")
        below = lf[lf.index(MARKER):] if name == WWA else None
        for old, new in EDITS[name]:
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. If "
                      "this patch already ran, there is nothing to do. "
                      "NOTHING was written." % (name, n, old[:60]))
                return 1
            lf = lf.replace(old, new)
            print("ok  %s: %s" % (name, old.strip().splitlines()[0][:60]
                                  .decode("ascii")))
        if below is not None and lf[lf.index(MARKER):] != below:
            print("ERROR: an edit reached below the run-record marker. "
                  "NOTHING was written.")
            return 1
        staged.append((name, path, lf, b"\r\n" in raw))
    if not os.path.exists(old_brief):
        print("ERROR: %s not found. NOTHING was written." % BRIEF_OLD)
        return 1
    raw = open(old_brief, "rb").read()
    blf = raw.replace(b"\r\n", b"\n")
    n = blf.count(b"L-509")
    if n != 9:
        print("ANCHOR FAIL: the L509 brief names L-509 %d times, not the 9 "
              "this patch was built on. NOTHING was written." % n)
        return 1
    blf = blf.replace(b"L-509", b"L-510")
    if blf.count(BRIEF_HEADER_OLD) != 1:
        print("ANCHOR FAIL: the L509 brief's base lines are not as built "
              "on. NOTHING was written.")
        return 1
    blf = blf.replace(BRIEF_HEADER_OLD, BRIEF_HEADER_NEW)
    print("ok  brief: 9 mentions of L-509 read as L-510; base lines moved")
    for _o, new in [e for name in EDITS for e in EDITS[name]] + \
            [(None, BRIEF_HEADER_NEW)]:
        if any(c > 127 for c in new):
            print("ERROR: inserted text holds non-ASCII. NOTHING was "
                  "written.")
            return 1
    total = 0
    for name, path, lf, was_crlf in staged:
        with open(path, "wb") as handle:
            handle.write(lf)
        total += len(lf)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    with open(old_brief, "wb") as handle:
        handle.write(blf)
    os.replace(old_brief, new_brief)
    total += len(blf)
    print("renamed: %s -> %s" % (BRIEF_OLD, BRIEF_NEW))
    print("stamps updated: WHERE_WE_ARE.md (Last updated line); the brief's "
          "base lines")
    print("patch applied (%d bytes, 3 files, one renamed)" % total)
    print()
    print("Do next, in order:")
    print("  1. Run the maintenance run from the dashboard. Its Ledger index")
    print("     line should say it rewrote the index (L-510 is new). Its last")
    print("     line: all gating checkers passed, Tier-1 0 on the gate path.")
    print("  2. Move this patch into documentation/, then commit and push the")
    print("     orrery in GitHub Desktop. It shows the brief as renamed.")
    print("  3. Next: the brief for L-484's check, when that build is next.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
