<!-- Doc-Kind: hand | L-512 part 2's map, by test: what the desktop orrery draws today when JPL cannot answer, what data/orbit_paths.json holds and whether it matches JPL, and the rulings Tony is asked for before part 2 is built. No code was changed for this map. -->
# Map: what the orrery draws when JPL cannot answer (L-512, part 2)

Tony Quintanilla, PE | Claude Opus 5.5 (Claude Code session) | November 4, 2026, afternoon, Chicago

Built on orrery 3fb14c269f215c57cfcb9bd7b6973589eef857ea at
https://github.com/tonylquintanilla/palomas_orrery, plus this session's
uncommitted part 1 (path_or_orbit.py, test_path_or_orbit.py,
idealized_orbits.py, palomas_orrery.py), and gallery
5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (not
touched). Brief: `COORD_L512_jpl_fallbacks_brief_20261104.md`, section 4.

## How it was tested

- A throwaway copy of the folder's code and `data/*.json` (outside the
  repository). The orrery's own code ran unedited; only the test
  harness around it was patched: no window shown, the plot thread run in
  place, the figure captured instead of opened, and the two cache
  dialogs answered "No" ("Update Orbital Elements?" and "Update Orbit
  Data?": the saved paths were not updated).
- JPL unreachable: every web request sent to a closed local port, so
  each JPL question failed the way a dropped connection does
  ("Max retries exceeded ... Unable to connect to proxy"). The same run
  with JPL reachable, for comparison.
- Plotted: Mars, Juno (the spacecraft), Halley and Voyager 1 around the
  Sun, static and animated (one day a frame, 29 frames); Juno around
  Jupiter, static.

## What draws today, JPL reachable against JPL unreachable

| Drawing | JPL reachable | JPL unreachable |
|---|---|---|
| Mars, Halley: the path over the plot's dates (`plot_actual_orbits`, `fetch_trajectory`) | "Actual Orbit", 51 points each | nothing |
| Mars, Halley: the Keplerian orbit and its markers (`idealized_orbits`) | drawn | drawn, from the saved osculating elements (`data/osculating_cache.json`), with no fresh JPL question |
| Juno, Voyager 1 around the Sun: the full mission by its plan (`path_drawing.draw_plan`) | 244 + 30 and 65 + 5 points | nothing; the console says "[PATH PLAN] Voyager 1: not drawn by its plan; JPL gave no path". The plot does not then try any other source |
| Juno, Voyager 1: the plotted period | 51 points each | nothing |
| Every body's position marker (`fetch_position`) | drawn | static plot: no marker, no legend line; animation: a legend line with an empty marker (every frame's x, y, z is None) |
| Juno around Jupiter: the full mission (`fetch_trajectory`) | 51 points | 51 points, drawn: see the next section |
| The comet tails, the CAD close-approach box, Juno's Jupiter-centred osculating orbit | drawn | not drawn; each prints its failure |

The other three of the five consumers (protocol, Check All Parallel
Pipelines) fetch nothing: the social export copies the figure the
static plot or the animation made, and Gallery Studio and the JSON
converter work on saved HTML. They show whatever those two drew.

## A finding: two path questions are not asked fresh

`fetch_trajectory` (palomas_orrery_helpers.py line 385) and
`fetch_orbit_path` (line 598) call astroquery's `vectors()` without
`cache=HORIZONS_CACHE`. Astroquery then hands back its own saved answer
to the same question for a week. That is why Juno around Jupiter drew
with JPL unreachable: its planned span is fixed, so the question was
the same as an earlier run's. Around the Sun the dates move with today,
so the question differs and JPL is asked.

- So "every JPL question asked fresh" (utc_clock.HORIZONS_CACHE False,
  and horizons-orbital-mechanics' Query Mechanics) is not true for the
  plot's two path fetches, and `fetch_orbit_path` is the writer of
  `data/orbit_paths.json`: the saved record can hold a week-old answer.
- The same omission at `spacecraft_encounters.py` lines 637, 672 and
  985 and `comet_visualization_shells.py` line 2114. The orbit-cache
  test's clock check (TestUtcClock) watches ten modules of the data path,
  and palomas_orrery_helpers.py is not among them.

## "No such object" against "no answer"

Asked with JPL reachable for a body JPL does not have (C/2099 Z9, as a
small body), and with JPL unreachable for Mars:

- `fetch_trajectory` returns `[None, None, None]` in both cases.
- `fetch_position` returns `None` in both cases.
- Only the printed text differs: "Unknown target (C/2099 Z9)" against
  "Max retries exceeded ... Unable to connect to proxy". No caller can
  tell the two apart. Any fallback must first be able to, so that "no
  such object" is never answered from saved points (Tony's Oct 31 ruling
  holds an identity).

## The three copies of the analytical fallback list

The same four names in each (MK2, Xiangliu, Vanth, 6AC4721), each with
the same comment, at palomas_orrery.py, as the file stands after part 1:

- `ANALYTICAL_POSITION_FALLBACK`, line 4568, in `plot_actual_orbits`.
- `ANALYTICAL_POSITION_FALLBACK`, line 5961, in the static plot's
  worker (the position marker).
- `ANALYTICAL_ANIMATION_FALLBACK`, line 7062, in the animation's worker.

Whatever part 2 builds reads one list; it adds no fourth copy.

## data/orbit_paths.json, read on a copy

- 137.6 MB; 1,503 entries keyed `<name>_<centre>`; 1,527,707 points;
  dates 1965-10-17 to 2064-12-12. Points per entry: 2 to 24,479,
  median 737. Each point is `{x, y, z}` under a date key `YYYY-MM-DD`.
- Centres: the Sun 164 entries, Earth 137, the Moon 113, Mars 107,
  Jupiter 105, and ten more with about 100 each.
- Metadata: `earliest_date`, `latest_date`, `center_body`,
  `last_updated` (and `start_date`/`end_date` on 165, and
  `converted_from_legacy` on 421). No JPL record number, no time of day.
- Last updated: 978 entries in May 2025, 277 in June 2025, the rest
  spread to Nov 4, 2026. No entry for 6AC4721.

### Do the saved points match JPL's today? Three bodies, eight dates each

Each saved point against JPL's position at 00:00 TDB of its date
(asked fresh on Nov 4, 2026, around the Sun):

- Mars (7,730 points): six of eight equal JPL's to the kilometre. The
  point under 2023-05-07 is 51,511 km off. The point under 2026-05-16
  is 70,254,917 km off, and it equals JPL's Mars of 2026-04-15 to the
  kilometre: filed 31 days late.
- Halley (24,479 points): off by 1 km (2052) to 1,959,174 km (1985).
  The 2023-11-25 point matches JPL's of the next day within 2,022 km:
  filed about a day early.
- Voyager 1 (1,390 points): the four dates from 2025-05 to 2026-12 are
  44 million km off; the 2025-05-13 point matches JPL's of 30 days
  earlier within 365,491 km. The later four are 1.1 to 2.2 million km
  off.

Why: the file does not keep the times JPL answered with. Its writer
(`orbit_data_manager.fetch_orbit_path_by_dates`) spreads the returned
points evenly from the start date it asked for to the end date, and
files each one under the day of its spread time (lines 913 to 933). When
JPL returns fewer points or another span than was asked (a clipped
ephemeris, a step that does not divide the span), every point after
that is filed under the wrong day. A step under a day files four points
under one date, and the last one wins. A merge then mixes those with
points from other fetches.

So the file holds JPL's positions, but not reliably at the dates it
files them under. Drawn as a path's shape, much of it would look right.
Drawn as "the body on this date", it can be a month wrong.

## Rulings asked before part 2 (brief, section 5), each with a recommendation

The map adds one question in front of the brief's six (0).

0. The saved file's dates. Recommended: the writer starts keeping JPL's
   own time for each point (the answer's `datetime_jd`), the record it
   came from, and asks with `cache=HORIZONS_CACHE`; and no entry written
   before that is drawn, since its dates cannot be trusted (Mars filed
   31 days late, Voyager 1 about 30). The fallback then starts empty and
   fills as plots run.
1. When the saved points are used. Recommended: only when JPL cannot be
   reached, never to spare a question. And JPL answering "no such
   object" is not a failure to reach it, so part 2 first teaches the
   fetch to tell the two apart (above, they look the same today).
2. How a fallback drawing says so. Recommended: a hover line naming the
   source and the day the points were fetched, a console line, and a
   dashed line, so that it reads as "not today's answer" at a glance.
3. The guard. Recommended: the file records which JPL record each path
   came from, and a saved path whose record differs from the entry's
   today is refused by name, never drawn. Entries saved before the guard
   are refused (this is ruling 0's answer for them).
4. Which drawings fall back. Recommended: the static path over the
   plot's dates first, in this session; the position marker, the
   plan-drawn full mission and the animation each ruled on their own once
   the path works.
5. The record's integrity. Recommended: the maintenance run checks the
   file (that it reads, that each entry has its record and its times,
   counts by centre), and on GitHub's computers, where the file does not
   exist, it reports "no file here" as its own outcome, neither a pass
   nor a failure that stops the night.
6. The third link for a path body (a hyperbolic comet, a spacecraft)
   when JPL and the saved file both fail. Recommended: nothing drawn,
   and the console and the legend say why. The map shows that today such
   a body is silently absent in the static plot.

Written November 4, 2026 with Anthropic's Claude Opus 5.5 (Claude Code
session, L-512).

## Tony's rulings, November 4, 2026, 12:36 to 12:56 Chicago

Taken in the coordinating session (Claude Fable 5.1) over the map
above, one at a time. The coordinating session read, at orrery HEAD
3fb14c26 and gallery HEAD 5abca2c6: osculating_cache_manager.py,
data/osculating_cache.json (137 entries, 79 around the Sun), path_plan.py,
and the gallery's data/solar-system/coverage_index.json (97 objects, 68
with osculating elements, 28 with positions files, served window about
three months each side of today). Code confirms each fact at HEAD before
building on it.

THE OBJECTIVE, in Tony's words (12:44): "a fallback to a JPL outage for
our full complement of objects." The full complement is the orrery's
dictionary (celestial_objects.py, L-395), not the website's served set.

RULING 0, the saved file: DELETE. Tony (12:36): "a heavy file that is
wrong and nobody reads is a bad breadcrumb leading nowhere. I recommend
delete, even as I built it over many months." Three pieces go with it:
- data/orbit_paths.json and its two backups (.backup, .backup_old),
  deleted from Tony's machine by Tony, on Code's run order.
- The writer (orbit_data_manager.update_orbit_paths_incrementally and
  what only it serves) and the "Update Orbit Data?" dialog in
  palomas_orrery.py, removed now: otherwise every plot keeps asking and
  keeps writing a file nobody reads.
- verify_orbit_cache.py and export_orbit_cache.py on the dashboard:
  marked obsolete under L-509's rule, removed when a build next touches
  them.
The map's recommendation (fix the writer, start empty) is not taken.

THE SHAPE: two mechanisms, not one file (accepted 12:51).

1. Propagation from committed elements, for every body that moves on a
   Keplerian orbit (planets, dwarf planets, asteroids, comets below e 1,
   moons around their planet). The store is data/osculating_cache.json,
   already committed and refreshed by the night and by Tony's plots; it
   already holds elements around other centres (Charon@9, Titan@699).
   When JPL cannot be reached, the position marker and the path over the
   plot's dates are propagated along the cached elements, the way the
   website draws its analytic bodies. One propagator in the orrery, used
   for every such body; the four-name lists (ANALYTICAL_POSITION_FALLBACK
   twice, ANALYTICAL_ANIMATION_FALLBACK) go, since the rule now covers
   every body with cached elements. The hover says "propagated from JPL's
   elements of <epoch date>", since the error grows with time from the
   epoch.

2. A committed positions record, for every path body in the orrery's
   dictionary (a spacecraft, or a small body JPL classes at or above
   e 1: today 13 comets), in the orrery repository, written by the
   orrery's own night. Nothing can compute these; they are stored. The
   website keeps its own served files as now; the orrery's record is its
   own because its object set is larger and it carries a daily window
   the website's files do not. Code names the file(s) by the skills'
   conventions.

RULING ON THE RECORD'S SIZE: option B (12:56, "Yes", with the plan's
thinned-and-fine points as its history).
- History: the plan's points exactly as path_plan.py asks and thins
  them: a 7-day backbone thinned where the path runs straight, fine
  steps around each event with the window and step worked out from the
  event's distance and speed (Juno 244 + 30 points, Voyager 1 65 + 5
  with JPL on, Nov 4). Re-asked on the 30-day cycle with the plan, as
  now. A spacecraft around a planet is keyed by that centre, which the
  plan's arrival rule already knows.
- Window: a daily step over the served window (about three months each
  side of today; Code matches the website's window constant), asked
  each night.
- Size: all path bodies together under 10,000 points, well under 1 MB;
  the same shape as the website's positions files, which git has
  carried nightly since October.
- The marker from the record: inside the window, exact to the day;
  outside it, set on the stored path between its two neighbouring
  points, and the hover names the two JPL dates it sits between (up to
  seven days apart on a straight run, hours apart near a flyby).
- The fallback never draws finer than it stored, and says its step.
Options A (a daily step over every mission, about 150,000 points) and C
(the window only, no fallback for the full mission) were declined.

NOTHING ABOVE REACHES: not drawn, and the console and the legend say
why (ruling 6, as recommended). Today such a body is silently absent.

THE OTHER RULINGS:
- 1 (when the saved points are used): as recommended. Only when JPL
  cannot be reached, never to spare a question; and JPL answering "no
  such object" is not a failure to reach it, so part 2 first teaches
  fetch_trajectory and fetch_position to tell the two apart (today
  both return the same None). "No such object" is never answered from
  a store (the Oct 31 ruling holds an identity).
- 2 (how a fallback drawing says so): as recommended: a hover line
  naming the source and its date, a console line, and a dashed line.
- 3 (the guard): the record carries each body's JPL record number as
  the night's existing hold already does; a stored path whose record
  differs from the entry's today is held, by name, not drawn. Nothing
  is stored before the guard exists, so there are no pre-guard entries.
- 4 (which drawings fall back): see the order below.
- 5 (the record's integrity): the Daily Run and the maintenance run
  check the orrery's record as they check the night's other files; on
  GitHub's computers the record exists, since it is committed. The
  "no file here" outcome is no longer needed.
- The fresh switch: a method fix, no ruling needed. cache=HORIZONS_CACHE
  at all six sites the map names (palomas_orrery_helpers.py lines 385
  and 598; spacecraft_encounters.py lines 637, 672 and 985;
  comet_visualization_shells.py line 2114), and palomas_orrery_helpers.py
  added to TestUtcClock so the check can fail next time.

THE ORDER FOR PART 2 (recommended by the coordinating session; Tony
confirms or changes it): each slice ends with Tony's look, wifi off
and on.
  a. The delete (ruling 0) and the fresh switch, with the not-found
     test (ruling 1). Nothing new drawn yet; Mars and Halley still
     keep their orbits with JPL off.
  b. Mechanism 1: the marker and the path by propagation, for orbit
     bodies, static plot first, then the animation. Uses the existing
     store; the night does not change.
  c. Mechanism 2: the night writes the path record (the maintenance
     run's new step, on GitHub's computers and by hand); then the plot
     draws a path body from it with JPL off, static first. Tony's look:
     Voyager 1 and Juno around the Sun, Juno around Jupiter.
Each slice is its own commit and its own run record.
