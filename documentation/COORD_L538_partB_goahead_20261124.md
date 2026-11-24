<!-- Doc-Kind: hand | The coordinating session's answer to the Part A report of L-538 (the orbiters' printed error): Tony's ruling of Nov 24, what changes in the proposal, and the go-ahead for Part B. -->
# Go-ahead for Part B: the orbiters' printed error (L-538)

Built on orrery 6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written November 24, 2026 by the coordinating session (Claude Fable
5.2) for the Claude Code session that wrote
`documentation/REPORT_L538_partA_20261124.md`. It amends
`documentation/COORD_L538_orbiters_brief_20261123.md`; where the two
differ, this one holds.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

The report was read whole from Tony's folder (16,780 bytes), not from
its summary. Say back that you read this file, and L-538's note of
2026-11-24 in the ledger.

## 1. The ruling

Your question was a BepiColombo file of about 470 KB or about 740 KB.
Neither. What the coordinating session read and told Tony:
- The 740 KB is today's size. The fine span starts at the arrival and
  the window moves forward over it: 140 days at 96 points a day is
  about 13,400 points, about 1.0 MB, by mid-January, and more if JPL
  extends its data past 2027-04-10. That passes your own limit of
  12,000 points about the end of December. (The session's arithmetic
  from your figures; check it.)
- Every visitor pays for it. `solarSystemPositionFiles` in
  `interactive.html` fetches every spacecraft's positions file among
  the room's rows before the room draws. The 42 files are 1,084 KB
  together at gallery 9e7bb99f.
- By April the loop is within 4,000 km of Mercury's centre. At the
  room's scale the marker sits on Mercury either way.

The session's recommendation, as put to Tony: "Juno gets the full fix
as measured. BepiColombo gets fine points only for the few days around
today, and a point a day elsewhere. On the other days its box prints a
coarser, true figure: an error no smaller than the reach of its loop
around Mercury, which the builder measures from JPL each night. The
same second test proves it. The loop itself goes in the BepiColombo
encounter you asked for this morning, loaded only by a visitor who
opens it." And: "This needs your ruling, because on Nov 19 you declined
a coarser figure as a stopgap. I think this one is different: it is
permanent and it is true. But it is a coarser figure."

Tony, November 24, 2026, 09:38: "I agree with your recommendation. Fine
points around today."

## 2. The outcomes, restated

These replace outcomes 1 to 3 of the brief. Outcomes 4 and 5 stand.
1. For a craft inside a capture, on every day the date box offers, the
   box's error is never smaller than the real miss, by BOTH tests: its
   served points held out, and JPL's own points between them. Your
   correction to the brief is taken whole.
2. A craft whose fine layer across the whole window stays small (Juno:
   636 points) is served it as you proposed, day by day.
3. A craft whose fine layer would not stay small (BepiColombo) is
   served fine points in the band around today only, and a point a day
   across the rest of the window. Outside the band its box's error is
   never smaller than a floor: the reach of its loop around its planet.
4. The floor is measured from JPL each night and served; never typed.

## 3. What is yours to propose in Part B's report, before the room is touched

The session's starting points, not rulings:
- WHICH CRAFT GETS WHICH is decided by a measured size, never by a
  name: a limit on a craft's fine points across the window, with the
  band-only shape past it. Tony ruled on BepiColombo; that the same
  rule sorts the next craft is the session's reading, as method.
  Propose the limit, and show each capture craft's size for every week
  from now to the end of its span, not today's alone.
- THE BAND. Yesterday to the day after tomorrow, as ruled Nov 23,
  refined by both tests as you measured (30 minutes today). Say whether
  a visitor who opens the room late in a served night can fall outside
  it.
- THE FLOOR. Worked from a quantity with a name: the craft's distance
  from its planet's centre, from JPL's points around that centre, over
  the loops of that day. Propose the exact form (the farthest distance,
  twice it, or what the geometry gives) and why. It is then TESTED
  against JPL's check points. A floor fitted to the points that test it
  cannot fail: the points it is worked from and the points that test it
  are different points, and the report says which is which.
- WHERE THE FLOOR ENTERS. Part A's map says the room is not touched;
  now it is. `position_at` makes the error and three places in
  `interactive.html` read it. Propose where the larger of the chord
  figure and the floor is taken, so there is one place, and map every
  reader again, the golden artifacts and the smoke suites included.
- THE BOX'S WORDS do not change: the same sentence prints fewer digits.
  If you think the box must say why, that is a question for Tony; put
  it in the report and change nothing.

## 4. Four smaller things

- THE LIMITS (12,000 points, 60 questions) were set before the day by
  day build was measured: Part A asked 557 questions stretch by
  stretch and did not run the other. Measure a night's questions and
  seconds for both craft, check points included, then set the limits
  with room to spare.
- THE CHECK POINTS' TIMES MOVE EACH NIGHT. A point every 37 minutes
  from a fixed start meets a loop at the same few places whenever the
  loop's period is a multiple of 37 minutes, and BepiColombo's passes
  through several (148, 185, 222, 259 minutes) between January and
  April. Shift the start each night by an amount worked from the date,
  so a night can be run again, and print it in the record.
- HOW FRESH JPL'S PATH IS. The served file's arrival, from the plan of
  Nov 4, is thousands of km from JPL's answer of Nov 24, and ESA
  reported the capture burn cut short. Print, for each capture craft,
  what JPL's answer says of its own path's date or version, in the
  build's record. Do not remake the plan; say whether its old events
  inside the capture mislead the room's list.
- WHAT A NIGHT COMMITS. The check points are saved and not served. Say
  whether they are committed, and measure the nightly commit's growth
  in Part C against the repository's size, as your own last thought
  asks.

NOT IN THIS BUILD, as before, and two more:
- "This mission ended" on days past the end of JPL's data for a craft
  still flying (BepiColombo past 2027-04-10, in the window from about
  2027-01-12). It goes to L-533 (ESCAPADE), every path to its last
  day, the next build. Your closing records add the line there.
- BepiColombo's loop around Mercury, drawn. It belongs to an encounter
  of its own, L-529 (guided encounters), with Mercury's features and
  its Hill sphere (Tony, Nov 24).

## 5. Go ahead

Part B may start, in this order: the measure and the proposals of
section 3 first, with no edit to the room's code, and a short report;
the builder, the validator and the widened check may be built before
that report where section 3 does not reach them (Juno's layer, the
capture function, the served block, yesterday's hours). Read
`safe-file-editing` and `ledger-and-session-records` whole before the
first edit, as your report said you would. The brief's section 4
(delivery) and section 5 (the report) stand.

Written November 2026 with Anthropic's Claude Fable 5.2.
