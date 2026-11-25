<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-533 (ESCAPADE), the last-day build. A path still flying is asked of JPL at its span's last moment too, so its line and its box reach the plan's last day. Communication; written once, read by its session. -->
# Brief: every path runs to its span's last day (L-533)

Built on orrery a33c1d972f230b3eb22b755550e438b9791516cc at
https://github.com/tonylquintanilla/palomas_orrery
and gallery b2d9eaa66ed33ec93fc2bbcbdc5b85d5b872e043 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-25, 00:35 Chicago; Tony's two folders
stood at the same commits, his orrery folder with this session's
records waiting). Nightly bot commits since are expected. This brief
is in Tony's next orrery push.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session through the python_work door. The
code is the gallery's: the builder, its offline suite, one check, and
`CACHE_BUILDER_AS_BUILT.md` in the same commit. The orrery gets the
records and one line of gallery-cache-builder. Written November 25,
2026 with Anthropic's Claude Fable 5.2, the coordinating session.
Method table: a Code session, Opus (METHOD_MODEL_EFFORT.md, a build).

Tony's words, both on L-533. Nov 19, 21:03, asked whether to make the
change: "Yes". Nov 22, 21:58, asked whether it rides L-538's build:
"Keep its own build".

## What this is, in one paragraph

The builder asks JPL for a path's backbone a point every 7 days,
counted from the span's start, and never for the span's last moment.
So a path still flying stops at its last 7-day point, and its box
names that day and not the plan's ("as far as 7 September 2027" for
ESCAPADE-Gold, whose span ends 2027-09-10). An ended mission does not
stop short: `fetch_path_last_day` asks its last day (L-507). Read by
the coordinating session from `data/objects_config.json` and
`data/solar-system/coverage_index.json` at gallery b2d9eaa6: 34 paths,
7 ended and at their last day, 27 still flying and every one short.
- 7 days short (10): new_horizons, juno, parker_solar_probe, lucy,
  psyche_spacecraft, west, c2025_k1, c2025_k1_b, c2025_k1_d, atlas_3i.
- 6 days (1): bepicolombo.
- 5 days (5): voyager_2, osiris_apex, europa_clipper, mcnaught,
  tsuchinshan_atlas.
- 4 days (1): oumuamua.
- 3 days (5): voyager_1, panstarrs_2025_r3, borisov_2025_v1,
  borisov_2i, escapade_gold (its last point is 2027-09-07 01:49).
- 2 days (3): juice, escapade_blue, atlas_2024_g3.
- 1 day (2): solar_orbiter, wierzchos.

## Start

1. The orrery's CLAUDE.md from its first step, then the gallery's.
   Both bases recorded; edits waiting in either folder: say so and
   stop.
2. L-533: its two notes of Nov 19 (THE BOX'S LAST DAY, the cause
   found; RULED) and its Gap. L-507's note on `fetch_path_last_day`.
3. Skills: gallery-cache-builder 1.23, A Spacecraft Is Fetched by Its
   Plan, and on the page `CACHE_BUILDER_AS_BUILT.md` the section of
   the same title; horizons-orbital-mechanics, How a Path's Events Are
   Found and A Comet on an Open Path; agentic-pre-test;
   safe-file-editing.
4. The code, read where it runs: `_plan_span`, `fetch_path_by_plan`,
   `fetch_path_tail`, `fetch_path_last_day`, and every place a path's
   last served point is read (the box's "as far as", the checks on a
   path's points, a capture craft's fine layer).

IF A SENTENCE OF THIS BRIEF DISAGREES WITH THE CODE, SAY WHICH, AND
STOP. It was written from a reading of those four functions only.

## The outcome

- Every path's last served point is at its span's end as the builder
  asks it, for a path still flying as for an ended one. Each dashed
  line runs to it, and each box names that day.
- Nothing is asked past the span. The Voyagers' data ends at
  2100-01-01 00:00 on JPL's clock to the minute, and JPL refused a
  stop one minute later (`_plan_span`, FIXED, L-443).
- A check holds it every night: each path's last served point against
  its span's end, each path named, with the count; red when one is
  short. It is seen to fail on a planted path before it is trusted.

## The job, in two parts

**Part 1: the plan, before any edit.** One report, then stop.
- How the last moment is asked, and on which nights. A path is
  fetched whole only when its plan is new; otherwise only its tail.
  Say how the 27 get their last point on the first night after the
  push, and what that costs in questions to JPL.
- The 13 comets on open paths: their span ends a year after the day
  the plan was made, and the plan is remade. Say what "the last day"
  is for them and how it moves.
- Juno and BepiColombo are capture craft. Say what their fine layer
  and its checks do with a new last point.
- What each of the 27 boxes reads, before and after, by name. If any
  words change beyond the day, say so plainly: that goes to Tony.
- ONE FACT, NOT A BUILD. L-538's Part A report (section 5) says that
  on a date past the end of JPL's data for a craft still flying, the
  box reads "This mission ended on ...", which is false; BepiColombo's
  data ends 2027-04-10 and the date window reaches it about
  2027-01-12. Confirm from the code when the box says it and whether
  any date reaches it today. Propose words; do not build them. They
  are Tony's.
- The planted cases you will add, by name, and where each runs.

**Part 2: the build, on the go-ahead.**
- The changes of the plan as accepted.
- The planted cases in the offline suite, and the nightly check.
- A dry run against JPL that fetches the 27 and prints each one's
  span end beside its last point. That is the proof on real data.
- `CACHE_BUILDER_AS_BUILT.md` in the same commit, the section that
  changed, replaced not appended.
- gallery-cache-builder's line "An ended mission's last served point
  is on its span's last day" becomes every path's. Its text comes
  with the go-ahead, written after your plan. The skill is at its
  cap; a line replaced, none added.
- agentic-pre-test, whole, on a throwaway copy before the report.

## Out of scope

- L-556 (a date to choose in the rooms) and L-557 (the error away
  from today): held for a design session, on Tony's word of Nov 25.
- The box's words on a no-distance day (L-553), JPL's sentence when a
  path is a prediction (L-554), orbiters in general (L-555).
- The backbone's 7-day step and its thinning.
- The row under Mars (L-534), the loops near L2, and the Mars arrival
  line on L-533's Gap.
- No orrery code. If the cause proves to be in `path_plan.py`, stop
  and say.

## Checks

- The gallery maintenance run, offline, whole: no row red that was
  green at the base; say what a red row reads, not only its colour.
- The builder's offline suite with its new count (620 at the base, by
  the coordinating session's run of Nov 24).
- As-built names, green on both pages.
- The orrery maintenance run if the skill changed.
- The coordinating session runs the suite and the new check on a
  clean checkout before Tony pushes.

## Close

- L-533: what changed, the 27 by name before and after, the planted
  cases by name, what is owed. It stays OPEN for a night on GitHub and
  Tony's phone look: ESCAPADE-Gold's box should read "as far as 10
  September 2027" and ESCAPADE-Blue's "12 September 2027".
- Where We Are by section, within its 130 lines.
- The final report in the form the doors set, with the token count.
  Commit and push are Tony's: the website, then the orrery.

Written November 2026 with Anthropic's Claude Fable 5.2.
