---
name: gallery-cache-builder
description: Nightly data-serving pipeline for the Paloma's Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers
---

# Gallery Cache Builder (Phase 1b data serving)

Skill version: 1.6 | Cut from tonyquintanilla.github.io @ a1a516cf (tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, documentation/check_cache_siblings.py, gallery_maintenance_run.py, .gitignore) and palomas_orrery @ ba94e80e (LEDGER_CONSOLIDATED.md L-216) | 2026-09-20, with Anthropic's Claude Opus 5
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
a config change reached the live site ahead of the cache and broke both
exhibit rooms: A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS
REBUILT (L-336). It also corrects this skill's own claim that the failed
`staging -> live` rename was "one data point" -- there have been three,
the third on 2026-09-17 -- and writes down the hand routine Tony
actually uses now.
v1.4 adds Recovery from a failed swap: discard and re-run -- Tony's
operational rule of 2026-08-19, after a nightly run wiped the served tree
and the ~30 quarantine directories turned out to be the same mechanism
printing harmlessly every night since July 21 (L-216).

The standalone builder that fetches fresh JPL Horizons data and deploys the
web gallery's served cache. Tony runs it MANUALLY and commits the result
himself; the scheduled nightly was retired August 10, 2026 (see Operating
mode below).

## Operating mode -- manual, as of August 10 2026

The Windows scheduled task is DISABLED, not deleted. Tony's ruling: "It
can't run without my machine being on anyway and it's consistent with me
being the only commit authority. And obviates complicated fail safe
procedures that could also fail."

What this means in practice:
- The builder is launched from the dashboard's Developer Tools group, or
  by running `tools/gallery_cache_builder.py` from the GALLERY REPO ROOT.
  The root matters: `--config` and `--output-dir` default to paths
  relative to the working directory, so launching from `tools/` fails at
  load_config.
- No flags runs nightly mode. `--commit` is NOT passed, so the builder
  swaps the new cache in and stops. Tony commits in GitHub Desktop.
- Because Tony starts the run, he knows a build is in flight. This is the
  substantive safety change: the atomic swap's window shows deletions only
  in a git client, and on August 10 that was committed by mistake by
  someone who did not know a build was running.
- A `pre-commit` hook refusing a deletion-only commit under
  `data/solar-system/` was designed and is deliberately NOT built. It
  becomes relevant again if the schedule returns, if a second person gains
  commit access to the gallery repo, or if the builder ever runs
  unattended in any other form.

The cadence question did not go away, it changed shape. "Did the nightly
run?" became "when did I last run it?" -- and a manual build has no
expected time at all, so an explicit staleness check is now the ONLY thing
that can report that the served data is eleven days old. That is L-189. A GALLERY-repo tool; this skill is authored in
the orrery repo per the L-002 convention (both SHAs on the cut line, like
gallery-pipeline). For the interactive Studio/converter/viewer chain, load
gallery-pipeline instead.

## What it is

tools/gallery_cache_builder.py: read data/objects_config.json -> fetch fresh
from JPL Horizons per object at its explicit canonical center -> validate in a
STAGING directory -> whole-generation atomic swap of data/solar-system/ ->
single verified commit + push. It REPLACES the served generation every run by
design (the prior cache's framing errors were unfixable in place), so "runs
without errors" is never the gate -- validation is. No orrery imports; the
hard-won fetch specifics are provenance-copied from the orrery with per-function
# Source comments, kept in sync on change.

Key functions: run_build (orchestrator), derive_served (raw -> served files),
assert_structural + shrink_gate (validation), atomic_swap_dir /
_rename_with_retry / restore_after_failed_swap / swap_log_write /
print_failed_swap_advice / recover_incomplete_swap / _sweep_siblings
(deployment), guard_monitor /
emit_guard_warnings (Guard v2), git_commit (push with round-trip verify),
douglas_peucker (glide thinning), load_config, main.

## Swap blast radius [QUALITY]

atomic_swap_dir replaces data/solar-system/ WHOLESALE (live -> .prev,
staging -> live; a rename is all-or-nothing, so a crash leaves either a
COMPLETE .prev or a COMPLETE live, never a mixed generation). Anything that must
survive a build lives OUTSIDE that directory. The config is a sibling,
data/objects_config.json, for exactly this reason (L-114: it was stranded into
.prev on every real build when it lived inside). Before adding any file the
builder READS but does not WRITE into staging, decide which side of the blast
radius it belongs on.

## Sibling directory semantics [QUALITY]

- data/solar-system.prev/ is the retained ONE-GENERATION rollback and the
  self-healing recovery source. NORMAL BUT SCARY: it looks like a stale
  duplicate; never hand-delete it. recover_incomplete_swap clears it at the
  next run's start once live is confirmed healthy.
- .staging_solar-system_* and solar-system.quarantine_* siblings are crash
  remnants. _sweep_siblings reaps them after keep_days (default 3); recent ones
  are kept deliberately as autopsies (A-11). Throwaway; do not build on them.
- A stale .prev that recovery cannot clear (e.g. a Windows file lock from a
  backup/AV process) is QUARANTINED and the run proceeds, rather than wedging
  every future run; the sweep reaps the quarantine later.

## Recovery ordering (why L-114 mattered twice)

recover_incomplete_swap runs at build start. load_config reads the sibling
data/objects_config.json, so it no longer depends on the swap-managed directory
existing -- which is what used to deadlock: config-inside-the-swap-dir meant a
crash mid-swap left load_config unable to read the config before recovery could
restore the directory. Moving the config out (L-114) closed that; a crash
mid-swap now self-heals on the next run.

## The swap retries, rolls back, and leaves a record [QUALITY]

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

## A config change is not deployed until the cache is rebuilt [CRITICAL]

The rooms in `interactive.html` draw their shells from the SERVED CACHE,
`data/solar-system/coverage_index.json`, which this builder copies from
`data/objects_config.json`. Pushing the config alone changes nothing a
visitor sees -- except where the two disagree, and there it breaks the
page.

WHAT HAPPENED, 2026-09-17 (L-336). L-322's gallery half was pushed at
gallery `d2ca28b6` before the builder had run. The unit spellings had
changed in the config and in the renderers (`R_sun` to `r_sun`); the
cache still held the old spelling; the renderers refused every shell
that used it. Tony's phone showed the Sun's room with 9 drawer rows
instead of 18 and Earth's with 8, on the live site, while the
maintenance run printed 11 of 11.

THE ROUTINE, and it is one routine rather than a judgement call:

  1. Change `data/objects_config.json`.
  2. Run this builder. By hand -- see Operating mode.
  3. Run `python gallery_maintenance_run.py`.
  4. Commit the CONFIG AND THE CACHE TOGETHER, and push.

`tools/check_cache_in_step.py` gates step 3 and compares the served
cache against the config it was built from. A red "Cache in step" right
after a config change is CORRECT and means step 2 has not happened yet.

THE ONE EXCEPTION, and it is worth knowing because it is the only part
of a room's data the page reads directly: the `arrival` block --
`drawn` and `moon` -- is fetched from `data/objects_config.json` by
`gallery/arrival.js`, not from the cache. A change to what a room OPENS
on needs only the push. Everything else needs the builder.

## Validation stance

Two dispositions, and the difference is load-bearing:
- ABORT (raise ValidationAbort -> nonzero exit; the nonzero exit surfaces in
  the console Tony is watching, since he starts the run -- through 2026-08-10
  this read "Task Scheduler history is the monitoring channel," which was
  true until the schedule was retired and is now the note to fix if the
  schedule ever returns): structural invariants (#2/#3/#C/#8), #B3
  conversion-consistency (served km must equal raw * AU at the matching point),
  the #T as_of_today freshness check, and the shrink_gate (per-object AND
  aggregate point count must be >= 95% of the live generation; first build is
  exempt).
- WARN AND KEEP, never reject: Guard v2 (guard_monitor / emit_guard_warnings,
  the per-object k*a(1+e) distance band). It is a MONITOR, not a gate.

Field note: an inline comment mislabels this as "guard/B3 WARN" (search for that string; it has drifted from line 755 to ~1099 and will move again).
#B3 is an ABORT -- the code raises ValidationAbort. The module docstring is
correct; the inline comment is stale (candidate cleanup, tracked separately).

## Commit with round-trip verify

git_commit (N2) does not report pushed_remote until it has confirmed the remote
branch CONTAINS the new SHA (git branch -r --contains). A local commit that
never reached GitHub Pages is the exact failure this closes -- the same SHA
round-trip discipline the project uses by hand, baked into the builder.

## The three-layer gate (documentation/TESTING_PROTOCOL.md, orrery repo)

- Layer 1 -- offline suite (mocked fetch, 75 checks): proves the LOGIC. Run
  `python3 tools/test_gallery_cache_builder_offline.py` from a CLEAN checkout
  after ANY builder or config-layout change -- it is the canary for path
  assumptions (the L-114 config move silently broke it until the test's own
  path was swept; see field notes).
- Layer 2 -- live dry-run on Tony's hardware: `--dry-run --object <slug>` per
  tranche object, then a real --first-build. Proves the OUTPUT against real
  Horizons.
- Layer 3 -- scheduling (unattended nightly). RETIRED 2026-08-10; the task
  is disabled, not deleted. The layer is kept here because it becomes live
  again the moment the build runs unattended by any mechanism, including a
  GitHub Action. Its gating items are unchanged (gap-aware catch-up, a
  health summary) -- see L-098 / L-111.

## Adding a new object -- the full sequence, and where it silently breaks

Beyond the three-layer gate above, onboarding a genuinely NEW object needs
two things the general gate description doesn't spell out:

- **--first-build is required, not --nightly, for a new non-spacecraft
  object.** Verified in code: only first-build mode fetches the full
  365-day backfill window for non-spacecraft objects; nightly mode only
  fetches [today - freeze, today] -- a few days. Add an object and run
  --nightly and it onboards with almost no data. first-build also carries
  the N3 floor check (rejects a clipped/truncated fetch), which nightly
  skips. Spacecraft are the one exception: a genuinely new one has no
  prior points, so the code auto-detects this (`not points`) and
  backfills fully regardless of mode.
- **Layer 1's offline suite has a hardcoded served-object COUNT
  assertion** (`check(len(objs) == N, ...)`), separate from the per-object
  ELEMS mock keys. Adding a new object's ELEMS entry is necessary but not
  sufficient -- the count itself needs bumping too, or Layer 1 fails on a
  fully correct addition. Caught concretely adding Halley (11 -> 12): the
  ELEMS/fake_solution_tp mocks were right the first pass; the count
  assertion was the thing still pointing at the old total.

Full sequence for onboarding: (1) source horizons_id/id_type/dates from
celestial_objects.py rather than deriving them -- usually already there
(see horizons-orbital-mechanics for the record-pinning rule); (2) add the
ELEMS mock entry (+ fake_solution_tp branch if Tp-anchored) AND bump the
count assertion; (3) Layer 1 from a clean checkout; (4) Layer 2:
--dry-run --object <slug> against real Horizons; (5) --first-build (not
--nightly, per above).

## Fetch facts proven live (2026-07-11 gate)

- Periodic comets pin to a specific 900000XX record (Encke 90000091; Halley
  90000030 pattern). The short-designation trap and full rule live in
  horizons-orbital-mechanics.
- Spacecraft arcs: a coarse glide (fetch_step, ~7d) + daily densify inside
  curated event_windows (flybys) + douglas_peucker thinning of the GLIDE ONLY
  (windows are pinned, exempt). Voyager 1 verified: both windows fully daily,
  zero gaps; 49-year glide 2549 -> 29 points with a genuine 12-year straight
  segment. Refresh is overwrite-by-date on the forward window; the past is
  frozen.

## Field notes

- The moved config had FOUR consumers (builder argparse default, offline-test
  primary path, offline-test comment, TESTING_PROTOCOL prose). Moving the file
  without sweeping the consumers broke Layer 1 at HEAD (L-114/F1). When a
  producer moves, grep every consumer -- then run Layer 1 from a clean clone as
  the proof they all moved.
- interactive.html (gallery repo root) is the EVENTUAL consumer of the served
  data; at the time of writing it does not yet read data/solar-system/ (zero
  references -- verified). Describe the wiring as future work (L-102's open
  question), not as existing.

Origin: created for L-098 (Phase 1b) from Fable 5's 2026-07-12 Mode 7 review;
every code fact verified against gallery HEAD 8e060677 / orrery HEAD e83fe9ce
with Anthropic's Claude Opus 4.8.
