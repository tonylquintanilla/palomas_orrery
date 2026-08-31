"""
patch_L269_1_ledger_blocks_and_protocol_v3_49.py

Run:  python patch_L269_1_ledger_blocks_and_protocol_v3_49.py
From: the ORRERY repo root (the folder holding LEDGER_CONSOLIDATED.md and
      PROJECT_INSTRUCTIONS.md).
In VS Code: open this file from that folder and click Run.

Built on orrery ded99fbe3d9ebbdbc6a2c86ed017c79763d23646 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES (four files, seven edits, all-or-nothing).

  LEDGER_CONSOLIDATED.md
    1. L-262: updates the metadata date to 2026-08-30.
    2. L-262: appends the AMENDED DIAGNOSIS -- the original bullets are
       kept, because a record that rewrites its own past stops being
       evidence -- and replaces the Gap/Ref tail.
    3. Inserts the L-265, L-266, L-267, L-268 and L-269 detail blocks
       into section A, immediately before "## PENDING ACTION (Tony-side)".
       L-265 through L-268 are EXTRACTED from
       documentation/LEDGER_ENTRIES_20260830.md rather than retyped, so
       there is no transcription step to get wrong.

  PROJECT_INSTRUCTIONS.md
    4. Header: v3.48 -> v3.49, date, and the cut anchor -> ded99fbe.
    5. Part 3: adds "A Report Names Its Items [CRITICAL]" immediately
       after "A Check That Cannot Fail Is Not Passing [CRITICAL]".
    6. Version History: adds v3.49 and REMOVES the v3.46 block, which
       moves down to keep three entries resident.

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    7. Receives the v3.46 block at the end of PART 1, with the standard
       moved-down note.

  documentation/LEDGER_ENTRIES_20260830.md
    8. Gets a PLACED stamp at the top so a later session does not place
       it twice, and so the wrong placement instruction it carries is
       corrected in view rather than silently.

WHAT IT DOES NOT DO.
  Nothing here touches the index zone. Run ledger_index.py afterwards;
  it rebuilds every index row from the <!-- L:... --> comments. The
  staged file's hand-written INDEX ROWS are deliberately NOT used -- its
  four scores disagree with its own metadata comments (it lists 12.0,
  10.8, 9.6, 10.8 where the comments compute 9.0, 5.4, 3.4, 4.5).

SUCCESS looks like: one "ok" line per edit, a per-file byte count, and
"PATCH APPLIED".
FAILURE looks like: a single "ERROR" or "ANCHOR FAIL" line and NOTHING
written. Safe to re-check and re-run.
This script is one-shot; a second run aborts on the fingerprints.
"""

import hashlib
import os
import sys

# Content fingerprints (CRLF-normalised) of the expected base.
EXPECTED = {
    "LEDGER_CONSOLIDATED.md":
        "6a7e7609c6aabce88b02fc8497616566",
    "PROJECT_INSTRUCTIONS.md":
        "3691eab6cbfc531fae763326737bfae4",
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md":
        "9e658b3b4f422bdd23f68054d3b02667",
    "documentation/LEDGER_ENTRIES_20260830.md":
        "e8b50c24073d5c458cbb85177829904b",
}

STAGED = "documentation/LEDGER_ENTRIES_20260830.md"


def die(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def read_norm(path):
    """Return (raw_bytes, lf_content, was_crlf). Compare content, not bytes."""
    if not os.path.exists(path):
        die("not found: %s -- run this from the orrery repo root." % path)
    with open(path, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    return raw, content, was_crlf


# ---------------------------------------------------------------------------
# EDIT 1 + 2 -- L-262 amendment
# ---------------------------------------------------------------------------

L262_META_OLD = (
    b"<!-- L:262 status:OPEN upd:2026-08-29 section:A flag: rice:3/4/95/1 -->"
)
L262_META_NEW = (
    b"<!-- L:262 status:OPEN upd:2026-08-30 section:A flag: rice:3/4/95/1 -->"
)

L262_TAIL_OLD = b"""**Gap:** the suite cannot run. Decide which fix, then do it.
**Ref:** L-236 (the runner that found it); L-238 (the commit that
added the suite); A Check That Cannot Fail Is Not Passing [CRITICAL],
resident protocol Part 3.
"""

L262_TAIL_NEW = b"""- **AMENDED 2026-08-30: the diagnosis above is wrong, and the bullets
  are kept rather than corrected in place so the record stays
  evidence.** The measurement was right; the conclusion drawn from it
  was not. The test was never about `interactive.html`. It takes the
  page path as `process.argv[2]`, and its markers -- `gridDtick`,
  `frameLayout`, `rebuildFrameOptions` -- live in
  `gallery/solar_system_earth_test2.html`. Run against the page that
  actually holds its helpers it passes all twelve checks, verified
  2026-08-30.
- **Measured again at gallery `1bf98450`, 2026-08-30.**
  `gallery/solar_system_earth_test2.html` contains both slice anchors,
  once each. `interactive.html` contains neither, zero times. The two
  pages carry DIFFERENT framing implementations, which is why the
  original reading looked sound.
- **It is a GATING row, which the first write-up did not establish.**
  `gallery_maintenance_run.py`'s check tuple is
  `(label, runner, argv-tail, cwd, verdict hint, report_only)` and the
  Page framing row carries `report_only=False`. So this is not a dead
  check sitting quietly in `documentation/`; it is a gating check that
  fails on every run that reaches it. Either it has been failing, or it
  has not been running -- both are worth knowing and only the runner's
  own output can say which.
- **The fix, still two one-line edits, and neither touches a live
  page.**
  1. `gallery_maintenance_run.py` line 146 -- point the argv-tail at
     `gallery/solar_system_earth_test2.html` AND add
     `gallery/feature_renderers.js`. The script reads a second file at
     `process.argv[3]` for `window.GalleryFeatures`; the runner passes
     only one argument today, so the page fix alone would move the
     failure rather than clear it. The neighbouring "Sun shells" row
     already passes `feature_renderers.js` this way.
  2. `documentation/smoke_framing.js` -- it reads
     `payload_jupiter_saturn.json` from the working directory. The
     runner's cwd is the repo root and the file is in
     `documentation/`.
- **This voids the bundling argument.** L-262 was to ride along with
  the portrait pass to save one Mode 5. It needs no Mode 5 at all, so
  it should not wait for one.
- **Gap: the residual, recorded rather than left implied.** Once
  pointed correctly the test guards `solar_system_earth_test2.html` --
  a test page. The live exhibit's own framing, `sunRefitFrame` in
  `interactive.html`, still has no test, and L-267's work adds more
  framing logic to exactly that file. "Put the check where it runs" is
  half satisfied.
**Ref:** L-236 (the runner that found it); L-238 (the commit that
added the suite); L-267 (which adds framing logic to the untested
file); A Check That Cannot Fail Is Not Passing [CRITICAL] and A Report
Names Its Items [CRITICAL], resident protocol Part 3.
"""

# ---------------------------------------------------------------------------
# EDIT 3 -- the new L-269 block (265-268 are extracted, not retyped)
# ---------------------------------------------------------------------------

L269_BLOCK = b"""#### [L-269] A report names its items, not how many there are
<!-- L:269 status:OPEN upd:2026-08-30 section:A flag: rice:5/4/90/3 -->
- **Tony's ruling, 2026-08-30, and the reason is the load-bearing
  part:** "I can't go grep the code for all the instances that built a
  count. A list is manageable and it gives me a sense of the gap."
- **A count states a SIZE. Names state what is there.** A report that
  gives the size and withholds the names is complete only for a reader
  who can go and find out WHAT, and neither reader here can. Claude
  resets every session and will not think to open the file. Tony cannot
  read everything and does not grep. So a report has to be complete
  enough to ACT ON WHERE IT LANDS.
- **The correction to the first write-up matters.** This was initially
  recorded as an attention problem, a number being easy to skip past.
  It is not. A count is not a weak signal; it is a signal that only
  works for a reader who can perform a lookup neither reader performs.
- **The names carry the SHAPE, which no number can.** "16" is a size.
  "D Ring, C Ring, B Ring, A Ring, F Ring, G Ring, E Ring" says it is
  the whole of one body's ring system, one kind of thing, mechanical
  rather than seven separate judgments.
- **AND A COUNT CAN BE IDENTICAL ACROSS A REAL CHANGE**, which is why
  this is a protocol amendment rather than a style preference. Clear
  one finding in a file and introduce another in the same file, and a
  count-based delta reports that nothing moved. A count-based report is
  a check that cannot fail.
- **Recorded in protocol v3.49** as A Report Names Its Items
  [CRITICAL], Part 3, immediately after A Check That Cannot Fail Is Not
  Passing.
- **It is NOT a runner convention and does not belong in a skill.**
  Method Belongs to the Skill was applied and answered the other way:
  the grounds are the two READERS, not how any one tool reports, and
  the two readers are what the protocol is for.
- **Scope, on Tony's instruction of 2026-08-30, is broader than the
  sweep that raised it.** It is not only counts of grouped features. It
  covers scanner and runner summaries and their run histories; ledger
  enumerations in entries and handoffs, which name handles; counted
  claims in the protocol itself and in the skills; and findings, gaps
  and backlogs, which name by CLASS where the instance list is long,
  per The Braid.
- **Three instances measured 2026-08-30, spanning the range.**
  `MODULE_ATLAS.md` does it right -- "Undetermined role (4)" followed
  immediately by the four filenames, count and names together.
  `provenance_scanner.py`'s terminal summary does it not at all -- it
  prints "292 TIER-1 FINDINGS IN THE SCANNED TREE", explains that this
  is not the gate, and sends the reader to another document, so the
  number a reader needs is absent, the number present is the wrong one,
  and nothing is named. `PROVENANCE_AUDIT.md` is the middle -- "display
  string @ line 936" is a coordinate, not a name; the thing is
  `hover_text_sun_and_corona`, and a session had to open the file at
  that line to find out.
- **The hole underneath the middle case is the strongest evidence.**
  The audit reports "No file's Tier-1 count rose" and the run history
  tracks T1 as one number per run, 292 across six runs. Both are count
  deltas, so both are blind to a swap -- clear one finding, introduce
  another in the same file, and neither says anything happened.
- **Claude:** RICE 5/4/90/3 -> 6.0 proposed, not confirmed. Reach 5
  because it governs every report the project emits. Effort 3 is
  remediation, not the rule -- the rule landed with this entry.
- **Claude:** the tier is worth a look. [CRITICAL] is proposed because
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
- **Gap: remediation is separate and is not scheduled here.** Fixing
  the scanner's terminal summary and the audit's unit names is real
  work. Per The Braid it goes in slices and earns its own handle when
  someone takes it up.
- **Tony-action (decide):** whether the second-level review lives in
  the ledger skill -- ledger items reviewed for this property as they
  are touched -- as Tony proposed on 2026-08-30.
- **Ref:** A Check That Cannot Fail Is Not Passing and The Braid,
  resident protocol Part 3; L-268 (the sweep that raised it); L-235
  (checks that cannot fail, gallery side); L-230 (skill bumps and the
  protocol history, the same shape of unwatched transition).

"""

LEDGER_INSERT_ANCHOR = b"## PENDING ACTION (Tony-side)"

# ---------------------------------------------------------------------------
# EDITS 4-6 -- PROJECT_INSTRUCTIONS.md
# ---------------------------------------------------------------------------

PI_HEADER_OLD = b"""Tony Quintanilla, PE | Claude | v3.48 | August 29, 2026

Cut from bfa9de2f at https://github.com/tonylquintanilla/palomas_orrery"""

PI_HEADER_NEW = b"""Tony Quintanilla, PE | Claude | v3.49 | August 30, 2026

Cut from ded99fbe at https://github.com/tonylquintanilla/palomas_orrery"""

PI_RULE_ANCHOR = b"""Check All Parallel Pipelines [CRITICAL]"""

PI_RULE_NEW = b"""A Report Names Its Items [CRITICAL]
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

PI_HISTORY_ANCHOR = b"""v3.48 (August 29, 2026): No rule changed in this document. One skill"""

PI_V349 = b"""v3.49 (August 30, 2026): One rule added. No skill changed.

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

# ---------------------------------------------------------------------------
# EDIT 7 -- the v3.46 block moves down
# ---------------------------------------------------------------------------

V346_BLOCK = b"""v3.46 (August 28, 2026): No rule changed in this document. One skill
correction, recorded here because the recording is the fourth link of
L-230's chain and the only one that does not fire on its own.

provenance-discipline 2.8 -> 2.9 (L-256). The Gate Binds at SERVING
becomes The Gate Binds at EXPORT. 2.8 was written earlier the same
evening and placed the gate where the harm lands -- a visitor taking a
served value as true. Tony's ruling of 2026-08-28 moves it upstream to
where a check can still run: "I think provenance should be settled
before it leaves the orrery to the gallery cache. There is no
provenance checker in the gallery."

Verified rather than assumed before the edit was written.
provenance_scanner.py exists only in the orrery repo. The nightly
builder lives in the GALLERY repo and scores nothing -- two mentions of
provenance in the whole file, one a docstring line recording where its
copied constants came from, one a warning string. The two repositories
do not share a checker, so a gate at publication sits downstream of the
last instrument in existence. That is A Check That Cannot Fail Is Not
Passing in the pipeline layer rather than in code.

The section now separates WHY from WHERE explicitly, because the
correction is exactly the kind a future session would undo by
reasoning from harm rather than from enforceability. Why: serving.
Where it fires: export. What stays free: drawing.

One consequence raises a priority. objects_config.json is maintained by
hand in the gallery repo, so the export boundary the gate names is
today a human copy with no check on it. The cross-repo transport
becomes the gate's missing enforcement point rather than a defence
against later drift -- higher than MASTER_PLAN_INTERACTIVE_GALLERY.md
currently places segment 2, and an amendment that document is owed.

Version history: v3.43 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-08-29 when v3.48
made a fourth entry.)
"""

HIST_NOTE = b"""(Moved down from the resident protocol on 2026-08-30 when v3.49
made a fourth entry.)

"""

# ---------------------------------------------------------------------------
# EDIT 8 -- stamp the staged entries file as consumed
# ---------------------------------------------------------------------------

STAGED_ANCHOR = b"""# Ledger entries -- 2026-08-30 session
"""

STAGED_STAMP = b"""# Ledger entries -- 2026-08-30 session

**PLACED 2026-08-30 into `LEDGER_CONSOLIDATED.md`** by
`patch_L269_1_ledger_blocks_and_protocol_v3_49.py`, built on orrery
`ded99fbe`. This file is now a RECORD, not a pending input. Do not
place it a second time.

Two things it got wrong, corrected in view rather than silently:

1. The placement instruction below says "after L-264's block." L-264 is
   in section C (DONE). The four blocks belong in section A, where
   L-262 is, and that is where the patch put them -- immediately before
   `## PENDING ACTION (Tony-side)`.
2. The INDEX ROWS below were not used. Index rows are generated:
   `ledger_index.py` rebuilds them from the `<!-- L:... -->` comments,
   and hand-pasting summary rows is against the ledger convention. The
   four scores listed there also disagree with the file's own metadata
   comments -- 12.0, 10.8, 9.6 and 10.8 against the 9.0, 5.4, 3.4 and
   4.5 the comments compute.

A fifth handle, L-269, was written directly into the ledger by the same
patch and does not appear below.
"""


def main():
    root_marker = "LEDGER_CONSOLIDATED.md"
    if not os.path.exists(root_marker):
        die("run this from the orrery repo root (no %s here)." % root_marker)

    files = {}
    print("BASE CHECK -- content fingerprints (CRLF-normalised)")
    for path, want in EXPECTED.items():
        raw, content, was_crlf = read_norm(path)
        got = hashlib.md5(content).hexdigest()
        tag = "  [CRLF working copy; matched after normalising]" if was_crlf else ""
        if got != want:
            die("base moved for %s\n  expected %s\n  found    %s\n"
                "  Nothing was written. Re-pull or re-cut this patch."
                % (path, want, got))
        print("  ok  %-46s %s%s" % (path, got, tag))
        files[path] = {"content": content, "crlf": was_crlf, "orig": raw}

    # ---- extract L-265..L-268 from the staged file, do not retype them ----
    staged = files[STAGED]["content"]
    extracted = []
    for handle in (b"L-265", b"L-266", b"L-267", b"L-268"):
        start = staged.find(b"#### [" + handle + b"]")
        if start < 0:
            die("staged file has no detail block for %s" % handle.decode())
        end = staged.find(b"\n---\n", start)
        if end < 0:
            die("no block terminator after %s in the staged file"
                % handle.decode())
        block = staged[start:end].rstrip(b"\n") + b"\n\n"
        meta = b"<!-- L:" + handle[2:] + b" "
        if meta not in block:
            die("%s block is missing its %s metadata comment"
                % (handle.decode(), meta.decode().strip()))
        extracted.append((handle.decode(), block))

    new_blocks = b"".join(b for _, b in extracted) + L269_BLOCK
    for name, blk in extracted:
        first = blk.split(b"\n", 1)[0].decode()
        print("  extracted %-6s %5d bytes  %s" % (name, len(blk), first[:64]))
    print("  written   L-269  %5d bytes  %s"
          % (len(L269_BLOCK), L269_BLOCK.split(b"\n", 1)[0].decode()[:64]))

    # ---- ASCII gate on everything this patch inserts ----
    inserted = (L262_META_NEW + L262_TAIL_NEW + new_blocks + PI_HEADER_NEW
                + PI_RULE_NEW + PI_V349 + V346_BLOCK + HIST_NOTE
                + STAGED_STAMP)
    bad = [b for b in inserted if b > 127]
    if bad:
        die("inserted text is not ASCII (%d bytes over 127)." % len(bad))
    print("  ok  inserted text is ASCII (%d bytes)" % len(inserted))

    # ---- build every edit in memory; nothing is written until all pass ----
    edits = [
        ("LEDGER_CONSOLIDATED.md", "L-262 metadata date -> 2026-08-30",
         L262_META_OLD, L262_META_NEW),
        ("LEDGER_CONSOLIDATED.md", "L-262 amended diagnosis + new Gap/Ref",
         L262_TAIL_OLD, L262_TAIL_NEW),
        ("LEDGER_CONSOLIDATED.md",
         "insert L-265, L-266, L-267, L-268, L-269 into section A",
         LEDGER_INSERT_ANCHOR, new_blocks + LEDGER_INSERT_ANCHOR),
        ("PROJECT_INSTRUCTIONS.md", "header -> v3.49, cut anchor -> ded99fbe",
         PI_HEADER_OLD, PI_HEADER_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "Part 3: add A Report Names Its Items [CRITICAL]",
         PI_RULE_ANCHOR, PI_RULE_NEW + PI_RULE_ANCHOR),
        ("PROJECT_INSTRUCTIONS.md", "Version History: add v3.49",
         PI_HISTORY_ANCHOR, PI_V349 + PI_HISTORY_ANCHOR),
        ("PROJECT_INSTRUCTIONS.md", "Version History: remove the v3.46 block",
         V346_BLOCK, b""),
        ("documentation/PROJECT_INSTRUCTIONS_HISTORY.md",
         "PART 1 receives v3.46",
         HIST_ANCHOR, HIST_ANCHOR + b"\n" + V346_BLOCK + HIST_NOTE),
        (STAGED, "stamp the staged file as PLACED",
         STAGED_ANCHOR, STAGED_STAMP),
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
        print("  ok  %-46s %s" % (label, path))

    # ---- write, preserving each file's own line-ending style ----
    print("\nWRITE")
    for path in EXPECTED:
        out = files[path]["content"]
        if files[path]["crlf"]:
            out = out.replace(b"\n", b"\r\n")
        with open(path + ".bak", "wb") as f:
            f.write(files[path]["orig"])
        with open(path, "wb") as f:
            f.write(out)
        delta = len(out) - len(files[path]["orig"])
        print("  wrote %-46s %7d bytes (%+d)  [.bak written]"
              % (path, len(out), delta))

    print("\nPATCH APPLIED")
    print("\nNEXT, and both are yours:")
    print("  (do) Run ledger_index.py to rebuild the index rows. This patch")
    print("       deliberately wrote none.")
    print("  (do) Archive this script into documentation/ once it has run.")
    print("\nThe five handles now in LEDGER_CONSOLIDATED.md, by name:")
    print("  L-265  The i panel carries links, not curated prose")
    print("  L-266  Nothing checks that a cited link still resolves")
    print("  L-267  The Sun exhibit GUI shape: drawer, focus label,"
          " marker navigation")
    print("  L-268  Sweep: features collapsed out of their own identity")
    print("  L-269  A report names its items, not how many there are")
    print("  L-262  amended in place (diagnosis corrected, original kept)")


if __name__ == "__main__":
    main()
