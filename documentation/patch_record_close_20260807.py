"""
patch_record_close_20260807.py

Closes the record for the August 7 session. The CODE landed at 17dab34;
this brings the ledger, the master plan and the plan summary into
agreement with it.

Built on a24b867a5f472d7824f27ddd3d031908915e11e3 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the palomas_orrery folder (the folder holding
    LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.
    Equivalent command line: python patch_record_close_20260807.py

WHAT IT DOES
    LEDGER_CONSOLIDATED.md
        L-179 -> DONE, section C, with the as-built note
        L-180 -> DONE, section C, with the as-built note
        + L-188  Maintenance runner (one command, the whole suite)
        + L-189  Scanner run history and run-to-run delta
    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
        Section 7 decision 14 marked RESOLVED with the rulings
    documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md
        the UNRUN PATCH section rewritten as an as-built record;
        scanner figures, protocol version and skill state refreshed;
        anchor updated

AFTER RUNNING
    1. Run ledger_index.py (Developer Tools on the dashboard). It
       regenerates the INDEX table from the DETAIL blocks and migrates
       the two DONE items into section C. The index rows are NOT edited
       here on purpose -- the generator owns them.
    2. Commit and push in GitHub Desktop.

SAFETY
    Each file is fingerprinted on CONTENT (line endings normalized before
    hashing) and every anchor must match exactly once. Any mismatch aborts
    with NOTHING WAS WRITTEN. Line endings are preserved per file. The
    ledger contains non-ASCII characters (em dashes, approx signs), so all
    matching is byte-level in binary mode and anchors avoid those
    characters entirely.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
PLAN = 'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md'
SUMMARY = 'documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md'

FINGERPRINTS = {
    LEDGER:  'ad8da59bfcd0e850b113980ae0379070',
    PLAN:    'bb835f0dc259bb4828f152db60d93b61',
    SUMMARY: '325214257a198214e92536e837ebf995',
}

EDITS = {}

# ==================================================================
# LEDGER
# ==================================================================
EDITS[LEDGER] = [
    (
        "L-179 -> DONE",
        b"<!-- L:179 status:OPEN upd:2026-08-04 section:A flag: rice:4/3/40/3 -->\n",
        b"<!-- L:179 status:DONE upd:2026-08-07 section:C flag: rice:4/3/40/3 -->\n",
    ),
    (
        "L-179 as-built note",
        b"**Gap:** Resolve which value is authoritative. Update the loser.\n"
        b"**Ref:** FABLE_shell_consistency_audit_report.md findings #29-30;\n",

        b"- **RULED (Tony, 2026-08-07): 150,000 AU stands.** His reasoning:\n"
        b"  it is the range interpolation from the cross check -- the midpoint\n"
        b"  of the published 100,000-200,000 AU spread. The store already held\n"
        b"  150,000 (corrected 2026-08-02); every divergent copy was downstream.\n"
        b"- **DONE 2026-08-07, pushed at `17dab34`** (base `d38d314`,\n"
        b"  patch_L179_L180_derivation_v3.py). Five sites corrected, and the\n"
        b"  approach is derivation rather than replacement: no display figure\n"
        b"  is typed any more. Added to `constants_new.py`:\n"
        b"  `GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)` as DATA, and\n"
        b"  `AU_PER_LIGHT_YEAR` derived from `SPEED_OF_LIGHT_KM_S` and\n"
        b"  `KM_PER_AU`. `GRAVITATIONAL_INFLUENCE_SENTENCE` in\n"
        b"  `solar_visualization_shells.py` builds the statement once; both\n"
        b"  duplicate display strings reference it.\n"
        b"- **Per Tony's ruling the text carries the ENVELOPE, not the point.**\n"
        b"  Rendered: \"extends to roughly 2.4 light-years (~150,000 AU).\n"
        b"  Published estimates range 100,000-200,000 AU (1.6-3.2 light-years);\n"
        b"  this visualization draws the midpoint.\" Show-the-Envelope applied\n"
        b"  to a model-dependent quantity: the midpoint is a choice, and the\n"
        b"  hover says so rather than implying a measurement.\n"
        b"- **The geometry was never wrong.** `create_sphere_points` has drawn\n"
        b"  at 150,000 AU since 2026-08-02; the import chain from the store\n"
        b"  through `planet_visualization_utilities.py` is clean, with no\n"
        b"  shadow constant. Only the words had drifted. One store correct,\n"
        b"  four restatements adrift, every offline test passing throughout --\n"
        b"  L-181's thesis demonstrated in miniature.\n"
        b"- **Two citations were asserting a value the store did not hold**\n"
        b"  (`GRAVITATIONAL_INFLUENCE_AU=126000` at lines 50 and 174). One of\n"
        b"  them cited the constant for a string that states no such figure at\n"
        b"  all. Cite-to-clear caught in the wild: both passed every scanner\n"
        b"  run precisely because they were cited.\n"
        b"- **`palomas_orrery.py` line 10295 was the hard case** -- a bare\n"
        b"  \"126,000 AU\" in a scale-suggestion tooltip with no import and no\n"
        b"  link to the store. Now interpolated. Nothing mechanical would have\n"
        b"  found it; it is wrong only RELATIVE to a value in another file.\n"
        b"- **The whole divergent class was enumerated, not assumed.** A\n"
        b"  20-line check over all 157 Python files and 35 store constants,\n"
        b"  looking for citations that name a constant and state a value\n"
        b"  disagreeing with it, found exactly three sites: two here and one\n"
        b"  in L-180. The class is closed. The scanner is blind to it by\n"
        b"  construction (it flags UNCITED claims), which is why they\n"
        b"  survived. That check is the seed of L-189.\n"
        b"- Verified after the push: scanner Tier-1 unchanged at 206, no file's\n"
        b"  Tier-1 rose, +2 Tier-2 from the new constants registering as\n"
        b"  claims. SHA round trip confirmed against `17dab34`.\n"
        b"- Field note, recorded in safe-file-editing 1.3: the delivery hit a\n"
        b"  CRLF working copy whose content was byte-identical to the repo,\n"
        b"  and the patch harness read that as BASE MOVED. Fingerprint content,\n"
        b"  not raw bytes; translate anchors to the file's own convention.\n"
        b"  Nothing was edited on Tony's side and git was right all along.\n"
        b"**Gap:** None. Closed.\n"
        b"**Ref:** patch_L179_L180_derivation_v3.py (pushed `17dab34`);\n"
        b"FABLE_shell_consistency_audit_report.md findings #29-30;\n",
    ),
    (
        "L-180 -> DONE",
        b"<!-- L:180 status:OPEN upd:2026-08-04 section:A flag: rice:3/3/30/2 -->\n",
        b"<!-- L:180 status:DONE upd:2026-08-07 section:C flag: rice:3/3/30/2 -->\n",
    ),
    (
        "L-180 as-built note",
        b"**Gap:** Reconcile text, add Show-the-Envelope comment.\n"
        b"**Ref:** FABLE_shell_consistency_audit_report.md finding #31;\n",

        b"- **RULED (Tony, 2026-08-07): 1.1 stands as the drawn value; the\n"
        b"  other figures change to match.** The drawn shell is a declared\n"
        b"  stylization and the text now says so instead of implying a\n"
        b"  measurement.\n"
        b"- **DONE 2026-08-07, pushed at `17dab34`**, same patch as L-179.\n"
        b"  Added to `constants_new.py`: `CHROMOSPHERE_PHYSICAL_KM = 2000.0`\n"
        b"  (Carroll & Ostlie Ch. 11) and `CHROMOSPHERE_PHYSICAL_RADII`,\n"
        b"  derived as `1 + CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM`. Both\n"
        b"  drawn and physical extents are now first-class stored values that\n"
        b"  answer different questions.\n"
        b"- `CHROMOSPHERE_RADIUS_LINE` builds the statement once; both\n"
        b"  duplicate display strings reference it. Rendered: \"drawn from the\n"
        b"  photosphere out to 1.1 solar radii (~0.00465 - 0.00512 AU). This is\n"
        b"  a stylization for visibility: the physical chromosphere extends\n"
        b"  only ~2,000 km above the photosphere (~1.003 solar radii).\"\n"
        b"- The third extent (1.5) lived only in a `# Source:` comment claiming\n"
        b"  the store held that value; the store has held 1.1 since 2026-08-02.\n"
        b"  Corrected, with the erratum recorded at the site.\n"
        b"- Note for whoever writes the next erratum: the divergence check\n"
        b"  (L-189) initially fired on these very notes, because a comment\n"
        b"  saying \"X was wrong\" contains the same NAME=value shape as a\n"
        b"  comment asserting X. The notes were reworded rather than the\n"
        b"  checker taught exceptions -- a check that fires on its own fix is\n"
        b"  one people learn to ignore.\n"
        b"**Gap:** None. Closed.\n"
        b"**Ref:** patch_L179_L180_derivation_v3.py (pushed `17dab34`);\n"
        b"FABLE_shell_consistency_audit_report.md finding #31;\n",
    ),
    (
        "add L-188 and L-189",
        b"**Gap:** Write the enumeration. Then decide scope from real numbers.\n"
        b"**Ref:** FABLE_REVIEW_feature_constant_unification.md, Open Question 2(d)\n"
        b"and findings summary #5.\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",

        b"**Gap:** Write the enumeration. Then decide scope from real numbers.\n"
        b"**Ref:** FABLE_REVIEW_feature_constant_unification.md, Open Question 2(d)\n"
        b"and findings summary #5.\n"
        b"\n"
        b"#### [L-188] Maintenance runner -- one command, the whole suite\n"
        b"<!-- L:188 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/70/2 -->\n"
        b"- **Tony's idea, 2026-08-07:** \"a common batch file could run a suite\n"
        b"  of files that should run after every update, including module\n"
        b"  atlas.\" Raised while looking at a test file that had been failing\n"
        b"  for five days with nobody watching.\n"
        b"- **The problem is not discoverability.** `palomas_orrery_dashboard.py`\n"
        b"  already lists eight maintenance tools under Developer Tools, each\n"
        b"  with a description saying when to run it. They still get skipped:\n"
        b"  the skill manifest advertised wrong versions for about three weeks,\n"
        b"  and `test_constants_provenance.py` sat false for five days. Eight\n"
        b"  separate judgment calls after every edit is eight chances to skip\n"
        b"  one.\n"
        b"- **Therefore the design constraint: it must REPLACE the individual\n"
        b"  entries, not join them.** A ninth menu item reproduces the exact\n"
        b"  failure. One action instead of five, not a sixth thing to remember.\n"
        b"- Two kinds of tool, and the split decides the shape. GENERATORS\n"
        b"  rewrite a file and are safe to run every time (`ledger_index.py`,\n"
        b"  `skills_index.py`, `module_atlas.py`, `data_inventory.py`); running\n"
        b"  them when nothing changed is a no-op. CHECKERS report a problem and\n"
        b"  inform the push call (`provenance_scanner.py`, and whatever L-155\n"
        b"  absorbs from the constants pins); these run last so their verdict is\n"
        b"  the last thing on screen. `dep_trace.py` stays OUT -- it takes a\n"
        b"  module name and answers a question BEFORE an edit, a different job.\n"
        b"- Useful precedent: `ledger_index.py` already has a `--check` mode\n"
        b"  that reports without rewriting and exits 1 on problems. That is the\n"
        b"  gate shape; the other generators would need the same mode added.\n"
        b"- Correction worth carrying: the scanner imports `module_atlas`'s\n"
        b"  FUNCTIONS directly rather than reading the generated\n"
        b"  `MODULE_ATLAS.md`, so it does NOT depend on the atlas being\n"
        b"  regenerated first. Ordering is for readability, not correctness --\n"
        b"  do not build a dependency that is not there.\n"
        b"**Gap:** **(decide)** does this ship as a dashboard entry that\n"
        b"replaces the eight, or as a script run before every push? Then build.\n"
        b"**Ref:** L-160 (the unrun test file that prompted it); L-184\n"
        b"(build-path push gate, same family); L-189.\n"
        b"\n"
        b"#### [L-189] Provenance scanner: run history and run-to-run delta\n"
        b"<!-- L:189 status:OPEN upd:2026-08-07 section:A flag: rice:3/4/80/2 -->\n"
        b"- **Tony's request, 2026-08-07:** \"could the scanner keep a log of\n"
        b"  results by date so we can track this? maybe the last 6 runs.\"\n"
        b"  Raised after a session where the only way to learn whether a patch\n"
        b"  had ADDED findings was for Claude to diff two committed copies of\n"
        b"  `PROVENANCE_AUDIT.md` from two commits -- which needs repo access\n"
        b"  and a script, and is therefore not a check Tony can run.\n"
        b"- **The number that matters is the DELTA, and it belongs on the\n"
        b"  console** where the push call actually gets made -- not in a file\n"
        b"  that has to be opened. \"206 Tier-1\" answers nothing on its own;\n"
        b"  \"206, unchanged, and no file's Tier-1 rose\" answers the question.\n"
        b"- Shape: `data/provenance_history.json`, a ring buffer of the last 6\n"
        b"  runs. Per run: timestamp, repo HEAD SHA (readable from `.git`\n"
        b"  without a git command), per-tier counts, per-domain counts, and\n"
        b"  Tier-1 per file. Console prints the delta after the priority\n"
        b"  summary and NAMES any file whose Tier-1 rose. `PROVENANCE_AUDIT.md`\n"
        b"  gets a matching Run History table.\n"
        b"- **Tony's call, 2026-08-07: TRACK the history file in git.** When an\n"
        b"  audit was taken and against which SHA is itself provenance. Cost is\n"
        b"  one small file showing as modified after each deliberate run.\n"
        b"- Stays INFORMATIONAL. The scanner's own comments are emphatic that\n"
        b"  Tier-1 never gets an auto-exit gate at any threshold; history makes\n"
        b"  the judgment better informed, it does not automate it.\n"
        b"- Build note: the scanner scans itself, so this change will nudge its\n"
        b"  own findings count. The first run after it lands shows a delta that\n"
        b"  IS the change; have it say so rather than let it read as a\n"
        b"  regression.\n"
        b"- Seed already written: the 20-line divergence check from the L-179\n"
        b"  session, which finds citations naming a constant and stating a value\n"
        b"  that disagrees with the store. It caught all 3 sites in the codebase\n"
        b"  and the scanner cannot -- it flags UNCITED claims, and these were\n"
        b"  cited. Worth folding in as a checker in its own right.\n"
        b"**Gap:** Build it. Additive change to a ~3,000-line shared tool;\n"
        b"treat as a shared-CI change with family-wide ripple.\n"
        b"**Ref:** provenance_scanner.py console summary block (~line 2909);\n"
        b"L-188; L-184.\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",
    ),
]

# ==================================================================
# MASTER PLAN -- Section 7 decision 14
# ==================================================================
EDITS[PLAN] = [
    (
        "decision 14 -> RESOLVED",
        b"14. **L-179 and L-180 values.** Solar gravitational influence (150,000 vs\n"
        b"    126,000 AU) and the solar chromosphere's three inconsistent extents.\n"
        b"    Both are drift inside `constants_new.py` today. Under the v17 order\n"
        b"    they are the FIRST thing Track 0 settles -- migrating and deriving\n"
        b"    before they are resolved would transport a known-inconsistent value\n"
        b"    into the served cache and the hover text, authoritative-looking in\n"
        b"    three more places.\n",

        b"14. ~~**L-179 and L-180 values.**~~ **RESOLVED 2026-08-07, pushed at\n"
        b"    `17dab34`.** Tony ruled 150,000 AU (the midpoint of the published\n"
        b"    100,000-200,000 AU range) and 1.1 solar radii as the DRAWN\n"
        b"    chromosphere shell, with the physical ~2,000 km extent stated\n"
        b"    alongside it. Both were closed by derivation rather than\n"
        b"    replacement: the ranges are stored as data\n"
        b"    (`GRAVITATIONAL_INFLUENCE_RANGE_AU`, `CHROMOSPHERE_PHYSICAL_KM`),\n"
        b"    the light-year figure derives from existing primaries, and one\n"
        b"    shared fragment per fact feeds every display site, so no number is\n"
        b"    typed. The divergent class was then enumerated rather than assumed:\n"
        b"    a check across all 157 Python files and 35 store constants found\n"
        b"    exactly three sites -- the two in L-179 and one in L-180 -- and\n"
        b"    reads zero after the patch. Track 0's first step is complete.\n",
    ),
]

# ==================================================================
# SUMMARY
# ==================================================================
EDITS[SUMMARY] = [
    (
        "re-anchor the summary",
        b"Built on d38d31482a8fedc8d6625930bc6d2ba2f15fb8cb at\n",
        b"Updated 2026-08-07 after the L-179/L-180 close. Built on\n"
        b"a24b867a5f472d7824f27ddd3d031908915e11e3 at\n",
    ),
    (
        "UNRUN PATCH section -> as-built record",
        b"UNRUN PATCH SITTING AT HEAD\n"
        b"\n"
        b"patch_L179_L180_derivation.py was committed at d38d314 and has not been\n"
        b"run -- L-179 and L-180 still read status:OPEN in the ledger. It did not\n"
        b"come from the August 6-7 design session.\n"
        b"\n"
        b"Checked before recording: its anchor 6623c69 is one commit back and is a\n"
        b"real ancestor, and none of its five target files have changed since, so\n"
        b"its base is still valid. It closes both items by making every displayed\n"
        b"figure DERIVE from constants_new.py rather than be typed -- which is the\n"
        b"Track 0 approach, so it is aligned rather than competing. It touches\n"
        b"constants_new.py, planet_visualization_utilities.py,\n"
        b"solar_visualization_shells.py, palomas_orrery.py, and\n"
        b"test_constants_provenance.py.\n"
        b"\n"
        b"One small note for later: it adds GRAVITATIONAL_INFLUENCE_RANGE_AU as a\n"
        b"tuple. Under fetch-and-import, tuples become JSON lists, which the\n"
        b"serialization boundary check should handle deliberately rather than\n"
        b"discover.\n",

        b"TRACK 0 STEP ONE IS DONE -- L-179 AND L-180 CLOSED\n"
        b"\n"
        b"Ruled and shipped August 7, pushed at 17dab34. Tony ruled 150,000 AU,\n"
        b"the midpoint of the published 100,000-200,000 AU range, and 1.1 solar\n"
        b"radii as the DRAWN chromosphere shell with the physical ~2,000 km\n"
        b"extent stated beside it.\n"
        b"\n"
        b"Both closed by DERIVATION, not replacement, which is why this doubles\n"
        b"as the first exercise of the Track 0 authoring pattern. Ranges are\n"
        b"stored as data; the light-year figure derives from constants already\n"
        b"in the store; one shared fragment per fact feeds every display site.\n"
        b"No displayed number is typed any more. Change the constant and the\n"
        b"hover text, the AU figure and the light-year figure all move together.\n"
        b"\n"
        b"The geometry was never wrong -- the shells have drawn at the correct\n"
        b"radii since August 2. Only the words had drifted, across four\n"
        b"restatements, with every offline test passing throughout. That is\n"
        b"L-181's thesis in miniature, at one-tenth of Jupiter's size.\n"
        b"\n"
        b"What it did NOT exercise, stated plainly so nobody reads it as a\n"
        b"transport test: no fetch across the repo boundary, no pre-import gate,\n"
        b"no FEATURE_REGISTRY, no validation layers, no builder. It rehearsed\n"
        b"the authoring side only. The Jupiter pilot is still the pilot.\n"
        b"\n"
        b"The divergent class was enumerated rather than assumed. A check across\n"
        b"all 157 Python files and 35 store constants, looking for a citation\n"
        b"that names a constant and states a value disagreeing with it, found\n"
        b"exactly three sites -- two in L-179, one in L-180 -- and reads zero\n"
        b"after the patch. The scanner cannot find these, by construction: it\n"
        b"flags UNCITED claims, and every one of these was cited. That check is\n"
        b"the seed of L-189.\n"
        b"\n"
        b"One live note carried forward: GRAVITATIONAL_INFLUENCE_RANGE_AU is a\n"
        b"tuple. Under fetch-and-import, tuples become JSON lists, which the\n"
        b"serialization boundary check should handle deliberately rather than\n"
        b"discover. This is now real code, not a hypothetical.\n"
        b"\n"
        b"A relay hazard worth recording: the previous revision of this summary\n"
        b"described that patch as something that \"did not come from the August\n"
        b"6-7 design session.\" It did -- it came from a sibling session on the\n"
        b"same day. A committed artifact carries no authorship, so a parallel\n"
        b"reader cannot tell the project's own work from a stranger's.\n",
    ),
    (
        "refresh the scanner figures",
        b"SCANNER STATE, MEASURED AT 4b82384\n"
        b"\n"
        b"A live run, not a figure carried from a handoff: 877 findings across 117\n"
        b"files. Tier 1 206, Tier 2 581, Tier 3 88, Tier 4 2.",

        b"SCANNER STATE, MEASURED AT 1ba20c3\n"
        b"\n"
        b"A live run, not a figure carried from a handoff: 879 findings across 117\n"
        b"files. Tier 1 206, Tier 2 583, Tier 3 88, Tier 4 2. Measured after the\n"
        b"L-179/L-180 close: Tier-1 unchanged, no file's Tier-1 count rose, and\n"
        b"the +2 is Tier-2 -- the new constants and display fragments registering\n"
        b"as claims, which is correct behavior rather than a gap. (The previous\n"
        b"figures, 877 at 4b82384, differ only by that.)",
    ),
    (
        "refresh protocol and skill state",
        b"L-162 (CENTER_BODY_RADII naming) done. Artifact 1 (Earth) built and\n"
        b"Mode-5 accepted, golden fingerprint locked. Protocol at v3.34 and all ten\n"
        b"skills reconciled across their three stores.",

        b"L-162 (CENTER_BODY_RADII naming) done. Artifact 1 (Earth) built and\n"
        b"Mode-5 accepted, golden fingerprint locked. L-179 and L-180 closed\n"
        b"August 7 (see above). Protocol at v3.35; safe-file-editing at 1.3\n"
        b"(Line Endings Are Not Content, added August 7), all ten skills\n"
        b"reconciled across their three stores.",
    ),
]


# ==================================================================
# Harness
# ==================================================================
def main():
    here = pathlib.Path(__file__).parent
    staged = {}
    problems = []

    for name, fp_expected in FINGERPRINTS.items():
        path = here / name
        if not path.exists():
            problems.append(f"MISSING: {name} (run this from the palomas_orrery folder)")
            continue

        data = path.read_bytes()
        fp_actual = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if not fp_expected.startswith('__') and fp_actual != fp_expected:
            problems.append(
                f"BASE MOVED: {name}\n"
                f"    expected content MD5 {fp_expected}\n"
                f"    actual   content MD5 {fp_actual}\n"
                f"    (line endings normalized, so this is a real content\n"
                f"     difference.) Do not force it."
            )
            continue

        is_crlf = data.count(b'\r\n') > 0
        if is_crlf:
            print(f"  ..  {name}: CRLF file -- anchors translated, endings preserved")

        for label, old, new in EDITS.get(name, []):
            o, n = (old, new)
            if is_crlf:
                o = o.replace(b'\n', b'\r\n')
                n = n.replace(b'\n', b'\r\n')
            count = data.count(o)
            if count != 1:
                problems.append(
                    f"ANCHOR {count} MATCHES (expected 1): {name} -- {label}\n"
                    f"    first 70 bytes: {o[:70]!r}"
                )
            else:
                data = data.replace(o, n, 1)

        staged[name] = data

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    for name, data in staged.items():
        (here / name).write_bytes(data)
        for label, _o, _n in EDITS.get(name, []):
            print(f"  ok  {name} -- {label}")

    print("\npatch applied")
    print("\nNext, in order:")
    print("  1. Run ledger_index.py (dashboard > Developer Tools). It rebuilds")
    print("     the INDEX table and moves L-179 and L-180 into section C.")
    print("  2. Commit and push in GitHub Desktop.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
