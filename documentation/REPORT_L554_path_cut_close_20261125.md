<!-- Doc-Kind: hand | The close of L-554's build (BepiColombo's path cut at JPL's fit date, 17 November 2026): both halves as built, what each check printed, the planted cases, and Tony's run order. For the coordinating session's check on clean copies before Tony pushes the orrery half. Communication; written once. -->
# Close: BepiColombo's path cut at JPL's fit date (L-554)

Built on orrery 65945090bfe85129fefd9b3d74600e7687a39728 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 972b4a9366224160d03f84708c9d33f55b811b87 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main).

Both were read 2026-11-25, evening, and both equal GitHub. The orrery
folder held one edit, Tony's own run record below Where We Are's
marker, which does not stop the work. Tony's website push 9ce37e1c
carries the website half. The orrery half below is not pushed.

Written November 25, 2026 with Anthropic's Claude Opus 5.5, a Claude
Code session through the python_work door, by
`documentation/COORD_L554_path_cut_brief_20261125.md` and its
go-ahead `documentation/COORD_L554_path_cut_goahead_20261125.md`.

## What a visitor will see

From the first website night after the orrery half is pushed,
BepiColombo's box reads Tony's seven approved sentences on every day
shown after 17 November 2026. Its path is drawn to that day and its
marker sits there. JPL's prediction past that day is not drawn or used
for a figure. The orrery's own plot does the same. No other craft's
box changes.

## The website half (pushed, 9ce37e1c)

The files: `interactive.html` (6 edits), the walk (8), the figures
check (5), `INTERACTIVE_AS_BUILT.md` (a section replaced) and
`tools/mirror_objects.py` (its notes only).

The website's maintenance run: "53 of 53 gating checkers passed". The
walk: "PASS: 383 checks". Each new case was shown failing first:

| Case | Run against | Result |
|---|---|---|
| 43 | the page as it was | FAIL 2 |
| 42a | a page planted to give every flying craft the cut | FAIL 2 |
| 42b | a page planted to read a `cutoff_note` before a `mission_end` | FAIL 1 (Akatsuki) |
| The figures check's pins | the page as it was | FAIL 4 |
| The figures check's self-test | its old rule | FAIL 1 |

## The orrery half (not pushed)

- **The entry** (`celestial_objects.py`, BepiColombo):
  - `path_cutoff` 2026-11-17;
  - a new field, `cutoff_file`:
    `bc_mpo_fcp_00243_20181020_20270411_v01`;
  - `cutoff_note`, sentences 1 to 3;
  - `end_note`, sentence 4.

  Each sits under a `# Source:` line: JPL's sheet for -121 with its
  address and the day read, ESA's page with its address and the day
  read, and Tony's ruling and approvals.
- **The plan**, remade from JPL by the maintenance run: made
  2026-11-25, span 2018-10-21 to 2026-11-17, 33 events. Two left:
  - the arrival at Mercury, 2026-11-21 18:48;
  - the Sun's pass of 2027-02-06.

  The plan report counted 32 events before; there were 35. The
  website's builder clips every event window to the span
  (`fetch_path_by_plan`), as the orrery's `draw_plan` does. The export
  carries the cut plan and both sentences; `cutoff_file` stays in the
  orrery.
- **The orrery's drawing** (`path_drawing.last_day`; the console
  words in `console_word`, printed by `palomas_orrery.py`): a cut path
  with no `mission_end` holds its marker on its cut, in the static
  plot and the animation. The console says PATH CUT.
  - Drawn live from JPL: 1,426 points, from 2018-10-21 00:00 to
    2026-11-17 00:01, all solid.
  - The marker: `(2026-11-17 00:01, True)`.
  - Akatsuki and Juno are unchanged.
- **The night's check.**
  - `horizons_check.py` reads a cut path's sheet on every run
    (`current_cuts`, `parse_cut`) and keeps its fit day and path file
    on the sheet's record in `data/spacecraft_sheets.json`.
    `cut_state` holds them to the entry.
  - A change is JPL REFIT on the check's green verdict line. That
    raises the night's commit title (`NIGHT_TITLE_FLAGS` in
    `orrery_maintenance_run.py`).
  - `check_horizons_confirmations.py` (`cut_lines`) is red on JPL
    REFIT by day. At night it passes JPL REFIT by name. A sheet not
    read tonight prints NOT READ, neither a pass nor red.
  - An entry cut with no `cutoff_file` is red at any hour.
  - Its line today: "BepiColombo (-121): the cut holds -- JPL's fit
    date 2026-11-17 = path_cutoff 2026-11-17; JPL's path file
    bc_mpo_fcp_00243_20181020_20270411_v01 = cutoff_file
    bc_mpo_fcp_00243_20181020_20270411_v01 (sheet read 2026-11-25)".
- **The docstrings** of the export and the mirror say a cut craft
  still flying may carry the two notes. Their code is unchanged.

## Planted cases, each caught by name

**`test_horizons_check.py`, section 9** ("HORIZONS CHECK SUITE: pass
-- 144 checks"):
- JPL's -121 text, parsed across its line break.
- The fit date moved to 2026-Dec-04, the path file renamed to
  `_00251_`, and the fit sentence gone. Each is JPL REFIT by name on a
  green verdict line, red by day and passing at night.
- A sheet not read today: red by day, NOT READ at night.
- No `cutoff_file`: red at any hour.
- A `cut_state` planted blind to the file, and a checker planted to
  pass an unread sheet by day: each caught.
- The title flag is raised from the Horizons check row only.

**`test_path_drawing.py`, check 6c** ("15 of 15"): caught with
`last_day` planted as it was before L-554.

**`test_path_plan.py`, check 21** ("40 of 40"): a flying craft cut
alone stops at the cut, and its plan is made again.

## The go-ahead's five points

1. **JPL unreachable.** At night, NOT READ names the craft and the
   last day read, and is neither a pass nor red. By day it is red.
   Both are in section 9.
2. **A day before 17 November.** Left as the code makes it, and
   recorded on L-554. The coordinating session's proposal waits for
   Tony.
3. **The typed facts.** Each sits under a `# Source:` line. The
   orrery's run: "0 TIER-1 -- the push gate holds".
4. **The skill line.** horizons-orbital-mechanics 1.21, with the line
   as accepted. The skill was at its cap of 904 lines, so its 1.18
   entry moved to `documentation/SKILL_HISTORIES.md`; it is now 898
   lines. `skills_index.py --check` passes. Tony's reinstall is owed.
5. **What leaves with the capture.** `tools/test_curve_error.py`
   `capture_craft`, run with the cut plan laid over today's config and
   index: today it picks juno and bepicolombo; with the cut, juno
   alone. No count of capture craft is pinned anywhere. BepiColombo's
   check points are not on disk, since they are not committed, so
   nothing reads them.

## Checks

- The orrery's maintenance run, whole: "37 of 37 gating checkers
  passed", "0 TIER-1 -- the push gate holds". Run before the records
  and again after them (the ledger's line has the second).
- `doc_index.py --caps`: "DOCUMENT CAPS: PASS". Where We Are is at 130
  of 130 lines above the marker.
- agentic-pre-test: `py_compile` on every changed module; a throwaway
  copy of `palomas_orrery.py` run with a 30-second timeout ended
  exit 124 (the window healthy until the timeout), no traceback, the
  copy removed.

## Tony's run order

1. Send this report to the coordinating session. It runs the walk and
   the orrery's new check on clean checkouts.
2. Orrery: Commit, then Pull origin, then Push origin.
3. Reinstall horizons-orbital-mechanics (1.21) to your account from
   the repository.
4. After the next website night, look on your phone at BepiColombo's
   box.

Written November 2026 with Anthropic's Claude Opus 5.5.
