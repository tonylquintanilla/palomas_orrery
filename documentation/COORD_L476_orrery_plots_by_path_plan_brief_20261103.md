<!-- Doc-Kind: hand | Brief for a Claude Code session (build): the orrery's whole-path plots of planned spacecraft and comets drawn by the path plan, solid to today and dashed after, with their dates read from the plan instead of typed (L-476). Orrery only; the website read, never edited. -->
# Brief: the orrery's whole-path plots by the path plan (L-476)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 3, 2026, morning, Chicago

Built on orrery b60e296cb2068d8d69eb3b90f0a4a1227539d88f at
https://github.com/tonylquintanilla/palomas_orrery and gallery
3a211a8cf10a3002668a85836f31bf973e385f2c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 3, 16:20 UTC.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for one Claude Code session, opened through the python_work
door, working in the orrery folder. The website's folder is read, never
edited. Opus, high effort (orbital mechanics and typed dates, by
`METHOD_MODEL_EFFORT.md` row 26). Its report ends with its token count,
as Claude Code prints it (protocol, Token Economy).

## 1. Why, in two sentences

Tony ruled on Oct 23 that the orrery and the website draw a path by one
rule, the orrery's path plan, and that the part after today is dashed
for spacecraft and comets alike (`DESIGN_L443_slice2_rulings_20261023.md`,
rulings 2 and 6). The website has drawn by the plan since Oct 25; the
orrery still spreads an even count of points across dates typed by hand,
several of them stale against JPL, which is also the first finding the
website-orrery check (L-484) will make.

## 2. The rulings (read L-476's body in the ledger first)

- Ruling 2: the orrery works out each path's plan once
  (`path_plan.py`, `data/path_plans.json`); the website fetches by it;
  the orrery's own plot draws by it.
- Ruling 6: solid to today, dashed after. The part after today is JPL's
  own planned trajectory or prediction, never extended.
- Tony, Oct 24, 17:26: "the orrery's object list for served windows
  should be updated to match the website." By method (L-476): the dates
  are read from the plan, not kept as a second typed copy, so they
  cannot go stale again.
- Galileo ends at its impact, 2003-09-21 (L-507, "Yes stop at impact"):
  the plan already ends its span there, so the orrery's Galileo will
  stop nine days earlier than it does today. That is intended.

## 3. What is already found at b60e296c

- **The ledger names a dead function.** L-476 says the even spread is
  `create_dates_list_for_object` (palomas_orrery.py line 462). Nothing
  calls it. The live even spread is inside `plot_objects`' inner
  `worker`, the `obj_type == 'trajectory'` branch near line 5209:
  `np.linspace` across the entry's start_date and end_date at the GUI's
  trajectory point count. A second reader near line 5113 clips the GUI's
  dates to the entry's dates before `fetch_orbit_path`. Map both before
  editing either (Verify Execution, Not Appearance).
- **The typed dates:** 65 entries in `celestial_objects.py` carry
  `start_date` and `end_date`. Their readers, by function:
  palomas_orrery.py 42 lines (`worker` 28, `get_interval_settings` 13,
  `_apply_mission_preset` 12, `animation_worker` 9,
  `_apply_comet_perihelion_preset` 7, `create_dates_list_for_object` 5,
  `_add_close_approach_extras` 3, `_apply_comet_disintegration_preset`
  2, `plot_actual_orbits` 1, `create_mission_checkbutton` 1; one line
  can be counted under two names); `orbit_data_manager.py` 4;
  `path_plan.py` 3; `spacecraft_encounters.py` 2;
  `verify_orbit_cache.py` 1.
- **The plans:** `data/path_plans.json` holds 28 plans: the 14 keyed
  spacecraft and the comets on open paths. The other 13 spacecraft
  (Apollo 11 S-IVB, Pioneer 10, Pioneer 11, SOHO, Rosetta, Akatsuki,
  Gaia, Hayabusa2, OSIRISREx, MarsRover, DART, JamesWebb, Artemis II)
  have no plan and keep their typed dates. So do the Lagrange points
  and the rest of the 65.
- **What the plan holds:** a span (JPL's own first and last day), a
  backbone (a 7-day step, Douglas-Peucker thinning at 0.02 AU), and
  events, each with its window and step. It holds no points; the
  drawing applies them.
- **The website's drawing of a plan** is `fetch_path_by_plan` and
  `douglas_peucker` in gallery `tools/gallery_cache_builder.py` (lines
  1394 and 1455 at 3a211a8c): backbone across the span, thinned; each
  event's window at its own step, thinned at its own scale
  (`WINDOW_THIN_FRACTION` of the passing distance) and merged after; then
  a daily tail and an ended mission's last day, which are the room's
  needs and not the orrery's.
- **The ask-from:** `path_plan.py` asks each path from the entry's
  `start_date` (the launch). A plan is made again when its inputs change.
  So start_date stays on planned entries; changing it would remake
  plans.
- **The export carries no typed dates:** `export_objects.py` does not
  read start_date or end_date, so this build should leave the objects
  export unchanged. Prove it by a diff (section 6).
- **Dated checkbox labels:** typed in palomas_orrery.py, for example
  `create_mission_checkbutton("Voyager 2", voyager2_var, "(1977-08-21 to 2029-12-31)")`.
  One pattern found 46 on Nov 3; the ledger counted 51 on Oct 24. Count
  them by name.

## 4. The work, in order

1. **Map.** The five parallel consumers (protocol, Check All Parallel
   Pipelines): static plot, animation, social export in this repo;
   Gallery Studio and the JSON converter in the website's, read only.
   For each, say whether it draws a planned entry's whole path, and
   where. Stop and report if the live path is not the one section 3
   names.
2. **One function that draws a plan,** in `path_plan.py` or a module
   beside it: given a planned entry, it returns the dates and positions
   by the website's method (backbone, thinning, event windows; no tail,
   no last-day pair). The website's code is the reference; the orrery
   holds its own copy because the repositories cannot import each other.
   Say in its docstring where the twin lives.
3. **The plot.** In the Sun-centred whole-path plot, a planned entry is
   drawn by that function, split at today by the UTC clock
   (`utc_clock`), not by the GUI's date: solid before, dashed after, one
   colour, one legend entry. Today means where JPL's reconstructed path
   ends and its plan begins, which is what the dash says. Hover by
   orrery-coding-conventions. Unplanned entries draw as today.
4. **Other centres.** A plan's backbone and thinning are worked in
   heliocentric distances; centred on Jupiter, a 7-day step thinned at
   0.02 AU would erase Juno's orbits. Tony's ruling, Nov 3, 12:06
   Chicago, asked whether only Sun-centred plots switch to the plan:
   "yes and the orrery and the website should both follow this." So a
   planned path centred on any body but the Sun keeps today's drawing,
   in the orrery now and in the website's rooms centred on a planet
   when they come (12b and 13 on Where We Are, L-433). The website draws
   no such path today, so nothing there changes in this build.
5. **The dates.** Every reader of a planned entry's start_date or
   end_date that means its span takes it from the plan. The planned
   entries lose their typed `end_date`; `start_date` stays as the
   ask-from (section 3). A guard fails the path plan's own suite, and
   so the maintenance run, if a planned entry carries an `end_date`
   again. The dated labels of planned entries are written from the
   plan's span when the window is built, in their present format.
6. **The animation, social export, Studio and converter** follow by
   step 1's map. A consumer that does not draw the whole path is left
   as it is, and the report says so. Whether a dashed 3D line survives
   Studio and the converter is read and reported, never fixed here.
7. **The orbit cache.** `fetch_orbit_path` and `orbit_data_manager.py`
   may store a path keyed by its dates. Read how; a plan-drawn path
   must never be served an even-spread one from the cache, nor the
   reverse.

## 5. Things this build does not do

- No new words, no new numbers, no website edits.
- Galileo's colour (white in the orrery, goldenrod on the website) is a
  chosen difference for L-484, not this build.
- The encounter views keep their own curvature rule
  (`_calculate_encounter_resolution`), which the plan already uses.

## 6. The rules it runs under

Read each before the work it governs; open the first report with each
version line read, against the manifest in `PROJECT_INSTRUCTIONS.md` at
b60e296c: horizons-orbital-mechanics 1.14 (a spacecraft path's plan, the
orbiter rule, the window and step); orrery-coding-conventions 1.13
(legendgroups, hover, the live dispatch path); gallery-cache-builder
1.17 (A Spacecraft Is Fetched by Its Plan; A Served Number That Changes
on Purpose, for the export diff); provenance-discipline 2.36 (typed
dates removed, nothing recalled); safe-file-editing 1.14;
agentic-pre-test 1.3; ledger-and-session-records 1.22. A skill loaded
only for one section is read in that section.

## 7. Done when

- **A check that can fail:** for Galileo, an ended path that JPL no
  longer revises, the dates the orrery's plan drawing produces equal the
  dates in the website's served `data/solar-system/positions/galileo.json`
  at 3a211a8c, apart from the last-day pair, which is named. Shown
  failing once with a planted fault (a changed tolerance).
- The guard of step 5 shown failing once on a planted `end_date`.
- The objects export byte-identical before and after, by diff, or each
  moved line named with the website's pins it would move.
- py_compile, the pre-test on a throwaway copy, and the orrery's
  maintenance run, all read from their output.
- Tony's run order ends with his Mode 5 look at five Sun-centred plots:
  Voyager 1 (dashed after today), Juno (dashed to 2028-09-02), Galileo
  (ending at impact, all solid), 3I/ATLAS (a comet's plan), and Pioneer
  10 (no plan, unchanged); and one Jupiter-centred Juno, unchanged.

## 8. Records, in the same session

- L-476: what was built, verified against claimed; the dead function
  named, removed only if Tony says so; Tony's ruling of step 4 in his
  words.
- horizons-orbital-mechanics, one sentence in its path plan section at
  its next version (this session's, if it bumps the skill): a plan
  draws a path only around the Sun; around any other centre, both
  instruments draw it as before (Tony, Nov 3).
- L-484: its L-476 finding (the typed dates) answered by this build.
- Where We Are, by section: the road line, the box, Signals read from
  files; nothing below the run-record marker.
- The report: files changed with their edit counts, the labels changed
  by name, the token count, Tony's run order, one question at most.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
