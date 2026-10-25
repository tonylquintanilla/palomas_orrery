<!-- Doc-Kind: hand | Coordination note: Tony's ruling of Oct 25 on L-461 (when the Daily Run's pull and his push differ, the run stops), from a talk-only session; build B of slice 2 builds it. -->
# Coordination note: when the pull and the push differ, the run stops

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 25, 2026

Built on orrery 0c27f47ad631efbfc611a80404095649025687d6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b1a4ce6c7fc72b17571a13e18ab11df98b86485b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on the morning of Oct 25.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). Answers the open question on
L-461 (the Daily Run confirms the orrery it pulled is the one Tony
pushed), which `HANDOFF_L443_slice2_buildB_brief_20261024.md` section
2, item 4, and section 3, item 3, send to Tony. Build B's records patch
carries it into L-461.

## The question

When the website's Daily Run pulls the orrery's export from GitHub and
finds it is not the one in Tony's orrery folder, does the run stop, or
wait and try again?

## Tony's ruling, Oct 25, 08:38

"stop. confirmed."

Put to him with this reasoning, which he confirmed: the one time it
happened (2026-10-21), the cause was an unpushed orrery, which waiting
cannot fix; GitHub's own delay after a push is a minute at most; a run
that waits hides the common cause behind the rare one.

## What build B builds

- In gallery `daily_run.py`, the pull step compares the orrery version
  the pull brought with the newest commit in Tony's orrery folder.
- When they differ, the run STOPS before the cache builder, with a
  plain message that names both versions and the two likely causes:
  the orrery's work is not pushed, or a push GitHub has not finished
  serving. No retry, no wait.
- The message says what to do: push the orrery (or wait a minute if
  GitHub Desktop shows the push just went), then run the Daily Run
  again.
- The rule goes into gallery-cache-builder at its next version, under
  the Daily Run's order and a failed pull: a pull that does not match
  the push is a failed pull.

## Tony-action rollup

- **(do)** Commit this note with build B's first push.
- **(decide)** Nothing further on L-461.

Written October 25, 2026 with Anthropic's Claude Fable 5.1.
