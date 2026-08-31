"""
patch_L269_3_gate_correction_and_readme.py

Run:  python patch_L269_3_gate_correction_and_readme.py
From: the ORRERY repo root (the folder holding LEDGER_CONSOLIDATED.md and
      PROJECT_INSTRUCTIONS.md).
In VS Code: open this file from that folder and click Run.

Built on the tree left by patch_L269_2_tier_split_and_pipeline_measurement.py,
which ran against orrery a667e12824db71f5cc1ddd1503c1afe72db4a986 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

SEQUENCE. Third and last in the L-269 chain. Patch 1 landed the rule at
ded99fbe; patch 2 split it and dropped the tier to [QUALITY]; this one
corrects the founding case that both of them described wrongly.

It does NOT matter whether ledger_index.py has run since patch 2. The
regenerated index is byte-identical either way -- L-269's row did not
change -- so the fingerprints below cover both states. Verified, not
assumed.

If you also downloaded patch_L269_2_tier_split_and_gate_correction.py:
that file is DEAD. It was the same corrections folded into patch 2, and
patch 2 has already run. Delete it. This script does the same work
against the tree that actually exists.

WHY. Patch 2 recorded the pipeline count as UNDECIDABLE -- two rival
readings of one question, with the gate left standing until someone
ruled between them. That framing was wrong twice over, and Tony's
ruling of 2026-08-30 settles it:

  THE FIVE WERE NAMED. README.md names them: static plot, animation,
  social export, gallery curation, JSON conversion. Patch 1's "named
  nowhere" was measured against the protocol, the skills and the ledger,
  and the README was not in that set. The gate does not point to it,
  which is a different and smaller problem than the names not existing.

  THE TWO LISTS ARE NOT RIVAL READINGS. They sit on DIFFERENT AXES.
  The README's five are CONSUMERS across the project. The six functions
  in palomas_orrery.py are FETCHERS. Static plot and animation appear in
  both; social export, gallery curation and JSON conversion fetch
  nothing at all, they render what was already fetched. Neither list is
  a subset of the other, so there was never a question with one answer.

  THE GATE HAD MERGED THEM: a cross-file count of five with
  "in palomas_orrery.py" attached, a scope from the other axis. Together
  they describe a set that does not exist. Then the next sentence
  half-named the real list -- four of the README's five, missing social
  export.

  Tony's ruling: the gate means the CONSUMERS; the names move into the
  gate so a reader is not sent to another document to learn what five
  means; the in-file scoping goes.

VERIFIED AT a667e128 BEFORE THE NAMES WERE WRITTEN IN, because the
ruling turned the remaining work from discovery into checking. All five
paths exist. Two of them live in the GALLERY repository under tools/,
which the old scoping actively hid: a reader grepping palomas_orrery.py
as instructed would find three of five.

WHAT IT DOES (two files, six edits, all-or-nothing).

  PROJECT_INSTRUCTIONS.md
    1. CHECK ALL PARALLEL PIPELINES rewritten. Names the five consumers
       with file and repo, drops the in-file scoping, and warns against
       substituting the fetcher list for the consumer list.
    2. A Report Names Its Items: its origin note carries the two-axes
       correction instead of "undecidable".
    3. The v3.49 entry's founding-case paragraph, likewise.

  LEDGER_CONSOLIDATED.md
    4. L-269: the two-axes finding, the verification that closed it, and
       a narrowed Gap -- three live stores still carrying the old
       sentence, and the fetcher list having no home.
    5. L-270 opened: README.md is a stale live store.
    6. L-237's Ref gains L-270, same class of unwatched record.

SUCCESS: one "ok" line per edit, a byte count per file, "PATCH APPLIED".
FAILURE: one "ERROR" or "ANCHOR FAIL" line and NOTHING written.
One-shot; a second run aborts on the fingerprints.
"""

import hashlib
import os
import sys

EXPECTED = {
    "LEDGER_CONSOLIDATED.md": "70d024e8e18ab00b7227d5c38d41ab04",
    "PROJECT_INSTRUCTIONS.md": "5a5b4f2f450c5530df8cbc3d1f9f1e5b",
}

L270_ANCHOR = b"## PENDING ACTION (Tony-side)"

L237_REF_OLD = b"**Ref:** L-234; L-235; L-080 (the fingerprint's field list).\n"
L237_REF_NEW = (b"**Ref:** L-234; L-235; L-080 (the fingerprint's field list); "
                b"L-270\n(README staleness -- the same class of unwatched "
                b"record).\n")

GATE_OLD = b"""Check All Parallel Pipelines [CRITICAL]
Position data flows through 5 parallel pipelines in palomas_orrery.py.
Fixing one does not propagate. Map ALL consumers before patching.
Same bugs appear independently in gallery_studio.py / json_converter.py
and in plot_objects / animate_objects. Check both when fixing one.
"""

GATE_NEW = b"""Check All Parallel Pipelines [CRITICAL]
Position data reaches a viewer through FIVE parallel consumers. Fixing
one does not propagate to the others; the same bug appears
independently in each, and a change as small as hover text can touch
all five. Map ALL of them before patching anything in the data flow.

  static plot        plot_objects              palomas_orrery.py
  animation          animate_objects           palomas_orrery.py
  social export      export_social_view ->     palomas_orrery.py ->
                     social_media_export.py    orrery repo
  gallery curation   tools/gallery_studio.py   GALLERY repo
  JSON conversion    tools/json_converter.py   GALLERY repo

TWO OF THE FIVE ARE IN THE OTHER REPOSITORY. Grep one repo and you find
three. That is the trap the earlier wording set, by scoping the count
to palomas_orrery.py.

Fetching is a different question from consuming, and the answer is a
different list. Six functions in palomas_orrery.py acquire position
data, and three of the five consumers above fetch nothing at all -- they
render what was already fetched. The fetcher list is on L-269; do not
substitute one for the other.

(Corrected August 30, 2026; L-269, and it is that rule's founding case.
The line had read "5 parallel pipelines in palomas_orrery.py" and named
none of them, in the sentence telling the reader to map ALL consumers.
Five was README.md's cross-file consumer count; "in palomas_orrery.py"
was a single-file scope from the other axis. Together they described a
set that does not exist, and the next sentence then half-named the real
list, four of five, missing social export. All five paths were verified
present at a667e128 before they were written here. A count does not
carry the axis it was counted on.)
"""

NOTE_OLD = b"""(Tony's ruling, August 30, 2026; L-269. Three instances measured that
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

NOTE_NEW = b"""(Tony's ruling, August 30, 2026; L-269. Three instances measured that
session, spanning the range: MODULE_ATLAS.md doing it right, the
scanner summary doing it not at all, PROVENANCE_AUDIT.md naming a
coordinate. The founding case was this document's own Check All
Parallel Pipelines, one section down, which said five and named none in
the sentence telling the reader to map ALL consumers. It is corrected
now -- and how it was wrong is the lesson. The five WERE named, in
README.md, which the gate did not point to. And a second candidate list
existed on a different axis: six FETCHERS inside palomas_orrery.py
against the README's five CONSUMERS across the project, neither a
subset of the other. The gate had merged them, a cross-file count
wearing a single-file scope. A count does not carry the axis it was
counted on, which is the sharpest form of this rule there is.)

"""

V349_OLD = b"""The founding case is left standing in this document rather than quietly
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

"""

V349_NEW = b"""THE FOUNDING CASE IS CORRECTED TOO, and how it was wrong is the lesson.
Check All Parallel Pipelines had read "5 parallel pipelines in
palomas_orrery.py" and named none, in the sentence telling the reader
to map ALL consumers. The five WERE named -- in README.md, which the
gate does not point to. And a second candidate list existed on a
DIFFERENT AXIS: six FETCHERS inside palomas_orrery.py against the
README's five CONSUMERS across the project. Two entries appear in both,
three of the consumers fetch nothing, and neither list is a subset of
the other. The gate had merged them, taking a cross-file count and
attaching a single-file scope, describing a set that does not exist --
then half-naming the real list in the next sentence, four of five,
missing social export. Tony's ruling: the gate means the CONSUMERS, the
names belong in the gate rather than in another document, and the
in-file scoping goes. All five paths were verified present at a667e128
before being written in, and two of them turn out to live in the
GALLERY repository under tools/, which the old scoping actively hid.
The fetcher list is kept on L-269 as the answer to a different
question. A count does not carry the axis it was counted on.

"""

L269_OLD = b"""- **THE FOUNDING CASE IS THE PROTOCOL'S OWN Check All Parallel
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

L269_NEW = b"""- **THE FOUNDING CASE IS THE PROTOCOL'S OWN Check All Parallel
  Pipelines [CRITICAL]**, and it is a better one than the L-268 sweep
  that raised the rule. That gate said "Position data flows through 5
  parallel pipelines in `palomas_orrery.py`" and named none of them --
  in the same sentence instructing the reader to map ALL consumers
  before patching. The sweep's count was merely ignorable. This was a
  count nobody could check, inside a CRITICAL gate.
- **The first read of it was wrong in BOTH directions, and the
  correction is the sharpest form of this rule there is.** Patch 1
  recorded that the five were "named nowhere." They were named -- in
  `README.md`, which the gate does not point to. And the two candidate
  lists are not rival readings of one question. THEY SIT ON DIFFERENT
  AXES:
  - **README.md's five CONSUMERS, across the project:** static plot,
    animation, social export, gallery curation, JSON conversion.
  - **Six FETCHERS inside `palomas_orrery.py`,** the functions that
    call Horizons for position data:
    `resolve_shell_sun_position`, `update_orbit_paths`,
    `plot_actual_orbits`, `plot_objects`, `animate_objects`,
    `open_orbital_param_visualization`. `plot_objects` alone holds
    three near-identical branches with the same Vanth special case in
    each, across four routes -- `fetch_position`, `fetch_trajectory`,
    `fetch_orbit_path` and `orbit_data_manager`.
  Static plot and animation appear in both. Social export, gallery
  curation and JSON conversion fetch nothing; they render what was
  already fetched. Neither list is a subset of the other.
- **The gate had MERGED the two.** It took the README's cross-file
  count of five and attached "in `palomas_orrery.py`", a single-file
  scope from the other axis, so together they described a set that does
  not exist. The next sentence then half-named the real list --
  `gallery_studio.py`, `json_converter.py`, `plot_objects`,
  `animate_objects` -- four of the README's five, missing social
  export. A COUNT DOES NOT CARRY THE AXIS IT WAS COUNTED ON.
- **Tony's ruling, 2026-08-30:** the gate means the CONSUMERS; the
  names move into the gate itself so a reader is not sent to another
  document to learn what five means; the in-file scoping goes. Applied
  in the same commit as the rule, so the founding case is closed by the
  rule rather than left as an exhibit.
- **Verified at `a667e128` before the names were written in**, because
  the ruling turned the remaining work from discovery into checking.
  All five paths exist: `plot_objects`, `animate_objects` and
  `export_social_view` in `palomas_orrery.py` (the last delegating to
  `social_media_export.py`), and `tools/gallery_studio.py` and
  `tools/json_converter.py` in the GALLERY repo. Two of five are in
  the other repository, which the old scoping actively hid -- a reader
  following the instruction as written would grep one repo and find
  three.
- **Cross-checked, not taken on report.** A second Opus session
  enumerated the six fetchers on 2026-08-30 and made the two-axes
  argument; this entry's fetcher list was measured independently at
  `ded99fbe` and agrees on all six names and their line numbers. The
  two sessions disagreed only on how many call sites sit inside
  `plot_objects` -- itself a count nobody should be carrying, and the
  reason this row names functions rather than sites.
- **The correction has not travelled, and that is what remains.** The
  old sentence appears in 46 documents at `ded99fbe`. Most are frozen
  archives and session records, correctly left alone. THREE are live
  stores still carrying it after this commit: `README.md`,
  `documentation/CLAUDE.md`, and
  `skills/orrery-coding-conventions/SKILL.md` -- so the merged count
  also sits in a skill that loads on every orrery visual session.
  **Tony-action (decide):** whether those three are swept now or when
  the next job opens each file. The skill copy carries its own
  four-step bump chain.
- **Gap: the fetcher list has no home.** It is recorded here and
  nowhere else. It answers a real question -- which functions must be
  patched when the FETCH changes rather than the render -- and
  `orrery-coding-conventions` is the plausible place for it.
  **Tony-action (decide):** whether it earns a place in that skill or
  stays a ledger record.
"""

L270_BLOCK = b"""#### [L-270] README.md is a stale live store, and a gate depended on it
<!-- L:270 status:OPEN upd:2026-08-30 section:A flag: rice:4/3/95/2 -->
- **Surfaced 2026-08-30 while correcting L-269's founding case.** The
  five consumer names that Check All Parallel Pipelines now carries
  came from `README.md`. That made the README's freshness a property
  of a CRITICAL gate, which nobody had noticed it was.
- **Measured at `a667e128`.** `README.md` says 118 Python modules and
  roughly 96,000 non-blank lines. `MODULE_ATLAS.md`, regenerated the
  same day, says 129 modules and 104,494 lines. Elsewhere the README
  says 90,000 lines. It was last committed 2026-08-11 (`bebf0f7`),
  nineteen days earlier.
- **The gate no longer depends on it**, because v3.49 moved the five
  names INTO the gate. That is the fix for the dependency. It is not a
  fix for the README.
- **What is actually at risk is the SHAPE, not the counts.** The
  gallery moved to the assembler and cache-builder architecture after
  2026-08-11. The five consumers were verified present at `a667e128`,
  so the list is right today; whether the README still describes the
  gallery correctly around them is unexamined, which is not the same
  as clean.
- **Two of the five are not where the README's own prose implies.**
  `gallery_studio.py` and `json_converter.py` live in the GALLERY repo
  under `tools/`. A reader taking the README's project description at
  face value would look in the orrery repo.
- **A smaller instance, and it is self-inflicted.** The atlas run at
  `a667e128` lists `patch_L269_1_ledger_blocks_and_protocol_v3_49.py`
  under both Undetermined role and Undetermined domain, because a
  spent patch script was left at the repo root. It is inflating the
  module count that L-270 is about.
  **Tony-action (do):** archive both L-269 patch scripts into
  `documentation/` per safe-file-editing's Naming and Archiving rule,
  and re-run `module_atlas.py`.
- **Tony-action (decide):** whether the README gets a refresh pass of
  its own or is corrected the next time it is opened. The counts are
  mechanical; the architecture description is not.
- **Claude:** RICE 4/3/95/2 -> 5.7 proposed, not confirmed. Reach 4
  because the README is what a newcomer and a relay partner read
  first; Confidence 95 because the staleness is measured rather than
  suspected.
- **Ref:** L-269 (which surfaced it and removed the gate's dependency
  on it); L-237 (the other stale-record item); The Correction Does Not
  Travel, safe-file-editing 1.9; A Report Names Its Items, resident
  protocol Part 3.

"""


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
                "  Patches 1 and 2 must both have run first.\n"
                "  Nothing was written." % (path, want, got))
        tag = "  [CRLF working copy; matched after normalising]" if was_crlf else ""
        print("  ok  %-26s %s%s" % (path, got, tag))
        files[path] = {"content": content, "crlf": was_crlf, "orig": raw}

    inserted = GATE_NEW + NOTE_NEW + V349_NEW + L269_NEW + L270_BLOCK \
        + L237_REF_NEW
    if any(b > 127 for b in inserted):
        die("inserted text is not ASCII.")
    print("  ok  inserted text is ASCII (%d bytes)" % len(inserted))

    edits = [
        ("PROJECT_INSTRUCTIONS.md",
         "Check All Parallel Pipelines: the five consumers NAMED",
         GATE_OLD, GATE_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "A Report Names Its Items: origin note -> the two-axes correction",
         NOTE_OLD, NOTE_NEW),
        ("PROJECT_INSTRUCTIONS.md",
         "v3.49: founding-case paragraph -> the two-axes correction",
         V349_OLD, V349_NEW),
        ("LEDGER_CONSOLIDATED.md",
         "L-269: two axes separated, gate closed, Gap narrowed",
         L269_OLD, L269_NEW),
        ("LEDGER_CONSOLIDATED.md",
         "L-270 opened: README.md is a stale live store",
         L270_ANCHOR, L270_BLOCK + L270_ANCHOR),
        ("LEDGER_CONSOLIDATED.md",
         "L-237 Ref: cross-reference to L-270",
         L237_REF_OLD, L237_REF_NEW),
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
        print("  ok  %-56s %s" % (label, path))

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

    # ---- post-write verification: prove the new block is INDEXABLE ----
    # Writing bytes is not the same as writing a block ledger_index.py can
    # see. A three-hash header, or a metadata comment whose number does not
    # match, is invisible to it -- and the indexer reports a clean pass on a
    # file it silently skipped. So check the two things it keys on.
    print("\nVERIFY -- is L-270 visible to ledger_index.py?")
    with open("LEDGER_CONSOLIDATED.md", "rb") as f:
        back = f.read().replace(b"\r\n", b"\n")
    probes = [
        (b"\n#### [L-270] ", "four-hash detail header"),
        (b"<!-- L:270 status:OPEN", "metadata comment with matching number"),
    ]
    bad = []
    for probe, what in probes:
        n = back.count(probe)
        print("  %s  %-42s (%d)" % ("ok " if n == 1 else "MISS", what, n))
        if n != 1:
            bad.append(what)
    if bad:
        print("  The bytes were written but the block will NOT be indexed.")
        print("  Restore from LEDGER_CONSOLIDATED.md.bak and report this.")
        sys.exit(1)

    print("\nPATCH APPLIED")
    print("\nNEXT, and all of these are yours:")
    print("  (do) Run ledger_index.py. L-270 is new, so the index WILL")
    print("       change this time.")
    print("  (do) Archive the THREE spent L-269 patch scripts into")
    print("       documentation/, then re-run module_atlas.py. Two of them")
    print("       are sitting at the repo root being counted as")
    print("       undetermined-role modules, which inflates the very count")
    print("       L-270 is about.")
    print("  (do) Re-run maintenance_run.py before the push.")
    print("\nWhat changed, by name:")
    print("  PROJECT_INSTRUCTIONS.md")
    print("    Check All Parallel Pipelines   five consumers NAMED;"
          " in-file scoping removed")
    print("    A Report Names Its Items       origin note corrected")
    print("    v3.49 entry                    founding-case paragraph"
          " corrected")
    print("  LEDGER_CONSOLIDATED.md")
    print("    L-269  two axes separated; founding case closed;"
          " Gap narrowed")
    print("    L-270  NEW -- README.md is a stale live store")
    print("    L-237  Ref line gains L-270")
    print("\nThe five consumers now named in the gate:")
    print("    static plot        plot_objects              palomas_orrery.py")
    print("    animation          animate_objects           palomas_orrery.py")
    print("    social export      export_social_view        palomas_orrery.py")
    print("    gallery curation   tools/gallery_studio.py   GALLERY repo")
    print("    JSON conversion    tools/json_converter.py   GALLERY repo")
    print("\nStill carrying the OLD merged sentence, and NOT touched here:")
    print("    README.md")
    print("    documentation/CLAUDE.md")
    print("    skills/orrery-coding-conventions/SKILL.md")


if __name__ == "__main__":
    main()
