<!-- Doc-Kind: hand | Brief for a short orrery Claude Code session on L-485 (a nightly run): a hand-fired switch that makes the night's Horizons check ask JPL about everything, so the one verification the first run could not make (JPL answering GitHub's computers) is made this week. Written by the coordinating session; zero code. -->
# Brief: the orrery session (L-485, "ask JPL for everything", a hand-fired switch)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 30, 2026, 18:05

Written at orrery 00c5576cda29d8a64b517db8970ef4ea694afbca at
https://github.com/tonylquintanilla/palomas_orrery (branch main), the
nightly run's own first commit, and gallery
b55109f228f37b38f248c6359298783889f992af at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 30, 17:45. YOUR BASE
IS HEAD WHEN YOU OPEN THE SESSION, which will be the commit that
carries this brief; read it yourself and anchor everything there.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a short build session in the ORRERY repository, a
slice of L-485 (a nightly run) following the orrery half built Oct 30
(`COORD_L485_orrery_nightly_brief_20261029.md`, its records on L-485).
The session reads this file, that brief, and L-485's block first.
Tony's ruling, Oct 30, 17:54: "yes, let's prove this part of the
workflow now."

## 0. The base, and what is waiting

- Orrery: HEAD, clean, with `.github/workflows/nightly.yml` and the
  runner's `--night` switch already in it. Tony's run record of today,
  `WHERE_WE_ARE_10-29-26_2320_run_record.md`, may show an edit waiting
  (his own notes); leave it alone.
- Gallery: read only, if at all; this slice does not touch it.
- Skills this job fires, read in full before the work, versions
  stated in the first report against the manifest in
  PROJECT_INSTRUCTIONS.md v3.118: safe-file-editing 1.14,
  agentic-pre-test 1.3, ledger-and-session-records 1.22,
  horizons-orbital-mechanics 1.13 (the Horizons check and what --all
  asks), provenance-discipline 2.36 (the push gate).
- The session asks Tony ONE question in all; this brief leaves none
  open.

## 1. Why

The first run on GitHub (Oct 30, 22:39 UTC, commit 00c5576) ran the
night set clean and committed its record, but asked JPL nothing:
"NOTHING DUE -- 90 entries and 26 sheets current, no query asked."
So the design record's one remaining verification, that JPL Horizons
answers a request from GitHub's computers as it does from Tony's house,
is still unmade. Waiting for a confirmation to come due would make it
on some night in the next weeks, unwatched. Tony wants it proven now,
by a run he fires by hand.

## 2. What to build

The orrery already has the form: the dashboard's "Horizons Check --
everything, now" button runs `horizons_check.py --all`, which asks JPL
about every keyed entry, every fetched period and every spacecraft
sheet whatever their dates (`horizons_check.py` line 1158,
`check_all="--all" in argv`). GitHub's computer cannot press a button,
so:

- **The runner:** a second switch beside `--night`, the session names
  it (`--ask-everything` is the coordinating session's suggestion),
  which adds `--all` to the Horizons check row's arguments and changes
  nothing else about the night. The shape already there for the
  confirmations checker (`NIGHT_ARGS`, `orrery_maintenance_run.py`
  line 553 at 00c5576) is the pattern; the switch prints one line
  naming what it changed ("Horizons check runs with --all: every
  entry, period and sheet asked tonight"). Without the switch the
  night is exactly as before.
- **The workflow:** `workflow_dispatch` gains one input, a tick box
  (`type: boolean`, default false), labelled in plain words ("Ask JPL
  for everything, not only what is due"); the night step passes the
  switch when it is ticked. The nightly schedule never sets it.
- **A test that can fail:** in `test_maintenance_report.py`'s night
  cases, the Horizons check row carries `--all` when the switch is on
  and not when it is off, with a planted fault for each direction, so
  a later edit that drops the switch or leaves it always on is caught
  by name.
- **Time.** The check pauses two seconds between questions
  (`horizons_check.py` line 179, `PAUSE_SECONDS = 2.0`); today's log
  counts 90 entries, 63 periods and 26 sheets. The runner kills a tool
  at 900 seconds (`TOOL_TIMEOUT_SECONDS`, line 502 at 586c46d1; re-read
  at HEAD). Read whether the check writes its two records only at the
  end (`_write_if_changed`, lines 1113 and 1118) or as it goes; if only
  at the end, a run cut at 900 seconds would ask JPL for fifteen
  minutes and keep nothing. BEFORE building, time `horizons_check.py
  --all` once on Tony's machine from the sandbox copy and report the
  seconds. If it is within a comfortable margin of 900, nothing
  changes. If not, the switch also raises the Horizons check row's
  timeout for that run, or the check saves as it goes; the session
  picks and says why. Do not guess the figure; the brief's "on the
  order of ten minutes" is the coordinating session's arithmetic, not
  a measurement.
- **Not in scope:** the path plan's "every path, now" (28 minutes on
  Tony's machine, Oct 24); the per-body form of a disagreement (P1,
  the orrery's next slice, on L-485); anything in the gallery.

## 3. What the hand-fired run proves, and what it commits

A clean run with the box ticked prints "Asked JPL for:" with names in
the Horizons check's verdict, and the confirmations come back stamped
with today's date. The night then commits `data/horizons_confirmations.json`,
`data/spacecraft_sheets.json` and `data/objects_export.json` (which
copies the dates); all three are on the allow-list already. That is
real data, not a test artefact: the confirmations are simply thirty
days younger. The website's next Daily Run pulls them as usual.

If the run instead prints UNREACHABLE for every object while Tony's
own machine can reach JPL at the same hour, that is the finding (R4:
reported, not red), and it goes on L-485 and L-490 as a legacy fact:
GitHub's computers cannot ask JPL, and the night tools' fetching must
run elsewhere. Do not retry around it.

## 4. Records

- L-485: the switch, by file; the measured time of `--all` on Tony's
  machine; and, after Tony's run, verification 5 closed with the log's
  "Asked JPL for" line quoted, or the finding above.
- Where We Are: one line in the box's "Changed" list and the Do-next
  line (push; the hand-fired run with the box ticked; Pull origin);
  nothing else moves. The marker and the zone below it untouched.
- Tier-1 = 0 on the active build path before Tony pushes.
- The final report, per the orrery's CLAUDE.md: the skills read with
  their version lines; the measured time; every file changed with its
  edit count; Tony's run order; the Tony-action rollup.

## 5. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. GitHub Desktop: commit and push the orrery.
3. GitHub's website, the Actions tab, "Nightly run" under "All
   workflows", "Run workflow": tick the box "Ask JPL for everything",
   leave the branch at main, click the green "Run workflow". It takes
   longer than the first run; the measured time from the report says
   how long.
4. Open the run, then the "night" job. In the night set's rows, the
   Horizons check's verdict should begin "Asked JPL for:" with names,
   and the commit step should name the three files. Paste the Horizons
   check's lines and the commit step's lines to the coordinating
   session.
5. GitHub Desktop: Fetch origin, then Pull origin. The dashboard's top
   line shows the run's time.
6. The Daily Run, as today, after the pull.
7. Send the orrery's SHA to the coordinating session.

## 6. Tony-action rollup

- (do) Open a Claude Code session on the orrery repository (the
  python_work door) and paste the short prompt the coordinating
  session gives you; it points here.
- (do) Afterwards, the run order in section 5.
- (decide) Nothing; the slice is ruled (Oct 30, 17:54).

Written October 30, 2026 with Anthropic's Claude Fable 5.1.
