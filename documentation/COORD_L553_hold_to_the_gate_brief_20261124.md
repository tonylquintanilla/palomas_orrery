<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-553 (a held body turns the night red). Tony's rule "Hold the bad data and report, then continue" carried from the builder to the night's gate, for every kind of body, with planted cases. Communication; written once, read by its session. -->
# Brief: one body JPL does not answer no longer stops the night (L-553)

Built on orrery 6e24640261ebb8cb23cf1f113e7df88c7bef2d19 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery d976d3dba8f04fdb80056ff0b46b7171c4074ada at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-24, 20:00 Chicago; Tony's two folders
stood at the same commits, his orrery folder with this session's
records waiting). Nightly bot commits since are expected. This brief
is in Tony's next orrery push.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session through the python_work door. The
code is the gallery's: the builder, the checks, the offline suite, and
`CACHE_BUILDER_AS_BUILT.md` in the same commit. The orrery gets the
records and one rule in gallery-cache-builder. Written November 24,
2026 with Anthropic's Claude Fable 5.2, the coordinating session.
Method table: a Code session, Opus (METHOD_MODEL_EFFORT.md, a build).

Tony's words, Nov 24, in this coordinating session, on L-553 in full:
20:00, "wait, i thought that our rule was that if one body fails, we
continue and report not turn the whole night red, in effect."
20:11, to the offer of a hand-started night, "You or I can press it,
but shouldn't we fix the issue first".
So this build is next, ahead of L-533 (ESCAPADE)'s.

## What this is, in one paragraph

Tony's rule of 2026-11-11 is "Hold the bad data and report, then
continue." The builder follows it for most bodies. The night does
not: a check after the build can still turn the whole night red for
one body JPL did not answer, and a red night commits nothing. On
2026-11-24 the website's run #58 lost a night that way, the first
night of L-538 (the orbiters' printed error): one request for Deimos
timed out, everything else passed, and nothing was committed. This
build carries the rule to the night's gate, for every kind of body.

## Start

1. The orrery's CLAUDE.md from its first step, then the gallery's.
   Both bases recorded; edits waiting in either folder: say so and
   stop.
2. L-553, whole, with its three notes of Nov 24. L-525 (hold the bad
   data), its rulings. L-538's finding re-homed to L-553.
3. Skills: gallery-cache-builder 1.22, whole (728 lines), and on the
   page `CACHE_BUILDER_AS_BUILT.md` the sections A Body That Fails Its
   Test Is Held and A Capture Craft's Box Never Claims Less Than Its
   Miss; agentic-pre-test; safe-file-editing.
4. The code named under "The three paths" below, read where it runs.

## The outcome

On a night when JPL does not answer one or more questions, for a body
of any kind:
- the build holds or leaves out that body by the rules it already has,
  and goes on;
- no check after the build is red BECAUSE a body is held;
- the night is green and commits;
- each hold is reported by name where holds are reported today: the
  build's warnings, the run record, the night's commit title.
The limits stay. More than `HOLD_LIMIT` held in one build is still a
failed build. A body with something missing and NO hold named in its
served entry is still red: a check accepts a held body by the hold
its entry names, never by what happens to be missing, and it prints
each held body it accepted, by name, with the count.

## The three paths known today

Each is closed, with a planted case that is red before and green
after. These were read by the coordinating session at 727ebf79; the
line numbers are a start, not a promise.

A. A BODY NOT HELD BY ITS TEST WHOSE TEST COULD NOT BE MADE (run #58,
   Deimos). `measure_trust` catches the failed request and returns a
   null window ("trust measurement failed ...; served null window",
   near line 1044 of `tools/gallery_cache_builder.py`). For a body
   `held_by_test` covers, `trust_verdict` says 'untested' and it is
   held. For any other body, a moon among them, nothing holds it: it
   is served with no measured error, and the Solar System figures row
   (`documentation/smoke_solar_system_figures.js`) says "deimos's box
   cannot be built: ... no measured error is served for it".
B. A BODY HELD AS UNANSWERED, SERVED WITH NO as_of_today (Chariklo,
   L-538's Part C). `hold_from_prior` builds the entry with
   `as_of_today: None`; the same row refuses "no as_of_today or
   trust".
C. A CAPTURE CRAFT SERVED LAST-GOOD. Its night writes no check points,
   so the Curve error row (`tools/test_curve_error.py`, with --night)
   is red by name. And with no saved layer, the pre-swap check #O
   aborts the whole build for one craft.

Then look for a fourth. By grep and by reading the night pass's
gating rows, list every other place a body the build held, or served
last-good, or could not test, can turn a row red. Name each in the
report, fixed or not.

## The job, in two parts

**Part 1: the plan, before any edit.** One report, then stop.
- For each path: which side changes, the builder or the check, and
  why. The coordinating session's expectation, for you to confirm or
  correct from the code: in A the body is held at its last good build
  like any body JPL did not answer, since "a moon is not held" is for
  a number over the limit, not for a test that could not be made; in
  B and C the check accepts the held body by its named hold.
- What a visitor sees for each held body, in its box, before and
  after. If any choice changes what a visitor reads, say so plainly:
  that one goes to Tony.
- #O's abort for a capture craft with no saved layer: what could be
  served instead that never claims less error than its miss, and what
  it costs. Propose; do not build it without the go-ahead.
- One fact, not a build: does a request to JPL that times out get
  tried again today, anywhere in the builder? Run #58's was a single
  connect timeout of 30 seconds. Say what a second try would cost.
- The planted cases you will add, by name, and where each runs.

**Part 2: the build, on the go-ahead.**
- The changes of the plan as accepted.
- THE PLANTED NIGHT. The rule's proof is not a lucky night. On a
  throwaway copy, with JPL made to fail for one moon's accuracy test,
  one Sun-centred body's fetch and one capture craft's questions, the
  night's own pass is green, would commit, and names all three. Then
  the same with one more held than `HOLD_LIMIT`: red, as today. These
  cases join the offline suite or a gating row, so they run every
  night, not only now. Tony asked "can we run the nightly by hand and
  test it?"; this is the test that can fail.
- `CACHE_BUILDER_AS_BUILT.md` in the same commit, the sections that
  changed, replaced not appended.
- gallery-cache-builder's rule: its text comes with the go-ahead,
  written after your plan and from it. The skill is at its cap of
  728; the report says which lines leave to make room, and where to.
- agentic-pre-test, whole, on a throwaway copy before the report.

## Out of scope

- L-533 (ESCAPADE)'s build, every path to its last day.
- The hold's leftovers on Where We Are (Earth's own box, a close pass
  held on its older orbit, L-526).
- Any change to what a body's box reads when nothing is held.
- A retry, unless the go-ahead asks for it.
- No other skill. No orrery code.

## Checks

- The gallery maintenance run, offline, whole: no row red that was
  green at the base. Curve error is red at the base in Tony's folder
  until a night commits the fine layer; say what it reads, not only
  its colour.
- The builder's offline suite, with its new count.
- As-built names, green on both pages.
- The orrery maintenance run if the skill changed: `skills_index.py
  --check`, `doc_index.py --caps`.

## Close

- L-553: what changed on each path, the planted cases by name, what
  was found beyond the three, what is owed. It stays OPEN for a night
  on GitHub read by the coordinating session after Tony's push.
- L-538: its Gap unchanged, Tony's look after a green night.
- Where We Are by section, within its 130 lines.
- The final report in the form the doors set. Commit and push are
  Tony's: the website, then the orrery.

Written November 2026 with Anthropic's Claude Fable 5.2.
