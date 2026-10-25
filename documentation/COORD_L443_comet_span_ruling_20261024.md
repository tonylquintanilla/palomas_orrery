<!-- Doc-Kind: hand | Coordination note: Tony's ruling of Oct 24 on how much of an open-path comet's path the website draws (L-443 slice 2), recorded before the night's records patch runs. -->
# Coordination note: how much of a comet's path is drawn

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026, evening

Built on orrery 206f96c988569496d9cf12b9e3e45d73e61132d4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 96173b88e4da9661fcfe3a389a96c6bab19b60cc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). Answers the question put in chat
on Oct 24 and listed in `HANDOFF_L443_slice2_buildA_20261024.md`,
section 4, question 1. It came after that handoff was written into
`patch_L443_8_session_close_20261024.py`, so the next records patch
carries it into the ledger (L-443).

## The question

A spacecraft's path runs from launch to where JPL's planned trajectory
ends. A comet has no launch and no end, so how much of its path should
the website draw? Recommended: from one year before perihelion, solid
up to today, then dashed for one more year.

## Tony's ruling, Oct 24, 17:07

"On the comet window, yes but within the JPL served window which may be
less."

## What that means for the build

- A comet's path runs from one year before its perihelion to one year
  after today: solid up to today, dashed after.
- Both ends are clipped to what JPL serves for the comet's record, read
  from JPL's own refusals as the path plan already reads a spacecraft's
  span (`path_plan.py`, `path_rows_and_span`). Where JPL serves less, the
  path is shorter, and nothing is extended.
- The perihelion is found from JPL's positions, by the plan's rule for
  the Sun (the Sun needs no Hill-sphere gate).
- The two one-year margins are drawing choices; the hover says so.

## Tony-action rollup

- **(do)** Commit this note with the night's push.
- **(decide)** Nothing further on this.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
