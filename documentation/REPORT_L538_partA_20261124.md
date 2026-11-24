<!-- Doc-Kind: hand | Part A report of the L-538 brief (the orbiters' printed error): the map of a path's points, the live measure for Juno and BepiColombo, and the proposal. No code was changed. -->
# L-538 (the orbiters' printed error): Part A report

Built on 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); ready
at "not pushed" (no code changed; this file is the only new one).
Written November 24, 2026 by one Claude Code session (Claude Opus 5.5)
working from documentation/COORD_L538_orbiters_brief_20261123.md.

## The claim

The fix works as designed for Juno and needs one more test for
BepiColombo: holding out served points is not enough for a craft whose
loop is shorter than its step, so the builder must also compare the box
with JPL's own points between the served ones. With both tests, both
boxes are honest on every day of the window, no day comes near the
1-minute floor, and the cost is BepiColombo's file growing about four
to six times.

## Bases and what was read

- Website: HEAD 9e7bb99f, equal to GitHub's, nothing waiting; the brief's
  base exactly. Orrery: HEAD 6a42ab3b, equal to GitHub's; descends from
  the brief's 2634031c by two records commits ("L538 design" and a run
  record). One edit waiting: Tony's own run record of this session
  (WHERE_WE_ARE_11-24-26_0835_run_record.md, the pushed SHA written in).
  Nothing named in the brief's section 2 had moved.
- Rules: the website's CLAUDE.md, the protocol v4.0
  (PROJECT_INSTRUCTIONS.md).
- Skills, the repository's copies, in the parts the brief names:
  gallery-cache-builder 1.21 (A Spacecraft Is Fetched by Its Plan; A
  Lagrange Point Is Served as a Point; A Served Number That Changes on
  Purpose; Every Question Is Asked of JPL, Fresh; the three-layer gate;
  also A Body That Fails Its Test Is Held, Validation stance);
  gallery-assembler 1.5 (Golden artifact process);
  horizons-orbital-mechanics 1.20 (How a Path's Events Are Found, with
  the orbiter rule); provenance-discipline 2.37 (A Computed Position
  Prints What Its Errors Earn); orrery-coding-conventions 1.14 (the six
  consumers); agentic-pre-test 1.4 (the Standard Test and the throwaway
  rule). safe-file-editing 1.15 and ledger-and-session-records 1.24:
  their version lines only; they govern Part B's edits and the closing
  records, and Part A made neither.
- Ledger: L-538 whole; L-297 (the Lagrange points), its Session 2 notes.

## 1. The map: where a path's points go

All in the website repository.

FETCHED (tools/gallery_cache_builder.py)
- `process_object`, the spacecraft branch (about line 1478): a new plan
  clears the saved points and asks the whole path, `fetch_path_by_plan`
  (line 1643): the backbone at 7 days across the span, the events'
  windows at their own steps, the daily tail, an ended mission's last
  day. Otherwise `fetch_path_tail` (line 1629): daily, from the freeze
  window before today to 2 days after.
- `fetch_vectors_range` (line 507): every question, keyed to the minute
  for a path (`MINUTE_KEY`), `cache=HORIZONS_CACHE` (False).
MERGED
- `points.update(new)` (line 1499): every tail day kept until the plan is
  made again; then cleared.
THINNED
- `douglas_peucker` (line 1704): the backbone at 0.02 AU, each event's
  window at 1% of its passing distance. This is what thinned Juno's
  loop away.
GATED
- The shrink gate, `shrink_gate` (line 2867): counts the raw archive's
  points per body and in all; a re-planned path is held out of the
  count, named.
- The sanity bound and Guard v2, `guard_monitor` (line 1178): a path is
  only checked for 0 < r < 1,000 AU and time increasing; warn and keep.
- No hold: a path is never held (L-525); a failed fetch serves last-good,
  `serve_last_good` (line 1760), today's point nulled.
VALIDATED
- `assert_structural` (line 2780): #2, a path has positions and no
  elements; #8, #B3, #T as for every body. `point_problems` (line 2269),
  #L, is the pattern for a check by name (a missing day, a missing hour).
SERVED
- `build_position_file` (line 1351): the whole raw archive becomes
  positions/<slug>.json, km about the Sun, Julian dates on JPL's clock.
- The window: `served_window_from` (line 2085), about 88 days either
  side of the build's minute, set only by Sun-centred bodies drawn from
  elements; `point_window` (line 2119) hands it to the late fetches.
READ
- gallery/assembler/render_spacecraft.py: `position_at` (line 169) puts
  the marker on the parabola through the three nearest points and makes
  the error (chord, or curve for `CURVE_KINDS`); `build_spacecraft_traces`
  hands it on as `interp_err_km`.
- interactive.html: the spacecraft's box, line 4618
  (`SolarSystemFigures.pathDistanceLine`, the distance from the Sun to
  the place the error earns); a Lagrange point's two boxes, lines 4469
  and 4570 (`pointBox`). gallery/solar_system_figures.js does the
  rounding (`pathDistanceLine`, line 353; whole kilometres at finest).
CHECKED
- tools/test_curve_error.py, the gallery run's gating row "Curve error":
  today it holds only the Lagrange points and the comets on open paths.
- tools/test_gallery_cache_builder_offline.py, the builder's suite.
- Readers of the served positions that Part C must compare:
  tools/check_cache_in_step.py, tools/test_served_list.py,
  documentation/smoke_solar_system_figures.js and
  documentation/smoke_hover_budget.js among the 34 files that read the
  served cache.

THE SIX CONSUMERS of position data, and what each reads of a path:
1. Static plot, `plot_objects` (orrery, palomas_orrery.py): asks JPL
   itself; reads nothing the website serves. Untouched.
2. Animation, `animate_objects` (orrery): the same. Untouched.
3. Social export, `export_social_view` (orrery): the same. Untouched.
4. Gallery curation, tools/gallery_studio.py (website): curates the
   orrery's exported pictures; does not read the served cache (grep).
5. JSON conversion, tools/json_converter.py (website): converts those
   pictures; does not read the served cache (grep).
6. The website's rooms: the builder, then gallery/assembler/ (cache_reader,
   resolver, render_spacecraft), then interactive.html. The only one
   that reads a path's served points, and the only one this fix touches.

## 2. Who is in a capture

Read from each plan's events (an arrival that stays, no departure),
against the window JD 2461280.53 to 2461456.47 (2026-08-28 to
2027-02-19):
- Juno, by Jupiter, since 2016-07-05. In a capture all window.
- BepiColombo, by Mercury, since 2026-11-21 18:48. JPL serves it as
  "MPO-BepiColombo". In a capture from its arrival day on.
- Not in one inside the window: Europa Clipper (Jupiter, 2030-04-11),
  ESCAPADE-Blue and -Gold (Mars, 2027-09-09 and 09-07; the window reaches
  them about June 2027), and the ended Galileo, Cassini and Akatsuki,
  whose spans end before the window.
- An ended mission on a day in the window: `position_at` finds no
  bracket after the span's end, so the room draws it ended, the marker on
  its last served point, `interp_err_km` 0, and the box prints that
  point's own distance to whole kilometres. No box works out a figure
  between its old points.

## 3. The measure, live against JPL (November 24, 2026)

Method: the builder's own `fetch_vectors_range`, a point a day across
the window and a day past each edge (from the arrival day on), and an
hour apart from 2026-11-23 00:00 to 2026-11-27 00:00 UTC. Two tests:
HELD OUT, each served point in the window held out and worked out from
the rest by `position_at` with the figure the box prints (curve=False);
and THE REAL MINUTE, the box's figure at minutes between served points
against JPL's own points there (asked off the grid: every 37 minutes
across the span, every 3 hours offset 97 minutes, every 7 minutes in the
band, and every minute for two days in January and April). Scratch
scripts, not deliverables, in the session's scratchpad
(measure_l538.py, step_test.py, loop_bepi.py).

JUNO
- Before (today's served file): 6 of 32 held out over the figure, worst
  3.9 times, 2026-12-19.
- A point a day: 16 of 267 over, worst 3.3 times, 2027-01-18. They fall
  in threes on six days a loop apart, Juno's closest passes of Jupiter:
  2026-09-09, 10-11/12, 11-13, 12-16, 2027-01-17/18, 02-19.
- The hourly band passed at once.
- Halving those days' steps cured them at 45 minutes, in five rounds.
  After: none over; worst 0.98, 2027-02-19 15:00. Real minutes: none of
  6,848 (every 37 minutes) nor of 1,408 (every 3 hours) over; worst
  0.59, 2026-10-11 22:38 (miss 2,847 km, figure 4,795 km).
- Cost: 636 served points (was 289), about 48 KB (was 22 KB); 35
  questions to JPL, 14 seconds.

BEPICOLOMBO
- Before: 1 of 294 held out over, 6.8 times, 2027-01-03.
- A point a day: held out, NONE over. But at real minutes, 56 of 728
  (every 3 hours) were over, up to 2.0 times (2026-12-28 22:38, miss
  10,786 km, figure 5,390 km). Its loop around Mercury is shorter than a
  day, and points at the same hour each day cannot see it, nor can
  holding one of them out.
- The hourly band: 4 over (2026-11-24 05:00 to 06:00 and 2026-11-26
  15:00 to 16:00, up to 1.5 times, its closest passes); cured at 30
  minutes.
- Driven by both tests, the steps settled at 15 minutes on every day
  from 2026-11-27 to 2027-02-19 (with 45 and 90 minutes between its
  passes), coarser in the days after the arrival while the loop was a
  day long. After: none over, held out or at any of 3,541 real minutes;
  worst at real minutes 0.78 (2026-11-21 19:38, the arrival day) and
  0.91 in the band.
- Every minute for two days: at a 30-minute step the box holds on
  2027-01-20 (worst 0.90) and 2027-04-06 (0.93); at 45 minutes it does
  not (1.27 and 1.43). The held-out test asks for 15, which doubles to
  30 when a point is held out. So 15 minutes holds to the end of JPL's
  data, and the 1-minute floor is never near.
- Cost: 6,179 served points (was 1,517), about 472 KB (was 115 KB),
  refined stretch by stretch. My scratch script asked each stretch
  separately, 557 questions and 175 seconds; a builder asking a day's
  run in one question would ask far fewer (not measured). Refined day by
  day instead (each day at the finest step any of its stretches needed),
  about 9,700 points and 740 KB (worked out from the measured steps, not
  run).

BEPICOLOMBO'S LOOP AROUND MERCURY, from JPL's own points around Mercury's
centre: 28 hours just after arrival (2026-11-26 to 11-28, 3,062 to
55,341 km), 4.40 hours by 2027-01-20 (2,995 to 7,379 km), 2.37 hours by
2027-04-06 (2,904 to 3,955 km). The coordinating session's "a few hours"
was right.

ONE MORE THING THE MEASURE FOUND: the served file's own points inside
the fine span must not be mixed with the fresh ones. BepiColombo's file
still holds the arrival as predicted by the plan of November 4; next to
JPL's answer of today the two disagree by thousands of kilometres within
a minute. So inside the span the fresh points replace the old ones.

THE FIGURE: the chord figure (the one the box prints) holds everywhere
after the fix. The curve's figure does not: BepiColombo 6 held out and 4
real minutes under it, Juno 12 band minutes under it by less than a
kilometre. So the chord stays, and Tony's ruling of November 19 has
nothing to revisit.

## 4. The proposal, starting point by starting point

WHO IS IN A CAPTURE. One function, shared by the builder, the validator
and the check: from the plan's events, captured from the last arrival's
closest moment to the next departure's, or to the span's end when it
stays. The fine span is that, clipped to a day before the window to a
day after, from the arrival's day at 00:00 UTC. Not empty means a capture
craft. The build prints each by name with its body: "CAPTURE: Juno by
Jupiter since 2016-07-05; BepiColombo by Mercury since 2026-11-21".

THE FINER STEP. Day by day. Every day of the fine span starts at a day,
the band's at an hour. Each round runs both tests: every served point
held out, and JPL's own check points, one question every 37 minutes
across the span. A day with a miss larger than its figure is asked again
at the next rung: 1 day, 12 h, 6 h, 3 h, 90 min, 45 min, 15 min, 5 min,
1 min. Each rung divides the one above, so new points fall on the old
ones' minutes and never a few seconds off them (the measure tripped on
that once). The floor is 1 minute, the finest the minute keys can hold.
The limit for one craft in one night: 12,000 fine points and 60
questions. A craft at the floor or the limit fails by name and is served
its saved fine layer of the night before (last-good, as a path is; a
path is never held). If it has none, it is served without, and the
widened check turns the night red, so nothing is committed and the site
keeps yesterday's cache.

YESTERDAY'S HOURS. The fine layer is kept in the raw archive apart from
the plan's points and replaced whole each night, never merged. An hour
that left the band and a day that left the window are simply not asked
again. Inside the fine span the served file holds only the fine layer;
outside it, the plan's points as now. So the file's size follows the
window, and the archive does not grow by 24 points a day. The tail's
daily points stay as now, one a day until the next plan. The shrink gate
keeps counting the plan's points; the fine layer is counted by the new
validator check instead, day by day, because a Juno pass leaving the
window drops about 40 points in a night, and the 95% gate would stop it.

THE ORDER. A pass right after `point_window` (the window known, before
the Lagrange points) over the results that are capture craft: fetch the
fine layer, refine it, rebuild the positions file, add the served block.
It cannot narrow the window: `served_window_from` takes only Sun-centred
bodies with a measured trust window; a spacecraft is `arc-natural` and
has none, and this pass runs after the window is set. Proposed: an
explicit path-body skip there, as a Lagrange point has, with a planted
fault (a capture craft given the Sun's frame and a short window must not
narrow the site's window).

THE SERVED BLOCK. A `capture` block on the craft's served entry: its
body, arrival and departure (or none), the fine span, the band, the step
of each day (for example "2026-11-27": "15m"), the counts of points held
out and check points, the worst ratio, and last_good. A new validator
check refuses, by name: a capture craft with no block; a day in the
window with no point at its 00:00 or served coarser than its step; a
missing hour in the band; a plan point served inside the fine span; a
block on a craft that is not in a capture (past its departure).

THE CHECK, WIDENED. "Curve error" holds every capture craft by the same
capture function, with the figure the box prints, across the window, in
two parts: its served points held out, and the JPL check points the
builder saved beside the raw archive (not served). Its line names each
craft with both counts. A capture craft with no fine points is a
failure. Self-test: the same craft thinned to a point a day must fail;
for BepiColombo only the check points can catch it, which proves they are
read.

THE FIGURE. The chord figure stays; the curve's is reported beside it in
the build's record. Nothing to switch.

## 5. What the brief got wrong

- Outcome 1 says "as the held-out measure finds it". For BepiColombo
  that measure passes with a point a day while the box is wrong at real
  minutes by up to twice its figure. The outcome needs "and at JPL's own
  points between them".
- Juno's daily misses are not spread through the window; they come on
  its closest passes of Jupiter, about one a month.
- Not wrong, but new: from about 2027-01-12 the window will include days
  after 2027-04-10, the end of JPL's data for BepiColombo. On those days
  its box would read "This mission ended on ...", which is false. That is
  the box's words, not this session's; for L-538's notes.

## 6. The one question

BepiColombo's box can be made honest at about 470 KB refined stretch by
stretch, or about 740 KB refined day by day (today: 115 KB). I recommend
day by day, because the validator can then name each day's step and the
night asks fewer questions. Is a file of about three quarters of a
megabyte, loaded on a phone and committed every night, acceptable?

## Where this leaves us

No code changed. Part B waits for the coordinating session's go-ahead on
this proposal.

One final thought: every night's commit will carry the whole fine layer
again, about half a megabyte more for BepiColombo; worth measuring in
Part C against the repository's 84 MB before it is taken as cheap.

Written November 2026 with Anthropic's Claude Opus 5.5.
