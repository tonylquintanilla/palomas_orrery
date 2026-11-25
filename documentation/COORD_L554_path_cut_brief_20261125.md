<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-554 (JPL's sentence when a path is a prediction), BepiColombo's path cut at JPL's fit date, 17 November 2026, with its seven approved sentences and a night's check on JPL's sheet. The plan first, then the build. Communication; written once. -->
# Brief: BepiColombo's path is cut at JPL's fit date (L-554)

Built on orrery 18df08b735655b75435566fbba22db6ec7cbbc21 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery 3fb13a27763600b08cb67f710167d7fafa52153c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-25, 13:40 Chicago; Tony's two folders
stood at the same commits by git's own record in each, his orrery
folder with this session's records waiting). Nightly bot commits
since are expected. This brief is in Tony's next orrery push.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session through the python_work door. The
code is in both repositories: the orrery's entry and whatever carries
its note to the website; the website's page, its walk, and one check
at night. Written November 25, 2026 with Anthropic's Claude Fable 5.2,
the coordinating session. Method table: a Code session, Opus
(METHOD_MODEL_EFFORT.md, a build).

Tony's words, all on L-554, 2026-11-25. 14:41: "Stay with JPL and
11/17 until refit." 14:58: "Not at my computer. Words and plan
approved. Thanks." The words:
`documentation/WORDS_L554_path_cut_20261125.md`, seven sentences,
used word for word.

## What this is, in one paragraph

BepiColombo entered orbit around Mercury on 21 November 2026. ESA
reports the burn ended early and the craft is on a 75-hour orbit, not
the planned 58-hour one. JPL's path for record -121 is "Data fit
through 2026-Nov-17, prediction thereafter", one file,
`bc_mpo_fcp_00243_20181020_20270411_v01`, and read live on Nov 25 it
still gives the plan: 58.7 to 58.9 hours around Mercury to 26
November, 27.7 hours from the 27th. The website and the orrery draw
that plan as the craft's path. Tony's ruling: the path is drawn to 17
November 2026, the last day JPL's data is fitted, and no further,
until JPL fits past the arrival. The same rule cut Akatsuki's path
(L-507; his words of 2026-11-05 are on its entry in
`celestial_objects.py`).

## Start

1. The orrery's CLAUDE.md from its first step, then the gallery's.
   Both bases recorded; edits waiting in either folder beyond Tony's
   run record: say so and stop.
2. L-554, whole: its notes of 2026-11-25 and its Gap. The words file
   above. L-507's notes on Akatsuki's cut.
3. Skills, each in the parts the job fires: horizons-orbital-mechanics
   (a spacecraft path's plan; which record serves a body);
   gallery-cache-builder (a spacecraft fetched by its plan; a config
   change is not deployed until the cache is rebuilt);
   interactive-exhibit (the box's served words; who may write
   `data/objects_config.json`; the walks); provenance-discipline (a
   typed day and typed words with their sources);
   orrery-coding-conventions (the six consumers of position data,
   mapped before any edit); agentic-pre-test; safe-file-editing.
4. The code, read where it runs. Orrery: Akatsuki's entry and
   BepiColombo's in `celestial_objects.py`; `path_plan.py`
   (`path_stop`, `plan_inputs`); `path_drawing.py`;
   `export_objects.py`. Website: `tools/mirror_objects.py`;
   `interactive.html` at `pastPath`, `PAST_PATH_OPENING`,
   `ENDED_EARLY_OPENING` and `solarSystemEndedEarly`;
   `tools/gallery_cache_builder.py` at `fetch_path_revised` and
   wherever a capture craft's fine points are asked; the figures
   check that holds a `cutoff_note`'s day to the path's last day.

IF A SENTENCE OF THIS BRIEF DISAGREES WITH THE CODE, SAY WHICH, AND
STOP. It was written from a reading of these places, not a run:
`path_stop` and `plan_inputs` (a `path_cutoff` is among a plan's
inputs, so setting one should make the plan again);
`interactive.html` lines 3922 to 3950 and 4628 to 4665 at gallery
3fb13a27 (a craft with no `mission_end` past its path's last point
takes this morning's words and its `cutoff_note` is not read);
`fetch_path_revised` (it already reads JPL's fit sentence and the
first path file named).

## The outcome

- BepiColombo's path ends on 17 November 2026 in the website's room
  and in the orrery's own plot, from one field on its entry. Nothing
  after that day is drawn or used for a figure.
- Its box reads the seven sentences of the words file, in their
  order, word for word, on every day shown after 17 November. No
  other craft's box changes by a letter: the 7 ended missions,
  Akatsuki's cut, a craft past the end of JPL's path with no cut
  (this morning's words, the walk's section 42), every comet.
- The entry carries its sources as Akatsuki's does: JPL's sentence
  and file name with the day read, ESA's page with its address and
  the day read, and Tony's ruling. No day is typed anywhere a tool
  could read it from JPL instead.
- A check at night holds the cut to JPL's sheet for -121: the fit
  date and the path file's name, against what the entry was cut on.
  A change in either is red, by name, saying which changed and to
  what. It is seen to fail on a planted change of each kind before it
  is trusted, and its passing line prints both values it compared.
- When it goes red, nothing un-cuts by itself. A session reads JPL's
  new path and takes the cut and its words off the entry.

## The job, in two parts

**Part 1: the plan, before any edit.** One report, then stop.
- The six consumers of position data, each named, and what the cut
  does to each.
- Where each of the seven sentences lives: the entry (as Akatsuki's
  `cutoff_note` and `end_note` do) or the page. If the two fields
  that exist cannot carry sentences 1 to 4 in the approved order,
  say what is added, and why nothing smaller does it.
- What a new plan for BepiColombo holds once its span ends on the
  17th: the Mercury arrival event of 21 November leaves it. Say
  every place that event is read (the page's reading of a path's
  events, a capture craft's fine points, L-538's figures, any check
  that expects BepiColombo to be an orbiter) and what each does
  without it.
- The box, whole, before and after, as a visitor reads it today.
- Where the night's check runs, which repository's night, and how it
  knows what the entry was cut on. Say plainly if a night made red by
  JPL changing its sheet sits badly with L-485's rulings (an outside
  failure is reported and never halts the night; a held body is not
  a red night). If it does, propose the loudest report that fits
  them; the choice goes to Tony.
- The order of Tony's two pushes and what a visitor sees between
  them, and on which night the website shows the cut.
- The planted cases you will add, by name, and where each runs.

**Part 2: the build, on the go-ahead.**
- The changes of the plan as accepted.
- The walk's planted cases, each shown failing first: BepiColombo cut
  and shown past the 17th, reading the seven sentences; a craft past
  JPL's path with no cut, its words kept; Akatsuki's box kept.
- The night's check, with its two planted changes.
- The as-built pages in the same commit where they describe these
  words or this check, the section replaced, not appended.
- A skill's line only where a rule changed, its text proposed in
  your report and not written until the go-ahead.
- agentic-pre-test, whole, on a throwaway copy before the report.

## Out of scope

- JPL's sentence in the source line of every craft whose path is a
  prediction: L-554's first question, not ruled.
- The arrival's encounter and Mercury's features (L-529 (guided
  encounters)); orbiters in general and Mio (L-555).
- The error away from today (L-557) and the date picker (L-556).
- The box's words on a no-distance day (L-553).
- A cut that follows JPL's fit date by itself. The day is typed on
  the entry with its source, as Akatsuki's is, and the night says
  when it is stale.

## Checks

- Both maintenance runs, whole: no row red that was green at the
  base; say what a red row reads, not only its colour.
- The path plan's and the export's own suites, the mirror's, the
  builder's offline suite and the walk, each with its count.
- The coordinating session runs the walk and the new check on a
  clean checkout before Tony pushes.

## Close

- L-554: what changed, the planted cases by name, what is owed. It
  stays OPEN for a night on GitHub and Tony's phone look at
  BepiColombo's box, and for its first question.
- Where We Are by section, within its 130 lines.
- The final report in the form the doors set, with the token count.
  Commit and push are Tony's, in the order your plan gives.

Written November 2026 with Anthropic's Claude Fable 5.2.
