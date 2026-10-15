<!-- Doc-Kind: hand | Brief for the L-444 build: a new generator row in the orrery's maintenance run that fetches, from JPL, the orbital period of each served body that has none fetched, before the Horizons check compares it. Orrery only. -->
# Brief: the maintenance run fetches the missing periods (L-444)

Built on orrery ffc4bd4eef2ee24b23c272feee49bd84c298d58b at
https://github.com/tonylquintanilla/palomas_orrery ("L442 close and
rulings"). The gallery is not touched by this build (read at
86ef2df6313f956f5c9e49611e6a2bdd0e95da29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; its
website prints whatever period the orrery's export carries).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 14, 2026 with Anthropic's Claude Opus 5.5, in the
coordination session of that day.

- Type: BUILD brief, orrery only. One session, Tony's word on the one
  decision below, then the build.
- Ledger: L-444 (the missing periods), opened 2026-10-14 with Tony's
  ruling. Read its block first; it carries his question and his "yes".
- Order: on the road as stage 8a, before L-443 (the objects to the
  website). Every object L-443 adds gets its period this way.

## 0. Before building

- Pull the orrery at HEAD and pin it.
- Skills this task fires, confirmed against the manifest at HEAD:
  horizons-orbital-mechanics (1.6; Where the Check Lives, and What It
  Compares; A Period Depends on Its Centre), safe-file-editing (the
  patch), agentic-pre-test (new code), ledger-and-session-records
  (the close).
- THE OBLIGATION THAT TRAVELS: this session confirms its loaded copy of
  ledger-and-session-records reads 1.21 before ledger work (bumped
  2026-10-14, protocol v3.97).

## 1. The ruling (Tony, 2026-10-14; recorded on L-444, not re-asked)

Tony's question, in his run record: "should the 30-day Horizons checker
initiate a fetch of the missing data as well as report, including a new
object as never having been fetched?" Claude recommended a separate
step, and Tony said "yes" to it as written:
- the fetch uses the orrery's own fetching code, the path plotting
  takes, so a period fetched this way is the same record plotting
  would write;
- it asks JPL only for what is missing: a keyed, served object with no
  fetched period, including a new one the first time the run sees it;
  on most days it asks nothing;
- it runs before the Horizons check, which then compares the new
  periods with JPL the same day;
- a fetch that fails is named, never passed;
- the check stays a check and fills no gaps itself.

## 2. What is there at ffc4bd4e

- `horizons_check.py` is a generator row of `orrery_maintenance_run.py`
  (the row named "Horizons check"). For a served body whose period is
  typed or missing it prints "typed, not fetched from JPL" or "no
  period fetched from JPL" and compares nothing (its "not compared"
  branch). It reads the bodies through `export_objects.load_inputs`.
- A period record is written only by
  `osculating_cache_manager.fetch_osculating_elements(...,
  with_period=True)`, which calls `orbital_period.build_period_record`
  and returns a cache entry holding the elements AND the period. The
  orrery's plotting path reaches it through `get_elements_with_prompt`,
  which shows Tony a dialog first and saves with `save_cache` into
  `data/osculating_cache.json`.
- Eight served bodies print a typed period, marked: Venus, Earth, Mars,
  Saturn, Uranus, Neptune, Apophis and Halley. Mercury, Jupiter and
  Encke print JPL's (L-431).
- Not in scope, and staying on L-443: served objects with no `'key'`
  (moon, io, titan, pluto, charon, voyager_1), and the Pluto-Charon
  barycentre's own period, which the orrery never fetches.

## 3. What to build

- A generator row in `orrery_maintenance_run.py`, just before
  "Horizons check", named for what it prints (a dashboard button is
  named what the run prints, Tony's ruling of Oct 12). Suggested name:
  "Period fetch".
- Its set: the same keyed, served objects the check reads, whose cache
  entry has no fetched period record. It prints that set by name before
  asking anything, and "nothing missing, no query asked" when it is
  empty.
- Its fetch: the same call plotting makes, without the dialog, saved
  the same way. Read `get_elements_with_prompt` for the centre, the
  id_type and the date it passes, and pass the same. The record that
  results must be indistinguishable from one written by plotting; a
  planted fault proves it (below).
- Network: any failure to get JPL's answer is UNREACHABLE by name, the
  convention for every row that needs the network. The body stays
  missing, the row says so, and no further query is asked that day.
- The run's order then carries the new periods through: the Horizons
  check compares them with JPL's PR within their own error, and the
  objects export writes them, so the website prints them after Tony's
  push and the gallery's pull.
- A dashboard button for the row (every new check gets a button), so
  Dashboard Parity (L-440) still passes.

## 4. The one decision, for Tony at the session's start

(decide) The plotting call fetches the ELEMENTS and the period together.
For a body that already has cached elements but only a typed period
(the eight above), the fetch also refreshes its elements, without the
dialog that plotting shows ("System provides information, user makes
decision", the elements prompt's own philosophy). Two ways:
- A (default): the same call as plotting, elements and period together,
  only for bodies missing a period. The drawn orbit and the period then
  describe one fetch at one date, which is what The Drawn Orbit Follows
  the Period's Centre needs. The row names each body whose elements it
  refreshed.
- B: fetch the period record alone and leave the elements as they are.
  Fewer changes, but a record from another date is not paired with the
  drawing, so the hover falls back for those bodies until they are
  plotted.

## 5. Planted faults, each shown caught

- A body with a fetched period asked again (the row must ask nothing).
- A fetch that fails, read as a pass (it must print UNREACHABLE and
  leave the body missing).
- A record written by a path other than plotting's (the record's
  fields and their sources must match a plotted one, compared against
  a recorded entry).
- A new keyed object with no cache entry at all, missed by the set.

The tests run offline on recorded JPL answers, as the Horizons check's
own suite does (`documentation/worksheets/horizons_answers_L395.json`
is the precedent); the first live run, on Tony's machine, is the real
test.

## 6. Close

- The L-444 block records the build, Tony's run and the first live
  fetch by body name.
- Where We Are: stage 8a done; the eight bodies named as fetched (or
  each failure named).
- horizons-orbital-mechanics: one line under Where the Check Lives
  saying the fetch row runs first. That is a skill bump (1.7), with the
  protocol entry, under One Session, One Bump.

## 7. Tony's actions, all of them

- (do) Start the build session from this brief.
- (decide) Section 4, A or B; default A.
- (do) Run the patch; run `orrery_maintenance_run.py` (the first live
  fetch); look at one fetched body's hover in the orrery and on the
  website after the push; reinstall horizons-orbital-mechanics if it
  was bumped; commit; push.

Brief written October 2026 with Anthropic's Claude Opus 5.5.
