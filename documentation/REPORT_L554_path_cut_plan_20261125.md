<!-- Doc-Kind: hand | The plan (Part 1) for L-554's build: BepiColombo's path cut at JPL's fit date, 17 November 2026, with its seven approved sentences and a night's check on JPL's sheet. Read-only; no code edited. For the coordinating session to read against the code before Tony's go-ahead. Communication; written once. -->
# Plan: BepiColombo's path cut at JPL's fit date (L-554, Part 1)

Read on Tony's working copies, not on a clean base:
- orrery 18df08b735655b75435566fbba22db6ec7cbbc21 at
  https://github.com/tonylquintanilla/palomas_orrery (branch main);
- gallery 3fb13a27763600b08cb67f710167d7fafa52153c at
  https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
  main).

Both were read 2026-11-25, late afternoon, Chicago.
- The website folder is clean and equals GitHub.
- The orrery folder holds the coordinating session's four records, not
  yet committed: the ledger, Where We Are, the brief and the words file.
- GitHub's orrery is one commit ahead of the folder: 9de39f3c, the
  night's bot, `data/nightly_run_record.json` only.

Tony was away from his computer and asked for the plan from the folder
as it stands ("Can you read them from my local folder?"). Part 1
edits no code. Part 2 waits until the orrery's records are committed,
the night's commit pulled, and both pushed.

Written November 25, 2026 with Anthropic's Claude Opus 5.5, a Claude
Code session through the python_work door, by
`documentation/COORD_L554_path_cut_brief_20261125.md`.

Skills read, the repository's copies, in the parts this job fires:
- horizons-orbital-mechanics 1.20
- gallery-cache-builder 1.24
- interactive-exhibit 1.45
- provenance-discipline 2.37
- orrery-coding-conventions 1.14, its six consumers
- agentic-pre-test 1.4
- safe-file-editing 1.15

## The brief against the code: no sentence disagrees

The brief named three readings to check against the code. Each holds.

- **`plan_inputs` counts a `path_cutoff`** (`path_plan.py`, the
  "L-507, more voyages" lines), so setting one makes the plan again.
  `path_stop` takes the earlier of `mission_end` and `path_cutoff`, so
  a flying craft with a cut alone stops at the cut.
- **The page ignores a flying craft's `cutoff_note`.**
  `interactive.html`, `const pastPath = ended &&
  !solarSystemMissionEndDay(b);`: a craft with no `mission_end`, past
  its path's last point, opens with `PAST_PATH_OPENING`.
  `cutoff_note` is read only in the `early` branch, which needs a
  `mission_end`.
- **`fetch_path_revised` reads the fit sentence and the first file
  named** (`read_path_revised`).

Three findings that the brief does not contradict, but the plan must
carry:

1. `fetch_path_revised` runs only inside `process_capture`, for a
   capture craft. Once the cut takes the arrival out of the plan,
   BepiColombo is no capture craft, and the website's night stops
   reading its header. A check on JPL's sheet therefore cannot lean on
   it.
2. The figures check's `missionEndIssue` turns red on an `end_note`
   with no `mission_end`. It holds a `cutoff_note`'s day to the path's
   last day only for an ended mission. The served cache's ended branch
   also labels the craft "(ended)". So the check changes with the page.
3. JPL's sheet for -121 carries both things the night must watch, in
   the same answer the orrery's Horizons check already asks
   (`OBJ_DATA=YES&MAKE_EPHEM=NO`). Read live today:

   > Revised: Nov 23, 2026 ... Trajectory for MPO from ESA. Data fit
   > through 2026-Nov-17, prediction thereafter.

   with the table row `bc_mpo_fcp_00243_20181020_20270411_v01
   2018-Oct-20 02:14  2027-Apr-10 23:59`. The fit sentence wraps
   across two lines in the answer.

## 1. The six consumers, and what the cut does to each

The plan's span is the one field every consumer reads, so the cut
reaches all of them through `data/path_plans.json`:
`path_cutoff` -> `path_stop` -> span end 2026-11-17.

| Consumer | Where | What the cut does |
|---|---|---|
| Static plot | `plot_objects`, palomas_orrery.py | The path is drawn by its plan (`path_drawing.draw_plan`) to 17 Nov, with the last-day pair (00:00 and 00:01 UTC), all of it solid. **The marker does not follow by itself.** `path_drawing.last_day` returns None for an entry with no `mission_end`, so `marker_moment` asks JPL for the day chosen: today, where the prediction puts it. **Change:** `last_day` also returns the plan's last day for an entry with a `path_cutoff`. The marker then sits on 17 Nov 00:01, and the hover's "Position at:" says that day. The console line reads "[PATH CUT]", not "[ENDED MISSION]", for a craft with no `mission_end`. |
| Animation | `animate_objects`, palomas_orrery.py | The frames after 17 Nov hold the marker there (`hold_last_day`, through the same `last_day`). Today they hide it, past the span. |
| Social export | `export_social_view`, palomas_orrery.py | It re-renders the last plotted figure, so it follows the two rows above. No change. |
| Gallery curation | `tools/gallery_studio.py`, website | It curates saved orrery pictures and fetches nothing. A saved picture keeps what it drew (L-520 (old pictures carry old words)). No change. |
| JSON conversion | `tools/json_converter.py`, website | The same. No change. |
| Website rooms | builder, then `gallery/assembler/`, then `interactive.html` | The mirror copies the new plan. The builder sees a new plan (made, span), clears the saved points and fetches the path whole to 17 Nov, with the last-day pair. The arrival leaves the plan, so there is no capture, no fine layer and no capture block (finding 1). `render_spacecraft` marks the craft `ended` past its last point, with a zero error. The box takes the seven sentences (section 4). |

An orrery plot centred on Mercury reads the same plan's span, so it
stops on 17 Nov too.

## 2. Where each of the seven sentences lives

The two fields that exist carry sentences 1 to 4 in the approved
order. Nothing is added to the entry for the words.

- **`cutoff_note`** = sentences 1, 2 and 3, as one bullet, as
  Akatsuki's two sentences are one. It opens the box in place of
  `PAST_PATH_OPENING`:
  "The path is drawn to 17 November 2026, the last day JPL's path is
  fitted to data, and the marker is where it was that day. JPL calls
  its path after that day a prediction, and it is not drawn. ESA
  reports that the entry burn ended early and the craft is in a
  75-hour orbit, not the planned 58-hour one; JPL's prediction still
  shows the planned orbit."
- **`end_note`** = sentence 4, its own bullet. The page already prints
  `end_note` after the opening for any ended path:
  "It entered orbit around Mercury on 21 November 2026."
- **The page**, for any craft with a `cutoff_note` and no
  `mission_end`, shown past its last point:
  - Sentence 5 is `ENDED_EARLY_DISTANCE_WORDS`, reused.
  - Sentence 6 is a new constant, `CUT_PATH_WORDS` + starts + " to " +
    ends + ".", from the served path's own days.
  - Sentence 7 is the source line's end, ", as far as JPL's data is
    fitted".

The page tells the cut craft by `pastPath && cutoff_note`. A flying
craft with no `cutoff_note` keeps this morning's words, and every
ended mission keeps its branch.

The export (`export_objects.py`) already writes `cutoff_note` and
`end_note` wherever an entry sets them, and the mirror already copies
both. Only their documented meaning widens ("an ended mission's" also
covers a cut on a flying craft), in the export's and the mirror's
docstrings.

Each typed day is held by a check:
- `path_cutoff`'s 17 November is held to JPL's fit date by the night
  (section 5).
- The 17 November in `cutoff_note` is held to the served path's last
  day by the figures check (widened, section 7).
- The two days in sentence 6 are the served path's own.
- 21 November 2026 in sentence 4 is ESA's, cited on the entry. JPL's
  plan has it today, at 2026-11-21 18:48, and loses it with the cut.

The entry's sources sit beside the fields, as Akatsuki's do:
- JPL's sentence, its file name and "Revised: Nov 23, 2026", read
  2026-11-25 through the horizons.api URL;
- ESA's page with its address, read 2026-11-25, 14:12 Chicago, and its
  words on the orbit;
- Tony's 14:41 ruling, "Stay with JPL and 11/17 until refit", and his
  approvals of 14:52 and 14:58.

## 3. What the new plan holds, and who read the arrival

BepiColombo's plan today (`data/path_plans.json`, made 2026-11-04,
span 2018-10-21 to 2027-04-10) holds 32 events. Remade with the span
ending 2026-11-17, it keeps every event before that day, including
the Mercury flyby of 2026-10-26 and the Sun's pass of 2026-11-10. Two
events leave:
- the arrival at Mercury, 2026-11-21 18:48, `stays: true`;
- the Sun's pass of 2027-02-06.

Every reader of that arrival, and what it does without it:

- **The page's companions** (`_path_events`): they collect the bodies
  of flybys, arrivals and departures. Mercury stays, through its six
  flybys, so the drawer's companions are unchanged.
- **The builder's capture** (`captures_of`, `capture_of`,
  `process_capture`): BepiColombo is no longer a capture craft. No
  fine layer is made, and no capture block or check points are
  written.
  - The saved `fine` layer in `raw/bepicolombo.json` and
    `raw/checks/bepicolombo.json` stay on disk. Nothing reads them for
    a craft with no capture.
  - L-553's `capture_hold` holds nothing for it.
  - The night's record no longer prints JPL's header for it.
- **L-538's figures** (`tools/test_curve_error.py`): they hold capture
  craft chosen by the builder's own rule, so BepiColombo leaves and
  Juno stays. To verify in Part 2: no count of capture craft is
  pinned, and leftover check points for a craft that is no longer
  captured are not read as a failure.
- **The figures check**: today BepiColombo is a flying craft that
  serves `as_of_today`. After the cut it serves none, as an ended
  path, and enters part 7's ended branch. That is finding 2, met in
  section 7.
- **Orrery**: `path_plan.riding_passes` filters Sun passes inside a
  capture. With no capture and the span ended, nothing is left to
  filter. No orrery test names BepiColombo.
- **Encounters** (`data/encounters/`): only ESCAPADE's Earth flybys.
  Nothing reads BepiColombo's arrival.

## 4. The box, before and after

**Today**, a visitor in the Solar System room, BepiColombo ticked,
spacecraft part:
- "<d> AU from the Sun (<km> km)", then the sentence that JPL serves
  no accuracy for it;
- "Its path is solid where it has already flown, and dashed where
  JPL's predicted path takes it next, as far as 10 April 2027.";
- `SPACECRAFT_DATES_WORDS`;
- the source line, "... from 21 October 2018 ... UTC to 10 April 2027
  ... UTC, as far as JPL's data runs, retrieved ...".

The marker sits on JPL's planned 58-hour loop at Mercury.

**After**, from the first website night after the orrery's push, on
any day shown after 17 November:
1. "The path is drawn to 17 November 2026, the last day JPL's path is
   fitted to data, and the marker is where it was that day. JPL calls
   its path after that day a prediction, and it is not drawn. ESA
   reports that the entry burn ended early and the craft is in a
   75-hour orbit, not the planned 58-hour one; JPL's prediction still
   shows the planned orbit."
2. "It entered orbit around Mercury on 21 November 2026."
3. "<d> AU from the Sun (<km> km) on the last day drawn", then the
   accuracy sentence as before.
4. "Its path is solid all the way, since the day shown is past the
   last day drawn, from 21 October 2018 to 17 November 2026."
5. `SPACECRAFT_DATES_WORDS`, unchanged.
6. The source line: "... from 21 October 2018 ... UTC to 17 November
   2026 ... UTC, as far as JPL's data is fitted, retrieved ...".

The marker sits where the craft was on 17 November, about 169,000 km
from Mercury's centre (the coordinating session's live read), so on
Mercury at the room's scale.

The boxes that do not change by a letter:
- the 7 ended missions (Akatsuki's cut included);
- every flying craft with no cut, before or past its path's end
  (this morning's words);
- every comet.

**Not covered by the approved words: a day shown before 17 November**
(a shared address from the served window, which starts 29 August).
The path is then solid to the day shown and dashed to 17 November.
The box would say "dashed where JPL's predicted path takes it next,
as far as 17 November 2026", and "as far as JPL's data runs" in the
source line. Both are true-ish but not the cut's words. The plan
leaves that box as the code makes it and records it on L-554 for
Tony. It does not invent words.

## 5. The night's check: where it runs, and how it knows the cut

**The orrery's night**, for three reasons:
- the entry and its cut live in the orrery;
- `horizons_check.py` already reads every spacecraft's sheet into
  `data/spacecraft_sheets.json`, by the same question that carries the
  fit sentence and the file name;
- the website's reading of the header stops with the capture
  (finding 1).

The parts:
- **What the entry was cut on.**
  - `path_cutoff`, the day, already there.
  - One new field, `cutoff_file`:
    `'bc_mpo_fcp_00243_20181020_20270411_v01'`, JPL's path file the
    cut was made on, with its source comment.

  The file cannot be read from anywhere else at the time of the cut.
  The night must compare against what the session saw, so it is typed
  once, on the entry, and taken off with the cut. Nothing smaller
  holds it: a value seeded into the tool's own record would move when
  the record does.
- **The read.** `horizons_check.py` asks the sheet of every entry
  that has a `path_cutoff` and no `mission_end` every night, not on
  the 30-day cycle. Today that is one question, for -121. It records
  the sheet's fit sentence and its first file name on that sheet's
  record (`fit`, `file`, the day read). The parse is the website's
  `read_path_revised`, copied, since the repositories cannot import
  each other, and run against today's text as a fixture. Akatsuki
  has a `mission_end`, so it is not asked: its cut is for good.
- **The check.** It goes in `check_horizons_confirmations.py`, the
  checker that already judges the Horizons check's records and has a
  `--night` mode.
  - A pass prints both values compared, for example "BepiColombo's
    cut holds: JPL's fit 2026-Nov-17 = path_cutoff 2026-11-17; JPL's
    file bc_mpo_fcp_00243_20181020_20270411_v01 = cutoff_file (sheet
    read 2026-11-26)".
  - A change in either is named, with what it changed to, for example
    "BepiColombo: JPL's fit date changed from 2026-Nov-17 to
    2026-Dec-04; read its new path, then take the cut and its words
    off the entry".
  - A sheet with no fit sentence or no file row, or one not read
    tonight, announces itself and never passes.

**How it sits with L-485's rulings (the nightly run).** It sits
badly, said plainly.
- A red orrery night commits nothing. JPL changing its sheet would
  freeze every other night-written file (periods, confirmations,
  plans, the export) until a session edits the entry. It is an outside
  event halting the night, which R4 rules out ("an outside failure is
  reported, never halting").
- The case nearest it was ruled the other way. L-539's JPL DIFFERS
  (JPL giving an entry another name or kind) is a flag at the start of
  the night's commit title (`NIGHT_TITLE_FLAGS`), not red. EL NINO
  DUE is the same shape, and Where We Are tells Tony what to do when
  he sees it.

**The loudest report that fits, proposed; the choice is Tony's:**
- **At night:** a clean night whose commit title starts **JPL REFIT**,
  with the row's line naming which value changed and to what.
- **By day:** the same check is red in the orrery's maintenance run,
  which every orrery session runs before it closes. The first session
  after the change cannot close with it standing, and Where We Are
  carries a "(do)" line for JPL REFIT beside EL NINO DUE's.
- **The other choice, the brief's as written:** red at night, with
  the freeze described above.

Whichever is chosen, nothing un-cuts by itself. The entry keeps its
cut until a session reads JPL's new path and takes the cut, the file
and the words off together.

## 6. Tony's two pushes, and what a visitor sees

**The website first, then the orrery.** The website pulls the
orrery's export from GitHub, not from the folder beside it.

- **After the website's push:** the page knows the cut's words, but
  no craft carries a cut yet. Visitors see no change.
- **After the orrery's push**, with the remade plan, the export and
  the entry's new fields: the next website night (08:00 UTC, 2 am
  Chicago) pulls them, refetches BepiColombo whole and serves the
  cut. If both pushes are in before then, the website shows the cut
  on that night's build.
- **The reverse order is safe but red.** The old page and figures
  check would meet an `end_note` with no `mission_end`, and the
  website's night would commit nothing. The uncut path stays live,
  never false words, until the website is pushed.

## 7. The planted cases, by name, and where each runs

Each one is shown failing before it is trusted.

**The website's headless walk** (`tools/headless/walk_solar_system_drawer.js`):
- **43, "BepiColombo cut, shown past the 17th".**
  - The setup: a planted payload copy, BepiColombo's path ending on 17
    November 2026, its marker on that point, `ended`, no error, with
    `cutoff_note` and `end_note` set and no `mission_end`.
  - The check: the box reads the seven sentences in order, word for
    word, and none of this morning's words.
  - It must fail on the page as it is now.
- **42, kept, "a craft past JPL's path with no cut".**
  - It now picks a flying craft with no `cutoff_note`, since after the
    cut BepiColombo is the wrong pick.
  - Its words are this morning's.
  - It must fail on a page planted to give every flying craft the cut
    branch.
- **42b, kept, "Akatsuki's box kept"**, with every ended mission:
  their words exactly.
  - It must fail on a page planted to read `cutoff_note` before
    `mission_end`, which gives Akatsuki the cut words.

**The figures check** (`documentation/smoke_solar_system_figures.js`),
part 7:
- `missionEndIssue` gains the cut on a flying craft. A `cutoff_note`
  with no `mission_end` must name the path's last day. An `end_note`
  with no `mission_end` passes only beside a `cutoff_note`.
- Its self-test gains three cases: an `end_note` with no cut (red), a
  `cutoff_note` naming another day (red), and BepiColombo's right case
  (passes).
- The page pins `pastPath`'s cut branch and the new words.

**Orrery, `test_path_drawing.py`:**
- `marker_moment` and `hold_last_day` gain "cut, flying": the marker
  at 2026-11-17 00:01, and frames held after it.
- They must fail with `last_day` as it is now.

**Orrery, `test_path_plan.py`:** a flying entry with a cut alone. Its
plan stops at the cut, and an arrival after the cut is not among its
events.

**Orrery, the night's check:**
- In `test_horizons_check.py`: the parse of today's -121 text, the fit
  sentence across its line break and the file row.
- In the checker's own self-test, the two planted changes, each red by
  name:
  - the fit date moved, 2026-Nov-17 to 2026-Dec-04;
  - the file renamed, `_00243_` to `_00251_`.
- Also: a sheet with neither, red as a blind spot.
- At night: JPL unreachable, reported and not red. The flag, if
  chosen, raised in the title by `night_title_flags`.

**Run whole, each with its count, before the report:**
- both maintenance runs;
- the path plan suite, the export's own suite, the mirror suite;
- the builder's offline suite;
- the walk.

Also agentic-pre-test on a throwaway copy, for the orrery's changed
modules.

## As-built pages and skills

- **`INTERACTIVE_AS_BUILT.md`:** the section "A CRAFT STILL FLYING,
  PAST JPL'S PATH" is replaced, not appended, by one that covers both
  cases, with a cut and without. It goes in the same commit as the
  page.
- **`CACHE_BUILDER_AS_BUILT.md`:** unchanged. The builder is not
  edited; it only meets a plan with no arrival.
- **A skill line, proposed only, not written until the go-ahead.** In
  horizons-orbital-mechanics, beside `path_cutoff`: "A cut on a craft
  still flying is at JPL's fit date, typed with the path file it was
  made on (`cutoff_file`); the night reads that craft's sheet and
  reports when either changes; a session takes the cut off."

Written November 2026 with Anthropic's Claude Opus 5.5.
