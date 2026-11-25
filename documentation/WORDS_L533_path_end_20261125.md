<!-- Doc-Kind: hand | The words for a craft still flying when the day shown is past the end of JPL's published path, in place of a false "This mission ended on": four sentences, approved by Tony on 2026-11-25, for a later small build under L-533 (ESCAPADE). Communication; written once. -->
# A craft past the end of JPL's path: the box's words, approved (November 25, 2026)

Tony Quintanilla, PE | Claude Fable 5.2, the coordinating session | November 25, 2026

Built on orrery 7b128d8fa83a302fedc2a019bc0c4ded97901b73 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b2d9eaa66ed33ec93fc2bbcbdc5b85d5b872e043 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main), read 2026-11-25, 09:40 Chicago.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: WORDS, APPROVED (zero code). Nothing is built. For a later small
build on the website's page, under L-533 (ESCAPADE).

## The fault

The Solar System room's box says "This mission ended on ..." whenever
the moment shown is after a path's last served point
(`gallery/assembler/render_spacecraft.py`: `ended = at is None and
epoch_jd > rows[-1][0]`). Nothing asks whether the mission ended. For a
craft still flying it is false. Found by L-538's Part A report, section
5; confirmed in L-533's Part 1 report, section 5
(`documentation/REPORT_L533_last_day_plan_20261125.md`).

## When a visitor meets it

- THE ORDINARY CASE: the day real time passes the end of the path JPL
  has published, before JPL publishes more or before the site picks it
  up (a plan is made again every 30 days). A room opened normally then
  says it to every visitor. First possible: 11 April 2027, BepiColombo,
  whose published path stops on 10 April 2027.
- A date typed into a room's address reaches the same sentence sooner,
  from about 12 January 2027. That use is not supported (Tony, L-556 (a
  date to choose in the rooms)); the words are not written for it.
- So the build is wanted before 10 April 2027.

## The four sentences

For a craft whose entry has no `mission_end` and whose path's last
point is before the moment shown. BepiColombo's days as the example.

1. The opening.
   Today: "This mission ended on 10 April 2027. The marker is where it
   was that day."
   APPROVED: "JPL's published path for this craft stops on 10 April
   2027. The marker is where that path ends."
2. After the distance figure.
   Today: " on its last day"
   APPROVED: " on the last day of JPL's path"
3. The sentence about the line.
   Today: "Its path is solid all the way, since all of it was flown,
   from 21 October 2018 to 10 April 2027."
   APPROVED: "Its path is solid all the way, since the day shown is
   past the end of JPL's path, from 21 October 2018 to 10 April 2027."
4. The end of the source line.
   Today: ", to the day the mission ended"
   APPROVED: ", as far as JPL's data runs" (the box's own phrase for a
   craft still flying).

The words say only what the data supports. They do not say the mission
continues: nothing in the data says so, only that no end is recorded.
An ended mission's box (a `mission_end` on its entry) keeps its words.

## Tony's words

09:47, on the open item: "can you ask me specifically what words are
needed". 09:54, on who would see it: "I'm unclear. Are we writing for
an unsupported use case? What do you recommend?" 09:57, to the four
sentences above as the coordinating session recommended them:
"Approved".

Numbers 2 and 4 are the Code session's proposal as written; 1 and 3
are the coordinating session's rewording of it. Where JPL's sheet says
when a path turns to prediction, L-554 (JPL's sentence when a path is
a prediction) may add its sentence; that item's, not this one's.

Written November 2026 with Anthropic's Claude Fable 5.2.
