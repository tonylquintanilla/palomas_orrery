#!/usr/bin/env python3
"""patch_L216_4_records_20260920.py -- stage C of the L-216 build. ORRERY.

The records for a build that already landed. Four files, one transaction:

  1. skills/gallery-cache-builder/SKILL.md      1.5 -> 1.6
  2. PROJECT_INSTRUCTIONS.md                    v3.65 entry, v3.62 removed,
                                                header stamp and SHA anchor
  3. documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.62
  4. LEDGER_CONSOLIDATED.md                     L-216 as-built and new Gap

This is the four-step binding rule from ledger-and-session-records: bump
the version line, run skills_index.py, write the protocol history entry,
commit the three together. Step 3 is the one that stops firing, so it is
in the same patch as step 1 rather than left to a later checkpoint.

Built on palomas_orrery ba94e80e91c35d76a6e355ffff650373f64affa9
at https://github.com/tonylquintanilla/palomas_orrery ,
recording work that landed in the gallery at
a1a516cfbfe6c83fbd2c79c57a107feb0624ca27 .

RUN IT LIKE THIS, from the ORRERY repo root (the folder that holds
LEDGER_CONSOLIDATED.md), by opening this file in VS Code and clicking Run:

    python patch_L216_4_records_20260920.py

All-or-nothing: every file is read and checked first, and nothing is
written unless every edit in every file matches. Both generated zones --
the ledger's INDEX and the protocol's SKILL-MANIFEST -- are excluded from
the fingerprints, because this patch ends by telling you to run the tools
that rewrite them.

Module created: September 20, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


# ==========================================================================
# 1. skills/gallery-cache-builder/SKILL.md -- 1.5 to 1.6
# ==========================================================================

SKILL = "skills/gallery-cache-builder/SKILL.md"

S_VER_OLD = b"""Skill version: 1.5 | Cut from tonyquintanilla.github.io @ d9d7a48f (tools/check_cache_in_step.py, gallery_maintenance_run.py, data/objects_config.json) and palomas_orrery @ e1a79f67 (LEDGER_CONSOLIDATED.md L-216, L-322, L-334, L-336) | 2026-09-19, with Anthropic's Claude Opus 5
v1.5 adds the rule the project did not have written down anywhere until
"""

S_VER_NEW = b"""Skill version: 1.6 | Cut from tonyquintanilla.github.io @ a1a516cf (tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, documentation/check_cache_siblings.py, gallery_maintenance_run.py, .gitignore) and palomas_orrery @ ba94e80e (LEDGER_CONSOLIDATED.md L-216) | 2026-09-20, with Anthropic's Claude Opus 5
v1.6 records the build that stops a failed swap depending on a person
noticing (L-216): each rename is retried, a swap that still cannot finish
puts the previous generation back, and every run that reaches the swap
writes one line to `data/cache_swap_log.jsonl`, a tracked file outside the
generation. The count goes to FIVE occurrences, and pausing OneDrive did
not prevent the last two. It adds what Tony does before and after a hand
build, and it writes down two things that had lived only in code or only
in a ledger block: never `shutil.rmtree` anything in this tree, and judge
a conflict copy by what is inside it.
v1.5 adds the rule the project did not have written down anywhere until
"""


S_FRONT_OLD = b"""documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; and for the rule that a config change is not deployed until the cache is rebuilt. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers
"""

S_FRONT_NEW = b"""documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers
"""

S_KEYS_OLD = b"""assert_structural + shrink_gate (validation), atomic_swap_dir /
recover_incomplete_swap / _sweep_siblings (deployment), guard_monitor /
"""
S_KEYS_NEW = b"""assert_structural + shrink_gate (validation), atomic_swap_dir /
_rename_with_retry / restore_after_failed_swap / swap_log_write /
print_failed_swap_advice / recover_incomplete_swap / _sweep_siblings
(deployment), guard_monitor /
"""


S_BODY_OLD = b"""## Recovery from a failed swap: discard and re-run [QUALITY]

Tony's operational rule, 2026-08-19 (L-216). When a run leaves the gallery
repo showing deletions -- most visibly `data/solar-system/` gone, with
GitHub Desktop reporting deletions and no additions -- DISCARD the changes
in GitHub Desktop and RE-RUN the builder. Discard restores the live tree
from HEAD byte for byte; the re-run builds a fresh generation.

Three conditions make that safe, and they travel WITH the rule because the
rule is only safe while all three hold:

- the live tree is committed, so HEAD has something to restore from;
- the swap is all-or-nothing, so a failed run leaves a COMPLETE `.prev` or
  a complete staging directory and never a mixed one;
- nothing reaches the remote until Tony commits by hand.

Running with `--commit` breaks the third condition and therefore breaks
the rule. Do not use `--commit` while L-216 is open.

What causes it, as far as it is measured: a filesystem lock -- almost
certainly OneDrive -- makes directory renames fail. WHICH of the swap's
three renames the lock catches decides the damage. Catching the `.prev`
cleanup is harmless and self-heals, and it has been happening every night
since 2026-07-21; the roughly 30 `solar-system.quarantine_*` directories
are that, one per night, printing as normal because the builder is built
to survive it. Catching `staging -> live` has no in-run recovery and
leaves the live directory missing. Same cause, different victim.

THREE OCCURRENCES, so the exposure IS established (corrected 2026-09-19;
this skill said "one data point" until then and that was already false).
The `staging -> live` rename is exposed to the same lock as the cleanup.
It is not bad luck. The third was 2026-09-17, during the rebuild L-336's
deployment fault made necessary; Tony: "This is like the third time."

WHAT IS STILL NOT ESTABLISHED is the fix, and one thing that is NOT a fix
is a louder failure. The run record is written INSIDE the generation, so
a run whose swap fails strands its own record in a directory `.gitignore`
hides -- meaning the committed history shows no sign that a run lost its
data. Recording the swap OUTCOME outside the generation comes BEFORE
fixing the cause; otherwise every recurrence costs another evening of
inference.

TONY'S HAND ROUTINE, 2026-09-17, and it is deliberate rather than a
workaround he would rather not need. The scheduled nightly is SUSPENDED.
He pauses OneDrive syncing FIRST, runs the builder by hand, and watches
GitHub Desktop's change list, stopping if the commit does not form
correctly. Pausing sync before a re-run worked.

ONE STEP IS ADDED TO THE DISCARD RULE ABOVE when the change list also
holds work that is not the cache -- which it did on 2026-09-17, because
the arrival work was sitting beside the wreckage. COMMIT THE NON-CACHE
FILES FIRST, then discard the rest, then re-run. A blanket discard would
have thrown away committed-worthy work.

MOVING THE REPOSITORIES OFF ONEDRIVE is the lasting fix and Tony's answer
on 2026-09-17 was "not at this time". It changes his machine outside his
usual working set and needs its steps and risks written out before he
decides. Do not propose it casually.

"""

S_BODY_NEW = b"""## The swap retries, rolls back, and leaves a record [QUALITY]

Built 2026-09-20 (L-216), at gallery `a1a516cf`. Before it, a refused
`staging -> live` rename left the working copy with no served cache, a
change list that looked like total loss, and the run's own record stranded
inside a directory `.gitignore` hides. Whether anything bad happened next
depended on Tony reading that change list correctly.

THREE THINGS THE BUILDER NOW DOES, in the order L-216 asked for them.

- EVERY RUN THAT REACHES THE SWAP WRITES ONE LINE to
  `data/cache_swap_log.jsonl`, a TRACKED file that is a SIBLING of the
  served directory rather than part of it -- same blast-radius reasoning
  as the config (L-114). The line is appended with outcome `started`
  before the swap and that same line is rewritten with the outcome after,
  so a process killed outright mid-swap leaves a `started` line saying a
  run reached the swap and never reported back. A dry run writes nothing.
  This came FIRST because without it nothing else here is observable.
- EACH RENAME IS RETRIED. `SWAP_RENAME_ATTEMPTS` is 6 and
  `SWAP_RENAME_WAITS` spends about fifty seconds in total, which is longer
  than any refusal measured. Every attempt after the first prints.
- A SWAP THAT STILL CANNOT FINISH PUTS THE OLD CACHE BACK.
  `restore_after_failed_swap` renames `.prev` back to live with the same
  retries and returns one word -- `live_intact`, `rolled_back`,
  `nothing_to_restore` or `rollback_refused` -- read off the filesystem
  rather than off whichever rename raised. The staging directory is KEPT;
  the sweep reaps it after keep_days.

READING THE LOG IS THE ONLY EVIDENCE THERE IS, because a retry that worked
looks exactly like a run with no problem at all. A LINE WITH MORE THAN ONE
ATTEMPT AND OUTCOME `ok` IS A FAILURE THIS BUILD ABSORBED. A log that only
ever shows one attempt means the lock has not recurred, and proves nothing
either way -- say that rather than claiming success.
`gallery_maintenance_run.py` prints the last line's verdict at the end of
its summary, so it lands on a screen Tony already reads.

WHAT TONY DOES, and it is a routine rather than a judgement call:

  1. Pause OneDrive syncing, and NOTE THE TIME. A pause lasts 2 hours.
  2. Run the builder by hand -- see Operating mode.
  3. Watch GitHub Desktop's change list; do not commit if it looks wrong.
  4. Afterwards, read the last line of `data/cache_swap_log.jsonl`.

Step 4 is new with this version and it is the point of the whole build:
it is the one step that does not depend on anyone noticing anything.

## Recovery by hand, when the roll-back also fails [QUALITY]

The builder now prints these in plain words when it needs them. They are
here too, because a session explaining them should not have to read the
source to do it.

- DISCARD AND RE-RUN. In GitHub Desktop, discard the changes, then run the
  builder again; discard restores the live tree from HEAD byte for byte.
  ONE STEP IS ADDED when the change list also holds work that is NOT the
  cache -- which it did on 2026-09-17, because the arrival work was
  sitting beside the wreckage. COMMIT THE NON-CACHE FILES FIRST, then
  discard the rest, then re-run. A blanket discard throws away
  committed-worthy work.
- RENAME THE STAGING FOLDER. In File Explorer, rename
  `.staging_solar-system_<runid>` to `solar-system`. Tony did this on
  2026-09-20, minutes after Python had been refused, and it worked -- so
  the lock is brief, and Windows will rename a directory it refuses to
  delete.

Three conditions make the discard rule safe and they travel WITH it:

- the live tree is committed, so HEAD has something to restore from;
- the swap is all-or-nothing, so a failed run leaves a COMPLETE `.prev` or
  a complete staging directory and never a mixed one;
- nothing reaches the remote until Tony commits by hand.

Running with `--commit` breaks the third condition and therefore breaks
the rule. Do not use `--commit` while L-216 is open.

## The cause, and what is still open

A filesystem lock -- OneDrive -- makes directory renames fail. WHICH of
the swap's renames it catches decides the damage. Catching the `.prev`
cleanup is harmless and self-heals; the roughly 30
`solar-system.quarantine_*` directories from 2026-07-21 onward are that,
one per night, printing as normal because the builder is built to survive
it. Catching `staging -> live` is the one that hurts.

FIVE OCCURRENCES: 2026-07-24, 2026-08-19, 2026-09-17, and TWICE on
2026-09-20. The exposure is established, not bad luck, and both ends of
that list carry a fact worth keeping.

THE FIRST ONE WAS NOT CAUGHT. On 2026-07-24 a SCHEDULED run's swap failed
with nobody aware a build was in flight; the mass deletion was read as
routine cleanup and was committed and pushed, then reverted after the
fact. So the human check has not merely risked failing -- it failed once,
and retiring the schedule on 2026-08-10 is what made Tony present for the
four since. (The account is in the gallery repo, in the Origin paragraph
of `documentation/AS_BUILT_L173_numbering_fix.md` and the
`verify_promoted_data` docstring.)

THE LAST TWO HAPPENED WITH SYNCING PAUSED. Both 2026-09-20 failures came
with OneDrive paused, so pausing is not a reliable cure. Unconfirmed and
worth carrying: the two staging directories are 1 hour 57 minutes apart
and a pause lasts 2 hours, so the pause may have expired about when the
second run reached its swap. That is why step 1 of the routine above says
to note the time.

MOVING THE REPOSITORIES OFF ONEDRIVE is the lasting fix and it is
UNDECIDED. Tony, 2026-09-17: "not at this time"; on 2026-09-20, having
seen occurrences four and five, he ruled "do option 1" -- harden the swap
-- "and take it from there as needed". It changes his machine outside his
usual working set. Do NOT propose it casually. If he raises it, what he
wants first is the data inventory, a backup plan for the gitignored local
data (966.8 MB, including star tables he says are difficult to rebuild),
the steps in GitHub Desktop's own terms, and what could go wrong at each
step. The whole analysis is written out in L-216 so it need not be argued
from memory again.

## Never shutil.rmtree anything in this tree [QUALITY]

Every directory under `data/` here carries the Windows read-only attribute
OneDrive sets. Windows permits RENAMING a read-only directory and REFUSES
to delete one, so a plain `shutil.rmtree` dies with `[WinError 5] Access
is denied` at the first subdirectory it reaches. The files inside are not
read-only; only the directories are. Use the `_rmtree_force` pattern: an
`onexc`/`onerror` callback that ADDS the write bit and retries, returning
the count of entries that needed it so a recovery that fired is reported
rather than silent.

THIS APPLIES TO ANY CODE TOUCHING THE TREE, not only the builder. On
2026-09-20 a patch script moving 42 run records out of a conflict copy
called plain `shutil.rmtree` and failed exactly this way, after the
records had been copied and verified. Nothing was lost and the commit was
unaffected -- rmtree unlinks files before it removes directories, and it
failed at the rmdir of a folder it had just emptied -- but a second patch
was needed to finish. The fix already existed in `_rmtree_force` with the
reason in its docstring, and the session that wrote the patch had read
that function an hour earlier. Knowledge that lives only inside a function
does not fire; that is why it is in the skill now.

[QUALITY] rather than [CRITICAL] on this document's own promotion test:
the failure is LOUD and recoverable, and the critical tier only works
while it stays short.

## The sibling report names what the builder did not make [QUALITY]

`documentation/check_cache_siblings.py` globbed only the two name shapes
the BUILDER makes, so four OneDrive conflict copies sitting beside the
cache -- `solar-system (1)`, `(2)`, `(3)` and `1260806133443-solar-system`
-- printed as "no sibling directories". It was a report that could not see
the thing it exists to report. Since 2026-09-20 it classifies EVERY
directory in `data/` and names anything that is neither the live cache,
nor `.prev`, nor a builder-made sibling, under its own heading. `.gitignore`
carries the two known conflict-copy shapes, `data/solar-system (*)/` and
`data/[0-9]*-solar-system/`. Neither the rules nor the report removes
anything; they make it visible.

JUDGE A CONFLICT COPY BY WHAT IS INSIDE IT, not by its name. One of those
four had been committed and published by accident and was described as 42
published files that serve nothing -- a count, from someone who had not
opened them. They turned out to be the ONLY copy of the run history for
2026-07-29 to 2026-09-04, 38 days the live cache's own records skip,
including the 2026-08-19 failure. Those 42 records now live at
`documentation/cache_run_history/` in the gallery repo, with a README
saying where they came from.

"""


# ==========================================================================
# 2. PROJECT_INSTRUCTIONS.md
# ==========================================================================

PROTOCOL = "PROJECT_INSTRUCTIONS.md"

P_HEAD_OLD = b"""Tony Quintanilla, PE | Claude | v3.64 | September 19, 2026

Cut from 21065c5d at https://github.com/tonylquintanilla/palomas_orrery
"""
P_HEAD_NEW = b"""Tony Quintanilla, PE | Claude | v3.65 | September 20, 2026

Cut from ba94e80e at https://github.com/tonylquintanilla/palomas_orrery
"""


P_NEW_ENTRY_OLD = b"""v3.64 (September 19, 2026): No rule changed in this document. ONE
skill bump, taken after a review found a rule being decided in the
wrong place.
"""

P_NEW_ENTRY_NEW = b"""v3.65 (September 20, 2026): No rule changed in this document. ONE
skill bump, taken AFTER the build it records, which is v3.62's
exception rather than v3.55's ordering: three of these rules were
learned while the build ran and there was nothing to write before it.

gallery-cache-builder 1.5 -> 1.6 (L-216). THE CACHE SWAP STOPS
DEPENDING ON TONY NOTICING.

WHAT LANDED, in the gallery at `a1a516cf`. Each rename inside the swap
is retried for about fifty seconds. A swap that still cannot finish
renames the previous generation back, so the working copy is never left
without a served cache and GitHub Desktop never shows the pile of
deletions. And every run that reaches the swap writes one line to
`data/cache_swap_log.jsonl`, a tracked file OUTSIDE the generation --
which L-216 has said since 2026-08-19 must come first, because a run
whose swap fails strands its own record where `.gitignore` hides it.
The offline suite went from 167 checks to 190, and each of the three
pieces was removed on purpose to confirm the matching checks go red by
name.

THE COUNT IS FIVE, and the two ends of the list are the argument. The
first occurrence, 2026-07-24, was a SCHEDULED run: nobody knew a build
was in flight, the mass deletion was read as routine cleanup, and it
was committed and pushed before being reverted. The human check did not
merely risk failing; it failed once. The last two, both on 2026-09-20,
happened with OneDrive syncing PAUSED, so pausing is not the cure it
looked like. Tony's words are in L-216: "catching the failures depended
on me stopping with the malformed commit lists, but the fix was not
obvious."

TWO RULES IN THE SKILL CAME FROM MISTAKES MADE DURING THE BUILD, and
both are the same shape. A patch script called plain `shutil.rmtree` on
the cache tree and was refused by the read-only attribute OneDrive sets
-- the exact failure `_rmtree_force` was written for, in a docstring
the session had read an hour earlier. And the build manifest described
a folder by a COUNT, "42 published files that serve nothing", written
by an author who had not opened them; they were the only copy of 38
days of run history. Knowledge that lives only inside a function does
not fire, and a count does not say what is there. Both now live in the
skill.

THE MOVE OFF ONEDRIVE IS NOT DECIDED and is not to be pressed. Tony
ruled "do option 1 and take it from there as needed" on 2026-09-20; the
analysis he asked to have recorded, including what a move would need
first, is written into L-216.

THE OBLIGATION TRAVELS, as it always does. This session loaded 1.5, and
a reinstall cannot be verified from inside the session that makes it.
The next session confirms its loaded copy reads 1.6 before cache work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.62 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.64 (September 19, 2026): No rule changed in this document. ONE
skill bump, taken after a review found a rule being decided in the
wrong place.
"""


# The v3.62 entry, removed from the protocol in full. Its first and last
# lines are reproduced exactly; the body lives in P_V362_BODY below and is
# checked against the file before anything is written.
P_V362_HEAD = b"v3.62 (September 19, 2026): No rule changed in this document. TWO skill"
P_V362_TAIL = b"""Version history: v3.59 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""


# ==========================================================================
# 3. documentation/PROJECT_INSTRUCTIONS_HISTORY.md
# ==========================================================================

HISTORY = "documentation/PROJECT_INSTRUCTIONS_HISTORY.md"

H_ANCHOR_OLD = b"""(Moved down from the resident protocol on 2026-09-19 when v3.64
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
"""


# ==========================================================================
# 4. LEDGER_CONSOLIDATED.md
# ==========================================================================

LEDGER = "LEDGER_CONSOLIDATED.md"

L_GAP_OLD = b"""**Gap (corrected 2026-09-20):** the CAUSE, and now a specified fix for
the exposure. `documentation/BUILD_MANIFEST_L216_cache_swap_20260920.md`
carries the build: retry each rename, put the old cache back if the swap
still fails, record every swap's outcome in a tracked file outside the
generation, and keep OneDrive's conflict copies out of git. Until that
lands, the only thing between a failed swap and a bad commit is Tony
reading the change list. The move off OneDrive stays Tony's and is
undecided.
"""

L_GAP_NEW = b"""**Note (2026-09-20) -- AS BUILT.** The build in
`documentation/BUILD_MANIFEST_L216_cache_swap_20260920.md` is done, in
three gallery pushes: `d0317aa3` (the hardening), then `a1a516cf` (the
run history moved and the conflict copy removed). Built by Claude Opus 5
from a manifest written by Claude Fable 5.1, Tony integrating.
WHAT THE BUILDER DOES NOW. Each rename inside the swap is retried six
times over about fifty seconds. A swap that still cannot finish renames
`.prev` back to live, so the working copy is never left without a served
cache and GitHub Desktop never shows the pile of deletions; the staging
directory is kept. Every run that reaches the swap writes ONE line to
`data/cache_swap_log.jsonl` -- tracked, and a sibling of the served
directory rather than part of it -- appended as `started` before the swap
and rewritten with the outcome after. A dry run writes nothing. When the
roll-back also fails the builder prints, in plain words, that nothing is
lost and which two hand recoveries to use; it never says "will self-heal"
without saying what Tony does.
HOW WE WILL KNOW IT WORKS, and it is the only evidence there is, because
a retry that worked looks exactly like a run with no problem: A LINE IN
THE LOG WITH MORE THAN ONE ATTEMPT AND OUTCOME `ok` IS A FAILURE THIS
BUILD ABSORBED. `gallery_maintenance_run.py` prints the last line's
verdict at the end of its summary. If the log only ever shows one
attempt, the lock has not recurred and nothing is proven either way.
TESTED. The offline suite went from 167 checks to 190. Each of the three
pieces was then removed on purpose and the matching checks went red BY
NAME -- 4 for the retry, 5 for the roll-back, 7 for the log. One of those
runs found a real weakness first: a missing log crashed the suite instead
of failing a named check, which is the blind spot not announcing, and it
was fixed before delivery.
PIECE 4. `.gitignore` gains `data/solar-system (*)/` and
`data/[0-9]*-solar-system/`, and `documentation/check_cache_siblings.py`
now classifies EVERY directory in `data/` and names anything the builder
did not make. It found four on Tony's machine at the first run, having
reported "no sibling directories" the day before.
THE RUN HISTORY IS KEPT. The 42 records are at
`documentation/cache_run_history/` in the gallery repo with a README, and
`data/1260806133443-solar-system/` is gone.
**Note (2026-09-20) -- two mistakes made during this build, both recorded
because they are the same shape.** A patch script called plain
`shutil.rmtree` on the cache tree and was refused by the Windows
read-only attribute -- the exact failure `_rmtree_force` was written for,
in a docstring the session had read an hour earlier. Nothing was lost
(rmtree unlinks files before removing directories, and it failed at the
rmdir of a folder it had just emptied), but a second patch was needed to
finish. And the build manifest described the conflict copy by a COUNT,
"42 published files that serve nothing", written by an author who had not
opened them. Fable 5.1 named its own error on review: "I counted the
files and never opened them." Knowledge that lives only inside a function
does not fire, and a count does not say what is there. Both rules are now
in `gallery-cache-builder` 1.6.
**Tony-action (do) -- carried, not cleared:** this session loaded
gallery-cache-builder 1.5 and bumped it to 1.6. A reinstall cannot be
verified from inside the session that makes it. The next session confirms
its loaded copy reads 1.6 before cache work.
**Gap (corrected 2026-09-20, after the build):** the CAUSE. The exposure
is handled and the fix is in; what remains is whether the repositories
stay under OneDrive. WATCH THE SWAP LOG: a line with more than one
attempt and outcome `ok` is the fix doing its job, and Tony should expect
one within a few weeks. The move off OneDrive is Tony's and is UNDECIDED;
the analysis, the inventory and what a move would need first are in the
2026-09-20 notes above, so it need not be argued from memory.
"""


L_STAMP_OLD = b"""(L-216: occurrences four and five recorded, the three OneDrive options
weighed and Tony's ruling written down; the 38-day hole in the committed
run history measured and its only copy named; the 2026-07-24 occurrence
corrected on Fable 5.1's review), built on ee37cc1f.
"""
L_STAMP_NEW = b"""(L-216: occurrences four and five recorded, the three OneDrive options
weighed and Tony's ruling written down; the 38-day hole in the committed
run history measured and its only copy named; the 2026-07-24 occurrence
corrected on Fable 5.1's review), built on ee37cc1f.
Module updated: September 20, 2026 with Anthropic's Claude Opus 5 (L-216
as built: the swap retries, rolls back and logs; the run history kept;
gallery-cache-builder 1.5 -> 1.6 and protocol v3.65), built on ba94e80e.
"""


# ==========================================================================
# The transaction
# ==========================================================================

INDEX_ZONES = {
    LEDGER: (b"<!-- INDEX:START", b"<!-- INDEX:END -->"),
    PROTOCOL: (b"<!-- SKILL-MANIFEST:START", b"<!-- SKILL-MANIFEST:END -->"),
}

FILES = [
    (SKILL, "b36e855259bb2007649b91dc1c5581ba", [
        ("skill: version line 1.5 -> 1.6", S_VER_OLD, S_VER_NEW),
        ("skill: description and fires_when reach the new subject matter",
         S_FRONT_OLD, S_FRONT_NEW),
        ("skill: key functions gain the new names", S_KEYS_OLD, S_KEYS_NEW),
        ("skill: retry/roll-back/log, hand recovery, the cause, rmtree, "
         "siblings", S_BODY_OLD, S_BODY_NEW),
    ]),
    (PROTOCOL, "6684f79aa91c786d92e338a950645f43", []),
    (HISTORY, "014ddf570af857926d1073ad7becef1d", []),
    (LEDGER, "57fba9cfd744be7dcdc8097061412fc4", [
        ("ledger: L-216 as-built, the two mistakes, new Gap",
         L_GAP_OLD, L_GAP_NEW),
        ("ledger: header currency stamp", L_STAMP_OLD, L_STAMP_NEW),
    ]),
]


def fail(msg):
    print("")
    print("FAILURE: %s" % msg)
    print("NOTHING was written -- not one of the four files.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 1


def content_of(path):
    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    return (raw.replace(b"\r\n", b"\n") if was_crlf else raw), was_crlf


def fingerprint(path, content):
    """Hash OUTSIDE any generated zone, because this patch ends by telling
    the operator to run the tool that rewrites it."""
    zone = INDEX_ZONES.get(path)
    if not zone:
        return hashlib.md5(content).hexdigest()
    start, end = zone
    a = content.index(start)
    b = content.index(end) + len(end)
    return hashlib.md5(content[:a] + content[b:]).hexdigest()


def main():
    if not os.path.isfile(LEDGER) or not os.path.isfile(PROTOCOL):
        return fail(
            "this is not the orrery repo root (%s).\n"
            "         Run it from the folder that holds\n"
            "         LEDGER_CONSOLIDATED.md and PROJECT_INSTRUCTIONS.md."
            % os.getcwd())

    staged = []
    for path, expected, edits in FILES:
        if not os.path.isfile(path):
            return fail("%s is missing from this checkout." % path)
        content, was_crlf = content_of(path)
        actual = fingerprint(path, content)
        if actual != expected:
            return fail(
                "BASE MOVED. %s is not the file this patch was built\n"
                "         against.\n"
                "         expected %s\n"
                "         found    %s\n"
                "         (Compared with line endings normalised and with any\n"
                "         generated zone excluded, so neither CRLF nor a\n"
                "         ledger_index.py or skills_index.py run explains it.)"
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
        staged.append([path, out, content, was_crlf])

    by_path = dict((row[0], row) for row in staged)

    # ---- the protocol: add v3.65, lift v3.62 out whole ------------------
    proto = by_path[PROTOCOL]
    text = proto[1]
    for label, old, new in (
            ("protocol: header stamp, version and SHA anchor",
             P_HEAD_OLD, P_HEAD_NEW),
            ("protocol: the v3.65 entry", P_NEW_ENTRY_OLD, P_NEW_ENTRY_NEW)):
        if text.count(old) != 1:
            return fail("ANCHOR FAIL: expected 1 match for: %s" % label)
        text = text.replace(old, new)
        print("  ok  %s" % label)

    if text.count(P_V362_HEAD) != 1 or text.count(P_V362_TAIL) != 1:
        return fail("ANCHOR FAIL: could not bound the v3.62 entry uniquely")
    start = text.index(P_V362_HEAD)
    end = text.index(P_V362_TAIL) + len(P_V362_TAIL)
    if end <= start:
        return fail("ANCHOR FAIL: the v3.62 entry's end precedes its start")
    v362 = text[start:end]
    if b"interactive-exhibit 1.3 -> 1.4" not in v362:
        return fail("ANCHOR FAIL: the block lifted out is not the v3.62 entry")
    text = text[:start] + text[end:]
    proto[1] = text
    print("  ok  protocol: v3.62 lifted out (%d bytes) to keep three resident"
          % len(v362))

    # ---- the history file receives it -----------------------------------
    hist = by_path[HISTORY]
    if hist[1].count(H_ANCHOR_OLD) != 1:
        return fail("ANCHOR FAIL: could not find the end of PART 1 in %s"
                    % HISTORY)
    moved = (v362.rstrip(b"\n") + b"\n\n"
             + b"(Moved down from the resident protocol on 2026-09-20 when\n"
             + b"v3.65 made a fourth entry.)\n\n")
    hist[1] = hist[1].replace(
        H_ANCHOR_OLD,
        H_ANCHOR_OLD.split(b"\n\n====")[0] + b"\n\n" + moved
        + b"================================================================\n"
        + b"PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n")
    print("  ok  history: v3.62 appended to PART 1, before the PART 2 banner")

    # ---- encoding gate ---------------------------------------------------
    inserted = b"".join(
        [new for _, _, edits in FILES for _, _, new in edits]
        + [P_HEAD_NEW, P_NEW_ENTRY_NEW, moved])
    bad = sum(1 for byt in inserted if byt > 127)
    if bad:
        return fail("this patch would insert %d non-ASCII byte(s); refusing"
                    % bad)
    dirty = [(row[0], sum(1 for byt in row[2] if byt > 127)) for row in staged]
    dirty = [(p, n) for p, n in dirty if n]
    if dirty:
        for path, n in dirty:
            print("note: %s already held %d non-ASCII byte(s) this patch did"
                  % (path, n))
            print("      not reach; they are unchanged.")
    else:
        print("  ok  encoding gate: inserted text is ASCII, and none of the")
        print("      four files holds a non-ASCII byte.")

    for path, out, _before, was_crlf in staged:
        final = out.replace(b"\n", b"\r\n") if was_crlf else out
        with open(path, "wb") as handle:
            handle.write(final)
        print("  wrote %s (%d bytes)%s"
              % (path, len(final), " [CRLF, as found]" if was_crlf else ""))

    print("")
    print("patch applied to 4 file(s)")
    print("  stamped: the skill's version line and cut-from SHAs, the")
    print("           protocol's header and anchor, the ledger's header.")
    print("")
    print("WHAT TO DO NEXT, in this order:")
    print("")
    print("  1. Move THIS script into documentation/. It has run.")
    print("  2. From this same folder, regenerate both zones:")
    print("         python ledger_index.py LEDGER_CONSOLIDATED.md")
    print("         python skills_index.py")
    print("     The ledger's open-item count should not change -- this patch")
    print("     added no new L-handle. skills_index.py should report")
    print("     gallery-cache-builder moving 1.5 -> 1.6 in the manifest.")
    print("  3. Run the orrery maintenance run:")
    print("         python orrery_maintenance_run.py")
    print("  4. Commit all of it together in GitHub Desktop and push.")
    print("  5. REINSTALL the skill: Settings > Skills, reinstall")
    print("     gallery-cache-builder so the account copy reads 1.6.")
    print("     This session cannot verify that from the inside, which is")
    print("     why L-216 now carries it as an obligation for the NEXT")
    print("     session to discharge.")
    print("  6. Tell Claude the new orrery SHA.")
    print("")
    print("TONY-ACTION ROLLUP for this stage:")
    print("  (do)     steps 1 to 6 above.")
    print("  (do)     at your next hand cache build: pause OneDrive and note")
    print("           the time, then read the last line of")
    print("           data/cache_swap_log.jsonl afterwards. A line with more")
    print("           than one attempt and outcome \"ok\" is a failure this")
    print("           build absorbed.")
    print("  (decide) still open, unpressed: whether the repositories move")
    print("           off OneDrive. L-216 holds the analysis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
