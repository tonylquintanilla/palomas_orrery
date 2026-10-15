<!-- Doc-Kind: hand | Build record for L-444: the maintenance run fetches a served body's missing period from JPL, before the Horizons check. Orrery only. -->
# Build record: the run fetches the missing periods (L-444)

Built on orrery ffd6c36a1546d844987d2b36aaee510225d2d64b at
https://github.com/tonylquintanilla/palomas_orrery ("L444 missing
periods brief"). The gallery is not touched (read at
86ef2df6313f956f5c9e49611e6a2bdd0e95da29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Pushed at: 9579fcd577706b2eec8a9e552949331074f4e45b (Tony's commit
after his run, 2026-10-15 10:57).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD, orrery only.
- Brief: `documentation/HANDOFF_L444_missing_periods_brief_20261014.md`.
- Patch: `patch_L444_missing_periods_20261015.py`.
- Ledger: L-444 (the missing periods), still OPEN until Tony's first
  live run.

## 0. Before building

- HEAD was ffd6c36a, the brief's base plus the brief itself and four
  lines of Tony's run record. The code was what the brief describes.
- Skills loaded, each matching the manifest: horizons-orbital-mechanics
  1.6, safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.21. The last discharges protocol v3.97's
  obligation.
- JPL could not be reached from the session (the proxy refused it), as
  for L-431's build 3. Every test runs on recorded answers; Tony's first
  run is the live test.

## 1. Tony's ruling, at the start

The brief's section 4, asked with Claude's recommendation (A): should
the step refresh a body's saved elements along with its period? Tony:
"A". The elements and the period are fetched together, by the same call
plotting makes, and the step names each body whose elements it
refreshed.

## 2. What was built

- `period_fetch.py`, the generator row "Period fetch" of
  `orrery_maintenance_run.py`, just before "Horizons check".
  - Its set: every keyed entry of `celestial_objects.py` whose period,
    read through `export_objects.period_block` exactly as the check and
    the export read it, is not "fetched": a typed period, none, or no
    cache entry at all (a new object). Printed by name before any
    question.
  - Skipped and named, for plotting's own reasons: the Sun (no period),
    and any object plotting's pre-fetch never asks elements for (an
    object_type outside orbital, satellite, trajectory, lagrange_point;
    a mission; MK2, Xiangliu, Vanth, Gonggong). Today that is the
    Pluto-Charon barycentre, which L-443 carries.
  - Its fetch: `fetch_osculating_elements(name, horizons_id=<id>,
    id_type=<id_type or 'smallbody' when absent>, date=<now>,
    center_body=None, with_period=True)`, then `save_cache` under
    `get_cache_key(name, None)`: the arguments palomas_orrery.py's
    pre-fetch passes for a Sun-centred view, read from both its sites.
  - After each save the cache is read back through export_objects and
    the body must read "fetched", or FAIL names it.
  - Any failure to get the whole answer is UNREACHABLE, by name; nothing
    is saved for that body and nothing more is asked that day.
  - One difference from plotting, on failure only: plotting saves the
    elements when the period query fails; this step saves nothing for
    that body, so it stays missing and is asked again next run.
- `test_period_fetch.py`, the checker "Period fetch suite". It replaces
  only the three functions that reach the network
  (`orbit_data_manager.query_horizons_elements`,
  `orbital_period.query_period_pair`,
  `orbital_period.fetch_sbdb_period_sigma`) with answers recorded in
  `documentation/worksheets/period_fetch_answers_L444.json`, taken from
  the period records plotting wrote for Mercury, Jupiter and Encke at
  ffd6c36a. One answer per body, the period around the barycentre, is
  constructed (plotting kept only how much it moved), and the file says
  so. Everything above those three functions is the real code.
- Dashboard: Period Fetch under the orrery's generators, Period Fetch
  Suite under its checkers, each in alphabetical place with its short
  line.
- Two descriptions that would have gone stale were corrected: the
  exporter's PERIOD section named only plotting as the writer of a
  period record; the cache manager's opening said it always asks.
- horizons-orbital-mechanics 1.7: one bullet under Where the Check
  Lives, and What It Compares, saying the fetch runs first. Its 1.4
  entry moved to `documentation/SKILL_HISTORIES.md`. Protocol v3.98,
  v3.95 moved down.

## 3. What was verified, and how

On a throwaway copy of HEAD with the patch applied (the deliverable was
never edited by a test):

- The planted faults, 12, each in a copy of `period_fetch.py` (or of
  plotting's filter), each caught by name: a fetched period asked
  again; the set not printed before asking; a new object with no cache
  entry missed; the period alone beside the old elements (option B),
  caught by the call check and again by the field comparison alone; the
  id_type read as the export reads it; a failed fetch read as a pass; a
  partial answer, elements without a period, treated as whole; the stop
  after a failure removed; the read-back removed; plotting's filter
  changed in palomas_orrery.py; the filter not found there.
- The real step: asks nothing when nothing is missing; fetches Mercury
  (period removed) and Encke (no cache entry) with plotting's exact
  arguments; the records saved match plotting's recorded ones field by
  field, except the dates written and the two-centre test's own date;
  leaves Jupiter, already fetched, untouched; UNREACHABLE on a refused
  period query and on a refused elements query, with nothing saved and
  nothing more asked; FAIL when a save does not read back.
- On the real list, offline, the set is the brief's eight: Venus, Earth,
  Mars, Saturn, Uranus, Neptune, Apophis and Halley. The Sun and the
  Pluto-Charon barycentre are named and skipped.
- The whole maintenance run, on the throwaway copy with the gallery
  beside it: the Period fetch row printed exit 1, "UNREACHABLE -- JPL
  could not be reached for Venus", named the other seven as not asked,
  and left data/osculating_cache.json byte-identical (the workspace
  cannot reach JPL). Period fetch suite: pass, 23 checks, 12 planted.
  Dashboard parity: PASS. Skill headers: 12 parsed, no problems.
  Provenance scanner: 0 Tier-1 on the gate path; whole tree unchanged
  at 280. Every other checker passed once the workspace had the
  orrery's libraries (matplotlib and customtkinter were missing at
  first, and Reset completeness and Orbit markers failed the same way on
  untouched HEAD).
- py_compile on every edited and new .py file; the orrery's window
  opened under xvfb on a throwaway copy and stayed open, no errors.
- The patch refuses a second run and writes nothing.
- The coordination session's
  `patch_L442_3_order_earth_sun_objects_20261015.py` (Tony's ruling on
  the order, 08:58, after this session began) edits Where We Are and
  the ledger too. The two run in either order, checked by text without
  running that patch: after this one, each of its six anchors is still
  there once; with its changes made first, this one also updates "Do
  next" and "Next". Run alone, this patch leaves those two lines and
  says why. The page stays at 130 lines above the run record either
  way.

## 4. For the next session

- The first live run is the real test of the fetch: the eight fetched
  by name, or each failure named. Record it on L-444 from Tony's run
  record, then close L-444.
- The obligation that travels: horizons-orbital-mechanics went to 1.7 at
  this patch; this session loaded 1.6. The next session confirms its
  loaded copy reads 1.7 before work that fires it.
- Recorded on L-444, not changed: a generator row does not count in the
  run's checker total, so a failed fetch shows on its own row and in the
  failure detail while the checker count can still read all passed. That
  is a question for the runner as a whole.

## 5. Tony's actions, all of them

- (do) Save `patch_L444_missing_periods_20261015.py` in the orrery folder
  and click Run.
- (do) Run `orrery_maintenance_run.py`: the first live period fetch.
- (do) Reinstall horizons-orbital-mechanics (1.7) in Settings > Skills.
- (do) Save `PROJECT_INSTRUCTIONS.md` as
  `documentation/project_instructions_v3_98.md`, and copy it into the
  Project instructions.
- (do) Move the patch script into `documentation/`; commit; push.
- (do) Look at one fetched body's hover in the orrery, and on the
  website after the gallery's pull.

## 6. Tony's run, and the close (added 2026-10-15)

- The patch applied on 7166648d. The first live run fetched all eight,
  Venus, Earth, Mars, Saturn, Uranus, Neptune, Apophis and Halley, and
  the Horizons check confirmed each against JPL: 31 of 31 gating
  checkers, pushed at 9579fcd. Venus's hover in the orrery: "orbital
  period around the sun fetched today, correct."
- Tony asked whether the Horizons check should come before the cache
  build. It does in the orrery; the website's Daily Run builds before
  it pulls. Opened as L-446 (the daily run's order), with his "Yes".
- Earth printed 366 days: the period of Earth's centre, which the Moon
  makes wobble through the month. Tony's ruling the same day: take
  Earth's period from the Earth-Moon barycentre. Opened as L-445
  (Earth's period), which also carries the look at the website.
- L-444 closed by `patch_L444_2_close_20261015.py`.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
