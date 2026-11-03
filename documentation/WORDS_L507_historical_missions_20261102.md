<!-- Doc-Kind: hand | The words for historical missions, slice 1 (L-507): Cassini and Galileo, an ended mission's text box, the dates sentence on every spacecraft, the drawer's new group; for Tony's approval before anything is written. -->
# Historical missions, slice 1: the words, for your approval

Tony Quintanilla, PE | Claude Opus 5.5 (Claude Code) | November 2, 2026

Built on orrery 15dc8e34e2ea17bd57d4af9b61d138a6fb4479ba at
https://github.com/tonylquintanilla/palomas_orrery and website
c77f87f64c0ba619326a02e7f876d94eda4767be at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, plus this
session's uncommitted edits.

From the brief `COORD_L507_gallery_historical_missions_slice1_brief_20261102.md`,
section 5. Nothing in the website below is written yet. Each item says
what a visitor reads now, what I propose, and why. The room prints a
date as "21 September 2003".

## In one look

| # | Where | Proposal |
|---|---|---|
| 1 | Every spacecraft's text box, Voyager's too | a new sentence: the path covers the mission's dates, the planets are today's |
| 2 | An ended mission's box, first line | "This mission ended on 21 September 2003. The marker is where it was that day." (as you ruled) |
| 3 | An ended mission's box, the path sentence | "solid where flown, dashed ahead" becomes "solid all the way" |
| 4 | An ended mission's box, the distance | "on its last day" added after the distance |
| 5 | The drawer | a new group row, "Historical missions", right after the twelve spacecraft |
| 6 | The i panel | Galileo's description as the orrery has it; Cassini's shortened to what NASA's page says |

## 1. The dates sentence (every spacecraft)

Now: nothing.

Proposed, after the path sentence, on every spacecraft's box (the
twelve active ones, Voyager 1 and 2 among them, and the two ended):

"Its path covers the mission's own dates, but the planets are drawn
where they are today, so a flyby bends the line where the planet was
then, not where it is now."

- Why: your ruling of Nov 2, 14:32, in nearly your own words.
- Not on the comets' boxes: the ruling names spacecraft. Say if you want
  it there too.

## 2. The ended box's opening (Galileo and Cassini)

Proposed, the box's first line under the name, verbatim as you ruled:

"This mission ended on 21 September 2003. The marker is where it was
that day." (Galileo)

"This mission ended on 15 September 2017. The marker is where it was
that day." (Cassini)

- The date's source: NASA's mission pages, read this session.
  Galileo, https://science.nasa.gov/mission/galileo/: "The mission ended
  when the spacecraft deliberately impacted Jupiter on Sept. 21, 2003."
  Cassini, https://science.nasa.gov/mission/cassini/: "Sept. 15, 2017".
- The orrery's list now carries each date as `mission_end`, with that
  source, and the path plan stops each path on that day (your ruling,
  "Yes stop at impact"). So the path's last served day IS the mission's
  end, and the box prints that day.
- The marker sits at the path's last point: the start of that day, by
  JPL's clock. For Galileo that is some hours before the impact, about
  1.3 million km from Jupiter's centre; for Cassini, some hours before
  its plunge. In the Solar System room each sits on its planet's orbit
  line, where the planet was then, not on the planet's dot, which is
  drawn where it is today. That is exactly what sentence 1 explains.

## 3. The ended path's sentence (replaces solid-and-dashed)

Now, on every spacecraft: "Its path is solid where it has already
flown, and dashed where JPL's predicted path takes it next, as far as
<day>."

Proposed, for an ended mission only:

"Its path is solid all the way, since all of it was flown, from
<first day> to <last day>."

- The active spacecraft keep today's sentence unchanged.
- The line is solid, as you ruled; whether it should look different
  from an active one is yours on the render (Mode 5).

## 4. The distance line's qualifier (ended missions)

Now, on every spacecraft: "<n> AU from the Sun (<n> km)", then "JPL's
own uncertainty for this position is not yet included."

Proposed, for an ended mission:

"<n> AU from the Sun (<n> km) on its last day", then the same note.

- The marker sits on a served point, so nothing is worked out between
  points, and the distance prints to whole kilometres, the finest the
  room ever prints (provenance-discipline 2.23).

## 4b. The source line (ended missions, the i panel)

Now, on every spacecraft: "Positions measured from the Sun's centre,
from <day> UTC to <day> UTC, as far as JPL's data runs, ..."

Proposed, for an ended mission: "... from <day> UTC to <day> UTC, to the
day the mission ended, ..."

- Why: "as far as JPL's data runs" would be false for Galileo, whose
  path now stops at the impact, nine days before JPL's data does.

## 5. The drawer's group row

Proposed: a group row "Historical missions", right after the Spacecraft
group's twelve and before Apollo asteroids, with Galileo then Cassini
in launch order. Folded shut like every group. Find words: "probe",
"mission", "ended", so typing "probe" or "mission" now finds both
groups, listed closed with their counts.

- Why the label: your words of Nov 1, 15:51, "a separate group for
  historical missions in addition to active missions."
- The Spacecraft group keeps its name.

## 6. The i panel's descriptions

Galileo, the orrery's words unchanged: "Galileo studied Jupiter and its
moons from 1995 to 2003." NASA's page: "It started orbiting Jupiter in
December 1995", and the end above.

Cassini, now in the orrery: "Cassini-Huygens studied Saturn and its
moons from 2004 to 2017." Proposed: "Cassini-Huygens studied Saturn
and its moons. The Saturn system was its home for 13 years."

- Why: NASA's Cassini page, as I could read it, does not give the 2004
  arrival in words; it says "The Saturn system was Cassini's home for
  13 years." So the sentence says what the page supports. The path
  plan will find Cassini's arrival at Saturn in JPL's positions, to the
  minute, but that is a drawing event, not a description.
- Each link becomes NASA's current mission page (above); the old
  solarsystem.nasa.gov addresses are the retired site.

## Decided by method, for your phone look (not asked)

- Colours, the orrery's own (constants_new.py, color_map): Cassini
  green. Galileo is white in the orrery; it is goldenrod here, by your
  rule of Oct 26 that a white path is gold for contrast (Voyager 1,
  ATLAS).
- The ended marker is the spacecraft's diamond-open, like every
  spacecraft's: the symbol says what the thing is, the text box says
  when. Written into orrery-coding-conventions.

Written November 2, 2026 with Anthropic's Claude Opus 5.5.
