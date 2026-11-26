<!-- Doc-Kind: hand | The plan (Part 1) for L-545's build: the drawer walk and the clock walk become rows of the website's maintenance run, at night on GitHub and on Tony's computer, each with its dashboard button. No code edited. For the coordinating session to read against the code before Tony's go-ahead. Communication; written once. -->
# Plan: the walks become checks of the website's maintenance run (L-545, Part 1)

Read on Tony's working copies, each equal to GitHub at its HEAD:
- orrery 78f32c5e828262c81a8c1ab436a725b9f08b315e at
  https://github.com/tonylquintanilla/palomas_orrery (branch main);
- gallery 972b4a9366224160d03f84708c9d33f55b811b87 at
  https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
  main).

Both read 2026-11-26, 11:00 to 11:30 Chicago. The website folder is
clean. The orrery folder holds one edit, in Tony's run record copy
`WHERE_WE_ARE_11-26-26_1111_run_record.md`, his own. 78f32c5e is his
push of the brief ("L545 walks") on top of the brief's 0666ad67; no
night has committed in either repository since.

Written November 26, 2026 with Anthropic's Claude Opus 5.5, a Claude
Code session through the python_work door, by
`documentation/COORD_L545_walks_in_the_runner_brief_20261126.md`.

Skills read, the repository's copies, in the parts this job fires:
- interactive-exhibit 1.45 (Phone first, A SESSION THAT CHANGES THE
  PAGE RUNS THE WALKS)
- gallery-cache-builder 1.24 (Operating mode; The Daily Run's Steps)
- safe-file-editing 1.15 and agentic-pre-test 1.4 (version lines; read
  whole before the build)
- ledger-and-session-records 1.25 (version line; read at the close)

## Measured this session, on Tony's computer

Windows 11, Node 24.13.1 (not GitHub's 22.23.4), jsdom 24.1.3 installed
from npm into this session's scratch folder (63 packages, 15 MB, 1,419
files, 5 seconds). The served window at gallery 972b4a93 runs from
JD 2461282.44 to 2461458.38: 29 August 2026 to 21 February 2027, 21:05
UTC; the cache was built 25 November, 21:47 UTC.

The drawer walk, each scene made by `run_room_driver.py
SOLAR_SYSTEM_DRIVER` (under a second each, 430 traces, 0 warnings):

| Scene's minute (UTC) | Days from the build | Result | Time |
|---|---|---|---|
| 2026-08-29 23:00 | 88 before | FAIL 1 of 383 (Io, below) | 57 s |
| 2026-10-15 00:00 | 42 before | PASS: 383 checks | 54 s |
| 2026-11-26 17:22 (the run's own) | 1 after | PASS: 383 checks | 53 s |
| 2026-12-25 12:00 | 30 after | PASS: 383 checks | 54 s |
| 2027-01-31 06:00 | 66 after | PASS: 383 checks | 53 s |
| 2027-02-07 00:00 | 73 after | PASS: 383 checks | about 53 s |
| 2027-02-14 00:00 | 80 after | PASS: 383 checks | about 53 s |
| 2027-02-21 21:00 | 88 after | FAIL 1 of 383 (Io, below) | 52 s |

The one red check at both edges: "Io's box does not open on its name
and its distance from Jupiter". The page prints "0.0028 AU from Jupiter
(400,000 km)", two figures, since its digits shrink as the minute moves
away from Io's orbit date; the walk works the distance out (421,661 km
and 423,595 km) and allows 1 percent. So the walk's tolerance, not the
page, fails far from the build. FOUND, NOT CHASED: what the walks check
is out of this build's scope.

The clock walk, at the run's minute and the window's last whole
minute, 2027-02-21 21:05 UTC: solar-system "13 of 13 checks passed"
(3 s); earth "10 of 10 checks passed" (1 s), the Earth room's frozen
note reading "This room shows 21 Feb 2027, 21:05 UTC, the last day its
data covers, and not today."

A planted page for the drawer walk (below): "FAIL 7 of 66", one for
each ended mission, in 13 seconds.

After every run `git status` in the website folder was clean: the
walks and the scene maker wrote nothing inside it.

## The plan

### 1. Two rows, their place, their buttons

- Rows `Drawer walk` and `Clock walk` in `OFFLINE_CHECKERS`, right
  after `Room clock`, with the page's other checks.
- Both run one new Python tool, `tools/headless/run_walk.py drawer` and
  `run_walk.py clock`, from the gallery root. It finds the library and
  Node, makes the scenes fresh, walks the real page, then walks a
  planted page, and prints one last line the row shows: "DRAWER WALK:
  PASS -- 383 checks on the real page at 2026-11-26 17:22 UTC; planted
  fault (an ended mission's last day one day early) caught, 7 of 66
  red".
- A new runner kind, `"walk"`: run under Python like a `"python"` row,
  except that exit code 3 means it could not run, and the row is
  UNREACHABLE. Only the walk rows use it, so no other row changes.
  Dashboard parity reads it as a Python step (it only asks whether a
  row is `"node"`).
- Dashboard buttons `Drawer Walk` and `Clock Walk`, indented in
  "Gallery -- checks and data", each running `tools/headless/run_walk.py`
  with `drawer` or `clock`, from the gallery root, and a short line each
  in CARD_LINES (twelve words or fewer). This session adds them (L-550
  (a website check with no dashboard button)).

### 2. Which moment, and whether it holds

- The drawer walk's scene is made at the run's own minute (UTC, to the
  minute). The clock walk makes two per room: the run's minute and the
  last whole minute at or before the served window's end, read from
  `coverage_index.json`.
- The clock walk holds at any minute inside the window by how it is
  written: it reads the window's end and the real clock itself.
  Measured only today, in both rooms.
- The drawer walk holds from 42 days before the build to 80 days after
  it, and fails on Io's digits at 88 days either side (the table). The
  run's minute is never before the build, and the night rebuilds every
  night, so the run's minute sits a day or two after the build. It goes
  red only when the served cache is 81 or more days old, when the room
  is days from freezing at its last day and the nights have been red
  for weeks for other reasons. Not a red night for nothing in practice.
- WHAT THIS SETTLES OF L-551 (no saved scenes): for the two walks, no
  saved scene, a fresh one at every run, at the run's minute (and the
  window's last minute for the clock walk). WHAT IT LEAVES: the ten
  smoke checks and the two walks (drawer order, shell reset) that read
  the three saved copies; `tools/record_earth_scene.py`; and whether
  one moment is enough for those. Io's 1 percent is recorded on L-545.

### 3. Which rooms the clock walk walks

Both the walk knows: solar-system and earth. Earth is measured at 1
second, so it costs nothing to keep.

### 4. Where the library lives, how it is found, another version

- One place in the code: `WALKS_LIBRARY` in `run_walk.py`, the folder
  `palomas_orrery_walks` in the home folder. On Tony's computer that is
  `C:\Users\tonyq\palomas_orrery_walks`, outside OneDrive (which holds
  only `C:\Users\tonyq\OneDrive`) and outside both repositories. On
  GitHub it is `/home/runner/palomas_orrery_walks`, outside the
  checkout, so the night's commit step, which refuses anything new in
  the checkout, never sees it. Same line of code, both computers; no
  setting to keep in step.
- The tool reads `node_modules/jsdom/package.json` there. Missing, or
  any version but 24.1.3: UNREACHABLE, exit 3, in one sentence naming
  the library, the folder looked in, the version found if any, and the
  command that installs it. Node missing: UNREACHABLE too.
- The tool hands the walk the library through NODE_PATH for that one
  run; nothing global changes.
- At night the workflow installs it with the same command, a step
  before the night's step. Nothing of it is committed.

### 5. The install: a command, not a button

The command, typed once in PowerShell, printed by the UNREACHABLE
sentence itself:

    npm install --prefix "$HOME\palomas_orrery_walks" jsdom@24.1.3

Why not a button: Dashboard parity's rule 3 holds every indented
button in "Gallery -- checks and data" to a step of the run, so an
install button there is red, and one placed elsewhere is code kept for
one use. The command is in the sentence Tony would read anyway, the
day the library goes missing. The same command mends a wrong version.

### 6. A night when npm cannot be reached (the question for Tony)

As the run's header has it today, the walk rows would be UNREACHABLE
and UNREACHABLE is red at night: the night commits nothing, the site
keeps the previous night's data, and the next night tries again.

That sits badly with L-485's R4. Tony's words: "the other failure points
are beyond our control and should be reported but not halt the rest of
the run or future runs", and R4 names "an outside library's address
failing". Every row would still run, but one outside failure would stop
the night's data. (The night already has this exposure today: its
`pip install` step stops the whole job if PyPI cannot be reached. Not
in this build.)

- A. Keep the header's rule: red, nothing committed. Nothing new to
  build. Loud in the Actions tab and the dashboard's last-run line.
- B. R4's way, and the loudest report that fits it: the install step is
  allowed to fail and says so to the night's step. Then the walk rows
  print "NOT RUN TONIGHT: npm could not be reached" and are reported,
  not red; the night commits, and its commit title STARTS "WALKS NOT
  RUN: npm unreachable", every night it lasts, where Tony reads titles
  (as a held body's name is). Any other cause (the library missing on
  a computer that installed it, a wrong version, Node missing) stays
  red. Costs one line in the workflow, one exit code, and the title's
  words from the Daily Run, their one home.
- RECOMMENDED: B. A night that cannot fetch the walks' library still
  runs every other check of the page, and the night never changes the
  page's code, only its data.

### 7. The time added, and the run's order

About 70 to 80 seconds a run: the drawer walk 53 s and its planted page
13 s, the clock walk 4 s, the scenes about 5 s; the clock walk's
planted page is not measured yet (a few seconds, by its size). Nothing
in the run's order needs to change. At night the checkers run after
the build, so the walks walk that night's served data, which is the
point.

### 8. Tony's two pushes, and once afterwards

- Website first, then the orrery, in one sitting. Neither is red
  between them: the website's run reads nothing of the dashboard, and
  the orrery's Dashboard parity reads Tony's own website folder, which
  will already hold the rows; the orrery's night skips Dashboard parity.
- Once, after both: the install command above, in PowerShell (what it
  does: downloads the library, 1,419 files, about 15 MB, into that one
  folder; what could go wrong: npm not found, said in its own words);
  then the dashboard's Drawer Walk and Clock Walk buttons, then his
  maintenance runs. Until the install, his website run shows the two
  rows UNREACHABLE, neither pass nor fail by day, each naming the
  command.

### 9. The planted faults, by name

Each is a copy of `interactive.html` in a temporary folder, with one
exact line changed; the tool refuses (FAIL) if the line is not found
exactly once, so a fault that could not be planted never reads as
caught. The planted walk must exit red, and the check must be the one
named, or the row FAILS as "cannot fail".
- Drawer walk: AN ENDED MISSION'S LAST DAY ONE DAY EARLY, Nov 21's kind
  of fault (`solarSystemMissionEndDay` gives the day before
  `mission_end`). Measured: 7 of 66 red, section 42b, every ended
  mission (Pioneer 10, Pioneer 11, Galileo, Cassini, Rosetta, Akatsuki,
  DART).
- Clock walk: THE FREEZE THAT NEVER ANSWERS (`?freeze=1` read as if it
  were "0"), in the solar-system room. Expected red: the frozen step's
  EPOCH_ISO and its "the last day our data covers". Not yet measured:
  the clock walk takes no planted page today. The build adds an
  optional fifth argument handed to the harness's own `{page}`, as the
  drawer walk's third does; what it checks does not change.

### 10. Part 2, on the go-ahead

- Website: `tools/headless/run_walk.py` (new); the two rows and the
  `"walk"` kind in `gallery_maintenance_run.py`, its header's THREE
  STATES saying so; the planted-page argument in `walk_scene_moment.js`;
  the headers of both walks and `page_harness.js` (they now run in the
  run and on the dashboard, not "Claude-only"); the install step in
  `.github/workflows/nightly.yml`; and, if B, the night's title words in
  `daily_run.py` with `CACHE_BUILDER_AS_BUILT.md`'s The Daily Run's
  Steps. `INTERACTIVE_AS_BUILT.md`'s The headless recipe, its opening
  and its walk bullet replaced (it says "the maintenance run does not").
- Orrery: the two buttons and their lines in `palomas_orrery_dashboard.py`.
- Each check shown three ways: PASS with the library (the scratch one,
  by setting `WALKS_LIBRARY` from the test's own call, so the code keeps
  one place), UNREACHABLE without it by day and under `--night`, FAIL
  on its planted page. agentic-pre-test on a throwaway copy. Both
  maintenance runs whole, and Dashboard parity's count.
- interactive-exhibit's rule, proposed here and written only on the
  go-ahead, in the same length (the skill is at its cap, 738):

  A SESSION THAT CHANGES THE PAGE READS THE WALKS (v1.46, L-545; Tony,
  2026-11-21: "should this be method?"; 2026-11-26: "Option 3 and add
  it to the dashboard"). The drawer walk and the clock walk are rows of
  the gallery run, `Drawer walk` and `Clock walk`
  (`tools/headless/run_walk.py`), at night and on Tony's computer, each
  with its dashboard button; each makes its scenes at the run's minute
  and shows its planted fault caught. Their library, jsdom 24.1.3, is
  `WALKS_LIBRARY`, outside OneDrive and both repositories; missing, the
  row is UNREACHABLE and names its install command. After a change to
  `interactive.html` or a script it loads, the closing report gives
  both rows' counts and any red check by name, from the gallery run on
  a copy holding only what a push carries (L-543). The other walks stay
  a session's job. A NEW GALLERY-RUN ROW NEEDS A DASHBOARD BUTTON in
  the orrery, which a website session may not edit: the brief says who
  adds it, and the closing report names it as owed (L-550).

Written November 2026 with Anthropic's Claude Opus 5.5.
