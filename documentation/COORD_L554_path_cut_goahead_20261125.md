<!-- Doc-Kind: hand | The go-ahead for Part 2 of L-554's build (BepiColombo's path cut at JPL's fit date): the plan accepted as written, the night's report settled as a title flag and not a red night, and five points the build carries. Communication; written once. -->
# Go-ahead: BepiColombo's path cut, Part 2 (L-554)

Built on orrery 18df08b735655b75435566fbba22db6ec7cbbc21 as it stood
in Tony's folder at 15:40 Chicago on 2026-11-25, with the coordinating
session's records and the plan waiting there, and GitHub one commit
ahead of it (9de39f3c, the night's `data/nightly_run_record.json`), at
https://github.com/tonylquintanilla/palomas_orrery (branch main); and
gallery 3fb13a27763600b08cb67f710167d7fafa52153c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: GO-AHEAD, for the Claude Code session that wrote
`documentation/REPORT_L554_path_cut_plan_20261125.md`, by the brief
`documentation/COORD_L554_path_cut_brief_20261125.md`. Written
November 25, 2026 with Anthropic's Claude Fable 5.2, the coordinating
session.

## Before the first edit (amended 15:55, on Tony's question)

Tony, 15:42, away from his computer: "Can we give Code a go ahead
from my local folder?" Yes, for the website half, which your report
of 15:42 offered.
- THE WEBSITE HALF MAY START NOW. By your read the website folder is
  clean and equals GitHub at 3fb13a27. Record its base again first.
  Build there only: the page's words, the figures check, the walk's
  planted cases, the as-built page; then the website's maintenance
  run and the walk, each with its count. If a night commits to the
  website meanwhile, say so; Tony pulls before his push.
- NOTHING IS WRITTEN IN THE ORRERY FOLDER until Tony has committed,
  pulled and pushed it: no code, no records, no report file. If a
  website run or check would write there, stop and say which. The
  website half's report comes in chat; its file and the ledger's note
  are written with the orrery half.
- THE ORRERY HALF WAITS for his commit, pull and push, as before.
  Then record the orrery's base again; if edits wait beyond his run
  record, say so and stop.
- The website half does not depend on the night's report below; the
  orrery half does, and Tony has confirmed it (below).
- Nothing is pushed until the coordinating session has run the walk
  and the figures check on a clean checkout.

## The plan is accepted as written

Read against the code by the coordinating session, on copies equal to
both bases. Read, not run:
- `path_drawing.last_day` returns None without a `mission_end`, so the
  orrery's marker would stay on JPL's prediction: the plan's one
  change to the orrery's drawing is needed.
- `fetch_path_revised` is called only in `process_capture`: the
  website's night stops reading the sheet once the arrival leaves the
  plan, so the check belongs in the orrery's night.
- `missionEndIssue` is red on an `end_note` with no `mission_end`: the
  figures check changes with the page, and the website is pushed
  first.
- `horizons_check.py` keeps `data/spacecraft_sheets.json` from the
  same question that carries the fit sentence and the file name.
- A red night commits nothing: the workflow's commit step follows the
  run step.

The fields as planned: sentences 1 to 3 in `cutoff_note`, sentence 4
in `end_note`, sentences 5 to 7 on the page, and one new typed field,
`cutoff_file`.

## The night's report: a title flag, not a red night

Tony, 15:33, to your question: "Yellow? Not an issue." Read by the
coordinating session as: JPL fitting its path again is no failure, so
the night is not red. Your proposal is that reading, and it is the
shape the project already has for it (`test_horizons_unserved.py`:
"an entry JPL differs on: red by day ..., passes at night").
- At night: a clean night whose commit title starts JPL REFIT, the
  row's line naming which value changed and to what.
- By day: the same check red in the orrery's maintenance run.
- Where We Are: one "(do)" line for JPL REFIT beside EL NINO DUE's,
  inside the 130 lines.
CONFIRMED. Asked whether it means a green night with "JPL REFIT" in
its title, Tony, 15:46: "Yes".

## Five points the build carries

1. JPL UNREACHABLE. The plan says a sheet not read tonight "never
   passes" and also "reported and not red" at night. Both, said in
   one place: at night it prints a line that is neither the passing
   line nor red, naming the craft and that the sheet was not read; by
   day it is red. Show each in the checker's self-test.
2. A DAY SHOWN BEFORE 17 NOVEMBER. Left as the code makes it, as you
   propose, and recorded on L-554. Build no words for it. The
   coordinating session's proposal, for Tony's later word and not for
   this build: the source line's end takes sentence 7 on any day for
   a craft with a cut, since "as far as JPL's data runs" is not true
   of a path we cut.
3. THE TYPED FACTS ON THE ENTRY. The days, the 75 and 58 hours and the
   file name each sit under a `# Source:` line that is true of them:
   JPL's sheet with the day read; ESA's page with its address and the
   day read. The provenance scanner's Tier-1 on the gate path stays
   0; print its line.
4. THE SKILL'S LINE. Your text for horizons-orbital-mechanics is
   accepted as proposed. Read the skill's row on `DOCUMENT_CAPS.md`
   first: at its cap, a line is replaced or moved to its home, none
   added. The skill's change makes Tony's reinstall owed; say so in
   the rollup.
5. WHAT LEAVES WITH THE CAPTURE. Your Part 2 check that no count of
   capture craft is pinned and that BepiColombo's leftover check
   points are not read as a failure: print what you ran and its line.

## Checks, and the close

As the brief has them. The coordinating session runs the walk and the
orrery's new check on clean checkouts before Tony pushes: the website
first, then the orrery. L-554 stays OPEN for a night on GitHub and
Tony's phone look at BepiColombo's box.

Written November 2026 with Anthropic's Claude Fable 5.2.
