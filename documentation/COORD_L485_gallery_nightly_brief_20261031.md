<!-- Doc-Kind: hand | Brief for the gallery Claude Code session on L-485 (a nightly unattended run), the gallery half: the website's own workflow on GitHub's computers, which pulls the orrery's exports, builds the cache, runs the checks and commits what the tools wrote; the website's date fix and three small items first. Written by the coordinating session; zero code. -->
# Brief: the gallery session (L-485, the nightly run, the gallery half)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 31, 2026, 10:45

Written at orrery 94d87a3aca40a5490e8ecef12a11c422b0200b07 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 981198c88535818fac82428b8cc912e5c085bb10 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 31, 09:52 Chicago
(14:52 UTC), and both matched Tony's folders at that moment. Every
line number below was read from those two commits. YOUR BASE IS HEAD
WHEN YOU OPEN THE SESSION, which will be later than these: the
orrery's nightly run commits to the orrery each night, and this brief
and Tony's run record travel in his next pushes. Read HEAD yourself
and anchor everything there.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the GALLERY repository, item 1 of
`HANDOFF_coordination_20261029_31.md`, section 5. The session reads
this file, that handoff (its section 4 is what this brief is built
from), the orrery half's brief
(`COORD_L485_orrery_nightly_brief_20261029.md`) and the design record
(`DESIGN_L485_nightly_run_rulings_20261025.md`) before anything else.
The ledger item is L-485 (a nightly run); its block carries the five
rulings (R1 to R5), the four proposals (all taken), the orrery half as
built, and the sentences the orrery sessions left for this half. This
brief does not repeat them; it says how the gallery half is built
under them, and what the coordinating session found while reading.

The gallery's own door, `CLAUDE.md` in the gallery folder, governs the
session: it edits the gallery's files directly, reads the orrery's
folder and does not edit it except the ledger and Where We Are, and
never commits or pushes.

## 0. The base, and what is waiting

- Gallery: HEAD, clean. Tony's run record for this session appears in
  the ORRERY's documentation folder when he copies the page at your
  first run order; that one is expected. Anything else waiting is not.
- Orrery (the sibling folder): HEAD or one nightly commit ahead of
  Tony's folder, since the orrery's run commits at 07:17 UTC. The
  gallery door's step 2 reads the GALLERY's base; the orrery's
  difference is read, not acted on, and Tony's Pull origin clears it.
  Read, never written, except the two record files at the close.
- Skills this job fires, each read in full from the orrery folder's
  `skills/` before the work, versions stated in the first report
  against the manifest in PROJECT_INSTRUCTIONS.md v3.118:
  safe-file-editing 1.14, agentic-pre-test 1.3,
  ledger-and-session-records 1.22, gallery-cache-builder 1.14 (the
  Daily Run's order, the swap log, the run records check, the pull
  that does not match the push), interactive-exhibit 1.29 (the three
  small website items of section 2: a served number's words, the
  digits rule, the Solar System figures check), provenance-discipline
  2.36 (What a Visitor Reads, for the sentence in section 2, item 3).
  A gallery session reads the skills and does not edit them; the
  sentences this build makes true or false go on L-485 for the next
  orrery session (section 6).
- Order of work: section 2 (the four small website items, the date
  first) before anything else, because the first one fires on its own
  schedule every evening until it is fixed; then section 1 (the
  verifications), whose results go in the report whatever they are;
  section 3 (the night form of the Daily Run) and section 4 (the
  workflow) are the build; section 5 (what Tony will notice) is
  written into the report; section 6 is the records. If the session
  runs out of room, section 4's keep-alive and concurrency lines are
  what move to the next gallery session, and the report says so
  plainly.
- The session asks Tony ONE question in all; this brief leaves none
  open. Tony ruled the one question the coordinating session had (Oct
  31, 10:20): the guest book stays OUT of the night; he does it himself
  each morning. Three things the session should TELL him, because
  they change his mornings (section 5).

## 1. What this session verifies before trusting the design

The design record's section 4 named five checks. The orrery half
settled three for the orrery's tools (L-485's block: the sixty-day
pause and its keep-alive; the token's permission and who is told of a
failure; LF and ASCII on Linux). Two were left for this half, and the
coordinating session adds three, each with what was already found:

1. **The pulls ask GitHub without signing in, and GitHub limits that
   by address.** `tools/pull_constants_export.py` line 93,
   `tools/pull_objects_export.py` line 60 and `tools/pull_drawings.py`
   line 158 each read the orrery's newest commit from
   `https://api.github.com/repos/.../commits/main` with no token, then
   fetch the file at that commit from raw.githubusercontent.com.
   GitHub's page on rate limits, read Oct 31 (docs.github.com, "Rate
   limits for the REST API"): "The primary rate limit for
   unauthenticated requests is 60 requests per hour", and
   "Unauthenticated requests are associated with the originating IP
   address". GitHub's own runners share addresses among many people's
   jobs, so three unsigned requests a night may be refused on a night
   the shared address has already spent its sixty. The same page: "The
   rate limit for GITHUB_TOKEN is 1,000 requests per hour per
   repository." So: have each pull send the run's own token when the
   environment carries one (`GITHUB_TOKEN`, as an `Authorization:
   Bearer` header, GitHub's words for it read from its page on
   authenticating in a workflow), and send nothing on Tony's machine,
   where the variable does not exist and the sixty are his own. Three
   edits under safe-file-editing, one per pull, and `tools/
   test_pull_failures.py` ("Pull failures", gating) still plants its
   three failures. If the session finds a reason the header is wrong,
   the other honest form is `git ls-remote` for the commit, which asks
   no interface at all; say which it chose and why. The first run by
   hand proves it either way: a pull refused with GitHub's rate-limit
   message, by name, is the finding.
2. **The runner's tools and the night's time.** Python 3.13 with the
   builder's libraries from `requirements.txt` (astropy and astroquery
   for Horizons, numpy, pandas; the file is the orrery's and installed
   clean on the orrery's runner, Oct 30). Node for the smoke suites:
   every `documentation/smoke_*.js` the maintenance run names requires
   only `fs` and `path` (read Oct 31, 38 and 36 requires, no browser
   library anywhere in them), so a headless Chromium is NOT needed for
   the night; the design record's sentence saying it was is corrected
   on L-485. Confirm from GitHub's runner-image software list for
   ubuntu-24.04 that node is on the image; if it is not, add
   `actions/setup-node` and say so. Time: the cache build took about
   three minutes in Tony's Daily Run of Oct 31 (swap log, run
   20261031T140937Z, started 14:09:37, swapped 14:12:36 UTC); the
   offline pass's time is
   not recorded anywhere, so time one full night on your machine in a
   spare clone before the workflow is written, and put the seconds in
   the report. Each tool keeps the maintenance run's own 900-second
   limit (`gallery_maintenance_run.py` line 214); the job keeps
   GitHub's six hours.
3. **Permissions, and Pages.** The workflow declares `contents: write`
   and `actions: write` as the orrery's does, AND the gallery
   repository's own setting must allow the token to write: Settings,
   Actions, General, "Workflow permissions", "Read and write
   permissions", Save, the same clicks Tony made for the orrery on Oct
   30. Give him the clicks in the report; it is one Tony-action (do).
   Pages: a commit pushed with the workflow's token started a "pages
   build and deployment" run in the ORRERY repository after each of
   the night's commits (runs 1175 and 1177, read from the Actions list
   on Oct 31), so GitHub redeploys on the bot's commit. The gallery is
   the site itself; the first hand-fired run confirms it there: a
   "pages build and deployment" line under the night's commit, and
   then Tony's `--live` pass from the dashboard reading the served
   bytes as current.
4. **LF and ASCII on Linux, and no Windows path.** The builder writes
   `coverage_index.json` and `feature_configs.json` in text mode
   (`gallery_maintenance_run.py` lines 812 to 827 record why those two
   read CRLF in Tony's working copy); on Linux that is LF, and
   `.gitattributes` (`* text=auto eol=lf`) stores every text file LF
   whatever a tool writes. Grep the night's tools (`daily_run.py`,
   `gallery_maintenance_run.py`, the three pulls, the two mirrors,
   `tools/gallery_cache_builder.py`) for backslashes and drive letters
   before the run; `daily_run.py` line 168 is the one known Windows
   assumption, the sibling folder, and section 3 replaces it. The
   night's gate (section 3) refuses a non-ASCII byte in any file it
   would commit, so this is checked every night, not once.
5. **JPL from GitHub's computers, for the builder.** Settled for the
   orrery's three JPL tools on Oct 31, 00:10 UTC: "PASS -- 179 checked
   today, 269 queries" (L-485). The builder asks Horizons through the
   same library, so the expectation is yes; the first run by hand shows
   it. A night the builder cannot reach JPL is a RED night: the build
   does not swap, nothing is committed, the site keeps serving the
   previous cache, and the next night tries again (R1 and R4 together;
   nothing to build for it beyond the log line that says so).

## 2. First, the four small website items (carried since Oct 29)

Each was found by an earlier session and is on L-485's gap or the Oct
29-30 handoff's section 4; none needs a design word. In this order:

1. **The confirmations check reads UTC today.**
   `tools/check_horizons_confirmations.py` line 272 passes
   `datetime.date.today()`, the machine's local date; the orrery's
   reader passes `utc_clock.utc_today()` since L-504. On Oct 30 at
   20:10 Chicago the orrery had stamped every confirmation 2026-10-31
   (UTC) and this check read 2026-10-30, so every entry failed as
   "confirmed on 2026-10-31, which is after today". The one-line fix:
   `datetime.datetime.now(datetime.timezone.utc).date()` in `main()`
   (the gallery cannot import the orrery's `utc_clock`, and a date read
   is not a stored number, so no second store is made). `self_test`
   at line 172 takes the same `today`, so nothing else moves. Say in
   the docstring why. On GitHub's computers the local date is already
   UTC, so this fix is for Tony's evening Daily Run; it closes the
   L-504 website item.
2. **The belt's kilometres.** The orrery's export carries the main
   belt's bounds in kilometres since Oct 29 (L-503: "the export now
   carries the belt's kilometres", the new "in" fields); the website
   prints the AU alone. Print them the way the orrery does ("1.67 AU
   (about 250 million km)"), from the served copy of those fields,
   never typed; read the field names from `data/objects_export.json`
   at HEAD and the room's row for the belt. Closes L-503.
3. **"JPL states none", not "not yet included".**
   `gallery/solar_system_figures.js` line 115 prints "JPL's own
   uncertainty for this position is not yet included." for every small
   body with no served `position_uncertainty`. Since Oct 29 the
   builder serves, in the index's `position_uncertainty` block, why
   each missing one is missing (gallery-cache-builder 1.14, A Small
   Body's Own Uncertainty Is Served). Read those reasons at HEAD and
   print the true sentence for each: JPL gave no figure ("JPL states
   none" -- the orrery's sentence since Oct 29, L-484), or the figure
   was refused or not asked (say which). provenance-discipline's What
   a Visitor Reads, principle 5: JPL's own word kept and explained.
   Closes the L-484 website item.
4. **The digits a distance with no uncertainty prints.** The orrery
   prints the whole kilometre and the website the tens (L-484). This
   is METHOD, settled in interactive-exhibit 1.29 (read its rule on a
   served number's figures before touching the page); apply the skill's
   rule to the website's formatter and say in the report which digits
   now print and why. Not Tony's question.

Known and NOT in this brief's scope: the Solar System room's headless
walk fails 3 of 171 on the base since Oct 27's one text box (the Oct
29-30 handoff, section 4; the recipe is in interactive-exhibit 1.29,
"testing a room headlessly"). Fix it only if it is in the way of a
check this build adds; otherwise leave it on its item.

## 3. The night form of the Daily Run (one pipeline, a switch)

The anti-pattern table rules this: no second runner. `daily_run.py`
is the Daily Run, and it gains a switch (`--night`, the orrery's name;
the session settles it and says so) that runs the same steps without
a keyboard and ends in one gate. What changes at night, read from
`daily_run.py` at 981198c8 before editing:

- **The guest book is skipped, by name, with its reason.** Tony's
  ruling of Oct 31, 10:20: it stays his morning's. The night prints
  the row as skipped ("needs Tony's answers; his morning's, Oct 31")
  and reads nothing from Google, so no address, secret or sign-in
  exists on the runner. R5's "lists new messages" is NOT built; say so
  on L-485 as Tony's ruling, so no later session builds it unasked.
- **The pulls run as they do** (step 2, `gallery_maintenance_run.py
  --pull`, lines 148 to 155), with section 1 item 1's token.
- **Pull matches push gets its runner form.** `pull_matches_push()`
  (line 242) reads the newest commit in Tony's orrery FOLDER (line
  168); on GitHub's computer there is no such folder, and
  `local_head()` would return "cannot", which stops the run. The
  honest form there, from the Oct 29-31 handoff's section 4: the
  three pulled commits (`data/constants_export.sha`,
  `data/objects_export.sha`, `data/drawings/pulled_at.sha`) must agree
  with each other AND with the orrery's remote HEAD read live
  (`git ls-remote https://github.com/tonylquintanilla/palomas_orrery
  HEAD`, the same read the coordinating session makes), which is the
  same question asked of the only copy a runner can see. A difference
  means the orrery was pushed during the pulls; the night STOPS before
  the builder, as Tony's ruling of Oct 25 says ("stop. confirmed."):
  no retry, no wait, and tomorrow's run reads the new commit. Tony's
  morning Daily Run keeps the folder form untouched. `--check`'s
  fixtures (line 283) gain the runner form's cases and one planted
  fault for it, so "Daily run steps" still proves the comparison can
  fail.
- **The builder runs with no flags**, as in the Daily Run; NEVER with
  `--commit` (line 3000), which commits and pushes from inside the
  builder BEFORE the checks run: the workflow commits, after the gate,
  and only then (R1).
- **The run-records check runs** (line 539) and a loss stops the
  night as it stops the day. "Could not compare" (a failed or
  rolled-back build) is a red night, since the builder itself failed.
- **The offline maintenance run runs whole** (step 4), minus the one
  generator that writes documents, "Module atlas" (`MODULE_ATLAS.md`,
  `MODULE_INDEX.md`; `gallery_maintenance_run.py` line 223): R1
  forbids the night committing a page or a word. Add the gallery
  maintenance run's own switch for that one skip, printed by name with
  its reason, or let the night's gate refuse the two files if they
  changed; the session picks and says why. Every offline checker runs:
  none opens a window (the Store editor suite is checked without one,
  lines 300 to 309), none reads a git diff, and each is minutes, so there is
  nothing to skip and more gate is better. A row that cannot run on
  Linux, if one turns up, is skipped BY NAME with the reason, and the
  report says so; it is not folded into a pass (A Check That Cannot
  Fail Is Not Passing, and the runner's own UNREACHABLE state).
- **The gate (R1), in the night's own terms**, exit 0 only when ALL
  hold, and every reason named in its last line otherwise:
  - the pulls passed and pull matches push;
  - the builder exited 0 AND the swap log's last line
    (`data/cache_swap_log.jsonl`) is THIS run's id with outcome `ok`
    (read back off the disk, the way the maintenance run's last line
    does, line 1481): a build that did not reach the swap is not a
    build;
  - the run records were carried;
  - every gating checker of the maintenance run passed, and no row is
    UNREACHABLE (node missing on the runner is a setup fault, red, not
    an outside failure);
  - git sees nothing changed or new outside the ALLOW-LIST (section
    4);
  - every changed text file is ASCII;
  - the change under `data/solar-system/` is NOT deletions only. This
    is the pre-commit hook gallery-cache-builder 1.14 says was designed
    and deliberately not built, "relevant again ... if the builder
    ever runs unattended in any other form" (Operating mode, lines 97
    to 101): the Aug 10 commit of a half-swapped cache. On the runner
    the swap and the commit are one after the other, so the window
    cannot be hit; the guard is cheap and makes the skill's sentence
    true, so build it into the gate rather than as a hook.
- **The record.** A clean night writes `data/nightly_run_record.json`
  in the gallery, the orrery's shape (schema, `clean_run_utc`, where,
  the run's log address, each row's verdict, the rows skipped and why,
  the pulled orrery commit, the swap log's line). A red night writes
  nothing: its record is the run's log on GitHub (R1's dated log).
  Stamp it in UTC with a plain `datetime.now(timezone.utc)` as in
  section 2 item 1.
- **Nothing in the Daily Run commits or pushes**, by day or by night;
  the workflow does.

## 4. The workflow (GitHub Actions, in the gallery repository)

One file, `.github/workflows/nightly.yml`, the gallery's first `.github`
folder, modelled on the orrery's (`.github/workflows/nightly.yml` at
94d87a3a, 124 lines: read it first; its comments carry GitHub's own
words and the dates they were read). Its shape:

- **Schedule:** `cron: '17 8 * * *'`, 08:17 UTC every day (3:17 am in
  Chicago until the clocks change on Nov 1, 2:17 am after). Tony's
  ruling of Oct 29, 23:36: the orrery at 7 UTC, the website at 8; the
  minute off the hour by GitHub's advice. Also `workflow_dispatch:`
  for a run by hand. No tick box: the orrery's "ask JPL for
  everything" has no counterpart here.
- **The hour gap is a hope, not a rule** (the Oct 29-31 handoff,
  section 1): the orrery's first scheduled run started 6 h 22 min
  late, and GitHub's documentation allows a delay without bounding it.
  The website's run pulls whatever the orrery's GitHub copy holds when
  it starts, at worst the previous night's exports, inside the
  thirty-day margin; it never waits for the orrery's run, and no
  credential is shared between the repositories to chain them (P3's
  reason stands). Write this in the file's comment so a later reader
  does not "fix" it by chaining.
- **Concurrency:** a run by hand and the scheduled run must never
  overlap, since both push; one line with GitHub's `concurrency` key
  (its page read, its words quoted in the comment) so a second run
  waits for the first. The orrery's workflow lacks this; put a sentence
  on L-485 for the next orrery session.
- **Runner and steps:** `ubuntu-24.04`, named as the orrery's is (the
  image page's reason is in the orrery file's comment); check out;
  Python 3.13; `pip install -r requirements.txt`; node confirmed or set
  up (section 1 item 2); run `python daily_run.py --night`; then the
  gate's commit step.
- **The commit step, in the runner's terms (R1):** if the night exited
  non-zero, the job fails and commits nothing. If it exited 0, stage
  ONLY the allow-list, compare `git status --porcelain` against it,
  fail naming any path outside it, then commit with a message naming
  the files and the UTC date, as `github-actions[bot]` with the name
  and address the orrery's file uses, and push. A night that changed
  nothing commits nothing and says so.
- **The allow-list, read from the tools' declared outputs (one
  home), as the orrery's is read from its runner:**
  - the five pull-and-mirror rows' outputs (`GENERATORS`, lines 231 to
    253): `data/constants_export.json`, `data/constants_export.sha`,
    `data/objects_export.json`, `data/objects_export.sha`,
    `data/objects_config.json` (the two mirrors' numbers and words,
    tool-written, so R1 allows it), and `data/drawings/` as the pull
    writes it (`pulled_at.sha` and each drawing the config names; the
    row's declared list names three drawings and `pulled_at.sha`, and
    git tracks eight drawings and the sha under `data/drawings/`, so
    read the pull's own list, not the row's);
  - the served cache, the WHOLE of `data/solar-system/` as the swap
    leaves it, deletions included (334 tracked files under `data/` at
    981198c8, 318 of them under `data/solar-system/`: runs 120,
    vectors 94, elements 68, positions 26, drawings 8, two indexes);
    `git add -A -- data/solar-system` is the honest form, under the
    deletions-only guard of section 3;
  - `data/cache_swap_log.jsonl`;
  - `data/nightly_run_record.json`.
  Never `data/guestbook.json` (R5 as ruled: the night does not touch
  it), never a page, a script, a card or `MODULE_ATLAS.md`.
  `.gitignore` already keeps `.prev`, `.staging_*`, `.quarantine_*`
  and the OneDrive siblings out.
- **The keep-alive**, as the orrery's last step: `gh workflow enable
  nightly.yml`, `if: always()`, with the comment naming L-490 and why.
- **The live pass (`--live`) is NOT in the night.** It means something
  only after Pages has deployed, which happens in GitHub's own run
  after the commit, minutes later and outside this job. The Actions
  tab's "pages build and deployment" line is the night's deploy check,
  green or red; Tony's `--live` pass from the dashboard stays his, when
  he likes. A later slice may chain a second job on it; not this one.
- **The dashboard's second line** (the website's last clean night,
  read from the gallery's record in the sibling folder) is an ORRERY
  edit, `palomas_orrery_dashboard.py` beside `nightly_run_line()`
  (line 2382 at 94d87a3a), which a gallery session does not make. Put
  it on L-485 for the next orrery session, with the gallery-cache-
  builder bump (section 6).

The first run is by hand, from the gallery's Actions tab, with the
session's report in Tony's hand and the coordinating session reading
the log with him; the schedule is trusted only after that run has
pulled, built, swapped, passed, committed (or truthfully committed
nothing), Pages has redeployed, and Tony's `--live` pass reads the
site as current (P4: then a week of mornings).

## 5. What Tony will notice, to say in the report before he runs anything

- **His mornings change shape, once both halves run.** Pull origin
  on BOTH repositories, orrery then gallery, before anything else
  (GitHub Desktop shows "Pull origin" with a number on each). Then the
  guest book updater alone, from the dashboard's button, and his
  commit and push of `data/guestbook.json` if it changed. Then a look
  at two logs: the orrery's Actions tab and the gallery's. The Daily
  Run stays a button for when he wants a build now (after Pull
  origin), not a habit; its own gate (L-461) still reads his orrery
  folder, so Pull origin first.
- **Push before bed, for the gallery too.** The night's mirrors
  rewrite `data/objects_config.json` and the swap rewrites the served
  cache. If Tony edits the config's words with the store editor in the
  evening, or builds the cache by hand, and does not push, the morning
  pull reports a conflict in GitHub Desktop. His loop avoids it. If it
  happens anyway: his copy of the config is the one to keep (the
  mirrors rewrite only the fields they own, next run); for the cache,
  either copy, since the next build replaces it whole. Tell the
  coordinating session before clicking anything.
- **A session that opens before he pulls will stop**, on either
  repository, as the orrery's door already does. The gallery door's
  step 2 gains the same case; that amendment is the records session's
  (the coordination handoff's queue, item 6), not this one's; put it
  on L-485 and tell Tony the order: Pull origin first.

## 6. Records

- L-485: the gallery half built, by file; section 1's five findings
  as found, with the time measured; the night rows and skips by name;
  the allow-list by name; the gate's seven conditions; the schedule;
  the four small items closed (L-504's website item, L-503, L-484's
  two) with their lines; Tony's ruling of Oct 31 (the guest book out
  of the night, his mornings); the design record's "headless
  Chromium" sentence corrected; and the sentences for others:
  - for the next ORRERY session: gallery-cache-builder's next version
    (the lines already on L-485 from Oct 28 and 30, plus this build:
    the Operating mode section rewritten, since the builder now runs
    unattended on GitHub's computer and the skill still says "manual,
    as of August 10 2026"; Layer 3 live again, in the GitHub Action
    form; the Daily Run's night form and its runner-side pull-match;
    the deletions-only guard built into the gate rather than as a
    hook); the dashboard's second line; the `concurrency` line for the
    orrery's workflow;
  - for the records session: the gallery door's step 2 case.
- L-503: closed when the website prints the kilometres and Tony's
  look passes (Mode 5: his phone, the belt's row).
- L-484: the website's half (the sentence and the digits) closed.
- L-504: the website item closed; the later orrery slices unchanged.
- L-461 (pull matches push): the runner form, a third shape of the
  same question.
- L-490 (the legacy list): the gallery's keep-alive built; the Pages
  redeploy verified on the site; the pulls' token.
- Skills: no bump in this session (a gallery session reads them). If a
  sentence in one would make a following session DO something wrong
  after this build, name it on L-485 for the orrery session, as
  ledger-and-session-records says (A Wrong Sentence in a Skill); the
  Operating mode sentence above is the candidate.
- Where We Are (in the orrery folder): the box rewritten (Changed: the
  website's nightly run exists and what it commits; the date fix; Do
  next: the GitHub setting, the push, the hand-fired first run, the
  `--live` pass, then the new mornings); the road's 11b line marked by
  what this half did; "Pull origin on both repositories each morning"
  in Needs-you-now; the marker and the zone below it untouched; the
  ledger's index rebuilt.
- The final report, per the gallery's CLAUDE.md: the skills read with
  their version lines; section 1's findings and the time; section 5's
  three tellings; every file changed with its edit count, in both
  folders; Tony's run order; the Tony-action rollup. Tony pastes that
  report to the coordinating session before he commits.

## 7. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. On GitHub's website, the GALLERY repository
   (github.com/tonylquintanilla/tonyquintanilla.github.io): Settings,
   Actions, General, "Workflow permissions", "Read and write
   permissions", Save. The same clicks as the orrery's on Oct 30, once.
3. GitHub Desktop: Pull origin on the orrery if it shows a number
   (last night's run); then commit and push the GALLERY (the workflow
   file, the Daily Run's switch, the pulls, the four small fixes, the
   record's writer); then commit and push the ORRERY (this brief, the
   records, your run record).
4. On GitHub's website, the gallery's Actions tab, "Nightly run", "Run
   workflow", branch main: the first run, by hand. Expect the build's
   minutes plus the checks'. Read its log to the end with the
   coordinating session: the pulls (what commit), pull matches push,
   the builder's [SWAP] line, the run records line, the checkers'
   count, the gate's last line, the commit's files or "nothing
   committed", the keep-alive.
5. On the same Actions list, a "pages build and deployment" run should
   appear under the night's commit within a few minutes. Then GitHub
   Desktop: Fetch origin, Pull origin on the gallery. Then the
   dashboard's live pass (`gallery_maintenance_run.py --live`): the
   site serves the night's bytes.
6. Every morning after, for a week: both Actions tabs (note each
   start time in your run record, for the delay question), Pull
   origin on both, the guest book updater, a push if it changed.
7. Send both SHAs to the coordinating session.

## 8. Tony-action rollup

- (do) Open a Claude Code session on the GALLERY repository (the
  python_work door: the prompt names the gallery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 7.
- (decide) Nothing; the hour is ruled (Oct 29, 23:36), the guest book
  is ruled (Oct 31, 10:20), P1 to P4 are taken, and every remaining
  question is the skill's or the session's.

Written October 31, 2026 with Anthropic's Claude Fable 5.1.
