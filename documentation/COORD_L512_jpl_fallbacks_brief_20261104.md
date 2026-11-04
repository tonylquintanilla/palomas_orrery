<!-- Doc-Kind: hand | Brief for a Claude Code session (design stop, then build): what the desktop orrery draws when JPL cannot answer. The path-or-orbit decision falls back to a body's own cited elements; the saved JPL positions in data/orbit_paths.json become the drawing's fallback, guarded and marked. Orrery only. -->
# Brief: the orrery's fallbacks when JPL cannot answer (L-512)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 4, 2026, morning, Chicago

Built on orrery 190f42c4f2cd46e63393597a159534d6e17c00e1 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (not
touched), both read live on Nov 4, 2026. The code facts below were read
at 83981b09, the L-510 build, which 190f42c4 follows.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for one Claude Code session, opened through the python_work
door, working in the orrery folder. Opus, high effort (a data pipeline
and its integrity, orbital mechanics; `METHOD_MODEL_EFFORT.md`). The
session has ONE STOP, in section 5, for Tony's rulings before part 2 is
built. Its report ends with its token count, or the sizes read and
written if none prints (protocol, Token Economy).

## 1. Why, in Tony's words

Tony, Nov 4, 10:32, on `data/orbit_paths.json`: "this was my
understanding: that this file was our record of fetched data from jpl
and that it was a fallback in the event of a jpl failure." And at
10:34: "i would like to address this gap now. it is an important part
of the pipeline as a fallback and data integrity issue." On 6AC4721,
10:22: "the analytical orbit is not plotted. this could be an issue.
what happens if Horizons is unavailable, i thought that the fallback is
the cache, and if the cache is incomplete the typed elements ... this
is not trivial."

The chain Tony expects, in his order: JPL live, then the saved record
of JPL's answers, then the typed elements. Today the second link does
not exist for drawing, and the decision of path or orbit has no third.

## 2. What is already found (read at 83981b09; confirm at HEAD)

The decision of path or orbit (L-510):
- `path_or_orbit.py` reads JPL's database e from
  `data/small_body_solutions.json`. The plot never asks JPL for it. If
  JPL is down at the 30-day refresh, `period_fetch.py` (near line 430)
  stops asking and keeps every record. So for the 68 bodies on record,
  an outage changes nothing.
- A body with NO record raises `NoSolution` (`_record`, near line 150);
  `drawn_type_or_none` prints the failure and returns None, and the
  body is drawn by neither a plan nor an orbit. 6AC4721 is that case:
  it has no JPL record (`'id': 'none'`), and its elements are typed in
  `orbital_elements.py` (near line 588) from MPEC 2026-A49, e 0.99994.
  Tony keeps it on purpose, as the record of how C/2026 A1 (MAPS) was
  drawn before JPL carried it (Nov 4, 08:50). His plot of Nov 4, 14:33
  UTC (`solar_system_20261104_1433_maps.html`) shows "6AC4721
  Analytical Orbit" with one point: no line. Before L-510 it drew.

The saved positions, `data/orbit_paths.json`:
- Gitignored (`.gitignore` line 11); on Tony's machine only, with two
  backup generations (`.backup`, `.backup_old`), a repair tool
  (`verify_orbit_cache.py`, on the dashboard) and an export
  (`export_orbit_cache.py`). Keyed `f"{name}_{center}"`.
- WRITTEN on every plot that updates it: the static plot's worker
  (palomas_orrery.py, near lines 4985 to 5145) checks whether the file
  covers the GUI's dates, asks Tony whether to update, then
  `orbit_data_manager.update_orbit_paths_incrementally` fetches only the
  missing dates and saves.
- NEVER READ for drawing. `plot_actual_orbits` (near line 4239) in
  normal mode draws every path from a fresh JPL question
  (`fetch_trajectory`, `palomas_orrery_helpers.py` near line 329),
  which returns a list of None on failure. Both `plot_orbit_paths`
  (palomas_orrery.py near line 4166; `orbit_data_manager.py` near line
  1535) are called from nowhere. The only saved data the plot reads is
  "special fetch" mode's temporary copy.
- Its metadata records dates, the centre and the last update, but NOT
  which JPL record the points came from (`orbit_data_manager.py` near
  line 1025). The ledger found in October that a path saved under
  C/2025_K1 could hold another comet's points after JPL renumbered
  (the 2026-10-24 lines, on the C/2025 K1 item).
- `fetch_position` (palomas_orrery.py near line 1371) returns None on a
  failed question; four bodies have a calculated position instead
  (`ANALYTICAL_POSITION_FALLBACK`: MK2, Xiangliu, Vanth, 6AC4721).
- `HORIZONS_CACHE = False` (`utc_clock.py` line 65): every JPL question
  is asked fresh, by Tony's standing practice. Part 2 must keep that as
  the normal case.

The website is not part of this: it serves the files built the night
before, and a failed night keeps the last good set.

## 3. Part 1, build: the decision falls back to the cited elements

1. In `path_or_orbit.py`, the order becomes: JPL's database e from the
   store; if there is no record, the e of the entry's elements in
   `orbital_elements.py` (typed from a cited source, or stored there
   from the cache); only if neither, the named failure as now. The
   console says which source decided, every time it is not the first.
2. Not today's heliocentric osculating e: Tony ruled it out on Nov 4
   (McNaught), and that stays.
3. `test_path_or_orbit.py`: the second link, with a planted fault (the
   typed e put on the wrong side of 1 must change the answer; the
   lookup turned off must fail by name).
4. Read whether 6AC4721's analytical orbit then draws, and why it drew
   one point; fix only what the decision broke.
5. Name every body the second link decides, not only 6AC4721: the
   small bodies the plot sends through `drawn_type_or_none` that have
   no record among the store's 68. Each one's drawing changes with this
   build, and the report lists them by name (protocol, A Report Names
   Its Items). Added Nov 4, 10:42, by the coordinating Fable session.

## 4. Part 2, map before any design (no edits)

For each of the five consumers (protocol, Check All Parallel
Pipelines), and for `fetch_position` and the plan drawing
(`path_drawing.py`), say what it draws today when JPL fails, by test,
not by reading: make JPL unreachable in a throwaway run and plot Mars,
Juno (centred on the Sun and on Jupiter), Halley and Voyager 1. In the
same run, ask for a body JPL does not have, and say whether the code
can tell that answer ("no such object") from no answer at all; today
`fetch_trajectory` returns a list of None for both. The map also
names the three copies of the analytical fallback list, the same four
names each: `ANALYTICAL_POSITION_FALLBACK` at palomas_orrery.py near
lines 4561 and 5954, and `ANALYTICAL_ANIMATION_FALLBACK` near line
7055. Whatever part 2 builds reads one list; it adds no fourth copy.
Then
read `data/orbit_paths.json`'s shape on a copy (sizes, keys, date
ranges, how many entries; never edit it) and whether its points match
JPL's today for three bodies.

## 5. STOP: Tony's rulings, then build part 2

Bring Tony the map and these questions, each with a recommendation,
one per message if he asks. Build nothing in part 2 until he rules.

- When the saved points are used: only when JPL cannot be reached
  (recommended: keeps "asked fresh" as the normal case), or also to
  spare JPL questions when the file covers the dates. Either way, JPL
  answering "no such object" is not a failure to reach JPL: no saved
  point stands in for it (Tony's Oct 31 ruling holds an identity).
- How a fallback drawing says so: a hover line naming the source and
  the date the points were fetched, and a console line (recommended),
  and whether the line itself looks different.
- The guard: the file starts recording which JPL record each path came
  from, and a saved path whose record differs from the entry's today
  is refused by name, never drawn (recommended). Entries saved before
  the guard have no record; whether they are trusted, checked once
  against JPL, or refused.
- Which drawings fall back: the path over the plot's dates, the
  position marker (from the saved point nearest the date, with what
  tolerance), the plan-drawn full mission, the animation. Recommended:
  the static path first, in this session; the marker, the full mission
  and the animation each ruled on their own once the path works.
- Integrity of the record itself: whether the maintenance run checks
  the file (it is not in git, so nothing else does), and what Tony
  wants kept as the record of JPL's answers. The run also fires
  nightly on GitHub's computers (L-485), where the file does not
  exist: a check there reports "no file here" as its own outcome,
  never as a pass and never as a failure that stops the night.
- The third link, for the drawing: when JPL and the saved file both
  fail, what draws for a path body (a hyperbolic comet, a spacecraft),
  which has no ellipse to fall back on. Tony's chain has three links;
  part 1 gives the decision its third, and this asks whether the
  drawing gets one (recommended: nothing drawn, and the console and
  the legend say why). Added Nov 4, 10:42, by the coordinating Fable
  session.

## 6. Rules to load

Read in full: horizons-orbital-mechanics 1.16, safe-file-editing 1.14,
agentic-pre-test 1.3. In the parts the job needs: orrery-coding-
conventions 1.13 (hover, the live dispatch path), provenance-discipline
2.36, ledger-and-session-records 1.22, gallery-cache-builder 1.17 (only
its HORIZONS_CACHE section). Open the first report with each version
line read, against the manifest in `PROJECT_INSTRUCTIONS.md` at HEAD.

## 7. Done when

- Part 1: 6AC4721 draws its analytical orbit again, the test fails on
  its planted faults, and the maintenance run's last line passes.
- Part 2, as ruled: a throwaway run with JPL unreachable draws from the
  saved points, marked, and refuses a planted mismatched record by
  name; with JPL reachable, nothing changes and no saved point is
  drawn.
- Tony's run order ends with his look, wifi off and then on: Mars, Juno
  and Halley around the Sun, and 6AC4721 with MAPS.

## 8. Records, in the same session

- L-512 opened (confirm it is the next free handle at HEAD): "the
  orrery's fallbacks when JPL cannot answer", Tony's words of Nov 4
  quoted, the map, his rulings, what was built and verified. One
  sentence says why part 1 is not L-510 undone: L-510 retired
  `object_type`, a project label with no source; part 1's second link
  is a measurement typed from a cited source, used only when JPL has
  no record.
- horizons-orbital-mechanics, one bump for both parts (one session, one
  bump), with the protocol's entry; L-510's "named failure" sentence in
  that skill corrected by part 1.
- Where We Are, by section, under its 130-line cap; nothing below the
  run-record marker.
- The report: files changed with edit counts, the bodies whose drawing
  changed by name, the token count, Tony's run order, one question at
  most.

Written November 4, 2026 with Anthropic's Claude Opus 5.5. Part 1 step
5 and the sixth question in section 5 added the same morning with
Anthropic's Claude Fable 5.1, on Tony's "yes" of 10:42, after the
brief's code facts were confirmed at 190f42c4. At 10:47, on Tony's
"yes, based on your decision", three points from GPT's review of the
handoff were added (part 2's not-found test; questions 1, 4 and 5);
GPT's fingerprint guard was not, since it would refuse a value change
the Oct 31 ruling takes. At 10:53, on Tony's "yes", the three fallback
lists (part 2) and the L-510 sentence (section 8) were added.
