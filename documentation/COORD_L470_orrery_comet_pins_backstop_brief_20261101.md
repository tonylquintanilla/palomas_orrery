<!-- Doc-Kind: hand | Brief for the next orrery Claude Code session: the six periodic comets' record pins retired for the designation with CAP (section 4 of the Oct 31 brief, rebased on the hold as built); the orrery workflow's backstop line (11:17 UTC); L-484's lesson into gallery-cache-builder; L-503 closed; horizons-orbital-mechanics 1.14 and gallery-cache-builder 1.16 under protocol v3.120. Written by the coordinating session; zero code. -->
# Brief: the orrery session (the comet pins, the backstop line, the lesson)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | November 1, 2026, 14:10

Written at orrery 8f851c15cefb9ff0111ed1c622e47e48b5910396 at
https://github.com/tonylquintanilla/palomas_orrery (branch main; Tony's
push of the morning addendum's section 2b) and gallery
b6574a0fa374be2faf526d7c5e5b6f8988515652 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main; the website's night commit of 16:11 UTC). Both read live with git
ls-remote on Nov 1, 19:00 UTC, then cloned at those commits; every line
number below was read from them. YOUR BASE IS HEAD WHEN YOU OPEN THE
SESSION, which will be the commit that carries this brief and Tony's
run record, and may be a nightly commit or two newer; read it yourself
and anchor everything there.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the ORRERY repository. It REPLACES
section 4 of `COORD_L485_orrery_rounding_hold_pins_brief_20261031.md`,
which the session of Oct 31 stopped before, as that brief allowed; that
section was written at dc85f372, before the hold was built, and this
one is rebased on `horizons_check.py` as it is at HEAD. Read, in this
order: this file; the Oct 31 brief's sections 3 and 4 (the hold as
designed; the pins as first written); `HANDOFF_coordination_20261101_morning.md`
(section 2b, Tony's rulings of noon); `HANDOFF_coordination_20261031_night.md`.
The ledger items: L-470 (JPL's permanent number: the comets), L-485 (a
nightly run: the backstop line, the schedule's lateness), L-484 (the
two agree: the lesson into a skill), L-503 (the belt's cloud: closed).

The gallery is READ, never written, from this session. Two findings
below need a gallery build to finish (the website asking a comet by
designation with CAP, and six config notes that will say the wrong
thing); each is written on the ledger for the gallery session after the
ruler build, not built here.

## 0. The base, the skills, the order

- Orrery: HEAD, clean, after Tony's Pull origin (the nightly run
  commits at 07:17 UTC when GitHub is on time, up to seven hours later
  when it is not). Tony's run record for this session,
  `documentation/WHERE_WE_ARE_11-<d>-26_<hhmm>_run_record.md`, appears
  when he copies the page at your first run order; that one is
  expected. Anything else waiting is not.
- Gallery (the sibling folder): b6574a0 or newer (its own nightly run
  commits at 08:17 UTC, same caveat), clean, read only.
- Skills this job fires, each read in full before the work, versions
  stated in the first report against the manifest in
  PROJECT_INSTRUCTIONS.md v3.119: safe-file-editing 1.14,
  agentic-pre-test 1.3, ledger-and-session-records 1.22,
  provenance-discipline 2.36 with its `references/figures.md`,
  horizons-orbital-mechanics 1.13 (Which Record Serves a Body,
  Small-Body Record Pinning, Checking an Entry Against JPL, Where the
  Check Lives), gallery-cache-builder 1.15 (The Daily Run's Steps, A
  Pull That Does Not Match the Push), orrery-coding-conventions 1.12
  (docstrings). A Code session reads the repo's copies, which are the
  manifest's.
- Order of work: section 1 (the backstop line, one line, first and
  smallest); section 2 (the lesson into gallery-cache-builder, and the
  morning sentence); section 3 (L-503 closed, records only); section 4
  (the comet pins, the whole of the room); section 5 (the two skill
  bumps and the protocol's entry); section 6 (the records). A session
  running out of room stops BEFORE section 4 and says so plainly;
  sections 1 to 3 and 5 to 6 are then a complete session, with
  horizons-orbital-mechanics untouched (its pinning sentence stays
  true until the pins go), and section 4 moves on with this brief
  still its base.
- The session asks Tony ONE question in all. This brief leaves none
  open; what it cannot settle it names as the session's, and section
  4.6 names one method choice Tony may overturn when he reads the
  report.

## 1. The backstop line (L-485; Tony's ruling of Nov 1, 12:04 Chicago)

- The fact: GitHub's schedule is best-effort. Its page, read Nov 1:
  "The schedule event can be delayed during periods of high loads of
  GitHub Actions workflow runs" and "If the load is sufficiently high
  enough, some queued jobs may be dropped." Observed: Oct 31, the
  orrery's schedule 6 h 22 min late; Nov 1, the orrery's 7 h 0 min late
  (run 4, 14:17 UTC) and the website's 6 h 58 min late (run 3, 15:15
  UTC). Nothing was dropped yet; a dropped night and a late one look
  the same until it arrives.
- The ruling: both schedules keep their times (07:17 UTC the orrery,
  08:17 the website) and each gains a SECOND scheduled line, 11:17 UTC
  for the orrery and 12:17 for the website, so a night GitHub drops is
  caught the same day. No reschedule: the lag is GitHub's, not the
  clock's; the times are right relative to Tony's day (after his last
  push by about 06:00 UTC, before his morning when on time).
- The build, in `.github/workflows/nightly.yml`: under `schedule:`
  (line 35 on), after the existing `- cron: '17 7 * * *'` (line 42), a
  second line `- cron: '17 11 * * *'`, with a comment in the file's
  own voice naming L-485, the ruling (Nov 1, 12:04), GitHub's two
  sentences above (already quoted at lines 53 to 58 for the
  concurrency group; refer to them, do not repeat), and why a second
  firing is harmless: the concurrency group `nightly-run` (lines 63
  to 64) queues it behind a run still going, and a clean second run
  commits only its record, because the record carries its time stamp
  (seen Nov 1: b0acdea then 0c0bac8). The header comment (lines 1 to
  30) gains one "Updated November <d>, 2026" sentence. The file must
  still read as valid workflow YAML (the Oct 31 session checked this
  with a YAML load; do the same).
- Not built here: the website's line (12:17 UTC) rides the next
  gallery session, the ruler build, as Tony ruled; its workflow is not
  written from the orrery.
- The orrery's dashboard needs nothing: its nightly lines read the
  record, not the schedule.

## 2. The lesson into a skill, and the morning sentence (L-484, L-485)

- THE LESSON, written on L-484 by the gallery session of Nov 1 and
  confirmed by the coordinating session: a served number that changes
  on purpose is grepped in the OTHER repository's checks before the
  push; the website's acceptance lines (`documentation/smoke_display_figures.js`,
  ACCEPTANCE_LINES) and its hover fixture (`fixture_hovers_*.json`)
  consume the export as much as its renderers do; and the brief for
  such a change names the pins that move. Neither the orrery session
  of Oct 31 nor the coordinating session did; the website's night of
  Nov 1 went red on the inner Van Allen belt's old line and committed
  nothing, as designed.
- WHICH SKILL: this brief recommends gallery-cache-builder, at 1.16,
  under its "A PULL THAT DOES NOT MATCH THE PUSH" section or beside it
  as a new short section, "A Served Number That Changes on Purpose":
  that skill already describes what the website consumes from the
  export and the Daily Run that consumes it, and provenance-discipline
  binds at the export, not at the website's checks. The session may
  choose provenance-discipline instead if, reading both, it finds a
  better anchor there; say which and why in the report. One skill, not
  both.
- THE MORNING SENTENCE (Tony's ruling of noon, section 2b of the
  morning addendum): pull first; do not wait for the run; a run that
  lands later in the day comes with the next Pull origin. It goes to
  Where We Are's "Needs you now" (section 6) and to gallery-cache-
  builder's Daily Run section at the same bump, one sentence, with the
  observed lateness as its reason (the three times in section 1).
- The skill's version line, its Contents list (`skills_index.py
  --check`), and the three-resident rule for its version entries, as
  the Oct 31 session did for 1.15.

## 3. L-503 closed (records only)

Tony's phone look of Nov 1 (run record, the 16:11 UTC run's last step):
Earth's inner radiation belt "= 10,000 km (0.00006 AU)", the main
belt's 90th height "about 100 million km", both "yes". L-503's gap
reads "then DONE": write the close with the date and the two sentences
as read, and move it on Where We Are. No code.

## 4. The six periodic comets' record pins retired for the designation (L-470)

**4.1 The ruling, unchanged.** Tony, Oct 31, 18:45: "the third case
where a non permanent record number is reassigned is fragile: we
should use the permanent record." Each periodic comet is asked by its
permanent designation with JPL's CAP directive ("closest apparition",
the last apparition before the current date, the Horizons manual), as
the non-periodic comets are asked by JPL's permanent number since Oct
24 (L-470, "B"). JPL then follows a new apparition by itself, nightly;
a reassigned record number cannot bite because no number is typed
anywhere. Where We Are already lists it as Settled: "The comets are
asked by designation, not record number (Oct 31)."

**4.2 The six, and JPL's answers.** `celestial_objects.py` holds SIX
record pins (`'id_type': 'smallbody'`, id of the form 9000xxxx), read
at 8f851c15: Tempel 2 90000214 (line 585, 10P), Schaumasse 90000356
(596, 24P), Howell 90000901 (606, 88P), Churyumov-Gerasimenko 90000703
(616, 67P), Halley 90000030 (632, 1P), Encke 90000091 (642, 2P). The
other 9000xxxx numbers in the file are comments (C/2025 K1 and its
pieces, lines 662 and 770 to 772). The coordinating session's fetch of
Oct 31 (JPL's clock 19:05, Pacific), by designation with CAP,
`COMMAND='DES=<d>;CAP'`, each answer's `Rec #:` line:
- 2P: Rec #:90000091 (+COV) Soln.date: 2026-Oct-22_15:51:34, # obs: 1329 (2018-2026), EPOCH 2024-Jun-01
- 1P: Rec #:90000030, Soln.date: 2025-Nov-21_15:57:34, # obs: 8518 (1835-1994), EPOCH 1968-Jan-20
- 10P: Rec #:90000214 (+COV) Soln.date: 2026-Oct-22_15:52:05, # obs: 7130 (2003-2026), EPOCH 2017-Sep-21
- 24P: Rec #:90000356 (+COV) Soln.date: 2026-Jul-07_05:58:32, # obs: 3535 (2000-2026), EPOCH 2024-Jan-12
- 88P: Rec #:90000901 (+COV) Soln.date: 2026-Oct-14_16:22:22, # obs: 4019 (2014-2026), EPOCH 2021-Mar-05
- 67P: Rec #:90000703 (+COV) Soln.date: 2026-Sep-04_10:25:07, # obs: 8610 (2008-2025), EPOCH 2015-Oct-10
Every CAP answer equals today's pin. ASKED AGAIN ON NOV 1 from the
coordinating session: every answer came back with JPL's own clock
reading "2026-Oct-31 19:05" in its header, the same second as the Oct
31 fetch, whatever the address's parameter order; a `DES=2P;CAP;NOFRAG`
form came back dated "2026-Oct-03 01:02:47" with Soln.date 2026-Oct-01
and 880 observations (an older cached copy; it also shows 90000091
re-solved in place between Oct 1 and Oct 22, the skill's "a pin fixes
the apparition, not the numbers"). So the coordinating session's tool
serves cached copies of JPL's answers, and Oct 31 stands as the latest
fresh read. The session's own fetch (4.4) is the fresh one; record its
header dates.

**4.3 The trap, confirmed in the code.** A bare semicolon in the
address makes JPL ignore CAP and return Encke's whole list of 61
records; encoded as `%3B` it returns the one record (JPL's API page:
"API calls must encode semicolons as %3B in the URL"). At HEAD,
`horizons_check.record_list_url` (line 241) writes `%%3B` itself and
quotes the designation with `safe="/"`; `period_url` (line 525) quotes
`command_of`'s output with `safe="="`, so its trailing `;` becomes
`%3B`; `path_plan.vectors_url` and `sheet_url` (lines 339 and 352)
build on `hc.command_of`. Any new CAP address goes through the same
quoting, and the test in 4.4 reads the answer back through THAT code,
not only by hand.

**4.4 TEST BEFORE RETIRING, through the orrery's own two routes**
(criterion (iii): the whole answer, read back). The orrery asks JPL
two ways: astroquery (`Horizons(id=..., id_type=...)`; the night
tools and the plotting readers listed in 4.5) and raw URLs
(`horizons_check.command_of` and `period_url`, `path_plan.vectors_url`).
horizons-orbital-mechanics 1.13 (lines 182 to 186) records that
`closest_apparition=True` threw a syntax error with
`id_type='smallbody'`, because astroquery prepends `DES=` only for
`id_type='designation'` or `'name'`. So the test is: for each of the
six, ask with `id_type='designation'`, `closest_apparition=True`, with
and without `no_fragments=True`, through astroquery; and ask
`DES=<d>;CAP` (and `;NOFRAG`) through the raw-URL builder; read back
the designation, the name and the record number from each answer, and
confirm all four forms name the same record as 4.2 and as the pin.
Save the six raw answers, dated, into the recorded-answers file the
suite uses (`documentation/worksheets/horizons_answers_L395.json`, as
the suite's `recorded_fetch` reads it), so the new cases in 4.8 run
offline. One disagreement, and the pins stay, the report says which
form failed, and sections 1 to 3 and 5 to 6 are the session. A comet
with a future-only apparition would need CAP's date form; note it on
L-470, do not build it.

**4.5 Then switch every reader, as one change** (Which Record Serves a
Body: one record per body and centre, in every reader). The entry
keeps `horizons_name` and gains the designation as its handle; whether
that is `id: '2P', id_type: 'designation'` with a comet flag, or a new
field read by one helper that every reader calls, is the session's,
chosen so that EVERY reader asks the same question and none can forget
CAP. This brief's recommendation: one helper, so that a grep for
`Horizons(` outside it finds no comet. The readers of a comet's id, at
8f851c15: the night tools (`export_objects.served_identity` line 283
and the identity written at 403 to 405; `horizons_check.check_entry`
line 402 and `command_of` 512; `period_fetch.served_entries` line 185
and `plotting_fetch` 305; `path_plan` lines 321 to 333 and the
`vectors_url` sites); the orrery's own plotting (`palomas_orrery.py`
has two `Horizons(` sites and many callers of the helpers;
`palomas_orrery_helpers.fetch_orbit_path`, `orbit_data_manager`,
`osculating_cache_manager`, `idealized_orbits`, `spacecraft_encounters`,
`orbital_period`, `position_accuracy`, `close_approach_data`,
`orbital_param_viz`, `apsidal_markers`). Three functions recognise a
pinned record by the pattern `^9\d{7}$`: `horizons_check.PINNED` line
208 (and `LIST_ROW` 326), `orbital_period.py` lines 406 and 451,
`position_accuracy.py` line 232; each is read and told what a
designation looks like, and `test_position_digits.py` line 633 carries
the same pattern in a test. GREP FOR THE CALLERS AGAIN AT HEAD; the
list is the repo's, not this brief's.

**4.6 The Horizons check: the pinned branch becomes the designation
branch, and an apparition change is TAKEN.** As built at HEAD,
`check_entry`'s pinned branch (lines 402 to 434) asks the record, then
lists the designation's records and reports a newer one as a `pin`
disagreement; `HOLD_FIELDS` (line 218) includes `"pin"`, so the hold as
built would HOLD a comet whose apparition moved. Tony's ruling makes a
change of apparition a VALUE: taken and reported with the old and new
record numbers; the hold applies to IDENTITY alone (a designation
answering with a different name). So:
- The branch asks `DES=<d>;CAP` (encoded, 4.3), parses the one record
  with `parse_record` (line 329), and reads the record number JPL
  answers; `designation_of` (line 361) already gives "2P" from
  "2P/Encke". The record-list query (line 422) and the `pin` kind go;
  `"pin"` leaves `HOLD_FIELDS`; the confirmation's `pin` block (lines
  1115 to 1117) becomes an `apparition` block: {record, solution_date,
  asked}, named for what it now is, JPL's current apparition.
- JPL's name differing from `horizons_name` is still identity, held
  (line 412's branch stays).
- A record number different from the one the body's served elements
  came from (the confirmation's apparition.record) is a value change:
  routed into the take, not the hold: run() (lines 1021 to 1077) takes
  it as it takes a period, through `make_taker` (line 1338), which
  re-fetches the elements and period together by period_fetch's path,
  and logs "TAKEN <key>.apparition: <old record> -> <new record>" in
  the record's taken list and on the verdict line. `check_horizons_confirmations.py`
  prints it as it prints a taken period (line 192 on).
- THE CADENCE, a method choice written here for Tony to confirm or
  overturn when he reads the report: a comet asked by designation is
  asked EVERY RUN, as a held body is (lines 914 to 919), not every 30
  days: six queries a night, so the record number the export serves
  (4.7) is never more than a night old, which is the whole point of
  the ruling. If Tony overturns it, the 30-day cadence applies and the
  export serves the record of the last confirmation, up to 30 days old.
- The checker (`check_horizons_confirmations.py`) and the dashboard
  line need no new state: taken is taken.

**4.7 THE EXPORT, AND THE WEBSITE, read before changing a byte of the
export.** Read at b6574a0: the website's builder asks JPL by the
`horizons_id` the objects mirror copies from the export
(`tools/mirror_objects.py` REPLACED, line 133: name, horizons_id,
id_type; nothing else is copied), and asks with no CAP: its
`closest_apparition` hook (`tools/gallery_cache_builder.py` lines 762
to 763, `resolve_comet_conic` 1046 to 1049) reads an `overrides.comet`
block no config entry has and the mirror never writes; a pinned
record number is recognised "whatever its id_type" (line 600). If the
orrery exported a bare designation, the website's builder would ask
`2P` as a designation with no CAP, get 61 records, fail the fetch for
all six comets and serve last-good with today's date on it, every
night, on the live site. SO THE EXPORT KEEPS SERVING A RECORD NUMBER
for each of the six: the one JPL's CAP answer named at the last ask
(4.6; `apparition.record` in the confirmation, which `export_objects`
already reads: `confirmation_of`, line 563), written as `horizons_id`
with `id_type` smallbody, as today, and the period block's `target`
the same record. No number is typed anywhere; the website asks the
record JPL named a few hours before. The Horizons check runs before
the Objects export in the night set, so the export reads that night's
answer. A comet never confirmed under the new branch has no record to
serve: `ExportError` naming it, not a bare designation. The export's
schema stays 4; an informational field (the designation, the
apparition's date) may be added, since the mirror copies only the
three, but nothing the website must read is added. PROVE IT the way
the Oct 31 session proved the rounding: save `data/objects_export.json`
before the switch, diff it after, and the report says the six
`horizons_id` and `target` values are unchanged and names every field
that moved. BY THE LESSON OF SECTION 2: the gallery's checks were
grepped for the six record numbers at b6574a0 by the coordinating
session: they occur in `data/objects_config.json` and
`data/objects_export.json` (the mirror's copies, rewritten by the
pull), `tools/test_gallery_cache_builder_offline.py`,
`tools/debug_encke_tp.py` and seven patch files under documentation;
no acceptance line and no fixture pins them, so NO WEBSITE PIN MOVES
as long as the served numbers do not; the diff above is the proof.
The website asking by designation with CAP itself (the mirror writing
the override, the builder sending it) is written on L-470 for the
gallery session after the ruler build, not built here.

**4.8 The suites.** `test_horizons_check.py` section 7 (the take and
the hold; `take_and_hold`, line 351) gains: a designation entry whose
CAP answer names the same record (agrees, apparition recorded); one
whose CAP answer names a NEW record (taken, the line reads "TAKEN
encke.apparition: 90000091 -> <new>", the elements re-fetched through
the taker); one whose CAP answer names a different NAME (held, as
before); and the %3B form planted wrong (a bare `;`) caught by name.
Each planted fault fails by name, read from the suite's output;
`test_maintenance_report.py` and the export check (`test_objects_export`
and the Objects export check row) accept the new shape and refuse a
bare designation in `horizons_id`.

**4.9 The night form, in a spare clone,** as the Oct 30 and 31
sessions did: "NIGHT RUN: CLEAN" read, the six comets asked and their
apparitions recorded, with one planted apparition change seen as TAKEN
in the record and one planted name change seen as held.

**4.10 Found, for the gallery session, not fixed here.** The website's
`data/objects_config.json` carries six `notes` fields written when the
comets were keyed (Encke's at line 1757, Halley's at 1777, and the
four of Oct 22) that explain the pin and say the orrery's check
"reports one for a person to decide"; after this session that is a
wrong sentence about the orrery. Whether `notes` reaches a visitor is
the gallery session's to read; write it on L-470 beside the website's
CAP.

## 5. The skills, and the protocol's entry (v3.120)

- horizons-orbital-mechanics 1.14, if and only if section 4 is built
  (A Wrong Sentence in a Skill: bump now, because Small-Body Record
  Pinning, lines 177 to 205, says the house pattern is to pin the
  record and never re-pin, and a following session would re-pin a
  comet by hand): that section rewritten as asking by designation with
  CAP; the %3B trap (4.3); the astroquery form (`id_type='designation'`,
  `closest_apparition=True`); the export's resolved record (4.7); the
  apparition change as a taken value and the nightly ask (4.6); the
  future-only apparition noted. Which Record Serves a Body: "A PINNED
  COMET GOES STALE" (lines 121 to 127) rewritten for the same reason.
  Where the Check Lives gains the lines carried on L-485 since Oct 30
  and 31 (the night form; the take and the hold; a refused question
  reported), read from the code before they are written. Its oldest
  version entry moves to `documentation/SKILL_HISTORIES.md` (three
  resident).
- gallery-cache-builder 1.16 (section 2), whether or not section 4 is
  built.
- The protocol: `skills_index.py` rebuilds the manifest; the version
  history gains v3.120 in the shape of v3.118's entry (two bumps under
  one version: what prompted each, what changed, what was not done and
  why, the obligation that the next account-loading session confirms
  its copies read 1.14 and 1.16), the header stamp and the SHA anchor
  move, and v3.117 moves down to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1 to keep three
  resident. A copy `documentation/project_instructions_v3_120.md`, as
  the previous versions have. "One Session, One Bump" is one protocol
  version per session, not one skill: v3.118 carried four skills.

## 6. Records

- L-470 (JPL's permanent number): the six, JPL's answers of Oct 31 and
  of the session's own test with their header dates, the cached-copy
  finding of Nov 1 (4.2), the readers switched by name, the export's
  resolved record and the diff (4.7), the nightly ask (4.6), the
  website's CAP and the six notes as a gallery item (4.7, 4.10), the
  future-only apparition noted; West's id (C/1975 V1-A) stays on its
  gap unless the session has room, in which case it is one entry and
  one Horizons check line.
- L-485 (a nightly run): the backstop line built, with the ruling and
  the three observed start times; the website's run 3 (scheduled,
  15:15 UTC, red on the same pin before the fix was pushed) and run 4
  (16:11 UTC, clean, b6574a0) of Nov 1, which the item does not yet
  carry; the website's line and the morning sentence for the gallery
  session; the apparition taken as a new kind of take (4.6).
- L-484 (the two agree): the lesson's skill and section named.
- L-503 (the belt's cloud): DONE (section 3).
- Where We Are: the box rewritten (Changed: the comets asked by
  designation, if built, and what the website will NOT change; the
  backstop; L-503 closed; Do next: the push, the morning routine's new
  sentence; Needs you now: pull first, do not wait for the run, a late
  run comes with the next Pull origin); the road's 11b line (the
  orrery's backstop built, the website's with the ruler build) and 5c
  line (closed); the Settled list unchanged (the designation line is
  there); Deferred: the website's CAP and the six notes behind the
  ruler build; Signals read from files; the marker and the zone below
  it untouched; the ledger's index rebuilt; the page's cap of 130
  lines above the marker kept (the Oct 31 session trimmed to 130; read
  the count before and after).
- The maintenance run green, read from its output, 33 of 33 or the
  count the run prints; the night form in a spare clone (4.9);
  Tier-1 = 0 on the active build path before Tony pushes; the encoding
  gate (ASCII, LF) on every file changed, run after the ledger script
  as the Oct 31 session had to.
- The final report, per the orrery's CLAUDE.md: the skills read with
  their version lines; 4.6's cadence for Tony to confirm or overturn;
  the six comets' header dates from the session's own fetch; the export
  diff's verdict in one line; what the website will print after its
  next pull (expected: nothing changes); every file changed with its
  edit count; Tony's run order; the Tony-action rollup. Tony pastes
  that report to the coordinating session before he commits.

## 7. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word. Read 4.6's cadence there: it is the brief's reading, and one
   sentence from you changes it.
2. GitHub Desktop: Pull origin first if it shows a number (the night
   may have committed, at 07:17 UTC or hours later); then commit and
   push the orrery (the commit carries the workflow line, the comets if
   built, the two skills, the protocol, this brief, the handoff beside
   it and your run record).
3. The website's night (08:17 UTC, or 12:17 once its own backstop is
   built) pulls the new export by itself; or run the gallery's Daily
   Run from the dashboard if you want it the same day. Then Pull origin
   on the gallery. Its night should be CLEAN with nothing printed
   changing; a red Display figures or Solar System figures row is news,
   and its log is the record.
4. On your phone, after closing the saved tab: Encke's row in the Solar
   System room, its hover unchanged, its orbit where it was.
5. The orrery's Actions tab the next morning: a run at 07:17 UTC or a
   late one, and, if GitHub dropped the night, one at 11:17; both
   clean; two record commits at most.
6. Send the orrery's SHA to the coordinating session.

## 8. Tony-action rollup

- (do) Open a Claude Code session on the orrery repository (the
  python_work door: the prompt names the orrery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 7.
- (decide) Nothing before the session. After it, one method choice to
  confirm or overturn when you read the report: the six comets asked
  every night, not every 30 days (4.6).

Written November 1, 2026 with Anthropic's Claude Fable 5.1.
