#!/usr/bin/env python3
"""patch_L216_8b_ledger_and_dashboard_20260921.py -- ORRERY repo.

Replaces patch_L216_8_ledger_and_dashboard_20260921.py, which was
withdrawn before it ran. Its ledger note said OneDrive made the new stray
folder `data/solar-system (4)` when Tony's sync pause ran out. His pause
never ran out; that was a guess stated as likely. This version records
what the stray-folder report actually measured.

Two files, one transaction.

  LEDGER_CONSOLIDATED.md, L-216
      The first real build on the new code (2026-09-21), with what it
      proves and what it does not; the four empty stray folders, measured;
      the three changes that followed the as-built (patches 5, 6 and 7);
      the skill wording owed to gallery-cache-builder's next bump; a
      corrected Gap.

  palomas_orrery_dashboard.py
      The builder button's routine now matches what the builder prints
      since patch 7 -- a [SWAP] line, then its own numbered steps, the
      maintenance run BEFORE the commit. Gallery Builder Offline Tests no
      longer carries a check count, which went stale the day after it was
      written.

WHY THE SKILL IS NOT TOUCHED. This session already moved
gallery-cache-builder to 1.6, and the project's rule is one version per
skill per session (ONE SESSION, ONE BUMP, L-296). The ledger note records
the wording the skill owes, so the next bump picks it up.

Built on palomas_orrery b9cd48440a8879f7c79207dfc181bfaaf584caf4
at https://github.com/tonylquintanilla/palomas_orrery , recording work
pushed to the gallery at 8a38a917f39df6e87108dce15285b978eb901e34 and
the stray-folder report Tony ran on 2026-09-21.

RUN IT LIKE THIS, from the ORRERY repo root (the folder that holds
LEDGER_CONSOLIDATED.md), by opening this file in VS Code and clicking Run:

    python patch_L216_8b_ledger_and_dashboard_20260921.py

All-or-nothing. The ledger's generated INDEX zone is excluded from its
fingerprint, because this patch ends by telling you to run the tool that
rewrites it.

Module created: September 21, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
DASHBOARD = "palomas_orrery_dashboard.py"


# ==========================================================================
# LEDGER_CONSOLIDATED.md
# ==========================================================================

L_META_OLD = b"<!-- L:216 status:OPEN upd:2026-09-20 section:A flag: rice:3/3/85/2 -->"
L_META_NEW = b"<!-- L:216 status:OPEN upd:2026-09-21 section:A flag: rice:3/3/85/2 -->"


L_GAP_OLD = b"""**Gap (corrected 2026-09-20, after the build):** the CAUSE. The exposure
is handled and the fix is in; what remains is whether the repositories
stay under OneDrive. WATCH THE SWAP LOG: a line with more than one
attempt and outcome `ok` is the fix doing its job, and Tony should expect
one within a few weeks. The move off OneDrive is Tony's and is UNDECIDED;
the analysis, the inventory and what a move would need first are in the
2026-09-20 notes above, so it need not be argued from memory.
"""

L_GAP_NEW = b"""**Note (2026-09-21) -- the first real build on the new code, and what it
does and does not prove.** Run `20260921T173303Z`, a hand build with
OneDrive paused beforehand, pushed at gallery `39bde09d`. Its swap log
line reads one attempt on each rename and outcome `ok`. The change list
held 25 changed files and 2 added -- this run's own record and the swap
log itself -- and no deletions. WHAT IT PROVES: the new code works on
Tony's machine. The swap log was written where it should be, as a tracked
file, one line; the `started` line was rewritten in place with the
outcome, which until then had only been tested in a sandbox; the
run-start recovery and the sweep each cleared the read-only bit on 6
entries and said so; and the live check confirmed the site serves the new
cache byte for byte. WHAT IT DOES NOT PROVE: the retry or the roll-back
against a real refusal, because nothing was refused. The only evidence of
those is still a line with more than one attempt.
**Note (2026-09-21) -- the empty "solar-system (N)" folders, measured.**
Four sat beside the cache, `(1)` to `(4)`; `(4)` appeared the same
afternoon as the build above. A report-only script,
`report_L216_stray_folders_20260921.py` in the gallery, captured what
only the folders could say before they were deleted. ALL FOUR WERE EMPTY,
hidden and system files counted, and each was empty from the start:
created at most four minutes before it was last modified, so nothing was
made at the swap and emptied later. EACH WAS CREATED 36 TO 39 MINUTES
AFTER A BUILD STARTED -- 36.9, 35.9, 38.6 and 38.2 minutes, after the
builds of 2026-09-05, 09-10, 09-18 and 09-21 -- on 4 of the 26 builds since
2026-09-05, with no pattern in the time of day. NOT TIED TO A COMMIT: the
nearest preceding commit was 2.7 minutes, 35.1 minutes, 11 seconds and
14.1 minutes earlier, and on 09-10 there was no commit anywhere near. NOT
MADE BY OUR CODE: Python never names a folder with " (N)", and nothing in
either repository creates a folder beside the cache; only Windows and
OneDrive name folders that way. PAUSING DOES NOT PREVENT IT: `(4)`
appeared with syncing paused the whole time. Every one carried OneDrive's
"always keep on this device" flag, but so does the live cache folder, so
the flag does not settle who made them.
CAUSE: UNDETERMINED. The strongest suspect is OneDrive, or the Windows
cloud-files layer beneath it, catching up on the swap after a delay.
That is a suspicion, not a finding. They are harmless as measured --
empty, kept out of git by `data/solar-system (*)/`, and named by the
sibling report whenever one appears -- so expect another now and then.
Tony was cleared to delete these four by hand on 2026-09-21, once the
report had been sent. IF THEY BECOME A NUISANCE, the choice is Tony's:
delete them by hand, or let the builder's sweep remove EMPTY ones -- which
would change the rule that the sweep never touches what the builder did
not make, the rule that kept the 42 run records safe. Not pressed.
A WRONG CLAIM, recorded because it nearly landed here. Claude told Tony
that OneDrive made `(4)` when his sync pause ran out. His pause never ran
out; it was a guess stated as likely. It was withdrawn, with the patch
that carried it, before that patch ran.
THREE CHANGES FOLLOWED THE AS-BUILT, recorded here so this block is
complete. PATCH 5, orrery `ac397e52`: the dashboard's descriptions of
three buttons, which the build never opened and so still described the
tools as they were the morning before. PATCH 6, gallery `06fdad8c`, Fable
5.1's final line break in `.gitignore`: stage B had kept the file's
missing final newline, which left the new `data/[0-9]*-solar-system/`
rule as the unterminated last line, so the next line anyone appended
would have joined it and broken it silently. PATCH 7, gallery `8a38a917`,
on Tony's two requests of 2026-09-21: the builder prints a `[SWAP]` line
after every good swap, so a clean swap is SAID rather than silent; it
ends a good hand run with its own numbered next steps, the maintenance
run BEFORE the commit; and the maintenance run's swap line reads EVERY
rename. Stage B's version read only `staging -> live`, so a refusal the
retry absorbed on the `.prev` cleanup -- the rename the lock catches most
-- would have printed "succeeded first time". A named check now fails if
that code comes back. The offline suite is at 201.
**Owed to gallery-cache-builder's next bump** (ONE SESSION, ONE BUMP --
this session already shipped 1.6). The routine should say the builder now
prints a `[SWAP]` line and its own next steps; that the maintenance run
comes BEFORE the commit; and that its last line should agree with the
`[SWAP]` line. "Reading the log" should say the maintenance run reads
every rename, not only the last. And the sibling-report section should
say the " (N)" folders measured on 2026-09-21 are empty and appear on a
delay after some builds -- it currently calls them conflict copies, which
the report does not support. The builder's printout and the dashboard
carry the routine meanwhile.
**The same "conflict copy" wording lives in four more places**, found by
search on 2026-09-21 and left for a pass that touches them anyway: the
comment above the two rules in the gallery's `.gitignore`; the docstring
of the gallery's `documentation/check_cache_siblings.py`; the orrery
dashboard's Cache Siblings description; and
`documentation/L342_install_test_run_sequence.md` in the orrery. It is
right for `1260806133443-solar-system`, which held real run records, and
unsupported for the empty " (N)" folders, whose maker is unknown.
**Gap (corrected 2026-09-21):** the CAUSE, unchanged. WATCH FOR A SWAP
THAT TOOK MORE THAN ONE ATTEMPT -- the builder's `[SWAP]` line now says it
on screen, and the maintenance run's last line reads it back from the
log. That is the fix doing its job, and until one appears the retry is
unproven. The empty " (N)" folders are a second, smaller symptom with the
same suspected cause and no known harm. The move off OneDrive is Tony's
and is UNDECIDED; the analysis, the inventory and what a move would need
first are in the 2026-09-20 notes above.
"""


L_STAMP_OLD = b"""gallery-cache-builder 1.5 -> 1.6 and protocol v3.65), built on ba94e80e.
"""
L_STAMP_NEW = b"""gallery-cache-builder 1.5 -> 1.6 and protocol v3.65), built on ba94e80e.
Module updated: September 21, 2026 with Anthropic's Claude Opus 5 (L-216:
the first real build on the new code, with what it proves and what it
does not; the empty " (N)" folders measured, cause undetermined; patches
5 to 7 recorded; the skill wording owed to its next bump), built on
b9cd4844.
"""


# ==========================================================================
# palomas_orrery_dashboard.py
# ==========================================================================

D_BUILDER_OLD = b'''         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "
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

D_BUILDER_NEW = b'''         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "
         "a pause lasts 2 hours -- then run the build. It ends with a "
         "[SWAP] line saying how the swap went, and then prints its own "
         "numbered next steps. Follow them: run Gallery Maintenance Run -- "
         "offline BEFORE you commit, and check that its last line agrees "
         "with the [SWAP] line; then look at GitHub Desktop's change list, "
         "commit and push. The swap retries a refused rename for about "
         "fifty seconds and puts the PREVIOUS cache back if it still "
         "cannot finish, so you are never left without one. A swap that "
         "took more than one attempt is a refusal the builder absorbed, "
         "and those two lines are the only way you will know.",
'''


D_TESTS_OLD = b'''        "No network. 190 checks as of 2026-09-20, up from 167: the new 23 "
        "cover the swap's retries, the roll-back that puts the previous "
        "cache back, the swap log, a dry run leaving that log alone, and "
        "the sibling report naming folders the builder did not make "
        "(L-216). The lock itself cannot be produced in a sandbox, so a "
        "refused rename is simulated through the builder's own _rename "
        "seam -- the same name the real build path goes through.",
'''

D_TESTS_NEW = b'''        "No network. Since L-216 it also covers the swap's retries, the "
        "roll-back that puts the previous cache back, the swap log, a dry "
        "run leaving that log alone, the sibling report naming folders the "
        "builder did not make, the builder SAYING how each swap went, the "
        "maintenance run reading every rename, and the next steps printing "
        "only after a good hand run. The lock itself cannot be produced in "
        "a sandbox, so a refused rename is simulated through the builder's "
        "own _rename seam -- the same name the real build path goes "
        "through. The run itself prints the current count of checks.",
'''


D_STAMP_OLD = b"""it, which is how three descriptions came to describe tools as they were
the morning before.
"""
D_STAMP_NEW = b"""it, which is how three descriptions came to describe tools as they were
the morning before.
September 21, 2026 with Anthropic's Claude Opus 5 (L-216, patch 8b): the
builder button's routine now matches what the builder prints -- a [SWAP]
line, then its own numbered steps, the maintenance run BEFORE the commit
-- and Gallery Builder Offline Tests no longer carries a check count,
which went stale the day after it was written.
"""


FILES = [
    (LEDGER, "2a7c0f347e560c071f6f3de5edf0c9c6", [
        ("ledger: L-216 metadata date 2026-09-20 -> 2026-09-21",
         L_META_OLD, L_META_NEW),
        ("ledger: the first real build, the stray folders measured, the "
         "wrong claim, patches 5-7, the owed skill wording, new Gap",
         L_GAP_OLD, L_GAP_NEW),
        ("ledger: header currency stamp", L_STAMP_OLD, L_STAMP_NEW),
    ]),
    (DASHBOARD, "fc3acdfeba36256730664f2a313ec6a7", [
        ("dashboard: the builder button's routine matches what it prints",
         D_BUILDER_OLD, D_BUILDER_NEW),
        ("dashboard: Gallery Builder Offline Tests drops the stale count",
         D_TESTS_OLD, D_TESTS_NEW),
        ("dashboard: module stamp for this edit", D_STAMP_OLD, D_STAMP_NEW),
    ]),
]

INDEX_ZONE = (b"<!-- INDEX:START", b"<!-- INDEX:END -->")


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written -- neither file.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def fingerprint(path, content):
    if path != LEDGER:
        return hashlib.md5(content).hexdigest()
    start, end = INDEX_ZONE
    a = content.index(start)
    b = content.index(end) + len(end)
    return hashlib.md5(content[:a] + content[b:]).hexdigest()


def main():
    if not os.path.isfile(LEDGER) or not os.path.isfile(DASHBOARD):
        return fail(
            "this is not the orrery repo root (%s).\n"
            "         Run it from the folder that holds LEDGER_CONSOLIDATED.md\n"
            "         and palomas_orrery_dashboard.py -- not from\n"
            "         documentation/ and not from the gallery repo."
            % os.getcwd())

    staged = []
    for path, expected, edits in FILES:
        raw = open(path, "rb").read()
        was_crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
        actual = fingerprint(path, content)
        if actual != expected:
            return fail(
                "BASE MOVED. %s is not the file this patch was built\n"
                "         against.\n"
                "         expected %s\n"
                "         found    %s\n"
                "         (Compared with line endings normalised and, for the\n"
                "         ledger, the generated INDEX zone excluded. If you ran\n"
                "         the WITHDRAWN patch 8 by mistake, this is why -- send\n"
                "         Claude this message and nothing is lost.)"
                % (path, expected, actual))
        if was_crlf:
            print("note: %s is CRLF here; compared normalised, written back"
                  % path)
            print("      CRLF exactly as found.")
        out = content
        for label, old, new in edits:
            count = out.count(old)
            if count != 1:
                return fail("ANCHOR FAIL: expected 1 match, found %d for: %s"
                            % (count, label))
            out = out.replace(old, new)
            print("  ok  %s" % label)
        staged.append((path, out, content, was_crlf))

    inserted = b"".join(new for _, _, edits in FILES for _, _, new in edits)
    bad = sum(1 for byt in inserted if byt > 127)
    if bad:
        return fail("this patch would insert %d non-ASCII byte(s); refusing"
                    % bad)
    dirty = [(p, sum(1 for byt in c if byt > 127)) for p, _, c, _ in staged]
    dirty = [(p, n) for p, n in dirty if n]
    if dirty:
        for path, n in dirty:
            print("note: %s already held %d non-ASCII byte(s) this patch did"
                  % (path, n))
            print("      not reach; they are unchanged.")
    else:
        print("  ok  encoding gate: inserted text is ASCII, and neither file")
        print("      holds a non-ASCII byte.")

    for path, out, _before, was_crlf in staged:
        final = out.replace(b"\n", b"\r\n") if was_crlf else out
        with open(path, "wb") as handle:
            handle.write(final)
        print("  wrote %s (%d bytes)%s"
              % (path, len(final), " [CRLF, as found]" if was_crlf else ""))

    print("")
    print("patch applied to 2 file(s)")
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Move THIS script into documentation/. It has run.")
    print("  2. From this same folder, regenerate the ledger index:")
    print("         python ledger_index.py LEDGER_CONSOLIDATED.md")
    print("     The open-item count should not change -- this patch added no")
    print("     new L-handle.")
    print("  3. Run the orrery maintenance run:")
    print("         python orrery_maintenance_run.py")
    print("     The module atlas reads the dashboard's docstring, so expect")
    print("     MODULE_ATLAS.md and MODULE_INDEX.md in the written list.")
    print("  4. Commit and push.")
    print("  5. Tell Claude the new orrery SHA.")
    print("")
    print("IN THE GALLERY REPO, when you next commit there:")
    print("  Move report_L216_stray_folders_20260921.py into documentation/,")
    print("  so the report the ledger cites is filed where it says.")
    print("")
    print("TONY-ACTION ROLLUP for this patch:")
    print("  (do)     steps 1 to 5 above.")
    print("  (do)     the gallery filing above, at your next gallery commit.")
    print("  (do)     delete the four empty solar-system (N) folders in File")
    print("           Explorer, if you have not already.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
