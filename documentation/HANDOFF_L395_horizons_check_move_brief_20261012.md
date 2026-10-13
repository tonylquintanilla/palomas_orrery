<!-- Doc-Kind: hand | Brief for the session that moves the Horizons check from the website's daily run into the orrery's maintenance run, beside the objects export, and adds the spacecraft data sheets' 30-day re-read (L-395). Tony's rulings of 2026-10-12. -->
# Brief: the Horizons check moves to the orrery (L-395)

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery; it arrives with
`patch_L401_4_look_close_20261012.py`. Gallery read at
f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; it is
not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Opus 5.5.

- Type: DESIGN SESSION record and build brief (zero code).
- Companions: the check's design,
  `documentation/DESIGN_L395_horizons_check_20261007.md`; its build
  record, `documentation/HANDOFF_L395_horizons_check_build_20261010.md`;
  the survey of the spacecraft data sheets,
  `documentation/SURVEY_L401_spacecraft_data_sheets_20261012.md`.
- Supersedes one ruling: Tony's placement of 2026-10-07, the check as
  step 2 of the website's daily run.

## 0. Before building

- Build only on an orrery HEAD that carries patch_L401_4 (this brief
  is in `documentation/`, and L-401's ledger block records Tony's
  look). If it does not, stop: this build edits files that patch
  edits (the ledger, Tony's page).
- Confirm the loaded horizons-orbital-mechanics reads 1.3 (the
  obligation L-401's build 1 left).
- Pin each repository's SHA separately; this build touches both.

## 1. What Tony ruled, 2026-10-12

- The check belongs with the data. Tony: "shouldn't the horizons check
  live in the orrery repo? the orrery stores and serves the data not
  the other way around."
- It becomes part of the exporter's routine. Tony: "can we make the
  Horizons check part of the exporter routine?" The routine is the
  orrery's maintenance run, which runs `export_objects.py` every time.
- The shape below, as Claude described it, confirmed: "Yes." On JPL
  being unreachable: "Horizons seldom is down. The last time was the
  Pasadena wild fire last year."
- What happens when the orrery's maintenance run is not run for a
  while, as Claude described it, confirmed: "Yes that works."
- Already ruled the same day, from L-401: the spacecraft data sheets
  are re-read on the check's 30-day cycle. Tony: "agree. let's add it
  to the horizons check that runs every 30 days i believe."

## 2. The shape

- **Where it runs.** A row of the orrery's maintenance run, beside the
  objects export. It looks first for entries that are due (never
  confirmed, confirmed 30 or more days ago, or changed since) and asks
  JPL about those only. On most runs it asks JPL nothing.
- **The data sheets.** The same row re-reads each spacecraft's
  Horizons data sheet on the same 30-day cycle, and reports a sheet
  whose "Revised:" date moved or whose stated uncertainty changed. It
  never edits a row of `constants_new.py`; a person does, by a patch.
- **The record.** The confirmations live in the orrery's `data/`
  folder, and the export carries them: each exported object says when
  JPL last confirmed it, and what was confirmed.
- **The website.** Step 2 of its daily run goes away. Its offline check
  stays, in its maintenance run, and reads the confirmation dates from
  the pulled export instead of keeping its own record.
- **The network.** This is the orrery maintenance run's first row that
  needs the internet, and only on days something is due: a couple of
  minutes, one query at a time with a pause between. When JPL cannot be
  reached that day, this row is red and says why. Every other row runs
  as before, and the entries stay due for the next run.
- **When the orrery's maintenance run is not run for a while.** The
  website's daily run still runs every day, and its offline check
  compares the dates in the pulled export with today. On the day an
  object's confirmation turns 30 days old, its "Horizons confirmations"
  row goes red and names the overdue objects; the fix is to run the
  orrery's maintenance run and push. The dates in an old copy keep
  aging, so this works even if no new export was pulled. The website
  still builds and serves; the red row is a report, as it is today.

## 3. What does not change

Everything the check's design ruled on 2026-10-07 carries over as it
is: the Lookup search by index and the primary-id filter; the other
index must find nothing; pinned comet records through the main service,
newest-record check, never re-pinned; what is compared (id, id_type,
horizons_name, object_type only where it means something); one query
at a time with a pause, no retries, the run stops asking after the
first unreachable answer; an unreachable JPL never passes; it never
edits the list. The scope stays the keyed entries (the thirteen the
website serves) for identity, plus the spacecraft sheets.

## 4. Build notes (method; the build session settles these and records them)

- **Order inside the maintenance run.** The export must carry the
  dates written on the same run. Either the check runs before the
  "Objects export" generator, reading the list through
  `export_objects.py`'s own reader, or the export is written after it.
  The check's output on a day it asked JPL must be visible in the run's
  summary, not only in its own lines.
- **Carry the dates over.** The website's
  `data/horizons_confirmations.json` holds thirteen confirmations
  dated 2026-10-10, due 2026-11-09. Carry them into the orrery's record
  with their dates and queries, so the move does not re-ask JPL. If the
  build lands after 2026-11-09, the first orrery run asks for all
  thirteen, which is also fine.
- **The export.** `export_objects.py` is deterministic and fingerprints
  `celestial_objects.py`; it now also reads the confirmations record.
  `test_objects_export.py` must know that, and refuse an export whose
  dates do not match the record. The website's `tools/mirror_objects.py`
  must ignore the new fields, not fail on them.
- **The website's offline check.** `tools/check_horizons_confirmations.py`
  imports its due rule from `tools/horizons_check.py`, which leaves.
  The website never reads orrery source, so it gets its own copy of
  the rule, small and tested, and the export carries `cadence_days`.
- **What moves.** Into the orrery: `tools/horizons_check.py`,
  `tools/test_horizons_check.py` and
  `documentation/horizons_answers_L395.json` (the recorded answers the
  tests run on). Out of the website: daily run step 2, the "Horizons
  check suite" row of its maintenance run, and its confirmations file
  once the dates are carried. Git keeps their history in the website's
  repository.
- **The sheets' record.** A new file in the orrery's `data/`, seeded
  from the survey of 2026-10-12: each spacecraft's Horizons id, its
  "Revised:" date and its stated uncertainty in JPL's words. Which
  spacecraft: every list entry with a spacecraft id; one not yet in the
  record is reported as not yet read until its first read. Check
  against the survey that the two sets agree before seeding.
- **Testing.** This sandbox cannot reach JPL. Every network answer in
  the tests is recorded, and every fault is planted first: a moved
  "Revised:" date, a changed uncertainty, a sheet that no longer states
  one, a spacecraft missing from the record, JPL unreachable on a due
  day, nothing due (no query asked), and the website's check on an
  export 31 days old.
- **Dashboard.** `palomas_orrery_dashboard.py` has "Horizons Check" in
  its Daily Run group, running the website's copy, with "Horizons Check
  Suite" and "Horizons Confirmations" among the gallery checks. The
  check and its suite move to the orrery's groups and run the orrery's
  copies; "Horizons Confirmations" stays with the gallery checks (every
  check keeps its button, Tony, 2026-10-10).
- **Skills.** horizons-orbital-mechanics (where the check lives, the
  sheets), gallery-cache-builder (the daily run's steps) and any other
  skill sentence naming the check's place: find them by search, one
  version each, under One Session, One Bump.

## 5. For Tony, one at a time, in the build session

- (decide) **How a changed sheet is cleared.** The check reports a
  moved "Revised:" date and never edits a row. Something must then
  accept the new date, or the row stays red forever. The build session
  brings Tony the options with a recommendation. A report that cannot
  fail is not a check, so "report and pass" is not one of them.
- (decide, recorded, not urgent) **Whether the identity check widens**
  past the thirteen keyed entries now that it lives beside the whole
  list. The default is no: the website serves thirteen, and widening is
  a later round (The Braid).

## 6. Tony's actions, all of them

- (do) Run patch_L401_4 and the maintenance run, push. This brief
  rides that patch.
- (do) Start the build session from this brief after that push, when
  it comes in your order.
- (decide) The two items in section 5, in that session.

Brief written October 2026 with Anthropic's Claude Opus 5.5.
