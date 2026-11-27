<!-- Doc-Kind: hand | The brief for a small fix by the Claude Code session that built L-545: the website's night has been red since the orrery's export carried BepiColombo's cut, because the figures check, run by the cache builder's suite on its pretend nights of July 2026, calls a craft cut in November a fault. Website code only. Communication; written once. -->
# Brief: the cut craft in the suite's pretend nights (L-554)

Built on orrery c54123426cc4ab8710b2d4e1c267d94f375fea4a at
https://github.com/tonylquintanilla/palomas_orrery (branch main), the
night's commit of 2026-11-26, 14:17 Chicago, one file above Tony's
push 3955c056; and gallery 571ac6768108cf6109a29db69a38bb346ee93a67
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main), Tony's push of the walks. Both read 2026-11-26, 14:30
Chicago. Tony's orrery folder is one night's commit behind GitHub.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a small fix, for the Claude Code session that built
L-545 (checks that wait to be remembered) and is still open. Website
code only; the records in the orrery. No plan round: build, show,
report. Written November 26, 2026 with Anthropic's Claude Fable 5.2,
the coordinating session. Tony, 14:26, to "shall I write that brief
for the Code session now?": "Yes please write the fix for code, who
is running now."

## What happened

The website's night #62 ran red at 12:27 Chicago (Tony's run record;
its log was not read here, GitHub's run logs cannot be reached from
this session). It ran gallery 972b4a93, before the walks' push, and
was the first website night to pull the orrery after 651422cb, whose
export gives BepiColombo a `path_cutoff`, a `cutoff_note` and an
`end_note`.

## What was measured here

On a clean clone of gallery 571ac676, with the five data files your
run pulled into Tony's folder laid over (`data/objects_config.json`,
`objects_export.json`, `objects_export.sha`, `constants_export.sha`,
`drawings/pulled_at.sha`):
- `tools/test_gallery_cache_builder_offline.py` fails two checks it
  passes without those files: "L-553 (10): the Solar System figures
  check, whole, is GREEN on the planted night (exit 1)" and "L-553
  (7, 8, paths D and E): ... the figures check green and naming both
  (exit 1)".
- On each of those planted folders the figures check prints one
  problem: "bepicolombo: serves a mission_end, end_note or
  cutoff_note but its path has not ended"
  (`documentation/smoke_solar_system_figures.js`, line 1400, under
  "A mission still flying serves no mission_end or end_note").
- The suite's nights are built in a temporary folder by `run_build`
  with a stand-in JPL and the clock at `FIXED_NOW`, 2026-07-09 (line
  204). They read the live `data/objects_config.json`. In July the
  served window ends before 17 November, so the path has not ended,
  and the live entry says it is cut.
- So the real cache has no part in it: A REBUILD DOES NOT CLEAR THIS
  ROW. Your report said it clears both; it clears Solar System
  figures. The row "Cache builder suite" is a gate of the night
  ("PASS (631 checks, 0 failures)" in the last clean night's record).
- Here two more checks fail with and without the cut (L-399, the
  astroquery questions): this session's Python has no astroquery.
  Not yours to chase.

## The outcome

1. THE RULE SAYS WHAT IS TRUE. A craft whose last day (its
   `path_cutoff`, or its `mission_end`) lies after the last day the
   served folder covers is still flying in that folder, and its notes
   are no fault. A craft whose last day lies inside what is served,
   and whose path has not ended, is still the fault it was. If you
   find the suite's pretend nights the better place to mend, say why
   and mend there; the outcome is the same either way.
2. IT CAN STILL FAIL. The figures check's own worked cases gain the
   pair: green on an end day after the served window, red on one
   inside it with the path not ended.
3. THE NIGHT, WHOLE, SHOWN GREEN BEFORE THE PUSH. On a throwaway copy
   with the orrery's export pulled and the cache rebuilt from JPL:
   the night's pass, every gating row, with its last line quoted.
   This is the proof the cut's build lacked: its website half was
   checked before the orrery's export carried the notes.
4. THE CLASS, RECORDED AND NOT CHASED, on L-554: a check with a fixed
   clock that reads the live list of objects meets every dated fact
   added to that list after its clock. Say which other fixed clocks
   in the website's checks read the live list, by name.

## Out of scope

- What a cut craft's box says on a day before its cut (Tony's open
  decision on L-554). This is a test, not the page's words.
- The walks, the workflow, the orrery's code.

## Checks and close

- The suite on Tony's computer with the export pulled: every check,
  with its count. Both maintenance runs, whole: no row red that was
  green at the base, and what a red row reads.
- The data files the run pulls into the website folder are not for
  the push, as before; name them.
- A note on L-554: what failed, why, what changed, the planted cases
  by name; and that the coordinating session wrote nothing in the
  ledger or on Where We Are while you ran, so the red night and this
  brief are yours to record there. Where We Are by section, within
  130 lines.
- Before Tony pushes, the coordinating session runs the suite and the
  figures check on a clean checkout with your files laid over.
- The final report in the form the doors set. Website pushed first,
  then the orrery; Tony pulls the orrery's night commit of 14:17
  with his commit.

Written November 2026 with Anthropic's Claude Fable 5.2.
