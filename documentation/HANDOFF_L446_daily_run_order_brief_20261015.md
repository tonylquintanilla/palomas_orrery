<!-- Doc-Kind: hand | Brief for the L-446 build: the website's Daily Run pulls the orrery's exports, and copies them into the config, before it builds the cache; a pull that cannot fetch fails by name and nothing writes after it. Takes in L-380 and L-388 (item 2 of L-423). Gallery, with a small orrery patch for the dashboard, the ledger and the skill. -->
# Brief: the Daily Run pulls before it builds (L-446, with L-380 and L-388)

Built on gallery 95713f4912d3e1863390a246d2ba8004bc7cf4c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run again") and orrery b4105c0c7224f5b58984c3ead8b26b1c8653909a at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-14-26_2250_run_record.md"; the code is 802e5bd's).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of that evening.

- Type: BUILD brief. One session, two patches: the gallery's (the
  work) and the orrery's (the dashboard, the ledger, Where We Are, the
  skill). Tony's word on the one decision in section 4.
- Ledger: L-446 (the Daily Run's order), opened 2026-10-15 with Tony's
  "Yes." Read its block first. By Tony's ruling of 2026-10-15 in the
  coordination session, L-380 (the pull after the build; the stamp one
  step behind) and L-388 (a pull that prints success when it could not
  fetch) are the same build: both close at this build's close, and
  item 2 of L-423 (the website's checks) is done by it.
- Order: road stage 8c, and item 2 of stage 9. Independent of L-445
  (Earth's period, orrery); either may go first.

## 0. Before building

- Pull BOTH repositories at HEAD and pin each. If the gallery's HEAD
  has moved past 95713f4, read `daily_run.py` and
  `gallery_maintenance_run.py` again before writing anchors.
- Skills this task fires, confirmed against the manifest at HEAD:
  gallery-cache-builder (1.9; The Daily Run's Steps; a config change is
  not deployed until the cache is rebuilt), safe-file-editing (both
  patches), agentic-pre-test (the gallery maintenance run, offline, on
  a throwaway copy of the gallery; the orrery's on a throwaway copy of
  the orrery), ledger-and-session-records (1.21; the close).
- No skill obligation is pending for these: gallery-cache-builder 1.9
  and ledger-and-session-records 1.21 were both confirmed loaded on
  2026-10-14 and 2026-10-15.

## 1. The ruling (Tony, 2026-10-15; recorded on L-446, not re-asked)

Tony's question, after L-444's first live run: "Wait, shouldn't the
horizons check come before the cache build?" Claude's recommendation,
and Tony's "Yes": the pulls, each with its copy step, run before the
cache builder, so one Daily Run carries checked data straight into the
build. The Horizons check itself already runs in the orrery, before the
export, so everything the website pulls was checked (L-431 build 3).

## 2. What is there at 95713f4 (gallery) and b4105c0 (orrery)

- `daily_run.py`: STEPS is three scripts, run in order with
  `subprocess.call`: `tools/guestbook_updater.py`,
  `tools/gallery_cache_builder.py` (no flags), `gallery_maintenance_run.py`
  (offline). "A step that reports a problem does not stop the next"
  (its docstring and the skill). `--check` lists the steps and fails if
  one is missing. The summary names any step that reported a problem.
- `gallery_maintenance_run.py` GENERATORS, in order: Module atlas;
  Constants export pull (`tools/pull_constants_export.py`); Config
  mirror (`tools/mirror_constants.py --write`); Objects export pull
  (`tools/pull_objects_export.py`); Objects mirror
  (`tools/mirror_objects.py --write`); Drawings pull
  (`tools/pull_drawings.py`). Each mirror runs second because it reads
  what its pull wrote. So today each cache build reads what the
  PREVIOUS run's pull brought: the lag Tony saw on 2026-10-15, when
  "Cache in step" failed for Saturn, Uranus and Neptune because the
  config had the new periods and the cache did not.
- The three pulls, by design (L-322, each docstring's WHEN THE NETWORK
  IS DOWN): when they cannot read the orrery's HEAD or fetch the file,
  they print `N-A: ...`, leave the previous copy, and EXIT 0. The
  maintenance run's generator row then reads as a pass, and the mirror
  writes from the old export. That is L-388's class: a generator whose
  failure prints as success, followed by a writer that trusts it (A
  Check That Cannot Fail Is Not Passing). It has not happened on
  Tony's machine; it was measured in a sandbox at gallery 2df02f3b.
- L-380: the served `frame_constants.orrery_sha` names the export
  pulled BEFORE the build it was built from, one step behind. The
  order fix cures it; nothing else to build for it.
- The orrery's dashboard, `palomas_orrery_dashboard.py`, has a Daily
  Run group: the Daily Run button (`daily_run.py`), Guest Book Updater,
  Cache Builder, Gallery Maintenance Run offline, and the "Daily Run
  Steps" check (`daily_run.py --check`, "fails if any of the three
  scripts ... is missing"). The orrery's "Dashboard parity" checker
  matches every step to its button by name and script (81 steps at
  802e5bd), so a new Daily Run step needs its button and its short
  line, or the orrery's maintenance run goes red.
- The gallery's "Cache in step" checker compares the served cache with
  the config and is the check that catches the lag; "Export freshness"
  (`--live`) compares the served export with the orrery's HEAD.

## 3. What to build

ONE HOME for the pull list. The five pull-and-mirror rows stay where
they are, in `gallery_maintenance_run.py`'s GENERATORS, and the Daily
Run runs THAT list before the builder rather than a second copy of it:

- `gallery_maintenance_run.py` gains a `--pull` mode that runs only the
  pull and mirror generators (Constants export pull, Config mirror,
  Objects export pull, Objects mirror, Drawings pull), prints their
  rows, and exits non-zero if any failed. The offline run keeps those
  rows; on the Daily Run's second pass they print "no change", which
  is the proof the first pass did the work.
- `daily_run.py`: STEPS becomes four: the guest book updater; the pulls
  (`gallery_maintenance_run.py --pull`); the cache builder; the
  maintenance run offline. Its docstring, `--check` and the summary
  follow. Its header comments say why the order is what it is.
- Fail by name (L-388): each pull exits non-zero and prints
  `FAIL: <what it could not fetch, from where, why>` when it cannot
  read HEAD or fetch at it; the `N-A ... exits 0` branch and its
  docstring paragraph go. A mirror row after a failed pull does not
  run: the maintenance run skips it and names the pull that failed as
  the reason, red, never "no change".
- Section 4's decision: what the Daily Run does after a failed pull.
- The orrery's dashboard: the Daily Run group gains the pulls' button
  (name it what the run prints), its short line, and the "Daily Run
  Steps" text says four scripts; Dashboard parity must pass.
- gallery-cache-builder, The Daily Run's Steps: four steps, the order
  and the reason, and the failed-pull rule from section 4. That is a
  bump (1.10) with the protocol entry, under One Session, One Bump.

Options the builder weighed and set aside, for the record: five new
STEPS entries in `daily_run.py` (a second copy of the list, and five
dashboard buttons); a new `tools/pull_all.py` (a second home). Choose
otherwise only for a reason the record states.

Cluster the Tail by Files Touched: before writing the patches, sweep
the open ledger for items whose files are `daily_run.py`,
`gallery_maintenance_run.py`, the three pulls, the two mirrors, the
dashboard's Daily Run group. L-380 and L-388 are the two known; name
any other found, and carry it only if it is small.

## 4. The one decision, for Tony at the session's start

When a pull cannot fetch (no network, GitHub down), what does the
Daily Run do next?

- A (recommended, default if Tony is away): the Daily Run STOPS before
  the builder, names the pull that failed, and the summary says so.
  Nothing is built on yesterday's export; Tony runs it again later. The
  builder needs Horizons over the same network anyway, so a day with no
  network builds nothing in either case.
- B: the Daily Run carries on and builds on the previous pull, with the
  failed pull named in red in the summary. Faster when GitHub alone is
  down; the cache then carries a stamp one step behind, which is L-380
  again for that day.

This changes the Daily Run's standing rule that a step's problem does
not stop the next, for the pull step only; the guest book's problems
still do not stop the build. Tony's word goes on L-446 and into the
skill.

## 5. Planted faults, each shown caught, by name

- A pull with the network off (point it at an unreachable host or a
  repository name that does not exist, in a test copy): it must print
  FAIL by name and exit non-zero, and the mirror after it must not
  write. Show `data/objects_config.json` byte-identical before and
  after. This is L-388's Gap, "show it failing with the network off
  before trusting it", and it is the test that matters most.
- The Daily Run with the pull step failing: under A it must stop before
  the builder; under B it must name the failure in the summary.
- `daily_run.py --check` with one of the four scripts renamed away.
- The pulls' second pass in the same Daily Run: every pull row prints
  "no change" and the config is unchanged, proving the first pass did
  the work and the second is a no-op.
- The orrery's Dashboard parity with a step and no button.

The gallery maintenance run, offline, on a throwaway copy, before the
patch is delivered (agentic-pre-test): 27 of 27 at 95713f4, so 27 of 27
after, plus whatever new row the builder adds for the `--pull` mode.

## 6. The proof on Tony's machine

- Run the gallery patch; run the Daily Run ONCE. The pull step runs
  first; the builder builds from what it pulled; the maintenance run's
  pull rows print "no change"; Cache in step passes in the same run.
- If L-445 (Earth's period) has already been pushed by then, this one
  Daily Run also carries Earth's new period words to the website: the
  two-run lag L-445's brief describes becomes one run. Say which case
  it was in the build record.
- Commit; push; `gallery_maintenance_run.py --live`: Export freshness
  names today's orrery HEAD.

## 7. Close

- L-446 to DONE after Tony's run, his verdicts quoted from his run
  record; L-380 and L-388 to DONE, each saying it closed in L-446's
  build; L-423's item 2 marked done, with the date.
- A Closing Item Re-homes Its Loose Ends: read L-380's and L-388's
  bodies for anything the order fix and the fail-by-name do not cover,
  and re-home or strike each by handle.
- Where We Are: stage 8c done; stage 9 (the website's checks) notes
  item 2 done and names the next item still open on L-423's list
  (item 1, L-262, the framing test, if its close is not yet recorded);
  the box; the
  signals re-read; the marks reset; the run-record zone read first and
  emptied after.
- gallery-cache-builder 1.10, the protocol entry, the manifest; the
  reinstall is Tony's and the obligation travels to the next session.
- The build record, `documentation/HANDOFF_L446_daily_run_order_build_<date>.md`,
  in the ORRERY's documentation/; the spent gallery patch in the
  gallery's documentation/, the orrery patch in the orrery's.

## 8. Tony's actions, all of them

- (do) Start the build session from this brief.
- (decide) Section 4, A or B; default A.
- (do) Run the gallery patch; run the Daily Run once; commit; push;
  `gallery_maintenance_run.py --live`.
- (do) Run the orrery patch; run `orrery_maintenance_run.py`
  (Dashboard parity, the ledger index, the skill manifest); commit;
  push.
- (do) Reinstall gallery-cache-builder (1.10) in Settings > Skills;
  save PROJECT_INSTRUCTIONS.md as its versioned copy and copy it into
  the Project instructions.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
