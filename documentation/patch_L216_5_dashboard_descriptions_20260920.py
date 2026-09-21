#!/usr/bin/env python3
"""patch_L216_5_dashboard_descriptions_20260920.py -- ORRERY.

The L-216 build changed what three of the dashboard's buttons do and left
their descriptions describing the tools as they were that morning. This
fixes that, and puts Tony's cache-build routine on the button he launches
the build from.

The three:

  Gallery Cache Builder -- Manual Run   said nothing about pausing
                                        OneDrive, the retries, the
                                        roll-back, or the swap log.
  Cache Siblings                        said it reports the builder's own
                                        .staging_* and .quarantine_*
                                        remnants. It now names every
                                        directory in data/ the builder did
                                        NOT make, which is how four
                                        OneDrive conflict copies became
                                        visible.
  Gallery Builder Offline Tests         said it covers first-build,
                                        nightly re-run and Guard v2. It
                                        now runs 190 checks, 23 of them
                                        over the retry, the roll-back, the
                                        swap log and the sibling report.

WHY IT IS A SEPARATE PATCH. The dashboard was not in the build manifest
and the build never opened it. It is the screen Tony launches these tools
from, so a description that is a day out of date is the same failure the
build was about: a thing the project knows, sitting where the person who
needs it will not meet it.

Built on palomas_orrery d426ec009301ca4c95152636363b0d8fd6bbe227
at https://github.com/tonylquintanilla/palomas_orrery , describing tools
at gallery a1a516cfbfe6c83fbd2c79c57a107feb0624ca27 .

RUN IT LIKE THIS, from the ORRERY repo root (the folder that holds
LEDGER_CONSOLIDATED.md), by opening this file in VS Code and clicking Run:

    python patch_L216_5_dashboard_descriptions_20260920.py

It edits one file, palomas_orrery_dashboard.py, and changes only text
shown to the reader -- three descriptions and the module's own stamp. No
button is added, removed or reordered, and no code path changes.

Module created: September 20, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "palomas_orrery_dashboard.py"
EXPECTED_FP = "360b0d389f955ea669ae4d8e6a993686"


# --------------------------------------------------------------------------
# 1. Gallery Cache Builder -- Manual Run
# --------------------------------------------------------------------------

BUILDER_OLD = b'''         "Manual serving-cache build. Runs from the gallery repo ROOT: the "
         "builder resolves its data/ paths from the working directory, so "
         "launching it from tools/ cannot find data/objects_config.json. "
         "With no flags it fetches from Horizons, validates, atomic-swaps "
         "the new cache into data/solar-system, and STOPS -- it does not "
         "commit or push. Commit it yourself in GitHub Desktop after the "
         "run finishes. Do not commit while it is still running: mid-build "
         "the working tree shows deletions only, which is the swap in "
         "progress, not data loss. The console stays open at the repo root "
         "if you want a flagged re-run (--dry-run --object <slug>, "
         "--first-build).",
'''

BUILDER_NEW = b'''         "Manual serving-cache build. Runs from the gallery repo ROOT: the "
         "builder resolves its data/ paths from the working directory, so "
         "launching it from tools/ cannot find data/objects_config.json. "
         "With no flags it fetches from Horizons, validates, atomic-swaps "
         "the new cache into data/solar-system, and STOPS -- it does not "
         "commit or push. Commit it yourself in GitHub Desktop after the "
         "run finishes. Do not commit while it is still running: mid-build "
         "the working tree shows deletions only, which is the swap in "
         "progress, not data loss. The console stays open at the repo root "
         "if you want a flagged re-run (--dry-run --object <slug>, "
         "--first-build).\\n"
         "\\n"
         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "
         "a pause lasts 2 hours -- then run the build and watch GitHub "
         "Desktop's change list. Afterwards run Gallery Maintenance Run -- "
         "offline; its last line reports the swap. The swap now retries a "
         "refused rename for about fifty seconds, and puts the PREVIOUS "
         "cache back if it still cannot finish, so you are never left "
         "without one. A line in data/cache_swap_log.jsonl showing more "
         "than one attempt and outcome \\"ok\\" is a refusal it absorbed -- "
         "and that line is the only way you will know, because a retry "
         "that worked looks like an ordinary run.",
'''


# --------------------------------------------------------------------------
# 2. Cache Siblings
# --------------------------------------------------------------------------

SIBLINGS_OLD = b'''        "Reports the served cache's sibling directories -- the .staging_* "
        "and .quarantine_* remnants -- with each one's age taken from the "
        "run id in its NAME, and names those the builder's next run should "
        "reap. Report-only: it exits 0 whatever it finds. It exists because "
        "the builder's sweep failed silently for six weeks and nothing said "
        "so (L-274); if it goes quiet again this says so within a day. "
        "Runs from the gallery repo ROOT and deletes nothing.",
'''

SIBLINGS_NEW = b'''        "Reports the served cache's sibling directories -- the .staging_* "
        "and .quarantine_* remnants -- with each one's age taken from the "
        "run id in its NAME, and names those the builder's next run should "
        "reap. Report-only: it exits 0 whatever it finds. It exists because "
        "the builder's sweep failed silently for six weeks and nothing said "
        "so (L-274); if it goes quiet again this says so within a day. "
        "Runs from the gallery repo ROOT and deletes nothing.\\n"
        "\\n"
        "SINCE 2026-09-20 (L-216) it also names every OTHER directory in "
        "data/, under its own heading -- OneDrive's conflict copies land "
        "there and the sweep will never touch them. It used to look only "
        "for the builder's own name shapes, so four of them printed as "
        "\\"no sibling directories\\". One had been published by accident "
        "and held the only copy of 38 days of run history, now kept at "
        "documentation/cache_run_history/. Judge a copy by what is inside "
        "it, not by its name.",
'''


# --------------------------------------------------------------------------
# 3. Gallery Builder Offline Tests
# --------------------------------------------------------------------------

TESTS_OLD = b'''        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network.",
'''

TESTS_NEW = b'''        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network. 190 checks as of 2026-09-20, up from 167: the new 23 "
        "cover the swap's retries, the roll-back that puts the previous "
        "cache back, the swap log, a dry run leaving that log alone, and "
        "the sibling report naming folders the builder did not make "
        "(L-216). The lock itself cannot be produced in a sandbox, so a "
        "refused rename is simulated through the builder's own _rename "
        "seam -- the same name the real build path goes through.",
'''


# --------------------------------------------------------------------------
# 4. The module's own stamp
# --------------------------------------------------------------------------

STAMP_OLD = b'''same thing. Typing now changes one short label, which says "press Find,
or Enter" whenever the box and the drawn list disagree -- without it a
typed-but-unsearched box would sit above a list that silently did not
match it. Clear empties the box and brings every group back in one
action.
"""
'''

STAMP_NEW = b'''same thing. Typing now changes one short label, which says "press Find,
or Enter" whenever the box and the drawn list disagree -- without it a
typed-but-unsearched box would sit above a list that silently did not
match it. Clear empties the box and brings every group back in one
action.
September 20, 2026 with Anthropic's Claude Opus 5 (L-216): rewrote three
descriptions the L-216 build had made stale, and put Tony's four-step
cache-build routine on Gallery Cache Builder -- Manual Run, which is the
screen he launches the build from. Gallery Cache Builder now carries the
routine and what the hardened swap does; Cache Siblings says it names
every other directory in data/, not only the builder's own leftovers;
Gallery Builder Offline Tests says 190 checks and what the new 23 cover.
No button added, removed or reordered, and no code path touched. The
dashboard was not in that build's manifest and the build never opened
it, which is how three descriptions came to describe tools as they were
the morning before.
"""
'''


EDITS = [
    ("Gallery Cache Builder -- Manual Run: the routine and the new swap",
     BUILDER_OLD, BUILDER_NEW),
    ("Cache Siblings: it names every other directory in data/ now",
     SIBLINGS_OLD, SIBLINGS_NEW),
    ("Gallery Builder Offline Tests: 190 checks, and what the new 23 cover",
     TESTS_OLD, TESTS_NEW),
    ("dashboard: module stamp for this edit", STAMP_OLD, STAMP_NEW),
]


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def main():
    if not os.path.isfile(TARGET):
        return fail(
            "%s is not in this folder (%s).\n"
            "         Run this from the ORRERY repo root -- the folder that\n"
            "         holds LEDGER_CONSOLIDATED.md and the dashboard -- not\n"
            "         from documentation/ and not from the gallery repo."
            % (TARGET, os.getcwd()))

    raw = open(TARGET, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    actual = hashlib.md5(content).hexdigest()
    if actual != EXPECTED_FP:
        return fail(
            "BASE MOVED. %s is not the file this patch was built against.\n"
            "         expected %s\n"
            "         found    %s\n"
            "         (Line endings were normalised before comparing, so CRLF\n"
            "         does not explain this -- the content differs.)"
            % (TARGET, EXPECTED_FP, actual))

    if was_crlf:
        print("note: the working copy is CRLF; it was compared with line")
        print("      endings normalised and will be written back CRLF.")

    out = content
    for label, old, new in EDITS:
        count = out.count(old)
        if count != 1:
            return fail("ANCHOR FAIL: expected 1 match, found %d for: %s"
                        % (count, label))
        out = out.replace(old, new)
        print("  ok  %s" % label)

    inserted = b"".join(new for _, _, new in EDITS)
    bad = sum(1 for byt in inserted if byt > 127)
    if bad:
        return fail("this patch would insert %d non-ASCII byte(s); refusing"
                    % bad)
    pre_existing = sum(1 for byt in content if byt > 127)
    if pre_existing:
        print("note: %s already held %d non-ASCII byte(s) this patch did not"
              % (TARGET, pre_existing))
        print("      reach; they are unchanged.")
    else:
        print("  ok  encoding gate: inserted text is ASCII; the file holds no")
        print("      non-ASCII bytes.")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(TARGET, "wb") as handle:
        handle.write(final)

    print("")
    print("patch applied (%d bytes)" % len(final))
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Move THIS script into documentation/. It has run.")
    print("  2. Open the dashboard and look at the three buttons:")
    print("         python palomas_orrery_dashboard.py")
    print("     Gallery Cache Builder -- Manual Run and Cache Siblings are")
    print("     under \"Gallery -- checks and data\"; Gallery Builder Offline")
    print("     Tests is under the gallery maintenance runner. The three")
    print("     descriptions are the only thing that changed, so if the")
    print("     dashboard opens and the buttons are where they were, it is")
    print("     right.")
    print("  3. Run the orrery maintenance run:")
    print("         python orrery_maintenance_run.py")
    print("     The module atlas reads this file's docstring, so expect")
    print("     MODULE_ATLAS.md and MODULE_INDEX.md in the written list.")
    print("  4. Commit and push.")
    print("")
    print("TONY-ACTION ROLLUP for this patch:")
    print("  (do)     steps 1 to 4 above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
