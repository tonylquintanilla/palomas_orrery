<!-- Doc-Kind: hand | Addendum from the coordinating session of Nov 1, 2026, afternoon (Claude Fable 5.1): the comet-pins brief written, rebased on the hold as built; the orrery's backstop line and L-484's lesson folded into the same orrery session; a rule for coordinating sessions on JPL's cached answers; section 6, the orrery session's result and the two stores a Code session cannot update; section 8, the comets' nightly ask ruled; section 9, encounters are both, in the Solar System room and in rooms of their own. Zero code. -->
# Coordination handoff addendum: November 1, 2026, afternoon

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | November 1, 2026, 14:20; section 6 added 14:55

Built on orrery 8f851c15cefb9ff0111ed1c622e47e48b5910396 and gallery
b6574a0fa374be2faf526d7c5e5b6f8988515652, both read live on Nov 1,
19:00 UTC and cloned at those commits. Companion to
`HANDOFF_coordination_20261101_morning.md` (its section 2b carries
Tony's rulings of noon, now on GitHub at 8f851c15) and to
`HANDOFF_coordination_20261031_night.md`, which stays the latest
coordination record and carries the queue. This file adds one
afternoon and one brief; the queue's order is as Tony ruled at noon.

Type: COORDINATION HANDOFF addendum (zero code). This session wrote
one brief, `COORD_L470_orrery_comet_pins_backstop_brief_20261101.md`,
which replaces section 4 of the Oct 31 brief as the next orrery
session's base and folds in the orrery's backstop line (L-485) and
L-484's lesson into gallery-cache-builder, so that one orrery session
carries all three.

## 1. What this session did

- Read HEAD on both repositories; found the morning addendum's section
  2b was not yet on GitHub (the 10:30 push was the 94-line version);
  Tony pushed it (8f851c15). Tony's live pass after his Pull origin:
  all 52 files served and byte-identical, which confirms L-461's "not
  yet pulled" cause for the 16:20 reading.
- Read `horizons_check.py` as built on Oct 31 and found that the hold
  would HOLD a comet whose apparition moved (`"pin"` is in
  HOLD_FIELDS), where Tony's ruling of Oct 31, 18:45 makes a change of
  apparition a VALUE, taken. The brief's 4.6 rebases the pinned branch
  on that: a designation branch asking DES=<d>;CAP, the apparition
  change routed into the take, the export serving the record JPL named
  (4.7). It writes one method choice for Tony to confirm or overturn
  when he reads the report: the six comets asked every night, not
  every 30 days.
- Asked JPL again for the six comets by designation with CAP. Every
  answer came back carrying JPL's own clock of Oct 31, 19:05 in its
  header, the same second as the Oct 31 fetch, whatever the address's
  parameter order; a NOFRAG form came back dated Oct 3. The
  coordinating session's fetch tool serves cached copies of JPL's
  answers. So Oct 31 stands as the latest fresh read, and the build
  session's own fetch is the fresh one (the brief, 4.2 and 4.4).
- Confirmed the protocol's rule: "One Session, One Bump" counts
  protocol versions (v3.118 bumped four skills under one version), so
  the orrery session may take horizons-orbital-mechanics to 1.14 and
  gallery-cache-builder to 1.16 under v3.120.
- Grepped the gallery at b6574a0 for the six record numbers, by
  L-484's lesson: no acceptance line and no fixture pins them (they
  occur in the mirror's copies, two tools and seven patch files), so
  no website pin moves as long as the export's served numbers do not;
  the brief makes the export diff the proof (4.7). Found six config
  `notes` on the website that will describe the orrery wrongly after
  the switch; written for the gallery session after the ruler build
  (4.10).

## 2. For the coordinating session's own rules

- AN ANSWER FROM JPL IS LIVE ONLY IF ITS HEADER SAYS SO. JPL prints its
  clock on the `JPL/HORIZONS ... <date> <time>` line. Before calling
  an answer "fetched today", read that line; a date other than today's
  is a cached copy, and the brief says so and carries the fresh date
  it has. The build session, which fetches through the orrery's own
  code, is the fresh read.
- A HOLD BUILT BEFORE A RULING CAN CONTRADICT IT QUIETLY. The hold
  sorted an apparition change under "pin", an identity, a day before
  the ruling made it a value; both were written by the same brief.
  When one brief carries a mechanism and a later ruling about what
  the mechanism sorts, the next brief re-reads the mechanism as built
  and says where the two disagree, by line.

## 3. The queue, as Tony ruled at noon (unchanged in content, renumbered)

1. **The orrery session** (`COORD_L470_orrery_comet_pins_backstop_brief_20261101.md`):
   the backstop line; the lesson into gallery-cache-builder 1.16 with
   the morning sentence; L-503 closed; the comet pins (may stop before
   them if the room runs out); horizons-orbital-mechanics 1.14 if the
   pins go; protocol v3.120. This week, short.
2. **The ruler build** (`DESIGN_axis_ticks_and_ruler_rulings_20261031.md`),
   a gallery session next weekend. ITS BRIEF IS WRITTEN (15:40, this
   session): `COORD_L505_gallery_ticks_ruler_backstop_brief_20261101.md`,
   which carries the website's backstop line (12:17 UTC), the dots on
   the axes, the ruler, the edge numbers off in the rooms, the Explorer
   kept as it is by R4's own clause, and the one pin that moves (the
   headless walk's reading of the chip). It opens L-505. The prompt:

   > Gallery repository. Please build from
   > ..\palomas_orrery_for_github\documentation\COORD_L505_gallery_ticks_ruler_backstop_brief_20261101.md:
   > the workflow's backstop line first, then the tick dots on the
   > axes, the ruler in place of the grid chip, and Plotly's edge
   > numbers off in the rooms. Read the brief, the design record it
   > names, and the morning addendum's section 2b first.
3. **The hold's website half and the website's CAP**, a short gallery
   session after the ruler build, with the six config notes (4.10).
4. The shared link. 5. L-314 live solar wind as a nightly step.
6. Earth's list (L-413), talks 3, 5 and 6. 7. A records session.
8. Compositions (L-489).

## 4. Owed

- Tony: commit this addendum and the brief with the next orrery push
  (the session's, or earlier); the orrery session this week with the
  prompt below; its report pasted to the coordinating session before
  he commits; mornings as the noon ruling has them (pull first, do not
  wait for the run; both Actions tabs; start times noted).
- The next coordinating session: read HEAD on both and Tony's run
  record; read the orrery session's report against the brief's
  sections 4.6 and 4.7 and the export diff; the ruler build's brief
  when Tony asks.

The prompt for the orrery session, through the python_work door:

> Orrery repository. Please build from
> documentation/COORD_L470_orrery_comet_pins_backstop_brief_20261101.md:
> the workflow's backstop line first, then the lesson into
> gallery-cache-builder, then L-503's close, then the comet pins if
> there is room. Read the brief, the Oct 31 brief's sections 3 and 4
> it names, and the two coordination handoffs of Nov 1 first.

## 5. Tony-action rollup (as written at 14:20; section 6 replaces it)

- (do) Commit `COORD_L470_orrery_comet_pins_backstop_brief_20261101.md`
  and `HANDOFF_coordination_20261101_afternoon.md` with the next orrery
  push. -- done, 6a434ed.
- (do) The orrery session, when you choose this week; its run order is
  in the brief's section 7. -- run the same afternoon; section 6.
- (decide) Nothing before the session. After it, one method choice in
  the brief's 4.6 to confirm or overturn when you read the report. --
  waits for the switch (section 6).

## 6. Added 14:55: the orrery session's result, and two stores a Code session cannot update

The orrery session ran at once (Claude Opus 5.5, built on 6a434ed;
pushed by Tony as 856922f8, read live). It built sections 1, 2, 3, 5
and 6 of the brief: the backstop line (both times in the workflow, 07:17
and 11:17 UTC), gallery-cache-builder 1.16 with the lesson and the
morning sentence, L-503 closed, protocol v3.120. Section 4 it tested
and did not switch: all six comets asked by designation with CAP, four
ways each, 24 live answers (JPL's clock of Nov 1, 12:07 Pacific), every
one the pin; the record is
`documentation/CHECK_L470_comet_cap_answers_20261101.md`. The switch
waits because the orrery's plotting knows a periodic comet by its
record number in four places the brief's 4.5 did not name:
`palomas_orrery.py` `_is_comet` (line 1699, a numeric id of 90,000,000
or more) and the three comet-tail tests (lines 2618, 6386, 7730,
`id_type in ['smallbody', 'id']`); asked as "2P", the six would lose
their tails and their perihelion orbits with no error. Two more facts
from the test for the switch's brief: JPL now refuses an unencoded
semicolon with HTTP 400 (on Oct 31 it returned the whole list), and
astroquery adds CAP only through the query methods' own
`closest_apparition=True`, so a shared helper has to own the query
call; the COMMAND it writes is read on both machines (Tony's 0.4.9,
GitHub's newest). The 4.6 cadence question waits for that session.

TWO STORES A CODE SESSION CANNOT UPDATE, found by Tony at 14:49: the
Project's instructions on claude.ai still read v3.118, and the
account's installed gallery-cache-builder is behind the repo's 1.16
(1.15, the Oct 31 bump, may never have been installed either). A Code
session writes the protocol and the skills in the repo and can reach
neither the Project page nor Settings > Skills, so after every Code
session that bumps the protocol or a skill, two steps are Tony's: paste
the repo's PROJECT_INSTRUCTIONS.md into the Project's instructions,
and reinstall each bumped skill from skills/<name>/SKILL.md. Until
then every chat session in the Project reads a manifest whose rows are
behind the skills, and the Stale Skill = Stop gate fires. Both take
effect in new conversations only. THE RULE, for ledger-and-session-
records' next version and for every Code session's report: a report
that bumps the protocol or a skill ends with those two steps named in
its Tony-action rollup, by version. The coordinating session repeats
them in its own rollup until Tony says they are done.

For the coordinating session's own rules, a third line beside section
2's: A BRIEF'S READER LIST IS FOUND BY BEHAVIOUR, NOT BY ONE PATTERN.
The brief's 4.5 listed the sites that match `^9\d{7}$` and missed the
four that test the same fact another way (`int(id) >= 90000000`,
`id_type in [...]`). The grep for "who treats this as a comet" is a
grep for every test of comet-ness, by whatever means, and the brief
names them all or says it did not look.

A fourth line for the coordinating session's own rules, learned
placing this file: A FILE PLACED TWICE FROM THE SAME STAGING PATH
ARRIVES AS ITS FIRST COPY. The section-6 version of this handoff was
sent at 14:52 and the folder received the 14:20 version again, with a
new time stamp; placed from a fresh path at 15:51 it arrived whole.
After every placement the file's size is read back from the folder
listing, and a changed file goes from a path not used before.

## 8. Added 15:25: the cadence ruled (L-470)

Tony, Nov 1, 15:21 Chicago, from his phone, after the two choices
were put to him (every night: six queries, the served record never
more than a night old; every 30 days: one cadence for everything, up
to a month on the previous apparition's record after perihelion, and
up to a month asking a reassigned number if JPL ever reuses one):
"As we add more comets a conflict may arise. So daily is approved."
RULED: a comet asked by designation with CAP is asked EVERY NIGHT, as
a held body is, so the record number the export serves the website is
never more than a night old. The comet-switch brief carries this as
the rule, not as the reading the comet-pins brief's 4.6 left open; the
one decision that brief deferred is closed. His reason is the record's:
the cost of the nightly ask is six queries today, and it stays small as
the list grows, while a month's window on a reassigned number grows
with every comet added.

## 9. Added 15:45: encounters are both (L-489, compositions; with L-433, the rooms)

The road's item 12 opened with Tony's own question of Oct 27: do
encounters come on their own, or as scenes? Put to him from his phone
on Nov 1, 15:41, with the two shapes (the Solar System room already
shows a flyby on its own, since a ticked spacecraft brings its
companion planets; a scene is a named, authored view with an
interpretation and its own address). His ruling, in his words:
"Encounters whether perihelion events, near earth asteroids, or
spacecraft flybys, are both: visualized in the solar system view as
today and in addition not as a replacement, in rooms we create for
those bodies with the center body changed to the object that is being
encountered. Other features may apply like comet features, body
shells, and better info."
RULED, read as three things:
- The Solar System room keeps showing encounters as it does today (a
  spacecraft with its companion planets; a comet on its path; a
  near-Earth asteroid on its orbit). Nothing there is replaced.
- An encounter also gets a ROOM OF ITS OWN, centred on the body being
  encountered: a flyby's room is centred on the planet flown past, a
  perihelion's on the Sun, a near-Earth asteroid's on Earth. These are
  the rooms of item 13 (the planets' rooms from the template, L-433)
  and the Earth and Sun rooms that exist, used as hosts; the centre
  body is the room's.
- In that room the encounter may carry what the Solar System room
  cannot: the host body's shells, a comet's features (its tail, its
  coma), and fuller words, sourced under the provenance rules (C3 on
  L-489: a spacecraft is a story, cited to the agency's page).
Three kinds of encounter are named, and the rule covers all three:
a perihelion, a near-Earth asteroid's pass, a spacecraft's flyby.
What this does to the design: a composition (L-489) is the way an
encounter is authored in a room, so compositions and the planets'
rooms are one line of work, not two, and the first composition can be
an encounter in a room that already exists (Earth's, for a near-Earth
pass, or the Sun's, for a perihelion). The compositions talk starts
from here. ADDED 15:50, Tony, 15:45: "I would identify the Artemis II
mission as the first encounter to draw. It belongs in the earth slice.
It already has a build in the orrery. The moon is already drawn."
RULED: the first encounter is Artemis II, in the Earth room (Earth the
centre, the Moon already drawn there, L-413's slice). Read at gallery
b6574a0 by the coordinating session: the orrery built the mission in
April 2026 (the gallery's artemis_ii_* plot files are its exports),
but the website's served cache does not yet carry an Artemis II path
(the 26 served paths, read from the night's log, run from the
Voyagers to the comets with no Artemis among them), so that build
starts where every spacecraft's did, with the entry carried from the
orrery's list into the served data, then the room. Its brief is a
coordinating session's, after the ruler build and the comet switch
unless Tony asks sooner; it opens L-489's first build.
ADDED 15:55, Tony, 15:51, on reading why Artemis II is not served
(no key, by the Oct 1 rule; and JPL's data for it covers only April 2
to 10, 2026, so at today's date it has no position to draw): "this
actually suggests a separate group for historical missions in addition
to active missions with special windows." DIRECTION, details to be
ruled at the talk: a HISTORICAL MISSIONS group beside the active
spacecraft, its members served with their own windows (the mission's
dates) and drawn at a date inside those, not at today's. What it
touches: the cache's one served window (88 days either side of today,
set by the shortest trusted span) and the resolver's gating of a body
by that window (gallery-assembler, M2), both of which today assume one
date for every body; the Solar System drawer, which lists one JPL
class to a row and would gain the group's row; and goal 15 (a date to
choose), whose machinery this is. The design question the talk opens
with: when a visitor ticks a historical mission in the Solar System
room, does the room's date move into the mission's window, or does the
row say the mission is shown in its own room? Artemis II's room is the
first instance either way.

## 7. Tony-action rollup (current, replacing section 5's)

- (do) Paste the repo's `PROJECT_INSTRUCTIONS.md` (v3.120, at 856922f8)
  into the Orrery Project's instructions on claude.ai.
- (do) Reinstall gallery-cache-builder (1.16) in Settings > Skills from
  `skills/gallery-cache-builder/SKILL.md`.
- (do) Commit this file and
  `COORD_L505_gallery_ticks_ruler_backstop_brief_20261101.md` with the
  next orrery push.
- (do) The ruler build next weekend, with the prompt in section 3.
- (do) Mornings this week: Pull origin on both first, without waiting
  for the run; both Actions tabs; start times noted.
- (decide) Nothing. The 4.6 cadence is ruled (section 8): every night.

Written November 1, 2026 with Anthropic's Claude Fable 5.1.
