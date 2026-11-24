<!-- Doc-Kind: hand | Design record, for a talk: how a craft orbiting a planet is served in general, so that many orbiters and stays of years do not burden the page, the repository or JPL. A proposal with its measurements; the rulings it cites are L-538's. -->
# Design record: orbiters in general

Built on orrery 6a42ab3bc703bac58ad80d9b738c3cd546803d47 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 9e7bb99ffb77799759abe5a3e6d6dc556853da8e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
L-538's build read from Tony's working copies, not pushed.
Type: DESIGN (zero code). Written November 24, 2026 by the
coordinating session (Claude Fable 5.2), for the next talk with Tony.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

## Why

Tony, November 24, 2026, 13:53, on L-538's build: "we don't want to
overly burden serving this path. there are many missions with orbits
lasting years and a similar problem. we should define an architecture
that will work generally." At 14:00, to the session's recommendation
(check points out of the repository, L-538 ships as built, the general
design into a design record for the next talk): "i agree with the
recommendation".

## What L-538 measured (two craft, Juno and BepiColombo)

From the Claude Code session's reports of Nov 24 (Parts A, B and C),
read whole; its figures, not re-measured here.

SERVED, what every visitor to the Solar System room downloads:
- Juno's file 22 KB to about 46 KB (290 points to 758).
- BepiColombo's 115 KB to about 130 KB (1,518 points to 1,674 and a
  reach for 89 days; the 130 is the session's arithmetic).
- All 42 spacecraft files 1,084 KB to about 1,125 KB. The page fetches
  every one before the room draws (`solarSystemPositionFiles`).
- Not built: BepiColombo with fine points across the whole date window,
  17,650 points, about 1.36 MB by mid-January.

STORED, what a night commits and no visitor downloads:
- These two craft, compressed: about 200 KB a night before, 312 KB
  with the build; 64 KB of that the saved check points, which change
  whole each night. 23 to 41 MB a year on a repository of 84 MB.
- Ruled out of the repository on Nov 24: the check points (23 MB a
  year of it).

ASKED OF JPL each night: Juno 33 questions, 14 s; BepiColombo 10, 14 s.

So each orbiter costs in three ways, and the cost grows with the
number of orbiters, not with what a visitor opens.

## What is ruled already (L-538, the orbiters' printed error)

- No stopgap; the error is worked out from served points (Nov 19).
- A craft in a capture: a point a day across the date window, an hour
  apart around today, finer where the check finds that too coarse
  (Nov 23).
- Where that would not stay small: fine points around today, a point a
  day elsewhere, and outside the band a figure never smaller than the
  reach of the loop (Nov 24, morning). Which craft gets which is
  decided by a measured size, never a name (the session's reading, as
  method).

## The proposal: five parts

Nothing below is ruled. Each part says what was checked.

1. IN THE SUN'S ROOM AN ORBITER IS AT ITS PLANET. A point a day and
   the loop's reach, which L-538 built: about 15 KB a craft (the
   session's arithmetic), the same however tight the loop and however
   many years the stay. Fine points around today are then a choice made
   within a budget, with a third shape below the two built: a point a
   day and the reach, no band at all.
2. THE LOOP LIVES IN THE PLANET'S OWN VIEW, loaded when a visitor opens
   it. This is the split Tony agreed on Nov 20: encounters as moments,
   and a path drawn around the body for stays.
3. A STEADY ORBIT IS SERVED AS AN ORBIT, NOT AS POINTS. Checked at
   gallery 9e7bb99f: the six moons served carry a parent, osculating
   elements about a stored centre, and a measured trust
   (`two_body_rate_v1`; the Moon's holds 3.4 days, Titan's 2.0, Io's
   0.2). An orbiter in a steady orbit could be served the same way, a
   few numbers a day. NOT CHECKED: that elements hold for a spacecraft
   at all. A craft fires its engine and a moon does not; Juno's close
   passes bend its orbit fast. Measure the trust on Juno and
   BepiColombo before anything is designed on it.
4. AN IRREGULAR STRETCH (an arrival, a flyby, a burn) IS A PACKAGE OF
   POINTS, built once when it is complete and never rebuilt, as L-529
   (guided encounters) does. An ended mission's whole stay is the same:
   built once, so it adds nothing to a night. Its path is thinned in
   the frame where its shape lives: today's thinning is 0.02 AU about
   the Sun, which erased Juno's loop around Jupiter.
5. BUDGETS, BY MEASURED SIZE AND NEVER BY NAME, printed each night for
   the three costs: bytes served, for a craft and for a room; bytes a
   night commits; questions to JPL. And the page fetches a craft's
   file when its row is opened, where today it fetches all of them
   before it draws.

## For the talk

- Which view holds the loop: an encounter's row, the planet's room, or
  both.
- The first test: BepiColombo's arrival at Mercury (Tony, Nov 24,
  L-529). The session's recommendation, not ruled: it waits until
  JPL's path is fitted past the arrival. JPL's header on Nov 24 reads
  "Data fit through 2026-Nov-17, prediction thereafter", and ESA
  reported the capture burn cut short.
- Mercury's features are not served to the website; the Hill sphere at
  least comes first (L-529's note of Nov 24).
- Whether a spacecraft's box carries JPL's own sentence when its path
  is a prediction: asked of Tony on Nov 24, not answered.
- The numbers for the budgets.
- Stays of years by craft still flying (Juno to 2028 in JPL's data):
  how much of the stay is drawn, and how a night adds to it without
  rebuilding it.
- The order, against the road on Where We Are.

Written November 2026 with Anthropic's Claude Fable 5.2.
