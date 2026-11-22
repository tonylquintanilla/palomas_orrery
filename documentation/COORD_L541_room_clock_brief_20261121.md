<!-- Doc-Kind: hand | Brief for one Claude Code session: the live rooms ask JPL's dates on JPL's clock, so a body is drawn where it is at the UTC minute shown (L-541). -->
# Brief: the rooms' clock (L-541)

Built on orrery ae9ec0f9 at https://github.com/tonylquintanilla/palomas_orrery
and gallery 7d1e2e16 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main
for both). Written November 21, 2026 by the coordinating session (Claude
Fable 5.2) for ONE Claude Code session in the WEBSITE repository.

Read before building, and say back which you read: the website's
CLAUDE.md and the files it points to; the skills `interactive-exhibit`
(a room, its date line, the words and numbers it prints, testing a
room), `gallery-assembler` (resolver.py, render_orbits.py, the served
window), `gallery-cache-builder` (what the builder serves and the
night's gate), `horizons-orbital-mechanics` (The Clock Is Read as UTC),
`provenance-discipline` (a served number's source; a computed position
prints what its errors earn), `safe-file-editing`, and
`ledger-and-session-records` (the closing report). Then this brief;
L-541 (a plan's clock) in the orrery's LEDGER_CONSOLIDATED.md, read
whole; and documentation/SURVEY_L541_clock_69s_20261121.md.

## 1. The ruling

Tony, November 21, 2026, after the coordinating session traced L-541's
wider question and reported that every body in a live room is drawn
where it was 69 seconds before the minute its date line shows.

16:18, his question: "What will we show visitors UTC converted from
TDB, or TDB?" He was told: visitors see UTC; the date line is the
visitor's own UTC minute and does not change; the room adds the
difference before it looks up JPL's data; a body's source line keeps
naming JPL's clock for the date of its orbit, as it does now, because
it quotes the source; a path plan's moments, where a visitor reads
them, print as UTC converted from JPL's clock, as the encounter already
does. 16:21: "Yes".

On the order of the cleanup, 16:04: "in whatever order you believe
works best." The coordinating session put this first because it reaches
every room, and before L-538 (the orbiters' printed error).

## 2. What was found at gallery 7d1e2e16 (read it; do not trust this list)

- THE DATES ARE JPL'S. `tools/gallery_cache_builder.py` stores, as each
  point's `jd`, the `datetime_jd` JPL returns (its JDTDB column); an
  orbit's `epoch_jd` is the Julian date Horizons was asked, which it
  reads on its own clock; `as_of_today.t` reads 2461365.500694444 on
  the Moon's record, which is 00:01:00 on JPL's clock.
- THE MINUTE IS UTC. `gallery/scene_moment.js` (`askFor`) turns the
  visitor's clock into an ISO minute; `interactive.html` hands it to
  Pyodide as `EPOCH_ISO`, in three scene specs and once more as
  `_jd = _iso_to_jd(EPOCH_ISO)`; `gallery/assembler/resolver.py`
  (`_iso_to_jd`) makes `resolved_epoch_jd` from it as it stands.
- NOTHING CONVERTS BETWEEN THEM. `render_orbits.propagate_marker`,
  `render_spacecraft.position_at` and `compose_children` take that
  Julian date against JPL's dates. So the room draws, at UTC minute M,
  the place a body had at M on JPL's clock, which is 69.184 seconds
  earlier.
- THE DATE LINE SAYS UTC. `sceneMomentStamp(jd)` in `interactive.html`
  prints the Julian date the driver returns (`epoch_jd`, `epochJd`)
  with the word "UTC". `SolarSystemFigures.distanceLine` and `pastSpan`
  subtract an orbit's `element_epoch_jd` (JPL's clock) from the same
  number (UTC). `scene_moment.js` reads the served window's `end_jd`
  to find the last minute it may ask for.
- A PLAN'S DAY IS PRINTED AS WRITTEN. `gallery/solar_system_figures.js`
  (`planDay` in `loiterLine`) prints a plan moment's day on JPL's
  clock in a sentence whose other dates are UTC (L-541, PRINTED).
- THE NUMBER HAS NO SOURCE. The 69 is whole seconds, typed in the
  builder's `utc_to_tdb`, copied from the orrery's
  `orbit_data_manager.py`; the orrery's `constants_new.py` has no row
  for it. The figure is 69.184 s: TAI is 37 s ahead of UTC (IERS
  Bulletin C 70 of 7 July 2025: "from 2017 January 1, 0h UTC, until
  further notice : UTC-TAI = -37 s"), and Bulletin C 72 of 6 July 2026
  says "NO leap second will be introduced at the end of December 2026"
  (both read Nov 21, 2026 in the tz list's forwards of them; C 72's at
  https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/QXCI2R2IOCR6XHSWBBTYXXE4WT2LEY3R/
  ; read the bulletin at IERS yourself before citing it). The 32.184 s
  between TAI and JPL's clock is in the builder's own docstring and is
  NOT sourced there; source it or let astropy carry it (below).
- WHAT IT COSTS. The survey: at 22:00 UTC on Nov 21, for 56 of 106
  served bodies the distance from the centre changes in 69.184 s by
  more than the error its box prints with. Mercury prints to whole
  kilometres and is about 640 km off.

## 3. What to build

The outcomes, which are Tony's ruling:
1. A body is drawn where JPL puts it at the UTC minute the date line
   shows, in every live room.
2. No date a visitor reads changes its clock: the date line, the frozen
   minute past the served window, and the shared link's minute stay
   UTC. A body's source line keeps its words on JPL's clock.
3. Where a room subtracts two dates (drift, the checked span), both are
   on one clock.
4. A plan's moment printed to a visitor is UTC, converted (the loiter
   sentence; right today for ESCAPADE, and must stay right).
5. The difference between the clocks is not typed in the page or the
   assembler. It is served, with its source.
6. A check that can fail holds outcome 1, every night.

How, which is yours to propose in Part A; this is the coordinating
session's starting point, not a ruling:
- ONE SEAM. JPL's dates stay as served. The UTC minute becomes a date
  on JPL's clock in one place, and what comes back to the page says
  both: the UTC minute asked and the date used. Nothing downstream
  converts again. Every place that prints a date from a Julian date
  says which clock that number is on.
- THE DIFFERENCE, SERVED. The builder has astropy, which carries the
  leap seconds; it can work the difference out for the served window's
  first and last minute, serve it with its source line, and fail
  loudly if the two ends differ. Say if a row in the orrery's store is
  the better home; that would be an orrery change, not this session's.
- THE WITNESS. At each build the builder asks JPL where two bodies are
  at one stated UTC minute inside the window, converting that minute
  with astropy, and serves the answers. A checker in the night pass
  works out the same two places the way the room does and compares,
  each within the error its box prints. Choose bodies whose 69 seconds
  of motion is far larger than that error (the survey ranks them): one
  worked out from its orbit, one from served points. With the seam
  taken out, the witness must go red by about the 69 seconds' motion,
  and the checker shows that on a planted break every run.

PART A, no edits. Map every place that makes, reads, subtracts or
prints a moment or a Julian date in a live room: the page, the scripts
under `gallery/`, the assembler under Pyodide, its tests and harness,
`tools/headless`, and the gallery run's checks that use a moment
(Scene moment, Scene address, Curve error, Solar System figures,
Display figures, Arrival, Earth scene geometry, the walks). For each:
the file and function, which clock the number is on, which clock the
code assumes. Then your proposal for the seam, the served difference
and the witness, and what the served window's last minute becomes (it
moves by 69 seconds; a minute asked past the end must still be
refused, and the last minute allowed must still be accepted). Stop
with that report. Tony carries it to the coordinating session.

PART B, after the go-ahead. The seam, the served difference, the date
line and each printing site, the two subtractions, the loiter
sentence. INTERACTIVE_AS_BUILT.md in the same commit, each file named
with its folder.

PART C. The witness and its checker; each existing check that moved,
changed in the same way and for a stated reason; then the whole
gallery run TWICE: on Tony's working copy, and in a throwaway folder
holding only what a push would carry (the files `git ls-files --cached
--others --exclude-standard` lists). Report the rows from the second.
On Nov 20 and 21 two nights went red on a check that was green only on
Tony's disk; documentation/patch_L529_4_as_built_names_night.py in the
website tells it.

NOT IN THIS SESSION.
- The builder's keys (`Time(jd).datetime` read as UTC) and its reading
  of a plan's windows as UTC, and the orrery's `path_drawing.py` and
  `utc_to_tdb` (L-541, READ AS UTC): named in your report, not changed.
- What `jd` means in a served file. An encounter's package and player.
  Hourly points for an orbiter (L-538).
- Any skill file. Name in the report what each of
  `horizons-orbital-mechanics`, `gallery-assembler`,
  `interactive-exhibit` and `gallery-cache-builder` should say.
- The orrery repository.

## 4. Delivery

- Work in the website repository only, through the python_work door.
  Record its base (`git rev-parse HEAD`, `git ls-remote origin HEAD`).
  The night commits under data/ every day, so the base will be a
  descendant of 7d1e2e16; stop only if a file named in section 2 is
  not as described, and name what moved.
- Edit the files in Tony's working copy, ASCII and LF, each change
  stamped where it is made; Tony commits and pushes. Nothing is pushed
  by the session.
- After Tony's push he runs the night by hand (the website's Actions
  tab, "Nightly run", "Run workflow") and reads it green before
  anything else is built in the website. Say so in the report.
- His phone look: the date line still reads UTC and nothing he can see
  has moved. The evidence is the witness, so the report shows its two
  rows, with the seam in and with it taken out.

## 5. The report

Plain words, in this order: what was built, file by file; the gallery
run's rows by name with their results, from the throwaway folder; the
witness's two rows both ways; what Tony does next (the push, the night
by hand, the phone look); the skill text owed; what is left on L-541;
anything this brief got wrong. It ends with the session's token count
as Claude Code's /cost prints it (Token Economy), and opens with the
anchor line: built on <base SHA> at the website's URL; ready at <new
SHA or "not pushed">.
