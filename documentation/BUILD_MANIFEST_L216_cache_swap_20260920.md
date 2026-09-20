# Build Manifest -- L-216: the cache swap stops depending on Tony noticing

**Built on gallery `1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `ee37cc1ff911d96e87fd5d714a456b53f2aef50e`
at https://github.com/tonylquintanilla/palomas_orrery.
Both HEADs were read live with `git ls-remote` on 2026-09-20 and both
repositories cloned there. Everything in section 2 was read from those
clones.**

**Rules this work runs under.** Also fetch, from the orrery at
`ee37cc1f`: `PROJECT_INSTRUCTIONS.md` (v3.64) and these skills under
`skills/<name>/SKILL.md`: gallery-cache-builder 1.5,
safe-file-editing 1.11, agentic-pre-test 1.2,
ledger-and-session-records 1.11. Inside Tony's Project they load as
installed skills; compare each loaded version line with the protocol's
manifest table and STOP on a mismatch. **In your first reply, name the
rule files you actually read.**

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 20, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator. **For:** Claude Opus 5, as builder.
**Comes BEFORE** Stage C2 of L-322, which needs at least two cache
builds. `BRIEF_L322_C2_design_session_20260920.md` section 4 points
here.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. Write to him in plain sentences, one
request per message.

---

## 1. What is wrong, in plain terms

The cache builder makes a complete new copy of the served data in a
staging folder, then swaps it in with two renames: the live folder
becomes `.prev`, then the staging folder becomes live. On Tony's
machine the second rename is sometimes refused with "Access is denied".
It has happened five times: 2026-07-24, 2026-08-19, 2026-09-17, and
twice on 2026-09-20. OneDrive syncing was paused for the last two, so
pausing is not a reliable cure.

When it happens the working copy has NO served cache. GitHub Desktop
shows about sixty deletions and no additions, because the two folders
that still hold the data are hidden by `.gitignore`. Nothing is lost,
but it looks like total loss.

**The one thing that has protected the live site every time is Tony
reading the change list and stopping.** Tony, 2026-09-20: "catching the
failures depended on me stopping with the malformed commit lists, but
the fix was not obvious." A single human check with nothing behind it
is the fault this build removes. It does not remove the CAUSE, which is
the repository living under OneDrive. That decision is Tony's and is
recorded in stage A, not built here.

L-216 has named both halves of this build since 2026-08-19: record the
swap's outcome outside the generation FIRST, then retry the renames.
Neither was built.

## 2. What was measured at gallery `1061ae4d`

All in `tools/gallery_cache_builder.py`:

- `atomic_swap_dir` (line 1227) does three `os.replace` calls with no
  retry: a stale `.prev` to a quarantine name, live to `.prev`, staging
  to live.
- The caller (near line 1664) catches an `OSError` from the swap, prints
  "no commit; next run will self-heal", and returns. It does NOT put
  `.prev` back. So the live folder stays missing until another run
  starts.
- `recover_incomplete_swap` (line 1320) runs at the START of the next
  run and restores `.prev` to live if live is missing. On 2026-09-20
  the next run then met the same refusal.
- `_write_run_manifest` (line 1714) writes the run's record into
  `<staging>/raw/runs/`. A run whose swap fails strands its record in a
  folder `.gitignore` hides.
- `tools/test_gallery_cache_builder_offline.py` (near line 444) already
  tests a swap that raises, by replacing `atomic_swap_dir` with a
  function that raises. It does not test a rename that fails and then
  succeeds.

Elsewhere:

- `.gitignore` hides `data/.staging_*/`, `data/solar-system.prev*/`,
  `data/solar-system.quarantine_*/` and `data/_backup/`. It does not
  name OneDrive's conflict copies.
- `data/1260806133443-solar-system/` is TRACKED: 42 files, published on
  the live site, serving nothing. The as-built of L-342 reports three
  more on Tony's disk only: `solar-system (1)`, `(2)` and `(3)`.
- `documentation/check_cache_siblings.py` looks only for names the
  builder makes (lines 74 and 75). With four OneDrive copies beside the
  cache it printed "no sibling directories". It is a report that cannot
  see the thing it should report.
- The gallery's offline run is 15 of 15.

**Tony's recovery on 2026-09-20** was to rename the staging folder to
`solar-system` by hand in File Explorer. It worked minutes after Python
was refused. So the lock is brief. L-216's recorded rule from
2026-08-19 is different and also sound: discard the deletions in GitHub
Desktop and run again.

**Unconfirmed, worth carrying:** the two staging folders of 2026-09-20
are 1 hour 57 minutes apart and a OneDrive pause lasts 2 hours. The
pause may have expired about when the second run reached its swap.

## 3. Stage A -- the ledger patch (orrery)

On L-216, a dated note carrying this session's analysis, so the OneDrive
question does not have to be argued from memory next time:

- Occurrences four and five, 2026-09-20, with syncing paused.
- Tony's words quoted in section 1, and the point they make: the only
  barrier has been a person noticing.
- The three options weighed. ONE, harden the swap (this build): makes a
  failure rare and visible, does not remove the cause. TWO, keep the
  repositories under OneDrive and have the builder avoid the swap: not
  favoured, because the all-or-nothing swap is the builder's main
  protection, and the conflict copies dated 2026-09-05 onward show
  OneDrive fighting that folder apart from the builder. THREE, move both
  repositories out of OneDrive: removes the cause.
- What stands in the way of THREE. GitHub holds what is committed.
  OneDrive is today the only second copy of what `.gitignore` excludes.
  From `DATA_INVENTORY.md`, generated 2026-09-20: 966.8 MB of local
  orrery data, including the Gaia star tables (`.vot`, 295.1 MB), the
  star property files (`.pkl`, 33.6 MB), `orbit_paths.json` (130.9 MB),
  the ERA5 climate files (`.nc`, 161.1 MB), and the `papers/` folder.
  Tony, 2026-09-20: the large star data files are "difficult to
  rebuild". A move needs a backup plan for these BEFORE it happens.
- Facts that bear on it, Tony, 2026-09-20: one computer. A Mac exists
  for Mac and Linux Python, is rarely used, and its copy is badly stale.
  So OneDrive is not carrying the work between machines.
- Tony's ruling, 2026-09-20: "let's put your analysis in the ledger, do
  option 1, and take it from there as needed." Option THREE is NOT
  decided and is not to be pressed. If he asks, he wants the inventory,
  a backup plan, the steps in GitHub Desktop's terms, and what could go
  wrong at each step, written out first.
- New Gap: this manifest.

One ledger patch per pushed HEAD. `ledger_index.py` twice, same count.

## 4. Stage B -- the build (gallery)

Four pieces, one patch.

**Piece 1: the swap's outcome is recorded where a failure cannot hide
it.** Every run that reaches the swap appends ONE line to a tracked
file, `data/cache_swap_log.jsonl`, written BEFORE the swap is attempted
and completed after it: the run id, the time, which rename was reached,
how many attempts each rename took, the outcome in one word, and the
error text if any. It is written outside both the staging and the live
folder. A dry run writes nothing. This comes first because L-216 says
so: without it, every other piece is unobservable.

**Piece 2: each rename is retried.** A refused rename is tried again
after a short wait, several times, for about a minute in total. The
number of tries and the waits are named constants at the top of the
module with a comment saying why. Every retry prints a line. A rename
that succeeds first time behaves exactly as today.

**Piece 3: a swap that still fails puts the old cache back.** If
staging cannot become live after every try, the builder renames `.prev`
back to live, with the same retries, so the working copy is never left
without a served cache and GitHub Desktop never shows the deletions.
The staging folder is kept. The builder then prints a short block in
plain words: what happened, that nothing was lost, that the live site
is unaffected, and that the next step is simply to run the builder
again. If even the roll-back is refused, it prints the two hand
recoveries by name: discard the deletions in GitHub Desktop and run
again, or rename the staging folder to `solar-system` in File Explorer.
It never says "will self-heal" without saying what Tony does.

**Piece 4: OneDrive's copies are seen and kept out of git.**
`.gitignore` gains the two shapes, `data/solar-system (*)/` and
`data/[0-9]*-solar-system/`. `check_cache_siblings.py` reports EVERY
folder in `data/` other than `solar-system` and the names the builder
makes, by name, under its own heading "not made by the builder". It
stays report-only. The maintenance run's summary also prints the last
line of the swap log, so the most recent outcome is on the screen Tony
already reads.

**What this build must not change.** The swap stays all-or-nothing. No
file is written in place into the live folder. `.prev` is never
deleted by hand or by new code. Nothing here commits or pushes.

## 5. How we will know it is working

A retry that works looks exactly like a run with no problem, so the log
is the evidence. **A line in `data/cache_swap_log.jsonl` with more than
one attempt and outcome "ok" is a failure this build absorbed.** Tony
should expect to see one within a few weeks. If the log only ever shows
one attempt, the lock has not recurred and nothing is proven either
way; say so rather than claim success.

## 6. Tests

The lock cannot be produced in the sandbox, so `os.replace` is replaced
inside the offline test. Add to
`tools/test_gallery_cache_builder_offline.py`:

- refused twice, then allowed: the swap completes, the new generation is
  live, the log line says 3 attempts and "ok".
- refused every time on staging to live: the OLD generation is live
  again, byte for byte; staging is kept; the log line says
  "rolled_back"; the run does not commit.
- refused every time on both: live is missing, the plain-words block is
  printed, the log line says "failed".
- a dry run leaves the log untouched.
- the sibling report names a folder called `solar-system (1)` and one
  called `123-solar-system`.

Show each failing once on purpose before it passes: remove the retry,
remove the roll-back, remove the log write, and confirm the matching
test goes red and names it. Pre-test every delivered file under
agentic-pre-test.

## 7. Stage C -- records (orrery)

gallery-cache-builder 1.5 to 1.6, with ONE protocol entry (v3.65),
following the bump routine. The skill gains: the retry and the
roll-back; the swap log and what a multi-attempt line means; five
occurrences, and that pausing OneDrive did not prevent the last two;
the recovery steps in plain words; and that the sibling report now
names folders it did not make. The reinstall cannot be verified in the
session that makes it; write the obligation into the handoff.

L-216 stays OPEN for the cause. Its Gap becomes: watch the swap log;
the move off OneDrive is Tony's, undecided.

## 8. Tony's decisions, and when they fall due

1. **(decide, with stage B)** Remove
   `data/1260806133443-solar-system/` from the gallery. It is 42
   published files that serve nothing. Recommended: yes. In GitHub
   Desktop it will show as 42 deletions, which this once is correct;
   the patch's closing text must say so in those words, so the change
   list is not mistaken for a failed swap. The three local-only copies
   can then be deleted in File Explorer.
2. **(look, after the first real build)** The last line of
   `data/cache_swap_log.jsonl`.

## 9. Out of scope

- Moving the repositories. Recorded in stage A, not built, not pressed.
- Re-enabling the scheduled nightly run. Tony suspended it and builds by
  hand; that stays until he says otherwise.
- Any change to what the cache contains.
- Stage C2 of L-322.

## 10. Tony-action rollup

1. **(do)** File this manifest in the orrery's `documentation/`, commit,
   push. Give Opus this file and both SHAs, saying which is which.
2. **(do)** At each stage: run the patch from the ROOT of the repository
   it names, move it to `documentation/`, run that repository's
   maintenance run, commit, push, report the SHA.
3. **(do)** For the first cache build after stage B: pause OneDrive
   syncing as before, and note the time you paused it.

---

Written September 20, 2026 with Anthropic's Claude Fable 5.1.
