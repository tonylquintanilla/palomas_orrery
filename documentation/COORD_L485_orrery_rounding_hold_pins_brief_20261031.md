<!-- Doc-Kind: hand | Brief for the next orrery Claude Code session: the export's rounding fault first; the dashboard's second line and the orrery workflow's concurrency line; the per-body form of a night's disagreement with JPL (take a value, hold an identity); the periodic comets' record pins retired for the designation with CAP; gallery-cache-builder 1.15. Written by the coordinating session; zero code. -->
# Brief: the orrery session (the rounding fault, the hold, the comet pins)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 31, 2026, 21:45

Written at orrery dc85f372bcaec6178806affe4006a348a557e997 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery c1c578f57f812aa0dcc0f1fec45bab43e7826bd0 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Nov 1, 01:55 UTC (Oct 31,
20:55 Chicago). Every line number below was read from those two
commits. YOUR BASE IS HEAD WHEN YOU OPEN THE SESSION, which will be the
commit that carries this brief, the coordination handoff beside it and
Tony's run record, and may be a nightly commit or two newer than that;
read it yourself and anchor everything there.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the ORRERY repository: item 1 of
the queue in `HANDOFF_coordination_20261031.md`, section 6, built from
that handoff's section 4 (items 1 to 5). The session reads this file,
that handoff, and the orrery half's brief
`COORD_L485_orrery_nightly_brief_20261029.md` (the shape of the night
it is changing) before anything else. The ledger items: L-484 (the two
agree: the rounding), L-503 (the belt's cloud: the pin that moves),
L-485 (a nightly run: the hold, the dashboard line, the concurrency
line, the skill), L-470 (JPL's permanent number: the comets), L-461
(pull matches push) and L-490 (the legacy list).

The gallery is READ, never written, from this session. Three findings
below need a gallery build to finish (the hold's website half, and the
website asking a comet by designation); each is written on the ledger
for a gallery session, not built here.

## 0. The base, the skills, the order

- Orrery: HEAD, clean, after Tony's morning Pull origin (the nightly
  run commits at 07:17 UTC). Tony's run record for this session,
  `documentation/WHERE_WE_ARE_11-<d>-26_<hhmm>_run_record.md`, appears
  when he copies the page at your first run order; that one is
  expected. Anything else waiting is not.
- Gallery (the sibling folder): c1c578f5 or newer (its own nightly run
  commits at 08:17 UTC), clean, read only.
- Skills this job fires, each read in full before the work, versions
  stated in the first report against the manifest in
  PROJECT_INSTRUCTIONS.md v3.118: safe-file-editing 1.14,
  agentic-pre-test 1.3, ledger-and-session-records 1.22,
  provenance-discipline 2.36 WITH its `references/figures.md` (Rules 3
  to 5 and the Report test live there, not in SKILL.md),
  horizons-orbital-mechanics 1.13 (Which Record Serves a Body,
  Small-Body Record Pinning, Checking an Entry Against JPL),
  gallery-cache-builder 1.14 (bumped here, section 5),
  orrery-coding-conventions 1.12 (the dashboard line, docstrings).
  A Code session reads the repo's copies, which are the manifest's
  (v3.118's note).
- Order of work, and it is the point: section 1 (the rounding fault,
  small and first); section 2 (the dashboard's second line, the
  concurrency line, both small); section 3 (the hold); section 4 (the
  comet pins); section 5 (the skill bump and the protocol entry);
  section 6 (the records). A session running out of room stops BEFORE
  section 4 and says so plainly; sections 1 to 3 and 5 to 6 are then a
  complete session, and section 4 moves to the next orrery session
  with the live answers in section 4 as its base.
- The session asks Tony ONE question in all. This brief leaves none
  open; what it cannot settle it names as the session's or a skill's,
  and section 3.1 names one reading of Tony's ruling he may overturn
  when he reads the report.

## 1. The export's rounding fault (L-484, L-503) -- first, and small

**The fault, confirmed by the coordinating session at dc85f372.**
`constants_rows._to_place(value, place)` (line 634) rounds to a
FIGURE COUNT computed from the unrounded value, then, when the result
has carried into a new leading digit, re-rounds the ORIGINAL value at
one more figure, which undoes the carry. Run on Oct 31: 9.996 at the
hundredths returns 9.996 (its own docstring promises 10.00), and the
belt's 90th height, 0.667 AU times 149,597,870.7 km = 99,781,779.76 km
at the million place, returns 99,800,000 (the rule's answer is
100,000,000). The website prints what is served, so the Solar System
room reads "about 99.8 million km" where the orrery's own hover
(`main_belt_sampler.hover_text`) reads "about 100 million km". The
orrery's hover is right; the export is wrong.

**The rule, in the skill's words** (provenance-discipline
`references/figures.md`, the paragraph under Rule 3, "A value in
another unit is computed, never stored"): the place printed is found
by the Report test from the source's scaled uncertainty; "the count is
the figures of the full-digit value down to that place, and never
fewer than one: where the place is coarser than the value's leading
digit, the value keeps its one leading figure (a one-figure 100 Earth
radii is 0.004 AU, not 0.00)". Rule 5: round half to even. Tony,
Oct 31, 17:10: "do all the computations with all the numbers and
round at the end to significant figures." The fault is in that last
rounding, not in the rule or the store.

**The fix** (the session's, under safe-file-editing): round the value
AT THE PLACE, half to even, and count the figures of the ROUNDED
value; keep the one-figure branch exactly as the docstring states it
(the place coarser than the leading digit keeps one leading figure --
this branch is why 637,800 km at the million place stays 600,000 and
not 1,000,000; do not "fix" it). The docstring's example then holds.
Expected values, WORKED BY HAND, never read from the function (GPT's
criterion (ii), `HANDOFF_coordination_20261031.md` section 4):
99,781,779.76 at place 6 is 100,000,000, three figures; 9.996 at place
-2 is 10.00, four figures; 9.6 at place 0 is 10, two figures; 637,800
at place 6 stays 600,000, one figure (the branch); 2.5 and 1.5 at
place 0 are both 2 (half to even).

**What changes in the export, by name.** The coordinating session
rebuilt `data/constants_export.json` in memory with a rounding of that
shape: FIVE served "in" entries change out of 830, and nothing else:
- `EARTH_VAN_ALLEN_INNER_RADII` in km: 9,600 becomes 10,000 (two figures)
- `EARTH_EXOSPHERE_H_FIT_OUTER_RADII` in km: 96,000 becomes 100,000 (two)
- `MAIN_BELT_A_INNER_AU` in pc: 9.7e-6 becomes 1.0e-5 (two)
- `MAIN_BELT_DISTANCE_PERCENTILES_AU[100]` in r_earth: 99,990 becomes 100,000 (four)
- `MAIN_BELT_HEIGHT_PERCENTILES_AU[90]` in km: 99,800,000 becomes 100,000,000 (three)
That list is a CLAIM for the session to confirm by its own diff of the
export before and after (names, not a count: A Report Names Its
Items). Each is a value whose correct rounding carries into a new
leading digit, which is the fault's whole domain, so a sixth name
would mean the fix did something else as well.

**The tests, two kinds kept apart** (criterion (ii)):
- The regression test establishes the RULE with the hand-worked
  values above as pins, and plants the two faults (the docstring's
  case and the belt's case) so a return of the old behaviour fails by
  name. Where it lives is the session's: no `test_constants_rows.py`
  exists at dc85f372; the CHECKERS table in `orrery_maintenance_run.py`
  (line 401 on) has Constants relations (`test_constants_provenance.py`)
  and Constants export check (`test_constants_export.py`, line 411).
  Read both before choosing; a new suite is a new row in that table,
  and the night set (NIGHT_ROWS, line 556) is read for whether it runs
  at night (it judges a function, not data, so probably not: say so).
- `test_constants_export.py` check 6 (CONVERSION_PINS, line 361) moves
  its pin from 99,800,000 to 100,000,000; the figure count stays 3.
  Its comment "whose place, the hundredth of an AU, carried into
  kilometres, prints three (Rule 3)" is right about the place and
  stays; the Oct 29 session's reasoning that 99,800,000 "prints three"
  conflated the count with the place, and the pin's new value is the
  correction. The Constants export check then establishes only that
  the export used the corrected function; it recomputes with the same
  function and so cannot fail on this fault by itself, which is why
  the regression test exists.

**Then:** `export_constants.py` rerun (the Run button, or the
maintenance run's generator row); the Constants export check green;
the diff of `data/constants_export.json` read and the five names
confirmed; the push gate (Tier-1 = 0 on the active build path).

**The website, read only.** `documentation/smoke_solar_system_figures.js`
in the gallery (the part that holds each served km to its AU "to both
roundings", about line 821) accepts 100,000,000 at three figures
against 0.667 AU at two, and its kmText prints "about 100 million km".
So the website's night after Tony's push will pull the new export and
print the orrery's sentence; no gallery edit is needed for the belt.
The Van Allen inner belt (km) and the exosphere fit's outer edge (km)
are Earth-room numbers: read where the gallery prints those two "in"
km entries, if anywhere, and tell Tony in the report which sentence on
the site changes, for his phone look (Mode 5). Record on L-484: the
orrery's hover was right, the export was wrong, the five names.

## 2. Two small items from the gallery session's list (L-485)

**2.1 The dashboard's second line.** `palomas_orrery_dashboard.py`
`nightly_run_line(path=NIGHTLY_RECORD, now=None)` (line 2382) returns
`(text, red)` for the orrery's record and has one caller in
`_build_header` (about line 2856). The website's record has the SAME
key, `clean_run_utc` (gallery `daily_run.py` write_night_record, about
line 1043; the file at c1c578f5 reads 2026-10-31T18:29:04 UTC), and
`GALLERY_REPO_DIR` already exists (line 362). So: the function gains a
label parameter (its words "Nightly run:" and the orrery file's name
are hard-coded today), and a second call reads
`os.path.join(GALLERY_REPO_DIR, "data", "nightly_run_record.json")`
and prints the website's last clean night, red when older than a day,
with the sibling folder missing or the file absent saying so in words
("the website's folder is not beside the orrery" is a true state on a
machine with one clone). Dashboard parity run and read afterwards; the
docstring's Oct 30 entry updated; orrery-coding-conventions fires.

**2.2 The orrery workflow's concurrency.** `.github/workflows/nightly.yml`
in the orrery has no `concurrency:` key; the gallery's has
`concurrency: group: nightly-run` with no cancel-in-progress (so a
second run waits and a running night is never cut off; its comment
quotes GitHub) and checks out `main` as it stands when the job starts,
so a run that waited builds on the first one's push. Copy both lines'
sense into the orrery's file, in its own words; a hand-fired run and
the schedule then never push at once. The ask-everything tick box and
everything else stay.

## 3. The hold: a night's disagreement with JPL, body by body (L-485)

**3.1 The ruling, and how each disagreement sorts under it.** Tony,
Oct 31, 18:38: "take-and-report for values and hold for identity and
record -- confirmed. In other words we hold only where a project
choice matters." JPL is the authority, so a disagreement is never JPL
versus us; it is "what we pinned is no longer what JPL says". Where
that is a value there is nothing to judge; where it is a choice the
automation cannot know which. The Horizons check finds its
disagreements in two functions, and the session sorts EACH cause,
listing the sorting in its report:
- `horizons_check.check_period` (line 524): JPL's period for the same
  record, centre and epoch differs from the served one beyond its
  error -- a VALUE: taken. An open/closed mismatch (line 565) is also a
  value JPL changed: taken. An unreadable epoch or a query JPL refuses
  (lines 534 to 557) is not a disagreement with JPL's data; it is
  REPORTED under R4 as an outage is, not taken and not held.
- `horizons_check.check_entry` (line 338): `horizons_name` differs for
  the same handle (lines 375 and 437) -- an IDENTITY: held. The handle
  answers no record, or more than one, or is found in neither index
  (lines 368, 414, 423) -- identity: held. `id_type` found in the other
  index or in both (lines 419, 433), and `object_type` (line 441): the
  project chose which index and kind a body is asked as, so these are
  a project choice -- held. THIS IS THE COORDINATING SESSION'S READING
  OF THE RULING'S TEST; Tony reads it in the report and may overturn
  it. `pin` stale, a newer record for a pinned comet (line 392): the
  "record" kind of Tony's ruling, held -- until section 4 retires the
  pins, after which this cause no longer exists and a change of
  apparition is a value change, taken (section 4).
- Period fetch finds nothing to take: `period_fetch.classify` (line
  262) fetches only a period that is MISSING or was fetched against
  another target; a fetched period whose value JPL now gives differently
  is seen only by the check. So "take" is new behaviour, not a switch.

**3.2 What a TAKE does.** The night takes JPL's new value, serves it,
and writes the change in the log and the night's record with the old
and the new number, by name. Mechanics, with one constraint that is the
skill's (one home per file): `data/osculating_cache.json` is written
by ONE writer, `period_fetch.plotting_save` (line 319), which wraps
`osculating_cache_manager`; a take re-fetches that body's elements and
period through the same path period_fetch uses (`plotting_fetch`, line
305), so the served period, epoch and elements move together as JPL's
new solution, not a lone number pasted over old elements. Then the
confirmation record (`data/horizons_confirmations.json`, written at
`horizons_check.py` lines 965 to 993, which today SKIPS a DISAGREES
result at line 966) records the new `days`, `jpl_days` and `confirmed`,
and the check's verdict names it: "TAKEN encke.period: 1206.3202 ->
<new> days (JPL's solution of <date>)". Whether the check does the
re-fetch itself in the same run, or writes a take-list the period fetch
consumes, is the session's; the first keeps the night to one pass and
is this brief's expectation. The export follows from the cache. The
exit code: a night with takes and no failures is CLEAN (exit 0); the
check's "FAIL" stays for what is neither taken, held nor reported.

**3.3 What a HOLD does.** That one body is held at its last confirmed
values, with their date, and named for Tony; it is not refreshed until
he looks. Today the record already keeps the old values and date on a
DISAGREES (line 966), so the data is right; what is missing is the
MARK and the PASS:
- The record's entry gains a hold block, written by the check when an
  identity cause fires: since (UTC date), the cause by name, what the
  list says and what JPL said, the query. Name the field `hold`, not
  `held`: `held` is a local variable in the gallery's
  `tools/check_horizons_confirmations.py` (line 118) and in
  `horizons_check.period_state` (line 738), and a field and a variable
  with one name read as one thing.
- `export_objects.confirmation_of` (line 553) carries the hold block
  out beside `identity` and `period`, so the export says: last
  confirmed values, their date, held since, why. Schema bumps (3 to
  4); `test_objects_export.py` compares each object's confirmation
  with the record date for date (lines 40 to 48) and the schema (line
  274) -- both stay true, since a held body keeps its old date.
- `check_horizons_confirmations.py` (the night's checker, `--night`)
  passes a held body AS HELD, printed by name with its date and cause
  ("HELD encke -- since 2026-11-03: horizons_name 2P/Encke -> ..."),
  not red, and not overdue however long the hold lasts; the lapse
  clock does not run on a held body, because Tony's look is what ends a
  hold. By day (no --night) the same line prints, and whether it is
  red by day is the session's reading of the checker's two voices (the
  orrery half's brief, section 2: by day the checker goes red where
  the night reports); say which in the report.
- The other bodies save that night either way: the gate's two lines
  that make one disagreement a red night (`orrery_maintenance_run.py`
  night_gate, lines 723 and 725: the checker "failed" and the generator
  "exited 1") stop firing because neither tool exits non-zero on a take
  or a hold. Confirm with the suites: `test_horizons_check.py` (the
  night form, line 703) and `test_maintenance_report.py` (the gate's
  cases, line 235) each gain a take case, a hold case and a planted
  fault for each (a hold dropped; a take not logged; a held body
  turning the night red).
- Ending a hold is Tony's, by hand, for now: he reads the hold in the
  log, edits the pin (or the designation after section 4) in
  `celestial_objects.py`, pushes, and the next night re-confirms. No
  tool un-holds; say so on L-485 and in the report.

**3.4 The night's record and the dashboard line name what was taken
and what is held.** `write_night_record` gains `taken` and `held`
lists (name, old, new, date; name, since, cause), and
`nightly_run_line` appends them in words ("; 1 held: Encke since
2026-11-03") -- the record is read, never retyped. Red stays as it is
(no clean run in a day); a hold is named, not red, by the ruling.

**3.5 The website's half, NOT built here, recorded for a gallery
session.** Read at c1c578f5, so the record is exact:
- `tools/mirror_objects.py` copies only `REPLACED` (name, horizons_id,
  id_type; line 133) and `INSERTED` (description, info_url, period,
  path, open_path, horizons_name; line 134); every other export field
  is dropped with no message (`confirmation` and `object_type` already
  are). A hold block would be dropped the same way.
- The builder asks JPL by `horizons_id` from the mirrored config
  (`tools/gallery_cache_builder.py` fetch_vectors_range line 447,
  fetch_elements line 480); nothing honours a hold.
- Its last-good path (`serve_last_good`, line 1483) re-stamps
  `source.retrieved` with the current time (lines 1109 and 1134) and
  drops its own `stale` flag before `coverage_index.json` (derive_served,
  line 1785 on), so the room's source line would print the night it
  was re-served, not the date of its data; and a held body that is not
  a path nulls `served_window` for the whole cache (line 1822 on).
- The website's own `tools/check_horizons_confirmations.py` goes red
  for a held body at day 30 (`_age`, lines 100 to 112).
So until that gallery build exists, a held body makes the WEBSITE's
night red from day 30 -- which is exactly today's behaviour, so
nothing gets worse, and nothing is held today. Tony's ruling of Oct
31, 21:30: that gallery session comes AFTER the ruler build (queue
item 2), as its own short session. Write it on L-485 under "for a
gallery session: the hold's website half", with the four facts above
and GPT's criterion (i): the export marks a held body; the builder
honours the mark (no fetch, last-good served and NAMED, its own data's
date kept); the room's hover prints the held date; the website's
checker passes held as held. The coordinating session opens its ledger
item when it writes that brief.

## 4. The periodic comets' record pins retired for the designation (L-470)

**4.1 The ruling.** Tony, Oct 31, 18:45: "the third case where a non
permanent record number is reassigned is fragile: we should use the
permanent record." Each periodic comet is asked by its permanent
designation with JPL's CAP directive ("closest apparition": the "last
apparition before current date", the Horizons manual), the way the
non-periodic comets are asked by JPL's permanent number since Oct 24
(L-470, "B"). JPL then follows a new apparition by itself, nightly; a
reassigned record number cannot bite because no number is typed. With
that, the "record" kind of section 3 disappears: a change of
apparition is a VALUE change, taken and reported with the old and new
record numbers; the hold applies to IDENTITY alone, a designation
answering with a different name. Three things confirmed with the
ruling are in `HANDOFF_coordination_20261031.md` section 4, item 2
(the window not the hold was the fragility; CAP keeps a comet inbound
to a new perihelion on its previous apparition's record until
perihelion passes; no threshold on a jumped value is built until a jump
has been seen).

**4.2 The six, and JPL's answers on Oct 31.** `celestial_objects.py`
holds SIX record pins, not five (`'id_type': 'smallbody'`, id of the
form 9000xxxx): Tempel 2 90000214 (line 585, 10P), Schaumasse 90000356
(596, 24P), Howell 90000901 (606, 88P), Churyumov-Gerasimenko 90000703
(616, 67P), Halley 90000030 (632, 1P), Encke 90000091 (642, 2P). The
other 9000xxxx numbers in the file are comments (C/2025 K1 and its
pieces). The coordinating session asked JPL's API on Oct 31 (JPL's
clock 19:05, Pacific) by designation with CAP, `COMMAND='DES=<d>;CAP'`,
and read each answer's `Rec #:` line:
- 2P: Rec #:90000091 (+COV) Soln.date: 2026-Oct-22_15:51:34, # obs: 1329 (2018-2026), EPOCH 2024-Jun-01
- 1P: Rec #:90000030, Soln.date: 2025-Nov-21_15:57:34, # obs: 8518 (1835-1994), EPOCH 1968-Jan-20
- 10P: Rec #:90000214 (+COV) Soln.date: 2026-Oct-22_15:52:05, # obs: 7130 (2003-2026), EPOCH 2017-Sep-21
- 24P: Rec #:90000356 (+COV) Soln.date: 2026-Jul-07_05:58:32, # obs: 3535 (2000-2026), EPOCH 2024-Jan-12
- 88P: Rec #:90000901 (+COV) Soln.date: 2026-Oct-14_16:22:22, # obs: 4019 (2014-2026), EPOCH 2021-Mar-05
- 67P: Rec #:90000703 (+COV) Soln.date: 2026-Sep-04_10:25:07, # obs: 8610 (2008-2025), EPOCH 2015-Oct-10
Every CAP answer equals today's pin. Encke's and Tempel 2's records
were re-solved on Oct 22 under the same number, the skill's "a pin
fixes the apparition, not the numbers".

**4.3 The trap, found doing it.** Sent with a BARE semicolon in the
address (`COMMAND='DES=2P;CAP'` unencoded), JPL ignored CAP and
returned Encke's whole list of 61 records, twice; with the semicolon
encoded as `%3B` it returned the one record. JPL's API page says so:
"API calls must encode semicolons as %3B in the URL". So before
trusting any answer, the session reads how `horizons_check.command_of`
(line 475) and `record_list_url` (line 204) encode their commands, and
tests a CAP query through THAT code path, not only by hand.

**4.4 TEST BEFORE RETIRING, through the orrery's own two routes**
(criterion (iii): the whole answer, read back). The orrery asks JPL two
ways: astroquery (`Horizons(id=..., id_type=...)` at twelve sites, the
list in 4.5) and raw URLs (`horizons_check.command_of`, `path_plan`'s
`vectors_url`). horizons-orbital-mechanics 1.13 records that
`closest_apparition=True` threw a syntax error with
`id_type='smallbody'` because astroquery prepends `DES=` only for
`id_type='designation'` or `'name'`. So the test is: for each of the
six, ask with `id_type='designation'`, `closest_apparition=True`,
with and without `no_fragments=True`, through astroquery; and ask
`DES=<d>;CAP` (and `;NOFRAG`) through the raw-URL builder; read back
the designation, the name and the record number from each answer, and
confirm all four forms name the same record as the list above and as
the pin. One disagreement, and the pins stay and the report says
which form failed. A comet with a future-only apparition would need
CAP's date form; note it on L-470, do not build it.

**4.5 Then switch every reader, as one change** (Which Record Serves a
Body: one record per body and centre, in every reader). The entry
keeps `horizons_name` and gains the designation as its handle;
whether that is `id: '2P', id_type: 'designation'` with a comet flag,
or a new field, is the session's, chosen so that EVERY reader below
asks the same question. Readers of a comet's `id`, read at dc85f372
(the night tools: `export_objects.served_identity` line 272,
`horizons_check` lines 347 and 543, `period_fetch.served_entries` line
215, `path_plan` lines 287 to 328; the orrery's fetches in
`palomas_orrery.py`: fetch_position 1330/1392, add_celestial_object
2035, plot_actual_orbits 4321, plot_objects' pre-fetch 4742 to 4785 and
its worker 5122 to 5839, animate_objects 6506 to 6548 and
animation_worker 6908 to 7310, can_be_horizons_center 9143; the
helpers: `palomas_orrery_helpers.fetch_orbit_path` 579/597,
`orbit_data_manager` 682/697, 1013, 1181, 1296 and
`query_horizons_elements` 1810, `osculating_cache_manager` 386/429/441
and resolve_tp 670, `idealized_orbits` (ten sites, 5023 to 7309),
`spacecraft_encounters` 613, 863, 1245, `orbital_period` 338,
`position_accuracy` 822, `close_approach_data` 572, `orbital_param_viz`
2096/2107, `apsidal_markers` 902). Three functions recognise a pinned
record by the pattern `^9\d{7}$`: `horizons_check` line 182,
`orbital_period` lines 406 and 451, `position_accuracy` line 232; each
is read and told what a designation looks like. Grep for the callers
again at HEAD; the list is the repo's, not this brief's.

**4.6 The Horizons check's pinned branch becomes the designation
branch.** `check_entry`'s pinned branch (line 365 on) asks the record
and lists the designation's records to find a newer one. With no pin
it asks `DES=<d>;CAP`, reads the record number JPL answers, compares
it with the record the body's served elements came from (the
confirmations record's `pin.record` today; name it for what it now is,
JPL's current apparition), and a DIFFERENT record is a value change:
taken (3.2), logged "TAKEN encke.apparition: 90000091 -> <new>", the
elements and period re-fetched from the new record. The name still
holds: `horizons_name` differing is identity, held (3.1).

**4.7 THE EXPORT, AND THE WEBSITE, read before changing a byte of the
export.** The website's builder asks JPL by the `horizons_id` the
objects mirror copies from the export (REPLACED, 3.5), and asks with
no CAP: its `closest_apparition` hook (`resolve_comet_conic` line 1045,
`process_object` line 1233) reads an `overrides.comet` block no config
entry has and the mirror never writes. If the orrery exported a bare
designation tonight, the website's builder would ask `2P` as a
designation with no CAP, get 61 records, fail the fetch for all six
comets and serve last-good with today's date on it, every night, on the
live site. SO THE EXPORT KEEPS SERVING A RECORD NUMBER for each of the
six: the one JPL's CAP answer named THAT NIGHT, resolved by the orrery
and written as `horizons_id` with `id_type` smallbody, as today. No
number is typed anywhere; the website asks the record JPL named an
hour before. This is the coordinating session's reading of "no number
is used" (the orrery types none; the export carries JPL's own answer),
and it is method until Tony says otherwise. The website asking by
designation with CAP itself (the mirror writing the override, the
builder sending it) is written on L-470 for the same gallery session
as 3.5, not built here.

**4.8 The skill.** Small-Body Record Pinning (horizons-orbital-mechanics
1.13, lines 177 to 205) says the house pattern is to pin the record and
never re-pin; after this section that sentence would make a following
session re-pin a comet by hand. So if section 4 is BUILT, the skill
goes to 1.14 in this session (A Wrong Sentence in a Skill: bump now):
the pinning section rewritten as asking by designation with CAP, the
%3B trap (4.3), the astroquery form (`id_type='designation'`,
`closest_apparition=True`), the export's resolved record (4.7), and
the apparition change as a taken value. If section 4 is NOT built, the
skill is not touched and the sentence stays true.

## 5. gallery-cache-builder 1.15, and the protocol's entry (One Session, One Bump)

The lines already on L-485 for the skill's next version, from Oct 28,
30 and 31, each read from the code before it is written:
- Operating mode (lines 78 to 109, "manual, as of August 10 2026",
  "Tony runs it MANUALLY", "the scheduled nightly was retired") is a
  WRONG SENTENCE a session would act on: the builder runs unattended
  every night on GitHub's computer through `daily_run.py --night`
  since Oct 31; the pre-commit hook it calls "deliberately NOT built"
  is built as the night gate's deletions-only condition; the intro at
  lines 45 to 48 says the same wrong thing.
- Layer 3 (line 679) is live again, in the GitHub Action form: its gate
  is the night's, its health summary the night's record.
- The Daily Run's Steps (line 540 on) gains the night form, the guest
  book skipped by Tony's ruling of Oct 31 ("his morning's"), and the
  runner form of pull matches push; "A PULL THAT DOES NOT MATCH THE
  PUSH" gains L-461's second honest cause, "not yet pulled"; the
  Validation stance's "the console Tony is watching" is the night's log
  at night.
- From Oct 28: a comet is drawn from its elements of today, not "from
  its elements at perihelion"; a Daily Run onboards a new analytic body
  without --first-build; a config change turns the Solar System figures
  check red too, for a body the cache does not hold yet;
  `osculating_cache_manager.save_cache` writes in text mode (CRLF on
  Windows, LF on Linux, git normalizes).
- From this session: the export marks a held body (3.3) and the
  builder does not yet honour it; the website's half is a gallery
  item (3.5). A skill states what is built and what is not.
The skill's oldest of four version entries moves to
`documentation/SKILL_HISTORIES.md` (three resident). `skills_index.py`
rebuilds the manifest in PROJECT_INSTRUCTIONS.md; its version history
gains v3.119 in the shape of v3.118's entry (what prompted it, what
changed, what was not done and why, the obligation that the next
account-loading session confirms its copies read 1.15 and, if section
4 was built, horizons-orbital-mechanics 1.14), the header stamp and
the SHA anchor move, and v3.116 moves down to
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1 to keep three
resident. A copy `documentation/project_instructions_v3_119.md`, as
the previous versions have.

## 6. Records

- L-484 (the two agree): the rounding fault, its cause by line, the
  fix's shape, the five names, the pin moved; the gallery session's
  "which place is right is the orrery's question" answered: the hover
  was right. L-503 (the belt's cloud): the belt's 90th height now
  serves 100,000,000; it closes on Tony's phone look at the live site
  after the website's next pull.
- L-485 (a nightly run): the hold as built (3.1's sorting, 3.2, 3.3,
  3.4), by file; "for a gallery session: the hold's website half" with
  3.5's four facts and criterion (i); the dashboard's second line; the
  concurrency line; the skill's bump; what moved to the next orrery
  session if section 4 was not built.
- L-470 (JPL's permanent number): the six, JPL's answers of Oct 31 and
  of the session's own test, the %3B trap, the readers switched by
  name, the export's resolved record (4.7), the website asking with CAP
  as a gallery item, the future-only apparition noted.
- L-461 (pull matches push), L-490 (the legacy list): only if touched.
- Where We Are: the box rewritten (Changed: the export's rounding
  fixed and what the site will print; a night now takes a value and
  holds an identity, naming each; the comets asked by designation, if
  built; Do next: the push, the website's pull, the phone look at the
  belt's sentence); the road's L-485 line by what this did; the
  Deferred section gains the hold's website half and the website's CAP
  (behind the ruler build); the Settled list gains the ruling of 18:38
  in one line; the marker and the zone below it untouched; the
  ledger's index rebuilt.
- The maintenance run green, read from its output; the night form run
  in a spare clone as the Oct 30 and 31 sessions did, with "NIGHT RUN:
  CLEAN" read, and a planted hold and a planted take each seen in its
  record. Tier-1 = 0 on the active build path before Tony pushes.
- The final report, per the orrery's CLAUDE.md: the skills read with
  their version lines; section 3.1's sorting for Tony to read; the
  website sentences that change (section 1); every file changed with
  its edit count; Tony's run order; the Tony-action rollup. Tony
  pastes that report to the coordinating session before he commits.

## 7. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word. Read section 3.1's sorting there: it is a reading of your
   ruling, and one sentence from you changes it.
2. GitHub Desktop: Pull origin first if it shows a number (the night
   may have committed); then commit and push the orrery (the commit
   carries the fix, the hold, the pins if built, the skill, the
   protocol, this brief, the handoff and your run record).
3. The website's night at 08:17 UTC pulls the new export by itself; or
   run the gallery's Daily Run from the dashboard if you want it the
   same day. Then Pull origin on the gallery.
4. On your phone, after closing the saved tab: the belt's text box
   should read "about 100 million km" for the 90th height; and the
   Earth-room sentence the report names, if any.
5. Open the dashboard: two nightly lines, the orrery's and the
   website's, both reading a date within a day.
6. Send the orrery's SHA to the coordinating session.

## 8. Tony-action rollup

- (do) Open a Claude Code session on the orrery repository (the
  python_work door: the prompt names the orrery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 7.
- (decide) Nothing before the session. After it, one reading to
  confirm or overturn when you read the report: that an `id_type` or
  `object_type` disagreement is a project choice and so is HELD
  (section 3.1).

Written October 31, 2026 with Anthropic's Claude Fable 5.1.
