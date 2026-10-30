<!-- Doc-Kind: hand | Brief for the orrery Claude Code session on L-485 (a nightly unattended run), the orrery half: the design record's section 4 verified first, then the GitHub Actions workflow that runs the orrery's night tools and commits their data files, gated by the checkers. Written by the coordinating session; zero code. -->
# Brief: the orrery session (L-485, the nightly run, the orrery half)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 29, 2026, 23:50

Written at orrery 586c46d1d17a4379a5d1450be40132b2bae681f1 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b55109f228f37b38f248c6359298783889f992af at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 29, 23:13, after
Tony's orrery push of 23:11. Every line number below was read from
those two commits. YOUR BASE IS HEAD WHEN YOU OPEN THE SESSION, which
will be the commit that carries this brief and Tony's run record; read
it yourself and anchor everything there (the handoff's lesson of Oct
29, section 1).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the ORRERY repository, item 1 of
`HANDOFF_coordination_20261029_30.md`, section 5. The session reads
this file, that handoff, and the design record
`DESIGN_L485_nightly_run_rulings_20261025.md` before anything else.
The ledger item is L-485 (a nightly run); its block carries the five
rulings (R1 to R5), the four proposals (P1 to P4, all now taken), and
the list of what the build verifies first. This brief does not repeat
them; it says how the orrery half is built under them, and what the
coordinating session found while reading for it.

## 0. The base, and what is waiting

- Orrery: HEAD, clean. Tony's run record for this session,
  `documentation/WHERE_WE_ARE_10-<d>-26_<hhmm>_run_record.md`, appears
  when he copies the page at your first run order; that one is
  expected. Anything else waiting is not.
- Gallery (the sibling folder): b55109f2 or later, clean. Read, never
  written, from this session. If Tony's Daily Run of Oct 30 has pushed,
  the gallery's HEAD is newer than b55109f2; that is expected too.
- Skills this job fires, each read in full before the work, versions
  stated in the first report against the manifest in
  PROJECT_INSTRUCTIONS.md v3.118: safe-file-editing 1.14,
  agentic-pre-test 1.3, ledger-and-session-records 1.22,
  gallery-cache-builder 1.14 (the Daily Run's order, the run records
  and their check), horizons-orbital-mechanics 1.13 (the three JPL
  tools the night runs), provenance-discipline 2.36 (the push gate),
  orrery-coding-conventions 1.12 (a new module's docstring, the
  dashboard). Note the obligation in v3.118's entry: a Code session
  reads the repo's copies, which are the manifest's.
- Order of work: section 1 (the verifications) first, and its results
  go in the report whatever they are; section 2 (the runner's night
  set) and section 3 (the workflow) are the build; section 4 (what
  Tony will notice) is written into the report; section 5 is the
  records. If the session runs out of room, section 3's keep-alive and
  the dashboard line are what move to the next orrery session, and the
  report says so plainly.
- The session asks Tony ONE question in all; this brief leaves none
  open. Three things it should TELL him, because they change his
  mornings (section 4).

## 1. What this session verifies before trusting the design

The design record's section 4 names five checks. Two are the gallery
half's (GitHub Pages redeploying on the workflow's commit; the guest
book's Google sign-in on a runner) and are not this session's. The
other three, and two the coordinating session adds, each with what was
already found:

1. **The sixty-day pause.** GitHub's documentation, read Oct 29
   (docs.github.com, "Events that trigger workflows", the schedule
   section, and "Disabling and enabling a workflow"): "In a public
   repository, scheduled workflows are automatically disabled when no
   repository activity has occurred in 60 days." Neither page defines
   repository activity, so whether the run's own nightly commits count
   is NOT stated by GitHub. Do not reason your way to "they must
   count". A check that leans on an undefined rule is a check that
   cannot fail, so the design gets the keep-alive regardless (section
   3), and the fact goes on L-490 (the legacy list) as the record
   asked: the pause exists, its definition of activity is unwritten,
   and the run re-enables itself each night.
2. **The runner's tools and time.** Read from GitHub's "Limits" page,
   Oct 29: "Each job in a workflow can run for up to 6 hours of
   execution time." The path plan's full re-check ran 28 minutes on
   Tony's machine on Oct 24 and now saves as it goes under the runner's
   own 15-minute per-tool timeout (`orrery_maintenance_run.py` line
   502, `TOOL_TIMEOUT_SECONDS = 900`), so the job fits with room. What
   is NOT yet known: whether `actions/setup-python`'s Python on
   ubuntu-latest can `import tkinter.messagebox`.
   `osculating_cache_manager.py` imports it at module top (line 41) and
   uses it only in a GUI dialog (line 825); `period_fetch.py` imports
   that module (lines 308 and 321), so a runner without Tk fails the
   period fetch at import. If the first hand-fired run shows that,
   the fix is in the module: move the import inside the one function
   that uses it, under safe-file-editing, and say so in the report.
   Confirm also, from GitHub's billing page, that Actions on a public
   repository costs nothing; the orrery is public (this brief's author
   cloned it with no credentials).
3. **Permissions.** The workflow declares `permissions: contents:
   write` (and `actions: write` for the keep-alive), AND the
   repository's own setting must allow the built-in token to write.
   Fetch GitHub's page on that setting and give Tony its exact words
   and clicks in the report (it is under the repository's Settings,
   Actions; the wording is GitHub's, not recalled). Confirm from the
   documentation who GitHub notifies when a SCHEDULED run fails; if
   nobody by default, that is a Tony-action (do) with the setting
   named.
4. **LF and ASCII on Linux.** The night tools write with `newline=""`
   where it matters (`horizons_check.py` line 1151, `path_plan.py` line
   1083); `osculating_cache_manager.save_cache` writes in text mode with
   no newline argument (L-485's body records this), which on Linux is
   LF anyway. Confirm by the first run's diff that no committed file
   changed its line endings or gained a non-ASCII byte, and that no
   tool assumed a Windows path (grep the six tools for backslashes and
   drive letters before the run).
5. **JPL from a GitHub runner** (added). Nothing in the record says
   whether Horizons answers a request from GitHub's addresses as it
   does from Tony's house. The first run is fired by hand from the
   Actions tab and its log read to the end; UNREACHABLE by name on
   every object on a night Tony's own machine can reach JPL is the
   finding to report, not to retry around (R4: reported, never
   halting; but the design is not trusted until one run has fetched).

## 2. The runner's night set (one pipeline, tagged rows)

The anti-pattern table rules this: no second runner. The orrery's
nightly job is `orrery_maintenance_run.py` with a switch (the shape the
coordinating session expects; the session settles the name and says
so), which runs the rows tagged for the night and PRINTS, by name, the
rows it ran and the rows it skipped and why (A Report Names Its Items).

The night rows, from the record's P2 and the tables at HEAD (lines 277
to 500), re-read before editing:

- Generators that write data the website pulls: Period fetch
  (`period_fetch.py`), Horizons check (`horizons_check.py`), Path plan
  (`path_plan.py`), Objects export (`export_objects.py`), Constants
  export (`export_constants.py`), Drawings export
  (`export_drawings.py`). Not the generators that write documents
  (Ledger index, Skill manifest, Module atlas, Data inventory, Exact
  rows report, Document index): at night no code changes, and R1
  forbids the nightly commit touching a page or a word a visitor
  reads.
- Checkers that gate those files and need no display and judge no
  code: Constants export check, Objects export check, Horizons
  confirmations, Horizons check suite, Period fetch suite, Path plan
  suite, Drawings export check, Orbit cache. Read each one's imports
  before tagging it (`test_period_fetch.py` imports
  `osculating_cache_manager`, see section 1, item 2). Not: Reset
  completeness (opens the Tk window), Dashboard parity, Constants
  change (reads a git diff of code), the provenance scanner as a gate,
  and the rest of the code-judging rows. The staleness report at the
  top and the files-written list at the end run as they do today.
- The link check named in P2 is not built. L-266 (the dead-link check)
  is open and is the first job of L-459 (a monthly run). The night set
  does not wait for it; it joins when built. Say this on L-485.
- The exit code is the gate (R1): 0 only when every night checker
  passed. The run also writes ONE record file the dashboard reads
  (section 3), stamped in UTC through `utc_clock.py`.

Behaviour on a JPL outage, under R4: the three JPL tools already print
UNREACHABLE by name and their suites carry a planted outage (the
runner's comments at lines 295 to 320 and 384 to 402). Confirm, by
running the suites and reading the verdicts, that an outage night is
REPORTED (the record and the log say UNREACHABLE) and is not a red row
unless a 30-day confirmation has actually lapsed; and that the
confirmations checker, which goes red on day 30, cannot be reached by
a run that asks again from day 25 (`horizons_check.py` line 167)
unless JPL is unreachable five nights running, which is then the true
finding.

## 3. The workflow (GitHub Actions, in the orrery repository)

One file, `.github/workflows/nightly.yml` (neither repository has a
`.github` folder at HEAD; this is the first). Its shape, which the
session builds and may improve, saying how:

- **Schedule:** `cron: '17 7 * * *'`, 07:17 UTC every day (2:17 am in
  Chicago until the clocks change on Nov 1, 1:17 am after). Tony's
  ruling of Oct 29, 23:36: the orrery at 7 UTC, the website at 8 UTC;
  the minute is 17 because GitHub's documentation says "High load
  times include the start of every hour" and "schedule your workflow
  to run at a different time of the hour". The website's workflow, the
  gallery half's job, follows at 08:17 UTC and pulls what this one
  pushed. Also `workflow_dispatch:`, so Tony and the session can fire
  it by hand from the Actions tab ("Run workflow").
- **Steps:** check out the repository; set up Python 3.13 (the
  requirements file's recommended version) and install
  `requirements.txt`; run the night set (section 2); then the gate.
- **The gate, in the runner's terms (R1):** if the night set exited
  non-zero, the job fails and commits nothing. If it exited 0, list
  the changed files (`git status --porcelain`) and compare the list
  with the ALLOW-LIST below; any path outside it fails the job without
  committing, naming the path. Then commit the allow-listed files with
  a message that names them and the UTC date, and push with the
  built-in token. A night that changed nothing commits nothing and
  says so.
- **The allow-list, read from `git ls-files data` at 586c46d1,
  fourteen tracked files:** `data/osculating_cache.json`,
  `data/horizons_confirmations.json`, `data/spacecraft_sheets.json`,
  `data/path_plans.json`, `data/objects_export.json`,
  `data/constants_export.json`, and the eight under `data/drawings/`
  (earth_exosphere, galactic_tide, hills_cloud, main_belt,
  outer_oort_cloud, sun_corona, van_allen_belts, zodiacal_dust); plus
  the one record file of section 2. `data/horizons_check_last_run.json`
  and the cache's backup files are git-ignored already and never
  appear. Re-read the list at HEAD; the count is the repo's, not this
  brief's.
- **The keep-alive (section 1, item 1):** the job's last step
  re-enables its own workflow (`gh workflow enable nightly.yml` with
  the built-in token), so the sixty-day pause cannot bite whatever
  GitHub counts as activity. One line, with a comment saying why and
  naming L-490.
- **The dated log and the dashboard's last-run line (R1):** GitHub
  keeps every run's log under the Actions tab; that is the dated log,
  and on a red night it is the ONLY record, since nothing is committed.
  The committed record file therefore carries the last CLEAN run's UTC
  stamp and its row verdicts; `palomas_orrery_dashboard.py` (the one
  dashboard for both repositories, L-416) gains one line that reads it
  and prints the last clean run's date, red when older than a day,
  with the words "no clean run since <date>" so silence cannot read as
  fine. orrery-coding-conventions fires for the line; Dashboard parity
  is run and read afterwards.
- **Who commits:** the built-in token, as `github-actions[bot]`.
  Scheduled workflows run on the latest commit of the default branch
  (GitHub's words), so each night builds on whatever Tony pushed last.

The first run is by hand, from the Actions tab, with the session
watching the log; the schedule is trusted only after that run has
fetched from JPL, committed its files (or truthfully committed
nothing), and the dashboard line reads it (P4: Tony then reads the log
each morning for a week).

## 4. What Tony will notice, to say in the report before he runs anything

- **His mornings gain one click.** The night's commit lands on GitHub,
  not on his laptop. GitHub Desktop will show "Pull origin" with a
  small number where "Push origin" was. He clicks it before any work,
  every morning the run committed something. Until he does, his orrery
  folder is yesterday's, and the gallery's Daily Run stops on purpose
  at its pull-matches-push check (L-461), which reads the commit in his
  orrery folder: a difference now has a second honest cause, "not yet
  pulled", beside "not yet pushed". Say this in plain words, and record
  the second cause on L-461.
- **Push before bed.** The run writes `data/osculating_cache.json`,
  which the orrery's own plotting also writes when it fetches an
  orbit. If Tony plots in the evening and does not push, and the night
  also changes that file, the morning pull reports a conflict in
  GitHub Desktop. His loop (commit and push after every session)
  avoids it. If it happens anyway, every file the night writes is
  regenerated by the maintenance run, so either copy may be kept and
  the maintenance run then rewrites it; say that too.
- **A session that opens before he pulls will stop.** The orrery's
  CLAUDE.md step 2 says a Code session stops when the folder and the
  remote differ. After a nightly commit they differ every morning until
  he pulls. The sentence stays true; it gains a case. That amendment is
  the records session's (handoff section 5, item 6), not this one's;
  put it on L-485 for that session, and tell Tony the morning order:
  Pull origin first, then anything else.

## 5. Records

- L-485: the orrery half built, by file; section 1's five findings as
  found; the night rows by name; the allow-list by name; the schedule
  and why the minute; the link check's status; the two sentences for
  the records session (CLAUDE.md step 2; one session per run record is
  already queued there). The gallery half is next and takes the four
  small website items on the handoff's section 4.
- L-490 (the legacy list): the sixty-day pause, GitHub's sentence, the
  undefined activity, the keep-alive built.
- L-461 (pull matches push): the second honest cause of a mismatch.
- L-459 and L-266: the night set runs without the link check; it joins
  when built.
- Skills: no bump in this session unless a sentence in one would make a
  following session DO something wrong (ledger-and-session-records,
  "A Wrong Sentence in a Skill"). The method the record says goes to
  gallery-cache-builder rides the gallery half's bump, which already
  carries received items; write the sentences on L-485 under "for
  gallery-cache-builder's next version" and, for the three JPL tools'
  new switch, "for horizons-orbital-mechanics' next version".
- Where We Are: the box rewritten (Changed: the orrery's nightly run
  exists and what it commits; Do next: the GitHub setting, the push,
  the hand-fired first run, then the morning routine); the road's L-485
  line marked by what this half did and that the gallery half is next;
  the marker and the zone below it untouched; the ledger's index
  rebuilt. `WHERE_WE_ARE.md` says "Pull origin each morning" in the
  Needs-you-now list from now on.
- Tier-1 = 0 on the active build path before Tony pushes
  (provenance-discipline): a new record file's writer, the dashboard
  line and any docstring are scanned; the workflow file is YAML and
  outside the scanner, which is fine, but any number typed into it
  (the hour, the version) is fetched or Tony's, never recalled.
- The final report, per the orrery's CLAUDE.md: the skills read with
  their version lines; section 1's findings; section 4's three
  tellings; every file changed with its edit count; Tony's run order;
  the Tony-action rollup. Tony pastes that report to the coordinating
  session before he commits.

## 6. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. On GitHub's website, the repository setting the report names, in
   its words: allow the workflow's token to write. One click, once.
3. GitHub Desktop: commit and push the orrery (the commit carries the
   workflow file, the runner's switch, the dashboard line, this brief,
   your run record and the records).
4. On GitHub's website, the Actions tab, the nightly workflow, "Run
   workflow": the first run, by hand. Read its log to the end with the
   coordinating session: what it fetched, what it committed or that
   it truthfully committed nothing, and no red row.
5. GitHub Desktop: "Fetch origin", then "Pull origin" if the run
   committed. Open the dashboard; its last-run line should read the
   run's date.
6. Every morning after, for a week: the Actions tab's latest run, green
   or red; then Pull origin; then the Daily Run as today.
7. Send the orrery's SHA to the coordinating session.

## 7. Tony-action rollup

- (do) Open a Claude Code session on the orrery repository (the
  python_work door: the prompt names the orrery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 6.
- (decide) Nothing; the hour is ruled (Oct 29, 23:36), P1 to P4 are
  taken, and every remaining question is the skill's or the session's.

Written October 29, 2026 with Anthropic's Claude Fable 5.1.
