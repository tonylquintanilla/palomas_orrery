<!-- Doc-Kind: hand | Brief for one Claude Code session in the website repository: a craft orbiting a planet is served points fine enough that its box never claims a smaller error than its real miss, on every date the date box offers (L-538). -->
# Brief: the orbiters' printed error (L-538)

Built on gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
orrery 2634031c19ff78e591ebbdc1d724ff4f0d494484 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written November 23, 2026 by the coordinating session (Claude Fable
5.2) for ONE Claude Code session in the WEBSITE repository. The orrery
is touched only for the closing records.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Read before building, and say back which you read, with each skill's
version line: the website's CLAUDE.md and the files it points to; the
skills `gallery-cache-builder` (A Spacecraft Is Fetched by Its Plan; A
Lagrange Point Is Served as a Point; A Served Number That Changes on
Purpose; Every Question Is Asked of JPL, Fresh; the three-layer gate),
`gallery-assembler` (the golden artifact process),
`horizons-orbital-mechanics` (How a Path's Events Are Found, with the
orbiter rule), `provenance-discipline` (A Computed Position Prints
What Its Errors Earn), `orrery-coding-conventions` (the six consumers
of position data), `agentic-pre-test`, `safe-file-editing` and
`ledger-and-session-records` (the closing records). Then this brief,
and L-538 (the orbiters' printed error) and L-297 (the Lagrange
points) in LEDGER_CONSOLIDATED.md.

## 1. The rulings

Tony, November 19, 2026 (L-538): no stopgap. A coarser figure in those
boxes until the fix was offered and not taken; "Yes" to the real fix,
soon.

Tony, November 23, 2026, 23:38, to the coordinating session's question
whether the fix is daily points across the whole date window plus
hourly points around today, or hourly points around today alone: "What
is your recommendation?" The recommendation given: "Daily points
across the whole date window, plus hourly points around today", with
one rule as method, in the session's words: "when the night check
finds an hour too coarse for a craft, the builder halves the step for
that craft, down to a floor, and comes to you only if the floor still
fails." Tony, 23:39: "Yes".

One thing in section 3 goes past those words and is the coordinating
session's reading, told to Tony after his "Yes": the same finer-step
rule is applied to the daily part, not only to the hourly band,
because the measurement in section 2 says a day will be too coarse on
some days.

## 2. What was found at gallery 9e7bb99f (read it; do not trust this list)

Read from the served cache built 2026-11-24T00:01 UTC
(`data/solar-system/`), `data/objects_config.json`,
`tools/gallery_cache_builder.py`, `tools/test_curve_error.py` and
`gallery/assembler/render_spacecraft.py`.

- WHO IS IN A CAPTURE. Eight plans carry an arrival that stays, none a
  departure: Juno (Jupiter, 2016-07-05), BepiColombo (Mercury,
  2026-11-21 18:48, 3,073.0 km), Clipper (Jupiter, 2030-04-11),
  ESCAPADE-Blue and ESCAPADE-Gold (Mars, 2027-09-09 and 2027-09-07),
  and three ended missions, Galileo, Cassini and Akatsuki. So two are
  in a capture inside today's date window: Juno and BepiColombo.
  BepiColombo's arrival is two days old; L-538's figures of Nov 19 for
  it were taken before it.
- THE DATE WINDOW. `coverage_index.json`'s served_window, JD 2461280.53
  to 2461456.47, about 176 days. `interactive.html` has a date input
  (`id="date-input"`), so a visitor can show any day in it.
- JUNO'S POINTS ARE NOT A WEEK APART. L-538 says so; the file says
  otherwise. Of its 289 served points, 32 lie in the window: a daily
  run of 28, JD 2461342.5 to 2461369.5 (the nightly tail, kept until
  the plan is made again), and four single points. With the two just
  outside the window the single points stand at 2461274.5, 2461323.5,
  2461372.5, 2461393.5, 2461442.5 and 2461456.5: gaps of 49, 19, 3, 21,
  49 and 14 days. The 7-day backbone is thinned at 0.02 AU
  (`douglas_peucker`, `fetch_path_by_plan`), and Juno's loop around
  Jupiter is small enough to be thinned away.
- THE MISS, MEASURED. Each served point in the window held out and
  worked out from the rest by `position_at` with the figure the box
  prints (curve=False), as `tools/test_curve_error.py`'s `held_out`
  does. Juno, 6 of 32 missed by more than the figure:
    JD 2461393.5  miss 4,780,840 km  figure 1,234,320 km  (3.9)
    JD 2461323.5  miss 4,409,146 km  figure 1,590,655 km  (2.8)
    JD 2461357.5  miss   385,224 km  figure   170,258 km  (2.3)
    JD 2461442.5  miss 8,292,035 km  figure 3,775,987 km  (2.2)
    JD 2461358.5  miss   584,820 km  figure   467,098 km  (1.3)
    JD 2461359.5  miss   602,788 km  figure   491,989 km  (1.2)
  The three of JD 2461357.5 to 2461359.5 are inside the daily run, so
  a point a day, held out, was too coarse on those days. BepiColombo, 1
  of 294: JD 2461408.5, miss 5,780 km, figure 847 km (6.8). Holding a
  point out doubles the spacing around it, so each is harder than a
  real minute; it is the measure L-538 and L-297 use.
- HOW A PATH'S POINTS ARE KEPT. `points.update(new)` in the spacecraft
  branch (near line 1499): the saved points keep every tail day until
  the plan is made again, when they are cleared and the whole path is
  fetched (`fetch_path_by_plan`), the tail merged after the thinning.
  An hourly band merged the same way would pile up, 24 points a day,
  until the next plan.
- THE WINDOW IS KNOWN LATE. A Lagrange point is fetched last, once the
  window is known (`point_window`, `process_point`), and never takes
  part in it. A path body is fetched before that and has no window.
- THE PATTERN TO FOLLOW is the Lagrange points' (`POINT_*`,
  `point_near_span`, `process_point`, the served `point` block with its
  `near`, the validator's `point_problems`): a day apart across the
  window and a day past each edge, an hour apart from yesterday 00:00
  UTC to the end of the day after tomorrow.
- WHERE THE ERROR IS MADE AND READ. `render_spacecraft.position_at`
  makes it (the room runs this Python in the page); it reaches the box
  as `interp_err_km`, read at three places in `interactive.html` and in
  `gallery/solar_system_figures.js`. `CURVE_KINDS` keeps the curve's
  figure off for spacecraft, by Tony's ruling of Nov 19.
- THE CHECK. `tools/test_curve_error.py` is the gallery run's gating
  row "Curve error". It holds only the Lagrange points and the comets
  on open paths: 3,035 points across 21 files on this cache, worst miss
  0.54 of the figure. `kinds()` already names spacecraft; `main` does
  not hold them.

## 3. What to build

The outcomes, which are Tony's ruling:
1. For a craft inside a capture, on every day the date box offers, the
   box's error is never smaller than the real miss, as the held-out
   measure finds it.
2. Such a craft is served a point a day across the whole date window,
   unthinned, and a point an hour apart from yesterday to the day after
   tomorrow.
3. Where a day or an hour is too coarse, the builder asks a finer step
   there, down to a floor. Only a craft that still fails at the floor
   comes to Tony, by name.
4. No stopgap and no typed figure. The error stays worked out from
   served points.
5. Nothing else moves. Every other served file (a craft not in a
   capture, a comet, a Lagrange point, every orbit) is compared before
   and after, by name, with only what a night moves moved.

How, which is yours to propose in Part A. These are the coordinating
session's starting points, not rulings:
- WHO IS IN A CAPTURE is read from the plan the entry already carries
  (an arrival, and no departure before the day asked), never a typed
  list of names. The build prints who it found, by name, and the body
  each is captured by. A craft whose arrival falls inside the window
  gets the fine points from its arrival on. An ended mission's span
  ended before the window, so it gets none; say what the room shows for
  one and confirm no box works out a figure between its old points.
- THE FINER STEP is found by the measure itself: hold out each new
  point, and where the miss is larger than the figure ask that stretch
  again at a finer step, until none is. Propose the steps (the plan's
  own events use 1h, 30m, 5m, 1m), the floor, and a limit on points and
  on questions to JPL for one craft in one night. A craft that reaches
  the limit is named and fails as the builder's other named failures
  do; say which (served last-good, or held).
- YESTERDAY'S HOURS. Say what the saved points keep once a day has left
  the hourly band, and once it has left the window, so neither the
  served file nor the raw archive grows by 24 points a day.
- THE ORDER. The fine points need the window, which is known after the
  path bodies are fetched today. Say where the fetch goes, and show a
  capture craft cannot narrow the window.
- THE SERVED BLOCK. A capture craft's served entry says what it was
  served by (the step, the window, the hourly band, the finer
  stretches), as a point's `point` block does, so the validator can
  refuse a missing day or hour by name.
- THE CHECK IS WIDENED, not copied: "Curve error" holds every capture
  craft, with the figure its box prints, across the window. Its line
  names the craft held and how many points. A capture craft with no
  fine points is a failure, not a skip.
- THE FIGURE. Keep the chord figure for spacecraft. Report the curve's
  figure beside it on the new points. If only the curve's holds, do not
  switch: that is Tony's ruling of Nov 19 to revisit, and it is the one
  question of your Part A report.

PART A, no edits. Map every place a path's points are fetched, merged,
thinned, gated (the shrink gate, the sanity bound, Guard), validated,
served and read, in the builder, the room and the checks, and name the
six consumers of position data with what each reads of a path. Then
measure, live against JPL, for Juno and BepiColombo: a point a day
across the window and an hour apart in the band; each held out; the
days and hours that fail, by date; the finer steps that cure them; the
points, bytes, questions and seconds it costs. Measure BepiColombo's
loop around Mercury from JPL's own points at the start, the middle and
the end of its span (to 2027-04-10): the time between two nearest
approaches. The coordinating session expects it to shorten to a few
hours, from memory, not checked; the floor has to stand for that day.
Then your proposal for each starting point above. Stop with that
report. Tony carries it to the coordinating session.

PART B, after the go-ahead. The builder, the validator, the offline
suite and the widened check. Each new check is shown able to fail, by
a planted fault caught by name: a capture craft missing a day in the
window; missing an hour in the band; a figure smaller than its miss; a
craft with an arrival and no departure that the build did not treat as
captured; a craft past its departure treated as captured; a craft at
the limit; yesterday's hours still served. `agentic-pre-test` before
any file is called done. Stop with a report and wait for the go-ahead.

PART C. A whole build on a throwaway copy, the served files compared
before and after by name (outcome 5). `gallery_maintenance_run.py`
whole, read green from its output, the rows that could not run named.
What Tony looks at on his phone, written before he looks: the Solar
System room, Juno's box and BepiColombo's box, today and on one other
day in the window, with what each read before and what it should read
now. His look is the gate. Then the closing records and the report.

NOT IN THIS SESSION.
- Any skill file. List on L-538 the rules you learned, in plain
  sentences, and name in the report what `gallery-cache-builder` should
  say. It stands at its cap, 944 of 944 lines, and its split has not
  been put to Tony; the coordinating session writes the bump.
- The box's words, and which figure it prints.
- The orrery's code, and `path_plan.py`. If the plan lacks something
  the build needs, stop and say what.
- Every path to its last day (L-533 (ESCAPADE)), the next build, its
  own. The clock items left open on L-541 (a plan's clock).
- A wider date window. Days outside it, for an ended mission or any
  other, are noted on L-538 if you find a box that can show one.

## 4. Delivery

- Work in the website repository, through the python_work door. Record
  both bases (`git rev-parse HEAD`, `git ls-remote origin HEAD`, each
  repository). A night commits under data/ every day, so a base may be
  a descendant of the ones above; stop only if a file named in section
  2 is not as described, and name what moved.
- Edit the files in Tony's working copy, ASCII and LF, each change
  stamped where it is made. Tony commits and pushes. Nothing is pushed
  by the session.
- The closing records go to the orrery: L-538 on
  `LEDGER_CONSOLIDATED.md`, Where We Are edited by section, the run's
  tools after them. Tony's run order names the two repositories apart.
- After Tony's push, the website's next night is the proof on GitHub's
  machine. Say in the report what its "Curve error" row should read,
  with the craft named.

## 5. The report

Plain words, in this order: what was built, file by file; who is in a
capture, by name; the measure before and after, with the worst day
named for each craft; the cost (points, bytes, questions, seconds);
the served files compared; the gallery run's rows by name; what Tony
looks at on his phone; what Tony does next; the skill text owed;
anything this brief got wrong. It opens with the anchor line: built on
<base SHA> at each repository's URL; ready at <new SHA or "not
pushed">. It ends with the session's token count as Claude Code's
/cost prints it (Token Economy).

Written November 2026 with Anthropic's Claude Fable 5.2.
