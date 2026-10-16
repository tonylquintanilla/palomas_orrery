<!-- Doc-Kind: hand | Build record for L-446: the website's Daily Run pulls the orrery's exports before it builds the cache, and stops on a failed pull (Tony's option A). Takes in L-380 and L-388. Two patches, gallery and orrery. -->
# Build record: the Daily Run pulls before it builds (L-446, with L-380 and L-388)

Built on gallery 95713f4912d3e1863390a246d2ba8004bc7cf4c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run again") and orrery 77245ea87179455bb4794ba7ed8712b98350fdb7 at
https://github.com/tonylquintanilla/palomas_orrery ("L445 L446 rulings
and briefs"; no code moved since the brief's b4105c0). The orrery patch
was rebuilt on 54c27d7fbda8bcc977a46914a9846b913e303276 ("L445 earth
period build") after L-445 landed first.
Gallery pushed at 0f8efb17996453d31328bc0a114e95b949ca00d6 ("L445
gallery period words L446 daily run again"). Orrery: Tony's push.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD. Two patches: the website's (the work) and the orrery's
  (the dashboard, the ledger, Where We Are, the skill, the protocol).
- From: `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.
- Ledger: L-446, with L-380 and L-388; L-423's item 2. All stay OPEN
  until Tony's run; the session that reads his run record closes them.

## 1. The one decision

Tony chose option A at the session's start: "A: Stop before the build
(Recommended)". When a pull cannot reach the orrery, the Daily Run stops
before the cache builder and names the pull. Nothing is built on
yesterday's export.

## 2. What was built

The website (patch_L446_2_daily_run_gallery_20261015.py):

- `daily_run.py` is four steps: the guest book, the pulls from the
  orrery, the cache builder, the offline maintenance run. If the pulls
  fail it stops and its summary quotes the line naming which failed.
- `gallery_maintenance_run.py --pull` runs only the five
  pull-and-mirror rows. It reads them from GENERATORS, so the list
  still has one home. Its last line starts "=== PULLS:".
- The three pulls (`tools/pull_constants_export.py`,
  `tools/pull_objects_export.py`, `tools/pull_drawings.py`) print a
  line starting "FAIL:" with the address they tried, and exit 1, where
  they printed N-A and exited 0.
- A mirror whose pull failed is not run; its row is red and names the
  pull.
- A failed generator now fails the offline run and is named in the
  summary. This goes one step past the brief. Before, generator rows
  were not counted, so a red pull sat above "27 of 27 passed" and the
  run exited 0. That is the same failure L-388 names, one level up.
- New gating checker "Pull failures", `tools/test_pull_failures.py`.

The orrery (patch_L446_3_daily_run_orrery_20261015.py):

- Dashboard: Pulls From The Orrery in the Daily Run group; Pull
  Failures in the gallery checks; Daily Run Steps says four scripts;
  the Daily Run's short line no longer names the JPL check.
- gallery-cache-builder 1.10: The Daily Run's Steps rewritten; its
  description names the Daily Run. Its 1.8 entry moved to
  `documentation/SKILL_HISTORIES.md`.
- Protocol v3.100, with v3.97 moved to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`.
- The ledger: the ruling and the build on L-446; notes on L-380, L-388
  and L-423's item 2.
- Where We Are: the box, road stage 8c, one Settled line, the
  pointers. Nothing below the run-record marker is touched.
- This record.

## 3. What was tested, in a sandbox

The sandbox cannot reach GitHub's API (it answers HTTP 403). That made
the network-off case real rather than staged.

- Network off. The Daily Run stopped after the pulls. The builder did
  not run. Every file under `data/` was byte-identical before and
  after. All five pull rows were red, each naming the address or the
  pull it waited on.
- Network on. Only the API's one answer, the orrery's HEAD SHA, was
  stood in for; the files themselves were fetched from GitHub. The
  pulls wrote orrery 77245ea's SHA; the builder (a stand-in) ran after
  them; the maintenance run's pull rows all printed "no change"; 28 of
  28 gating checkers passed (27 at the base, plus Pull failures).
- `daily_run.py --check` with the builder renamed away: "1 of 4 step
  scripts MISSING", exit 1.
- Pull failures against the ORIGINAL pulls: 9 of 13 FAILED. So the
  check can fail.
- Dashboard Parity: PASS, 83 steps. Against today's dashboard it
  names the two new steps with no button.
- The dashboard opened headlessly ("Dashboard ready").
- `skills_index.py --check`: no problems, once the skill's description
  was cut back under Anthropic's 1024-character limit; the check
  caught it at 1044.

The real cache builder was not run in the sandbox: it needs JPL. Your
Daily Run is its test.

## 4. The proof on Tony's machine

- Run the gallery patch, then the Daily Run once.
- Watch for: step 2 "Pulls from the orrery" runs before the builder;
  "=== PULLS: all 5 passed"; in step 4, the five pull rows print "no
  change"; Cache in step passes in the same run.
- L-445 (Earth's period) is not pushed yet, so this run carries no new
  period. That makes it the case where the pulls should change only
  the three SHA files, from 45085c4 to today's orrery HEAD.
- Commit, push, then the live run: Export freshness should name
  today's orrery HEAD.
- Then the orrery patch and `orrery_maintenance_run.py` (Dashboard
  parity, the ledger index, the skill manifest), commit, push.

## 5. Loose ends

- L-380 and L-388, read for anything the build does not cover: nothing.
- Ledger sweep for other open items on these files: none small enough
  to carry.
- The obligation: the next session confirms its loaded copy of
  gallery-cache-builder reads 1.10. v3.98's horizons-orbital-mechanics
  1.7 obligation also still travels.

## 6. Tony's actions, all of them

- (do) Save `patch_L446_2_daily_run_gallery_20261015.py` in the
  website folder and run it.
- (do) Run the Daily Run once; commit; push; run the live maintenance
  run.
- (do) Save `patch_L446_3_daily_run_orrery_20261015.py` in the orrery
  folder and run it; run `orrery_maintenance_run.py`; commit; push.
- (do) Move each spent patch into its repository's documentation/.
- (do) Reinstall gallery-cache-builder (1.10) in Settings > Skills;
  save PROJECT_INSTRUCTIONS.md as
  `documentation/project_instructions_v3_100.md` and copy it into the
  Project instructions.

## 7. What happened at Tony's first Daily Run (2026-10-15, evening)

- The pulls ran first and the build used them. The swap needed one
  retry, which the builder absorbed.
- Tony saw "a long row of red lines" and 117 changes, and committed
  nothing. The red lines were 82 deletions: the build had kept only its
  own run record in `data/solar-system/raw/runs/` and dropped the 82
  older ones. The data itself carried forward correctly, and the new
  cache passed 28 of 28 checks in a sandbox copy.
- The cause is not known: nothing in the builder deletes a run record,
  and four earlier swaps with the same retry kept them all. The 82 were
  put back from gallery 95713f4, at Tony's word. L-449 carries the
  question, and Tony's: whether to keep them at all.
- The orrery patch then refused, correctly: L-445's build had moved
  `documentation/SKILL_HISTORIES.md`. It was rebuilt on 54c27d7, and its
  protocol entry became v3.100.

Record written October 2026 with Anthropic's Claude Opus 5.5.
