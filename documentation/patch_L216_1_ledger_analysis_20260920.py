#!/usr/bin/env python3
"""patch_L216_1_ledger_analysis_20260920.py -- stage A of the L-216 build.

Writes this session's analysis into L-216 of LEDGER_CONSOLIDATED.md so the
OneDrive question does not have to be argued from memory next time, and
records a measurement made while preparing the build: the committed run
history has a 38-day hole whose only copy is inside the conflict copy the
build manifest proposes to delete.

Built on palomas_orrery ee37cc1ff911d96e87fd5d714a456b53f2aef50e
at https://github.com/tonylquintanilla/palomas_orrery
and measured against tonyquintanilla.github.io
1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2.

Revised 2026-09-20 after a review by Claude Fable 5.1, which found one
sentence claiming more than the record supports. The July 24, 2026
occurrence was NOT caught by a person reading the change list; it was
committed, pushed, and reverted afterwards. The note now says so.

RUN IT LIKE THIS, from the ORRERY repo root (the folder that holds
LEDGER_CONSOLIDATED.md), by opening this file in VS Code and clicking Run:

    python patch_L216_1_ledger_analysis_20260920.py

It edits one file: LEDGER_CONSOLIDATED.md. It is all-or-nothing -- either
every edit lands or nothing is written. It does not commit, push, or run
any other tool; it prints the steps that follow.

Module created: September 20, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"

# The content fingerprint is taken OUTSIDE the generated INDEX zone, because
# this patch ends by telling the operator to run ledger_index.py, which
# rewrites that zone. A guard that fenced the zone would refuse for a reason
# that has nothing to do with content.
EXPECTED_FP = "dadbc1b942185e10bdd62c1c5341ce26"

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"


# --------------------------------------------------------------------------
# The edits. Each old_str must match exactly once.
# --------------------------------------------------------------------------

OLD_META = (
    b"<!-- L:216 status:OPEN upd:2026-09-19 section:A flag: rice:3/3/85/2 -->"
)
NEW_META = (
    b"<!-- L:216 status:OPEN upd:2026-09-20 section:A flag: rice:3/3/85/2 -->"
)


OLD_GAP = b"""**Gap (corrected 2026-09-17):** the CAUSE, not the exposure. Three
occurrences settle what one did not: the `staging -> live` rename IS
exposed to the same lock as the cleanup, and it is not bad luck. What
remains is the fix -- retry the renames with backoff, or move the
repository off OneDrive (Tony: not at this time) -- and the visibility
gap above, which still comes first.
"""

NEW_GAP = b"""**Note (2026-09-20) -- OCCURRENCES FOUR AND FIVE, and the OneDrive
question written out so it need not be argued from memory again.** The
swap failed twice more on 2026-09-20, both times at `staging -> live`
with "Access is denied", and both times with OneDrive syncing PAUSED.
Pausing is therefore not a reliable cure. The two staging directories
are 1 hour 57 minutes apart and a OneDrive pause lasts 2 hours, so the
pause may have expired about when the second run reached its swap. That
is a possibility worth carrying, not a finding; nobody checked the clock
at the time.
THE ONLY BARRIER SO FAR HAS BEEN A PERSON NOTICING, AND IT HAS ALREADY
FAILED ONCE. Tony, 2026-09-20: "catching the failures depended on me
stopping with the malformed commit lists, but the fix was not obvious."
The four occurrences from 2026-08-19 onward were each caught that way --
Tony read GitHub Desktop's change list and declined to commit, on a run
he had started himself. THE FIRST ONE WAS NOT. The 2026-07-24 run was
SCHEDULED, nobody knew a build was in flight, and the mass deletion was
read as routine cleanup: it was committed and pushed, then reverted
after the fact. The account is in the gallery repo, in the Origin
paragraph of `documentation/AS_BUILT_L173_numbering_fix.md` and in the
`verify_promoted_data` docstring in `tools/gallery_cache_builder.py`.
Retiring the schedule on 2026-08-10 is what made Tony present for every
run since. It is still one person looking, with nothing behind him, and
that is what stage B of the build manifest removes.
A SECOND RECOVERY ROUTE WAS MEASURED. Tony renamed the staging folder to
`solar-system` by hand in File Explorer, minutes after Python had been
refused, and it worked. So the lock is brief. The rule of 2026-08-19 --
discard the deletions in GitHub Desktop and re-run -- is unchanged and
still sound; this is a second way out, not a replacement for it.
THREE OPTIONS WERE WEIGHED, 2026-09-20.
- ONE, harden the swap. Retry each rename, put the old cache back if the
  swap still fails, and record every swap's outcome in a tracked file
  outside the generation. Makes a failure rare, and makes it visible
  without anyone having to notice anything. Does NOT remove the cause.
- TWO, keep the repositories under OneDrive and have the builder avoid
  the swap altogether. Not favoured. The all-or-nothing swap is the
  builder's main protection -- it is what guarantees that a failure
  leaves a complete old generation or a complete new one and never a
  mixture -- and the conflict copies dated 2026-09-05 onward show
  OneDrive fighting that folder independently of the builder anyway.
- THREE, move both repositories out of OneDrive. Removes the cause.
WHAT STANDS IN THE WAY OF THREE. GitHub holds everything that is
committed. OneDrive is today the only second copy of what `.gitignore`
excludes. `DATA_INVENTORY.md`, generated 2026-09-20, counts 966.8 MB of
local orrery data, including the Gaia star tables (`.vot`, 295.1 MB),
the star property files (`.pkl`, 33.6 MB), `orbit_paths.json`
(130.9 MB), the ERA5 climate files (`.nc`, 161.1 MB), and the `papers/`
folder. Tony, 2026-09-20: the large star data files are "difficult to
rebuild". A move needs a backup plan for these BEFORE it happens.
TWO FACTS THAT BEAR ON IT, Tony, 2026-09-20. He works on the repositories
from one computer. A Mac kept for Mac and Linux Python is rarely used and
its copy is badly stale. So OneDrive is not carrying the work between
machines; here it is buying a second copy, not portability.
**Tony's ruling, 2026-09-20:** "let's put your analysis in the ledger, do
option 1, and take it from there as needed." Option THREE is NOT decided
and is not to be pressed. If Tony raises it, what he wants first is the
inventory, a backup plan for the files above, the steps in GitHub
Desktop's own terms, and what could go wrong at each step -- all written
out before he decides anything.

**Note (2026-09-20) -- the committed run history has a 38-day hole, and
the only copy of it sits inside the conflict copy the build manifest
proposes to delete.** Measured at gallery `1061ae4d`.
`data/solar-system/raw/runs/` holds 37 run records: 2026-07-11 to
2026-07-28, then nothing at all until 2026-09-05, then near-daily to
2026-09-20. The TRACKED conflict copy
`data/1260806133443-solar-system/raw/runs/` holds 42 run records,
2026-07-29 to 2026-09-04, and not one of them appears in the live tree.
The two sets are disjoint and the second exactly fills the first's hole.
That window contains the 2026-08-19 occurrence and the whole of the
L-274 silent-sweep period.
WHY IT BEARS ON THE DECISION IN STAGE B. The manifest recommends
deleting `data/1260806133443-solar-system/` as 42 published files that
serve nothing. Serving nothing is correct -- they are records, not
served data. Deleting them would destroy the only committed evidence for
exactly the stretch this item is investigating, inside the build whose
stated purpose is that a recurrence should stop costing an evening of
inference.
HOW IT CAME TO BE RECOMMENDED is an instance of a rule this project
already holds. The manifest described the folder by a COUNT and its
author had not opened the files. Fable 5.1, reviewing this patch on
2026-09-20: "I counted the files and never opened them... I gave you a
count." A Report Names Its Items, measured once more.
**Claude's recommendation, for Tony to rule on:** keep the records and
move them. Copy the 42 files to `documentation/cache_run_history/` in
the gallery repo -- a name that is not a cache sibling, so it stops
reading as a stray generation and is not caught by the new ignore rules
-- and then delete the folder. Putting them back inside the live cache
is the worse option: nothing should write into that tree by hand.
**Tony-action (decide)**, due with stage B.

**Gap (corrected 2026-09-20):** the CAUSE, and now a specified fix for
the exposure. `documentation/BUILD_MANIFEST_L216_cache_swap_20260920.md`
carries the build: retry each rename, put the old cache back if the swap
still fails, record every swap's outcome in a tracked file outside the
generation, and keep OneDrive's conflict copies out of git. Until that
lands, the only thing between a failed swap and a bad commit is Tony
reading the change list. The move off OneDrive stays Tony's and is
undecided.
"""


OLD_STAMP = b"""built on 85c308cf.
Review and RICE update Tony 6-21-2026
"""

NEW_STAMP = b"""built on 85c308cf.
Module updated: September 20, 2026 with Anthropic's Claude Opus 5
(L-216: occurrences four and five recorded, the three OneDrive options
weighed and Tony's ruling written down; the 38-day hole in the committed
run history measured and its only copy named; the 2026-07-24 occurrence
corrected on Fable 5.1's review), built on ee37cc1f.
Review and RICE update Tony 6-21-2026
"""


EDITS = [
    ("L-216 metadata date 2026-09-19 -> 2026-09-20", OLD_META, NEW_META),
    ("L-216: the 2026-09-20 analysis, the run-history finding, new Gap",
     OLD_GAP, NEW_GAP),
    ("ledger header: currency stamp for this edit", OLD_STAMP, NEW_STAMP),
]


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def main():
    if not os.path.exists(TARGET):
        return fail(
            "%s is not in this folder (%s).\n"
            "         Run this from the ORRERY repo root -- the folder that\n"
            "         holds LEDGER_CONSOLIDATED.md and PROJECT_INSTRUCTIONS.md\n"
            "         -- not from documentation/ and not from the gallery repo."
            % (TARGET, os.getcwd()))

    raw = open(TARGET, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    try:
        a = content.index(INDEX_START)
        b = content.index(INDEX_END) + len(INDEX_END)
    except ValueError:
        return fail("could not find the INDEX:START / INDEX:END markers in %s"
                    % TARGET)

    actual = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if actual != EXPECTED_FP:
        return fail(
            "BASE MOVED. %s is not the file this patch was built against.\n"
            "         expected %s\n"
            "         found    %s\n"
            "         (Compared outside the generated INDEX zone, with line\n"
            "         endings normalised, so neither a ledger_index.py run\n"
            "         nor CRLF explains this -- the prose has changed.)"
            % (TARGET, EXPECTED_FP, actual))

    if was_crlf:
        print("note: the working copy is CRLF; anchors translated, and the")
        print("      file will be written back CRLF as found.")

    out = content
    for label, old, new in EDITS:
        n = out.count(old)
        if n != 1:
            return fail("ANCHOR FAIL: expected 1 match, found %d for: %s"
                        % (n, label))
        out = out.replace(old, new)
        print("  ok  %s" % label)

    # Encoding gate. Everything this patch inserts must be ASCII; anything
    # the file already held is reported either way, because a clean run on a
    # dirty file is how a convention quietly stops being true.
    inserted_non_ascii = sum(1 for byt in b"".join(new for _, _, new in EDITS)
                             if byt > 127)
    if inserted_non_ascii:
        return fail("this patch would insert %d non-ASCII byte(s); refusing"
                    % inserted_non_ascii)
    pre_existing = sum(1 for byt in content if byt > 127)
    if pre_existing:
        print("note: %s already held %d non-ASCII byte(s) this patch did not"
              % (TARGET, pre_existing))
        print("      reach; they are unchanged.")
    else:
        print("  ok  encoding gate: inserted text is ASCII; the file holds no")
        print("      non-ASCII bytes.")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(TARGET, "wb") as f:
        f.write(final)

    print("")
    print("patch applied (%d bytes)" % len(final))
    print("  stamped: the L-216 metadata date, and the ledger header's own")
    print("           currency block.")
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Put the build manifest in documentation/ if it is not there")
    print("     already, as")
    print("     documentation/BUILD_MANIFEST_L216_cache_swap_20260920.md .")
    print("     The new Gap points at that exact path.")
    print("  2. Move THIS script into documentation/ as well. It has run; it")
    print("     is kept as the record, not for re-use.")
    print("  3. From this same folder, regenerate the ledger index:")
    print("         python ledger_index.py LEDGER_CONSOLIDATED.md")
    print("     The open-item count should not change. This patch added no")
    print("     new L-handle.")
    print("  4. Run the orrery maintenance run:")
    print("         python orrery_maintenance_run.py")
    print("  5. Commit all of it together in GitHub Desktop and push.")
    print("  6. Tell Claude the new orrery SHA. Stage B is built against it.")
    print("")
    print("TONY-ACTION ROLLUP for this stage:")
    print("  (do)     steps 1 to 6 above.")
    print("  (decide) due with stage B, not now: whether the 42 run records")
    print("           in data/1260806133443-solar-system/raw/runs/ are moved")
    print("           to documentation/cache_run_history/ in the gallery repo")
    print("           before that folder is deleted. They are the only copy")
    print("           of the run history for 2026-07-29 to 2026-09-04.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
