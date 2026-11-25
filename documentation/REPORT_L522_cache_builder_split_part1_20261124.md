<!-- Doc-Kind: hand | Part 1 of L-522's split of the gallery-cache-builder skill: the plan, for the coordinating session to read before Tony's go-ahead. Communication; written once. -->
# L-522 (document caps): the cache builder's skill split, Part 1, the plan

Built on orrery eb90dff7a4a2d0872d0d21e24176238b0d642c5f at
https://github.com/tonylquintanilla/palomas_orrery and gallery
727ebf791666a515b9cf18d869ca3507daf11606 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (both
branch main). Written November 24, 2026 by the Claude Code session
(Claude Opus 5.5) through the python_work door, working from
`documentation/COORD_L522_cache_builder_split_brief_20261124.md`, read
whole.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

## The claim

The skill would go from 944 lines to 728, counted on a draft. Every
line of the eight sections' text moves to the new page; only the 1.19
version entry goes to the history file. Two sentences of L-538's text
disagree with the code, so they wait for the coordinating session.

## The base, and what was read

- The orrery folder stood at eb90dff7 (Tony's "L538 close"); GitHub
  was one commit ahead, 5f9d92f1, the orrery's own night
  (github-actions[bot], 2026-11-24 21:22 UTC), changing
  `data/nightly_run_record.json` alone. Tony, not at his machine, on
  being asked whether to go on without the pull: "If not arm proceed."
  The split touches no file that commit changed. Waiting in the folder:
  this brief (untracked, as the brief expects) and Tony's own edit to
  `documentation/WHERE_WE_ARE_11-24-26_0835_run_record.md`, the two
  pushed commits written beside its run order; neither is touched.
- The gallery folder stood at 727ebf79, equal to GitHub, clean.
- Skills read, the repository's copy: gallery-cache-builder, "Skill
  version: 1.21 | 2026-11-22", in full, with its line numbers;
  ledger-and-session-records, "Skill version: 1.24 | 2026-11-23", its
  version line and the parts on three version entries and the binding
  rule; safe-file-editing, "Skill version: 1.15 | 2026-11-22", its
  version lines.
- L-522's notes on step 2 and the carried list; `DOCUMENT_CAPS.md`
  whole; the step 2 brief for its shape; the gallery's
  `tools/check_as_built_names.py` whole and its `CLAUDE.md` paragraph
  on `INTERACTIVE_AS_BUILT.md`; the builder's L-538 code at 727ebf79
  (lines 2382 to 3070 and 4446 to 4468).
- The builder's offline suite at the base: "PASS (604 checks, 0
  failures)".
- Written in this part: the brief's note on L-522, word for word,
  before its Gap, and `ledger_index.py` ("OK: 548 L-blocks parsed, no
  consistency problems"). Nothing else in either repository; this
  report is the part's report.

## 1. The eight sections

Every line of each section's text goes to the page whole, under the
same title. The page's heading drops the tier mark ("[QUALITY]"), so
the account finds each skill heading in one place only. In the skill,
each section keeps its heading word for word, then one line naming the
page, then its rules, written new.

| Section | Old lines | Lines | To the skill | To the page | To the history |
|---|---|---|---|---|---|
| The Builder Reads the Period's Centre | 389-424 | 36 | heading | 35 | 0 |
| A Spacecraft Is Fetched by Its Plan | 425-523 | 99 | heading | 98 | 0 |
| A Lagrange Point Is Served as a Point | 524-539 | 16 | heading | 15 | 0 |
| The Clock Block and Its Witness | 540-558 | 19 | heading | 18 | 0 |
| A Small Body's Own Uncertainty Is Served | 559-601 | 43 | heading | 42 | 0 |
| Every Question Is Asked of JPL, Fresh | 602-614 | 13 | heading | 12 | 0 |
| A Body That Fails Its Test Is Held | 615-648 | 34 | heading | 33 | 0 |
| The Daily Run's Steps | 649-800 | 152 | heading | 151 | 0 |
| All eight | 389-800 | 412 | 8 | 404 | 0 |

The page's counts include each section's blank lines. Outside the
eight, the 1.19 version entry (old lines 25 to 31, 7 lines) goes to
`documentation/SKILL_HISTORIES.md`, by the three-entry rule, when 1.22
is added.

One judgement, for the coordinating session to overrule if it likes:
"WHY IT WAS CORRECTED" (old lines 597 to 600, under A Small Body's Own
Uncertainty Is Served) tells how the fixed tolerance refused 2026
ED138. It goes to the page, not the history: it is the reason for the
match rule's present numbers, and its "(next)" points at the section
that follows it there. No other paragraph of the eight only tells how
a thing used to be; the remarks inside sentences ("until 2026-10-15",
"Before, ...") move with their sentences.

## 2. The rules each section leaves in the skill

As each would stand in the skill. The bracketed old line numbers are
for this report only and are not written into the skill. Each rule
says no more than the old text it rests on; the coordinating
session's list of rules expected to stay is covered whole.

### The Builder Reads the Period's Centre (old lines 389 to 424)

```
## The Builder Reads the Period's Centre [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- The `period` block is the orrery's, copied onto each entry by
  `tools/mirror_objects.py` from its export, never by hand. [394-397]
- The served `osculating` block, its positions and its trust stay
  Sun-centred. A `drawn_orbit` is served beside them, at the SAME
  date, never in their place; no perturbation lines are drawn for it
  (Tony, 2026-10-13). [398-407]
- A set from another date is never paired: the builder raises, the
  pre-swap check aborts, and `tools/check_cache_in_step.py` asks the
  same question from the other side, with the same rule. [408-414]
- Which bodies this touches is decided by the orrery's period
  records, not here. [419-420]
```

### A Spacecraft Is Fetched by Its Plan (old lines 425 to 523)

```
## A Spacecraft Is Fetched by Its Plan [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- THE PLAN IS THE ORRERY'S ("One path rule, the orrery's."): made by
  `path_plan.py`, copied by `tools/mirror_objects.py`, never by
  hand. [428-439]
- Nothing is extended past the span. JPL's predicted part is fetched
  with the rest, and asked again whole when the plan is new, since JPL
  revises it. [446-450]
- A flyby is never thinned away: an event's window is thinned at its
  own scale and merged after the backbone's thinning. [441-446]
- An ended mission's last served point is on its span's last
  day. [455-471]
- `as_of_today` is today's point, never the path's last; none when no
  point lies within two days before today. [477-480]
- The shrink gate holds a re-fetch by a new plan out of its count, and
  names it. [481-484]
- No plan and no typed start: the object fails by name and is served
  last-good, never asked from 1970. [487-491]
- The offline suite gives a path body with no plan a stand-in plan, so
  it does not depend on a pull. [492-494, 508]
- A COMET ON AN OPEN PATH IS A PATH BODY: one test, `is_path_body`,
  asked wherever the builder asks "is this a spacecraft?". [495-499]
- A body that changes side across e = 1 is followed by the mirror,
  never by hand; a side change over fields set by hand is refused, and
  the drawer row is left for a person to check. The suite compares such
  comets with the export by name, with no count to bump. [511-522]
```

### A Lagrange Point Is Served as a Point (old lines 524 to 539)

```
## A Lagrange Point Is Served as a Point [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- A point has no mass and no orbit: no elements are fetched, only
  JPL's positions, a day apart across the window and an hour apart
  near today (Tony, 2026-11-19). [526-532]
- A point never takes part in the window, so it cannot narrow
  it. [533-534]
- JPL's answer is held to the point's own name. [535]
- A failed fetch serves the saved days, today's point nulled. [535-537]
```

### The Clock Block and Its Witness (old lines 540 to 558)

```
## The Clock Block and Its Witness [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- A served `jd` is on JPL's clock (TDB) and a visitor's minute is UTC,
  so each build serves the difference, asked of JPL and worked out by
  astropy; the build stops, by name, when the two disagree or JPL does
  not answer. [542-551]
- A witness does not share its clock with what it tests. [552-555]
```

### A Small Body's Own Uncertainty Is Served (old lines 559 to 601)

```
## A Small Body's Own Uncertainty Is Served [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Each small body is asked JPL's own uncertainty; the planets and
  Pluto keep JPL's planetary report, from the config. It is cache
  data, so it reaches a visitor only after a build. [564-572]
- AN ANSWER THAT CANNOT BE SERVED HONESTLY SERVES NOTHING, NAMED, and
  never costs the orbit. [573-579]
- JPL's answer is matched to the served point within the body's own
  3-sigma, floored and capped; the cap stays under half the closest
  pair of records measured, so one record's answer cannot stand in for
  another's. [580-591]
- A REFUSAL NAMES ITS NUMBERS, and the run record keeps the refused
  answer. [592-596]
```

### Every Question Is Asked of JPL, Fresh (old lines 602 to 614)

```
## Every Question Is Asked of JPL, Fresh [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Every astroquery call the builder makes passes
  `cache=HORIZONS_CACHE`, which is False: a saved answer handed back
  serves an old orbit under a new "retrieved" stamp. The offline suite
  holds every call to the setting; the orrery made the same
  choice. [604-613]
```

### A Body That Fails Its Test Is Held (old lines 615 to 648)

```
## A Body That Fails Its Test Is Held [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- Tony, 2026-11-11: "Hold the bad data and report, then
  continue." [617-618]
- A moon, or any body with its own span, is NOT held for a number over
  the limit: over it is likely physics, and an older orbit draws it
  worse. [623-626]
- A held body is served from its entry in the replaced cache, its hold
  copied forward while it lasts; `.prev` is never the store. It leaves
  the served window, is tested every build, and ends when it
  passes. [628-633]
- REPORTED, NOT RED: the night's commit title names each held
  body. [635-640]
- More than `HOLD_LIMIT` held is a failed build. [641]
- A fault in the maths, not the data, is held while drawn wrong; the
  title is then the only signal. [643-644]
```

### The Daily Run's Steps (old lines 649 to 800)

```
## The Daily Run's Steps [QUALITY]

What it does: `CACHE_BUILDER_AS_BUILT.md`, under this title.

- THE ORDER IS THE POINT (Tony's design, 2026-09-27): the guest book,
  the pulls from the orrery, this builder, the maintenance run. The
  pulls come BEFORE the builder, so the build reads what the orrery
  exported today. [651-664]
- The pull list has ONE home, the maintenance run's GENERATORS. Do not
  add the pulls to `daily_run.py`'s STEPS as rows of their own: that is
  a second copy of the list. [668-671]
- A PULL THAT CANNOT FETCH FAILS, AND THE DAILY RUN STOPS (Tony's
  option A, 2026-10-15): nothing is built on yesterday's export; option
  B, build on the previous pull and say so in red, was
  declined. [673-686]
- A PULL THAT DOES NOT MATCH THE PUSH IS A FAILED PULL (Tony,
  2026-10-25: "stop. confirmed."). The cure is Pull origin, orrery then
  website, then the Daily Run again; no retry, no wait. [691-709]
- EVERY RUN RECORD IS KEPT until the cause of the losses is found, then
  a deliberate limit, its number set at that time, with the builder
  naming each record it removes (Tony, 2026-10-16); on a loss, stop and
  name (2026-10-17). [714-726]
- AT NIGHT THE GATE DECIDES THE COMMIT: the same steps with no
  keyboard, the guest book skipped (Tony, 2026-10-31), and a red night
  commits nothing. A hold is not red. [743-773]
- THE MORNING DOES NOT WAIT FOR THE NIGHT (Tony, 2026-11-01): he pulls
  first, and a night that lands later comes with his next Pull
  origin. [776-789]
- Apart from the pulls and the records, a step that reports a problem
  does not stop the next. Nothing in the Daily Run commits or
  pushes. [791-793]
```

## 3. The size, counted

On a draft built by script in the session's scratch folder, from the
skill at the base: the eight sections as above, L-538's section from
the brief (44 lines) after A Body That Fails Its Test Is Held, the 1.22
entry (7 lines) in place of the 1.19 entry, the Contents list with the
new heading, the "Older entries" line naming 2026-11-24 (L-522), and a
four-line pointer to the page after the opening paragraph.

- THE SKILL: 944 lines to 728. The cap is lowered to the size at the
  close; the cross-reference edits below may move it by a line or two.
- THE PAGE: the eight sections' 404 lines and their 8 headings, its
  opening (a Doc-Kind line, a title and the brief's three sentences),
  and L-538's new section, counted when written in Part 2.
- THE HISTORY FILE: the 1.19 entry, 7 lines.

## 4. L-538's text against the code at 727ebf79

Five of its seven rules agree with the code as read. Two sentences of
THE FINER-STEP RULE do not, and by the brief they are not corrected
here:

- "the builder halves that craft's step". The code steps down a
  ladder, not by halves: a day runs 1440, 720, 360, 180, 90, 45, 15, 5,
  1 minutes (`CAPTURE_LADDER`), the band near today 60, 30, 15, 5, 1
  (`CAPTURE_BAND_LADDER`), to a floor of one minute
  (`CAPTURE_FLOOR_MIN`). From 45 down it is a third, then a fifth.
- "It covers the daily part as well as the band around today". True
  of a craft served whole (Juno): every day is made finer
  (`fine_days()` in `build_capture_layer`). For a craft served in the
  band only (BepiColombo), the days outside the band are set back to a
  point a day and are not made finer; they carry the loop's floor
  instead, which the rule above it says.

A wording that would match, offered, not ruled: "When the test finds a
step too coarse for a craft, the builder makes that craft's step
finer, down to a floor of a minute, and it comes to Tony only if the
floor still fails. For a craft served whole it covers the daily part as
well as the band around today (Tony, 2026-11-24, 08:12: "yes"); a craft
served in the band only keeps a point a day outside it, with the
loop's floor."

Checked and agreeing: who is in a capture (`capture_of` with the
window, `capture_span`, and the build's selection at lines 4451 to
4464); the shape by `CAPTURE_FINE_LIMIT`; the two tests and each
craft's own self-test (`capture_self_test` in
`tools/test_curve_error.py`); the floor as the sum (`_loop_term` in
`gallery/assembler/render_spacecraft.py`); the check points not
committed and the `--night` flag.

## 5. Cross-references in sections that stay

Each points at text that moves to the page; in Part 2 each would say
so:
- Operating mode, old lines 86 to 88: "The gate's conditions are in The
  Daily Run's Steps, below" -- the conditions are on the page.
- Operating mode, old lines 113 to 114: "(The Daily Run's Steps, the
  night form, says why)" -- the why (GitHub's schedule is best-effort)
  is on the page; the rule stays.
- The three-layer gate, old lines 874 to 875: "Its gate is the night's
  (`daily_run.py --night`, The Daily Run's Steps)" -- the gate is
  described on the page.
- Adding a new object, old lines 896 to 897: "(A Comet on an Open Path
  Is a Path Body, v1.18)" names no heading in this skill; the text is a
  paragraph of A Spacecraft Is Fetched by Its Plan, which moves. It
  would read "(A Spacecraft Is Fetched by Its Plan, on the as-built
  page, v1.18)".
Checked and left as they are: old line 378, "(A Small Body's Own
Uncertainty Is Served)", whose point (the served uncertainty reaches a
visitor only after a build) stays as a rule.

## 6. Listed, not moved or fixed

PASSAGES OUTSIDE THE EIGHT THAT PLAINLY DESCRIBE THE CODE (the brief:
listed, not moved): What it is (its list of key functions, old lines
139 to 145); The swap retries, rolls back, and leaves a record (what
the builder does, 185 to 203); The sibling report names what the
builder did not make (314 to 323); Commit with round-trip verify (857
to 860); the field note A BODY THE ORRERY HOLDS IS NOT YET HONOURED
HERE (930 to 944).

RULES THAT LOOK STALE, for Tony, not fixed:
- "Do not use `--commit` while L-216 is open" (old line 256): L-216
  (the swap's lock) is DONE since 2026-10-08 by the ledger's index.
- Layer 1's "537 checks at v1.19" (old line 864): the suite at the
  base passes 604.
- The field note on "guard/B3 WARN" says the comment "has drifted from
  line 755 to ~1099" (old line 851): it is at line 3575 of the builder
  at 727ebf79.

## Where this leaves us

Part 1 is done, and the skill and the gallery are untouched. Part 2
waits on two things: the coordinating session's word on L-538's two
sentences, and Tony's go-ahead.

Written November 2026 with Anthropic's Claude Opus 5.5.
