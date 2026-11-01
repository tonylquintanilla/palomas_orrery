---
name: gallery-cache-builder
description: Nightly data-serving pipeline for the Paloma's Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written; and for daily_run.py's order, a failed pull and the run records check. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma's Orrery.
fires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers, the Daily
  Run's order and a failed pull, the run records and their check, a spacecraft fetched by its path plan, a pull that does not match the push, a comet on an open path fetched by its plan (is_path_body, open_path), a small body's own uncertainty (position_uncertainty, the match rule), every JPL question asked fresh (HORIZONS_CACHE), a drawing named on a room's row
---

# Gallery Cache Builder (Phase 1b data serving)

Read this file in 4 parts: lines 1-249, 250-530, 531-783, 784-907.

Skill version: 1.16 | 2026-11-01, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 6a434ed8 and gallery @ b6574a0f. v1.16 (L-484, with
L-485) adds A Served Number That Changes on Purpose, the lesson of the
website's red nights of 2026-11-01: a number the orrery's export
changes on purpose is looked for in the website's CHECKS before the
push -- its acceptance lines and its hover fixture consume the export
as much as its renderers do -- and the brief for such a change names
the pins that move. And under The Daily Run's Steps, the night form:
GitHub's schedule is best-effort, so the morning pulls first and does
not wait for the run (Tony's ruling of 2026-11-01, 12:04 Chicago); the
orrery's night gains a second scheduled line at 11:17 UTC, the
website's waits for its next gallery session. Each fact was read from
the code at 6a434ed8 and b6574a0f before it was written.
Earlier: 1.15 | 2026-10-31, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ f4994ffc and gallery @ c1c578f5. v1.15 (L-485, with
L-461 and L-443) records that the builder runs unattended: every night
at 08:17 UTC on GitHub's computer, through `daily_run.py --night`, whose
gate carries the deletions-only guard this skill called designed and
not built. Operating mode, the routines that said "by hand", Layer 3,
the Validation stance and The Daily Run's Steps say so; a pull that
does not match the push has a second honest cause, not yet pulled.
Riding the bump, from L-443's and L-501's closes: a comet is drawn from
its elements of today; a new body the room draws from its elements
onboards on a Daily Run; a config change turns the Solar System figures
check red too; the orrery's orbit cache is written in text mode. And
from this session: the orrery's export marks a held body (L-485, the
hold), which the builder does not honour yet. Each fact was read from
the code at f4994ffc and c1c578f5 before it was written.
Earlier: 1.14 | 2026-10-29, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 571b9bf4 and gallery @ b55109f2. v1.14 (L-399, L-503)
records the builder's changes of 2026-10-29: each small body is served
`position_uncertainty`, JPL's own 3-sigma from the 2xr table, by a match
rule held to the body's own 3-sigma, floored at 1e-7 AU and capped at
1e-3 AU by the closest comet pieces, a refusal naming its numbers;
every JPL question is asked fresh (`HORIZONS_CACHE`) and why; and
`serve_drawings` serves a drawing named on a room's own row. Each fact
was read from the builder at b55109f2 before it was written.
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 (L-418), 2026-10-14 (L-431), 2026-10-15 (L-446),
2026-10-17 (L-449), 2026-10-25 (L-443), 2026-10-26 (L-443),
2026-10-29 (L-399), 2026-10-31 (L-485) and 2026-11-01 (L-484).

The standalone builder that fetches fresh JPL Horizons data and deploys the
web gallery's served cache. It runs unattended every night on GitHub's
computer, through `daily_run.py --night`, whose gate decides whether the
night's files are committed; Tony can also run it by hand for a build the
same day (see Operating mode below).

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- Operating mode -- unattended every night, since October 31 2026
- What it is
- Swap blast radius [QUALITY]
- Sibling directory semantics [QUALITY]
- Recovery ordering (why L-114 mattered twice)
- The swap retries, rolls back, and leaves a record [QUALITY]
- Recovery by hand, when the roll-back also fails [QUALITY]
- The cause, and what is still open
- Never shutil.rmtree anything in this tree [QUALITY]
- The sibling report names what the builder did not make [QUALITY]
- A config change is not deployed until the cache is rebuilt [CRITICAL]
- The Builder Reads the Period's Centre [QUALITY]
- A Spacecraft Is Fetched by Its Plan [QUALITY]
- A Small Body's Own Uncertainty Is Served [QUALITY]
- Every Question Is Asked of JPL, Fresh [QUALITY]
- The Daily Run's Steps [QUALITY]
- A Served Number That Changes on Purpose [QUALITY]
- Validation stance
- Commit with round-trip verify
- The three-layer gate (documentation/TESTING_PROTOCOL.md, orrery repo)
- Adding a new object -- the full sequence, and where it silently breaks
- Fetch facts proven live (2026-07-11 gate)
- Field notes

## Operating mode -- unattended every night, since October 31 2026

THE NIGHT (L-485; Tony's rulings R1 to R5 of 2026-10-25,
documentation/DESIGN_L485_nightly_run_rulings_20261025.md). The
gallery's `.github/workflows/nightly.yml` runs `python daily_run.py
--night` on GitHub's computer at 08:17 UTC (`cron: '17 8 * * *'`), an
hour after the orrery's own night at 07:17, and can be fired by hand
from the Actions tab. The first run, by hand, was clean on 2026-10-31
(commit c1c578f5, by github-actions[bot]). What makes it safe is the
night's GATE, not a person at the keyboard: the workflow commits only
when `daily_run.py --night` exits 0, and stages only its allow-list
(`daily_run.py --allow-list`). The gate's conditions are in The Daily
Run's Steps, below; one of them is the guard this section used to call
designed and not built.

- THE DELETIONS-ONLY GUARD IS BUILT, in the gate: a change under
  `data/solar-system/` that is deletions only stops the night, by name.
  That is the August 10 failure -- a half-swapped cache committed by
  someone who did not know a build was running -- refused by the
  machine. (Until 2026-10-31 this was a `pre-commit` hook "deliberately
  NOT built", relevant "if the builder ever runs unattended in any
  other form". It now does.)
- The builder runs with no flags, never `--commit`: it swaps the new
  cache in and stops, and the workflow's own commit step commits after
  the gate.
- A red night commits nothing; the run's log on the Actions tab is its
  only record, and the previous served cache stays live.
- `concurrency: group: nightly-run`, without cancel-in-progress: a run
  fired by hand waits for a running night rather than overlapping it,
  and checks out `main` as it stands when it starts.

BY HAND, for a build the same day. The builder is launched from the
dashboard's Developer Tools group, or by running
`tools/gallery_cache_builder.py` from the GALLERY REPO ROOT. The root
matters: `--config` and `--output-dir` default to paths relative to the
working directory, so launching from `tools/` fails at load_config. No
flags runs nightly mode, and Tony commits in GitHub Desktop. Tony's
morning order since the night exists: Pull origin on both repositories
first, then anything else, without waiting for a night that has not
run yet (The Daily Run's Steps, the night form, says why).

The history, kept because it explains the gate. The Windows scheduled
task was disabled on 2026-08-10 (Tony: "It can't run without my machine
being on anyway and it's consistent with me being the only commit
authority"), after a scheduled run's failed swap was committed on
2026-07-24 by someone who did not know a build was running. The night on
GitHub's computer answers both reasons: it needs no machine of Tony's,
and its gate refuses exactly that commit.

How old the served data is: the night's record,
`data/nightly_run_record.json`, carries its last clean run, and the
orrery's dashboard prints it, red when more than a day old. L-189's
staleness check is the older answer to the same question. A GALLERY-repo tool; this skill is authored in
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

  1. RETIRED 2026-10-10: no OneDrive pause. Tony: "the retry is
     sufficient." The builder retries a refused rename and the swap log
     records it; the Daily Run no longer asks (L-216).
  2. Run the builder by hand -- see Operating mode.
  3. Watch GitHub Desktop's change list; do not commit if it looks wrong.
  4. Afterwards, read the last line of `data/cache_swap_log.jsonl`.

Step 4 is new with this version and it is the point of the whole build:
it is the one step that does not depend on anyone noticing anything.
AT NIGHT THE GATE DOES STEPS 3 AND 4 (v1.15, L-485): it reads the swap
log's last line back off the disk and requires tonight's run with
outcome ok, and it refuses a change under `data/solar-system/` that is
deletions only, before anything is committed.

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
the rule. Do not use `--commit` while L-216 is open. The night never
passes it: its workflow commits after the gate, and a night whose swap
was not ok, or whose served change is deletions only, commits nothing,
so the third condition holds at night by the gate instead of by Tony.

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
second run reached its swap. That is why step 1 of the routine above said
to note the time, until the pause was retired on 2026-10-10.

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
  2. Run this builder, by hand -- see Operating mode. (The night runs
     it too, but on GitHub's copy, so a change not yet pushed is not in
     it.)
  3. Run `python gallery_maintenance_run.py`.
  4. Commit the CONFIG AND THE CACHE TOGETHER, and push.

`tools/check_cache_in_step.py` gates step 3 and compares the served
cache against the config it was built from. A red "Cache in step" right
after a config change is CORRECT and means step 2 has not happened yet.
So is a red Solar System figures check (v1.15, from L-501's close), for
a body the config names and the cache does not hold yet.

THE ONE EXCEPTION, and it is worth knowing because it is the only part
of a room's data the page reads directly: the `arrival` block --
`drawn` and `moon` -- is fetched from `data/objects_config.json` by
`gallery/arrival.js`, not from the cache. A change to what a room OPENS
on needs only the push. Everything else needs the builder.

Three more fields are read from the config by the rooms' drivers, not
from the cache, so they too reach a visitor on the push alone: a body's
`position_accuracy` (L-398), its `description` and `info_url` (L-395),
and its `period` (L-431 build 3), which `tools/mirror_objects.py` copies
from the orrery's export. The orbit drawn around a period's centre is
NOT one of them: it is the cache's `drawn_orbit`, and needs the builder.
Nor is a small body's own uncertainty, the cache's
`position_uncertainty` (A Small Body's Own Uncertainty Is Served).

A STORED DRAWING NAMED ON A ROOM'S ROW IS SERVED TOO (v1.14, L-503).
`serve_drawings()` copies the drawings named under the served objects'
features and, since 2026-10-29, those named on the rows of the config's
`"rooms"` section, which the served index does not hold
(`serve_drawings(staging, index, drawings_dir, rooms=...)`). The main
belt's cloud, the Solar System room's own row, is the first.
`tools/pull_drawings.py` reads the rooms section the same way, so the
orrery's file is pulled before the build serves it.

## The Builder Reads the Period's Centre [QUALITY]

Built 2026-10-14 (L-431 build 3), at the rule horizons-orbital-mechanics
calls The Drawn Orbit Follows the Period's Centre.

- Each object in `data/objects_config.json` carries a `period` block,
  copied by `tools/mirror_objects.py` from the orrery's export, never by
  hand. `kind` is `fetched`, `typed` or `none`; a fetched one names its
  `center`, the Horizons centre JPL's period was taken around.
- The served `osculating` block, its positions and its trust stay
  Sun-centred and unchanged. Where a fetched period's centre is the
  solar system's barycentre ('@0') and the body is drawn from its
  elements around the Sun (not a comet, not a spacecraft), the builder
  ALSO fetches the body's elements around that centre at the SAME date
  as the Sun-centred ones, and serves them as `drawn_orbit` (centre
  slug `ssb`, `paired_with: osculating`). The room pairs the two sets
  at that date to find where the barycentre sits seen from the Sun, and
  draws the ellipse there (`render_orbits.drawn_orbit_offset`). No
  perturbation lines are drawn for it (Tony, 2026-10-13).
- A set from another date is never paired: `build_drawn_orbit_block`
  raises, and the pre-swap check #D aborts a `drawn_orbit` that is
  around the stored centre, is not at the `osculating` date, or has no
  mean motion. `tools/check_cache_in_step.py` asks the same question
  from the other side, with the same rule (`drawn_centre_wanted`):
  every object whose period wants a drawn orbit has one, and no other
  object does.
- A comet whose period is around another centre is drawn from its
  elements of today, around the Sun (since 2026-10-22, L-443: every
  comet is anchored at today; until then "at perihelion"), and the
  builder WARNS rather than fetching. Encke, today, is around the Sun.
- Which bodies this touches is decided by the orrery's period records,
  not here. On 2026-10-14 no served body's period was around the
  barycentre (Sedna is not served), so the first live `drawn_orbit` may
  come from a planet whose period the orrery fetches around '@0' when
  Tony plots it.

## A Spacecraft Is Fetched by Its Plan [QUALITY]

Built 2026-10-25 (L-443 build B), on the method horizons-orbital-mechanics
calls How a Path's Events Are Found. Design: ruling 1 of
`documentation/DESIGN_L443_slice2_rulings_20261023.md`, "One path rule,
the orrery's."

- THE PLAN IS THE ORRERY'S. `path_plan.py` makes each served
  spacecraft's plan in the orrery's maintenance run; the objects export
  carries it; `tools/mirror_objects.py` copies onto the entry in
  `data/objects_config.json` what the builder and the room need: its
  `made` date, its `span` (JPL's own, launch to the end of JPL's data),
  its `backbone` (step and thinning), and each event's body, kind,
  moment, distance, window and step. Never by hand.
- THE WHOLE PATH, WHEN THE PLAN IS NEW (`fetch_path_by_plan`): the
  backbone across the span at its step (7 days), thinned by
  Douglas-Peucker at its tolerance (0.02 AU); each event's window at the
  event's own step, clipped to the span, thinned at the event's own
  scale (`WINDOW_THIN_FRACTION`, 1% of its passing distance) and merged
  after the backbone's thinning so a flyby is never thinned away; then
  the daily tail. JPL's predicted part is fetched with the rest; nothing
  is extended past the span. "New" means the raw archive's `plan_made`
  or `plan_span` differs from the entry's, or a first build, or
  --refresh-spacecraft; the archive is cleared first, since JPL revises
  the predicted part.
- OTHERWISE, ONLY THE TAIL (`fetch_path_tail`): daily from the freeze
  window before today to two days after (`PATH_TAIL_AHEAD_DAYS`), inside
  the span, so the room, drawing the minute it is opened, finds a point
  either side of it until the next build.
- EVERY POINT IS KEYED TO THE MINUTE (`MINUTE_KEY`), since a window's
  step can be a minute; every other object keeps day keys.
- AS_OF_TODAY IS TODAY'S POINT, the latest at or before today, not the
  path's last (which may be in 2100); none when no point lies within two
  days before today, so a path whose data ended serves no "you are here"
  and passes #T.
- THE SHRINK GATE HOLDS A RE-FETCH BY A NEW PLAN OUT OF ITS COUNT, and
  names it, old count and new: its count is its plan's, not the old one.
  The suite shows the gate refusing the same re-fetch without the
  exemption.
- THE SPACECRAFT SANITY BOUND IS 1,000 AU (`SPACECRAFT_SANITY_AU`); the
  Voyagers' JPL data runs to 2100, past 400 AU.
- NO PLAN AND NO TYPED START: the object fails by name ("no path plan
  is served for this spacecraft yet") and is served last-good, never
  asked from 1970. A spacecraft with a typed `overrides.spacecraft`
  start and no plan keeps the old fetch; none does since 2026-10-25,
  Voyager 1's typed windows having been replaced by its plan's events.
- THE OFFLINE SUITE gives a spacecraft with no plan a stand-in plan, as
  it gives stand-in drawings, so it does not depend on a pull: in the
  config as committed, a plan arrives only when the mirror copies it.
- SIZE: the first simulated build of 2026-10-25, on fake straight paths,
  served 68 KB of positions for the twelve; before the windows were
  thinned at their own scale it was about 1.7 MB. The real paths curve,
  so the first real build measures it.
- A COMET ON AN OPEN PATH IS A PATH BODY (v1.13, L-443, slice 2, build
  B part 2). `is_path_body` is one test, a spacecraft or an entry with
  `open_path`, and every place above that asked "is this a spacecraft?"
  asks it: the fetch by the plan, last-good serving, structural check
  #2, the trust branch (`fetched_positions`, no window) and the floor on
  points. Such a comet is served positions and no `osculating` block,
  with `open_path: true` on its served entry, which the room reads to
  draw it as a path. Its plan comes from the orrery like a
  spacecraft's (horizons-orbital-mechanics, A Comet on an Open Path);
  its span is a year before its perihelion to a year after today, so
  "nothing extended past the span" means past that. With no plan yet it
  fails by name, "no path plan is served for this comet yet". The
  mirror copies `open_path` from the export (`INSERTED`). The offline
  suite gives such a comet a stand-in plan and the fake answers it with
  a straight line past the Sun; four checks hold it, among them one
  fetched inside its plan's span and no further.

## A Small Body's Own Uncertainty Is Served [QUALITY]

Built 2026-10-29 (L-399), on the method horizons-orbital-mechanics calls
A Small Body's Uncertainty Comes With Its Position.

- EACH SMALL BODY IS ASKED JPL'S OWN UNCERTAINTY: an asteroid, a comet
  or a dwarf planet asked as a small body (`is_small_body_target`, the
  orrery's own test), by Horizons' vector table 2xr, read by column
  name, at the moment of its served "you are here" point. What is
  served is `position_uncertainty` on its entry
  (`build_position_uncertainty`): the 3-sigma of its distance from the
  Sun. The planets and Pluto keep JPL's planetary report, from the
  config (`position_accuracy`). It is cache data, so unlike
  `position_accuracy` it reaches a visitor only after a build.
- AN ANSWER THAT CANNOT BE SERVED HONESTLY SERVES NOTHING, NAMED, and
  never costs the orbit: no point to ask at, a body not measured from
  the Sun, an empty position column, no R_s ("JPL gives no range
  uncertainty (R_s) for it" -- Bennu, Halley and Ikeya-Seki, whose
  column reads "n.a."), or a position that does not match. The index's
  `position_uncertainty` lists who was asked and why each missing one
  is missing.
- THE MATCH RULE (`uncertainty_match_tolerance`, corrected
  2026-10-29). The 2xr answer's position must sit within the body's own
  3-sigma of the served point, 3 x R_s, R_s read first, floored at
  1e-7 AU (`UNCERTAINTY_MATCH_AU`, about 15 km, the earlier fixed
  tolerance, which Ceres and Apophis keep) and capped at 1e-3 AU
  (`UNCERTAINTY_MATCH_CAP_AU`, about 150,000 km). THE CAP IS SET BY
  THE CLOSEST COMET PIECES, the one case where another record sits
  close: C/2025 K1's pieces B and D were 0.0042 AU apart on 2026-10-29
  and D's own 3-sigma was 0.0043 AU, so D's answer standing in for B's
  would pass the 3-sigma alone; the cap is under half the closest pair
  measured that day, the parent and C at 0.0024 AU. Every other body
  asked had no neighbour nearer than 0.117 AU.
- A REFUSAL NAMES ITS NUMBERS. The line says how far JPL's 2xr answer
  sits from the served point against the tolerance, and the run
  record keeps the refused answer's items under
  `position_uncertainty.refused` -- the id asked, JPL's X, Y, Z, the
  served point -- so a refusal can be read later.
- WHY IT WAS CORRECTED: the fixed 1e-7 AU refused 2026 ED138 at the
  21:57 UTC build of 2026-10-29, its answer 8.88e-05 AU (13,000 km)
  from a served point read from astroquery's saved answers after JPL
  had revised the orbit -- a thirtieth of its own 3-sigma (next).

## Every Question Is Asked of JPL, Fresh [QUALITY]

`HORIZONS_CACHE = False` (L-399, 2026-10-29), passed as `cache=` at
every astroquery call the builder makes. astroquery keeps each answer
on disk for a week (`astroquery.cache_conf.cache_timeout`, 604800 s,
in `~/.astropy/cache/astroquery/Horizons`) and hands it back when the
same question is asked again, so a second build on the same day served
the first build's orbit and positions under a new "retrieved" stamp.
The 2xr question, sent directly, was always fresh, which is how the
two came to disagree. The offline suite holds every call to the
setting. The orrery made the same choice the same night (L-504,
`utc_clock.HORIZONS_CACHE`; horizons-orbital-mechanics).

## The Daily Run's Steps [QUALITY]

`daily_run.py`, Tony's design of 2026-09-27 (L-281), is FOUR steps
since 2026-10-15 (L-446), and the order is the point:

  1. The guest book updater. First, because it needs Tony's answers,
     and what he approves is saved at once.
  2. The pulls from the orrery: `gallery_maintenance_run.py --pull`,
     which runs only the five pull-and-mirror rows of its GENERATORS
     (constants export, config mirror, objects export, objects mirror,
     drawings). BEFORE the builder, so the build reads what the orrery
     exported today and the served `frame_constants.orrery_sha` names
     that export. Until 2026-10-15 the pulls ran only in step 4, after
     the build, so every build read the previous run's pull and its
     stamp was one step behind (L-380).
  3. This builder, with no flags.
  4. The gallery maintenance run, offline. Its pull rows run again and
     print "no change", which is the proof step 2 did the work.

The pull list has ONE home, the maintenance run's GENERATORS; `--pull`
reads it through `PULL_ROWS`. Do not add the pulls to `daily_run.py`'s
STEPS as rows of their own: that is a second copy of the list, and five
more dashboard buttons for Dashboard Parity to hold.

A PULL THAT CANNOT FETCH FAILS, AND THE DAILY RUN STOPS (Tony's option
A, 2026-10-15). Each pull prints one line starting `FAIL:` naming what
it could not fetch, from which address and why, writes nothing, and
exits 1 (L-388; until 2026-10-15 it printed N-A and exited 0, the
maintenance run read that as PASS "no change", and the mirror wrote the
config from the old export). The maintenance run does not run a mirror
whose pull failed (`FED_BY`): its row is red and names the pull. A
failed generator fails the whole run and is named in the summary. And
`daily_run.py` stops after step 2: the builder and the checks do not
run, and the summary quotes `--pull`'s "=== PULLS:" line. Nothing is
built on yesterday's export; Tony runs it again later. The builder
needs the network for Horizons anyway, so a day with no network builds
nothing either way. Option B -- build on the previous pull and say so
in red -- was declined. `tools/test_pull_failures.py` ("Pull failures",
gating) runs each pull with its network replaced by one that fails,
three ways, so these branches are tested every day and not only on the
day the network is down.

A PULL THAT DOES NOT MATCH THE PUSH IS A FAILED PULL (L-461; Tony,
2026-10-25: "stop. confirmed."). After the pulls, `daily_run.py`
compares each pull's recorded orrery commit (`data/constants_export.sha`,
`data/objects_export.sha`, `data/drawings/pulled_at.sha`) with the newest
commit in Tony's orrery folder, the folder `palomas_orrery_for_github`
beside the website's, read from its `.git` folder (HEAD, then the
branch's loose ref or packed-refs), so no git command is needed. When
they differ, the run STOPS before the builder, naming both commits and
the two likely causes -- the orrery's work is not pushed, or GitHub has
not finished serving a push -- and says to push, or wait a minute if the
push just went, then run the Daily Run again. SINCE THE ORRERY'S NIGHT
COMMITS (L-461's second honest cause, v1.15): Tony's orrery folder is
behind GitHub every morning the orrery's night committed, until he
clicks Pull origin, so the pulls (GitHub's copy) and his folder differ
for that reason too -- not yet pulled. The cure is Pull origin, orrery
then website, then the Daily Run again. No retry, no wait: the one
time it happened (2026-10-21) the cause was an unpushed orrery, which
waiting cannot fix, and a run that waits hides the common cause behind
the rare one. A folder or commit it cannot read stops it too, saying
where it looked. `python daily_run.py --check` runs the comparison on
five made-up cases and two planted faults (one that always matches, one
that ignores the drawings' pull).

THE RUN RECORDS ARE KEPT, AND CHECKED AFTER THE BUILDER (L-449). Each
build writes one record to `raw/runs/`, and the builder copies the old
ones forward. Records went missing after builds on 2026-10-15 and
2026-10-16, cause unknown, and were put back from `.prev` on Tony's
word. Tony's rulings: keep EVERY record until the cause is found, then
a deliberate limit, its number set at that time, with the builder naming
each record it removes (2026-10-16); and on a loss, stop and name
(2026-10-17). So:

- The builder prints two `[RUNS]` lines at its copy-forward: how many
  records `raw/runs` held before the copy and how many the staging
  copy holds after it, with both paths. It removes no record. These
  two lines are what the next loss is read from; record them in L-449.
- `daily_run.py` compares `data/solar-system/raw/runs/` with the
  replaced cache's `data/solar-system.prev/raw/runs/` between the
  builder and the maintenance run. On success it prints what it
  compared ("carried 85 of 85, plus tonight's"). A record in the old
  and not the new STOPS the Daily Run before the maintenance run,
  naming each lost record with its copy's path; Tony copies them back
  in File Explorer, then runs the maintenance run. The copies stay in
  `.prev` only until the next build clears it. A missing folder is
  "could not compare", reported as a problem, never as a pass; it does
  not stop the run, since it is what a failed or rolled-back build
  leaves.
- It is not a step of its own and has no dashboard button: it runs no
  script, and it means something only straight after a build. The
  builder's offline suite runs the comparison on its own builds and
  plants a loss, which must stop it by name.

THE NIGHT FORM (v1.15, L-485; `python daily_run.py --night`, run by the
gallery's workflow at 08:17 UTC). The same steps with no keyboard,
ending in one gate:

- The guest book is SKIPPED, by name: it needs Tony's answers and stays
  his morning's (Tony's ruling of 2026-10-31, 10:20). Nothing is read
  from Google on the runner.
- The pulls run as by day, asking GitHub's interface with the run's own
  token.
- PULL MATCHES PUSH, THE RUNNER FORM (`pull_matches_remote`): there is
  no orrery folder beside the website on GitHub's computer, so the three
  pulled commits must agree with each other and with the orrery's
  GitHub copy, read live with `git ls-remote`. A difference stops the
  night before the builder: no retry, no wait.
- The builder with no flags, never `--commit`; its swap read back off
  the swap log as tonight's, outcome ok. The run records check: a loss,
  or "could not compare", is red at night.
- The maintenance run's night pass (`gallery_maintenance_run.py
  --night`), an UNREACHABLE row red.
- THE GATE (`night_gate`), exit 0 only when ALL hold, each failure named
  on the last line, "NIGHT RUN: RED -- ...": the pulls passed and match
  the orrery's GitHub copy, and did not move after the build; the
  builder exited 0 and tonight's swap is ok; the run records were
  carried; the night pass passed with nothing UNREACHABLE; git sees
  nothing changed or new outside the allow-list (`night_allow_list`);
  every changed file is ASCII; and the change under
  `data/solar-system/` is not deletions only.
- A clean night writes `data/nightly_run_record.json`; a red night
  writes nothing, and its record is the run's log. `python daily_run.py
  --check` judges made-up nights and planted faults for the gate and
  the runner form.
- THE MORNING DOES NOT WAIT FOR THE NIGHT (v1.16, L-485; Tony's ruling
  of 2026-11-01, 12:04 Chicago): Tony pulls first and does not wait for
  the run, and a run that lands later in the day comes with his next
  Pull origin -- because GitHub's schedule is best-effort. Its page
  "Events that trigger workflows", read 2026-11-01: "The schedule event
  can be delayed during periods of high loads of GitHub Actions
  workflow runs" and "If the load is sufficiently high enough, some
  queued jobs may be dropped." On 2026-11-01 the website's 08:17 run
  started at 15:15 UTC, 6 h 58 min late, and the orrery's 07:17 run at
  14:17, 7 h 0 min late (6 h 22 min on 2026-10-31). A dropped night is
  caught the same day by a second scheduled line: the orrery's at 11:17
  UTC since 2026-11-01 (its `.github/workflows/nightly.yml`); the
  website's at 12:17 comes with its next gallery session, and until
  then its workflow carries the 08:17 line alone. A second firing is
  harmless: the concurrency group queues it, and a clean second run
  commits only its night record. The times stay (no reschedule): the
  lag is GitHub's, not the clock's.

Apart from the pulls and the records, a step that reports a problem
does not stop the next: the guest book's problems still do not stop the
build. Nothing in
the Daily Run commits or pushes. The Horizons
check was its step 2 from 2026-10-10 to 2026-10-14 and moved into the
orrery's maintenance run beside the objects export (L-395; Tony,
2026-10-12: "the orrery stores and serves the data not the other way
around"). The gallery's "Horizons confirmations" row still reads the
dates JPL confirmed each object, from the pulled export, offline, and
goes red, naming the objects, on the day a confirmation turns 30 days
old: the cure is the orrery's maintenance run, then the push, then the
pull here. `python daily_run.py --check` lists the steps and fails if a
script is missing; the maintenance run runs it.

## A Served Number That Changes on Purpose [QUALITY]

Learned 2026-11-01 (v1.16, L-484, with L-485). The orrery's export
changed one served number on purpose -- Earth's inner Van Allen belt,
9,600 km to 10,000 km, by the export's rounding fix of 2026-10-31 --
and the website's night refused every cache built on it until a
gallery session moved two pins: the website's run 2 (by hand, 14:24
UTC) and run 3 (scheduled, 15:15 UTC) were red, "1 of 36 gating
checkers FAILED: Display figures", and committed nothing, as designed.
The renderers were right. Two of the website's CHECKS still held the
old number.

- THE WEBSITE'S CHECKS CONSUME THE EXPORT TOO. The gallery's "Display
  figures" row, `documentation/smoke_display_figures.js` in the
  gallery repo, pins what the export serves two ways: ACCEPTANCE_LINES,
  the approved wording of each listed hover, and the hover fixture
  every built hover is compared with (`FIXTURE`, a
  `fixture_hovers_<handle>_on_<sha>.json` beside it, re-recorded when
  hovers change on purpose). A served number that moves moves the
  hover, and both pins fail, by name.
- SO BEFORE THE PUSH, GREP THE OTHER REPOSITORY'S CHECKS for the number
  that moves, in the form a visitor reads it ("9,600"), and not only
  its renderers. The orrery session of 2026-10-31 and the coordinating
  session that wrote its brief read the renderers alone.
- THE BRIEF FOR SUCH A CHANGE NAMES THE PINS THAT MOVE, by file, or
  says that none does and how that was found. The gallery session then
  moves each pin in the build that pulls the new export, re-records the
  fixture, and proves the old figure fails by name (2026-11-01:
  `fixture_hovers_L484_on_c1c578f5.json`, "9,600" planted and failing).
- A CHANGE MEANT TO MOVE NOTHING SERVED is proved the other way round:
  save `data/objects_export.json` (or `data/constants_export.json`)
  before the change, diff it after, and name every field that moved.

The check refusing was the gate working; the lesson is that the session
making the change can know ahead. provenance-discipline binds at the
export and asks whether a served number is TRUE (The Gate Binds at
EXPORT); this section is about the other repository still expecting
the old one, which is why it lives here, beside the Daily Run that
pulls the export.

## Validation stance

Two dispositions, and the difference is load-bearing:
- ABORT (raise ValidationAbort -> nonzero exit; the nonzero exit surfaces in
  the console Tony is watching when he starts the run by hand, and at
  night in the run's log on the gallery's Actions tab, where the gate
  reads the builder's exit and turns the night red, so nothing is
  committed -- through 2026-08-10 this read "Task Scheduler history is
  the monitoring channel"): structural invariants (#2/#3/#C/#8), #B3
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
- Layer 3 -- scheduling (unattended nightly). LIVE AGAIN since
  2026-10-31, in the GitHub Action form (L-485): the gallery's
  workflow at 08:17 UTC. Its gate is the night's (`daily_run.py
  --night`, The Daily Run's Steps); its health summary is the night's
  record, `data/nightly_run_record.json`, which the orrery's dashboard
  reads. The Windows task retired on 2026-08-10 stays disabled. The
  gap-aware catch-up L-098 / L-111 named is not built.

## Adding a new object -- the full sequence, and where it silently breaks

Beyond the three-layer gate above, onboarding a genuinely NEW object needs
two things the general gate description doesn't spell out:

- **--first-build fetches the full 365-day backfill for a new
  non-spacecraft object; nightly mode only [today - freeze, today].**
  first-build also carries the N3 floor check (rejects a
  clipped/truncated fetch), which nightly skips. Whether that matters
  depends on how the room draws the body (v1.15, from L-443's close):
  one drawn from its ELEMENTS, as every orbit in the Solar System room
  is, needs only today's point, so a Daily Run (or the night) onboards
  it -- slice 1's 50 bodies and 2026 ED138 went in that way. A body
  whose drawing needs the past positions themselves needs --first-build.
  Spacecraft and comets on an open path are the other exception: they
  are fetched by their plan, whole when the plan is new.
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
- The orrery's `osculating_cache_manager.save_cache` writes
  `data/osculating_cache.json` in text mode with no `newline=''`, so on
  Windows every save turns it CRLF; git stores it LF (`* text=auto
  eol=lf`), and on GitHub's Linux computer it is LF anyway (v1.15, from
  L-485). A difference that is only line endings is not a change.
- A BODY THE ORRERY HOLDS IS NOT YET HONOURED HERE (v1.15, L-485, the
  hold). Since 2026-10-31 the orrery's Horizons check holds a body whose
  identity JPL no longer gives as the list does, and its objects export
  (schema 4) carries a `hold` block in that body's confirmation: since
  when, why, what the list says and what JPL said. This builder does
  not read it: `tools/mirror_objects.py` copies only its REPLACED and
  INSERTED fields and drops the rest unnamed, the builder asks JPL by
  the mirrored `horizons_id`, its last-good path re-stamps
  `source.retrieved`, and the website's own confirmations check goes
  red at day 30. So a held body is still fetched and served, and the
  website's night goes red at day 30, as before the hold. Nothing is
  held today. The website's half -- the mirror carries the mark, the
  builder serves last-good named with its own data's date, the hover
  prints the held date, the website's check passes held as held -- is a
  gallery session after the ruler build, recorded on L-485.
- interactive.html (gallery repo root) is the EVENTUAL consumer of the served
  data; at the time of writing it does not yet read data/solar-system/ (zero
  references -- verified). Describe the wiring as future work (L-102's open
  question), not as existing.

Origin: created for L-098 (Phase 1b) from Fable 5's 2026-07-12 Mode 7 review;
every code fact verified against gallery HEAD 8e060677 / orrery HEAD e83fe9ce
with Anthropic's Claude Opus 4.8.
