"""
patch_L269_2_tier_split_and_pipeline_measurement.py

Run:  python patch_L269_2_tier_split_and_pipeline_measurement.py
From: the ORRERY repo root (the folder holding LEDGER_CONSOLIDATED.md and
      PROJECT_INSTRUCTIONS.md).
In VS Code: open this file from that folder and click Run.

Built on orrery a667e12824db71f5cc1ddd1503c1afe72db4a986 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

SEQUENCE. This is the SECOND patch in the L-269 pair.
patch_L269_1_ledger_blocks_and_protocol_v3_49.py ran at ded99fbe and is
already in the tree; this one edits what that one wrote. Running them out
of order aborts safely on the fingerprints.

WHY THIS EXISTS. Patch 1 landed the rule at [CRITICAL], as one section.
A second Opus session reviewed it the same evening and made two arguments
that hold, and Tony carried them across. This patch applies both, plus a
measurement that changes what the rule's founding case actually says.

  ONE -- THE TIER, on this document's own promotion test: a check moves
  up when a failure demonstrates it was load-bearing. The NAMING half has
  failed repeatedly and in view -- the scanner summary, the audit's
  coordinates, the L-268 sweep's first pass, the pipeline count -- and
  every one of those was recoverable. The COUNT-DELTA half has NOT been
  witnessed here; it is inferred, and it is the half that can pass while
  blind.

  TWO -- THE SPLIT follows from one. The sharp case goes INTO A Check
  That Cannot Fail Is Not Passing, which is already [CRITICAL], as its
  fourth move. The general habit stays where it is at [QUALITY]. The
  critical tier only works while it stays short, and this leaves a clean
  promotion path if the delta case ever bites.

  THREE -- THE MEASUREMENT. Patch 1 said the five pipelines were "named
  nowhere" and left naming them as a judgment call. Measured at ded99fbe,
  the number is worse than unnamed. It is UNDECIDABLE. Six functions in
  palomas_orrery.py acquire position data; README.md names a DIFFERENT
  five that span several files; and the gate's own paragraph straddles
  both readings -- it scopes the count to one file, then names
  gallery_studio.py and json_converter.py. 46 documents carry the
  sentence, four of them live stores including a skill that loads every
  orrery session.

WHAT IT DOES (two files, six edits, all-or-nothing).

  PROJECT_INSTRUCTIONS.md
    1. "Three moves" -> "Four moves" in A Check That Cannot Fail.
    2. That gate gains the fourth move: make the delta name what moved.
    3. A Report Names Its Items goes [CRITICAL] -> [QUALITY], loses the
       count-delta paragraph that moved up, gains the tier reasoning, and
       its origin note carries the measurement.
    4. The v3.49 version-history entry is rewritten to match. The version
       number does NOT change: v3.49 was pushed today and this is the
       same day's rule reaching its settled form, not a new one.

  LEDGER_CONSOLIDATED.md
    5. L-269: the proposed-tier note becomes the ruling, and the Gap
       becomes the measurement -- the six function names, the two
       readings, and the four live stores.
    6. L-262's Ref line: the tier on A Report Names Its Items.

WHAT IT STILL DOES NOT DO. Check All Parallel Pipelines is left exactly
as it stands. Choosing between the two readings changes what the gate
INSTRUCTS, so it is a ruling and not an edit. L-269 now carries the
measurement so the next session verifies rather than rediscovers.

SUCCESS: one "ok" line per edit, a byte count per file, "PATCH APPLIED".
FAILURE: one "ERROR" or "ANCHOR FAIL" line and NOTHING written.
One-shot; a second run aborts on the fingerprints.
"""

import hashlib
import os
import sys

EXPECTED = {
    "LEDGER_CONSOLIDATED.md": "d53f927ae8d5b60d3a799f5a13305dd8",
    "PROJECT_INSTRUCTIONS.md": "1a30d270c34ecec6d88bf26467f10b46",
}

# ---------------------------------------------------------------------------
# EDIT 1 + 2 -- A Check That Cannot Fail Is Not Passing gains a fourth move
# ---------------------------------------------------------------------------

MOVES_COUNT_OLD = b"Three moves, in order of how often they are the answer:"
MOVES_COUNT_NEW = b"Four moves, in order of how often they are the answer:"

FOURTH_OLD = b"""- Put the check where it runs. A check in a store nobody opens is a
  check that cannot fail, no matter how correct it is. Prefer the tool
  already in the routine over the file that has to be remembered.
"""

FOURTH_NEW = b"""- Put the check where it runs. A check in a store nobody opens is a
  check that cannot fail, no matter how correct it is. Prefer the tool
  already in the routine over the file that has to be remembered.
- Make the delta name what moved. A check that reports a COUNT delta
  cannot fail: clear one finding and gain another between runs and the
  total is identical, so a real change and no change print the same
  line. Compare NAMES. PROVENANCE_AUDIT.md's "No file's Tier-1 count
  rose" and a run history tracking one number per run are both that
  shape. (The general habit this is the sharp end of is A Report Names
  Its Items, below.)
"""

# ---------------------------------------------------------------------------
# EDIT 3 -- the section itself, [CRITICAL] -> [QUALITY], count-delta removed
# ---------------------------------------------------------------------------

SECTION_OLD = b"""A Report Names Its Items [CRITICAL]
Companion to the gate above, and it reaches every report this project
produces, not only checks. A count states a SIZE. Names state what is
there. A report that gives the size and withholds the names is complete
only for a reader who can go and find out WHAT -- and neither reader
here can. Claude resets every session and will not think to open the
file. Tony cannot read everything and does not grep: "I can't go grep
the code for all the instances that built a count. A list is manageable
and it gives me a sense of the gap."

So a report has to be complete enough to ACT ON WHERE IT LANDS.

The names also carry the SHAPE, which no number can. "16" is a size.
"D Ring, C Ring, B Ring, A Ring, F Ring, G Ring, E Ring" says it is the
whole of one body's ring system, one kind of thing, mechanical rather
than seven separate judgments.

AND A COUNT CAN BE IDENTICAL ACROSS A REAL CHANGE. Clear one finding in
a file and introduce another in the same file, and a count-based delta
reports that nothing moved. That is why this sits beside the gate above
rather than in a style guide: a count-based report is a check that
cannot fail.

It is count AND names, not names instead of the count. MODULE_ATLAS.md
is the worked example -- "Undetermined role (4)" followed immediately by
the four filenames.

The scope is every place this project reports a set:
- Scanner and runner summaries, and their run histories. A delta over
  counts cannot see a swap; a delta over names can.
- Ledger and handoff enumerations, which name the handles.
- Counted claims in this document and in the skills. "Three moves" and
  "two limits" name what they count; "5 parallel pipelines" does not.
- Findings, gaps and backlogs -- named by CLASS where the instance list
  is long, since The Braid already rules that a backlog grows by kinds
  rather than by counts.

Where the full list genuinely cannot land, name the CLASSES and give
the exact path where the instances live. A bare pointer is not enough:
the provenance scanner prints "292 TIER-1 FINDINGS IN THE SCANNED
TREE", explains that this is not the gate, and sends the reader to
another document -- the number a reader needs absent, the number
present wrong, and nothing named at all.

A coordinate is not a name. PROVENANCE_AUDIT.md reporting "display
string @ line 936" is better than a count and still requires opening
the file to learn the thing is hover_text_sun_and_corona.

(Tony's ruling, August 30, 2026; L-269. Three instances measured that
session, spanning the range: MODULE_ATLAS.md doing it right, the
scanner summary doing it not at all, PROVENANCE_AUDIT.md naming a
coordinate. This document's own Check All Parallel Pipelines is an
unmet instance -- it counts five pipelines and names none, in the
paragraph telling the reader to map ALL consumers -- and a search that
day across this file, the ten skills and the ledger found the five
named nowhere. Left standing and carried as L-269's Gap, because
naming them needs a read of the code rather than an edit here.)

"""

SECTION_NEW = b"""A Report Names Its Items [QUALITY]
The general habit whose sharp end is the fourth move above. It reaches
every report this project produces, not only checks. A count states a
SIZE. Names state what is there. A report that gives the size and
withholds the names is complete only for a reader who can go and find
out WHAT -- and neither reader here can. Claude resets every session
and will not think to open the file. Tony cannot read everything and
does not grep: "I can't go grep the code for all the instances that
built a count. A list is manageable and it gives me a sense of the
gap."

So a report has to be complete enough to ACT ON WHERE IT LANDS.

The names also carry the SHAPE, which no number can. "16" is a size.
"D Ring, C Ring, B Ring, A Ring, F Ring, G Ring, E Ring" says it is the
whole of one body's ring system, one kind of thing, mechanical rather
than seven separate judgments.

It is count AND names, not names instead of the count. MODULE_ATLAS.md
is the worked example -- "Undetermined role (4)" followed immediately by
the four filenames.

The scope is every place this project reports a set:
- Scanner and runner summaries, and their run histories.
- Ledger and handoff enumerations, which name the handles.
- Counted claims in this document and in the skills. "Four moves" and
  "two limits" name what they count; "5 parallel pipelines" does not.
- Findings, gaps and backlogs -- named by CLASS where the instance list
  is long, since The Braid already rules that a backlog grows by kinds
  rather than by counts.

Where the full list genuinely cannot land, name the CLASSES and give
the exact path where the instances live. A bare pointer is not enough:
the provenance scanner prints "292 TIER-1 FINDINGS IN THE SCANNED
TREE", explains that this is not the gate, and sends the reader to
another document -- the number a reader needs absent, the number
present wrong, and nothing named at all.

A coordinate is not a name. PROVENANCE_AUDIT.md reporting "display
string @ line 936" is better than a count and still requires opening
the file to learn the thing is hover_text_sun_and_corona.

[QUALITY] rather than [CRITICAL], on this document's own promotion
test. The naming half has failed repeatedly and in view, and every one
of those failures was recoverable -- a report nobody can act on gets
asked about. The count-delta half can pass while blind, so it lives in
the gate above. A check moves up when a failure shows it was
load-bearing, and the critical tier only works while it stays short.

(Tony's ruling, August 30, 2026; L-269. Three instances measured that
session, spanning the range: MODULE_ATLAS.md doing it right, the
scanner summary doing it not at all, PROVENANCE_AUDIT.md naming a
coordinate. The founding case is this document's own Check All Parallel
Pipelines, one section down: it says five, names none, and does it in
the sentence telling the reader to map ALL consumers. Measuring it
found the number UNDECIDABLE rather than merely wrong -- six functions
in palomas_orrery.py acquire position data, README.md names a different
five that span several files, and that paragraph straddles both
readings. Left standing, because choosing which one the gate means is a
ruling and not an edit. The six names, the two readings and the four
live stores carrying the sentence are recorded on L-269.)

"""

# ---------------------------------------------------------------------------
# EDIT 4 -- the v3.49 entry, rewritten in place (the version does not move)
# ---------------------------------------------------------------------------

V349_OLD = b"""v3.49 (August 30, 2026): One rule added. No skill changed.

A Report Names Its Items [CRITICAL], Part 3, immediately after A Check
That Cannot Fail Is Not Passing. Tony's ruling, 2026-08-30. A count
states a size; names state what is there. A report giving only the size
is complete only for a reader who can go and find out what, and neither
reader here can -- Claude resets and will not open the file, Tony
cannot read everything and does not grep. A report has to be complete
enough to act on where it lands.

The first write-up had this as an attention problem, a number being
easy to skip past. Tony corrected it, and the correction is the rule:
a count is not a weak signal, it is a signal that only works for a
reader who can perform a lookup neither reader performs.

NOT a runner convention, and deliberately not a skill. Method Belongs
to the Skill was applied and answered the other way -- the grounds are
the two READERS rather than how any one tool reports, and the two
readers are what this protocol is for.

The scope is broader than the sweep that raised it, on Tony's
instruction of the same day: scanner and runner summaries, ledger and
handoff enumerations, counted claims in this document and in the
skills, and findings and backlogs. Not only counts of grouped features.

The load-bearing half is that a count can be identical across a real
change. Clear one finding and introduce another in the same file and a
count delta reports nothing moved. PROVENANCE_AUDIT.md's "No file's
Tier-1 count rose" and the run history's one-number-per-run are both
that shape, which is why the rule sits beside A Check That Cannot Fail
Is Not Passing rather than in a style guide.

An unmet instance is left standing in this document rather than quietly
fixed. Check All Parallel Pipelines counts five pipelines in
palomas_orrery.py and names none, in the paragraph instructing the
reader to map ALL consumers. A search on 2026-08-30 across this file,
the ten installed skills and the ledger found the five named nowhere,
so naming them needs a read of the code and not an edit here. Carried
as L-269's Gap with a Tony-action.

Ledger, same commit: L-265 through L-269 placed, and L-262's diagnosis
amended in view rather than corrected in place. The framing smoke test
was never about interactive.html, its row in the gallery runner gates,
and the fix is two lines needing no Mode 5.

Version history: v3.46 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V349_NEW = b"""v3.49 (August 30, 2026): One rule added, in two pieces and two tiers.
No skill changed. Landed in two commits the same evening; this entry
describes the settled form, and says below what the first commit got
wrong.

A Report Names Its Items [QUALITY], Part 3, immediately after A Check
That Cannot Fail Is Not Passing -- and a FOURTH move inside that gate,
make the delta name what moved. Tony's ruling, 2026-08-30. A count
states a size; names state what is there. A report giving only the size
is complete only for a reader who can go and find out what, and neither
reader here can -- Claude resets and will not open the file, Tony
cannot read everything and does not grep. A report has to be complete
enough to act on where it lands.

The first write-up had this as an attention problem, a number being
easy to skip past. Tony corrected it, and the correction is the rule:
a count is not a weak signal, it is a signal that only works for a
reader who can perform a lookup neither reader performs.

NOT a runner convention, and deliberately not a skill. Method Belongs
to the Skill was applied and answered the other way -- the grounds are
the two READERS rather than how any one tool reports, and the two
readers are what this protocol is for.

The scope is broader than the sweep that raised it, on Tony's
instruction of the same day: scanner and runner summaries, ledger and
handoff enumerations, counted claims in this document and in the
skills, and findings and backlogs. Not only counts of grouped features.

THE SPLIT IS THE PART THE FIRST COMMIT GOT WRONG. It put the whole rule
in at [CRITICAL]. This document's own promotion test is that a check
moves up when a failure demonstrates it was load-bearing. The naming
half has failed repeatedly and in view -- the scanner summary, the
audit's coordinates, the L-268 sweep, the pipeline count below -- and
every one of those was recoverable. The count-delta half has NOT been
witnessed here: nobody has yet cleared one Tier-1 finding and gained
another with the total unchanged. It is inferred, and it is the half
that can pass while blind. So the sharp case went into a gate that is
already [CRITICAL] and the general habit went in at [QUALITY], which
keeps the critical tier short and leaves a promotion path if the delta
case ever bites. A second Opus session argued it; Tony carried it.

The founding case is left standing in this document rather than quietly
fixed, and measuring it is what made it the founding case. Check All
Parallel Pipelines says five pipelines in palomas_orrery.py and names
none, in the sentence instructing the reader to map ALL consumers. The
number is not merely stale; it is UNDECIDABLE. Six functions in that
file acquire position data and README.md names a different five that
span several files, and the gate's paragraph straddles both -- it
scopes the count to one file and then names gallery_studio.py and
json_converter.py. Choosing which reading it means changes what the
gate instructs, so it is a ruling. 46 documents carry the sentence,
four of them live stores including a skill that loads every orrery
session. The six names, the two readings and the four stores are on
L-269 so the next session verifies rather than rediscovers.

Ledger, first commit: L-265 through L-269 placed, and L-262's diagnosis
amended in view rather than corrected in place. The framing smoke test
was never about interactive.html, its row in the gallery runner gates,
and the fix is two lines needing no Mode 5. Confirmed the same evening:
the Page framing row now passes twelve checks in the gallery runner.

Version history: v3.46 moved down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

# ---------------------------------------------------------------------------
# EDIT 5 -- L-269's tier note and Gap
# ---------------------------------------------------------------------------

L269_OLD = b"""- **Claude:** the tier is worth a look. [CRITICAL] is proposed because
  the count-delta case is exactly A Check That Cannot Fail Is Not
  Passing, and that gate is [CRITICAL]. The counter-argument is real:
  the critical tier must stay short, and most of this rule's failures
  are recoverable rather than expensive. Changing it is one word in
  two places.
- **Gap: an unmet instance is left standing in the protocol itself,
  deliberately.** Check All Parallel Pipelines [CRITICAL] says
  "Position data flows through 5 parallel pipelines in
  palomas_orrery.py" and names none of the five, in the same paragraph
  that instructs the reader to map ALL consumers before patching. A
  search on 2026-08-30 across `PROJECT_INSTRUCTIONS.md`, the ten
  installed skills and `LEDGER_CONSOLIDATED.md` found the five named
  nowhere. `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` carries the
  same unnamed count as a preserved v3.29 field note. Naming them needs
  a read of `palomas_orrery.py`, which is a judgment call and not a
  mechanical fix, so it was not folded into this patch.
  **Tony-action (decide):** whether naming the five is worth a pass of
  its own or waits for the next job that opens that file.
"""

L269_NEW = b"""- **THE TIER WAS RULED [QUALITY], 2026-08-30, and the reasoning is
  worth keeping.** The first commit put the whole rule in at
  [CRITICAL]. The protocol's own promotion test is that a check moves
  up when a failure demonstrates it was load-bearing. The NAMING half
  has failed repeatedly and in view -- the scanner summary, the audit's
  coordinates, the L-268 sweep's first pass, the pipeline count below
  -- and every one of those failures was recoverable. The COUNT-DELTA
  half has NOT been witnessed here; nobody has yet cleared one Tier-1
  finding and gained another with the total unchanged. It is inferred,
  and it is the half that can pass while blind.
- **So the rule went in as TWO pieces at TWO tiers.** The count-delta
  case became the FOURTH move inside A Check That Cannot Fail Is Not
  Passing, which is already [CRITICAL], beside make success carry
  evidence, make the blind spot announce, and put the check where it
  runs. The general habit stayed at [QUALITY]. This keeps the critical
  tier short and leaves a clean promotion path if the delta case ever
  bites. (Argued by a second Opus session, 2026-08-30, reviewing the
  first commit; carried by Tony.)
- **THE FOUNDING CASE IS THE PROTOCOL'S OWN Check All Parallel
  Pipelines [CRITICAL]**, and it is a better one than the L-268 sweep
  that raised the rule. That gate says "Position data flows through 5
  parallel pipelines in `palomas_orrery.py`" and names none of them --
  in the same sentence instructing the reader to map ALL consumers
  before patching. The sweep's count was merely ignorable. This is a
  count nobody can check, inside a CRITICAL gate, with nothing to
  compare it against.
- **Measured at orrery `ded99fbe`, 2026-08-30: the number is
  UNDECIDABLE rather than merely wrong.** That is the finding, and it
  is why patch 1's "named nowhere" was too kind. Two incompatible
  readings both fit the words:
  - **SIX functions in `palomas_orrery.py` acquire position data:**
    `resolve_shell_sun_position`, `update_orbit_paths`,
    `plot_actual_orbits`, `plot_objects`, `animate_objects`,
    `open_orbital_param_visualization`. They do not share a route --
    `fetch_position`, `fetch_trajectory`, `fetch_orbit_path` and
    `orbit_data_manager` between them -- and `plot_objects` alone
    holds three near-identical branches with the same Vanth special
    case duplicated in each.
  - **`README.md` names a DIFFERENT five, and they span several
    files:** static plot, animation, social export, gallery curation,
    JSON conversion.
  The gate's own paragraph straddles both. It scopes the count to
  `palomas_orrery.py` and then names `gallery_studio.py` and
  `json_converter.py`, which belong to the README's taxonomy and not
  to the function one.
- **Cross-checked, not taken on report.** A second Opus session
  enumerated six functions from the same file on 2026-08-30; this
  entry's list was measured independently at `ded99fbe` and agrees on
  all six names and on their line numbers. The two sessions disagreed
  only on how many call sites sit inside `plot_objects` -- which is
  itself a count nobody should be carrying, and the reason this row
  names functions rather than sites.
- **The correction did not travel, and the spread is the
  measurement.** 46 documents at `ded99fbe` carry the sentence. Most
  are frozen archives and session records, correctly left alone. FOUR
  are live stores and would each need the fix: `PROJECT_INSTRUCTIONS.md`,
  `README.md`, `documentation/CLAUDE.md`, and
  `skills/orrery-coding-conventions/SKILL.md` -- so the unnamed count
  also sits in a skill that loads on every orrery visual session.
- **Gap: the gate is left standing, deliberately.** Choosing which
  taxonomy it means changes what the gate INSTRUCTS, which is a ruling
  and not a mechanical fix.
  **Tony-action (decide):** whether Check All Parallel Pipelines means
  the six functions inside `palomas_orrery.py` or the README's five
  consumers across files. Once that is settled the edit is mechanical
  in all four live stores, and the skill copy carries its own
  four-step bump chain.
"""

# ---------------------------------------------------------------------------
# EDIT 6 -- L-262's Ref line carries the ruled tier
# ---------------------------------------------------------------------------

L262_REF_OLD = b"""Names Its Items [CRITICAL], resident protocol Part 3."""
L262_REF_NEW = b"""Names Its Items [QUALITY], resident protocol Part 3."""


def die(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists("LEDGER_CONSOLIDATED.md"):
        die("run this from the orrery repo root.")

    files = {}
    print("BASE CHECK -- content fingerprints (CRLF-normalised)")
    for path, want in EXPECTED.items():
        if not os.path.exists(path):
            die("not found: %s" % path)
        with open(path, "rb") as f:
            raw = f.read()
        was_crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
        got = hashlib.md5(content).hexdigest()
        if got != want:
            die("base moved for %s\n  expected %s\n  found    %s\n"
                "  Patch 1 must run first, and its commit must be in place.\n"
                "  Nothing was written." % (path, want, got))
        tag = "  [CRLF working copy; matched after normalising]" if was_crlf else ""
        print("  ok  %-26s %s%s" % (path, got, tag))
        files[path] = {"content": content, "crlf": was_crlf, "orig": raw}

    inserted = (MOVES_COUNT_NEW + FOURTH_NEW + SECTION_NEW + V349_NEW
                + L269_NEW + L262_REF_NEW)
    if any(b > 127 for b in inserted):
        die("inserted text is not ASCII.")
    print("  ok  inserted text is ASCII (%d bytes)" % len(inserted))

    edits = [
        ("PROJECT_INSTRUCTIONS.md",
         "A Check That Cannot Fail: three moves -> four",
         MOVES_COUNT_OLD, MOVES_COUNT_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "A Check That Cannot Fail: add make-the-delta-name-what-moved",
         FOURTH_OLD, FOURTH_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "A Report Names Its Items: [CRITICAL] -> [QUALITY], split applied",
         SECTION_OLD, SECTION_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "v3.49 entry rewritten (version number unchanged)",
         V349_OLD, V349_NEW),
        ("LEDGER_CONSOLIDATED.md",
         "L-269: tier ruled, pipeline measurement recorded",
         L269_OLD, L269_NEW),
        ("LEDGER_CONSOLIDATED.md",
         "L-262 Ref: tier on A Report Names Its Items",
         L262_REF_OLD, L262_REF_NEW),
    ]

    print("\nEDITS")
    for path, label, old, new in edits:
        content = files[path]["content"]
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL (%d matches, expected 1): %s -- %s"
                  % (n, path, label))
            print("  anchor head: %r" % old[:70])
            print("NOTHING WAS WRITTEN.")
            sys.exit(1)
        files[path]["content"] = content.replace(old, new)
        print("  ok  %-58s %s" % (label, path))

    print("\nWRITE")
    for path in EXPECTED:
        out = files[path]["content"]
        if files[path]["crlf"]:
            out = out.replace(b"\n", b"\r\n")
        with open(path + ".bak", "wb") as f:
            f.write(files[path]["orig"])
        with open(path, "wb") as f:
            f.write(out)
        print("  wrote %-26s %7d bytes (%+d)  [.bak written]"
              % (path, len(out), len(out) - len(files[path]["orig"])))

    print("\nPATCH APPLIED")
    print("\nNEXT, and both are yours:")
    print("  (do) Run ledger_index.py. L-269's row is unchanged in the")
    print("       index -- same title, same score, same date -- so expect")
    print("       'unchanged, content identical'. That is the correct")
    print("       result, not a sign it did nothing.")
    print("  (do) Archive both L-269 patch scripts into documentation/.")
    print("\nWhat changed, by name:")
    print("  PROJECT_INSTRUCTIONS.md")
    print("    A Check That Cannot Fail Is Not Passing  three moves -> four")
    print("    A Report Names Its Items                 [CRITICAL] -> [QUALITY]")
    print("    v3.49 version-history entry              rewritten in place")
    print("    Check All Parallel Pipelines             UNCHANGED, awaiting a"
          " ruling")
    print("  LEDGER_CONSOLIDATED.md")
    print("    L-269  tier ruled; the six pipeline functions named")
    print("    L-262  Ref line tier corrected")


if __name__ == "__main__":
    main()
